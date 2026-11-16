# Exact dyadic Fourier gcd for transitive tournaments

## Finding

Let \(n\ge 1\), \(E=\{\{i,j\}:1\le i<j\le n\}\), and \(H=\mathbb F_2^E\). Encode each total order \(\pi\) of the labeled vertices by its inversion vector \(x_\pi\in H\), with \((x_\pi)_{ij}=1\) when vertex \(j\) precedes vertex \(i\) in the order. These are exactly the labeled transitive-tournament orientations relative to the ascending reference orientation. Let \(f_n\) be their indicator and define the **unnormalized** Walsh transform
\[
 W_n(b)=\sum_{\pi\in S_n}(-1)^{\langle b,x_\pi\rangle},\qquad b\in H.
\]
The greatest common divisor of **every** integer Walsh multiplier is
\[
 \boxed{\gcd_{b\in H} W_n(b)=2^{n-s_2(n)}=2^{\nu_2(n!)}},
\]
where \(s_2(n)\) is the binary digit sum, \(\nu_2\) is the exponent of two in a positive integer, and the gcd is taken to be nonnegative. In particular, every signed graphical-inversion sum is divisible by the full power of two dividing \(n!\), and no larger integer divides all such sums. For \(n\ge2\), every odd-Hamming-weight frequency has zero multiplier, so at least \(2^{\binom n2-1}\) frequencies vanish. For unnormalized convolution by \(f_n\), every nonzero eigenvalue is an integer multiple of \(2^{n-s_2(n)}\), and
\[
 \|C_{f_n}^{\dagger}\|_{\ell^2\to\ell^2}\le 2^{-(n-s_2(n))}.
\]
This is an upper bound, not a claim that the smallest nonzero eigenvalue always attains the divisor.

## Assumptions and scope

The complete graph has \(n\) **labeled** vertices, and every labeled total order is counted once. The Fourier group is the full binary edge-coordinate group \(H\), with \(|H|=2^{\binom n2}\). The character is \((-1)^{\langle b,x\rangle}\) with the standard mod-two pairing. The convention \(n=1\) gives \(H=\{0\}\) and \(W_1(0)=1\). All sums and divisibilities are exact integers; no probability normalization is used. A graph selected by the negative signs in \(b\) is not required to be transitive, bipartite, or connected.

## Proof

**1. Signed graphical inversion sums.** For any finite subset \(S\) of distinct labeled vertices and fixed arbitrary edge signs \(\varepsilon_{ij}\in\{+1,-1\}\), define
\[
 F(S)=\sum_{\pi\text{ an order of }S}\ \prod_{\substack{i<j\\i,j\in S\\ j\text{ before }i\text{ in }\pi}}\varepsilon_{ij}.
\]
Empty products are one. If an order is split into a first block containing precisely \(A\) and a second block containing its complement \(B\), its cross-block sign \(c(A,B)\in\{\pm1\}\) depends only on the two vertex sets, not on either internal order. Summing all such orders therefore yields \(c(A,B)F(A)F(B)\).

**2. Dyadic-block divisibility.** We prove by induction on \(k\ge0\) that \(2^{2^k-1}\mid F(S)\) whenever \(|S|=2^k\), independently of the signs. The singleton case is \(F(S)=1\). Suppose \(|S|=2m\), where \(m\) is a power of two. Partition each order into its first and last \(m\) positions and group the terms by the set \(A\) in the first half. Paired complementary choices \((A,B)\) and \((B,A)\) contribute
\[
 [c(A,B)+c(B,A)]F(A)F(B).
\]
The bracket belongs to \(\{-2,0,2\}\), while induction makes each of \(F(A),F(B)\) divisible by \(2^{m-1}\). Thus each complementary pair contributes a multiple of \(2^{1+2(m-1)}=2^{2m-1}\). No such pair is fixed under swapping because \(A\) and \(B\) are nonempty disjoint halves. This establishes the induction step.

