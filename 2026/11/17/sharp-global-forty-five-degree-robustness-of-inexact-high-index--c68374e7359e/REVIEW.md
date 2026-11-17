# Scientific review

## Correctness — PASS

For the stipulated globally split energy, the negative eigenspace is fixed and \(\nabla E=(I-2P_0)\nabla F\). For any orthogonal projectors \(P,P_0\), the exact identity
\[
\operatorname{sym}\big((I-2P)(I-2P_0)\big)=I-2(P-P_0)^2
\]
is obtained solely by expanding the idempotent symmetric matrices. The resulting strict Lyapunov inequality, global strong convexity and gradient-dominance inequality prove the stated all-start exponential bounds, while compact sublevel sets prevent finite-time escape. In dimension two, rotating the approximate projector by \(\phi\) gives an exact scaled rotation flow with real growth exponent \(-\beta\mu\cos(2\phi)\), proving attainment of the positive-rate bound, closed periodic trajectories at the threshold and instability above it. The same two-coordinate block embeds in any allowed index. The independent reproducibility script checked exact rational instances; the general result does not rely on finite sampling.

## Originality — PASS within checked evidence

The closely related 2026 perturbed high-index saddle result assumes \(\mu-2\alpha L>0\) and provides a *local sufficient* estimate. Here the fixed-splitting subclass supports a *global* guarantee, permits arbitrary projector variation, removes dependence on upper curvature, and has a matching exact failure at the threshold. The 2025 Householder-angle result concerns the angle between a *gradient* and an ascent subspace to classify instantaneous increase/decrease of the original energy, not an error between exact and approximate unstable eigenspaces or a Lyapunov convergence theorem. The 2026 preconditioned method gives local/discrete spectral estimates and does not subsume the present continuous-time nonlinear guarantee. The sharp coefficient is derived, not assumed from an angular heuristic.

Published mathematical finding summaries concerning switched unstable saddle flows and approximate preconditioner directions were also compared by their hypotheses and implied conclusions. Neither concerns this globally split HiSD vector field. Historical novelty remains provisional because general variable-metric/sectorial gradient-flow results may imply parts of the argument; the elementary projector identity is not asserted to be original. The closely relevant three primary full texts were inspected in their applicable sections; an older discrete HiSD study was available only through its abstract in this review.

## Mathematical value — PASS

The natural question is how inaccurate an unstable eigenspace can be while preserving saddle-search dynamics. Existing curvature-ratio-dependent sufficient bounds do not identify the *sharp* feasible angle even in a globally well-conditioned geometric class. A forty-five-degree threshold valid for arbitrary time-varying and state-varying subspaces, exact worst-case exponential rate, and critical periodic obstruction distinguish a universal robust-stability mechanism from mere local matrix stability. The result remains meaningful for nonlinear strongly convex block functions and arbitrarily ill-conditioned block curvatures. It neither asserts new projector algebra nor extrapolates to coupled landscapes, state-dependent true eigenspaces, discretizations, or eigenspace-tracking dynamics.

## Closest literature and limitations

Most directly relevant are Shi et al., *Asymptotic stability of high-index saddle dynamics*, arXiv:2611.09049v1, Section 3.2, and Chu–Lin, *Generalized Gentlest Ascent Dynamics Methods for High-Index Saddle Points*, DOI:10.1137/24M1710905, Sections 2–3. Huang et al., *Preconditioned High-index Saddle Dynamics for Computing Saddle Points*, arXiv:2603.25390v1, contains a separate local/discrete inexact projector analysis. The fixed splitting is an essential hypothesis; no statement is made about general nonseparable nonlinear saddle energies. Mathematical priority and validation have not been independently established.

Self-review: passed. Independent audit: not yet performed.
