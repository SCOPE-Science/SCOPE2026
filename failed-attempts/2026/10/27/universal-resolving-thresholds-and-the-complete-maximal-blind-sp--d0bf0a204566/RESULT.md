# Universal resolving thresholds and the complete maximal-blind-spot census in Hamming graphs

## Finding

For integers \(d\ge1\), \(q\ge2\), the Hamming graph \(H(d,q)=K_q^{\square d}\) has vertex set \([q]^d\), where \([q]=\{0,\ldots,q-1\}\). Its graph metric is Hamming distance. Define the *resolving number* \(\operatorname{res}(G)\) as the least integer \(t\) such that every subset of \(t\) vertices distinguishes all pairs of vertices by distances. For this entire graph family,

\[
\boxed{\operatorname{res}(H(d,q))=\begin{cases}
1,&q=2,\ d=1,\\
2^{d-1}+1,&q=2,\ d\ge2,\\
(q-2)q^{d-1}+1,&q\ge3.
\end{cases}}
\]

In addition, every *maximum-cardinality nonresolving set* is classified and counted. A landmark set \(S\) is nonresolving when at least one pair of distinct vertices has equal distances to every member of \(S\). All the largest such sets are the following exact coordinate families:

1. For \((d,q)=(1,2)\), just \(S=\varnothing\) (one set).
2. For \(q=2\), \(d\ge2\), the sets \(S=\{z\in[2]^d:z_i\oplus z_j=\epsilon\}\), where \(1\le i<j\le d\) and \(\epsilon\in[2]\). There are exactly \(2\binom d2\) sets.
3. For \(q=3\), either \(S=\{z\in[3]^d:z_i=a\}\), where \(i\in[d]\), \(a\in[3]\), or \(S=\{z\in[3]^d:z_j=\pi(z_i)\}\), where \(i<j\) and \(\pi\in\mathfrak S_3\). There are exactly \(3d+6\binom d2\) sets.
4. For \(q\ge4\), the sets \(S=\{z\in[q]^d:z_i\notin\{a,b\}\}\), where \(i\in[d]\) and \(\{a,b\}\subset[q]\) has size two. There are exactly \(d\binom q2\) sets.

Here \(\oplus\) is binary addition modulo two. The ternary alphabet is the unique transition case in which one-coordinate and two-coordinate obstructions both attain the maximum. This is a classification of *all* largest failing landmark configurations, not only a threshold value.

## Assumptions and scope

All graphs are finite, simple and connected. The integers \(d\) and \(q\) range independently over \(d\ge1\) and \(q\ge2\). Coordinate labels and symbols are fixed, so different displayed subsets are counted separately as labeled vertex subsets. A landmark set may be empty; that convention makes the two-vertex complete graph exception explicit. A resolving set is any subset \(S\subseteq V(G)\) for which
\[
\forall x,y\in V(G),\ x\ne y:\quad \exists z\in S\quad d(x,z)\ne d(y,z).
\]
The *metric dimension* asks for one smallest resolving set, whereas \(\operatorname{res}(G)\) is the uniform threshold for **every** set of that size; these parameters are distinct. Likewise, the equidistant dimension is a different existential covering invariant.

## Proof

**Step 1: Failure sets are contained in equal-distance fibers.** For distinct vertices \(x,y\), define the equalizer
\[
E(x,y)=\{z\in[q]^d:d(x,z)=d(y,z)\}.
\]
A landmark subset \(S\) fails to resolve precisely when \(S\subseteq E(x,y)\) for at least one unordered pair \(\{x,y\}\). Consequently
\[
\operatorname{res}(H(d,q))=1+\max_{x\ne y}|E(x,y)|.
\]
The equality is also the general relation of Garijo, González and Márquez, Proposition 2.1 of the cited work; the graph-family evaluation and full equality-case classification are established below.

**Step 2: Reduce the equalizer count to one parameter.** Suppose \(x\) and \(y\) differ in exactly \(r\) coordinates. In each such coordinate, the contribution of \(z\) to \(d(x,z)-d(y,z)\) is \(-1\) if \(z\) agrees with one endpoint, \(+1\) if it agrees with the other, and \(0\) for each of the remaining \(q-2\) symbols. In unchanged coordinates there are \(q\) unrestricted choices. Equality requires matching counts of the two nonzero contributions. Thus \(E(x,y)\) depends only on \(r\), with exact cardinality
\[
E_r=q^{d-r}\sum_{j=0}^{\lfloor r/2\rfloor}
\frac{r!}{j!\,j!\,(r-2j)!}(q-2)^{r-2j}
=q^{d-r}[t^0](t+t^{-1}+q-2)^r.
\]
Here the coefficient notation is for a Laurent polynomial; no asymptotic or extrapolation is involved. Every \(r\in\{1,\ldots,d\}\) is realized by some pair.

