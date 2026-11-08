# Forced colouring with one surplus colour on complete multipartite graphs

## Finding
Let \(r\ge3\) be an integer, and let \(G=K_{n_1,\ldots,n_r}\) be a finite simple complete multipartite graph whose labelled partite sets \(V_i\) are all nonempty, with \(|V_i|=n_i\). There are \(\lambda=r+1\) named available colours. An uncoloured vertex is *locally forced* when its already-coloured neighbours display precisely \(\lambda-1=r\) distinct colours; it then receives the unique missing colour. A partial assignment is *forcing* if iterative local forcing produces a proper total colouring.

The full polynomial of forcing partial assignments, weighted by initial domain size, is
\[
 F_{r+1}(G;z)=(r+1)!z^N+\frac{(r+1)!}{2}\sum_{j=1}^{r}(2^{n_j}-2)z^{n_j}\left(\prod_{i\ne j}A_i(z)+\sum_{k\ne j}\prod_{i\notin\{j,k\}}A_i(z)\right),
 \qquad A_i(z)=(1+z)^{n_i}-1,\quad N=\sum_{i=1}^{r}n_i.
\]
Empty products are \(1\). The coefficient of \(z^d\) is the exact number of forcing partial assignments with \(d\) initially coloured vertices.

A forcing assignment has exactly one of the following disjoint forms:

1. It is a *total* proper colouring in which every part is monochromatic (thus exactly \(r\) of the \(r+1\) available colours occur).
2. A unique part \(V_j\) is fully coloured initially and uses exactly two colours, both occurring. All other initially coloured vertices in each part \(V_i\) use the unique monochromatic colour assigned to that part; these part colours are pairwise distinct and differ from the two colours in \(V_j\). At most one of the other \(r-1\) parts is wholly uncoloured initially.

For the probability form of the forced-colouring polynomial, let each specified colour occur independently at each vertex with probability \(p\), and let a vertex be uncoloured with probability \(q=1-(r+1)p\), where \(0\le p\le 1/(r+1)\). Put
\[
 B_i(p)=(p+q)^{n_i}-q^{n_i}=(1-rp)^{n_i}-q^{n_i}.
\]
Then
\[
 \operatorname{FC}_{r+1}(G;p)=(r+1)!p^N+\frac{(r+1)!}{2}\sum_{j=1}^{r}(2^{n_j}-2)p^{n_j}\left(\prod_{i\ne j} B_i(p)+\sum_{k\ne j}q^{n_k}\prod_{i\notin\{j,k\}}B_i(p)\right).
\]
These are polynomial identities, including at the endpoint \(q=0\).

If every part is a singleton, the minimum initial forcing domain size is \(r\), with \((r+1)!\) minimum assignments. Otherwise let \(s=\min\{n_j:n_j\ge2\}\). The smallest forcing domain has size
\[
 \sigma_{r+1}(G)=s+r-2,
\]
and the exact number of labelled forcing assignments at this minimum size is
\[
 \frac{(r+1)!}{2}(2^s-2)
 \sum_{j:n_j=s}\ \sum_{k\ne j}\prod_{i\notin\{j,k\}}n_i.
\]
The formula identifies a sharp palette-surplus effect: at the chromatic palette size \(r\), the smallest forcing domain has size \(r-1\), whereas adding one available colour raises it to \(s+r-2\) whenever a nonsingleton part exists.

For example, for \(G=K_{2,2,2}\) and four colours,
\[
 F_4(G;z)=288z^3+432z^4+288z^5+96z^6.
\]
Thus exactly \(288\) partial assignments of three initially coloured vertices force a proper four-colouring, and none with fewer vertices can do so.

## Assumptions and scope
The graph is finite, simple and complete multipartite, with \(r\ge3\) nonempty **distinguishable vertex parts** and labelled vertices. Colours are named, not identified up to permutation. The forcing rule is the unique-missing-colour local rule in Farr's 2026 forced-colouring function, not the zero-forcing colour-change rule or a mere unique-extension test. A partial assignment counted here must ultimately extend to a proper colouring. Arbitrary nonnegative part sizes are not allowed: each \(n_i\ge1\). No uniform-part-size assumption is made.

