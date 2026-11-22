# The first unexpected Fourier nullspace of classical parking functions

## Finding

For each integer \(1\le n\le5\), let \(m=n+1\), \(G_n=(\mathbb Z/m\mathbb Z)^n\), and \(P_n\subset G_n\) be the **zero-based classical parking functions**: vectors \(a=(a_1,\ldots,a_n)\in\{0,\ldots,n-1\}^n\) whose nondecreasing rearrangement \(b_0,\ldots,b_{n-1}\) satisfies \(b_i\le i\) for every \(0\le i<n\). Put \(f_n=1_{P_n}\), and let \(T_nh=f_n*h\) be unnormalized convolution on complex functions on \(G_n\). Its Fourier multiplier at \(u\in G_n\) is
\[
\widehat f_n(u)=\sum_{a\in P_n}\exp\!\left(\frac{2\pi i}{m}\sum_{j=1}^n u_ja_j\right).
\]
Define the *forced zero set* \(Z_n^{\mathrm{forced}}=\{u\in G_n:\sum_j u_j=0\pmod m,\ u\ne0\}\).

**Theorem.** Every \(Z_n^{\mathrm{forced}}\) is contained in the Fourier zero set for every \(n\ge1\), with exactly \(m^{n-1}-1\) forced zeros. For \(1\le n\le4\), these are **all** the zeros. At \(n=5\), precisely 360 additional zeros occur: the coordinate-multiset of an additional zero is exactly one of
\[
(1,2,3,3,4),\quad(1,2,3,3,5),\quad(1,2,3,4,5),\quad
(1,3,3,4,5),\quad(2,3,3,4,5).
\]
The five coordinate-permutation orbit sizes are respectively \(60,60,120,60,60\), and no other nonforced zeros occur. Consequently
\[
\operatorname{rank}(T_5)=6121,\qquad\operatorname{nullity}(T_5)=1655.
\]
For \(1\le n\le4\), the exact ranks are \(m^n-m^{n-1}+1\), equal to \(2,7,49,501\), respectively. Thus five cars and the six-element cyclic alphabet constitute the first size at which the classical diagonal-transversal Fourier zeros are not exhaustive.

## Assumptions and scope

All groups are finite abelian, Fourier transforms are unnormalized, convolution acts on the entire complex group algebra, and ranks and nullities are over \(\mathbb C\). Coordinate residues and the displayed exceptional multisets use representatives \(0,\ldots,m-1\). The asserted complete zero-set classification is only for \(1\le n\le5\); there is **no** assertion that primality or prime-power status of \(n+1\) characterizes Fourier support at larger sizes. The universal forced-zero inclusion holds for all positive integers \(n\).

## Proof

**1. Forced zeros.** Write \(H=\{(t,\ldots,t):t\in\mathbb Z/m\mathbb Z\}\). Pollak's classical circular-parking argument says that \(P_n\) contains exactly one representative of each of the \(m^{n-1}\) cosets of \(H\) in \(G_n\). If \(\sum_j u_j=0\pmod m\), the character \(a\mapsto\exp(2\pi i\langle u,a\rangle/m)\) is constant on every coset of \(H\). Its sum over \(P_n\) is then the full character sum over \(G_n/H\), zero for every nontrivial character. The only trivial character in the annihilator is \(u=0\), with multiplier \(|P_n|=m^{n-1}>0\). This proves the all-size inclusion and its exact count.

**2. Symmetry and an exact cyclotomic test.** Since the parking inequalities depend only on the sorted coordinate values, \(P_n\) is invariant under all coordinate permutations, so the multiplier depends only on the sorted multiset of \(u\). Each multiset has orbit size \(n!/\prod_r c_r!\), where \(c_r\) is the multiplicity of residue \(r\). For fixed \(u\), put
\[
C_r(u)=\#\{a\in P_n:\langle u,a\rangle\equiv r\pmod m\},\qquad 0\le r<m.
\]
Then \(\widehat f_n(u)=\sum_{r=0}^{m-1} C_r(u)\zeta_m^r\). Since \(\zeta_m\) has minimal polynomial \(\Phi_m\) over \(\mathbb Q\), the multiplier vanishes **if and only if** the integer polynomial \(\sum_r C_r(u)X^r\) has zero remainder on division by \(\Phi_m(X)\). No floating-point approximation is involved. For \(m=3,4,5,6\), respectively, the exact monic cyclotomic polynomials are \(1+X+X^2\), \(1+X^2\), \(1+X+X^2+X^3+X^4\), and \(1-X+X^2\).

