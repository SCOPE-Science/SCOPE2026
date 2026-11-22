# Boolean shattering and mod-two homology of the labelled Fano-plane incidence class

## Finding

Let \(V=\{0,1,\dots,6\}\), let \(U=\binom{V}{3}\), and let \(\mathcal F\) consist of the thirty sets of seven triples that are the line sets of the labelled Fano planes on \(V\). Regard \(\mathcal F\subseteq 2^U\) as a class of Boolean predicates on the thirty possible Steiner triple-system structures of order seven.

**Theorem.** A support \(S\subseteq U\) is shattered by \(\mathcal F\) precisely in the following cases:

1. \(|S|\le1\);
2. \(|S|=2\) and its two triples meet in exactly one point;
3. \(|S|=3\), every two triples meet in exactly one point, and their three pairwise intersection points are distinct.

No four-element support is shattered. The full shattered-support polynomial is
\[
\Phi_{\mathcal F}(z)=1+35z+315z^2+840z^3.
\]
The shattered-support complex is pure of dimension two: its 840 facets form one orbit under the relabelling group \(\mathfrak S_7\). Its reduced homology over \(\mathbb F_2\) is
\[
\widetilde H_i(\operatorname{Sh}(\mathcal F);\mathbb F_2)
\cong\begin{cases}\mathbb F_2^{559},&i=2,\\0,&i\ne2.\end{cases}
\]
Both static and online shattering dimensions are three:
\[
\operatorname{VCdim}(\mathcal F)=\operatorname{Ldim}(\mathcal F)=3.
\]
Here the Littlestone dimension uses the same triple-membership questions, with binary-labelled decision trees.

## Assumptions and scope

The vertex set \(U\) contains all 35 unordered triples of the *fixed* seven-element label set. A concept is the seven-block set of one entire Steiner triple system of order seven, not a single Fano plane's point or line neighborhood. The thirty concepts are different as labelled sets, though isomorphic as abstract incidence structures. Shattering means that for every \(T\subseteq S\) there exists \(F\in\mathcal F\) such that \(F\cap S=T\). The homology claim is over the field \(\mathbb F_2\); no integral or homotopy-type claim is made.

## Proof

**Geometry and single/pair counts.** The standard projective plane over \(\mathbb F_2\) has seven nonzero vectors and lines \(\{a,b,a+b\}\). Its automorphism group has order 168, hence the orbit under all \(7!\) relabellings contains exactly 30 distinct line sets. Each such line set has seven blocks, so a fixed triple belongs to \(30\cdot7/35=6\) concepts. Two distinct lines of any Fano plane intersect in exactly one point. There are \(7\binom62\binom42/2=315\) unordered pairs of triples meeting in one point. Relabelling is transitive on them, and each Fano plane has \(\binom72=21\) line pairs. Consequently each compatible pair is jointly present in \(30\cdot21/315=2\) concepts. No incompatible pair is jointly present. Thus every singleton is shattered; a pair is shattered precisely when its triples intersect in one point. For a compatible pair, the four trace multiplicities are \((20,4,4,2)\), in the order \(00,10,01,11\).

**Three-block configurations.** For three distinct triples whose pairs meet at one point, either all three share their common point (*concurrent*) or the three pairwise intersection points are different (*triangular*). There are \(7\cdot 15=105\) concurrent supports: after choosing the common point, partition the other six points into three unordered pairs. There are \(\binom76\binom63\,3!=840\) triangular supports: choose the six used labels, choose the three intersection labels, and biject the other three labels with the three pairs of intersection labels.

Every Fano plane has exactly seven concurrent triples of lines, one at each point, and \(\binom73-7=28\) triangular triples of lines. Relabellings act transitively on each configuration type. Double-counting the plane/configuration incidences shows that each concurrent triple is contained in \(30\cdot7/105=2\) planes, and each triangular triple in \(30\cdot28/840=1\) plane. For a concurrent support every compatible pair has two completions, both of which also contain its third triple. The trace \(110\) is therefore absent, so it is not shattered. For a triangular support, each singleton lies in six planes, each pair in two, and all three together in one. Inclusion-exclusion gives the complete pattern multiplicities
\[
N_{000}=17,\quad N_{100}=N_{010}=N_{001}=3,\quad
N_{110}=N_{101}=N_{011}=N_{111}=1.
\]
All eight traces occur. A support with an incompatible pair cannot be shattered. This proves the three-support characterization.

