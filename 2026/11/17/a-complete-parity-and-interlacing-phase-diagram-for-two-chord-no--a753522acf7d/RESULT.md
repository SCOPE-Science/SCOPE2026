# A complete parity-and-interlacing phase diagram for two-chord non-matching complexes

## Finding
For any integer \(t\ge3\), start with \(C_{2t}\), whose vertices are labeled \(0,1,\dots,2t-1\) cyclically, and add two distinct chords \(e,f\), neither of which is a cycle edge. Define \(\operatorname{NM}_t(G)\) to be the abstract simplicial complex on \(E(G)\) whose faces are precisely the edge sets having no matching of \(t\) edges. An **odd chord** joins opposite parities; an **even chord** joins equal parities.

The complete integral homotopy classification is
\[
|\operatorname{NM}_t(C_{2t}+e+f)|\simeq
\begin{cases}
S^{2t-3},& e,f\text{ both odd};\\
S^{2t-2},& e,f\text{ both even and cross with different parity classes};\\
*,&\text{otherwise}.
\end{cases}
\]
In the second case the two even chords have four distinct endpoints and these endpoints alternate between the two chords in cyclic order. Sharing endpoints is allowed in the first case. Both noncontractible cases have one primitive integral homology generator and no other reduced homology.

## Assumptions and scope
Graphs are simple; \(t\ge3\) ensures the cycle has genuine chords. The two added chords are distinct, but need not be vertex-disjoint. The non-matching convention excludes a \(t\)-matching from a face, so its minimal nonfaces are exactly the edge sets of perfect matchings of \(G\). All homotopy statements concern the usual geometric realization and integral coefficients.

## Proof
**1. Perfect-matching census.** Let \(A\) and \(B\) denote the two alternating perfect matchings of \(C_{2t}\). An odd chord \(x\) belongs to a unique perfect matching \(M_x\) in \(C_{2t}+x\): deleting its endpoints divides the remaining cycle into two paths of even order, each with a unique perfect matching. An even chord belongs to none. In \(C_{2t}+e+f\), the only additional possibility is a matching \(M_{ef}\) using both chords. This exists exactly when the chords have disjoint endpoints and the four endpoints, in circular order, alternate parity. Indeed, the complementary four path segments must all have even numbers of interior vertices, and their perfect matchings are then unique.

**2. Cone cases.** If an added chord belongs to no perfect matching, it occurs in no minimal nonface, so it is a cone vertex of \(\operatorname{NM}_t(G)\). An even chord can belong to a perfect matching only alongside a second even chord whose endpoints have the opposite parity and whose endpoints interlace cyclically. Thus all cases other than two odd chords or crossing, opposite-parity even chords are cones.

**3. Two even interlacing chords.** Here there are precisely three perfect matchings \(A,B,M_{ef}\). For a complex on an \(m\)-element ground set, its Alexander dual has facets the complements of its minimal nonfaces. Here \(m=2t+2\). All three dual facets intersect pairwise: the complement of \(A\cup B\) is the two-chord set; the complements of \(A\cup M_{ef}\) and \(B\cup M_{ef}\) each include cycle edges not used by the corresponding matchings. Their triple intersection is empty because \(A\cup B\cup M_{ef}=E(G)\). Every nonempty intersection is a simplex, so the nerve theorem identifies the Alexander dual with the boundary of a triangle, hence \(S^1\).

**4. Two odd chords: no joint matching.** Write \(X=M_e\), \(Y=M_f\). If no matching uses both chords, the only perfect matchings are \(A,B,X,Y\). Every triple among their complements intersects: the triples omitting \(X\) or \(Y\) omit that chord; for \(A,X,Y\) or \(B,X,Y\), a cover of all cycle edges would force \(B\subseteq X\cup Y\) or \(A\subseteq X\cup Y\). To see this is impossible, note that the symmetric differences \(X\triangle A\) and \(Y\triangle A\) are unique alternating circuits through their respective added chords. If \(A\subseteq X\cup Y\), their removed \(A\)-edges are disjoint, so the two circuits are vertex-disjoint (every affected vertex lies on a removed \(A\)-edge), and flipping both gives a perfect matching using both chords, contradiction; the same argument applies to \(B\). The fourfold intersection is empty because \(A\cup B\cup X\cup Y\) uses every edge. Thus the dual-facet nerve is exactly the boundary of a tetrahedron, \(S^2\).

