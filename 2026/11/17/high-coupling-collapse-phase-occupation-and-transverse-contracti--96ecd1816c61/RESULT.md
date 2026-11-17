# High-coupling collapse, phase occupation, and transverse contraction of four chemical limit cycles

## Finding
Consider the planar polynomial chemical flow
\[
\dot x=xy(-h h_x-\varepsilon h_y),\qquad
\dot y=xy(-h h_y+\varepsilon h_x),
\]
where \(\varepsilon>0\), \(h(x,y)=q_\mu(x-2,y-2)\), and
\[
q_\mu(u,v)=16(u^4+v^4)-25(u^2+v^2)+\mu u^2v^2+9.
\]
For \(\mu>337/9\), four attracting periodic ovals are known to exist in the strictly positive quadrant. This theorem classifies their *opposite, high-coupling degeneration* as \(\mu\to\infty\) in four quantitative senses: geometric area and thickness, original-time period, time-uniform phase occupation, and transverse Floquet contraction.

Write \(\sigma=+1\) for the right and upper ovals and \(\sigma=-1\) for the left and lower ovals, with axes centered at \((2,2)\). Let \(A_\mu\) denote the Euclidean area enclosed by any one oval, \(T_{\sigma,\mu}\) its least *original physical-time* period, and \(\rho_\mu\) the common nontrivial transverse Floquet multiplier. Set
\[
a(s)=(16s^2-9)(1-s^2),\qquad
J_\sigma=\int_{3/4}^1\frac{ds}{(2+\sigma s)s\sqrt{a(s)}}.
\]
Then all four limit cycles satisfy
\[
A_\mu=\frac{\pi}{8\sqrt\mu}+O(\mu^{-3/2}),\qquad
T_{\sigma,\mu}=\frac{J_\sigma}{2\varepsilon\sqrt\mu}+O_\varepsilon(\mu^{-3/2}),
\]
\[
\log\rho_\mu=-\frac{49\pi}{256\varepsilon}\sqrt\mu+O_\varepsilon(\mu^{-1/2}).
\]
Their maximum normal displacement from the corresponding axis tends to zero with the sharp law \(\sqrt\mu\,\max|v|\to1\) (with the coordinate roles interchanged for upper/lower ovals). The two period constants are distinct, \(0<J_+<J_-\), and obey the explicit sum identity
\[
J_++J_-=\frac\pi2\left(\frac13+\frac1{\sqrt{165}}\right).
\]
Consequently the original-time transverse Lyapunov exponents \(\chi_{\sigma,\mu}=\log\rho_\mu/T_{\sigma,\mu}\) satisfy
\[
\frac{\chi_{\sigma,\mu}}{\mu}\longrightarrow-\frac{49\pi}{128J_\sigma},
\]
independently of \(\varepsilon\): the multipliers tend to zero while the physical periods tend to zero, with two distinct linear-in-\(\mu\) contraction rates.

There is also a singular *physical-time occupation law*. For an oval with axial sign \(\sigma\), sample a point uniformly in time during one complete circuit. Let \(S\in(3/4,1)\) be the absolute unshifted axial coordinate and let \(\Xi\) be \(\sqrt\mu\) times the signed unshifted transverse coordinate (for a vertical oval exchange \(u,v\)). Then for every bounded continuous test function \(\varphi\),
\[
\lim_{\mu\to\infty}\mathbb E\varphi(S,\Xi)
=\frac1{2J_\sigma}\sum_{\eta=\pm1}\int_{3/4}^1
\frac{\varphi\bigl(s,\eta\sqrt{a(s)}/s\bigr)}{(2+\sigma s)s\sqrt{a(s)}}\,ds.
\]
The limiting phase distribution is not uniform along the collapsed axial segment: its two signed transverse branches have equal weights but a nonconstant, integrable endpoint-singular axial density.

## Assumptions and scope
The parameters are \(\varepsilon>0\) fixed and real \(\mu\to+\infty\). The four ovals are those of the strictly positive chemical flow defined above, not arbitrary reaction-network realizations. All geometry is measured in the physical \((x,y)\) plane; area is Euclidean area. Both period and phase occupation use the actual ODE time, without time reparametrization. Floquet multipliers are nontrivial eigenvalues of a return map on transverse sections. Big-O constants for period and multiplier may depend on fixed \(\varepsilon\). The exact graph formulas below apply whenever \(\mu>400/9\); that restriction is immaterial to the high-coupling limits. The identities describing the originating algebraic family and the four stable ovals are prior inputs.

