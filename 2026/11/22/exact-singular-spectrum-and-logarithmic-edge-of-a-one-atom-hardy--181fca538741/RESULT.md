# Exact singular spectrum and logarithmic edge of a one-atom Hardy average

## Finding

For every \(\beta>0\), let \(\mu_\beta=\beta\delta_0+\mathbf1_{(0,1)}\,dx\) and let the Hardy averaging operator on \(L^2([0,1],\mu_\beta)\) be
\[
(H_\beta f)(0)=f(0),\qquad
(H_\beta f)(x)=\frac{\beta f(0)+\int_0^x f(t)\,dt}{\beta+x}\quad(0<x<1).
\]
Put \(T=\log(1+\beta^{-1})\). For every integer \(j\ge1\), there is exactly one positive solution \(\kappa_j\) of
\[
\boxed{\kappa_j T+3\arctan(2\kappa_j)=j\pi.}
\]
All nonzero singular values of \(H_\beta\), in strictly decreasing order and each with multiplicity one, are exactly
\[
\boxed{s_j(H_\beta)=\frac{2}{\sqrt{1+4\kappa_j^2}}.}
\]
In particular \(1<\|H_\beta\|<2\), and the Hilbert–Schmidt identity is
\[
\boxed{\sum_{j=1}^\infty s_j(H_\beta)^2=1+\log(1+\beta^{-1}).}
\]
For fixed \(\beta\), \(s_j(H_\beta)\sim T/(\pi j)\), so \(H_\beta\) belongs to the Schatten class \(\mathcal S_p\) exactly for \(p>1\). For every fixed \(j\ge1\), the vanishing-atom limit obeys
\[
\boxed{\lim_{\beta\downarrow0}T^2\bigl(2-s_j(H_\beta)\bigr)=4\pi^2j^2.}
\]
For a dominating atom \(\beta\to\infty\), \(s_1=1+T/2+O(T^2)\), whereas \(s_j/T\to[\pi(j-3/2)]^{-1}\) for every fixed \(j\ge2\). Thus the spectrum interpolates between a rank-one limit and infinitely many singular values condensing at the Hardy norm edge.

## Assumptions and scope

The measure has one atom of mass \(\beta>0\) at the left endpoint and unit Lebesgue density on \((0,1)\). The Hilbert space and all operator norms are complex \(L^2\) norms with respect to this same measure on input and output. Positive singular values mean the positive square roots of eigenvalues of \(H_\beta^*H_\beta\), counted with multiplicity. All asymptotic limits specify the parameters held fixed. The logarithm is natural.

The normalized averaging formula uses \(\mu_\beta([0,x])=\beta+x\) for \(x>0\). It is not the unnormalised Volterra integral and it is not the ordinary atomless Hardy operator. The physical continuous interval has length one; changing that length merely rescales the atom-to-continuum mass ratio.

## Proof

