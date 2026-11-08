# Variance-to-skewness reversal of epidemic seeding on a three-agent simplex

## Finding

**Theorem (full three-coordinate basin-boundary transition).** Consider the synchronous deterministic discrete-time mean-field SIS map on a complete three-agent simplex defined below. For each recovery rate \(1/10<\delta<121/400\), its three spatially uniform fixed points are disease-free \(0\), a saddle \(p_-\mathbf1\), and an attracting endemic state \(p_+\mathbf1\), where
\[
p_\pm=\frac9{20}\pm\sqrt{\frac{121}{400}-\delta}.
\]
Every trajectory in the probability cube converges to one of these equilibria. In a neighborhood of \(p_-\mathbf1\), write its initial mean as \(m\), its centered coordinates as \(y_i=x_i-m\), and its variance as \(V=\tfrac13\sum_i y_i^2\). The exact boundary between extinction and persistence is the local stable manifold of the saddle, a symmetric smooth graph
\[
m=p_-+a(\delta)V+O(\|y\|^3),\quad
 a(\delta)=\frac{(3p_--9/10)/4}{\ell^2-\lambda},
\]
where \(\lambda=1+\tfrac12p_-(9/10-2p_-)>1\) and \(\ell=1-\tfrac12[\delta+(1+p_-)/20+p_-]\in(0,1)\). The coefficient \(a\) is positive for \(\delta<7/25\), zero at \(\delta=7/25\), and negative for \(\delta>7/25\). Hence at the same mean exactly \(p_-\), a sufficiently small nonzero initial heterogeneity leads to extinction on the first side, but endemic persistence on the second side.

At the **unique curvature cancellation** \(\delta=7/25\), define the third centered product \(P=y_1y_2y_3\). The basin boundary has the sharper expansion
\[
m=\frac3{10}+\frac{32000000}{46977489}P+O(\|y\|^4).
\]
For every sufficiently small \(t>0\), the two *nonuniform positive* initial conditions
\[
x^{(+)}=(3/10+2t,\ 3/10-t,\ 3/10-t),\qquad
x^{(-)}=(3/10-2t,\ 3/10+t,\ 3/10+t)
\]
have **identical mean** \(3/10\) and **identical variance** \(2t^2\) but opposite terminal outcomes:
\[
F^n(x^{(+)})\longrightarrow(0,0,0),\qquad
F^n(x^{(-)})\longrightarrow(3/5,3/5,3/5).
\]
Thus the first distinction between their epidemic outcomes is the sign of their centered third product, equivalently of the centered third moment for three zero-sum coordinates.

## Assumptions and scope

Let \(x_i\in[0,1]\) be the deterministic mean-field infection probability of agent \(i\in\{1,2,3\}\), and let \(\{i,j,k\}=\{1,2,3\}\). The update is
\[
F_i(x)=x_i+\frac12\left[-\delta x_i+(1-x_i)\left(\frac{x_j+x_k}{20}+x_jx_k\right)\right].
\]
This is the three-vertex simplex specialization of the pairwise-plus-third-order **Euler mean-field map**, with Euler step \(h=1/2\), two incoming pairwise rates \(1/20\) each, and a total triangle rate of one (realized by two ordered third-order coefficients \(1/2\)). The recovery parameter obeys \(1/10<\delta<121/400\). No claims about the exact stochastic finite-agent SIS Markov chain are made. All global statements concern this explicitly defined deterministic map, and all basin-surface expansions are local near the intermediate fixed point.

The map is well-defined on the cube: \(F_i=(1-\delta/2)x_i+\tfrac12(1-x_i)[(x_j+x_k)/20+x_jx_k]\). It takes \([0,1]^3\) to itself because \(0<\delta/2<1\) and the incoming rate is at most \(11/10\), hence its half-step at most \(11/20<1\). All partial derivatives are nonnegative, with a strictly positive own-coordinate derivative; thus \(F\) is order-preserving.

## Proof

**1. Exact contraction of differences and scalar reduction.** Direct subtraction of the equations gives, for distinct \(i,j,k\),
\[
F_i(x)-F_j(x)=\left[1-\frac12\left(\delta+\frac{1+x_k}{20}+x_k\right)\right](x_i-x_j).
\]
The multiplier is positive and at most \(\rho=1-\tfrac12(\delta+1/20)<1\) throughout the cube. Therefore \(\max_{i,j}|x_i(n)-x_j(n)|\le\rho^n\max_{i,j}|x_i(0)-x_j(0)|\). In particular, every equilibrium is spatially uniform, and every trajectory exponentially approaches the diagonal.

