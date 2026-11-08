# Clique-coning additivity of the preference-stable chromatic number

## Finding
For every finite **nonempty** simple undirected graph \(G\) and every integer \(t\geq0\), the preference-stable chromatic number obeys the exact join law
\[
\chi_{\mathrm{stable}}(K_t\vee G)=t+\chi_{\mathrm{stable}}(G).
\]
Here \(K_0\vee G=G\), and \(K_t\vee G\) is the graph obtained by adding a clique of \(t\) new vertices, each adjacent to every vertex of \(G\). In particular, adjoining one universal vertex increases the parameter by exactly one, even when \(G\) is disconnected.

Since also \(\chi(K_t\vee G)=t+\chi(G)\), the stable-colouring excess \(\chi_{\mathrm{stable}}-\chi\) is unchanged by clique coning. Combined with the previously proved values for paths, cycles, and complete bipartite graphs [1], the law yields \(\chi_{\mathrm{stable}}(K_t\vee P_n)=t+3\) for \(n\ge4\), \(\chi_{\mathrm{stable}}(K_t\vee C_n)=t+3\) for \(n\ge3\), and
\[
\chi_{\mathrm{stable}}(K_t\vee K_{a,b})=t+\min\{a,b\}+1\qquad(a,b\ge1).
\]
The general join identity, not any particular substituted family, is the finding.

## Assumptions and scope
A preference profile on a palette \([q]=\{1,\dots,q\}\) assigns to every vertex a strict total ordering of these \(q\) named colours. A proper \(q\)-colouring \(f\) may use fewer than \(q\) colours. Its **envy digraph** has an arc \(x\to y\) for each edge \(xy\) of the graph whenever \(x\) strictly prefers \(f(y)\) to \(f(x)\); opposite arcs are allowed. The colouring is **stable** if this digraph has no directed cycle. The integer \(\chi_{\mathrm{stable}}(G)\) is the least \(q\) such that *every* preference profile on \([q]\) has a stable proper \(q\)-colouring. This definition agrees with [1]; colour names can be relabelled by a bijection. We assume a nonempty vertex set to avoid the convention-dependent value for an empty graph. The universal-existence property is monotone in palette size: if every profile on \(q\) colours has a stable proper colouring, then every profile on \(q+1\) colours does too, because deleting any fixed colour from all rankings gives a \(q\)-profile and its stable colouring still has the same envy arcs when regarded as a \(q+1\)-colouring. Thus ruling out stable \(q\)-colourings for one profile excludes all smaller palette sizes.

## Proof
**Step 1: one-vertex upper bound.** Set \(k=\chi_{\mathrm{stable}}(G)\). Given *any* profile on \(k+1\) colours for \(H=K_1\vee G\), let \(u\) be the new universal vertex and choose its most preferred colour \(c\). Assign \(c\) to \(u\). There are \(k\) other colours; restrict each original vertex's ranking to them. By the definition of \(k\), after a harmless relabelling, \(G\) has a stable proper colouring with these \(k\) colours. The combined colouring of \(H\) is proper. In its envy digraph, \(u\) has no outgoing arc because it has its favourite colour. A directed cycle therefore cannot pass through \(u\); any directed cycle entirely inside \(G\) is excluded by the restricted colouring. Hence \(\chi_{\mathrm{stable}}(H)\le k+1\).

**Step 2: one-vertex lower bound when \(k\ge2\).** Since \(k\) is minimal, there exists a preference profile \(R\) on the palette \([k-1]\) for which \(G\) has **no** stable proper colouring. On the \(k\)-colour palette \([k]\), extend each vertex ranking in \(G\) by placing the extra colour \(k\) *last*, leaving the relative order within \([k-1]\) unchanged. Give \(u\) a ranking with colour \(k\) *first* (the order of other colours does not matter). Suppose a stable proper \(k\)-colouring \(f\) of \(H\) exists.

If \(f(u)=k\), then all vertices of \(G\), adjacent to \(u\), receive colours in \([k-1]\); their induced envy digraph is acyclic. This contradicts the choice of \(R\).