**1. Compactness and the Sobolev pencil.** Write \(g(y)=\beta f(0)+\int_0^{y-\beta}f(x)\,dx\) on \(\beta\le y\le\beta+1\). Then \(g(\beta)=\beta f(0)\), \(g'(\beta+x)=f(x)\) almost everywhere, and every \(H^1\) function \(g\) on this interval corresponds uniquely to an input \(f\). Directly,
\[
\begin{aligned}
\|f\|^2&=\frac{|g(\beta)|^2}{\beta}+\int_\beta^{\beta+1}|g'(y)|^2\,dy,\\
\|H_\beta f\|^2&=\frac{|g(\beta)|^2}{\beta}+\int_\beta^{\beta+1}\frac{|g(y)|^2}{y^2}\,dy.
\end{aligned}
\]
Set \(t=\log(y/\beta)\), \(g(y)=\sqrt y\,h(t)\), so \(t\in[0,T]\). The two squared norms become the positive forms
\[
Q(h)=|h(0)|^2+\int_0^T|h'(t)+h(t)/2|^2\,dt,
\qquad
R(h)=|h(0)|^2+\int_0^T|h(t)|^2\,dt.
\]
Integration by parts for complex \(h\in H^1(0,T)\) yields
\[
Q(h)=\int_0^T\left(|h'|^2+\frac14|h|^2\right)dt
+\frac12|h(0)|^2+\frac12|h(T)|^2.
\]
Consequently,
\[
Q(h)-\frac14R(h)=\int_0^T|h'|^2\,dt
+\frac14|h(0)|^2+\frac12|h(T)|^2>0
\]
for every nonzero \(h\). The map \(H^1(0,T)\to\mathbb C\oplus L^2(0,T)\), \(h\mapsto(h(0),h)\), is compact; hence the ratio \(R(h)/Q(h)\) gives the compact positive singular-value problem and its maximal value is strictly less than four. Moreover the constant input is fixed by \(H_\beta\), so its norm is at least one. Strict inequality above one follows from the first-root characterization below, since \(T>0\).

**2. Exact eigenvalue boundary conditions.** Let \(\lambda>0\) be an eigenvalue of \(H_\beta^*H_\beta\), and put \(\eta=1/\lambda>1/4\). Stationarity of \(Q(h)-\eta R(h)\) against all \(H^1\) test functions gives the interior ordinary differential equation and the endpoint conditions
\[
-h''+\tfrac14h=\eta h,\qquad
h'(0)=(\tfrac12-\eta)h(0),\qquad h'(T)=-\tfrac12h(T).
\]
With \(\kappa=\sqrt{\eta-1/4}>0\) and \(\theta=2\arctan(2\kappa)\in(0,\pi)\), the first boundary condition is satisfied, up to a nonzero scalar, precisely by
\[
h(t)=\sin(\kappa t+\theta),\qquad
\kappa\cot\theta=\frac14-\kappa^2.
\]
The second boundary condition is equivalent to
\[
\kappa T+3\arctan(2\kappa)\in\pi\mathbb Z.
\]
Its left side increases continuously and strictly from zero to infinity, with derivative \(T+6/(1+4\kappa^2)>0\). Hence for each \(j\ge1\) there is exactly one positive root \(\kappa_j\); there are no further positive solutions. Conversely every such root yields a nonzero eigenvector of the compact form problem. A second-order initial-value problem with a single initial Robin condition has a one-dimensional solution space, so each eigenvalue is simple. The formula \(\lambda=(\kappa^2+1/4)^{-1}\) proves the stated singular-value classification. It also gives \(\kappa_1<\sqrt3/2\) because at \(\kappa=\sqrt3/2\) the phase already exceeds \(\pi\), proving \(s_1>1\).

**3. The exact square-summable mass.** In the orthogonal decomposition \(L^2(\mu_\beta)=\mathbb C\oplus L^2(0,1)\), with the atomic coordinate normalized by \(\sqrt\beta\), the atomic input column contributes
\[
1+\int_0^1\frac{\beta}{(\beta+x)^2}\,dx
=2-\frac{\beta}{\beta+1}
\]
to the Hilbert–Schmidt norm squared. The continuous-to-continuous kernel is \(\mathbf1_{0<t<x}/(\beta+x)\), and its contribution is
\[
\int_0^1\frac{x}{(\beta+x)^2}\,dx
=T+\frac{\beta}{\beta+1}-1.
\]
Adding gives \(\|H_\beta\|_{\mathcal S_2}^2=1+T\), the asserted exact trace identity. This also establishes compactness independently of the Sobolev embedding argument.

**4. High-rank and two endpoint limits.** For fixed \(T>0\), the phase equation and \(\arctan(2\kappa)=\pi/2-(2\kappa)^{-1}+O(\kappa^{-3})\) give
\[
\kappa_j=\frac{(j-3/2)\pi}{T}+O_T(j^{-1})\quad(j\to\infty).
\]
Since \(s_j=2(1+4\kappa_j^2)^{-1/2}\), it follows that \(j s_j\to T/\pi\); the \(p=1\) Schatten endpoint diverges and precisely the exponents \(p>1\) converge.

If \(T\to\infty\) at fixed \(j\), the phase equation first forces \(\kappa_j\to0\). Expanding \(3\arctan(2\kappa)=6\kappa-8\kappa^3+O(\kappa^5)\) gives
\[
\kappa_j=\frac{j\pi}{T+6}+O_j(T^{-4}),\qquad
s_j=2-\frac{4\pi^2j^2}{(T+6)^2}+O_j(T^{-4}).
\]
Since \(T=\log(1+\beta^{-1})\to\infty\) as \(\beta\downarrow0\), the logarithmic-edge constant follows.

If \(T\downarrow0\), then \(3\arctan(2\kappa_1)\to\pi\), so \(\kappa_1\to\sqrt3/2\), and implicit differentiation at \(T=0\) yields \(s_1=1+T/2+O(T^2)\). For fixed \(j\ge2\), the phase equation forces \(\kappa_j\to\infty\) and \(T\kappa_j\to(j-3/2)\pi\); therefore \(s_j/T\to[\pi(j-3/2)]^{-1}\). Every limit is for an explicitly fixed rank; no uniform-in-rank edge claim is made.

## Verification

The standalone file `check_atomic_hardy.py` implements monotone bisection for the phase equation, checks singular-value ordering and the Hilbert–Schmidt sum for six atom masses, tests the fixed-rank logarithmic-edge and rank-one limits, and compares the exact roots with singular values of finite cellwise-constant Galerkin compressions. The compression uses exact cell integrals of the Hardy kernel. Its result is `ATOMIC_HARDY_SPECTRAL_DIAGNOSTIC_OK 12069`. These are finite numerical checks, not an infinite-dimensional proof; the proof is the analytic argument above.

## Relationship to prior work

Alhamzi, Sheikh, Jadhav, Beleyur and Jeelani (2026) transfer Hardy averaging through atomless distribution functions and explicitly identify measures with atoms as requiring separate discrete–continuous theory. Their hypotheses exclude the positive initial atom here, and they do not give a spectral quantization law. Nie and Yan (2018), Example 6.3, prove a strict inequality from the classical sharp constant for general finite measures with an initial atom, but do not specify the singular spectrum, exact trace, or the logarithmic boundary law. The classical large-rank \(1/j\) singular-value behavior is consistent with existing Volterra results; the exact phase, atomic mass dependence and both limiting regimes are the claims here.

Some known discrete finite Cesàro edge laws share the same inverse-logarithmic-square scale. They concern different discretizations, and the agreement of leading coefficients is not, by itself, evidence of a new universal theorem.

## Limitations

Only one endpoint atom and an otherwise constant density on a finite interval are treated. The result concerns \(L^2\) singular values, not the full spectrum of the generally nonnormal averaging operator, and it does not classify multiple atoms or arbitrary Stieltjes measures. The literature comparison cannot rule out an implicit equivalent in a less-indexed Hardy or Sturm–Liouville text; no independent mathematical audit has been carried out. Numerical Galerkin checks support but do not replace the exact proof.

## References

1. G. Alhamzi, S. A. Sheikh, P. Jadhav, V. Beleyur and M. B. Jeelani, *Hardy Averaging via Distribution Transport: Sharp Lp Bounds, Power Weights, and a Volterra Resolvent*, Axioms **15** (2026), 391. https://doi.org/10.3390/axioms15060391 (publicly posted 25 May 2026).
2. X. Nie and D. Yan, *Sharp constant of Hardy operators corresponding to general positive measures*, Journal of Inequalities and Applications **2018**, article 78. https://doi.org/10.1186/s13660-018-1660-8 (especially Example 6.3).
3. V. K. Tuan and R. Gorenflo, *Asymptotics of singular values of Volterra integral operators*, Numerical Functional Analysis and Optimization **17** (1996), 453–461. https://doi.org/10.1080/01630569608816704 (general Volterra asymptotic background, not an asserted exact atom model).
