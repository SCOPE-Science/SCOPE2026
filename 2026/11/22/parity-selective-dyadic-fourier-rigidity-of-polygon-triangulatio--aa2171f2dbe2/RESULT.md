# Parity-selective dyadic Fourier rigidity of polygon-triangulation ear profiles

## Finding

For \(n\ge5\), label the vertices of a convex polygon cyclically by \(\mathbb Z/n\mathbb Z\). The original-boundary ear-tip set \(E(T)\) of a triangulation \(T\) consists of the vertices \(i\) for which \((i-1,i,i+1)\) is a triangle in \(T\). For each frequency \(S\subseteq \mathbb Z/n\mathbb Z\), put
\[
 W_n(S)=\sum_T(-1)^{|S\cap E(T)|},\qquad v_n=s_2(n-1)-1=v_2(C_{n-2}),
\]
where \(s_2(a)\) counts the binary ones of \(a\) and \(C_j=\binom{2j}{j}/(j+1)\). Then:

* If \(n\) is odd, \(W_n(S)\equiv C_{n-2}\pmod{2^{v_n+1}}\) and \(v_2(W_n(S))=v_n\) for every \(S\). Counting convolution by the ear-profile multiplicities is invertible and its determinant has valuation \(2^n v_n\).
* If \(n\) is even, \(W_n(S)/2^{v_n}\equiv1+|S|\pmod 2\) for every \(S\). All even-cardinality frequencies are nonzero with exact valuation \(v_n\). The odd-cardinality frequencies are divisible by \(2^{v_n+1}\) and may vanish. The convolution rank is at least \(2^{n-1}\).

In both cases the greatest common divisor of the absolute coefficients is \(2^{v_n}\). The empty frequency attains the minimum **2-adic valuation**, since \(W_n(\varnothing)=C_{n-2}\); its absolute coefficient need not equal the gcd. For example, for \(n=5\) the empty coefficient is \(5\) and a singleton coefficient is \(1\). There are infinitely many odd sizes \(n=2^k+3\), \(k\ge2\), with an even Catalan count and invertible convolution; at \(n=2^k+7\), \(k\ge3\), the asserted odd-order modulus is eight rather than four.

## Assumptions and scope

