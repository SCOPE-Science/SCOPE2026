# A sharp detector-placement threshold for stationary ballistic-reset speed-law identification

## Finding
Consider a one-dimensional ballistic particle that repeatedly travels from a launch point \(L>0\) toward an absorbing threshold at \(0\). After each arrival it is instantaneously returned to \(L\), draws a new independent speed \(V\) from an unknown probability law \(\phi\), and continues. Let the known admissible speed interval be \([v_-,v_+]\), with \(0<v_-<v_+<\infty\). In the stationary process, suppose only a binary detector \(B_a(t)={\bf 1}_{\{X(t)>a\}}\) at one fixed location \(a\in(0,L)\) is observed. Its complete two-time law is specified by \(H_a(t)=\mathbb P(B_a(0)=1,B_a(t)=1)\), because its stationary one-time mean is \((L-a)/L\).

**Theorem (sharp finite-window identifiability).** Ideal knowledge of \(H_a(t)\) at every \(0<t<a/v_+\) uniquely identifies the *entire* unknown speed law \(\phi\), among all Borel probability laws supported on \([v_-,v_+]\), if and only if
\[
a\ge a_c:=\frac{Lv_+}{v_-+v_+}.
\]
This includes probability atoms and the critical equality case. For every \(0<a<a_c\), distinct laws with the same known speed bounds have identical observed two-time laws throughout that interval, even when both laws possess strictly positive continuous densities on the interior of the bounds.

More precisely, put \(z_0=(L-a)v_+/a\), and define the stationary, time-size-biased speed distribution and its stop-loss potential by
\[
\psi(dv)=\frac{\phi(dv)/v}{\int\phi(du)/u},\qquad
K(z)=\frac{Lz}{L-a}\,H_a\!\left(\frac{L-a}{z}\right),\quad z>z_0.
\]
Then
\[
K(z)=\int(z-v)_+\,\psi(dv),\qquad K''=\psi
\]
in the sense of distributional derivatives on \((z_0,\infty)\). The data determine exactly the restriction of \(\psi\) to \((z_0,v_+]\) and the total mass and first moment of its restriction to \([v_-,z_0]\) (with an empty or full interval interpreted naturally). Whenever \(a\ge a_c\), this determines \(\psi\) completely and yields the explicit reconstruction
\[
\phi(dv)=\frac{v\,\psi(dv)}{\int u\,\psi(du)}.
\]

## Assumptions and scope
The particle is ballistic at constant positive speed during each flight, independent speeds are redrawn at every threshold arrival, resetting is instantaneous, and no other displacement or killing mechanism operates. The spatial length \(L\), detector coordinate \(a\), and admissible positive speed bounds are known. The observation consists of ideal exact stationary two-time probabilities for all lags in the stated *short-time* interval; no reset times, speeds, or continuous positions are observed. The theorem concerns this specified observation window, not arbitrarily long-lag detector histories, multiple detectors, finite samples, or noisy measurements.

For arbitrary laws including purely atomic laws, stationarity means the canonical equilibrium renewal process obtained by length-biasing complete flights and choosing a uniform phase within the selected flight. A process freshly released from \(L\) need not converge in law in the arithmetic or deterministic cases; the theorem does not assert such convergence. For nonlattice speed laws, the usual stationary long-time regime is compatible with this construction.

## Proof
**Stationary marking.** One flight at speed \(v\) lasts \(L/v\). The renewal-reward formula therefore gives the speed distribution seen at a stationary time as \(\psi(dv)\) above. Given the current speed, the fraction of the flight completed is uniform, so the current position \(X(0)\) is uniform on \((0,L)\), independent of the current speed. This also establishes \(\mathbb P(B_a(0)=1)=(L-a)/L\) for all \(\phi\).

**A reset-free observation window.** Condition on \(X(0)>a\). The soonest possible threshold arrival is \(X(0)/v_+>a/v_+\). Thus, at any \(0<t<a/v_+\), the particle cannot reset before the second observation; it simply moves to \(X(0)-Vt\). Integrating the uniform starting position yields the exact identity
\[
H_a(t)=\frac1L\int (L-a-vt)_+\,\psi(dv).
\]
No renewal expansion or approximation is used here, and the formula remains valid for atomic speed distributions.

**Integral-transform inversion.** Set \(\ell=L-a\) and \(z=\ell/t\). The available time window corresponds precisely to \(z>z_0=\ell v_+/a\). Multiplying the last identity by \(Lz/\ell\) gives \(K(z)=\int(z-v)_+\,\psi(dv)\). Since the distributional second derivative of \((z-v)_+\) in \(z\) is the unit point mass at \(v\), \(K''=\psi\) on the observed interval. If two laws have the same \(K\), their speed-biased laws agree on \((z_0,v_+]\). The difference between their remaining lower parts contributes an affine function \(z\,\Delta M-\Delta m\) to \(K(z)\) for every \(z>z_0\); equality of \(K\) forces both total-mass difference \(\Delta M\) and first-moment difference \(\Delta m\) to vanish. Conversely those conditions force equality of the observed potentials. This proves the stated *complete equivalence-class characterization*, including possible atoms at \(z_0\).

