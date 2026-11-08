# Twenty-six top-degree integral cycles in the three-particle dodecahedral configuration space

## Finding

Let \(D\) denote the graph underlying a regular dodecahedron and \(B_3(D)\) its space of three distinct **unordered** points on the associated one-dimensional CW complex. Then

\[
H_3(B_3(D);\mathbb Z)\cong\mathbb Z^{26},\qquad H_j(B_3(D);\mathbb Z)=0\quad(j>3).
\]

This is a calculation of **integral top-degree homology**. It does not determine degree-one or degree-two homology, the ring structure, or the homotopy type of this configuration space.

## Assumptions and scope

Realize the dodecahedral graph as the generalized Petersen graph \(\operatorname{GP}(10,2)\) with vertices \(u_i,v_i\) for \(i\in\mathbb Z/10\mathbb Z\) and the 30 unoriented edges

\[
\{u_i,u_{i+1}\},\quad\{u_i,v_i\},\quad\{v_i,v_{i+2}\}\quad(i\in\mathbb Z/10\mathbb Z).
\]

For any graph \(G\), the unordered configuration space \(B_3(G)\) is the quotient by the permutation group \(\mathfrak S_3\) of the subspace of \(G^3\) consisting of ordered triples of pairwise distinct points. All homology is singular homology with integer coefficients.

The original vertices each have degree three. The zero-dimensional and higher-degree structure of the dodecahedral realization is taken literally as a graph; no ambient three-dimensional dodecahedral solid is used.

## Proof

**1. A chain model that computes the continuous configuration space.** The comparison theorem and all-vertex reduction of the Świątkowski chain model (An–Drummond-Cole–Knudsen, Construction 4.3, Theorem 4.5 and Proposition 4.9) identify \(H_*(B_3(D);\mathbb Z)\) with the weight-three homology of a reduced integral chain complex. For each vertex \(v\), order its incident half-edges \(h_0(v),h_1(v),h_2(v)\). The local reduced module has the empty generator and two degree-one generators

\[
a_1(v)=h_1(v)-h_0(v),\qquad a_2(v)=h_2(v)-h_0(v),
\]

with \(\partial a_j(v)=e_j(v)-e_0(v)\), where \(e_j(v)\) is the graph-edge polynomial generator incident at \(h_j(v)\). Each \(a_j(v)\) has weight one, and a graph-edge generator has weight one and homological degree zero. Degree-one factors at distinct vertices are ordered by the vertex index, so the graded Leibniz sign applies.

**2. The only map needed for the top group.** A weight-three chain can have homological degree at most three. In degree three there are three distinct vertices, each assigned one of the two local difference generators; in degree two there are two distinct vertices and one edge generator. Hence the exact chain-group ranks are

\[
\operatorname{rank} C_3=\binom{20}{3}2^3=9120,\qquad
\operatorname{rank} C_2=\binom{20}{2}2^2\cdot30=22800,\qquad C_4=0.
\]

For a basis monomial \(a_{j_1}(v_1)a_{j_2}(v_2)a_{j_3}(v_3)\) with \(v_1<v_2<v_3\), its signed boundary is

\[
\partial\bigl(a_{j_1}(v_1)a_{j_2}(v_2)a_{j_3}(v_3)\bigr)
=\sum_{t=1}^3(-1)^{t-1}
\bigl(e_{j_t}(v_t)-e_0(v_t)\bigr)
\prod_{s\ne t}a_{j_s}(v_s).
\]

These six edge-terms (with coefficients \(\pm1\)) specify the entire \(22800\times9120\) integral matrix \(\partial_3\). The standalone verifier builds it from the displayed graph and conventions, with no external files or mathematical software required.

**3. Integral rank with explicit kernel certificates.** The verifier reduces the columns in their stated lexicographic order over \(\mathbb Z\). At each nonzero residual it selects the largest row index as pivot; all \(9094\) such pivot coefficients have absolute value one, so each elimination is an integer unimodular column operation. The other \(26\) columns reduce exactly to zero. For every zero residual, the verifier tracks the corresponding integer linear combination of original columns and directly recomputes its full boundary to be zero. Moreover, the coefficient of the newly processed nonpivot column in that cycle is one and all other columns in its expression have lower index. The resulting \(26\) cycles are therefore linearly independent over \(\mathbb Z\). The integer column reduction proves that there can be no further independent kernel elements: it gives a rank-\(9094\) rationally independent collection of image columns, while precisely \(26\) independent null combinations account for the remaining \(9120-9094\) dimensions.

Since a subgroup of a free abelian group is free abelian, \(\ker\partial_3\cong\mathbb Z^{26}\). Because \(C_4=0\), there are no degree-three boundaries to quotient by; hence \(H_3\cong\mathbb Z^{26}\). Degree greater than three is absent from the chain model, proving the asserted vanishing.

## Verification

Run `python3 verify.py` in a standard-library Python 3 environment. It checks the 20 vertices, 30 edges, cubic incidence, every one of the 9,120 columns, 9,094 integer unit pivots, all 26 exact integer-cycle witnesses, and an independent characteristic-two elimination. It also enumerates cancellations in the compositions of adjacent local differentials to check that the signed boundary squares to zero. The recorded output in `verify.stdout` ends in `ALL_CHECKS_PASS`, and includes the SHA-256 digest of the canonical list of 26 integer witnesses.

Each integer pivot, cycle and zero-boundary check is recomputed rather than inferred from an earlier log. A mod-two computation alone would not establish the integral statement; it is secondary here.

## Relationship to prior work

Ghrist's 1999 work introduced homological and geometric questions for configurations on graphs, and Świątkowski's 2001 work studied their homological dimension. The 2017 preprint of An, Drummond-Cole and Knudsen provides the exact homology-computing chain model used here; its results for near-maximum homological degree relative to the number of essential vertices concern a different regime from three particles at 20 cubic vertices. Their later asymptotic Betti-number theorem concerns sufficiently many particles, not this fixed weight. An and Knudsen's theorem on the second homology of planar graph braid groups has a different homological degree.

A published calculation of the **two-particle** dodecahedral configuration space does not determine its **three-particle** top homology. Nearby computations for the Heawood and Pappus graphs involve different graphs. A targeted mathematical-record and literature comparison identified no explicit degree-three integral result for three unordered particles on the dodecahedral graph; this is evidence of a gap, not a proof of publication priority.

## Limitations

The group in homological degree three is determined integrally; nothing is asserted about \(H_1\), \(H_2\), multiplicative or equivariant homology, graph braid-group presentations or the full homotopy type. Reproducible exact arithmetic does not replace an independent review, and equivalent work may exist outside the inspected records. The comparison theorem and reduced-complex quasi-isomorphism are used as established published results, not reproved here.

## References

1. R. Ghrist, *Configuration spaces and braid groups on graphs in robotics*, arXiv:math/9905023, initial public version 1999-05-05, https://arxiv.org/abs/math/9905023.
2. J. Świątkowski, *Estimates for homological dimension of configuration spaces of graphs*, Colloq. Math. 89 (2001), 69–79, doi:10.4064/cm89-1-5, https://doi.org/10.4064/cm89-1-5.
3. B. H. An, G. C. Drummond-Cole and B. Knudsen, *Subdivisional spaces and graph braid groups*, first posted 2017-08-08, arXiv:1708.02351, https://arxiv.org/html/1708.02351v5.
4. B. H. An, G. C. Drummond-Cole and B. Knudsen, *Asymptotic homology of graph braid groups*, arXiv:2005.08286, https://arxiv.org/abs/2005.08286.
5. B. H. An and B. Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371, https://arxiv.org/abs/2008.10371.
