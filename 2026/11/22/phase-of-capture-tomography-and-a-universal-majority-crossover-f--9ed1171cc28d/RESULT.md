# Phase-of-capture tomography and a universal majority crossover for Brownian search with stochastic home returns

## Finding

An absorption-phase label alone, measured as the Poisson interruption rate varies, uniquely determines the complete return-phase target-versus-home splitting function of a one-dimensional Brownian search-and-return process. For a diffusion with known return diffusivity, this determines its entire inward return drift on the interval between home and the target. Every nondegenerate return protocol has **exactly one** interruption rate at which half of all successful trajectories finish in the return phase. Nonetheless, **any finite number** of exact phase-fraction observations can be reproduced by two distinct smooth, strictly homeward return forces.

More precisely, take a target at \(L>0\), free Brownian search with generator \(D\partial_{xx}\), \(D>0\), starting at the home position \(0\), and an independent exponential search interruption of rate \(r>0\). If interruption precedes first target hitting, the current position is retained and a fixed, rate-independent stochastic return dynamics starts. Return ends upon first hitting either \(0\) or \(L\); hitting \(L\) terminates the entire search, and hitting \(0\) initiates a fresh independent Brownian search. From negative interruption positions the return is assumed to hit \(0\) almost surely without reaching \(L\). Define the splitting profile
\[
h(x)=\Pr_x\{\text{return reaches }L\text{ before }0\},\quad x\in[0,L].
\]
Assume \(h\) is continuous, \(h(0)=0\), \(h(L)=1\), and \(0<h(x)<1\) in the open interval. For \(z=L\sqrt{r/D}\) and \(F(r)=\Pr\{\text{the eventual target detection occurs in the return phase}\}\), the exact odds are
\[
\boxed{\frac{F(r)}{1-F(r)}=\mathcal B_h(z),\qquad
\mathcal B_h(z)=z\int_0^1\sinh(z(1-y))h(Ly)\,dy.}\tag{1}
\]
The function \(F\) is strictly increasing from zero to one, so the equation \(F(r)=1/2\) has exactly one finite positive solution. The entire exact curve \(F(r)\), or its values on any infinite set of rates having an accumulation point in \([0,\infty)\), uniquely determines \(h\). In particular, a sequence of arbitrarily weak but exact positive-rate measurements tending to zero suffices in principle.

