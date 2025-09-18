# IPToolkit

```
██╗██████╗ ████████╗ ██████╗  ██████╗ ██╗     ██╗  ██╗██╗████████╗
██║██╔══██╗╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██║  ██║██║╚══██╔══╝
██║██████╔╝   ██║   ██║   ██║██║   ██║██║     ███████║██║   ██║   
██║██╔═══╝    ██║   ██║   ██║██║   ██║██║     ██╔══██║██║   ██║   
██║██║        ██║   ╚██████╔╝╚██████╔╝███████╗██║  ██║██║   ██║   
╚═╝╚═╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   

              🛠️  IPToolkit by Parth Palande
```

## 📌 Description

**IPToolkit** is a Python-based CLI tool for analyzing IP addresses and subnet masks. It provides essential networking details such as CIDR notation, network address, broadcast address, usable hosts, and IP class. It’s a simple utility for students, system admins, and security enthusiasts.

## 🚀 Features

* Convert IP address & subnet mask to **CIDR notation**
* Display **network & broadcast address**
* Show **usable host range** and **host count**
* Detect if an IP is **private or public**
* Identify the **IP class (A, B, C, D, E)**
* Colorized **ASCII banner** branding

## 🛠️ Usage

Run the tool:

```bash
python3 iptoolkit.py
```

Example:

```
Enter IP address: 192.168.1.10
Enter subnet mask: 255.255.255.0

=== IP & Subnet Information ===
IP Address: 192.168.1.10
Subnet Mask: 255.255.255.0 (/ 24)
CIDR Notation: 192.168.1.0/24
Network Address: 192.168.1.0
Broadcast Address: 192.168.1.255
Number of Usable Hosts: 254
First Usable Host: 192.168.1.1
Last Usable Host: 192.168.1.254
Is Private?: True
IP Class: Class C
```

## 📂 Project Structure

```
iptoolkit/
│-- iptoolkit.py   # Main script
│-- README.md      # Documentation
```

## ⚡ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/iptoolkit.git
cd iptoolkit
```

Run with:

```bash
python3 iptoolkit.py
```

## 🏷️ Tags

`python` `networking` `subnetting` `iptoolkit` `cli-tool` `cybersecurity`

---

✨ Created by **Parth Palande**
