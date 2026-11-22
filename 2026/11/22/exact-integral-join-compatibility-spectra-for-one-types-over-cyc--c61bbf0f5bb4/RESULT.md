# Exact integral join-compatibility spectra for one-types over cycles in the triangle-free homogeneous graph

## Finding

Let \(\mathcal H_3\) be the countable homogeneous universal triangle-free graph. For every integer \(n\ge4\), individually name the vertices of an induced cycle \(C_n\). Complete nonalgebraic one-point types are indexed by the independent sets \(S\subseteq V(C_n)\), including the empty set: \(S\) is the set of old vertices adjacent to the new vertex. Two types \(S,T\) are **join-compatible** if the union of their positive adjacency requirements is consistent as the positive adjacency set of a single further nonalgebraic one-point type. (The negative requirements of the original types are not imposed on this union.) Define the symmetric integer matrix \(M_n\), indexed by all these types, by \((M_n)_{S,T}=1\) exactly when the two types are join-compatible.

Let \(m_n=F_{n-1}+F_{n+1}\) be the number of independent sets of \(C_n\), with Fibonacci numbers \(F_0=0\), \(F_1=1\). Define \(s_0=3\), \(s_1=0\), \(s_2=2\), and \(s_n=s_{n-2}+2s_{n-3}\) for all \(n\ge3\), and put
\[
r_n=s_n+1-3\mathbf1_{\{3\mid n\}}.
\]
Then the complete integer Smith normal form of this \(m_n\)-square matrix is
\[
\boxed{\operatorname{SNF}_{\mathbb Z}(M_n)=
\begin{cases}
\operatorname{diag}(I_{r_n},0_{m_n-r_n}),&3\nmid n,\\
\operatorname{diag}(I_{r_n-1},[2],0_{m_n-r_n}),&3\mid n.
\end{cases}}
\]
Thus its finite cokernel torsion is either trivial or exactly \(\mathbb Z/2\mathbb Z\), with the latter occurring precisely when \(3\mid n\). Its rank over any field of odd characteristic is \(r_n\), and its rank in characteristic two is \(r_n-\mathbf1_{\{3\mid n\}}\). The first cycle base exhibiting a nonunit Smith factor is \(C_6\).

For \(n=4,5,6,7,8,9,10\), the respective matrix orders are \(7,11,18,29,47,76,123\), the rational ranks are \(3,11,12,15,35,40,63\), and only \(n=6,9\) exhibit a nonunit Smith factor in this range.

## Assumptions and scope

Work in the pure symmetric irreflexive graph language. All parameters are named individually and induce exactly the cycle \(C_n\). An independent subset is a set spanning no edge. A type prescribes both the positive and negative adjacencies of a new point to all named vertices, but **join-compatibility concerns only the union of its positive requirements**; it does not ask for a pair of new points to be adjacent or for a single new point to realize both full original types. The object is a natural consistent-positive-literal join relation on complete one-types, not the usual existential pair-adjacency feasibility matrix.

## Proof

**1. Type classification and join criterion.** The Henson triangle-free graph has the extension property for finite independent neighborhoods and eliminates quantifiers, so a complete nonalgebraic one-point type over \(C_n\) is uniquely specified by an independent set \(S\) of old neighbors. Any positive adjacency set \(U\subseteq V(C_n)\) can be extended to a nonalgebraic one-point type exactly when \(U\) is independent: an edge inside \(U\) would form a triangle with the new vertex, whereas independent \(U\) is realized by the extension property. Therefore
\[
\boxed{(M_n)_{S,T}=\mathbf1_{\{S\cup T\in\Delta\}},}
\]
where \(\Delta=\operatorname{Ind}(C_n)\) includes the empty face.

**2. Unimodular zeta factorization.** Order the faces of \(\Delta\) by nondecreasing cardinality and form the integer incidence matrix \(Z_{S,F}=\mathbf1_{\{S\subseteq F\}}\), which is upper triangular with all diagonal entries one. For each face \(F\), put
\[
w(F)=\sum_{G\in\Delta,\,G\supseteq F}(-1)^{|G|-|F|}.
\]
Boolean-interval inclusion-exclusion gives, for any faces \(S,T\),
\[
\sum_{F\in\Delta,\,F\supseteq S\cup T}w(F)
=\mathbf1_{\{S\cup T\in\Delta\}}.
\]
Indeed, for \(S\cup T\in\Delta\) the inner sum over intermediate faces between \(S\cup T\) and \(G\) vanishes unless \(G=S\cup T\); for a nonface there are no qualifying \(F\). Hence the **exact integer-unimodular congruence** is
\[
\boxed{M_n=Z\operatorname{diag}_{F\in\Delta}(w(F))Z^{\mathsf T}.}
\]
The weights are evaluations \(w(F)=I(C_n[V\setminus N[F]],-1)\) of the independence polynomial of the induced graph outside the closed neighborhood of \(F\), where \(I(G,z)=\sum_{J\in\operatorname{Ind}(G)}z^{|J|}\).

