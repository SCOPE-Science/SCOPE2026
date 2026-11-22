# Rank-two coset rigidity for finite Fourier restrictions and a semiprime incidence law

## Finding
Let \(G\) be any finite abelian group, with character group \(\widehat G\). For nonempty sets \(R\subset G\) and \(C\subset\widehat G\), form the unnormalized complex Fourier restriction
\[
F[R,C]=(\chi(r))_{r\in R,\,\chi\in C}.
\]
Define two annihilator subgroups
\[
H_C=\{g\in G: \chi(g)=\psi(g)\text{ for all }\chi,\psi\in C\},
\qquad
K_R=\{\eta\in\widehat G:\eta(r)=\eta(s)\text{ for all }r,s\in R\}.
\]
Let \(a=|\{r+H_C:r\in R\}|\) and \(b=|\{\chi K_R:\chi\in C\}|\). The exact rank-two rigidity theorem is
\[
\boxed{\min\{3,\operatorname{rank}_{\mathbb C}F[R,C]\}=\min\{3,a,b\}.}
\]
Thus, for any rectangular restriction, rank at most two occurs **if and only if** the selected rows occupy at most two \(H_C\)-cosets or the selected columns occupy at most two \(K_R\)-cosets. There are no additional accidental rank-two dependencies.

**Infinite-family consequence.** Let \(p\ge5\) be prime and \(N=3p\). Among all ordered choices of an unordered four-point row set and an unordered four-point column set of the cyclic Fourier matrix
\[
F_N=(\exp(2\pi irc/N))_{0\le r,c<N},
\]
there are no rank-one restrictions, and the exact number of rank-two restrictions is
\[
\boxed{90\binom p4\binom p2.}
\]
Such a restriction has rank two precisely when, after possibly interchanging rows and columns, one four-point set lies wholly in one residue class modulo three and the other meets exactly two residue classes modulo \(p\). For \(p=5\) this gives \(4500\) and for \(p=7\) it gives \(66150\); these finite checks are not substitutes for the general proof.

## Assumptions and scope
All groups are finite and abelian; all matrix ranks are over \(\mathbb C\). The selected row and character sets are nonempty and contain distinct indices. A row and column index set is unordered, while an ordered pair of such sets distinguishes the row and column roles. Characters have unit complex modulus. Multiplying the full Fourier matrix by a common nonzero scalar cannot change the claims. The statement determines rank exactly when it is at most two; when the right-hand minimum is three it claims only that the true rank is at least three, not that it equals three.

For cyclic \(G=\mathbb Z/N\mathbb Z\), the subgroups and cosets can be computed by integer gcds: with row representatives \(r_0\) and column representatives \(c_0\), define \(d_R=\gcd(N,\{r-r_0:r\in R\})\) and \(d_C=\gcd(N,\{c-c_0:c\in C\})\). Then \(a\) is the number of distinct row residues modulo \(N/d_C\), and \(b\) is the number of distinct column residues modulo \(N/d_R\).

## Proof
**Unit-modulus rank-two lemma.** Let \(M\) be an arbitrary complex matrix with every entry of modulus one and rank at most two. We claim that either its rows fall into at most two proportionality classes or its columns do. If the rank is one the assertion is immediate. Otherwise choose two independent rows \(u,v\). Set \(z_j=v_j/u_j\); every \(z_j\) lies on the complex unit circle.

If the \(z_j\) take at most two values, then every column vector has the form \(u_j w(z_j)\), where the vector \(w(z)\) has entries \(\alpha_i+\beta_i z\) expressing all rows as linear combinations of \(u,v\). Columns with equal \(z_j\) are proportional, so there are at most two column classes.

If at least three different \(z_j\) occur, take any row \(w=\alpha u+\beta v\). Since \(|w_j|=|u_j|=1\), all occurring \(z_j\) solve
\[
|\alpha|^2+|\beta|^2+2\operatorname{Re}(\overline\alpha\beta z_j)=1.
\]
If \(\overline\alpha\beta\ne0\), a nonconstant real affine functional on the unit circle equals a fixed real number at at most two points. This contradicts the three distinct \(z_j\). Hence \(\alpha\beta=0\) and every row is proportional either to \(u\) or to \(v\), completing the lemma.

**Character proportionality.** Two rows indexed by \(r,s\in R\) are proportional on the selected columns precisely when \(\chi(r-s)\) is constant as \(\chi\) varies in \(C\). This holds if and only if \(r-s\in H_C\), so row classes are exactly the cosets counted by \(a\). Dually, two selected columns \(\chi,\psi\) are proportional on \(R\) if and only if \(\chi\psi^{-1}\in K_R\), so column classes are exactly those counted by \(b\). If \(a\le2\) or \(b\le2\), the rank is at most two. Conversely the unit-modulus lemma forces this alternative whenever rank is at most two. If either class count is one, rank is one; otherwise both class counts are at least two and any restriction of rank at most two has rank exactly two. This proves the boxed minimum identity, including every possible rectangular size.

**Four-by-four semiprime classification.** Identify \(\mathbb Z/(3p)\mathbb Z\cong\mathbb Z/3\mathbb Z\times\mathbb Z/p\mathbb Z\). Four distinct elements cannot all have one fixed residue modulo \(p\), since each such fiber has only three elements. Consequently neither a four-row nor a four-column Fourier restriction can have rank one.

