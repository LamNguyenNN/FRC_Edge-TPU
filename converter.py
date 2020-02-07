import json
import os

def convert(json_file=''):
  with open(json_file) as f:
    data = json.load(f)

  dx = 1/data['size'].get('width')
  dy = 1/data['size'].get('height')

  cells_list = []

  for i in range(len(data['objects'])):
    dim = data['objects'][i].get('points').get('exterior')
    x = (dim[0][0] + dim[1][0]) * .5 * dx
    y = (dim[0][1] + dim[1][1]) * .5 * dy
    w = (dim[1][0] - dim[0][0]) * dx
    h = (dim[1][1] - dim[0][1]) * dy

    cells_list.append((0,x,y,w,h))

  return cells_list

directory_in_str = 'Valid_Images/ann'
directory = os.fsencode(directory_in_str)

for file in os.listdir(directory):
  filename = os.fsdecode(file)

  if filename.endswith('.json') or filename.endswith('json'):
    dir = directory_in_str + '/' + filename
    power_cells = convert(dir)

    with open('Valid_Images/annotations/' + filename.replace('.json', '.txt'), 'w') as f:
      if len(power_cells) > 0:
        f.write('\n'.join('%s %s %s %s %s' % x for x in power_cells))
      else:
        f.write('')
