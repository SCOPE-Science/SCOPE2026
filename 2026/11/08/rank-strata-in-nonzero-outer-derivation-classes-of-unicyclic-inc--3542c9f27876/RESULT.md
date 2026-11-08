# Rank strata in nonzero outer-derivation classes of unicyclic incidence algebras

## Finding
Let \(k=\mathbb F_q\) be any finite field and \(P\) a finite connected height-two poset whose undirected comparability graph \(G\) is unicyclic. Write \(m=|E(G)|=|V(G)|\), and let \(\ell\ge4\) be the (necessarily even) length of the unique cycle. Put \(A=I(P,k)\), let \(\operatorname{Der}_k(A)\) denote the \(k\)-linear associative derivations, and let \(\operatorname{IDer}_k(A)\) denote the inner derivations.

There is a natural one-dimensional quotient \(\operatorname{Der}_k(A)/\operatorname{IDer}_k(A)\cong k\), obtained by taking an alternating signed sum of edge coefficients around the unique cycle. After choosing one direction of traversal and identifying the quotient with \(k\), **every nonzero quotient class \(\lambda\in k^\times\) has the same exact rank enumerator**:

\[
\boxed{\sum_{\substack{D\in\operatorname{Der}_k(A)\\[D]=\lambda}}T^{\operatorname{rank}_k D}
=\frac{(1+(q^2-1)T)^{m-\ell}}{q}\left((1+(q^2-1)T)^\ell-(1-T)^\ell\right).}
\]

In particular, **every nonzero outer-derivation class contains exactly \(q\ell\) rank-one representatives**, and representatives of every rank \(1,2,\dots,m\) occur. The complete enumerator over all non-inner derivations is \(q-1\) times the displayed polynomial. The rank-one multiplicity in any nonzero class recovers the unique cycle length \(\ell\) when the field is known.

## Assumptions and scope
The poset is connected, finite and of height two, so all strict comparabilities join a minimal element to a maximal element. Its graph is simple, bipartite and has exactly one undirected cycle, of even length at least four; trees may be attached arbitrarily to cycle vertices. The ground field is arbitrary finite \(\mathbb F_q\), including characteristic two. Derivations are ordinary \(k\)-linear maps satisfying \(D(xy)=D(x)y+xD(y)\), and rank refers to rank of the linear transformation \(A\to A\), **not** its class in the quotient. A nonzero quotient class is a fixed affine coset of \(\operatorname{IDer}_k(A)\), not a quotient element counted once.

## Proof
**1. Explicit derivations.** Let \(p_v=e_{vv}\) be the vertex idempotents and \(a_e=e_{uv}\) the radical basis element for each edge \(e:u<v\). All products of two arrows vanish. The identity \(D(p_v^2)=D(p_v)p_v+p_vD(p_v)\), together with orthogonality of the vertex idempotents, forces each derivation to be specified uniquely by independent coefficient pairs \((\beta_e,z_e)\in k^2\) for all edges:
\[
D(a_e)=\beta_e a_e,\qquad
D(p_u)=\sum_{e:u\to v}z_ea_e-\sum_{e:v\to u}z_ea_e.
\]
These formulas satisfy the Leibniz rule on all pairs of basis elements: the only nonzero basis products are \(p_v^2=p_v\), \(p_ua_e=a_e\), and \(a_ep_v=a_e\). Hence \(\operatorname{Der}_k(A)\cong k^{2m}\) as a vector space. Here \(u\to v\) always follows the poset order.

**2. Detecting innerness.** For a commutator derivation \(D=\operatorname{ad}_x\), the coefficients \(\beta_e\) equal a vertex potential difference \(d_u-d_v\). Conversely, if such vertex potentials exist, arbitrary \(z_e\) can be realized by the radical coordinates of \(x\). Because \(G\) is connected unicyclic, a potential exists exactly when the signed sum of \(\beta_e\) along its unique cycle vanishes. Fix a traversal and let \(\epsilon_e\in\{1,-1\}\) be the signs of its oriented edges. The quotient-class coordinate is
\[
\omega(D)=\sum_{e\text{ on cycle}}\epsilon_e\beta_e.
\]
Thus \(D\) is inner if and only if \(\omega(D)=0\). Each specified value \(\omega(D)=\lambda\) defines one full affine cohomology class, and the quotient is one-dimensional.

