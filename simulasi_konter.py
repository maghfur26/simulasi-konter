import os

def provider_indosat():
    '''function untuk indosat'''
    provider = "indosat"
    pulsa = [25000,30000,50000,100000]
    print("provider: ", provider)
    print("Daftar pulsa:")
    
    for i in pulsa:
        print("Rp.", i)
    return provider,pulsa

def provider_xl():
    '''function untuk xl'''
    provider = "xl"
    pulsa = [25000,30000,50000,100000]
    print("provider: ", provider)
    print("Daftar pulsa:")
    
    for i in pulsa:
        print("Rp.", i)
    return provider,pulsa

def provider_tri():
    '''function untuk tri'''
    provider = "tri"
    pulsa = [25000,30000,50000,100000]
    print("provider: ", provider)
    print("Daftar pulsa:")
    
    for i in pulsa:
        print("Rp.", i)
    return provider,pulsa
    
def provider_liveon():
    '''function untuk liveon'''
    provider = "liveOn"
    pulsa = [65000,120000,250000]
    print("provider: ", provider)
    print("Daftar pulsa:")
    
    for i in pulsa:
        print("Rp.", i)
    return provider,pulsa    

def list_provider():
    daftar_provider = ["1.indosat", "2.xl", "3.tri", "4.liveOn"]
    for i in daftar_provider:
        print(i)
    return daftar_provider

list_provider()
print()
operator = input("Pilih no.provider: ")
if operator == "1":
    provider = "indosat"
    provider_indosat()    
elif operator == "2":
    provider = "xl"
    provider_xl()
elif operator == "3":
    provider = "tri"
    provider_tri()
elif operator == "4":
    provider = "liveOn"
    provider_liveon()   

pulsa = int(input("\nInput jumlah pulsa: "))

# output
os.system("cls") 
print("Uye Konter".center(26))
print("Bantarbolang,Pemalang".center(26))
print("-"*26)
nohp = int(input("nomor hp: "))
print("Provider: ", provider)
print("pulsa   : ", pulsa)
bayar = int(input("jumlah bayar: "))
print("sisa    : ", bayar - pulsa)
print("-"*26)
print("terimakasih".upper().center(26))
print("-"*26)