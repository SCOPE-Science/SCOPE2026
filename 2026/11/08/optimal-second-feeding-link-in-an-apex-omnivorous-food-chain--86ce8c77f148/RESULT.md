# Optimal second feeding link in an apex-omnivorous food chain

## Finding

For every integer \(n\ge4\), take a unit-link food chain on species \(0,1,\ldots,n-1\), with prey-to-consumer links \(i\to i+1\), and one pre-existing omnivory link \(0\to n-1\). Add exactly one distinct *forward* feeding link \(i\to j\) with \(i<j\) that is not already present. Under the usual prey-average trophic levels and the standard squared trophic-incoherence index \(q^2\), the globally optimal link is always to a non-apex consumer, and is characterized by

\[
 j-i-1=h_n=\left\lfloor\frac{2n-2}{5}\right\rfloor,\qquad
 0\le i\le n-3-h_n.
\]

Thus **all** optimal links skip the same number of species, have the same cost irrespective of their position along the chain, and no link directly into the apex is optimal. The exact minimum is

\[
 q_{\min}^2=\frac{h_n^2+\bigl(n-2-h_n/2\bigr)^2}{2(n+1)}.
\]

The original incoherence is \(q_0^2=(n-2)^2/(2n)\), and \(q_{\min}^2<q_0^2\) for all \(n\ge4\). Moreover

\[
 \lim_{n\to\infty}\frac{h_n}{n}=\frac25,\qquad
 \lim_{n\to\infty}\frac{q_{\min}^2}{q_0^2}=\frac45.
\]

For the smallest eligible chain, \(n=4\), adding \(0\to2\) decreases \(q^2\) from \(1/2\) to \(13/40\), despite adding a new long-range trophic interaction.

## Assumptions and scope

Every link \(a\to b\) points from a prey species to its consumer. The web is a simple, unweighted, directed acyclic graph; the original links are precisely \((a,a+1)\) for \(0\le a<n-1\) and \((0,n-1)\). The basal species is vertex \(0\); every other species is reachable from it. The additional link must respect the same strict feeding order, \(0\le i<j<n\), and cannot duplicate an existing link. Reverse links, cannibalism, changes of link weights, deletions, and multiple simultaneously added links are *not* considered.

For any such graph \(G\), define trophic levels by \(s_0=1\) and

\[
 s_v=1+\frac{1}{|N^-(v)|}\sum_{u\in N^-(v)}s_u\quad(v\ge1),
\]

where \(N^-(v)\) denotes the prey of consumer \(v\). For every edge \(u\to v\), its trophic distance is \(s_v-s_u\). Set

\[
 q(G)^2=\frac{1}{|E(G)|}\sum_{u\to v\in E(G)}(s_v-s_u-1)^2.
\]

This equals the usual variance of trophic distances because their mean equals one. We optimize this purely structural index, **not** dynamical stability, species abundances, extinction risk, or empirical management outcomes.

## Proof

Write \(k=n-2\ge2\). In the original chain, the basal-to-apex link and the final chain link have trophic deviations \(+k/2\) and \(-k/2\), respectively; all other links have deviation zero. There are \(n\) links, so \(q_0^2=k^2/(2n)\).

Every missing forward link falls into one of two exhaustive classes.

**Case 1: a new link ends before the apex.** Let \(i\to j\) have \(j\le n-2\), and put \(h=j-i-1\). Then \(1\le h\le k-1\). The trophic levels through \(j-1\) remain the original levels. At \(j\), adding a second prey changes its level from \(j+1\) to \(j+1-h/2\). This shift \(-h/2\) persists to \(n-2\) along the chain; the apex, which averages levels of \(0\) and \(n-2\), shifts by \(-h/4\). Exactly four edges have nonzero trophic deviations: the two into \(j\) have deviations \(\pm h/2\), while the two into the apex have deviations \(\pm(k/2-h/4)\). Since the enlarged network has \(n+1\) links,

\[
 q_{\mathrm{int}}^2(h)=\frac{h^2+(k-h/2)^2}{2(n+1)}.
\]

Every integer \(1\le h\le k-1\) occurs, and for a given \(h\) exactly \(k-h\) links realize it: \(i\to i+h+1\), for \(0\le i\le k-h-1\). Completing the square gives

\[
 h^2+(k-h/2)^2=\frac54\left(h-\frac{2k}{5}\right)^2+\frac45k^2.
\]

The unique closest integer to \(2k/5\) is \(h_n=\lfloor(2k+2)/5\rfloor\); no half-integer tie is possible, since \(2k/5=m+1/2\) would imply the even integer \(4k\) equals the odd integer \(10m+5\). For \(k=2\), \(h_n=1\), and for \(k\ge3\) it lies in \([1,k-1]\). Hence \(h_n\) is the unique optimal span in Case 1.

