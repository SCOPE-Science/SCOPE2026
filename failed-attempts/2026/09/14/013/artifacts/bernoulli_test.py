# Exact integer computation: B_{1,psi} for psi = chi*omega^{-1}, chi=Kronecker(-1031), omega=Teichmuller mod 3.
# chi(a) = Legendre(a mod 1031) for (a,3093)=1 (since 1031 prime =3 mod 4, d=-1031).
# psi(a) = chi(a)*omega(a); omega(a) = +1/-1 by a mod 3. S = sum a*psi(a); B = S/3093.
def legendre(a, p):
    a %= p
    if a == 0: return 0
    v = pow(a, (p-1)//2, p)
    return 1 if v == 1 else -1
S = 0
N = 3093
for a in range(1, N+1):
    if a % 3 == 0 or a % 1031 == 0: continue
    om = 1 if a % 3 == 1 else -1
    S += a * legendre(a, 1031) * om
print("S =", S)
print("S/3093 =", S/3093)
# 3-adic valuation of S
t = S
v = 0
while t % 3 == 0:
    t //= 3; v += 1
print("v3(S) =", v)
print("v3(3093) = 1 => v3(B) =", v-1)
print("S mod 9 =", S % 9)
