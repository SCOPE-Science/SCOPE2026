# Sharp eight-point rank-three onset and full extremal census in two-sorted bipartite graphs

## Finding

In the Fraïssé class of finite simple bipartite graphs with the two shores named by disjoint unary predicates, the least order of a finite structure of one-point-extension rank at least three is **eight**. Every eight-vertex rank-three witness has exactly four vertices in each shore. Among the \(2^{16}=65,536\) labelled incidence matrices on two fixed four-element shores, precisely **9,672** have rank at least three, forming **29** side-preserving isomorphism classes. Those classes have the following orbit sizes under \(S_4\times S_4\): eight orbits of size 576, sixteen of size 288, four of size 96, and one of size 72.

The exact edge distribution in this eight-point stratum, indexed by edge count \(e\), is

\[
\begin{array}{c|rrrrrrr}e&5&6&7&8&9&10&11\\\hline
\#&576&1248&1536&2952&1536&1248&576\end{array}.
\]

Five edges are necessary for rank at least three **at every finite order**, and suffice. At eight points and five edges there is exactly one side-preserving isomorphism type: a six-vertex path with its consecutive vertices alternating between shores, together with one isolated vertex in each shore. A representative four-by-four incidence matrix, with rows in the left shore and columns in the right shore, is

```
0000
1000
1100
0110
```

The claims are about the one-point-extension rank in the specified Fraïssé age; they are not claims about ordinary first-order quantifier rank, two-variable rank, uncoloured graph rank, or all finite bipartite graphs viewed without named shores.

## Assumptions and scope

A finite two-sorted bipartite graph is \(H=(L\sqcup R,E)\), where \(L,R\) partition the vertices, the two unary shore predicates are named, and \(E\subseteq L\times R\) is a simple symmetric adjacency relation with no within-shore edges. Embeddings preserve both shore predicates and the induced adjacency/nonadjacency relation. We allow empty shores and isolated vertices.

For an induced finite substructure \(A\subseteq H\) define its relative rank by \(\operatorname{rk}_H(A)\ge0\) always, and, for each integer \(k\ge0\), by \(\operatorname{rk}_H(A)\ge k+1\) if **every** permitted nonalgebraic one-point extension type of \(A\) in this age has a witness \(v\in H\setminus A\) with \(\operatorname{rk}_H(A\cup\{v\})\ge k\). A new left point has an arbitrary Boolean incidence vector to the existing right points, and a new right point has an arbitrary vector to the existing left points; there are no constraints on its incidences to the existing same-shore points because these are forbidden. Define \(\operatorname{rk}(H)=\operatorname{rk}_H(\varnothing)\). This agrees with the finite relative-rank recursion of the motivating reference, specialized to the two-sorted bipartite age.

The eight-point enumeration fixes the four labels on each shore. Two matrices are isomorphic when related by separate permutations of rows and columns; interchanging named shores is **not** an isomorphism. An edge count refers to the number of ones in the binary incidence matrix.

## Proof

**1. Rank of a two-point parameter set.** Fix a pair \(\{u,v\}\subseteq H\). Rank at least one means that every one-point extension type of the pair is realized elsewhere in \(H\), with no deeper condition. If both parameters lie in the left shore, the extension types include one new right vertex with each of the four incidence profiles \((0,0),(0,1),(1,0),(1,1)\). There is also a new-left type, requiring a third left vertex. Thus the pair has relative rank at least one exactly when all four profiles occur among right vertices and another left vertex is available. The right-right case is symmetric. If \(u\in L\) and \(v\in R\), the two possible new-left incidence values to \(v\) must both occur among other left vertices, and the two possible new-right incidence values to \(u\) must both occur among other right vertices. These conditions are necessary and sufficient; no other one-point types exist.

**2. Rank of a singleton and of the empty structure.** For a left vertex \(u\), the definition says \(\operatorname{rk}_H(\{u\})\ge2\) exactly when (i) some other left vertex \(u'\) makes \(\operatorname{rk}_H(\{u,u'\})\ge1\), and (ii) for each of the two possible incidences \(\epsilon\in\{0,1\}\), there is a right vertex \(v\) adjacent to \(u\) with bit \(\epsilon\) and \(\operatorname{rk}_H(\{u,v\})\ge1\). For a right singleton the symmetric condition holds. Finally, \(\operatorname{rk}(H)\ge3\) if and only if some left singleton and some right singleton attain relative rank at least two. This is a direct expansion of the rank recursion, not an empirical proxy for it.

**3. Sharp order lower bound.** If the empty structure has rank at least three, the rank-two left singleton yields a rank-one pair of left vertices. The four distinct right incidence profiles force \(|R|\ge4\). A rank-two right singleton analogously forces \(|L|\ge4\). Therefore every rank-three host has at least eight vertices, with equality only at \((|L|,|R|)=(4,4)\).

**4. Five edges are necessary independently of host order.** The rank-one left-left pair requires distinct right vertices realizing profiles \(00,01,10,11\), which together entail at least \(0+1+1+2=4\) edges incident to that pair. Similarly a rank-one right-right pair exists and requires profiles \(00,01,10,11\) among left vertices. If \(|E|=4\), all four edges are incident to the first left-left pair. Hence at most two distinct left vertices meet any edge, contradicting the other pair's need for at least three distinct left rows of patterns \(01,10,11\). Hosts with fewer than four edges are already excluded. Thus \(|E|\ge5\).

