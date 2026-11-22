# Uniform near-quarter-modulus balance for two-generator numerical-semigroup gaps

## Finding
Let \(a,b>1\) be coprime integers and let \(m\ge2\) satisfy \(\gcd(ab,m)=1\). Write
\[
S=\langle a,b\rangle,\quad H=\mathbb Z_{\ge0}\setminus S,\quad
N_r=\#\{h\in H:h\equiv r\pmod m\}\quad(0\le r<m).
\]
Set \(s=a\bmod m\in\{1,\ldots,m-1\}\) and \(t=b\bmod m\). Then the *entire* vector \((N_0,\ldots,N_{m-1})\) is recovered from the genus and the cyclic differences
\[
N_r-N_{(r-s)\bmod m}
=\mathbf{1}_{0\le r<s}-\mathbf{1}_{0\le (t^{-1}r\bmod m)<s}.
\tag{1}
\]
In particular its range obeys the generator-size-independent bound
\[
\boxed{\max_r N_r-\min_r N_r\le\left\lceil\frac m4\right\rceil.}
\tag{2}
\]
For every \(m\ge2\) there exist coprime \(a,b>1\), both coprime to \(m\), attaining a range of at least \(\lfloor(m+1)/4\rfloor\). Thus (2) is **exactly sharp** for every \(m\equiv0,3\pmod4\). For \(m\equiv1,2\pmod4\) the proven upper and lower bounds differ by at most one. At \(m=2\), all the counts are equal.

An explicit recovery formula is as follows. Put \(r_j=js\bmod m\), \(D_0=0\), and
\[
D_j=\left\lfloor\frac{js}{m}\right\rfloor
-\sum_{i=1}^j\mathbf{1}_{0\le(t^{-1}si\bmod m)<s}
\qquad (1\le j<m).
\]
With \(g=(a-1)(b-1)/2\), one has
\[
\boxed{N_{r_j}=\frac{g-\sum_{i=0}^{m-1}D_i}{m}+D_j\quad(0\le j<m).}
\tag{3}
\]
Consequently the centered histogram depends only on the two unit residues of the generators, rather than on their magnitudes.

## Assumptions and scope
All parameters are integers, \(a,b>1\), \(m\ge2\), \(\gcd(a,b)=\gcd(ab,m)=1\). Residues in comparisons are least nonnegative representatives. Equation (2) concerns the absolute difference between the largest and smallest **gap counts**, not the discrepancy of partial sums or the largest missing integer. There is no assertion for \(\gcd(ab,m)>1\). The statements are exact for every admissible integer triple, and do not invoke an asymptotic limit.

## Proof
**1. Gap-polynomial identity.** Because \(\gcd(a,b)=1\), the smallest member of \(S\) in residue class \(ib\bmod a\), for \(0\le i<a\), is \(ib\). Thus the generating series of \(S\) is
\[
\sum_{n\in S}x^n=\frac{\sum_{i=0}^{a-1}x^{ib}}{1-x^a}.
\]
Subtracting from \(1/(1-x)\), the (finite) gap polynomial \(P(x)=\sum_{h\in H}x^h\) satisfies the polynomial identity
\[
(1-x^a)P(x)=\sum_{i=0}^{a-1}x^i-\sum_{i=0}^{a-1}x^{ib}.\tag{4}
\]
Reduce (4) modulo \(x^m-1\), identifying the coefficient of \(x^r\) with \(N_r\). Write \(a=qm+s\). The first sum has exactly \(q+\mathbf{1}_{r<s}\) indices in class \(r\). Since multiplication by \(b\) permutes residues modulo \(m\), the second has \(q+\mathbf{1}_{(t^{-1}r\bmod m)<s}\) such indices. This proves (1).

