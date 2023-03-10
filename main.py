from scanner.scanner import normal_scan
import argparse
import timeit
import socket

if __name__ == '__main__':    

    parser = argparse.ArgumentParser(description='Get IP address from domain name or vice versa')
    parser.add_argument('input', type=str, help='Domain name or IP address')

    args = parser.parse_args()

    # Check if the input is an IP address or a domain name
    try:
        socket.inet_aton(args.input)
        is_ip = True
    except socket.error:
        is_ip = False

    # If the input is a domain name, get the IP address
    if not is_ip:        
        normal_scan(target = args.input)
        # print(f'The IP address of {args.input} is {ip_address}')
    else:        
        normal_scan(target = args.input)
        # domain_name = socket.gethostbyaddr(args.input)[0]
        # print(f'The domain name of {args.input} is {domain_name}')
    
    t = timeit.timeit(normal_scan(target = args.input), number=1)/10
    print(f"Operation completed in {t:.6f}")
