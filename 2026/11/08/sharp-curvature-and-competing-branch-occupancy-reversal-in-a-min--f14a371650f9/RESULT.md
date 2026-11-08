# Sharp curvature and competing-branch occupancy reversal in a minimal resetting semi-Markov network

## Finding

**Theorem (gamma-memory response and sharp reversal).** In the three-state resetting semi-Markov star specified below, let \(x(\lambda)\) and \(y(\lambda)\) denote the stationary occupancies of the two leaves when the center-to-first-leaf competing rate \(\lambda\) varies. The response graph \(y\) against \(x\) is strictly convex for gamma shape \(0<\nu<1\), a straight line for \(\nu=1\), and strictly concave for \(\nu>1\). In the last regime, the occupancy of the **other, decreasingly selected leaf** has at most one strict maximum; it exists exactly when \(r/k>z_*(\nu,a/(a+r))\), where \(z_*\) is the unique positive solution of

\[
\frac{a}{a+r}+(1+z)^{\nu-1}\big((\nu-1)z-1\big)=0.
\]

The maximum occurs at \(\lambda_*=r/z_*-k\). For gamma shape \(\nu=2\), the condition and maximizer simplify to

\[
\boxed{\ r(r+a)>k^2,\qquad \lambda_*=\sqrt{r(r+a)}-k.\ }
\]

For \(0<\nu\le1\), or when \(\nu>1\) and \(r/k\le z_*\), the second leaf occupancy is strictly decreasing for every \(\lambda>0\). A three-state occupancy graph is the smallest state space where nonaffine pairwise stationary response can occur.

## Assumptions and scope

The state space is \(\{0,1,2\}\), with center state \(0\) and two leaf states \(1,2\). Fix \(k,a,r>0\), gamma shape \(\nu>0\), and variable \(\lambda>0\). On entering state \(0\), independently sample a sojourn time with gamma distribution of shape \(\nu\) and rate \(q=k+\lambda\). At completion, jump to leaf \(1\) with probability \(\lambda/q\), or leaf \(2\) with probability \(k/q\). On entering either leaf, wait an independent exponential time of rate \(a\) and jump to state \(0\). Independently, a Poisson process of rate \(r\) resets the system instantaneously to \(0\), restarting its center waiting time even if the reset occurs while already in \(0\). All waiting times, branch choices and reset times are mutually independent between renewals.

The initial state after reset is \(0\). The positive reset rate gives a unique limiting time-stationary occupancy distribution. Occupation probabilities refer to visible states, not internal phases of an integer-shape gamma distribution. The parameter variation changes both the center exit branch probability and its holding-time scale; that coupled variation is essential.

Put

\[
 p=\frac{\lambda}{k+\lambda},\quad c=\frac rk,\quad
 v=\frac a{a+r},\quad
 h(p)=\frac{(1+c(1-p))^\nu-v}{1-v}.
\]

Then the full stationary law is

\[
 \boxed{\quad \pi_1=x(p)=\frac p{h(p)},\qquad
 \pi_2=y(p)=\frac{1-p}{h(p)},\qquad
 \pi_0=1-\frac1{h(p)}.\quad}
\]

Every denominator is positive for the stated domain; \(p\in(0,1)\).

## Proof

**1. Reset-renewal occupation formula.** For a no-reset process launched from the center, denote by \(U_s\) and \(V_s\) the Laplace transforms of the center and leaf sojourn laws at \(s>0\). Here \(U_s=((k+\lambda)/(k+\lambda+s))^\nu\) and \(V_s=a/(a+s)\). Each complete center-to-leaf-to-center excursion has transform \(U_sV_s\). The Laplace transform of the probability of still being in the center during its current sojourn, summed over arbitrarily many excursions, is

\[
 \widetilde P_0(s)=\frac{1-U_s}{s(1-U_sV_s)}.
\]

The transform for occupation of leaf \(1\) is the sum of a center completion, a branch choice and the residual leaf survival time:

\[
 \widetilde P_1(s)=\frac{pU_s(1-V_s)}{s(1-U_sV_s)},\qquad
 \widetilde P_2(s)=\frac{(1-p)U_s(1-V_s)}{s(1-U_sV_s)}.
\]

Their sum is \(1/s\), confirming conservation. Poisson resetting to the same initial center-age state supplies the renewal identity \(\pi_i=r\widetilde P_i(r)\). With \(u=U_r=(1+c(1-p))^{-\nu}\), \(v=V_r\), and \(w=u(1-v)/(1-uv)=1/h\), this gives the stated \(\pi_0,\pi_1,\pi_2\). Regeneration on every reset makes the invariant occupation law unique.

**2. Universal curvature.** Since

\[
 h'(p)=-\frac{\nu c(1+c(1-p))^{\nu-1}}{1-v}<0,
 \quad h''(p)=\frac{\nu(\nu-1)c^2(1+c(1-p))^{\nu-2}}{1-v},
\]

we have \(x'(p)=(h-ph')/h^2>0\), so \(y\) is a single-valued function of \(x\). Directly differentiating \(y=(1-p)/h\) and eliminating \(p\) gives

