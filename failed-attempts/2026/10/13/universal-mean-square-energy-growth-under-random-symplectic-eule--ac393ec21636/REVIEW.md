# Independent mathematical audit

## correctness

PASS

The one-step matrix A(h) sends (q,p) to ((1-h^2)q+hp,-hq+p). At constant h, the form q^2-hqp+p^2 is invariant and positive definite for 0<h<2. For the random case, expand the quadratic action on (q^2,qp,p^2), then average independently of the incoming state. Direct expansion of the three-by-three determinant at 1 gives -2(m1^2 m4-2 m1 m2 m3+m2^3); the latter bracket is E[(m1 H^2-m2 H)^2]. It is strictly positive for a non-point distribution because H>0 almost surely. The monic real characteristic polynomial is negative at 1 and positive at large positive arguments, so the covariance spectral radius rho exceeds 1. The positive-map cone theorem supplies a nonzero PSD adjoint eigenmatrix P at rho. If P is rank one, write P=vv^T and test on a real w perpendicular to v, giving E[(v^T A(H)w)^2]=0, hence a real invariant line for A(H)^T almost surely. This is impossible because the discriminant is h^2(h^2-4)<0. P is thus positive definite; iteration of its eigenform gives both upper and lower rho^k comparisons for every starting direction. Neither the computation nor the definiteness argument requires the law to stay away from 0 or 2. Including 0 would invalidate the nondegeneracy argument for a mixture of 0 and one fixed positive step. Replay: RESULT.md lines 23–78; verify.py lines 8–60 was inspected without execution. Its symbolic and rational tests are not the proof of the all-law spectral implication.

## originality

FAIL

Demonstrated prior coverage, not a search miss or inaccessible-source judgment. The Resultary kick–drift record d766129a463b gives the same hypotheses, all nonzero deterministic initial vectors, same covariance spectral radius and stronger two-sided bounds, with the identical deterministic alternative and rational witness. Its proof also publishes the exact single-step three-by-three transfer from which the only distinct scalar certificate follows by averaging, evaluating det(I-T), and completing a square. The alternate proof neither extends the classification nor leaves an independently supported substantial new claim.

## value

FAIL

The universal instability question is scientifically meaningful, but its useful classification and exact rate characterization are already available. The residual determinant-at-one identity is a short alternate sign proof by expanding the available three-dimensional transfer, not a new growth estimate, stability boundary or independently needed exact invariant. The scalar identity and identical two-point witness do not justify a standalone repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
