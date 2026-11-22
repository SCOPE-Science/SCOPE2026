# A universal one-quarter chirality-flip boundary for stationary kurtosis in a trapped swimmer

## Finding
A planar active Brownian swimmer under isotropic harmonic confinement can have either negative or positive stationary Cartesian fourth cumulant when its angular velocity changes randomly between equal clockwise and counterclockwise magnitudes. The number of cumulant-sign transitions as the angular-speed magnitude increases is exactly classified by the ratio of the chirality-flip rate to the trap relaxation rate. **The universal boundary is a flip rate equal to one quarter of the trap rate.** The classification is unchanged by independent translational thermal diffusion.

Let \(\kappa,v,D_r,\lambda>0\), \(D_t\ge0\), \(\Omega\in\mathbb R\). Define the dimensionless parameters
\[
 g=\frac{D_r}{\kappa},\qquad \ell=\frac{\lambda}{\kappa},\qquad W=\left(\frac{\Omega}{\kappa}\right)^2.
\]
Define the polynomials
\[
\begin{aligned}
 A={}&4\ell-1,\\
 B={}&10g^3+(13\ell+8)g^2-(28\ell^2+38\ell+12)g
 -(28\ell^3+68\ell^2+47\ell+10),\\
 C={}&14g^5+(91\ell+83)g^4+(210\ell^2+396\ell+166)g^3\\
 &+(196\ell^3+594\ell^2+538\ell+148)g^2\\
 &+(56\ell^4+280\ell^3+454\ell^2+284\ell+60)g\\
 &+(24\ell^4+84\ell^3+102\ell^2+51\ell+9),
\end{aligned}
\]
and the strictly positive polynomial
\[
\begin{aligned}
 H={}&(g^2+2g\ell+2g+2\ell+W+1)^2\\
 &\quad\cdot(g^2+2g\ell+6g+6\ell+W+9)\\
 &\quad\cdot(4g^2+2g\ell+4g+\ell+W+1).
\end{aligned}
\]
For every unit vector \(e\) in the plane, the stationary fourth cumulant of the projected position \(e\cdot X\) is exactly
\[
\boxed{\operatorname{cum}_4(e\cdot X)=
\frac{3v^4}{8\kappa^4}\frac{AW^2+BW-C}{H}.}
\]
All coefficients in \(C\) are strictly positive for \(g,\ell>0\); therefore the fourth cumulant is strictly negative at zero angular velocity.

The following is the complete sign classification for all \(W\ge0\):

1. If \(\ell>1/4\), there is exactly one positive zero \(W_*\) and the sign is strictly negative before it and strictly positive after it. In particular,
   \[
   W_*=\frac{-B+\sqrt{B^2+4AC}}{2A}.
   \]
2. If \(\ell=1/4\), then
   \[
   B=\frac{(2g+3)(80g^2-30g-141)}{16}.
   \]
   Set \(g_c=(15+\sqrt{11505})/80\). For \(g>g_c\), there is exactly one positive zero \(W_*=C/B\), with the same negative-to-positive sign change. For \(g\le g_c\), the cumulant is strictly negative for every finite \(W\ge0\).
3. If \(0<\ell<1/4\), a strictly positive cumulant interval exists if and only if \(B>0\) and \(\Delta=B^2+4AC>0\). In that case there are exactly two positive zeros
   \[
   W_-=\frac{-B+\sqrt\Delta}{2A},\qquad
   W_+=\frac{-B-\sqrt\Delta}{2A},\qquad 0<W_-<W_+,
   \]
   and the cumulant is positive precisely for \(W_-<W<W_+\), and negative outside the closed interval. If \(B>0\) and \(\Delta=0\), there is a single zero of even multiplicity, with no positive region. Otherwise the cumulant is strictly negative for all \(W\ge0\).

In particular, at large \(|\Omega|\), for \(\ell\ne1/4\),
\[
\operatorname{cum}_4(e\cdot X)\sim
\frac{3v^4}{8\kappa^4}(4\ell-1)
\left(\frac{\kappa}{\Omega}\right)^4.
\]
For instance, \(g=1,\ell=1\) gives the unique positive root \(W_*=82.23232\ldots\). For \(g=5,\ell=1/10\), there are instead two roots \(W_-=100.22544\ldots\) and \(W_+=2210.92789\ldots\), exhibiting a negative–positive–negative sequence.

