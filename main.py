from scanner.scanner import normal_scan, stealth_scan
import argparse
import timeit
import socket

if __name__ == '__main__':    

    parser = argparse.ArgumentParser(description='Get IP address from domain name or vice versa')
    parser.add_argument('input', type=str, help='Domain name or IP address')
    parser.add_argument('-s', '--stealth', action='store_true', help='Stealth Scan')

    args = parser.parse_args()

    # Check if the input is an IP address or a domain name
    try:
        socket.inet_aton(args.input)
        is_ip = True
    except socket.error:
        is_ip = False

    # If the input is a domain name, get the IP address        
    if not is_ip:        
        if args.stealth:
            print ('Stealth Scan')
            stealth_scan(target = args.input)
        else:
            print ('Normal Scan')
            normal_scan(target = args.input)        
    else:                
        if args.stealth:
            print ('Stealth Scan')
            stealth_scan(target = args.input)
        else:
            print ('Normal Scan')
            normal_scan(target = args.input)
    
    t = timeit.timeit(normal_scan(target = args.input), number=1)/10
    print(f"Operation completed in {t:.6f}")
