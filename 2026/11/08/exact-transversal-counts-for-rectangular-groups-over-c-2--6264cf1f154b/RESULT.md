# Exact transversal counts for rectangular groups over \(C_2\)

## Finding
Let \(r,s\geq1\), and let \(S_{r,s}=[r]\times C_2\times[s]\) have multiplication \((i,a,\lambda)(j,b,\mu)=(i,a+b,\mu)\), where the middle coordinate is computed modulo two. A *complete mapping* is a bijection \(\alpha:S_{r,s}\to S_{r,s}\) such that \(\theta(x)=x\alpha(x)\) is also bijective. Let \(N_{r,s}\) be the number of complete mappings.

With commuting indeterminates \(z,x_{i,0},x_{i,1}\), define the polynomial
\[
 A_r(\mathbf x)=[z^r]\prod_{i=1}^{r}
 \left((1+z^2)x_{i,0}x_{i,1}+z(x_{i,0}^2+x_{i,1}^2)\right).
\]
Here \([z^r]\) denotes coefficient extraction. For **every pair of positive integers** \(r,s\),
\[
\boxed{N_{r,s}=(r!)^{2s}(s!)^{2r}
  [\prod_{i=1}^{r}x_{i,0}^{s}x_{i,1}^{s}]\,A_r(\mathbf x)^s.}
\]
In addition, \(N_{r,s}=N_{s,r}\), and the one-row and two-row cases reduce to the explicit sums
\[
 N_{1,s}=\begin{cases}(s!)^2\binom{s}{s/2},&2\mid s,\\0,&2\nmid s,\end{cases}
\]
\[
 \boxed{N_{2,s}=4^s(s!)^4\sum_{\substack{0\le k\le s\\2\mid k}}
 \binom{s}{k}\,2^{s-k}\binom{k}{k/2}^2.}
\]
The existence boundary \(N_{r,s}>0\iff2\mid rs\) is already covered by the general existence theorem of Araújo–Bentz–Cameron–Hendrey–Kinyon and is **not** asserted as novel here. The new result is the exact enumeration, including the closed two-row specialization.

## Assumptions and scope
The indices \([r]\) and \([s]\) are fixed labeled sets. The binary group \(C_2=\{0,1\}\) is written additively. All maps are arbitrary set bijections, with no requirement to preserve multiplication. Every counted mapping is distinct as a function on the labeled \(2rs\)-point set. The theorem is valid for all finite positive \(r,s\), including the degenerate group case \(r=s=1\), where \(N_{1,1}=0\).

## Proof
**1. Parameterize mappings by their product permutation.** Given \(\alpha\), put \(\theta(x)=x\alpha(x)\). Because \(\theta\) is a permutation, for each output \((i,t,\mu)\) there is a unique source \((i,g,\lambda)\) and a unique target \(\alpha(i,g,\lambda)=(j,b,\mu)\) such that \(t=g+b\pmod2\). Thus \(g=t+b\) in \(C_2\). We can instead choose, for each output triple \((i,t,\mu)\), its target coordinates \((j,b,\mu)\). The chosen target assignment must be a bijection over all outputs, and the induced source assignments must be a bijection over all inputs.

**2. Count target labels.** Fix \(\mu\in[s]\). In its \(2r\) output positions \((i,t)\), the middle target coordinate \(b\) must occur exactly \(r\) times with value zero and \(r\) times with value one; otherwise the targets \((j,b,\mu)\) cannot be covered exactly once. Once the \(2r\) binary choices have been made, the first target coordinates \(j\in[r]\) can be assigned bijectively to the zero choices in \(r!\) ways and independently to the one choices in \(r!\) ways. This supplies \((r!)^2\) choices in each of the \(s\) output slices, giving the factor \((r!)^{2s}\).

**3. Record which source group coordinates occur.** Fix a first output index \(i\) and an output last coordinate \(\mu\). The two output group coordinates are \(t=0,1\), and the chosen pair of middle target coordinates is \((b_0,b_1)\). The corresponding input group coordinates are \((g_0,g_1)=(b_0,1+b_1)\) in \(C_2\). The four choices contribute exactly
\[
\begin{array}{c|c|c}
 (b_0,b_1)&\#\{b=1\}&\text{source monomial}\\ \hline
(0,0)&0&x_{i,0}x_{i,1}\\
(1,1)&2&x_{i,0}x_{i,1}\\
(0,1)&1&x_{i,0}^2\\
(1,0)&1&x_{i,1}^2
\end{array}
\]
where \(z\) marks the number of target middle bits equal to one. Multiplying the local four-term polynomials over all \(i\) and extracting \(z^r\) enforces the target-balance condition of Step 2 in one slice. This is precisely \(A_r(\mathbf x)\). The \(s\) slices have independent choices, hence their joint polynomial is \(A_r(\mathbf x)^s\).

