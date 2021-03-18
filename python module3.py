def print_menu( ):
    print("Welkom!")
    print("Kies d om door te gaan")
    print("Kies q om te stoppen")
    

def main( ):
    doorgaan = True
    praten = {"vraag": "Wat is uw keuze? ", "stop": "Ok ik stop"}
    while doorgaan:
        print_menu( )
        
        keuze = input(praten["vraag"])
        
        if keuze == 'q':
            doorgaan = False
            print(praten["stop"])
            
            
            
main()