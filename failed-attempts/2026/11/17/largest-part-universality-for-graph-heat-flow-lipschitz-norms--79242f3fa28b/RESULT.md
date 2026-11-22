# Largest-part universality for graph heat-flow Lipschitz norms

## Finding

Let \(G=K_{n_1,\ldots,n_r}\) be any finite, simple, complete multipartite graph, with \(r\ge2\), \(n_i\ge1\), \(N=\sum_i n_i\), and \(M=\max_i n_i\). Give each edge length one, write \(d\) for shortest-path distance, and let \(L=D-A\) be the **unnormalized** combinatorial Laplacian. For real vertex functions, let
\[
\operatorname{Lip}(f)=\max_{uv\in E(G)}|f(u)-f(v)|,\qquad H_t=\exp(-tL),\quad t\ge0.
\]
The exact induced norm on functions modulo constants is
\[
\boxed{\quad\|H_t\|_{\mathrm{Lip}\to\mathrm{Lip}}
=e^{-Nt}\left[1+\frac{2(M-1)}{M}(e^{Mt}-1)\right].\quad} \tag{1}
\]
More precisely, if the endpoints of an edge belong to parts of sizes \(a,b\), its exact Lipschitz-dual heat-kernel difference equals
\[
\boxed{\quad W_1(H_t(u,\cdot),H_t(v,\cdot))
=e^{-Nt}\left[1+\frac{2(h-1)}{h}(e^{ht}-1)\right],\quad h=\max\{a,b\}.\quad} \tag{2}
\]
Here \(W_1\) is the graph-distance transportation cost. For \(t>0\), the norm is attained across any edge incident to a largest part. In particular, **every complete multipartite graph with the same order and largest part has the same entire sharp Lipschitz heat-flow profile**, regardless of its other part sizes or number of parts.

The semigroup is nonexpansive for every \(t\ge0\) exactly when \(2M\le N+2\). If \(2M>N+2\), it has a unique positive amplification peak at
\[
t_* =\frac1M\log\frac{N(M-2)}{2(N-M)(M-1)},
\qquad
\|H_{t_*}\|_{\mathrm{Lip}\to\mathrm{Lip}}
=\frac{2(M-1)}N
\left[\frac{2(N-M)(M-1)}{N(M-2)}\right]^{(N-M)/M}>1. \tag{3}
\]
In the nonexpansive regime the norm decreases strictly for \(t>0\). In the expansive regime it increases strictly until \(t_*\), decreases strictly afterwards, and crosses the value one at exactly one positive time later than \(t_*\). For fixed order \(N\), (1) is strictly increasing in \(M\) at every \(t>0\), so the clique minimizes and the star maximizes the sharp norm among complete multipartite graphs.

If \(M/N\to\alpha\) along multipartite graphs with \(N\to\infty\), the peak constants converge to
\[
\mathcal C(\alpha)=
\begin{cases}
1,&0\le\alpha\le\frac12,\\
2\alpha[2(1-\alpha)]^{(1-\alpha)/\alpha},&\frac12<\alpha<1,\\
2,&\alpha=1.
\end{cases} \tag{4}
\]
Consequently the universal supremum of the peak amplification over this family is \(2\), not attained by a finite graph. It is approached with a fixed number of vertices outside a largest part and the largest part tending to infinity.

## Assumptions and scope

All graphs in the theorem are connected complete multipartite *simple* graphs with at least two nonempty parts. Edge lengths and conductances are one, vertex measure is counting measure, and the generator is the unnormalized operator \(L=D-A\), not the degree-normalized random-walk Laplacian. The norm is on **real** functions modulo constants; graph-distance Lipschitz norm equals the maximum edge increment. Every formula covers single-vertex parts, the complete graph, and the two-vertex graph. At \(t=0\), the norm is one.

## Proof

