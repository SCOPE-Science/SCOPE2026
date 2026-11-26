# Independent mathematical audit

## correctness

PASS

For fixed q, complete coloured stars are counted by q times the number of weak q-compositions of m-1; this includes the q singleton types. The components form a multiset, giving the stated Euler product and the exact fixed-type deletion bijection. In the tilted geometric model, the expectation and variance follow by Riemann sums: the leading coefficient of a_m is q/(q-1)!, and the mean kernel integrates to Gamma(q+1) zeta(q+1), giving q^2 zeta(q+1). The next-order O(t) relative mean estimate holds by integrability of the leading kernel derivative and the lower-order coefficient terms; q=1 has no lower-order terms. For the Fourier check, on the band m in [1/(2t),1/t] the geometric parameters are bounded away from zero and one, each logarithmic modulus costs at least a constant times 1-cos(m theta), and a_m is of order t^(-(q-1)). For |theta|<=t this yields Gaussian decay; for t<=|theta|<=Mt the band Riemann sum has a uniformly positive mean, and above Mt the geometric-sum bound O(1/|theta|) is smaller than a fixed fraction of the band length for large fixed M. The Lyapunov bound follows from the geometric third centered absolute moment bounded by a constant times e^(-mt)/(1-e^(-mt))^3 before multiplying by m^3; summing gives O(t^(-(q+3))), which is o(sigma_t^3). Normalized central inversion and the tail bounds then give the asserted local limit at integral mean. The additional factor |1-exp(i h theta)|<=h|theta| in the difference gives O(sigma_t^-2) absolute error, hence o(t) relative error. Undoing the exponential tilt gives the stated leading fixed-shift ratio with the negative sign. The EF strategy pairs fresh components by truncated profile and has enough unused copies and leaves for r moves. A union bound over the finite canonical set gives the fixed-sentence rate, and the colour-1 singleton deletion with shift one proves sharpness. The finite checker was inspected, not run; it tests only finite coefficients, deletion, and coarse scaling, not the asymptotics or EF argument.

## originality

FAIL

The quantitative input, including the exact constant, is mechanically implied by Bridges–Brindle–Bringmann–Franke, arXiv:2303.11864v1 (2023), Theorem 1.4 and (1.11). The specialized FO rate is a routine fixed-profile saturation consequence of that stronger input. This is demonstrated broader coverage, not a verdict based on inaccessible material or the older qualitative law alone.

## value

FAIL

Sharp convergence in this natural measure is a well-motivated question. But the asserted speed and exact obstruction are obtained by inserting a positive polynomial weight into an existing stronger theorem, taking a fixed-shift ratio and applying the standard finite-profile saturation argument. The record does not identify an independent structural obstacle, a new bound beyond that implication, or a distinct regime. A direct specialization proof is useful exposition but does not rescue the stated contribution under the scientific value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
