# Sharp dyadic Walsh gaps for avoidance of unbordered binary words

## Finding
Let \(k\ge2\), let \(w\in\{0,1\}^k\) have no nonempty proper prefix equal to a suffix, and let \(n\ge1\). Define \(A_n(w)\subseteq\mathbb F_2^n\) to be the length-\(n\) binary strings with no contiguous occurrence of \(w\). For \(s\in\mathbb F_2^n\), define the **unnormalized** Walsh coefficient
\[
W_{n,w}(s)=\sum_{x\in A_n(w)}(-1)^{\langle s,x\rangle}.
\]
Write \(n=qk+r\), with integers \(q\ge0\) and \(0\le r<k\). Then every coefficient is divisible by \(2^r\), and
\[
\gcd_{s\in\mathbb F_2^n}|W_{n,w}(s)|
=\min_{W_{n,w}(s)\ne0}|W_{n,w}(s)|=2^r.
\]
More precisely, for the frequency \(s^*\) supported on the first \(qk\) coordinates, with the empty support when \(q=0\),
\[
W_{n,w}(s^*)=(-1)^{q(1+\operatorname{wt}(w))}2^r.
\]
If \(k\mid n\), every Walsh multiplier is odd and counting convolution by \(\mathbf1_{A_n(w)}\) on \(\ell^2(\mathbb F_2^n)\) is invertible. At all lengths its exact Moore–Penrose inverse-on-range norm is \(2^{-r}\).

There is an additional universal first-valuation-layer law. If \(n=qk+1\), then
\[
\frac{W_{n,w}(s)}2\equiv (q+1)+\sum_{j=0}^{q}s_{jk+1}\pmod2.
\]
Consequently exactly \(2^{n-1}\) of the \(2^n\) characters satisfy \(W_{n,w}(s)\equiv2\pmod4\). This includes \(n=1\), when \(q=0\).

## Assumptions and scope
The alphabet is binary; the avoidance constraint is **linear**, not cyclic, with allowed occurrence starts \(1\) through \(n-k+1\). A word is unbordered if no overlap of a proper prefix with a same-length suffix is possible. Fourier coefficients and counting convolution are unnormalized; the latter is \((Tf)(z)=\sum_{x\in A_n(w)}f(z\oplus x)\). The minimum excludes zero coefficients. These statements apply uniformly to all unbordered \(w\), all \(k\ge2\), and all \(n\ge1\), including \(n<k\).

## Proof
For a valid start \(a\), write \(E_a(x)\) for the indicator that the substring at \(a,a+1,\ldots,a+k-1\) equals \(w\). Since \(w\) is unbordered, two occurrences at distinct starts less than \(k\) positions apart cannot coexist: such an overlap would equate a proper suffix of \(w\) with a proper prefix. Therefore every nonzero product \(\prod_{a\in J}E_a(x)\) corresponds to a family \(J\) of pairwise disjoint length-\(k\) intervals. Inclusion–exclusion for the avoidance indicator is exact:
\[
\mathbf1_{A_n(w)}(x)=\sum_{J\text{ disjoint}}(-1)^{|J|}\prod_{a\in J}E_a(x).
\]
Let \(U_J\) be the union of the intervals of \(J\), and \(v_J\in\mathbb F_2^{U_J}\) the forced bits of \(w\) on those intervals. By independence of the remaining free coordinates,
\[
W_{n,w}(s)=\sum_{\substack{J\text{ disjoint}\\\operatorname{supp}(s)\subseteq U_J}}
(-1)^{|J|+\langle s|_{U_J},v_J\rangle}
2^{n-k|J|}.
\tag{1}
\]
Every packing has \(|J|\le q\), so every term in (1) is divisible by \(2^{n-kq}=2^r\). This proves the lower bound on every nonzero multiplier and its common divisibility.

For \(s^*\) supported on all of \(\{1,\ldots,qk\}\), any contributing packing must cover these \(qk\) positions. Therefore it has precisely \(q\) intervals and their union is exactly the prefix \(\{1,\ldots,qk\}\). The unique such packing is the consecutive tiling by blocks starting at \(1,1+k,\ldots,1+(q-1)k\). Its contribution to (1) equals \((-1)^{q+q\operatorname{wt}(w)}2^r\). When \(q=0\), the only inclusion–exclusion term is the empty packing and \(W_{n,w}(0)=2^n=2^r\), agreeing with the same formula. This proves attainment and the exact greatest common divisor.

