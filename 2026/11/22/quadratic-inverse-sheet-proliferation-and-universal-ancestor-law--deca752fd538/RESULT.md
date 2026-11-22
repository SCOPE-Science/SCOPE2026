# Quadratic inverse-sheet proliferation and universal ancestor law in a coupled cosine–sine map

## Finding

The two-dimensional logistic–sine cosine map of Yang, Chang, Feng, Li, Chen and Zhang [1, Equation (6)] has a uniform small-parameter inverse-fiber asymptotic and a universal spatial distribution for its ancestors. In the notation defined below, for every interior target \((u,v)\in(-1,1)^2\), the number of *distinct* source preimages in the invariant square satisfies

\[
N_b(u,v)=\frac{256}{\pi b^2}+O(b^{-1})\quad(b\downarrow0).
\]

The error constant is absolute: it is independent of the target and of all phase and coupling parameters. If \(\nu_b^{u,v}\) denotes the uniform probability on this finite inverse fiber, then, with Euclidean-ground-metric Wasserstein distance,

\[
W_1\bigl(\nu_b^{u,v},\mu\otimes\mu\bigr)=O(b),\qquad
\mu(dt)=\frac{\pi}{4}|\cos(\pi t)|\,\mathbf1_{[-1,1]}(t)\,dt.
\]

The latter error constant is also absolute and uniform. Moreover, at most \(O(b^{-1})\) inverse points have singular Jacobian, so the regular inverse fraction tends to one with error \(O(b)\). The theorem concerns one-step inverse images, *not* periodic points or forward-invariant distributions.

## Assumptions and scope

Let \(a,\alpha_1,\alpha_2\in\mathbb R\), \(b>0\), and \(H=4/b\). On \(Q=[-1,1]^2\), take the map **exactly as printed in [1, Equation (6)]**, with the placements of \(\pi\) respected:

\[
\begin{aligned}
u &= \cos\!\left(\pi H\sin(\pi x)+a y(1-y)+\alpha_1\right),\\
v &= \cos\!\left(\pi a u(1-u)+H\sin(\pi y)+\alpha_2\right).
\end{aligned}
\]

Write \(F_b(x,y)=(u,v)\). Cosine boundedness makes \(F_b(Q)\subseteq Q\). The parameter \(a\) and phase shifts may be arbitrary, even dependent on \(b\), because all estimates below are uniform in phase; the target lies in the open square to exclude coinciding cosine phase branches. The count \(N_b(u,v)\) is the cardinality of \(F_b^{-1}(u,v)\cap Q\), without algebraic multiplicity. The Wasserstein distance uses the Euclidean cost on \(Q\); convergence statements concern inverse-fiber empirical laws, not physical measures of forward iteration.

## Proof

**1. Uniform scalar inverse lemma.** Let \(K>0\), \(\delta\in\mathbb R\), \(t\in(-1,1)\), and

\[
E_{K,\delta,t}=\{z\in[-1,1]:\cos(K\sin(\pi z)+\delta)=t\}.
\]

Write \(\theta=\arccos(t)\in(0,\pi)\). The exact phase equations are

\[
K\sin(\pi z)=2\pi k+\sigma\theta-\delta,
\qquad k\in\mathbb Z,\ \sigma\in\{-1,1\}.
\]

The two progressions are disjoint because \(0<\theta<\pi\). Each of the four monotonicity intervals of \(\sin(\pi z)\) on \([-1,1]\) maps onto either \([-1,0]\) or \([0,1]\). In the phase coordinate \(s=\sin(\pi z)\), the two progressions have spacing \(2\pi/K\) each, giving combined density \(K/\pi\) per unit \(s\). Consequently each monotonicity interval contributes its length in \(s\), namely 1, times \(K/\pi\), up to an absolute \(O(1)\) endpoint error. Shared boundaries such as \(s=0\) are identified rather than double-counted, affecting only a bounded number of points. Hence

\[
\#E_{K,\delta,t}=\frac{4K}{\pi}+O(1)
\]

uniformly over \(K,\delta,t\) as \(K\to\infty\). More generally, for every real 1-Lipschitz \(g\colon[-1,1]\to\mathbb R\) with \(g(0)=0\), an equally spaced grid on each monotone branch has bounded-variation quadrature error \(O(1)\): the composition of \(g\) with the inverse sine branch has variation at most the length of that branch. Adding the four branches and the two phase progressions yields

\[
\sum_{z\in E_{K,\delta,t}}g(z)
=K\int_{-1}^1 g(z)|\cos(\pi z)|\,dz+O(1),
\]

uniformly in the same parameters. Dividing by the count proves the quantitative 1D bounded-Lipschitz, hence \(W_1\), approximation to \(\mu\) at rate \(O(K^{-1})\). (An arbitrary 1-Lipschitz function may be centered at 0, which does not change the difference of expectations.)

**2. Exact triangular inverse construction.** Fix \((u,v)\in(-1,1)^2\). The second target equation depends on the first *target* coordinate \(u\), not on the unknown first *source* coordinate \(x\). Therefore its complete set of source \(y\)-values is

\[
Y=E_{H,\,\pi a u(1-u)+\alpha_2,\,v},\qquad
\#Y=\frac{4H}{\pi}+O(1).
\]

For every \(y\in Y\), the complete set of compatible source \(x\)-values is

\[
X_y=E_{\pi H,\,a y(1-y)+\alpha_1,\,u},\qquad
\#X_y=4H+O(1),
\]

