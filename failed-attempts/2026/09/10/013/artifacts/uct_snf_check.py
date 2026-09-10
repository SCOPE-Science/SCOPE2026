"""Step 2 (bounded): UCT torsion-transfer + abelianization sensitivity check.
No external deps beyond sympy. Logs SNF of candidate abelianized relation
matrices for B_n(S), S=once-punctured torus, and the UCT consequence.
This is a plausibility/sensitivity probe, NOT a proof of H1 (presentation
sourced from memory; exact reference not verified in-lane)."""
from sympy.matrices.normalforms import smith_normal_form
from sympy import Matrix, ZZ

def snf_diag(M):
    S = smith_normal_form(M, domain=ZZ)
    return [S[i, i] for i in range(min(S.rows, S.cols))]

n = 5
# Generators ordered (s, A, B): s=braid-class, A,B=surface-loop classes.
# Candidate R1 (naive boundary-relation abelianization): 2(n-1)*s = 0.
M1 = Matrix([[2 * (n - 1), 0, 0]])
# Candidate R2 (order-2 braid class, as in closed-genus literature): 2*s = 0.
M2 = Matrix([[2, 0, 0]])
print("n =", n)
print("R1 diag:", snf_diag(M1), "-> H1 = Z^2 x Z/%d; Ext(H1,Z)=Z/%d" % (2*(n-1), 2*(n-1)))
print("R2 diag:", snf_diag(M2), "-> H1 = Z^2 x Z/2; Ext(H1,Z)=Z/2")
print("UCT: tors H^2(B_n;Z) ~= tors Ext(H1,Z), so R1 predicts Z/8 torsion in H^2, R2 predicts Z/2.")
print("CONCLUSION: H^2 torsion order is presentation-sensitive; without a verified")
print("in-lane presentation + Totaro cocycle z5 + mod-2 reduction + Bockstein cert,")
print("neither target nor exact fallback criterion can be honestly closed.")
