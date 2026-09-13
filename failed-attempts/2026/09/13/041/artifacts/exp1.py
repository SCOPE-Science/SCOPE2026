"""Exp1: supersingular E/F13 + point counts; Kummer trace signature; free-sign-involution linear algebra."""
p = 13
QR = {pow(a, 2, p) for a in range(p)}

def chi(a):
    a %= p
    if a == 0: return 0
    return 1 if a in QR else -1

def count_weierstrass(rhs):
    # y^2 = rhs(x), affine + point at infinity
    n = 1
    for x in range(p):
        c = chi(rhs(x))
        n += 1 + c
    return n

# Candidate E: y^2 = x^3 + x (j=1728)
E1 = count_weierstrass(lambda x: x**3 + x)
# Candidate E2: y^2 = x^3 + 1 (j=0)
E2 = count_weierstrass(lambda x: x**3 + 1)
# Candidate E3: y^2 = x^3 + 2x + 1
E3 = count_weierstrass(lambda x: x**3 + 2*x + 1)
print("counts:", E1, E2, E3, "traces:", 1+p-E1, 1+p-E2, 1+p-E3)
for name, n in [("E1", E1), ("E2", E2), ("E3", E3)]:
    t = 1 + p - n
    print(name, "n=", n, "t=", t, "t mod 13 =", t % p, "supersingular=", (t % p == 0))

# Kummer Km(E x E): #Km(Fq) formula for Kummer resolution:
# #Km = (1/2)(#A + 2*T1 + ... ) -- use simple singular model count instead:
# singular Kummer quartic: #A(Fq) + correction. Just print #AxA:
for name, n in [("E1", E1), ("E2", E2), ("E3", E3)]:
    print(name, "#AxA =", n * n)

# Target signature: sigma=1 fully split => #X(F13) = 1 + 169 + 22*13 = 456
print("sigma=1 fully-rational target count:", 1 + p*p + 22*p)
# Enriques quotient Y: #Y = (#X + 4)/2 if free involution over Fq? (Lefschetz: trace on H^2_X splits)
# For free involution, #Y(Fq) = 1 + q^2 + t_q where t from invariant part. Print X target:
print("If X#=456 and iota free defined/F13, Y# = (456 + 0)/2 + ... need trace split; rough Y# in [~...]")
