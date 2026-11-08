# Shattering complexes of finite onto maps: a duplicate-color criterion and a matroid boundary

## Finding

Let \(n>q\ge 2\) be integers. Write \([n]=\{1,\ldots,n\}\), let \(\mathcal S_{n,q}\) be the set of all surjections \(f:[n]\to[q]\), and regard each \(f\) as the binary incidence set \(G_f=\{(i,f(i)):i\in[n]\}\subseteq[n]\times[q]\). A support \(E\subseteq[n]\times[q]\) is *shattered* if \(\{E\cap G_f:f\in\mathcal S_{n,q}\}=2^E\).

**Complete criterion.** A support \(E\) is shattered if and only if (a) each row \(\{i\}\times[q]\) contains at most one element of \(E\), (b) \(s=|E|<n\), and (c) \(s-d(E)\le n-q\), where \(d(E)\) is the number of different colors appearing as second coordinates of \(E\). The nonnegative quantity \(s-d(E)\) measures color repetitions among the tested rows.

**Complete face enumerator.** Write \(\left\{\begin{smallmatrix}s\\d\end{smallmatrix}\right\}\) for a Stirling number of the second kind, with \(\left\{\begin{smallmatrix}0\\0\end{smallmatrix}\right\}=1\), and \((q)_{\underline d}=q!/(q-d)!\). The polynomial counting shattered supports by size is
\[
\Phi_{n,q}(z)=\sum_{s=0}^{n-1}\binom ns z^s
 \sum_{d=\max(0,s-n+q)}^{\min(s,q)}
 (q)_{\underline d}\left\{\begin{matrix}s\\d\end{matrix}\right\}.
\]

**Purity, facet count, and matroid boundary.** Every inclusion-maximal shattered support has exactly \(n-1\) elements. The number of maximal supports is
\[
 n q!\left(\left\{\begin{matrix}n-1\\q-1\end{matrix}\right\}+\left\{\begin{matrix}n-1\\q\end{matrix}\right\}\right).
\]
In particular \(\operatorname{VCdim}(\mathcal S_{n,q})=n-1\), independent of \(q\). As an abstract independence complex on \([n]\times[q]\), the shattered-support complex is a matroid complex if and only if \(q=2\). For \(q=2\) it is precisely the rank-\((n-1)\) truncation of the row-partition matroid. For every \(3\le q<n\), its maximal supports fail basis exchange.

## Assumptions and scope

Every row of an incidence graph has exactly one positive edge; every color must occur at least once in a concept. The support itself need not be a graph of a function before testing shattering. Only ordinary binary edge-membership shattering is considered; multivalued label shattering, online shattering, and arbitrary lower-bounded color multiplicities are not asserted. The theorem deliberately treats \(q<n\): the bijective boundary \(n=q\) is a distinct, previously considered perfect-matching setting. The formulas extend to \(n=q\ge2\) by the same proof, but that boundary is not asserted as a separate novelty claim.

## Proof

**1. Necessity.** If two tested edges share a row, their labels cannot both be positive. Thus a shattered support contains at most one edge per row. If there is a tested edge in every row, choose a color \(c\) present in the tests, label all tested edges of color \(c\) negative, and label all other tested edges positive. Every row then either excludes \(c\) or is fixed to a different color, contradicting surjectivity. Thus \(s<n\). Finally the all-positive labeling fixes \(s\) rows to only \(d(E)\) different colors. The \(n-s\) untested rows can introduce at most \(n-s\) additional colors, so \(q\le d(E)+n-s\), equivalent to (c).

**2. Sufficiency.** Suppose (a)--(c) hold. Choose any subset \(P\subseteq E\) to be labeled positive. Fix the corresponding rows to their designated colors; let \(p=|P|\) and let \(t\) be the number of different positive colors. Since adjoining a test can only maintain or increase the number of repeated colors, \(p-t\le s-d(E)\le n-q\). Hence the \(m=n-p\) remaining rows outnumber or equal the \(k=q-t\) colors not yet present. Each remaining tested row forbids at most its one negative queried color; untested rows forbid nothing. In the bipartite graph between the \(k\) missing colors and the \(m\) remaining rows, any subset of at least two colors is adjacent to *every* remaining row, since a row forbids at most one color. A singleton missing color is adjacent to at least one row, because \(s<n\) guarantees an untested row outside \(P\). Thus Hall's condition holds for every subset of missing colors: for subsets of size at least two, \(m\ge k\), and for singletons an untested row is available. A matching assigns each missing color to a different remaining row. Fill any other remaining row with any allowed color (at least one exists because \(q\ge2\)). This extends the chosen labeling to a surjection. Because \(P\) was arbitrary, \(E\) is shattered.

