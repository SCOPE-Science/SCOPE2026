# Comparison shattering of stack-sortable permutations and a linear online gap

## Finding

Let \(\operatorname{Av}_n(231)\) be the permutations \(\pi\) of \([n]\) with no indices \(i<j<k\) satisfying \(\pi(k)<\pi(i)<\pi(j)\). For every pair of positions \(i<j\), define the binary query \(q_{ij}(\pi)=1\) if and only if \(\pi(i)<\pi(j)\). Write \(\mathcal H_n\) for this concept class on the set of all position-pair queries.

For every integer \(n\ge1\), a collection \(S\) of queries is VC-shattered by \(\mathcal H_n\) **if and only if it contains at most one query of the form \(q_{ij}\) for each fixed left endpoint \(i\)**. Consequently, the shattered-support complex is a partition-matroid independence complex, with parts of sizes \(n-1,n-2,\ldots,1\). Its complete enumerator is

\[
\Phi_n(z):=\sum_{S\text{ shattered}}z^{|S|}
=\prod_{j=1}^{n-1}(1+jz)
=\sum_{k=0}^{n-1}\left[{n\atop n-k}\right]z^k,
\]

where the brackets are the *unsigned* Stirling numbers of the first kind. In particular, \(\operatorname{VCdim}(\mathcal H_n)=n-1\) and there are exactly \((n-1)!\) maximum-size shattered supports.

The online behavior separates sharply. An explicit depth-eight binary query tree on \(\mathcal H_7\), provided in `depth8_tree.json`, proves

\[
\operatorname{Ldim}(\mathcal H_7)=8,
\qquad
\operatorname{VCdim}(\mathcal H_7)=6.
\]

For every integer \(q\ge1\),

\[
\operatorname{Ldim}(\mathcal H_{7q})\ge8q,
\qquad
\operatorname{Ldim}(\mathcal H_{7q})-\operatorname{VCdim}(\mathcal H_{7q})\ge q+1.
\]

Thus the Littlestone–VC gap grows *linearly* with permutation length within the Catalan class of permutations avoiding the pattern \(231\).

## Assumptions and scope

All permutations and comparison queries are **labeled by positions**. Queries ask whether the value at the smaller-index position is smaller than the value at the larger-index position, not whether a pair of symbols precedes one another in the inverse permutation. Shattering means that all \(2^{|S|}\) binary labelings of the fixed query support have witnesses in \(\operatorname{Av}_n(231)\). A Littlestone tree has the same binary comparison query at a node on both outgoing branches and requires a possibly different consistent hypothesis for every full root-to-leaf outcome string.

The all-order support classification applies to every integer \(n\ge1\), including the empty query domain at \(n=1\). The online lower bound is asserted only at positive multiples of seven; no all-order exact formula for Littlestone dimension is claimed.

## Proof

**1. Necessary restriction.** Fix \(i<j<k\). The labeling \(q_{ij}=1\) and \(q_{ik}=0\) would give \(\pi(j)>\pi(i)>\pi(k)\), exactly a forbidden \(231\) occurrence. Therefore two different queries with the same left endpoint cannot both lie in a shattered support. This proves necessity of the partition-matroid condition.

**2. Sufficient restriction.** Let \(S\) contain at most one query with each left endpoint. Fix any binary labeling \(b:S\to\{0,1\}\). Build a permutation from right to left. At step \(i\), insert the new first element as the **new minimum** among the suffix values if the unique query from \(i\) is labeled \(1\), as the **new maximum** if labeled \(0\), and as the new minimum if there is no such query. Standardize the suffix after each insertion to the consecutive value set.

The new value compares identically with *every* later value, so its query, if present, has precisely the prescribed label. The new element is the first position and an extremum; it cannot be the middle-ranked first member of a \(231\) triple. Thus insertion at the left preserves \(231\) avoidance. Induction yields a permutation realizing the entire labeling. Every support satisfying the restriction is therefore shattered.

**3. Enumerating all supports.** For left endpoint \(i\), there are \(n-i\) possible later positions and we may select zero or one of those queries. The independent choices give \(\prod_{i=1}^{n-1}(1+(n-i)z)\). The Stirling-number identity follows from the standard rising-factorial expansion. The largest support chooses one query from every nonempty part, so its size is \(n-1\) and its multiplicity \(\prod_{j=1}^{n-1}j=(n-1)!\).

**4. A finite exact online seed.** The attached file `depth8_tree.json` specifies, in breadth-first heap order, all \(255\) internal query labels of a complete depth-eight decision tree on seven positions. `verify.py` independently enumerates every \(231\)-avoiding permutation of length seven (exactly \(429\)) and tests every one of the \(256\) root-to-leaf response strings. Every leaf has at least one realizing permutation. This is a complete, finite witness to \(\operatorname{Ldim}(\mathcal H_7)\ge8\); no numerical extrapolation is used. Conversely, distinct leaves of any depth-nine shattered tree require at least \(512\) distinct hypotheses, exceeding \(429\), so \(\operatorname{Ldim}(\mathcal H_7)=8\).