**Step 3: The binary case.** If \(q=2\), the zero contribution is unavailable in changed coordinates, so \(E_r=0\) for odd \(r\), while
\[
E_{2k}=2^{d-2k}\binom{2k}{k}=2^d\frac{\binom{2k}{k}}{4^k}.
\]
For \(k\ge1\), the ratio between successive central-binomial factors equals \((2k+1)/(2k+2)<1\). Hence, when \(d\ge2\), the largest equalizer has size \(E_2=2^{d-1}\), and **only** pairs at Hamming distance two attain it. When \(d=1\), the only pair has empty equalizer, so the largest failing set is empty and \(\operatorname{res}=1\).

**Step 4: The nonbinary case and the ternary tie.** Suppose \(q\ge3\). Put \(s=(q-2)/q\) and \(u=1/q\), so \(s\ge u>0\). Let \(p_r(j)\) be the probability that the sum of \(r\) independent increments taking values \(-1,0,+1\) with probabilities \(u,s,u\) equals \(j\). Then \(E_r=q^d p_r(0)\). Every \(p_r\) is symmetric and nonincreasing for nonnegative \(j\). This follows by induction, as follows: for \(j\ge1\),
\[
\begin{aligned}
p_{r+1}(j)-p_{r+1}(j+1)
={}&u[p_r(j-1)-p_r(j)]\\
&+s[p_r(j)-p_r(j+1)]\\
&+u[p_r(j+1)-p_r(j+2)]\ge0;
\end{aligned}
\]
while at \(j=0\),
\[
p_{r+1}(0)-p_{r+1}(1)
=(s-u)[p_r(0)-p_r(1)]+u[p_r(1)-p_r(2)]\ge0.
\]
The initial point mass \(p_0\) satisfies the requisite conditions. Therefore
\[
p_{r+1}(0)=s p_r(0)+2u p_r(1)\le(s+2u)p_r(0)=p_r(0).
\]
If \(q\ge4\), then \(p_1(0)=(q-2)/q>1/q=p_1(1)\), and the displayed difference recurrence makes this strict gap persist. Thus \(E_1>E_2>E_3>\cdots\). If \(q=3\), then \(p_1(0)=p_1(1)=1/3\), so \(E_1=E_2=q^{d-1}\), but \(p_2(0)=1/3>2/9=p_2(1)\); from that point the strict gap persists and \(E_2>E_3>E_4>\cdots\). Thus for every \(q\ge3\) the maximum equalizer size equals \(E_1=(q-2)q^{d-1}\), attained only at \(r=1\) unless \(q=3\), when precisely \(r=1,2\) attain it.

**Step 5: Equality-case geometry.** For \(q\ge4\), a pair differing at coordinate \(i\) in symbols \(a,b\) has equalizer exactly the exclusion cylinder \(z_i\notin\{a,b\}\). For \(q=3\) and \(r=1\), the sole remaining symbol at the changed coordinate gives a hyperplane \(z_i=c\). For \(q=3\) and \(r=2\), the possible two-coordinate symbol pairs in the equalizer are the two crossed endpoint combinations together with the ordered pair of third symbols. These three distinct ordered pairs form the graph of a bijection \(\pi:[3]\to[3]\); conversely every such bijection arises by choosing the two target vertices in the corresponding crossed pairing. For \(q=2\) and \(r=2\), exactly two of the four local binary words have equal distances, characterized by one fixed value of \(z_i\oplus z_j\). Both parities arise.

**Step 6: Exhaustive classification and exact counting.** A nonresolving set of largest possible cardinality must be contained in some equalizer of equal cardinality, hence must **equal** that equalizer. Steps 3–5 therefore give the entire classification. Different named coordinate pairs, symbols, excluded unordered pairs and permutations yield distinct subsets: the one-coordinate cylinders are detectable from their proper one-coordinate projections, and the two-coordinate graph/parity cylinders are detected by their nontrivial two-coordinate marginals. In the ternary case, permutation graphs have full one-coordinate projections while the hyperplanes do not, so the two families are disjoint. Counting the choices yields respectively \(1\), \(2\binom d2\), \(3d+6\binom d2\), and \(d\binom q2\). This also completes the resolving-number formula.

