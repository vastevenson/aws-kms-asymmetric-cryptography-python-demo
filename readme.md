### Readme 

Goal: show how to do asymmetric encryption and decryption with Aws Kms in Python. 

Steps: 
1. Create an Iam user with programmatic access 
2. Don't worry about attaching any policies to this user
3. Copy the access key: `AKIA4HNKMWVRVRX7DMCD`
4. Copy the secret access key: `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`
5. Go to the KMS page in the console - create a key
6. Choose: Asymmetric, Encrypt + Decrypt, RSA_2048
7. Note that the key spec you choose will require specific `EncryptionAlgorithm` choices
8. Choose the Iam user you just made as a key admin
9. Choose the Iam user you just made as a key user
10. Click finish
11. In `secrets.json`, paste in the access key and secret access key for your Iam User.
12. Make sure you made your Iam User + Kms key in the correct region for the boto3 Kms client.
13. Copy the ARN of the Kms key that you just made: `arn:aws:kms:us-east-2:840560325987:key/e13e3762-04c4-4fba-a57f-4c93beb4e935`