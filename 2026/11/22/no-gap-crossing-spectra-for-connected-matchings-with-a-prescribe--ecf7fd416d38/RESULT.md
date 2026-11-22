# No-gap crossing spectra for connected matchings with a prescribed opening set

## Finding

Let \(n\geq 1\) and fix the left endpoints of a perfect matching on \([2n]\). Encode those endpoints by an admissible word \(w\) of \(n\) opening symbols \(U\) and \(n\) closing symbols \(D\), with every prefix having at least as many openings as closings. Let \(h_j\) be the number of unmatched openings just before the \(j\)-th closing symbol, and put
\[
K(w)=\sum_{j=1}^{n}(h_j-1).
\]
For a matching \(M\), let \(\mathcal X(M)\) be the graph whose vertices are its chords, adjacent exactly when their endpoints alternate. Let \(c(M)=|E(\mathcal X(M))|\).

**Theorem.** There is a matching with opening word \(w\) and connected crossing graph if and only if \(w\) is *primitive*, meaning its opening-minus-closing prefix sum is positive at every proper nonempty prefix. For every primitive word, the set of crossing counts of such connected matchings is **exactly**
\[
\{n-1,n,\ldots,K(w)\}.
\]
The minimum has a construction whose crossing graph is a tree. The maximum has a construction whose crossing graph contains a Hamiltonian path. Moreover, a sequence of local, opening-set-preserving swaps visits every intermediate crossing count while maintaining connectedness.

## Assumptions and scope

The vertices are linearly labelled \(1,\ldots,2n\). Every edge of a perfect matching is written \((a,b)\) with \(a<b\); an *opening* is a smaller endpoint. A crossing is a pair \((a,b),(c,d)\) with \(a<c<b<d\) or \(c<a<d<b\). Containments \(a<c<d<b\) do **not** count as crossings. A graph with one vertex is connected. No equivalence is asserted for alternate definitions of chord intersection or for crossing-free reconfiguration graphs.

A word with \(n\) openings and \(n\) closings occurs as an opening word precisely when it is a Dyck word: the prefix condition is necessary, and the usual stack pairing supplies sufficiency. There are \(h_j\) choices of an active opener at the \(j\)-th closing.

## Proof

**Disconnected words.** Suppose \(n\ge2\) and \(w\) returns to height zero before its final symbol. Each opening preceding that return must be paired with a closing preceding it. All chords on either side of this cut have nonalternating endpoints, so the crossing graph is disconnected. A primitive word has no such obstruction; the constructions below establish sufficiency.

**Sharp upper bound and connected maximizer.** When a closing symbol is processed, the chosen active opener can cross only the still-active openers occurring after it. Consequently this closing creates at most \(h_j-1\) crossing pairs, counted at the earlier of the two closing times. Summing gives \(c(M)\le K(w)\). The first-in-first-out pairing, which pairs the \(i\)-th opener to the \(i\)-th closer, selects the oldest unmatched opener and realizes equality at every step. If \(w\) is primitive and \(o_i,c_i\) are the positions of its \(i\)-th opener and closer, then \(o_i<o_{i+1}<c_i<c_{i+1}\) for every \(i<n\). Its consecutive chords therefore cross, giving a Hamiltonian path in the crossing graph.

**Crossing-tree construction.** We induct on \(n\). The unique two-symbol primitive word has one chord and zero crossings. For \(n>1\), write \(w=U v D\) where \(v\) is nonempty and Dyck. Choose a consecutive \(UD\) inside \(v\), delete it, and call the resulting primitive word \(w'\). Let \(s\) denote the position of the deleted opening; after relabelling, the deleted closing will occupy \(s+1\). By induction, \(w'\) has a matching \(M'\) with tree crossing graph. Since the height at the deletion position was positive in \(w'\), at least one arc spans that position. Choose \((a,b)\) among such spanning arcs with smallest right endpoint. Restore the two consecutive positions and replace this arc by \((a,s+1)\) and \((s,b)\), leaving the other arcs unchanged (with their endpoints relabelled).

