# PaymentQRCodeGeneratorPL

PaymentQRCodeGeneratorPL is a Python library for generating QR codes for payments, following the [Polish payment standards](https://zbp.pl/getmedia/1d7fef90-d193-4a2d-a1c3-ffdf1b0e0649/2013-12-03_-_Rekomendacja_-_Standard_2D). The library accommodates both institutional and individual payment receivers. The generated codes are compatible with major Polish banking apps like IKO by PKO BP, mBank, and Millennium.

The default functionality of the library allows for manual edit of the amount by the client making the payment. If the `amount` field is set to 0.00, this will result in an amount of "000000" in the generated QR code, enabling the client to manually edit the amount.

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

qr = qr_generator.create_qr_code() # creates QR code, returns a segno.QRCode object
qr_generator.save_qr_code('qr_code.png') # saves the QR code as a PNG file
qr_generator.display_qr_code() # displays the QR code in Jupyter notebook
```

Here is an example of a QR code generated using this code:

<div align="left">
  <img src="./assets/qr_code_institutional.png" alt="Example QR Code" width="200"/>
</div>

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgements

This project makes use of the following third-party libraries:

- [Matplotlib](https://matplotlib.org/): A Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. I use Matplotlib for QR code displaying in this project.
- [Segno](https://segno.readthedocs.io/): A Python library for generating QR Codes and Micro QR Codes. I use Segno to generate QR codes in this project.

## Trademark
"QR Code" and "Micro QR Code" are registered trademarks of DENSO WAVE INCORPORATED.

## Keywords
Python, QR Code, QR Code Generator, Polish Payment Standard, Płatności QR, Generowanie kodów QR, Standard Płatności Polska, Payment QR Code Poland
