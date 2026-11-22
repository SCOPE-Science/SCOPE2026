# Sharp open-neighborhood trace growth in finite interval graphs

## Finding
For the class \(\mathcal I\) of all finite simple interval graphs, define the *open-neighborhood shatter function*
\[
\pi_{\mathcal I}(m)=\max_{G\in\mathcal I,\ A\subseteq V(G),\ |A|=m}\left|\{N_G(v)\cap A:v\in V(G)\}\right|.
\]
The exact values are
\[
\pi_{\mathcal I}(0)=1,\qquad \pi_{\mathcal I}(1)=2,\qquad
\pi_{\mathcal I}(m)=\frac{m(m+3)}2-1\quad(m\ge2).
\]
In particular, the associated open-neighborhood set system has VC dimension \(3\) and VC density \(2\). This is an *open*-neighborhood statement, not a closed-neighborhood claim.

## Assumptions and scope
An interval graph is a finite, loopless undirected graph represented by nondegenerate closed intervals \(I_v=[L_v,R_v]\) on a real line, with distinct vertices adjacent exactly when their intervals intersect. We may perturb endpoints so that all marked endpoints are distinct, without changing any marked-pair adjacencies; the unmarked query intervals can be analyzed directly with arbitrary endpoints, while the two small witness queries below use the strict gaps between marked endpoints. The maximum permits arbitrarily many unmarked vertices. A marked vertex's trace omits itself even though its representing interval intersects itself.

## Proof
Fix \(m\) marked intervals, indexed by increasing left endpoint. Let \(\mathcal Q\) be the family of intersection sets \(\{i:I_i\cap J\ne\varnothing\}\) realized by arbitrary intervals \(J\) on the line, including intervals not present in the graph. For \(J=[a,b]\), its intersection set equals \(P_k\setminus Q_t\), where \(P_k=\{i:L_i\le b\}\) is a left-endpoint prefix of cardinality \(k\) and \(Q_t=\{i:R_i<a\}\) is a right-endpoint prefix. For fixed \(k\), as \(t\) varies these sets are nested subsets of a \(k\)-element set, so at most \(k\) of them are nonempty. Summing over \(k=1,\ldots,m\) and adjoining the one empty set gives
\[
|\mathcal Q|\le 1+\sum_{k=1}^m k=1+\frac{m(m+1)}2.\tag{1}
\]
Every unmarked vertex contributes a trace from \(\mathcal Q\). Each of the \(m\) marked vertices contributes at most one additional trace: its full interval-intersection trace with itself deleted.

Assume first \(m\ge2\) and the marked vertex \(v\) whose right endpoint is smallest is different from the vertex \(w\) whose left endpoint is largest. Because all other right endpoints exceed \(R_v\), a sufficiently short interval just to the right of \(R_v\) intersects precisely those marked intervals intersecting \(I_v\), except \(I_v\) itself. Thus it realizes \(N_G(v)\cap A\). Similarly, a short interval just to the left of \(L_w\) realizes \(N_G(w)\cap A\). These are two marked-vertex traces already in \(\mathcal Q\); (1) yields
\[
\bigl|\{N_G(x)\cap A:x\in V(G)\}\bigr|\le 1+\frac{m(m+1)}2+m-2=\frac{m(m+3)}2-1.\tag{2}
\]

Suppose instead \(v=w\). Then one marked interval starts last and ends first, so it is properly contained in every other marked interval. Whenever a query \(J=[a,b]\) has \(b<L_v\), it also has \(a<L_v<R_v\), and consequently its right-endpoint deletion prefix \(Q_t\) is empty. Therefore all queries with left-endpoint prefix size \(k<m\) yield at most one trace each. The queries with \(k=m\) yield at most \(m+1\) distinct traces. Hence \(|\mathcal Q|\le 2m\). Moreover the open trace of \(v\), namely \(A\setminus\{v\}\), belongs to \(\mathcal Q\): take a short interval just right of \(R_v\) but left of all the other right endpoints. Therefore the total is at most \(2m+m-1=3m-1\), which is no larger than the right-hand side of (2) whenever \(m\ge3\). For \(m=2\) the elementary Boolean ceiling \(2^2=4\) equals the proposed bound. The cases \(m=0,1\) have upper bounds \(1,2\) by cardinality.

