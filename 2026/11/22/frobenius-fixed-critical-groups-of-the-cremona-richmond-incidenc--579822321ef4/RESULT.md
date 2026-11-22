# Frobenius-fixed critical groups of the Cremona–Richmond incidence graph

## Finding
For any finite field \(k=\mathbb F_q\) of characteristic \(p\ge7\) and any six-dimensional finite étale \(k\)-algebra \(E\), form the trace Igusa quartic on \(\mathbb P(\ker\operatorname{Tr}_{E/k})\) with equation
\[
\operatorname{Tr}_{E/k}(z^2)^2-4\operatorname{Tr}_{E/k}(z^4)=0.
\]
Its reduced singular curve has fifteen geometric lines and fifteen triple points. Let \(\Gamma\) be the bipartite incidence graph whose vertices are these thirty geometric objects, joined by the forty-five incidences. Define its integral critical group by \(K(\Gamma)=\operatorname{Div}^0(\Gamma)/\operatorname{Prin}(\Gamma)\). The geometric \(S_6\)-action arising from permutations of the six embeddings of \(E\) induces an action on \(K(\Gamma)\). If Frobenius has six-label cycle type \(\lambda\), then the fixed group \(K(\Gamma)^\sigma\) is determined completely by the following table, where the last column counts individually fixed geometric point and line vertices (not graph divisor classes).

| Frobenius cycle type | Invariant factors of the fixed critical group | Number of fixed critical classes | Fixed geometric vertices |
|---|---|---:|---:|
| \(6\) | \(\mathbb Z/3\mathbb Z\oplus \mathbb Z/15\mathbb Z\) | 45 | 1 |
| \(5,1\) | \(\mathbb Z/5\mathbb Z\oplus \mathbb Z/45\mathbb Z\) | 225 | 0 |
| \(4,2\) | \(\mathbb Z/5\mathbb Z\oplus \mathbb Z/45\mathbb Z\) | 225 | 2 |
| \(4,1,1\) | \((\mathbb Z/3\mathbb Z)^{2}\oplus \mathbb Z/45\mathbb Z\) | 405 | 2 |
| \(3,3\) | \((\mathbb Z/3\mathbb Z)^{2}\oplus (\mathbb Z/15\mathbb Z)^{2}\) | 2,025 | 3 |
| \(3,2,1\) | \(\mathbb Z/3\mathbb Z\oplus \mathbb Z/15\mathbb Z\) | 45 | 1 |
| \(3,1,1,1\) | \((\mathbb Z/3\mathbb Z)^{2}\oplus (\mathbb Z/15\mathbb Z)^{2}\) | 2,025 | 3 |
| \(2,2,2\) | \((\mathbb Z/15\mathbb Z)^{4}\oplus \mathbb Z/45\mathbb Z\) | 2,278,125 | 10 |
| \(2,2,1,1\) | \(\mathbb Z/3\mathbb Z\oplus (\mathbb Z/15\mathbb Z)^{3}\oplus \mathbb Z/45\mathbb Z\) | 455,625 | 6 |
| \(2,1,1,1,1\) | \((\mathbb Z/15\mathbb Z)^{4}\oplus \mathbb Z/45\mathbb Z\) | 2,278,125 | 10 |
| \(1,1,1,1,1,1\) | \(\mathbb Z/3\mathbb Z\oplus (\mathbb Z/15\mathbb Z)^{7}\oplus \mathbb Z/45\mathbb Z\) | 23,066,015,625 | 30 |

Without Frobenius restriction, the graph's integral critical group is
\[
K(\Gamma)\simeq\mathbb Z/3\mathbb Z\oplus(\mathbb Z/15\mathbb Z)^7\oplus\mathbb Z/45\mathbb Z,
\qquad \#K(\Gamma)=\tau(\Gamma)=3^{10}5^8.
\]
In the five-cycle class \(\lambda=(5,1)\), none of the thirty geometric vertices is Frobenius-fixed, but the fixed critical group is \(\mathbb Z/5\mathbb Z\oplus\mathbb Z/45\mathbb Z\), comprising \(225\) classes.