**No larger shattered supports.** If four distinct triples were shattered, every three of them would be a shattered triangular support. In particular one plane would contain all four (the all-positive trace). Any three of the four determine a *unique* plane by the preceding completion count. That plane also contains the fourth triple, making the trace of three positives and one negative impossible. Therefore no four-support is shattered, and hereditary closure excludes every larger support.

**Purity, facets, and online dimension.** Every compatible pair extends to a triangular triple: this follows by relabelling transitivity and the concrete example \(\{012,034,135\}\), whose first two triples are compatible. Thus no edge or singleton is a facet; the 840 triangular supports are exactly the facets. All triangles have the same six-label incidence type, so \(\mathfrak S_7\) acts transitively. This proves purity and the polynomial. An online depth-four complete mistake tree would require, at its root, at least eight distinct concepts in each branch; the positive branch for any triple contains only six planes, ruling out depth four. A shattered triangle supplies a depth-three tree, establishing both dimension claims.

**Mod-two homology.** The complete face vector in positive dimensions is \((f_0,f_1,f_2)=(35,315,840)\). The one-skeleton is connected, in fact has graph diameter at most two: two distinct triples meeting in one point are adjacent; if they are disjoint, choose an intermediate triple consisting of one point from each and the sole point outside their union; if they meet in two points, choose an intermediate triple consisting of one common point and two points outside their union. Every intermediate triple meets each original in exactly one point. Thus its first boundary has rank 34 over \(\mathbb F_2\). The two-dimensional boundary matrix has 315 rows indexed by compatible pairs and 840 columns indexed by triangular triples, with three ones per column. Exact binary Gaussian elimination gives rank 281; both independent checkers construct this boundary from scratch and obtain that rank. Hence \(\widetilde\beta_1=315-34-281=0\) and \(\widetilde\beta_2=840-281=559\). There are no simplices of dimension at least three, so all remaining reduced Betti numbers vanish. This last rank is a finite, fully enumerated computational certificate, not an inferred general formula.

## Verification

Two complete, independent verification programs are provided in the same directory as this document. Run `python3 check_fano.py` and run `c++ -O2 -std=c++17 check_fano.cpp -o check_fano && ./check_fano`. The Python implementation generates all planes by the symmetric-group orbit of the standard binary projective plane; the C++ implementation instead solves the exact cover of all 21 point pairs by seven blocks. Both enumerate every potential shattered support through size four (the only possible size relevant to the theorem), test all Boolean traces, and independently compute the exact \(\mathbb F_2\) boundary rank. Every support of size at least five is ruled out by hereditary shattering once size four is excluded. The programs require no data downloads or third-party packages.

## Relationship to prior work

Baldwin and Paolini (2019 preprint; published 2020/2021) study model-theoretic Steiner systems and explicitly use the Fano plane as a finite primitive incidence structure. Saniga (2015 preprint; 2016 article) explicitly lists the thirty labelled Fano planes and their line-overlap properties. Heinlein and Östergård (2022) give algorithms for counting Steiner configurations and discuss the Fano plane's generating triples and automorphism group. These are essential prior facts and are not claimed as new. Their inspected results do not state this Boolean type-realization classification or the 559-dimensional mod-two second homology of its shattered-support complex. The structural proof here is not a new enumeration of labelled Fano planes; it uses the classical enumeration to determine a different invariant.

## Limitations

The conclusion applies only to the thirty labelled Fano planes of order seven. It does not extend to all larger Steiner triple systems without further arguments. The homology is computed over \(\mathbb F_2\), not integrally; simple connectivity and a wedge-of-spheres homotopy type are not asserted. The novelty comparison covers the inspected references and indexed research records, not every historical computation; the explicit thirty-plane tables make historical independent derivations possible. A separate independent scientific audit has not been performed.

## References

- J. Baldwin and G. Paolini, *Strongly Minimal Steiner Systems I: Existence*, arXiv:1903.03541 (first posted 8 March 2019), https://arxiv.org/abs/1903.03541.
- D. Heinlein and P. R. J. Östergård, *Algorithms and complexity for counting configurations in Steiner triple systems*, Journal of Combinatorial Designs 30 (2022), https://doi.org/10.1002/jcd.21839.
- M. Saniga, *Combinatorial Intricacies of Labeled Fano Planes*, arXiv:1509.06009 (2015); Entropy 18 (2016), 312, https://doi.org/10.3390/e18090312.
