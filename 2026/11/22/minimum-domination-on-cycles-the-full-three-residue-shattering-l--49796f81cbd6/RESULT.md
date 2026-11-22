# Minimum domination on cycles: the full three-residue shattering law

## Finding
For every integer \(n\ge3\), let \(C_n\) be the simple cycle with vertex set \(\{0,1,\ldots,n-1\}\), in cyclic order. Let \(\mathcal G_n\) consist of **all minimum-cardinality dominating vertex sets** of \(C_n\), regarded as their Boolean membership vectors. A support \(S\subseteq V(C_n)\) is *shattered* if every subset of \(S\) occurs as \(D\cap S\) for some \(D\in\mathcal G_n\). Write \(\Phi_n(z)=\sum_{S\text{ shattered}}z^{|S|}\).

**Theorem (complete support classification and polynomial).** For every integer \(k\ge1\),
\[
\begin{aligned}
\Phi_{3k}(z)&=1+3kz,\\
\Phi_{3k+1}(z)&=1+(3k+1)z+\binom{3k+1}{2}z^2+(3k+1)\binom{k}{2}z^3,\\
\Phi_{3k+2}(z)&=1+(3k+2)z+k(3k+2)z^2.
\end{aligned}
\]
The coefficientwise conclusion follows from the following **necessary and sufficient support tests**. Empty supports and all singleton supports are shattered. For \(n\equiv0\pmod3\), no support of size two or more is shattered. For \(n\equiv2\pmod3\), the shattered pairs are exactly pairs whose two clockwise cyclic separation lengths have residues \(0\) and \(2\) modulo three; no triple is shattered. For \(n\equiv1\pmod3\), every pair is shattered, and a triple \(\{a,b,c\}\), listed clockwise, is shattered exactly when the three positive clockwise gaps \(b-a,c-b,n-c+a\), evaluated with a cyclic lift, have residues \(0,2,2\) in some order modulo three; no four-set is shattered.

Hence the exact VC dimensions are
\[
\operatorname{VCdim}(\mathcal G_{3k})=1,\qquad
\operatorname{VCdim}(\mathcal G_{3k+2})=2,\qquad
\operatorname{VCdim}(\mathcal G_{3k+1})=
\begin{cases}2,&k=1,\\3,&k\ge2.\end{cases}
\]
These are dimensions of the optimal-solution incidence system, **not** the set system of all dominating sets, inclusion-minimal dominating sets, or maximal independent sets.

## Assumptions and scope
All graphs are simple, finite and undirected. The cycle has \(n\ge3\) distinct vertices. Domination means every vertex is selected or adjacent to a selected vertex. The minimum domination number of the cycle is \(\gamma(C_n)=\lceil n/3\rceil\), since one vertex dominates at most three vertices and a covering pattern of that size exists. Each chosen vertex has Boolean label one. The empty support is shattered because \(\mathcal G_n\) is nonempty. The generating polynomial counts distinct **query supports**, not dominating sets or hypothesis traces with multiplicity.

For a cyclic interval of integer length \(g\ge1\) define its *minimum gap deficit* \(r(g)\) to be the member of \(\{0,1,2\}\) congruent to \(-g\pmod3\). In particular, \(r(g)=0,1,2\) for \(g\equiv0,2,1\pmod3\), respectively. In a dominating set, all clockwise gaps between consecutive selected vertices have lengths one, two or three.

## Proof
**1. The defect budget.** Write \(n=3k+j\) with \(j\in\{0,1,2\}\), and put \(m=\lceil n/3\rceil\). Every minimum dominating set \(D\) consists of exactly \(m\) selected vertices whose \(m\) successive positive cyclic gap lengths lie in \(\{1,2,3\}\), summing to \(n\). Conversely, any such cyclic configuration is minimum dominating. Thus the total *deficit* is
\[
\sum_{\text{selected gaps }h}(3-h)=3m-n
=\begin{cases}0,&j=0,\\2,&j=1,\\1,&j=2.\end{cases}
\]
If \(P\subseteq D\) is a nonempty selected query set, order its elements clockwise and let \(g_1,\ldots,g_s\) be their cyclic gaps. Each such arc is subdivided into one or more of the selected gaps of \(D\), so its total deficit is a nonnegative integer congruent to \(-g_i\pmod3\); in particular, it is at least \(r(g_i)\). The sum of these arc deficits is the full budget. An arc whose deficit is zero contains only selected-vertex gaps of length three. Its selected vertices therefore occur **exactly** every three steps from the first selected endpoint to the last.

