# Integral symmetry module of full strong Morse complexes of complete bipartite graphs

## Finding

For every integer \(n\ge2\), let \(X_n=\mathcal{SM}(K_{2,n})\) be the **full** strong discrete-Morse matching complex of the *unfilled one-dimensional* graph \(K_{2,n}\). The natural group \(G=S_2\times S_n\) acts by permuting its two-vertex class and its \(n\)-vertex class. There is a canonical \(G\)-equivariant exact sequence of integral lattices

\[
0\longrightarrow H_1(X_n;\mathbb Z)\longrightarrow\mathbb Z[E_n]\mathop{\longrightarrow}^{\varepsilon}\mathbb Z_{\mathrm{sgn}}\longrightarrow0,
\]

where \(E_n=\{A_i,B_i,C_i:1\le i\le n\}\), \(S_n\) permutes indices, and the nontrivial class swap \(s\in S_2\) acts by

\[
sA_i=-A_i,\qquad sB_i=-C_i,\qquad sC_i=-B_i.
\]

Here \(\varepsilon(A_i)=\varepsilon(B_i)=\varepsilon(C_i)=1\), with the target the rank-one lattice on which \(s\) acts by \(-1\) and \(S_n\) acts trivially. Thus, if \(f(\sigma)\) is the number of fixed points of \(\sigma\in S_n\), the character on \(H_1(X_n;\mathbb Q)\) is

\[
\chi(1,\sigma)=3f(\sigma)-1,\qquad
\chi(s,\sigma)=1-f(\sigma).
\]

The underlying homotopy type \(X_n\simeq\bigvee^{3n-1}S^1\) is included for context; the integral \(G\)-lattice and its character are the refinement asserted here.

## Assumptions and scope

Write the graph vertices as \(a_0,a_1,b_1,\ldots,b_n\), with all and only the edges \(a_tb_i\) for \(t\in\{0,1\}\) and \(1\le i\le n\). The graph is one-dimensional, not its clique or flag completion. A strong gradient is obtained from an injective vertex filtration using descending dominated vertices; in a graph a vertex is descending dominated precisely when it has a **unique** earlier neighbor. That vertex is paired to its incident edge to this neighbor. The simplicial complex \(X_n\) consists of all nonempty subsets of these gradients, for every filtration. Its vertices are the pairs

\[
x_{t,i}=(b_i,a_tb_i),\qquad y_{t,i}=(a_t,a_tb_i).
\]

The group action relabels indices and exchanges the values of \(t\). The hypothesis \(n\ge2\) is necessary for the two subcomplexes below to be connected. No assertion concerns the pure strong subcomplex or the ordinary Morse matching complex.

## Proof

**1. Every strong gradient.** Assume \(a_t\) precedes \(a_{1-t}\) in a filtration. Split the \(b\)-vertices into \(C,D,F\), respectively those preceding \(a_t\), between the two \(a\)-vertices, and following \(a_{1-t}\). Exactly these pairs occur: \(x_{t,i}\) for \(i\in D\); \(y_{t,i}\) for the unique \(i\in C\) if \(|C|=1\); and \(y_{1-t,i}\) for the unique \(i\in C\cup D\) if \(|C\cup D|=1\). No other vertex has precisely one earlier neighbor. For a one-dimensional graph there are no higher-dimensional face-pairs. Every disjoint triple \((C,D,F)\) can be realized by some total order, so this is an exact enumeration, not just an upper bound.

**2. Complete facet description.** For each \(t\), let \(T_t\) denote the simplex on \(\{x_{t,i}:1\le i\le n\}\); for each \(i\), let \(S_{t,i}\) denote the simplex on \(\{y_{t,i}\}\cup\{x_{t,j}:j\ne i\}\). Let \(U_t\) be the union of these \(n+1\) simplices and their faces. The enumeration in Step 1 says that the only simplices not contained in \(U_0\) or \(U_1\) are the three bridges, for each \(i\),

\[
A_i=[y_{0,i},y_{1,i}],\qquad B_i=[y_{0,i},x_{1,i}],\qquad C_i=[x_{0,i},y_{1,i}].
\]

Indeed a gradient with \(C=\varnothing\) and \(|D|=1\) supplies a bridge of type \(B\) or \(C\), and one with \(|C|=1,D=\varnothing\) supplies a bridge of type \(A\). If \(|D|\ge2\), the only arrows are \(x_{t,i}\); if \(|C|=1\) and \(|D|\ge1\), all arrows lie in one \(S_{t,i}\). Conversely each \(T_t,S_{t,i}\) and each bridge occurs as a complete gradient, so there are no additional facets. The full complex has \(5n+2\) facets.

