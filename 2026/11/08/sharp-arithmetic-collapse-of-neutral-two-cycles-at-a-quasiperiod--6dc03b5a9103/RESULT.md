# Sharp arithmetic collapse of neutral two-cycles at a quasiperiodic flip boundary

## Finding
Let \(\omega/(2\pi)\notin\mathbb Q\), choose its representative \(0<\omega<2\pi\), and put
\[
c=|\cos(\omega/2)|,\qquad b_*=\frac{2c}{1+c}.
\]
For the quasiperiodically forced clipped reflection
\[
F_b(x,\theta)=\bigl(\min\{1,-x\}-b(1+\cos\theta),\ \theta+\omega\pmod{2\pi}\bigr),
\qquad 0<b\le b_*,
\]
there is a completely explicit central invariant graph
\[
\mu_b(\theta)=-\frac b2-\frac{b}{2\cos(\omega/2)}\cos(\theta-\omega/2).
\]
Define \(A=b/(2c)\), \(d_b=1-b/2-A\), and choose \(\theta_*\) such that
\[
1+\mu_b(\theta)=d_b+A\bigl(1-\cos(\theta-\theta_*)\bigr).
\]
Here \(d_b\ge0\), with equality exactly at \(b=b_*\). For every \(0<b<b_*\), each \(r\in[0,d_b]\) yields two continuous graphs \(\mu_b\pm r\), which the map exchanges; the midpoint graph is invariant. Every real-fiber orbit asymptotically shadows one of these graph pairs, selected by the sign and magnitude of its initial displacement.

At the critical value \(b=b_*\), all real-fiber orbits converge **uniformly in their initial fiber and angular coordinates after two steps** toward the unique continuous invariant graph. More precisely, let \(\rho_m\in[0,\pi]\) denote the angular covering radius of the finite set
\[
\{2j\omega\pmod{2\pi}:0\le j<m\}\subset\mathbb T,
\]
namely the maximal distance of a circle point from its nearest member. For every integer \(m\ge1\),
\[
\boxed{\ \sup_{x_0\in\mathbb R,\,\theta_0\in\mathbb T}|x_{2m}-\mu_{b_*}(\theta_{2m})|
=\sup_{x_0,\theta_0}|x_{2m+1}-\mu_{b_*}(\theta_{2m+1})|
=\frac{1-\cos\rho_m}{1+c}.\ }
\]
Writing \(E_n=\sup_{x_0,\theta_0}|x_n-\mu_{b_*}(\theta_n)|\), the minimax convergence is quadratic in iteration count, \(E_n=\Theta(n^{-2})\), **if and only if** \(\omega/\pi\pmod1\) has bounded continued-fraction partial quotients. For unbounded partial quotients, \(\limsup_{n\to\infty}n^2E_n=\infty\), although \(E_n\to0\) for every irrational rotation.

## Assumptions and scope
The phase space is \(\mathbb R\times(\mathbb R/2\pi\mathbb Z)\). The rotation number is irrational, the harmonic forcing is exactly \(g(\theta)=1+\cos\theta\), and \(b\in(0,b_*]\). Because \(\omega/(2\pi)\) is irrational, \(\cos(\omega/2)\ne0\). An orbit starts from arbitrary \((x_0,\theta_0)\), with no bounded-fiber restriction. The phrase *two-cycle graphs* refers to a pair of continuous graphs exchanged by one skew-product step, not a finite orbit of the irrational base rotation. The covering radius uses geodesic angular distance on the circle.

## Proof
**Central graph and threshold.** The trigonometric identity
\[
\mu_b(\theta+\omega)=-\mu_b(\theta)-b(1+\cos\theta)
\]
is verified by expanding the shifted cosine; its harmonic coefficient is well-defined since \(\cos(\omega/2)\ne0\). The maximum of \(\mu_b\) equals \(-b/2+A\), hence \(\min_\theta(1+\mu_b(\theta))=d_b=1-b/2-A\). The equality \(d_b=0\) is equivalent to \(b=b_*\). In particular \(\mu_b(\theta)\ge-1\) for all \(\theta\), so the clipped fiber map acts linearly on the central graph and it is invariant.

