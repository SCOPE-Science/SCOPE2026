# One-sided resetting forces a unique permeability-independent current reversal at a biased membrane

## Finding

A directionally biased membrane on a Brownian ring can carry stationary probability current against its preferred transmission direction when Poisson resetting is sufficiently rapid. **For every fixed source distribution supported strictly inside either open semicircle, the signed membrane current has either exactly one positive-reset-rate reversal or no reversal at all, with a complete criterion determined solely by membrane bias and which semicircle receives resetting.** When the reversal exists, its resetting rate is independent of membrane permeability.

**Theorem.** Fix a ring circumference \(L>0\), diffusivity \(D>0\), permeability \(\kappa>0\), bias \(\beta>0\), and a Borel probability measure \(\mu\) on \((0,L)\), all fixed independently of reset rate \(r>0\). Cut the ring at its membrane to obtain \(0<x<L\). Define

\[
\eta=\sqrt{r/D},\qquad
A(\eta)=\frac{\eta}{\sinh(\eta L)}\int\cosh[\eta(L-y)]\,\mu(dy),\qquad
B(\eta)=\frac{\eta}{\sinh(\eta L)}\int\cosh(\eta y)\,\mu(dy),
\]
\[
g(\eta)=\frac{\tanh(\eta L/2)}{D\eta}.
\]

The unique stationary membrane current, positive when transported from \(L^-\) to \(0^+\), is exactly

\[
\boxed{J(r)=\frac{\kappa[B(\eta)-\beta A(\eta)]}{1+\kappa(1+\beta)g(\eta)}.}
\]

Let \(R(\eta)=B(\eta)/A(\eta)\). The following classification is exhaustive under the one-semicircle support hypothesis.

- **Left-side resetting:** If \(\mu((0,L/2))=1\), then \(R\) decreases strictly from \(1\) to \(0\). For \(0<\beta<1\), exactly one \(r_c>0\) satisfies \(R(\sqrt{r_c/D})=\beta\); \(J(r)>0\) below and \(J(r)<0\) above \(r_c\). If \(\beta\ge1\), then \(J(r)<0\) at every positive reset rate.
- **Right-side resetting:** If \(\mu((L/2,L))=1\), then \(R\) increases strictly from \(1\) to \(+\infty\). For \(\beta>1\), exactly one \(r_c>0\) satisfies \(R(\sqrt{r_c/D})=\beta\); \(J(r)<0\) below and \(J(r)>0\) above \(r_c\). If \(0<\beta\le1\), then \(J(r)>0\) for every positive reset rate.

