# Centralizer run factorization and the rank-refined commutation law for shift-one partial isometries

## Finding
For every integer \(n\ge 2\), put \(N=n-1\) and \(X_n=\{1,\ldots,n\}\). Let \(B_n\) be the set of the \(2^N\) partial maps \(\xi_A\), indexed by \(A\subseteq\{2,\ldots,n\}\), that send \(a\in A\) to \(a-1\) and are undefined elsewhere. This set contains the zero map, but is **not** asserted to be closed under composition. For \(1\le r\le N\), the rank-\(r\) stratum of \(B_n\) is the shift-one generating family \(F_r\) used for minimal ideal generators in [1]. The following three parts concern the same commutation relation inside this family.

**Individual centralizers.** Represent \(A\) by its binary indicator word \(a_1\cdots a_N\), with \(a_i=1\) exactly when \(i+1\in A\). Write \(\ell_1,\ldots,\ell_s\) for the lengths of its maximal nonempty runs of ones. Let \(h(A)\) count the zero positions that are not adjacent to a one (with positions outside the word treated as zero). Then the *rank polynomial of the commuting partners inside \(B_n\)* is exactly
\[
P_A(y)=\sum_{\substack{D\subseteq\{2,\ldots,n\}\\\xi_A\xi_D=\xi_D\xi_A}}y^{|D|}
=(1+y)^{h(A)}\prod_{j=1}^{s}(1+y^{\ell_j}).
\]
The empty product is one. This gives the full partner-rank distribution, not just its total size.

**All-rank pair census.** Set \(C_N(x,y)=\sum_{\xi_A\xi_D=\xi_D\xi_A}x^{|A|}y^{|D|}\), where both subsets range over \(\{2,\ldots,n\}\), and put
\[
Q(z,x,y)=\frac{zx}{1-zx}+\frac{zy}{1-zy}+\frac{zxy}{1-zxy}.
\]
The exact trivariate formal-power-series identity is
\[
\boxed{\displaystyle \sum_{N\ge0} C_N(x,y)z^N=\frac{1+Q(z,x,y)}{1-z-zQ(z,x,y)}.}
\]
In particular, the number of ordered commuting pairs of the *essential shift-one rank-\(r\) generators* from \(F_r\) is \([z^{n-1}x^ry^r](1+Q)/(1-z-zQ)\). The unweighted total is
\[
\boxed{C_N(1,1)=\frac{(1+\sqrt3)^{N+1}+(1-\sqrt3)^{N+1}}2.}
\]
Consequently the probability that two independent uniformly selected members of \(B_n\) commute equals \(C_N(1,1)/4^N\), with asymptotic equivalent
\[
\frac{1+\sqrt3}{2}\left(\frac{1+\sqrt3}{4}\right)^N.
\]

**Sharp centralizer maximum at prescribed rank.** For \(1\le r\le N\), write \(z=N-r\). Then
\[
\boxed{\max_{|A|=r}P_A(1)=\begin{cases}2^{z+1},&0\le z\le r-1,\\2^z,&z\ge r.\end{cases}}
\]
In the first regime the maximizing binary words are precisely the ones with \(z+1\) nonempty one-runs separated by single zeros, and with no initial or final zeros. Their number is \(\binom{r-1}{z}\). In the second regime a contiguous rank-\(r\) block touching either boundary attains the stated maximum.

## Assumptions and scope
The product convention is first the left map, then the right map; commutation itself is independent of this convention. Maps are ordinary partial injections of the finite chain; \(\xi_A\) is order-preserving, order-decreasing and distance-preserving. The rank is the cardinality of the domain (equivalently the image). The base case \(N=0\) is included only in the generating function, with \(C_0(x,y)=1\). Every count is for *ordered* pairs. No assertion is made that \(B_n\) is a semigroup: in general the composition of two shift-one maps is a shift-two map.

## Proof
**1. Local commutation constraint.** For binary words \(a_i,b_i\) representing \(\xi_A,\xi_D\), each composite has displacement minus two wherever defined. At each source \(i+1\) with \(2\le i\le N\), the left-then-right composite is defined exactly when \(a_i b_{i-1}=1\); the reverse composite is defined exactly when \(b_i a_{i-1}=1\). Their images then agree automatically. Therefore
\[
\xi_A\xi_D=\xi_D\xi_A\quad\Longleftrightarrow\quad a_i b_{i-1}=b_i a_{i-1}\ \text{for all }2\le i\le N.
\]
The criterion remains valid for \(N=1\), when both products are empty and the conditions are vacuous.

**2. Partner polynomial.** Fix \(a\). At two adjacent occupied positions the preceding equation forces the corresponding \(b\)-digits to agree. Thus the \(b\)-digits on each maximal one-run share one binary choice, contributing either rank zero or its entire length \(\ell_j\), a factor \(1+y^{\ell_j}\). A zero position adjacent to a one must carry \(b=0\), by the condition at their common edge. At every zero position with both neighbors zero, its \(b\)-digit is unconstrained and contributes \(1+y\). These choices are independent and account for all positions, proving the factorization of \(P_A\).

