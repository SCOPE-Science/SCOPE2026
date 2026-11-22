# A sharp peak-number transition under thermally calibrated Gaussian resetting of a harmonic diffusion

## Finding

Consider a harmonically confined overdamped particle, completely reset at Poisson rate \(r>0\) to either of two equilibrium-width Gaussian packets centered at \(\pm L\), with equal probabilities. Let \(\kappa,D,L>0\) denote relaxation rate, diffusion coefficient and packet-center distance; reset width is fixed to the bath-equilibrium variance \(V=D/\kappa\). Write \(a=r/\kappa\) and \(s=V/L^2\).

**Complete stationary mode classification.** For \(0<a\le1\), the stationary density has exactly one mode at zero for every \(s>0\). For \(a>1\), put
\[
H_a(t)=(a-1)\int_0^1 u^{a-1}\exp\{t(1-u^2)\}\,du,\qquad t=\frac{1}{2s}.
\]
There is exactly one positive \(t_c(a)\) satisfying \(H_a(t_c)=1\). Set \(s_c(a)=1/[2t_c(a)]\). The stationary density is strictly unimodal if \(s\ge s_c(a)\); at equality its unique central maximum is quartically flat. If \(0<s<s_c(a)\), the density has exactly two strict symmetric global modes and the origin is a strict local minimum. As \(s\uparrow s_c(a)\) from below, their locations \(\pm Lm(s)\) satisfy the exact square-root opening law
\[
m(s)^2=3\bigl(s_c(a)-s\bigr)+o\bigl(s_c(a)-s\bigr).
\]
For \(a=2\), the critical root is the unique positive solution of \(e^t=1+2t\), namely \(t_c=1.2564312086\ldots\), and \(s_c=0.3979525473\ldots\). The critical function satisfies \(t_c(a)\to\infty\) as \(a\downarrow1\) and \(t_c(a)\to1/2\) as \(a\to\infty\).

## Assumptions and scope

The unreset dynamics on the real line are the Itô diffusion
\[
dX_t=-\kappa X_t\,dt+\sqrt{2D}\,dW_t.
\]
At the times of an independent rate-\(r\) Poisson process, the entire position is replaced by an independent draw from \(\tfrac12\mathcal N(-L,V)+\tfrac12\mathcal N(L,V)\), where \(V=D/\kappa\). Every reset draw, sign and Brownian increment is independent. All parameters \(\kappa,D,L,r\) are strictly positive. Statements concern the unique stationary position density on \(\mathbb R\), global maxima (modes), and its derivatives; they do not concern pathwise entropy production or a finite-time transient.

## Proof

**1. Exact stationary representation and uniqueness.** The last-reset age \(A\) in stationarity is exponential with rate \(r\). The Ornstein–Uhlenbeck semigroup maps \(SL+Z_0\), where \(S\) is an unbiased random sign and \(Z_0\sim\mathcal N(0,V)\), to \(SLe^{-\kappa A}+Z_A\). The Gaussian noise at age \(A\) has variance \(V(1-e^{-2\kappa A})\), so the sum of the damped reset Gaussian and this noise has exactly the age-independent variance \(V\). Consequently the stationary law is
\[
X\ \overset{d}=\ L S U+Z,\qquad U=e^{-\kappa A}\sim\operatorname{Beta}(a,1),\quad Z\sim\mathcal N(0,V),
\]
with all three variables independent. Regeneration at a positive Poisson rate gives existence and uniqueness. Dividing by \(L\) gives the convolution \(p_{a,s}=f_a*\varphi_s\), with
\[
f_a(u)=\frac a2 |u|^{a-1}\mathbf1_{\{|u|<1\}},\qquad
\varphi_s(x)=\frac{e^{-x^2/(2s)}}{\sqrt{2\pi s}}.
\]
All derivatives of \(p_{a,s}\) exist and are analytic in the real argument.

