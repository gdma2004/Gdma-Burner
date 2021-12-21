import os
from os import path

tamanho = os.get_terminal_size().columns

print(' YOUR PENDRIVE WILL BE FORMATTED AND ALL DATA WILL BE LOST '.center(tamanho, '!'))

tree = str(input('\nShow your home files? (y/n)\n-> '))

if tree == 'y':
    os.system('tree ~/')
else:
    pass

pathisoinput = str(input('\nSpecify the path of your .iso file:\n-> '))
parameter_iso = bool(path.exists(pathisoinput))

if parameter_iso == True:
    print('\nDirectory found, proceeding.\n\nThese are your disks and removable devices:\n')

    os.system('lsblk')
    pathpendriveinput = str(input('\nSpecify your pendrive:\n-> '))
    pathpendrivecompleto = ('/dev/{}'.format(pathpendriveinput))
    parameter_pendrive = bool(path.exists(pathpendrivecompleto))
    
    if parameter_pendrive == True:
        os.system('sudo umount {}'.format(pathpendrivecompleto))
        os.system('sudo mkfs.ext4 {}'.format(pathpendrivecompleto))
        print('\nBurning...\n')
        os.system('sudo dd if={} of={} bs=4M'.format(pathisoinput, pathpendrivecompleto))
    else:
        print('\nPendrive not found.')

else:
    print('\nDiretory not found.')
