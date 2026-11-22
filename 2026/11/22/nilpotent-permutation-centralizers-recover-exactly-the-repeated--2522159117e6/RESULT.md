# Nilpotent permutation centralizers recover exactly the repeated cycle lengths

## Finding
Let \(n\geq1\), let \(\sigma\in S_n\), and let \(\mathcal I_n\) denote the inverse monoid of all partial bijections of \(\{1,\ldots,n\}\), including the empty map \(0\). For every integer \(d\geq1\), let \(r_d(\sigma)\) be the number of cycles of length \(d\) in \(\sigma\), including fixed-point cycles. Define the nilpotent-centralizer rank polynomial
\[
P_\sigma(z)=\sum_{\substack{f\in\mathcal I_n:\ f\sigma=\sigma f,\\ f^j=0\text{ for some }j\geq1}}z^{|\operatorname{dom} f|}.
\]
Then
\[
\boxed{P_\sigma(z)=\prod_{d:r_d>0}\left(\sum_{k=0}^{r_d-1}\binom{r_d-1}{k}\frac{r_d!}{(r_d-k)!}\,d^kz^{dk}\right).}
\]
More strongly, for any two permutations \(\sigma\) and \(\tau\), even of different positive degrees,
\[
\boxed{P_\sigma=P_\tau\quad\Longleftrightarrow\quad
r_d(\sigma)=r_d(\tau)\text{ whenever }\max\{r_d(\sigma),r_d(\tau)\}\geq2.}
\]
Equivalently, this polynomial determines every repeated cycle length and its exact multiplicity, while individual cycle lengths that occur only once make no contribution whatsoever. Thus it is a complete invariant of the repeated-cycle profile, but not of permutation conjugacy.

There is also a simultaneous exact domain-rank and nilpotency-index law. For integer \(s\geq1\), let \(P_{\sigma,\leq s}(z)\) count the same maps with \(f^s=0\). Then
\[
\boxed{P_{\sigma,\leq s}(z)=\prod_{d:r_d>0}r_d!\,[u^{r_d}]\exp\left(\sum_{j=1}^{s}d^{j-1}u^jz^{d(j-1)}\right).}
\]
The exact-index-\(s\) polynomial is \(P_{\sigma,\leq s}-P_{\sigma,\leq s-1}\) (with \(P_{\sigma,\leq0}=0\)). The largest possible nilpotency index is \(\max\{r_d:r_d>0\}\), and the largest possible domain rank is \(\sum_{d:r_d>0}d(r_d-1)\).

## Assumptions and scope
All sets are finite, \(n\geq1\), and composition of partial maps is understood with undefined values remaining undefined. Commutation is equality as partial maps, including equality of their domains. A partial map is nilpotent if one of its positive powers is empty, not merely if it fails to be invertible. All products and exponential coefficients are formal polynomial or formal-power-series identities with integer coefficients; the exponential notation is shorthand for a finite coefficient extraction and does not require a field of characteristic zero in the underlying semigroup. The polynomial is not normalized by the total number of commuting maps. A fixed-point cycle counts as a cycle of length one.

## Proof
**Orbit restriction and phase labels.** Since \(\sigma\) is total and invertible, the equality \(f\sigma=\sigma f\) implies \(\sigma^{-1}(\operatorname{dom} f)=\operatorname{dom} f\). Hence the domain is a union of full cycles of \(\sigma\). Equivariance maps any domain cycle of size \(d\) onto one cycle of the same size: the image is one transitive \(\langle\sigma\rangle\)-orbit and the injectivity of \(f\) forces equal cardinality. Different domain cycles have disjoint image cycles. Once an ordered domain cycle, a target cycle, and cyclic origins are fixed, there are exactly \(d\) possible equivariant bijections. Conversely, each such choice commutes with \(\sigma\). Therefore the centralizer within \(\mathcal I_n\) is a direct product, over distinct \(d\), of partial injections on \(r_d\) cycle labels with \(d\) independent phase choices on each arrow.

**Nilpotence.** A partial injection on finitely many labels decomposes uniquely into directed cycles and finite directed chains (isolated vertices are chains of length one). If there is a directed cycle, then a power of the original point map permutes the corresponding nonempty union of \(\sigma\)-cycles, so the map is not nilpotent. With no directed cycle, each chain eventually leaves its domain; hence a sufficiently high power is empty. The nilpotency index equals the largest number of vertices of a label-chain (not the number of point-level vertices in its \(\sigma\)-orbits).

**Rank enumeration.** A nilpotent partial injection on \(r\) labeled vertices with exactly \(k\) arrows has exactly \(r-k\) chain components, including isolated vertices. Placing \(r\) labels in linearly ordered nonempty blocks, disregarding order among blocks, gives the unsigned Lah count
\[
L(r,r-k)=\binom{r-1}{k}\frac{r!}{(r-k)!},\qquad 0\leq k\leq r-1.
\]
Each of its \(k\) arrows receives one of \(d\) phase labels and contributes \(d\) points to \(\operatorname{dom} f\). Thus the factor for orbit length \(d\) is precisely \(\sum_k L(r_d,r_d-k)d^kz^{dk}\), and different lengths multiply. Taking every chain into one block realizes the maximal domain rank.

