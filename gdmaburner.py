import os
from os import path

print(' ---- YOUR PENDRIVE MUST BE FORMATTED ----')
print(' ')
print('Specify the path of your .iso file:')
print(' ')
pathisoinput = str(input('-> '))
parameter_iso = bool(path.exists(pathisoinput))

if parameter_iso == True:
    print(' ')
    print('Directory found, proceeding.')
    print(' ')
    print('These are your disks and removable devices: ')
    print(' ')
    os.system('lsblk')
    print(' ')
    print('Specify your pendrive:')
    print(' ')
    pathpendriveinput = str(input('-> '))
    pathpendrivecompleto = ('/dev/{}'.format(pathpendriveinput))
    parameter_pendrive = bool(path.exists(pathpendrivecompleto))
    
    if parameter_pendrive == True:
        print(' ')
        print('Burning...')
        print(' ')
        os.system('sudo dd if={} of={} bs=4M'.format(pathisoinput, pathpendrivecompleto))
    else:
        print(' ')
        print('Pendrive not found.')

else:
    print(' ')
    print('Diretory not found.')