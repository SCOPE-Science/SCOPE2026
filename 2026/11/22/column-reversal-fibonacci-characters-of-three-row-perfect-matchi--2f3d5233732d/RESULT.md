# Column-reversal Fibonacci characters of three-row perfect-matching complexes

## Finding

For every integer \(n\geq1\), let \(G_n=P_3\square P_{2n}\), and let \(\Delta_n\) be its **perfect-matching complex**: the abstract simplicial complex on grid edges whose facets are exactly the perfect matchings. Let \(\kappa\) reverse the order of the \(2n\) grid columns and act simplicially on \(\Delta_n\). Put \(F_0=0\), \(F_1=1\), \(F_{j+2}=F_{j+1}+F_j\), and adopt \(F_{-1}=1\).

**Theorem.** The integral homology group \(\widetilde H_{n-1}(\Delta_n;\mathbb Z)\) is free of rank \(F_{n-1}\), and the column-reversal involution has the following **exact integral trace**, for every indicated integer \(k\):

\[
\operatorname{tr}\bigl(\kappa_*\mid\widetilde H_{2k-1}(\Delta_{2k};\mathbb Z)\bigr)
=(-1)^{k-1}F_{k-2}\qquad(k\ge1),
\]
\[
\operatorname{tr}\bigl(\kappa_*\mid\widetilde H_{2k}(\Delta_{2k+1};\mathbb Z)\bigr)
=(-1)^kF_k\qquad(k\ge0).
\]

The first case with \(k=1\) uses \(F_{-1}=1\). At \(n=1\) the complex is contractible and its reduced trace is zero. For every \(n\ge2\) the only nonzero reduced homology is in degree \(n-1\), by the theorem of Chandrakar–Chau–Goyal–Karki–Subhash [1]. Thus the positive and negative eigen-dimensions over \(\mathbb Q\) are exactly
\[
\dim H_{\pm}=\frac{F_{n-1}\pm t_n}{2},
\qquad
 t_n=\operatorname{tr}\bigl(\kappa_*\mid\widetilde H_{n-1}(\Delta_n;\mathbb Q)\bigr).
\]
In particular, the reduced rational homology of \(|\Delta_n|/\langle\kappa\rangle\) is concentrated in degree \(n-1\) and has rank \((F_{n-1}+t_n)/2\) for \(n\ge2\). This rational quotient consequence does not assert an integral equivariant splitting.

## Assumptions and scope

Grid vertices are \((r,c)\) with \(r\in\{0,1,2\}\), \(c\in\{0,\ldots,2n-1\}\), with unit horizontal and vertical edges. The involution is \(\kappa(r,c)=(r,2n-1-c)\). A face is any subset of an actual perfect matching, not any matching independently. The homology normalization is reduced **integral** simplicial homology and its trace is of the induced integral linear automorphism. The known nonequivariant homotopy theorem [1] provides the free-rank and concentration premise; the new assertion is the entire column-reflection character for all lengths.

## Proof

**1. Symmetric extension lemma.** Each edge orbit under \(\kappa\) is either a pair of grid edges contained in opposite halves, or a singleton horizontal edge crossing the central mirror. Identify a paired orbit with its left-half edge, and a singleton crossing edge with a permitted *monomer* at one vertex of column \(n-1\) in the \(3\times n\) half-grid. An invariant face is a set \(S\) of orbit-tiles. Such an \(S\) is contained in an original perfect matching if and only if it is contained in some **mirror-symmetric** perfect matching.

The reverse implication is immediate. For the forward implication take any perfect matching containing all edges in \(S\), average its zero-one edge vector with that of its mirror image, and restrict to the left half. The result is a feasible fractional exact-one covering of the half-grid by ordinary domino edges and central-column monomers, with every orbit-tile of \(S\) fixed at value one. The vertex-tile incidence matrix of a bipartite grid graph is totally unimodular after orienting one bipartition; adjoining monomer unit columns preserves total unimodularity. The constraints fixing coordinates at zero or one and the bounds \(0\le x\le1\) also preserve integrality. Consequently this nonempty bounded matching polytope has an integral vertex, which chooses an ordinary domino/monomer tiling extending \(S\). Reflecting it gives the requisite full-grid symmetric perfect matching. This proves the lemma without assuming the originally chosen perfect matching was symmetric.

**2. Fixed-face Lefschetz reduction.** Suppose an invariant nonempty face contains \(p\) paired edge orbits and \(s\) singleton orbits. It has \(2p+s\) vertices and column reversal permutes its oriented simplex with sign \((-1)^p\). Its reduced chain Lefschetz contribution is therefore \(-(-1)^{p+s}\). The empty face makes the same contribution \(-1\) in the augmented chain convention. Hence, writing \(\mathcal A_n\) for all orbit-tile selections that extend to a half-grid tiling,
\[
Z_n=\sum_{S\in\mathcal A_n}(-1)^{|S|},\qquad
\widetilde L(\kappa;\Delta_n)=-Z_n.
\]
By the nonequivariant homology concentration in [1], \((-1)^{n-1}t_n=-Z_n\), so \(t_n=(-1)^n Z_n\). Thus it remains to determine the exact integer sequence \(Z_n\).

