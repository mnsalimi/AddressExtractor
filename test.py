
from address_extractor.address_extractor import AddressExtractor

if __name__ == "__main__":
    extractor = AddressExtractor()
    address = extractor.run("خیابان قم") 
    print(address)