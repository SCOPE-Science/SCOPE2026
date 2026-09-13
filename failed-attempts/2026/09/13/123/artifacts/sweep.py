"""Refine: restrict to well-conditioned principal subspace? No — max over subspace can
only UNDERestimate. Instead do shift-invert Lanczos / dense geev on (Js, Is) restricted
to kept-55 subspace: max there is a LOWER bound candidate but must double check it's
not a spurious mode (Is nearly singular there inflates). Validate via Rayleigh quotient
in ORIGINAL matrices (done: 3.44341 matches) — Rayleigh match means it IS a genuine
achievable value... but wait, Rayleigh uses same I,J; if I has numerical error, could be off.
Cross-check: evaluate Rayleigh with mpmath 80-digit recomputation for the top vector?
Cheaper: recompute I,J action on c via independent Monte-Carlo-free exact-arithmetic check
on a few entries + increase precision of DP with mpmath for the top-vector quadratic forms.
Also try: does max keep growing if keep threshold lowered (1e-12)? And what is the top vector?
Also important: is 3.44 < 4 robustly? Need certified UPPER bound <4: show 4I-J PSD via exact arithmetic.
Plan: exact rational matrices (Fractions) -> scale to integers -> attempt exact LDL or
interval-Gershgorin certificate. 97x97 exact PSD is heavy but doable via exact Cholesky with Fractions?
Alternative rigorous upper bound: M <= max over a COARSE reliable subspace + bound on tail?
Simplest robust certificate: exact rational computation of A=4I-J entries (common denominator),
then verify PSD by exact LDL' (Fractions, O(n^3) with big ints — 97 dim, feasible in minutes?).
Or compute with sympy exact + cholesky. Let's first inspect: eigenvalue gap below 4: top=3.44, need
upper bound <4, i.e., margin 0.55 (~16%). Also refine float max with threshold sweep.
"""
import numpy as np
I=np.load("output/artifacts/I_mat.npy"); J=np.load("output/artifacts/J_mat.npy")
s0=I[0,0]; In=I/s0; Jn=J/s0
dd=np.sqrt(np.diag(In)); Is=In/dd[:,None]/dd[None,:]; Js=Jn/dd[:,None]/dd[None,:]
for thr in [1e-8,1e-9,1e-10,1e-11,1e-12,1e-13]:
    s,U=np.linalg.eigh((Is+Is.T)/2)
    keep=s>thr
    Uk=U[:,keep]; sk=s[keep]
    A=(Uk*np.sqrt(1/sk)[None,:])
    Y=A.T@((Js+Js.T)/2)@A
    w=np.linalg.eigvalsh(Y)
    print("thr=%.0e kept=%d top6=%s" % (thr, keep.sum(), np.array2string(w[-6:], precision=4)))
