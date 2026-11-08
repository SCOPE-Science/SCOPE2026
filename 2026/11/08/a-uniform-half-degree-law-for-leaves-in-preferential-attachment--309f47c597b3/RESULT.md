# A uniform half-degree law for leaves in preferential-attachment trees

## Finding

**Theorem.** Start with one edge joining two labelled vertices. For each integer \(n\ge2\), form the \((n+1)\)-vertex tree by attaching a new vertex to an existing vertex \(v\) with conditional probability \(d_v(n)/(2(n-1))\), where \(d_v(n)\) is the ordinary (undirected) degree. Let \(\ell_v(n)\) count the degree-one neighbours of \(v\), and put

\[
D_n=\max_{v\le n}d_v(n),\qquad L_n=\max_{v\le n}\ell_v(n).
\]

Then, simultaneously over all vertices,

\[
\boxed{\max_{v\le n}\left|\ell_v(n)-\tfrac12d_v(n)\right|
=O_{\mathbb P}\!\left(n^{1/4}(\log n)^2\right).}
\]

In particular, the extremal leafdegree conjecture for this model holds:

\[
\boxed{\frac{L_n}{D_n}\xrightarrow[n\to\infty]{\mathbb P}\frac12.}
\]

The same bound entails \(L_n-D_n/2=o_{\mathbb P}(\sqrt n)\). The logarithmic power in the uniform bound is not asserted optimal.

## Assumptions and scope

The model is the degree-proportional, single-edge, one-new-leaf-per-step preferential-attachment tree. There are no fitness parameters, added edge choices, deletions, or loops. \(\ell_v(n)\) means **leaf neighbours**, not the total number of descendant leaves. Initial labels and ties in either maximum play no role. Probability refers to the attachment randomness. The theorem is asymptotic in the number of vertices \(n\), and the concentration statement holds for a single tree uniformly over all its vertices.

## Proof

**1. Exact local drift.** For \(n\ge3\), fix an existing vertex \(v\), abbreviate \(d=d_v(n)\) and \(\ell=\ell_v(n)\), and write \(A_v(n)=\ell_v(n)-d_v(n)/2\). Let \(I\) indicate selection of \(v\) for the next attachment, and \(J\) selection of one of its \(\ell\) leaf neighbours. These events are disjoint. Their conditional probabilities are

\[
\mathbb P(I=1\mid\mathcal F_n)=\frac{d}{2(n-1)},\qquad
\mathbb P(J=1\mid\mathcal F_n)=\frac{\ell}{2(n-1)},
\]

because each leaf neighbour has current degree one. An attachment at \(v\) adds a new leaf neighbour and increases \(d\) by one; an attachment at a leaf neighbour removes that neighbour from the leaf count without changing \(d\). Therefore

\[
A_v(n+1)-A_v(n)=\tfrac12 I-J,
\]

and hence

\[
\mathbb E[A_v(n+1)\mid\mathcal F_n]
=\left(1-\frac1{2(n-1)}\right)A_v(n).
\]

Set \(\xi_{v,n+1}=A_v(n+1)-\mathbb E[A_v(n+1)\mid\mathcal F_n]\). This is a martingale difference, with \(|\xi_{v,n+1}|\le2\) and

\[
\mathbb E[\xi_{v,n+1}^2\mid\mathcal F_n]
\le\frac{d_v(n)}{8(n-1)}+\frac{\ell_v(n)}{2(n-1)}
\le\frac{d_v(n)}{n-1}.
\]

The bound uses \(0\le\ell_v(n)\le d_v(n)\). The first attachment is handled by starting the recursion at size three, where \(|A_v(3)|\le1\); each later-born vertex has \(A_v(v)=-1/2\).

**2. Control of the largest degree.** Let \(S_n=\sum_{v\le n}d_v(n)^2\). When a vertex of degree \(d\) is selected, the increment of \(S_n\) is \(2d+2\). Consequently,

\[
\mathbb E[S_{n+1}\mid\mathcal F_n]=\frac{n}{n-1}S_n+2.
\]

Since \(S_2=2\), iteration gives the **exact** formula

\[
\mathbb ES_n=2(n-1)H_{n-1},\qquad H_m=\sum_{j=1}^m\frac1j.
\]

Thus, for \(K_n=\sqrt n\log n\),

\[
\mathbb P(D_n>K_n)\le
\frac{2(n-1)H_{n-1}}{n(\log n)^2}=O(1/\log n).
\]

**3. A simultaneous concentration bound.** Put \(r_s=1-1/(2(s-1))\) for \(s\ge3\). For each vertex \(v\), let \(b_v=\max\{3,v\}\) and \(w_{s,n}=\prod_{u=s}^{n-1}r_u\), with an empty product equal to one. The recursion in Step 1 gives

\[
A_v(n)=w_{b_v,n}A_v(b_v)
+\sum_{s=b_v}^{n-1}w_{s+1,n}\xi_{v,s+1}.
\]

These are deterministic weights in \([0,1]\); the initial term has absolute value at most one. Stop the martingale increments at the first time the maximum degree exceeds \(K_n\). Up to this stopping time, the predictable quadratic variation of the weighted sum is at most

\[
V_n=K_nH_{n-1},
\]

and each weighted increment has magnitude at most two. The two-sided Freedman bound and a union bound over at most \(n\) vertices imply, for every \(t>0\),

