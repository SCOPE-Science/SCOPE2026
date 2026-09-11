import sympy as sp
x=sp.Symbol('x')
f = x**6 - 3*x**5 + x**4 + 0*x**3 + 3*x**2 - x + 1
print("f =", f)
print("f(0) =", f.subs(x,0))
fp = sp.diff(f,x)
print("fp =", fp)
disc = sp.discriminant(f, x)
print("disc =", disc)
print("factor disc:", sp.factorint(int(disc)))
# gcd(f,fp) over QQ
print("gcd:", sp.gcd(f, fp))
# check roots mod small primes: good reduction = disc != 0 mod p
for p in [2,3,5,7,11,13,17,19,31]:
    print(p, int(disc)%p != 0)
