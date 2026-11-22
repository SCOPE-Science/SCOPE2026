# Finite-cover type spectra and unary recovery in the homogeneous matching 3-graph

## Finding
Let \(M=C(\Gamma)\) be the countable homogeneous complete three-edge-coloured graph of Aranda, with colours \(R,S,T\). The reflexive closure of \(R\) partitions \(M\) into two-element classes, and the \(S\)-edges between every pair of different classes form a perfect matching (the other two cross-edges have colour \(T\)). Every finite consistent configuration of such matchings embeds in \(M\).

Fix any finite pointwise named base \(A\). Suppose that \(f\) of its \(R\)-classes are completely represented and \(s\) are represented by exactly one vertex. Put \(m=f+s\), so \(|A|=2f+s\). For \(r\geq0\), let \(t_r(A)\) be the number of complete types over \(A\) of ordered injective \(r\)-tuples of elements outside \(A\). A tuple may contain the as-yet-unnamed mate of a singleton class in \(A\).

Then the entire exponential generating function is
\[
\boxed{\sum_{r\geq0}\frac{t_r(A)}{r!}z^r
=(1+z)^s\sum_{k\geq0}\frac{2^{mk+\binom{k}{2}}}{k!}
\left(z+\frac{z^2}{2}\right)^k.}
\]
In particular, for each integer \(r\geq0\),
\[
\boxed{t_r(A)=\sum_{j=0}^{\min(s,r)}\binom rj(s)_{\underline j}
\sum_{p=0}^{\lfloor(r-j)/2\rfloor}
\frac{(r-j)!}{2^p p!(r-j-2p)!}
2^{m(r-j-p)+\binom{r-j-p}{2}}.}
\]
Here \((s)_{\underline j}=s!/(s-j)!\). These numbers depend only on \((f,s)\), not on the actual \(S/T\) matching pattern among the classes of \(A\).

Even the single numerical value \(t_1(A)=2^m+s\) uniquely recovers \(m\) and \(s\), and hence \(f\), among all finite bases. Therefore bases with the same unary type count have identical injective tuple-type counts at every arity, although they need not be isomorphic as edge-coloured bases.

## Assumptions and scope
We use the complete relational language with three symmetric irreflexive edge colours and no uncoloured pairs of distinct vertices. The colouring of any two different \(R\)-classes is a perfect \(S\)-matching and its \(T\)-complement; all finite matching choices are simultaneously realizable. The latter free finite-diagram property is important: it is not asserted for arbitrary finite covers or reducts. Complete types equal realised finite induced-diagram orbits because \(M\) is homogeneous. The tuples have distinct coordinates, none equal to a named base element; algebraic mates of singleton base classes are allowed.

## Proof
First, because every \(R\)-class has size two, each coordinate of a new tuple is either the unique mate of one of the \(s\) singleton represented classes or belongs to an entirely new class. A mate of an old singleton is uniquely determined as a vertex once the old named point is fixed. Selecting a subset of these \(s\) mates contributes the labelled exponential factor \((1+z)^s\). In an ordered tuple no mate may occur twice.

Next consider the \(k\) entirely new \(R\)-classes touched by the remaining tuple coordinates. Every such class contributes either one named new coordinate or both of its elements, with respective labelled exponential weights \(z\) and \(z^2/2\). The latter denominator accounts for the unordered two-element class, while the overall labels are those of the tuple coordinates. Dividing the product by \(k!\) makes the new classes an unordered set.

For each of the \(k\) new classes and each of the \(m\) distinct old classes there are exactly two possible \(S\)-matching alignments. This is true even when the old class is represented by just one vertex: the new coordinate has exactly one of the two possible colours \(S,T\) to that old named vertex, and the missing mate has the opposite colour. The choices for a new class and different old classes are independent, producing \(2^{mk}\). Each of the \(\binom{k}{2}\) pairs of different new classes has two matching alignments, independently, producing \(2^{\binom{k}{2}}\).