## Proof
**Colour-capacity dichotomy.** In any proper total colouring of a complete \(r\)-partite graph, colours occurring in different parts are disjoint because every pair of vertices in different parts is adjacent. Every part uses at least one colour. With just \(r+1\) available colours, either each part is monochromatic, with exactly \(r\) colours used, or exactly one part is bichromatic and every other part is monochromatic, with all \(r+1\) colours used. No other proper total colouring type is possible.

**Necessity in the all-monochromatic type.** A non-total restriction of an all-monochromatic proper colouring cannot force its first new vertex: an uncoloured vertex in any part sees at most one colour per other part, hence at most \(r-1\) distinct colours, strictly below the required \(r\). Therefore only the total assignment is forcing in this type.

**Necessity in the bichromatic type.** Fix the unique bichromatic part \(V_j\). A vertex in \(V_j\) sees only colours from the other \(r-1\) monochromatic parts; even after arbitrary legitimate forcing elsewhere, it can see at most \(r-1\) distinct colours. Consequently **every vertex in \(V_j\) must be coloured initially**. Both colours of \(V_j\) therefore occur initially. If the initial assignment is not total, consider its first forced vertex. It lies in some monochromatic part \(V_k\), and its neighbours can display the necessary \(r\) distinct colours only when both colours of \(V_j\) and the distinct monochromatic colours of every other \(r-2\) part are already represented. No other vertex has yet been forced. Hence every part other than \(V_j,V_k\) is initially seeded, so at most one of the \(r-1\) monochromatic parts was initially unseeded. The same condition is automatic for a total assignment.

**Sufficiency.** Suppose \(V_j\) is fully coloured and bichromatic, and all but at most one other part are seeded with their respective distinct final colours. If one monochromatic part \(V_k\) is unseeded, each of its vertices sees the two colours of \(V_j\) and the \(r-2\) other monochromatic colours, a total of exactly \(r\), so every vertex in \(V_k\) is forced to its missing colour. Now all parts are seeded. For any still-uncoloured vertex of any monochromatic part, its neighbours exhibit the two colours of \(V_j\) and one colour from each of the other \(r-2\) monochromatic parts; it is forced. This yields a proper total colouring, proving the structural classification.

**Enumeration.** Total monochromatic proper colourings use \(r\) distinct named colours from \(r+1\), giving \((r+1)!\) assignments of weight \(z^N\). In the bichromatic case choose the two-colour subset assigned to \(V_j\), and distinct colours for the other \(r-1\) parts. The number of such allocations is \((r+1)!/2\). The fully coloured part \(V_j\) receives a surjective assignment of its two colours in \(2^{n_j}-2\) ways, with domain weight \(z^{n_j}\). For each other part \(V_i\), a nonempty initially coloured subset contributes \(A_i(z)=(1+z)^{n_i}-1\). Either all these parts are seeded or exactly one part \(V_k\) is unseeded. Their disjoint contributions are the displayed product and sum of products. Every partial assignment of this kind forces a **unique** proper total colouring: the two colours on \(V_j\) and the seeded monochromatic colours determine the colour of the at most one entirely unseeded part. There is no double counting, giving the domain-size formula.

For the probability version, a vertex initially blank contributes \(q\), while one receiving the specified monochromatic colour contributes \(p\). A nonempty seeded part \(V_i\) therefore contributes \((p+q)^{n_i}-q^{n_i}=B_i(p)\), while an unseeded part contributes \(q^{n_i}\). The bichromatic part is fully assigned and contributes \(p^{n_j}\) per surjective two-colour assignment. Summation gives \(\operatorname{FC}_{r+1}(G;p)\), including the endpoint by direct polynomial evaluation.