**3. Enumeration and purity.** To count supports of size \(s\), choose \(s\) distinct rows and a color function on them. Such a function using exactly \(d\) colors has \((q)_{\underline d}\left\{\begin{smallmatrix}s\\d\end{smallmatrix}\right\}\) choices. The criterion gives exactly the displayed bounds on \(s,d\). Every shattered set of size \(s\le n-2\) extends: choose an unused row and, if \(d<q\), test a previously unused color so \(s-d\) stays unchanged; if \(d=q\), add any test, and note \((s+1)-d\le(n-1)-q<n-q\). All maximal supports therefore have size \(n-1\). For such a support, condition (c) is exactly \(d\ge q-1\). The facet formula follows by counting the possibilities \(d=q-1,q\); there are supports of this size, proving the VC formula.

**4. Matroid boundary.** If \(q=2\), a row-distinct support of size \(s\le n-1\) automatically has \(s-d(E)\le n-2\); thus the complex is the rank-\((n-1)\) truncation of the partition matroid with row classes of size two. Suppose now \(3\le q<n\). Choose a maximal support \(A\) using rows \(1,\ldots,n-1\), with test \((1,q-1)\) and all other tests using exactly the colors \(1,\ldots,q-2\). Choose a maximal support \(B\) using rows \(2,\ldots,n\), whose test in row \(n\) uses color \(1\), while tests in rows \(2,\ldots,n-1\) use every color \(1,\ldots,q-1\) at least once. Both choices exist because \(n-2\ge q-1\) and both have at least \(q-1\) distinct colors, so both are shattered facets. Remove \(e=(1,q-1)\) from \(A\). Every element of \(B\setminus A\) on a row \(2,\ldots,n-1\) conflicts with its existing row test. The only other candidate is \((n,1)\), but adjoining it produces a size-\((n-1)\) set with only \(q-2\) colors, which violates (c). Hence no element of \(B\setminus A\) exchanges for \(e\), contradicting the matroid basis-exchange axiom. Therefore the complex is not matroidal for any \(3\le q<n\).

## Verification

Run \(\texttt{python3 verify\_surjection.py}\) in the directory containing the accompanying script; no third-party packages are required. The script constructs every surjective function for the tested parameter pairs, enumerates *every* candidate support (including supports with multiple tests in one row), computes all traces directly, and independently compares with the proposed criterion and Stirling coefficients. Exhaustive cases are \((n,q)=(2,2),(3,2),(3,3),(4,2),(4,3),(4,4),(5,2),(5,3)\), totaling 104,272 supports. It also checks explicit basis-exchange counterexamples for \(3\le q\le5\) and \(q\le n\le8\), including the bijective boundary. This is finite corroboration; the unrestricted assertions follow from the foregoing proof.

## Relationship to prior work

Leboeuf, LeBlanc and Marchand (2022), especially Section 5.3 and Theorem 10, analyze equality tests on nominal categorical features and upper-bound the two-partitioning functions of decision stumps. That setting permits arbitrary categorical samples rather than the global every-color-used constraint of the present onto-function family. Godbole, Pinella and Zhuang (2013), Sections 1--3, study covering-array and permutation-pattern shattering by random collections of words/permutations, not binary incidences of the entire family of onto maps. Bucic, Devlin, Hendon, Horne and Lund (2019) study intersections and counts of perfect matchings and derangements, not these onto-function shattered supports. Existing exact results for derangement incidence and permutation assignments address the bijective or forbidden-diagonal boundary; they do not imply the repeated-color condition or the nonmatroid transition for \(q<n\).

The contribution claimed here is the *complete all-parameter support classification for surjections with strictly more rows than colors*, its Stirling face enumerator and purity, and the exact matroid/nonmatroid boundary. Neither the definition of surjection, Hall's theorem, Stirling numbers, nor perfect-matching counting is claimed as new.

## Limitations

The result is confined to binary graph-incidence queries on all onto functions \([n]\to[q]\) with \(n>q\ge2\). It does not determine Littlestone dimensions, induced topology or homology of the complexes, nor capacities when different colors have imposed quotas. The primary sources inspected do not state the present full classification; nonetheless, equivalent terminology in unindexed combinatorial literature may yield earlier coverage. Independent expert validation and comprehensive historical-priority certification have not occurred.

## References

- J.-S. Leboeuf, F. LeBlanc, M. Marchand, *Generalization Properties of Decision Trees on Real-valued and Categorical Features*, arXiv:2210.10781, first submitted 2022-10-18; Section 5.3, Theorem 10.
- A. P. Godbole, S. Pinella, Y. Zhuang, *Shattering Thresholds for Random Systems of Sets, Words, and Permutations*, arXiv:1301.6371, first posted 2013-01-29; Sections 1--3.
- M. Bucic, P. Devlin, M. Hendon, D. Horne, B. Lund, *Perfect matchings and derangements on graphs*, arXiv:1906.05908, first posted 2019-06-13; Introduction and Theorems 1--3.
- P. Hall, *On Representatives of Subsets*, Journal of the London Mathematical Society (1935); Hall's marriage theorem (standard ingredient).