**4. Count source labels.** For every \(i\in[r]\), the original input set has exactly \(s\) elements of group coordinate zero and \(s\) elements of group coordinate one, distinguished by their last coordinates \(\lambda\in[s]\). The extracted coefficient of \(\prod_i x_{i,0}^s x_{i,1}^s\) selects exactly those binary patterns for which these counts are correct. For each such pattern, assign the \(s\) available last-coordinate labels \(\lambda\) bijectively to the source positions of each \((i,g)\) in \(s!\) ways, independently across \(2r\) pairs \((i,g)\). The multiplier is \((s!)^{2r}\). The target assignment, source labeling, and product permutation now uniquely determine \(\alpha\); conversely, any complete mapping produces exactly one such choice. Thus the coefficient formula is a bijective, exhaustive count without overcounting.

**5. Symmetry.** For a complete mapping \(\alpha\) on any semigroup \(S\), put \(\beta=\alpha^{-1}\). In the opposite semigroup, \(y\cdot_{\mathrm{op}}\beta(y)=\beta(y)y\). Substituting \(y=\alpha(x)\) yields \(x\alpha(x)\), a permutation of \(S\). Thus inversion of mappings gives a bijection between complete mappings of \(S\) and those of \(S^{\mathrm{op}}\). The coordinate swap \((i,a,\lambda)\mapsto(\lambda,a,i)\) identifies \(S_{r,s}^{\mathrm{op}}\) with \(S_{s,r}\), proving \(N_{r,s}=N_{s,r}\).

**6. Specializations.** For one row, \(A_1=x_{1,0}^2+x_{1,1}^2\). The balanced coefficient in its \(s\)-th power is zero unless \(s\) is even and then is \(\binom{s}{s/2}\); multiply by \((s!)^2\). For two rows, multiplication followed by \(z^2\)-extraction gives
\[
 A_2=2x_{1,0}x_{1,1}x_{2,0}x_{2,1}+(x_{1,0}^2+x_{1,1}^2)(x_{2,0}^2+x_{2,1}^2).
\]
Choose \(k\) of the \(s\) slices using the latter term and \(s-k\) using the first. The balanced exponent condition requires \(k\) even. For each row, exactly \(k/2\) of the \(k\) square factors must choose the zero variable, producing \(\binom{k}{k/2}^2\) choices. The remaining terms have weight \(2^{s-k}\), yielding the asserted finite sum. This concludes the proof.

## Verification
The accompanying standard-library program `verify.py` independently computes the coefficient via a bounded integer dynamic program and counts full permutations directly when \(2rs\le8\). For \((r,s)\in\{(1,1),(1,2),(1,3),(1,4),(2,1),(2,2),(3,1),(4,1)\}\), independent exhaustive permutation totals are respectively \(0,8,0,3456,8,2048,0,3456\), all matching the formula. Sixteen additional parameter pairs \(1\le r,s\le4\) verify symmetry and the known existence boundary; the two-row and one-column closed formulas are also independently evaluated. Run `python3 verify.py` in the same folder; `verification_output.txt` is the reference output. The universal conclusion is proved above, not inferred from the finite tests.

## Relationship to prior work
Araújo, Bentz, Cameron, Hendrey and Kinyon (2026), Theorem 5.1, characterize **existence** of complete mappings for general normalized Rees matrix semigroups. For these all-identity-sandwich \(C_2\) rectangular groups, the theorem gives existence exactly when \(rs\) is even. Their Section 6.1 counts mappings of **zero-containing Brandt semigroups** using Latin squares; those are a different multiplication and do not imply the present enumerator. Other accessible results for rectangular **bands** (trivial maximal subgroup) enumerate a different family, and the associated formula is not asserted as new. Davis, Jedwab, Wanless and Wiebe (October 2026) investigate transversals of **group Latin squares**, where both index sets have size one; the non-group rectangular family counted here is distinct. The group-order-two boundary has zero transversals, so their counts do not supply this formula.

## Limitations
The closed enumeration treats only the normalized all-identity Rees sandwich and the group of order two. It does not enumerate arbitrary Rees sandwich matrices, other groups, or Brandt semigroups. The known parity-based existence criterion is prior work, not an originality claim. The independent computations cover only the explicitly listed finite cases. Historical priority of equivalent counting formulas under alternate nomenclature cannot be ruled out solely by literature searching.

## References
1. J. Araújo, W. Bentz, P. J. Cameron, K. Hendrey and M. Kinyon, *Complete Mappings of Semigroups*, arXiv:2608.25092v1 (25 August 2026), Theorem 5.1 and Section 6.1, https://arxiv.org/html/2608.25092v1.
2. J. A. Davis, J. Jedwab, I. M. Wanless and A. Wiebe, *Counting transversals in Latin squares over groups of even order*, arXiv:2610.35611v1 (26 October 2026), https://arxiv.org/abs/2610.35611.
