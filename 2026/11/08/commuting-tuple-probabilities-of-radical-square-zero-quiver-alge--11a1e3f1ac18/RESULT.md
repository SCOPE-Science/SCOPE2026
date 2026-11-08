# Commuting-tuple probabilities of radical-square-zero quiver algebras recover the Tutte polynomial

## Finding

Let \(Q\) be a finite quiver with \(n\ge1\) vertices, \(m\ge0\) arrows, and **no loops**. Oppositely oriented arrows and parallel arrows are allowed. Write \(G\) for the undirected multigraph obtained by forgetting arrow directions but retaining every arrow as a distinct edge. For each prime power \(q\), put
\[
A_Q(q)=\mathbb F_q Q/J^2,
\]
where \(J\) is the arrow ideal. For an integer \(t\ge2\), let \(p_t(Q;q)\) be the probability that an ordered uniformly sampled \(t\)-tuple of elements of \(A_Q(q)\) commutes pairwise. Define the ordinary two-variable random-cluster polynomial
\[
Z_G(X,v)=\sum_{F\subseteq E(G)}X^{k(F)}v^{|F|},
\]
where \(k(F)\) is the number of connected components of the spanning multigraph \((V(G),F)\), including isolated vertices.

**Exact theorem.** For every such \(Q,q,t\),
\[
\boxed{p_t(Q;q)=q^{-tn-(t-1)m}\,Z_G(q^t,q^{t-1}-1).}
\]
Thus the complete pairwise-commutation probability is independent of arrow orientation and depends on \(G\) only through its ordinary Tutte polynomial (together with the known vertex and edge counts).

**Recovery theorem.** Fix the known counts \(n,m\), and fix **one** integer \(t>m\) with \(t\ge2\). The function \(q\mapsto p_t(Q;q)\), for all prime powers \(q\), uniquely determines the entire two-variable polynomial \(Z_G(X,v)\), hence the usual Tutte polynomial of \(G\). In particular, among loopless quivers with the same \(n,m\), equality of these probability functions for a single \(t>m\) is equivalent to equality of the underlying undirected multigraphs' Tutte polynomials. No graph-isomorphism reconstruction is asserted.

For a tree on \(n\ge2\) vertices and for a cyclically oriented or arbitrarily oriented simple cycle on \(n\ge3\) vertices, respectively, set
\[
U=q^t,\qquad a=\frac{1+(U-1)q^{1-t}}U,\qquad b=\frac{1-q^{1-t}}U.
\]
Then
\[
\boxed{p_t(\text{tree};q)=a^{n-1}},\qquad
\boxed{p_t(\text{cycle};q)=a^n+(U-1)b^n}.
\]
These identities hold for every prime power and every \(t\ge2\). For instance, at \(q=t=2\), a four-vertex tree has commuting-pair probability \(125/512\), while a triangle plus one isolated vertex (also four vertices and three edges) has probability \(1/4\). Therefore this invariant detects genuine cyclic dependence, rather than merely the number of arrows.

## Assumptions and scope

The path algebra convention is \(e_u a=a=a e_v\) for an arrow \(a:u\to v\). In the quotient by \(J^2\), every directed path of length at least two is zero, irrespective of whether the original quiver contains directed cycles. Every element is uniquely a sum of \(n\) vertex coefficients and \(m\) arrow coefficients. The algebra is associative, unital and has dimension \(n+m\) over \(\mathbb F_q\). All elements, rather than only units or idempotents, are sampled independently and uniformly.

The comparison polynomial is the ordinary (equal-edge-weight) Tutte/Potts polynomial, not the stronger multivariate Tutte polynomial with individually distinguished edges. The reconstruction theorem requires the values as \(q\) varies over infinitely many prime powers; it does **not** assert reconstruction from the probability at a single field size. It also assumes the vertex and arrow counts are given.

## Proof

