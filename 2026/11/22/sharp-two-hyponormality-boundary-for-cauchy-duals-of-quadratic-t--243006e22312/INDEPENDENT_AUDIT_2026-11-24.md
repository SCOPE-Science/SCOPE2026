# Independent mathematical audit

## correctness

PASS

For a>0 and b>=0 the positive weights telescope, increase the norm pointwise for the original shift, tend to one, and give reciprocal Cauchy-dual moments. The second forward difference of the original quadratic norm polynomial is nonzero, and its third vanishes on every basis orbit; the diagonal identities prove strict three-isometry. Independently clearing the 2x2 and 3x3 Hankel determinants gives the stated positive denominators and numerators. The y-derivative has negative discriminant and negative leading coefficient for u=(a+2)^2>4; F(u,0)>0 and F(u,y) tends to minus infinity. For fixed y=b^2>=0 the discriminant in u is negative and F(0,y)<0, so the first determinant controls all later ones. Substituting the initial size-two cutoff gives the stated strictly negative product, proving all leading size-two minors are strictly positive at and below the cubic threshold. The Schur complement proves positivity, rank two at the initial equality block, and positive definiteness thereafter; above the threshold the initial determinant is negative. The Laplace integral gives the finite signed density; compact-interval moment uniqueness and its sign change exclude subnormality for b>0, while at b=0 it is a probability density. The scaled cubic converges coefficientwise and strict sign brackets at its unique positive root prove the stated limit. Exact algebra independently replayable with python3 /workspace/review_checks/hankel.py (SymPy); the replay does not stand in for the shifted positivity proof. Read the frozen checker and verification guide as recorded evidence, not as formal certification.

## originality

PASS

Best of current knowledge: the distinct result is the exact finite size-three Hankel cutoff, including its first-shift reduction, boundary ranks and large-displacement constant. Neither the same-family weak-concavity criterion nor the full Hausdorff characterization covers it. The moment family, Hankel framework and complete subnormality dichotomy are not new.

## value

PASS

This is an all-parameter exact finite-order positivity classification for a natural polynomial-shift family. The initial-to-tail comparison solves an infinite sequence of constraints, and the sharp separation, rank transition and ratio quantify a real gap between ordinary hyponormality, two-hyponormality and subnormality. It is not just a symbolic determinant or an isolated numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
