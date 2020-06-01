def find_empirical_formula(info, l, r):
    for i in range(l, r+1):
        counter = 0
        ans = []
        for t in info:
            integer, dec = str(t[1]*i).split(".")
            integer = int(integer)
            if dec[0] == "0":
                counter += 1
                ans.append((t[0], str(integer)))
            elif dec[0] == "9":
                integer += 1
                counter += 1
                ans.append((t[0], str(integer)))
        if counter == len(info):
            return "".join([t[0]+t[1] for t in ans]), i
    return "RIP (prøv et annet intervall)", -1

if __name__ == "__main__":
    N = int(input("Antall stoffer: "))
    print("Skriv inn grunnstoff og antall mol.")
    print("Eksempel: H 0.69")
    info = []
    lowest = float('inf')
    for _ in range(N):
        g, mm = [x for x in input().split()]
        mm = float(mm)
        if mm < lowest:
            lowest = mm
        info.append((g, mm))
    info = [(t[0], t[1]/lowest) for t in info]
    while True:
        l = int(input("Nedre grense for søk (inklusivt): "))
        r = int(input("Øvre grense for søk (inklusivt): "))
        if l > r:
            print("Nå var du jævlig morsom. Faen ta deg og alt du står for. Vit at Dilawar hater deg.")
            continue
        svar, i = find_empirical_formula(info, l, r)
        if i != -1:
            print(f"Del på {lowest} og multipliser med {i}")
        print(svar)
        s = input("Ønsker du å prøve igjen (Y/N): ")
        if s.lower() == "n":
            break
    print("Du skylder Dilawar 100000000000000000000000 kr nå.")