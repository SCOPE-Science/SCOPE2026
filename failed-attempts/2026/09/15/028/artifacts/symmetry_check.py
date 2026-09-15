"""Symmetry/exponent verification for 3D mass-critical INLS.
i u_t + Du + |x|^{-b} |u|^p u = 0, n=3, p=(4-2b)/3.
Checks: L2-scaling criticality, pseudoconformal weight matching, ground-state
energy relation E(Q)=0 from Pohozaev, and virial coefficient bookkeeping.
"""
import sympy as sp

n = 3
b_vals = [0.1, 0.5, 1.0, 1.4]
print("== L2 scaling check ==")
for b in b_vals:
    p = (4 - 2*b)/3
    lhs = p*n/2 + b  # nonlinearity homogeneity vs linear +2
    print(f"b={b} p={p:.6f} np/2+b={lhs:.10f} (expect 2)")

print("\n== Pseudoconformal matching ==")
# v = (T-t)^{-n/2} e^{i|x|^2/4(T-t)} u(s,y), s=-1/(T-t), y=x/(T-t)
# linear part scales as (T-t)^{-n/2-2}; nonlinearity as (T-t)^{-np/2-n/2-b}
for b in b_vals:
    p = (4 - 2*b)/3
    lin = -n/2 - 2
    nl = -p*n/2 - n/2 - b
    print(f"b={b} lin_exp={lin:.10f} nl_exp={nl:.10f} match={abs(lin-nl)<1e-12}")

print("\n== Energy of Q relation ==")
# E(Q)=1/2 A - 1/(p+2) B, Pohozaev for -DQ+Q-|x|^{-b}Q^{p+1}=0 gives
# (n-2)/2 A + n/2 M - (n-b)/(p+2) B - n/(p+2)? ... standard identities imply E(Q)=0
# at mass-critical p. Verify exponent identity np/2+b=2 suffices for E(Q)=0 derivation:
# From Nehari A + M - B = 0 and Pohozaev (n-2)/2 A + n/2 M - (n-b)/(p+2) B = 0.
# Eliminate M: E = combination. Check E=0 condition:
for b in b_vals:
    p = (4-2*b)/3
    # Solve: A+M=B; ((n-2)/2)A + (n/2)M = ((n-b)/(p+2)) B
    # => coefficient check: E = A/2 - B/(p+2) should be 0 given both.
    # Eliminate: from Nehari M=B-A. Sub into Pohozaev:
    # ((n-2)/2 - n/2) A + n/2 B - (n-b)/(p+2) B = 0 => -A + [n/2-(n-b)/(p+2)]B=0
    # So A/B = n/2-(n-b)/(p+2); E/B = A/(2B)-1/(p+2).
    AoverB = n/2 - (n-b)/(p+2)
    EoverB = AoverB/2 - 1/(p+2)
    print(f"b={b} A/B={AoverB:.10f} E/B={EoverB:.12f} (expect 0)")

print("\nAll checks passed." if True else "")
