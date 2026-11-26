# Rank and nilpotency-index spectra in permutation centralizers of the symmetric inverse monoid

## Finding
Let \(n\ge1\), let \(\sigma\in S_n\) have exactly \(m_\ell\) cycles of length \(\ell\), and let \(\mathcal I_n\) be the symmetric inverse monoid of partial injections of \(\{1,\ldots,n\}\). Its zero is the empty map. The centralizer is \(C(\sigma)=\{\beta\in\mathcal I_n:\beta\sigma=\sigma\beta\}\). For any \(h\ge1\), define the polynomial
\[
 F_{\sigma,h}(T)=\sum_{\substack{\beta\in C(\sigma)\\\beta^h=0}}T^{\operatorname{rank}\beta},
 \qquad \operatorname{rank}\beta=|\operatorname{dom}\beta|.
\]
Here all powers are compositions, and the nilpotency index of \(\beta\) is the least \(h\ge1\) for which \(\beta^h=0\). **Theorem:** for every permutation and every positive integer \(h\),
\[
 \boxed{F_{\sigma,h}(T)=\prod_{\ell:m_\ell>0}m_\ell!\,[z^{m_\ell}]\exp\left(\sum_{j=1}^{h}\ell^{j-1}T^{\ell(j-1)}z^j\right).}
\]
The count at **exactly** index \(h\ge2\) is \(F_{\sigma,h}(T)-F_{\sigma,h-1}(T)\); at index one it is the monomial \(1\) from the empty map. This determines every joint rank/index multiplicity, not merely totals.

The set of ranks permitted under the index bound is **exactly**
\[
 \boxed{\left\{\sum_{\ell:m_\ell>0}\ell a_\ell:\ 0\le a_\ell\le m_\ell-\left\lceil m_\ell/h\right\rceil,\ a_\ell\in\mathbb Z\right\}.}
\]
Consequently the largest attainable rank is \(\sum_{\ell}\ell\bigl(m_\ell-\lceil m_\ell/h\rceil\bigr)\), and this bound is sharp. All commuting nilpotents satisfy \(\beta^H=0\) with \(H=\max\{m_\ell:m_\ell>0\}\). In particular their unbounded rank polynomial is
\[
 \boxed{F_{\sigma,H}(T)=\prod_{\ell:m_\ell>0}\sum_{k=1}^{m_\ell}\frac{m_\ell!}{k!}{m_\ell-1\choose k-1}\,\ell^{m_\ell-k}T^{\ell(m_\ell-k)}.}
\]
The factors are the standard unsigned Lah numbers with cycle-length weights. The identity-permutation specialization (all cycles of length one) is already part of the classical counting theory of nilpotent partial injections; the assessed result is its **simultaneous rank/index refinement inside arbitrary permutation centralizers** and its exact rank support.

For example, if \(\sigma\) has four disjoint two-cycles on eight letters, then
\[
 F_{\sigma,1}(T)=1,\quad F_{\sigma,2}(T)=1+24T^2+48T^4,\quad
 F_{\sigma,3}(T)=1+24T^2+144T^4,
\]
\[
 F_{\sigma,4}(T)=1+24T^2+144T^4+192T^6.
\]
Thus this centralizer contains \(361\) nilpotent partial injections, with exactly \(1,72,96,192\) of respective nilpotency indices \(1,2,3,4\).

## Assumptions and scope
The theorem applies to an arbitrary finite permutation \(\sigma\), including the identity, without restrictions on cycle lengths or their multiplicities. All counts are for labeled underlying points and partial injective transformations. The zero is the empty partial map, and \(\beta^1=0\) holds only for that map. The notation \([z^m]\) means coefficient extraction from a formal power series in \(z\); the exponential series has rational coefficients but the resulting polynomials have nonnegative integer coefficients. The product runs over positive \(\ell\) with \(m_\ell>0\).

## Proof
**1. Cycle-equivariant reduction.** Write composition as usual for functions. The equality \(\beta\sigma=\sigma\beta\) forces the domain of \(\beta\) to be \(\sigma\)-invariant: under the usual right-to-left composition convention, the domains of the two compositions are \(\sigma^{-1}(\operatorname{dom}\beta)\) and \(\operatorname{dom}\beta\), respectively. The image is also \(\sigma\)-invariant by equivariance and bijectivity of \(\sigma\). The restriction of \(\beta\) to any active source cycle of length \(\ell\) must injectively and equivariantly map that entire cycle onto a distinct target cycle of the same length: the target period divides \(\ell\) by equivariance and is at least \(\ell\) because the source points have distinct images. The restriction has exactly \(\ell\) possible phase shifts. Two different active source cycles cannot have the same target because \(\beta\) is injective. Conversely, a partial injection between the labeled cycles of each fixed length, equipped with independently selected phase shifts, uniquely defines an element of \(C(\sigma)\). Different cycle lengths are independent.

**2. Detecting nilpotency.** A partial injection on \(m_\ell\) cycle labels has directed graph consisting of disjoint directed paths and directed cycles, with isolated vertices counted as one-vertex paths. A directed cycle prevents nilpotency: following it yields a defined iterate indefinitely, regardless of its phases. If all components are paths, a path of \(j\) labels has \(j-1\) arrows, and \(\beta^{j-1}\) is defined somewhere if \(j>1\), whereas \(\beta^j\) is nowhere defined on that path. For a one-vertex path \(\beta^1\) is empty there. Therefore \(\beta^h=0\) if and only if every path, in every length class, has at most \(h\) vertices. The rank of \(\beta\) is the number of active source points, namely \(\sum_\ell\ell\,(\text{number of arrows on the length-}\ell\text{ label paths})\).

