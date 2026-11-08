# Nilpotent rank spectra and a binomial law for cycle partial isometries

## Finding

For every integer \(n\ge3\), let \(\mathcal D_n\) be the inverse monoid of all partial isometries of the cycle graph \(C_n\), with ordinary graph distance. Let \(\rho(f)=|\operatorname{dom}f|\), and call \(f\) nilpotent when \(f^k=\varnothing\) for some positive integer \(k\). The empty partial map is included among nilpotents. Define
\[
N_n(x)=\sum_{\substack{f\in\mathcal D_n\\ f\text{ nilpotent}}}x^{\rho(f)},\qquad A_d(x)=(1+x)^d-x^d.
\]
For Euler's totient function \(\varphi\), put
\[
S_n(x)=\sum_{d\mid n}\varphi(d)A_d(x)^{n/d}+\begin{cases}
n(1+2x)^{(n-1)/2},&n\text{ odd},\\
\dfrac n2\left((1+2x)^{n/2}+(1+2x)^{(n-2)/2}\right),&n\text{ even}.
\end{cases}
\]
Then the complete nilpotent domain-rank polynomial is
\[
\boxed{N_n(x)=S_n(x)-(2n-1)-n(n-1)x-\mathbf 1_{2\mid n}\,\frac{n(n-2)}2 x^2.}
\]
Thus each coefficient counts the distinct nilpotent partial isometries of that rank, without duplicating maps that admit two dihedral extensions. Write \(M_n=|\mathcal D_n|\); the previously known cardinality is
\[
M_n=2n2^n-n^2-2n+1-\mathbf1_{2\mid n}\,\frac{n^2}{2}.
\]
The density and the whole typical rank distribution satisfy
\[
\boxed{\frac{N_n(1)}{M_n}\longrightarrow\frac12,\qquad
\bigl\|\mathcal L(\rho(F_n))-\operatorname{Bin}(n,1/2)\bigr\|_{\mathrm{TV}}
=O\!\left(\frac{(\log n)^2}{n}\right),}
\]
where \(F_n\) is uniform among the distinct nilpotent members of \(\mathcal D_n\). In particular,
\[
\frac{\rho(F_n)-n/2}{\sqrt n/2}\ \Longrightarrow\ \mathcal N(0,1).
\]

## Assumptions and scope

All statements concern finite simple cycles \(C_n\), \(n\ge3\), and partial bijections preserving the graph's geodesic distance. The monoid's elements are maps, not presentations by a pair consisting of a dihedral permutation and a chosen domain. A map can have multiple presentations at small domain ranks, which the polynomial explicitly corrects. Composition is ordinary partial-map composition; \(\varnothing\) denotes its zero map. Binomial distribution here refers to the number of vertices in a uniformly sampled subset of an \(n\)-element set.

## Proof

**1. Reduction to dihedral permutations and orbit avoidance.** Fernandes and Paulista prove for \(n\ge4\) that every element of \(\mathcal D_n\) is a restriction \(\sigma|_E\) of a rotation or reflection \(\sigma\) of the cycle to an arbitrary vertex subset \(E\). The same assertion for \(n=3\) is immediate because the triangle has the full symmetric group \(S_3=D_6\) as its isometry group. The directed functional graph of \(\sigma|_E\) consists of paths and cycles. It has a directed cycle exactly when \(E\) contains an entire cycle of the permutation \(\sigma\): a cycle in the restriction must follow an orbit of \(\sigma\), and an included orbit yields a cycle. A finite partial injection is nilpotent precisely when it has no directed cycle. Consequently, if the disjoint cycles of \(\sigma\) have lengths \(d_1,\ldots,d_s\), the rank enumerator of its nilpotent restrictions is \(\prod_{j=1}^s((1+x)^{d_j}-x^{d_j})\). All assertions include empty restrictions.

**2. Enumeration before identifying coincident restrictions.** There are exactly \(\varphi(d)\) rotations of permutation order \(d\) for each divisor \(d\mid n\); each has \(n/d\) cycles of length \(d\). Their sum is the first term of \(S_n(x)\). For odd \(n\), each of the \(n\) reflections has one fixed vertex and \((n-1)/2\) transposed pairs; the fixed vertex must be excluded, and each transposed pair contributes \(1+2x\). For even \(n\), half the reflections have two fixed vertices and \((n-2)/2\) transposed pairs, while the other half have no fixed vertices and \(n/2\) transposed pairs. This gives exactly the remaining terms of \(S_n(x)\).

