# Four edge types govern matching-difference shattering on six vertices

## Finding
Let \(K_6\) be the complete graph on six vertices, let \(\mathcal M\) be its fifteen perfect matchings, and regard each member of \(\mathcal D=\{M\triangle M':M,M'\in\mathcal M,\ M\ne M'\}\) as a Boolean concept on the fifteen edges. A query support \(S\subseteq E(K_6)\) is shattered by \(\mathcal D\) **if and only if** \(|S|\le4\) and \(S\) is contained in the edge set of some simple four-cycle or six-cycle of \(K_6\).

The full shattered-support polynomial is
\[
\Phi_{\mathcal D}(z)=1+15z+105z^2+375z^3+675z^4.
\]
Consequently \(\operatorname{VCdim}(\mathcal D)=4\). The shattered-support complex is pure of dimension three, with exactly 675 facets, of four edge-isomorphism types:

| Four-edge support type | Number of labelled facets |
|---|---:|
| Four-cycle \(C_4\) | 45 |
| Five-vertex path \(P_5\) | 360 |
| Disjoint union \(P_4\sqcup P_2\) | 180 |
| Disjoint union \(P_3\sqcup P_3\) | 90 |

With coefficients in \(\mathbb F_2\), its only nonzero reduced Betti number is \(\widetilde\beta_3=391\); all other reduced Betti numbers vanish.

## Assumptions and scope
The vertex set is \(\{0,1,2,3,4,5\}\). The ground set of queries is the collection of fifteen unordered edges. The family of concepts contains **distinct** symmetric differences of two **distinct** perfect matchings, not the matchings themselves and not the full even-cycle space. A support \(S\) is shattered if all \(2^{|S|}\) subsets of \(S\) occur as \(D\cap S\) for some \(D\in\mathcal D\). Homology is reduced simplicial homology over \(\mathbb F_2\), not integral homotopy information.

## Proof

**Cycle decomposition.** The symmetric difference of two perfect matchings is a union of disjoint alternating even cycles. On six vertices, distinct matchings therefore yield a single simple four-cycle (with their common matched edge excluded from the difference) or a single simple six-cycle. Conversely, alternating edges on either such cycle can be completed to two perfect matchings. There are \(3\binom64=45\) four-cycles and \(5!/2=60\) six-cycles, hence exactly 105 distinct concepts.

**Positive-pattern necessity.** If \(S\) is shattered, the all-one trace on \(S\) is realized, so \(S\subseteq D\) for some four-cycle or six-cycle \(D\). In particular \(|S|\le6\).

**Five-edge obstruction.** Every five-edge subset of a six-cycle is a six-vertex path. Write its ordered edges as \(e_1,e_2,e_3,e_4,e_5\). The Boolean pattern requiring \(e_1,e_2,e_3,e_4\) but excluding \(e_5\) cannot occur: four consecutive edges form a path on five vertices; no four-cycle contains that path, while the only six-cycle containing it uses the sixth vertex to join its endpoints and necessarily contains \(e_5\). Therefore no five-edge support is shattered. By downward closure of shattering, none of larger size is shattered.

**Four-edge sufficiency.** Every four-edge subset of a four-cycle or six-cycle belongs to exactly one of four graph-isomorphism types: \(C_4\), \(P_5\), \(P_4\sqcup P_2\), \(P_3\sqcup P_3\). A certificate for one labelled representative of each type appears in `witnesses.json`. Each of the sixteen possible Boolean patterns on its four edges is accompanied by a concrete four-cycle or six-cycle from \(\mathcal D\) realizing that pattern. The certificate is checked by both standalone verification programs. Vertex permutations preserve \(\mathcal D\), so every four-edge subset of a concept is shattered. Every smaller subset of a concept extends to a four-edge subset of the same cycle, hence is shattered. Together with necessity this proves the iff characterization.

**Face and facet counts.** All fifteen one-edge supports and all \(\binom{15}{2}=105\) two-edge supports lie in some even cycle. Three-edge supports are precisely all three-edge sets except the \(6\binom53=60\) three-stars and the \(\binom63=20\) triangles, giving \(\binom{15}{3}-60-20=375\) shattered triples. The four edge types above have \(3\binom64=45\), \(\binom65\cdot5!/2=360\), \(\binom64\cdot4!/2=180\), and \(\binom63\cdot3^2/2=90\) labelled realizations, respectively. Their sum is 675. Every shattered support extends to a four-edge shattered set, and no five-edge support is shattered, proving purity and the complete polynomial.

**Mod-two homology.** Index the faces by their fifteen-bit edge masks. The numbers of faces in cardinalities \(0,1,2,3,4\) are \((1,15,105,375,675)\). Exact Gaussian elimination over \(\mathbb F_2\) on the reduced augmented boundary matrices yields ranks \((1,14,91,284)\) for the maps from cardinality-one through cardinality-four faces, respectively. The kernel-minus-image formula gives reduced homology ranks \((0,0,0,391)\) in dimensions \(0,1,2,3\). The two independently implemented rank calculations reproduce these values.

## Verification
Reproduce without network access. For a C++17 compiler, run `c++ -O2 -std=c++17 even_cycle_verify.cpp -o verify` followed by `./verify`. Independently, run `python3 even_cycle_verify.py` using Python 3.9 or later. Keep `witnesses.json` beside the Python script. Both programs enumerate perfect matchings from scratch, form their pairwise symmetric differences, compute all Boolean traces, and eliminate exact boundary matrices over \(\mathbb F_2\). The C++ program independently loops over all \(2^{15}=32768\) potential supports; Python grows only genuinely shattered supports and separately checks the explicit 64-pattern witness table and the four graph types.

## Relationship to prior work
Cambie, Girão and Kang (first public preprint 7 August 2018) developed VC-dimension bounds for repeated symmetric differences of general set systems. That theory motivates the operation \(\mathcal M\triangle\mathcal M\) but does not give these finite matching-difference traces, four facet types, or homology groups. The standard alternating-cycle description of differences of perfect matchings is used here as an elementary structural input, not claimed as new. Previously published Hamiltonian-cycle membership results treat only the six-cycle subfamily and do not directly determine the Boolean traces after adding all four-cycles.

## Limitations
The assertion is an exact result for the six-vertex complete graph and this specified concept family only. It is not an all-order formula, not an integral-homology or homotopy classification, and not an assertion of independently certified historical priority. The mod-two homology computation is exhaustive and reproducible, but a separate conceptual homotopy proof is not provided.

## References
1. S. Cambie, A. Girão, R. J. Kang, *VC dimension and a union theorem for set systems*, arXiv:1808.02352 (first posted 2018-08-07); *Electronic Journal of Combinatorics* 26(3), P3.24 (2019), https://arxiv.org/abs/1808.02352 and https://doi.org/10.37236/8288.
2. Published research record, *Hamiltonian-cycle edge shattering: exact VC dimension and a first adaptive gap* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-hamiltonian-cycle-edge-shattering-exact-vc-dimension-and-a-first--3eaf6a69af80 (indexed summary consulted; complete text not accessible).
