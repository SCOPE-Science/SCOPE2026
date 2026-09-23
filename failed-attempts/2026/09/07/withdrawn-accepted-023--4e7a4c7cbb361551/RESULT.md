# Certified equiangular lines with angle arccos(1/3) in R^6-R^8

## Statement

For alpha=1/3: N_{1/3}(6)=16 and N_{1/3}(7)=28 exactly; 28<=N_{1/3}(8)<=29;
the 28-line triangular configuration is inclusion-maximal (no 29th
+-1/3 line extends it in any dimension).

## Context

Equiangular lines connect spherical codes, quantum measurements and
Delsarte-type bounds. For fixed alpha, Jiang et al. give N_{1/3}(d)=2d-2
for sufficiently large d, which does not settle small dimensions where
sporadic configurations (e.g. 28 in R^7) exceed the asymptotic line.
The strata d=6,7,8 at alpha=1/3 are patchy in handbooks; this work
provides a fully machine-checkable certified table with explicit Gram
witnesses, an explicit Delsarte polynomial tightening d=8, and an
elementary nonextendability theorem.

## Definitions

For d>=1 and alpha in (0,1), N_alpha(d) is the maximum n for which unit
vectors v_1..v_n in R^d satisfy |<v_i,v_j>|=alpha for i!=j.
Put G_ij=<v_i,v_j>: G_ii=1, G_ij in {+alpha,-alpha}, G PSD of rank<=d,
and conversely any such G arises from lines. For alpha=1/3 write
M=3G: M_ii=3, M_ij in {+1,-1}, M PSD, rank<=d.

## Result

(a) N_{1/3}(6)=16, N_{1/3}(7)=28.
(b) 28<=N_{1/3}(8)<=29 (Gerzon 36 tightened to 29).
(c) The 28 vectors attaining (a) in R^7 (hence R^8) admit no additional
unit vector x with |<x,v_ij>|=1/3 in any dimension; i.e. the saved
28x28 M has no PSD extension [[M,b],[b^T,3]] with b in {+-1}^28.
Conjecture (not proved): N_{1/3}(8)=28.

## Proof / Evidence

Absolute (Gerzon): v_i v_i^T in Sym_d (dim d(d+1)/2) have Frobenius
products 1 diag, alpha^2 off; ((1-alpha^2)I+alpha^2 J)c=0 forces c=0
since eigenvalues 1-alpha^2>0 and 1-alpha^2+n alpha^2>0; hence
n<=d(d+1)/2: 21,28,36 for d=6,7,8.

Relative (trace): eigenvalues lambda>=0, at most d nonzero,
tr G=n, tr(G^2)=n+n(n-1)alpha^2, n^2=(sum lambda)^2<=d sum lambda^2;
hence n(1-d alpha^2)<=d(1-alpha^2); for alpha^2=1/9: 16 (d=6),
28 (d=7), 64 (d=8).

Delsarte LP (Delsarte-Goethals-Seidel 1977, cited): if
f=sum f_k P_k (P_k Gegenbauer for S^{d-1}, P_k(1)=1) with f_k>=0
(k>=1) and f<=0 on {+-alpha}, then n<=f(1)/f_0.
Certificates (exact rational checks):
d=6: 18t^2-2=1+15P2, P2=(6t^2-1)/5, f(1)=16, f(+/-1/3)=0;
d=7: (63t^2-7)/2=1+27P2, P2=(7t^2-1)/6, f(1)=28;
d=8: (3240t^4-1620t^2+140)/59=1+(1701/59)P4,
P4=(40t^4-20t^2+1)/21, f(1)=1760/59=29.8305, f(+/-1/3)=0.
Hence n<=16,28,29 integrally. Among evens to degree 60, k=4 is
optimal for d=8; odd terms cannot help alone.

