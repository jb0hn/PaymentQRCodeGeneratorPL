import segno
from matplotlib import pyplot as plt

class QRCodeGenerator:
    """
    A class used to generate QR codes.
    """

    def __init__(self, receiver_type, id_receiver, country_code, account_number, amount, receiver_name, payment_title, reserve1='', reserve2='', reserve3=''):
        """
        Constructor method
        """
        if receiver_type == 2 and not id_receiver:
            id_receiver = ''
        self.data = self._generate_qr_data(id_receiver, country_code, account_number, amount, receiver_name, payment_title, reserve1, reserve2, reserve3)
    

    def _generate_qr_data(self, id_receiver, country_code, account_number, amount, receiver_name, payment_title, reserve1, reserve2, reserve3):
        """
        Generate a QR data string based on given input
        """
        amount_in_groszy = "{:06d}".format(int(amount * 100))
        data = f'{id_receiver}|{country_code}|{account_number}|{amount_in_groszy}|{receiver_name}|{payment_title}|{reserve1}|{reserve2}|{reserve3}'

        return data

    def create_qr_code(self):
        """
        Create a QR code based on the data string
        """
        self.qr = segno.make(self.data, error='l', boost_error=False)
        return self.qr

    def save_qr_code(self, filename):
        """
        Save the QR code as a PNG file
        """
        self.qr.save(filename, kind='png', scale=10, border=4)

    def display_qr_code(self):
        """
        Display the QR code in Jupyter Notebook
        """
        qr_pil = self.qr.to_pil(scale=10, border=4)
        plt.imshow(qr_pil, cmap='gray')
        plt.axis('off')  # turn off the axis
        plt.show()