**Case 2: a new link ends at the apex.** The new edge is \(i\to n-1\) for \(1\le i\le k-1\). The apex now averages three prey levels. Its three incoming edges have respective deviations \((k+i)/3\), \((k-2i)/3\), and \((i-2k)/3\). All others have zero deviation. Consequently,

\[
 q_{\mathrm{apex}}^2(i)=\frac{2(k^2-ki+i^2)}{3(n+1)}
 \ge \frac{k^2}{2(n+1)},
\]

where the inequality follows by completing the square in \(i\).

Since \(h_n\) is within \(1/2\) of \(2k/5\), the best Case 1 value obeys

\[
 q_{\mathrm{int}}^2(h_n)\le\frac{(4/5)k^2+5/16}{2(n+1)}
 <\frac{k^2}{2(n+1)}
 \le q_{\mathrm{apex}}^2(i).
\]

The strict middle inequality holds because \(k\ge2\). Therefore no apex-targeting edge can be optimal, proving the classification.

For strict improvement over the original graph, the feasible Case 1 edge with \(h=1\) already gives

\[
 q_0^2-q_{\mathrm{int}}^2(1)
 =\frac{k^2+n(k-5/4)}{2n(n+1)}>0.
\]

Finally \(h_n=2k/5+O(1)\). Substitution into the completed square shows \(q_{\min}^2=(2/5)k^2/(n+1)+O(1/n)\), while \(q_0^2=k^2/(2n)\). The displayed limits follow. This finishes the proof for every integer \(n\ge4\).

## Verification

The included Python 3 script `verify.py` independently computes trophic levels and \(q^2\) directly from their definitions using exact rational arithmetic. For every \(n\in\{4,5,\ldots,32\}\), it enumerates **every** missing forward link, compares the direct value against the relevant closed formula, confirms that the complete minimizing set equals the theorem's links, and verifies strict improvement. This checks 4,930 link configurations, 29 network sizes, and 278 exact optimizing links. It is a finite reproducibility test, not the proof for all \(n\); the proof is above.

Run from a directory containing the standalone artifact with `python3 verify.py`. It has no external dependencies. The program reports the exact example \(1/2\to13/40\) for \(n=4\).

## Relationship to prior work

Johnson, Domínguez-García, Donetti, and Muñoz (2014) introduce the trophic-coherence index and study its relationship with stability in food webs, including a preferential preying generative model; their main text and accessible supporting material do not establish an all-length optimal single-link *repair* of a chain already containing apex omnivory. Klaise and Johnson (2016 preprint; 2017 journal article) analyze food-web motif families and the relationship between omnivory and coherence; their inspected main text uses a stochastic link-generation model rather than minimizing the recalculated incoherence over all available edges. The present classification uses the same established index but solves a different deterministic optimization problem.

The statement also differs from using a distinct alternative trophic-level convention that minimizes an edge-energy functional, as in later work on directed-network non-normality: here levels are specifically the **prey-averaging** levels and the standardized index of the 2014 paper. No claim is made that this is the first possible analysis of structural food-web coherence, and independent historical priority review has not been performed.

## Limitations

This theorem applies to one prescribed family of acyclic, unweighted food webs with one pre-existing basal-to-apex omnivory edge, **only one additional forward link**, and one basal species. It is not a classification of all food webs or all intervention models. Lower \(q\) is not by itself a proof of greater biological stability or biodiversity. The literature search could not exhaust unpublished manuscripts, all theses, or every future and past specialization; an equivalent statement could exist outside the inspected sources. The algebraic proof is exact, but the accompanying tests only cover \(4\le n\le32\).

## References

1. Johnson, S., Domínguez-García, V., Donetti, L., and Muñoz, M. A., *Trophic coherence determines food-web stability*, PNAS **111** (2014), 17923–17928, doi:10.1073/pnas.1409077111; first preprint arXiv:1404.7728 (2014-04-30). https://www.pnas.org/doi/10.1073/pnas.1409077111
2. Klaise, J., and Johnson, S., *The origin of motif families in food webs*, Scientific Reports **7** (2017), 16197, doi:10.1038/s41598-017-15496-1; preprint arXiv:1609.04318 (2016-09-14). https://www.nature.com/articles/s41598-017-15496-1
3. Drysdale, C., and Johnson, S., *The connection between non-normality and trophic coherence in directed graphs*, Frontiers in Applied Mathematics and Statistics **10** (article dated 2025-01-07). https://www.frontiersin.org/journals/applied-mathematics-and-statistics/articles/10.3389/fams.2024.1512865/full
