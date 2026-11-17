# Signed equivariant sphere models for acyclic directed-subgraph complexes

## Finding
For a finite nonempty loopless simple directed graph \(D=(V,E)\), let \(\mathcal A(D)\) be the simplicial complex of arc subsets without directed cycles (a pair of oppositely directed arcs is a directed two-cycle). Let \(C_1,\ldots,C_k\) be the strongly connected components of \(D\). Define
\[
W_D=\{x\in\mathbb R^V:\sum_{v\in C_i}x_v=0\text{ for }1\le i\le k\}.
\]
The *signed symmetry group* \(\Gamma_D\) consists of pairs \((\sigma,\varepsilon)\), where \(\sigma\) permutes \(V\), \(\varepsilon\in\{+1,-1\}\), and the action on arcs given by \((i\to j)\mapsto(\sigma(i)\to\sigma(j))\) for \(\varepsilon=+1\) and \((i\to j)\mapsto(\sigma(j)\to\sigma(i))\) for \(\varepsilon=-1\) preserves \(E\). It acts on \(W_D\) by \(x\mapsto\varepsilon P_\sigma x\).

**Theorem (one dichotomy).** If \(D\) has any arc between distinct strongly connected components, \(|\mathcal A(D)|\) is \(\Gamma_D\)-equivariantly contractible. Otherwise, there is a genuine \(\Gamma_D\)-equivariant homotopy equivalence
\[
|\mathcal A(D)|\simeq_{\Gamma_D} S(W_D),
\]
where \(S(W_D)\) is the Euclidean unit sphere, interpreted as empty when \(W_D=0\). Consequently, for every subgroup \(H\le\Gamma_D\), its actual geometric fixed-point space is contractible in the first case and homotopy equivalent to \(S(W_D^H)\) in the second. Thus the latter is empty when \(\dim W_D^H=0\), and otherwise is \(S^{\dim W_D^H-1}\).

For the complete bidirected graph \(\overleftrightarrow{K_n}\), \(n\ge2\), the symmetry group includes \(S_n\times C_2\), with \(C_2\) reversing every arrow. Let \(H\le S_n\times C_2\), and call an orbit \(O\) of its projected permutation group *balanced* if every signed group element fixing a chosen \(v\in O\) has positive sign. Let \(b\) count balanced orbits and let \(o\) count all projected orbits. Then
\[
\dim W^H=\begin{cases}o-1,&H\subseteq S_n\times\{+1\},\\b,&\text{otherwise.}\end{cases}
\]
This is an explicit classification for every subgroup, including mixed permutations and global reversals. In particular, the arrow-reversal quotient is homotopy equivalent to \(\mathbb{RP}^{n-2}\); hence for \(n\ge4\) its first integral homology is \(\mathbb Z/2\). The orientation character on top integral homology is \((\sigma,\varepsilon)\mapsto\operatorname{sgn}(\sigma)\varepsilon^{n-1}\).

## Assumptions and scope
All graphs are finite, nonempty, without loops or parallel arcs. Directed cycles include length two. The complex consists of *all* acyclic subsets of the specified arc set, not directed forests, the non-strong-connectivity complex, or a quotient of graph realizations. The group \(\Gamma_D\) is finite. An equivariant homotopy equivalence means equivariant maps with equivariant homotopies, and therefore homotopy equivalences on every subgroup-fixed space; no PL homeomorphism is claimed. The sphere of a zero-dimensional vector space and the geometric realization of a complex with no nonempty faces are both empty.

## Proof
**1. Component reduction.** Write \(E=E_{\mathrm{int}}\sqcup E_{\mathrm{cross}}\) according as endpoints lie in the same or distinct strongly connected components. A directed cycle cannot use an arc in \(E_{\mathrm{cross}}\). Therefore
\[
\mathcal A(D)=2^{E_{\mathrm{cross}}}*\mathcal A(D|_{E_{\mathrm{int}}}),
\]
with the conventional interpretation when a factor has no vertices. If \(E_{\mathrm{cross}}\ne\varnothing\), the full simplex on those arcs has a \(\Gamma_D\)-fixed barycenter, even when the group permutes its vertices. Contracting the join toward that barycenter gives an equivariant contraction. This also proves that every subgroup-fixed space is contractible in this case.

**2. Open-sphere covering in the remaining case.** Suppose \(E_{\mathrm{cross}}=\varnothing\). Every arc \(a=(i\to j)\) has both endpoints in one strongly connected component. For \(W_D\ne0\), set
\[
U_a=\{x\in S(W_D):x_j-x_i>0\}.
\]
These open hemispheres cover \(S(W_D)\): if \(x\) lies in none of them, each directed arc gives \(x_j\le x_i\); moving along directed paths both ways inside an SCC forces all its coordinates equal. Its zero-sum condition forces these coordinates to be zero, contrary to \(\|x\|=1\).

For every nonempty arc set \(F\), its intersection \(U_F=\bigcap_{a\in F}U_a\) is nonempty exactly when \(F\) is acyclic. A directed cycle would give incompatible strict inequalities. Conversely a topological ordering of an acyclic \(F\), applied component by component and translated to zero mean on each component, gives a point satisfying every strict inequality; normalization puts it on the sphere. Hence the nerve of this covering is **exactly** \(\mathcal A(D)\), with no extra or missing faces.