**Minimum domains and their multiplicity.** If every part is a singleton, the graph is complete and has maximum degree \(r-1<r\), so no vertex can be forced; only total proper assignments count, giving \(\sigma_{r+1}=r\) and \((r+1)!\) minimizers. Otherwise let \(s\) be the smallest nonsingleton part size. In the bichromatic type, \(n_j\) vertices of \(V_j\) must be seeded and at least one vertex of each of \(r-2\) other parts must be seeded. This costs at least \(n_j+r-2\ge s+r-2\), attained by making a part of size \(s\) bichromatic, choosing exactly one other part to leave unseeded, and seeding exactly one vertex in each of the remaining \(r-2\) parts. Since \(N\ge s+r-1\), this beats all total initial assignments. The number of minimizers follows by choosing the part \(j\) of size \(s\), the unseeded part \(k\), an individual seeded vertex from each remaining part, a two-colour surjection on \(V_j\), and the named colour allocation. These choices are disjoint and exhaust all minimizers.

## Verification
Run `python3 verify.py` using Python 3 standard library only. The verifier constructs each labelled complete multipartite graph from its part-size vector, enumerates **every** initial assignment with the available colours plus a blank state, rejects improper initial assignments, repeatedly applies the local unique-missing-colour rule, and counts the forcing assignments by domain size. It computes the proposed polynomial separately by ordinary coefficient arithmetic and compares the entire coefficient vectors.

The script checks 14 multipartite profiles, including nonsingleton and all-singleton boundaries, unequal parts, three, four and five parts, and sizes through seven vertices. Its final output is `ALL_PROFILES_OK 14`. The unrestricted result is proved by the structural argument above; exhaustive finite tests are corroboration, not an infinite proof.

## Relationship to prior work
Farr and Morgan introduced the forced-colouring framework in *Graph polynomials: some questions on the edge* (arXiv:2406.15746v1), including its reduction-based treatment. Farr's *The forced colouring function of a graph* (arXiv:2609.17108v1, September 2026) develops the probability function, small graph examples, a bipartite formula when exactly two colours are available, and general computational hardness. It does not state the present first-surplus-palette formula for general complete multipartite graphs.

Two earlier published research records are especially close. *Forced colourings of complete multipartite graphs at the chromatic palette size* determines the exact polynomial for \(r\) colours on complete \(r\)-partite graphs; its central condition is that at least \(r-1\) parts be initially seeded, and it explicitly does not cover a palette larger than \(r\). *Forced three-colouring polynomial of complete bipartite graphs* treats the special case of two parts and three colours. The present statement concerns at least three parts with \(r+1\) colours; neither record implies its classification or enumeration for those graphs.

The 2019 paper *Multi-color forcing in graphs* by Bozeman and coauthors instead studies directed colour-change networks on already-coloured graphs, with colour propagation between adjacent vertices. That process is distinct from forcing uncoloured vertices to the unique missing colour in a proper graph colouring.

## Limitations
The theorem concerns the single surplus-colour regime \(\lambda=\chi(G)+1\) for complete multipartite graphs with at least three parts. It does not evaluate the forced-colouring polynomial for larger palette surpluses, or for general graphs. The minimum-domain result concerns the local forcing rule, not unique extension without local steps. Novelty comparisons were made against the cited primary papers and accessible published research records, but unindexed parallel work remains a residual historical-priority risk. Independent mathematical validation has not been performed.

## References
1. G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108v1 (first submitted 2026-09-15), https://arxiv.org/abs/2609.17108.
2. G. E. Farr and K. Morgan, *Graph polynomials: some questions on the edge*, arXiv:2406.15746v1 (2024), https://arxiv.org/abs/2406.15746.
3. *Forced colourings of complete multipartite graphs at the chromatic palette size*, published research record, 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-forced-colourings-of-complete-multipartite-graphs-at-the-chromat--ab08eebc2655.
4. *Forced three-colouring polynomial of complete bipartite graphs*, published research record, 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-forced-three-colouring-polynomial-of-complete-bipartite-graphs--3fb93c858f69.
5. C. Bozeman, P. E. Harris, N. Jain, B. Young, T. Yu, *Multi-color forcing in graphs*, arXiv:1912.02001v1 (2019), https://arxiv.org/abs/1912.02001.
