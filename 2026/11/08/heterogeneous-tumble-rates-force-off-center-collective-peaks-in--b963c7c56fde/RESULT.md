# Heterogeneous tumble rates force off-center collective peaks in a repulsive harmonic pair

## Finding

Consider two repelling run-and-tumble particles in one dimension, harmonically confined at strength \(\mu>0\), propelled at the same speed \(v>0\), and independently reversing direction at rates \(\gamma_1,\gamma_2>0\). The logarithmic repulsion has strength \(g>0\). Put \(a=\gamma_1/\mu\), \(b=\gamma_2/\mu\), and let \(Z=\mu(X_1+X_2)/(2v)\) be the stationary dimensionless center of mass. Its law is independent of \(g\).

For every \(a,b>0\) with \(a+b>3\), its density \(p_{a,b}\) is twice continuously differentiable, is even, is positive on \((-1,1)\), and vanishes at and outside the endpoints.

- If \(\min(a,b)<1\), then \(\max(a,b)>2\). The origin is a strict local minimum and there is at least one local maximum strictly inside each half interval. Assuming \(a<1<b\),
  \[
  p_{a,b}''(0)=\frac{16K_aK_b(b-1)(1-a)}{a+b-3}\,B(\tfrac12,a+b-2)>0,
  \qquad K_t=\frac{\Gamma(t+1/2)}{\sqrt\pi\Gamma(t)}.
  \]
- If \(\min(a,b)\ge1\), the density is strictly decreasing on \((0,1)\) and has its unique global maximum at the origin. When \(\min(a,b)=1\), this maximum has zero second derivative.

For all \(a,b>0\), the endpoint asymptotic is
\[
 p_{a,b}(z)\sim 4^{a+b-1}K_aK_bB(a,b)(1-z)^{a+b-1},\qquad z\uparrow1.
\]
Thus, in the sector \(a+b>3\), the smaller individual tumble rate controls whether the center is a local minimum or the unique global maximum, even when the total tumble rate is large. This does not classify the number of off-center maxima.

## Assumptions and scope

In the ordered region \(X_1>X_2\), let the independent stationary telegraph processes \(\sigma_i\) flip between \(\pm1\) at rates \(\gamma_i>0\). The dynamics are
\[
\dot X_1=-\mu X_1+v\sigma_1+\frac{g}{X_1-X_2},\qquad
\dot X_2=-\mu X_2+v\sigma_2+\frac{g}{X_2-X_1}.
\]
The same center law holds in the opposite ordering sector. There is no translational Brownian noise or orientation coupling. For unequal rates the collective three-valued forcing is not treated as a three-state Markov process.

## Proof

**1. Stationarity and cancellation.** The ordered gap obeys \(\dot d=-\mu d+v(\sigma_1-\sigma_2)+2g/d\). Uniformly over the orientations, this drift is positive for sufficiently small positive \(d\) and negative for sufficiently large \(d\). The gap therefore remains in its ordering sector and has a compact forward-invariant trapping interval bounded away from zero. The center has bounded forcing and also admits a compact forward-invariant trapping interval. The potential \(\mu(X_1^2+X_2^2)/2-g\log d\) has Hessian bounded below by \(\mu I\) throughout the convex ordering sector. Two trajectories with the same headings contract at rate at least \(\mu\), which gives the unique stationary pullback solution within that sector. In particular, summing the equations for \(M=(X_1+X_2)/2\) yields
\[
 \dot M=-\mu M+(v/2)(\sigma_1+\sigma_2).
\]
Hence \(Z=(U_a+U_b)/2\), where the independent variables are the stationary telegraph filters, for example \(U_a=\mu\int_0^\infty e^{-\mu s}\sigma_1(-s)\,ds\).

