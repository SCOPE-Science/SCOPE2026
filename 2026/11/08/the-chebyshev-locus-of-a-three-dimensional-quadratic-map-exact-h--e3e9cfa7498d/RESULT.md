# The Chebyshev locus of a three-dimensional quadratic map: exact hyperchaos and periodic census

## Finding

For the real polynomial map
\[
F(x,y,z)=\bigl(a_1x+a_2y+a_3y^2,\ b_1-b_2z,\ cx\bigr),
\]
consider the nondegenerate parameter region \(a_1=0\), \(a_3b_2c\ne0\). Put \(k=b_2c\). **The scalar third-step feedback polynomial is affinely conjugate to the full logistic map \(g(v)=4v(1-v)\) if and only if**
\[
\boxed{k^2a_2^2+2k(a_2+2a_3b_1)=8.}\tag{1}
\]
For every such parameter, an explicitly given nondegenerate compact rectangular box \(B\subset\mathbb R^3\) is invariant, and the restriction \(F|_B\) is affinely conjugate to
\[
G(u,v,w)=(g(v),w,u),\qquad G^3=(g,g,g).\tag{2}
\]
Consequently \(F|_B\) has a unique invariant probability absolutely continuous with respect to three-dimensional Lebesgue measure. It is exact (hence mixing), ergodic, and physical for Lebesgue-almost every initial state in \(B\); its support is the whole box. Its three Lyapunov exponents, counted with multiplicity, are all exactly \(\frac{\log 2}{3}>0\). Its Kolmogorov–Sinai entropy with respect to that probability and its topological entropy on \(B\) both equal \(\log2\). For every integer \(n\ge1\),
\[
\boxed{\#\operatorname{Fix}(F^n|_B)=2^n,\qquad
\zeta_{F|_B}(t)=\frac1{1-2t},\qquad
\#\{\text{primitive }n\text{-cycles}\}=\frac1n\sum_{d\mid n}\mu(n/d)2^d.}\tag{3}
\]
Here \(\mu\) in the last sum denotes the arithmetic Möbius function, not the invariant measure. Every periodic point in \(B\) is hyperbolic and repelling in all three directions; each Floquet multiplier of an \(n\)-periodic point has modulus at least \(2^{n/3}\).

## Assumptions and scope

All six parameters are real and satisfy \(a_1=0\), \(a_3b_2c\ne0\). Set
\[
A=a_3k^2,\quad B_0=-k(a_2+2a_3b_1),\quad C_0=a_2b_1+a_3b_1^2,\quad
s=-\frac4A,\quad t=\frac{4-B_0}{2A}.
\]
The affine isomorphism \(\Phi:[0,1]^3\to\mathbb R^3\) is
\[
\Phi(u,v,w)=\bigl(t+su,\ b_1-k(t+sv),\ c(t+sw)\bigr),\qquad B=\Phi([0,1]^3).
\]
Since \(s,k,c\ne0\), \(\Phi\) is injective and its image is a three-dimensional rectangular box, with interval orientations immaterial. The claimed invariant probability is \(\Phi_*\rho^{\otimes3}\), where
\[
\rho(du)=\frac{du}{\pi\sqrt{u(1-u)}}\quad\text{on }(0,1).
\]
All recurrence, measure, entropy, and exponent conclusions are **restricted to this invariant box**. The box need not attract external initial conditions. The formula \(\#\operatorname{Fix}(F^n|_B)\) counts distinct periodic points including those of periods dividing \(n\), not primitive orbits. The statement about scalar affine conjugacy refers exactly to the feedback polynomial defined in the proof; it does not classify nonlinear conjugacies or general \(a_1\ne0\) behavior.

The concrete choice
\[
(a_1,a_2,a_3,b_1,b_2,c)=(0,4,-4,1,1,1)
\]
has \(B=[0,1]^3\) and \(F(x,y,z)=(4y(1-y),1-z,x)\), illustrating the invariant box without any parameter limit.

## Proof

**1. Algebraic characterization.** For \(a_1=0\), eliminate the two linear feedback coordinates in three steps. The relevant univariate quadratic polynomial is
\[
\psi(X)=a_2(b_1-kX)+a_3(b_1-kX)^2=AX^2+B_0X+C_0.
\]
A nonsingular affine conjugacy \(X=t+sv\) between \(\psi\) and \(g(v)=4v(1-v)\) must match quadratic coefficients, giving \(As=-4\), and linear coefficients, giving \(2At+B_0=4\); hence \(s=-4/A\), \(t=(4-B_0)/(2A)\) are forced. With these values, equality of constant coefficients is \(\psi(t)=t\), equivalent (multiply by \(4A\)) to \(4AC_0-B_0^2+2B_0+8=0\). Direct cancellation gives \(4AC_0-B_0^2=-k^2a_2^2\), so the constant equation is precisely (1). This proves both necessity and sufficiency for scalar affine conjugacy, including \(b_1=0\).

**2. Three-coordinate conjugacy.** Under (1), the polynomial identity \(\psi(t+sv)=t+s g(v)\) holds for all real \(v\). Thus
\[
\begin{aligned}
F(\Phi(u,v,w))
&=\bigl(\psi(t+sv),\ b_1-k(t+sw),\ c(t+su)\bigr)\\
&=\Phi(g(v),w,u).
\end{aligned}
\]
This establishes (2), forward invariance \(F(B)=B\), and the conjugacy on the entire closed box, not merely almost everywhere.

**3. Invariant measure, mixing, and exponents.** The increasing homeomorphism \(h(q)=\sin^2(\pi q/2)\) of \([0,1]\) conjugates the full tent map \(T(q)=1-|1-2q|\) to \(g\): \(g\circ h=h\circ T\). The tent map preserves Lebesgue measure, is exact by independent binary full-branch coding and the zero–one law, and has entropy \(\log2\). Its pushforward by \(h\) is exactly \(\rho\). Consequently \((g,g,g)\) is exact for \(\rho^{\otimes3}\), with entropy \(3\log2\). Since \(G^3=(g,g,g)\), the probability \(\rho^{\otimes3}\) is \(G\)-invariant (the map permutes independent coordinates and applies one \(g\)); \(G\) is exact because its third iterate is exact, hence mixing and ergodic. Exactness also rules out a second invariant probability absolutely continuous with respect to \(\rho^{\otimes3}\). This probability is equivalent to Lebesgue measure inside the cube, so its basin has full Lebesgue measure there. Its support is the full closed cube.

For the tent system, the a.e. expanding slope magnitude is two. Under \(h\), each logistic Lyapunov exponent remains \(\log2\): the derivative conjugacy introduces the endpoint term \(\log h'(T^nq)-\log h'(q)\), whose quotient by \(n\) tends to zero almost surely, since \(\mathbb P(|\log h'(T^nq)|>\epsilon n)\) is exponentially small and Borel–Cantelli applies. By (2), \(DG^{3n}\) is diagonal with entries \((g^n)'\) on the respective coordinates. Thus all three singular-value exponents of \(G\) are \(\frac{\log 2}{3}\). Affine conjugacy transfers them to \(F\). The entropy power rule gives both measure and topological entropies \(\log2\), because the tent map has topological entropy \(\log2\) and entropy is additive under Cartesian products.

**4. Every-period census.** The \(n\)-fold tent iterate has \(2^n\) monotonic full branches, each with slope \(\pm2^n\), and exactly one fixed point on each. No branch-boundary point is fixed except the endpoint zero; all other turning preimages enter the preperiodic critical orbit. Hence \(\#\operatorname{Fix}(g^n)=2^n\). For \(n=3r\), (2) immediately gives \(\#\operatorname{Fix}(G^n)=2^{3r}\). For \(n=3r+1\), a fixed point satisfies
\[
u=g^{r+1}(v),\quad v=g^r(w),\quad w=g^r(u),
\]
so it is determined uniquely by \(u=g^{3r+1}(u)\). For \(n=3r+2\), the equations are \(u=g^{r+1}(w)\), \(v=g^r(u)\), \(w=g^{r+1}(v)\), likewise equivalent to \(u=g^{3r+2}(u)\). Therefore \(\#\operatorname{Fix}(G^n)=2^n\) for every \(n\). The exponential definition of the Artin–Mazur zeta function and Möbius inversion prove (3).

**5. Repelling periodic points.** At every periodic point of \(g\), the \(m\)-fold derivative has modulus at least \(2^m\): away from zero this follows by conjugacy to the tent map and the nonvanishing endpoint-free derivative of \(h\) at the periodic point; at the fixed endpoint zero the derivative is exactly \(4^m\). If \(p\) is an \(n\)-periodic point of \(G\), \(D G^{3n}(p)\) is diagonal and its three diagonal entries have modulus at least \(2^n\). Since \(G^n(p)=p\), the same matrix is \((DG^n(p))^3\); every eigenvalue of \(DG^n(p)\) therefore has modulus at least \(2^{n/3}\). Affine similarity transfers this conclusion to \(F\).

## Verification

The standalone file `check.py` performs exact symbolic elimination of the defining parameter relation, verifies the affine conjugacy at six nondegenerate rational parameter choices at 36 rational cube points, checks the full tent-map fixed-point enumeration for all \(1\le n\le10\), and computes primitive-period counts through \(n=9\). Successful output begins `CHECK_OK`. These bounded finite tests independently catch algebra and indexing errors; the all-parameter and all-period assertions rely on the analytic proof above. Run `python check.py` with Python 3 and SymPy installed.

## Relationship to prior work

Ren, Zhou, and Liu (2017) give this polynomial-map family and investigate controlled finite-period points and bifurcations; Muni (2024) analyzes numerical routes to three-positive-exponent hyperchaos in the same family and reports repelling periodic trajectories. Those published observations do **not** themselves state the nondegenerate algebraic locus (1), affine cubical model (2), exact invariant density, or all-period zeta (3). The full logistic/tent conjugacy and its ergodic theory are classical and are not claimed as new. The claimed contribution is the exact parameter locus **inside this named quadratic family** together with its simultaneous dynamical consequences and all-period census. Similar constructions in general coupled-map literature could have priority; no general novelty of products of logistic maps is asserted.

## Limitations

This is a codimension-two algebraic subfamily of the six-parameter system, not a generic parameter regime, and does not prove persistence of three positive exponents off the locus. The maximal invariant box is not asserted to attract any neighborhood in ambient \(\mathbb R^3\). Multiple singular invariant probabilities exist, so uniqueness is only among absolutely continuous invariant probabilities on the box. The exact density is not uniform Lebesgue density. A related 2024 study of quasiperiodic torus doubling in the same family was accessible as abstract/publisher preview but not inspected in full; an equivalent special-case formula there or in other unindexed literature remains a publication-priority risk.

## References

1. C. Ren, J. Zhou, C. Liu, "Chaos control of a multi-dimensional chaotic mapping system by modified stability transformation method," *Journal of Vibroengineering* 19 (2017), 1103–1115, DOI: 10.21595/jve.2016.17317. Full text: https://www.researchgate.net/publication/315997911_Chaos_control_of_a_multi-dimensional_chaotic_mapping_system_by_modified_stability_transformation_method .
2. S. S. Muni, "Pathways to hyperchaos in a three-dimensional quadratic map," arXiv:2406.08317v1, publicly posted 2024-06-12, https://arxiv.org/abs/2406.08317 .
3. S. S. Muni, "Ergodic and resonant torus doubling bifurcation in a three-dimensional quadratic map," *Nonlinear Dynamics* 112 (2024), 4651–4661, DOI: 10.1007/s11071-024-09284-6 (abstract/publisher-preview comparison).
4. Classical full tent/logistic conjugacy, binary coding, and entropy: standard one-dimensional ergodic theory; recalled constructively in the proof.