**2. Subdivision lifting.** Let an edge \(uv\) of \(C_n\) be subdivided into a path of four edges (three new vertices). For any minimum dominating set \(D\) of the original cycle, the edge lies in a clockwise gap of length \(d\in\{1,2,3\}\) from a selected vertex \(x\) to the next selected vertex \(y\). If the edge is the \((t+1)\)-st edge of this gap, then \(0\le t\le d-1\le2\). After the subdivision, the three new vertices have distances \(t+1,t+2,t+3\) from \(x\), hence one lies exactly three steps after \(x\). Select that new vertex, keep every old vertex's membership unchanged, and leave the other new vertices unselected. The old gap of length \(d\) has become two gaps of lengths \(3\) and \(d\). All other gaps are unchanged and every gap remains at most three. The enlarged selected set has \(\gamma(C_n)+1=\gamma(C_{n+3})\) members, so it is minimum dominating. Thus **every old Boolean trace on old query vertices lifts**, for every choice of subdivided edge. Iterating permits any desired addition of multiples of three to individual gaps between query vertices without destroying shattering.

**3. Base supports and lower bounds.** On \(C_4\), both two-point support types, of clockwise gap lengths \((1,3)\) and \((2,2)\), are shattered: the six two-element subsets are all minimum dominating, so every binary pair labeling is realized (an opposite pair also has an opposite complementary pair). On \(C_5\), the pair \(\{0,2\}\) is shattered: its four patterns \(00,01,10,11\) are witnessed respectively by \(\{1,3\},\{2,4\},\{0,3\},\{0,2\}\). On \(C_7\), the triple \(\{0,2,4\}\), with gaps \((2,2,3)\), is shattered by the following eight minimum dominating sets, one per trace in the order of the three queries:

| Trace | Witness on \(C_7\) | Trace | Witness on \(C_7\) |
|:---:|:---|:---:|:---|
| `000` | \(\{1,3,5\}\) | `001` | \(\{1,4,5\}\) |
| `010` | \(\{1,2,5\}\) | `011` | \(\{2,4,6\}\) |
| `100` | \(\{0,3,5\}\) | `101` | \(\{0,1,4\}\) |
| `110` | \(\{0,2,5\}\) | `111` | \(\{0,2,4\}\) |

Rotations and reflections cover all cyclic orders of these base gaps. The lifting lemma proves that every pair on \(C_{3k+1}\) is shattered: any pair of clockwise gaps summing to \(3k+1\) reduces modulo three to either \((1,3)\), \((3,1)\), or \((2,2)\), followed by additions of multiples of three. Likewise, every pair on \(C_{3k+2}\) with residues \(\{0,2\}\) lifts from the pair on \(C_5\); every triple on \(C_{3k+1}\) with gap residues \(\{0,2,2\}\) lifts from the triple on \(C_7\). All singletons are shattered since rotation gives both selected and omitted realizations at each vertex.

**4. Necessity for pairs and triples.** For \(n=3k\), the defect budget is zero, so the only possible minimum dominating sets are the three translates of the every-third-vertex pattern. Three concepts cannot shatter a pair. For \(n=3k+2\), the budget is one. If two query vertices are simultaneously selected, their two arc deficits must total one. Since the residues of the two gaps sum to one modulo three, their minimum deficits must be \(\{0,1\}\), equivalently the gap residues \(\{0,2\}\). For a triple of simultaneously selected vertices, the minimum deficits must be a permutation of \((1,0,0)\): they total one modulo three and cannot exceed one. The two zero-deficit arcs are consecutive. Consider their three consecutive query endpoints \(a,b,c\). In a labeling demanding \(a,c\) positive and \(b\) negative, the complementary arc from \(c\) to \(a\) has minimum deficit one, using the entire budget. The arc from \(a\) to \(c\) passing through \(b\) consequently has zero deficit and is forced to select \(b\), a contradiction. Thus no triple is shattered in this residue class.

For \(n=3k+1\), the budget is two. If a triple is shattered it must admit the all-positive trace. Its gap minimum deficits sum to two modulo three and are at most two, so they are a permutation of either \((2,0,0)\) or \((1,1,0)\). The first has two consecutive zero-deficit arcs. In the trace with their common endpoint omitted and their outer endpoints positive, the complementary arc consumes both defects, and the zero-deficit arc through the omitted endpoint forces it to be selected. Hence the first pattern is impossible. The second pattern is exactly the stated gap-residue condition \(\{0,2,2\}\), whose sufficiency was proved by lifting.

