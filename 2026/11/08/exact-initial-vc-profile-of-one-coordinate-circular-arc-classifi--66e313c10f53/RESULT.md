# Exact initial VC profile of one-coordinate circular-arc classifiers

## Finding

Let \(\mathbb S^1\) denote the unit circle. For an integer \(\ell\geq 1\), let \(\mathcal A_\ell\) consist of the binary classifiers on \((\mathbb S^1)^\ell\) of the form \(x\mapsto\mathbf 1\{x_j\in I\}\), where \(j\in\{1,\ldots,\ell\}\) and \(I\) is a connected circular arc; the empty arc and full circle are allowed. Only **one** coordinate is tested by a classifier, and one connected arc (not a union of arcs) is allowed.

The exact first eight feature-count VC dimensions are
\[
\operatorname{VCdim}(\mathcal A_\ell)=
\begin{cases}
3,&\ell=1,\\
5,&\ell=2,3,\\
6,&\ell=4,\\
7,&5\le\ell\le8.
\end{cases}
\]
For every integer \(d\ge2\), if \(d\) distinct sample points are shattered using \(\ell\) circular coordinates, then the general middle-layer obstruction holds:
\[
\ell\ge \left\lceil \frac{1}{d}\binom d{\lfloor d/2\rfloor}\right\rceil.
\]
More precisely, the minimum number \(\kappa(d)\) of circular orderings of \(d\) labels whose cyclic consecutive segments collectively include every subset satisfies
\[
\kappa(3)=1,\quad\kappa(4)=2,\quad\kappa(5)=2,\quad\kappa(6)=4,\quad\kappa(7)=5.
\]
The last two values explain the jumps from five to six and from six to seven shatterable points. The assertion concerns the unrestricted domain \((\mathbb S^1)^\ell\), not a fixed finite data set or a fixed arrangement of coordinates.

## Assumptions and scope

A circular arc is a connected subset of \(\mathbb S^1\) with arbitrary endpoints, optionally including either endpoint. Including the two constant classifiers avoids irrelevant conventions for the empty and all-positive traces. A sample is a set of distinct vectors \(x^{(0)},\ldots,x^{(d-1)}\in(\mathbb S^1)^\ell\). A sample is shattered if, for each \(B\subseteq\{0,\ldots,d-1\}\), one classifier has positive set exactly \(\{x^{(i)}:i\in B\}\) on that sample. Coordinates may repeat individual angles across samples; the arguments allow ties.

Let \(\kappa(d)\) be the least positive integer \(s\) for which \(s\) cyclic permutations of \(\{0,\ldots,d-1\}\) have the property that each subset of labels is a possibly empty or complete cyclic consecutive segment of at least one permutation. This finite invariant is precisely the least number of circular coordinates needed to shatter \(d\) points: freely assign distinct angular positions along the circle in each coordinate according to the chosen permutations.

## Proof

**1. The permutation reduction.** In one coordinate with \(d\) distinct angular positions, the positive trace of a connected arc is exactly a consecutive block of its cyclic ordering (including empty and full blocks). Conversely every consecutive block is realized by choosing endpoints in the gaps adjoining the block. With coordinate ties, the possible positive traces are consecutive unions of tied groups and are a subfamily of the traces of an arbitrarily chosen strict refinement of that cyclic order. Consequently ties cannot increase shattering. Independently assign the \(d\) angular values in each coordinate to realize any proposed family of cyclic permutations; all vectors are distinct because the first coordinate has distinct positions.

**2. Middle-layer bound.** Fix \(k\) with \(1\le k<d\). A cyclic ordering of \(d\) labels has exactly \(d\) distinct consecutive \(k\)-subsets: one beginning at each of its \(d\) positions. Hence \(\ell\) circular coordinates can realize at most \(\ell d\) distinct \(k\)-subsets. Shattering requires all \(\binom dk\) such subsets; taking \(k=\lfloor d/2\rfloor\) proves the stated obstruction. This proof does not assume that different coordinates contribute disjoint subsets.

**3. Constructions.** The following cycles are written as rows; entry \(0\) starts each displayed cyclic ordering, and the last entry is adjacent to the first. The labels always range from \(0\) through \(d-1\).

For \(d=3\):

```text
0 1 2
```

For \(d=4\):

```text
0 1 2 3
0 1 3 2
```

For \(d=5\):

```text
0 1 2 3 4
0 2 4 1 3
```

For \(d=6\):

```text
0 1 2 3 4 5
0 1 2 3 5 4
0 2 4 5 1 3
0 3 4 1 2 5
```

For \(d=7\):

```text
0 1 2 3 4 5 6
0 1 3 4 6 2 5
0 2 3 5 1 4 6
0 4 1 2 6 3 5
0 3 6 1 5 2 4
```

