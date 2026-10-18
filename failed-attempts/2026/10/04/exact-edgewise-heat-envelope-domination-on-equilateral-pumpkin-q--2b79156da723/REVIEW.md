# Independent mathematical audit

## correctness

FAIL

The claimed identity is explicitly basis-independent for any L2-orthonormal eigenbasis, but the proof uses ||a cos θ+b sin θ||_sup²=|a|²+|b|²; that identity fails for complex coefficients. For N=2, let u_c have cos θ/sqrt(ell) on both edges and u_s have sin θ/sqrt(ell) and -sin θ/sqrt(ell) respectively. This is a real orthonormal pair at every positive eigenvalue and contributes 2/ell in summed edgewise sup². Replacing it by the equally valid complex ONB (u_c+i u_s)/sqrt(2), (u_c-i u_s)/sqrt(2) gives two constant-modulus edge restrictions with sup²=1/(2ell) each, totaling 1/ell, contrary to the claimed 2/ell. The projected sine coefficient trace verifies only a real orthogonal change of basis; a complex unitary mix introduces phase and destroys sup² additivity. A real-eigenbasis-restricted theorem might be correct, but the current final claim unqualified is false. This independent analytic counterexample overrides the saved VERIFY_OK and any real-basis finite tests.

## originality

PASS

No directly inspected prior result states the all-positive-frequency real-basis pumpkin heat-envelope equality, so the mathematical comparison appears new conditional on a real-valued ONB restriction. This originality assessment does not rescue the false unqualified scientific claim. Harrell–Maltsev's general edge-envelope conjecture and Kennedy–Rohleder's first-eigenvalue calculation are not the full all-level sum; primary full-text retrieval of Harrell–Maltsev was not available in this run.

## value

PASS

A correct basis-specified edgewise heat-envelope identity would give a sharp exact check of a conjectural metric-graph comparison for a natural full family and reveal how multiplicity affects edge sup norms. The current claimed basis-invariant assertion is false; this is an independent value assessment of the natural target, not acceptance of the uncorrected package.

The dated certificate retains the supplied scientific assessment, sources and limitations.