\[
\begin{split}
\mathbb P\!\left(\max_{v\le n}|A_v(n)|>1+t\right)
&\le \frac{2(n-1)H_{n-1}}{n(\log n)^2}\\
&\quad+2n\exp\!\left(\frac{-t^2}{2(K_nH_{n-1}+2t/3)}\right).
\end{split}
\]

Indeed, if the degree threshold was never crossed, the stopped and unstopped sums coincide. With \(t=n^{1/4}(\log n)^2\), the second term tends to zero superpolynomially while the first term tends to zero. This proves the asserted uniform \(O_{\mathbb P}\) bound (in fact the displayed threshold holds with probability tending to one).

**4. A nonvanishing \(\sqrt n\)-scale degree.** Let \(R_n=d_1(n)\) denote the degree of either initial vertex. For each positive integer \(r\), write the rising factorial \(x^{\overline r}=x(x+1)\cdots(x+r-1)\). Selection with probability \(R_n/(2(n-1))\) gives

\[
\mathbb E[R_{n+1}^{\overline r}\mid\mathcal F_n]
=\left(1+\frac r{2(n-1)}\right)R_n^{\overline r}.
\]

As \(R_2=1\),

\[
\mathbb ER_n^{\overline r}
=\frac{r!\,\Gamma(n-1+r/2)}{\Gamma(1+r/2)\Gamma(n-1)}.
\]

Since ordinary and rising powers differ by lower-degree terms, it follows for each fixed \(r\) that

\[
\lim_{n\to\infty}\mathbb E\left(\frac{R_n}{\sqrt n}\right)^r
=\frac{r!}{\Gamma(1+r/2)}
=\frac{2^r\Gamma((r+1)/2)}{\sqrt\pi}.
\]

These are the moments of \(|Z|\), where \(Z\sim N(0,2)\). The latter law is moment-determinate and the bounded second moments give tightness, so

\[
\frac{R_n}{\sqrt n}\Longrightarrow |Z|.
\]

In particular, \(D_n\ge R_n\) and \(|Z|>0\) almost surely imply \(\sqrt n/D_n=O_{\mathbb P}(1)\).

**5. Transfer to maxima.** The deterministic inequality

\[
\left|\max_v\ell_v(n)-\tfrac12\max_vd_v(n)\right|
\le\max_v\left|\ell_v(n)-\tfrac12d_v(n)\right|
\]

holds for every finite tree. Step 3 makes the right side \(o_{\mathbb P}(\sqrt n)\); Step 4 bounds \(\sqrt n/D_n\) in probability. Divide by \(D_n\) to obtain \(L_n/D_n\to1/2\) in probability. All quantifiers include every vertex, including those born near time \(n\).

## Verification

The standalone standard-library script `verify.py` enumerates all increasing attachment histories through seven vertices and checks the exact conditional drift and conditional second-moment bound for every existing vertex and all possible next attachments. It separately sums exact rational history weights to verify the squared-degree identity and the initial-vertex rising-factorial moments for orders one through five. Fixed-seed larger-tree simulations provide consistency diagnostics only. On replay, 53,992 finite assertions passed. This finite verification does not prove the infinite-size concentration or limit; those rely on the analytic martingale and moment arguments above.

To reproduce: `python3 verify.py`. No third-party libraries or downloaded datasets are needed.

## Relationship to prior work

Hartle and Krapivsky (2026), arXiv:2602.01021v1, derived the limiting fixed-degree/leafdegree joint distribution, found concentration near half degree for vertices in a fixed-degree stratum as that degree increases, and expressly posed the global maximum-leafdegree versus maximum-degree ratio as a conjecture (overview around their Eq. (18) and discussion of large degrees). That prior information takes the graph-size limit at fixed degree and does not control all \(n\) vertices simultaneously at degrees of order \(\sqrt n\). The present theorem supplies such a simultaneous pathwise-probabilistic bound and proves the conjectured extremal ratio. None of the source's exact joint-distribution formulas or finite-degree variance statements are claimed as new.

Hartle and Krapivsky (2025), arXiv:2511.04085v1, investigated ordinary random recursive trees and a *leafdegree-driven* attachment mechanism; the maximal-leafdegree estimates there refer to different processes. Standard preferential-attachment maximal-degree results supply background on hub scaling but not the uniform leafneighbour comparison. The explicit moment derivation here avoids assuming a maximal-degree limit theorem.

## Limitations

Only the classical degree-proportional model starting with a single edge is covered. The finite-size concentration bound is not asserted sharp and its leading probability term decays only logarithmically. The result does not claim that a maximum-degree vertex and a maximum-leafdegree vertex are the same, nor does it provide the distribution of either maximum. It does not prove almost-sure convergence of their ratio or conclusions for changed attachment mechanisms. Independent mathematical validation and a definitive determination of priority relative to every historical source have not been performed.

## References

1. H. Hartle and P. L. Krapivsky, *Leaves of preferential attachment trees*, arXiv:2602.01021v1 (first posted 2026-02-01). https://arxiv.org/html/2602.01021
2. H. Hartle and P. L. Krapivsky, *Statistics of leaves in growing random trees*, arXiv:2511.04085v1 (first posted 2025-11-06). https://arxiv.org/abs/2511.04085
3. D. A. Freedman, *On tail probabilities for martingales*, Ann. Probability 3 (1975), 100–118. Standard bounded-increment quadratic-variation inequality used in the proof.
