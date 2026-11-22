# All-arity type-spectrum blindness in homogeneous layered permutations

## Finding
Let \(\mathcal L\) be the countable Fraïssé limit of layered permutations, regarded as structures with two named linear orders. A finite layered permutation is a direct sum of nonempty decreasing blocks; in \(\mathcal L\), an old finite parameter structure \(A\) has a uniquely determined ordered list of layer sizes \((a_1,\ldots,a_k)\), all positive, with \(n=\sum_i a_i\ge1\). All points of \(A\) are individually named.

For every integer \(r\ge0\), let \(t_r(A)\) be the number of complete types over \(A\) of ordered \(r\)-tuples of new, pairwise distinct points outside \(A\). Then

\[
T_A(z):=\sum_{r\ge0}t_r(A)\frac{z^r}{r!}=\frac{(1-z)^{1-n}}{(1-2z)^{k+1}}.
\]

In particular
\[
t_1(A)=n+2k+1,\qquad t_2(A)=t_1(A)^2+n+4k+3.
\]
Thus the first two *numerical* counts determine \(n\) and \(k\) without either being supplied:
\[
k=\frac{t_2-t_1^2-t_1-2}{2},\qquad n=t_1-2k-1.
\]
Two finite bases have the same whole numerical injective extension spectrum if and only if they have the same \((n,k)\); this invariant is blind to the individual sizes and order of their layers. A single count cannot generally determine \((n,k)\): the one-block four-point base and two-block two-point base both have \(t_1=7\), but their respective \(t_2\) are \(60\) and \(62\). The first nonisomorphic bases of the *same size* with identical all-arity spectra occur at \(n=3\), with layer compositions \((1,2)\) and \((2,1)\), both with \(t_1=8\), \(t_2=78\).

## Assumptions and scope
A layered finite permutation is a pair \((<_{1},<_{2})\) of strict total orders on one finite set, for which the relation “the two orders reverse the pair” is an equivalence relation and its equivalence classes occur consecutively in the same order in both linear orders. Within each class the two orders are opposite. The unique ordered sequence of classes is the layer decomposition. This is Cameron's homogeneous class \(\mathcal J/\mathcal J^*\), consisting of permutations avoiding the patterns \(231\) and \(312\). Its limit is the lexicographic product of two copies of the dense order, with the inner order reversed in the second coordinate order.

There is also a direct pattern-popularity interpretation. If \(\mathcal L_m\) denotes the set of layered permutations on \(m\) canonically ordered positions, and \(\operatorname{occ}_A(\pi)\) counts induced occurrences of the old layered pattern \(A\) in \(\pi\), then \(t_r(A)=r!\sum_{\pi\in\mathcal L_{n+r}}\operatorname{occ}_A(\pi)\). The factor \(r!\) labels the remaining new coordinates. Hence the theorem equivalently classifies equipopularity **within the layered permutation class**, by \((n,k)\). This equivalence does not hold by replacing the ambient layered class with a larger permutation class.

The new tuple coordinates are ordered/labeled and pairwise distinct; they do not equal the individually named old parameters. By ultrahomogeneity, each finite induced extension pattern is exactly one complete type, and conversely each such pattern is realized. The counts include all internal relations among new coordinates, not just products of singleton types.

## Proof
Write the base's \(k\) nonempty old layers, in their common outer order, as \(B_1,\ldots,B_k\), with \(|B_i|=a_i\). Any layered extension has two disjoint kinds of new coordinates: those lying inside one of the old layers, and those lying in one of the \(k+1\) outer gaps between consecutive old layers or at the ends. No new-only layer can lie strictly inside an old layer without contradicting that the old points in it are pairwise reversed by the two orders.

For fixed \(j\ge0\) distinct labeled coordinates joining an old layer of size \(a\), choose their relative order in \(j!\) ways and then interleave that order with the fixed decreasing order of the \(a\) old labels in \(\binom{a+j}{j}\) ways. The exponential generating function for their placements is therefore
\[
\sum_{j\ge0}\binom{a+j}{j}z^j=(1-z)^{-a-1}.
\]
The product over all old layers is \((1-z)^{-n-k}\).

