# Forced-colouring polynomials of clique-bouquet windmills

## Finding
For integers \(k\ge 2\) and \(m\ge 3\), let \(W_{k,m}\) be the graph obtained from \(k\) copies of \(K_m\) by identifying precisely one common vertex \(c\), with no other intersections or edges. Equivalently, \(W_{k,m}=K_1\vee(k K_{m-1})\). Its order is \(N=1+k(m-1)\), and its chromatic number is \(m\).

Use Farr's locally forced colouring rule with exactly \(m\) named colours: an initially uncoloured vertex acquires its unique missing colour when its coloured neighbours exhibit precisely \(m-1\) distinct colours. For a successful partial colouring, let \(j\) be the number of vertices initially uncoloured. The polynomial \(B_{k,m}(t)\) counting successful labelled partial colourings by \(j\) is
\[
\boxed{B_{k,m}(t)=m((m-1)!)^k\left[(1+t)(1+(m-1)t)^k-(m-1)t^{k+1}\right].}
\]

Equivalently, in Farr's probability model each of the \(m\) colours occurs independently at a vertex with probability \(p\), and the vertex remains uncoloured with probability \(r=1-mp\). For \(0\le p\le 1/m\), the forced-colouring probability polynomial is
\[
\boxed{\operatorname{FC}_m(W_{k,m};p)=m((m-1)!)^k p^{k(m-2)}\left[(p+r)(p+(m-1)r)^k-(m-1)r^{k+1}\right].}
\]

A partial assignment succeeds if and only if it is a restriction of a proper total \(m\)-colouring, at most one noncentral vertex per clique is initially uncoloured, and, if \(c\) is initially uncoloured, at least one of the \(m-1\) noncentral colours occurs among the initially coloured peripheral vertices for each of the \(m-1\) colours (equivalently, the omitted peripheral colours are not all the same across the \(k\) cliques).

In particular, the minimum number of initially coloured vertices needed for local forcing is exactly \(k(m-2)\). The number of such minimum-domain partial colourings is
\[
\boxed{m((m-1)!)^k\left[(m-1)^k-(m-1)\right].}
\]
The one-clique case \(k=1\) is the already-known complete-graph boundary and is not presented as new.

## Assumptions and scope
Graphs are finite, simple and undirected. The cliques have equal order \(m\ge3\), meet only at their common centre \(c\), and there are \(k\ge2\) petals. The palette has exactly \(m\) labelled colours, the graph's chromatic number. An initial partial assignment is successful only if repeated applications of the local rule produce a *proper* complete colouring. We do not identify success with mere unique extendability, nor with the different zero-forcing colour-change rule. The indeterminate \(t\) in \(B_{k,m}\) counts initially uncoloured vertices, not initially coloured vertices.

## Proof
**1. Unique total extension.** Every proper complete \(m\)-colouring of \(W_{k,m}\) uses one colour at the centre and, for each petal, uses the other \(m-1\) colours bijectively on its \(m-1\) peripheral vertices. Thus the number of total colourings is \(A=m((m-1)!)^k\). If an initial partial assignment can be completed by successive local forcing steps, every forced colour is uniquely determined at its step, so its entire completed proper colouring is uniquely determined. Consequently, it is legitimate to fix each of the \(A\) total colourings, count its successful restrictions, and sum without duplication.

**2. Necessary peripheral bound.** Fix one of those proper colourings. If at least two peripheral vertices of a petal start uncoloured, neither can ever be the first of those two to be forced. A peripheral vertex sees only the centre and the other \(m-2\) peripherals in its petal. With its partner still uncoloured, at most \(m-2\) different coloured-neighbour colours are possible, even if the centre is eventually coloured. Thus success requires at most one initially uncoloured peripheral per petal.

**3. Initially coloured centre.** If the centre is initially coloured and each petal has at most one peripheral blank, then any blank has its \(m-1\) neighbours coloured in all remaining \(m-1\) distinct colours and forces immediately. For each petal we may omit no peripheral (weight \(1\)) or any one of its \(m-1\) peripheral vertices (weight \((m-1)t\)). This contributes \((1+(m-1)t)^k\) successful restrictions of each fixed total colouring.

**4. Initially uncoloured centre.** If the centre is initially blank, initially uncoloured peripheral vertices cannot force before the centre: each has no coloured centre and sees at most \(m-2\) distinct colours among its peripheral neighbours. Therefore the first possible forcing step must colour the centre. The centre can force if and only if all \(m-1\) colours different from its eventual colour already occur on coloured peripheral vertices. Under the bound of Step 2, a colour is absent from the coloured periphery precisely when *every petal* omits its single vertex with that colour. There are exactly \(m-1\) such obstruction patterns, each leaving one peripheral blank in all \(k\) petals, of weight \(t^k\). All other patterns first force the centre and then every remaining single peripheral blank. Their contribution is \(t[(1+(m-1)t)^k-(m-1)t^k]\), where the leading \(t\) marks the initially blank centre.