**3. Removing all duplicates.** The original dihedral-extension theorem also shows that every nonempty rank-one partial isometry has two dihedral extensions. If \(n\) is even, rank-two maps with antipodal domain vertices likewise have two; every other nonempty map has one. The empty map is counted \(2n\) times and is nilpotent, so subtract \(2n-1\). Every singleton map \(i\mapsto j\) with \(i\ne j\) is nilpotent, while \(i\mapsto i\) is not; the first set comprises exactly \(n(n-1)\) distinct maps, each counted twice. If \(n\) is even, there are \(n/2\) antipodal source pairs. A map from one antipodal pair to another has two possible bijections. Such a map is nilpotent exactly when the target pair is different from the source pair: different antipodal pairs are disjoint, while a map between the same pair has a permutation cycle. Hence the duplicated nilpotent rank-two maps number \(2(n/2)(n/2-1)=n(n-2)/2\). No further duplicate is possible, proving the boxed polynomial. The displayed cardinality \(M_n\) is the known count of all distinct maps.

**4. Typical rotations are nilpotent.** Sample independently a uniform rotation \(\sigma\) of \(C_n\) and a uniform subset \(E\) of its vertices. Then \(|E|\sim\operatorname{Bin}(n,1/2)\). Set \(T=\lceil2\log_2 n\rceil\). The proportion of rotations of order at most \(T\) is bounded by \(n^{-1}\sum_{d\le T}d=O((\log n)^2/n)\). If the rotation has order \(d>T\), a union bound over its \(n/d\) orbits shows that \(\Pr(\sigma|_E\text{ is not nilpotent}\mid\sigma)\le(n/d)2^{-d}\le n2^{-T}=O(1/n)\). It follows that the proportion of labeled rotation restrictions that are nilpotent is \(1-O((\log n)^2/n)\).

**5. Quotienting rotation presentations and bounding reflection contributions.** Every nonempty restriction of a rotation has a unique rotation extension, because distinct rotations disagree at every vertex. The only duplication within rotation presentations is the empty restriction, with \(n\) presentations. Thus the number of distinct nilpotent rotation restrictions is \(n2^n(1-O((\log n)^2/n))\); removing nonnilpotent presentations and identifying the empty map changes the binomial rank distribution by total variation at most \(O((\log n)^2/n)\). Any reflection admits at most \(3^{n/2}\) nilpotent domain choices: its transposed pairs contribute three choices each and its fixed vertices contribute one. Across all reflections this gives at most \(n3^{n/2}\) additional distinct nilpotent maps, exponentially smaller than \(n2^n\). Adding these maps changes the normalized rank distribution by \(O((\sqrt3/2)^n)\), which is absorbed in the claimed error. Therefore the total-variation estimate holds. Since \(M_n=2n2^n-O(n^2)\), the nilpotent density tends to one-half. Finally the classical binomial central limit theorem transfers through total variation to \(\rho(F_n)\).

## Verification

The accompanying dependency-free `verify.py` independently constructs all restrictions of all \(2n\) dihedral permutations, deduplicates by their actual partial-map arrays, detects directed cycles by iterating each partial map, and compares every coefficient with the exact formula. It also compares the cardinality with the previously established monoid formula. All cases \(3\le n\le11\) pass and the program prints `VERIFY_OK`. For example, the coefficient vectors for \(n=4\) and \(n=6\), in ascending rank order, are respectively \((1,12,20,8,0)\) and \((1,30,108,108,48,12,0)\). These finite calculations corroborate but do not prove the all-size assertions.

## Relationship to prior work

Fernandes and Paulista (2022 preprint; 2023 journal article) prove that cycle partial isometries are exactly dihedral restrictions, determine their total cardinality and structural relations, and thereby supply essential premises for the present enumeration. Their total monoid cardinality is not claimed as new here. Dimitrova, Fernandes, Koppitz, and Quinteiro (2023 preprint) analyze three orientation/monotonicity submonoids, including their cardinalities, Green's relations and ranks. The inspected full texts do not assert this nilpotent rank spectrum, half-density limit, or binomial total-variation law. Search evidence does not establish worldwide priority; the general cycle-index treatment of restrictions or an unlocated semigroup enumerator could imply the finite formula. Novelty and journal priority remain provisional pending external review.

## Limitations

The results apply to entire partial-isometry monoids of ordinary cycle graphs, not arbitrary graphs, full symmetric inverse monoids, or other metrics. The total-variation rate is a proved upper bound, not claimed optimal. No limiting law for nilpotency **index** is asserted. Rank refers to domain size, not minimum generating-set cardinality. The contribution is self-reviewed and not independently audited.

## References

1. V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a cycle graph*, arXiv:2205.02196 (first publicly posted 2022-05-04); Turkish Journal of Mathematics **47** (2023), 1746–1760, DOI:10.55730/1300-0098.3460. Full text: https://arxiv.org/pdf/2205.02196.
2. I. Dimitrova, V. H. Fernandes, J. Koppitz, and T. M. Quinteiro, *On three submonoids of the dihedral inverse monoid on a finite set*, arXiv:2301.01519 (2023). Full text: https://arxiv.org/pdf/2301.01519.