The reversal is strict and transverse: \(J'(r_c)\ne0\). It occurs at the same \(r_c\) for every \(\kappa>0\).

**Explicit uniform-semiring case.** For reset positions uniform on \((0,L/2)\),

\[
R(\eta)=\frac{1}{2\cosh(\eta L/2)-1},\qquad
\boxed{r_c=\frac{4D}{L^2}\operatorname{arcosh}^2\!\left(\frac{1+\beta^{-1}}{2}\right)}\quad(0<\beta<1).
\]

For uniform resetting on \((L/2,L)\), the corresponding threshold is

\[
\boxed{r_c=\frac{4D}{L^2}\operatorname{arcosh}^2\!\left(\frac{1+\beta}{2}\right)}\quad(\beta>1).
\]

For example, with \(D=L=1\), uniform left-half resetting, and \(\beta=1/2\), the unique critical reset rate is \(r_c\approx3.7050371292\) for **every** positive permeability. The direction of the stationary membrane flux reverses at this exact rate.

## Assumptions and scope

The Brownian generator is \(D\partial_{xx}\) in the open interval. Independent Poisson resets at rate \(r\) relocate the particle to a fresh sample from \(\mu\), possibly across the membrane; reset events are not themselves counted as physical diffusive crossings. The membrane has the *directed linear transmission law*

\[
Dp_r''-rp_r=-r\mu\quad\text{in }(0,L),\qquad
-Dp_r'(0^+)=-Dp_r'(L^-)=J(r),
\]
\[
\boxed{J(r)=\kappa[p_r(L^-)-\beta p_r(0^+)].}
\]

These equations are interpreted distributionally when \(\mu\) has atoms. The stationary density integrates to one and may jump across the cut. The factor \(\beta\) encodes a directional transmission preference (an interfacial chemical-potential discontinuity); \(\beta=1\) is the symmetric membrane. The sign is defined by the displayed boundary law, not by whether a jump at a reset event winds around the ring. Throughout the theorem, \(D,L,\kappa,\beta,\mu\) are independent of \(r\); the support condition is strict, but the support need not have a positive distance from the midpoint. No assumptions of a smooth source density or a finite atomic support are made.

The theorem does not classify reset distributions placing positive mass on both semicircles, rate-dependent sources, heterogeneous diffusivity, or nonlinear/transient membrane laws.

## Proof

**1. The stationary Neumann resolvent and flux corrector.** Write \(\eta=\sqrt{r/D}\). The reflecting-boundary resolvent with normalized reset source is

\[
p_N(x)=\frac{\eta}{\sinh(\eta L)}\int_{(0,L)}\cosh[\eta\min(x,y)]\cosh\bigl(\eta[L-\max(x,y)]\bigr)\,\mu(dy).
\]

It solves \(Dp_N''-rp_N=-r\mu\), has \(p_N'(0)=p_N'(L)=0\), and integrates to one. Its endpoint values are \(p_N(0)=A\) and \(p_N(L)=B\). Given any common signed boundary flux \(J\), every solution is necessarily

\[
p_J(x)=p_N(x)-\frac{J}{D\eta}\,\frac{\sinh[\eta(x-L/2)]}{\cosh(\eta L/2)}.
\]

The correction solves the homogeneous differential equation, has zero integral and gives \(-Dp_J'(0)=-Dp_J'(L)=J\). Consequently

\[
p_J(0)=A+gJ,\qquad p_J(L)=B-gJ.
\]

The directed transmission condition gives \(J=\kappa[(B-gJ)-\beta(A+gJ)]\), which proves the displayed formula for \(J\). The denominator is strictly positive. Direct substitution also gives

\[
p_r(0)=\frac{A+\kappa g(A+B)}{1+\kappa g(1+\beta)}>0,
\qquad
p_r(L)=\frac{B+\beta\kappa g(A+B)}{1+\kappa g(1+\beta)}>0.
\]

The one-dimensional elliptic maximum principle, applied between atoms and across the source's nonnegative distributional forcing, proves nonnegativity in the interior; strict positivity follows from the positive endpoint values and the positive Green kernel. The positive reset rate supplies uniqueness of the stationary law. Thus no unphysical signed solution is being used in the flux formula.

**2. Strict monotonicity for every one-sided source.** The shared factor \(\eta/\sinh(\eta L)\) cancels in \(R=B/A\). Put \(m=L/2\) and suppose \(\mu((0,m))=1\). Differentiation under the integrals is legitimate because the integrands and their derivatives are bounded uniformly for \(y\in(0,L)\) at any fixed \(\eta>0\). We obtain

\[
\frac{d}{d\eta}\log R
=\frac{\int y\sinh(\eta y)\,\mu(dy)}{\int\cosh(\eta y)\,\mu(dy)}
-\frac{\int(L-y)\sinh[\eta(L-y)]\,\mu(dy)}{\int\cosh[\eta(L-y)]\,\mu(dy)}.
\]

The scalar function \(z\mapsto z\tanh(\eta z)\) is strictly increasing for \(z>0\). Because every sampled \(y\) satisfies \(y<m<L-y\), its weighted averages obey the strict sandwich

\[
\frac{\int y\sinh(\eta y)\,d\mu}{\int\cosh(\eta y)\,d\mu}
<m\tanh(\eta m)
<\frac{\int(L-y)\sinh[\eta(L-y)]\,d\mu}{\int\cosh[\eta(L-y)]\,d\mu}.
\]

Hence \(R'(\eta)<0\) at every positive \(\eta\). By bounded convergence \(R(\eta)\to1\) as \(\eta\downarrow0\). To determine the other endpoint without requiring uniform separation from \(m\), choose \(\varepsilon>0\) such that \(c=\mu((0,m-\varepsilon])>0\). Then the numerator of the unnormalized ratio is at most \(\cosh(\eta m)\), while its denominator is at least \(c\cosh[\eta(m+\varepsilon)]\). Therefore \(R(\eta)\to0\) as \(\eta\to\infty\).

If instead \(\mu((m,L))=1\), reflection \(y\mapsto L-y\) interchanges \(A\) and \(B\); the right-side \(R\) is the reciprocal of a strictly decreasing ratio. Thus it increases strictly from \(1\) to \(+\infty\).

**3. Complete current-sign classification.** Since \(A>0\), \(\kappa>0\), and the exact denominator is positive,

\[
\operatorname{sgn}J(r)=\operatorname{sgn}[R(\sqrt{r/D})-\beta].
\]

Strict monotonicity and the two endpoint ranges prove every asserted phase, including existence, uniqueness, and absence of roots in the complementary bias ranges. At a crossing \(\eta_c\), differentiating the exact current gives

\[
J'(r_c)=\frac{\kappa A(\eta_c)R'(\eta_c)}{1+\kappa(1+\beta)g(\eta_c)}\,\frac{1}{2D\eta_c},
\]

which is nonzero, with the appropriate opposite signs for left and right sources. The root condition \(R=\beta\) contains no permeability, proving exact permeability-independent crossover.

**4. Uniform sources and a weak-bias law.** If \(\mu\) is uniform on \((0,m)\), elementary integration yields

\[
\frac{B}{A}=\frac{\sinh(\eta m)}{\sinh(2\eta m)-\sinh(\eta m)}
=\frac{1}{2\cosh(\eta m)-1}.
\]

Inversion produces the stated explicit critical rates. Reflection gives the right-half result. More generally, expanding both hyperbolic cosines at \(\eta=0\) gives, for any left-half source,

\[
R(\eta)=1-\frac{\eta^2 L[L-2\mathbb E_\mu Y]}{2}+O(\eta^4).
\]

Because \(0<\mathbb E_\mu Y<L/2\), the critical rate near weak directional bias satisfies

\[
\boxed{r_c\sim\frac{2D(1-\beta)}{L[L-2\mathbb E_\mu Y]}}
\quad\text{as }\beta\uparrow1\text{ with }\beta<1.
\]

The analogous right-half weak-bias law follows by reflection, with \(\beta-1\) replacing \(1-\beta\) and the mean distance measured from the right endpoint. This asymptotic is a consequence of the same single-root classification, not an independent claim.

## Verification

`verify_biased_membrane.py` is a standalone Python 3 checker requiring NumPy and SciPy. In an actual execution it reported **877 passed diagnostic checks**. Its tests include multiple atomic and mixed one-sided reset distributions, root/bracketing and sign checks on both sides, direct verification of the biased boundary law, quadrature checks of the uniform-half formulas, and an independent finite-volume discretization of the stationary elliptic problem at three successively refined mesh widths and five parameter configurations. The finite-volume computation includes the half-cell membrane resistance and its bias dependence. The exact uniqueness and transversality conclusions follow from the inequalities in the proof, **not** from finite simulations or incomplete sampling.

To reproduce: run `python verify_biased_membrane.py` in an environment with NumPy and SciPy. No external data are required.

## Relationship to prior work

Bressloff (2024) derives the membrane entropy-production framework, demonstrates asymmetric permeation as a chemical-potential jump, and separately solves stationary diffusion with resetting on a **symmetric** permeable circle, including nonmonotone interfacial entropy production. The directional boundary condition and the unbiased resetting resolvent are therefore **antecedents**, not new claims. Bressloff (2022/2023) develops renewal equations for **biased** semipermeable interfaces and computes asymmetric first-passage quantities in an interval, but does not establish a reset-rate-induced stationary current reversal on a biased circle.

Previously available exact results for symmetric-membrane resetting provide stationary membrane currents and their inverse-source identification, as well as permeability optimizers. Their symmetric interface corresponds to \(\beta=1\), for which a strictly one-sided reset law gives a fixed-sign flux at every reset rate, so these statements do not imply the present bias-driven phase diagram. A reported reset-rate reversal in an asymmetric periodic-potential ratchet uses a different drift mechanism and does not cover a membrane with directed transmission. The distinct result here is the strict one-reversal/no-reversal classification for **every Borel source confined to a semicircle**, the analytically exact bias criterion and permeability-independent threshold, with a closed-form uniform-source example. The derivation reduces existing Green and boundary techniques, so latent implicit coverage by a broader boundary-control theorem remains a publication-priority risk.

## Limitations

The theorem is restricted to one-dimensional homogeneous diffusion on a single-ring cut, linear Markovian directional membrane transmission, Poisson resetting to a fixed one-sided source, and the **continuous diffusive membrane flux** rather than the total oriented displacement including reset jumps. If a source overlaps both halves, monotonicity of \(R\) is not asserted; no universal reversal count is claimed in that regime. Bias and permeability must be fixed while reset rate varies. This is a population-level stationary assertion and does not supply finite-sample detection guarantees. Independent scientific validation and publication-priority certification have not been performed.

## References

1. P. C. Bressloff, *Entropy production for diffusion processes across a semipermeable interface*, arXiv:2402.16403v1, first public 2024-02-26, https://arxiv.org/abs/2402.16403 ; *Physical Review Research* **6**, 023283 (2024), DOI 10.1103/PhysRevResearch.6.023283. Relevant: directional bias in Section II and stochastic resetting on a symmetric permeable circle in Section III, especially stationary Green identities.
2. P. C. Bressloff, *Renewal equations for single-particle diffusion through a semipermeable interface*, arXiv:2211.12460v1, public 2022-11-22, https://arxiv.org/abs/2211.12460 ; *Physical Review E* **107**, 014110 (2023). Relevant: Section II, biased interface and asymmetric first passage.
3. P. C. Bressloff, *Diffusion with stochastic resetting screened by a semipermeable interface*, arXiv:2211.12468v1, public 2022-11-22, https://arxiv.org/abs/2211.12468 ; *Journal of Physics A* **56**, 105001 (2023). Relevant: resetting screened by an interface and capture objectives.
4. G. Tucci, A. Gambassi, S. Gupta and É. Roldán, *Controlling particle currents with evaporation and resetting from an interval*, *Physical Review Research* **2**, 043138 (2020), DOI 10.1103/PhysRevResearch.2.043138. Related resetting-induced currents without the directed membrane theorem.
