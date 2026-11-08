# Sharp Fibonacci overhead for universal cyclic covers of the golden-mean language

## Finding

Let \(F_1=F_2=1\) and \(F_{j+2}=F_{j+1}+F_j\). For every integer \(n\ge2\), the minimum length of a binary **cyclic** word with no cyclic adjacent \(11\) and containing all \(F_{n+2}\) **linearly** \(11\)-avoiding words of length \(n\) as cyclic factors is

\[
M_n=F_{n+2}+F_n-1=L_{n+1}-1.
\]

Moreover, there is an optimal covering word in which precisely the words \(0u0\), for nonzero \(11\)-avoiding \(u\) of length \(n-2\), occur twice, and every other required word occurs once. Therefore the exact excess above the trivial factor-count bound is \(F_n-1\).

## Assumptions and scope

A cyclic word of length \(m\) is a binary word \(w\) whose indices are interpreted modulo \(m\). A cyclic length-\(n\) window at index \(i\) is \(w_i w_{i+1}\cdots w_{i+n-1}\), using periodic indexing. The cyclic word is *admissible* if every cyclic adjacent pair differs from \(11\). Let \(\mathcal L_j\) be the set of ordinary linear length-\(j\) words that avoid adjacent \(11\), including the empty word for \(j=0\). **Linear admissibility of required factors is distinct from the stronger condition that each factor is admissible when individually repeated periodically.** In particular, \(101\in\mathcal L_3\), despite the periodic word \((101)^\infty\) having adjacent \(11\) across its period boundary. We ask for one admissible cyclic word in which every member of \(\mathcal L_n\) occurs at least once, allowing repeated factors. All quantifiers are over integer \(n\ge2\), with binary symbols exactly \(0,1\).

## Proof

**Required-factor count and overlap graph.** The standard end-symbol recurrence gives \(|\mathcal L_j|=F_{j+2}\). Define a directed graph \(G_n\) with vertex set \(\mathcal L_{n-1}\), and one directed edge for every \(x=x_1\cdots x_n\in\mathcal L_n\), from \(x_1\cdots x_{n-1}\) to \(x_2\cdots x_n\). The graph is strongly connected: append \(n-1\) zeros to reach \(0^{n-1}\) from any vertex and then append the desired vertex to reach it. Any admissible cyclic covering word is a closed walk using each mandatory edge at least once. Conversely, every closed walk covering these edges produces such a cyclic word.

**A sharp lower bound.** For a vertex \(v\) of length \(n-1\), set \(p(v)=0\) when \(v\) has no one, and otherwise take the one-based index of its **rightmost** one. For every admissible edge \(x\), shifting its prefix to its suffix decreases \(p\) by at most one. Indeed, when its final symbol is zero the rightmost one shifts left by at most one; when its final symbol is one, the new potential is \(n-1\).

Let \(D\) be the sum, over each of the \(|\mathcal L_n|\) mandatory edges exactly once, of the difference \(p(\text{tail})-p(\text{head})\). For any vertex \(v\) the base graph has

\[
\operatorname{outdeg}(v)-\operatorname{indeg}(v)=\mathbf1_{v_{n-1}=0}-\mathbf1_{v_1=0}.
\]

Thus, pairing each word beginning \(0\), ending \(1\) with its reversal (which begins \(1\), ends \(0\)), their combined contribution to \(D\) is the negative of the number of leading zeros in the former word. All other vertices contribute zero. For each integer \(j\) between \(1\) and \(n-2\), the number of such vertices with at least \(j\) leading zeros is \(F_{n-1-j}\): remove the forced leading zeros and count admissible words ending in one. Consequently

\[
D=-\sum_{j=1}^{n-2}F_{n-1-j}=-(F_n-1).
\]

The empty sum when \(n=2\) is zero, as required. Every covering closed walk uses every mandatory edge at least once; if it uses \(r\) further admissible edges, the total potential drop along the closed walk is zero. Each further edge has potential drop at most one, hence

\[
0=D+\sum_{\text{extra edges}}\bigl(p(\text{tail})-p(\text{head})\bigr)\le -(F_n-1)+r,
\]