**5. Amplification without an unproved induction.** If \(\pi\in\operatorname{Av}_r(231)\) and \(\sigma\in\operatorname{Av}_s(231)\), their direct sum \(\pi\oplus\sigma\) places the \(r\) values of \(\pi\) first, followed by the \(s\) values of \(\sigma\) each increased by \(r\). It avoids \(231\): a candidate triple entirely inside one block is forbidden by the corresponding component; a crossing triple cannot have its first entry between the other two in value, because all values in the first block are smaller than all values in the second block.

Take \(q\) independent seven-position blocks and restrict queries to those internal to each block. All tuples of local \(231\)-avoiders appear as direct-sum global hypotheses. Concatenate \(q\) copies of the certified depth-eight tree: after each leaf, attach the next tree on the next disjoint block. Every outcome path is realized by the direct sum of its independent local witnesses. Hence a complete depth-\(8q\) mistake tree exists on \(\mathcal H_{7q}\). The all-order formula gives \(\operatorname{VCdim}(\mathcal H_{7q})=7q-1\), proving the stated linear gap.

## Verification

The two standalone companion artifacts are `verify.py` and `depth8_tree.json`. Place them together and run `python3 verify.py`. The checker uses only the standard library. It directly enumerates all permutations of each length from one through eight, filters the forbidden \(231\) pattern, forms every query's incidence bitset, and grows all shattered supports using their full collections of nonempty traces. It compares each resulting coefficient to the stated product formula.

Separately, it loads the explicit query tree, checks its format and all \(256\) root-to-leaf label strings against all \(429\) avoiding permutations of length seven, and verifies the hypothesis-count bound excluding depth nine. On the packaged files, it printed `LENGTH_SEVEN_DEPTH_EIGHT_CERTIFICATE_PASS leaves=256 hypotheses=429` and `AV231_COMPARISON_SHATTERING_AND_ONLINE_GAP_PASS`.

The finite computation proves the depth-eight seed only because the entire explicit tree and *all* of its leaves are checked. The unbounded gap follows from the independent direct-sum proof, not from finite sampling.

## Relationship to prior work

Permutation pattern avoidance and stack-sortability are classical; no new enumeration of \(231\)-avoiding permutations is asserted. Kozma's 2019 preprint (subsequently developed with Berendsohn and Marx) addresses computational pattern matching and gives background for this family. Guingona, Kolesnikov, Nierwinski and Soucy (2021) study VC and Littlestone dimensions of **linear zero-set systems**, for which they obtain equality of the two dimensions; they do not derive the present comparison-relation classification or online separation.

Johnson and Wickes (2021) and Raz (2000) study permutation shattering in the *all-orderings-of-a-subset* sense. Here the instance domain consists of **individual pair comparisons**, and a set of query pairs is shattered when all binary labelings are possible; the quantifiers and resulting dimensions are different. Ghazi and collaborators' general online-dimension closure bounds do not furnish the exact seven-position certificate or the partition-matroid trace classification.

The main output is the conjunction of a coefficientwise shattering classification and a concrete, linearly amplifiable adaptive separation. Searches under pairwise-comparison, inversion-relation, stack-sortable, Catalan, and online-shattering terminology did not identify a published theorem subsuming this statement.

## Limitations

The exact Littlestone dimension of \(\mathcal H_n\) is **not determined for every** \(n\). The finite depth-eight certificate should be checked independently before attributing final priority. The support-polynomial argument is elementary once its correct instance domain is fixed; the less immediate contribution is the strict online seed and its linear propagation. Results expressed in alternate permutation-learning or inversion-system language might already cover some or all claims and are a remaining historical-priority risk. No external independent mathematical audit was performed.

## References

- L. Kozma, *Faster and simpler algorithms for finding large patterns in permutations*, arXiv:1902.08809, first public version February 23, 2019; related later work: B. A. Berendsohn, L. Kozma, D. Marx, *Finding and counting permutations via CSPs*, arXiv:1908.04673, first version August 13, 2019, and *Algorithmica* 83 (2021), 2552–2577.
- V. Guingona, A. Kolesnikov, J. Nierwinski, R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805, first version September 10, 2021.
- J. R. Johnson, B. Wickes, *Shattering k-sets with Permutations*, arXiv:2112.01946, first version December 3, 2021.
- R. Raz, *VC-dimension of sets of permutations*, *Combinatorica* 20 (2000), 241–255, DOI: 10.1007/s004930070023.
- B. Ghazi, N. Golowich, R. Kumar, P. Manurangsi, *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, PMLR 132 (2021), 686–696.