**Sharp placement cutoff.** For \(z_0<v_-\), the observed distributional derivative contains every atom and every continuous component. At \(z_0=v_-\), all mass above \(v_-\) is recovered and the possible atom at \(v_-\) is fixed by total probability one. Thus \(z_0\le v_-\) is sufficient for uniqueness, and it is equivalent to \(a\ge Lv_+/(v_-+v_+)\). The inverse length-bias identity then reconstructs \(\phi\) uniquely.

If \(z_0>v_-\), choose three disjoint small intervals inside \((v_-,\min(z_0,v_+))\) and three smooth bump densities supported in them. Their nonzero linear combination can be chosen to have both zeroth and first moments equal to zero, because these impose only two linear conditions. Start with a continuous density \(\psi_0\) strictly positive throughout \((v_-,v_+)\); adding or subtracting a sufficiently small multiple of that signed bump preserves positivity, normalization, mean, and both support endpoints while changing the law. All observed potentials remain identical by the preceding equivalence characterization. Transforming each perturbed \(\psi\) to \(\phi(dv)=v\psi(dv)/\int u\psi(du)\) gives distinct admissible physical speed laws, proving necessity and sharpness. In the case \(z_0\ge v_+\), the same construction works, since all admissible speeds fall in the unidentified part.

## Verification
The exact identities and sharp threshold are proved for arbitrary Borel probability measures without relying on simulation. A standalone standard-library Python script, `check_binary_persistence.py`, performs 293 exact-rational checks of the stationary length-bias transform, the observed stop-loss potential, recovered cumulative weights, and a pair of distinct laws with identical subcritical detector observations. For example, with \(L=1\), \(v_-=1\), and \(v_+=4\), the placement threshold is \(a_c=4/5\): two distinct distributions with common endpoint masses and matched lower mass/mean give equal \(H_{7/10}(t)\) for all \(0<t<7/40\) but are distinguished by observations at \(a=4/5\). The script enumerates rational witness lags; the exact identity for *all* lags follows from the proof, not the enumeration.

To reproduce: run `python3 check_binary_persistence.py` with standard Python 3. It prints a PASS statement if all tests succeed. No external packages or downloaded data are required.

## Relationship to prior work
Das, Majumdar and Pal [1] established the same ballistic threshold-reset model's speed-independent uniform stationary position law, its one-time transient propagator, freezing transitions and cutoff-induced shocks. The stationary *binary two-time* inverse problem and sharp sensor-location identifiability threshold treated here are not stated in the relevant inspected sections of that work. The uniform stationary marginal used here is their known forward result, not a new claim.

Zamparo [2] established renewal correlations and inverse waiting-time problems for a discrete-time binary sequence marking *renewal epochs*. That is a different observable from the continuous-time occupation indicator of a spatial interval during each ballistic flight. Standard equilibrium renewal length bias and inversion of the stop-loss potential are classical components and are credited as methods, not claimed as new lemmas. Evans and Majumdar [3] analyzed run-and-tumble particles with external Poisson resets rather than the present threshold-triggered, fixed-flight-length inverse detector problem. The new theorem identifies precisely which portion of the hidden speed law survives binary spatial coarse-graining and when complete recovery becomes possible; its originality is qualified by the possibility that a more general existing alternating-renewal inverse theorem implicitly implies the transform identity.

## Limitations
Reconstructing a measure from a second distributional derivative is generally unstable under noisy finite-sample observations; neither a statistical estimator nor a stability rate is proved. A known finite upper speed bound is essential to the guaranteed reset-free window, and the positive lower bound is essential to the stated universal sensor cutoff. No assertion is made about identification from full long-lag binary histories when the placement is subcritical. The theorem has no diffusion, run-and-tumble reversal, noninstantaneous return, or multi-particle interactions. Independent audit and publication-priority verification have not been performed.

## References
[1] R. Das, S. N. Majumdar, A. Pal, *Freezing transition and shock-like transients in ballistic random walks under threshold resetting*, arXiv:2611.16733v1 (first public 2026-11-12 UTC). https://arxiv.org/abs/2611.16733 ; lawful readable copy: https://borowiecki.dev/pdf/2611.16733 .

[2] M. Zamparo, *Renewal Model for Dependent Binary Sequences*, Journal of Statistical Physics **187**, 5 (2022). https://doi.org/10.1007/s10955-022-02893-8 .

[3] M. R. Evans and S. N. Majumdar, *Run and tumble particle under resetting: a renewal approach*, arXiv:1808.06450 (2018). https://arxiv.org/abs/1808.06450 .