For a regular return diffusion on \((0,L)\) with generator \(D\partial_{xx}+b(x)\partial_x\), where \(D\) is known, \(b\) continuous, and the usual regular absorbing-endpoint boundary problem applies, the recovered \(h\) is twice continuously differentiable in the interior, has \(h'(x)>0\), and identifies the drift exactly by
\[
\boxed{b(x)=-D\frac{h''(x)}{h'(x)},\qquad 0<x<L.}\tag{2}
\]
This does not reconstruct the motion on the negative half-line, the clock or duration distributions of return, or a separate unknown return diffusivity.

The particularly transparent Brownian-return example \(b\equiv0\) has \(h(x)=x/L\) and therefore
\[
\boxed{F(r)=1-\frac{z}{\sinh z}.}\tag{3}
\]
For this neutral return, the complete search time has **infinite mean for every positive** \(r\): with positive probability an interrupted search begins an unbiased return from a negative position, and its first hitting time of home has infinite expectation. Nevertheless, the eventual capture phase is almost surely well defined and has the exact finite odds in (3). Here the unique majority threshold obeys \(\sinh z_*=2z_*\), with \(z_*=2.177318984965306\ldots\) and \(r_*L^2/D=4.740717962290353\ldots\). For a constant homeward drift \(b=-\mu\), \(\mu>0\), the profile \(h(x)=(e^{\mu x/D}-1)/(e^{\mu L/D}-1)\) makes the majority threshold strictly increase with \(\mu\).

## Assumptions and scope

All phases have continuous trajectories. The free-search process lives on \(( -\infty,L)\), starts at \(0\) after every completed home return, and is killed upon hitting \(L\). Interruptions occur only during free search, not during return. There is no simultaneous interruption and absorption with positive probability. Each new search excursion and clock are independent of the past, and the return dynamics depend on its initial position but not on the interruption rate or the earlier history. Return times are finite almost surely; their moments need not be assumed finite for the phase-label identities. Every finite \(r>0\) has a positive per-cycle probability of direct success, guaranteeing almost-sure eventual target detection. The return profile has the stated interior strict positivity, as for any regular elliptic return diffusion on \([0,L]\). The negative-side return needs only the assumed almost-sure home hitting, not a particular force law. The observables are ideal ensemble phase fractions, not single realizations or estimated finite-sample proportions.

The strong finite-observation nonuniqueness assertion concerns a class of smooth return drifts **strictly negative on the open interval** \((0,L)\), with the same positive known diffusivity and a fixed admissible return motion from negative positions. It does not assert that two physically different return models have identical full phase-response curves.

## Proof

**1. Killed Brownian excursion and one-attempt successes.** Let \(T_L\) be the free Brownian hitting time of \(L\), and let \(R\) be the independent exponential interruption clock. The standard hitting-time Laplace transform gives the probability of direct search-phase capture in one attempt:
\[
a(r)=\Pr(T_L<R)=\mathbb E e^{-rT_L}=e^{-z}.
\]
For an interrupted search, its unnormalized positional distribution is \(rG_r(0,x)\,dx\), with \(G_r\) the resolvent of Brownian motion killed at \(L\). Reflection at the absorbing target gives, for \(0<x<L\),
\[
G_r(0,x)=\frac{e^{-kx}-e^{-k(2L-x)}}{2Dk}
=\frac{e^{-kL}\sinh(k(L-x))}{Dk},\qquad k=\sqrt{r/D}.
\]
Thus the probability of a return-phase target capture in that attempt equals
\[
q(r)=\int_0^LrG_r(0,x)h(x)\,dx
=e^{-z}\,z\int_0^1\sinh(z(1-y))h(Ly)\,dy
=e^{-z}\mathcal B_h(z).
\]
The remaining per-cycle probability \(1-a(r)-q(r)\) corresponds to an interrupted trajectory that returns home; it regenerates exactly. The mutually exclusive terminal-event geometric renewal equation yields eventual direct and return capture probabilities \(a/(a+q)\) and \(q/(a+q)\), respectively. Their odds prove (1). Time spent in return does not enter this phase-label identity.

**2. Strict unique majority transition and protocol ordering.** For every interior \(y\in(0,1)\), \(z\mapsto z\sinh(z(1-y))\) increases strictly on \((0,\infty)\), and \(h(Ly)>0\). Dominated convergence near zero gives \(\mathcal B_h(z)\to0\). On a compact interior subinterval where \(h\) is bounded below by a positive number, \(\mathcal B_h(z)\) grows at least as a positive constant times \(z\sinh(\delta z)\), hence tends to infinity. Thus the odds increase continuously and strictly from zero to infinity, establishing the unique root \(\mathcal B_h(z)=1\) and the asserted limits. If one return model has pointwise smaller splitting profile than another, with strict inequality on a set of positive length, it has strictly smaller \(F(r)\) at each fixed rate and a strictly larger majority threshold.

**3. Entire-function inverse and Hausdorff moments.** Put \(H(y)=h(Ly)\). Compact support and boundedness imply that \(\mathcal B_h(z)/z\), extended at \(z=0\), is an *entire* function of the complex variable \(z\). Its derivatives at zero determine
\[
M_n=\left.\frac{d^{2n+1}}{dz^{2n+1}}\left(\frac{\mathcal B_h(z)}{z}\right)\right|_{z=0}
=\int_0^1(1-y)^{2n+1}H(y)\,dy,\qquad n=0,1,\ldots.
\]
With \(u=(1-y)^2\), this becomes
\[
2M_n=\int_0^1u^n H(1-\sqrt u)\,du.\tag{4}
\]
Equality of all such moments for two bounded profiles forces the difference of their transformed profiles to vanish almost everywhere, because polynomials are dense in continuous functions on the compact interval and finite signed measures are uniquely determined by their polynomial moments. Continuity then gives equality of \(h\) at every point. The identity theorem for entire functions shows that agreement on any set of positive \(z\)'s accumulating at any finite nonnegative \(z\), including zero, already forces equality of all the moments. Since \(r\mapsto z\) is one-to-one on the positive real axis, this proves the exact-data injectivity claim.

**4. Return-force reconstruction.** For a regular return diffusion with fixed known \(D>0\), its splitting function is the unique solution of
\[
D h''(x)+b(x)h'(x)=0,\qquad h(0)=0,\quad h(L)=1.
\]
For any interior reference point \(x_0\), the derivative is \(h'(x_0)\exp[-\int_{x_0}^x b(t)/D\,dt]\). The exponential is positive throughout the interior, so the distinct boundary values and continuity force \(h'(x_0)>0\). Rearranging the differential equation proves (2). This recovers the drift on the observed interval, but not other return information.

**5. Why finitely many rate readings cannot identify even inward forces.** Fix any distinct positive rates \(r_1,\ldots,r_m\), with corresponding \(z_1,\ldots,z_m\). Use as a baseline an inward constant drift \(b=-\mu\), \(\mu>0\), giving a smooth splitting function \(H_0(y)=(e^{cy}-1)/(e^c-1)\), with \(c=\mu L/D>0\). Consider the \(m+1\)-dimensional polynomial space
\[
\mathcal P=\{\,y(1-y)\sum_{j=0}^{m}a_jy^j:a_j\in\mathbb R\,\}.
\]
Each experimental reading imposes one homogeneous linear condition \(z_i\int_0^1\sinh(z_i(1-y))P(y)dy=0\) on \(P\in\mathcal P\), so there is a nonzero polynomial \(P\) satisfying all \(m\) conditions. For sufficiently small \(\varepsilon>0\), the distinct functions \(H_{\pm}=H_0\pm\varepsilon P\) have the same endpoint values, strictly positive first derivatives and strictly positive second derivatives throughout the closed interval. Their drifts \(b_{\pm}(Ly)=-(D/L)H_{\pm}''(y)/H_{\pm}'(y)\) are therefore smooth and strictly negative for \(0<y<1\). The two drifts are genuinely different: equal logarithmic derivatives would make the profiles proportional, and their endpoint normalization would then make them equal, contradicting \(P\ne0\). Their response odds agree at all the prescribed \(m\) rates, so the phase fractions also agree. This proves exact finite-data nonidentifiability within the strictly inward-force subclass.

**6. Explicit calibration, infinite-mean completion, and homeward-force ordering.** For neutral diffusive return \(H(y)=y\), direct integration gives \(\mathcal B_h(z)=\sinh(z)/z-1\); substituting in (1) gives (3). The function \(\sinh(z)/z\) is strictly increasing for \(z>0\), because \(z\cosh z-\sinh z\) vanishes at zero and has derivative \(z\sinh z>0\). Its value rises from one to infinity, so \(\sinh z=2z\) has one positive root. For neutral return, the interrupted-position density has positive mass on \((-\infty,0)\); from each fixed \(x<0\), unbiased Brownian first hitting of home has tail proportional to \(t^{-1/2}\), hence infinite mean. Conditioning on a negative-position interruption and applying Tonelli gives infinite expected total completion time at each \(r>0\), despite almost-sure eventual capture. For constant homeward drift \(-\mu\), the normalized splitting profile is the cumulative distribution function on \([0,1]\) of a density proportional to \(e^{cy}\). Increasing \(c\) moves that distribution strictly to the right in monotone likelihood-ratio order; its CDF \(H_c(y)\) strictly decreases for every \(0<y<1\). Step 2 then gives strict upward movement of the majority-reset threshold with increasing homeward force.

## Verification

The included `checker.py` uses only the Python standard library and runs with `python checker.py`. It independently evaluates the killed Brownian resolvent and the normalized odds integral, tests the neutral closed form at multiple rates, the unique numerical majority threshold, monotonicity and return-force ordering for several constant drifts, the analytic moment coefficients, and a three-rate nonzero polynomial null direction. It further samples 54,000 complete searches via exponential interruption clocks and the exact Brownian-bridge reflection probability, verifying the proportion of detections in each phase against (1). Its recorded run passed 57 finite diagnostics. The stochastic numerical tests corroborate the calculations but cannot establish the infinite-dimensional identifiability or global monotonicity; those follow from Steps 1–6.

## Relationship to prior work

The renewal structure, target accessibility during stochastic return, and the Green-function/splitting-probability inputs are established in Biswas, Kundu and Pal (2023, published 2024); these forward ingredients are not claimed as new. Biswas, Dubey, Kundu and Pal (2024, published 2025) study a drift-diffusive search with a linear homeward return potential and characterize mean completion times and speedups. Dubey and Pal (2026) analyze harmonic search-and-return dynamics with target detection during returns, emphasizing mean completion times and experimental comparisons. The new claim is the general **phase-label response transform, its all-rate identifiability of the return splitting function/force, the universal exactly-one majority crossover, and the finite-readout nonidentifiability boundary**; it does not claim discovery of stochastic returns or their basic renewal formula.

Related inverse-response results for *instantaneous* resetting concern recovering random reset-location distributions from first-passage *mean times* with movable targets; their unknown object and observation channel differ. Classical Hausdorff-moment and one-dimensional scale-function uniqueness supply proof ingredients, not a prior statement of this stochastic-return phase-label theorem. The new theorem would be covered if a published earlier result already identified an arbitrary return splitting profile from the full phase-of-absorption rate scan; such equivalence is a residual publication-priority risk.

## Limitations

The primary inverse result uses exact ensemble measurements at infinitely many reset rates, not a stable estimator from noisy finite data. Finite-rate nonuniqueness is proved, even for smooth strictly inward forces. Reconstructing return drift requires the return diffusivity to be known and the return dynamics to be a regular one-dimensional diffusion; otherwise only the splitting profile is identified. Return-time distributions, negative-side dynamics, hidden phases, and return diffusivity are not identified. The majority transition assumes a rate-independent, nondegenerate positive splitting profile; protocols entirely blind to the target during return have \(F\equiv0\) and are excluded. The paper is not an experimental demonstration, and independent scholarly verification has not been performed.

## References

1. A. Dubey and A. Pal, *Towards synergy between theory and experiments: First-passage processes under resetting with stochastic return protocols*, arXiv:2610.18814, first public 2026-10-13, https://arxiv.org/abs/2610.18814 .
2. A. Biswas, A. Kundu and A. Pal, *Search with stochastic home-returns can expedite classical first passage under resetting*, arXiv:2307.16294, first public 2023-07-30; Phys. Rev. E 110, L042101 (2024), https://arxiv.org/abs/2307.16294 .
3. A. Biswas, A. Dubey, A. Kundu and A. Pal, *Drift-diffusive resetting search process with stochastic returns: speed-up beyond optimal instantaneous return*, arXiv:2406.08975, first public 2024-06-13; Phys. Rev. E 111, 014142 (2025), https://arxiv.org/abs/2406.08975 .
4. Classical uniqueness of the Hausdorff moment problem on a compact interval and the one-dimensional diffusion scale-function/splitting boundary equation are standard mathematical ingredients, not claimed as new.
