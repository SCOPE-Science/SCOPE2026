# Sharp noise-stability ordering and Poisson refresh transition for cactus minimum spanning trees

## Finding

Let \(G\) be a finite connected simple cactus graph, whose \(c\ge1\) distinct edge-disjoint cycles have lengths \(n_1,\ldots,n_c\ge3\). Give every edge an independent weight from the same atomless law, producing the unique minimum spanning tree \(T\). Independently for every edge, with probability \(\varepsilon\in(0,1]\) replace its weight by a new independent sample from the same distribution; let \(T^\varepsilon\) be the new MST. Define
\[
H=\frac12|E(T)\mathbin{\triangle}E(T^\varepsilon)|.
\]
For every \(n\ge2\), define
\[
s_n(\varepsilon)=\sum_{r=0}^{n}\binom nr\varepsilon^r(1-\varepsilon)^{n-r}
\frac{n-r+2r/n}{n+r}.
\]

**Theorem.** The following statements hold.

1. **Exact distribution:** \(H\) is a sum of independent Bernoulli variables, one for each cycle, with respective probabilities \(d_{n_i}(\varepsilon)=1-s_{n_i}(\varepsilon)\). In particular
\[
\mathbb E[z^H]=\prod_{i=1}^c\bigl(s_{n_i}(\varepsilon)+[1-s_{n_i}(\varepsilon)]z\bigr),
\quad
\Pr(T=T^\varepsilon)=\prod_{i=1}^c s_{n_i}(\varepsilon).
\]
2. **Strict shape and optimization:** For fixed \(0<\varepsilon\le1\), \(s_n(\varepsilon)>s_{n+1}(\varepsilon)>0\) and
\[
s_n(\varepsilon)^2<s_{n-1}(\varepsilon)s_{n+1}(\varepsilon)
\quad(n\ge2).
\]
Thus, for \(c\ge2\) and fixed \(M=\sum_i n_i\ge3c\), the equality probability is **uniquely minimized** (up to permutation) by the balanced integer cycle-length profile (parts differ by at most one), and **uniquely maximized** by \((M-3(c-1),3,\ldots,3)\). These comparisons are conditional on the same number \(c\) of cycles and same \(M\); bridges do not affect them.
3. **Small-noise transition:** With \(\lambda_n=2(n-1)/(n+1)\),
\[
0\le\lambda_n\varepsilon-d_n(\varepsilon)\le2\varepsilon^2,
\qquad
\frac23\varepsilon\le d_n(\varepsilon)\le2\varepsilon
\quad(n\ge3).
\]
For a sequence of cactus graphs with \(c\to\infty\), if \(\varepsilon_c=\alpha/c\), \(\alpha\ge0\), and
\[
\frac1c\sum_{i=1}^c\lambda_{n_i}\longrightarrow\bar\lambda,
\]
then \(H\) converges in total variation to \(\operatorname{Poisson}(\alpha\bar\lambda)\). In particular, if the minimum cycle length tends to infinity, \(\bar\lambda=2\). The equality probability tends to one when \(c\varepsilon_c\to0\) and to zero when \(c\varepsilon_c\to\infty\).

## Assumptions and scope

A *cactus* is a connected finite simple graph in which every edge belongs to at most one simple cycle. A cycle-edge budget \(M\) counts all edges lying on cycles, not bridges. The weights need only be i.i.d. and atomless, not uniformly distributed; apply the common continuous distribution function, preserving all strict comparisons almost surely. All statements concern exact MST edge sets, not graph metric scaling limits. If \(c=0\), the unique spanning tree is \(G\) and \(H=0\), trivially. The case \(\varepsilon=0\) gives \(H=0\), but the **strict** shape statements intentionally require \(\varepsilon>0\).

## Proof

**1. A cycle's maxima after refreshing.** On a cycle of length \(n\), the MST deletes the unique maximum-weight edge. Condition on exactly \(r\) refreshed edges. Let \(U\) be the \(n-r\) retained edges and \(R\) the \(r\) refreshed edges. Their old and new \(R\)-weights are independent; the \(U\)-weights are shared. For \(0<r<n\), put \(V=\max_{e\in U}W_e\) after transforming weights to independent uniforms.

