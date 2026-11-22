# Exactly two pulse-frequency reversals in buffered Monod competition

## Finding

A fixed mean nutrient-supply flux need not induce a monotone competitive advantage as the interval between nutrient pulses increases. In the specific, completely defined two-type system below there are **exactly two**, and no other, reversals. Let \(T>0\) be the dimensionless interval between nutrient pulses. There exist precisely two positive constants
\[
T_-=3.206466658932142681\ldots,
\qquad T_+=7.730490160339883978\ldots
\]
with \(T_-<T_+\), such that type 2 excludes type 1 for \(0<T<T_-\) or \(T>T_+\), while type 1 excludes type 2 for \(T_-<T<T_+\), whenever both types start at strictly positive abundances. The constants are the two positive zeros of the explicit exponential polynomial
\[
F(T)=(8-T)e^{2T}-(16+10T^2)e^T+8+T.
\]
At each equality the two species have equal per-period uncrowded growth; strict exclusion is asserted only away from those equalities. Here “excludes” means that the losing species' abundance tends to zero while the total population remains bounded away from zero, under the stated common-density competition equation. The result is not a coexistence claim for a nutrient-consumption chemostat.

## Assumptions and scope

The time unit is one substrate decay time. The resource is **externally buffered**: for each fixed \(T>0\), exactly \(10T\) units of nutrient are added instantaneously at times \(kT\), \(k\in\mathbb Z\), and between pulses its concentration obeys \(\dot R=-R\). Organism uptake does not enter this externally imposed resource mass balance; thus this is not a conventional substrate-limited chemostat. The unique strictly positive periodic resource trajectory, measured from just after a pulse, is
\[
R(t)=H(T)e^{-t}\quad(0\le t<T),\qquad
H(T)=\frac{10T}{1-e^{-T}},\qquad
L(T)=\frac{10T}{e^T-1},
\]
where \(L(T)\) is its value just before the next pulse. Its mean concentration is \(T^{-1}\int_0^T R(t)\,dt=10\) at every period: pulse frequency varies while the average nutrient concentration and average nutrient input rate are fixed.

Two positive biomasses \(X_1,X_2\) compete according to
\[
\dot X_i=X_i\left(\mu_i(R(t))-[X_1+X_2]\right),\qquad
\mu_1(r)=\frac{r}{1+r},\qquad
\mu_2(r)=\frac{2r}{10+r},\qquad i=1,2.
\]
All initial biomasses are strictly positive; all coefficients are dimensionless. Both types have the same density-dependent mortality coefficient. No claim is made about endogenous nutrient consumption, lag phases, evolution, or stochastic forcing.

## Proof

**1. Exact period growth difference.** Integration under exponential resource decay yields
\[
\bar\mu_1(T)=\frac1T\log\frac{1+H}{1+L},\qquad
\bar\mu_2(T)=\frac2T\log\frac{10+H}{10+L}.
\]
Indeed, changing variables from time to \(r=R(t)\) turns \(\int\mu_1(R(t))dt\) into \(\int_L^H dr/(1+r)\), and likewise for \(\mu_2\). Let \(\Delta(T)=\bar\mu_1(T)-\bar\mu_2(T)\). Positivity and monotonicity of the logarithm show that the sign of \(\Delta\) is the sign of
\[
(1+H)(10+L)^2-(1+L)(10+H)^2
=(H-L)\left(80-HL-H-L\right).
\]
Here \(H-L=10T>0\). On putting \(E=e^T\), direct substitution gives
\[
80-HL-H-L=\frac{10F(T)}{(E-1)^2}.
\]
Consequently \(\operatorname{sgn}\Delta(T)=\operatorname{sgn}F(T)\) for every \(T>0\).

**2. Exactly two positive zeros.** The Taylor expansion at zero is the everywhere convergent series \(F(T)=\sum_{n=2}^{\infty}c_nT^n\), where
\[
c_n=\frac{2^{n-1}(16-n)-10n(n-1)-16}{n!}.
\]
The numerator is negative for \(n=2,3,4,5\); positive for each integer \(6\le n\le15\) (the exact numerators are \(4,140,448,1056,2156,4004,6856,10712,14548,14268\)); and negative for every \(n\ge16\), directly from the displayed formula. Define \(G(T)=F(T)/T^6\). Then
\[
J(T):=T^7G'(T)=TF'(T)-6F(T)
 =\sum_{n=2}^{\infty}(n-6)c_nT^n.
\]
All nonzero coefficients of \(J\) in degrees below 16 are **positive** (those in degrees 2--5 and 7--15), and all coefficients from degree 16 onward are **negative**. Hence \(J(T)/T^{16}\) is strictly decreasing on \(T>0\): each positive coefficient below degree 16 yields a strictly decreasing negative-power term and each negative coefficient at or above degree 16 yields a nonincreasing term. Termwise differentiation is justified by entire-series convergence on compact subsets of \((0,\infty)\).

