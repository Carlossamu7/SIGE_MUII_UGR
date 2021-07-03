import phe

public_key, private_key = phe.generate_paillier_keypair(n_length=1024)

# Se encripta el número 5
x = public_key.encrypt(5)

# Se encripta el número 3
y = public_key.encrypt(3)

# Se suman los dos valores encriptados
z = x + y

# Se desencripta el resultado
z_ = private_key.decrypt(z)
print("The Answer: " + str(z_))