**5. Attainment and exact enumeration.** For four vertices on each shore the pair and singleton criteria in steps 1–2 are finite Boolean predicates involving the sixteen matrix entries. `structural_census.py` evaluates the predicate for every integer matrix mask from 0 through 65,535, takes its orbit under all \(4!\times4!=576\) independent shore permutations, and tabulates edges and distinct orbit representatives. It returns 9,672 labelled matrices and the 29 classes and orbit-size profile stated above. `independent_recursion.py`, which does not import the pair predicate, independently enumerates all permitted one-point extension types at each marked subset and applies the original rank recursion directly to all 65,536 masks; it also returns 9,672. Therefore the algorithm is exhaustive, with its termination and coverage established by explicit finite loops and the proven Boolean equivalence in steps 1–2, rather than by sampling.

As a further independent check of the symmetry quotient, `burnside_direct.py` constructs matrices fixed by every row/column conjugacy-class pair as unions of its orbits on the sixteen cells, and tests rank with the direct recursion. For permutation cycle types \((1,1,1,1),(1,1,2),(1,3),(2,2),(4)\), with class sizes \(1,6,8,3,6\), the representative-pair fixed-count matrix is

\[
\begin{pmatrix}
9672&0&0&0&0\\
0&128&0&40&0\\
0&0&12&0&0\\
0&40&0&8&0\\
0&0&0&0&4
\end{pmatrix}.
\]

Weighting by the corresponding conjugacy-class sizes gives a fixed-point sum of \(16,704\); Burnside's lemma yields exactly \(16,704/576=29\) classes. This argument supplies a second census of the orbits without canonical relabelling.

The five-edge row of the structural census comprises 576 matrices, all in one orbit of size 576, represented by the displayed matrix. The six nonisolated vertices make a path of length five; the remaining row and column are isolated. Direct rank recursion confirms that this matrix has rank at least three. Together with steps 3–4, it proves both sharp minima and uniqueness of the eight-vertex, five-edge form.

## Verification

All programs use only Python 3's standard library and are independently executable with `python structural_census.py`, `python independent_recursion.py`, and `python burnside_direct.py`, from the same directory. `structural_output.txt`, `independent_recursion_output.txt`, and `burnside_output.txt` contain their actual full outputs. The first checker prints `ALL_CHECKS_OK`, counts 9,672 labelled structures and lists all 29 explicit orbit representatives; the second prints `INDEPENDENT_DIRECT_RECURSION_OK count=9672`; the independent Burnside check prints `BURNSIDE_DIRECT_OK fixed_sum= 16704 orbits= 29`.

The algorithms exhaust precisely the \(2^{16}\) fixed-side labelled eight-point matrices. The **all-order** order and edge lower bounds do not depend on the finite enumeration. Programs check the nontrivial finite enumeration but do not certify historical novelty, and no independent external mathematical audit has been performed.

## Relationship to prior work

López-Callejas and Navarro-Castillo, *A rank function for Fraïssé classes and the rank property*, version first public April 15, 2026, introduced the rank recursion and gave general constructions and examples; its inspected definitions, general results, and examples do not supply this two-sorted bipartite sharp threshold and symmetry-refined four-by-four census. The general seven-vertex, six-edge theorem for **uncoloured** graph extension rank concerns a different Fraïssé age and does not imply this two-sorted result. Previously tabulated row-column equivalence classes of all four-by-four binary matrices cover the ambient 317 classes, not which of them satisfy this extension-rank condition. Other work on random bipartite reduct tuple orbits or first-order theories of side-labelled chain graphs concerns different equivalences or different ranks.

The classification is not a claimed theorem about two-existentially-closed graphs, ordinary first-order quantifier rank, or matrices up to independent row flips. Isomorphism and permutation conventions are explicitly side-preserving throughout.

## Limitations

Only the **first possible host order** has a complete census here; no formula is claimed for all larger orders or for rank four. We do not assert that the listed structures have rank exactly three, only at least three. The edge lower bound is all-order, but uniqueness at five edges is claimed only among eight-point hosts. Historical priority is assessed relative to the inspected available literature and indexed records; an unindexed or inaccessible prior classification could affect that assessment. The mathematical argument and code have not undergone an independent external audit.

## References

1. López-Callejas and Navarro-Castillo. *A rank function for Fraïssé classes and the rank property*. arXiv:2604.14461, version 1, first publicly posted 2026-04-15. https://arxiv.org/html/2604.14461v1
2. J. K. Truss. *Countable homogeneous ordered bipartite graphs*. *Archive for Mathematical Logic*, published online 2025-09-08. https://doi.org/10.1007/s00153-025-00986-1
3. OEIS A241956. Enumeration of binary matrices under independent row and column permutations, with the ambient four-by-four count 317. https://oeis.org/A241956
4. published-finding corpus record, *Sharp rank-three onset and six-edge extremum for finite graphs* (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-rank-three-onset-and-six-edge-extremum-for-finite-graphs--a3c35b6162f1
5. published-finding corpus record, *Marked-base orbit spectra and a sharp single-parameter recovery threshold for random bipartite reducts* (2026-10-25), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-marked-base-orbit-spectra-and-a-sharp-single-parameter-recovery--1ceb9535794d