As \(T\downarrow0\), \(F(T)=-4T^2+O(T^3)\), so \(J(T)/T^{16}\to+\infty\). As \(T\to\infty\), \(F(T)\sim-Te^{2T}\) and \(J(T)\sim-2T^2e^{2T}\), giving \(J(T)/T^{16}\to-\infty\). It follows that \(J\), hence \(G'\), has exactly one zero; \(G\) first strictly increases, then strictly decreases. Moreover \(G(T)\to-\infty\) at both ends. Yet
\[
F(5)=3e^{10}-266e^5+13>0,
\]
because \(e^5>100\), which follows from the first seven nonnegative Taylor terms of \(e^5\). Therefore \(G\) crosses zero **exactly twice**, once on either side of 5. The asserted strict sign pattern follows. The two numerical roots above are decimal approximations, not ingredients of the infinite-root proof.

**3. Competitive consequence.** For positive biomass trajectories,
\[
\frac d{dt}\log\frac{X_1}{X_2}=\mu_1(R(t))-\mu_2(R(t)).
\]
After \(n\) complete periods, the relative log abundance has changed by exactly \(nT\Delta(T)\). The ratio therefore converges exponentially to zero or infinity according to the sign of \(\Delta(T)\), with bounded within-period modulation. Let \(N=X_1+X_2\). At fixed \(T>0\), the periodic resource lies in a compact strictly positive interval, so there is \(a_T>0\) with \(a_T\le \mu_i(R(t))\le2\). Thus
\[
N(a_T-N)\le\dot N\le N(2-N).
\]
Scalar logistic comparison shows that \(N\) is ultimately bounded above and bounded away from zero. The vanishing ratio consequently forces the losing biomass to zero while the winner persists. At \(T=T_\pm\), the period ratio returns to its starting value; no exclusion statement is asserted there.

**4. Stability under small parameter changes.** At \(T=1,5,20\), the exact \(\Delta\) has respective signs negative, positive, negative (as verified from the closed form). Because period-averaged Monod growth depends continuously on positive rate, affinity, pulse-size, and decay parameters, the existence of **at least two** reversals persists under sufficiently small changes of these parameters. This neighborhood argument does *not* establish exactly two reversals for arbitrary perturbed parameters.

## Verification

The accompanying standalone `verify.py` checks the exact algebraic factorization and the exponential reduction symbolically, evaluates the coefficient signs using integer arithmetic, brackets both zeros at 75-digit precision, and compares closed-form signs over 400 positive periods. Its finite checks support the displayed identities and approximations; the coefficient-sign and monotonicity argument above is the proof of global zero uniqueness. Execute `python verify.py` with Python, SymPy and mpmath installed.

## Relationship to prior work

Letten and Ludington (2023) motivate studying how pulsed versus continuous nutrient supply changes microbial community composition. Their simulations involve resource competition and resource dynamics, not this externally buffered, single-resource, exactly solvable Monod pair. Wortel (2023) develops invasion fitness under serial transfers with nutrient consumption and evolutionary trade-offs, a different comparison and resource law. General Monod growth, exponential resource decay and logarithmic relative-growth identities are established tools, not claimed inventions. The precise twice-reversing classification here is for the stated parameter choice and does not follow merely from the sign change of the instantaneous growth advantage at \(R=8\).

## Limitations

The fixed nutrient waveform is imposed externally and ignores depletion by biomass. Both types share exactly the same density regulation; the equalities at \(T_\pm\) are neutral, not asymptotically stable coexistence. The numerical values \(1,2,10\) are illustrative dimensionless rate and affinity parameters, not fitted measurements. A more general theorem for arbitrary Monod pairs, experimentally measured communities, and transient nonperiodic forcing is not established. Although the cited primary sources and relevant research records were compared, this is a best-knowledge originality assessment rather than exhaustive historical priority certification.

## References

1. Letten, A. D. and Ludington, W. B. (2023). *Pulsed, continuous or somewhere in between? Resource dynamics matter in the optimisation of microbial communities.* ISME Journal 17, 641–644. First public date 2023-01-24. https://doi.org/10.1038/s41396-023-01369-1
2. Wortel, M. T. (2023). *Evolutionary coexistence in a fluctuating environment by specialization on resource level.* Journal of Evolutionary Biology 36, 622–631. First public date 2023-02-17. https://doi.org/10.1111/jeb.14158
3. Carrero-Colón, M., Nakatsu, C. H., and Konopka, A. (2006). *Effect of Nutrient Periodicity on Microbial Community Dynamics.* Applied and Environmental Microbiology 72, 3175–3183. https://doi.org/10.1128/AEM.72.5.3175-3183.2006
4. Smith, H. L. (2011). *Bacterial competition in serial transfer culture.* Mathematical Biosciences. https://doi.org/10.1016/j.mbs.2010.12.001 (abstract inspected; full text inaccessible in the current review).