Write \(m=\tfrac13\sum_i x_i\), \(y_i=x_i-m\), \(V=\tfrac13\sum_i y_i^2\), and \(P=y_1y_2y_3\). Expanding the three polynomials (or symmetrizing their elementary symmetric functions) yields the **exact, global polynomial identity**
\[
m'=f_\delta(m)+k(m)V-\frac12 P,\qquad
f_\delta(m)=m+\frac12m[-\delta+(1-m)(1/10+m)],\qquad
k(m)=\frac{3m-9/10}{4}.
\]
Because \(y_i(n)=O(\rho^n)\), the correction to the scalar update is \(O(\rho^{2n})\), uniformly along each orbit. The scalar map \(f_\delta:[0,1]\to[0,1]\) is strictly increasing: its derivative is \(1+\tfrac12[-\delta+1/10+(9/5)m-3m^2]\), whose minimum on \([0,1]\) is positive throughout the stated range. The only fixed points of \(f_\delta\) are \(0\) and the roots \(p_\pm\) shown above, with \(0<p_-<p_+<1\).

For completeness, a bounded recursion \(m_{n+1}=f_\delta(m_n)+e_n\), with \(e_n\to0\), must converge whenever \(f_\delta\) is strictly increasing and has only finitely many fixed points. Otherwise, let \(a=\liminf m_n<b=\limsup m_n\). Choose any nonfixed \(c\in(a,b)\). If \(f_\delta(c)>c\), then eventually a trajectory that is at or above \(c\) cannot cross below it on the next step; if \(f_\delta(c)<c\), an eventual crossing from below to above is impossible. Either case contradicts infinitely many visits on both sides of \(c\). Hence \(m_n\) converges; continuity and \(e_n\to0\) force its limit to be a scalar fixed point. The coordinate contraction proves the asserted global trichotomy.

**2. Stable manifold is the basin divider.** The diagonal scalar derivative at the middle fixed point is
\[
\lambda=f_\delta'(p_-)=1+\frac12p_-(9/10-2p_-)>1.
\]
The two independent zero-sum directions have common eigenvalue
\[
\ell=1-\frac12[\delta+(1+p_-)/20+p_-]\in(0,1),
\]
by the exact difference formula. The equilibrium is hyperbolic with a two-dimensional local stable manifold. Because the map is polynomial, locally a diffeomorphism (its eigenvalues are nonzero), and invariant under agent permutations, the stable manifold is a smooth permutation-invariant graph \(m=p_-+g(y)\) with \(g(0)=Dg(0)=0\). Its points converge to \(p_-\mathbf1\).

The graph separates the two other basins near the saddle: for fixed small \(y\), raising \(m\) increases every coordinate. The map preserves coordinatewise ordering. A point strictly above the graph cannot converge to zero, since its iterates dominate those of the graph point converging to \(p_-\mathbf1\); it cannot converge to the saddle unless it belongs to the stable manifold. The global trichotomy thus forces convergence to \(p_+\mathbf1\). The same argument below the graph rules out endemic convergence and saddle convergence, leaving zero. These arguments work in the cube for sufficiently small \(y\) and \(|m-p_-|\).

