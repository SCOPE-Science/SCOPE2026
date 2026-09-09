# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Jones span and Khovanov torsion width on the minimal even-twist weaving ray of closed 3-braids
- **Round:** 2026-09-07-first-light-01
- **Lane:** 332
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Knot Theory
- **Method:** skein exact-triangle recursion with spanning-tree state-sum replay

## Problem

Survey Jones-polynomial spans and Khovanov torsion width over the committed twisted-weaving ray K_k = closure of (sigma1 sigma2^{-1})^{6k+1} sigma1^2 (k = 0,1,2,...), all knots by permutation (123)^{6k+1} = (123) times (12)^2 = id. Compute exact invariants by skein exact-triangle recursion with spanning-tree state-sum replay, prove a closed-form span/width formula in k, and certify the extremal torsion witness in the committed range.

## Attempted claim

For K_k = closure of (sigma1 sigma2^{-1})^{6k+1} sigma1^2 (k>=0): (i) Jones span(K_k) = 2(6k+1)+c with explicit proved constant c (skein induction, verified c on k=0,1); (ii) Khovanov homological width(K_k) = w(k) with explicit proved linear law (constant or linear, fixed by the induction); (iii) an extremal certificate: full integral Khovanov SNF decomposition for the top-range knot K_1 (16 crossings) showing torsion of maximal width in the range -- certified odd-torsion summand Z_p (p odd) with bigrading if present, otherwise certified Z2-only decomposition with maximal width w(1), deciding the odd-torsion appearance on this ray up to K_1 and conjectured for all k via the recursion.

## Research outcome

Refuted-and-corrected the admitted span law on the twisted-weaving ray K_k=cl((s1 s2^-1)^{6k+1} s1^2): K_0 is the trefoil (span 3) with SNF-certified integral Khovanov homology (Z at (0,1),(0,3),(2,5),(3,9); Z_2 at (3,7); width 2), while for k>=1 the committed diagrams are provably-computed adequate (k=1..8) hence alternating with span 12k+4 and width 2. The single-constant law 2(6k+1)+c is false (15 vs actual 16 at k=1). No odd torsion on this ray: Z_2-only holds (certified k=0; alternating structure k>=1), supporting Sazdanovic-Przytycki here. Exceeds the fallback with Jones through k=8 plus the K_0 SNF table.

## Why this attempt failed

Failed axes: value.

value: Intrinsic low value / missing substantive result despite correct+new finite data. Admitted headline required infinite span law 2(6k+1)+c plus width law w(k) plus K1 (16X) integral SNF maximal-width extremal deciding odd torsion. What was delivered: (a) K0 trefoil SNF — textbook-known homology, verification only; (b) refutation of own single-constant guess (15 vs 16) — correction of internal conjecture, not external gap; (c) K1..K8 adequate with sA/sB linear, gT=0, hence alternating, span=n, width 2 thin Z2-only via textbook Kauffman adequacy + Turaev-gT + Lee/Shumakovitch theorems — generic thin outcome, not the hoped thick maximal-width or odd-torsion extremal. K1 integral SNF (core of admitted fallback/extremal) was NOT computed (1.7M-dim, honestly admitted), so no per-bigrading SNF torsion-width extremal exists; torsion for k>=1 follows generically from alternating thinness, not a certificate. Narrow-datum exception does not save it: while the ray was motivated before computation, the established exact values are generic consequences of adequacy (span=n, thin, Z2-only) with no demonstrated downstream need for width-bound/quotient-localization tests (which need thick/maximal examples), and the infinite corrected law span=12k+4 remains unproved computed evidence to k=8. This is textbook application + parameter substitution (weaving word + s1^2) yielding the least-interesting thin case, plus recomputation of known trefoil data. Certification/replay alone does not rescue it. No bounded addition can create a thick extremal on this thin ray or supply the missing substantive phenomenon without new research direction.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: ['K_1 (16X, 1.7M-dim) full integral SNF Khovanov table not computed; torsion/width statements for k>=1 rely on computed adequacy plus the cited Lee alternating-thinness theorem, not a computed cube.', 'No formal infinite-k induction proof is written; the k>=1 span/adequacy law is computed for k=1..8 with the linear sA/sB mechanism, stated as computed law with mechanism, not as theorem.', 'K_0 = trefoil identification uses classical det-3 classification plus matching Jones polynomial.', 'KnotInf…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
