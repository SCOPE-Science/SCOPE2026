# Positive Fourier quadrature survives symmetric pair collision with a sharp singular-value law

## Finding

The interpolatory trigonometric quadrature associated with an odd periodic grid stays **strictly positive even when one adjacent pair is symmetrically brought all the way to collision**, although the associated Fourier interpolation matrix becomes singular. More precisely, for every odd integer \(N=2m+1\ge3\) and every \(0\le\alpha\le1/2\), the quadrature weights specified below are positive, sum to one, and integrate exactly every trigonometric polynomial of degree at most \(m\). For \(0\le\alpha<1/2\) they are the unique such weights. At \(\alpha=1/2\), the two coincident observations combine into one positive weight on the resulting \(N-1\) distinct nodes.

With normalized Fourier evaluation matrix \(F_\alpha\), its unique least singular value obeys, for fixed odd \(N\),
\[
\sigma_{\min}(F_\alpha)
 = \frac{2\pi\cos(\pi/(2N))}{N^2\sin^2(\pi/(2N))}\,(1/2-\alpha)
 +O_N((1/2-\alpha)^2)\quad(\alpha\uparrow1/2).
\]
The exact coefficient tends to \(8/\pi\) as \(N\to\infty\). Consequently integration of bounded sample data has optimal operator norm exactly one throughout this family, while recovering all Fourier coefficients loses stability at the collision.

## Assumptions and scope

Let \(N=2m+1\) be an odd integer with \(m\ge1\) and \(h=2\pi/N\). On the periodic circle \(\mathbb R/(2\pi\mathbb Z)\), define
\[
x_0=\alpha h,\qquad x_1=(1-\alpha)h,\qquad x_j=jh\quad(2\le j\le N-1),\qquad 0\le\alpha\le\tfrac12.
\]
Define \(\mathcal T_m=\{\sum_{k=-m}^{m}c_ke^{ikx}:c_k\in\mathbb C\}\), normalized integration \(I(f)=(2\pi)^{-1}\int_0^{2\pi}f(x)\,dx\), and the Dirichlet kernel
\[
D_m(t)=\sum_{k=-m}^m e^{ikt}=\frac{\sin(Nt/2)}{\sin(t/2)}
\]
with continuous values at removable singularities. Let
\[
A_\alpha=D_m(\alpha h)+D_m((1-\alpha)h),\qquad
w_0=w_1=A_\alpha^{-1},
\]
\[
w_j=\frac1N\left(1-\frac{D_m((j-\alpha)h)+D_m((j-1+\alpha)h)}{A_\alpha}\right),\quad 2\le j\le N-1.
\]
The number \(A_\alpha\) is strictly positive (indeed positive already for \(0\le\alpha\le1/2\)). For \(\alpha=0\), the formulas reduce to equal weights \(1/N\). For \(\alpha=1/2\), \(x_0=x_1=h/2\); although the indexed observations coincide, their combined weight is well-defined. We make no claim about arbitrary perturbations of all grid nodes, and the singular-value asymptotic is fixed-\(N\), not uniform in joint limits.

## Proof

**1. Exactness and uniqueness before collision.** Write \(u_j=jh\) for the uniform grid and use the finite Fourier identity
\[
\frac1N\sum_{k=-m}^m e^{ik(u_j-u_l)}=\delta_{jl},\qquad 0\le j,l\le N-1.
\]
For a prospective symmetric weight \(w_0=w_1=w\), the difference between the two shifted-node contributions and their original uniform-grid contributions has Fourier coefficients
\[
B_k=w(e^{ikx_0}+e^{ikx_1})-\frac1N(1+e^{iku_1}),\qquad -m\le k\le m.
\]
The inverse uniform discrete Fourier transform says that the needed corrections \(\Delta_j=w_j-1/N\) at the *unmoved* sites \(j\ge2\) are
\[
\Delta_j=-\frac{w}{N}\{D_m(u_j-x_0)+D_m(u_j-x_1)\},\qquad j\ge2,
\]
and the corrections at original indices \(0,1\) vanish exactly when
\(w A_\alpha=1\). Thus the displayed weights satisfy
\[
\sum_{j=0}^{N-1} w_j e^{ikx_j}=\begin{cases}1&k=0,\\0&0<|k|\le m,\end{cases}
\]
which is precisely exactness on \(\mathcal T_m\). For \(\alpha<1/2\) the \(N\) sites are distinct, so the square Laurent-Vandermonde matrix has full rank, proving uniqueness of all quadrature weights. Reflection around \(h/2\) preserves the set and the integration functional and interchanges the two moved points, justifying their common weight. Exactness continues by continuity to \(\alpha=1/2\). At that endpoint the remaining \(N-1\) distinct evaluation functionals are linearly independent; the merged weight is uniquely determined, whereas the separate labeled weights can be split arbitrarily while retaining their sum.

