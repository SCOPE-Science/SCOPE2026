"""Covering-formula gap check at d=16 (Demailly-El Goul order-2 bigness condition).
c1^2 = d(d-4)^2, c2 = d(d^2-4d+6) for smooth X_d in P^3.
Bigness on zero-locus component requires t < ((13c1^2-9c2)/(12c1^2)) m.
Logs binary gap verdict per (d,m). stdlib only."""
from fractions import Fraction
def chern(d):
    return d*(d-4)**2, d*(d*d-4*d+6)
for d in (15,16,17,18,21):
    c1sq, c2 = chern(d)
    num, den = 13*c1sq-9*c2, 12*c1sq
    r = Fraction(num, den)
    print(f"d={d} c1^2={c1sq} c2={c2} 13c1^2-9c2={num} ratio={r}={float(r):.6f}")
    for m in (3,5,12,19):
        print(f"   m={m}: need t < {r}*{m} = {float(r*m):.4f} -> integer t>=1 possible: {r*m > 1}")
print("GAP_CHECK d=16: ratio=5/96; t < (5/96)m < 1 for all m<=19 -> no (m,t) with t>=1 satisfies order-2 covering bigness. Confirms d=16 below order-2 sufficiency.")
