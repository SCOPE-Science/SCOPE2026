# Review of the dimension-twelve Gauss–Padé positivity boundary

## Correctness — PASS

The exact two-stage rational stability map is normalized by the unweighted combinatorial hypercube Laplacian. Walsh diagonalization gives every distance-shell entry. The common strictly positive step in dimension twelve is certified by thirteen positive integers at the rational step \(h=1/3\); the entire higher-dimensional obstruction is certified by three rational Sturm-sequence variation equalities on covering intervals. Marginalization across Boolean-cube coordinates extends both halves to every dimension. The companion source constructs and checks the integer and Sturm certificates from their defining expressions and passed 116 assertions. The small-step dimension-six threshold is obtained from the exact zero sixth Padé Taylor coefficient and the negative seventh-distance term. No finite timestep search is used as proof of an all-real statement.

## Originality — PASS on inspected evidence, with residual risk

The closest published Boolean-cube result gives a large-step negative adjacent entry and the complete three-cube interval; the closest Cartesian clique-product result characterizes positivity at **every** step. Neither result implies the present **existence-of-at-least-one-positive-step** characterization, because dimensions three through twelve have both positive and negative step ranges. The earliest focal primary work of Zappavigna, Colaneri, Kirkland and Shorten (2012) establishes method-wide Padé positivity counterexamples, and Lóczi and Ketcheson (2013) establish general rational absolute-monotonicity facts. The seventh-series-coefficient obstruction and all-step classifications are credited prior art, not newly claimed. The new dimension-twelve/twelve-versus-thirteen feasibility boundary and the exact three-shell obstruction were not found in the inspected primary material or targeted published-result searches. Unindexed specialist duplication remains possible.

## Value — PASS

For a canonical, highly symmetric Markov diffusion network, stability and conservation do not imply positivity. The theorem resolves the previously unidentified integer-valued design question of whether **any** legitimate positive-step Markov transition is available for a specific widely used fourth-order implicit method, and shows a sharp unexpected transition between dimensions twelve and thirteen. The gap between the local threshold six and the global feasibility threshold twelve demonstrates real intermediate-step recovery with practical interpretation for diffusion simulation and for diagnostic testing of rational integrators.

## Limitations

The result applies only to exact two-stage Gauss–Legendre completed steps on unweighted Boolean cubes. It does not enumerate all admissible steps in dimensions four through twelve, address internal stages or floating-point arithmetic, or guarantee preservation under asymmetric weights. The proof is reconstructed and supported by rational certificates in a self-review; an independent audit has not occurred. The published-source comparison is bounded and does not prove publication priority.

Self-review: passed. Independent audit: not yet performed.
