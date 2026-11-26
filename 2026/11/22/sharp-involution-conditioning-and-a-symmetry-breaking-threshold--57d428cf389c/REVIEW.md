# Independent mathematical audit

## correctness

PASS

Reconstructed the exhaustion and the sharp calculation. An anticommuting involution preserves ker N_c and ker N_c², hence is triangular. Up to overall sign its diagonal is (1,-1,1), its adjacent entries x,z satisfy x+z=-2c, and its (1,3) entry is -xz/2; these equations also suffice. The rank-one projection P=(I-J)/2 has norm p=sqrt((1+|x|²/4)(1+|z|²/4)). In an orthonormal range/kernel-complement block the reflection has a 2-by-2 block with diagonal -1,1 and off-diagonal magnitude 2 sqrt(p²-1); its largest singular value is p+sqrt(p²-1). For c≠0, shrinking the two moduli to a sum of |c| and aligning with -c strictly improves any strict triangle inequality. On that boundary p²=|c|²+(rs-1)² and rs runs through [0,|c|²/4]. This proves attainment and all equality cases including c=0 and the merged pair at |c|=2. J^{-1}=J gives squared condition number; the derivative jump is in the second derivative, since p and p' match at 2 with unequal p''. The one-sided construction has p=sqrt(1+|c|²) and is strictly worse for c≠0. Frozen RESULT.md §§1–4 are analytically sufficient. CHECK.py was inspected, not run; it tests finite samples and symbolic feasible-family identities, not continuum optimality. No formal or expert certification is claimed.

## originality

PASS

The supported distinct result is the sharp scalar spectral-norm optimum, its full minimizing set over complex involutions and its transition. The general qualitative anticommutation and involution–projection reduction are antecedents, not new claims. Ranked comparisons disclosed no distinct equivalent. This is a best-of-knowledge decision, not a priority guarantee.

## value

PASS

A qualitative sign symmetry does not measure how much distortion its implementation costs. The normalized three-step complex chain is a natural first case in which an extra coupling remains, and the least norm and the implementers are useful in comparing norm-controlled sign similarities. The two-to-one split of optimizers modulo sign and the optimal condition number are substantive, not just an explicit evaluation of the canonical construction. No claim is made for arbitrary block sizes or unrestricted similarities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
