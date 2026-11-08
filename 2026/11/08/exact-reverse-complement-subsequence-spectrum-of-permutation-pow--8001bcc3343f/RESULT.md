# Exact reverse-complement subsequence spectrum of permutation powers

## Finding

For all integers \(m\ge1\) and \(k\ge1\), write \(P_m=0\,1\,\cdots\,(2m-1)\) and \(W_{m,k}=P_m^k\). On the alphabet \(\Sigma_m=\{0,\ldots,2m-1\}\), define the fixed-point-free involution \(\theta(i)=2m-1-i\), extended letterwise to words. Let \(N_m(k,h)\) be the number of **distinct nonempty output strings** \(U\) that are scattered subsequences of \(W_{m,k}\), have length \(2h\), and satisfy \(U=\theta(U^{\mathrm{rev}})\). Distinct positional embeddings of the same string are counted once.

The complete bivariate spectrum is

\[\boxed{\sum_{k\ge1}\sum_{h\ge1}N_m(k,h)z^kt^h=\frac{z\big((1+t(1-z^2))^m-1\big)}{(1-z)\big(1-z(1+t(1-z^2))^m\big)}.}\]

Consequently, the total number \(N_m(k)=\sum_{h\ge1}N_m(k,h)\) has generating function

\[\sum_{k\ge1}N_m(k)z^k=\frac{z((2-z^2)^m-1)}{(1-z)(1-z(2-z^2)^m)}.\]

The first three totals are \(N_m(1)=2^m-1\), \(N_m(2)=4^m-1\), and \(N_m(3)=8^m-1-m2^{m-1}\). At \(m=2\), they begin \(3,15,59,223\) for \(k=1,2,3,4\).

## Assumptions and scope

A scattered subsequence is obtained by deleting zero or more positions while preserving the order of the survivors. For \(U=u_1\cdots u_\ell\), \(U^{\mathrm{rev}}=u_\ell\cdots u_1\). The condition \(U=\theta(U^{\mathrm{rev}})\) defines a reverse-complement palindrome, not necessarily an ordinary palindrome. Because \(\theta\) fixes no symbol, all such nonempty words have even length. All stated generating-function identities are formal in \(z\) with polynomial coefficients in \(t\) at each coefficient of \(z\); the absence of a length-zero output is intentional.

## Proof

**1. A general half-word reduction.** Let \(A\) be an arbitrary word of length \(n\) over an alphabet with a fixed-point-free involution \(\theta\), and put \(X=A\theta(A^{\mathrm{rev}})\). The distinct nonempty reverse-complement-palindromic scattered subsequences of \(X\) are exactly

\[\{V\theta(V^{\mathrm{rev}}):V\text{ is a nonempty scattered subsequence of }A\}.\]

For the forward containment, suppose \(U=V\theta(V^{\mathrm{rev}})\) is embedded at positions \(p_1<\cdots<p_{2h}\) in \(X\), numbering positions from \(1\) to \(2n\). By the symmetry \(X_j=\theta(X_{2n+1-j})\), the reflected positions \(q_i=2n+1-p_{2h+1-i}\) are another increasing embedding of \(U\). For \(1\le i\le h\), let \(r_i=\min(p_i,q_i)\). Both candidate position sequences strictly increase, so \(r_1<\cdots<r_h\), and each \(X_{r_i}=U_i\). Moreover \(r_i\le n\): if both \(p_i,q_i>n\), then \(p_i>n\) but \(p_{2h+1-i}<n+1\), contradicting \(p_i<p_{2h+1-i}\). Thus \(V\) embeds in the first half \(A\). The reverse containment follows by embedding \(V\) in \(A\) and reflecting those positions into the second half of \(X\). The map \(V\mapsto V\theta(V^{\mathrm{rev}})\) is injective because its first half recovers \(V\).

For \(A=P_m^k\) cut at its midpoint, the host \(W_{m,k}\) is itself reverse-complement symmetric: \(\theta(W_{m,k}^{\mathrm{rev}})=W_{m,k}\). Although the reduction applies to the literal midpoint of \(W_{m,k}\), the following independent greedy argument is more convenient for the exact bivariate count.

**2. Earliest-period criterion.** For a nonempty word \(U=u_1\cdots u_\ell\) over the ordered alphabet \(\Sigma_m\), define its weak-descent count