**3. Rank of an outer derivation.** The image lies in the arrow radical. The matrix of \(D\), with arrow rows and vertex-plus-arrow columns, has in edge row \(e:u<v\) the entries \(z_e\) at vertex \(u\), \(-z_e\) at vertex \(v\), and \(\beta_e\) at its private arrow column. Every row with \(\beta_e\ne0\) is an independent pivot. The remaining nonzero rows are weighted signed-incidence rows supported on edges with \(\beta_e=0\) and \(z_e\ne0\). If \(\omega(D)\ne0\), at least one edge of the unique cycle has nonzero \(\beta_e\); hence the remaining support is a forest. Signed-incidence rows of a forest are linearly independent over **every** field. Therefore
\[
\operatorname{rank}_k D=\#\{e:(\beta_e,z_e)\ne(0,0)\}\quad\text{whenever }\omega(D)\ne0.
\]

**4. Counting one nonzero class.** For each of the \(m-\ell\) off-cycle edges, an independent coefficient pair contributes \(1+(q^2-1)T\). Along the unique cycle, prescribe a nonzero signed sum \(\lambda\). If exactly \(j\) specified cycle edges have nonzero coefficient pairs, the number of choices with signed sum \(\lambda\) is
\[
B_j=\frac{(q^2-1)^j-(-1)^j}{q}.
\]
Indeed, insert the additive-character orthogonality relation for the linear equation on the first coordinates. For a nontrivial additive character, summing over the \(q^2-1\) nonzero pairs gives \(-1\), whereas the trivial character gives \(q^2-1\). Summing all nontrivial characters at \(\lambda\ne0\) gives \(-1\). The sign of an edge coefficient merely permutes field values and does not change the character sum. Consequently the cycle contribution is
\[
\sum_{j=0}^{\ell}\binom\ell j B_jT^j
=\frac{(1+(q^2-1)T)^\ell-(1-T)^\ell}{q}.
\]
Multiplying by the off-cycle contribution proves the claimed enumerator. Its coefficient of \(T\) is \(\ell(q^2-1+1)/q=q\ell\); the constant coefficient is zero, and the term at every degree through \(m\) is positive, as also follows by choosing one nonzero potential-difference coefficient on the cycle and adding arbitrary active edge pairs with zero first coordinate.

**5. Consistency counts.** Setting \(T=1\) yields \(q^{2m-1}\) derivations in each class, as expected from the surjective linear quotient map \(k^{2m}\to k\). There are \(q-1\) nonzero classes, and the full non-inner enumerator is their disjoint sum.

## Verification
The standalone program `verify_outer.py` constructs multiplication and derivation matrices for height-two incidence algebras, computes linear ranks over prime fields and over \(\mathbb F_4\), and checks innerness independently by solving for vertex potentials. It exhaustively enumerates every derivation for the four-cycle over fields of orders \(2,3,4\); the six-cycle over \(\mathbb F_2\); and a four-cycle with one pendant edge over fields of orders \(2,3\). It checks the defining Leibniz identity on sample coefficient choices, every rank coefficient of the theorem, the constant rank profile across all nonzero quotient classes, and the total class size. All tests return `VERIFY_OK`. These finite tests corroborate but do not substitute for the all-field character-sum proof.

## Relationship to prior work
Krylov and Tuganbaev (first public preprint May 4, 2023) describe the derivation module of general incidence rings and characterize inner additive derivations by vanishing fundamental-cycle weights; their framework supplies the structural context for the cycle functional used above. Fornaroli and Khrypchenko (first public preprint July 17, 2023) identify quotients of skew derivations by inner skew derivations with a poset cohomology group, including the ordinary-derivation specialization. Neither inspected paper supplies the prescribed **nonzero outer-class rank distributions** or the exact \(q\ell\) rank-one count.

General enumerations for ranks of **inner commutator maps** and ordinary commuting probabilities concern a different collection of linear transformations; they are not claimed anew here. The new counting step is the fixed-nonzero-cycle-weight enumeration of **all derivation representatives** in a particular outer class. No assertion of established publication priority or independent verification is made.

## Limitations
The result is restricted to ordinary field-linear derivations of incidence algebras of connected height-two unicyclic posets. It does not classify twisted derivations, graphs with multiple cycles, posets of greater height, non-field coefficients or arbitrary quivers with parallel arrows. The full general literature may contain an equivalent rank enumeration under another formulation; none was identified in the checked sources. The independent mathematical audit has not been performed.

## References
1. P. Krylov and A. Tuganbaev, *Incidence Rings: Automorphisms and Derivations*, arXiv:2305.02984, first posted 2023-05-04. In particular Sections 17–19 and Corollary 18.8.
2. É. Z. Fornaroli and M. Khrypchenko, *Skew derivations of incidence algebras*, arXiv:2307.08439, first posted 2023-07-17. In particular Theorem 3.7 and Corollary 3.8.
