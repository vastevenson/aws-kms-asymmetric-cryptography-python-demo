import boto3
import json


class Create_Kms_Client:
    """
    Create a KMS boto3 client with AWS to obtain asymmetric keys for encryption + decryption of secrets.
    """

    def __init__(self):
        self.config = self.load_config()
        self.aws_access_key = self.config['aws_access_key']
        self.aws_secret_access_key = self.config['aws_secret_access_key']
        self.aws_kms_arn = self.config['aws_kms_arn']
        self.aws_region_name = self.config['aws_region_name']
        self.kms_client = self.create_kms_client()

    def create_kms_client(self):
        return boto3.client('kms',
                            region_name=self.aws_region_name,
                            aws_access_key_id=self.aws_access_key,
                            aws_secret_access_key=self.aws_secret_access_key)

    def return_kms_client(self):
        return self.kms_client

    def load_config(self, fname='./secrets.json'):
        config = None
        with open(fname) as f:
            config = json.load(f)
        return config


def encrypt_string(secret_text, key_arn_id):
    """
    Use asymmetric encryption with the Aws Kms Sdk in Python to encrypt a string with a given Kms Key Id (ARN).
    :param s:
    :return cipher_text:
    """
    kms_client = Create_Kms_Client().return_kms_client()

    cipher_text = kms_client.encrypt(
        KeyId=key_arn_id,
        Plaintext=secret_text.encode(),
        EncryptionAlgorithm='RSAES_OAEP_SHA_1'
    )['CiphertextBlob']
    return cipher_text


def decrypt_string(cipher_text, key_arn_id):
    """
    Decrypts the cipher text (output of asymmetric encryption by Kms)
    :param cipher_text:
    :param key_arn_id:
    :return:
    """
    kms_client = Create_Kms_Client().return_kms_client()
    text = kms_client.decrypt(
        KeyId=key_arn_id,
        CiphertextBlob=cipher_text,
        EncryptionAlgorithm='RSAES_OAEP_SHA_1'
    )['Plaintext']
    return text.decode()


secret_text = 'sample_text !@#$%'
key_arn_id = 'arn:aws:kms:us-east-2:840560325987:key/e13e3762-04c4-4fba-a57f-4c93beb4e935'
cipher_text = encrypt_string(secret_text, key_arn_id)
text = decrypt_string(cipher_text, key_arn_id)

print(f"Secret text: {secret_text}")
print(f"Unencrypted secret text: {text}")