Lower bounds: Clebsch SRG(16,5,0,2) (4-bit strings, join iff
Hamming xor in {1,4}, degree 5 verified) gives M=3I+S (S=J-I-2A),
exact LDL pivots 3,8/3,5/2,12/5,4/3,1 then 10x10 Schur zero, so PSD
rank 6; float eig min -2.3e-15, max 8.0. Triangular T(8) (28
two-subsets of an 8-set, join iff intersect in 1, degree 12) gives
M=3I-S, pivots 3,8/3,5/2,12/5,7/3,16/7,9/4 then 21x21 Schur zero,
so PSD rank 7; float min -5.5e-15, max 12.0. Geometric form
u_i=e_i-1/8*1, w_i=u_i/sqrt(7/8) (<w_i,w_j>=-1/7),
v_ij=sqrt(2/3)(u_i+u_j) has Gram +1/3 (share) / -1/3 (disjoint),
matching saved matrix to 3.4e-16. Embedding R^7 in R^8 gives 28
in R^8. With upper bounds this proves (a)-(b).

Nonextendability: write putative new unit vector as (y,t) with y in
the 7-dim span (covers every ambient dimension). Put z_i=<y,w_i>,
sum z=0, <y,v_ij>=sqrt(7/12)(z_i+z_j), so |z_i+z_j|=2/sqrt(21)=:c.
Sum_{i<j}(z_i+z_j)^2=28c^2 but also =6 sum z_i^2 (each square in 7
pairs, cross term -S2/2), so sum z_i^2=8/9 exact (c^2=4/21).
For distinct i,j,k, 2z_i=c(s_ij+s_ik-s_jk) with s=+-1, so
z_i in {+-1,+-3}/sqrt(21). Write a=1/sqrt(21); (sum z_i^2)/a^2 must
be integer, but (8/9)/(1/21)=56/3, contradiction. QED. Norm
(7/8)*8/9=7/9<=1 consistent.

Search frontier (not claiming closure): PSD backtracking leaves
1,2,8,53,523,6899 for n=2..7 (stacked 1,3,11,75,923,17659, 0.14s at
n=7); 2^406 patterns to n=29 hopeless in 2h; even fixed-T8 extension
(2^28) needs ~0.8h for float filter alone (min residual 0.4364).
Second PSD implementation (pivoted float Cholesky) agrees with eig.

## Limitations

Delsarte positivity cited, not reproved. Small-d values 16,28 follow
from classical bounds plus known graphs and may be handbook-tabulated;
contribution is machine-checkable certification plus tightened 29 and
nonextendability. N_{1/3}(8)=28 conjectured but not proved; a
non-T8 29-set is not ruled out. Kao-Yu SSRN 2026 four-point SDP claims
uniqueness for 7<=d<=14 at 1/3 (unrefereed, only abstract inspected);
if verified it would subsume the gap. Barg-Yu SDP tables may already
imply <=29; comparison beyond Gerzon baseline not performed.

## Reproducibility

Requires python3 + numpy + sympy only.
`python3 output/artifacts/bounds.py` recomputes Gerzon/relative and
verifies Delsarte identities, prints 16,28,1760/59.
`python3 output/artifacts/witnesses.py` rebuilds both matrices from
graph definitions, checks symmetry/diag/alphabet, runs exact Fractions
LDL (prints pivots/perm, asserts Schur zero) and float eig, rewrites CSVs.
`python3 output/artifacts/nonextend.py` rebuilds simplex-sum coordinates,
checks Gram equality, verifies 56/3 contradiction.
`python3 output/artifacts/frontier.py` checks second PSD implementation,
small-n counts, T8-extension barrier. All scripts assert; any failure raises.

## References

P. Delsarte, J. M. Goethals, J. J. Seidel, Spherical codes and designs,
Geom. Dedicata 6 (1977), 363-388. https://doi.org/10.1007/BF03187604
P. W. H. Lemmens, J. J. Seidel, Equiangular lines, J. Algebra 24 (1973),
494-512. https://doi.org/10.1016/0021-8693(73)90123-3
Z. Jiang et al., Equiangular lines with a fixed angle, Ann. Math. 194
(2021), 729-743. https://arxiv.org/abs/1907.12466
Y. Lin, W.-H. Yu, Equiangular lines and the Lemmens-Seidel conjecture.
https://arxiv.org/abs/1807.06249
D. de Laat et al., The Lasserre hierarchy for equiangular lines with a
fixed angle. https://arxiv.org/abs/2211.16471
G. Greaves et al., Equiangular lines in Euclidean spaces.
https://arxiv.org/abs/1403.2155
A. Barg, W.-H. Yu, New bounds for equiangular lines.
https://doi.org/10.1090/conm/625/12494
