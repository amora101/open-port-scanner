import socket

# Define the target host and port range
# host = input("Enter the IP address to scan: ")
# port_range = input("Enter the port range to scan (e.g. 1-1024): ")

# Normal Scan - Scan all the ports in the range
def normal_scan(target, port_range = "1-1024", verbose = False):
    """
    Scan the specified ports of a target host and return the open ports.

    Args:
        target (str): The IP address or hostname of the target host.
        port_range (tuple): A tuple containing the range of ports to scan, e.g. (1, 1024).

    Returns:
        A list of integers representing the open ports on the target host.

    Raises:
        ValueError: If the port range is invalid or the target host is unreachable.
        TypeError: If the port range is not a tuple of two integers.
    """

    # Convert the port range string to a list of integers
    start_port, end_port = map(int, port_range.split("-"))

    for port in range(start_port, end_port + 1):
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        
        # Try to connect to the target host and port
        result = s.connect_ex((target, port))
        
        # Check the connection status
        if result == 0:
            print("Port {} is open".format(port))
        
        # Close the socket
        s.close()

# Stealth or Passive Scan - Scan all the ports in the range
def stealth_scan(target, port_range = "1-1024"):
    """
    Scan the specified ports of a target host and return the open ports.

    Args:
        target (str): The IP address or hostname of the target host.
        port_range (tuple): A tuple containing the range of ports to scan, e.g. (1, 1024).

    Returns:
        A list of integers representing the open ports on the target host.

    Raises:
        ValueError: If the port range is invalid or the target host is unreachable.
        TypeError: If the port range is not a tuple of two integers.
    """

    # Convert the port range string to a list of integers
    start_port, end_port = map(int, port_range.split("-"))

    for port in range(start_port, end_port + 1):
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(0.5)
        
        # Try to send a UDP packet to the target host and port
        result = s.sendto(b"", (target, port))
        
        try:
            # Wait for a response from the target host
            data, addr = s.recvfrom(1024)
            
            # Check if the response is valid and print the open port number
            if addr[0] == target:
                print("Port {} is open".format(port))
        except socket.timeout:
            pass
        
        # Close the socket
        s.close()