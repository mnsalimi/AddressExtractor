
from address_extractor.src.address_extractor import AddressExtractor

if __name__ == "__main__":
    extractor = AddressExtractor()
    address = extractor.extract_address("خیابان قم") 
    print(address)