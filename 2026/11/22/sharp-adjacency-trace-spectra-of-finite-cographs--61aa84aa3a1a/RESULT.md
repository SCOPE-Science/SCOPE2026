# Sharp adjacency-trace spectra of finite cographs

## Finding

For every integer \(m\geq1\), let \(G\) range over finite simple undirected cographs (graphs without an induced four-vertex path), and let \(A\subseteq V(G)\) have exactly \(m\) vertices. Set
\[
\mathcal T(G,A)=\{N_G(v)\cap A:v\in V(G)\},\qquad t(G,A)=|\mathcal T(G,A)|,
\]
where \(N_G(v)\) is the *open* neighborhood. Then the complete possible-value spectrum is
\[
\boxed{\{t(G,A):G\text{ a finite cograph},\ |A|=m\}=\{1,2,\ldots,2m\}.}
\]
The maximum \(2m\) is attainable with exactly \(2m\) total vertices, which is the least possible order of any attaining graph. The same statements hold for *closed*-neighborhood traces \(\{N_G[v]\cap A:v\in V(G)\}\). Consequently the maximum VC dimension of the open- or closed-neighborhood set system of a finite cograph is exactly two.

This counts truth patterns for the \(m\) adjacency tests \(E(x,a)\) with named distinct parameters \(a\in A\). It does not count equality literals or formulas with quantifiers.

## Assumptions and scope

Graphs are finite, loopless, undirected, and simple; \(A\) is nonempty. A *cograph* is a graph obtainable from single vertices by successive disjoint unions and complete joins. Equivalently, it has no induced \(P_4\). A complete join \(H_1\vee H_2\) adds all edges between disjoint vertex sets. The quantifiers in the finding range over every such graph and every \(m\)-element parameter set, with no restriction on the order of \(G\) beyond \(|V(G)|\ge m\).

## Proof

**Augmented-trace lemma.** For every nonempty \(A\) in a cograph \(G\), define
\[
\widehat{\mathcal T}(G,A)=\mathcal T(G,A)\cup\{\varnothing,A\}.
\]
We prove by induction on \(|V(G)|\) that
\[
|\widehat{\mathcal T}(G,A)|\le 2|A|.
\]
For a single-vertex graph, \(A=V(G)\), \(\mathcal T=\{\varnothing\}\), and the augmented family has two members. Otherwise represent \(G=G_1\sqcup G_2\) or \(G=G_1\vee G_2\), with both factors nonempty cographs. Write \(A_i=A\cap V(G_i)\).

If one \(A_i\) is empty, every vertex of that factor contributes only \(\varnothing\) (disjoint union) or only \(A\) (complete join). Both traces are already present in the augmented family of the nonempty-parameter factor, so the inductive bound is unchanged.

Suppose both \(A_i\) are nonempty, of sizes \(m_i\). For disjoint union, each trace from \(G_i\) lies inside \(A_i\). The augmented trace family is contained in
\[
\widehat{\mathcal T}(G_1,A_1)\cup\widehat{\mathcal T}(G_2,A_2)\cup\{A\}.
\]
The two displayed augmented families overlap exactly at \(\varnothing\), and \(A\) is not in either; hence the size is at most \(2m_1+2m_2-1+1=2(m_1+m_2)\).

For complete join, put
\[
\mathcal K_1=\{X\cup A_2:X\in\widehat{\mathcal T}(G_1,A_1)\},\qquad
\mathcal K_2=\{A_1\cup Y:Y\in\widehat{\mathcal T}(G_2,A_2)\}.
\]
These families have intersection exactly \(\{A\}\). Every trace in \(G\) belongs to \(\mathcal K_1\cup\mathcal K_2\), and the only further member possibly introduced by augmentation is \(\varnothing\). Thus their total size is at most \(2m_1+2m_2-1+1=2m\). Induction proves the lemma, and \(t(G,A)\le2m\).

**Sharp minimal-order construction.** Fix \(m\ge2\), let \(A=\{a_1,\ldots,a_m\}\) induce a clique, and add an independent set of \(m\) vertices with respective neighborhoods in \(A\) of the prefix lengths
\[
0,1,\ldots,m-2,m.
\]
All these prefixes are nested, so the graph is a threshold graph, hence a cograph. The \(m\) vertices in \(A\) realize the distinct traces \(A\setminus\{a_i\}\). None of the \(m\) chosen prefixes equals any of these (the sole prefix collision would have length \(m-1\), which was omitted). Hence exactly \(2m\) traces occur on exactly \(2m\) vertices. For \(m=1\), a single edge with one endpoint marked provides the two traces \(\varnothing\) and \(A\). Any graph with \(2m\) distinct traces must have at least \(2m\) vertices because each vertex contributes only one trace.

