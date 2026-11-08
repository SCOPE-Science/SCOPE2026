# Sharp curvature transition and log-periodic flattening of planar bounded-noise attractors

## Finding

For the planar discrete-time dynamics
\[
z_{n+1}=Az_n+\xi_n,\qquad A=\operatorname{diag}(a,b),\quad 0<a<b<1,\quad\|\xi_n\|_2\le\varepsilon,
\]
with fixed \(\varepsilon>0\), let \(K\) denote its unique compact minimal invariant attractor for the full closed noise ball. Define
\[
q=\frac ba>1,\qquad \rho=\frac{b^2}{a},\qquad \sigma=\frac{\log\rho}{\log q}\quad\text{when }\rho>1.
\]
The entire boundary \(\partial K\) is a \(C^2\), strictly convex closed curve. Its curvature \(\kappa\), regarded as a continuous function of the outward unit normal \(u(\theta)=(\cos\theta,\sin\theta)\), is strictly positive at every normal except possibly \(u(0)\) and \(u(\pi)\). At the two exceptional normals it is exactly
\[
\kappa(0)=\kappa(\pi)=\begin{cases}(1-\rho)/\varepsilon,&0<\rho<1,\\0,&\rho\ge1.\end{cases}
\]
Thus \(b^2=a\) is the sharp transition between an everywhere positively curved boundary and a \(C^2\) boundary with exactly two zero-curvature points.

The flattening has a complete sharp asymptotic. At \(\rho=1\),
\[
\lim_{\theta\to0}\kappa(\theta)\log\frac1{|\theta|}=\frac{\log q}{\varepsilon}.
\]
At \(\rho>1\), necessarily \(0<\sigma<1\), and as \(\theta\to0\), with \(t=|\tan\theta|\),
\[
\kappa(\theta)=\frac{t^\sigma}{\varepsilon\,G(\{\log_q(1/t)\})}(1+o(1)),\quad
G(s)=\sum_{j\in\mathbb Z}\frac{\rho^{j-s}}{(1+q^{2(j-s)})^{3/2}}.
\]
Here braces mean fractional part, and \(G\) is a strictly positive, continuous, nonconstant function of period one. In particular, the normalized power law has a genuine logarithmically periodic modulation. The same conclusions hold near the opposite normal \(\pi\) by central symmetry. At the slow-axis normals \(\theta=\pi/2,3\pi/2\), the curvature is
\[\kappa(\pi/2)=\kappa(3\pi/2)=\frac{1-a^2/b}{\varepsilon}>0.\]

## Assumptions and scope

The noise support is the entire closed Euclidean disk of radius \(\varepsilon\) at every iteration; statements concern the deterministic minimal invariant set of this set-valued dynamics, not sample-dependent random pullback attractors. The matrix is diagonal with two unequal **positive** contraction factors, ordered \(0<a<b<1\). The unique invariant compact set satisfies \(K=AK+\overline{B_\varepsilon(0)}\). The angle \(\theta\) labels the outward normal, not arclength. At a point with positive curvature, \(\kappa=1/R\), where \(R\) is the radius of curvature; at a flat point this notation means its continuous extension \(\kappa=0\).

The statement of the logarithmically periodic asymptotic is uniform as the fractional logarithmic phase varies in \([0,1]\). All limits are for fixed admissible parameters. Neither arbitrary linear maps nor nonlinear perturbations are covered.

## Proof

**1. Exact convex support.** The set operator \(S\mapsto AS+\overline{B_\varepsilon(0)}\) is a contraction in Hausdorff distance with factor \(b<1\). Its unique compact fixed set is the convergent Minkowski sum
\[
K=\sum_{n=0}^\infty A^n\overline{B_\varepsilon(0)}.
\]
Every nonempty compact forward-invariant set contains this fixed set by iteration and compactness; this also identifies the natural minimal attractor. The support function is consequently
\[
h(\theta)=\varepsilon\sum_{n=0}^\infty \sqrt{a^{2n}\cos^2\theta+b^{2n}\sin^2\theta}.
\]
Each summand has derivative with absolute value at most \(\varepsilon b^n\), so \(h\in C^1(\mathbb R/2\pi\mathbb Z)\), uniformly by the Weierstrass test. The unique point with normal \(u(\theta)\) is
\[
r(\theta)=h(\theta)u(\theta)+h'(\theta)v(\theta),\qquad v(\theta)=(-\sin\theta,\cos\theta).
\]
Uniqueness follows also by summing the unique support points of the strictly convex ellipses (the disk term already has unique support); continuity follows from the convergent support-point series. The disk term gives a strictly positive lower bound on the radius wherever computed; strict convexity follows from uniqueness of the support point in every direction, which holds because every elliptical summand has a unique support point and their point series converges absolutely.