## Assumptions and scope
A *duad* is a two-element subset of \(\{0,1,2,3,4,5\}\), and a *syntheme* is a partition of the six labels into three duads. There are fifteen of each. Join a duad to a syntheme exactly when the former is a member of the latter. This defines \(\Gamma\) independently of the model of the quartic. The geometry identifies duads with the triple intersection points and synthemes with the fifteen singular lines. The six-label Frobenius action for the étale algebra has cycle type equal to the degrees of its field factors; all eleven cycle types occur via corresponding products of finite fields. The claim is for this **geometric incidence graph**, not the singular curve's generalized Jacobian or the Picard group of the ambient quartic.

## Proof
**The incidence graph and Laplacian.** Index the fifteen duads \(d\) and fifteen synthemes \(s\) in lexicographic order. Form \(B_{d,s}=1\) precisely if \(d\in s\), zero otherwise. Each row and column sum is three. For distinct duads, exactly one syntheme contains both when they are disjoint, and none if they intersect. Thus
\[
BB^\mathsf{T}=3I_{15}+A_{KG(6,2)},
\]
where \(A_{KG(6,2)}\) is the adjacency matrix for disjoint pairs, whose eigenvalues are \(6\) once, \(1\) nine times, and \(-3\) five times. Consequently the squared singular values of \(B\) are \(9^{(1)},4^{(9)},0^{(5)}\). The thirty-vertex graph has Laplacian
\[
L=\begin{pmatrix}3I_{15}&-B\\-B^\mathsf{T}&3I_{15}\end{pmatrix},
\]
whose eigenvalues are \(0^{(1)},1^{(9)},3^{(10)},5^{(9)},6^{(1)}\). The nullity-one calculation proves connectivity; the matrix-tree theorem gives \(\tau(\Gamma)=3^{10}5^8\).

**Integer presentation and group action.** Choose any vertex \(r\). Let \(Q\) be \(L\) with row and column \(r\) deleted. Relative to the basis \(e_v-e_r\), for \(v\neq r\), the group of degree-zero vertex divisors is \(\mathbb Z^{29}\) and the principal-divisor subgroup is \(Q\mathbb Z^{29}\). Thus \(K(\Gamma)=\mathbb Z^{29}/Q\mathbb Z^{29}\). The base Smith diagonal has twenty unit entries and the nonunit entries \(3,15,15,15,15,15,15,15,45\), giving the announced group.

Let \(\sigma\in S_6\), and let \(\pi\) denote its induced permutation of the thirty graph vertices. In the degree-zero divisor basis its integer action \(R\) has entries
\[
R_{u,v}=[u=\pi(v)]-[u=\pi(r)],\qquad u,v\ne r,
\]
with brackets denoting \(0\) or \(1\). This is an integral automorphism preserving the principal-divisor subgroup because the full graph Laplacian is equivariant. It therefore induces the desired \(\sigma\)-action on the finite group \(K(\Gamma)\). The coinvariants have the finite presentation
\[
K(\Gamma)_\sigma=\mathbb Z^{29}/\bigl(Q\mathbb Z^{29}+(R-I)\mathbb Z^{29}\bigr),
\]
so their invariant factors are the nonunit Smith factors of the \(29\times58\) integer matrix \(\left[Q\mid R-I\right]\).

**From coinvariants to fixed groups.** The graph's standard monodromy pairing is an equivariant nondegenerate symmetric pairing \(K(\Gamma)\times K(\Gamma)\to\mathbb Q/\mathbb Z\). Hence the Pontryagin dual of \(K(\Gamma)_\sigma\) is canonically \(K(\Gamma)^\sigma\). Every finite abelian group is (noncanonically) abstractly isomorphic to its Pontryagin dual, so both have the same invariant factors. The Smith presentations in the table therefore determine the claimed **fixed** groups, not merely the coinvariants.

