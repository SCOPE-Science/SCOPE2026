# Sharp positivity thresholds for Crank–Nicolson heat steps on periodic tori

## Finding
For integers \(d\ge1\), \(n\ge3\), take the standard nearest-neighbor Laplacian \(L_{d,n}=\sum_{j=1}^d(2I-S_j-S_j^{-1})\) on the \(d\)-dimensional discrete periodic torus \((\mathbb Z/n\mathbb Z)^d\). In dimensionless heat step \(c=\kappa\Delta t/h^2\ge0\), the Crank–Nicolson end-step is
\[
C_{d,n}(c)=(I+\tfrac c2L_{d,n})^{-1}(I-\tfrac c2L_{d,n}).
\]
Let \(Y_n=1-\cos(2\pi K/n)\), where \(K\) is uniform over \(\{0,\ldots,n-1\}\), and let \(Y_n^{(1)},\ldots,Y_n^{(d)}\) be independent copies. Define
\[
\Phi_{d,n}(c)=\mathbb E\frac{1}{1+c\sum_{j=1}^dY_n^{(j)}}.
\]
There is a unique \(c_{d,n}>0\) with \(\Phi_{d,n}(c_{d,n})=1/2\). The **sharp all-data positivity threshold** is
\[
\boxed{C_{d,n}(c)\text{ is entrywise nonnegative}\quad\Longleftrightarrow\quad0\le c\le c_{d,n}.}
\]
Every off-diagonal coefficient is strictly positive when \(c>0\). At the threshold every diagonal coefficient is zero. The thresholds are **strictly decreasing separately in dimension and period**:
\[
\boxed{c_{d+1,n}<c_{d,n},\qquad c_{d,n+1}<c_{d,n}.}
\]
For each fixed \(d\), \(c_{d,n}\downarrow c_{d,\infty}>1/d\) as \(n\to\infty\); \(c_{d,\infty}\) is the unique root obtained by replacing each \(Y_n\) with \(1-\cos\Theta\), for uniform \(\Theta\in[0,2\pi]\). The strict lower bound \(c_{d,n}>1/d\) also holds for finite \(n\).

The one-dimensional thresholds include
\[
c_{1,3}=2,\qquad c_{1,4}=\frac{1+\sqrt5}{2},\qquad c_{1,\infty}=\frac32,
\]
and the sharp finite-period correction is
\[
\boxed{c_{1,n}-\tfrac32=8\cdot3^{-n}\bigl(1+O(n3^{-n})\bigr).}
\]
For the three-by-three two-dimensional torus,
\[
\boxed{c_{2,3}=\frac{1+\sqrt{57}}{14}.}
\]
On the infinite square lattice the root is explicitly determined by a complete elliptic integral:
\[
\Phi_{2,\infty}(c)=\frac{2}{\pi(1+2c)}K\left(\frac{2c}{1+2c}\right),
\quad c_{2,\infty}=0.5881972836856281148591\ldots,
\]
where \(K(k)=\int_0^{\pi/2}(1-k^2\sin^2\theta)^{-1/2}\,d\theta\) uses the **modulus** convention. In high dimension, uniformly for \(n\in\{3,4,\ldots\}\cup\{\infty\}\),
\[
\boxed{c_{d,n}=\frac1d+\frac{1}{4d^2}+O(d^{-3})\quad(d\to\infty).}
\]

## Assumptions and scope
All grids are periodic, unweighted, translation invariant, and have \(n\ge3\) sites in each coordinate; \(n=\infty\) denotes a limiting spectral distribution, not a finite matrix. The positivity test is on the final exact-arithmetic numerical matrix acting on all coordinatewise nonnegative vectors. \(c=\kappa\Delta t/h^2\) is a dimensionless diffusion step and the Laplacian has \(2d\) on the diagonal. No statement concerns internal stages, general boundaries, variable coefficients, or accuracy at large time steps. The big-O bound in the dimension law has an absolute constant independent of the side length.

## Proof
**1. Entrywise criterion and spectral return.** Put \(R=(I+\frac c2 L_{d,n})^{-1}\). Since \(L_{d,n}\) is a connected graph Laplacian, \(R\) is a strictly positive inverse \(M\)-matrix for \(c>0\). It fixes the constant vector, and
\[
C_{d,n}(c)=2R-I.
\]
Every off-diagonal entry is strictly positive; diagonal entries are identical by translation invariance. The discrete characters have Laplacian eigenvalues \(2\sum_{j=1}^d(1-\cos(2\pi k_j/n))\); taking the diagonal of the inverse Fourier transform gives \(R_{xx}=\Phi_{d,n}(c)\). The function \(\Phi\) is continuous and strictly decreasing, since the summed frequency variable is positive with positive probability, and varies from \(1\) to \(n^{-d}<1/2\). Thus its unique \(1/2\) crossing gives exactly the stated positivity interval.