**2. Exact reconstruction.** Since \(s\) is a unit modulo \(m\), the classes \(r_j=js\bmod m\) visit each residue once for \(0\le j<m\). In (1) at \(r_j\), the first indicator equals \(\lfloor js/m\rfloor-\lfloor(j-1)s/m\rfloor\). Summing from \(1\) to \(j\) gives \(N_{r_j}-N_0=D_j\). The classical two-generator genus formula \(\#H=g=(a-1)(b-1)/2\), together with \(\sum_r N_r=g\), gives (3). In particular its right side is an integer and uniquely defines the histogram.

**3. Uniform range bound.** Choose two indices \(0\le u<v\le m\), and let \(L=v-u\). By the recurrence,
\[
N_{r_v}-N_{r_u}=A-B,
\quad A=\left\lfloor\frac{vs}{m}\right\rfloor-\left\lfloor\frac{us}{m}\right\rfloor,
\]
where \(B\) counts those \(j\in\{u+1,\ldots,v\}\) with \((t^{-1}sj\bmod m)<s\). In any full cycle of \(m\) successive indices there are exactly \(s\) such marked indices, as \(t^{-1}s\) is a unit. Hence
\[
\left\lfloor\frac{Ls}{m}\right\rfloor\le A\le\left\lceil\frac{Ls}{m}\right\rceil,
\qquad
\max(0,L+s-m)\le B\le\min(L,s).
\]
If \(L\le s\), then \(B-A\le L-\lfloor Ls/m\rfloor=\lceil L(m-s)/m\rceil\). If \(L\ge s\), then \(B-A\le s-\lfloor Ls/m\rfloor\le\lceil s(m-s)/m\rceil\). Likewise, when \(L\le m-s\), \(A-B\le\lceil Ls/m\rceil\), and when \(L\ge m-s\),
\[
A-B\le\left\lceil\frac{Ls}{m}\right\rceil-(L+s-m)
=\left\lceil\frac{(m-s)(m-L)}m\right\rceil.
\]
Therefore in every case \(|A-B|\le\lceil s(m-s)/m\rceil\le\lceil m/4\rceil\). Every two residue classes can be represented by two indices along this cycle, proving (2).

**4. Infinite witness families and near-sharpness.** Fix any unit \(s\pmod m\), and take \(a=s+m\), \(b=s+2m\). Then \(\gcd(a,b)=\gcd(s,m)=1\). Since \(t=s\), for \(0\le j<m\) the formula above simplifies to
\[
D_j=\left\lfloor\frac{js}{m}\right\rfloor-\min(j,s-1).
\]
All these values are nonpositive. The minimum occurs at \(j=s-1\), while the maximum is zero at \(j=0\). Thus the exact range in this diagonal-residue family is
\[
R_m(s)=s-1-\left\lfloor\frac{s(s-1)}m\right\rfloor
=\left\lceil\frac{(s-1)(m-s)}m\right\rceil.\tag{5}
\]
For odd \(m\ge5\), take \(s=(m-1)/2\). For even \(m\ge8\), take \(s=2\lfloor m/4\rfloor-1\). In either case \(s\) is coprime to \(m\), and elementary substitution in (5) gives \(R_m(s)=\lfloor(m+1)/4\rfloor\). The small moduli \(m=2,3,4,6\) are handled by units \(s=1,2,3,5\), respectively, giving ranges \(0,1,1,1\). This establishes the universal lower witnesses and exact sharpness for the stated congruence classes. For \(m=2\), (1) has zero right side, so the range is zero for every permitted pair.

## Verification
Run `python3 verify.py` with Python 3.8 or newer. This standalone program compares the integer gap sets to the separate cyclic reconstruction for 10,743 triples, checks the range bound for 835,733 pairs of unit residues, and verifies the diagonal witness formula for moduli \(2\) through \(180\). The analytic proof above, not the finite tests, proves the statements for arbitrary parameters. No external data files or third-party packages are needed.

## Relationship to prior work
Shor's *Equidistribution of numerical semigroup gaps modulo* \(m\) (first public preprint January 5, 2021; subsequently published in 2022) determines exactly when the two-generator gap histogram is constant, in particular its Corollary 5.5. It does not state a quantitative range bound, uniform over arbitrarily large coprime generators, or an exact reconstruction and near-sharp witness family for the nonconstant distributions. Its generating-function and Apéry methods motivate the derivation in (4). Komatsu and Zhang (arXiv:2101.04298, first public January 12, 2021, and the two-generator-specific arXiv:2105.08274, first public May 18, 2021), in their weighted Sylvester sum formulas, supply exponential gap sums which, when evaluated at roots of unity and Fourier inverted, already determine every residue count in principle. Thus no novelty is asserted for the mere computability of the histogram or for the modular generating-function identity. The contribution claimed here is the **uniform near-quarter-modulus range inequality and explicit witness families**, neither of which follows immediately from the previously known weighted formulas without a new uniform estimate. Shor and Sim (first preprint March 13, 2025) investigate equidistribution for geometrically generated semigroups, a different question, and restate the two-generator zero-range criterion. Both works' mathematical statements were compared, not merely their titles.

## Limitations
The bound (2) is shown to be exactly sharp for \(m\equiv0,3\pmod4\), but for \(m\equiv1,2\pmod4\) the upper and witnessed lower bounds differ by one; no optimality assertion is made in those cases. The proof assumes the generators are units modulo \(m\): without that condition the discrepancy can grow with their size (for \(\langle2,2q+1\rangle\) modulo \(2\), all \(q\) gaps are odd). The exact modular recurrence is an efficient form of already obtainable coefficient information, not an assertion of unprecedented exact histogram computability, genus or zero-discrepancy criteria. An equivalent quantitative inequality from weighted Sylvester-sum, exponential-sum or Dedekind-sum methods might exist outside the inspected sources.

## References
- C. M. Shor, *Equidistribution of numerical semigroup gaps modulo m*, arXiv:2101.01760, first publicly posted January 5, 2021; *Discrete Mathematics* 345 (2022), article 112995. https://arxiv.org/abs/2101.01760
- T. Komatsu and Y. Zhang, *Weighted Sylvester sums on the Frobenius set in more variables*, arXiv:2101.04298, first posted January 12, 2021; Theorems 1–4 and two-generator specialization. https://arxiv.org/abs/2101.04298
- T. Komatsu and Y. Zhang, *Weighted Sylvester sums on the Frobenius set*, arXiv:2105.08274, first posted May 18, 2021; Theorems 1–3. https://arxiv.org/abs/2105.08274
- C. M. Shor and J. H. Sim, *Equidistribution Conditions for Gaps of Geometric Numerical Semigroups*, arXiv:2503.10826, first posted March 13, 2025. https://arxiv.org/abs/2503.10826
- W. Wang and T. Wang, *Alternate Sylvester sums on the Frobenius set*, *Computers & Mathematics with Applications* 56 (2008), 1328–1334. Bibliographic reference as cited by Shor; the original full text was not inspected.
