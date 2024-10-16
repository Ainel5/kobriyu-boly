x=3
def qosu (birinchi_san, ekinchi_san):
    nat = birinchi_san+ekinchi_san
    print ("eki san kosyndysy: ",nat)
def azaitu (birinchi_san, ekinchi_san) :
    nat = birinchi_san-ekinchi_san
    print ("eki san aiyrmasy: ", nat)
def kobeity (birinchi_san, ekinchi_san) :
    nat = birinchi_san * ekinchi_san
    print ("eki san kobeity: ", nat)
def boly (birinchi_san, ekinchi_san):
    nat = birinchi_san/ekinchi_san
    print ("eki san boly:",nat)

while x>2:
    san1= int (input ("1-san: ") )
    amal=input ("amaldy engiz ( (+-*/):")
    san2= int (input ("2-san: ") )
    if (amal=="+") :
        qosu (san1, san2)
    elif (amal=="-"):
        azaitu (san1, san2)
    elif (amal=="*"):
        kobeity (san1, san2)
    elif (amal=="/"):
        boly (sanl, san2)