## Assumptions and scope
Let \(\sigma_t\in\{-1,+1\}\) be a stationary symmetric telegraph chain changing sign at rate \(\lambda>0\) in each state. Let \(B_t\), \(W_t\) be independent two-sided standard Brownian motions, independent of the telegraph chain, with \(B_t\) scalar and \(W_t\) two-dimensional. Let \(\theta_t\) take values modulo \(2\pi\), with the stationary rotationally invariant distribution, and let \(X_t\in\mathbb R^2\) solve
\[
 d\theta_t=\Omega\sigma_t\,dt+\sqrt{2D_r}\,dB_t,\qquad
 dX_t=(-\kappa X_t+v(\cos\theta_t,\sin\theta_t))\,dt
 +\sqrt{2D_t}\,dW_t.
\]
Because \(D_r>0\), the angular subsystem has uniform stationary orientation and a symmetric stationary telegraph sign; \(\kappa>0\) gives a unique stationary positional solution obtained by convolution from the infinite past. All reported cumulants are central stationary cumulants. No result depends on the observation direction \(e\) by joint rotational invariance. The parameter \(D_t\) may be zero.

## Proof
**1. Separate active and Gaussian fluctuations.** The stationary solution splits into independent contributions \(X=X^{(a)}+X^{(t)}\), with \(X^{(t)}\) a centered isotropic Gaussian vector of per-coordinate variance \(D_t/\kappa\) and \(X^{(a)}\) determined by orientation and chirality switching. The fourth cumulant of a sum of independent variables is additive; the Gaussian fourth cumulant is zero. Therefore \(\operatorname{cum}_4(e\cdot X)=\operatorname{cum}_4(e\cdot X^{(a)})\) and is independent of \(D_t\).

**2. Close the angular-moment hierarchy exactly.** Rescale time by \(\kappa^{-1}\) and active position by \(v/\kappa\). Write \(Z\) for the resulting complex active position. Its deterministic drift is \(\dot Z=-Z+e^{i\theta}\). For every pair of nonnegative integers \(p,q\), let \(m=q-p\) and define
\[
 S_{pq}=\mathbb E[Z^p\overline Z^{q}e^{im\theta}],\qquad
 T_{pq}=\mathbb E[\sigma Z^p\overline Z^{q}e^{im\theta}].
\]
The stationary generator gives, for \(p+q>0\),
\[
\begin{aligned}
 nS_{pq}-im\sqrt W\,T_{pq}&=pS_{p-1,q}+qS_{p,q-1}=R_S,\\
 (n+2\ell)T_{pq}-im\sqrt W\,S_{pq}&=pT_{p-1,q}+qT_{p,q-1}=R_T,
\end{aligned}
\qquad n=p+q+gm^2.
\]
Terms with negative indices are omitted. The initial values are \(S_{00}=1\), \(T_{00}=0\). Since \(n>0\) and \(n(n+2\ell)+m^2W>0\), this is an unambiguous exact recursive solution through any finite degree:
\[
 S_{pq}=\frac{(n+2\ell)R_S+im\sqrt W\,R_T}{n(n+2\ell)+m^2W},\qquad
 T_{pq}=\frac{im\sqrt W\,R_S+nR_T}{n(n+2\ell)+m^2W}.
\]
In particular the second radial active moment is
\[
 S_{11}=\frac{g+2\ell+1}{g^2+2g\ell+2g+2\ell+W+1}.
\]
Application of exactly the same recursion through total degree four and cancellation of common factors yields the polynomial identity
\[
 S_{22}-2S_{11}^2=\frac{AW^2+BW-C}{H}.
\]
This identity is also checked symbolically by the accompanying standalone program, which constructs the complete recursive moment system from the generator rather than taking the polynomial formula as input.

**3. Convert radial moments into projected cumulants.** Rotational invariance and conditioning on radius give \(\mathbb E[(e\cdot X^{(a)})^2]=\mathbb E|X^{(a)}|^2/2\) and \(\mathbb E[(e\cdot X^{(a)})^4]=3\mathbb E|X^{(a)}|^4/8\). Thus
\[
 \operatorname{cum}_4(e\cdot X^{(a)})=
 \frac38\left(\frac v\kappa\right)^4(S_{22}-2S_{11}^2),
\]
which proves the exact formula and independence from \(e\) and \(D_t\).

**4. Classify every zero and sign.** For positive \(g,\ell\) and \(W\ge0\), all factors in \(H\) are positive and every summand of \(C\) is positive. The sign of the cumulant is exactly that of the quadratic \(P(W)=AW^2+BW-C\). If \(A>0\), then \(P(0)<0\), \(P(W)\to+\infty\), and its root product \(-C/A<0\) forces exactly one positive root. If \(A<0\), it is a concave quadratic starting and ending negative; it has a positive open interval precisely when its positive vertex lies above zero, equivalent to \(B>0\) and \(\Delta=B^2+4AC>0\). Equality in the latter yields a double zero, never positivity. If \(A=0\), the sign is that of the linear polynomial \(BW-C\); exact factorization of \(B\) gives \(g_c\). These arguments prove all cases without numerical extrapolation.

