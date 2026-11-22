# Parity-sharp phase locking of extreme angular gaps in aligned Blaschke fibres

## Finding
Let \(N\ge2\) be an integer and let \(a_1,\ldots,a_N\in[0,1)\), with at least one \(a_j>0\). Form the normalized finite Blaschke product
\[
B(z)=\prod_{j=1}^N\frac{z-a_j}{1-a_jz}.
\]
For each \(\eta\in\mathbb T\), write the \(N\) (distinct) solutions of \(B(z)=\eta\) on \(\mathbb T\) in circular order and let \(m(\eta)\) and \(M(\eta)\) be respectively their smallest and largest successive angular gaps, including the wraparound gap.

**Theorem.** The unique phase maximizing \(m\) is \(\eta=1\). The unique phase minimizing \(M\) is \(\eta=(-1)^N\). Hence the maximin-separation and minimax-covering phases coincide exactly when \(N\) is even; when \(N\) is odd they are antipodal.

The following formulas give the complete phase dependence, not merely the optimizers. Let
\[
v(\theta)=\sum_{j=1}^N\frac{1-a_j^2}{1-2a_j\cos\theta+a_j^2},\quad F(\theta)=\int_0^\theta v(t)\,dt,
\]
where \(F\) is strictly increasing, odd, and \(F(\theta+2\pi)=F(\theta)+2\pi N\). Define \(G=F^{-1}\), \(h(u)=G'(u)=1/v(G(u))\), and
\[
J(c)=G(c+\pi)-G(c-\pi),\qquad 0\le c\le N\pi.
\]
Then \(J\) is strictly increasing on \((0,N\pi)\). If \(\eta=e^{i\phi}\), and \(d(\phi,\psi)=\min_{k\in\mathbb Z}|\phi-\psi+2k\pi|\in[0,\pi]\), then
\[
\boxed{m(\eta)=J\bigl(\pi-d(\phi,0)\bigr),\qquad M(\eta)=J\bigl((N-1)\pi+d(\phi,N\pi)\bigr).}
\]
In particular, the two optimal objective values are
\[
\boxed{\max_\eta m(\eta)=G(2\pi),\qquad \min_\eta M(\eta)=\pi-G((N-2)\pi).}
\]
These exact gaps have strict linear angular-phase cusps. Put \(d_+=G(2\pi)\), \(d_-=\pi-G((N-2)\pi)\). For \(\varepsilon\to0\),
\[
 m(e^{i\varepsilon})=d_+-\left[\frac1{v(d_+)}-\frac1{v(0)}\right]|\varepsilon|+O(\varepsilon^2),
\]
\[
 M((-1)^Ne^{i\varepsilon})=d_-+\left[\frac1{v(\pi)}-\frac1{v(\pi-d_-)}\right]|\varepsilon|+O(\varepsilon^2).
\]
Both displayed linear coefficients are strictly positive.

## Assumptions and scope
The zeros are real and nonnegative, i.e. all lie on one prescribed radius; rotation of the disk transfers the theorem to any common ray. Repeated zeros and zeros at the origin are permitted. At least one nonzero zero is essential for strict uniqueness: when all \(a_j=0\), every fibre is a rotated regular \(N\)-gon and both objectives are phase independent. There is no claim for arbitrary non-collinear or negative-real zero configurations, nor for arbitrary inner functions of infinite degree.

The natural motivating application is angular site selection among minimal-support optimal prediction measures for polynomial extrapolation outside the disk. For \(B(z)=z^{N-1}(z-a)/(1-az)\), \(0<a<1\), its fibres are precisely the possible \(N\)-node optimal measures for polynomials of degree at most \(N-1\) evaluated at \(1/a\). Their known positive masses are
\[
w_j=\frac{1-a^2}{1-a^2+(N-1)|z_j-a|^2}.
\]
The theorem singles out the unique most-separated optimal prediction design, and identifies whether that design also minimizes its largest unsampled angular arc. The optimal-prediction characterization and weights are prior work, not claimed new here.

## Proof
**1. Boundary phase and monotone speed.** Each Möbius factor has a strictly positive angular derivative on \(\mathbb T\), so the chosen lift \(F\) satisfies \(B(e^{i\theta})=e^{iF(\theta)}\) and \(F'=v\). Every summand has derivative
\[
-\frac{2a_j(1-a_j^2)\sin\theta}{(1-2a_j\cos\theta+a_j^2)^2}.
\]
Thus \(v\) is even, \(2\pi\)-periodic, and strictly decreasing on \((0,\pi)\), since at least one \(a_j>0\). Consequently \(F\) is odd, \(F(\pi)=N\pi\), and \(h=1/(v\circ G)\) is even, \(2\pi N\)-periodic, and strictly increasing with circular distance from \(0\) on the half-period \([0,N\pi]\).

**2. A strict interval-length rearrangement.** The physical angular length of the interval carrying boundary-phase mass \(2\pi\) and centered at phase coordinate \(c\) equals \(J(c)=\int_{c-\pi}^{c+\pi}h(u)\,du\). Evenness and periodicity make \(J\) even and \(2\pi N\)-periodic. For \(0<c<N\pi\),
\[
J'(c)=h(c+\pi)-h(c-\pi)>0.
\]
Indeed, the circular distance of \(c+\pi\) to \(0\) is strictly greater than that of \(c-\pi\): for \(c+\pi\le N\pi\), compare \(c+\pi\) and \(|c-\pi|\); otherwise compare \(2\pi N-c-\pi\) and \(c-\pi\). Strict monotonicity of \(h\) proves the inequality. The endpoint values follow by symmetry and inverse-phase normalization.

**3. Complete gap optimization.** The lifted fibre points have phase coordinates \(\phi+2k\pi\), modulo the phase circumference \(2\pi N\), so the centers of its \(N\) successive intervals have coordinates \(\phi+(2k+1)\pi\). Those centers are equally spaced by \(2\pi\). Their smallest circular distance from \(0\) is \(\pi-d(\phi,0)\); their largest distance is \((N-1)\pi+d(\phi,N\pi)\). By the strict ordering of \(J\), the smallest and largest physical gaps are exactly the two boxed profiles. Maximizing the former requires \(d(\phi,0)=0\), i.e. \(\eta=1\). Minimizing the latter requires \(d(\phi,N\pi)=0\), i.e. \(\eta=(-1)^N\). Both phase optimizers are unique. At these phases, \(J(\pi)=G(2\pi)\) and \(J((N-1)\pi)=\pi-G((N-2)\pi)\), proving the exact optimal values.

**4. Sharp cusp coefficients.** The profiles near their unique phase extrema are \(J(\pi-|\varepsilon|)\) and \(J((N-1)\pi+|\varepsilon|)\). Ordinary Taylor expansion at the interior points \(\pi\) and \((N-1)\pi\), together with \(J'=h(c+\pi)-h(c-\pi)\), gives the two stated coefficients. Since \(0<d_+\le\pi\) and \(0<d_-\le\pi\), strict decrease of \(v\) on \((0,\pi)\) makes both coefficients positive. This completes the theorem.

## Verification
The companion script `checks/fibre_gaps_check.py` uses only the Python standard library. It inverts the continuous Blaschke boundary-phase lift by bisection, directly constructs all fibre gaps for multiple distinct and repeated aligned-zero lists, checks the exact two full-phase profiles, both unique extrema, inverse normalization, and both sharp cusp coefficients. Running `python checks/fibre_gaps_check.py` produced `PASS 7208 finite checks across 34 aligned-zero lists`. These finite tests check formulas and branches; they are not the proof for all degrees, zeros, or phases.

## Relationship to prior work
Breuer and Seelig (2019) study local and asymptotic spacing of paraorthogonal zeros, particularly singular measures; their theorems do not determine the optimizing boundary phase of all fibres of a prescribed aligned finite Blaschke product. Kovalev and Yang (2020) give the Poisson-kernel identity for \(|B'|\) and optimize its extreme derivative values across *products*; the present statement fixes a product and optimizes extreme *gaps across target phases*. Bos, Levenberg and Ortega-Cerdà (2019) and Charpentier, Levenberg and Wielonsky (2022) establish optimal polynomial prediction measures and matching disk moments, but not this two-objective phase-locking theorem. The standard paraorthogonal-polynomial representation of the prediction fibres is background. Closely related published finite Blaschke and quadrature results may contain an equivalent phase-ordering principle; absence of a matching indexed statement is not a proof of priority.

## Limitations
Strictness requires a nonconstant angular-speed profile; co-radial nonnegative zeros guarantee it but are not claimed necessary. The result does not optimize quadrature weights, noise sensitivities, determinant conditioning, or gap criteria under arbitrary location constraints. No result for unrestricted Blaschke zero arrays or for non-uniformly spaced target values is asserted. The substantive novelty assessment is best-knowledge rather than a certified priority determination; independent verification is outstanding.

## References
- J. Breuer and E. Seelig, *On the spacing of zeros of paraorthogonal polynomials for singular measures*, arXiv:1908.06737 (first posted 19 August 2019), https://arxiv.org/abs/1908.06737.
- L. V. Kovalev and X. Yang, *Extreme values of the derivative of Blaschke products and hypergeometric polynomials*, arXiv:2007.09760 (first posted 19 July 2020), https://arxiv.org/abs/2007.09760.
- L. Bos, N. Levenberg and J. Ortega-Cerdà, *Optimal Polynomial Prediction Measures and Extremal Polynomial Growth*, arXiv:1912.12462 (first posted 28 December 2019), https://arxiv.org/abs/1912.12462.
- S. Charpentier, N. Levenberg and F. Wielonsky, *An extremal problem for the Bergman kernel of orthogonal polynomials*, arXiv:2207.04662 (first posted 11 July 2022), https://arxiv.org/abs/2207.04662.
- L. Bos, *A Characterization of Optimal Prediction Measures via \(\ell_1\) Minimization*, arXiv:2312.03091 (first posted 5 December 2023), https://arxiv.org/abs/2312.03091.
