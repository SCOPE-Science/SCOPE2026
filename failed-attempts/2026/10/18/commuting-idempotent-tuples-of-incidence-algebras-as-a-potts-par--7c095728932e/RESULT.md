# Commuting idempotent tuples of incidence algebras as a Potts partition function

## Finding

Let \(P\) be any nonempty finite poset, \(q\ge 2\) any prime power, and \(k\ge2\) any integer. Let \(A=I(P,\mathbf F_q)\) be its incidence algebra. Define \(C_k(P;q)\) to be the number of **ordered** \(k\)-tuples \((e_1,\ldots,e_k)\in A^k\) such that \(e_i^2=e_i\) for all indices and \(e_ie_j=e_je_i\) for every pair. Let \(\Gamma(P)\) be the simple comparability graph of \(P\): its vertices are \(P\), and there is one edge for each unordered pair of distinct comparable elements. Write \(m=|E(\Gamma(P))|\) and \(Q=2^k\). Then

\[
\boxed{C_k(P;q)=\sum_{c:P\to\{0,1\}^{k}}q^{d(c)},\qquad d(c)=|\{(x,y):x<y,\ c(x)\ne c(y)\}|.}
\]

Every fixed joint diagonal bit-pattern \(c\) is one orbit of the unit group of \(A\) acting by simultaneous conjugation, and that orbit has precisely \(q^{d(c)}\) elements. Equivalently,

\[
C_k(P;q)=q^m\sum_{S\subseteq E(\Gamma(P))}(q^{-1}-1)^{|S|}Q^{\kappa(S)},
\]

where \(\kappa(S)\) denotes the number of connected components, including isolated vertices, in the spanning subgraph with edge set \(S\). Thus the ordered commuting-idempotent tuple count is a \(Q\)-state Potts/Tutte partition function on the comparability graph, and it is invariant under changes of the transitive orientation that keep that graph fixed. As a polynomial in \(q\), its degree is the maximum number of graph edges joining differently colored endpoints in a \(Q\)-coloring; its leading coefficient is the number of colorings attaining that maximum.

## Assumptions and scope

The incidence algebra consists of functions \(a(x,y)\in\mathbf F_q\) on comparable ordered pairs \(x\le y\), with convolution \((ab)(x,y)=\sum_{x\le z\le y}a(x,z)b(z,y)\). A unit is exactly an element with every diagonal entry nonzero. A \(k\)-tuple is counted as ordered; its coordinates need not be distinct. The comparability graph uses **all** strict order relations, not merely cover relations. The formulas hold in characteristic two without extra hypotheses. The polynomial identity is evaluated at prime powers \(q\), though its right-hand side defines a polynomial for an indeterminate.

## Proof

Fix \(n=|P|\) and enumerate \(P\) by any linear extension. Let \(r\) be the number of strict comparable pairs; hence \(r=m\). Diagonal extraction is a multiplicative map from \(A\) into \(\mathbf F_q^P\). Any idempotent therefore has each diagonal entry in \(\{0,1\}\). Consequently any commuting idempotent tuple has a well-defined joint diagonal coloring \(c:P\to\{0,1\}^{k}\).

To show simultaneous conjugation to its diagonal tuple, for each word \(\alpha\in\{0,1\}^{k}\) form the mutually orthogonal idempotents

\[
F_\alpha=\prod_{j=1}^{k}e_j^{\alpha_j}(1-e_j)^{1-\alpha_j}.
\]

Because the \(e_j\) commute, the \(F_\alpha\) are orthogonal, sum to \(1\), and have diagonal \(1\) precisely on the vertices colored \(\alpha\). Let \(D_\alpha\) be the corresponding diagonal projector and set

\[
u=\sum_{\alpha\in\{0,1\}^{k}}F_\alpha D_\alpha.
\]

Every diagonal entry of \(u\) is one, so \(u\) is a unit in the incidence algebra. Orthogonality gives \(F_\alpha u=F_\alpha D_\alpha=uD_\alpha\). With \(D_j=\sum_{\alpha:\alpha_j=1}D_\alpha\), summing this identity shows \(e_ju=uD_j\), or \(e_j=uD_ju^{-1}\), simultaneously for all \(j\). Thus **every** tuple with joint diagonal \(c\) lies in the conjugation orbit of the canonical diagonal tuple \((D_1,\ldots,D_k)\). Conjugation preserves diagonal entries, so different colorings cannot lie in the same orbit.

