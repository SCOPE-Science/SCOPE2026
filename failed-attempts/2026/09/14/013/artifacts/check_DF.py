from cypari2 import Pari
pari = Pari()
pari.default("parisize", "2048M")
Q='x^6 - 3*x^5 + 771*x^4 - 1535*x^3 + 200463*x^2 - 201249*x + 17575221'
# degree / signature
print("nfinit poldegree:", pari(f'poldegree({Q})'))
print("nfdisc factors:", pari(f'factor(nfdisc({Q}))'))
# Galois group of degree-6 layer?
print("polgalois K1,1:", pari(f'polgalois({Q})'))
# norm of relative units / prime splitting above 3 in K1,1: count primes
nf = pari(f'nfinit({Q})')
dec = pari(f'idealprimedec(nfinit({Q}),3)')
print("primes above 3 in K11:", dec)
print("nprimes:", len(list(dec)))