**Exhaustive exact class calculation.** There are eleven partitions of six, corresponding to the eleven \(S_6\) conjugacy classes. The bundled `verify.py` constructs \(B,L,Q,R\) by exhaustive pairings and permutations of six labels; for each class it performs exact integral Smith reduction of \(\left[Q\mid R-I\right]\) and independently first computes the full-rank column Hermite normal form and takes its Smith form. Both routes give exactly the table. It also repeats all eleven calculations with two different deleted vertices, verifies Laplacian equivariance and graph automorphisms for all \(720\) permutations, checks the base Smith form and the matrix-tree order. Since conjugate permutations act by conjugate integral graph automorphisms, one representative of each cycle type exhausts the possible fixed groups.

## Verification
Run `python3 verify.py` using Python 3 and SymPy. Every matrix is formed exactly over the integers; no floating-point thresholds or random sampling occur. The printed record includes the full eleven-row table, the base invariant factors and the spanning-tree count, and concludes with `IGUSA_CREMONA_RICHMOND_FIXED_CRITICAL_GROUP_VERIFIED_OK`. The script checks two independent choices of root and two exact integer normal-form routes. The infinite statement follows from the canonical geometric correspondence, group presentation, equivariant pairing, and exhaustive six-label classification; checking finitely many base fields is not used as a substitute for proof.

## Relationship to prior work
Prokhorov established the fifteen-line singular locus and its \(S_6\)-action in Lemma 3.16 of *Fields of invariants of finite linear groups*; the Cremona–Richmond incidence structure and its generalized-quadrangle description are classical. Prażmowska and Prażmowski study the combinatorial configuration and projective realizations, not its finite graph Jacobian. Two separately published analyses of Igusa twists already determine the reduced singular curve's eleven-case zeta functions and the connected Picard torus of that curve; they use the same duad–syntheme incidence configuration, but the torus character lattice \(H_1(\Gamma,\mathbb Z)\) and the full singular-curve zeta function do **not** determine the discriminant quotient \(K(\Gamma)\) or its Frobenius-fixed subgroups. The Kneser-graph critical-group paper concerns the fifteen-vertex disjointness graph, not the thirty-vertex incidence graph. Results on Vietoris–Rips or independence-complex homology of the Tutte–Coxeter graph concern other invariants. The novelty assessed here is the specific eleven-case integral finite-group classification, not its underlying geometry, Frobenius point counts, or the general monodromy-pairing theorem.

## Limitations
Only the fifteen-line singular-curve incidence graph and the specified six-coordinate Frobenius action in characteristic at least seven are covered. No identification with an algebraic variety's Picard, Brauer or Jacobian group is asserted. The complete table is an exact computation with explicit constructions and independent normal-form checks, not a human-readable sequence of unimodular certificates for all matrix reductions. Historical priority is provisional: an older unindexed calculation of Tutte–Coxeter critical groups with the full six-label action, or a general equivariant Smith theorem specializing to this case, may imply the table. No independent scientific audit has been performed.

## References
1. Yu. G. Prokhorov, *Fields of invariants of finite linear groups*, arXiv:0707.1738, first submitted 2007-07-12, Lemmas 3.16–3.17. https://arxiv.org/abs/0707.1738
2. M. Prażmowska and K. Prażmowski, *The Cremona–Richmond Configuration revisited and generalized*, arXiv:1404.7166, first submitted 2014-04-28. https://arxiv.org/abs/1404.7166
3. J. Ducey, I. Hill, and P. Sin, *The critical group of the Kneser graph on 2-subsets of an n-element set*, arXiv:1707.09115, first submitted 2017-07-28. https://arxiv.org/abs/1707.09115
4. *The singular-curve zeta functions of all sextic trace twists of the Igusa quartic*, public mathematical record, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-singular-curve-zeta-functions-of-all-sextic-trace-twists-of--8fe51bf4025e
5. *Finite-field twists and integral Picard tori of the fifteen-line Igusa boundary*, public mathematical record, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-finite-field-twists-and-integral-picard-tori-of-the-fifteen-line--71e0231fbb0b