**Exact running minima.** Write \(\delta_n=x_n-\mu_b(\theta_n)\) and \(h_b(\theta)=1+\mu_b(\theta)\). Subtraction of the central graph identity gives the exact scalar relation
\[
\delta_{n+1}=\min\{-\delta_n,h_b(\theta_n)\}.
\]
With \(r=|\delta_0|\), if \(\delta_0>0\) then for all \(m\ge0\)
\[
\delta_{2m}=\min\bigl(\{r\}\cup\{h_b(\theta_0+(2j+1)\omega):0\le j<m\}\bigr),
\quad\delta_{2m+1}=-\delta_{2m}.
\]
If \(\delta_0<0\), then for all \(m\ge0\)
\[
\delta_{2m+1}=\min\bigl(\{r\}\cup\{h_b(\theta_0+2j\omega):0\le j\le m\}\bigr),
\quad\delta_{2m+2}=-\delta_{2m+1}.
\]
For \(\delta_0=0\), every displacement is zero. The identities follow by alternating the sign in the preceding recurrence; no truncation or approximation is involved.

**Neutral graph pairs and selection.** If \(r\le d_b\), then \(h_b(\theta)\ge r\) for all \(\theta\), so \(\delta=\pm r\) maps exactly to \(\mp r\). For a general orbit, the two subsequences of sampled phases above are dense because \(\omega/(2\pi)\) is irrational. Therefore their running minima converge to \(\min(r,d_b)\). The even displacement converges to \(\operatorname{sgn}(\delta_0)\min(r,d_b)\), and the odd one to its negative. These are genuine moving-graph shadowing statements (the base angles themselves do not converge).

**Sharp critical minimax identity.** At \(b=b_*\), the height is
\[
h_{b_*}(\theta)=\frac{1}{1+c}\bigl(1-\cos(\theta-\theta_*)\bigr).
\]
The running-minimum identities show that, at step \(2m\), positive initial displacement samples exactly \(m\) translates of \(2j\omega\), and negative displacement does the same with a different overall translate. Optimizing over unbounded \(r\) removes the initial-magnitude cutoff, while optimizing over \(\theta_0\) is exactly the covering-radius optimization. The same \(m\)-sample optimization applies at step \(2m+1\): positive displacements use \(m\) samples, whereas negative ones use \(m+1\) and cannot give a larger maximum. This proves both displayed equalities. Density of the irrational orbit implies \(\rho_m\to0\), hence \(E_n\to0\) uniformly. If another continuous invariant graph existed, its bounded fiber difference, carried through arbitrarily many iterations and using surjectivity of the base rotation, would be uniformly at most \(E_n\); thus it coincides with \(\mu_{b_*}\). The same argument rules out nontrivial continuous graph pairs invariant under the second iterate.