**2. Curvature formula away from the fast-axis normals.** If \(c=\cos\theta\) and \(s=\sin\theta\), the \(n\)-th support summand has curvature radius
\[
(h_n+h_n'')(\theta)=\varepsilon\frac{a^{2n}b^{2n}}{(a^{2n}c^2+b^{2n}s^2)^{3/2}}.
\]
This follows by differentiating the square root twice and using the algebraic identity \(W^2+WW''/2-(W')^2/4=a^{2n}b^{2n}\), where \(W=a^{2n}c^2+b^{2n}s^2\). For \(s\ne0\), the differentiated series converges locally uniformly: each displayed summand is bounded by \(\varepsilon |s|^{-3}(a^2/b)^n\), with \(a^2/b<1\). Consequently \(r'=Rv\) and
\[
R(\theta)=\varepsilon\sum_{n=0}^\infty\frac{\rho^n}{(c^2+q^{2n}s^2)^{3/2}},\qquad s\ne0.
\]
The series is finite and strictly positive there; \(r\) is smooth on those arcs. The usual planar curvature calculation gives \(\kappa=R^{-1}\). In particular, substituting \(c=0\) gives \(R(\pi/2)=\varepsilon/(1-a^2/b)\).

**3. Passage through the fast-axis points and global \(C^2\) regularity.** As \(\theta\to0\), if \(\rho<1\), dominated convergence in the radius series gives \(R\to\varepsilon/(1-\rho)\). If \(\rho\ge1\), every fixed summand tends to \(\varepsilon\rho^n\), and positivity plus Fatou's lemma gives \(R\to+\infty\). Thus the reciprocal radius \(R^{-1}\) has a continuous finite limit, whether or not the support function has a bounded second normal-angle derivative.

This suffices to prove actual geometric \(C^2\) regularity, which must **not** be confused with \(C^2\) regularity of \(h\). Write \(r=(X,Y)\) near \(\theta=0\). Off the axis,
\[
\frac{dY}{d\theta}=R\cos\theta>0,\qquad
\frac{dX}{dY}=-\tan\theta,\qquad
\frac{d^2X}{dY^2}=-\frac1{R\cos^3\theta}.
\]
The series defining \(r\) converges continuously at \(\theta=0\); integrating on a one-sided interval gives a strictly monotone graph coordinate \(Y\) with \(Y\to0\). The tangent slope tends to zero and the second graph derivative tends continuously to \(-1/R(0)\) (zero if \(R(0)=+\infty\)). The left arc matches by reflection \(Y\mapsto -Y\), yielding a \(C^2\) graph at the tip. The same applies at \(\theta=\pi\), completing global \(C^2\) regularity. For \(\rho\ge1\), \(h''\) cannot be continuous at the two tips, since the positive curvature-radius series diverges there; this is no contradiction because normal-angle parametrization degenerates at zero curvature.

**4. The logarithmic threshold.** Let \(t=|\tan\theta|\). The radius formula becomes
\[
\frac{R(\theta)}\varepsilon=(1+t^2)^{3/2}\sum_{n\ge0}\frac{\rho^n}{(1+q^{2n}t^2)^{3/2}}.
\]
When \(\rho=1\), put \(L=\log_q(1/t)\) and split the sum at \(\lfloor L\rfloor\). The terms more than a fixed distance below \(L\) differ from one by a geometrically summable quantity \(O(q^{-2(L-n)})\); the terms above \(L\) total \(O(\sum_{j\ge0}q^{-3j})\). Uniformly for the fractional part of \(L\),
\[
\sum_{n\ge0}(1+q^{2(n-L)})^{-3/2}=L+O(1).
\]
Therefore \(R(\theta)=\varepsilon\log(1/t)/\log q+O(1)\). As \(t/|\theta|\to1\), its reciprocal yields the asserted critical limit.

**5. The supercritical log-periodic law.** Assume \(\rho>1\). Since \(\rho/q=b<1\), \(0<\sigma<1\). Write \(L=\log_q(1/t)=k+s\) with integer \(k=\lfloor L\rfloor\), \(s\in[0,1)\). The expression from step 4 gives
\[
\frac{R(\theta)}{\varepsilon\rho^{k+s}}=(1+t^2)^{3/2}\sum_{j\ge-k}\frac{\rho^{j-s}}{(1+q^{2(j-s)})^{3/2}}.
\]
The omitted negative tail is uniformly \(O(\rho^{-k})\); the positive tail is uniformly geometrically bounded by a multiple of \((\rho/q^3)^j\), since \(0<\rho/q^3=a^2/b<1\). Hence this converges to \(G(s)\), uniformly for \(s\in[0,1]\). Also \(\rho^{-(k+s)}=t^\sigma\), proving the stated asymptotic and positivity/continuity/periodicity of \(G\).

Finally the first nonzero Fourier coefficient of \(G\) is
\[
\widehat G(1)=\frac{1}{2\log q}\,
B\!\left(\frac\sigma2+\frac{\pi i}{\log q},\frac{3-\sigma}{2}-\frac{\pi i}{\log q}\right),
\]
by integrating the periodization and substituting \(u=q^{2x}\). Both beta-function arguments have positive real parts; the identity \(B(z,w)=\Gamma(z)\Gamma(w)/\Gamma(z+w)\) and the absence of zeros of \(\Gamma\) show that \(\widehat G(1)\ne0\). Thus \(G\) is genuinely nonconstant. Central symmetry transfers all tip statements to \(\pi\).

## Verification

The accompanying standard-library checker `check_curvature.py` performs 120 exact-rational evaluations of the decisive ellipse curvature identity and 30 auxiliary floating-point tests of the two equivalent radius formulas, axis curvatures, critical logarithmic scaling, and supercritical periodic-phase limit. Run `python3 check_curvature.py` from the directory holding the extracted files. The checker is finite corroboration only: the uniform series convergence, \(C^2\) gluing, and nonconstant modulation are established analytically above.

## Relationship to prior work

Lamb, Rasmussen, and Tey (2023, [1]) prove the existence, uniqueness, strict convexity and \(C^1\) boundary of these bounded-noise attractors for general contracting invertible linear maps; their Section 5 explicitly identifies precise boundary smoothness and the need for \(C^2\) as an open issue. Tey's 2022 thesis [2], Chapter 4, explicitly conjectures \(C^2\) regularity and considers diagonal examples but does not state a curvature phase diagram. The smooth-persistence result [3] assumes higher regularity/hyperbolicity rather than proving it for the present family. The later boundary-map classification [4] concerns periodic normal directions and Morse–Smale dynamics, not the curvature threshold. Formulas for **finite** Minkowski sums of ellipsoids [5] give antecedents for the support-point calculus but do not resolve the infinite-sum zero-curvature threshold, critical logarithm, or nonconstant scaling profile. Only this explicit planar diagonal subfamily is asserted to settle the regularity question; no claim of global originality over every possible unpublished source is made.

## Limitations

The conclusion concerns the exact closed-ball support; a noise law supported on a proper subset of the disk can give a different attractor. The proof needs two distinct positive diagonal eigenvalues; general normal, complex, negative, defective and nonnormal matrices are not classified. The boundary is \(C^2\) even when its normal-angle support function is not \(C^2\); no \(C^3\) regularity classification is claimed. The formula does not imply persistence of \(C^2\) regularity under nonlinear perturbations, which requires additional hypotheses. Priority relative to unindexed or inaccessible literature remains uncertain; independent mathematical audit has not occurred.

## References

1. J. S. W. Lamb, M. Rasmussen, W. H. Tey, *Attractors of Linear Maps with Bounded Noise*, arXiv:2310.03437v1 (first public 2023-10-05), https://arxiv.org/abs/2310.03437; especially Sections 2, 4, 5.
2. W. H. Tey, *On Minimal Invariant Sets of Certain Set-Valued Dynamical Systems – A Boundary Map Approach*, PhD thesis (2022), Chapter 4 and Chapter 5, https://www.researchgate.net/publication/366016533_On_Minimal_Invariant_Sets_of_Certain_Set-Valued_Dynamical_Systems_-_A_Boundary_Map_Approach.
3. K. Kourliouros et al., *Smooth Persistence of Attractors for Set-Valued Dynamical Systems: A Boundary Map Approach*, arXiv:2303.01895, https://arxiv.org/abs/2303.01895.
4. O. V. Pochinka, A. A. Yagilev, *Dynamics of the boundary map of a system with spherical noise*, Theoretical and Mathematical Physics 224 (2025), 1271–1279; doi:10.4213/tmf10870, https://www.mathnet.ru/eng/tmf10870.
5. N. Hashemi, J. Ruths, *Generalized Outer Bounds on the Finite Geometric Sum of Ellipsoids*, arXiv:2006.08739 (2020), https://arxiv.org/abs/2006.08739.