If \(f(u)=c\in[k-1]\) and some \(v\in V(G)\) has \(f(v)=k\), then \(u\) envies \(v\) (its favourite is \(k\)) and \(v\) envies \(u\) (\(k\) is worst at every original vertex). The two arcs form a directed \(2\)-cycle, contrary to stability. Consequently no vertex of \(G\) uses \(k\). Properness also excludes the colour \(c\) from \(G\). Restricting \(f\) to \(G\) thus gives a stable proper colouring using colours among \([k-1]\), again contradicting \(R\). Hence no stable \(k\)-colouring of \(H\) exists for this profile, and \(\chi_{\mathrm{stable}}(H)\ge k+1\).

**Step 3: \(k=1\) boundary.** For nonempty \(G\) with \(k=1\), there are no edges in \(G\), since any edge forbids a one-colouring. The cone \(H\) contains an edge, so every proper colouring uses at least two colours. Step 1 supplies a stable two-colouring under every profile. Thus \(\chi_{\mathrm{stable}}(H)=2=k+1\).

**Step 4: induction and ordinary chromatic excess.** Repeatedly apply the established one-vertex identity to \(G,K_1\vee G,\ldots\). Their successive clique joins are isomorphic to \(K_t\vee G\). Ordinary chromatic additivity under joining a clique is elementary because each clique vertex must receive its own colour distinct from all colours on \(G\); applying both identities proves the excess assertion.

All steps hold for every graph order, every strict profile, and every nonnegative integer \(t\); no finite enumeration is used to extrapolate the theorem.

## Verification
The proof above is self-contained once the definition from [1] is fixed. To independently cross-check the envy-cycle definition and the lower-bound preference lifting, run `python3 artifacts/verify.py` from a directory containing the extracted package. The program exhaustively enumerates strict preference profiles and proper colourings for several one- to four-vertex graphs, then constructs the prescribed cone obstruction. It also independently checks acyclicity by depth-first-search, rather than by the mathematical proof's case argument. Its expected final line is `VERIFY_OK`. This finite check is supplementary; the universal statement follows from the proof.

## Relationship to prior work
Koana, Oh, and Yoneda [1] introduced this precise stable-colouring invariant and proved a reachability upper bound, a Grundy lower bound, subgraph monotonicity, and exact values for paths, cycles, and complete bipartite graphs. Their appendix supplies a small preference obstruction, but the inspected text does not state or prove the **universal clique-coning identity**. An acyclic-orientation bound for the cone is generally only \(\mathrm{reach}(G)+1\), which can strictly exceed \(\chi_{\mathrm{stable}}(G)+1\) (as [1] demonstrates for odd cycles), so the new exact law is not a numerical corollary of those two bounds. The source's special-family values yield the displayed cone families only after applying the new law.

The published result *Stable chromatic number of the complete tripartite graph \(K_{2,3,3}\)* [2] proves one graph-specific value by a finite five-colour obstruction. Its full scientific result was inspected. A fixed tripartite example cannot imply the general identity for **every** \(G\) and \(t\); neither does its upper-bound orientation argument establish the lower-bound preference-lifting mechanism. Searches of published result records and literature for `stable chromatic join`, `universal vertex`, `apex`, `cone`, and equivalent colour-preference formulations did not identify a stronger covering statement. These are bounded searches, not proof of historical uniqueness.

## Limitations
The theorem is for the **clique** join \(K_t\vee G\), not the join of two arbitrary graphs, not a classification of stable colourings of \(G\), and not a formula for stable chromatic numbers before a base graph's value is known. Its correctness does not depend on any computer calculation. The finite verifier checks examples rather than providing independent certification. The literature comparison is best-knowledge and may miss unpublished, differently termed, or inaccessible earlier formulations. Independent mathematical audit has not been performed.

## References
1. Tomohiro Koana, Yeeseok Oh, and Hirotaka Yoneda, *Graph Coloring with Color Preferences*, arXiv:2609.00569v1, first submitted 1 September 2026, https://arxiv.org/abs/2609.00569 . Definition of stable colouring, Theorem 3.1, Theorem 3.3, Proposition 3.4, Propositions 3.5–3.7, and Appendix A.
2. *Stable chromatic number of the complete tripartite graph \(K_{2,3,3}\)*, published mathematical record dated October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-stable-chromatic-number-of-the-complete-tripartite-graph-k-2-3-3--b34a81e3d305 . Inspected `RESULT.md`.
