def main():
    m = int(input("m: "))
    Emc2(m)
def Emc2(mass):
    c = 300000000
    E = mass * pow(c, 2)
    print("E: ",E)

main()