**3. Link weights and the unique possible nonunit factor.** For a path on \(t\) vertices put \(p_t=I(P_t,-1)\). The deletion recurrence gives \(p_0=1\), \(p_1=0\), and \(p_t=p_{t-1}-p_{t-2}\). Therefore \(p_t\) is periodic with six terms \(1,0,-1,-1,0,1\) and is zero precisely when \(t\equiv1\pmod3\). For a nonempty independent face \(F\), list its selected vertices in cyclic order and let \(d_i\ge2\) be the cyclic distances between successive selected vertices (for a singleton, its sole distance is \(n\)). The induced graph outside \(N[F]\) is the disjoint union of paths on \(\max(d_i-3,0)\) vertices. Consequently
\[
w(F)=\prod_i p_{\max(d_i-3,0)},
\]
which lies in \(\{-1,0,1\}\) and is nonzero exactly when no \(d_i\equiv1\pmod3\). For the empty face, the transfer matrix \(\begin{psmallmatrix}1&-1\\1&0\end{psmallmatrix}\), whose eigenvalues are \(e^{\pm i\pi/3}\), yields
\[
w(\varnothing)=I(C_n,-1)=2\cos(n\pi/3).
\]
Its absolute value is two exactly when \(3\mid n\), otherwise one. Since \(Z\) is integer-unimodular, this proves that there is at most one nonunit Smith factor, equal to two, and it occurs exactly as stated.

**4. Rank formula.** All diagonal weights other than the empty-face weight are nonzero precisely for independent sets whose cyclic gaps belong to \(\{2,3,5,6,8,9,\ldots\}\). Their gap generating function is
\[
A(z)=\frac{z^2+z^3}{1-z^3}.
\]
For each \(k\ge1\), rooted cyclic-gap tuples of length \(k\) with total length \(n\) give \(n[z^n]A(z)^k\) rooted sets; every actual \(k\)-point set is counted \(k\) times. Thus the total number of nonempty faces with nonzero weight is
\[
\sum_{k\ge1}\frac nk[z^n]A(z)^k
=n[z^n]\log\!\left(\frac{1-z^3}{1-z^2-2z^3}\right).
\]
Let \(\alpha_1,\alpha_2,\alpha_3\) be the roots of \(u^3-u-2=0\), and let \(s_n=\sum_{i=1}^3\alpha_i^n\). The characteristic equation gives the stated integer recurrence and initial conditions. Since \(1-z^2-2z^3=\prod_i(1-\alpha_i z)\), the preceding coefficient is \(s_n-3\mathbf1_{\{3\mid n\}}\). Adding the always nonzero empty face gives exactly \(r_n\), completing the Smith and field-rank formulas.

## Verification

The standalone exact-integer script `verify.py` reconstructs \(M_n\) from the union-independence criterion, compares independent inclusion-exclusion weights with the path-link formula, checks the entire matrix congruence and computes direct Smith normal forms for \(4\le n\le10\). It also checks rank and exceptional weights through \(n=19\). The proof above, rather than this finite computation, establishes all \(n\ge4\).

## Relationship to prior work

The Henson construction and Conant's 2014 account establish the generic triangle-free graph and complete one-point types. Kozlov's earlier homotopy classification of cycle and path independence complexes explains the period-three Euler characteristic of the empty-face link, but does not compute the rank or Smith factors of this join-compatibility matrix. Knill's counting and connection matrices instead encode the number of subsimplices in intersections or nonempty intersection; their general unimodularity conclusions do not apply to the present union-compatible matrix, which can be singular and have a factor two. The finite-face zeta inversion used here is elementary and is not claimed as new in isolation.

## Limitations

The join relation explicitly discards the negative literals of the input types, and is **not** the adjacency-feasibility relation between two realizations (which has a different matrix). Only induced cycle parameter bases are classified; general triangle-free bases may have richer link Euler weights. The historical-literature search is not exhaustive, particularly for differently named union-of-faces matrices.

## References

1. C. Ward Henson, *A family of countable homogeneous graphs*, Pacific Journal of Mathematics 38 (1971), 69–83.
2. Gabriel Conant, *Forking and dividing in Henson graphs*, arXiv:1401.1570, first posted 2014-01-08. https://arxiv.org/abs/1401.1570
3. Dmitry Kozlov, *Combinatorial Algebraic Topology*, Springer, 2008, Proposition 11.17. https://webhomes.maths.ed.ac.uk/~v1ranick/papers/kozlov.pdf
4. Oliver Knill, *The counting matrix of a simplicial complex*, arXiv:1907.09092 (2019). https://people.math.harvard.edu/~knill/graphgeometry/papers/slnz.pdf
