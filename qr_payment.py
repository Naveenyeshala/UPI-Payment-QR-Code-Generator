import qrcode

def generate_upi_qr(upi_id, recipient_name):
    # Define the UPI payment URLs
    #upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE  

#defining the payment url based on the upi id and the payment app 
# you can modify these urls based on the payment apps you want to support
    phonepe_url = f'upi://pay?pa={upi_id}&pn={recipient_name}'
    google_pay_url = f'upi://pay?pa={upi_id}&pn={recipient_name}'
    paytm_url = f'upi://pay?pa={upi_id}&pn={recipient_name}'

    # Create QR code for each payment app
    phonepe_qr = qrcode.make(phonepe_url)
    google_pay_qr = qrcode.make(google_pay_url)
    paytm_qr = qrcode.make(paytm_url)

    # Save the QR codes as images
    phonepe_qr.save('phonepe_qr.png')
    google_pay_qr.save('google_pay_qr.png')
    paytm_qr.save('paytm_qr.png')

    # Display the QR codes
    phonepe_qr.show()
    google_pay_qr.show()
    paytm_qr.show()

if __name__ == "__main__":
    # Get user input for the UPI ID and recipient name
    upi_id = input("Enter your UPI ID: ")
    recipient_name = input("Enter the recipient name: ")

    # Generate and display the QR codes
    generate_upi_qr(upi_id, recipient_name)