**1. Exact spectral heat kernel.** Let \(C_i\) be a part of size \(n_i\) and let \(1_{C_i}\) be its indicator. The space of vertex functions is the orthogonal sum of global constants, block-constant mean-zero functions, and mean-zero functions on each \(C_i\). The corresponding Laplacian eigenvalues are \(0\), \(N\), and \(N-n_i\), respectively. Thus, for \(u\in C_i\), the \(u,w\) entry of the heat kernel is
\[
H_t(u,w)=\frac1N+e^{-Nt}\left(\frac{1_{C_i}(w)}{n_i}-\frac1N\right)
+e^{-(N-n_i)t}\left(1_{\{u\}}(w)-\frac{1_{C_i}(w)}{n_i}\right). \tag{5}
\]
This identity is valid even if \(n_i=1\), when the last bracket vanishes. It follows either by the stated orthogonal decomposition or by checking initial data and the heat equation.

**2. Exact transport for one edge.** Fix \(u\in C_i\), \(v\in C_j\), \(i\ne j\), and write \(a=n_i\ge b=n_j\), \(x=e^{-(N-a)t}\), \(y=e^{-(N-b)t}\), \(z=e^{-Nt}\). Then \(x\ge y\ge z\). By subtracting (5), the signed measure \(H_t(u,\cdot)-H_t(v,\cdot)\) is supported on the two parts: it has a positive mass
\(P=((a-1)x+z)/a\) at \(u\), a negative total mass \(R=(a-1)(x-z)/a\) on \(C_i\setminus\{u\}\), a negative mass \(S=((b-1)y+z)/b\) at \(v\), and a positive total mass \(Q=(b-1)(y-z)/b\) on \(C_j\setminus\{v\}\). These totals obey \(P+Q=R+S\). Moreover
\[
ab(P-S)=b(a-1)(x-y)+(a-b)(y-z)\ge0. \tag{6}
\]
Transport \(S\) units from \(u\) to \(v\) (unit cost), \(Q\) units from \(C_j\setminus\{v\}\) to \(C_i\setminus\{u\}\) (unit cost), and the remaining \(P-S\) units from \(u\) to \(C_i\setminus\{u\}\) (cost two). The receiving masses match because \(R=Q+P-S\). The total cost is \(S+Q+2(P-S)=P+R\). All these edges or length-two paths exist in the graph. When a listed mass is zero, the corresponding shipment is omitted.

The 1-Lipschitz potential \(f(u)=1\), \(f(w)=-1\) for \(w\in C_i\setminus\{u\}\), and \(f(w)=0\) elsewhere pairs with the signed measure to give \(P+R\). Hence Kantorovich duality proves the transport plan is optimal and
\[
W_1= P+R=\frac{2(a-1)}a e^{-(N-a)t}-\frac{a-2}a e^{-Nt}
=e^{-Nt}\left[1+\frac{2(a-1)}a(e^{at}-1)\right]. \tag{7}
\]
Interchanging the parts if necessary yields (2). This argument includes \(a=b=1\).

**3. Global norm and extremizers.** On any connected graph, the Lipschitz seminorm is the maximum edge increment, and finite-dimensional Kantorovich duality gives
\[
\|H_t\|_{\mathrm{Lip}\to\mathrm{Lip}}
=\max_{uv\in E(G)}W_1(H_t(u,\cdot),H_t(v,\cdot)). \tag{8}
\]
For fixed \(t>0\), the factor \((1-1/h)(e^{ht}-1)\) is strictly increasing over positive integers \(h\) (its two nonnegative factors are nondecreasing and the second is strictly increasing). The largest possible edge endpoint class has size \(M\). Equations (2) and (8) establish (1). When \(M\ge2\), the potential used above, with \(C_i\) a largest part, is an explicit norming input; for \(M=1\), every nonconstant Lipschitz input norms \(H_t=e^{-Nt}\) on the mean-zero quotient.

