# Independent mathematical audit

## correctness

PASS

Independently reconstructed the threshold by sink elimination, rather than matrix inversion from the uploaded checker. With w=B/m, the sink block of −H is positive definite and its Schur complement on the refuge is the threshold minus r. Set the refuge coordinate to one. A single sink branch gives value w/(d+w); the branch of length two gives the first value w(d+w)/(d²+3dw+w²) by solving its two sink equations. Thus the interior-refuge path has threshold wd[1/(d+w)+(d+2w)/(d²+3dw+w²)], with w=B/3, yielding the stated r_P. In the diamond the refuge is linked to all three sinks; equal sink values w/(d+w) solve their equations (all sink–sink flows cancel). The threshold is 3wd/(d+w), w=B/5. On a common positive denominator their difference has numerator 3Bd²(3d²−B²), so gives a strict single crossing and opposite invasion decisions between the thresholds. The exact example inequalities 66/155<107/250<3/7 and 1/2<51/100<39/76 hold. For order three, write t=d/B. The path center, path endpoint and triangle thresholds divided by B are 2t/(2t+1), 2t(t+1)/(4t²+6t+1), and 2t/(3t+1). Center minus triangle is 2t²/[(2t+1)(3t+1)] and triangle minus endpoint is 2t²(t+2)/[(3t+1)(4t²+6t+1)], both positive. Order two has only one rooted type, so minimality holds at fixed order. General inertial sign and simplicity follow from the positive definite sink block (equivalently the rank-one congruence), with strict positivity of the principal eigenvector by connectivity. For the logistic corollary, v·x decays to zero when λ≤0 by weighted Cauchy–Schwarz. When λ>0 a small multiple of v and a large constant are lower and upper solutions; their monotone bounded trajectories converge, and the maximal-coordinate ratio test rules out distinct positive equilibria by strict quadratic loss. Positivity after any positive time and comparison give convergence from all nonzero nonnegative states. Inspected check.py and VERIFICATION.md without executing source code; numerical eigensamples corroborate the symbolic thresholds but are not the proof.

## originality

PASS

The distinct supported claim is the exact equal-total-conductance threshold crossing at B/d=√3 for the specified rooted path and diamond, with the fixed-order two/three-vertex obstruction. Spectral invasion tests, rank-one reductions, and topology-dependent examples in other ecological models are established and not part of the originality basis.

## value

PASS

This is a sharp minimal benchmark showing that adding uniform corridors under a fixed total budget can favor either topology, depending on the ratio of total conductance to sink mortality. The exact threshold separation yields an explicit window in which the two graphs differ in deterministic invasion, not just in the value of an eigenvalue, and the rooted low-order obstruction explains why smaller examples cannot show this effect under the same normalization. The model does not identify realistic ecological parameters or stochastic extinction times.

The dated certificate retains the supplied scientific assessment, sources and limitations.
