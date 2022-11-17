
from address_extractor.address_extractor import AddressExtraction

if __name__ == "__main__":
    extractor = AddressExtraction()
    address = extractor.run("انگلیس خیابان ملکی") 
    print(address)