from collections import Counter

#Variables Globales

alpha = 'abcdefghijklmnopqrstuvwxyz'

#Assigne un index pour chaque lettre dans un dictionnaire

def corresp(lettre):
     for i in range(len(alpha)):
         if alpha[i] == lettre:
            return i

texte = 'snzsmmifkcgusivsniwnasotshnohbzizgkcsfmgulifbsmizfiwyvhybjyvocmbnxfcaruvgxmguntuqfyaeoqgyupfiwyvhcudizhuvhyasnkchawxmfujzyadoqgkcsfmgazohlsmxslachvsmijuqshbzuqfnzsmwqwcdymgybduzqyyiivbykcgxfyvocbfcmbutsozgamgnmgfwfmyiivguxslkccbihjsucxicfkcsfmilacwkijihcwbmachbdcmhlmgfmilusnqslnwamsnyictghwbnxzoarytwyvopmqfijcmdicfkcccvsjigwwbnqbomfnmzovshnohbojwfnmffiryagoazyusgmfyoolleomgozqyyicmgnmhlibamfliwhmfgifcifctyytsnbfyaoovxycbyxcybs'

#scindermod
def scindermod(texte, longueur):
    liste = []
    for i in range(longueur):
        liste.append(texte[i::longueur])
    return liste

liste = scindermod(texte, 3)

ListeUn = Counter(liste[0]).most_common(2)
ListeDeux = Counter(liste[1]).most_common(2)
ListeTrois = Counter(liste[2]).most_common(2)

print(alpha[corresp(ListeUn[0][0])-corresp('e')])
print(alpha[corresp(ListeDeux[0][0])-corresp('e')])
print(alpha[corresp(ListeTrois[0][0])-corresp('e')])

#Concaténation pour avoir notre clé
cle = alpha[corresp(ListeUn[0][0])-corresp('e')] + alpha[corresp(ListeDeux[0][0])-corresp('e')] + alpha[corresp(ListeTrois[0][0])-corresp('e')]

#Dechiffrement Vigenere
def dechiffrementVigenere(texte, cle):
    dechiffrer = ""
    for i in range(len(texte)):
        dechiffrer += alpha[(corresp(texte[i]) - corresp(cle[i % len(cle)])) % len(alpha)]
    return dechiffrer

#Chiffrement Vigenere
def chiffrementVigenere(texte, cle):
    chiffrer = ""
    for i in range(len(texte)):
        chiffrer += alpha[(corresp(texte[i]) + corresp(cle[i % len(cle)])) % len(alpha)]
    return chiffrer
        

print(dechiffrementVigenere(texte, cle))















