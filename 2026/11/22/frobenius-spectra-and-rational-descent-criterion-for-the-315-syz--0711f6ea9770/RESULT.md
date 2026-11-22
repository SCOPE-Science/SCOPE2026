# Frobenius spectra and rational-descent criterion for the \(315\) syzygetic tetrads of a Cayley octad

## Finding
Let \(q\) be odd and let \(C/\mathbb F_q\) be a smooth plane quartic equipped with a regular Cayley octad \(\Omega\) whose unordered eight-point set is defined over \(\mathbb F_q\). Let \(\mathcal T\) denote the finite étale scheme of unordered syzygetic tetrads of four distinct geometric bitangents; over an algebraic closure it consists of \(315\) points. Label the octad geometrically by \(\{1,\ldots,8\}\), and write \(\sigma\in S_8\) for its Frobenius permutation. Under the Cayley bijection, bitangents correspond to \(\binom{[8]}{2}\); the tetrads split into two \(S_8\)-stable families, namely \(210\) simple four-cycles and \(105\) perfect matchings of the complete graph on eight vertices.

**Complete arithmetic classification.** In the table, \(d^{c}\) denotes \(c\) cycles of length \(d\) under Frobenius. All \(22\) partitions of eight occur as group-theoretic possibilities; a fixed \(q\) is not asserted to realize all types.

| Octad Frobenius type | Four-cycle tetrads | Matching tetrads | All tetrads | Rational bitangents |
|:--|:--|:--|:--|--:|
| \(8\) | \(2^{1}\,4^{4}\,8^{24}\) | \(1^{1}\,2^{2}\,4^{5}\,8^{10}\) | \(1^{1}\,2^{3}\,4^{9}\,8^{34}\) | 0 |
| \(7,1\) | \(7^{30}\) | \(7^{15}\) | \(7^{45}\) | 0 |
| \(6,2\) | \(3^{6}\,6^{32}\) | \(1^{1}\,2^{1}\,3^{8}\,6^{13}\) | \(1^{1}\,2^{1}\,3^{14}\,6^{45}\) | 1 |
| \(6,1,1\) | \(3^{4}\,6^{33}\) | \(1^{1}\,2^{1}\,3^{2}\,6^{16}\) | \(1^{1}\,2^{1}\,3^{6}\,6^{49}\) | 1 |
| \(5,3\) | \(5^{3}\,15^{13}\) | \(15^{7}\) | \(5^{3}\,15^{20}\) | 0 |
| \(5,2,1\) | \(5^{12}\,10^{15}\) | \(5^{3}\,10^{9}\) | \(5^{15}\,10^{24}\) | 1 |
| \(5,1,1,1\) | \(5^{42}\) | \(5^{21}\) | \(5^{63}\) | 3 |
| \(4,4\) | \(1^{2}\,2^{8}\,4^{48}\) | \(1^{5}\,2^{10}\,4^{20}\) | \(1^{7}\,2^{18}\,4^{68}\) | 0 |
| \(4,3,1\) | \(1^{1}\,2^{1}\,3^{1}\,4^{3}\,6^{2}\,12^{15}\) | \(3^{1}\,6^{1}\,12^{8}\) | \(1^{1}\,2^{1}\,3^{2}\,4^{3}\,6^{3}\,12^{23}\) | 0 |
| \(4,2,2\) | \(1^{4}\,2^{7}\,4^{48}\) | \(1^{3}\,2^{3}\,4^{24}\) | \(1^{7}\,2^{10}\,4^{72}\) | 2 |
| \(4,2,1,1\) | \(1^{2}\,2^{8}\,4^{48}\) | \(1^{1}\,2^{4}\,4^{24}\) | \(1^{3}\,2^{12}\,4^{72}\) | 2 |
| \(4,1,1,1,1\) | \(1^{4}\,2^{7}\,4^{48}\) | \(1^{3}\,2^{3}\,4^{24}\) | \(1^{7}\,2^{10}\,4^{72}\) | 6 |
| \(3,3,2\) | \(3^{20}\,6^{25}\) | \(1^{3}\,3^{4}\,6^{15}\) | \(1^{3}\,3^{24}\,6^{40}\) | 1 |
| \(3,3,1,1\) | \(3^{70}\) | \(1^{3}\,3^{34}\) | \(1^{3}\,3^{104}\) | 1 |
| \(3,2,2,1\) | \(1^{3}\,2^{6}\,3^{5}\,6^{30}\) | \(3^{3}\,6^{16}\) | \(1^{3}\,2^{6}\,3^{8}\,6^{46}\) | 2 |
| \(3,2,1,1,1\) | \(1^{3}\,2^{6}\,3^{19}\,6^{23}\) | \(3^{5}\,6^{15}\) | \(1^{3}\,2^{6}\,3^{24}\,6^{38}\) | 4 |
| \(3,1,1,1,1,1\) | \(1^{15}\,3^{65}\) | \(3^{35}\) | \(1^{15}\,3^{100}\) | 10 |
| \(2,2,2,2\) | \(1^{18}\,2^{96}\) | \(1^{25}\,2^{40}\) | \(1^{43}\,2^{136}\) | 4 |
| \(2,2,2,1,1\) | \(1^{12}\,2^{99}\) | \(1^{7}\,2^{49}\) | \(1^{19}\,2^{148}\) | 4 |
| \(2,2,1,1,1,1\) | \(1^{18}\,2^{96}\) | \(1^{9}\,2^{48}\) | \(1^{27}\,2^{144}\) | 8 |
| \(2,1,1,1,1,1,1\) | \(1^{60}\,2^{75}\) | \(1^{15}\,2^{45}\) | \(1^{75}\,2^{120}\) | 16 |
| \(1,1,1,1,1,1,1,1\) | \(1^{210}\) | \(1^{105}\) | \(1^{315}\) | 28 |

