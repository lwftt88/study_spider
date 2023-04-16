from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


class AES_DEMO(object):

    def __init__(self, password=b'1234567812345678') -> None:
        self.password = password

    def encrypt_str(self, text = b'abcdefghijklmnhi1'):
        aes = AES.new(self.password, AES.MODE_ECB)  # 创建一个aes对象
        # AES.MODE_ECB 表示模式是ECB模式
        
        en_text = aes.encrypt(pad(text, AES.block_size) )  # 加密明文
        # print("密文：", en_text)  # 加密明文，bytes类型
        return en_text

    def dencrypt_str(self, en_text):
        aes = AES.new(self.password, AES.MODE_ECB)  # 创建一个aes对象
        den_text = unpad(aes.decrypt(en_text), AES.block_size)  # 解密密文
        # print("明文：", den_text)
        return den_text

    def encrypt_file(self):
        block_size = 1024 * 1024  * 1024
        with open('/Users/liuwf/Downloads/test.zip', 'rb') as f:
            with open('/Users/liuwf/Downloads/test.zip.enc', 'wb') as fw:
                while True:
                    content = f.read(block_size)
                    if len(content)==0:
                        break
                    en_text = self.encrypt_str(content)
                    fw.write(en_text)
 
    def dencrypt_file(self):
        block_size = 1024 * 1024 * 1024
        with open('/Users/liuwf/Downloads/test.zip.enc', 'rb') as f:
            with open('/Users/liuwf/Downloads/test1.zip', 'wb') as fw:
                while True:
                    content = f.read(block_size)
                    if len(content)==0:
                        break
                    den_text = self.dencrypt_str(content)
                    fw.write(den_text)
 
 
if __name__ == '__main__':
    aes = AES_DEMO()
    # str_en = aes.encrypt_str()
    # print( aes.dencrypt_str(str_en))

    # aes.encrypt_file()
    
    aes.dencrypt_file()