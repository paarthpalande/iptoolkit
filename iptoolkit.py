import ipaddress

def banner():
    print(r"""
██╗██████╗ ████████╗ ██████╗  ██████╗ ██╗     ██╗  ██╗██╗████████╗
██║██╔══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██║  ██║██║╚══██╔══╝
██║██████╔╝   ██║   ██║   ██║██║   ██║██║     ███████║██║   ██║   
██║██╔═══╝    ██║   ██║   ██║██║   ██║██║     ██╔══██║██║   ██║   
██║██║        ██║   ╚██████╔╝╚██████╔╝███████╗██║  ██║██║   ██║   
╚═╝╚═╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   

              🛠️  IPToolkit by Parth Palande
    """)

def mask_to_prefix(mask):
    """Convert subnet mask to prefix length."""
    return ipaddress.IPv4Network(f"0.0.0.0/{mask}").prefixlen

def ip_info(ip_input, subnet_mask_input):
    try:
        ip_address = ipaddress.IPv4Address(ip_input)
        prefix_length = mask_to_prefix(subnet_mask_input)
        network = ipaddress.IPv4Network(f"{ip_input}/{prefix_length}", strict=False)

        print("\n=== IP & Subnet Information ===")
        print(f"IP Address: {ip_address}")
        print(f"Subnet Mask: {subnet_mask_input} (/ {prefix_length})")
        print(f"CIDR Notation: {network.network_address}/{network.prefixlen}")
        print(f"Network Address: {network.network_address}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"Number of Usable Hosts: {network.num_addresses - 2}")
        print(f"First Usable Host: {list(network.hosts())[0]}")
        print(f"Last Usable Host: {list(network.hosts())[-1]}")
        print(f"Is Private?: {ip_address.is_private}")
        print(f"IP Class: {ip_class(ip_address)}")

    except ValueError as e:
        print("Invalid input:", e)

def ip_class(ip):
    """Return IP class based on first octet."""
    first_octet = int(str(ip).split('.')[0])
    if 1 <= first_octet <= 126:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D (Multicast)"
    elif 240 <= first_octet <= 255:
        return "Class E (Experimental)"
    return "Unknown"

if __name__ == "__main__":
    banner()
    ip_input = input("Enter IP address: ")
    subnet_mask_input = input("Enter subnet mask: ")
    ip_info(ip_input, subnet_mask_input)
