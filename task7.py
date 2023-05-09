def int32ToIp(int32):
    # Convert the integer to binary and pad it with leading zeros
    binary = bin(int32)[2:].zfill(32)
    # Split the binary string into 4 octets of 8 bits each
    octets = [binary[i:i+8] for i in range(0, 32, 8)]
    # Convert each octet from binary to decimal and join them with dots
    return ".".join(str(int(octet, 2)) for octet in octets)