**5. No shattered four-support in the remaining residue class.** Fix four clockwise query vertices and suppose their all-positive labeling is realizable on \(C_{3k+1}\). The four minimal arc deficits total two, so, up to cyclic order, either the pattern consists of one \(2\) and three zeroes, or two \(1\)'s and two zeroes. If some two zero entries are adjacent, the labeling requiring their outer endpoints positive and their shared endpoint negative is impossible by the same zero-deficit forcing argument: the complementary arc consumes the two available defects. The only remaining arrangement is alternating \((1,0,1,0)\). Name the consecutive vertices \(a,b,c,d\), with arc deficits \(1,0,1,0\) in that order. Demand that \(a,b\) are selected and \(c,d\) omitted. The arc from \(a\) to \(b\) consumes at least one defect; the opposite arc from \(b\) back to \(a\) has minimum deficit one, so it uses exactly one defect. Its selected-vertex gaps are therefore all length three except a single length-two gap. From \(b\), the positions of \(c\) and \(d\) along that arc are congruent to zero and two modulo three, respectively. Before the unique length-two step, selected positions have displacement zero modulo three from \(b\); afterward they have displacement two modulo three. Omitting \(c\) forces that step to occur before \(c\), which then forces \(d\) to be selected. This contradicts the required trace. Every four-set is therefore unshattered. By heredity, no larger support is shattered.

**6. Coefficient counts.** The degree-zero and degree-one coefficients are one and \(n\). For \(n=3k+1\), all \(\binom n2\) pairs are shattered. Every shattered triple has clockwise gaps, in some order, \(2+3a,2+3b,3+3c\), with \(a,b,c\ge0\) and \(a+b+c=k-2\). Choosing its starting vertex and the location of the gap congruent to zero modulo three gives \(3n\binom{k}{2}\) rooted descriptions; each unoriented triple has exactly three rooted descriptions. Thus there are \(n\binom{k}{2}\) shattered triples. For \(n=3k+2\), the two gaps of a shattered pair are \(2+3a,3+3b\), with \(a+b=k-1\). The uniquely distinguished direction from the residue-two gap contributes one of \(n\) starting vertices and \(k\) compositions, giving \(nk\) pairs. These counts and the previously established degree bounds give the polynomial and VC dimensions.

## Verification
The self-contained `verify_cycle_gamma.py` script uses an **independent domination test**, enumerating all vertex subsets of size \(\lceil n/3\rceil\) for every cycle length \(3\le n\le22\). It compares the exact traces of all supports of cardinality at most four against the theorem's residue tests and compares all coefficients against the closed forms. This checks **44,544** supports, including all potentially shattered supports in those orders. Separately, the script checks **1,420** edge-subdivision lifts from independently enumerated minimum solutions for cycle orders \(3\) through \(15\). A successful run prints `CYCLE_GAMMA_SHATTERING_VERIFIED orders=3..22 supports=44544 edge_lifts=1420`. The unrestricted theorem is established by the defect and lifting proofs, not by finite sampling.

## Relationship to prior work
Hernández-Gómez, Reyna-Hérnandez, Romero-Valencia, and Rosario Cayetano (2020) completely describe minimum dominating sets of paths and cycles, including the three cyclic residue cases and their dihedral orbits [1, Section 2.1.2]. That classification, the domination number, and solution cardinalities are **prior results**, not new findings here. The added assertions concern **which coordinate supports realize all Boolean traces** and their complete face polynomial; the arguments require the defect-exhaustion obstruction and uniform subdivision-lifting property. Brewster, Mynhardt, and Teshima (2023) determine the minimum *independent* dominating set reconfiguration graphs of paths and cycles, including gap representations and counts [2, Section 3]. Although their independent class agrees with the minimum dominating class in some cycle residue classes, the cycle-wide Boolean trace law and degree-three residue class are not given there. Published work on inclusion-**minimal** dominating sets of small cycles studies a genuinely larger hypothesis class and a different adaptive question [3].

## Limitations
No formula for Littlestone dimension, trace multiplicities, or the homology of this shattering complex is asserted. The theorem is restricted to simple cycles and minimum-cardinality domination. Previously published descriptions of these minimum solutions make the new classification a refinement, not a new characterization of optimal dominating sets. Equivalent Boolean-trace results might exist under a different name; the mathematical priority assessment is qualified. The finite checker is corroborative only, and independent mathematical audit has not been performed.

## References
1. J. C. Hernández-Gómez, G. Reyna-Hérnandez, J. Romero-Valencia, and O. Rosario Cayetano, *Transitivity on Minimum Dominating Sets of Paths and Cycles*, *Symmetry* 12(12) (2020), article 2053, published 11 December 2020. https://doi.org/10.3390/sym12122053
2. R. C. Brewster, C. M. Mynhardt, and L. E. Teshima, *The i-Graphs of Paths and Cycles*, arXiv:2303.08190v1 (14 March 2023), https://arxiv.org/html/2303.08190v1
3. *The first minimal-domination cycle gap: complete five-query traces and a vertex-transitive amplification*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-first-minimal-domination-cycle-gap-complete-five-query-trace--84ef6ec729bc
