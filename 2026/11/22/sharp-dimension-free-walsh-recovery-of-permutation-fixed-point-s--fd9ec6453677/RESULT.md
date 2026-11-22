# Sharp dimension-free Walsh recovery of permutation fixed-point sets

## Finding

For each integer \(n\ge1\), let \(\mathfrak S_n\) be the permutations of \([n]\), let \(F(\pi)=\{i\in[n]:\pi(i)=i\}\), and form the probability mass on \(H_n=(\mathbb Z/2\mathbb Z)^n\)
\[
 p_n(x)=\frac{1}{n!}\#\{\pi\in\mathfrak S_n:F(\pi)=\operatorname{supp}(x)\}.
\]
Let \(T_n\) be convolution by \(p_n\) on real or complex \(\ell^2(H_n)\). Then \(T_n\) is singular **exactly at \(n=2\)**, where its rank is \(2\) and nullity is \(2\); it is indefinite and invertible at \(n=1,3\), and **strictly positive definite for every \(n\ge4\)**. For \(n=1,3\), its negative inertia is exactly one; for \(n\ge4\), no Fourier eigenvalue is negative or zero.

For \(n\ge4\), the sharp normalized spectral gap and Euclidean condition number satisfy
\[
 \min_{A\subseteq[n]}\widehat p_n(A)=\begin{cases}
 \frac16,&n=4,\\
 S_n:=\displaystyle\sum_{j=0}^n\frac{(-2)^j}{j!},&n\ge5,
 \end{cases}
 \qquad \kappa_2(T_n)=\frac{1}{\min_A\widehat p_n(A)}.
\]
Consequently, uniformly over every \(n\ge4\),
\[
 \boxed{\ \frac1{15}\le\widehat p_n(A)\le1\quad\text{for all }A\subseteq[n],\qquad
 \sup_{n\ge4}\kappa_2(T_n)=15\ },
\]
with equality at the lower bound **only** when \(n=5\) and \(A=[5]\). The condition numbers converge to \(e^2\), the odd-order subsequence strictly decreasing and the even subsequence increasing from order six.

## Assumptions and scope

The group operation on \(H_n\) is coordinatewise XOR. Normalized convolution is \((T_nh)(x)=\sum_{y\in H_n}p_n(y)h(x+y)\). Its unitary Walsh characters are \(\chi_A(x)=(-1)^{|A\cap\operatorname{supp}(x)|}\) for \(A\subseteq[n]\); normalization of the \(\ell^2\) inner product does not change the eigenvalues. All statements concern the **full labelled fixed-position set**, not merely the number of fixed points, a permutation matrix in \(n^2\) binary coordinates, or a central convolution on \(\mathfrak S_n\). We set \(D_0=1\) and \(D_1=0\) for derangement counts, so \(p_n(x)=D_{n-|\operatorname{supp}(x)|}/n!\). There is no randomness in the claims after the uniform counting measure is specified.

## Proof

**1. Exact Walsh diagonalization.** For any \(A\subseteq[n]\) with \(|A|=k\), multiply the fixed-point indicator signs:
\[
 n!\widehat p_n(A)=\sum_{\pi\in\mathfrak S_n}\prod_{i\in A}(1-2\mathbf1_{\{\pi(i)=i\}}).
\]
Expanding the product, for each \(J\subseteq A\), exactly \((n-|J|)!\) permutations fix all labels in \(J\). Hence the unnormalized multiplier \(L_{n,k}:=n!\widehat p_n(A)\) is
\[
 L_{n,k}=\sum_{j=0}^{k}\binom{k}{j}(-2)^j(n-j)!.
 \tag{1}
\]
It depends only on \(k\), with multiplicity \(\binom nk\). Pascal's identity gives the **exact adjacent-frequency recurrence**
\[
 L_{n,k}-L_{n,k+1}=2L_{n-1,k},\qquad 0\le k<n. \tag{2}
\]
At the full character, equation (1) simplifies to
\[
 L_{n,n}=n!S_n,\qquad S_n=\sum_{j=0}^{n}\frac{(-2)^j}{j!}. \tag{3}
\]

**2. Positivity and all exceptional orders.** The first four complete lists of \(L_{n,k}\), indexed by \(k=0,\ldots,n\), are
\[
 \begin{aligned}
 n=1:&\ (1,-1),\\
 n=2:&\ (2,0,2),\\
 n=3:&\ (6,2,2,-2),\\
 n=4:&\ (24,12,8,4,8).
 \end{aligned}
\]
This proves the stated small-dimensional inertia, rank, and the strict positivity at order four. If every \(L_{n-1,k}>0\) (as is true for \(n-1=4\)), equation (2) shows the entire row \(L_{n,0},\dots,L_{n,n}\) is strictly decreasing. Its final term \(n!S_n\) is positive for \(n\ge5\): the alternating-series sums satisfy
\[
 S_{2m+1}\ge S_5=\frac1{15}>0\quad(m\ge2),
 \qquad S_{2m}>e^{-2}>0\quad(m\ge2).
\]
Thus induction proves strict positivity and strict decreasing order for all \(n\ge5\), and their smallest eigenvalue is exactly \(S_n\). At order four, the smallest eigenvalue is \(4/24=1/6\). This establishes the complete rank and inertia classification and the sharp gaps.

