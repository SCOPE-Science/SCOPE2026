# Mathematical assessment

## Correctness — PASS

The claim is restricted to stationary two-coordinate Gaussian observations with known added-noise intensity. For \(|b|<1\), the drift is strictly stable and the Gaussian covariance solves a unique Lyapunov equation. The stationary covariance and Fisher information are reconstructed independently from the model, not merely copied from a source. Symbolic differentiation produces an explicit cubic \(P\) whose sign controls the coupling derivative. Its strictly negative second derivative on the physical interval proves at most two interior stationary points; normalization by \(d^4\) produces a family strictly increasing in added-noise strength, giving exactly one onset. The double-root expansion and the strong-noise roots follow from nondegenerate Taylor expansion and uniform polynomial limits. The bundled script verifies all exact algebraic identities, 152 rational tests and the numerical critical pair. Numerical calculations are not used as infinite proofs.

## Originality — PASS, with explicit qualification

The closest source is Nascimento and Morgado (arXiv:2610.20963, 2026), which provides the exact Fisher-information formula and states that a nonmonotone dependence on coupling is possible at sufficiently large noise. Those are acknowledged prior results. The final claim is neither a new Gaussian distribution nor a new formula for Fisher information. The qualitative statement and the exact formula do not, in the inspected text, supply the unique onset \(d_\star\), an exact global classification into zero/two turning points, the saddle-node splitting or the two large-noise branches. These require a concavity and parameter-order argument for the derivative polynomial. The result remains an algebraic extension of an explicit published formula, a meaningful residual priority and scope limitation.

Matsumoto, Sasa and Dechant (arXiv:2504.09981, 2025) study a different learning-rate information matrix associated with probability currents and coordinate rotations. Their Brownian-gyrator example does not give Fisher information for estimating the coupling as a statistical parameter. Accessible preceding claims about Gaussian fluctuations and stochastic dynamics concern different observables or models. Independent publication-priority examination has not been performed.

## Value — PASS

The source reports an experimentally relevant nonmonotone sensitivity effect, but without identifying the boundary between monotone and nonmonotone regimes. The exact threshold locates the noise intensity at which increasing coupling first becomes information-suppressing over a nonempty interval; the unique pair of turning points gives that entire interval without numerical curve scanning. The square-root opening describes the onset, and the large-noise laws show that one extremum moves toward zero coupling while the other remains at finite coupling. This is a natural and complete classification of a qualitative regime change, not an arbitrary parameter table or a small numeric improvement.

## Limitations and closest prior literature

The result concerns \(\mathcal I_{bb}\) with \(d\) known, not the Schur-complement information for simultaneously estimating \(b\) and \(d\). The 2026 source supplies all underlying distributional and Fisher-information formulas, and those are not claimed. The inspected 2025 learning-rate study concerns a distinct observable. Exhaustive publication coverage is not guaranteed. The numerical critical values are computed to high precision, not interval-certified; the exact threshold is defined and proved unique without relying on those decimals.

Self-review: passed. Independent audit: not yet performed.