For sharpness when \(m\ge3\), mark \(m\) intervals arranged as an induced path, with consecutive intervals overlapping in disjoint short overlaps, and every nonconsecutive pair disjoint; for example choose
\[
I_i=[2i-2,2i+1]\quad(1\le i\le m).
\]
For each nonempty consecutive index block \(\{a,a+1,\ldots,b\}\), there is an auxiliary interval meeting exactly the marked intervals in that block: use a small interval inside \(I_a\) before the overlap with \(I_{a-1}\) and inside \(I_b\) after the overlap with \(I_{b+1}\), joining those two portions when \(a<b\); for \(a=b\), choose a short private segment. (At endpoints, absent neighbors impose no restriction.) An auxiliary interval disjoint from all marks realizes the empty set. Thus auxiliary vertices give \(1+m(m+1)/2\) different traces. Each internal marked vertex \(i\), for \(2\le i\le m-1\), has open trace \(\{i-1,i+1\}\), not a consecutive block, with these \(m-2\) traces pairwise distinct. The two endpoint marked traces are singleton blocks. This attains (2).

For \(m=2\), two overlapping but nonnested marked intervals allow auxiliary intervals with traces \(\varnothing,\{1\},\{2\},\{1,2\}\). For \(m=1\), use an isolated auxiliary interval and one intersecting auxiliary interval. For \(m=0\), a nonempty graph has one empty trace. The value at \(m=3\) equals \(8\), so three marked points can be shattered; at \(m=4\) the value is \(13<16\), so no four points can be shattered (the shatter function is monotone with respect to the support). The polynomial is quadratic with positive leading coefficient, proving VC density \(2\).

## Verification
The accompanying standalone `verify.py` constructs interval graphs from all pairings of ordered endpoints and calculates their open-neighborhood traces directly, with marked vertices treated separately from auxiliary interval probes. It verifies the exact maximum for each \(1\le m\le7\), including \(135135\) endpoint pairings at \(m=7\), and checks the explicit path construction for all \(2\le m\le20\). This finite enumeration corroborates but does not replace the proof for arbitrary \(m\). Run `python verify.py` in an ordinary Python 3 environment.

## Relationship to prior work
Dreier, Mählmann, and Toruńczyk (2026) consider general bounded-rank types and open-neighborhood complexity for broad model-theoretic graph classes; their work does not assert an exact interval-graph shatter polynomial. Dreier, Mählmann, McCarty, Pilipczuk, and Toruńczyk (2026) establish almost-linear complexity for monadically dependent classes; the present exact quadratic interval-graph calculation neither follows from nor contradicts that result. Parreau's 2013 interval-graph VC bound is explicitly for **closed** neighborhoods \(N[v]\); the extra open traces of marked vertices here are caused by deleting self-membership. Published general shatter bounds, including Sauer–Shelah, constrain the degree but do not imply this coefficient and additive term. published-finding corpus database searches for this precise open-neighborhood statement and its aliases identified no matching exact result; this is not a proof of universal historical novelty.

## Limitations
The theorem maximizes over arbitrary finite interval graphs and all marked sets; it does not classify every extremizing interval representation or all possible trace families. No claim is made for higher-arity first-order types, general chordal graphs, or closed-neighborhood systems. The historical-priority conclusion is limited by accessible literature and database coverage, and independent verification has not been performed.

## References
1. J. Dreier, N. Mählmann, and S. Toruńczyk, *First-Order Model Checking on Monadically Dependent Graph Classes*, arXiv:2611.08143, first posted 2026-11-05, https://arxiv.org/html/2611.08143v1.
2. J. Dreier, N. Mählmann, R. McCarty, M. Pilipczuk, and S. Toruńczyk, *Neighborhood Complexity and Radius-1 Merge-Width in Monadically Dependent Graph Classes*, arXiv:2607.10941, first posted 2026-07-12, https://arxiv.org/abs/2607.10941.
3. A. Parreau, *Identifying Codes and VC-Dimension*, Combgraph Seminar slides, 2013-10-03, https://perso.liris.cnrs.fr/aline.parreau/Research/Slides/seminaireCombgraph13.pdf (closed-neighborhood definition, slide 15; interval bound, slide 17).