The group \(A^\times\) has \((q-1)^nq^r\) elements: the \(n\) diagonal entries are arbitrary nonzero field elements and the \(r\) strict comparable entries are arbitrary. An invertible \(v\) centralizes every \(D_j\) exactly when, for every \(x<y\),

\[
(c_j(y)-c_j(x))v(x,y)=0\qquad(1\le j\le k).
\]

Hence \(v(x,y)=0\) if \(c(x)\ne c(y)\), while the other \(r-d(c)\) off-diagonal entries are unrestricted. The stabilizer consequently has \((q-1)^nq^{r-d(c)}\) elements. Orbit-stabilizer gives exactly \(q^{d(c)}\) tuples with diagonal pattern \(c\). Summing disjoint orbits proves the first boxed identity.

For the second identity write, on each comparability edge \(xy\),

\[
q^{\mathbf 1_{c(x)\ne c(y)}}=q\bigl(1+(q^{-1}-1)\mathbf 1_{c(x)=c(y)}\bigr).
\]

Expand the product over edges. For each chosen edge subset \(S\), compatible colorings are precisely those constant on each connected component of its spanning subgraph, and there are \(Q^{\kappa(S)}\) such colorings. This yields the stated Potts expansion. The graph invariance follows because no orientation occurs on the right. Finally the direct color-sum polynomial has nonnegative integer coefficients; its highest exponent and coefficient are respectively the largest \(d(c)\) and the number of colorings achieving it. This completes the proof.

## Verification

The standalone `verify.py` constructs incidence algebras over the prime fields \(\mathbf F_2\) and \(\mathbf F_3\) by enumerating every permissible entry and multiplying using convolution. It directly tests idempotency and pairwise commutation, and separately evaluates the proposed graph-coloring sum. Examples include chains of two through four elements, a three-vertex fork, a four-vertex diamond, a complete height-two bipartite poset, and a four-vertex star. It checks tuple lengths one, two, and (on the smaller examples) three. All tested totals agree. In particular, for the three-element chain over \(\mathbf F_2\), the ordered-pair count is \(340\), and for the four-element diamond it is \(4132\). Run with `python3 verify.py` using the standard Python library.

The proof, not the finite experiments, establishes all finite posets, all prime powers, and arbitrary fixed tuple lengths. The one-tuple specialization is included only as a consistency check; it is not offered as a new enumeration theorem.

## Relationship to prior work

Can, Casimiro and Malheiro (2022), Theorem 3.2, identify the connected components and single-idempotent conjugacy orbits of incidence monoids over the complex numbers. Gargate and Gargate (2020), Theorems 1.1–1.2 and their incidence-poset examples, count **individual** potent matrices over finite fields and describe free off-diagonal entries when diagonal values differ. These results provide the structural motivation and recover the \(k=1\) boundary, but neither checked statement gives the simultaneous conjugacy classification and \(k\ge2\) commuting-family enumerator here. Cheraghpour and coauthors (2024) count edges and other parameters of the commuting graph of the whole two-by-two triangular ring rather than joint-idempotent tuples of arbitrary incidence algebras. The graph-polynomial transformation is proved directly above and requires no unproved reduction to a more general statement.

## Limitations

This counts ordered, pairwise commuting idempotent tuples, not arbitrary commuting elements, commuting nilpotents, or conjugacy classes under all algebra automorphisms. The finite-field result is derived algebraically and does not claim an independent external audit. It is not a claim that related general ring-theoretic simultaneous-idempotent diagonalization is new. No exhaustive claim about all published or unindexed literature is made; an equivalent counting formula could be implicit in a different formulation of finite-ring or Potts-model enumeration. The graph formula may require exponential work for arbitrary input posets.

## References

1. M. B. Can, A. Casimiro, A. Malheiro, *Idempotent Varieties of Incidence Monoids and Bipartite Posets*, arXiv:2208.01073v1, first posted 2022-08-01, especially Theorem 3.2 and Section 7. https://arxiv.org/abs/2208.01073
2. I. Gargate, M. Gargate, *(k+1)-potent Matrices in Triangular Matrix Groups and Incidence Algebras of Finite Posets*, arXiv:2009.04243v1, first posted 2020-08-30, especially Theorems 1.1–1.5. https://arxiv.org/abs/2009.04243
3. H. Cheraghpour, M. N. Ghosseiri, M. Jafari, F. Seyfpour, *On Commuting Graphs of Triangular Rings*, arXiv:2402.12619v1, first posted 2024-02-20, especially Introduction and Section 2. https://arxiv.org/abs/2402.12619
