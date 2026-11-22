# Six line-intersection profiles of longest total-dominating sequences in \(\operatorname{PG}(2,4)\)

## Finding

Let \(G\) be the 42-vertex point–line incidence graph of the Desarguesian projective plane \(\operatorname{PG}(2,4)\). Its Grundy total domination number is exactly
\[
\gamma_{\mathrm{gr}}^t(G)=20,
\]
whereas its ordinary total domination number is \(\gamma_t(G)=10\).

On either bipartition shore there are exactly **140,448** ten-element supports of longest legal incidence-covering sequences, with exactly **36,288,000,000** ordered longest sequences. The supports have exactly the following six line-intersection profiles. Write \(h_j(S)\) for the number of projective lines containing exactly \(j\) selected points, so a profile is \((h_0,h_1,h_2,h_3,h_4,h_5)\).

| Profile | Supports |
| --- | ---: |
| \((0,3,11,4,2,1)\) | 30,240 |
| \((0,4,8,7,1,1)\) | 20,160 |
| \((0,4,9,4,4,0)\) | 20,160 |
| \((0,5,5,10,0,1)\) | 6,048 |
| \((0,5,6,7,3,0)\) | 60,480 |
| \((0,6,3,10,2,0)\) | 3,360 |
| **Total** | **140,448** |

Thus 56,448 maximum supports contain a whole projective line, while the other 84,000 are nontrivial blocking sets containing no whole line. The number of unordered vertex supports of longest total-dominating sequences in \(G\) is exactly
\[
140448^2=19\,725\,640\,704,
\]
and the number of ordered longest total-dominating sequences (different interleavings counted separately) is exactly
\[
\binom{20}{10}(36\,288\,000\,000)^2
=20!\cdot10^8
=243\,290\,200\,817\,664\,000\,000\,000\,000.
\]

## Assumptions and scope

The ground field is \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\), represented by \(0,1,t,t+1\) as the integers \(0,1,2,3\). Projective points are one-dimensional nonzero vector subspaces of \(\mathbb F_4^3\); projective lines are kernels of nonzero linear forms. Normalize each vector by multiplying by the inverse of its first nonzero coordinate and sort the resulting triples lexicographically. There are 21 points and 21 lines. Incidence is the vanishing of their coordinate dot product over \(\mathbb F_4\). The asserted census concerns this fixed, canonical plane, not all projective planes of unspecified order.

A point sequence \((p_1,\ldots,p_r)\) is *legal* when each point \(p_i\) lies on a line not incident to any of \(p_1,\ldots,p_{i-1}\). It is *complete* when its points hit every projective line. A *total-dominating sequence* in a graph is an ordered vertex sequence in which each selected vertex has an open neighbor not covered by earlier selected vertices, and at the end every graph vertex has a selected neighbor. Its maximum length is \(\gamma_{\mathrm{gr}}^t\). All counts refer to labelled plane points and lines, not equivalence classes under automorphisms.

## Proof

**1. Exact finite recurrence.** Index the 21 points by \(0,\ldots,20\). For each point \(i\), let \(B_i\) be the 21-bit mask of its incident lines. For every subset \(S\) of the 21 points let \(C(S)=\bigvee_{i\in S}B_i\). Define \(W(\varnothing)=1\) and
\[
W(S)=\sum_{i\in S}\mathbf1_{\{C(S\setminus\{i\})\ne C(S)\}}\,W(S\setminus\{i\}).
\]
Deleting the last point of a legal ordering gives exactly one summand. Conversely, appending \(i\) to any ordering counted in its summand preserves legality. Hence this recurrence counts **all and only** legal orderings of each support \(S\). It is finite and exhaustive: \(S\) ranges over all \(2^{21}=2\,097\,152\) subsets, with no sampling, search cutoff, or unexamined extension.

The two standalone programs independently construct the incidence plane and evaluate this recurrence, one by forward additions and one by last-point deletions. Both give 738,840 subsets with positive \(W(S)\); the largest such subset has cardinality ten. Among the 140,448 positive supports of size ten, their order counts sum to 36,288,000,000. Every one hits all 21 lines. Their six profile multiplicities are exactly the table above. The checkers verify that each of the 21 lines has five points and each pair of distinct lines meets once. In each displayed profile, the identities \(\sum_jh_j=21\), \(\sum_jj h_j=50\), and \(\sum_j\binom j2h_j=45\) provide additional incidence consistency checks, not substitutes for enumeration.