**2. Two strict monotonicities.** Adding an independent nonnegative \(Y_n\) that is positive with nonzero probability decreases \(\Phi_{d,n}(c)\) strictly for every \(c>0\), proving the dimension ordering. For the period ordering, use the Laplace transform
\[
\Phi_{d,n}(c)=\int_0^\infty e^{-(1+dc)t}A_n(ct)^d\,dt,
\qquad A_n(z)=\frac1n\sum_{k=0}^{n-1}e^{z\cos(2\pi k/n)}.
\]
The absolutely convergent Fourier–Bessel expansion is
\[
A_n(z)=I_0(z)+2\sum_{\ell\ge1}I_{\ell n}(z).
\]
Here \(I_m(z)>0\) denotes the modified Bessel coefficient \(I_m(z)=\sum_{k\ge0}(z/2)^{2k+m}/[k!(k+m)!]\). For fixed \(z>0\), these coefficients **strictly decrease in integer order**. To verify this without invoking a monotonicity theorem, put \(r_m=I_{m+1}/I_m\); the standard recurrences derived by differentiating the displayed series give
\[
r_m'=1-r_m^2-\frac{2m+1}{z}r_m.
\]
At \(z\downarrow0\), \(r_m(z)\sim z/[2(m+1)]<1\). At any putative first upward crossing of \(r_m=1\), its derivative would equal \(-(2m+1)/z<0\), impossible. Hence \(I_{m+1}<I_m\) for every \(z>0\). Termwise, \(A_{n+1}(z)<A_n(z)\), and the Laplace integral yields \(\Phi_{d,n+1}(c)<\Phi_{d,n}(c)\). The strict threshold ordering follows. Trapezoidal Riemann sums for each fixed \(c\), together with monotone convergence of the roots, give the limiting continuous-angle distribution.