When \(r=0\), the only packing with \(q\) intervals is the full consecutive tiling. Every packing with fewer intervals contributes an even integer. Thus equation (1) reduces modulo two to the contribution from the full tiling, which is odd regardless of \(s\). Hence no multiplier vanishes. Walsh characters form a complete orthogonal eigenbasis for unnormalized counting convolution, and its eigenvalues are exactly the \(W_{n,w}(s)\); the pseudoinverse norm is the reciprocal of their smallest nonzero magnitude.

When \(r=1\), reducing (1) after division by two modulo two removes all packings with fewer than \(q\) intervals. Every maximum packing leaves exactly one unoccupied coordinate, and these possible holes are precisely \(1,1+k,\ldots,1+qk\). For a hole \(j\), its term contributes one modulo two exactly when \(s_j=0\). Since the signs disappear modulo two, the sum of these indicators is \(\sum_{i=0}^q(1+s_{ik+1})\pmod2\), giving the displayed formula. This affine Boolean functional is nonconstant because its variable coordinates are distinct, so it equals one for exactly half the frequencies. Finally, \(2\cdot\text{odd}\equiv2\pmod4\).

## Verification
Two complementary exact-arithmetic programs accompany this result. The Python 3 standard-library program `check_fwht.py` constructs avoidance indicators directly and applies an integer Walsh–Hadamard transform. It checks all unbordered words of lengths \(2\) through \(6\), and every ambient length \(1\) through \(12\): 528 entire Walsh spectra, including their exact gcd, minimal nonzero magnitude, modular divisibility, and the half-spectrum first valuation claim. It checks Parseval for every spectrum. The C++17 program `check_inclusion.cpp` independently enumerates compatible interval packings and computes the signed inclusion–exclusion sum, comparing every character against direct avoidance enumeration for six named unbordered patterns and lengths through ten (12,276 exact coefficient comparisons). It also tests the explicit attaining character and the parity criterion for divisible lengths. Both executables returned their indicated success messages when checked against these exact source files.

Reproduce using `python3 check_fwht.py` and `c++ -std=c++17 -O2 check_inclusion.cpp -o check_inclusion && ./check_inclusion`. The all-length proof above, not the finite computations, establishes the quantified theorem.

## Relationship to prior work
Guibas and Odlyzko studied overlap/correlation methods and avoidance-word enumeration; these give essential context for the unbordered hypothesis, but ordinary avoidance counts alone do not imply characterwise divisibility or sharp recovery stability. The 2024 analysis by Chandgotia, Marcus, Richey and Wu treats autocorrelation equivalence and inclusion–exclusion for pattern-avoidance cardinalities, including unbordered patterns; its inspected full text develops neither a Walsh valuation law nor a characterwise smallest-multiplier theorem. De Wolf develops Fourier normalization and convolution diagonalization, without this avoidance specialization. Bilotta and coauthors enumerate selected two-run patterns; their openly available arXiv HTML full text develops Riordan-array and generating-tree enumeration, without a characterwise Walsh law. Further older literature may still contain implicit formulations. Previously studied special cases such as avoidance of `001` are subsumed rather than counted as separate results.

## Limitations
There is no claim that every nonmultiple length is singular, no formula for the complete Fourier nullity at those lengths, and no extension to bordered forbidden words or to cyclic avoidance. The unbordered hypothesis is essential to this proof: for the bordered word `11` and ambient length three, the minimum nonzero Walsh magnitude is one, not the value two predicted by this law. The external novelty comparison is bounded; unindexed historical treatments may contain a differently stated equivalent result. Independent mathematical validation has not been performed.

## References
- L. J. Guibas and A. M. Odlyzko, “String overlaps, pattern matching, and nontransitive games,” *J. Combin. Theory Ser. A* 30 (1981), 183–208. DOI: https://doi.org/10.1016/0097-3165(81)90005-4
- R. de Wolf, “A Brief Introduction to Fourier Analysis on the Boolean Cube,” *Theory of Computing Graduate Surveys* 1 (2008), 1–20. https://doi.org/10.4086/toc.gs.2008.001
- S. Bilotta, D. Merlini, E. Pergola, and R. Pinzani, “Binary words avoiding a pattern and marked succession rule,” arXiv:1103.5689, first posted 2011-03-29. https://arxiv.org/abs/1103.5689
- N. Chandgotia, B. Marcus, J. Richey, and C. Wu, “Shifts of Finite Type Obtained by Forbidding a Single Pattern,” arXiv:2409.09024, first posted 2024-09-13. https://arxiv.org/abs/2409.09024
