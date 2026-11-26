# Joint weak-dissipation law for mode-locking periods and rotation phases

## Finding
Consider the contracted rotations \(f_{\lambda,\delta}(x)=\{\lambda x+\delta\}\) on \([0,1)\), with fixed \(0<\lambda<1\) and \(\delta\) chosen uniformly from \([0,1)\). Let \(\rho_{\lambda,\delta}\in[0,1)\) be the rotation number, and let \(Q_{\lambda,\delta}\) be the least period of the attracting periodic orbit where it exists (defined arbitrarily on the null exceptional parameter set). Set \(h=-\log\lambda\).

**Joint limit theorem.** As \(\lambda\uparrow1\),
\[
(\rho_{\lambda,\delta},\,hQ_{\lambda,\delta})\ \Longrightarrow\ (U,Y),
\]
where \(U\) is uniform on \([0,1]\), \(Y\) is independent of \(U\), and \(Y\) has the probability density
\[
 f_Y(t)=\frac{6}{\pi^2}\frac{t}{e^t-1},\qquad t>0.
\]
In particular, for every continuous \(g:[0,1]\to\mathbb R\) and every integer \(k\ge0\),
\[
\lim_{\lambda\uparrow1}\mathbb E\big[g(\rho_{\lambda,\delta})(hQ_{\lambda,\delta})^k\big]
=\left(\int_0^1g(u)\,du\right)\frac{6\,\Gamma(k+2)\zeta(k+2)}{\pi^2}.
\]
Thus \(\lim\mathbb E[hQ]=12\zeta(3)/\pi^2\), and the full limiting phase-period law factorizes despite arithmetic correlations at fixed contraction.

The previously known rational mode-locking plateau formula yields the following **supporting exact identity** for the period marginal, valid for each integer \(q\ge1\):
\[
\mathbb P(Q_{\lambda,\delta}=q)
=\frac{4\sinh^2(h/2)\,\varphi(q)}{e^{hq}-1}.
\]
This finite-contraction identity is a direct consequence of the cited plateau formula and is **not** claimed as an independent original theorem.

## Assumptions and scope
The random variable \(\delta\) has normalized Lebesgue distribution on \([0,1)\); \(\lambda\) is a fixed scalar contraction while the parameter is sampled, then tends to one. \(\varphi(q)\) is Euler's totient, \(\zeta\) is the Riemann zeta function, and \(\Gamma\) is the Euler gamma function. The attracting orbit and its least period are well defined outside a set of parameters of Lebesgue measure zero; boundary parameters may be assigned any period without affecting any statement. Weak convergence is on \([0,1]\times[0,\infty)\). The moment statement quantifies over each **fixed** nonnegative integer \(k\), not an order that grows with the contraction scale.

## Proof
**1. The exact joint atomic measure from rational plateaux.** For a reduced rational rotation number \(0<p/q<1\), the classical rational plateau formula (Laurent–Nogueira–Pollicott, Theorem 1(ii), reproducing earlier results) gives parameter interval width
\[
 w_q(\lambda)=\frac{(1-\lambda)^2\lambda^{q-1}}{1-\lambda^q}
=\frac{4\sinh^2(h/2)}{e^{hq}-1}.
\]
Crucially this width does not depend on \(p\). There are \(\varphi(q)\) reduced fractions of denominator \(q\) in \((0,1)\). Rotation number zero occupies \(0\le\delta\le1-\lambda\), of width \(1-\lambda\), which equals the displayed formula at \(q=1\) with \(\varphi(1)=1\). The cited theorem also establishes that irrational-rotation parameters have Hausdorff dimension zero and that nonboundary rational maps have one periodic orbit. Hence the joint distribution consists of one atom of mass \(1-\lambda\) at \((0,h)\), and, for every reduced \(p/q\) with \(q\ge2\), one atom of mass \(w_q(\lambda)\) at \((p/q,hq)\).

For completeness, the weights sum to one: by \(\sum_{d\mid n}\varphi(d)=n\), for \(|z|<1\),
\[
\sum_{q\ge1}\varphi(q)\frac{z^q}{1-z^q}
=\sum_{n\ge1}\left(\sum_{q\mid n}\varphi(q)\right)z^n
=\frac{z}{(1-z)^2}.
\]
Multiplication by \((1-\lambda)^2/\lambda=4\sinh^2(h/2)\) gives exact normalization.

**2. Arithmetic equidistribution at the shrinking scale.** The classical estimate
\[
\Phi(N):=\sum_{q\le N}\varphi(q)
=\frac{3}{\pi^2}N^2+O(N\log(2N))
\]
follows from \(\varphi(q)=q\sum_{d\mid q}\mu(d)/d\) and \(\sum_{d\ge1}\mu(d)/d^2=6/\pi^2\). Consequently, on compact subsets of \((0,\infty)\), the positive measures
\[
 h^2\sum_{q\ge1}\varphi(q)\,\delta_{hq}
\]
converge weakly to \((6/\pi^2)t\,dt\). Here \(\delta_t\) denotes a point mass at \(t\). Since \(4\sinh^2(h/2)/h^2\to1\), multiplication by the continuous function \(t\mapsto1/(e^t-1)\) gives convergence of the period marginal on compact subsets away from zero.

