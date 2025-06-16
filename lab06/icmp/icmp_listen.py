from scapy.all import *

def packet_callback(packet):
    if packet.haslayer(ICMP):
        icmp_packet = packet[ICMP]
        print("\nICMP Packet Information:")
        print(f"Source IP: {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")
        print(f"Type: {icmp_packet.type}")
        print(f"Code: {icmp_packet.code}")
        print(f"ID: {icmp_packet.id}")
        print(f"Sequence: {icmp_packet.seq}")
        print(f"Load: {icmp_packet.load}")
        print("=" * 30)

def main():
    print("Starting ICMP packet sniffer...")
    print("Press Ctrl+C to stop\n")
    try:
        sniff(prn=packet_callback, filter='icmp', store=0)
    except KeyboardInterrupt:
        print("\nSniffer stopped by user")

if __name__ == '__main__':
    main()