**5. Enumeration.** Adding Steps 3 and 4 gives \(B_{k,m}(t)/A\). Every term represents a unique initial restriction and hence has multiplicity one among labelled assignments. To obtain the probability polynomial, replace each initially coloured vertex by weight \(p\) and each blank vertex by weight \(r\). Since there are \(k(m-2)\) peripheral vertices certainly initially coloured across all petals, the two cases respectively contribute
\[
A p^{k(m-2)}p(p+(m-1)r)^k\quad\text{and}\quad A p^{k(m-2)}r\left[(p+(m-1)r)^k-(m-1)r^k\right].
\]
Their sum is the displayed formula.

**6. Minimum seed cardinality and multiplicity.** Any successful restriction omits at most \(k+1\) vertices, by Step 2. The coefficient of \(t^{k+1}\) in \(B_{k,m}(t)/A\) equals \((m-1)^k-(m-1)\), which is strictly positive for \(k\ge2,m\ge3\). Hence some successful restrictions omit \(k+1\) vertices, so their minimum seed cardinality is \(N-(k+1)=k(m-2)\). Multiplication by \(A\) gives the stated count.

## Verification
The accompanying Python program `verify.py` constructs the graph directly and implements the simultaneous iterative local-colouring rule on actual partial colourings, independently testing the characterized success condition and every polynomial coefficient for \((m,k)=(3,1),(3,2),(3,3),(3,4),(4,1),(4,2),(5,1)\). It also enumerates *all* \((m+1)^N\) possible named partial assignments for five small parameter pairs, without assuming the existence of a proper total-colouring extension. Its recorded output in `verify_output.txt` ends with `VERIFY_OK`.

The \(k=1\) test checks consistency with the previously known complete-graph boundary; the theorem being claimed is for \(k\ge2\). These finite tests corroborate the structural proof; they do not establish the statement for unbounded parameters.

## Relationship to prior work
Farr's *The forced colouring function of a graph* (first public version 15 September 2026, arXiv:2609.17108v1) gives the precise local rule, the generating framework, elementary complete-graph examples and general complexity results, but its inspected definitions, propositions and examples do not give this bouquet formula. Farr and Morgan (2024) introduce the underlying colouring-probability model and a general recurrence using labelled graphs, but such a recursive expression does not supply the above explicit two-parameter closed form or the global omitted-colour obstruction.

Previously published explicit formulas for \(\operatorname{FC}_3\) on paths and cycles concern graphs of maximum degree at most two. The full chromatic-palette polynomial of complete multipartite graphs concerns a different graph class: these bouquets contain disjoint peripheral cliques and, with at least two petals, are not complete multipartite. The known \(\operatorname{FC}_3\) expression for complete bipartite graphs is similarly inapplicable because our graphs contain triangles. The exact zero-forcing polynomial of friendship graphs concerns the different rule “one blue vertex with exactly one white neighbour” and counts uncoloured/coloured sets without arbitrary named proper colour assignments; its formula does not imply this one.

## Limitations
The proof requires equally sized cliques meeting at one common vertex and a palette of exactly \(m\) colours. It does not classify colour-forcing probabilities for unequal clique bouquets, excess palettes or general chordal graphs. The literature search, including repository full text for the closest formulas, cannot exclude a differently indexed equivalent theorem. No independent mathematical audit has been carried out.

## References
1. G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108v1 (first submitted 15 September 2026), https://arxiv.org/abs/2609.17108.
2. G. Farr and K. Morgan, *Graph polynomials: some questions on the edge*, arXiv:2406.15746v1 (22 June 2024), Sections 3.5 and 5.4, https://arxiv.org/abs/2406.15746.
3. *Forced colourings of complete multipartite graphs at the chromatic palette size*, public record dated 4 October 2026, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-forced-colourings-of-complete-multipartite-graphs-at-the-chromat--ab08eebc2655.
4. *Exact forced 3-colouring polynomials at maximum degree two*, public record dated 17 September 2026, https://github.com/Resultary/2026/tree/main/2026/9/17/SCOPE-forced-three-colouring-max-degree-two--2226d8f07ffd.
5. *Forced three-colouring polynomial of complete bipartite graphs*, public record dated 4 October 2026, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-forced-three-colouring-polynomial-of-complete-bipartite-graphs--3fb93c858f69.
6. *Zero forcing polynomial of friendship graphs*, public record dated 4 October 2026, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-zero-forcing-polynomial-of-friendship-graphs--b77605779c1b.
