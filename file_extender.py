import os
import json
import shutil

'''
path = 'Valid_Images/Filming Day 1 Video/ann'
for file in os.listdir(os.fsencode(path)):
  filename = os.fsdecode(file)
  new_name = filename.replace('.png.json', '.json')
  os.rename(path + '/' + filename, path + '/' + new_name)

path ='Valid_Images/(Done) Filming Day 2 Video/ann'
for file in os.listdir(os.fsencode(path)):
  filename = os.fsdecode(file)
  new_name = filename.replace('.png.json', '_1.json')
  os.rename(path + '/' + filename, path + '/' + new_name)
'''
path = 'Valid_Images/Filming Day 1 Video/img'
for file in os.listdir(os.fsencode(path)):
  filename = os.fsdecode(file)
  with open('Valid_Images/train.txt', 'a') as f:
      f.write('D:\\ProgramFiles\\Darknet\\darknet\\build\\darknet\\x64\\data\\obj\\' + filename + '\n')

path ='Valid_Images/(Done) Filming Day 2 Video/img'
for file in os.listdir(os.fsencode(path)):
  filename = os.fsdecode(file)
  #new_name = filename.replace('.png', '_1.png')
  #os.rename(path + '/' + filename, path + '/' + new_name)
  with open('Valid_Images/train.txt', 'a') as f:
      f.write('D:\\ProgramFiles\\Darknet\\darknet\\build\\darknet\\x64\\data\\obj\\' + filename + '\n')

'''
path = 'Valid_Images/ann'
dir = os.fsencode(path)

for file in os.listdir(dir):
    filename = os.fsdecode(file)
    with open(path + '/' + filename) as f:
        data = json.load(f)
        if data['tags'][1].get('name') == 'val':
            shutil.move('Valid_images-detection/annotations/' + filename.replace('json', 'txt'), 'Valid_Images-detection/test/' + filename.replace('json', 'txt'))
            shutil.move('Valid_images-detection/img/' + filename.replace('json','png'), 'Valid_images-detection/test/' + filename.replace('json','png'))
        elif data['tags'][1].get('name') == 'train':
            shutil.move('Valid_images-detection/annotations/' + filename.replace('json', 'txt'), 'Valid_Images-detection/train/' + filename.replace('json', 'txt'))
            shutil.move('Valid_images-detection/img/' + filename.replace('json','png'), 'Valid_images-detection/train/' + filename.replace('json','png'))

path = 'Valid_Images-detection/train'
for file in os.listdir(os.fsencode(path)):
  filename = os.fsdecode(file)
  with open('Valid_Images-detection/train.txt', 'a') as f:
      if 'png' in filename:
          f.write('D:\\ProgramFiles\\Darknet\\darknet\\build\\darknet\\x64\\data\\obj\\' + filename + '\n')
      else:
          continue

path = 'Valid_Images-detection/test'
for file in os.listdir(os.fsencode(path)):
  filename = os.fsdecode(file)
  with open('Valid_Images-detection/test.txt', 'a') as f:
      if 'png' in filename:
          f.write('D:\\ProgramFiles\\Darknet\\darknet\\build\\darknet\\x64\\data\\obj\\' + filename + '\n')
      else:
          continue

'''