**3. Quadratic heterogeneity effect.** The quadratic permutation-invariant forms on the plane \(y_1+y_2+y_3=0\) are scalar multiples of \(V\). Thus \(g(y)=aV+O(\|y\|^3)\). To second order, \(y'=\ell y+O(\|y\|^2)\), \(V'=\ell^2V+O(\|y\|^3)\), and the exact mean identity gives \(m'-p_-=\lambda aV+k(p_-)V+O(\|y\|^3)\). Invariance of the graph therefore yields
\[
a\ell^2=\lambda a+k(p_-),\qquad a=\frac{k(p_-)}{\ell^2-\lambda}.
\]
Since \(\ell^2<1<\lambda\), the sign of \(a\) is the opposite of \(3p_--9/10\). The equation \(p_-=3/10\) is equivalent to \(\delta=7/25\); hence the sign reversal is sharp and unique. At mean \(m=p_-\), the signed difference \(m-(p_-+g(y))=-aV+O(\|y\|^3)\) establishes the asserted basin classification for every sufficiently small nonzero centered perturbation when \(a\ne0\).

**4. Critical cubic skewness.** At \(\delta=7/25\), the intermediate fixed point is \(p_-=3/10\), the upper fixed point is \(p_+=3/5\), and
\[
\lambda=209/200,\qquad \ell=271/400,\qquad k(p_-)=0.
\]
The quadratic stable-manifold coefficient vanishes. Every symmetric cubic polynomial in zero-sum triples is a multiple of \(P=y_1y_2y_3\); thus \(g(y)=cP+O(\|y\|^4)\). On this graph, \(m-p_-=O(\|y\|^3)\), so \(k(m)V=O(\|y\|^5)\), while \(P'=\ell^3P+O(\|y\|^4)\). The exact mean identity and graph invariance give
\[
c\ell^3=\lambda c-\frac12,
\qquad c=\frac{1}{2(\lambda-\ell^3)}=\frac{32000000}{46977489}>0.
\]
The two initial triples in the theorem have \(V=2t^2\) and respectively \(P=+2t^3\) and \(P=-2t^3\). Both start at \(m=p_-=3/10\). Therefore, for all sufficiently small \(t>0\), the positive-product triple is strictly **below** the boundary and converges to zero; the negative-product triple is strictly **above** it and converges to \((3/5)\mathbf1\), as claimed. The identity \(y_1^3+y_2^3+y_3^3=3P\) for \(\sum_i y_i=0\) identifies this sign with that of the centered third moment.

## Verification

Run `python3 verify.py` with Python 3.10 or later; no third-party packages are required. The program evaluates the exact polynomial mean identity and all three exact difference identities coefficientwise over rational numbers, verifies the equilibria, tangent Jacobians, curvature coefficients at two sides of the transition and the exact cubic coefficient at criticality, and performs four finite trajectory diagnostics. It returns `VERIFY_OK 72 exact identities/certificates and finite trajectory diagnostics`. The computations corroborate the algebra. The global convergence and infinite-time basin outcomes follow from the preceding proof, **not** from finite simulations. In particular, the critical outcome claim is an all-sufficiently-small-\(t\) theorem, not a claim based on sampled \(t\).

Independent exact-parameter illustrations: at \(\delta=9/50\), \(p_-=1/10\) and \(a=8000/18237>0\); at \(\delta=3/10\), \(p_-=2/5\) and \(a=-1000/8557<0\). These examples check both sides of the unique sign transition.

## Relationship to prior work

Liang, Cui and Liu [1], equations (5)–(7), introduce the discrete-time pairwise-plus-triangle mean-field SIS map on directed weighted hypergraphs, establish sufficient conditions for disease-free and endemic equilibria, and construct sufficient attraction regions. The present model is an exact symmetric three-vertex specialization, not a different stochastic update. Their Section 3 and Appendix provide parameter-based bounds and stability criteria; the exact local stable-manifold expansion, its variance-sign reversal, and the equal-mean/equal-variance opposite-outcome pair are not derived there.

Kiss, Iacopini, Simon and Georgiou [2] give exact stochastic SIS and homogeneous scalar mean-field analyses for complete higher-order networks, including bistability and 3-body versus 4-body effects. Their one-coordinate prevalence bifurcation does not determine an inhomogeneous three-coordinate basin separatrix or its cubic skewness term. Iacopini, Petri, Barrat and Latora [3] establish simplicial contagion and critical-mass effects, but do not provide this specific finite-dimensional Euler-map curvature cancellation. The present result acknowledges bistability as prior knowledge; the new object is the *shape and sign change of the seed-composition basin boundary*.

## Limitations

This theorem is about the deterministic mean-field probability map, which is an approximation to the finite stochastic SIS chain; with only three agents it should not be presented as an accurate empirical stochastic approximation. The explicit coefficients rely on equal triangle and pairwise weights and on \(h=1/2\). The separatrix expansion and identical-mean examples hold for sufficiently small perturbations, not globally for arbitrary infection profiles. Generic literature on cooperative contagion and threshold surfaces could contain equivalent specialized deductions; the checked publications and topical research records did not establish priority exhaustively.

## References

1. L. Liang, S. Cui and F. Liu, *Discrete-time SIS Social Contagion Processes on Hypergraphs*, arXiv:2408.08602v1 (first public 2024-08-16), https://arxiv.org/html/2408.08602v1 ; https://arxiv.org/abs/2408.08602 .
2. I. Z. Kiss, I. Iacopini, P. L. Simon and N. Georgiou, *Insights from exact social contagion dynamics on networks with higher-order structures*, arXiv:2309.12752 (2023), https://arxiv.org/abs/2309.12752 .
3. I. Iacopini, G. Petri, A. Barrat and V. Latora, *Simplicial models of social contagion*, Nature Communications 10, 2485 (2019), https://doi.org/10.1038/s41467-019-10431-6 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC6554271/ .