In particular,
\[
\boxed{\mathcal T(\mathbb F_q)\ne\varnothing\quad\Longleftrightarrow\quad \sigma\text{ has no cycle of length }5\text{ or }7.}
\]
Moreover, the three octad types \(8\), \(4,4\), and \(4,3,1\) have respectively \(1\), \(7\), and \(1\) rational tetrads **and no rational bitangents**. The complete splitting degree of the tetrads equals \(\operatorname{ord}(\sigma)\), the splitting degree of the octad. If the final column of cycles of the \(315\)-point scheme is \(d^{c_d}\), then for every \(n\ge1\),
\[
\#\mathcal T(\mathbb F_{q^n})=\sum_{d\mid n}d c_d,\qquad
Z(\mathcal T/\mathbb F_q,T)=\prod_d(1-T^d)^{-c_d}.
\]

## Assumptions and scope
The characteristic is different from \(2\). A *regular Frobenius-stable Cayley octad* means eight distinct geometric points in \(\mathbb P^3\), the complete intersection of a net of quadrics defining the given smooth quartic, such that the set is preserved by the arithmetic Frobenius. It need not consist of rational points. The Cayley construction identifies the geometric bitangents equivariantly with pairs of octad points. The \(315\) tetrads are defined intrinsically by four bitangents whose combined degree-eight tangency divisor lies on a conic (equivalently, by a four-element odd theta-characteristic relation). We count *unordered tetrads*, not ordered quadruples, conics, or individual contact points. The classification is conditional on the given stable Cayley octad and does not assert that each of the \(22\) classes occurs over each finite field.

## Proof
**1. The complete geometric combinatorial model.** For a chosen even theta characteristic, the six-dimensional vector space \(J(C)[2]\) is identified with the even-cardinality subsets of \([8]\) modulo complement. The \(28\) odd characteristics are represented by the two-element subsets. Four odd theta characteristics form a syzygetic tetrad if and only if their sum is zero in this affine difference space. In terms of four distinct edges on eight labels, the symmetric difference of their endpoint sets must be either the empty set or all eight labels.

If the difference is empty, each vertex of the four-edge graph has even degree; in a simple graph with exactly four edges the only such nonempty graph is a four-cycle. This gives \(3\binom{8}{4}=210\) tetrads. If the symmetric difference is all eight labels, each vertex has odd degree; since the total degree is \(8\), each vertex has degree one, so the edges form a perfect matching. There are \(7\cdot5\cdot3=105\) such tetrads. The two types are disjoint and exhaust all \(315\) syzygetic tetrads. The classical theta/bitangent and Cayley correspondences, not the present computation, supply the geometric premise.

**2. Frobenius and the exhaustive table.** Since the Cayley octad is Frobenius-stable, its action on pairs and thus on tetrads is induced by \(\sigma\in S_8\). Conjugate permutations have isomorphic actions, so the \(22\) partitions of eight exhaust the possibilities. For each partition, choose consecutive disjoint cycles on the eight labels. Enumerate all \(\binom{28}{4}=20475\) unordered four-edge subsets and retain those whose eight-bit vertex-incidence parity mask is either \(0\) or \(255\); this selects precisely the \(315\) tetrads proved above. Then apply the representative permutation to the four edges of each tetrad and decompose the induced permutation into orbits. The table gives the exact resulting cycles separately for the two invariant types. The accompanying `VERIFY.py` reconstructs the types independently by four-vertex cycles and disjoint matchings, and checks every orbit count against fixed-point counts for all powers.