**3. Finite transfer certificate.** Process the \(3\times n\) half-grid by columns. Encode incoming horizontal-domino occupations as row masks \(b\in\{0,\ldots,7\}\), and encode the set of all incoming masks compatible with previously *forced* orbit-tiles as the 8-bit subset state \(q\). Initially \(q=1\), representing the singleton incoming mask zero. At each of the first \(n-1\) columns, specify forced vertical-edge bits \(v\in\{0,1,2,3\}\) and forced outgoing-horizontal bits \(h\in\{0,\ldots,7\}\). There are three possible actual vertical choices with (tile bit, covered-row mask) \((0,0),(1,3),(2,6)\). For each incoming mask \(b\) in \(q\), an actual vertical choice \((u,d)\) is allowed when \(u\) contains \(v\) and \(b\mathbin\&d=0\); then the actual outgoing mask is \(b'=7\mathbin\oplus(b\mathbin|d)\), and is allowed when it contains the forced bits \(h\). The next state is the union of all resulting masks \(b'\), encoded as \(q'=\bigvee_{b'}2^{b'}\). The symbol receives weight \((-1)^{\operatorname{popcount}(v)+\operatorname{popcount}(h)}\), and a transition to the zero state is discarded.

For the final column there is no outgoing horizontal domino; instead each uncovered row is covered by a singleton mirror-axis monomer. Given an incoming state \(q\), sum \((-1)^{\operatorname{popcount}(v)+\operatorname{popcount}(a)}\) over forced vertical bits \(v\) and forced monomer bits \(a\), when a compatible actual vertical choice and actual remaining monomers exist. Let \(w(q)\) be this terminal sum.

The finite closure of nonzero reachable states is exactly fourteen states, in this deterministic order:

```
[1,146,130,128,144,16,2,73,8,72,64,65,9,18]
```

Let \(T\) be the integer matrix formed by summing symbol weights between each ordered pair of states; it has exactly 38 nonzero entries. The fourteen entries of the terminal column vector in the same order are

```
[0,-2,-1,1,-1,-1,-1,0,0,-1,0,0,0,-2]
```

The preceding state recurrence is an exact formula for the matrix, with no omitted cases; the standalone `verify.py` constructs it from those rules rather than trusting a hard-coded matrix. With \(e_1\) the first basis column, every selection of forced orbit-tiles occurs once, so
\[
Z_n=e_1^{\mathsf T}T^{n-1}w\qquad(n\ge1).
\]
Construct the exact integer residual \(r=(T^4+T^2-I)w\). The verifier computes, with exact integer arithmetic,
\[
e_1^{\mathsf T}T^j r=0\qquad\text{for every }j=0,1,\ldots,13.
\]
Since \(T\) is a \(14\times14\) integer matrix, Cayley–Hamilton implies these equalities for every \(j\ge0\). Consequently
\[
Z_{n+4}+Z_{n+2}-Z_n=0\qquad(n\ge1).
\]
The same exact transfer yields \(Z_1=0\), \(Z_2=1\), \(Z_3=1\), and \(Z_4=0\). Separating even and odd indices and solving this recurrence using the standard Fibonacci recurrence gives
\[
Z_{2k}=(-1)^{k-1}F_{k-2}\ (k\ge1),\qquad
Z_{2k+1}=(-1)^{k+1}F_k\ (k\ge0).
\]
As \(t_n=(-1)^n Z_n\), both asserted trace formulas follow. The eigenspace dimensions follow from the rational involution projector \((1\pm\kappa_*)/2\); rational quotient homology agrees with rational invariant homology for a finite simplicial group action after equivariant subdivision.

## Verification

`verify.py` is a self-contained Python 3 verifier, requiring no external libraries. Run `python3 verify.py` from the directory containing the file. It recomputes the fourteen reachable subset states, the 38 nonzero weighted transitions, and every scalar equality in the 14-moment Cayley–Hamilton certificate. It verifies the formulas directly to \(n=30\). Separately, it enumerates **all original domino tilings** of the \(3\times2n\) grid and all invariant faces for \(1\le n\le6\), checks the symmetric-extension lemma in these instances, and compares the signed fixed-face sums to the transfer formula. The actual output is in `verification_output.txt`. The finite enumerations are consistency checks; the infinite claim follows from the explicit transition definition, exact finite moment certificate, Cayley–Hamilton and [1].

The first fifteen integral traces are
\[
0,1,-1,0,1,1,-2,-1,3,2,-5,-3,8,5,-13.
\]

## Relationship to prior work

Chandrakar, Chau, Goyal, Karki and Subhash [1] establish that \(\Delta_n\) is contractible for \(n=1\) and is a wedge of \(F_{n-1}\) spheres of dimension \(n-1\) for \(n\ge2\); these nonequivariant results are **premises rather than novelties**. Their proof classifies the homotopy types but does not determine the column-reversal action. Chandrakar and Singh [2] classify the different two-row ladder family and polygonal line tilings. A published individual \(3\times4\) column-reflection calculation gives \(t_2=1\), matching the present formula but not determining later widths. A published all-length **row**-reflection Lefschetz calculation concerns a different automorphism. Published reflection calculations for the *ordinary matching complex*, rather than its perfect-matching subcomplex, do not imply this result. Search of the relevant indexed records revealed no published all-width column-reflection formula, but this does not certify worldwide priority.

## Limitations

The statement applies to the perfect-matching complex of the three-row, even-column rectangular grid and to its *column-order reversal*; it is not a theorem about row reversal, arbitrary rectangular grids or ordinary matching complexes. The derived rational eigenspace and quotient ranks do not establish an integral eigenspace splitting, quotient torsion classification, or equivariant homotopy type. The exact closed trace relies on the nonequivariant homology theorem [1]. An independent review and a comprehensive priority search have not been performed.

## References

1. H. Chandrakar, T. Chau, S. Goyal, R. Karki and B. Subhash, *Perfect Matching Complexes of \(3\times2n\) Grid Graph*, arXiv:2611.18058, first public 13 November 2026, https://arxiv.org/abs/2611.18058. Especially Theorem 3.5.
2. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809, first public 8 July 2024; *Annals of Combinatorics* 29 (2025), https://arxiv.org/abs/2407.05809.