with errors independent of \(y\), including any dependence of \(a\) or phase shifts on \(b\). Every pair \((x,y)\) with \(y\in Y\) and \(x\in X_y\) is a preimage, and every preimage arises exactly once. Thus

\[
N_b(u,v)=\sum_{y\in Y}\#X_y
=\left(\frac{4H}{\pi}+O(1)\right)(4H)+O(H)
=\frac{16H^2}{\pi}+O(H)
=\frac{256}{\pi b^2}+O(b^{-1}).
\]

In particular, every interior target is attained for all sufficiently small positive \(b\), uniformly over the other parameters.

**3. Product ancestor law.** Let \(\varphi:Q\to\mathbb R\) be 1-Lipschitz with \(\varphi(0,0)=0\). For each fixed \(y\), apply the scalar quadrature estimate to \(x\mapsto\varphi(x,y)\), after removing the value at \(x=0\). This gives

\[
\frac{1}{\#X_y}\sum_{x\in X_y}\varphi(x,y)
=\int_{-1}^{1}\varphi(x,y)\,d\mu(x)+O(H^{-1})
\]

uniformly in \(y\). Since \(\#X_y=4H+O(1)\), weighting the \(y\)-points by their cardinalities rather than uniformly changes the average of bounded \(\varphi\) by at most \(O(H^{-1})\). The function \(y\mapsto\int\varphi(x,y)\,d\mu(x)\) is 1-Lipschitz. Applying the scalar quadrature estimate to the \(y\)-set \(Y\) gives a second \(O(H^{-1})\) error. Therefore

\[
\left|\int_Q \varphi\,d\nu_b^{u,v}
-\int_Q\varphi\,d(\mu\otimes\mu)\right|=O(H^{-1}).
\]

The Kantorovich–Rubinstein duality on compact \(Q\) and \(H=4/b\) prove the asserted uniform \(W_1\) bound.

**4. Regular inverse sheets.** Put \(A=\pi H\sin(\pi x)+a y(1-y)+\alpha_1\) and \(B=\pi a u(1-u)+H\sin(\pi y)+\alpha_2\). The chain-rule terms involving \(u_y\) cancel in the determinant, leaving

\[
\det DF_b(x,y)=\pi^3H^2\cos(\pi x)\cos(\pi y)\sin A\sin B.
\]

For an interior target, \(\sin A\) and \(\sin B\) are nonzero. Hence singularity occurs only at \(x=\pm1/2\) or \(y=\pm1/2\). For each of the \(O(H)\) possible \(y\)-values there are at most two such critical \(x\)-values. Each of the two special critical \(y\)-values can accompany only \(O(H)\) valid \(x\)-values. The total singular count is \(O(H)=O(b^{-1})\), and division by \(N_b=\Theta(H^2)\) gives a regular fraction \(1-O(b)\).

## Verification

The accompanying standalone `verify_inverse.py` enumerates both cosine phase lattices and the sine inverse branches in the source square, checks direct substitution into the **printed** two-dimensional formula, compares finite counts with the predicted scaling, and compares second coordinate moments with quadrature of the proposed limiting density. Its fixed tests exercise 95 parameter configurations and 70,328 directly substituted inverse points, plus four finer-scale empirical laws. Run with `python3 verify_inverse.py` using the standard library. These floating-point tests illustrate, but do not establish, the infinite-limit and uniform-quantifier claims; those follow from the scalar grid proof above.

## Relationship to prior work

Yang et al. [1] construct the 2D-LSM map as an example of their cosine-transform coupling model and analyze forward trajectories, Lyapunov exponents, permutation entropy, and data-hiding performance. Their Equation (6) supplies the exact map analyzed here, but its published analysis does not state the inverse-fiber scaling, limiting ancestor measure, or asymptotic regularity fraction.

The general inverse-branch density calculus for sine and cosine functions explains local branch inversions, but it does not itself supply the uniform two-dimensional result and coefficient for this particular sequentially coupled map. Other reported inverse-fiber results for polynomial Gumowski–Mira rings, cosine-memristive Chialvo maps, and reciprocal sine-square coupled maps concern distinct source domains, singularities, and maps: their results do not imply the quadratic \(b^{-2}\) law here. Broad general oscillatory-map theorems and unindexed equivalent treatments remain publication-priority risks.

## Limitations

This is an exact-real deterministic statement for one-step inverse fibers of the literal displayed map on \(Q\). It does not assert that \(\nu_b^{u,v}\) is forward invariant, that physical orbit distributions converge to \(\mu\otimes\mu\), or that numerical encryption is secure. The small-\(b\) asymptotic does not give an exact count at arbitrary fixed \(b\); its \(O(b^{-1})\) term accounts for lattice endpoints and phase offsets. For targets on the boundary \(u=\pm1\) or \(v=\pm1\), the two cosine phase progressions merge, so the interior-target theorem does not directly apply. Independent mathematical validation and a comprehensive publication-priority review have not been performed.

## References

1. Y. Yang, R. Chang, X. Feng, P. Li, Y. Chen, and H. Zhang, “An n-Dimensional Chaotic Map with Application in Reversible Data Hiding for Medical Images,” *Entropy* 26 (2024), article 254, published 13 March 2024. DOI: https://doi.org/10.3390/e26030254. In particular, Section 2.2.1, Equation (6), and Sections 2.3–4.
2. Elementary bounded-variation grid quadrature and Kantorovich–Rubinstein duality (standard analytic tools; no priority asserted for these ingredients).
