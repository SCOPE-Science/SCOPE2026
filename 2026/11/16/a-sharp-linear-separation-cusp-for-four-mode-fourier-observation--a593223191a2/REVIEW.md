# Independent mathematical audit

## correctness

PASS

Normalized Haar integration yields the exact four-by-four Toeplitz Gram coefficients b0=2α/π, b1=A x, b2=A cosα(2x²-1), b3=A(4cos²α-1)(4x³-3x)/3, with x=cos(θ/2), A=2sinα/π. Reversal symmetry gives two two-by-two blocks. At antipodal x=0 the smallest eigenvalue m-B has multiplicity two and lower eigenspace (u,v,u,v). Exact polynomial expansion of the averaged shifted determinants is -(4/3)A²sin²α x⁴, so for x>0 at least one shifted eigenvalue is negative. The positive eigenvalue is ≤4A, yielding the stated explicit quartic global deficit. At x=0 the two simple lower block eigenvalues have slopes ±2A sin²α in x, so the combined least eigenvalue has cusp 2sin³α/π·(π-θ)+Oα((π-θ)²). The 2α≤θ≤π and 0<α<π/2 domains were observed. Independent symbolic determinant simplification held exactly; the previous four-mode checker additionally verifies independent quadrature. No finite sampling substitutes for the algebraic proof.

## originality

PASS

Carefully separated PRIOR implications: the three-mode antipodal maximin theorem already gives the four-mode optimum AND a stronger quadratic-in-cos(θ/2) global deficit via principal-submatrix interlacing, so the displayed weaker quartic global bound is also a corollary and must NOT be treated as original in isolation. However three-mode simple-eigenvalue stability has a quadratic (not linear) separation loss. The genuinely additional final component is the four-mode lower eigenspace of dimension two and its nonzero sharp one-sided LINEAR cusp coefficient. It is not implied by the prior three-mode lower bound, which offers no local upper bound on four-mode deficit. Best-of-knowledge this structural cusp is new; the original package overstates novelty of its global bound, a bibliographic interpretation risk not a false mathematical inequality.

## value

PASS

The *sharp linear cusp* resolves a genuinely structural stability question for four-mode observation: a two-dimensional optimal least-eigenvalue space splits into opposite first-order branches under arc displacement, unlike the smooth quadratic loss of the three-mode case. This exact local sensitivity matters for a natural finite-dimensional Fourier sensor-design problem. The weaker global quartic bound, though covered by earlier three-mode quantitative estimates, is not the basis for the value verdict.

The dated certificate retains the supplied scientific assessment, sources and limitations.
