import base64
import binascii

def decode_base64_string(encoded_string):
    try:
        encoded_bytes = encoded_string.encode('ascii')
        decoded_bytes = base64.b64decode(encoded_bytes)

        try:
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except UnicodeDecodeError:
            return f"Decoded (binary data, hex representation): {decoded_bytes.hex()}"
    
    except binascii.Error as e:
        return f"Error decoding base64 string: {e} Input may be invalid."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    
if __name__ == "__main__":    
    print("Base64 Decoder script started")
    print("-----------------------")
    input_string = input("Enter a base64 encoded string: ")
    if not input_string:
        print("No input provided. Exiting.")
    else:
        cleaned_input_string = input_string.strip()
        decoded_result = decode_base64_string(cleaned_input_string)
        print(f"\nDecoded result:\n{decoded_result}")

   