so \(r\ge F_n-1\) and every covering cycle has length at least \(F_{n+2}+F_n-1\).

**An optimal covering cycle.** Add a second copy to each edge corresponding to \(0u0\), for every \(u\in\mathcal L_{n-2}\) except \(u=0^{n-2}\). There are exactly \(F_n-1\) extra copies. For each nonzero vertex \(v\), these copies increase its outgoing degree by \(\mathbf1_{v_1=0}\) and incoming degree by \(\mathbf1_{v_{n-1}=0}\); the allzero vertex receives no extra edge. The displayed degree imbalance is canceled at every vertex, and the augmented graph remains strongly connected. It is therefore Eulerian. Reading the last symbol of its successive edge labels on any Eulerian tour produces an admissible cyclic word whose length is precisely \(F_{n+2}+F_n-1\). Each mandatory factor occurs exactly once except for the specified \(F_n-1\) factors, which occur exactly twice. This meets the lower bound and proves the result for all \(n\ge2\).

## Verification

The standalone `verify.py` constructs the augmented graph, checks edge counts, all vertex balances, the potential inequality, the exact total mandatory potential drop, and the cyclic-window multiset of a Hierholzer tour for every \(2\le n\le12\). It reports `VERIFY_OK`. The separately implemented `construct.py` builds the tours by another graph routine and checks by exhaustive enumeration that no shorter admissible cycle works for \(2\le n\le5\); it reports `CONSTRUCT_OK`. As an additional non-embedded cross-check, integer min-cost circulation in the original constrained graph reproduced the minimal overhead at each \(2\le n\le10\). The arbitrary-length result follows from the proof, not extrapolation from finite verification.

Values of \(M_n\) for \(n=2,3,4,5,6,7,8,9,10\) are respectively \(3,6,10,17,28,46,75,122,198\).

## Relationship to prior work

Moreno and Matamala (2007) study lexicographically minimal de Bruijn cycles for restricted **periodic** languages; their Section 2.1 explicitly requires the infinite periodic repetition of each permitted factor to belong to the subshift. For the golden-mean condition, that changes the required factor set: at length three their periodic language has four factors, while the present linear factor set has five, including \(101\). Their “minimal” concerns lexicographic ordering of Eulerian tours, rather than the minimum number of repeated admissible edges needed to cover all linearly admissible words. Bernardini et al. (2022) give general algorithms for making de Bruijn graphs Eulerian, encompassing broad edge-augmentation problems but not this Fibonacci closed form or its explicit primal/dual witnesses. Cazaux and Rivals (2016) investigate shortest cyclic covers in general; the full text was not accessible for a decisive exhaustive comparison. The result here identifies the exact optimal augmentation for this specific constrained infinite family, rather than claiming originality of Eulerian augmentation as a method.

## Limitations

The theorem assumes exactly two symbols, the single forbidden adjacent pattern \(11\), **cyclic** admissibility of the covering word, linear admissibility of the required factors, and repeated factors being allowed. It does not classify all minimizers, cover other forbidden patterns, or imply a corresponding minimum for unconstrained covering words or linear superstrings. The full text of Cazaux and Rivals (2016) was unavailable for complete historical-priority comparison, so an independent literature audit remains appropriate.

## References

1. Eduardo Moreno and Martín Matamala, *Minimum de Bruijn Sequence in a Language with Forbidden Substrings* (arXiv:0711.1695, version posted 2007-11-12), especially Sections 1–3, https://arxiv.org/abs/0711.1695 .
2. Giulia Bernardini, Huiping Chen, Grigorios Loukides, Solon P. Pissis, Leen Stougie, and Michelle Sweering, *Making de Bruijn Graphs Eulerian*, CPM 2022, DOI:10.4230/LIPIcs.CPM.2022.12, especially Sections 1–2, https://doi.org/10.4230/LIPIcs.CPM.2022.12 .
3. Bastien Cazaux and Eric Rivals, *A linear time algorithm for shortest cyclic cover of strings*, Journal of Discrete Algorithms 37 (2016), 56–67, DOI:10.1016/j.jda.2016.05.001. Full text unavailable at time of comparison.
