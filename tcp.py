def printer(seq, kvi, data, i):
    if i % 2:
        print("B:")
    else:
        print("A:")
    print(f"Sekvensnr.: {seq}")
    print(f"Kvitteringsnr.: {kvi}")
    print("ACK: 1")
    print(f"Data: {data}")
    print()

def updater(seq, kvi, data):
    old_kvi = kvi
    kvi = data + seq
    seq = old_kvi
    return seq, kvi

if __name__ == "__main__":
    seq, kvi, i, ms = 1, 1, 0, 1460
    print("Skriv inn X for å avslutte")
    print()
    while True:
        if i % 2:
            d = input("Antall bytes fra B: ")
        else:
            d = input("Antall bytes fra A: ")
        print()
        if d.lower() == "x":
            break
        d = int(d)
        if d != 0:
            if d > ms:
                rest = d % ms
                tot = d // ms
                new_seq  = seq
                new_kvi = kvi
                for j in range(tot):
                    printer(new_seq, new_kvi, ms, i)
                    new_seq += ms
                    kvi += j*ms
                    if j % 2:
                        printer(new_kvi, new_seq, 0, i+1) 
                printer(new_seq, new_kvi, rest, i)
                new_seq += rest
                printer(new_kvi, new_seq, 0, i+1)
                seq = new_kvi
                kvi = new_seq
            else:
                printer(seq, kvi, d, i)
                seq, kvi = updater(seq, kvi, d)
                printer(seq, kvi, 0, i+1)
        else:
            seq, kvi = updater(seq, kvi, d)
        i += 1