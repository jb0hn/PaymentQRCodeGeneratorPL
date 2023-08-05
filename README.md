# PaymentQRCodeGeneratorPL

PaymentQRCodeGeneratorPL is a Python library for generating QR codes for payments, following the [Polish payment standards](https://zbp.pl/getmedia/1d7fef90-d193-4a2d-a1c3-ffdf1b0e0649/2013-12-03_-_Rekomendacja_-_Standard_2D). The library accommodates both institutional and individual payment receivers. The generated codes are compatible with major Polish banking apps like IKO by PKO BP, mBank, and Millennium.

## Usage

You can use this library with Python files or Jupyter notebook. Check the `example.py` and `example.ipynb` files in the repository for usage examples.

```python
from PaymentQRCodeGeneratorPL import QRCodeGenerator

qr_generator = QRCodeGenerator(
    receiver_type=1, # for institutional clients, use 1; for individual clients, use 2
    id_receiver='1234567890', # for institutional clients is obligatory (must be a NIP), for individual clients voluntary 
    country_code='PL', 
    account_number='92124012340001567890123456', 
    amount=12.00, 
    receiver_name='Odbiorca 1', 
    payment_title='FV 1234/34/2012'
)

qr_generator.create_qr_code() # creates and displays QR code
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Keywords
Python, QR Code, QR Code Generator, Polish Payment Standard, Płatności QR, Generowanie kodów QR, Standard Płatności Polska, Payment QR Code Poland
