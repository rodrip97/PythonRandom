import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
data = data.decode('utf-8').split('\n')

wifi_names = []

for profile in data:
    if "All User Profile" in profile:

     profile = profile.split(':')

    profile = profile[1]
    profile = profile[1:-1]

    wifi_names.append(profile)

    for name in wifi_names:
        print(name)

print('{:<20}| {:}\n'.format('Wifi-names', 'Passwords'))

for name in wifi_names:
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear'])
    data = data.decode('utf-8').split('\n')

    passwords = []

    for passw in data:
        if "Key Content" in passw:
            password = passw.split(':')

            password = password[1]
            password = password[1, -1]

            passwords.append(password)

try:
    print('{:<20}| {:}\n'.format('name', 'Passwords[0]'))
except IndexError:
    print('{:<20}| {:}\n'.format('name'))
    print('password' + passw)






