from numpy.polynomial.polynomial import Polynomial
import numpy as np

class LatticeBasedEncryption:
    def __init__(self, degree=256, modulus=8192):
        self.degree = degree
        self.modulus = modulus

    def generate_keys(self):
        secret_key = Polynomial(np.random.randint(0, 2, self.degree))
        public_key = Polynomial(np.random.randint(0, self.modulus, self.degree))
        return secret_key, public_key

    def encrypt(self, message, public_key):
        message_poly = Polynomial(message)
        noise_poly = Polynomial(np.random.randint(-1, 2, self.degree))
        ciphertext = (message_poly + public_key * noise_poly) % self.modulus
        return ciphertext

    def decrypt(self, ciphertext, secret_key):
        decrypted_poly = (ciphertext * secret_key) % self.modulus
        return np.round(decrypted_poly.coef) % 2