The same edge is deleted both times if the maximum lies in \(U\) both times, or if an edge of \(R\) is the maximizer both times. The first event has probability
\[
\mathbb E[V^{2r}]=\frac{n-r}{n+r}.
\]
For the second event, conditional on \(V=v\), independence of the old and refreshed \(R\) coordinates gives
\[
\sum_{e\in R}\Pr(e\text{ wins among }R\text{ and exceeds }v)^2
=\frac{(1-v^r)^2}{r}.
\]
Since \(\mathbb E[V^r]=(n-r)/n\), this contributes exactly \(2r/[n(n+r)]\). The boundary cases \(r=0\) and \(r=n\) follow directly: probabilities \(1\) and \(1/n\), matching the same expression. Average over \(r\sim\operatorname{Bin}(n,\varepsilon)\) to obtain \(s_n\).

**2. Product law for a cactus.** Every bridge lies in every spanning tree, and on each edge-disjoint cycle the maximum-weight edge is the unique removed edge. This holds simultaneously because the cycles are edge-disjoint. Edge weights and refresh coins on distinct cycles are independent. The event that a cycle's removed edge changes is therefore a Bernoulli event of probability \(d_n\), independently across cycles. Each change contributes exactly two edges to the symmetric difference, proving the generating-function formula.

**3. Strict log-convexity.** For one edge, let \((X,Y)\) be the old/new uniformized weights. Its joint distribution has copula
\[
C_\varepsilon(x,y)=(1-\varepsilon)\min(x,y)+\varepsilon xy.
\]
Write \(q=1-\varepsilon\) and \(Z=C_\varepsilon(X,Y)\). Among \(n\) independent copies of the pair, a designated edge is maximum in both coordinates exactly when each other pair lies coordinatewise below it. Hence, by exchangeability,
\[
s_n=n\,\mathbb E[Z^{n-1}].
\]
For \(0<\varepsilon<1\), set \(y(t)\in(0,1)\) to be the unique root of
\[
q y+\varepsilon y^2=t.
\]
The law of \(Z\) has density
\[
h_\varepsilon(t)=
\frac{q}{q+2\varepsilon y(t)}
+2\varepsilon\int_{y(t)}^1\frac{du}{q+\varepsilon u},
\qquad 0<t<1.
\]
Indeed the first term comes from the diagonal component \(X=Y\), and the second from integrating the continuous component over \(X<Y\) and \(X>Y\). Both terms decrease in \(y(t)\), and at least the latter decreases strictly, so \(h'_\varepsilon(t)<0\). Moreover
\[
h_\varepsilon(1)=\frac{1-\varepsilon}{1+\varepsilon}.
\]
For \(\varepsilon=1\), \(Z=XY\) with independent uniforms, and \(h_1(t)=-\log t\), also strictly decreasing. Integration by parts gives in both cases
\[
s_n=h_\varepsilon(1)+\int_0^1 t^n[-h'_\varepsilon(t)]\,dt.
\]
The right side is a moment representation by a positive measure on \((0,1]\) with positive mass in \((0,1)\). Therefore \(s_n>s_{n+1}\), and strict Cauchy–Schwarz for adjacent moments gives \(s_n^2<s_{n-1}s_{n+1}\). The assertion at \(n=2\) uses the same representation for \(s_1=1\).

**4. Cycle-length extremizers.** Strict log-convexity means the first differences of \(\log s_n\) are strictly increasing. Replacing a pair of lengths \(a<b-1\) by \(a+1,b-1\) strictly lowers \(\log s_a+\log s_b\). Repeated balancing yields the unique minimizing length multiset. Conversely, transferring one unit from the smaller eligible length (\(\ge4\)) to the larger strictly raises the sum, terminating uniquely at one cycle of length \(M-3(c-1)\) and \(c-1\) triangles. Every cycle-length multiset with parts at least three is realized by a cactus in which all cycles meet at one vertex; hence both extremal profiles are attained. Exponentiating proves the optimization statements.

**5. Uniform small-noise estimate and threshold.** The conditional calculation gives
\[
d_n(\varepsilon)=2\left(1-\frac1n\right)\mathbb E\left[\frac{R}{n+R}\right],
\quad R\sim\operatorname{Bin}(n,\varepsilon).
\]
Binomial size biasing with \(R'\sim\operatorname{Bin}(n-1,\varepsilon)\) yields
\[
d_n(\varepsilon)=2(n-1)\varepsilon\,
\mathbb E\left[\frac1{n+1+R'}\right].
\]
Thus \(d_n\le\lambda_n\varepsilon\), while
\[
0\le\lambda_n\varepsilon-d_n
\le\frac{2(n-1)^2}{(n+1)^2}\varepsilon^2
\le2\varepsilon^2.
\]
Since \(0\le R'\le n-1\), \(d_n\ge(n-1)\varepsilon/n\), giving the stated lower bound for \(n\ge3\).

If \(\varepsilon_c=\alpha/c\), these uniform bounds show
\[
\sum_i d_{n_i}(\varepsilon_c)
=\frac{\alpha}{c}\sum_i\lambda_{n_i}+O(\alpha^2/c).
\]
Since every \(d_{n_i}\le2\alpha/c\), Le Cam's elementary Bernoulli-to-Poisson bound \(\sum_i d_{n_i}^2\le4\alpha^2/c\) yields total-variation convergence to the asserted Poisson law. Finally the product \(\prod_i(1-d_i)\) tends to one if \(c\varepsilon_c\to0\), by a union bound, and is at most \(\exp[-(2/3)c\varepsilon_c]\) if \(c\varepsilon_c\to\infty\). This proves the transition.

## Verification

Run `python3 verify.py` from the directory containing the extracted files. The checker directly enumerates all relative weight orders of old and replacement samples for cycle sizes two through four and each possible refreshed count; it then checks the rational formula, strict shape, small-noise inequalities, and balanced/extreme cactus profiles at multiple exact rational refresh probabilities. Expected stdout: `VERIFY_OK 554 exact rational assertions`. Finite tests check algebraic consistency and are not substituted for the proofs above.

## Relationship to prior work

Israeli and Peled study stability under independent edge-weight refreshing for the MST on a *complete graph*, identifying a threshold at the graph's critical random-graph scale. Their graph family and scaling observables differ from the exact equality event for cactus MSTs considered here. Mathwieser and Çela exploit independent cycle structure in cactus graphs for an *explorable-uncertainty query algorithm*, not the two-sample noise law or optimal cycle-size profile. Dombry, Ribatet and Stoev develop the general probability of sample concurrence of coordinatewise maxima; the generic concurrence formula is prior work and **is not claimed new**. What is asserted here is the explicit partial-refresh cycle law, its strict log-convexity in cycle length, the resulting full cactus extremal classification and the sharp many-cycle Poisson refresh transition.

## Limitations

The theorem requires identical atomless original/refreshed weight laws and independent edgewise refreshing. It is not an MST-noise theorem for arbitrary graphs with overlapping cycles, nor a metric Gromov–Hausdorff scaling result. A prior paper may contain an equivalent specialized concurrence/log-convexity statement under different terminology; the present literature comparison does not establish global historical priority. Independent mathematical validation has not been performed.

## References

1. O. Israeli and Y. Peled, *Noise Sensitivity of the Minimum Spanning Tree of the Complete Graph*, arXiv:2306.07357, first public June 12, 2023; https://arxiv.org/abs/2306.07357.
2. C. Mathwieser and E. Çela, *Special Cases of the Minimum Spanning Tree Problem under Explorable Edge and Vertex Uncertainty*, arXiv:2211.15611, first public November 28, 2022; https://arxiv.org/abs/2211.15611.
3. C. Dombry, M. Ribatet and S. Stoev, *Probabilities of Concurrent Extremes*, arXiv:1503.05748 (2015), https://arxiv.org/abs/1503.05748.
