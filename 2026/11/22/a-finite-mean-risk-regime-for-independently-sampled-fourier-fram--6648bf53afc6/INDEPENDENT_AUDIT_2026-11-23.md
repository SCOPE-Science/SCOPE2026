# Independent mathematical audit

## correctness

PASS

The frozen Gram-matrix bounds are correct. The frozen statistical statement in RESULT.md line 40 is false as literally quantified: e_j=√ν Z_j are independent centered coordinates of common variance ν, but the noise vector is a design column times √ν. The least-squares coefficient error then has deterministic squared norm ν, not νR conditional on A. In particular this noise can have finite mean risk even where R has infinite expectation. The corrected statistical hypothesis explicitly imposes conditional mean zero and second moment E[ee*|A]=νI, under which tracing the conditional second moment of A†e proves the asserted identity. The repaired theorem also sharpens the partial frozen sampling regimes. Verify full rank by the first N distinct nodes; the normalized (z−Z_1)^(N−1) and Haar cluster probability (δ/π)^(m−1) give the lower power α=(m−1)/(2(N−1)). For strict events one can set δ so the Rayleigh upper bound is s/2. The checked square lemma uses a Lagrange inverse, coefficient binomial norm, and the conditional chord law P(|Z_i−Z_j|/2≤u)=(2/π)arcsin(u)≤u, so reciprocal chord products have a logarithmically corrected square-root tail at the Gram threshold. In the repaired upper bound condition on Z_1; rotations of every node preserve the subframe Gram spectrum by a diagonal unitary, so the square probability q_N(s) is the same for any fixed anchor. There are M=m−1 residual cyclic windows of d=N−1 variables; each variable occurs in exactly d windows, also at m=N when windows coincide. Full Gram dominance forces all M anchored windows to have small least eigenvalue. Integrate one independent residual coordinate at a time, applying Hölder of exponent d to the d incident factors. Their old roots cancel on the next integration, leaving the product of the full L^d norms, so the intersection probability is at most q_N(s)^(M/d) with no independence assertion for the overlapping events. This gives the identical power α with a log upper loss. Layer cake gives finiteness exactly for p<α and divergence at equality by the lower bound, transferred to R^p by 1/Λ≤R≤N/Λ. In particular mean risk under the corrected noise assumptions is finite exactly for m≥2N. The original uniform disjoint-block bound is retained as a corollary and is valid by positive Gram addition and true block independence. Corrections are complete in /workspace/repairs/5; replay its RESULT.md proof and run the new CHECK.py there (318 bounded exact window/threshold cases and column identity passed). The frozen CHECK.py was inspected statically only. No finite check proves the analytic quantifiers.

## originality

PASS

Qualified for the repaired exact rectangular inverse-moment threshold and matching small-eigenvalue power up to the explicit logarithmic upper factor. The frozen m≥3N finite regime follows directly from known square inverse moments plus elementary independent positive-Gram addition; that corollary is not credited as new. The new comparison uses overlapping, conditioned subframes to reach the known geometric obstruction's exact exponent in the rectangular model.

## value

PASS

The repaired theorem distinguishes exactly when expectations of noise amplification exist, including the boundary and all positive inverse-moment orders, in a standard iid Fourier design. It resolves the previously unclassified 2N≤m<3N range and gives a precise correction to the tall-design divergence claim. The required noise assumption separates inverse-Gram integrability from potentially design-correlated error. No uniform-in-dimension guarantee, leading coefficient, or sharp logarithmic factor is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