**2. The low-rate regime.** For \(0<a\le1\), \(f_a\) is symmetric and nonincreasing on the positive half-line. Any such integrable density is a positive mixture of uniform densities on symmetric intervals; the convolution of \(\varphi_s\) with a uniform density on \([-b,b]\) has derivative \([\varphi_s(x+b)-\varphi_s(x-b)]/(2b)<0\) for every \(x>0\). Mixture and strict Gaussian positivity give \(p'_{a,s}(x)<0\) for \(x>0\), hence a unique global mode at zero.

**3. One-zero theorem for the density derivative.** Suppose \(a>1\). Distributionally differentiate \(f_a\) in the interval and include the two endpoint jumps. With \(w=x/s>0\) and \(t=1/(2s)\), convolution and pairing the positive and negative halves yield
\[
p'_{a,s}(x)=a\varphi_s(0)e^{-x^2/(2s)}e^{-t}\sinh(w)\bigl[H_{a,t}(w)-1\bigr],
\]
where
\[
H_{a,t}(w)=(a-1)\int_0^1u^{a-2}e^{t(1-u^2)}\frac{\sinh(uw)}{\sinh w}\,du.
\]
For every fixed \(0<u<1\), the ratio \(\sinh(uw)/\sinh w\) decreases strictly with \(w>0\). Indeed, its logarithmic derivative is \(u\coth(uw)-\coth w<0\), because \(z\mapsto z\coth z\) strictly increases on \((0,\infty)\). Thus \(H_{a,t}(w)\) is continuous and strictly decreasing. Its limit at infinity is zero by dominated convergence, while its limit as \(w\downarrow0\) is exactly \(H_a(t)\). Hence \(p'\) has no positive zero when \(H_a(t)\le1\) and exactly one positive zero when \(H_a(t)>1\); in the latter case \(p'\) changes sign from positive to negative. Symmetry establishes the complete global mode classification, without assuming a priori that only two peaks can appear.

**4. The unique threshold.** For \(a>1\), \(H_a(0)=(a-1)/a<1\); moreover
\[
H'_a(t)=(a-1)\int_0^1u^{a-1}(1-u^2)e^{t(1-u^2)}\,du>0.
\]
An interval of positive measure with \(u<1\) makes \(H_a(t)\to\infty\) as \(t\to\infty\). Hence it crosses one exactly once. Since \(t=1/(2s)\), the two-mode phase occurs precisely for \(s<s_c\).

**5. Critical quartic behavior and opening.** Uniformly for \(t\) near \(t_c\), expansion at \(w=0\) gives
\[
H_{a,t}(w)=H_a(t)-\frac{H'_a(t)}6w^2+O(w^4).
\]
At \(t_c\), the prefactor of \(p'\) is positive and asymptotic to a positive multiple of \(w\), whereas the bracket is a strictly negative multiple of \(w^2\). Consequently \(p''(0)=0\) and \(p^{(4)}(0)<0\). On the two-mode side the unique nonzero critical point obeys \(w^2=6(t-t_c)+o(t-t_c)\). Replacing \(w=x/s\) and \(t=1/(2s)\) gives \(m(s)^2=3(s_c-s)+o(s_c-s)\), as stated.

**6. Exact example and limits.** When \(a=2\), direct integration yields \(H_2(t)=(e^t-1)/(2t)\), so the positive threshold solves \(e^t=1+2t\). To see \(t_c(a)\to\infty\) as \(a\downarrow1\), use \(H_a(t)\le(a-1)e^t/a\) for fixed \(t\). To see \(t_c(a)\to1/2\) as \(a\to\infty\), write \(H_a(t)=(1-1/a)\mathbb E[e^{t(1-U_a^2)}]\), \(U_a\sim\operatorname{Beta}(a,1)\); the uniform-on-compact-\(t\) asymptotic is \(a[H_a(t)-1]\to 2t-1\). This places the unique root between any two fixed values on opposite sides of \(1/2\) for large \(a\).

## Verification

The independently runnable Python 3 standard-library file `checker.py` verifies the threshold, strict monotonicity of the derivative-sign ratio, several explicit one-mode/two-mode examples, the exact \(a=2\) root, beta moment identities, and convergence of the opening coefficient to three. It completed 59 numerical assertions. Quadrature and finite sampling are consistency checks; the all-parameter and global statements are established by the analytic steps above. Reproduce with `python3 checker.py`.

## Relationship to prior work

Olsen, *Steady-state moments under resetting to a distribution* (2023), derives the last-reset renewal equation and exact moment hierarchies for general distributed resetting in harmonic confinement, including Gaussian reset distributions. The renewal representation and the equilibrium Gaussian identity are used here as established starting points; neither is claimed as original. Olsen's Sections II–III develop moments, cumulants and their response to resetting, not this complete symmetric-packet stationary mode classification. Trajanovski and collaborators (2023) address ordinary Ornstein–Uhlenbeck resetting and comb geometries, not paired, thermally calibrated Gaussian packets. Research records on symmetric **point** resetting and thermal run-and-tumble bimodality have related peak-transition statements, but their reset laws and underlying dynamics differ and their reported thresholds do not imply the parameter-dependent integral boundary here. The assessed result is the exact one-versus-two stationary mode theorem, including an exhaustive derivative sign argument and the mode-opening law, for the stated Gaussian-packet model.

## Limitations

Thermal calibration \(\operatorname{Var}(\text{packet})=D/\kappa\) is an essential hypothesis: without it the Gaussian component at a fixed reset age has age-dependent variance and the proof does not apply. The reset packets are exactly equally weighted and equally broad; non-symmetric resetting can have different mode geometry. The mathematical result does not quantify physical preparation cost, finite-sample mode detection or experimental feasibility. General renewal identities predate this classification; implicit prior deductions from those identities or the Gaussian-convolution literature cannot be completely excluded without an independent literature audit.

## References

1. K. S. Olsen, *Steady-state moments under resetting to a distribution* (first arXiv version, 7 October 2023), arXiv:2310.04840. https://arxiv.org/abs/2310.04840
2. P. Trajanovski, P. Jolakoski, K. Zelenkovski, A. Iomin, L. Kocarev, T. Sandev, *Ornstein-Uhlenbeck process and generalizations: particle's dynamics under comb constraints and stochastic resetting* (first arXiv version, 28 January 2023), arXiv:2301.12304. https://arxiv.org/abs/2301.12304
3. M. Gueneau, S. N. Majumdar, G. Schehr, *Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables* (first arXiv version, 15 June 2023), arXiv:2306.09453. https://arxiv.org/abs/2306.09453
