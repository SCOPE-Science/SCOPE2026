# Coupled Poisson extremes of degrees and universal vertices in random interval graphs

## Finding
For each integer \(n\ge2\), let \(G_n\) be the interval-intersection graph of \(n\) independently sampled intervals formed by sorting two independent endpoints from one common atomless real distribution. Transform the endpoints by their common continuous distribution function, obtaining ordered pairs \(0<L_i<R_i<1\) almost surely. Let \(D_i\) be the degree of vertex \(i\) and let \(U_n=\#\{i:D_i=n-1\}\).

Define a side \(S_i=L\) if \(R_i\le1-L_i\), and \(S_i=R\) otherwise. On the left let \(Q_i=L_i/R_i\); on the right let \(Q_i=(1-R_i)/(1-L_i)\). Then the point measure
\[
\Theta_n=\sum_{i=1}^n\delta_{(D_i/\sqrt n,S_i,Q_i)}
\]
converges vaguely in distribution on \([0,\infty)\times\{L,R\}\times[0,1]\) to a Poisson point process whose intensity, on **each** side, is
\[
\frac{d}{2}\,dd\,dq,\qquad d>0,\quad 0<q<1.
\]
Moreover this convergence holds *jointly* with the universal-vertex count, with the following explicit dependence structure. Let \(\mathcal P_L,\mathcal P_R\) be independent Poisson point processes of intensity \(2\,du\,dv\) on \(\{0<u<v<\infty\}\), and let \(\mathcal P_C\) be a third independent process of intensity \(2\,ds\,dt\) on the positive quadrant. Set
\[
A=\inf\{v:(u,v)\in\mathcal P_L\},\qquad B=\inf\{v:(u,v)\in\mathcal P_R\},
\]
\[
\Theta=\sum_{(u,v)\in\mathcal P_L}\delta_{(2v,L,u/v)}+\sum_{(u,v)\in\mathcal P_R}\delta_{(2v,R,u/v)},\qquad
U=\mathcal P_C([0,A]\times[0,B]).
\]
Then \((\Theta_n,U_n)\Rightarrow(\Theta,U)\) in the product of the vague point-process topology and the discrete topology. Conditional on the two low-degree side processes,
\[
U\mid\mathcal P_L,\mathcal P_R\sim\operatorname{Poisson}(2AB).
\]
In particular, if \(D_{(k),n}\) is the \(k\)-th smallest vertex degree for fixed \(k\ge1\), then for each \(t\ge0\),
\[
\lim_{n\to\infty}\Pr(D_{(k),n}>t\sqrt n)
=e^{-t^2/2}\sum_{j=0}^{k-1}\frac{(t^2/2)^j}{j!},
\]
and the left/right side labels of successive low-degree vertices are independent fair signs, with independent uniform \([0,1]\) endpoint-ratio marks. If \(T_{L,1}=2A\) and \(T_{R,1}=2B\) denote the limiting least degree on each side, then
\[
U\mid T_{L,1},T_{R,1}\sim\operatorname{Poisson}\left(\frac{T_{L,1}T_{R,1}}2\right).
\]
Write \(T_{\min}=\min\{d:(d,s,q)\in\Theta\}\). Thus the extreme low-degree and universal-vertex statistics are not asymptotically independent. More sharply, the limiting covariance is the exact positive constant
\[
\operatorname{Cov}(U,T_{\min})=\sqrt{\pi}\left(4-\frac{7+\pi}{2\sqrt2}\right)=0.7345146798\ldots.
\]
For \(t\ge0\) their joint absence-and-minimum tail is
\[
\Pr\bigl(U=0,T_{\min}>t\bigr)
=4\int_{t/2}^{\infty}\!\int_{t/2}^{\infty}
 ab\,e^{-(a+b)^2}\,da\,db.
\]
At \(t=0\) this is \(1/3\), in agreement with the previously established universal-vertex existence probability.

## Assumptions and scope
The graph is the paired-endpoint, *not* the independent-edge or fixed-length, random interval graph. Each pair has two iid endpoints; all pairs are independent. Common atomless endpoint laws give the same result by the probability integral transform and order preservation. Vertex degrees count neighbors, not self-loops; the case \(n=1\) is immaterial to the limit. Vague convergence concerns bounded degree coordinates, and the vertex labels do not appear in the limiting process. Every assertion about \(k\) fixes \(k\) before taking \(n\to\infty\).

## Proof
**1. The three independent endpoint corner processes.** Each sampled interval has uniform density \(2\) on \(0<a<b<1\). Under the square-root scaling, the endpoint neighborhoods \((a,b)\approx(0,0)\), \((a,b)\approx(1,1)\), and \((a,b)\approx(0,1)\) are disjoint. Write the corresponding coordinates respectively as \((u,v)=(\sqrt n a,\sqrt n b)\), \((u,v)=(\sqrt n(1-b),\sqrt n(1-a))\), and \((s,t)=(\sqrt n a,\sqrt n(1-b))\). Multinomial rare-cell factorial moments (equivalently, the Laplace functional of iid points) give joint convergence on every compact set to independent Poisson processes of intensity \(2\) in each of these three domains, namely \(\mathcal P_L,\mathcal P_R,\mathcal P_C\). Localizing and then letting the compact windows increase preserves the claimed joint convergence.

**2. Localization of low-degree vertices.** For a tagged interval \([a,b]\), the other intervals intersect it independently, each with probability
\[
p(a,b)=1-a^2-(1-b)^2=2b-b^2-a^2.
\]
Consequently \(D_i\mid (L_i,R_i)=(a,b)\sim\operatorname{Bin}(n-1,p(a,b))\). The deterministic inequality \(p(a,b)\ge\min\{b,1-a\}\) holds: if \(a+b\le1\), distinguish \(b\le1/2\) and \(b>1/2\), using respectively \(a\le b\) and \(a\le1-b\) to prove \(p\ge b\); reflect the interval for \(a+b\ge1\).

For any fixed \(t\ge0\), choose \(C>4(t+1)\). Outside the two endpoint corner windows \(b\le C/\sqrt n\) and \(1-a\le C/\sqrt n\), the conditional mean of \(D_i\) exceeds \(C\sqrt n(1-1/n)\). A binomial Chernoff bound gives \(\Pr(D_i\le t\sqrt n\mid a,b)\le e^{-c_t\sqrt n}\) there; a union bound over all \(n\) vertices makes this negligible. Thus all bounded rescaled degrees arise from the two short-interval corners with probability tending to one.

In the left corner \(a=u/\sqrt n\), \(b=v/\sqrt n\) with bounded \(u,v\), the conditional mean satisfies \(\mathbb E(D_i/\sqrt n\mid a,b)=2v+O_C(n^{-1/2})\), and the conditional variance is \(O_C(n^{-1/2})\). Each corner window contains a tight number of vertices (its expected size is bounded by \(C^2\)), so Chebyshev's inequality and a union bound show that, uniformly for its vertices, \(D_i/\sqrt n=2v+o_{\Pr}(1)\). Reflection gives the same statement in the right corner. The side and endpoint-ratio marks converge to \(L,u/v\) or \(R,u/v\). The continuous mapping theorem, excluding probability-zero boundary marks, proves the limit of \(\Theta_n\) and its joint convergence with the three raw corner processes.

**3. Intensity and order statistics.** With \(d=2v\), \(q=u/v\), the planar intensity \(2\,du\,dv\) pushes forward to \((d/2)\,dd\,dq\) on each side. The unmarked combined degree process therefore has intensity \(d\,dd\). Its count in \([0,t]\) is Poisson with mean \(t^2/2\), proving the \(k\)-th degree formula. Factorization of the intensity gives the independent fair side and uniform ratio marks.

**4. Universal vertices and joint coupling.** Let \(r_n=\min_iR_i\) and \(b_n=\max_iL_i\). Their rescaled gaps \((\sqrt n r_n,\sqrt n(1-b_n))\) converge jointly to \((A,B)\); these are the least second coordinates of the two short-corner processes. When \(r_n<b_n\), an interval is universal exactly if its left endpoint is no larger than \(r_n\) and its right endpoint is no smaller than \(b_n\). In that event the two intervals attaining \(r_n\) and \(b_n\) are disjoint and cannot be universal. The exceptional event \(r_n\ge b_n\), when every interval contains a common point, has probability \(2^n/\binom{2n}{n}\), as follows by uniformly pairing the ordered \(2n\) endpoints and requiring each pair to cross the median gap; this tends to zero. The universal intervals are therefore, with probability tending to one, exactly the points from the long-interval corner lying in the random rectangle \([0,\sqrt n r_n]\times[0,\sqrt n(1-b_n)]\). The rectangle-count map is almost surely continuous at the three Poisson limits because no long-corner point lies on either random boundary. Hence the claimed *joint* convergence, not merely marginal convergence. Conditional independence of \(\mathcal P_C\) gives \(U\mid\mathcal P_L,\mathcal P_R\sim\operatorname{Poisson}(2AB)\).

**5. Quantified dependence.** The distributions of \(A\) and \(B\) are independent with \(\Pr(A>x)=\Pr(B>x)=e^{-x^2}\), since each truncated triangle has Poisson mean \(x^2\). Thus their densities are \(2x e^{-x^2}\). Integrating the conditional zero probability \(e^{-2AB}\) over \(A,B>t/2\) proves the displayed integral. The covariance in the limiting variables equals \(4\operatorname{Cov}(AB,\min(A,B))\). The independent Rayleigh-type minima have \(\mathbb EA=\sqrt\pi/2\), \(\mathbb E\min(A,B)=\sqrt\pi/(2\sqrt2)\), and \(\mathbb E(AB)=\pi/4\). Polar integration with joint density \(4ab e^{-a^2-b^2}\) gives
\[
\mathbb E[AB\min(A,B)]=\frac{15\sqrt\pi}{4}\,2\int_0^{\pi/4}\cos^2\theta\sin^3\theta\,d\theta=\sqrt\pi\left(1-\frac7{8\sqrt2}\right).
\]
Substitution gives the displayed exact positive covariance. These are moments **of the limiting variables**; no finite-size covariance convergence is claimed.

## Verification
The standalone \(\texttt{verify.py}\) checks the exact endpoint-degree formula against exhaustive labeled endpoint pairings, validates the short-corner localization inequality, evaluates the point-process mean formulas, checks the shared-boundary conditional mean formula, and performs a deterministic, seeded numerical sanity check. Re-run with \(\texttt{python3 verify.py}\) from the package directory. Exhaustive finite enumeration and simulations are checks, not proofs of infinite-dimensional convergence or originality.

## Relationship to prior work
Scheinerman's 1988 paired-endpoint random-interval model establishes the one-dimensional Rayleigh limit of the *minimum* degree; Justicz, Scheinerman, and Winkler (1990) establish the exact \(2/3\) existence probability of a universal vertex. The accessible full text of Iliopoulos (2015), particularly Sections 3.2 and 4.2–4.3, reproduces these baseline results. Diaconis, Holmes, and Janson's interval-graph-limit paper (first public version 2011) discusses the same sampling model and these extrema. A previously described marked-Poisson limit for universal vertices already gives the marginal limiting universal count and the two outermost endpoint gaps; those marginal statements are used here as background, not claimed as new. The contribution assessed here is the **entire side- and ratio-marked low-degree Poisson spectrum and its joint dependence on the universal-vertex process**, including the resulting all-\(k\) low-degree order statistics and conditional coupling. These are not consequences of knowing the minimum-degree law and the universal count separately.

## Limitations
This is a weak limit for fixed bounded rescaled degree windows, not an all-vertex degree-distribution theorem or a uniform approximation as the degree cutoff increases with \(n\). Positive covariance is proved for the stated limiting variables; a finite-size covariance asymptotic would require separate uniform-integrability bounds. The proof is specific to the independent paired-endpoint interval model, although its common atomless endpoint distribution is arbitrary. Exact publication priority is not certified: the complete 1988 and 1990 primary articles were not accessible here, so potential implicit broader coverage in those sources remains a specific residual risk. A 2026 paper addressing the unmarked universal count does not by its available abstract establish the marked low-degree spectrum; its full text was unavailable.

## References
1. E. R. Scheinerman, *Random interval graphs*, Combinatorica 8 (1988), 357–371, doi:10.1007/BF02189092.
2. J. Justicz, E. R. Scheinerman and P. M. Winkler, *Random intervals*, American Mathematical Monthly 97 (1990), 881–889, doi:10.1080/00029890.1990.11995679.
3. P. Diaconis, S. Holmes and S. Janson, *Interval graph limits*, arXiv:1102.2841v1, 2011-02-14, https://arxiv.org/abs/1102.2841.
4. V. Iliopoulos, *Random Interval Graphs*, arXiv:1507.06275v1, 2015-07-22, https://arxiv.org/html/1507.06275v1.
5. J. Sarkar, *How Many Random Intervals Intersect All Others?*, Resonance 31 (2026), 739–751, doi:10.1007/s12045-026-1997-0 (abstract only inspected).
