# Palette capacity and an adaptive phase in complete multipartite colouring concepts

## Finding

Let \(r\ge 2\), let \(a_1\ge\cdots\ge a_r\ge1\) be integers, and let \(G=K_{a_1,\ldots,a_r}\) be the complete \(r\)-partite graph with **nonempty labelled** parts. For \(q\ge r\), take **all** proper named-\(q\)-colourings \(f:V(G)\to[q]\), not necessarily surjective. The Boolean query domain is \(V(G)\times[q]\); the concept associated to \(f\) answers \(1\) at \((v,c)\) exactly when \(f(v)=c\).

Write \(n=\sum_i a_i\) and \(s=\min\{r,q-r\}\) when \(q>r\). Then the exact VC dimension is

\[
\boxed{\operatorname{VCdim}(G,q)=
\begin{cases}
r-1,&q=r,\\
\sum_{i=1}^{s}a_i+(r-s),&q\ge r+1.
\end{cases}}
\]

Thus each spare colour initially unlocks one more full graph part in a maximum-size shattered equality-query support, until the full vertex count becomes attainable at \(q\ge2r\). The formula holds with singleton parts and without any balance or asymptotic assumptions.

The sharp finite online boundary is the octahedral graph \(K_{2,2,2}\). Its exact dimensions for all feasible palettes are

| Named palette \(q\) | \(\operatorname{VCdim}\) | \(\operatorname{Ldim}\) |
|---|---:|---:|
| \(3\) | \(2\) | \(2\) |
| \(4\) | \(4\) | \(4\) |
| \(5\) | \(5\) | \(6\) |
| \(q\ge6\) | \(6\) | \(6\) |

In particular, exactly at five colours, the octahedral graph admits a complete depth-six adaptive membership-query tree although **no** fixed six-query support is shattered. The positive conclusion is not an all-order Littlestone formula for arbitrary multipartite graphs.

## Assumptions and scope

All graphs and palettes are finite. Adjacency holds between every pair of vertices in distinct parts and no pair within one part. A proper colouring requires disjoint sets of colour names across distinct parts. Query inputs are binary **vertex–named-colour equality predicates**; this is not a whole-colour multiclass query, a query about whether two vertices share a colour, or a task of reconstructing an unknown graph. The static VC dimension is the maximum size of a set of distinct equality queries realizing every binary labelling. The Littlestone dimension is the maximum depth of a complete binary decision tree whose internal nodes are equality queries and every leaf admits a realizing proper colouring. Empty query supports are allowed.

At \(q<r\) no proper colouring exists; no empty-class dimension convention is asserted. The finite online table does not extend an exact adaptive formula to larger multipartite graphs.

## Proof

**1. A query-support restriction.** Two distinct colour queries at the same vertex cannot both be true, so a shattered support contains at most one query per graph vertex. Let \(k_i\) count tested vertices in part \(i\). In any part containing at least two tests, choose two of them. If their tested colours differ, the labelling making both tests true forces at least two colours in that part. If their tested colours agree, the labelling making one true and one false also forces at least two colours. Perform these choices independently in every part with \(k_i\ge2\); a shattered support would realize the resulting combined labelling. Since different graph parts use disjoint palettes and every part is nonempty, if \(t\) parts have at least two queries, this requires at least \(r+t\) colours. Therefore \(t\le q-r\). When \(q>r\) and \(s=\min(r,q-r)\), it follows by sorting the part sizes that

\[
|S|=\sum_i k_i\le \sum_{i=1}^{s}a_i+(r-s).
\]

**2. Every bound with a spare colour is attained.** Suppose \(q\ge r+1\). In each of the \(s\) largest parts test **all** vertices against the same part-specific colour \(c_i\); in each remaining part test one arbitrary vertex against its part-specific colour \(c_i\). Choose all \(r\) target colours \(c_1,\ldots,c_r\) distinct. There are exactly \(\sum_{i\le s}a_i+r-s\) selected queries.

Fix an arbitrary binary labelling of these queries. For each part containing positive tests, reserve the colour \(c_i\) for all its positively tested vertices. For each part containing negative tests, create one *free colour slot* to be used by all its negatively tested vertices; this slot must avoid \(c_i\). A part with both signs needs two slots, and only the \(s\) fully queried parts can be mixed, so there are at most \(r+s\le q\) slots altogether. Let \(p\) be the number of reserved positive colours and \(f\) the number of free slots. After reserving the \(p\) different colours, \(m=q-p\ge f\) colours remain. Each free slot forbids at most one of those remaining colours. Moreover, the forbidden colours of distinct free slots are pairwise distinct, since each part has at most one free slot and its target \(c_i\) is unique. For \(m\ge2\), Hall's theorem provides distinct admissible colours for the free slots: one slot has at least \(m-1\ge1\) neighbours, while any two or more slots collectively have all \(m\) colours as neighbours. If \(m=1\), then necessarily \(q=r+1\) and \(p=r\); every \(c_i\) has already been reserved, so the one remaining colour is forbidden by no free slot. All slots can therefore be assigned pairwise distinct colours. Give any untested vertices a colour already assigned to their own part. The resulting graph colouring is proper and realizes every requested bit. This proves the lower bound for every \(q>r\), including the full \(n\)-vertex result when \(q\ge2r\).