If \(C\) is not concentrated in one residue class modulo three, the differences in \(C\) generate both cyclic prime coordinates (because four distinct elements cannot share a single residue modulo \(p\)); thus \(H_C\) is trivial. If \(C\) *is* concentrated modulo three, \(H_C\) is the subgroup of order three, so \(a\) equals the number of residues modulo \(p\) represented in \(R\). The corresponding statements hold with rows and columns interchanged. The rank-two theorem therefore says that rank two occurs exactly when one set is pure modulo three and the other meets exactly two residue classes modulo \(p\). These alternatives are disjoint: if a four-set is pure modulo three, its four residues modulo \(p\) are necessarily distinct.

There are \(3\binom p4\) four-sets pure modulo three. For any two chosen residues modulo \(p\), a four-set using both of their three-point fibers has occupancy split \((1,3)\), \((2,2)\), or \((3,1)\). The number of choices is
\[
\binom31\binom33+\binom32^2+\binom33\binom31=3+9+3=15.
\]
Thus exactly \(15\binom p2\) four-sets use two residues modulo \(p\). Counting both disjoint row/column roles gives \(2\cdot3\binom p4\cdot15\binom p2=90\binom p4\binom p2\), as claimed. The proof is valid for every prime \(p\ge5\).

## Verification
Run `python3 CHECK.py` using Python 3 standard library. The companion output `CHECK_OUTPUT.txt` records an exhaustive order-six check of every \(3969\) nonempty rectangular restriction and an order-21 check compressed to the \(33\) affine orbits of four-point sets. The latter checks all \(1089\) ordered representative orbit pairs and recovers exactly \(66150\) rank-two cases, with no differences between the two modular ranks.

All computation is exact integer arithmetic. For order six, the single field prime \(1000000009\) exceeds \((6!)^{\varphi(6)}\). For order 21, the two distinct field primes \(1000000009\) and \(1000000093\), each congruent to one modulo 21, have product greater than \((4!)^{\varphi(21)}=24^{12}\). A nonzero \(k\)-minor of a Fourier matrix is a cyclotomic integer with nonzero integral norm, and every complex Galois conjugate of its determinant has modulus at most \(k!\). If a minor vanished in all chosen prime-field specializations, its norm would be divisible by the product of those distinct primes, contradicting the bound. Consequently these modular ranks are the exact complex ranks in the enumerated cases. Affine row/column changes preserve the complex rank, so the orbit compression is exhaustive. This computational corroboration does not prove the all-group theorem, whose proof is given above.

## Relationship to prior work
Tao's prime-order Fourier uncertainty theorem supplies Chebotarev's full-spark boundary, not composite-group rank-two coset classification. Meshulam's general finite-abelian uncertainty inequality gives support-size lower bounds but not the exact rank of each selected Fourier restriction. Krahmer–Pfander–Rashkov discuss subgroup-induced zero minors and give a small Fourier-rank table; their Section 3 does not state the rank-two equivalence for arbitrary rectangular restrictions. Delvaux–Van Barel's *Rank-deficient submatrices of Fourier matrices* constructs low-rank blocks and gives maximal-defect results for prime-power sizes; its inspected sections do not give the present unrestricted necessary-and-sufficient rank-two criterion.

An earlier published exact census of all order-fifteen four-point minors gives \(4500\) rank-two pairs, agreeing with the \(p=5\) consequence, but it does not classify rank-two cases for every odd semiprime or for arbitrary finite abelian groups. A published three-point census on \(\mathbb Z_{3p}\) gives the lower-order boundary using an already-known three-by-three unit-modulus rigidity lemma, but does not state the arbitrary-size rank-two rigidity theorem or count four-point restrictions for all primes. The 2007 paper by Delvaux and Van Barel on Kronecker products constructs subgroup-tiled deficient blocks and is a close historical comparison; its full text was not available in the inspected access routes, and an implicit stronger consequence remains an originality risk.

## Limitations
The theorem controls rank only through the threshold two; rank-three and higher defects require additional analysis. The semiprime counting formula is specific to the four-by-four restrictions at moduli \(3p\), with \(p\ge5\) prime. No Fourier singular-value bounds or condition numbers are claimed. Historical priority is qualified because unindexed equivalent derivations and an inaccessible plausible Kronecker-product text could contain the same rank-two insight. No finite computation is used as evidence for the theorem's universal quantifiers.

## References
1. T. Tao, *An uncertainty principle for cyclic groups of prime order*, first posted 2003-08-29, arXiv:math/0308286, https://arxiv.org/abs/math/0308286.
2. R. Meshulam, *An uncertainty inequality for finite abelian groups*, first posted 2003-12-22, arXiv:math/0312407, https://arxiv.org/abs/math/0312407.
3. F. Krahmer, G. E. Pfander, and P. Rashkov, *Uncertainty in time–frequency representations on finite Abelian groups and applications*, first posted 2006-11-16, arXiv:math/0611493, https://arxiv.org/abs/math/0611493.
4. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Fourier matrices*, KU Leuven report TW470 (September 2006), Linear Algebra Appl. 429 (2008), 1587–1605, DOI:10.1016/j.laa.2008.04.043.
5. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, report TW477 (November 2006), Linear Algebra Appl. 426 (2007), 349–367, DOI:10.1016/j.laa.2007.05.009.
6. *Complete rank-incidence census for four-frequency Fourier sampling on the cyclic group of order fifteen*, public mathematical finding (2026-11-01), identifier `6d1752cd1bea`.
7. *Complete third-order Fourier-minor rank incidence for distinct-prime cyclic products*, public mathematical finding (2026-11-08), identifier `6a97dfb3d140`.
8. *Exact rank spectrum of three-by-three Fourier minors on \(\mathbb Z_{3p}\)*, public mathematical finding (2026-10-18), identifier `0290eba11adf`.
