# Minimal forts of fan graphs: structural classification and rational enumeration

## Finding

For every integer \(n\ge2\), let \(F_n=K_1\vee P_n\), where the path has ordered vertices \(v_1,\ldots,v_n\) and the additional vertex \(h\) is adjacent to every path vertex. A **fort** is a nonempty vertex subset \(X\) for which every vertex outside \(X\) has either zero or at least two neighbors in \(X\). The following two classes are disjoint and exhaust the **inclusion-minimal forts** of \(F_n\):

1. **Path class.** Sets \(X\subseteq\{v_1,\ldots,v_n\}\) whose binary incidence word begins and ends in \(1\), contains no \(00\), and contains no \(111\).
2. **Hub class.** Sets \(\{h\}\cup D\), where \(D\) is an inclusion-minimal dominating set of \(P_n\), other than \(D=\{v_1,v_3,\ldots,v_n\}\) when \(n\) is odd.

Write \(f_n\) for the path-class count and \(d_n\) for the number of inclusion-minimal dominating sets of \(P_n\). Then
\[
 m_n= f_n+d_n-\mathbf1_{n\text{ odd}}\quad(n\ge2),
\]
where the generating functions (with \(f_0=0\) and \(d_0=1\)) are
\[
 F(z):=\sum_{n\ge0}f_n z^n=\frac{z+z^2}{1-z^2-z^3},\qquad
 D(z):=\sum_{n\ge0}d_n z^n=\frac{1+z+z^2-z^5}{1-z^2-z^3-z^4+z^6}.
\]
Consequently, with the natural initial conventions \(m_0=m_1=1\),
\[
 \boxed{\sum_{n\ge0}m_nz^n=D(z)+F(z)-\frac{z}{1-z^2}.}
\]
For \(n=2,3,\ldots,16\), the counts are respectively
\(3,2,6,5,10,12,18,24,34,47,65,90,125,173,240\).

## Assumptions and scope

Graphs are finite, undirected and simple; all vertex subsets and graph vertices are distinguished. Dominating means **closed-neighborhood domination**: \(D\subseteq V(G)\) dominates \(G\) if every vertex in \(V(G)\setminus D\) has a neighbor in \(D\). Minimality for forts and dominating sets is **inclusion minimality**, not minimum cardinality. For a subset \(X\) of path vertices, its incidence word has a \(1\) at precisely the selected indices. The general claim starts at \(n\ge2\); the zero/one initial coefficients are only the natural rational-series conventions (the one-vertex and two-vertex complete-graph cases). These formulas count **all** inclusion-minimal forts, not only minimum forts.

## Proof

**Step 1: path forts and their minimal members.** Let \(T\) be a nonempty fort of \(P_n\). Each endpoint must belong to \(T\): otherwise the boundary between the endpoint's omitted run and the first selected vertex would have an exterior vertex with exactly one neighbor in \(T\). Likewise, two consecutive unselected path vertices are impossible: a transition from a selected vertex into such an omitted run produces an exterior vertex with exactly one selected neighbor. Conversely, if both endpoints are selected and there are no consecutive omitted vertices, each omitted interior vertex has its two path neighbors selected; hence \(T\) is a fort. Every such fort dominates \(P_n\).

Among these, the inclusion-minimal forts are exactly those without three consecutive selected vertices. Indeed, if an interior selected vertex has both neighbors selected, it can be removed while retaining the endpoint and no-\(00\) properties. Conversely, when there is no \(111\), removing a selected endpoint violates the necessary selected-endpoint condition. Removing an interior selected vertex makes at least one pair of consecutive vertices unselected, since its two neighbors cannot both be selected. Thus every single-vertex deletion violates a necessary condition for being a path fort. Any proper subfort would permit a single-vertex removal first, so all these forts are inclusion-minimal. Every subset avoiding \(00\) and \(111\) with endpoints selected consists of blocks of one or two \(1\)'s separated by a single \(0\). The first block contributes \(z+z^2\), each further block contributes \(z^2+z^3\), giving
\[
 F(z)=\frac{z+z^2}{1-(z^2+z^3)}.
\]

**Step 2: forts without the hub.** If \(X\subseteq V(P_n)\) is a path fort, then \(|X|\ge2\), so the outside vertex \(h\) has at least two neighbors in \(X\). Thus \(X\) is a fan fort. Conversely, the restriction of a hub-free fan fort to path vertices is a path fort. The two families of nonempty hub-free forts are identical, so their inclusion-minimal members coincide.

**Step 3: forts with the hub.** Put \(X=\{h\}\cup D\), where \(D\subseteq V(P_n)\). An omitted path vertex has the selected neighbor \(h\), so it satisfies the fort condition precisely when it has at least one further neighbor in \(D\). Consequently \(X\) is a fan fort if and only if \(D\) dominates \(P_n\). Such \(X\) cannot be inclusion-minimal unless \(D\) is an inclusion-minimal dominating set. Conversely, for minimal dominating \(D\), no smaller fan fort containing \(h\) exists.

A smaller hub-free fan fort inside \(X\) would be a path fort \(T\subseteq D\). By Step 1, every path fort dominates \(P_n\); minimality of the dominating set \(D\) therefore forces \(T=D\). Thus the hub-containing fort \(\{h\}\cup D\) is inclusion-minimal exactly when \(D\) is minimally dominating and is not itself a path fort.