**2. Direct ten-point witness.** In the normalized, lexicographically ordered point coordinates, the following points form a legal ten-point covering sequence:
\[
(1,3,3),(1,3,2),(1,3,1),(1,2,3),(1,2,2),
(1,2,1),(1,3,0),(1,1,3),(1,0,3),(0,1,3).
\]
The respective numbers of lines newly hit are \((5,4,4,2,1,1,1,1,1,1)\), summing to 21. The preceding exhaustive recurrence rules out eleven or more points. Thus the maximum one-shore sequence length is exactly ten.

**3. Passage to total domination.** In the incidence graph, a chosen point can newly dominate only line-vertices, and a chosen line can newly dominate only point-vertices. Therefore legality and completion separate into independent subsequences on the two shores; their orders may be interleaved arbitrarily without affecting legality. The dot-product model identifies the point–line dual incidence structures, so both shores have the same ten-step maximum, support count and ordered count. This yields \(\gamma_{\mathrm{gr}}^t(G)=10+10=20\), the square for unordered supports and the \(\binom{20}{10}\) shuffle factor for ordered total-dominating histories. The ordinary total domination number is ten: on each shore at least five vertices are required to meet all 21 opposite-side vertices, since four vertices cover at most 20, while one complete five-point projective line meets every line; the dual construction supplies the other five vertices.

## Verification

Both programs are complete and require no data downloads. Run `python3 verify.py`; separately run `g++ -O3 -std=c++17 verify.cpp -o verifier && ./verifier`. The Python implementation constructs \(\mathbb F_4\) from its multiplication table and uses the deletion recurrence. The C++17 implementation computes polynomial reductions and propagates forward additions. Each program checks the projective-plane incidence axioms and asserts the maximum, exact support count, ordered count, reachable-set count, and all six profile populations. The Python program also asserts the derived two-shore counts.

The checkers process \(2^{21}\) masks and provide an exhaustive finite proof of this specific 42-vertex instance. They do not prove any formula for other orders. The direct ten-point witness can be checked independently against the incidence definition.

## Relationship to prior work

Brešar, Gologranc, Milanič, Rall and Rizzi introduced the Grundy covering number and its general legal-covering framework. Brešar, Henning and Rall developed Grundy total domination and proved the general incidence-graph conversion \(\gamma_{\mathrm{gr}}^t(I(\mathcal H))=2\rho_{\mathrm{gr}}(\mathcal H)\) (their Theorem 8.4). That conversion is acknowledged, not claimed as new. It does not supply the numerical Grundy covering number, ordered census, or six line profiles of the 21-point plane. Gologranc, Jakovac, Kos and Marc subsequently constructed a different, incidence-*complement* bipartite graph from projective planes in an equality classification; its length-six assertion is not the length of the ordinary plane-incidence graph.

The candidate new content is the exact order-four projective-plane census and its consequences for the 42-vertex Levi graph. The closest indexed mathematical results located concerned other incidence-graph parameters and other underlying graph families, not this sequence enumerator. Search non-detection is not proof of publication priority.

## Limitations

This is a finite exhaustive result for \(\operatorname{PG}(2,4)\) only; no extrapolation of a formula to larger field orders or non-Desarguesian planes is asserted. The six profiles are incidence signatures, **not** claimed to be six automorphism orbits. The numerical proof is computational but exhaustive and reproducible; independent scholarly audit has not occurred. Unindexed earlier computations or unavailable literature could affect publication priority.

## References

1. B. Brešar, T. Gologranc, M. Milanič, D. F. Rall, R. Rizzi, *Dominating sequences in graphs*, Discrete Mathematics **336** (2014), 22–36, https://doi.org/10.1016/j.disc.2014.07.016 (hypergraph legal-covering formalism).
2. B. Brešar, M. A. Henning, D. F. Rall, *Total dominating sequences in graphs*, Discrete Mathematics **339** (2016), 1665–1676, first arXiv posting 2016-01-27, https://arxiv.org/abs/1601.07525 (definition, Theorem 8.4).
3. T. Gologranc, M. Jakovac, T. Kos, T. Marc, *On graphs with equal total domination and Grundy total domination number*, https://arxiv.org/abs/1906.12235 (different projective-plane-derived graph, Theorem 4.7).