## Proof
**1. Exact oval graphs and thin geometry.** Put \(u=x-2\), \(v=y-2\). The right and left ovals are parametrized by
\[
(u,v)=(\sigma s,\eta v_\mu(s)),\qquad
3/4\le s\le1,\quad \sigma,\eta\in\{\pm1\},
\]
where \(v_\mu(s)\ge0\) is the positive square root of
\[
v_\mu(s)^2=\frac{2a(s)}{b_\mu(s)+\sqrt{b_\mu(s)^2+64a(s)}},\qquad b_\mu(s)=\mu s^2-25.
\]
Indeed \(q_\mu(s,v)=16v^4+b_\mu(s)v^2-a(s)\), and \(b_\mu>0\) on the interval when \(\mu>400/9\). The only intersections with the axial line are \(s=3/4\) and \(s=1\), and no point of the right or left oval crosses the axial barriers \(s=3/4\) or \(s=1\); the other two ovals arise by exchanging \(u\) and \(v\). By the four-oval classification in the originating work, these are precisely its four components. The explicit positive root gives, uniformly on the closed axial interval,
\[
v_\mu(s)=\mu^{-1/2}\frac{\sqrt{a(s)}}s\bigl(1+O(\mu^{-1})\bigr).
\]
The identity \(a(s)/s^2=25-16s^2-9/s^2\) shows that the rescaled maximal half-thickness tends to \(1\), attained in the limit at \(s=\sqrt3/2\).

The area of each lobe is exactly \(A_\mu=2\int_{3/4}^1v_\mu(s)\,ds\). Hence
\[
\sqrt\mu A_\mu\to2\int_{3/4}^1\frac{\sqrt{a(s)}}s\,ds=\frac\pi8.
\]
The final integral follows from \(t=s^2\) and the elementary semicircular-density identity
\[
\int_\alpha^\beta\frac{\sqrt{(t-\alpha)(\beta-t)}}t\,dt
=\pi\left(\frac{\alpha+\beta}2-\sqrt{\alpha\beta}\right),\quad 0<\alpha<\beta,
\]
with \(\alpha=9/16\), \(\beta=1\). The uniform relative expansion provides the claimed \(O(\mu^{-3/2})\) error.

**2. Exact physical-time quadrature and its two limits.** On \(h=0\), the velocity is \(\varepsilon xy(-h_y,h_x)\). On the upper branch \(v=v_\mu(s)\), define
\[
D_\mu(s)=2v_\mu(s)\bigl(b_\mu(s)+32v_\mu(s)^2\bigr)>0.
\]
This is \(h_y\) on the upper branch. For each axial sign \(\sigma\), the two signed transverse branches contribute the travel-time densities
\[
\frac{dt_\eta}{ds}=
\frac1{\varepsilon(2+\sigma s)(2+\eta v_\mu(s))D_\mu(s)},
\qquad\eta=\pm1.
\]
Adding gives the *exact* period formula
\[
T_{\sigma,\mu}=\frac4\varepsilon\int_{3/4}^1
\frac{ds}{(2+\sigma s)(4-v_\mu(s)^2)D_\mu(s)}.
\]
Since \(D_\mu(s)=2\sqrt\mu\,s\sqrt{a(s)}\,[1+O(\mu^{-1})]\) uniformly relative to its positive interior value, and \(a(s)^{-1/2}\) is integrable at both endpoints, dominated convergence with a uniform relative remainder gives
\[
T_{\sigma,\mu}=\frac1{2\varepsilon\sqrt\mu}
\int_{3/4}^1\frac{ds}{(2+\sigma s)s\sqrt{a(s)}}+O_\varepsilon(\mu^{-3/2}).
\]
The inequality \(J_- >J_+\) follows pointwise. Furthermore,
\[
J_++J_-=4\int_{3/4}^1\frac{ds}{s(4-s^2)\sqrt{a(s)}}
=\frac\pi2\left(\frac13+\frac1{\sqrt{165}}\right),
\]
using \(t=s^2\), partial fractions of \(1/[t(4-t)]\), and
\(\int_\alpha^\beta [(c-t)\sqrt{(t-\alpha)(\beta-t)}]^{-1}dt
=\pi/\sqrt{(c-\alpha)(c-\beta)}\) for \(c>\beta\). Right/top periods are identical by coordinate exchange; left/bottom similarly.

