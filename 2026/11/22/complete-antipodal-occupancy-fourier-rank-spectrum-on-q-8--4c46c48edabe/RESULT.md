# Complete antipodal-occupancy Fourier-rank spectrum on \(Q_8\)

## Finding
Let \(Q_8=\{\pm1,\pm i,\pm j,\pm k\}\), where \(i^2=j^2=k^2=ijk=-1\). For any nonzero complex-valued function \(f\) on \(Q_8\), let \(L_f\) be the left-convolution operator on \(\mathbb C[Q_8]\). Among the four central antipodal pairs \(\{\pm1\},\{\pm i\},\{\pm j\},\{\pm k\}\), let \(a\) pairs contain exactly one point of \(\operatorname{supp}f\), and let \(b\) pairs contain both points. The possible values of \(\operatorname{rank}_{\mathbb C}L_f\), on **each specified support** with those occupancies, are exactly as follows.

| \(a\) singletons | \(b\) doubled pairs | Support size | Number of specified supports | Attainable convolution ranks |
|---:|---:|---:|---:|---|
| 1 | 0 | 1 | 8 | 8 |
| 2 | 0 | 2 | 24 | 6, 8 |
| 0 | 1 | 2 | 4 | 4, 8 |
| 3 | 0 | 3 | 32 | 5, 6, 7, 8 |
| 1 | 1 | 3 | 24 | 4, 6, 8 |
| 4 | 0 | 4 | 16 | 4, 5, 6, 7, 8 |
| 2 | 1 | 4 | 48 | 4, 5, 6, 7, 8 |
| 0 | 2 | 4 | 6 | 2, 4, 6, 8 |
| 3 | 1 | 5 | 32 | 3, 4, 5, 6, 7, 8 |
| 1 | 2 | 5 | 24 | 4, 5, 6, 7, 8 |
| 2 | 2 | 6 | 24 | 3, 4, 5, 6, 7, 8 |
| 0 | 3 | 6 | 4 | 2, 3, 4, 5, 6, 7, 8 |
| 1 | 3 | 7 | 8 | 3, 4, 5, 6, 7, 8 |
| 0 | 4 | 8 | 1 | 1, 2, 3, 4, 5, 6, 7, 8 |

The fourteen rows partition **all 255 nonempty supports**. Every listed rank is achieved by some function nonzero at every point of the specified support, and no unlisted rank occurs. For example, a four-point support made of two whole antipodal pairs admits only even ranks \(2,4,6,8\), whereas a four-point support consisting of one whole pair and two singleton pairs admits every rank \(4,5,6,7,8\). At support size six, three whole pairs permit rank \(2\), while two whole pairs together with two singletons do not.

## Assumptions and scope
The coefficients of \(f\) range over \(\mathbb C\), with no positivity, reality, unit-modulus or equality-of-coefficients condition. A support is *exact*: every designated coefficient is nonzero and every undesignated coefficient vanishes. Convolution is \((L_fh)(x)=\sum_{g\in Q_8}f(g)h(g^{-1}x)\); using the opposite regular-convolution convention does not change its rank. There are four one-dimensional irreducible representations factoring through \(Q_8/\{\pm1\}\cong\mathbb F_2^2\), and one irreducible representation of dimension two. The rank under study equals the rank-weighted nonabelian Fourier support, not merely the number of nonzero irreducible blocks. An empty support is excluded.

## Proof
**1. Exact Fourier-block formula.** Write \(u_0=1,u_1=i,u_2=j,u_3=k\), and set \(s_t=f(u_t)+f(-u_t)\), \(d_t=f(u_t)-f(-u_t)\). The four one-dimensional Fourier blocks are the entries of \(Hs\), where
\[
H=\begin{pmatrix}1&1&1&1\\1&1&-1&-1\\1&-1&1&-1\\1&-1&-1&1\end{pmatrix}.
\]
One choice of the two-dimensional quaternion representation gives the remaining Fourier block
\[
M(d)=\begin{pmatrix}d_0+\mathrm i d_1&d_2+\mathrm i d_3\\-d_2+\mathrm i d_3&d_0-\mathrm i d_1\end{pmatrix},\qquad
\det M(d)=d_0^2+d_1^2+d_2^2+d_3^2.
\]
The regular representation contains the two-dimensional irreducible with multiplicity two. Consequently, with \(K(s)=|\{t:(Hs)_t\ne0\}|\),
\[
\operatorname{rank}L_f=K(s)+2r(d),\qquad
r(d)=\begin{cases}0&d=0,\\1&d\ne0,\ \sum_td_t^2=0,\\2&\sum_td_t^2\ne0.\end{cases}
\]
This holds for every complex coefficient vector; no numeric approximation enters the formula.

