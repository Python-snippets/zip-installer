import requests
import subprocess


print('''


███████╗██╗██████╗░  ██╗███╗░░██╗░██████╗████████╗░█████╗░██╗░░░░░██╗░░░░░███████╗██████╗░
╚════██║██║██╔══██╗  ██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██║░░░░░██║░░░░░██╔════╝██╔══██╗
░░███╔═╝██║██████╔╝  ██║██╔██╗██║╚█████╗░░░░██║░░░███████║██║░░░░░██║░░░░░█████╗░░██████╔╝
██╔══╝░░██║██╔═══╝░  ██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██║░░░░░██║░░░░░██╔══╝░░██╔══██╗
███████╗██║██║░░░░░  ██║██║░╚███║██████╔╝░░░██║░░░██║░░██║███████╗███████╗███████╗██║░░██║
╚══════╝╚═╝╚═╝░░░░░  ╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝

                                                                                 \n''')


def getDeviceCodename():
    result = subprocess.run(['adb', 'shell', 'getprop', 'ro.product.vendor.device'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    return result.strip()

print('Device:',getDeviceCodename())

print(" ")

def downloadzip():
    print('Beginning file download .......')
    url = 'https://leech.royalturd.workers.dev/Uploads/twrp-installer-3.5.2_9-0-laurel_sprout.zip'
    r = requests.get(url)
    with open("twrp.zip", "wb") as code:
        code.write(r.content)

def LocalZIPInstall():
    print('Device connected:',getDeviceCodename())
    x = input('Are you sure to continue? (Y/N)')
    if x.capitalize() == 'Y':
        print('Running zip installation, do not unplug your device or power it off.')
        result = subprocess.run(['adb', 'reboot', 'recovery'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        print(result)
        input('Once you see device rebooting to recovery go to Apply update from ADB, press enter.')
        result = subprocess.run(['adb', 'sideload', 'twrp.zip'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        print(result)
        print('zip successfully sideloaded.')


def reboot():
    print('Booting to system...')
    result = subprocess.run(['adb', 'reboot'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    print('Booting...')

downloadzip()
LocalZIPInstall()
reboot()



 
