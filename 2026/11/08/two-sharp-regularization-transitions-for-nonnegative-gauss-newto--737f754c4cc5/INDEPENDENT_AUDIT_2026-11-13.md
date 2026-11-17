# Independent mathematical audit

## correctness

PASS

For S_j=x^TH^jx, m=S2/S1 and variance v=S3/S1−m², expanding the update gives (1+σ²v)/(1+σm)². Endpoint inequality v≤(b−m)(m−a) is sharp for any actual extremal eigenspaces. Independent SymPy differentiation produced the affine derivative numerator σ[σ(a+b)+2σ²ab−2−σ(2+σ(a+b))m]; substitution of stationary m verified the quoted second rational branch identically. The branch switch, unique σ minimax point, and κ descent frontier follow from derivative and AM–GM with attainable two-point mass. Independent exact witness at H=diag(1,10), σ=2 is alpha=12/31 and ratio=41/31.

## originality

PASS

Source NGN and scaled-Polyak algorithms, constants and pointwise inequality were explicitly separated. The new continuously parameterized sharp finite-σ envelope, two-eigenspace maximizing state, mode switch and safe regularization frontier do not follow from the fixed-gamma source. Originality remains best-of-knowledge given the broad adaptive gradient literature.

## value

PASS

The exact worst one-step objective factor for a named adaptive optimization method is a natural benchmark. Separating universal one-step descent, regularization that minimizes worst-case loss, and transient objective spikes gives a meaningful calibration boundary and explicit extremizers across every SPD dimension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
