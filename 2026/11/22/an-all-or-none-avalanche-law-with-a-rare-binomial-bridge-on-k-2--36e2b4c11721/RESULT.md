# An all-or-none avalanche law with a rare binomial bridge on \(K_{2,n}\)

## Finding

Let \(n\ge 2\) be an integer. In the standard undirected Abelian sandpile on the complete bipartite graph \(K_{2,n}\), choose one vertex of the \(n\)-vertex part as the sink. Draw an initial stable configuration uniformly among all recurrent configurations, add one grain at a prescribed nonsink vertex, and let \(T\) be the total number of topplings, **counting repeated topplings**. Write \(H_n(x)=\sum_t N^{(H)}_{n,t}x^t\) when the driven vertex belongs to the two-vertex part, and \(L_n(x)=\sum_t N^{(L)}_{n,t}x^t\) when it is one of the other \(n-1\) vertices of the sink's part. Then the complete source-resolved avalanche-size polynomials are

\[
\boxed{H_n(x)=(n-1)2^{n-2}(1+x^{n+1})+x(1+x)^{n-1},}
\]
\[
\boxed{L_n(x)=(n-1)2^{n-2}(1+x^{n+2})+2x^2(1+x)^{n-2}.}
\]

In particular, there are exactly \(n2^{n-1}\) recurrent initial configurations. Under either source choice, the probability of no topplings and that of the maximum-size avalanche are both \((n-1)/(2n)\). The remaining event has probability exactly \(1/n\). Conditional on this intermediate event,

\[
T_H\stackrel{d}=1+\operatorname{Bin}(n-1,1/2),\qquad
T_L\stackrel{d}=2+\operatorname{Bin}(n-2,1/2).
\]

Consequently, for either source and \(n\to\infty\), the normalized avalanche size obeys

\[
T/n\ \Longrightarrow\ \tfrac12\delta_0+\tfrac12\delta_1.
\]

The exceptional intermediate avalanche is a binomially concentrated bridge near half-system size, occurring with probability \(1/n\). The exact mean toppling totals are \(\mathbb E T_H=(n+1)/2\) and \(\mathbb E T_L=(n+2)/2\), while \(\operatorname{Var}(T)/n^2\to1/4\) in both cases. The maximum event at a hub has \(n+1\) topplings, each site once; at a nonsink leaf it has \(n+2\) topplings, because the driven leaf fires twice.

## Assumptions and scope

The graph is simple, undirected, unweighted and labelled. Denote the vertices in the two-vertex part by \(A,B\), and the other part by the sink \(s\) and \(m=n-1\) nonsink leaves \(v_1,\ldots,v_m\). The sink absorbs every incoming grain without toppling. A hub has degree and toppling threshold \(n\); a nonsink leaf has degree and threshold \(2\). A toppling sends one grain along each incident edge, with dissipation at the sink. An initial stable state has hub heights \(a,b\in\{0,\ldots,n-1\}\) and leaf heights \(\epsilon_i\in\{0,1\}\). It is called recurrent in the usual Dhar/burning sense. Every recurrent state has equal weight. The two driving classes are a fixed hub, say \(A\), and a fixed nonsink leaf, say \(v_1\); permutations within each class preserve the law. The exponent of \(x\) records the sum of all individual legal topplings, not the number of distinct vertices or the number of grains lost.

## Proof

**1. Recurrent-state characterization.** Put \(k=\sum_{i=1}^{m}\epsilon_i\). By Dhar's burning criterion, a stable state is recurrent exactly when adding one grain to each hub (the grains contributed by firing the sink) triggers one toppling of every nonsink vertex and returns the same state. Since no leaf receives a grain directly from the sink, the first toppling must be a hub initially at height \(n-1\). Its toppling causes exactly the \(k\) leaves at height one to topple; each gives a grain to the other hub. The latter can topple exactly when its original height is at least \(n-1-k\). Its toppling makes all remaining leaves topple, completing the burning sequence. Thus recurrence is equivalent to

\[
\big(a=n-1\ \text{and}\ b\ge n-1-k\big)\quad\text{or}\quad
\big(b=n-1\ \text{and}\ a\ge n-1-k\big).
\tag{1}
\]