**3. General sizes.** Decompose \(n\) as a sum of distinct powers of two, \(n=2^{k_1}+\cdots+2^{k_r}\), where \(r=s_2(n)\). Divide the consecutive positions of each permutation into blocks of those lengths. Group orders by the corresponding ordered partition of the *vertex labels*. Cross-block signs depend only on this partition; its internal ordering sum factors as a product of the \(r\) terms \(F(S_j)\). Step 2 makes every such product divisible by
\[
 2^{\sum_{j=1}^r(2^{k_j}-1)}=2^{n-s_2(n)}.
\]
Every term in this partition sum is divisible by this power; hence so is \(W_n(b)\), for every frequency \(b\).

**4. The exact gcd.** Let \(g=\gcd_{b\in H}W_n(b)\). Character orthogonality and the fact that the identity total order has inversion vector zero give
\[
 \sum_{b\in H} W_n(b)=\sum_\pi\sum_{b\in H}(-1)^{\langle b,x_\pi\rangle}=|H|=2^{\binom n2}.
\]
Thus \(g\) divides a power of two. Also \(W_n(0)=n!\). The elementary Legendre valuation identity gives \(\nu_2(n!)=\sum_{j\ge1}\lfloor n/2^j\rfloor=n-s_2(n)\). Therefore \(g\le2^{n-s_2(n)}\), while Step 3 gives the reverse divisibility; equality follows.

**5. Vanishing characters and convolution.** Reversal of a total order complements every edge inversion bit. Consequently the map \(x\mapsto x+\mathbf1_E\) preserves the support of \(f_n\). Fourier transformation gives \(W_n(b)=(-1)^{\sum_{e\in E}b_e}W_n(b)\). Hence every odd-weight \(b\) has \(W_n(b)=0\). When \(n\ge2\), exactly half of the \(2^{\binom n2}\) frequencies have odd weight. Unnormalized group convolution is diagonalized by the Walsh characters, with eigenvalues \(W_n(b)\); the gcd formula makes every nonzero eigenvalue have modulus at least \(2^{n-s_2(n)}\). The stated pseudoinverse bound follows.

## Verification

The standalone `checker.py` enumerates the transitive tournament edge vectors, performs an exact integer Walsh–Hadamard transform for every frequency for \(1\le n\le6\), independently recomputes selected coefficients as signed permutation sums, and checks the universal divisor and gcd. The same script evaluates 300 deterministic sampled signed sums at each of \(n=7,8\). It reports `TRANSITIVE_TOURNAMENT_FOURIER_GCD_PASS`. The general proof above does not rely on a finite enumeration.

## Relationship to prior work

Foata and Zeilberger introduced graph-parameterized inversion statistics and characterized equidistribution with graphical major indices. Grady and Poznanović further studied equidistribution and sorting-index comparisons on rearrangement classes. Both supply directly relevant language for the signed graphical-inversion specialization \(q=-1\), but their inspected theorems do not state the uniform exact dyadic Walsh gcd, which concerns every arbitrary sign graph simultaneously and uses a different complementary-block divisibility argument. The standard univariate inversion \(q\)-factorial at \(q=-1\) supplies only the special frequency with *every* comparison signed negatively, where the sum is zero for \(n\ge2\); it does not imply the all-frequency divisor or its exact gcd. A preceding equivalence hidden in other signed-permutation or graph-inversion literature has not been excluded by exhaustive historical review.

## Limitations

The theorem determines the exact **common divisor** and a universal nonzero spectral gap, not the exact smallest positive multiplier for every \(n\), the full distribution of multipliers, or their exact zero multiplicity beyond the guaranteed half. Small numerical examples where the gap is attained do not prove all-length attainment. The originality comparison is bounded to identified sources, and no independent mathematical audit has occurred.

## References

1. D. Foata and D. Zeilberger, *The Graphical Major Index*, arXiv:math/9406220v1, first posted 1994-06-23. https://arxiv.org/abs/math/9406220
2. A. Grady and S. Poznanović, *Graphical Mahonian Statistics on Words*, arXiv:1607.00033v1, first posted 2016-06-30. https://arxiv.org/abs/1607.00033