**1. Coordinate-wise commutation.** For \(1\le j\le t\), write the \(j\)-th element as
\[
x^{(j)}=\sum_{v\in V(Q)}a_v^{(j)}e_v+\sum_{e\in E(Q)}b_e^{(j)}e.
\]
The arrow component of \([x^{(j)},x^{(\ell)}]\) at an arrow \(e:u\to v\) is
\[
(a_u^{(j)}-a_v^{(j)})b_e^{(\ell)}-(a_u^{(\ell)}-a_v^{(\ell)})b_e^{(j)}.
\]
Its diagonal component vanishes identically, and there are no terms from products of arrows because \(J^2=0\). Let
\[
\mathbf a_v=(a_v^{(1)},\ldots,a_v^{(t)})\in\mathbb F_q^t,\quad
\mathbf b_e=(b_e^{(1)},\ldots,b_e^{(t)})\in\mathbb F_q^t.
\]
All \(t\) elements commute pairwise exactly when
\[
(\mathbf a_u-\mathbf a_v)\wedge\mathbf b_e=0\quad\text{in }\bigwedge^2\mathbb F_q^t
\]
for every arrow. This equation means that the two vectors have rank at most one. If \(\mathbf a_u=\mathbf a_v\), every one of the \(q^t\) possible \(\mathbf b_e\) is allowed. Otherwise the allowed vectors are exactly the \(q\) multiples of the nonzero difference. This holds in characteristic two as well as odd characteristic, with no division by two.

**2. Finite-field count.** There are \(U=q^t\) choices for each vertex vector and, conditionally on all vertex vectors, independent arrow vectors. An arrow whose endpoints agree has conditional probability \(1\) of satisfying commutation; an arrow whose endpoints differ has probability \(q^{1-t}\). Hence
\[
p_t(Q;q)=U^{-n}\sum_{\sigma:V\to\mathbb F_q^t}
\prod_{e=uv}\left[q^{1-t}\bigl(1+(q^{t-1}-1)\mathbf 1_{\sigma(u)=\sigma(v)}\bigr)\right].
\]
Extracting the \(m\) common factors and expanding the product over subsets \(F\) of arrows gives
\[
p_t(Q;q)=U^{-n}q^{(1-t)m}
\sum_{F\subseteq E}(q^{t-1}-1)^{|F|}
\sum_{\sigma}\prod_{uv\in F}\mathbf 1_{\sigma(u)=\sigma(v)}.
\]
A coloring is constant on every connected component of \((V,F)\), so the innermost sum equals \(U^{k(F)}\). This proves the boxed exact identity and orientation independence, including repeated edges: each edge contributes its own independent arrow variable.

**3. Polynomial reconstruction.** Put \(H_G(X,Y)=Z_G(X,Y-1)\), an integer polynomial with \(\deg_Y H_G\le m\). Expand it uniquely as
\[
H_G(X,Y)=\sum_{0\le i\le n,\ 0\le j\le m}c_{ij}X^iY^j.
\]
The observed, known-normalization quantity is
\[
q^{tn+(t-1)m}p_t(Q;q)
=H_G(q^t,q^{t-1})
=\sum_{i,j}c_{ij}q^{t(i+j)-j}.
\]
For \(t>m\), the exponent mapping \((i,j)\mapsto t(i+j)-j\) is injective on this rectangle: if two exponents are equal, \(t\) divides the difference of their two \(j\)-indices, whose absolute value is at most \(m<t\), so the \(j\)-indices, then the \(i\)-indices, coincide. Therefore no coefficients coalesce under substitution. Since the last expression is a polynomial in the integer \(q\), and there are infinitely many prime powers, its values uniquely specify that polynomial and hence every \(c_{ij}\). Replacing \(Y\) by \(v+1\) reconstructs \(Z_G(X,v)\). The standard change of variables between \(Z_G\) and the ordinary Tutte polynomial completes the proof. The same argument establishes the stated equivalence for two graphs with known equal \(n,m\).

**4. Trees and cycles.** For a tree with \(n\) vertices the usual spanning-subgraph sum is \(Z_G(U,v)=U(U+v)^{n-1}\). For a simple cycle it is \(Z_G(U,v)=(U+v)^n+(U-1)v^n\). Substitute \(v=q^{t-1}-1\), multiply by the normalization from the exact theorem, and simplify. This produces the two formulas with \(a\) and \(b\) above. For the four-vertex tree \(a=5/8\) when \(q=t=2\), giving \(125/512\). For the triangle, \(a=5/8\), \(b=1/8\), and \(a^3+3b^3=1/4\). Adding an isolated vertex changes neither probability, since its coefficient algebra is a direct product factor that contributes probability one.

## Verification

The standalone standard-library program `verify.py` independently constructs multiplication in \(\mathbb F_q Q/J^2\) and tests commutation by multiplying actual elements, rather than using the proposed factorized probability. It performs exhaustive ordered-pair enumeration for multiple quivers of two through four vertices over \(\mathbb F_2\), and for a path and a triangle over \(\mathbb F_3\). It exhaustively checks all ordered triples for the triangle over \(\mathbb F_2\). These direct counts agree with independent spanning-subgraph enumeration, including orientation reversal, two parallel arrows, cycles, a tree, and a disconnected graph.

