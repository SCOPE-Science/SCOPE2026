# The smallest nonflat Fisher geometry of an absorbing reversible random walk

## Finding

Consider the **complete first-hitting-time distribution** of a discrete-time, nearest-neighbor random walk on a connected simple undirected graph, with positive symmetric edge weights, one absorbing vertex, one fixed transient starting vertex, and edge-log parameters. Equip its identifiable parameter family with the ordinary expected Fisher information of the **entire** hitting-time random variable, normalized without an additional factor of four.

**Theorem (sharp graph-size boundary).** On any graph with at most three vertices, this Fisher metric, wherever nonsingular of dimension two, is flat. A three-vertex triangle already has rank-two information from a single starting vertex, so a universal rank-one claim fails at the smallest possible graph size. There exists a four-vertex *path*, with only two independent log-edge parameters, for which the full-law Fisher metric is everywhere positive definite and has constant Gaussian curvature
\[
K=\frac14.
\]
Thus four vertices are necessary and sufficient for a nonflat two-dimensional full-hitting-time Fisher geometry among the stated undirected graphs. The curvature is intrinsic; it cannot be made zero by reparametrization or null-space quotienting.

Explicitly, take the path \(0-1-2-3\), absorb at \(0\), start at \(1\), and give the edges \((0,1),(1,2),(2,3)\) respective weights \(a,1,b\), with \(a,b>0\). Set
\[
u=\frac{a}{1+a},\qquad v=\frac{1}{1+b},\qquad w=uv.
\]
The log-edge parameters \((\log a,\log b)\in\mathbb R^2\) map diffeomorphically onto \(0<w<u<1\). With \(T\) the first hit of \(0\),
\[
\Pr(T=1)=u,\qquad
\Pr(T=2k+1)=(1-u)w(1-w)^{k-1}\quad(k\ge1),\qquad
\Pr(T=2k)=0\quad(k\ge1).
\]
The complete Fisher information metric and its determinant in coordinates \((u,w)\) are
\[
g=\frac{du^2}{u(1-u)}+\frac{1-u}{w^2(1-w)}\,dw^2,
\qquad \det(g)=\frac{1}{u w^2(1-w)}>0.
\]
At the symmetric weights \(a=b=1\), the Fisher matrix in the actual log-edge coordinates \((\log a,\log b)\) is explicitly
\[
I_{\log a,\log b}=\begin{pmatrix}5/12&-1/6\\-1/6&1/6\end{pmatrix},\qquad\det I=1/24>0.
\]
In particular, the full hitting-time law identifies both log-edge parameters. Its exact Kullback--Leibler divergence between interior points \((u,w)\) and \((u',w')\) is
\[
\begin{aligned}
D_{\mathrm{KL}}&=u\log\frac{u}{u'}+(1-u)\log\frac{1-u}{1-u'}\\
&\quad +(1-u)\left[\log\frac{w}{w'}+\frac{1-w}{w}\log\frac{1-w}{1-w'}\right].
\end{aligned}
\]
These exact formulas form one joint structural finding: a graph-size-minimal curved absorption-time statistical manifold, with an explicit contrast to the smallest full-rank but flat case.

## Assumptions and scope

The graph is finite, connected, simple, undirected, and has strictly positive symmetric edge weights and no self-loops. At a chosen single vertex, absorption replaces its outgoing transition row by a point mass. Other transition probabilities are edge weight divided by weighted degree. The starting vertex and absorbing vertex are fixed and distinct; only the first-hit time is observed, not the path. All parameters are interior and normalized by fixing an arbitrary overall edge-weight scale. Fisher information means
\[
I_{ij}(\theta)=\sum_{t:\Pr_\theta(T=t)>0}
\Pr_\theta(T=t)\,
\partial_i\log\Pr_\theta(T=t)\,
\partial_j\log\Pr_\theta(T=t).
\]
For finite connected graphs with positive weights, absorption is almost sure with geometric tails. All derivatives and sums below converge absolutely on compact subsets of parameter space. We make **no** assertion of a global classification of all four-vertex weighted graphs, multiple absorbing classes, observation of entire paths, or a different information metric.

