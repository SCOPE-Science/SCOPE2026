# Sharp fixed-variable spectrum for crown graphs and balanced bicliques

## Finding
For every integer \(n\ge2\), write \(B_n=K_{n,n}\) for the complete balanced bipartite graph, and \(C_n=K_{n,n}-M_n\) for the crown graph obtained by deleting one perfect matching. All graphs are simple, with the edge relation as their only nonlogical symbol. Let \(\equiv_{\mathrm{FO}^k}\) denote agreement on all counting-free first-order sentences using at most \(k\) distinct reusable variable names, with no limit on quantifier depth. Within the infinite family \(\mathcal F=\{B_n,C_n:n\ge2\}\), the complete classification is:

* For \(k=1\) or \(k=2\), every two members of \(\mathcal F\) are equivalent.
* For every integer \(k\ge3\), equivalence occurs exactly when the two graphs are of the **same type** (both bicliques or both crowns) and their indices agree after truncation at \(k\):
\[
 B_n\equiv_{\mathrm{FO}^k}B_m\ \Longleftrightarrow\ \min(n,k)=\min(m,k),\qquad
 C_n\equiv_{\mathrm{FO}^k}C_m\ \Longleftrightarrow\ \min(n,k)=\min(m,k).
\]
No \(B_n\) is \(\mathrm{FO}^k\)-equivalent to any \(C_m\) when \(k\ge3\).

Consequently the family has exactly \(1\) theory at widths \(1\) and \(2\), and exactly \(2(k-1)\) theories at every width \(k\ge3\). The hierarchy is strictly increasing at every step from \(k\ge2\): \(C_k\) and \(C_{k+1}\) agree in width \(k\), but not in width \(k+1\). Relative to \(\mathcal F\), the least number of variable names defining any particular \(C_n\) (or \(B_n\)) up to isomorphism is \(n+1\).

In particular, deleting a *whole perfect matching* is invisible to all two-variable sentences but detectable with three variables, for every \(n\ge2\). For \(n\ge3\), the crown graphs giving the strict hierarchy are connected, regular, and have arbitrarily large degree; the result is not simply a disconnected-component counting phenomenon.

## Assumptions and scope
Give both graphs the same two-part presentation \(\{a_i:i\in[n]\}\sqcup\{b_i:i\in[n]\}\), with \(E(a_i,b_j)\) always true in \(B_n\), and true precisely when \(i\ne j\) in \(C_n\). All pairs within one side are nonadjacent, all loops are absent, and the two sides and indices are **not named** in the language. The case \(C_2\) is two disjoint edges; for \(n\ge3\), \(C_n\) is connected. No constants, unary side predicates, edge colors, orders, or counting quantifiers are present. The phrase *least defining width* is relative to the specified family \(\mathcal F\), not among all finite graphs.

## Proof
**The two-variable collapse.** Every vertex of every member of \(\mathcal F\) has an adjacent vertex and a distinct nonadjacent vertex. For \(B_n\) the latter can be chosen on the same side; for \(C_n\) it can likewise be chosen on the same side. In the ordinary two-pebble game, after lifting one pebble, only the other vertex remains fixed. The next move asks for either equality to that vertex, adjacency to it, or a distinct nonneighbor. All three requests can be met in every member of \(\mathcal F\). Duplicator therefore wins for arbitrarily many rounds between any two members, proving the claim for \(k=2\). The \(k=1\) claim also follows, since all structures are nonempty and loopless.

**The three-variable matching-defect witness.** Consider
\[
\Psi:=\exists x\,\exists y\,\bigl[x\ne y\land\neg E(x,y)\land
\neg\exists z\,(E(x,z)\land E(y,z))\bigr].
\]
In a complete biclique, each distinct nonadjacent pair lies on the same side and has a common neighbor, so \(B_n\not\models\Psi\). In a crown graph, the deleted matched pair \((a_i,b_i)\) is nonadjacent; no vertex in a bipartite graph can be adjacent to both endpoints of an opposite-side pair. Thus \(C_n\models\Psi\). The formula uses precisely three variable names. This proves all cross-family separations at width three and above.

**The sharp index threshold.** Let \(\Phi_j\), for \(j\ge3\), assert the existence of \(j\) pairwise distinct, pairwise nonadjacent vertices. It uses exactly \(j\) distinct variable names. The maximum independent set of \(B_n\) has size \(n\). The same is true of \(C_n\): a set using vertices from both sides can contain only the matched pair \(a_i,b_i\), hence has size at most two; alternatively a whole side supplies \(n\) vertices. Therefore both graph types satisfy \(\Phi_j\) exactly when \(n\ge j\). If \(k\ge3\) and \(\min(n,k)\ne\min(m,k)\), a value \(j\in\{3,\ldots,k\}\) separates them, except when one index is two and the other is at least three, in which case \(j=3\) separates them as well. Thus equality of capped indices is necessary.

**Permanent \(k\)-pebble strategies.** If the capped indices agree and are less than \(k\), the indices are equal, and the graphs of a given type are isomorphic. Otherwise both indices are at least \(k\). For bicliques, Duplicator preserves the side of each pebbled vertex (with a once-chosen global swap of the sides) and an injective correspondence of currently occupied vertices separately inside each side. After one pebble is lifted, at most \(k-1\) vertices are occupied; a fresh response exists on either graph with side size at least \(k\). Equality and adjacency therefore remain preserved forever.