In any one of the \(k+1\) outer gaps, all new coordinates form an arbitrary *layered permutation*: an ordered sequence of nonempty decreasing layers. A single new-only layer, containing \(j\ge1\) labeled new coordinates, has \(j!\) admissible internal first orders; its exponential generating function is \(\sum_{j\ge1}z^j=z/(1-z)\). A possibly empty ordered sequence of such layers has exponential generating function
\[
\frac{1}{1-z/(1-z)}=\frac{1-z}{1-2z}.
\]
All old layers and gaps are separated by the fixed named old coordinates, so their structures combine bijectively by labeled disjoint distribution of the new coordinates. The labeled-product rule yields
\[
T_A(z)=(1-z)^{-n-k}\left(\frac{1-z}{1-2z}\right)^{k+1}=\frac{(1-z)^{1-n}}{(1-2z)^{k+1}}.
\]
The first two coefficients give the displayed formulas. Since \(n\ge1\), \(k\ge1\), their inversion is valid over integers, so equality of the entire numerical spectra is equivalent to equality of \((n,k)\). The opposite direction follows directly from the rational generating function. For \(n\le2\), each pair \((n,k)\) corresponds to exactly one ordered composition, whereas \(n=3,k=2\) admits the two distinct compositions \((1,2)\), \((2,1)\). They are nonisomorphic because the two named orders canonically distinguish the first layer; both share every \(t_r\). The two different-size bases \((n,k)=(2,2),(4,1)\) establish sharp failure of recovery from \(t_1\) alone.

## Verification
The standalone pure-Python verifier `check.py` independently enumerates all complete *finite labeled extension diagrams* with up to six combined old and new elements. It iterates every first-order permutation of the combined labels and every boundary mask defining the unique maximal decreasing-block decomposition, then retains diagrams whose restriction to named old labels is the prescribed ordered composition. A separate direct popularity enumerator counts occurrences of the old pattern among the canonical finite layered permutations. Both methods agree with the rational generating-function coefficient on all \(48\) tested (base-composition, tuple-arity) configurations and print `CHECK_OK`. This exhaustive test is a finite consistency check; the proof above, not the test, establishes the all-arity theorem. Reproduce with `python3 check.py`.

## Relationship to prior work
Peter J. Cameron, *Homogeneous Permutations* (published 2002-10-31), classifies the five nontrivial Fraïssé classes of finite permutations and explicitly identifies the layered class and its lexicographic limit. Its statements in Sections 3–4 do not enumerate finite-base pointwise stabilizer orbit profiles. This paper supplies the structural foundation, not the present rational type-series theorem.

Toufik Mansour and Alek Vainshtein, *Layered restrictions and Chebyshev polynomials* (arXiv 2000-08-22), enumerate permutations avoiding \(123\) and an additional layered pattern. Their avoidance enumerators do not count all injective extensions over a fixed individually named layered base.

Michael Albert, Cheyne Homberger and Jay Pantone, *Equipopularity Classes in the Separable Permutations* (arXiv 2014-10-27), classify pattern popularity among **all separable permutations**, a proper larger class containing layered permutations. Their exact equipopularity partition within the larger class does not imply equipopularity in its layered subclass, where the ambient summation set is different and the classification depends on \((n,k)\).

Vincent Vatter, *Reconstructing compositions* (arXiv 2006-10-16), proves sharp recovery of a composition from the **set** of its sufficiently small deletion patterns. Such information is substantially finer than the single numerical cardinality \(t_r(A)\) for each extension arity: the latter loses the ordered layer-size composition at every arity. There is no contradiction between the theorems.

## Limitations
The theorem concerns only the numerical spectra of injective ordered *new* tuples over individually named bases in one layered homogeneous permutation structure; it neither reconstructs exact extension diagrams nor covers other homogeneous permutation classes. The full source search cannot exclude an unindexed earlier stabilizer-orbit enumeration. The scientific review is non-independent; no independent audit or historical-priority certification is claimed.

## References
- P. J. Cameron, *Homogeneous Permutations*, Electronic Journal of Combinatorics 9(2), R2 (2002), https://doi.org/10.37236/1674 .
- T. Mansour and A. Vainshtein, *Layered restrictions and Chebyshev polynomials*, arXiv:math/0008173 (first posted 2000-08-22), https://arxiv.org/abs/math/0008173 .
- M. Albert, C. Homberger and J. Pantone, *Equipopularity Classes in the Separable Permutations*, arXiv:1410.7312 (first posted 2014-10-27), https://arxiv.org/abs/1410.7312 .
- V. Vatter, *Reconstructing compositions*, arXiv:math/0610477 (first posted 2006-10-16), https://arxiv.org/abs/math/0610477 .