The remaining relations are forced: the mates of singleton old classes have forced relations to every already named vertex and to one another; if such a mate and a vertex from a new class occur, their relations are the complementary colours of those between that new class and the mate's named old partner. No additional choices or identifications occur. Conversely, Aranda's random-graph matching construction realizes any independently prescribed finite matching choices. Homogeneity makes different resulting coloured diagrams different complete types. Multiplying these independent labelled-class contributions establishes the generating function.

For the coefficient formula, choose \(j\) old singleton mates and their coordinate positions in \(\binom rj(s)_{\underline j}\) ways. Partition the remaining \(r-j\) labelled coordinates into \(p\) unordered pairs and \(r-j-2p\) singletons, in \((r-j)!/(2^pp!(r-j-2p)!)\) ways. There are \(k=r-j-p\) fresh classes, giving precisely the indicated power of two. This proves the identity for every nonnegative integer \(r\).

For \(r=1\) the formula gives \(t_1=2^m+s\) and \(0\le s\le m\). For \(m=0\), the only possible value is 1. For each \(m\ge1\), the possible values lie in the interval \([2^m,2^m+m]\); these integer intervals are strictly disjoint, since \(2^m+m<2^{m+1}\) for every \(m\ge1\). Thus \(t_1\) determines \(m\); subtraction then determines \(s\), and \(f=m-s\). The generating function proves all-arity recovery. No part of this argument recovers the actual old matching colours.

## Verification
The accompanying `verify.py` independently constructs all finite coloured diagrams by choosing actual \(R\)-fibres, assigning old and new vertices their two fibre positions, selecting independent underlying binary edge bits between classes, and deduplicating the induced \(R/S/T\) signatures. It compares those exact diagram counts against the displayed formula in 40 cases with \(f+s\le3\) and \(r\le3\), including distinct old matching patterns. A separate rational-arithmetic expansion of the exponential generating function is compared with the explicit double sum in 288 cases. Exact output appears in `verification-output.txt`.

For the empty base, the initial counts are \(1,1,3,14,118,1784\) for \(r=0,\ldots,5\). These finite tests support but do not replace the coefficient-wise labelled-structure proof for all arities.

## Relationship to prior work
Aranda (2015), Chapter 3, defines and classifies this specific finite matching cover of the random graph and establishes the structural matching property used here. That classification and matching construction are credited, not claimed as new. Evans (1996) and Ivanov (1999) study finite covers and their splitting/cohomological structure at a more general level. The contribution here is the complete exact finite-parameter tuple-type generating series, its coefficient formula for bases with both full and singleton represented classes, and numerical all-arity recovery already from the first count. The sources inspected did not state or directly compute these exact spectra. Other prior enumerations for two-equivalence grids or bipartite reducts concern different languages and orbit relations, and do not imply this matching-cover formula.

## Limitations
This is an exact type-counting statement for the specified homogeneous three-coloured finite cover, not an assertion about all finite covers or about the one-relation reduct. The unary numerical invariant recovers only the occupancy profile \((f,s)\), not the old induced \(S/T\) pattern or its isomorphism class. Independent mathematical audit has not been performed; publication priority beyond the inspected sources is not certified.

## References
- A. Aranda, *The Classification of Homogeneous Simple 3-graphs*, arXiv:1505.01188v1 (first posted 2015-05-05), Chapter 3, especially Section 3.1 and Theorem 3.1.21. https://arxiv.org/abs/1505.01188
- D. M. Evans, *Splitting of Finite Covers of \(\aleph_0\)-Categorical Structures*, Journal of the London Mathematical Society 54 (1996), 210–226. https://doi.org/10.1112/jlms/54.2.210
- A. A. Ivanov, *Finite Covers, Cohomology and Homogeneous Structures*, Proceedings of the London Mathematical Society 78 (1999), 1–28. https://doi.org/10.1112/S002461159900163X
