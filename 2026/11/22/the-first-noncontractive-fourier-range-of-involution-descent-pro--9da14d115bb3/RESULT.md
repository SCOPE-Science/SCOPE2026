# The first noncontractive Fourier range of involution descent profiles

## Finding

Let \(\mathcal I_n\) denote all involutions of \(\{1,\ldots,n\}\), including those with fixed points, and let \(G_n=(\mathbb F_2)^{n-1}\). Count each involution at the binary vector of its descent positions, and define convolution \(T_n\) by that multiplicity function. For every \(1\le n\le8\), the dimension of the Fourier-visible range and the **sharp minimum** real or complex \(\ell^1\)- and \(\ell^\infty\)-operator norms of projections onto it are

| \(n\) | \(\operatorname{rank} T_n\) | number of coordinates in the function space \(\mathbb C^{G_n}\) | minimum projection norm |
|---|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 2 | 1 | 2 | 1 |
| 3 | 1 | 4 | 1 |
| 4 | 4 | 8 | 1 |
| 5 | 8 | 16 | 1 |
| 6 | 16 | 32 | 1 |
| 7 | 28 | 64 | \(9/4\) |
| 8 | 64 | 128 | 1 |

In particular, order seven is the **first failure of contractive range projection**, followed by recovery of contractivity at order eight. At order seven there are exactly four even-cardinality Walsh zeros beyond the 32 odd-cardinality symmetry zeros. With bits numbered from zero at descent position one, their integer masks are \(43,45,53,63\), corresponding respectively to
\[\{1,2,4,6\},\quad\{1,3,4,6\},\quad\{1,3,5,6\},\quad\{1,2,3,4,5,6\}.\]
The smallest nonzero absolute Walsh multiplier at this order is exactly \(8\), so the sharp \(\ell^2\) pseudoinverse norm is \(1/8\).

## Assumptions and scope

For each \(n\ge1\) and \(\pi\in\mathcal I_n\), write \(d(\pi)\in G_n\) with \(d_i(\pi)=1\) exactly when \(\pi(i)>\pi(i+1)\). Define \(f_n(x)=|\{\pi:d(\pi)=x\}|\) and \((T_nu)(x)=\sum_{y\in G_n}f_n(y)u(x+y)\). Use unnormalized Walsh characters \(\chi_s(x)=(-1)^{s\cdot x}\), so \(\Lambda_n(s)=\sum_{\pi\in\mathcal I_n}\chi_s(d(\pi))\) is the eigenvalue of \(T_n\) at \(s\). All spaces, norms and projections are unweighted finite-dimensional counting-measure spaces. A projection need not commute with translations. No assertion about all \(n>8\) is made.

## Proof

**Complement symmetry.** The classical Robinson--Schensted correspondence maps involutions bijectively to standard Young tableaux preserving the descent set. Transposing a tableau replaces each descent position by its complement in \(\{1,\ldots,n-1\}\). Thus \(f_n(x)=f_n(x+\mathbf1)\). For every odd-weight character \(s\), replacing \(x\) by \(x+\mathbf1\) in the Fourier sum gives \(\Lambda_n(s)=-\Lambda_n(s)=0\). This step is classical, not a new claim.

**Exhaustive exact spectra through order eight.** Each involution is uniquely constructed by taking the smallest currently unmatched label and either fixing it or pairing it with one larger unmatched label. This partitions the involutions into disjoint recursive branches, leaving no missing cases or multiplicities. For \(1\le n\le8\), count each branch's exact descent mask; transform the resulting integer histogram by the butterfly identity \((a,b)\mapsto(a+b,a-b)\). The accompanying `verify.py` implements this complete recursion, and separately counts the same histograms by adding the next cell to every addable corner of a Young diagram, recording a descent when the next label lies in a lower row. The two independent enumerations agree, and their Fourier data yield exactly the ranks in the table. At \(n=3\), every descent mask occurs once, so only the constant character survives. For \(n=1,2,4,5,6,8\) the nonzero Fourier support is precisely the even-weight characters. At \(n=7\), the entire 64-entry spectrum is supplied in `spectrum_n7.tsv` and verified by both exact character summation and the integer transform. Its even-character zeros are exactly \(E=\{43,45,53,63\}\), and all other 28 even-character coefficients are nonzero; their least absolute magnitude is \(8\). This is a finite exhaustive certificate, not a claim from sample tests.