**No gaps.** For \(m\ge2\), the edgeless graph on \(A\) has one trace; a star on \(A\) has two. For every \(3\le k\le m\), the disjoint union of a \((k-1)\)-clique and \((m-k+1)\) isolated vertices, all in \(A\), has precisely \(k\) traces. For \(m\le k\le2m\), start with the clique on \(A\), which has \(m\) traces. Select any \(k-m\) of the \(m\) independent-prefix witnesses from the previous construction; each adds a distinct new trace, and the resulting induced subgraph remains a cograph. The cases \(m=1\) have values one (single isolated vertex) and two (single edge). This proves the complete spectrum.

**Closed traces and VC dimension.** For every simple graph, \(N_G[v]\cap A=A\setminus(N_{\overline G}(v)\cap A)\). Cographs are closed under complementation. Complementing every trace is a bijection, proving the identical closed-trace spectrum. A shattered three-element parameter set would require eight traces, contradicting the upper bound six at \(m=3\). The \(m=2\) sharp construction has four traces and shatters its marked pair; its complement does so for closed neighborhoods.

## Verification

The standalone Python checker `verify.py` exhaustively enumerates every labeled simple graph through six vertices, filters by induced \(P_4\), and checks the bound for every nonempty parameter set. It also verifies the sharp threshold constructions for \(1\le m\le14\) and witnesses for each integer in each spectrum for \(1\le m\le11\). Execution output was:

```
VERIFY_OK exhaustive_cographs=6039 exhaustive_parameter_sets=362227 extremal_sizes=14 spectra=132
```

The all-\(m\) statements are proved by the induction and constructions above. The finite checker is a consistency test, not an infinite proof.

## Relationship to prior work

Dreier, Mählmann, and Toruńczyk (2026, arXiv:2611.08143, first posted November 5) prove broad fixed-parameter tractability and polynomial bounds on types in monadically dependent graph classes. Their results do not identify the exact coefficient or complete trace-count spectrum for the zero-twin-width subclass of cographs. Dreier, Mählmann, McCarty, Pilipczuk, and Toruńczyk (2026, arXiv:2607.10941) prove almost-linear general neighborhood complexity without this coefficient.

Bonnet, Foucaud, Lehtilä, and Parreau (arXiv:2301.04217, first posted January 10, 2023) give the explicit bound \((d+2)2^{d+1}m\) at twin-width at most \(d\). At \(d=0\), this yields \(4m\), not the sharp \(2m\) here. Bonamy and Geniet (arXiv:2504.08266, first posted April 11, 2025) give linear complexity for bounded merge-width but no cograph trace spectrum. Threshold-graph logical-type and online-shattering results concern different equivalence relations or complexity measures and do not supply this open-neighborhood count spectrum. These are comparisons of implications, not claims that the cited works have no other relevance.

## Limitations

The theorem concerns only the adjacency tests against named parameters, not complete first-order types with equality, counting, quantifiers, or arbitrary definable relations. Its scope is the cograph class, not all bounded-twin-width graphs. The exact same invariant might appear under another name in older cograph, cotree, or neighborhood-complexity literature; exhaustive historical priority is not established. The upper bound alone is a simple consequence of the cotree decomposition; the contribution assessed here is the *sharp coefficient, all-integer spectrum, and minimal witnessing order* together.

## References

1. J. Dreier, N. Mählmann, S. Toruńczyk, *First-Order Model Checking on Monadically Dependent Graph Classes*, arXiv:2611.08143 (first public 2026-11-05), https://arxiv.org/abs/2611.08143.
2. J. Dreier, N. Mählmann, R. McCarty, M. Pilipczuk, S. Toruńczyk, *Neighborhood Complexity and Radius-1 Merge-Width in Monadically Dependent Graph Classes*, arXiv:2607.10941 (first public 2026-07-12), https://arxiv.org/abs/2607.10941.
3. É. Bonnet, F. Foucaud, T. Lehtilä, A. Parreau, *Neighbourhood complexity of graphs of bounded twin-width*, arXiv:2301.04217 (first public 2023-01-10), https://arxiv.org/abs/2301.04217.
4. M. Bonamy, C. Geniet, *\(\chi\)-Boundedness and Neighbourhood Complexity of Bounded Merge-Width Graphs*, arXiv:2504.08266 (first public 2025-04-11), https://arxiv.org/abs/2504.08266.