Each triangulation is counted once, so a profile with several realizing triangulations is counted with multiplicity. For \(G=(\mathbb Z/2\mathbb Z)^n\), the kernel is \(f_n(x)=\#\{T:E(T)=x\}\) with a subset identified with its indicator. Convolution is on \(G\) with counting measure. Ears of recursively created subpolygons are not used. In even order the theorem does not classify singularity or claim that all odd-cardinality multipliers vanish.

## Proof

**Prescribed ears and signed sums.** Adjacent tips cannot both be ears because their diagonals cross. If \(I\) is a cyclically independent set of \(k\) tips, their prescribed ear triangles have nonoverlapping interiors. Cutting them off leaves the convex polygon on the other \(n-k\ge3\) vertices. Gluing back the ear triangles is a bijection between triangulations of that polygon and triangulations containing the specified ears, even if there are additional ears. The number with \(I\subseteq E(T)\) is \(C_{n-k-2}\). Expand each sign using \((-1)^{\mathbf 1_{i\in E(T)}}=1-2\mathbf 1_{i\in E(T)}\); with \(i_k(S)\) the number of independent \(k\)-subsets of \(S\), this gives
\[
 W_n(S)=\sum_{k=0}^{\lfloor n/2\rfloor} (-2)^k i_k(S) C_{n-k-2}.\tag{1}
\]
There is no independence restriction on \(S\). The first two terms are \(C_{n-2}-2|S|C_{n-3}\).

**Valuations.** The Catalan formula \(v_2(C_t)=s_2(t+1)-1\) follows from Legendre's factorial valuation formula. With \(N=n-1\), for \(k\ge2\) the valuation of \(2^kC_{n-k-2}\) is
\[
 k+s_2(N-k)-1\ge s_2(k)+s_2(N-k)\ge s_2(N)=v_n+1.
\]
Here \(k\ge s_2(k)+1\) for \(k\ge2\), and addition cannot increase the digit sum beyond the two summands' combined digit sums. Thus the higher terms vanish modulo \(2^{v_n+1}\). The valuation of \(2C_{n-3}\) is \(s_2(N-1)\). When \(n\) is odd, \(N\) is even and decrementing it does not decrease its digit sum; this kills the singleton term modulo \(2^{v_n+1}\) and proves the odd-order law. When \(n\) is even, \(N\) is odd and decrementing it removes exactly one binary one; the singleton prefactor has valuation \(v_n\). After dividing by \(2^{v_n}\), the constant and singleton terms reduce modulo two to \(1\) and \(|S|\), respectively.

**Excluding an odd common divisor.** Let \(A=\{1,n-1\}\). Given the two ears at \(A\), the possible additional tips are \(3,4,\ldots,n-3\), forming a path on \(L=n-5\) vertices (empty if \(n=5\)). Inclusion–exclusion over additional tips gives
\[
 f_n(A)=\sum_{r=0}^{\lfloor (L+1)/2\rfloor}(-1)^r\binom{L-r+1}{r}C_{L+1-r}
       =[z^{L+1}]C(z(1-z))=1.
\]
The binomial coefficient counts independent \(r\)-subsets of the path by subtracting \(0,1,\ldots,r-1\) from their increasing positions. In the coefficient extraction, the Catalan generating function is \(C(u)=\sum_j C_j u^j\); the identity \(C(z(1-z))=1/(1-z)\) follows by substituting \(u=z(1-z)\) in \(C(u)=1+uC(u)^2\) and using uniqueness of the formal solution with constant term one. Walsh inversion now gives
\[
 2^n=2^n f_n(A)=\sum_S (-1)^{|S\cap A|}W_n(S).
\]
Any common divisor divides \(2^n\); the empty-frequency valuation and the parity law therefore give exactly \(2^{v_n}\) as the gcd.

**Convolution.** The Walsh characters form a basis and diagonalize counting convolution by \(f_n\), with eigenvalues \(W_n(S)\). All \(2^n\) eigenvalues have valuation \(v_n\) in odd order, giving the determinant formula. In even order all \(2^{n-1}\) even-cardinality frequencies are nonzero, giving the rank bound.

## Verification

The accompanying standard-library `check.py` compares (1), evaluated using an independent-set enumeration and subset transform, against the integer Walsh–Hadamard transform of the profile histogram obtained by direct triangulation enumeration. The recorded comparison covers all \(4064\) frequencies for \(5\le n\le11\), and the script also checks the congruences for all frequencies through \(n=18\). The gcd assertion is justified by the exact-profile proof above, not by testing bounded sizes.

## Relationship to prior work and limitations

The Catalan valuation is a known input: Postnikov and Sagan, [*What power of two divides a weighted Catalan number?*](https://arxiv.org/abs/math/0601339), Theorem 1.1. Classical ear enumeration includes Hurtado and Noy, *Ears of triangulations and Catalan numbers*, Discrete Mathematics 149 (1996), 319–324, and related ear statistics are discussed by [Callan](https://arxiv.org/abs/1204.5704), [Asinowski and Regev](https://arxiv.org/abs/1309.0743), and [Mansour and Rastegar](https://arxiv.org/abs/1911.04025). The [ear-pattern covariance spectrum](https://github.com/Resultary/2026/tree/main/2026/11/16/SCOPE-sharp-harmonic-observability-crossover-for-ear-patterns-of-rando--503a9ed7716d) is an ordinary spatial Fourier analysis of pairwise ear indicators, not an all-frequency Boolean Walsh law.

The [full diagonal-incidence Walsh result](https://github.com/Resultary/2026/tree/main/2026/11/16/SCOPE-fourier-rigidity-and-cancellation-for-convex-polygon-triangulati--e73d48554b89) has uniform congruence modulo four in odd order. An ear tip is equivalent to the presence of the corresponding short diagonal, so that earlier result already implies the exact odd-order valuation for the ear frequencies at \(v_n=0,1\). The sharper odd-order law for \(v_n\ge2\) on the restricted ear sector and the even-order parity law are the distinct conclusions. In particular an unrestricted diagonal frequency can vanish at \(n=15\) without contradicting the absence of ear-sector zeros. These results give neither the full signed magnitude spectrum nor an even-order singularity classification, and do not assert comprehensive historical priority.