## Proof

**1. Four-vertex first-hit law.** At vertex \(1\), the walk absorbs with probability \(u\) or reaches vertex \(2\) with probability \(1-u\). Starting at vertex \(2\), the probability of reaching vertex \(1\) before a return to vertex \(2\) is \(v\) in one step; otherwise the excursion is \(2\to3\to2\). The probability of a successful two-step \(2\to1\to0\) attempt is \(uv=w\), with each failed two-step attempt returning to \(2\). Hence the displayed probability masses, with \(k-1\) failures before success for \(k\ge1\). Equivalently the generating function is
\[
\mathbb E[z^T]=zu+\frac{(1-u)wz^3}{1-(1-w)z^2}.
\]
Since \(w\in(0,u)\), both geometric and atom masses are strictly positive. The masses sum to one, and the first and third masses identify \(u\) and \(w\): \(u=\Pr(T=1)\), \(w=\Pr(T=3)/(1-u)\). Recover \(a=u/(1-u)\), \(b=u/w-1\), proving full identifiability and the claimed diffeomorphism.

**2. Fisher tensor and divergence.** The event \(T=1\) is Bernoulli with probability \(u\). Given \(T>1\), the integer \((T-3)/2\) has geometric-failures law \(\Pr(J=j)=w(1-w)^j\), \(j\ge0\). The log likelihood therefore splits into a Bernoulli likelihood and, with frequency \(1-u\), a geometric likelihood. The Bernoulli Fisher information is \(1/[u(1-u)]\), and the geometric information for one observation is \(1/[w^2(1-w)]\), with cross score expectation zero. This gives the displayed diagonal tensor, its strictly positive determinant, and the KL expression by the same conditional factorization. This is an exact identity of the **full** first-hit-time laws, not an observed rank-one outer product for a fixed time.

**3. Curvature.** Define interior smooth coordinates
\[
x=2\arcsin\sqrt{u},\qquad
y=\log\frac{1-\sqrt{1-w}}{1+\sqrt{1-w}}.
\]
Direct differentiation gives \(dx/du=[u(1-u)]^{-1/2}\) and \(dy/dw=[w\sqrt{1-w}]^{-1}\), hence
\[
g=dx^2+\cos^2(x/2)\,dy^2.
\]
For a two-dimensional warped metric \(dx^2+f(x)^2dy^2\), its Gaussian curvature is \(-f''(x)/f(x)\). With \(f(x)=\cos(x/2)>0\) the result is \(K=1/4\) at every interior parameter. This is a local spherical metric of radius \(2\), not a claim of a global isometric embedding into a spherical patch.

**4. Sharp minimality and rank-two triangle.** On at most two vertices, there is no two-dimensional hitting-time family. Any connected simple three-vertex graph is a path or triangle. A three-vertex path has, after fixing overall scale, only one edge-weight ratio; for a single absorbing target its first-hit-time law consequently has at most one identifiable parameter. For the triangle \(0-1-2-0\), absorb at \(0\), start at \(1\), assign respective edge weights \(a,1,c\), and put \(u=a/(1+a)\), \(v=c/(1+c)\), \(s=(1-u)(1-v)\). Its first-hit masses are
\[
\Pr(T=2j+1)=us^j,\qquad
\Pr(T=2j+2)=(1-u)v s^j,\qquad j\ge0.
\]
Set \(d=1-s=u+(1-u)v\) and \(r=u/d\), a diffeomorphism from \((u,v)\in(0,1)^2\) onto \((r,d)\in(0,1)^2\). The observed pair \((\lfloor(T-1)/2\rfloor,\ T\bmod2)\) consists of **independent** geometric-failures count with success probability \(d\) and Bernoulli odd-parity indicator with success probability \(r\). Therefore
\[
g_\triangle=\frac{dr^2}{r(1-r)}+\frac{dd^2}{d^2(1-d)}.
\]
Both terms admit independent one-dimensional arclength coordinates, so this rank-two metric is globally flat. Every dimension-two full-law Fisher metric on up-to-three-vertex graphs is therefore flat, and the four-vertex path is a smallest nonflat example. This proves all claims.