**3. Contractible sides.** For \(n\ge2\), every \(S_{t,i}\) intersects \(T_t\) in the nonempty facet spanned by \(\{x_{t,j}:j\ne i\}\), and its extra vertex \(y_{t,i}\) lies in no other \(S_{t,j}\) for \(j\ne i\). Hence each \(S_{t,i}\) is a cone attached along its base and can be collapsed onto that base within \(U_t\). Thus \(U_t\) collapses onto \(T_t\) and is connected and contractible. The sides \(U_0,U_1\) have disjoint vertex sets.

**4. Integral equivariant exact sequence.** Set \(Y=U_0\sqcup U_1\subset X_n\). The relative cellular chain group \(C_1(X_n,Y;\mathbb Z)\) is free on the \(3n\) bridge edges oriented from \(U_0\) to \(U_1\); there are no relative cells in higher dimensions. Thus \(H_1(X_n,Y;\mathbb Z)=\mathbb Z[E_n]\). The homology sequence of the pair, using \(H_1(Y)=0\), identifies \(H_1(X_n)\) with the kernel of the relative boundary into \(\widetilde H_0(Y;\mathbb Z)\). Orienting each bridge from side zero to side one sends every basis edge to the same generator of this reduced \(H_0\), giving the map \(\varepsilon\). Permuting the \(b\)-indices acts on the three families as stated. Exchanging the two \(a\)-vertices reverses every bridge orientation and interchanges bridge types \(B,C\), while multiplying the reduced component-difference by \(-1\). This proves \(G\)-equivariance over \(\mathbb Z\) with no rationalization or splitting assumption.

**5. Character and topology.** For \((1,\sigma)\), the signed bridge module has trace \(3f(\sigma)\), and the sign target has trace \(1\). For \((s,\sigma)\), only the \(A\)-family can contribute to the trace and does so by \(-f(\sigma)\); the sign target contributes \(-1\). Exactness yields the two character formulas. Collapsing each contractible side to a point non-equivariantly leaves two points joined by \(3n\) intervals, proving \(X_n\simeq\bigvee^{3n-1}S^1\). The homotopy statement alone does not determine the above integral module.

## Verification

The companion `verify.py` uses only the Python standard library. It independently enumerates every total ordering of graph vertices for \(2\le n\le6\), constructs its gradient by counting earlier neighbors, and compares the **complete** face set with the proposed facet construction. It checks that every bridge is exactly one mixed edge and that the facets are inclusion-maximal. It then computes signed simplicial Lefschetz traces for automorphisms chosen from the symmetric group, with and without swapping the two bipartition classes, and checks them against the character formula. The recorded output is in `verify_output.txt` and finishes `ALL_VERIFY_OK`. These finite checks independently corroborate the structural proof; the universal claim is proved by Steps 1–5.

## Relationship to prior work

Knudson and Owens-White introduced the full strong matching complex and calculated it for paths, cycles, stars, simplices and simplex boundaries. In particular, their computation for the four-cycle, isomorphic to \(K_{2,2}\), gives a wedge of five circles; that agrees with this result but does not determine the integral bipartition symmetry action. An earlier classification of the **nonequivariant** homotopy type for complete bipartite strong complexes yields the rank \(3n-1\) in the two-by-\(n\) case, so that rank is **not claimed here as new**. Results for the **ordinary** discrete Morse matching complex of \(K_{2,n}\) concern a different simplicial complex and do not determine the action here. The new assertion is the integral signed-augmentation kernel and resulting complete rational character for every \(n\ge2\).

## Limitations

This identifies integral degree-one homology as a lattice, and its rational character, but does not provide an equivariant homotopy equivalence, a classification of the pure strong complex, or corresponding formulas when both bipartition classes have more than two vertices. Bibliographic searches cannot exclude undiscovered equivalent work; independent validation has not been performed.

## References

Kevin P. Knudson and Abigail Owens–White, *Complexes of strong discrete Morse matchings*, first posted September 6, 2026, arXiv:2609.06844, https://arxiv.org/html/2609.06844v1. Sections 3–4 (definitions and construction), Section 8 (four-cycle) and Section 10 (other families).
