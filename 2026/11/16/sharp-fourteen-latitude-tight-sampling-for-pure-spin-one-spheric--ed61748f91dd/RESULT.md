# Sharp fourteen-latitude tight sampling for pure spin-one spherical harmonics of degree fourteen

## Finding
Let \(\mathcal H^{(1)}_{14}\) be the 29-dimensional space spanned by the usual orthonormal spin-weight-one spherical harmonics \({}_1Y_{14,m}\), \(-14\le m\le14\), with surface measure \(d\Omega=\sin\theta\,d\theta\,d\phi\). A **positive tight point-sampling rule** is a finite set of sites \((\theta_a,\phi_a)\) with weights \(w_a>0\), such that
\[
\sum_a w_a |f(\theta_a,\phi_a)|^2=\int_{S^2}|f|^2d\Omega\quad(f\in\mathcal H^{(1)}_{14}).
\]
Count distinct colatitudes \(\theta_a\in[0,\pi]\), not sample count and not absolute latitude. The minimum is **exactly 14**. Indeed, fourteen colatitudes strictly between the poles, each with 29 equally spaced azimuths and suitable strictly positive equal azimuthal weights, give the identity. No rule with 13 or fewer distinct colatitudes can do so, even with arbitrary longitudes or weights.

## Assumptions and scope
The spin-weight is exactly one and the degree exactly 14; the inner product is the complete surface \(L^2\) inner product. Points at poles are allowed in the lower bound. This is not a statement about all degrees below 14 or the minimum *total* number of points. Let \(x=\cos\theta\in[-1,1]\), let \(P_j\) denote the ordinary Legendre polynomial with \(P_j(1)=1\), and let \(\mu=dx/2\). All moment and Gaunt formulas below are exactly normalized for \(\mu\).

## Proof
**1. One missing Legendre moment.** Up to a constant and a phase, \({}_1Y_{14,m}(\theta,\phi)=\sqrt{29/(4\pi)}\,e^{im\phi}d^{14}_{m,-1}(\theta)\). The Clebsch–Gordan product identity expands \(|d^{14}_{m,-1}(\arccos x)|^2\) in \(P_J(x)\), \(0\le J\le28\). Its degree-\(J\) coefficient is a nonzero scalar multiple of
\[
\begin{pmatrix}14&14&J\\-1&1&0\end{pmatrix}
\begin{pmatrix}14&14&J\\m&-m&0\end{pmatrix}.
\]
The second Wigner array is orthogonal as \(J\) varies (the standard Clebsch–Gordan orthogonality). The first 29 coefficients vanish only for \(J=20\). This last finite exact assertion follows from the standard factorial formula, and is checked independently in the embedded script. (For even \(J\), it exhibits the familiar factor \(J(J+1)-2\cdot14\cdot15\); for odd \(J\), factorial evaluation gives nonzero values.) Hence the squared latitude profiles span **exactly** the codimension-one space of polynomials of degree at most 28 with zero \(P_{20}\)-coefficient.

**2. Reduction and lower bound.** For any tight point rule, group positive weights at the same \(x\). Taking the 29 diagonal Gram identities and using Step 1 gives a positive quadrature at those \(r\) nodes, exact for \(P_j\), \(0\le j\le28\), \(j\ne20\), against \(\mu\). Its moment functional on polynomials of degree \(\le28\) must therefore equal
\[
\mathcal L_t(p)=\frac12\int_{-1}^1 p(x)[1+tP_{20}(x)]\,dx
\]
for some real \(t\) (the signed auxiliary density is used only to define moments). Form the degree-14 moment matrix \(M_{14}(t)=(\mathcal L_t(P_iP_j))_{0\le i,j\le14}=D+tG\), where \(D_{ii}=1/(2i+1)\) and \(G_{ij}=\frac12\int P_iP_jP_{20}\). A measure on at most \(r\) nodes has \(\operatorname{rank}M_{14}\le r\). Since \(P_{20}\) is even, this matrix splits into even and odd blocks of sizes eight and seven. Their determinants, regarded as rational polynomials in \(t\), have respective degrees five and four, and their primitive numerator polynomials are squarefree and coprime. The exact rational verification is performed by the embedded `verify_spin_degree14.py` (Legendre triple-product factorial formula, rational determinants, polynomial gcd). Thus \(\det M_{14}(t)\) has only simple real or complex roots. Since \(M_{14}(t)\) is real symmetric, a nullity of at least two would give a repeated determinant root; consequently \(\operatorname{rank}M_{14}(t)\ge14\) for every real \(t\). Hence \(r\ge14\).

