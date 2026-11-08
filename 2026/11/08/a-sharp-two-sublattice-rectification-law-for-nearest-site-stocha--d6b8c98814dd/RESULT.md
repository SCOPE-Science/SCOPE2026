# A sharp two-sublattice rectification law for nearest-site stochastic resetting

## Finding

Let \(a,b,D,r_0,r_1\) be strictly positive and set \(L=a+b\). The resetting sites are
\[\mathcal S=\{nL,nL+a:n\in\mathbb Z\}.\]
A Brownian particle moves with diffusion coefficient \(D\). At each reset it is instantaneously projected onto the closest site of \(\mathcal S\), retaining the physical, unwrapped coordinate. The waiting time to the next reset is exponential of rate \(r_0\) or \(r_1\), according as the **most recent reset site** is of type \(nL\) or \(nL+a\). Each waiting time and each Brownian motion after a reset are freshly sampled independently. This dependence on the previous site is part of the model; the rate does not switch when the diffusing position merely crosses a Voronoi boundary.

Define
\[\kappa_j=\sqrt{r_j/D},\quad p(\kappa)=\frac{\sinh(\kappa a/2)+\sinh(\kappa b/2)}{2\sinh(\kappa L/2)},\quad d(\kappa)=\frac{a\sinh(\kappa b/2)-b\sinh(\kappa a/2)}{2\sinh(\kappa L/2)},\]
\[p_j=p(\kappa_j),\qquad d_j=d(\kappa_j).\]
For a particle initially at any resetting site, the almost-sure physical-time velocity exists and is deterministic:
\[\boxed{\lim_{t\to\infty}\frac{X_t}{t}=v=\frac{p_1d_0-p_0d_1}{p_1/r_0+p_0/r_1}.}\]
Its sign has a sharp, global classification:
\[\boxed{v=0\ \Longleftrightarrow\ a=b\ \text{or}\ r_0=r_1;\qquad \operatorname{sgn}v=\operatorname{sgn}((b-a)(r_0-r_1))\quad\text{otherwise}.}\]
Thus equal rates or equal gaps each prevent rectification, but simultaneous geometric staggering and clock staggering induce a current of fixed, exactly determined direction. No reversal occurs as a common positive factor rescales both reset rates.

For fixed \(c_0,c_1>0\), let \(r_j=tc_j\), \(t>0\). Then
\[\boxed{v(t)=\frac{ab(b-a)c_0c_1(c_0-c_1)}{48D(c_0+c_1)}t^2+O(t^3)\quad(t\downarrow0),\qquad v(t)\to0\quad(t\to\infty).}\]
When \(a\ne b\) and \(c_0\ne c_1\), the nonzero, fixed-sign velocity therefore attains a strictly positive maximum in absolute value at at least one finite common rate scale. No uniqueness of this optimum is asserted.

## Assumptions and scope

The assertion is on the infinite line, with unlimited possible jumps during each Brownian excursion; projection is genuinely to the nearest site among **all** sites. In particular, it is not a nearest-neighbor-only jump approximation. Resets occur at a last-site-type-dependent exponential rate, not at one homogeneous Poisson rate. Both \(r_0,r_1\) are finite and strictly positive. The initial position is any site; the same law of large numbers also holds for a deterministic initial position after specifying an initial site label and performing the first reset. Boundaries of Voronoi cells have probability zero and tie-breaking is immaterial. The velocity is unwrapped displacement per physical time, including diffusive intervals, not displacement per resetting event.

## Proof

**1. Brownian displacement at a reset.** Starting at an even site, let \(T\sim\operatorname{Exp}(r)\) and let \(Z=\sqrt{2D}B_T\), independent of the new reset event. Integrating the Gaussian heat kernel over \(T\) gives the symmetric Laplace density
\[\mathbb P(Z\in dz)=\frac{\kappa}{2}e^{-\kappa|z|}\,dz,\qquad\kappa=\sqrt{r/D}.\]
The nearest-site quantizer \(Q(z)\) is nondecreasing, satisfies \(Q(z+L)=Q(z)+L\), and has upward jumps of size \(a\) at \(nL+a/2\) and of size \(b\) at \(nL+a+b/2\). At the origin \(Q(0)=0\).

