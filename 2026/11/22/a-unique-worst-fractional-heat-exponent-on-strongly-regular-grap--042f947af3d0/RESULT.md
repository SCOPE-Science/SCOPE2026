# A unique worst fractional-heat exponent on strongly regular graphs

## Finding
Let \(G\) be a finite connected noncomplete unweighted strongly regular graph with \(N\) vertices and degree \(k\), and let \(0<a<b\) be the two distinct nonzero eigenvalues of its combinatorial Laplacian \(L\). Put \(d=N-k-1>0\). For every \(\alpha>0\) and \(t\geq0\) define
\[
 S_\alpha(t)=\exp(-tL^\alpha)
\]
using the nonnegative spectral functional calculus. The exact positivity, transient amplification, and optimizing exponent are as follows.

1. For \(0<\alpha\leq1\), \(S_\alpha(t)\) is entrywise strictly positive for every \(t>0\). For every \(\alpha>1\), there is a unique \(T_G(\alpha)>0\), characterized by
\[
 b e^{-a^\alpha T_G(\alpha)}-a e^{-b^\alpha T_G(\alpha)}=b-a,
\]
for which entrywise-nonnegative times are exactly \(\{0\}\cup[T_G(\alpha),\infty)\). All \(d\) nonedge entries in every row are negative for \(0<t<T_G(\alpha)\), zero at that threshold, and positive afterwards. Every edge and diagonal entry is strictly positive at every positive time.