For the rotation coordinate, let \(g\) be Lipschitz on \([0,1]\). Möbius inversion and the Riemann-sum error bound give
\[
\sum_{\substack{1\le p\le q\\ \gcd(p,q)=1}}g(p/q)
=\varphi(q)\int_0^1g(u)\,du+O_g(\tau(q)),
\]
where \(\tau(q)\le2\sqrt q\) is the divisor function. For \(a\le hq\le b\), where \(0<a<b<\infty\) are fixed, the total contribution of the errors after plateau weighting is at most
\[
 O_{a,b,g}\left(h^2\sum_{q\le b/h}\sqrt q\right)=O_{a,b,g}(\sqrt h)=o(1).
\]
It follows that, on every such compact period window, the limiting joint measure is the product of Lebesgue measure in the rotation coordinate and \((6/\pi^2)t/(e^t-1)\,dt\) in the scaled-period coordinate.

**3. Boundary mass and all moments.** With \(C_h=4\sinh^2(h/2)\sim h^2\), the elementary estimates \(\varphi(q)\le q\) and \(e^{hq}-1\ge hq\) give, for each fixed \(a>0\),
\[
\limsup_{h\downarrow0}\mathbb P(hQ\le a)\le a.
\]
For \(b\ge1\), \(\varphi(q)\le q\) and the exponential denominator give a bound \(O((b+1)e^{-b})\) on the upper tail \(\mathbb P(hQ\ge b)\), uniformly for sufficiently small \(h\). The same estimate with any fixed polynomial factor \((hq)^k\) proves uniform integrability of all fixed moments. Thus the compact-window result extends to the full joint weak limit and to the stated mixed moments.

Finally,
\[
\int_0^\infty \frac{t^{k+1}}{e^t-1}\,dt=\Gamma(k+2)\zeta(k+2),
\]
from the positive expansion \((e^t-1)^{-1}=\sum_{m\ge1}e^{-mt}\) and termwise integration. For \(k=0\), the integral is \(\pi^2/6\), showing the claimed density integrates to one. For continuous \(g\), uniformly approximate it by Lipschitz functions; moment uniform integrability just proved permits the same conclusion.

## Verification
The accompanying `verify.py` checks the published rational-plateau formula by exact rational arithmetic at contraction \(\lambda=1/2\) for all reduced fractions with denominators from two to twelve, independently reconstructs the claimed primitive orbit length, checks the totient divisor identity for integers through 120, and verifies a rational tail bound for the period weights. Numerical sums at four smaller dissipation scales provide an additional, **non-probative** consistency check of the limiting distribution. The proof above establishes all infinite and small-dissipation assertions independently of finite computation.

## Relationship to prior work
Bugeaud–Conze (1999), Ding–Hemmer and subsequent treatments established the rational mode-locking plateaux of contracted rotations. The fully inspected 2017 Laurent–Nogueira–Pollicott preprint states their widths and zero-dimensionality of irrational parameters; these are imported hypotheses rather than new findings here. Nogueira–Pires (first public preprint June 25, 2012; primary MSC 37E05) supplies earlier general context on one-dimensional piecewise contractions. The standard summatory-totient asymptotic and Farey equidistribution are also previously known. The present statement concerns their **joint, phase-resolved weak-dissipation dynamical limit and convergence of every fixed mixed period moment**, rather than claiming originality for its individual ingredients. Existing accessible works focus on rotation number versus parameters, arithmetic heights, exception-set dimensions, or bounds on the number of periodic orbits, and do not state this joint limiting law.

## Limitations
No claim of independent external audit or absolute historical priority is made. The original Bugeaud–Conze (1999) article is bibliographically confirmed, but its publisher full-text link was inaccessible during comparison; its substantive plateau result was independently available in the later complete theorem. A prior unindexed treatment of random-parameter period statistics could pre-empt some novelty. The convergence is weak, not total-variation convergence: each finite-dissipation joint measure is countably atomic. It is specific to the uniform shift parameter and the affine contraction family, not arbitrary circle maps or arbitrary parameter distributions. The exact finite-scale plateau law is known input.

## References
1. A. Nogueira and B. Pires, *Dynamics of piecewise contractions of the interval*, arXiv:1206.5676v1, first posted 2012-06-25, primary MSC 37E05. https://arxiv.org/abs/1206.5676
2. M. Laurent, A. Nogueira and M. Pollicott, *Rotation number of interval contracted rotations*, arXiv:1704.05130v1, first posted 2017-04-17, Theorems 1 and 2. https://arxiv.org/abs/1704.05130
3. Y. Bugeaud and J.-P. Conze, *Calcul de la dynamique de transformations linéaires contractantes mod 1 et arbre de Farey*, Acta Arithmetica 88 (1999), 201–218, DOI 10.4064/aa-88-3-201-218. Date of first public release not verified to the day.
4. The classical identities \(\sum_{d\mid n}\varphi(d)=n\), \(\sum_{q\le N}\varphi(q)=3N^2/\pi^2+O(N\log(2N))\), and the reduced-residue Riemann-sum formula, proved or derived above where needed.