**5. Large-chirality boundary.** The denominator has degree four in \(W\), and the numerator has degree two. Its leading coefficient is exactly \(A=4\ell-1\). Replacing \(W\) with \((\Omega/\kappa)^2\) proves the asymptotic sign law and the universal quarter-rate boundary. No finite computation is used in proving this limit or the uniqueness statements.

## Verification
Run `python verify.py` from the directory containing this file. The program requires SymPy and Python 3. It reconstructs both stationary radial moments through degree four using the generator, simplifies the resulting rational identity to zero symbolically, factors the critical boundary, and confirms the zero-angular-speed independence from the switching rate. A separate calculation integrates all orderings of two and four angular observations through Fourier-tilted two-state Markov resolvents. It successfully compared 37 sets of exact generator moments with these independent ordered-time integrals and exercised both one-crossing and two-crossing sign examples. Finite numerical checks corroborate, but do not replace, the generator proof and elementary sign arguments.

## Relationship to prior work
Das and Basu (2023, arXiv:2301.11194, Sections 2–5 and appendices) formulated exactly the free, symmetric *chirality-reversing* swimmer with angular velocity \(\Omega\sigma_t\), and determined its time-dependent second-order and position-distribution regimes. Their position was not harmonically trapped; the trap-dependent stationary fourth-cumulant phase diagram above is not among their results. Caprini, Löwen and Marini Bettolo Marconi (2023, arXiv:2306.11133, Sections III–IV) examined confined swimmers of *constant* chirality, including projected kurtosis. Pattanayak and collaborators (2025/2026, arXiv:2509.03448 and arXiv:2603.26967) derive extensive higher-moment results for fixed intrinsic torque, not an independently switching torque sign. Santra, Basu and Sabhapandit (2021, arXiv:2107.12640) instead reverse the *propulsion direction*.

The most closely matched independently published torque-switching result, *Faster biased chirality reversals strictly amplify trapped orbital circulation* (2026), establishes signed second-order orbital currents and spatial covariances for unequal sign-flipping rates in harmonic traps. Its complete result and proof address current/covariance, not the fourth cumulant or the universal one-quarter flip-rate boundary. Other related fourth-cumulant literature treats different mechanisms, including velocity-direction reversals, Poisson changes of orientation rather than angular velocity, or fixed-torque motion. General Fourier-generator and Markov-modulated linear-response methods are prior techniques and are not claimed as novel. Implicit coverage in broader unindexed higher-order results remains a scientific-priority risk, not a claim of exhaustive novelty.

## Limitations
The result concerns a single overdamped active swimmer with constant propulsion magnitude, isotropic linear confinement, Brownian angular diffusion, and independent symmetric exponential chirality reversal times. The full stationary spatial density, transition-path statistics, nonlinear traps, asymmetric sign-flip rates, inertial dynamics, interactions, and finite-sample statistical detection are not classified. Even when the fourth cumulant vanishes, the stationary position law is not asserted Gaussian. The sign classification is a rigorously derived model-specific mathematical result; it is not an experimental test or independent publication-priority certificate.

## References
1. S. Das and U. Basu, *Chirality Reversing Active Brownian Motion in Two Dimensions*, arXiv:2301.11194, first public 2023-01-26, https://arxiv.org/html/2301.11194v1 (Sections 2–5, Appendices A–B).
2. L. Caprini, H. Löwen and U. Marini Bettolo Marconi, *Chiral active matter in external potentials*, arXiv:2306.11133, first public 2023-06-19, https://arxiv.org/abs/2306.11133 (Sections III–IV).
3. I. Santra, U. Basu and S. Sabhapandit, *Direction reversing active Brownian particle in a harmonic potential*, arXiv:2107.12640, first public 2021-07-27, https://arxiv.org/abs/2107.12640 (Sections 1–4).
4. A. Pattanayak, A. Shee, D. Chaudhuri and A. Chaudhuri, *Chirality, confinement and dimensionality govern re-entrant transitions in active matter*, arXiv:2509.03448, first public 2025-09-03, https://arxiv.org/abs/2509.03448.
5. A. Pattanayak, A. Shee, A. Chaudhuri and D. Chaudhuri, *Characterizing exact dynamics of a trapped active Brownian particle under torque in two and three dimensions*, arXiv:2603.26967, first public 2026-03-27, https://arxiv.org/abs/2603.26967.
6. *Faster biased chirality reversals strictly amplify trapped orbital circulation*, public research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-faster-biased-chirality-reversals-strictly-amplify-trapped-orbit--86480f46eb3b.