**3. Floquet contraction.** Direct differentiation of the displayed vector field gives
\[
\dot h=-xy\,h\,|\nabla h|^2.
\]
Along a regular oval the tangential physical speed equals \(\varepsilon xy|\nabla h|\). Therefore the transverse multiplier is exactly
\[
\rho_\mu=\exp\left(-\frac{I_\mu}{\varepsilon}\right),
\qquad I_\mu=\oint_{\Gamma_\mu}|\nabla q_\mu|\,d\ell>0.
\]
Quarter-turn/reflection congruence makes \(I_\mu\) equal on all four ovals; the preceding exact formula for the common multiplier was also obtained in the closest published research note. Here we evaluate its new high-coupling behavior. Write
\[
H_\mu(s)=64s^3-50s+2\mu s v_\mu(s)^2.
\]
Using the two graph branches and the relation \(v_\mu'(s)=-H_\mu(s)/D_\mu(s)\) gives the exact identity
\[
I_\mu=2\int_{3/4}^1\left(D_\mu(s)+\frac{H_\mu(s)^2}{D_\mu(s)}\right)ds.
\]
The numerator \(H_\mu\) stays uniformly bounded because \(\mu v_\mu^2\) does, while
\(D_\mu^{-1}=O(\mu^{-1/2}a(s)^{-1/2})\). Consequently the second term contributes \(O(\mu^{-1/2})\). For the first,
\[
I_\mu=4\sqrt\mu\int_{3/4}^1s\sqrt{a(s)}\,ds+O(\mu^{-1/2})
=\frac{49\pi}{256}\sqrt\mu+O(\mu^{-1/2}).
\]
The last integral is the beta integral \(2\int_{9/16}^1\sqrt{(t-9/16)(1-t)}\,dt=49\pi/1024\). Division by the period formula yields \(\chi_{\sigma,\mu}/\mu\to-49\pi/(128J_\sigma)\), independent of \(\varepsilon\).

**4. Time-uniform phase distribution.** At fixed \(s\in(3/4,1)\), the signed transverse coordinate obeys \(\sqrt\mu\,\eta v_\mu(s)\to\eta\sqrt{a(s)}/s\). In each branch the exact physical-time density in step 2 equals
\[
\frac1{4\varepsilon\sqrt\mu}\,
\frac{1+o(1)}{(2+\sigma s)s\sqrt{a(s)}}.
\]
After dividing by the total period, both branches receive limiting weight one-half. The uniform integrable envelope \(C a(s)^{-1/2}\) applies for all sufficiently large \(\mu\), so dominated convergence proves the stated weak limit against every bounded continuous test function. No stronger total-variation convergence to a one-dimensional limiting graph is claimed.

## Verification
The accompanying standard-library program `verify.py` checks the exact quartic-root identity and the cofactor identity at rational points, evaluates the real quadratures by composite midpoint rules after removal of square-root endpoint singularities, checks the exact sum of period constants, and numerically tests the predicted area, period, and multiplier asymptotic constants. It prints `FOUR_OVAL_HIGH_COUPLING_CHECK_OK` if these finite diagnostics succeed. The universal limits and strict inequalities follow from the analytic arguments above rather than finite numerical tests.

## Relationship to prior work
Craciun and Erban, *Planar chemical reaction systems with algebraic and non-algebraic limit cycles*, arXiv:2406.05057 (first public version 2024-06-07), give the precise chemical system, the cofactor, the four-oval geometry, and the existence and stability of the four cycles. These are prior results. The closest published research note, *Two physical-time clocks and one transverse multiplier at a four-oval chemical bifurcation* (public identifier 748c2b58468f, 2026), establishes exact period and multiplier quadratures and evaluates the **opposite** nodal-merger limit \(\mu\downarrow337/9\). Its formulas hold for all \(\mu>337/9\) and are a powerful input, but they do not state or evaluate the high-coupling singular geometry, area, normal scaling, time-occupation law, sharp period constants, or the growing Floquet action. The present results require a separate limiting graph analysis and integrable endpoint estimates. Published general invariant-curve and cofactor methods are acknowledged, not claimed as new.

## Limitations
The results hold for this concrete shifted ninth-degree chemical flow at fixed \(\varepsilon>0\). No uniformity as \(\varepsilon\to0\), no stochastic reaction-network concentration theorem, and no full attraction-basin probability law are claimed. In particular, interior area of the cycles is not a full attraction-basin area. Other equivalent unpublished or unindexed asymptotic evaluations might exist; an exact general quadrature from prior work is acknowledged as the closest implication risk. Independent mathematical audit has not been performed.

## References
1. G. Craciun and R. Erban, *Planar chemical reaction systems with algebraic and non-algebraic limit cycles*, arXiv:2406.05057, version 1 posted 2024-06-07; *Journal of Mathematical Biology* 90, article 64 (2025), Theorem 3, Lemma 13, equations (5.13)–(5.19). https://arxiv.org/abs/2406.05057 ; https://doi.org/10.1007/s00285-025-02221-0 .
2. *Two physical-time clocks and one transverse multiplier at a four-oval chemical bifurcation*, publicly indexed research note (2026), identifier 748c2b58468f, RESULT section, exact polar period quadrature and cofactor Floquet integral. Source title and identifier enable independent retrieval.
3. A. Gasull and H. Giacomini, *Number of limit cycles for planar systems with invariant algebraic curves*, arXiv:2210.15803 (2022); background on invariant algebraic curves. https://arxiv.org/abs/2210.15803 .
