import random


def numbits(n):
    count = 0
    while (n != 0):
        n = n >> 1
        count += 1
    return count


def modexp(m, a, g):
    ''' This function computes g**a mod m using an efficient modexp algorithm'''
    A = 1
    powers = g
    while (a != 0):
        if (a & 0x1 != 0):
            A = (powers * A) % m
        powers = (powers * powers) % m
        a = a >> 1
    return A


# p is a 1536 bit number
p = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff

# Side question: how many bit is p?
print("Number of bits in p = ", numbits(p))

g = 2

# compute A = g**a mod p
a = random.randint(2, p)
A = modexp(p, a, 2)
print("Number of bits in a = ", numbits(a))
print("a = ", hex(a))
print("A = ", hex(A))

# compute B = g**b mod p
b = random.randint(2, p)
B = modexp(p, b, 2)
print("Number of bits in b = ", numbits(b))
print("b = ", hex(b))
print("B = ", hex(B))

# compute B**a and A**b
s1 = modexp(p, a, B)
s2 = modexp(p, b, A)

print("B**a = ", hex(s1))
print("A**b = ", hex(s2))


