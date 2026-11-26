# Independent mathematical audit

## correctness

PASS

With Haar measure dt/(2π), the m-th off-diagonal moment is 2 sin(ma) cos(mθ)/(mπ). Normalizing by h=2 sin(a)/π gives off-diagonals x=u, y=c(2u²−1), z=(4c²−1)(4u³−3u)/3, where c=cos(a) and 0≤u=cos(θ)≤c<1. Reversal splits cI±B into 2×2 blocks for B=(G−2aI/π)/h; each sum of determinants is −8(1−c²)u⁴/3. For u>0 each pair has an indefinite block and hence the two strict edge inequalities follow, including for touching arcs. The Gram is positive definite because vanishing on an arc forces the Fourier polynomial to vanish identically. At u=0 the edges are ±c, each double; compression of B′(0) to the respective lower and upper spaces has eigenvalues ±2(1−c²) and ±2c². This verifies the fixed-width cusp and, by the Taylor series for sin(2a), the 3/a² law. The ratio is for the Gram, or the square of the restriction-map condition number. Frozen CHECK.py and requirements.txt are supplemental replay paths; the symbolic proof, not grid sampling, establishes the global claim.

## originality

FAIL

The closest matching earlier four-mode record explicitly states the same optimal double spectrum, unique lower-edge optimum, and sharp lower-edge cusp after converting full separation to half-separation. It also gives both reversal blocks and the same determinant polynomial. Its polynomial is invariant under negation of all three off-diagonal moments, so that exact certificate applies immediately to (m+B)I−G as well as to G−(m−B)I (using the prior paper's scalar notation). This gives the upper-edge strictness by the very same negative determinant. In each displayed block the derivative at zero of the trace is ±(b₁′+b₃′)=±A(2−4c²); the prior lower slopes are ±2A(1−c²) with the same block signs, so subtraction gives the upper slopes ∓2Ac². The claimed upper cusp is therefore a direct readout of the prior blocks and perturbation calculation, and positivity gives the ratio comparison immediately. The fact that these upper-edge conclusions were not separately stated does not establish a distinct contribution.

## value

FAIL

The two-edge design question is natural, and the upper cusp may be useful to quote. However, after removing the prior double spectrum, lower-edge rigidity, and sharp lower cusp, what remains follows by a sign change of the same determinant test, subtraction of a block trace derivative, and a monotone ratio comparison. This is a routine extension of the specific earlier result rather than a new substantive spectral invariant or mechanism. No valuable distinct repair is supported.

The dated certificate retains the supplied scientific assessment, sources and limitations.
