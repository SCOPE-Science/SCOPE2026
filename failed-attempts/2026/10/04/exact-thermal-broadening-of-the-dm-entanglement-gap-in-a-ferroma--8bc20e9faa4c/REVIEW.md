# Independent mathematical audit

## correctness

PASS

Starting from the published undercritical and overcritical concurrence formulas, positivity is controlled solely by the signs of their numerators. Since \(\nu(D)=\sqrt{P^2+D^2}\) is strictly increasing, setting those numerators to zero gives exactly the stated inverse-hyperbolic lower and upper edges. The source critical value \(\nu_c=A+Z\) lies strictly between the edges by the displayed elementary exponential inequalities. Expanding the edge equations at low temperature gives equal leading shifts \(T e^{-2A/T}\) in \(\nu\), and applying \(D'(\nu_c)=\nu_c/D_c\) gives the stated width. The package verifier independently checks edge equations and concurrence signs on deterministic parameter grids. The all-parameter theorem rests on monotonicity and exact algebra.

## originality

FAIL

The same primary paper already prints the complete finite-temperature concurrence on both sides of the same ferromagnetic DM critical coupling. The audited edge formulas are obtained by setting the published numerators equal to zero and applying \(\operatorname{arcosh}\) or \(\operatorname{arsinh}\); the exact zero interval follows immediately from monotonicity. The low-temperature width is then a routine asymptotic expansion of those same closed formulas. Under implication-based originality, this is mechanically covered even though the source discusses the finite-temperature gap qualitatively rather than presenting the inverted edge formulas.

## value

FAIL

The closed edges are useful for exposition and plotting, but they arise from one-step inversion of already-published same-object concurrence numerators, followed by a standard low-temperature expansion. This does not introduce a new structural mechanism, boundary phenomenon, or difficult exact invariant beyond what the source formula already encodes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