**3. An intrinsic rational-descent criterion.** If \(\sigma\) contains a cycle of length \(5\) or \(7\), any edge incident to that vertex cycle has orbit length divisible by that prime. Such edges cannot lie in a \(\sigma\)-invariant set of four edges. The remaining at most three vertices support fewer than four distinct edges, so no tetrad is fixed. Conversely suppose there is no cycle of length \(5\) or \(7\). If every odd-length cycle occurs with even multiplicity, pair corresponding vertices across equal odd cycles, and pair antipodal vertices within every even cycle; this is an invariant perfect matching. Otherwise, parity of eight implies that the only possible partitions with unmatched odd cycles are \( (4,3,1)\), \( (3,2,2,1)\), \( (3,2,1,1,1)\), and \( (3,1,1,1,1,1)\). They possess invariant four-cycles respectively on the four-cycle of labels; between two transposed pairs; between a transposed pair and two fixed labels; and on four fixed labels. Hence a rational tetrad exists exactly in the stated cases.

**4. Splitting degrees and zeta functions.** The least extension on which every geometric tetrad becomes rational has degree the least common multiple of the lengths of its Frobenius cycles. In every one of the \(22\) rows the displayed least common multiple equals that of the octad partition, or equivalently \(\operatorname{ord}(\sigma)\); this is checked as an exact integer identity in the verifier. Finally, every finite étale Frobenius orbit of length \(d\) contributes \(d\) rational points over an extension of degree divisible by \(d\), and factor \((1-T^d)^{-1}\) to the zeta function. This proves the two displayed formulas for all extensions.

## Verification
Run `python3 VERIFY.py` with Python \(3\) and only its standard library. The verifier constructs the two families in two logically different ways: by explicit geometric shapes, and by parity-zero (or all-one) fourfold theta-subset sums. It checks exact equality of all \(315\) tetrads, all \(22\) conjugacy partitions, and both independently computed fixed-point/orbit-length identities for the complete range of powers. It also checks the class-size-weighted Burnside totals \(8!\) for each of the \(210\)- and \(105\)-element transitive families, and the bitangent action, then checks the existence criterion, exceptional rational-bitangent-free cases and the equality of splitting degrees. The terminal success marker is `CAYLEY_OCTAD_TETRAD_FROBENIUS_VERIFIED_OK`.

These are finite *exhaustive* computations on explicit sets of size \(315\) and \(22\); no finite-field sampling is used as a substitute for the uniform theorem, which follows from the Frobenius-equivariant geometric correspondence.

## Relationship to prior work
The basic Cayley-octad/bitangent labelling and geometric syzygetic four-cycles are classical; Plaumann, Sturmfels and Vinzant (2010 preprint, 2011 journal paper, especially Proposition 3.3 and Remark 3.8) treat these directly. Dolgachev (2012) records both tetrad combinatorial types, including the \(105\) disjoint-edge matchings. Elsenhans and Jahnel (2017) study Galois-invariant Cayley octads and prescribed bitangent actions, with an explicit warning that finite-field realizability has additional restrictions; their construction is not an enumeration of tetrad splitting. Bergvall (2021 preprint, 2023 article) identifies syzygetic tetrads as isotropic planes and gives permutation characters and moduli-space point counts. An earlier exact integral incidence-lattice computation for the \(315\) tetrads is a different invariant; it does not determine this finite-field orbit table. The present claim is restricted to the complete **twenty-two-class Frobenius cycle table**, the exact rational-tetrad existence obstruction and bitangent-free examples, and the tetrad zeta/splitting data. The underlying geometric counts are not claimed as discoveries.

## Limitations
The statement needs a smooth quartic in odd characteristic and a Frobenius-stable regular Cayley octad. It does not assert the existence of a curve of each octad Frobenius type over any particular finite field, nor any classification in characteristic \(2\). It says nothing about rationality of individual conic contact points or about Frobenius actions that do not preserve a Cayley octad. The arithmetic table is derived from the classical complete geometric permutation model; existing character-theoretic frameworks could implicitly encode its fixed-point data even without tabulating them. A full historical priority review of older finite permutation tables is not complete.

## References
1. D. Plaumann, B. Sturmfels, C. Vinzant, *Quartic Curves and Their Bitangents*, arXiv:1008.4104, first posted 2010-08-24; *J. Symbolic Computation* 46 (2011), 712–733. https://arxiv.org/abs/1008.4104
2. I. Dolgachev, *Classical Algebraic Geometry: A Modern View*, Cambridge University Press (2012), chapter on plane quartics and Cayley bitangent types.
3. A.-S. Elsenhans, J. Jahnel, *On plane quartics with a Galois invariant Cayley octad*, arXiv:1710.07279, first posted 2017-10-19. https://arxiv.org/abs/1710.07279
4. O. Bergvall, *Arithmetic and topology of classical structures associated with plane quartics*, arXiv:2106.13072 (2021), *European Journal of Mathematics* 9, article 117 (2023). https://doi.org/10.1007/s40879-023-00711-3