After this sequence all sites have toppled once, and firing the sink followed by all nonsink vertices once has zero net effect on every nonsink height. Hence the conditions are sufficient as well as necessary. For any fixed assignment of the leaf heights with \(k\) ones, relation (1) permits exactly \(2k+1\) ordered hub-height pairs: \(k+1\) pairs along each of two sides of a square, with their common corner counted once. Therefore the total number of recurrent states is

\[
\sum_{k=0}^{m}\binom mk(2k+1)=(m+1)2^m=n2^{n-1}.
\tag{2}
\]

**2. Adding at hub \(A\).** If \(a<n-1\), no site topples. For a fixed leaf assignment with \(k\) ones, (1) gives exactly \(k\) recurrent values of \(b\) with \(a<n-1\). Thus there are \(\sum_k k\binom mk=m2^{m-1}\) zero avalanches.

If \(a=n-1\), adding one grain makes \(A\) topple; then precisely the \(k\) initially occupied leaves topple. For the unique boundary value \(b=n-1-k\), hub \(B\) does not become unstable, so there are exactly \(1+k\) topplings. The \(\binom mk\) choices of occupied leaves produce the term \(x(1+x)^m\). For each of the other \(k\) admissible values \(b\in\{n-k,\ldots,n-1\}\), hub \(B\) topples and activates every originally empty leaf. Both hubs and all \(m\) leaves then fire exactly once, giving \(m+2=n+1\) topplings. To check termination, after all such firings the height of \(A\) is \(m<n\), that of \(B\) is at most \(n-2\), and every leaf is below threshold two. The number of this latter class is \(\sum_k k\binom mk=m2^{m-1}\). This proves the formula for \(H_n\).

**3. Adding at leaf \(v_1\).** If \(\epsilon_1=0\), no toppling occurs. Summing \(2k+1\) over assignments of the remaining \(m-1\) leaves gives \(m2^{m-1}\) zero avalanches. Suppose \(\epsilon_1=1\), with \(\ell\) other leaves at height one, so \(k=\ell+1\). The driven leaf topples and sends a grain to both hubs. At least one hub was at height \(n-1\) by (1), and therefore topples. Precisely two recurrent hub-height pairs, namely

\[
(a,b)=(n-1,n-1-k)\quad\text{or}\quad(a,b)=(n-1-k,n-1),
\]

have the other hub stop one grain below threshold after the \(\ell\) additional high leaves have fired. In either case the avalanche consists of the driven leaf, one hub, and those \(\ell\) leaves, hence \(\ell+2\) topplings. There are \(2\binom{m-1}{\ell}\) such states, yielding \(2x^2(1+x)^{m-1}\).

In every remaining recurrent state with \(\epsilon_1=1\), both hubs topple. Every one of the \(m-1\) other leaves topples once, and the driven leaf, having received a grain from each hub, topples for a **second** time. The number of topplings is \(2+2+(m-1)=m+3=n+2\). No further toppling is possible: the driven leaf has height zero after its second firing; each other leaf has height at most one; and each hub has received at most \(m+1=n\) grains while firing once from a height no greater than \(n-1\), ending below \(n\). For each fixed leaf assignment with \(k\ge1\), relation (1) supplies \(2k+1\) hub pairs, of which precisely two were intermediate. Thus there are \(2k-1\) maximum cases; summed over assignments including \(v_1\), this is \(m2^{m-1}\). This proves the formula for \(L_n\).

**4. Scaling and moments.** Divide either polynomial by (2) to get the exact stationary probability generating function. Each extreme term has probability \(m/(2(m+1))=(n-1)/(2n)\); the total weight of the intervening binomial term is \(1/n\). The conditional binomial distributions follow by coefficient comparison. Their means are centered at one-half of the corresponding maximal burst, making the unconditional mean exactly half of that maximum. The two extreme atoms converge to equal mass at zero and normalized one, while the intermediate event has vanishing total probability, which proves weak convergence. The extreme pair alone contributes \(n^2/4+o(n^2)\) to the variance; the intermediate component contributes only \(O(n)\) in its total second moment after centering, hence the claimed variance limit. No finite enumeration is used for any infinite-family conclusion.

## Verification

