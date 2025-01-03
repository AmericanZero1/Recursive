class SecureCommunication:
    def __init__(self, encryption_key):
        self.encryption_key = encryption_key

    def encrypt_message(self, message):
        encrypted_message = ''.join(chr(ord(char) ^ self.encryption_key[i % len(self.encryption_key)])
                                    for i, char in enumerate(message))
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        return self.encrypt_message(encrypted_message)