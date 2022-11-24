
from address_extractor.src.address_extractor import PersianAddressExtractor

if __name__ == "__main__":
    extractor = PersianAddressExtractor()
    address = extractor.extract_address("خیابان آزادی کوچه‌ی شهید رضایی") 
    print(address)