## Verification

The included pure-Python program `verify.py` enumerates every unordered pair of target vertices in 15 test Hamming graphs, determines its entire equal-distance vertex set by direct Hamming-distance comparisons, and identifies the family of largest equalizers. Separately it constructs the theoretically described coordinate cylinders and demands exact *set-family equality*, as well as the resolving-number formula and independent Laurent-coefficient count for every possible target-pair distance. The tested range is \(q=2,1\le d\le5\); \(q=3,1\le d\le4\); and \(q\in\{4,5\},1\le d\le3\). It passes all 15 cases. Example outputs: \(\operatorname{res}(H(4,3))=28\) with 48 maximal failures; \(\operatorname{res}(H(3,5))=76\) with 30 maximal failures. Run: `python3 verify.py`. The infinite theorem follows from Steps 1–6, *not* from these finite tests.

## Relationship to prior work

Laird, Tillquist, Becker and Lladser, *Resolvability of Hamming Graphs* (first public version 12 July 2019, arXiv:1907.05974v1), give a constrained-linear-system criterion for testing whether an arbitrary Hamming-graph landmark set resolves; see Theorem 2.3 and its hypercube specializations. It provides the natural problem setting but does not state the worst-case threshold, the exact extremal equal-distance distribution over pair distances, or the complete extremal failure-set census proved here. The existence of a decision criterion does not by itself evaluate the global combinatorial maximum and its equality cases.

Garijo, González and Márquez, *The resolving number of a graph* (2013, arXiv:1309.0252v1), Proposition 2.1, already provide the general reduction of the resolving number to the largest equal-distance set. That reduction is explicitly used and not presented as new. The new analysis determines the maximum and classifies every equality case for the entire Hamming family.

Tillquist, Frongillo and Lladser, *Getting the Lay of the Land in Discrete Space* (2021, arXiv:2104.07201v1), Sections 5.4 and 8.5, separately survey Hamming-graph metric dimension and resolving number but do not give this family-wide resolving-number formula or census. Kratica, Kovačević-Vujčić, Čangalović and Stojanović (2012) determine different Hamming invariants: minimum doubly resolving sets for two factors and strong metric dimension. The distinct notion *equidistant dimension* is addressed in a manuscript made accessible online entitled *On the equidistant dimension of Hamming graphs*, which minimizes sets meeting equal-distance pairs rather than maximizing nonresolving landmarks; it does not supply these results.

## Limitations

The classification concerns maximum-cardinality failing landmark sets, **not every** inclusion-maximal failing set, and not the minimum metric dimension. The finite code checks selected small parameter cases only. The prior-art comparison covered the directly relevant accessible primary full texts and record searches, but cannot exclude differently named, unindexed or inaccessible prior work. No independent mathematical audit has been performed; the proof and claims above are provided for independent scrutiny.

## References

- L. Laird, R. C. Tillquist, S. Becker, and M. E. Lladser, *Resolvability of Hamming Graphs*, arXiv:1907.05974v1, first public 2019-07-12. https://arxiv.org/abs/1907.05974
- R. C. Tillquist, R. M. Frongillo, and M. E. Lladser, *Getting the Lay of the Land in Discrete Space: A Survey of Metric Dimension and its Applications*, arXiv:2104.07201v1, 2021-04-15. https://arxiv.org/html/2104.07201v1
- D. Garijo, A. González, and A. Márquez, *The resolving number of a graph*, arXiv:1309.0252v1, 2013-09-01, especially Proposition 2.1. https://arxiv.org/pdf/1309.0252
- J. Kratica, V. Kovačević-Vujčić, M. Čangalović, and M. Stojanović, *Minimal doubly resolving sets and the strong metric dimension of Hamming graphs*, *Applicable Analysis and Discrete Mathematics* 6 (2012), 63–71. https://pefmath.etf.bg.ac.rs/accepted/1204-Kratica-nv.pdf
- J. J. Kratica, A. Lj. Savić, Z. Lj. Maksimović, and M. S. Bogdanović, *On the equidistant dimension of Hamming graphs*, manuscript available online, https://www.vesnik.math.rs/vol/mv26408.pdf. Its issue label is future-dated relative to this study, so the issue date is not being used as a public-source priority date.

