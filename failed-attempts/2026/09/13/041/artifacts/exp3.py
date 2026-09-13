"""Exp3: zeta trace of Km(E x E)/F13, E supersingular t=0 (pi^2=-13).
H^1(A): eigs a,abar,a,abar with a=i*sqrt(13). H^2(Km) = wedge^2 H^1(A) (+) 16 exc classes.
Exc trace over F13 = 13 * #(Frob-fixed nodes); nodes=A[2], Frob=pi mod 2, (pi+1)^2=0.
"""
p = 13
# wedge^2 eigenvalues from {a, abar, a, abar}: pairs i<j
# a*abar=13 (4 pairs), a^2=-13, abar^2=-13
tr_wedge = 4 * 13 + 2 * (-13)
print("Tr(Frob | wedge^2 H^1(A)) =", tr_wedge)
# nodes fixed: E[2](F13): #E(F13)=14 -> one nontrivial 2-torsion pt -> fixed line dim1 per E
fixed_nodes = 2 * 2
tr_exc = fixed_nodes * p
print("Tr(Frob | exc) =", tr_exc)
tr = tr_wedge + tr_exc
N = 1 + p * p + tr
print("Tr H^2 =", tr, " #Km(F13) =", N, " tr/13 =", tr / 13)
# F169 check: Frob^2 = -13 on H^1 -> wedge^2 eigs all 169; nodes: pi^2=-13 = 1 mod 2 -> all 16 def/F169
tr2_wedge = 6 * 169
tr2_exc = 16 * 169
N2 = 1 + p**4 + tr2_wedge + tr2_exc
print("#Km(F169) =", N2)
