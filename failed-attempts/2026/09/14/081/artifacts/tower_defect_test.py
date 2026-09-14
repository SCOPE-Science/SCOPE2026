"""Toy model of the Rokhlin-tower wrap-around defect (norm vs trace).

Models orthogonal tower projections e_0..e_n and the implementing unitary u
with u e_j u* ~= e_{j+1}. Compares:
 - cyclic tower: alpha(e_n) ~= e_0, so ||u p - p u|| is small (p = sum e_j)
 - non-cyclic tower: no relation on alpha(e_n), so u p - p u ~ (e_n - e_0) u,
   whose operator norm stays 1 even though its normalized trace -> 0 as n grows.

This illustrates why Lin-Osaka Thm 2.9's TR approximation (which needs
norm-small commutators ||[p,a]|| for a in a finite set containing u) collapses
without the cyclic condition. Routine illustration, not a theorem.
"""
import math

def defects(n, cyclic=True, delta=0.01):
    # idealised: each tower projection has trace 1/(n+2) (small remainder left over)
    tr_e = 1.0 / (n + 2)
    if cyclic:
        norm_defect = delta  # ||alpha(e_n)-e_0|| < delta closes the loop
    else:
        # ||e_n - e_0|| = 1 for orthogonal nonzero projections; no closing hypothesis
        norm_defect = 1.0
    trace_defect = 2 * tr_e  # trace of |e_n - e_0| scale
    return norm_defect, trace_defect

if __name__ == "__main__":
    print("n  cyclic_norm  noncyclic_norm  trace_scale")
    for n in [2, 5, 10, 50, 200]:
        cn, _ = defects(n, cyclic=True)
        nn, tr = defects(n, cyclic=False)
        print(f"{n}  {cn:.4f}  {nn:.4f}  {tr:.6f}")
    # TR0/TR1 definitions require norm-small commutators with the finite set
    # F containing u; trace-smallness does not suffice. Hence the gap.
    print("Conclusion: non-cyclic norm defect stays 1 while trace -> 0; proof gap is real.")