2. The positivity delay \(T_G(\alpha)\), over all real \(\alpha>1\), has **exactly one global maximizer** \(\alpha_G^*>1\). To calculate it, set
\[
 q=b/a>1,\qquad c=\log\frac{q}{q-1},\qquad
 \delta=\frac{\log a}{\log q}>0,\qquad
 h(z)=-\log(qe^{-z}-q+1),\quad 0<z<c.
\]
There is exactly one \(z_*\in(0,c)\) satisfying
\[
 \frac{z_*h'(z_*)}{h(z_*)}=1+\frac1\delta.
\]
The unique maximizing exponent and the maximum delay are
\[
 \boxed{\alpha_G^*=\frac{\log(h(z_*)/z_*)}{\log q},\qquad
 \max_{\alpha>1}T_G(\alpha)=\frac{z_*^{1+\delta}}{h(z_*)^\delta}.}
\]

3. The sharp counting-measure \(\ell^1\)- and \(\ell^\infty\)-operator norms agree. For \(\alpha>1\),
\[
 \|S_\alpha(t)\|_{1\to1}=\|S_\alpha(t)\|_{\infty\to\infty}
 =1+\frac{2d}{N(b-a)}\left[b e^{-a^\alpha t}-a e^{-b^\alpha t}-(b-a)\right]_+.
\]
Their unique positive-time maximum occurs at
\[
 \boxed{\vartheta_G(\alpha)=\frac{(\alpha-1)\log(b/a)}{b^\alpha-a^\alpha}.}
\]
For \(0<\alpha\leq1\) both norms equal one for all times.

4. At the critical exponent, as \(\varepsilon\downarrow0\),
\[
 \boxed{T_G(1+\varepsilon)=\frac{2\log(b/a)}{b-a}\varepsilon+O_G(\varepsilon^2),}
\]
\[
 \boxed{\sup_{t\ge0}\|S_{1+\varepsilon}(t)\|_{\infty\to\infty}
 =1+\frac{dab(\log(b/a))^2}{N(b-a)^2}\varepsilon^2+O_G(\varepsilon^3).}
\]
At large exponent the delay shrinks, but maximal transient amplification remains nontrivial:
\[
 \boxed{a^\alpha T_G(\alpha)\longrightarrow\log\frac b{b-a},\qquad
 \sup_{t\ge0}\|S_\alpha(t)\|_{\infty\to\infty}
 \longrightarrow1+\frac{2da}{N(b-a)}.}
\]

For the Petersen graph \((N,k,a,b)=(10,3,2,5)\), the maximizing exponent is \(\alpha_G^*=1.636435234508\ldots\), with worst delay \(0.131791058820\ldots\).

## Assumptions and scope
The graph is undirected, simple, unweighted, connected, noncomplete, and strongly regular, with at least two distinct nonzero Laplacian eigenvalues. In this standard nontrivial case \(2\le k<N-1\), every nonedge has a common neighbor, and the spectral gap satisfies \(a>1\). The functional calculus has \(0^\alpha=0\). All inequalities are entrywise in the standard vertex basis, with ordinary counting \(\ell^p\) norms. The endpoint \(t=0\) is deliberately included: \(S_\alpha(0)=I\) is nonnegative. No finite-graph or exponent-uniform error is hidden in the exact identities; \(O_G\) constants may depend on the fixed graph.

## Proof
**Spectral reduction.** Write \(P_0=J/N\), and let \(P_a,P_b\) be the spectral projections corresponding to \(a,b\). Then
\[
 P_a+P_b=I-P_0,\qquad aP_a+bP_b=L,
 \qquad S_\alpha(t)=P_0+e^{-a^\alpha t}P_a+e^{-b^\alpha t}P_b.
\]
For distinct nonadjacent vertices, \(L_{ij}=0\); hence \((P_a)_{ij}=-b/[N(b-a)]\) and \((P_b)_{ij}=a/[N(b-a)]\). Their common entry is
\[
 K_0(t)=\frac1N\left[1-\frac{be^{-At}-ae^{-Bt}}{b-a}\right],
 \quad A=a^\alpha,\ B=b^\alpha.
\]
For adjacent vertices \(L_{ij}=-1\), the entry is
\[
 K_1(t)=\frac1N\left[1-e^{-At}+\frac{N-a}{b-a}(e^{-At}-e^{-Bt})\right]>0
\]
for \(t>0\), since \(N\ge b>a\) (the complement Laplacian is \(NI-J-L\), which is positive semidefinite). Every diagonal entry is strictly positive because it is a positive sum of squared spectral-projection coordinates, including the contribution \(1/N\).

For completeness, \(a>1\) in every graph under consideration. Writing \(r=k-a\) and \(s=k-b\), the two nonprincipal adjacency eigenvalues solve \(x^2-(\lambda-\mu)x-(k-\mu)=0\), where \(\lambda\le k-2\) is the number of common neighbors of an edge pair and \(1\le\mu\le k\) that of a nonedge pair. The polynomial at \(x=k-1\) is at least \(\mu k-1>0\). Its smaller root is nonpositive and its larger root \(r\) is therefore strictly smaller than \(k-1\). Thus \(a=k-r>1\).

**Exact sign transitions.** For a nonedge the sign of \(K_0(t)\) equals the sign of
\[
 q(1-e^{-At})-(1-e^{-Bt}),\qquad q=b/a>1.
\]
For \(B>A>0\), the function \((1-e^{-Bt})/(1-e^{-At})\) decreases strictly from \(B/A=q^\alpha\) at \(t\downarrow0\) to one as \(t\to\infty\). Indeed its logarithmic derivative equals
\[
 \frac1t\left[\frac{Bt}{e^{Bt}-1}-\frac{At}{e^{At}-1}\right]<0
\]
because \(y/(e^y-1)\) is strictly decreasing. If \(\alpha\le1\), the ratio stays below \(q\), giving strict positivity. If \(\alpha>1\), it crosses \(q\) exactly once, from above, giving exactly the claimed negative-to-positive interval and its uniquely defined endpoint.

**Peak operator norm.** Since every row sums to one, and edge and diagonal entries are positive, its absolute row sum is exactly \(1+2d[-K_0(t)]_+\), proving the displayed sharp operator norms; symmetry gives the same column-sum norm. The derivative
\[
 K_0'(t)=\frac{bA e^{-At}-aB e^{-Bt}}{N(b-a)}
\]
has exactly one positive zero when \(\alpha>1\), at \(\vartheta_G(\alpha)\). It changes from negative to positive there. The sharp norm therefore has its unique global peak at that time.

**Unique exponent of maximal delay.** Let \(z=a^\alpha T_G(\alpha)\). The defining equation becomes
\[
 q(1-e^{-z})=1-e^{-q^\alpha z}.
\]
The positive solution has \(0<z<c=\log(q/(q-1))\). Solving for the exponent gives \(q^\alpha=h(z)/z\) with \(h(z)=-\log(qe^{-z}-q+1)\). As \(z\) increases from zero to \(c\), \(h(z)/z\) increases strictly from \(q\) to infinity: this follows from strict convexity of \(h\) and \(h(0)=0\). Consequently \(z\) parameterizes all \(\alpha>1\) bijectively. Since \(a>1\), \(\delta=\log a/\log q>0\), and
\[
 T_G=\frac{z^{1+\delta}}{h(z)^\delta}.
\]
Put \(f(z)=h'(z)=q/[q-(q-1)e^z]\). Its logarithmic derivative \((\log f)'=(q-1)e^z/[q-(q-1)e^z]\) is positive and strictly increasing. For each \(0\le\theta<1\), the ratio \(f(\theta z)/f(z)\) strictly decreases with \(z\), since its logarithmic derivative is \(\theta(\log f)'(\theta z)-(\log f)'(z)<0\). Therefore
\[
 \frac{h(z)}{zf(z)}=\int_0^1\frac{f(\theta z)}{f(z)}\,d\theta
\]
is strictly decreasing from one to zero as \(z\uparrow c\); equivalently \(zh'(z)/h(z)\) increases strictly from one to infinity. Differentiating \(\log T_G\) with respect to \(\log z\) gives \((1+\delta)-\delta zh'/h\), which has precisely one zero and changes from positive to negative. Both endpoint delays vanish, because \(T_G\to0\) as \(z\downarrow0\), while as \(z\uparrow c\) the positive power of \(h\) diverges. Thus this critical point is the unique global maximum, giving the claimed formulas.

**Boundary regimes.** Put \(\varepsilon=\alpha-1\). Expanding the nonedge formula simultaneously for \(t=O(\varepsilon)\) gives
\[
 K_0(t)=-\frac{ab\log(b/a)}{N(b-a)}\varepsilon t
 +\frac{ab}{2N}t^2+O_G(\varepsilon^2t+\varepsilon t^2+t^3).
\]
Its positive root is \(2\varepsilon\log(b/a)/(b-a)+O_G(\varepsilon^2)\); its minimum occurs at half that leading time, and has depth \(ab(\log(b/a))^2\varepsilon^2/[2N(b-a)^2]+O_G(\varepsilon^3)\). This yields the norm expansion. As \(\alpha\to\infty\), the equation \(h(z)/z=q^\alpha\) forces \(z\uparrow c\), which proves the delay limit. At the minimum time, \(a^\alpha\vartheta_G(\alpha)\to0\) and \(b^\alpha\vartheta_G(\alpha)\to\infty\), so \(K_0(\vartheta_G(\alpha))\to-a/[N(b-a)]\), proving the nonzero peak-norm limit.

## Verification
Run `python checker.py` with Python, NumPy, SciPy, and NetworkX installed. The script constructs eight named strongly regular examples (including primitive Petersen, pentagon, triangular and rook graphs and two imprimitive multipartite controls), computes the Laplacians independently from adjacency matrices, checks the two nonzero eigenvalues, and compares spectral-projector kernels with independently computed matrix exponentials. It checks predicted signs before/after the sharp threshold, strict edge/diagonal positivity, maximizing exponents, and the two asymptotic regimes. The included checker completed 568 matrix-time comparisons, 32 scale checks and 800 optimization-grid comparisons. Its finite numerical results corroborate the stated identities but do not replace the analytic proofs of exact thresholds or unique global optimality.

## Relationship to prior work
Riascos and Mateos (2014, openly accessible 2015 version) introduce spectral fractional network diffusion, emphasizing \(0<\alpha<1\) and explicit ring formulas; their Sections III–V do not establish the upper-order positivity frontier or a uniquely worst exponent for strongly regular networks. Daners, Glück and Kennedy (first available 2015; inspected later full-text revision) establish general qualitative eventual-positivity criteria; they do not optimize this fractional exponent or give the sharp finite family formula. A prior published published-finding corpus theorem proves sharp fractional-heat positivity and transient norm formulas for **complete multipartite** graphs. That covers the imprimitive equal-part subset of the present statement and is expressly not claimed as a new subcase; its full RESULT.md contains no unique-order optimizer. The distinct contribution here is the global uniqueness of the worst fractional exponent **for every connected noncomplete strongly regular graph**, including primitive families such as pentagons, Petersen, rook, and triangular graphs, together with an explicit optimizer equation and a nonvanishing large-order transient amplification limit. Related mixed quadratic graph-heat formulas concern a different generator family and do not imply this fractional-power optimizer.

## Limitations
This analysis is for the combinatorial Laplacian of finite unweighted connected noncomplete strongly regular graphs. It does not prove the corresponding statement for arbitrary graphs, weighted edges, directed or normalized Laplacians, or arbitrary spectral filters. For \(\alpha>1\) the operators are not positivity-preserving at small times; they are not Markov transition kernels then. The sharp times and optimizing exponents are generally specified by unique scalar roots, not elementary closed radicals. The numerical checks are finite. The inspected primary papers and recoverable published comparisons do not establish absolute priority; independent external mathematical review has not been performed.

## References
1. A. P. Riascos and J. L. Mateos, *Fractional dynamics on networks: Emergence of anomalous diffusion and Lévy flights*, Physical Review E 90, 032809, first publicly dated 17 September 2014, https://doi.org/10.1103/PhysRevE.90.032809 ; full openly accessible manuscript https://arxiv.org/abs/1506.06167 , especially Sections III–V.
2. A. P. Riascos and J. L. Mateos, *Fractional diffusion on circulant networks: emergence of a dynamical small world*, Journal of Statistical Mechanics (2015) P07015, https://doi.org/10.1088/1742-5468/2015/07/P07015 , especially fractional transport and circulant return-probability calculations.
3. D. Daners, J. Glück and J. B. Kennedy, *Eventually and asymptotically positive semigroups on Banach lattices*, first submitted 17 November 2015, https://arxiv.org/abs/1511.05294 , inspected full-text revised version https://arxiv.org/html/1511.05294v2 , especially introduction and eventual-positivity criteria.
4. *A sharp positivity transition for fractional graph heat on complete multipartite networks*, published published-finding corpus finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-sharp-positivity-transition-for-fractional-graph-heat-on-compl--8af258cef8b1 ; compared full RESULT.md.