**3. Sharp uniform conditioning.** The constant Walsh character has \(\widehat p_n(\varnothing)=1\). All other eigenvalues are positive and at most one for \(n\ge4\); therefore the \(\ell^2\) inverse operator norm and condition number are both the reciprocal of the smallest eigenvalue. For odd \(n\ge5\), consecutive odd truncations obey
\[
 S_{n+2}-S_n=\frac{2^{n+1}}{(n+1)!}\left(1-\frac{2}{n+2}\right)>0;
\]
for even \(n\ge4\), the same difference has the opposite sign. The odd sums increase from \(1/15\) toward \(e^{-2}\) and the even sums decrease toward \(e^{-2}\) from above. In particular \(S_n\ge1/15\) for all odd \(n\ge5\), and \(S_n>e^{-2}>1/9>1/15\) for even \(n\ge6\) (the elementary series bound \(e<3\) suffices). Together with the order-four gap \(1/6\), this proves the uniform lower bound \(1/15\), attained uniquely at \(n=5,k=5\). Its reciprocal \(15\) is the optimal global condition number. The two parity subsequences of condition numbers converge to \(e^2\) from opposite sides.

## Verification

Run `python3 verify_fixed_point_walsh.py` in Python 3 without nonstandard dependencies. The checker independently enumerates all permutations and exact fixed-position masks for \(1\le n\le8\), applies a fast Walsh–Hadamard transform to the count vector, and compares every resulting multiplier to equation (1). It then checks exact factorial and rational identities, exceptional orders, strict signs, recurrence (2), and the optimal bound for \(1\le n\le150\). All operations use arbitrary-precision integers or exact rational numbers. The all-order proof rests on equations (1)–(3) and the alternating-series argument; finite testing alone is not used as an infinite proof.

## Relationship to prior work

The rencontres/derangement distribution and the limiting Poisson law for fixed-point *counts* are classical, as surveyed by Diaconis, Fulman and Guralnick (2007). Diaconis, Evans and Graham (2013) establish the complete equality in distribution of the restricted fixed-position set and the unseparated-adjacency set. Harden and Penman (2013) study the fixed-point count polynomial, which also encodes the **full-character scalar** \(L_{n,n}\) on substituting \(-1\). These exact distributions and scalar identities are credited, not asserted new. A related published binary permutation-matrix self-sampling result uses central convolution on \(\mathfrak S_n\), with a distinct state space and representation-theoretic spectrum. The additional conclusion established here is the **complete Boolean incidence-convolution inertia and strict positivity transition, plus the sharp dimension-independent \(1/15\) spectral gap and optimal condition number \(15\)**. The claim is narrower than the pre-existing joint distribution in object, but has an additional nontrivial operator-inequality conclusion, not an enumeration claim. Absence of an explicitly equivalent published statement in inspected material does not certify absolute priority.

## Limitations

The theorem concerns uniform permutations, all fixed-position coordinates, and Hilbert-space conditioning; it gives no optimal \(\ell^1\)/\(\ell^\infty\) inverse bound or corresponding classification for other permutation distributions. It does not assert that the underlying exact fixed-set distribution is new. Historical-priority searches were bounded, and equivalent arguments could occur outside indexed literature. The numerical checks are finite corroboration; the induction and alternating-series inequalities prove the infinite statement.

## References

1. P. Diaconis, J. Fulman, R. Guralnick, *On Fixed Points of Permutations*, arXiv:0708.2643v1, first public 2007-08-20, https://arxiv.org/abs/0708.2643.
2. P. Diaconis, S. N. Evans, R. Graham, *Unseparated Pairs and Fixed Points in Random Permutations*, UC Berkeley Statistics Technical Report 822 (2013-08-01), https://statistics.berkeley.edu/sites/default/files/tech-reports/unseparated_pairs.pdf.
3. C. M. Harden, D. B. Penman, *Fixed Point Polynomials of Permutation Groups*, Electronic Journal of Combinatorics 20(2) P26 (2013), https://doi.org/10.37236/2955, lawful repository PDF https://repository.essex.ac.uk/6185/1/cmhpaper.pdf.
4. *An exact Specht resonance in binary Fourier sampling on permutation matrices*, published mathematical note, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-an-exact-specht-resonance-in-binary-fourier-sampling-on-permutat--aa53d61c75fb (distinct group and frequency space).