**3. Baseline and explicit low-dimensional thresholds.** For every \(n\ge3\), \(\mathbb EY_n=1\), \(\operatorname{Var}(Y_n)=1/2\), because the first two nontrivial root-of-unity sums vanish. The function \(x\mapsto(1+cx)^{-1}\) is strictly convex, so
\[
\Phi_{d,n}(1/d)>\frac{1}{1+(1/d)d}=\frac12.
\]
This also holds at infinite period and proves the lower baseline. In dimension one the infinite-resolvent recurrence and its positive root give
\[
\Phi_{1,n}(c)=\frac{1}{\sqrt{1+2c}}\frac{1+q(c)^n}{1-q(c)^n},\quad
q(c)=\frac{1+c-\sqrt{1+2c}}{c}\in(0,1).
\]
This formula can equivalently be verified by summing its periodized geometric Green kernel. At \(c=3/2\), \(q=1/3\), \(\Phi_{1,\infty}=1/2\) and \(\Phi'_{1,\infty}=-1/8\); the implicit-function expansion of the finite-period factor gives \(c_{1,n}-3/2=8\cdot3^{-n}(1+O(n3^{-n}))\). Substitution into the finite-frequency averages at \(n=3,4\) gives \(2\) and \((1+\sqrt5)/2\).

For \(d=2,n=3\) there are four nonzero one-coordinate frequencies and the independent frequency counts yield
\[
\Phi_{2,3}(c)=\frac19\left(1+\frac4{1+3c/2}+\frac4{1+3c}\right),\qquad
\Phi_{2,3}(c)-\frac12=-\frac{7c^2-c-2}{2(3c+1)(3c+2)}.
\]
The unique positive root gives the displayed radical. For the continuous two-dimensional torus, let \(a=1+2c\) and \(b=c\), so \(a>2b\). Expanding the angular integral in powers of \(b/a\) gives
\[
\begin{aligned}
\Phi_{2,\infty}(c)&=\frac1a\sum_{m\ge0}\frac{b^{2m}}{a^{2m}}\mathbb E(\cos\Theta_1+\cos\Theta_2)^{2m}\\
&=\frac1a\sum_{m\ge0}\binom{2m}{m}^{\!2}\left(\frac{b}{2a}\right)^{2m}
=\frac2{\pi a}K(2b/a).
\end{aligned}
\]
The middle equality follows by replacing the sum of cosines with \(2\cos U\cos V\) and applying Haar invariance of the integer torus map \((U,V)\mapsto(U+V,U-V)\), then using the standard central-binomial even cosine moment. The final equality is the binomial power series for \(K\). This derivation makes the modulus normalization explicit. Monotonicity gives the unique numeric root stated above.

**4. Uniform high-dimensional correction.** Write \(\bar Y_d=d^{-1}\sum_{j=1}^dY_n^{(j)}=1+Z_d\). Independently of \(n\ge3\) or \(n=\infty\), the bounded independent variables satisfy
\[
\mathbb EZ_d=0,\quad\mathbb EZ_d^2=\frac{1}{2d},\quad\mathbb EZ_d^3=O(d^{-2}),\quad\mathbb EZ_d^4=O(d^{-2}).
\]
For \(t\) in any fixed compact subinterval of \((0,\infty)\), expand \((1+t(1+Z_d))^{-1}\) about \(Z_d=0\) through cubic order, with fourth-order remainder bounded by a constant times \(\mathbb EZ_d^4\):
\[
\Phi_{d,n}(t/d)=\frac{1}{1+t}+\frac{t^2}{2d(1+t)^3}+O(d^{-2}).
\]
The error is uniform in \(n\). Concentration of \(\bar Y_d\) pins the unique root \(t_d=dc_{d,n}\) to \(1+o(1)\) uniformly; the displayed expansion and nonzero derivative at \(t=1\) sharpen it to \(t_d=1+(4d)^{-1}+O(d^{-2})\). Dividing by \(d\) proves the uniform asymptotic law.

## Verification
Run `python artifacts/verify.py` (Python standard library only). Its exact-rational tests independently form connected periodic Laplacian matrices, invert their resolvents by Gaussian elimination, check the all-entries positivity reduction, and verify the \(3\times3\) two-dimensional polynomial boundary. The program also tests finite Fourier sums, endpoint monotonicity for sample grids, dimension monotonicity in rational binomial spectral formulas, and the first two root-of-unity moments. It records 3,602 passing deterministic checks. The full all-\(d\), all-\(n\) theorem follows from the analytic proof above; finite tests are **not** treated as infinite certification. The displayed two-dimensional infinite-grid root was separately computed using the complete elliptic integral with 40-digit precision.

## Relationship to prior work
Higueras and Roldán (first public 2023) derive sharp positivity and maximum-norm contractivity bounds for the Crank–Nicolson heat equation with **homogeneous Dirichlet boundaries**, using Chebyshev-type matrix formulas. Faragó and Horváth develop general discrete maximum-principle criteria under Dirichlet conditions, and Faragó–Korotov–Szabó give exact one-dimensional and sufficient two-dimensional conditions for finite-difference and finite-element problems. These results motivate the new periodic-grid question but do not, in the inspected material, provide the strict two-parameter ordering, infinite-square elliptic threshold, or uniform high-dimensional law.

The already-published fixed-generator **resolvent-return criterion** establishes that \(C=2R-I\) is nonnegative exactly when all return diagonals of \(R\) exceed \(1/2\); the present first proof step is that known result specialized to the torus, **not** a new general Markov-chain positivity criterion. The existing one-dimensional **backward-Euler-filtered Crank–Nicolson** lattice result gives the 1D resolvent's geometric kernel; that kernel and filtered positivity mechanism are also prior work. What is assessed here is the combined multidimensional periodic-torus threshold classification, strict dependence on both torus dimensions, the elliptic and finite-torus constants, and the uniform dimension asymptotic. An unlocated specialist publication may still contain some of these refinements.

## Limitations
The sharp thresholds apply only to uniform isotropic nearest-neighbor periodic spatial differences, not Dirichlet boundaries, variable diffusion, nonuniform grids, anisotropic weights, unstructured meshes, or nonlinear positivity. The asymptotic expansion is a large-dimension statement; its remainder is not an explicit practical finite-d bound. The infinite-lattice quantities characterize limits of finite-grid thresholds, not a finite transition matrix. A further specialist prior-art comparison remains appropriate before publication, and no independent audit has been performed.

## References
1. I. Higueras and T. Roldán, *A new insight on positivity and contractivity of the Crank-Nicolson scheme for the heat equation*, arXiv:2301.01066 (first public 2023-01-03), https://arxiv.org/abs/2301.01066.
2. I. Faragó and R. Horváth, *Discrete Maximum Principle and Adequate Discretizations of Linear Parabolic Problems*, SIAM Journal on Scientific Computing, DOI 10.1137/050627241, https://doi.org/10.1137/050627241.
3. I. Faragó, S. Korotov and T. Szabó, *Non-negativity preservation of the discrete nonstationary heat equation in 1D and 2D* (2010), https://www.researchgate.net/publication/236611280_Non-negativity_preservation_of_the_discrete_nonstationary_heat_equation_in_1D_and_2D.
4. *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a.
5. *Unconditional lattice positivity from backward-Euler-filtered Crank–Nicolson* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-backward-euler-filtered-cn-lattice-positivity--1f6f56bd0eac.
