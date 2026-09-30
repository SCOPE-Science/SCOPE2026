# Independent Audit — 2026/09/11/085

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `f11ce2889d0d9b0f71b42c90c6a0f3afca714140`
- Disposition: **FAILED**

## Correctness

**PASS** — The counting argument is correct. Recomputing the integers gives N=C(4096,2)=8,386,560, the integer edge cap floor(0.52N)=4,361,011, hence every complement has at least 4,025,549 edges. A graph on 4096 vertices with r components has at most C(4096-r+1,2) edges; C(2837,2)=4,022,866<4,025,549, so r<=1259. A container can therefore cover at most 2^(r-1)<=2^1258 unordered balanced cuts, while there are C(4096,2048)/2>=2^4095/4097 such complete bipartite test graphs. Thus |C|>=2^2837/4097 and ln|C|>=1958.1405>26.2144. The book-free implication is also sound because each balanced complete bipartite graph is triangle-free.

## Originality

**FAIL** — The fixed-parameter lower bound is obtained by combining standard triangle-free balanced bipartite test graphs with the elementary extremal fact that, for a fixed number of connected components, all missing edges are maximized by one clique plus isolates. The parameter choices n=4096, defect 0.02 and B_2(64) do not introduce a new container mechanism: the proof in fact uses no property of the 64-page book beyond containing a triangle. Standard container literature already treats the genuinely structural part of the subject; this record is a numerical specialization of a one-paragraph covering count rather than a new theorem about containers.

## Scientific value

**FAIL** — The lower bound is mathematically valid but scientifically weak. It is only exp(O(n)) at one fixed n and edge cap, while container theory studies asymptotic families and much finer structural/counting behavior. The argument neither improves a container theorem, identifies a sharp transition, nor uses the book parameter in a meaningful way. The claimed relevance to an R(4,t) container-versus-induction tradeoff is not supported by a theorem connecting this fixed calculation to that program.

## Limitations

- The originality failure is not a claim that an identical numerical lower bound has previously been printed; it is a judgment that the fixed calculation is an immediate elementary specialization of standard facts.
- No claim is made about the optimal minimum number of containers at this edge cap.

## Sources

- The method of hypergraph containers — József Balogh; Robert Morris; Wojciech Samotij: https://arxiv.org/abs/1801.04584 — Survey of the structural container method and triangle-free applications; useful baseline for distinguishing a container theorem from a fixed covering count.
- An efficient container lemma — József Balogh; Wojciech Samotij: https://arxiv.org/abs/1910.09208 — Representative modern container theorem improving container-family bounds; the audited record does not alter this machinery.

The record was audited independently. GitHub was read only as evidence; no repository write was performed in this chat.
