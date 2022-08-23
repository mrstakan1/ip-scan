from func import get_ip_info


def main():
    print('Enter IP:')
    ip = input()
    get_ip_info(ip)

if __name__ == '__main__':
    main()