**Nilpotency-index refinement.** For a fixed \(d\), a chain with \(j\) label vertices contributes \(d^{j-1}z^{d(j-1)}\). An unordered collection of such chains, each with an internal linear order, is counted by the exponential formula, giving \(r_d![u^{r_d}]\exp(\sum_{j=1}^{s}d^{j-1}u^jz^{d(j-1)})\) when no chain has more than \(s\) vertices. Multiplication across \(d\) and subtraction of successive cutoffs give the stated joint law and the sharp maximal index.

**Reconstruction and exact ambiguity.** Let \(F_{d,r}(z)\) denote the displayed factor for a multiplicity \(r\), with \(F_{d,0}=F_{d,1}=1\). For \(r\geq2\),
\[
[z^d]F_{d,r}(z)=d\,r(r-1),
\]
and every other nonconstant term of this factor has degree at least \(2d\). Reconstruct in increasing \(d\). After dividing the already reconstructed factors for lengths below \(d\), all factors with larger lengths have constant term one and no term of degree at most \(d\). Therefore the remaining coefficient of \(z^d\) is \(d\,r_d(r_d-1)\). If this is positive, it determines the unique integer \(r_d\geq2\) (explicitly, \(r_d=(1+\sqrt{1+4[z^d]P_{\rm residual}/d})/2\)); divide out \(F_{d,r_d}\) and continue. If zero, \(r_d\leq1\). This recovers all repeated multiplicities and proves necessity of the equivalence. Conversely, factors for multiplicities zero or one are identically one, so changing any singly occurring cycle lengths leaves the polynomial unchanged. This proves sufficiency and the sharp information-loss statement.

## Verification
The companion `verify.py` independently enumerates every partial injection on selected sets of at most six points, checks commuting relations as partial maps, computes nilpotency indices by iterating each map, and compares the resulting rank/index counts with a separate chain-multiplicity generating-function calculation. It checks exact reconstruction of repeated cycle multiplicities. Tested types include \((1^6)\), \((2^3)\), \((3^2)\), \((2^2,1^2)\), and mixed unequal cycle lengths. The output terminates with `NILPOTENT_PERMUTATION_CENTRALIZER_CHECKS_PASSED`.

Examples: for cycle type \((2,2,2)\), \(P(z)=1+12z^2+24z^4\); for \((5)\) and \((4,1)\), both polynomials equal \(1\). For type \((2,2,2,5,5,7)\), the polynomial is \((1+12z^2+24z^4)(1+10z^5)\), showing explicitly that the solitary seven-cycle disappears. These finite checks corroborate but are not the proof of the all-degree statements.

## Relationship to prior work
The 2023 paper of Elliott, Levine, and Mitchell systematically counts isomorphism types of monogenic inverse submonoids and describes chain/cycle decompositions of partial permutations. Its objects are monogenic submonoids, not nilpotent elements commuting with a specified permutation, and its theorem does not reconstruct repeated cycle multiplicities from their nilpotent rank polynomial.

Lipscomb's 1988 work determines the structural wreath-product decomposition of permutation centralizers in symmetric inverse semigroups; the orbit/phase restriction used here belongs to that existing structural theory and is not claimed as new. Konieczny's 1999 paper concerns Green's relations in permutation centralizers of all partial transformations; the displayed centralizer characterization is consistent with its Theorem 2.1, but the present statistic restricts to injective nilpotent maps. The enumerative Lah-number ingredient is classical. The assessed mathematical point is the complete equivalence classification for the compressed nilpotent rank statistic and its simultaneous index refinement.

A published result on centralizers of **nilpotent** partial injections instead recovers a nilpotent element's chain partition from the rank distribution of **all** commuting partial injections; neither its input class nor its counted maps match the current theorem. A published permutation-centralizer **idempotent** enumeration concerns noninjective total maps and image-rank, not this inverse-monoid nilpotence statistic.

## Limitations
This result does not recover singly occurring cycle lengths: even at the same degree, a five-cycle and a disjoint four-cycle plus a fixed point both give \(P(z)=1\). The factorization is derived from established permutation-centralizer structure and classical Lah enumeration, and the independent contribution should be understood as the exact information-recovery/ambiguity classification rather than rediscovery of either ingredient. Full text for some older structural/isomorphism papers was not obtained; priority beyond the inspected comparisons is not claimed. No independent mathematical audit has been performed.

## References
1. L. Elliott, A. Levine, J. D. Mitchell, *Counting monogenic monoids and inverse monoids*, arXiv:2303.12387 (first publicly posted 2023-03-22), https://arxiv.org/abs/2303.12387.
2. S. L. Lipscomb, *The structure of the centralizer of a permutation*, Semigroup Forum 37 (1988), 301–312, doi:10.1007/BF02573142.
3. S. L. Lipscomb, *Centralizers in symmetric inverse semigroups: structure and order*, Semigroup Forum 44 (1992), 347–355, doi:10.1007/BF02574354.
4. J. Konieczny, *Green's relations and regularity in centralizers of permutations*, Glasgow Math. J. 41 (1999), 45–57, doi:10.1017/S0017089599970301.
5. W. Huang, X. Yang, *Isomorphisms of centralizers of group element on the finite symmetric inverse semigroup*, 2009, bibliographic record https://portal.mardi4nfdi.de/wiki/Isomorphisms_of_centralizers_of_group_element_on_the_finite_symmetric_inverse_semigroup.