For crowns, Duplicator instead preserves one global choice of side orientation and a partial injection from **occupied indices** to occupied indices: every pebbled \(a_i\) and every pebbled \(b_i\) are sent to vertices on their corresponding sides with a common target index. When a pebble is lifted, discard any source index no longer represented. A new vertex of an existing index must be sent to that corresponding index; a genuinely new index must be sent to an unused index. With at most \(k-1\) other pebbles, at most \(k-1\) indices are represented, so a fresh index exists on either graph. This is a partial isomorphism since crown adjacency is exactly opposite sides with unequal indices; equality is also preserved. The strategy works in both directions and at arbitrary round length. Sufficiency follows from the finite-variable pebble-game characterization.

For \(k\ge3\), there are exactly \(k-1\) possible capped index values, namely \(2,3,\ldots,k\), separately for bicliques and crowns. Thus the theory count is \(2(k-1)\). At width \(k\ge2\), \(C_k\equiv_{\mathrm{FO}^k}C_{k+1}\), but \(\Phi_{k+1}\) distinguishes them at width \(k+1\) (for \(k=2\), use \(\Phi_3\)). For a fixed graph of index \(n\), all smaller indices are separated at width \(n+1\), and all larger indices by \(\neg\Phi_{n+1}\). The formula \(\Psi\) distinguishes graph type. Hence the smallest defining width relative to \(\mathcal F\) is exactly \(n+1\). For \(n=2\), \(\neg\Phi_3\land\Psi\) defines \(C_2\) relative to \(\mathcal F\); for \(n\ge3\), \(\Phi_n\land\neg\Phi_{n+1}\land\Psi\) does so.

## Verification
Two separate finite programs were executed from the present package. `refinement_check.py` computes canonical atomic colors on complete tuples and repeatedly refines each color by the **set**, rather than the multiset, of colors reachable by replacing a single coordinate; this is the appropriate noncounting fixed-variable refinement. It compared \(217\) graph/width configurations across widths \(1\) through \(5\), with all comparisons matching the theorem. `extension_check.py` independently enumerated \(15{,}286\) canonical index-preserving one-point extension cases (widths up to five) and brute-forced maximum independent sets and the \(\Psi\) witness in ten graph models (five indices and two graph types). The recorded outputs are included. These finite runs do not prove the unbounded statement; its proof is the permanent strategy above.

Reproduce with a Python 3 installation and no third-party packages:

```text
python refinement_check.py
python extension_check.py
```

Both programs must exit successfully, with every comparison marked `PASS` and no assertions raised.

## Relationship to prior work
Grohe and Otto, *Pebble Games and Linear Equations* (first arXiv release April 9, 2012; CSL 2012), provide the general noncounting pebble-game framework and a two-variable Boolean-isomorphism criterion. Their result explains the coarse two-variable collapse but does not calculate the present matched-index hierarchy or the exact \(2(k-1)\) class count.

A separate prior result, *Exact logical width of arbitrary complete multipartite graphs* (published-finding corpus record `2026/10/4/SCOPE-exact-logical-width-of-arbitrary-complete-multipartite-graphs--2d960f9c3f1d`), establishes a broader theorem covering the biclique half of this statement. **The biclique-only width fact is not claimed as new.** The crown graphs (or their complements, two cliques joined by a perfect matching) are not complete multipartite in the adjacency language; that theorem does not imply the crown classification or the cross-family comparison.

Glen, Kitaev and Pyatkin, *On the representation number of a crown graph* (2018), investigate the same crown graphs and prove a sharp word-representation parameter. Their theorem concerns alternating letters in representing words, not fixed-variable first-order equivalence, and has no implication giving the present logical spectrum. Other searchable crown results address domination, colorings, or graph complexes. No exact equivalent classification was identified among inspected accessible claims. This is a documented search outcome, not proof of global priority.

## Limitations
The classification is *relative* to the two explicitly defined infinite graph families, and uses only the ordinary simple adjacency relation. It does not assign a global defining width among all finite graphs, cover unbalanced bicliques or partial matching deletions, or apply to logics with counting or additional side predicates. Although the all-index proof is elementary and self-contained, an equivalent previously known result may occur under another name, as folklore, or as a corollary of a stronger uninspected decomposition theorem. Independent mathematical review has not been performed.

## References
1. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, arXiv:1204.1990, first posted 2012-04-09; *Computer Science Logic 2012*, LIPIcs 16, 289–304, DOI:10.4230/LIPIcs.CSL.2012.289.
2. M. Glen, S. Kitaev and A. Pyatkin, *On the representation number of a crown graph*, *Discrete Applied Mathematics* 244 (2018), 89–93, DOI:10.1016/j.dam.2018.03.013, accessible author manuscript: https://strathprints.strath.ac.uk/63469/1/Glen_etal_DAM_2018_On_the_representation_number_of_a_crown.pdf.
3. *Exact logical width of arbitrary complete multipartite graphs*, published published-finding corpus finding `2026/10/4/SCOPE-exact-logical-width-of-arbitrary-complete-multipartite-graphs--2d960f9c3f1d`, cited only for the already-covered biclique case.