\[d(U)=\#\{i:1\le i<\ell,\ u_i\ge u_{i+1}\}.\]

The earliest embedding of \(U\) in the infinite periodic word \(P_m^\omega\) must advance by one period precisely at the weak descents, and never otherwise. Its final letter lies in period number \(d(U)+1\). Therefore \(U\) embeds in \(P_m^k\) if and only if \(d(U)\le k-1\). This also proves that the criterion accounts for repeated letters, since equal consecutive letters require a new period.

**3. Symmetry collapses the cost.** Every nonempty reverse-complement palindrome has a unique representation \(U=V\theta(V^{\mathrm{rev}})\), where \(V=v_1\cdots v_h\), \(h\ge1\). For adjacent letters in \(V\), their reflected counterparts contribute identical weak-descent indicators: \(v_i\ge v_{i+1}\) if and only if \(\theta(v_{i+1})\ge\theta(v_i)\). At the central pair \(v_h,\theta(v_h)\), a weak descent occurs exactly when \(v_h\ge m\). Thus, with \(D(V)=\#\{i:v_i\ge v_{i+1}\}\),

\[d(U)=2D(V)+\mathbf1_{\{v_h\ge m\}}.\]

Consequently, a given half-word \(V\) occurs in exactly the source powers indexed by \(k\ge1+d(U)\). Summing its contribution to the \(k\)-generating function gives \(z^{1+d(U)}/(1-z)\).

**4. Transfer recurrence and simplification.** Fix \(m\) and set \(r=1+t(1-z^2)\). For each \(0\le i<2m\), let \(B_i\) enumerate nonempty half-words \(V\) that end in \(i\), with weight \(t^{|V|}z^{2D(V)}\). If \(S=\sum_{i=0}^{2m-1}B_i\), adjoining a final letter gives

\[B_i=t\left(1+\sum_{j<i}B_j+z^2\sum_{j\ge i}B_j\right).\]

It follows directly that \(B_0=t(1+z^2S)\) and \(B_i=rB_{i-1}\) for \(i\ge1\). For each positive integer \(a\), let \(A_a=\sum_{j=0}^{a-1}r^j\). Thus

\[S=tA_{2m}(1+z^2S),\qquad B_i=t r^i(1+z^2S).\]

Incorporating the single central cost for last letters in \(\{m,\ldots,2m-1\}\) gives

\[T=\sum_{i<m}B_i+z\sum_{i\ge m}B_i=\frac{tA_m(1+zr^m)}{1-tz^2A_{2m}}.\]

The polynomial identities \(t(1-z^2)A_a=r^a-1\) and \((1-z^2)(1-tz^2A_{2m})=1-z^2r^{2m}\) yield, by cancellation of formal units,

\[T=\frac{r^m-1}{1-zr^m}.\]

Finally the previously established minimal-period criterion makes the desired series equal to \(zT/(1-z)\), proving the bivariate formula. Substituting \(t=1\) is legitimate coefficientwise in \(z\) and gives the univariate formula. The first-three-period expressions follow from extracting the first three coefficients, including the negative term \(-m2^{m-1}\) at the third period.

## Verification

The standalone Python 3 standard-library script `verify.py` expands the rational function coefficientwise as integer polynomials, independently enumerates **all distinct reverse-complement-palindromic subsequences** via positional masks for \((m,k)\in\{(1,1),\ldots,(1,9),(2,1),\ldots,(2,4),(3,1),\ldots,(3,3),(4,1),(4,2)\}\), and compares every half-length coefficient. It examines 751,506 masks across 18 configurations. It separately checks the universal half-word reduction on 466 symmetric hosts over alphabets of sizes two and four, and tests the greedy-period criterion on additional finite cases. Run `python3 verify.py` from the package directory; success ends in `VERIFY_OK configurations=18 masks=751506 symmetric_hosts=466 tests=histogram_greedy_half_spectrum`. These finite computations are checks, not the infinite proof.

## Relationship to prior work

Müllner and Ryzhikov (2019) investigate the lengths and extremal guarantees of ordinary palindromic and binary antipalindromic subsequences. Mahalingam and Pandoh (2021) study the numbers of distinct **ordinary** palindromic scattered subsequences of general words. Ambrož, Masáková and Pelantová (2019) study anti-palindromic **factors** of morphic words. These are related but neither their inspected main statements nor their treatments of restricted examples contain the all-alphabet, all-repetition, half-length-resolved reverse-complement enumeration proved here. An ordinary-palindrome enumeration is not an immediate implication because it requires equality under reversal rather than equality under reverse-complement; a maximum-length theorem also does not determine distinct-output counts. Established general subsequence automata could in principle recover the statistic computationally for each fixed instance; this does not supply the stated symbolic bivariate identity. Published literature comparisons were not exhaustive, so an unindexed equivalent identity remains possible.

## Limitations

This result concerns scattered subsequences, not contiguous factors, embeddings with multiplicity, approximate complementarity or palindromic length. It assumes a totally ordered alphabet of even size and the particular order-reversing involution \(\theta\); no claim is made for arbitrary involutions, arbitrary source words, or odd alphabets. The universal half-word reduction applies whenever the host is reverse-complement symmetric, but the rational generating function is established only for exact ascending permutation powers. Finite verification does not establish the infinite statements; the proof supplies that step. Independent validation has not been performed.

## References

1. C. Müllner and A. Ryzhikov, *Palindromic Subsequences in Finite Words*, arXiv:1901.07502v1 (first public 2019-01-22), https://arxiv.org/abs/1901.07502.
2. K. Mahalingam and P. Pandoh, *Counting scattered palindromes in a finite word*, arXiv:2108.02729v1 (first public 2021-08-05), https://arxiv.org/abs/2108.02729.
3. P. Ambrož, Z. Masáková and E. Pelantová, *Morphisms generating antipalindromic words*, arXiv:1906.06174v1 (first public 2019-06-14), https://arxiv.org/abs/1906.06174.