**2. The two exact one-step statistics.** Integrating the Laplace density over all Voronoi cells of odd sites and summing the resulting two geometric series yields
\[\mathbb P(Q(Z)\in a+L\mathbb Z)=p(\kappa).\]
For the mean, use the Stieltjes representation of the step quantizer:
\[\mathbb EQ(Z)=\tfrac12\sum_{z_j>0}(\Delta Q)_{z_j}e^{-\kappa z_j}-\tfrac12\sum_{z_j<0}(\Delta Q)_{z_j}e^{\kappa z_j}.\]
Summing the periodic jumps gives
\[\mathbb EQ(Z)=\frac{a(e^{-\kappa a/2}-e^{-\kappa(L-a/2)})-b(e^{-\kappa b/2}-e^{-\kappa(L-b/2)})}{2(1-e^{-\kappa L})}=d(\kappa).\]
The displayed hyperbolic-sine formulas follow from \(1-e^{-\kappa u}=2e^{-\kappa u/2}\sinh(\kappa u/2)\). Reflection about the midpoint \(a/2\) interchanges the two site types, so an excursion starting at an odd site has probability \(p(\kappa)\) to change type and mean physical displacement \(-d(\kappa)\).

**3. Continuous-time law of large numbers.** Record the position and type immediately after reset number \(n\). The type process is the irreducible, aperiodic two-state chain with transition matrix
\[P=\begin{pmatrix}1-p_0&p_0\\p_1&1-p_1\end{pmatrix},\qquad \pi=\left(\frac{p_1}{p_0+p_1},\frac{p_0}{p_0+p_1}\right).\]
The conditional mean increments are \(d_0\) and \(-d_1\), and the conditional mean holding times are \(1/r_0\) and \(1/r_1\). Each increment has an exponential tail because its magnitude is bounded by the Laplace excursion magnitude plus at most \(L\); holding times are exponential. The strong law for finite-state Markov additive rewards (alternatively, martingale differences plus the finite-state ergodic theorem) gives asymptotic mean reward \((p_1d_0-p_0d_1)/(p_0+p_1)\) per event and mean time \((p_1/r_0+p_0/r_1)/(p_0+p_1)\) per event. Taking their ratio proves the claimed speed at reset epochs.

For intermediate physical times, the maximum Brownian displacement within a single exponential holding interval obeys a uniform tail bound \(\mathbb P(\sup_{u\le T}|\sqrt{2D}B_u|>x)\le2e^{-x\min(\kappa_0,\kappa_1)}\), by the Brownian hitting-time Laplace transform and a union bound. Borel–Cantelli makes the residual excursion displacement \(o(n)\) after \(n\) reset events; the number of events grows linearly in time. Hence the same almost-sure speed holds for \(X_t\), not just reset-epoch positions.