The program also verifies the known generalized Kronecker specialization, the closed tree/cycle formulas, and the coefficient-injection reconstruction on four small graphs. The execution ends `VERIFY_OK`. These finite tests are corroboration; the proof of the all-graph and all-field statements is the coordinate argument and the injectivity proof above.

## Relationship to prior work

The standard radical-square-zero quiver-algebra framework is used extensively in Laertis Vaso, *n-cluster tilting subcategories for radical square zero algebras*, arXiv:2105.05830v1 (12 May 2021), especially its notation and the identification of the arrow ideal. Vaso studies higher representation-theoretic subcategories, not the pairwise-commutation probabilities of algebra elements.

The Fortuin–Kasteleyn spanning-subgraph expansion and the tree/cycle evaluations of \(Z_G\) are classical; see Alan D. Sokal, *The multivariate Tutte polynomial (alias Potts model) for graphs and matroids*, arXiv:math/0503607v1 (25 March 2005), Section 2. The Potts polynomial itself, its spanning-subgraph expansion, and its known relations to the Tutte polynomial are not claimed as new. The claimed new connection is the exact realization of this polynomial as a family of algebraic commuting-tuple probabilities, together with the fixed-arity polynomial-reconstruction result.

A prior published calculation for the two-vertex generalized Kronecker path algebra gives the commuting-pair probability \(q^{-2}+(q^2-1)q^{-r-2}\) with \(r\) parallel arrows. That formula is **fully covered as a specialization** of the present identity (two vertices, \(t=2\)); its recovery is not claimed as new. Its two-vertex family cannot imply the arbitrary-graph polynomial or the Tutte reconstruction theorem. Dutta, Basnet and Nath, *Commuting probabilities of n-centralizer finite rings*, arXiv:1803.04111v1 (12 March 2018), analyzes centralizer-based classes, not the proposed graph/Tutte identity.

Pavel Shumyatsky and Matteo Vannacci, *Commuting and product-zero probability in finite rings*, arXiv:2307.12633v1 (24 July 2023), gives structural bounds from a ring's two-element commuting probability, not an exact graph-indexed family or higher-tuple distribution. Green and Schroll, *The Commuting Algebra*, arXiv:2302.08169v1 (16 February 2023), studies a quotient obtained by identifying parallel paths, a different use of the word “commuting”.

## Limitations

The quiver must be finite and loopless; loops would require a separate treatment and are not asserted here. The relations are exactly those killing paths of length at least two. No result is claimed for general admissible ideals, full path algebras of arbitrary acyclic quivers, or the distribution of commuting tuples conditioned on units or idempotents.

The calculation recovers the **ordinary** Tutte polynomial when the entire prime-power field-size profile is known at one sufficiently large tuple arity. It cannot distinguish two graphs with equal Tutte polynomials; it does not prove that finitely many small fields suffice, and it does not recover the full edge-labeled multivariate Tutte polynomial. Formulae for trees and cycles are inherited from the classical Tutte polynomial once the algebraic identity is proved.

Novelty is assessed relative to the cited inspected literature and accessible mathematical-record comparisons, not as an exhaustive assertion about all possible terminology or unpublished work. 

## References

1. L. Vaso, *n-cluster tilting subcategories for radical square zero algebras*, arXiv:2105.05830v1, 2021, https://arxiv.org/abs/2105.05830.
2. A. D. Sokal, *The multivariate Tutte polynomial (alias Potts model) for graphs and matroids*, arXiv:math/0503607v1, 2005, https://arxiv.org/abs/math/0503607.
3. P. Shumyatsky and M. Vannacci, *Commuting and product-zero probability in finite rings*, arXiv:2307.12633v1, 2023, https://arxiv.org/abs/2307.12633.
4. J. Dutta, D. K. Basnet and R. K. Nath, *Commuting probabilities of n-centralizer finite rings*, arXiv:1803.04111v1, 2018, https://arxiv.org/abs/1803.04111.
5. E. L. Green and S. Schroll, *The Commuting Algebra*, arXiv:2302.08169v1, 2023, https://arxiv.org/abs/2302.08169.
6. *Commutator fibers and commuting probabilities of finite Kronecker path algebras*, previously disseminated mathematical note; the exact two-vertex formula is acknowledged above.