**Arithmetic rate criterion.** Set \(\alpha=\omega/\pi\pmod1\), and write \(p/q\), \(p'/q'\) for consecutive continued-fraction convergents, with \(q\le m<q'\). For each \(0\le j<q\),
\[
\left\|j\alpha-\frac{jp}{q}\right\|_{\mathbb R/\mathbb Z}<\frac1{q'}.
\]
Since \(p\) is invertible modulo \(q\), the rational points form a regular \(q\)-grid; the first \(m\) rotation points therefore have angular covering radius at most
\[
\rho_m\le2\pi\left(\frac1{2q}+\frac1{q'}\right)\le\frac{3\pi}{q}.
\]
If partial quotients are bounded by \(K\), then \(q'\le(K+1)q\) and \(\rho_m\le3\pi(K+1)/m\). Conversely the largest gap among \(m\) points has length at least \(2\pi/m\), so \(\rho_m\ge\pi/m\). The inequalities \(2s^2/\pi^2\le1-\cos s\le s^2/2\) for \(0\le s\le\pi\) now give \(E_n=\Theta(n^{-2})\).

If the partial quotients are unbounded, there is a sequence of consecutive denominators with \(q'/q\to\infty\). Put \(m=\lfloor q'/4\rfloor\); for sufficiently large indices \(m>q\) and every \(0\le j<m\),
\[
\left\|j\alpha-\frac{jp}{q}\right\|<\frac1{4q}.
\]
All these orbit points lie in neighborhoods of radius \(1/(4q)\) about the \(q\)-grid. At least one of the intervening intervals of angular length \(\pi/q\) is empty, giving \(\rho_m\ge\pi/(2q)\). Therefore \(m^2(1-\cos\rho_m)\) is bounded below by a positive multiple of \((q'/q)^2\), which diverges. The minimax identity transfers this to \(\limsup n^2E_n=\infty\). This proves both implications.

## Verification
Run `python verify.py` from the directory containing this document. Its standard-library-only checks directly iterate the original clipped skew product and separately calculate the running-minimum formulas in 1680 finite comparisons. At the critical parameter it reconstructs 18 worst-phase covering-radius cases over two irrational rotations, obtaining the same minimax values. Expected output:

`VERIFY_OK exact_running_min_cases=1680 covering_radius_cases=18 critical_rotations=2 source_slope=-1`

These tests do not establish the irrational-orbit density, continued-fraction dichotomy, or infinite-time statements; the preceding proof supplies those arguments.

## Relationship to prior work
Martinez-Vergara and Tatjer introduce the exact \(F_4\) clipped decreasing map and analyze its nonlinear nonsmooth period-doubling behavior for slopes \(a<-1\), with a separate contraction result for \(-1<a<0\). Their source explicitly excludes the boundary \(|a|=1\). The present result treats their omitted \(a=-1\) case with the specified harmonic forcing and proves an exact finite-time minimax law plus an arithmetic rate dichotomy. Jorba, Tatjer and Zhang treat a distinct, increasing and symmetrically clipped map with neutral positive slope \(a=1\). Its neutral families are related in spirit but neither entail the decreasing-map running-minimum identity nor its Diophantine criterion. General convex increasing-fiber saddle-node results likewise do not imply the displayed exact formula. These distinctions support originality within inspected material, not exhaustive historical priority.

## Limitations
All conclusions use the exactly marginal slope \(a=-1\), the single harmonic \(1+\cos\theta\), irrational base rotation, and \(0<b\le b_*\). The result does not determine the dynamics for \(b>b_*\), nonharmonic forcing, perturbations of the slope, or arbitrary irregular driving. The rate is a **uniform over all initial conditions** minimax statement; it is not a claim that each fixed trajectory has a matching \(n^{-2}\) lower bound. Finite computer checks are not infinite proofs. No independent mathematical audit has been performed.

## References
1. Rafael Martinez-Vergara and Joan Carles Tatjer, *Nonsmooth bifurcations in families of one-dimensional piecewise-linear quasiperiodically forced maps*, arXiv:2512.04234v1 (public 2025-12-03), published in *Qualitative Theory of Dynamical Systems*, DOI: 10.1007/s12346-025-01438-0. https://arxiv.org/abs/2512.04234 ; https://link.springer.com/article/10.1007/s12346-025-01438-0 .
2. Àngel Jorba, Joan Carles Tatjer and Yuan Zhang, *Non-smooth pitchfork bifurcations in a quasi-periodically forced piecewise-linear map* (preprint 2023). https://www.maia.ub.es/dsg/2023/2303jorba.pdf .
3. Vasso Anagnostopoulou and Tobias Jäger, *Nonautonomous saddle-node bifurcations: random and deterministic forcing*, arXiv:1105.5094 (2011). https://arxiv.org/abs/1105.5094 .