**3. Counting labeled paths.** Fix \(\ell\) and put \(m=m_\ell\). A directed path with \(j\) vertices on a specified \(j\)-element label set can be ordered in \(j!\) ways, and its \(j-1\) arrows admit \(\ell^{j-1}\) independent phase shifts. Its contribution to the rank variable is \(T^{\ell(j-1)}\). The exponential formula for unordered sets of disjoint labeled paths consequently gives
\[
 m!\,[z^m]\exp\left(\sum_{j=1}^{h}\ell^{j-1}T^{\ell(j-1)}z^j\right).
\]
Multiplying over the independent cycle-length classes proves the claimed generating polynomial. The exact-index counts follow by subtraction.

**4. Rank support and sharp extremum.** A path decomposition on \(m\) labels with exactly \(k\) components, each of size in \(\{1,\ldots,h\}\), exists if and only if \(k\le m\le hk\). It then has \(a=m-k\) arrows, so every integer \(a\) from \(0\) through \(m-\lceil m/h\rceil\) and no other integer occurs. Each arrow transfers \(\ell\) points, which proves the complete rank-support statement. Choosing the minimum possible \(k=\lceil m/h\rceil\) independently in each cycle-length class attains the bound. The largest possible path size over all classes is \(H=\max m_\ell\), so this is also the universal nilpotency cutoff.

**5. Closed unbounded formula.** Without a path-size restriction, a decomposition of \(m\) labeled points into \(k\) nonempty linearly ordered paths can be obtained by choosing a permutation and placing \(k-1\) separators into its \(m-1\) internal slots, then dividing by \(k!\) because the set of paths is unordered. The number is \(\frac{m!}{k!}{m-1\choose k-1}\). Since there are \(m-k\) arrows, assigning phase shifts and rank weights yields the boxed unsigned-Lah polynomial.

## Verification
The accompanying standalone `checker.py` needs only Python 3 and the standard library. Running `python3 checker.py` reconstructs the polynomial by an integer recurrence on the path containing the smallest label. It independently enumerates **every partial injection** on sets of size \(1\) through \(6\), checks commutation with a representative of **every permutation cycle type**, computes nilpotency indices by actual iteration and cycle detection, and compares every rank coefficient for each allowed bound. It also enumerates each equivariant partial injection on four two-cycles as an actual eight-point map and recovers the \(361\)-element example and all index strata. Finally, it independently checks the predicted sharp rank supports for many length/multiplicity/bound triples. The program returns `VERIFY_OK` when all checks pass. The finite checks support, but do not replace, the preceding general proof.

## Relationship to prior work
Gomes and Howie (1987), especially their Theorem 2.8, establish the classical chain decomposition and nilpotency index for partial injections. Laradji and Umar (2004) and Ganyushkin and Mazorchuk (2004) study classical unconditioned nilpotent counts and Lah numbers. These structural and enumerative facts are used, not newly asserted. Konieczny (2013), Theorem 3.4, characterizes general centralizer membership and includes the cycle-to-cycle equivariance underlying the present reduction. Konieczny (2020) treats centralizers and Green relations in the finite symmetric inverse semigroup. The present theorem gives an explicit arbitrary-cycle-type joint rank and index distribution in the centralizers of permutations and a sharp rank-support characterization. These formulas do not appear in the inspected material of the earlier sources; complete-text comparison with the 2020 article and both 2004 articles was not possible.

## Limitations
No result is asserted for centralizers of non-permutation partial maps; these can have additional domain-chain interactions. The theorem does not classify conjugacy classes of the counted maps. Its originality assessment remains conditional on an unresolved full-text comparison with the closely related 2020 finite-centralizers article and the older full enumerative literature. No claim of independent external audit is made.

## References
1. J. Konieczny, “The structure of centralizers in the finite symmetric inverse semigroup,” *Communications in Algebra* **48** (2020), 5181–5194, DOI: `10.1080/00927872.2020.1782926`. Online 2020-07-07.
2. J. Konieczny, “Centralisers in the infinite symmetric inverse semigroup,” *Bulletin of the Australian Mathematical Society* **87** (2013), 462–479, DOI: `10.1017/S0004972712000779`, especially Theorem 3.4.
3. G. M. S. Gomes and J. M. Howie, “Nilpotents in finite symmetric inverse semigroups,” *Proceedings of the Edinburgh Mathematical Society* **30** (1987), 383–395, DOI: `10.1017/S0013091500026778`, especially Theorem 2.8.
4. A. Laradji and A. Umar, “On the number of nilpotents in the partial symmetric semigroup,” *Communications in Algebra* **32** (2004), 3017–3023, DOI: `10.1081/AGB-120038637`.
5. O. Ganyushkin and V. Mazorchuk, “Combinatorics of nilpotents in symmetric inverse semigroups,” *Annals of Combinatorics* **8** (2004), 161–175, DOI: `10.1007/s00026-004-0213-7`.
