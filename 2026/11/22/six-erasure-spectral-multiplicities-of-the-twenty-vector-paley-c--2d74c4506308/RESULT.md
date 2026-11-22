# Six-erasure spectral multiplicities of the twenty-vector Paley conference frame

## Finding

Let \(S\) be the bordered quadratic-residue skew-conference matrix of order twenty, as defined below, and let \(P=(I+iS/\sqrt{19})/2\) be the rank-ten orthogonal projection giving a Parseval conference frame. For each six-element erasure set \(J\), write \(S_J\) for the principal submatrix. The six possible characteristic polynomials of \(S_J\), and their **exact occurrence counts for this particular frame**, are:

| \(\det(zI-S_J)\) | Number of six-element sets |
|---|---:|
| \(z^6+15z^4+15z^2+1\) | 1,140 |
| \(z^6+15z^4+39z^2+9\) | 6,840 |
| \(z^6+15z^4+47z^2+1\) | 13,680 |
| \(z^6+15z^4+55z^2+25\) | 6,840 |
| \(z^6+15z^4+63z^2+49\) | 7,980 |
| \(z^6+15z^4+63z^2+81\) | 2,280 |

The counts sum to \(\binom{20}{6}=38,760\). The six **possible** polynomials for an arbitrary six-vertex skew-sign matrix were previously listed by Klanderman et al. (2024); the contribution here is the complete, labelled Paley-twenty incidence distribution and its exact worst-erasure classification.

Exactly 1,140 erasure masks give the largest error. They are precisely the masks for which the induced six-vertex tournament is **switching-equivalent to a transitive tournament**. In the Parseval normalization, the worst operator error and sharp surviving lower frame bound are respectively

\[
\max_{|J|=6}\|P_J\|_{\mathrm{op}}=
\frac12+\frac{2+\sqrt3}{2\sqrt{19}},\qquad
\min_{|J|=6}\lambda_{\min}\!\left(I-\sum_{j\in J}f_j f_j^*\right)
=\frac12-\frac{2+\sqrt3}{2\sqrt{19}}>0.
\]

Here the Parseval analysis vectors \(f_j\) have Gram matrix \(P\); no choice of synthesis or phases affects these invariants.

## Assumptions and scope

The index set is \(\{\infty\}\cup\mathbb F_{19}\). Define \(S_{\infty,x}=1\), \(S_{x,\infty}=-1\), \(S_{x,x}=0\), and, for distinct field elements, \(S_{x,y}=\chi(x-y)\), with \(\chi\) the quadratic character of \(\mathbb F_{19}\). Since \(19\equiv3\pmod4\), this is a real skew-symmetric sign matrix. The classical Paley character-sum identity gives \(SS^{\mathsf T}=19I\), also checked exactly in the reproduction code. Therefore \(P\) is an orthogonal projection of rank ten; its rows realize a Parseval frame of twenty vectors in dimension ten. The six chosen indices are unordered and labelled by this point set, and all 38,760 choices are included. All rank, eigenvalue, and error statements are over \(\mathbb C\), with operator norm on Euclidean spaces.

## Proof

**1. Spectral normalization.** From \(S^{\mathsf T}=-S\) and \(SS^{\mathsf T}=19I\), one has \(S^2=-19I\) and \((iS/\sqrt{19})^2=I\). Thus \(P=(I+iS/\sqrt{19})/2\) is Hermitian idempotent, with diagonal \(1/2\). For a six-set \(J\), the nonnegative eigenvalues \(t_1,t_2,t_3\) of \(-S_J^2\), one per conjugate pair, obey \(t_1+t_2+t_3=15\). They are the roots of a cubic
\[
q_J(t)=t^3-15t^2+c_Jt-d_J,
\]
where \(c_J=\sum_{|K|=4,\,K\subset J}\operatorname{Pf}(S_K)^2\) and \(d_J=\operatorname{Pf}(S_J)^2=\det S_J\). Each four-by-four Pfaffian is a sum of three signs, hence its square is either \(1\) or \(9\). If \(k_J\) of the fifteen four-subsets have square nine, then \(c_J=15+8k_J\). The eigenvalues of the erasure compression \(P_J\) are \(\frac12(1\pm\sqrt{t_j/19})\), with one pair for each \(j=1,2,3\).

**2. Complete six-pattern classification.** Switching by a diagonal matrix of signs preserves the characteristic polynomial, the Pfaffian squares of principal submatrices, and the tournament switching class. Switch the first row of any six-by-six skew-sign matrix so that its five off-diagonal entries all equal \(+1\). Exactly \(\binom52=10\) independent signs remain. The script `universal_six.py` exhaustively enumerates all \(2^{10}=1024\) patterns and calculates all fifteen four-Pfaffians and the single six-Pfaffian by the alternating matching expansion. Its exact integer table is:

| \((k_J,d_J)\) | Normalized matrices |
|---|---:|
| \((0,1)\) | 120 |
| \((3,9)\) | 240 |
| \((4,1)\) | 360 |
| \((5,25)\) | 144 |
| \((6,49)\) | 120 |
| \((6,81)\) | 40 |

