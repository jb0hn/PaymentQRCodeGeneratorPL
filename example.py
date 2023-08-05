from qrcode_generator import QRCodeGenerator

# Example usage for institutional client
qr_generator_institutional = QRCodeGenerator(
    receiver_type=1,
    id_receiver='1234567890', 
    country_code='PL', 
    account_number='92124012340001567890123456', 
    amount=12.00, 
    receiver_name='Odbiorca 1', 
    payment_title='FV 1234/34/2012'
)

# Create the QR code
qr_generator_institutional.create_qr_code()

# Display the QR code in Jupyter notebook
qr_generator_institutional.display_qr_code()

# Save QR code to PNG
qr_generator_institutional.save_qr_code('qr_code_institutional.png')


# Example usage for individual client
qr_generator_individual = QRCodeGenerator(
    receiver_type=2,
    id_receiver='',  # NIP is optional for individual client
    country_code='PL', 
    account_number='92124012340001567890123456', 
    amount=12.00, 
    receiver_name='Odbiorca 2', 
    payment_title='FV 5678/78/2023'
)

# Create the QR code
qr_generator_individual.create_qr_code()

# Display the QR code in Jupyter notebook
qr_generator_individual.display_qr_code()

# Save QR code to PNG
qr_generator_institutional.save_qr_code('qr_code_individual.png')