Run `python3 verify.py` from the directory containing this file. The standard-library verifier independently implements legal topplings and Dhar burning, compares that burning test with (1) for **every stable state** on \(K_{2,n}\) for each \(2\le n\le10\), and enumerates all recurrent single-grain additions to each of the two driving classes. Every coefficient matches both stated polynomials. Additional integer-only coefficient, normalization, mean and extreme-event tests cover \(2\le n\le512\). The run reports `SANDPILE_TWO_HUB_CHECKS_PASSED finite_n=2..10 formulas_n=2..512`. Finite tests are implementation cross-checks, not substitutes for Steps 1–4.

## Relationship to prior work

Dhar's burning criterion and the uniform recurrent sandpile measure are standard. Dukes and Le Borgne classify recurrent configurations on general complete bipartite graphs using decorated polyominoes; their general recurrent-state framework covers the setting of Step 1, which is not claimed as independently novel. Aval, D'Adderio, Dukes and Le Borgne study further operators and cyclic-lemma bijections, not the complete fixed-source burst law. Austin and collaborators establish the general one-toppling bound for a drive adjacent to the sink and calculate avalanche polynomials on trees, cycles, wheels and complete graphs, not the present complete bipartite source-resolved formulas. Selig and Zhu later classify deterministic and stochastic recurrent configurations on complete bipartite graphs; the examined manuscript does not provide this avalanche-size law.

The published result *Full-system Abelian sandpile avalanches on complete bipartite graphs: a deletion-tree law and a rare-event activity fraction* already gives the maximum-event count for a driven hub (the adjacent-to-sink source) in the present family. That known maximal coefficient is duly excluded from the novelty claim. Its theorem does **not** determine the remaining binomial spectrum or the nonadjacent-to-sink leaf-driven polynomial with a double-toppling maximum. The published *Two macroscopic avalanche bands on a three-hub bipartite sandpile* studies \(K_{3,n}\) with the sink and driver in its three-vertex part; neither its source class nor its three-hub spectrum implies the present two-hub results. The new claim is the pair of complete polynomials, the exactly \(1/n\) intermediate binomial component and the resulting all-or-none limit, not isolated recurrence, burning or full-system coefficients.

## Limitations

The result concerns the stationary recurrent ensemble for a finite, unweighted simple graph \(K_{2,n}\), a single fixed sink in its \(n\)-vertex part, and a single added grain at one of two nonsink source types. It does not describe other complete bipartite ratios, nonuniform edges, different sink placement as an independent geometry, stochastic toppling rules, a mixing-time theorem, or any universal power law on spatial lattices. The weak limit is a two-point distribution, not evidence of self-organized scale-free criticality. Historical originality is based on examined literature and searchable published records, not an exhaustive certification, and no independent audit is claimed.

## References

1. P. Bak, C. Tang and K. Wiesenfeld, *Self-organized criticality: An explanation of the 1/f noise*, *Physical Review Letters* **59** (1987), 381–384, publicly published 1987-07-27, https://doi.org/10.1103/PhysRevLett.59.381.
2. M. Dukes and Y. Le Borgne, *Parallelogram polyominoes, the sandpile model on a complete bipartite graph, and a q,t-Narayana polynomial*, first public 2012-07-31, https://arxiv.org/abs/1208.0024.
3. J.-C. Aval, M. D'Adderio, M. Dukes and Y. Le Borgne, *Two operators on sandpile configurations, the sandpile model on the complete bipartite graph, and a Cyclic Lemma*, first public 2013-07-29, https://arxiv.org/abs/1307.7740.
4. D. Austin, M. Chambers, R. Funke, L. D. García Puente and L. Keough, *The Avalanche Polynomial of a Graph*, first public 2016-05-09, https://arxiv.org/abs/1605.02713.
5. T. Selig and H. Zhu, *Abelian and stochastic sandpile models on complete bipartite graphs*, first public 2024-09-18, https://arxiv.org/abs/2409.11811.
6. *Full-system Abelian sandpile avalanches on complete bipartite graphs: a deletion-tree law and a rare-event activity fraction*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-full-system-abelian-sandpile-avalanches-on-complete-bipartite-gr--c0b51f8711c3.
7. *Two macroscopic avalanche bands on a three-hub bipartite sandpile*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-two-macroscopic-avalanche-bands-on-a-three-hub-bipartite-sandpil--c0ce64f447b3.
