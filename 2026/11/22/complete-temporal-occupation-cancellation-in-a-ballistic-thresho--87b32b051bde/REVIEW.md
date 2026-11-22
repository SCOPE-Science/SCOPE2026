# Scientific review

## Correctness

PASS. The central identity \(\int_0^t(f(X_s)-\bar f)ds=\Phi_f(t)-\Phi_f(0)\) is derived by differentiating the phase primitive and checking it is zero at both reset endpoints. Equilibrium renewal length-bias gives an independent uniform phase and explicit primitive moments. Conditioning on the first regeneration, applying the nonlattice renewal convergence theorem, and truncating the primitive establishes asymptotic independence and the limit difference. The independent-copy difference has a finite \(q\)-th moment precisely when the \((q+1)\)-st duration moment exists. For \(q=2\), covariance mixing yields the exact stationary variance constant; if that moment fails, Portmanteau forces divergence of unscaled second moments. `checker.py` verifies exact identities and a nontrivial asymptotic example. No finite experiment is used as an infinite proof.

## Originality

PASS, with publication-priority qualifications. The closest 2026 primary paper (arXiv:2611.16733, full main text and relevant appendices inspected) establishes a universal stationary one-point density and spatial relaxation, not the all-observable coboundary, the unscaled limit law or the sharp moment hierarchy. Existing standard regenerative theory provides length bias and renewal convergence, but the particular zero-per-excursion reward for every centered spatial observable and its explicit limiting distribution are model-specific. The published threshold-reset sluggish-diffusion occupation results involve noisy excursions with nonzero centered cycle rewards and conventional Gaussian occupation fluctuations, hence neither imply the zero-reward law. An inaccessible full published companion and unindexed equivalents remain risks; searches do not prove universal novelty.

## Value

PASS. The entire family of natural spatial measurements in a one-dimensional resetting transport model has anomalously suppressed temporal averaging noise, despite randomness in flight velocity and a uniform stationary snapshot. The theorem gives its exact unscaled asymptotic distribution and a physically interpretable sharp negative-speed moment boundary; in particular, a low-velocity density exponent determines which long-time integrated-occupation moments are finite. This clarifies what a stationary one-point measurement conceals, rather than merely repeating its uniformity. The phenomenon is specific to fully traversed fixed-length ballistic flights; neither nonlinear dynamics nor noise within flights is addressed.

## Literature and limits

The original preprint was submitted on 12 November 2026. Its stationary propagator, nonuniform transient rates and finite-speed shock results are credited. General renewal references supply the equilibrium-cycle and convergence machinery. The exact comparison with a related published threshold-reset occupation theorem used accessible records; its full source files could not be inspected, so broad implicit coverage cannot be ruled out absolutely. Conditional hypotheses (stationary start, duration density, positive finite mean and moment cutoffs) are explicitly stated in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