Every possible six-by-six skew-sign matrix is represented in those cases; none is omitted. The same exhaustive check tests that \((k_J,d_J)=(0,1)\) if and only if the five-vertex tournament remaining after switching the first vertex to a source is transitive. This is also consistent with its 120 possible linear orders and their distinct labelled orientations. Consequently the worst mask type is exactly the switching-transitive type.

**3. Exact Paley-twenty incidence.** The companion `paley20.py` builds the twenty-by-twenty integer matrix using quadratic residues, verifies all 400 entries of \(SS^{\mathsf T}=19I\), then loops lexicographically through every one of the \(\binom{20}{6}\) six-sets. For each set, it computes \(\operatorname{tr}(S_J^4)\) by integer matrix multiplication and \(\det S_J\) by fraction-free integer elimination. Newton's identity gives
\[
c_J=\frac{225-\operatorname{tr}(S_J^4)/2}{2},\qquad
k_J=\frac{c_J-15}{8},\qquad d_J=\det S_J.
\]
The resulting exact integer multiplicities are \(1140,6840,13680,6840,7980,2280\) in the table's order. The separately supplied `paley20_pfaffian.py` independently computes all 38,760 signatures by a quadratic-character/Pfaffian-incidence method, reproducing the counts without using the determinant/trace route. Exhaustiveness is literal, since all index combinations are visited and the counts sum to 38,760; no sample inference or floating-point rank test is involved.

**4. Sharp error and strict recovery.** For the \((0,1)\) class, the cubic factors as
\[
q(t)=(t-1)(t^2-14t+1),
\]
so the largest \(\sqrt{t}\) is \(\sqrt{7+4\sqrt3}=2+\sqrt3\). For the other five cases, the largest squared values are, respectively, \(6+\sqrt{33}<12\); a root strictly between ten and eleven of \(t^3-15t^2+47t-1\); \(5+2\sqrt5<10\); seven; and nine. All are strictly less than \(7+4\sqrt3>13\). Thus only the 1,140 first-type masks maximize \(\|P_J\|\), giving the first formula. The nonzero eigenvalues of the erased-vector frame operator \(\sum_{j\in J} f_j f_j^*\) equal those of \(P_J\); the surviving operator is its complement to the identity, proving the lower bound. Positivity follows from \(7+4\sqrt3<19\). The first-type occurrence count is positive, so the bound is attained.

## Verification

Run `python universal_six.py`, `python paley20.py`, and `python paley20_pfaffian.py` using Python 3; each uses only the standard library. The first checks all 1,024 possible skew-sign patterns after a proven switching normalization and the exact transitive correspondence. The second independently checks the twenty-point conference identity and every one of the 38,760 masks with integer traces and Bareiss determinants. The third calculates an independent full Paley-twenty Pfaffian census. Both methods compute integer invariants without numerical spectral thresholds. The six-possibility classification is consistent with the previously published Seidel characteristic-polynomial table; that table alone cannot establish the Paley-specific multiplicities.

## Relationship to prior work

Renes (2004) constructed Paley-tournament equiangular tight frames; the construction is not new. Kalra (2006) analyzed complex cyclic equiangular frames and primarily two- and three-erasure behavior. Hoffman–Solazzo (2011) analyzed complex three-uniform erasures and the failure of general four-uniformity. Klanderman–Montee–Piotrowski–Rice–Shader (2024), Figure 5, **already lists exactly the six possible degree-six Seidel characteristic polynomials**; neither the list nor its algebraic roots is claimed new. A published five-column skew-conference frame theorem classifies the two possible five-erasure types and their universal multiplicities, without yielding this order-twenty six-erasure incidence distribution. The present claim is specifically the six multiplicities, sharp attained Paley-twenty erasure bound and precise switching-transitive worst-set criterion.

## Limitations

The six-polynomial possibility list was previously known. The six-bin counts and 1,140 worst masks are proved for the explicit order-twenty Paley matrix only, not for arbitrary skew-conference matrices or all prime-power Paley orders. The classification does not enumerate the finer automorphism orbits within each spectral type, weighted erasures, or the optimality of this frame against all possible twenty-vector frames. No independent mathematical audit or external validation has been performed. The literature comparison cannot exclude an unindexed earlier calculation of the same Paley-twenty incidence numbers.

## References

- J. M. Renes, *Equiangular Tight Frames from Paley Tournaments*, initial public version 2004-08-20, https://arxiv.org/abs/math/0408287.
- D. Kalra, *Complex Equiangular Cyclic Frames and Erasures*, initial public version 2006-02-15, https://arxiv.org/abs/math/0602342 (especially Section 6).
- T. R. Hoffman and J. P. Solazzo, *Complex Equiangular Tight Frames and Erasures*, initial public version 2011-07-08, https://arxiv.org/abs/1107.2267.
- S. Klanderman, M. Montee, A. Piotrowski, A. Rice and B. Shader, *Determinants of Seidel Tournament Matrices*, initial public version 2024-06-14, https://arxiv.org/abs/2406.09697 (Figure 5 and Section 7).
- *Five-column spectral dichotomy and exact multiplicities for skew-conference tight frames*, public mathematical manuscript, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-five-column-spectral-dichotomy-and-exact-multiplicities-for-skew--86724d774ebb.