**4. Time transitions.** Put \(q=N-M\ge1\). The right side of (1) is
\[
F(t)=\frac{2(M-1)}M e^{-qt}-\frac{M-2}{M}e^{-Nt}. \tag{9}
\]
Its initial derivative is \(F'(0)=2M-N-2\). When \(M=1\) or \(M=2\), (9) is strictly decreasing. For \(M>2\), its derivative has the same sign as
\[
\frac{N(M-2)}{2q(M-1)}e^{-Mt}-1. \tag{10}
\]
The prefactor in (10) exceeds one precisely when \(2M>N+2\). This proves the nonexpansivity classification, strict unimodality, the unique peak time, and the formula (3) on substituting (10) into (9). In the expansive case, strict decrease after the peak together with \(F(t)\to0\) implies the unique later crossing of one. Pointwise strict monotonicity in \(M\) follows from (1).

**5. Amplification limits.** If \(M/N\to\alpha>1/2\) with \(\alpha<1\), substitute (3), observe \(q/M\to(1-\alpha)/\alpha\) and the bracket base tends to \(2(1-\alpha)\), obtaining the middle branch of (4). For \(\alpha\le1/2\), either the norm is always nonexpansive or the peak excess tends to zero by continuity of the same expression as \(\alpha\downarrow1/2\). If \(M/N\to1\), the logarithm of the bracket in (3), multiplied by \(q/M\), tends to zero, while \(2(M-1)/N\to2\). The universal strict bound \(\|H_t\|<2\) for finite graphs follows from (9) if \(M>2\), while cases \(M\le2\) have peak one. This proves (4) and its sharp endpoint.

## Verification

The accompanying standard-library Python script `verify_multipartite_heat.py` checks the heat-kernel stochasticity and semigroup law in exact rational arithmetic at rational values of \(e^{-t}\). For 15 graph profiles and four rational parameters each, it exhaustively enumerates the **integer vertices** of the anchored Lipschitz potential polytope and checks all edge dual optima, including the proposed exact formula. Integer vertex exhaustiveness is justified by total unimodularity of the oriented incidence constraints with one fixed basepoint; bounded graph diameter restricts every coordinate to the range \([-2,2]\). The output reports 412 exact edge optimizations and 60 exact semigroup checks.

The checker does not prove the infinite family; steps 1–5 give the universal proof. Polynomial identities in \(q=e^{-t}\) and the rational grid are independent computational corroboration, not a formal certificate of all real parameters.

## Relationship to prior work

Ollivier introduced graph-metric \(W_1\) contraction as a curvature perspective for Markov kernels (arXiv:math/0701886, first posted January 30, 2007). Lin, Lu, and Yau developed graph Ricci curvature using lazy *degree-normalized* random walks and studied graph products, diameter and spectrum (Tohoku Math. J. 63 (2011), 605–627). Münch and Wojciechowski proved a general connection between graph Laplacian curvature and continuous-time heat-semigroup Lipschitz bounds (arXiv:1712.00875, December 2017). These results justify the geometric motivation and the duality in (8), but their general upper bounds or infinitesimal curvature statements do not give the all-time **sharp unnormalized complete-multipartite profile**, its largest-part universality, its exact peak, or the macroscopic amplification law.

The previously obtained exact star heat-flow constant is precisely the special case \(G=K_{1,M}\) of (1). It is not a new result of this statement. The new content is the complete multipartite classification, the independence from all smaller class sizes, the edge-local formula, and the exact comparison across graphs at fixed order. No exhaustive publication-priority assertion is made.

## Limitations

The proof requires unweighted, undirected, simple complete multipartite graphs, counting measure, the unnormalized Laplacian, and real-valued Lipschitz functions. It does **not** give the corresponding profile for degree-normalized heat kernels, arbitrary weighted or multipartite-incomplete graphs, nonlinear heat flows, or other norms. Priority relative to unindexed explicit graph heat-kernel calculations remains a bibliographic risk.

## References

1. Yann Ollivier, *Ricci curvature of Markov chains on metric spaces*, arXiv:math/0701886 (first submitted 2007-01-30); Journal of Functional Analysis 256 (2009), 810–864. https://arxiv.org/abs/math/0701886
2. Yong Lin, Linyuan Lu, Shing-Tung Yau, *Ricci curvature of graphs*, Tohoku Mathematical Journal 63 (2011), 605–627, DOI:10.2748/tmj/1325886283. https://www.jstage.jst.go.jp/article/tmj/63/4/63_605/_article/-char/en
3. Florentin Münch, Radosław K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875 (first submitted 2017-12-04). https://arxiv.org/abs/1712.00875
