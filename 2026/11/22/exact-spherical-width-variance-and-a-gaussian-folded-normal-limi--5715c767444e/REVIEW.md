# Independent mathematical audit

## correctness

PASS

With inherited Euclidean metric and full width, the box and segment contribute b times the spherical l1 norm and a times the absolute sum of coordinates, respectively. Each unit projection has absolute mean c_d. For two unit projections the absolute product mean is K(rho)/d by independent Gaussian polar decomposition and the two-dimensional angular integral. The coordinate pairs have rho=0 and the coordinate/diagonal pairs have rho=d^(−1/2); this yields the stated finite cross term as well as both individual variances. For fixed a,b, the joint iid CLT for (|G|−mu,G²−1,G) separates the last coordinate from the first two by odd parity. Radial expansion produces the correction −mu/2 times the second fluctuation in the l1 term, so its variance is 1−3/pi, and the diagonal produces an independent folded normal. The gamma ratio permits exact-mean centering. Sphere concentration with Lipschitz constants at most sqrt(d) for each width component gives uniform higher absolute moments and thus third-moment convergence. The absolute Gaussian third moment is 2mu, giving a³mu(4/pi−1). The a=0 boundary removes exactly the folded term. Independent vertex enumeration and midpoint quadrature for d=2 with 65,536 directions agreed with the exact mean and variance to 8.75e−10 and 5.78e−10, respectively. Replay: python3 /workspace/branches/d050110f-c0fb-40d8-850a-1b3e12aae924/independent_d2_width_check.py; see independent_d2_width_check.txt there. That check does not prove asymptotics. Frozen verification describes internal finite checks, not attestation or formal proof verification.

## originality

PASS

The box-plus-diagonal geometry, support identity, cube-only limit and general probability tools are prior. The strongest distinct width and isocanted-cube comparisons inspected do not provide the positive-cant Haar variance or the independent folded correction after radial normalization. The pass goes to the combined angular statistic under the stated sampling, not to the representation or a new Gaussian CLT.

## value

PASS

Angular width on this natural perturbation of the cube gives a concrete boundary of Gaussian width behavior: a single longitudinal generator retains its own random component even when the leading width scales like sqrt(d). The exact variance distinguishes the finite covariance from limiting independence, and the different first- and third-moment scalings recover box length and cant separately. This is more than computing an isolated low-dimensional entry or restating the cube CLT.

The dated certificate retains the supplied scientific assessment, sources and limitations.
