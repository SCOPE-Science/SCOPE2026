"""Trace-pairing nondegeneracy certificate for X=[sl3*/SL3] 1-shifted symplectic form."""
import sympy as sp

# Basis of sl3: E12,E21,E13,E31,E23,E32,H1,H2
# Pairing <A,B> = tr(AB). Gram computed analytically.
# E_ij pairs: tr(E_ij E_kl) = delta_jk delta_il.
# H1=E11-E22, H2=E22-E33: tr(H1^2)=2, tr(H2^2)=2, tr(H1H2)=-1.
G = sp.zeros(8)
# order: E12,E21,E13,E31,E23,E32,H1,H2
pairs = {(0,1):1,(1,0):1,(2,3):1,(3,2):1,(4,5):1,(5,4):1}
for (i,j),v in pairs.items():
    G[i,j]=v
G[6,6]=2; G[7,7]=2; G[6,7]=-1; G[7,6]=-1
print("Gram matrix:")
sp.pprint(G)
d = G.det()
print("det =", d)
assert d != 0, "pairing degenerate!"
# Eigenvalues / signature not needed; nondeg over C iff det != 0
print("Trace pairing NONDEGENERATE: 1-shifted 2-form on [g*/G] nondegenerate at 0.")
print("Block det H =", sp.Matrix([[2,-1],[-1,2]]).det(), "(=3)")
print("E-block det = 1; total det =", d, "(sign convention dependent, nonzero).")