**2. Exact-support constraints and scalar Fourier possibilities.** On an empty antipodal pair \((s_t,d_t)=(0,0)\). On a singleton pair \(s_t\ne0\) and \(d_t=\pm s_t\). On a doubled pair the only restriction is \(s_t\ne d_t\) and \(s_t\ne-d_t\); either \(s_t=0\) or \(d_t=0\) is allowed. For a vector \(s\) with exactly \(j\) nonzero coordinates, the possible values of \(K(s)\) are exactly
\[
\mathcal K_0=\{0\},\quad\mathcal K_1=\{4\},\quad\mathcal K_2=\{2,4\},\quad\mathcal K_3=\{3,4\},\quad\mathcal K_4=\{1,2,3,4\}.
\]
For two nonzero coordinates the Walsh coefficients are two copies each of their sum and difference. Three nonzero coordinates cannot have two Walsh zeros: a vector supported on only two Walsh characters has either two or four nonzero physical coordinates. With four physical coordinates, four possible Walsh-support sizes are realized by choosing Walsh coordinates with respectively one, two, three or four nonzero entries, avoiding the finitely many hyperplanes that would force a physical zero. The zero and one-coordinate cases are immediate. Concrete representatives for \(j=0,1,2,3,4\), with every permissible \(K\), appear in the exact witness generator. Every permutation of the four coordinates preserves the Walsh zero count, because the affine group of \(\mathbb F_2^2\) is the full symmetric group on its four elements, acting as signed row permutations on \(H\).

**3. Exclusions for the two-dimensional block.** Put \(a\) singleton and \(b\) doubled pairs into canonical positions. Since every singleton has \(d_t\ne0\), the case \(r=0\) requires \(a=0\); then all \(b\) doubled pairs must have \(s_t\ne0\) and \(K\in\mathcal K_b\). If \(a=0,b=1\), a nonzero \(d\) has one nonzero coordinate and cannot be isotropic, so \(r=1\) is impossible. If \(b=0\), the condition \(r=1\) is \(\sum_{t=0}^{a-1}s_t^2=0\) with every \(s_t\ne0\). It yields no solution for \(a=1\), only \(K=4\) for \(a=2\), precisely \(K=3,4\) for \(a=3\), and precisely \(K=2,3,4\) for \(a=4\). In the last case \(K=1\) is impossible because a nonzero scalar multiple of a Walsh character has four equal squares and hence nonzero square sum. All remaining theoretical possibilities are \(r=1,2\) with \(K\in\bigcup_{j=a}^{a+b}\mathcal K_j\) when \(b\ge1\), and \(r=2\) with \(K\in\mathcal K_a\) when \(b=0\). Summing \(K+2r\) gives precisely the candidate ranks displayed in the table.

**4. Exhaustive existence constructions.** Every scalar \(K\) needed in the preceding paragraph admits a real nonnegative \(s\), strictly positive at singleton positions, with every nonzero entry drawn from \(\{1,2,3,4,5,8\}\). For the first \(j\) occupied scalar coordinates, witnesses are: \(j=1\), \((1)\); \(j=2\), \((1,1)\) or \((1,2)\); \(j=3\), \((1,1,2)\) or \((1,1,1)\); \(j=4\), \((1,1,1,1)\), \((1,1,2,2)\), \((1,2,3,4)\), or \((1,2,4,8)\), with respectively one through four nonzero Walsh coefficients where applicable. Unused doubled positions take scalar value zero.

For \(r=2\), choose \(d_t=s_t\) at singleton positions and \(d_t=20\) at doubled positions; the determinant is nonzero and the full support is preserved. For \(r=0\) take \(d=0\), which is allowed only in the case already identified. If \(b=1\) and \(a\ge1\), choose the doubled-pair difference \(d=\mathrm i\sqrt{\sum_{\mathrm{single}}s_t^2}\); it yields \(r=1\), and it cannot equal either real doubled-pair scalar value or its negative. If \(b\ge2\), give the first \(b-1\) doubled positions difference \(7\), and the last difference \(\mathrm i\sqrt{\sum_{\mathrm{single}}s_t^2+49(b-1)}\). These differences satisfy the isotropy equation, never equal the corresponding scalar or its negative, and are not all zero. Hence every allowed \(r=1\) case with doubled pairs is realized.