**Sharp endpoint projection bound.** For any finite abelian group and translation-invariant subspace \(R\), translate-conjugate an arbitrary projection \(Q\) onto \(R\) and average over the group. The resulting map remains a projection onto \(R\), and its \(\ell^1\)- and \(\ell^\infty\)-norms do not exceed those of \(Q\). A translation-invariant projection with range \(R\) is unique: its Fourier multiplier is the indicator of the active characters. Thus the canonical Fourier projection minimizes either endpoint norm among *all* real or complex projections onto the range.

If the active characters are all even-weight characters, this canonical projector is \(P u(x)=[u(x)+u(x+\mathbf1)]/2\), a norm-one projection. At \(n=3\), it instead projects onto constants by group averaging, again norm one. At \(n=7\), the projector kernel is
\[p(x)=\frac12(\mathbf1_{x=0}+\mathbf1_{x=\mathbf1})-\frac1{64}\sum_{s\in E}\chi_s(x).\]
The four masks in \(E\) are linearly independent over \(\mathbb F_2\) (their restrictions to the first four coordinates have full rank). Therefore their four-character sign vectors each occur exactly four times as \(x\) ranges over \(G_7\). In particular, the numerator \(64p(x)\) has multiplicities \(28\) twice, \(4\) four times, \(-4\) twice, \(2\) sixteen times, \(-2\) sixteen times, and \(0\) twenty-four times. Consequently
\[\|P\|_{1\to1}=\|P\|_{\infty\to\infty}=\sum_x|p(x)|=\frac{144}{64}=\frac94.\]
This is globally optimal by the averaging argument. Finally, Walsh diagonalization gives \(\|T_7^+\|_{2\to2}=1/8\), since the smallest surviving multiplier magnitude is \(8\).

## Verification

Run `python verify.py` alongside `spectrum_n7.tsv` using Python 3.9 or later. The verifier performs 2,429 exact integer comparisons/assertions. It constructs involutions directly and standard tableaux independently for all orders through ten, checks the classical involution totals, compares direct character sums for orders through seven, verifies the 64-entry order-seven certificate, exhaustively determines the zero sets through order eight, checks rank and endpoint norms and verifies linear independence of the four extra zeros. Every arithmetic operation determining a reported theorem value is integer-exact; the projection formula is also proved above, not merely tested.

## Relationship to prior work

Barnabei--Bonetti--Silimbani (2007, arXiv:0704.3509) developed involution descent enumeration and its tableau symmetry. Chow (2008, DOI:10.37236/795) established the exact **prescribed descent-set counts for every order**, including a tableau/Kostka expression and complementary symmetry. The entire input distribution \(f_n\), as opposed to its new spectral/operator invariant, is therefore pre-existing mathematics. Barnabei--Bonetti--Elizalde--Silimbani (2014, arXiv:1401.3011) give a related descent-set refinement for **321-avoiding** involutions, a different subfamily. The results here add the exact first noncontractive Fourier support geometry, the rank sequence at the transition, and the globally optimal endpoint range-projection norm. These do not appear as claims in the inspected sources; they are computable consequences of known enumeration after a distinct Fourier and projection analysis. An equivalent older functional interpretation remains a priority risk.

## Limitations

The sharp spectral statements are proved only for \(1\le n\le8\); no eventual periodicity or classification at arbitrary order is asserted. The certificate's all-case logic is elementary finite recursion and the independent tableau check, not a formal proof assistant. Classical descent-set formulas are prior work, not claimed as new. The rank and projection result has had no independent external audit.

## References

1. M. Barnabei, F. Bonetti and M. Silimbani, *The descent statistic on involutions is not log-concave*, first arXiv submission 2007-04-26, https://arxiv.org/abs/0704.3509.
2. C.-O. Chow, *On the Eulerian Enumeration of Involutions*, Electronic Journal of Combinatorics **15** (2008), R71, https://doi.org/10.37236/795, full text https://www.combinatorics.org/ojs/index.php/eljc/article/download/v15i1r71/pdf/.
3. M. Barnabei, F. Bonetti, S. Elizalde and M. Silimbani, *Descent sets on 321-avoiding involutions and hook decompositions of partitions*, arXiv:1401.3011, https://arxiv.org/abs/1401.3011.
4. M. Barnabei, F. Bonetti and M. Silimbani, *The signed Eulerian numbers on involutions*, arXiv:0803.2126, https://arxiv.org/abs/0803.2126.
