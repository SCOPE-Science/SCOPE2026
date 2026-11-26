# Independent mathematical audit

## correctness

PASS

Taking absolute values of the first Gaussian coordinates and normalizing gives independent hemisphere points; normalization preserves signs. The other d−1 coordinates give a centered off-diagonal Gram vector independent of the first-coordinate products. The determinant characteristic function has quadratic term −||t||²/2 and cubic term −i times the sum of triangle monomials divided by sqrt(d−1); tr T³ counts each unordered triangle six times. For the Fourier remainder, on ||t||≤n^(1/8) the convergent log-determinant expansion and its fixed-order derivatives give an n^(−1) polynomial-times-Gaussian bound after subtracting the linearized cubic. Outside, each fixed-order derivative of the characteristic function costs at most a fixed power of n, since ||(I−iT/sqrt(n))^(−1)||≤1. The determinant bound is Gaussian up to ||t||=sqrt(n), and beyond that radius splitting off a fixed integrable power gives an exponentially small integral even after that polynomial cost. Fourier inversion with coordinate derivatives through order m+2 therefore gives the stated L¹ remainder. The Gaussian orthant integrals have globally bounded second derivatives with respect to the shifts; the shift mean is E|G_iG_j|=2/π. Each cubic monomial integrates over the unshifted orthant with three signed first moments ±1/sqrt(2π); shifting changes these integrals by O_k(n^(−1/2) sum H_ij) before the cubic prefactor. Thus both relative coefficients are (2/π)^(3/2). Finiteness of the half-normal moments gives a uniform bound at fixed k, and n=d−1 can be replaced by d at the claimed precision. For k=3 the signed sum plus product is 4 and −4 at the constant patterns and zero at each mixed pattern. The theorem also follows independently from the Wishart density and anchor conditioning comparison documented below.

## originality

FAIL

Although the hemisphere law is not stated verbatim in the inspected sources, it is a direct consequence of Ouimet's earlier precise central Wishart density expansion, ordinary orthant integration, and rotation-invariant conditioning on the signs to one additional full-sphere point. The prior expansion already provides the coefficient and the precision necessary for every fixed k and pattern.

## value

FAIL

The uniform sign law and equality of coefficients are useful descriptions. However, in the earlier full-matrix expansion the two contributions are the same triangle invariant, with the apparent edge term resulting from putting one vertex at the conditioned pole. The frozen result does not add a distinct asymptotic estimate or classification beyond this direct specialization, and it does not claim an independently assessed advance such as growing k or a new cap regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