**2. Strict positivity through the collision.** For \(0<\alpha\le1/2\), the Dirichlet-kernel sine identity gives
\[
A_\alpha=\sin(\pi\alpha)
\left[\csc\frac{\pi\alpha}{N}+\csc\frac{\pi(1-\alpha)}N\right]>0
\]
and, for \(2\le j\le N-1\),
\[
\frac{D_m((j-\alpha)h)+D_m((j-1+\alpha)h)}{A_\alpha}
=(-1)^{j-1}
\frac{\csc(\pi(j-\alpha)/N)+\csc(\pi(j-1+\alpha)/N)}
{\csc(\pi\alpha/N)+\csc(\pi(1-\alpha)/N)}.
\]
Every sine argument appearing here is strictly between zero and \(\pi\). If \(j\) is even, the ratio is negative and \(w_j>1/N\). If \(j\) is odd (necessarily \(3\le j\le N-2\)), the circular distances of \(j-\alpha\) and \(j-1+\alpha\) from the nearest endpoint of \((0,N)\) are strictly larger, respectively, than \(\alpha\) and \(1-\alpha\). Sine is strictly increasing with distance from these endpoints on their first half-interval, so each numerator cosecant is strictly smaller than the corresponding denominator cosecant. The ratio lies strictly between zero and one; hence \(0<w_j<1/N\). The first two weights are positive because \(A_\alpha>0\). The case \(\alpha=0\) is the positive uniform trapezoidal rule. In particular, at the collision
\[
w_0=w_1=\tfrac12\sin(\pi/(2N)),\quad
w_j=\frac1N\left(1-(-1)^{j-1}\frac{\sin(\pi/(2N))}{\sin(\pi(j-1/2)/N)}\right)>0.
\]
As the constant polynomial is integrated exactly, \(\sum_jw_j=1\). Therefore \(\sup_{\|y\|_{\infty}\le1}|\sum_j w_jy_j|=\sum_jw_j=1\), the smallest possible norm of any constant-exact quadrature functional.

**3. Rank loss and sharp singular slope.** Let \(F_\alpha=(N^{-1/2}e^{ikx_j})_{0\le j<N,\,-m\le k\le m}\). The uniform matrix \(F_0\) is unitary. Set \(B_\alpha=F_\alpha F_0^*\); its \(j\)-th row is \(N^{-1}(D_m(x_j-u_l))_{0\le l<N}\). For \(j\ge2\) this is the \(j\)-th standard row. At \(\alpha=1/2\) the first two rows agree, and the other \(N-2\) standard rows together with the midpoint row are linearly independent (the midpoint row has a nonzero entry in column zero). Thus the rank is exactly \(N-1\); its normalized left and right null vectors both equal \(v=(e_0-e_1)/\sqrt2\).

Put \(\varepsilon=1/2-\alpha\). The \(2\)-by-\(2\) upper-left block of \(B_\alpha\) has entries \(q,s;s,q\) with
\[
q=N^{-1}D_m((1/2-\varepsilon)h),\qquad
s=N^{-1}D_m((1/2+\varepsilon)h).
\]
Consequently
\[
v^*B_\alpha v=q-s
=-\frac{2h}{N}D_m'(h/2)\,\varepsilon+O_N(\varepsilon^3),
\]
and
\[
D_m'(h/2)=-\frac{\cos(\pi/(2N))}{2\sin^2(\pi/(2N))}.
\]
For a differentiable square matrix with a *simple* zero singular value, standard orthogonal nullspace block reduction (or a one-dimensional Schur complement) gives the least singular value as \(|v^*B_\alpha v|+O_N(\varepsilon^2)\). Since multiplication by \(F_0^*\) preserves singular values, this proves the claimed coefficient and error. Finally \(\sin(\pi/(2N))\sim\pi/(2N)\), so the coefficient tends to \(8/\pi\).

## Verification

The standalone `check.py` uses numerical Fourier moments, exact formula evaluations and direct singular-value calculations. Running `python check.py` from a directory containing NumPy yields `PASS 1226 assertions: positivity, all Fourier moments, collision rank, sharp singular slope`. Tested odd sizes are \(3\) through \(63\), with nine displacements including the collision; additional singular slopes were tested at eight sizes. This finite consistency check is not a proof of the claims quantified over every odd integer: steps 1–3 supply the analytical proof.

## Relationship to prior work

Austin and Trefethen [1] establish convergence and general conditioning estimates for perturbed trigonometric interpolation and discuss collisions and confluent interpolation. Yu and Townsend [2], Section 4.1 and Theorem 4.1, explicitly exhibit large alternating multi-site perturbations that produce **negative quadrature weights at any prescribed positive jitter bound**; their Theorem 4.2 gives a general total-variation estimate below the one-quarter boundary. Those results do not imply the exact all-order strict positivity of this special *two-site symmetric* family, its perfectly bounded quadrature limit at collision, or its sharp singular-value slope. Thus the claim is a structural qualification, not a contradiction, of general perturbed-grid instability. Search-based and full-text comparison do not prove absolute historical priority; classical exact quadrature and Vandermonde update literature is a residual risk.

## Limitations

Only odd node counts \(N\ge3\), the indicated symmetric inward displacement of **exactly one adjacent pair**, and a fixed-degree Fourier basis are treated. The quadrature weights are unique only for strictly separated nodes; at collision uniqueness concerns the aggregated weight on distinct nodes. The singular-slope asymptotic is at fixed \(N\). It does not establish robustness of Fourier coefficient reconstruction, arbitrary noisy interpolation, arbitrary perturbation configurations, or historical novelty by independent audit.

## References

[1] A. P. Austin and L. N. Trefethen, *Trigonometric Interpolation and Quadrature in Perturbed Points*, arXiv:1612.04018 (first public December 13, 2016); SIAM Journal on Numerical Analysis 55 (2017), 2113–2122. Author-accessible full text: https://people.maths.ox.ac.uk/trefethen/perturbed.pdf .

[2] A. Yu and A. Townsend, *On the Stability of Unevenly Spaced Samples for Interpolation and Quadrature*, arXiv:2202.04722 (first public February 9, 2022), especially Section 4 and Theorems 4.1–4.2. Full public text: https://www.researchgate.net/publication/358519870_On_the_stability_of_unevenly_spaced_samples_for_interpolation_and_quadrature .
