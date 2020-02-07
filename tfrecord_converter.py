import tensorflow as tf
import json
import os
from object_detection.utils import dataset_util

def create_tf_example(ann_json, img_subdir, img_filename):

    with open(ann_json) as f:
        data = json.load(f)

    img_path = os.path.join(img_subdir, img_filename)
    with tf.gfile.GFile(img_path, 'rb') as fid:
        encoded_png = fid.read()

    height = data['size'].get('height') # Image height
    width = data['size'].get('width') # Image width
    filename = img_filename # Filename of the image. Empty if image is not from file
    encoded_image_data = encoded_png # Encoded image bytes
    image_format = b'png' # b'jpeg' or b'png'

    xmins = [] # List of normalized left x coordinates in bounding box (1 per box)
    xmaxs = [] # List of normalized right x coordinates in bounding box
             # (1 per box)
    ymins = [] # List of normalized top y coordinates in bounding box (1 per box)
    ymaxs = [] # List of normalized bottom y coordinates in bounding box
             # (1 per box)
    classes_text = [] # List of string class name of bounding box (1 per box)
    classes = [] # List of integer class id of bounding box (1 per box)

    for i in range(len(data['objects'])):
        dim = data['objects'][i].get('points').get('exterior')
        xmins.append(dim[0][0]/width)
        xmaxs.append(dim[1][0]/width)
        ymins.append(dim[0][1]/height)
        ymaxs.append(dim[1][1]/height)
        classes_text.append(['power_cell'])
        classes.append(0)

    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_image_data),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
        }))

    return tf_example

#writer = tf.python_io.TFRecordWriter()
# TODO(user): Write code to read in your dataset to examples variable
# TODO: make image folder called 'images' and annotations folder called 'ann' to replace 'data' folder
# TODO: follow this link https://github.com/tensorflow/models/blob/master/research/delf/INSTALL_INSTRUCTIONS.md

for file in os.listdir(os.fsencode('images/')):
    img_filename = os.fsdecode(file)
    ann_path = 'ann/' + img_filename.replace('png', 'json')
    tf_example = create_tf_example(ann_path, 'images', img_filename)
  #writer.write(tf_example.SerializeToString())

#writer.close()
