# Lacunary dual strip ubiquity for shift sqrt(2)-1: full measure with overlap loss at most 1/2

## Context

Classical inhomogeneous Khintchine-Groshev theory gives full Lebesgue measure for
dually approximable sets over all heights for any fixed shift and monotonic
approximating function. Linear-forms mass transference converts Lebesgue
ubiquity inputs into Hausdorff statements but assumes a ubiquity hypothesis it
never verifies on thinned frequency sets. Whether dual ubiquity persists after
thinning frequencies to a lacunary sequence at a fixed inhomogeneous shift is
the recognized gap addressed here. The shift delta = sqrt(2)-1 is the canonical
silver-ratio conjugate in (0,1); heights H_k = 2^k form the canonical lacunary
sequence; Psi_L(H) = 1/(H ln(H+2)) is the Groshev critical decay with no tuned
log-log power.

## Definitions

Let delta = sqrt(2)-1, L = {2^k : k >= 10}, Psi_L(H) = 1/(H ln(H+2)).
For q in Z^2 \\ {0} put H(q) = max(|q1|,|q2|) and

  E_q = { x in T^2 = [0,1]^2 : ||q.x - delta|| < Psi_L(H(q)) },

where ||.|| is distance to Z. The lacunary dually approximable set is

  D_L(delta) = limsup { E_q : H(q) in L },

i.e. x belongs iff |q.x - p - delta| < Psi_L(H(q)) for infinitely many (q,p)
with H(q) in L. Let m be normalized Lebesgue measure on T^2.
Per-shell parallel-free subfamily: F_k = {(2^k, b) : b odd, |b| <= 2^k},
F = union_k F_k. Each q in F_k has H(q) = 2^k and |F_k| = 2^k.

## Result

Theorem. For delta = sqrt(2)-1 and Psi_L(H) = 1/(H ln(H+2)), the lacunary
dually approximable set D_L(delta) over heights H_k = 2^k (k >= 10) has full
two-dimensional Lebesgue measure m(D_L(delta)) = 1. The lacunary divergence
sum_k H_k Psi_L(H_k) = infinity holds, and the determinant overlap-loss ratio
D/S^2 is at most 0.316 (< 1/2) at K = 30 and tends to 0 as K -> infinity.

## Proof / evidence

Lemma 1 (single-strip mass). For every q != 0, m(E_q) = 2 Psi_L(H(q)).
Since 2 Psi_L(H) < 1 (Psi_L <= Psi_L(1024) < 0.0002), the fiber set
{y : ||y|| < Psi} has circle measure 2 Psi; if q1 != 0, x1 -> q1 x1 + c mod 1
is a |q1|-to-1 covering so the x1-section has measure 2 Psi for every x2 and
integrating gives 2 Psi (symmetric argument if q1 = 0).

Lemma 2 (exact pairwise factorization). If det(q,r) != 0 then
m(E_q cap E_r) = m(E_q) m(E_r) = 4 Psi_q Psi_r.
Indeed with integer matrix A with rows q,r and Phi(x) = A x - (delta,delta)
mod 1, the Fourier coefficients of the pushforward satisfy
int e^{2 pi i k.Phi(x)} dx = e^{-2 pi i k.(delta,delta)} int e^{2 pi i (A^T k).x} dx,
which is 1 if A^T k = 0 and 0 otherwise; det A != 0 forces k = 0, so
Phi_*m = m and E_q cap E_r = Phi^{-1}(I_q x I_r) has product measure.
No property of delta is used; all overlap excess sits on parallel pairs,
eliminated by the subfamily below.

Parallel-free property. Any two distinct vectors of F are linearly
independent: same shell gives det = 2^k(c-b) != 0 for distinct odds c != b;
cross-shell k < j gives det = 2^k(c - 2^{j-k} b), an odd-minus-even integer,
hence nonzero. Minimum |det| over shell pair (k,j) is at least 2^min(k,j)
>= 1024 in the window, certified by exact integer census.

First moment. Per-shell mass |F_k| 2 Psi_L(2^k) = 2/ln(2^k+2) =: s_k, and
S(M,K) = sum_{k=M..K} s_k. Since 2^k+2 <= 2^{k+1}, s_k >= 2/((k+1) ln 2):
harmonic divergence, S(10,K) -> infinity. With rigorous 0.693 < ln 2 < 0.6932
(exact rational series plus geometric tail), S(10,13) >= 0.9307 and
S(10,30) >= 3.1687 >= 2.

Second moment and overlap loss. Enumerating F_{<=K}, Lemma 2 makes every
distinct pair factor exactly, so sum_{i,j} m(E_i cap E_j) = S^2 + D with
D := sum_i (m_i - m_i^2) <= S. Hence D/S^2 <= 1/S. At K = 30,
D/S^2 <= 0.3156 < 1/2, and 1/S -> 0 as K -> infinity.

Full measure. Chung-Erdos: m(union_{i<=n} A_i) >= (sum m(A_i))^2 /
sum_{i,j} m(A_i cap A_j). Applied to F_{M..K},
m(union E_q) >= S^2/(S^2+D) >= S/(S+1), at least 0.76 at (10,30).
For every tail M, S(M,infinity) = infinity, so m(union_{k>=M} E_q) = 1.
Since limsup_{q in F} E_q = cap_M union_{k>=M} E_q has measure 1 and
limsup_F E_q subset D_L(delta), m(D_L(delta)) = 1.

## Limitations

Proves full Lebesgue measure and the overlap-loss bound for the named shift
and lacunary sequence only. Hausdorff-measure corollaries via mass
transference and extensions to other shifts or lacunary ratios are not proved
and remain conjectural motivation. Monte-Carlo spot checks in the script are
illustrative; the proof uses only the certified integers and rationals.

## Reproducibility

Run `python3 output/artifacts/verify_lacunary_dual.py` (copied verification
script). It checks with exact int64 arithmetic that all distinct pairs in the
window subfamily have det != 0 (min |det| = 1024), proves
0.693 < ln 2 < 0.6932 with exact Fraction series arithmetic, lower-bounds
S(10,30) >= 3.16 by exact rationals (hence loss <= 0.316 < 1/2), and
cross-checks Lemma 1 and Lemma 2 numerically at true and 100x scales with
fixed seeds. It prints VERIFY_OK and writes ledger.json.

## References

- S. Kim, Inhomogeneous Khintchine-Groshev theorem without monotonicity,
  Bull. London Math. Soc. 2025, doi:10.1112/blms.70114 (full-height
  background; no lacunary thinning).
- V. Beresnevich and S. Velani, Classical metric Diophantine approximation
  revisited: the Khintchine-Groshev theorem, arXiv:0811.0809 (monotonic
  full-height dual theory).
- D. Allen and V. Beresnevich, A mass transference principle for systems of
  linear forms, arXiv:1703.10015 (Lebesgue-to-Hausdorff transfer assuming
  ubiquity; no lacunary shell exponent).
- Kleinbock-Wang / Wang-Wu limsup rectangles ubiquity theory (ubiquity
  assumed, not verified on lacunary shifted frequencies).
- V. Beresnevich et al., Inhomogeneous dual approximation on affine
  subspaces / on manifolds (dual settings over full heights; no 2^k
  lacunary ledger at delta = sqrt(2)-1).