**3. Exhaustive finite classification.** The accompanying standalone `verify.py` implements the definition of \(P_n\), enumerates **every** sorted frequency multiset for each \(n=2,3,4,5\), computes every \(C_r(u)\) with integers, divides by the appropriate cyclotomic polynomial using exact monic polynomial division, and weights each tested orbit by the multinomial orbit size. There are \(\binom{10}{5}=252\) multiset orbits at \(n=5\), covering all \(6^5=7776\) characters. The exact test finds 1295 forced zeros and only the five additional multisets displayed in the theorem; the extra orbit sizes add to 360. For \(n=2,3,4\), no additional orbit passes the test. For \(n=1\), \(P_1=\{(0)\}\), so both Fourier coefficients are one and there are no zeros. These finite loops exhaust the specified finite universe; no extrapolation from the checked sizes is used.

**4. Rank.** Fourier characters diagonalize complex convolution on \(G_n\), so rank equals the number of nonzero multipliers. At five cars this gives \(6^5-(6^4-1)-360=6121\), and the nullity is \((6^4-1)+360=1655\). The smaller ranks follow in the same way. This proves every part of the theorem.

## Verification

Execute `python3 verify.py` with Python 3 and no third-party packages. The program independently checks the sorted-inequality definition against sequential parking simulation for every preference vector through five cars, checks the Pollak diagonal-transversal property, and exhaustively evaluates all sorted Fourier-character orbits by integer cyclotomic division. Its expected final line is `ALL EXACT CHECKS PASSED`; the complete expected output is recorded in `verification_output.txt`. The n=5 certificate is an exhaustive finite proof for exactly five cars, not an infinite-size assertion.

## Relationship to prior work

Richard P. Stanley, *Parking Functions and Noncrossing Partitions* (first public 12 November 1996), explicitly records Pollak's diagonal-coset transversal property in Section 2. This **already implies** the universal forced-zero inclusion; neither the Pollak lemma nor the resulting baseline nullity is claimed new. Stanley's Frobenius characteristic concerns the symmetric-group action on parking functions and does not state the full additive-character spectrum at the six-element modulus or the five exceptional frequency orbits. General cyclotomic divisibility is classical. The asserted finite finding is precisely the extra 360 zeros, their complete five-orbit classification, and the resulting first strict rank loss. Distinct published work on perturbed prime-power cyclic transversals and on farthest-available parking orders uses different underlying sets/operators and does not imply the displayed preference-vector spectrum.

## Limitations

This is an exactly verified small-size cutoff and a universal *forced* inclusion, **not** a theorem classifying all larger parking-function transforms. No claim is made of a new general cyclotomic lemma, a new Pollak theorem, an optimal condition number, or an independent scientific audit. A differently phrased historic root-of-unity specialization of the full multivariate parking-function enumerator may contain the same finite result; the accessible comparisons do not eliminate that priority risk. The verification program is part of the proof for the bounded case and is supplied in full.

## References

1. R. P. Stanley, *Parking Functions and Noncrossing Partitions*, *Electronic Journal of Combinatorics* 3 (1996), R20, submitted 12 August 1996, accepted/published 12 November 1996, Section 2 (Pollak's transversal lemma), https://math.mit.edu/~rstan/papers/nc.pdf and https://doi.org/10.37236/1335.
2. H. O. Pollak's circular-parking argument, credited and formulated explicitly in Stanley (1996), Section 2; the original argument is not re-claimed here.
3. P. Diaconis and A. Hicks, *Probabilizing Parking Functions*, arXiv:1611.09821 (first public 29 November 2016), later *Advances in Applied Mathematics* 89 (2017), 125–155, https://arxiv.org/abs/1611.09821 (supporting context; not an archival-date anchor).