**4. Exact sign.** Since \(0<p(\kappa)<1\), the denominator in the velocity formula is positive. Put
\[H(\kappa)=\frac{d(\kappa)}{p(\kappa)}=\frac{aR(\kappa)-b}{1+R(\kappa)},\quad R(\kappa)=\frac{\sinh(\kappa b/2)}{\sinh(\kappa a/2)}.\]
Then \(v=p_0p_1[H(\kappa_0)-H(\kappa_1)]/(p_1/r_0+p_0/r_1)\). The function \(x\mapsto x\coth x\) is strictly increasing for positive \(x\), since \(\sinh x\cosh x>x\). Consequently \(\operatorname{sgn}R'(\kappa)=\operatorname{sgn}(b-a)\), while \(dH/dR=L/(1+R)^2>0\). This proves all sign and zero assertions without numerical or perturbative assumptions.

**5. Rate scaling and the optimum.** Taylor expansion gives
\[p(\kappa)=\tfrac12+O(\kappa^2),\qquad H(\kappa)=\frac{ab(b-a)}{24}\kappa^2+O(\kappa^4).\]
Substituting \(\kappa_j^2=tc_j/D\) gives the displayed small-\(t\) coefficient. Since \(p(\kappa)=O(e^{-\kappa\min(a,b)/2})\) as \(\kappa\to\infty\) and \(|H(\kappa)|\le\max(a,b)\), the velocity magnitude is at most \(2\max(a,b)\min(r_0p_0,r_1p_1)\), which tends to zero as \(t\to\infty\). Continuity and the nonzero constant sign then imply a finite, nonzero maximizer of its absolute value.

## Verification

The standalone file `verify.py` independently sums a finite truncation of every Laplace-weighted Voronoi cell (with a rigorous exponentially small truncation scale), compares the results with \(p\) and \(d\), exercises the sign classification on a parameter grid, checks the small-rate coefficient, and simulates physical Brownian excursions with state-dependent exponential holding times. It passes 128 deterministic assertions in Python 3 with no third-party packages. For example, at \(a=1\), \(b=2\), \(D=1\), \(r_0=4\), \(r_1=1\), the exact formula gives \(v\approx0.0527361159474304\). Monte Carlo is only a finite diagnostic; it is not used to prove a strong law or monotonicity.

## Relationship to prior work

Alston and Bertrand, *Boosting macroscopic diffusion with local resetting* (first posted 2024-01-23), study nearest-site projection with one spatially constant Poisson reset rate and optimize macroscopic diffusivity. Their model does not contain a memory-labeled two-rate clock or the exact directional current criterion here. Ghosh et al., *Autonomous Ratcheting by Stochastic Resetting* (2023), and Liu et al., *Ratcheting by Stochastic Resetting With Fat-Tailed Time Distributions* (2024), instead reset within a spatially asymmetric ratchet potential under one common reset clock. Roberts, Sezik and Lardet (2024) use a finite-time potential-mediated return phase. None has two clocks conditioned on the type of the last projected site. Their broad physical rectification mechanism motivates the question but does not imply the displayed two-sublattice formula. Other general Markov-additive reward theorems supply the law-of-large-numbers technique, not these model-specific values or the sharp sign rule.

## Limitations

The two-rate rule uses the most recently selected resetting-site type, not the instantaneous nearest-site type; replacing that rule changes the generator and is not covered. The result does not give the diffusivity around the drifting mean, the full large-deviation function, entropy production, finite-return-time corrections, or a unique optimal rate. The two-site cell and strictly positive exponential reset rates are essential to the exact formulas. Priority against all unindexed, unpublished, or inaccessible literature has not been independently certified.

## References

1. H. Alston and T. Bertrand, *Boosting macroscopic diffusion with local resetting*, arXiv:2401.12772v1, first posted 2024-01-23. https://arxiv.org/html/2401.12772v1
2. J. Liu, Y. Li, P. K. Ghosh, S. Nayak, F. Marchesoni, *Ratcheting by Stochastic Resetting With Fat-Tailed Time Distributions*, ChemPhysChem 25 (2024), e202400313. https://doi.org/10.1002/cphc.202400313
3. C. Roberts, E. Sezik and E. Lardet, *Ratchet-mediated resetting: Current, efficiency, and exact solution*, arXiv:2405.10698, first posted 2024-05-17. https://arxiv.org/abs/2405.10698
4. P. K. Ghosh, S. Nayak, J. Liu, Y. Li, F. Marchesoni, *Autonomous Ratcheting by Stochastic Resetting*, arXiv:2307.06202, first posted 2023-07-12. https://arxiv.org/abs/2307.06202