**3. Rational pair series.** Encode an ordered binary-word pair at each position by one of four symbols \(00,10,01,11\), with weights \(1,x,y,xy\). The local criterion means any two adjacent *nonzero* symbols must be identical; the zero symbol \(00\) can neighbor anything. Every such word is therefore uniquely a sequence of positive-length constant-nonzero runs, each consecutive pair separated by at least one zero, with any nonnegative numbers of zeros at the beginning and end. The generating function for one nonzero run is \(Q=zx/(1-zx)+zy/(1-zy)+zxy/(1-zxy)\). The generating function for the empty nonzero-run case is \(1/(1-z)\). For exactly \(k\ge1\) nonzero runs it is
\[
\frac{Q^k}{(1-z)^2}\left(\frac{z}{1-z}\right)^{k-1}.
\]
Summing the geometric series in the formal power-series ring gives \((1+Q)/(1-z-zQ)\), proving the full rank refinement. At \(x=y=1\), \(Q=3z/(1-z)\), hence the series specializes to \((1+2z)/(1-2z-2z^2)\). Solving the order-two recurrence gives the stated exact expression and its exponential asymptotic (since \(|1-\sqrt3|<1+\sqrt3\)).

**4. Sharp fixed-rank maximum.** Let \(r\ge1\) be the number of ones, \(s\) the number of one-runs, \(z=N-r\) the number of zeros and \(f\) the number of zero positions adjacent to at least one one. The partner factorization gives
\[
P_A(1)=2^{s+z-f}.
\]
Each of the \(s-1\) gaps separating successive one-runs contains a distinct zero adjacent to a one, so \(f\ge s-1\). Therefore \(P_A(1)\le2^{z+1}\), with equality exactly when every separating gap is a single zero and there are no boundary zeros. Equality forces \(z=s-1\le r-1\); for \(z\le r-1\), split the \(r\) ones into \(z+1\) positive run lengths in \(\binom{r-1}{z}\) ways to attain equality. If \(z\ge r\), equality with \(2^{z+1}\) is impossible, and integrality of \(f\) and \(s\) forces \(f\ge s\), so \(P_A(1)\le2^z\). A contiguous one-run occupying the first \(r\) positions has exactly one neighboring zero when \(z>0\), giving \(s=f=1\) and attaining \(2^z\). The boundary case \(z=0\) lies in the first regime and gives \(2\), as required.

## Verification
The standalone `verify.py` performs two independent finite checks. It constructs each map as an explicit subset and compares the domains of both composed maps directly, then reconstructs its partner-rank profile by a separate run-factorization calculation. It also runs a four-state dynamic program to obtain the complete bivariate rank profiles without using the factorization. All three agree for \(1\le N\le8\), including \(65,536\) directly tested ordered pairs at \(N=8\). A further census for \(1\le N\le10\) independently verifies the prescribed-rank maximum and the number of maximizers in its first regime. Execute `python3 verify.py` using only the standard library. The recorded output ends in `VERIFY_OK`. These finite tests support, but cannot replace, the all-\(n\) proofs above.

## Relationship to prior work
Ayık, Ayık and Fernandes [1], Theorem 7 and its definition of \(F_r\), give the indispensable minimal-generating-set characterization and the rank \(\binom{n-1}{r}\) of the shift-one stratum. The paper's statements concern ideal generators, ranks and presentations, not commuting-partner rank distributions or the local edge compatibility and its rational census. The foundational order-decreasing partial-isometry study [2] treats cardinality and Green-type structure, not the stated pair enumerator.

Published work [3] computes the rank distribution of an unrestricted product of two random *full-family* order-preserving partial isometries; its factors vary over shifts in both directions. Our conditional commutation counts only two shift-one factors and is neither the same statistic nor an immediate coefficient specialization of that product-rank law. Work [4] counts nonzero-product commuting pairs for *interval-supported* translations. Here supports are arbitrary subsets, and our partner polynomial records rank for each fixed support pattern; the interval-only count cannot determine those data. Related nilpotency-height and symmetric-inverse centralizer results involve different operations or ambient families. The searches and inspected sources do not establish universal historical priority.

## Limitations
Only the shift-one subset \(B_n\) is considered; the results do not enumerate commuting pairs across all shifts, nor the centralizer in the entire order-decreasing semigroup. The rank-specific maximum for \(z\ge r\) is given with a construction, not a complete classification of all maximizers. Previous results may imply special cases under an unrecognized rephrasing; in particular wider symmetric-inverse-monoid centralizer literature and older restricted-transformation literature leave a residual priority risk. All tests are finite and no independent mathematical audit has been performed.

## References
1. G. Ayık, H. Ayık and V. H. Fernandes, *On semigroups of order-decreasing partial isometries: presentations and ranks of certain ideals*, arXiv:2611.12150v1 (first public posting 9 November 2026), Section 2, Theorem 7. https://arxiv.org/html/2611.12150v1
2. R. Kehinde, S. O. Makanjuola and A. Umar, *On the semigroup of order-decreasing partial isometries of a finite chain*, arXiv:1101.2558v1 (13 January 2011). https://arxiv.org/abs/1101.2558
3. *The product-rank law of finite-chain partial translations*, published mathematical research record, 26 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-the-product-rank-law-of-finite-chain-partial-translations--849553a20428
4. *Exact nonzero-product commuting pairs in interval-translation rook monoids*, published mathematical research record, 2 November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-nonzero-product-commuting-pairs-in-interval-translation-ro--12e310078e35
