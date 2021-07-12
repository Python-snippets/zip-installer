import requests
import sys
import subprocess

def splash():


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

print(' ')
def downloadtwrp():
    print('Beginning file download ..')
    url = 'https://leech.royalturd.workers.dev/Uploads/twrp-installer-3.5.2_9-0-laurel_sprout.zip'
    r = requests.get(url)
    with open("twrp.zip", "wb") as code:
        code.write(r.content)

def downloadpe():
    url = input("Enter rom url: ")
    print('Beginning file download ..')
    with open("pe.zip", "wb") as f:
         response = requests.get(url, stream=True)
         total = response.headers.get('content-length')

         if total is None:
             f.write(response.content)
         else:
             downloaded = 0
             total = int(total)
             for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
                 downloaded += len(data)
                 f.write(data)
                 done = int(50*downloaded/total)
                 sys.stdout.write('\r[{}{}]'.format('█' * done, '.' * (50-done)))
                 sys.stdout.flush()
    sys.stdout.write('\n')
            

def LocalZIPInstall():
    print('Device connected:',getDeviceCodename())
    x = input('Are you sure to continue? (Y/N)')
    if x.capitalize() == 'Y':
        print('Running zip installation, do not unplug your device or power it off.')
        result = subprocess.run(['adb', 'reboot', 'recovery'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        print(result)
        input('Once you see device rebooting to recovery go to Apply update from ADB, press enter.')
        print(' ')
        print("Flashing ROM")
        result = subprocess.run(['adb', 'sideload', 'pe.zip'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        print(result)
        print('zip successfully sideloaded.')

def installTWRP():
    x = input('Install TWRP? (Y/N)')
    if x.capitalize() == 'Y':
        print(' ')
        print("Flashing TWRP")
        result = subprocess.run(['adb', 'sideload', 'twrp.zip'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        print(result)
        print('TWRP successfully sideloaded.')        


def reboot():
    print('Booting to system...')
    result = subprocess.run(['adb', 'reboot'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    print('Booting...')



splash()
downloadtwrp()
downloadpe()
LocalZIPInstall()
installTWRP()
reboot()


 