**5. Two odd chords: a joint matching.** Let \(Z=M_{ef}\). The alternating-path description shows that exactly one of \(R\in\{A,B\}\) allows \(X\) and \(Y\) to be obtained by independent flips along vertex-disjoint \(R\)-alternating cycles; flipping both produces \(Z\). Denote the other cycle matching by \(R'\). Comparing union coverage on each alternating arc yields the *complete list of maximal simplices* of the dual-facet nerve:
\[
\{R,X,Y,Z\},\quad\{R',R,X\},\quad\{R',R,Y\},\quad\{R',X,Z\},\quad\{R',Y,Z\}.
\]
For example, a family containing \(R,R',Z\) covers all graph edges, so it is absent; the four displayed triangles containing \(R'\) miss one of the removed \(R\)-edges or one of the chords, so they are present. All remaining inclusions follow by the same two independent alternating arcs. The nerve is the tetrahedron on \(\{R,X,Y,Z\}\) union the cone from \(R'\) over its four-cycle \(R-X-Z-Y-R\). Both pieces are contractible, intersect in that cycle, and their union is homotopy equivalent to \(S^2\).

**6. Integral duality and homotopy upgrade.** Combinatorial Alexander duality gives
\[
\widetilde H_i(\operatorname{NM}_t(G);\mathbb Z)\cong
\widetilde H^{(2t+2)-i-3}(\operatorname{NM}_t(G)^\vee;\mathbb Z).
\]
Thus the even-crossing case has one copy of \(\mathbb Z\) in degree \(2t-2\); both odd cases have one in degree \(2t-3\); all other reduced groups vanish. For \(t\ge4\), every two-simplex is allowed (the minimum forbidden size is \(t\ge4\)), and the complete two-skeleton makes the complex simply connected. At \(t=3\), each missing triangle is a perfect matching. Its boundary is coned using any edge outside that perfect matching: replacing a single edge of a perfect matching cannot give another perfect matching of a simple graph. The three coning triangles are therefore present. Since the graph one-skeleton is complete, this kills every generator of \(\pi_1\), also proving simple connectivity at \(t=3\). Hurewicz and Whitehead now upgrade the isolated primitive homology group to the stated sphere homotopy type.

## Verification
The included standard-library Python program independently enumerates *all* pairs of distinct chords for \(t=3,4,5\), reconstructs all perfect matchings from the graph, constructs the dual-facet nerve from actual edge unions, and checks the predicted nerve face-vector and existence of cone vertices. The complete test checks 36, 190 and 595 chord pairs, respectively. Run `python check.py`; its recorded output is supplied as `check_output.txt`. Finite tests support, but are not used in place of, the general alternating-arc and duality proof.

## Relationship to prior work
Shan and Wang (2026) prove top-degree homology injectivity under bipartite edge additions and derive Leray/regularity statements, but the available abstract does not give the all-pair integral homotopy classification. A prior published mathematical note proves a particular even-crossing instance, with short chords \(\{0,2\}\) and \(\{1,3\}\), including an intermediate cone. That example is a covered specialization, **not** claimed as new here. The new claim is the exhaustive dependence on odd/even chord types, parity classes, and endpoint interlacing, particularly the two-odd-chord stability even with a shared endpoint. The primary paper's complete text and the prior note's complete source were not retrievable in this run; their summaries establish limited comparisons, not full-document absence of overlap.

## Limitations
Only the maximal matching threshold \(t\) on a cycle of length \(2t\), with precisely two added non-cycle edges, is classified. This is a nonequivariant homotopy result and does not determine other thresholds, more added chords, or equivariant modules. The originality comparison against two plausible complete papers has the stated access limitation.

## References
1. J. Shan and Z. Wang, *Homology of non-matching complexes under edge additions and applications to their Stanley-Reisner ideals*, arXiv:2609.02621, first posted 2026-09-02, https://arxiv.org/abs/2609.02621.
2. *The sphere–cone–sphere transition for twice-chorded even-cycle non-matching complexes*, published mathematical result dated 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-the-sphere-cone-sphere-transition-for-twice-chorded-even-cycle-n--5ef7c9c97e9d.
3. Standard combinatorial Alexander duality, nerve lemma, Hurewicz theorem, and Whitehead theorem.