\[
 \boxed{\frac{\mathrm d^2 y}{\mathrm d x^2}
 =-\frac{h''(p)h(p)^3}{(h(p)-p h'(p))^3}.}
\]

All other factors are strictly positive. Therefore the curvature sign is exactly the opposite of \(\nu-1\), with no zeros or inflection points away from \(\nu=1\). At \(\nu=1\), \(h\) is affine and the complete response graph is a straight line. In any two-state model, the two distinct occupation probabilities sum to one identically, so their graph is always affine: three states are minimal for this nonaffinity.

**3. Occupation response of the losing branch.** Because \(p\) is strictly increasing in \(\lambda\), it suffices to differentiate \(y(p)\). Put \(z=c(1-p)=r/(k+\lambda)\). A direct calculation yields

\[
 \frac{\mathrm d y}{\mathrm d p}
 =\frac{F_\nu(z)}{(1-v)h(p)^2},\quad
 F_\nu(z)=v+(1+z)^{\nu-1}((\nu-1)z-1).
\]

Moreover

\[
 F_\nu(0)=v-1<0,\qquad
 F'_\nu(z)=\nu(\nu-1)z(1+z)^{\nu-2}.
\]

For \(0<\nu<1\), \(F_\nu\) decreases from a negative value, while for \(\nu=1\) it equals \(v-1\). Thus \(y\) always falls as \(\lambda\) rises. For \(\nu>1\), \(F_\nu\) strictly increases, starts negative and tends to positive infinity as \(z\to\infty\); it consequently has exactly one positive zero \(z_*\). As \(\lambda\) rises from zero to infinity, \(z\) strictly decreases from \(r/k\) to zero. If \(r/k>z_*\), the sign of \(y'\) changes once from positive to negative at \(\lambda_*=r/z_*-k\), yielding its unique strict global maximum. Otherwise the response is strictly negative for all positive \(\lambda\). When \(\nu=2\), \(F_2(z)=z^2+v-1\), so \(z_*=\sqrt{1-v}=\sqrt{r/(a+r)}\) and the threshold reduces exactly to \(r(r+a)>k^2\). This completes the proof.

## Verification

`verify_gamma_star.py` performs 384 deterministic assertions. For integer gamma shapes one through four it independently constructs the expanded continuous-time Markov chain with the correct phase-by-phase reset transitions and solves its stationary linear system at multiple parameter values. The checks also compare gamma-function probability normalization, algebraic curvature signs, derivative signs and the unique maximizer in the shape-two case. Run using `python verify_gamma_star.py`; NumPy is required. These finite computations test the formulas but are not substitutes for the preceding proof for arbitrary real \(\nu\).

As an illustrative nondegenerate case, \(k=a=r=1\), \(\nu=2\) gives the exact peak \(\lambda_*=\sqrt2-1\); the other-leaf occupancy rises on \((0,\sqrt2-1)\) and falls on \((\sqrt2-1,\infty)\).

## Relationship to prior work

Bebon and Speck (first publicly available February 23, 2026) establish mutual linearity for stationary *Markov* networks under local edge-rate variation. Voits and Schwarz (first publicly available April 30, 2026) give graph-theoretic extensions to transient Markov occupations and first passage. Both are credited as foundational Markov results. For \(\nu=1\), the present theorem reproduces the affine pairwise Markov response, rather than claiming it anew.

Voits and Schwarz's November 4, 2026 semi-Markov extension establishes broad sufficient conditions for affine response, qualitative exceptions and renewal resetting identities, and numerically illustrates general memory-dependent counterexamples using a larger network. Its general framework and reset identity are credited. The present theorem specializes to a different, fully specified coupled gamma-rate/branching perturbation and derives a **sharp curvature sign for every positive gamma shape**, a **minimal three-state witness**, and an **exact necessary-and-sufficient criterion and location for the counterintuitive competing-leaf occupation maximum**. The generic affine criterion and renewal formula alone do not state these classifications; the specialization requires the calculations proved here.

## Limitations

The law requires all reset events to restart the center age. It does not apply unchanged to resets that preserve residual holding time, distinct leaf holding rates, non-Poisson resetting or arbitrary center waiting-time families. The curvature statement concerns the pair of leaf occupancies as \(\lambda\) varies, not their separate curvature against the control. Strict maximum classification assumes \(\lambda>0\) with \(k,a,r>0\) fixed. Although primary sources and indexed claims were compared, an unindexed or unavailable specialized result could still cover part of the exact model; no claim of exhaustive literature uniqueness or independent audit is made.

## References

1. R. Bebon and T. Speck, “Mutual Linearity Is a Generic Property of Steady-State Markov Networks,” arXiv:2602.20321v1, February 23, 2026, https://arxiv.org/abs/2602.20321 ; *Physical Review Letters* 136, 137401 (2026), https://doi.org/10.1103/jcm3-57d8.
2. J. B. Voits and U. S. Schwarz, “Graph theoretic derivation of mutual linearity for transient probabilities and hitting time distributions in Markov networks,” arXiv:2605.00135v1, April 30, 2026, https://arxiv.org/abs/2605.00135.
3. J. B. Voits and U. S. Schwarz, “Mutual linearity in semi-Markov networks,” arXiv:2611.06490v1, November 4, 2026, https://arxiv.org/html/2611.06490v1 (related comparison, not the first motivating source).