If \(D\) is both a path fort and a minimal dominating set, then no two selected vertices may be adjacent. Indeed, each omitted vertex in a path fort has *two* selected neighbors, so it cannot serve as a private dominated vertex of a selected vertex. If two selected vertices were adjacent, neither of their own vertices would be a private dominated vertex, contradicting minimal domination. With both endpoints selected and no two omitted vertices adjacent, the only remaining possibility is the alternating independent word \(101\cdots101\). It exists exactly when \(n\) is odd and is readily checked to dominate minimally. Hence exactly one hub-class candidate must be excluded when \(n\) is odd.

**Step 4: count all minimal dominating sets of a path.** In the indicator word of an inclusion-minimal dominating set, selected runs have length at most two (a middle vertex of a longer run would be removable); consecutive runs are separated by one or two zeros (domination), and a run of two selected vertices must have two zeros separating it from each neighboring run so that both selected vertices have private dominated vertices. Such a two-run at the left or right boundary needs exactly one leading or trailing zero, respectively; a singleton run permits zero or one boundary zero. Conversely, these conditions ensure domination and give a private dominated vertex to every selected vertex, hence are sufficient for inclusion-minimality.

Let run states \(A\), \(B\) represent singleton and doubleton selected runs. Marking total path length by \(z\), the initial-run weights, ending weights, and weighted transitions are respectively
\[
 u=\begin{pmatrix}z(1+z)&z^3\end{pmatrix},\qquad
 v=\begin{pmatrix}1+z\\z\end{pmatrix},\qquad
 T=\begin{pmatrix}z^2+z^3&z^4\\z^3&z^4\end{pmatrix}.
\]
The empty path contributes one, and nonempty minimal dominating sets correspond bijectively to nonempty walks through these states, whence
\[
 D(z)=1+u(I-T)^{-1}v
 =\frac{1+z+z^2-z^5}{1-z^2-z^3-z^4+z^6}.
\]
Combining Steps 1–4 gives the classification and the claimed rational generating function.

## Verification

The attached standalone `verify_fan_forts.py` enumerates every nonempty subset of each \(F_n\) for \(2\le n\le16\), tests the **original fort neighborhood condition** directly, and determines inclusion-minimality from all smaller fort subsets. It independently enumerates the proposed word/dominating-set family, comparing **the actual sets**, not only their counts. It examines \(262{,}121\) candidate subsets and verifies every family equality in the stated finite range. It also expands the two rational generating functions and checks coefficients through order \(100\); the latter is an algebraic consistency check, not an infinite theorem. The complete source and recorded execution output are included in the package. The all-\(n\) assertions follow from the preceding proof, not the finite tests.

## Relationship to prior work

Becker, Cameron, Hanely, Ong and Previte (arXiv:2404.05963, first public 9 April 2024) studied minimal forts, including enumeration in paths and a preservation theorem for minimal forts under joins (their Proposition 20). Thus the path-class lift and its Padovan-type count are explicitly **prior knowledge**, not independently claimed as new here.

A publicly available earlier result titled *Zero forcing polynomial of fan graphs* gives an exact trigger characterization of **all zero-forcing sets** of fans and their cardinality enumerator; its proof separates the presence or absence of the universal vertex. This is strongly related through fort/hitting-set blocker duality: full knowledge of successful forcing sets contains implicit information about all forts. However, the earlier result does **not explicitly determine the minimal-fort hypergraph, the necessary dominance/minimality conditions, the alternating-word correction, or the rational count of all inclusion-minimal forts**. The distinct enumerative equality-case extraction, not the fan zero-forcing-set decision rule, is the present contribution. In particular, a coefficient enumerator for all successful forcing sets does not in general determine the number of inclusion-minimal forts. The previously published local membership characterization makes an equivalent implicit derivation possible, and this relation is a bibliographic priority risk rather than evidence of independence.

The classical enumeration of minimal dominating sets of paths is likewise a **known ingredient**; the transfer expression is derived here to keep the fan enumeration self-contained. Existing general results on maximal failed zero-forcing sets, including Abara–Pelayo's work on graph products, do not provide an explicit all-\(n\) census of minimal forts of fans in the inspected materials.

## Limitations

The theorem is limited to the ordinary fort condition and fans with one universal vertex over a path. It does not enumerate minimal forts for arbitrary cone graphs or quotients modulo graph automorphisms. Because the full fan zero-forcing-set membership condition is previously published, explicit novelty depends on distinguishing its implicit blocker-dual information from the nontrivial closed enumeration and classified minimal structures proved here. Full literature priority verification and independent mathematical validation remain outstanding. No experiment on finitely many fans is offered as an infinite proof.

## References

1. P. Becker, T. R. Cameron, D. Hanely, J. Ong, J. P. Previte, *On the Number of Minimal Forts of a Graph*, arXiv:2404.05963v1 (public 9 April 2024), https://arxiv.org/abs/2404.05963.
2. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910v1, https://arxiv.org/abs/1801.08910.
3. *Zero forcing polynomial of fan graphs*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-zero-forcing-polynomial-of-fan-graphs--f3b2c94da283 (especially its `RESULT.md` proof and exact forcing-set membership characterization).
4. M. N. M. Abara, P. A. B. Pelayo, *Maximal failed zero forcing sets for products of two graphs*, arXiv:2202.04997v1, https://arxiv.org/abs/2202.04997.
5. B. Jacob, *Well-failed graphs*, Australasian Journal of Combinatorics 93(2) (2025), 359–374, https://ajc.maths.uq.edu.au/pdf/93/ajc_v93_p359.pdf.
