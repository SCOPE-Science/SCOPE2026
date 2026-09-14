from cypari2 import Pari
pari = Pari()
pari.default("parisize", "1024M")
# l=1031 in K1,1: splitting (should stay 2 primes: inert in Q-direction, split in K1-direction)
Q='x^6 - 3*x^5 + 771*x^4 - 1535*x^3 + 200463*x^2 - 201249*x + 17575221'
dec = pari(f'idealprimedec(nfinit({Q}),1031)')
print("primes above 1031 in K11:", dec)
print("count:", len(list(dec)))
# and above 3 in Q1: ramified?
print("primes above 3 in Q1:", pari('idealprimedec(nfinit(x^3-3*x+1),3)'))
# class group quotient approach: |A(K11)^G| via bnrinit ray class? just gens
print("A11 cyc:", pari(f'(bnfinit({Q},1)).cyc'))
print("A11 gen:", pari(f'(bnfinit({Q},1)).gen'))