The replacement arcs cross each other. Any third arc crossing \((a,b)\) formerly crosses **exactly one** of the replacement arcs: if it ends before the insertion position, it crosses \((a,s+1)\); if its opening lies after the insertion position, it crosses \((s,b)\); and if it spans the insertion position, its right endpoint is greater than \(b\) by the choice of \((a,b)\), and it crosses only \((a,s+1)\) when it formerly crossed \((a,b)\). A third arc not crossing \((a,b)\) cannot acquire a new crossing: the only apparent exceptional case would be an arc nested inside \((a,b)\) spanning the insertion position and ending before \(b\), excluded by the minimal right endpoint of the selected spanning arc. These statements follow directly from the strict linear order of the endpoints. Thus the new crossing graph replaces one tree vertex by two adjacent vertices and distributes its old incident edges, without deleting or duplicating any of those edges. It is a tree, with exactly one more crossing than \(M'\), namely \(n-1\).

**One-at-a-time monotone interpolation.** List the closing positions in increasing order. If two **consecutive closings** \(c<d\) are paired to openers \(b>a\), respectively, the arcs \((b,c)\), \((a,d)\) are nested. Interchange the partners to obtain \((a,c)\), \((b,d)\). Both original openers were present at \(c\), so the swap preserves the opening word. Counting crossings when chords close proves that the swap increases the total crossing count by exactly one: at \(c\), choosing \(a\) rather than \(b\) adds \(1+q\) crossings, where \(q\) is the number of other active openers between \(a\) and \(b\); at the immediately next closing \(d\), choosing \(b\) rather than \(a\) removes exactly \(q\), while the contribution from openers appearing between \(c\) and \(d\) cancels. There is no intervening closing. All other contributions are unchanged.

The swap also preserves connectedness: every other arc crossing either original nested arc still crosses at least one of the two new arcs. This is checked by the endpoint order \(a<b<c<d\): a third chord's endpoints lie in the five successive regions cut by these four endpoints; if exactly one endpoint lay inside \((a,d)\), it lies on opposite sides of at least one of \((a,c)\), \((b,d)\); if exactly one lay inside \((b,c)\), the same holds. The new arcs cross each other. Hence their union remains attached to every former neighbouring chord and the other adjacencies remain unchanged. Connectedness survives.

Repeatedly swapping adjacent inverted opener indices in the closing-order sequence bubble-sorts that sequence to \((1,\ldots,n)\), which is the first-in-first-out matching. Each swap increases the number of crossings by one and preserves connectedness. Applied to the crossing-tree matching, this visits exactly every integer from \(n-1\) through \(K(w)\), proving the theorem.

## Verification

The included `verify.py` uses exact integer arithmetic and no third-party dependencies. Run `python verify.py`. It independently enumerates all Dyck opening words and all compatible matchings through semilength six, checks each connected crossing-count spectrum, and validates every adjacent-inversion step for every connected matching in those sizes. It separately checks the recursive crossing-tree construction and its complete increasing sequence for each primitive word through semilength ten. These finite checks corroborate, but do not replace, the unrestricted induction and swapping arguments.

## Relationship to prior work

Gross and Šarković (arXiv:2607.02410, publicly posted July 2, 2026) study local chord swaps and the dynamics of polygonal side matchings under a fixed-genus constraint. The present question instead fixes the left-endpoint set and requires connectivity of the crossing graph, while varying the *number* of crossings. Their stated mixing result is not an implication of this theorem, nor is its converse established here.

Chen, Deng, Du, Stanley and Yan (arXiv:math/0501230) study crossings and nestings for matchings, including refinements fixing minimal and maximal endpoints; their joint-distribution symmetry does not impose connectedness of the crossing graph. Pilaud and Rué's *Analytic Combinatorics of Chord and Hyperchord Diagrams with \(k\) Crossings*, especially §2.2, explicitly defines connected matchings by connected crossing graph, proves the general \(n-1\) lower bound and enumerates the unrestricted connected family. Their statements do not give the present fixed-opening-set endpoint, exact maximum or gap-free support. The present result can therefore be read as a support refinement of these complementary frameworks, not a claim of novelty for their earlier definitions and bounds.

## Limitations

The theorem is about crossing counts and existence, not the number of matchings realizing each value, the complete topology of the local-swap reconfiguration graph, or chord-diagram genus. It does not claim strict log-concavity or any distributional asymptotic. Historical priority remains provisional: primary publications were checked for direct statement implication, but unindexed or differently named results may exist. No independent mathematical audit has occurred.

## References

1. R. Gross and A. Šarković, *Polynomial mixing for polygonal side matchings*, arXiv:2607.02410 (first public July 2, 2026), https://arxiv.org/abs/2607.02410.
2. W. Y. C. Chen, E. Y. P. Deng, R. R. X. Du, R. P. Stanley and C. H. Yan, *Crossings and Nestings of Matchings and Partitions*, arXiv:math/0501230, https://arxiv.org/abs/math/0501230.
3. V. Pilaud and J. Rué, *Analytic Combinatorics of Chord and Hyperchord Diagrams with \(k\) Crossings*, https://www.ub.edu/comb/vincentpilaud/documents/publications/PilaudRue_QuasiPlanarFamilies_DM.pdf, §2.2.