**3. Fixed-intersection condition and genuine equivariance.** The signed action on \(W_D\) maps \(U_a\) to \(U_{ga}\): when an arrow is reversed, the vector coordinates are simultaneously negated. Let \(L\le\Gamma_D\) stabilize a nonempty intersection \(U_F\) setwise. Its unnormalized cone
\[
C_F=\{x\in W_D:x_j-x_i>0\text{ for every }(i\to j)\in F\}
\]
is nonempty, open, convex, invariant under \(L\), and excludes the origin. For any \(x\in C_F\), the average \(y=|L|^{-1}\sum_{g\in L}gx\) still satisfies all strict inequalities and is fixed by \(L\). Normalizing \(y\) gives an \(L\)-fixed point of \(U_F\); normalized straight-line homotopy from any other point of \(U_F\) to that fixed point is \(L\)-equivariant. This remains true for every subgroup of every setwise stabilizer.

For completeness, the finite equivariant good-cover nerve argument can be expressed using the incidence space of pairs \((x,t)\) with \(x\in U_F\) when the barycentric point \(t\) has support \(F\). Its projections to the covered sphere and the nerve are equivariant homotopy equivalences: over an \(x\) the index simplex contracts equivariantly, using a group-averaged partition of unity; over the relative interior of any face, every stabilizer-fixed intersection contracts as proved above. Applying the ordinary nerve comparison on every subgroup-fixed diagram (equivariant Whitehead for finite CW type) gives a genuine \(\Gamma_D\)-equivalence. If \(W_D=0\), every strongly connected component is a singleton, and with no cross arcs the graph has no arcs; both geometric realizations are empty. This finishes the dichotomy.

**4. Explicit complete-graph fixed dimensions.** Here \(W=\{x\in\mathbb R^n:\sum_i x_i=0\}\). The equation for an \(H\)-fixed vector is \(x_{\sigma(i)}=\varepsilon x_i\) for every \((\sigma,\varepsilon)\in H\). On each projected orbit this system has dimension one exactly when the sign assignment is consistent around all stabilizer relations (a balanced orbit), and zero otherwise. If all signs are positive, the global zero-sum equation imposes one independent constraint on the orbit constants, giving \(o-1\). If a negative-sign element exists, every balanced-orbit vector has coordinate sum zero (the negative element sends that sum to its own negative), so no additional constraint occurs and the dimension is \(b\). Unit spheres in these fixed subspaces supply every claimed fixed homotopy type.

Global arrow reversal acts on \(W\) by \(-I\). Therefore the genuine equivariant equivalence descends to a homotopy equivalence of its geometric quotient with \(S^{n-2}/\{\pm I\}=\mathbb{RP}^{n-2}\). Finally, the top-homology action of a sphere is its representation determinant; the permutation augmentation determinant is \(\operatorname{sgn}(\sigma)\), and \(-I\) has determinant \((-1)^{n-1}\).

## Verification
Two standalone standard-library Python scripts accompany this result. `verify_signed_dag.py` constructs fixed-face orbit complexes of complete bidirected graphs, calculates their reduced homology over \(\mathbb F_2\), and compares against the dimensions predicted from actual signed permutation subgroup stabilizers. It checked 93 subgroup cases for \(2\le n\le6\). `verify_signed_dag_general.py` tests 491 directed-graph/signed-symmetry pairs, with and without arcs across strong components, using independent SCC construction and rational row-reduction of the predicted real fixed-subspace dimension. Recorded output is in `verification_output.txt`. Finite-field ranks are corroboration, not a proof of integral homotopy or an infinite theorem; those are supplied by the covering and contraction arguments above.

## Relationship to prior work
Hultman's 2004 Theorem 3.3 classifies the ordinary homotopy type of this **same acyclic directed-subgraph complex** as a sphere or contractible, according to its SCC decomposition. That result is expressly not claimed here as new. Björner–Welker previously proved the ordinary sphere for the complete case. Ayzenberg–Beketov–Magai give the open-hemisphere/type-\(A\) root realization for the complete case, also as an ordinary homotopy equivalence. The additional statement here concerns arbitrary signed graph automorphisms, the stabilizer-fixed intersections required for a *genuine* equivariant equivalence, the complete fixed-point dimensions, and the resulting projective-space reversal quotients. Ordinary sphere homotopy, ordinary character calculations, or an unequivariant nerve identification alone do not imply these conclusions. An equivalent equivariant refinement in older or unindexed work remains a publication-priority risk.

## Limitations
The result concerns the acyclic-**arc-subset** simplicial complex of finite simple loopless digraphs; it is not an assertion about directed flag, directed forest, multipath, or non-strong-connectivity complexes. There is no assertion of a canonical PL homeomorphism, of smooth equivalence, or of a sphere model for other monotone graph properties. Explicit fixed-space dimensions outside the complete case require computation of a finite real fixed subspace, although the dichotomy holds for every finite digraph. The full 1999 Björner–Welker article was not available for line-by-line comparison (institutional full-text access was unavailable); its inspected abstract states the ordinary result, and the directly inspected 2004/2023 texts do not state the signed-equivariant conclusion. Independent mathematical checking has not been performed.

## References
1. A. Hultman, *Directed subgraph complexes*, Electronic Journal of Combinatorics 11 (2004), R75; published 2004-10-26. Theorem 3.3. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v11i1r75/pdf/
2. A. Björner and V. Welker, *Complexes of directed graphs*, SIAM Journal on Discrete Mathematics 12 (1999), 413–424. DOI: 10.1137/S0895480198338724.
3. A. Ayzenberg, M. Beketov and G. Magai, *Coverings by open and closed hemispheres*, arXiv:2310.02827 (first posted 2023-10-04), Theorem 1 and Proposition 1.1. https://arxiv.org/pdf/2310.02827
4. J. Thévenaz and P. Webb, *Homotopy equivalence of posets with a group action*, Journal of Combinatorial Theory, Series A 56 (1991), 173–181; cited as general equivariant background, not as a source of this graph-specific result.