## Verification

The accompanying standalone `check.py` computes first-hit probabilities by exact-rational transition recursion for 25 sets of weights each for the path and triangle, at 64 successive times each. It compares the complete finite prefixes against independent closed-form laws; it also checks normalizations and the geometric score-moment identities, and uses symbolic differentiation to calculate Gaussian curvature in two different coordinate presentations. Executing it returned `PASS: 3296 exact rational/symbolic checks`. The infinite-time formulas are proved above by renewal/factorization and geometric-series summation; the finite checks are corroboration, not a substitute for infinite proof. To reproduce: `python check.py` in an environment with Python 3 and SymPy.

## Relationship to prior work

Kimura, *Information Geometry of Absorbing Markov-Chain and Discriminative Random Walks* (arXiv:2602.08185v1, publicly available February 9, 2026), develops finite reversible log-edge-weight random walks and the first-passage Fisher tensor. Section 3.5 defines the expected full-law Fisher matrix as a sum over hitting times; its subsequent Eq. (6) and Section 4 instead give a rank-one outer-product expression for each seed, and conclude local/global flatness after quotienting. The concrete reversible graph here obeys the stated model assumptions and has full-rank, positively curved *full-law* Fisher geometry. Consequently, the asserted rank-one reduction and flatness do **not** hold for that Fisher definition without additional conditions. The present result is **not** a challenge to first-hit pmf/resolvent formulas or to rank-one information from one single fixed-time event.

Srisuradetchai and Dangsupa (2022, *Thailand Statistician* 21, 93–109) study zero-inflated geometric likelihoods and Fisher estimation. Under the shift \(J=(T-1)/2\), the four-path law is a zero-inflated geometric distribution on \(\{0,1,\ldots\}\): its geometric parameter is \(w\), and its inflation probability is \((u-w)/(1-w)>0\). Thus the **distribution family** and ordinary generic likelihood machinery are not novel. The contribution established here is its specific fully identifiable reversible-graph realization, exact intrinsic curvature, and sharp comparison with all smaller graphs. General Fisher--Rao geometry (e.g. Amari--Nagaoka) provides background but does not by itself determine the induced curvature of this graph-specific two-dimensional submanifold.

## Limitations

This is a finite-graph structural boundary, not a claim of a general curvature formula for every absorbing Markov chain. The curvature normalization is the expected score outer-product metric without Hellinger division by four. The source rank-one formula may be meaningful for a different coarsened observable; that interpretation is separate from the explicitly defined complete first-hit-time Fisher matrix compared here. The full graph-specific historical priority beyond inspected references is not independently certified. All weighted edges must remain positive, and the parameter boundary is excluded. No external independent audit has been performed.

## References

1. M. Kimura, *Information Geometry of Absorbing Markov-Chain and Discriminative Random Walks*, arXiv:2602.08185v1 (February 9, 2026), https://arxiv.org/abs/2602.08185 ; *Information Geometry* 9 (2026), 351–372, https://doi.org/10.1007/s41884-026-00198-3 . Relevant material: §§2.1, 3.5, 4 and Eq. (6), including the full-law Fisher definition on printed page 10.
2. P. Srisuradetchai and K. Dangsupa, *On Interval Estimation of the Geometric Parameter in a Zero-Inflated Geometric Distribution*, *Thailand Statistician* 21 (2023), 93–109 (first publicly dated December 29, 2022), https://ph02.tci-thaijo.org/index.php/thaistat/article/view/248025 . Relevant material: §1 p.94 and §2 on full-likelihood Fisher information.
3. S. Amari and H. Nagaoka, *Methods of Information Geometry*, AMS/OUP (2000), https://doi.org/10.1090/mmono/191 . Background on expected Fisher tensor and information geometry.