For \(b=0\), the exceptional \(r=1\) witnesses are \(s=(1,\mathrm i)\) when \(a=2\), and \(s=(1,\omega,\omega^2)\), \(s=(1,1,\mathrm i\sqrt2)\) when \(a=3\), with \(\omega^2+\omega+1=0\) and \(\omega\ne1\). For \(a=4\), set \(s=H\lambda/4\) for \(\lambda=(1,\mathrm i,0,0)\), \((3,4,5\mathrm i,0)\), \((3,4,3\mathrm i,4\mathrm i)\); these yield respectively \(K=2,3,4\), have four nonzero coordinates, and satisfy \(\sum s_t^2=0\). Together with real representatives for \(r=2\), these exhaust all allowed triples \((a,b,\operatorname{rank}L_f)\). The finite certificate gives an explicit exact-algebraic witness for each of the 64 row-rank entries.

**5. Every specified support and exact count.** Any sign choice in a singleton pair changes only the sign of the corresponding \(d_t\), leaving the square sum unchanged. Any permutation of antipodal pairs preserves \(K(s)\), while permutation or sign reversal of differences preserves the determinant. Thus the canonical witnesses transport to every fixed support with the same \((a,b)\). Each occupancy row has exactly \(\frac{4!}{a!b!(4-a-b)!}2^a\) specified supports, whose counts sum to \(4^4-1=255\). This proves both attainment and impossibility on every fixed support.

## Verification
The reproducible package includes `quaternion_witnesses.json` (64 symbolic witnesses), `verify_quaternion_construction.py` (a standalone symbolic construction and determinant check) and `verify_quaternion_regular.py` (an independent, group-multiplication-based exact regular-matrix rank check). Execute both scripts in the directory containing the witness file after installing the versioned requirement in `requirements.txt`. The second program checks every listed rank on every one of the 255 nonempty supports, making 1,148 exact regular-matrix rank comparisons; it also verifies all 24 coordinate permutations of the Walsh block. The first verifies the determinant identity and exact-support inequalities and regenerates the stored 64 witness records. The recorded output is in `verification_output.txt`.

The scripts certify the finite realizations and symbolic identities they explicitly test. The impossibility of unlisted ranks is proved by the representation-theoretic block formula and the exhaustive scalar-support and quadratic cases above, **not** by absence from a finite search.

## Relationship to prior work
Alagic and Russell's 2006 nonabelian uncertainty theorem gives \(|\operatorname{supp}f|\operatorname{rank}L_f\ge8\) in this case, but not the occupancy-resolved lists or the attainable intermediate ranks. Stanković, Moraga and Astola (2001) give the explicit irreducible Fourier matrices of \(Q_8\), including the transform needed for the first proof step, but do not provide this complete support-rank classification. The published spinor coefficient zero-set theorem for binary polyhedral groups already covers certain rank-two cases inside the defining two-dimensional block (including the quaternion group); those particular support possibilities are not asserted to be individually new. Other exact Fourier-rank classifications for \(S_3\) and odd dihedral groups concern different support geometries and do not logically imply this fourteen-row table.

The contribution claimed here is the **full 255-support, fourteen-occupancy, all-coefficient, all-rank classification** with universal fixed-support realizability. Searches of indexed research and related records found no explicit equivalent table; this is a bounded originality assessment, not a guarantee that no earlier unindexed computation exists.

## Limitations
The classification is for the single group \(Q_8\) and arbitrary complex coefficients. It does not address real or positive weights, optimal condition numbers, larger quaternion groups or the full set of singular values. The many previously known special implications of Fourier uncertainty and rank-one coefficient theory remain prior art. Equivalence with an unindexed classical quaternion-convolution calculation is a residual priority risk. The accompanying exact tests have not been independently audited.

## References
1. G. Alagic and A. Russell, *Uncertainty Principles for Compact Groups*, arXiv:math/0608702, first publicly submitted 28 August 2006, https://arxiv.org/abs/math/0608702 .
2. R. S. Stanković, C. Moraga and J. Astola, *From Fourier Expansions to Arithmetic-Haar Expressions on Quaternion Groups*, Applicable Algebra in Engineering, Communication and Computing 12 (2001), 227–253, full text: https://web.cecs.pdx.edu/~mperkows/CAPSTONES/Quaternion/fuxcxlltext.pdf .
3. *Spinor coefficient zero sets and projective rigidity across finite binary polyhedral groups*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-spinor-coefficient-zero-sets-and-projective-rigidity-across-fini--502b53e637a6 .
4. *Complete three-tap Fourier-rank spectrum on odd-prime dihedral groups*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-complete-three-tap-fourier-rank-spectrum-on-odd-prime-dihedral-g--eb09d9b17153 .