For each family, direct enumeration of consecutive segments of every length gives the entire Boolean algebra of \(2^d\) subsets. The small-design checks can be done without trusting a search program: for \(d=5\), the two displayed cycles have disjoint edge sets and hence cover all ten unordered pairs; the other nontrivial subsets are their complements. For \(d=6\), the four cycles cover all fifteen pairs and all twenty triples; their complementary subsets and singletons are consequently also covered. More specifically, among the twenty triples, sixteen appear exactly once and four appear twice. For \(d=7\), all thirty-five triples occur exactly once in the five cycles, and among the twenty-one pairs, seven appear once and fourteen appear twice. Every singleton is consecutive, and complements of consecutive sets are consecutive, proving all labels are realized. The standalone checker performs each of these complete finite checks explicitly.

The middle-layer obstruction makes these coordinate counts minimal: \(\binom42>4\), \(\binom63>3\cdot6\), and \(\binom73>4\cdot7\). For \(d=5\), one coordinate has just five consecutive pairs, fewer than the required ten. For \(d=3\), one coordinate suffices.

**4. Exact feature profile and eight-point exclusion.** Increasing the number of coordinates never reduces VC dimension. The witnesses above give lower bounds \(3,5,6,7\) at the indicated feature counts. For the upper bounds, the middle-layer test forbids shattering four points with one coordinate, six points with at most three coordinates, seven points with at most four coordinates, and eight points with at most eight coordinates, since
\[
\binom42=6>4,\quad\binom63=20>18,\quad
\binom73=35>28,\quad\binom84=70>64.
\]
These exclusions and monotonicity yield exactly the piecewise VC profile claimed.

## Verification

The standalone program `check_circular_arc.py` uses Python's standard library, lists the exact cycles above, forms every distinct cyclic interval on each row, and checks equality with the full power set for \(d=3,4,5,6,7\). It independently checks triple multiplicity one and pair coverage at \(d=7\), each intermediate-size arc count, and four numerical middle-layer obstructions. Run `python3 check_circular_arc.py`. The expected final marker is `CIRCULAR_ARC_STUMP_PASS 248 WITNESSES 14 LOWER_BOUNDS 4`. This is a finite check of explicit witnesses, not a replacement for the unrestricted bound.

## Relationship to prior work

Leboeuf, LeBlanc, and Marchand (arXiv:2010.07374v1, 14 October 2020), Corollary 8, determine VC dimensions of ordinary real-coordinate threshold decision stumps by the different inequality \(2\ell\ge\binom{d}{\lfloor d/2\rfloor}\). Their feature partitions are linear threshold cuts, not arbitrary connected arcs on circular features. The construction in this note uses two freely positioned endpoints on one circular feature; it is therefore a different classifier class, not a correction to that result.

Dębski and Lonc (2016) analyze universal cycles and near-universal *single* cyclic sequences for fixed-uniformity subsets, allowing a long sequence with repeated labels. That is distinct from choosing a minimum number of permutations, each using every label exactly once, and requiring *all subset sizes simultaneously*.

Tight-cycle decompositions of uniform hypergraphs have substantial prior literature. In particular, Meihua, Meiling Guan, and Jirimutu (2019) explicitly acknowledge earlier decompositions of complete three-uniform hypergraphs of order seven into tight seven-cycles. Existence of a five-cycle decomposition of the thirty-five triples is **not claimed as new**. The contribution asserted here is the coordinate-arc learning formulation, the simultaneous pair-and-triple coverage witnesses, the necessary middle-layer inequality, and the precise feature-count VC profile through eight coordinates. These related design results remain a priority-risk channel for the finite witnesses.

## Limitations

No claim is made about the least number of coordinates for \(d\ge8\), or the full VC dimension for \(\ell\ge9\). The displayed five-cycle design at seven labels is not asserted to be a new hypergraph decomposition. The result is specific to connected circular arcs on **one** selected coordinate, not unions of arcs, intersections across coordinates, or ordinary one-threshold linear stumps. The originality assessment is limited by searchable records and inspected primary texts; a directly equivalent earlier learning-theoretic formulation under different terminology cannot be ruled out. Independent mathematical audit has not been carried out.

## References

1. J.-S. Leboeuf, F. LeBlanc, M. Marchand, *Decision trees as partitioning machines to characterize their generalization properties*, arXiv:2010.07374v1, 14 October 2020, especially Theorem 7, Corollary 8, and Appendix A. https://arxiv.org/abs/2010.07374
2. M. Dębski, Z. Lonc, *Universal Cycle Packings and Coverings for k-Subsets of an n-Set*, Graphs and Combinatorics 32 (2016), 2323–2337, first published 21 July 2016. DOI:10.1007/s00373-016-1727-6.
3. Meihua, Meiling Guan, Jirimutu, *Decomposing complete 3-uniform hypergraph into 7-cycles*, Opuscula Mathematica 39 (2019), 383–393, published online 23 February 2019. DOI:10.7494/OpMath.2019.39.3.383.
