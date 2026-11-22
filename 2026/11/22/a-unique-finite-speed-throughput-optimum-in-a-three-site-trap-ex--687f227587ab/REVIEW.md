# Review of the finite-speed throughput optimum

## Correctness — PASS

The eight-state stochastic generator is specified without closure approximation; its normalized stationary solution yields the displayed rational current. Exact symbolic reconstruction and independent rational-sample solves in `verify.py` support the algebra. Differentiation gives a quartic with coefficient signs \(+,+,+,-,-\) under the physical density-contrast bound; Descartes' rule and opposite signs at \(t=0\) and \(t=1\) establish a unique global maximum. Strict current comparisons, domain endpoints, and the fully biased example follow by exact factorizations. No finite numerical sampling is being used as an infinite proof.

## Originality — PASS, with priority risk

The most relevant primary source, Sakai–Akimoto arXiv:2609.03560, studies precisely this boundary-driven site-trap family, but develops an approximate general nonlinear response and exact reflection symmetries rather than the particular exact three-site current and global single-defect speed optimum. Their periodic external-field paper arXiv:2512.03316 does not imply the boundary-driven optimization. Earlier homogeneous-open current statistics do not cover variable departure rates. Indexed nearby technical results on minimal four-site rectification compare even-bias response under an asymmetric defect, not the unique optimal current through a reflection-symmetric three-site defect. Searches did not uncover equivalent optimization, but searchable databases and inaccessible full texts cannot establish publication priority conclusively.

## Value — PASS

The minimal channel with a genuine interior trap supplies an exact benchmark for finite-rate transport design. Its strict finite-speed optimum is counterintuitive: both ordinary centre waiting time and the infinitely fast-centre limit produce the same reference current, while a strictly intermediate rate improves it; the fully biased half-density case improves throughput by about 11%. The parameter-uniform uniqueness theorem and explicit quartic give a usable test of approximate closures for heterogeneous active and passive lattice transport. This is a natural complete global optimization, not an arbitrary numerical parameter slice.

## Scope and residual risks

Only three sites, symmetric nearest-neighbour bulk hops, a single departure-time defect, equal endpoint and contact time scales, and stationary mean current are covered. Larger systems may have different optima. An unindexed finite-chain solution with a stronger theorem could subsume this result; independent priority and scientific validation are not claimed.

Self-review: passed. Independent audit: not yet performed.