**2. Density and endpoints.** For a single normalized filter \(\dot U=\mu(-U+\sigma)\) with flip rate \(t\mu\), the two orientation densities with sum \(f_t\) have zero total positional flux. This fixes their difference as \(uf_t(u)\). Subtracting the orientation balance equations yields \((1-u^2)f_t'(u)=-2(t-1)uf_t(u)\). The normalized solution is
\[
 f_t(u)=K_t(1-u^2)^{t-1}\mathbf1_{\{|u|<1\}}.
\]
Indeed the individual fluxes of the two components \((1\pm u)f_t(u)/2\) vanish at the boundary, so these components define a weak stationary law without endpoint atoms. Stable contraction of the single filter identifies this law. The beta normalizer follows by substituting \(u^2\) in the integral. Thus \(p_{a,b}(z)=2(f_a*f_b)(2z)\), and the density is even with support \([-1,1]\), positive in the interior. At the center, when \(a+b>1\), \(p_{a,b}(0)=2K_aK_bB(1/2,a+b-1)\). For \(z=1-\epsilon\), the convolution interval is \([1-2\epsilon,1]\). With \(x=1-2\epsilon t\), the two squared-distance factors become \(4\epsilon t(1-\epsilon t)\) and \(4\epsilon(1-t)(1-\epsilon(1-t))\). After division by \((4\epsilon)^{a+b-1}\), dominated convergence against \(t^{a-1}(1-t)^{b-1}\) gives the coefficient \(K_aK_b B(a,b)\). The same limit of the density holds by reflection at the other end.

**3. Differentiability and the central minimum.** Suppose first \(0<a<1\). Then \(b>2\); the weak second derivative \(f_b''\) has no boundary delta since \(f_b,f_b'\) vanish at both endpoints. On \((-1,1)\),
\[
 f_b''(x)=K_b(b-1)\{-2(1-x^2)^{b-2}+4(b-2)x^2(1-x^2)^{b-3}\}.
\]
To justify continuous differentiation despite the endpoint singularity of \(f_a\), choose conjugate exponents \(P,Q\in(1,\infty)\) with \(1/P>1-a\), \(1/Q>\max(0,3-b)\). These exist since \((1-a)+\max(0,3-b)<1\). Then \(f_a\in L^P\) and \(f_b,f_b',f_b''\in L^Q\). Their convolutions are continuous by Hölder's inequality and continuity of translations in \(L^Q\); the distributional derivative identities thus give ordinary derivatives up to order two. Evaluation at zero gives
\[
 p_{a,b}''(0)=8K_aK_b(b-1)\left\{-2B(\tfrac12,a+b-2)+4(b-2)B(\tfrac32,a+b-3)\right\}.
\]
The beta recurrence gives \(B(3/2,s-3)=B(1/2,s-2)/[2(s-3)]\) for \(s=a+b>3\), proving the curvature formula. Evenness makes the first derivative zero. Positive curvature then gives a strict local minimum. Continuity on each closed half interval, positivity there away from the outer endpoint, and the strict central minimum imply attainment of a maximum strictly inside each half interval.

**4. The central-maximum sector.** For \(a,b>1\), the first weak derivatives have no boundary deltas. One has \(f_a'\in L^P\), \(f_b'\in L^Q\) for conjugate finite exponents with \(1/P>\max(0,2-a)\), \(1/Q>\max(0,2-b)\); the sum of these two lower bounds is less than one by \(a,b>1\) and \(a+b>3\). Hence \((f_a*f_b)''=f_a'*f_b'\) is continuous by the same Hölder argument, and the lower derivatives are also continuous. For \(x\in(0,2)\), using the oddness of \(f_b'\) gives
\[
 (f_a*f_b)'(x)=\int_0^1 f_b'(y)\,[f_a(x-y)-f_a(x+y)]\,dy<0.
\]
Indeed \(f_b'(y)<0\) in \((0,1)\) and the bracket is nonnegative by evenness and monotone decrease of \(f_a\) in the absolute argument; it is positive on the positive-measure set of \(y\in(0,1)\) with \(|x-y|<1\). If \(a=1\), then \(b>2\); \(f_a\) is the uniform density on \((-1,1)\), and
\[
 p_{1,b}'(z)=2[f_b(2z+1)-f_b(2z-1)].
\]
This is strictly negative for \(0<z<1\); \(f_b\) is \(C^1\) across the endpoints with \(f_b'(\pm1)=0\). The formula therefore implies \(p_{1,b}\in C^2\) with \(p_{1,b}''(0)=0\). Interchanging \(a,b\) covers the remaining cases.

## Verification

The unchanged `checker.py` in the source package evaluates the beta convolution by endpoint-weighted quadrature. The saved `CHECKER_OUTPUT.txt` records sixteen finite checks concerning curvature, monotonicity, boundary coefficients, normalization and force cancellation. These finite checks do not establish the continuum theorem; the proof above justifies differentiation even at the overlapping singular endpoints.

## Relationship to prior work

Touzo, Le Doussal and Schehr derive the force-cancelling center equation for active Dyson dynamics with equally tumbling particles. The single-filter beta law is standard. At equal rates, the centered two-heading sum is the three-state forcing of Basu and collaborators, with their outgoing rate \(\gamma_B=2\gamma_1\); that reduction does not apply to two unequal flip rates. The mixed-rate central dichotomy is not a consequence of the equal-rate case. For the edge, the exponent follows directly from the beta convolution; in particular at \(a=b=2\) the leading edge density is \(6(1-z)^3\), rather than the exponent two reported in Basu et al.'s Eq. (41) for the corresponding \(\beta=4\). Le Doussal, Majumdar and Schehr treat the relative coordinate under attraction, not this collective observable. These comparisons do not certify historical priority for the heterogeneous shape result.

## Limitations

The central dichotomy is proved only for \(a+b>3\). It proves at least one off-center maximum on each side in the mixed-rate case, not their uniqueness. The telegraph processes are independent and symmetric, confinement and propulsion are as stipulated, and there is no translational thermal noise. General beta-convolution literature could contain equivalent shape results or stronger classifications.

## References

- L. Touzo, P. Le Doussal and G. Schehr, *Interacting, running and tumbling: the active Dyson Brownian motion*, arXiv:2302.02937 (2023), Eq. (37).
- U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit and G. Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083 (2019), Eqs. (3), (7), (33), (41).
- P. Le Doussal, S. N. Majumdar and G. Schehr, *Stationary nonequilibrium bound state of a pair of run and tumble particles*, arXiv:2105.11838 (2021).