**3. At the chromatic palette.** When \(q=r\), each nonempty part is necessarily monochromatic, and its colour must be different from all other part colours. Hence the concepts correspond exactly to permutations of the \(r\) colour names among the parts. A shattered support can contain at most one test per part. If it tested all \(r\) parts, then its all-positive labelling forces the tested colour names to be distinct; changing exactly one answer to zero would be impossible because the other \(r-1\) positives force the last part to use the sole remaining name, its tested name. Thus \(\operatorname{VCdim}\le r-1\). Conversely choose one test in each of \(r-1\) parts, with distinct target names. After fixing all positive tests, match the remaining part slots to the remaining colour names while avoiding the distinct forbidden name in each negative tested part. The one completely untested part is unrestricted. Hall's theorem gives such a permutation: if at least two colours remain, each constrained slot forbids only its own distinct name, while the unrestricted slot accepts all; if only one colour remains, that slot is the untested part. Every labelling is realized, proving \(r-1\).

**4. Exact online table for the octahedron.** For any family of single-valued functions on \(n\) vertices tested by vertex–colour equalities, \(\operatorname{Ldim}\le n\). Indeed, along the all-positive branch of a complete decision tree, every tested vertex must be distinct: repeating a vertex with the same colour makes the later negative child impossible, while repeating it with a different colour makes the later positive child impossible. Hence a complete tree has depth at most \(n\). The static formula above gives the four VC entries in the table.

For \(q=3\), the only proper colourings of \(K_{2,2,2}\) are the six part-colour permutations. A complete depth-three tree would have eight leaves and therefore at least eight distinct concepts, so the online rank is exactly two.

For \(q=4\), there are exactly 96 proper colourings. The exhaustive, memoized finite decision-tree recurrence in `verify.py` tests every possible query on every surviving concept subset. It returns **False** for the existence of a complete depth-five tree; the VC witness gives depth four, hence \(\operatorname{Ldim}=4\). This is a finite, exhaustive proof of this case, not an inference from samples.

For \(q=5\), `tree_certificate.json` contains a complete depth-six decision tree, with 63 internal query nodes and 64 terminal colourings. Each leaf is a six-entry named-colour assignment, and `verify.py` independently checks that it is proper and satisfies every equality/inequality required along its root-to-leaf path. The verification explicitly checks both children of every internal node and all 64 leaves. Consequently the online rank is at least six; the general \(n=6\) bound gives equality. For \(q\ge6\), the static bound already equals the total vertex count six, so both dimensions are six.

## Verification

The standalone `make_certificate.py` deterministically rebuilds the entire adaptive tree from all 780 proper five-colourings of \(K_{2,2,2}\); its published output is `tree_certificate.json`. Independently, `verify.py` checks the stored tree without invoking the builder. The same verifier enumerates proper colourings and all trace patterns of the constructive support from Step 2 for ten small multipartite parameter choices. It checks the exact count of 96 four-colour concepts, evaluates the full rank-five decision-tree recursion without any sample or search cutoff, and validates every node and leaf of the rank-six witness. The recorded stdout is `checker_output.txt`. Run with `python3 make_certificate.py` followed by `python3 verify.py`, or run only `python3 verify.py` to validate the shipped certificate. No nonstandard Python packages are needed.

The arbitrary-parameter VC formula is proved by Steps 1–3, not by these finite enumerations. The rank-four exclusion is an exhaustive finite computation; it is not claimed as a symbolic infinite-family theorem.

## Relationship to prior work

The published study *Exact shattering polynomial and palette transition for complete-bipartite proper colourings* establishes both dimensions and all three-colour shattered supports when there are exactly **two** graph parts. The present all-parameter VC statement agrees with its ranks at \(r=2\), but is not implied by the two-part theorem at \(r\ge3\). More importantly, the explicit online gap on \(K_{2,2,2}\) contrasts with that paper's equality of both dimensions on all complete bipartite graphs. The present theorem neither reclaims its two-part theorem nor assumes its conclusions.

Blanca, Chen, Štefankovič and Vigoda (2017) work with proper graph colourings, but their structure-learning target is the unknown graph from random whole-colouring samples. Their theorems do not establish equality-query shattering ranks of a fixed graph's colourings. Fujita, Kitaev, Sato and Tong (2021) determine properly **ordered** colouring parameters for complete multipartite graphs; their weighted-order constraints and chromatic-number optimization differ from binary membership-query shattering. Guingona, Kolesnikov, Nierwinski and Soucy (2021) prove matching VC and Littlestone dimensions for zero sets of linear combinations of independent functions; they do not identify the present constrained-colouring concepts as such zero-set families, and the computed gap here rules out an immediate equality deduction. These distinctions were checked at the level of objects, quantifiers and implications rather than titles alone.

## Limitations

No exact online formula is claimed for general \(K_{a_1,\ldots,a_r}\) beyond the explicit octahedral case, and no complete count of shattered supports is asserted. The finite rank-four exclusion relies on exhaustive recurrence over every proper colouring and binary query; independent implementation or formal verification would further strengthen confidence. The source search and full-text comparisons are not proofs of absolute historical novelty; equivalent work under different terminology may exist. No independent mathematical audit has been performed.

## References

1. V. Guingona, A. Kolesnikov, J. Nierwinski and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805v1, first public 10 September 2021. https://arxiv.org/html/2109.04805v1
2. A. Blanca, Z. Chen, D. Štefankovič and E. Vigoda, *Structure Learning of H-colorings*, arXiv:1708.05118v1, first public 17 August 2017. https://arxiv.org/html/1708.05118v2
3. S. Fujita, S. Kitaev, S. Sato and L.-D. Tong, *On properly ordered coloring of vertices in a vertex-weighted graph*, arXiv:2102.08432v1, first public 16 February 2021. https://arxiv.org/html/2102.08432v1
4. *Exact shattering polynomial and palette transition for complete-bipartite proper colourings*, publicly posted 8 November 2026. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-shattering-polynomial-and-palette-transition-for-complete--69c08503d33f/RESULT.md