**3. Positive fourteen-node construction.** Let \(t_*\) be the unique determinant root in
\[
-\frac{19331}{5000}<t_*<-\frac{1933}{500}.
\]
Exact Sturm root counting checks that it is the closest negative determinant root to zero and is simple. Because \(M_{14}(0)=D\succ0\), continuity implies \(M_{14}(t_*)\succeq0\) with rank 14. Define the two localizing matrices, for indices \(0\le i,j\le13\),
\[
B_\pm(t)=\left(\mathcal L_t((1\pm x)P_iP_j)\right)_{0\le i,j\le13}.
\]
Every one of \(B_+(a),B_-(a),B_+(b),B_-(b)\) is strictly positive definite for \(a=-19331/5000\), \(b=-1933/500\), as verified by exact rational positive-pivot elimination in the checker. Each matrix is affine in \(t\), so \(B_\pm(t_*)\succ0\); also \(M_{13}(t_*)=(B_+(t_*)+B_-(t_*))/2\succ0\).

Let \(Q\) be the monic degree-14 polynomial spanning the kernel of \(M_{14}(t_*)\). On polynomials of degree at most 13, the positive form \(\mathcal L_{t_*}(fg)\) defines a real Hilbert inner product. Multiplication by \(x\) modulo \(Q\) gives a cyclic self-adjoint operator \(X\); the strict localizing forms imply \(-I\prec X\prec I\). Cyclicity forces 14 distinct eigenvalues \(x_1,\ldots,x_{14}\in(-1,1)\), each with a strictly positive spectral weight \(v_i\). The standard quotient-remainder argument using \(\mathcal L_{t_*}(Qp)=0\) for \(\deg p\le14\) proves
\[
\mathcal L_{t_*}(p)=\sum_{i=1}^{14}v_i p(x_i)
\quad(\deg p\le28).
\]
Therefore \(\sum_i v_iP_j(x_i)=\int P_jd\mu\) for every \(j\ne20\) through 28. Set \(\theta_i=\arccos x_i\); at each ring choose longitudes \(2\pi q/29\), \(0\le q<29\), with point weight \(4\pi v_i/29\). The 29th-root sum annihilates every nonzero azimuthal difference \(m-m'\) with \(|m-m'|\le28\), while the surviving diagonal integrals are exact by Step 1. Hence the Gram matrix of the 29 spin harmonics is exactly the identity, as claimed.

## Verification
Run `python verify_spin_degree14.py` with Python 3 and SymPy. It reconstructs the rational Gaunt matrices using the exact triple-Legendre factorial identity, verifies squarefreeness and coprimality of the two determinant polynomials, isolates the unique nearest negative simple root by exact real-root counts, and checks all four localizing endpoint matrices are positive definite via exact rational pivots. It additionally checks all 29 relevant Wigner \(3j\) symbols and finds precisely one zero at index 20. The checker prints `SPIN14_LATITUDE_CERTIFICATE_PASS`. All decisive computations use exact arithmetic; floating-point approximate nodes are not required for the proof. The spectral construction is an exact algebraic specification of the sites and weights.

## Relationship to prior work
Elahi–Khalid–Kennedy–McEwen (2018, arXiv:1809.01321) provide a sampling theorem for **all** spin-weighted degrees up to a bandlimit with optimally few total samples; their full text develops iso-latitude transforms but does not give the present fixed-degree positive tightness minimum. Pain (2020, arXiv:2011.05184), recalling much earlier work of Louck and Stein, reviews Pell-related nontrivial zeros of Wigner coefficients. The Wigner zero itself is known and is not asserted new here. The new assertion is that it permits a *sharp thirteen-versus-fourteen obstruction and fourteen-ring positive tight cubature*, supported by the exact truncated moment certificate.

## Limitations
This does not settle the least total number of samples, mixed harmonic degrees, arbitrary spin, robustness or conditioning. Novelty remains subject to equivalent positive quadrature constructions in the older cubature literature; an abstract-only older general cubature source is a residual historical-priority risk. Independent audit has not been performed.

## References
Elahi, U., Khalid, Z., Kennedy, R. A., and McEwen, J. D. (2018). *An Optimal-Dimensionality Sampling for Spin-s Functions on the Sphere*. arXiv:1809.01321, first public 5 September 2018; doi:10.1109/LSP.2018.2865676.

Pain, J.-C. (2020). *Some properties of Wigner 3j coefficients: non-trivial zeros and connections to hypergeometric functions*. arXiv:2011.05184, first public 10 November 2020; doi:10.1140/epja/s10050-020-00303-9. Includes historical discussion of Pell-linked zeros and the work of Louck and Stein.

Xu, Y. (1998). *Orthogonal Polynomials and Cubature Formulae on Spheres and on Balls*. SIAM J. Math. Anal., doi:10.1137/S0036141096307357 (general background; abstract inspected).
