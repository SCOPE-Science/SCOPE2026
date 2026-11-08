# Sharp Bessel-zero law for the SEP current–density resolvent

## Finding

The finite-time microscopic current–density equation for the symmetric simple exclusion process (SEP) has a **sharp, time-dependent analyticity boundary** in its natural scalar current-tilt parameter. It is controlled by the largest eigenvalue of a positive Bessel integral operator, and its long-time correction is determined by the first positive zero of the ordinary Bessel function \(J_1\).

For any fixed microscopic time \(t>0\), define the integral operator \(A_t:L^2(0,t)\to L^2(0,t)\) by
\[
(A_t f)(u)=\int_0^t e^{-(u+v)}I_1(2\sqrt{uv})f(v)\,dv,
\]
where \(I_1\) is the order-one modified Bessel function. Write \(\Lambda(t)=\|A_t\|\). Then \(A_t\) is strictly positive, compact and self-adjoint; its top eigenvalue \(\Lambda(t)\) is simple, satisfies \(0<\Lambda(t)<1\), and increases strictly with \(t\).

Consider the universal Poisson-transformed normalized current–density gradient \(\psi_t(T;\omega)\) from the exact microscopic SEP equation of Bénichou and Grabsch (2026), on \(0<T<t\):
\[
\psi_t(T;\omega)+\omega\int_0^t G(T\mid u)\psi_t(u;\omega)\,du
=\omega G(T\mid t),
\quad
G(T\mid u)=e^{-(T+u)}\sqrt{\frac{u}{T}}I_1(2\sqrt{Tu}).
\]
Here \(\omega\) is the scalar current-tilt parameter, rather than the exponential tilt itself. After multiplying by \(\sqrt T\), the solution is a resolvent of \(A_t\). Its Taylor expansion at \(\omega=0\), in \(L^2(0,t)\) after this multiplication, has **exact radius**
\[
R(t)=\frac{1}{\Lambda(t)}.
\]
The closest complex singularity is the simple pole \(\omega_*(t)=-R(t)<-1\); all other possible resolvent poles are real and strictly further from the origin. The leading pole has nonzero residue for the SEP right-hand side, not merely for a generic forcing.

Let \(j_{1,1}=3.831705970\ldots\) be the first positive zero of \(J_1\). The sharp asymptotics are
\[
\begin{aligned}
\Lambda(t)&=\frac{t^2}{2}-\frac{2t^3}{3}+O(t^4),&&t\downarrow0,\\
\Lambda(t)&=1-\frac{j_{1,1}^2}{4t}+o(t^{-1}),&&t\to\infty,\\
R(t)&=\frac{2}{t^2}+\frac{8}{3t}+O(1),&&t\downarrow0,\\
R(t)&=1+\frac{j_{1,1}^2}{4t}+o(t^{-1}),&&t\to\infty.
\end{aligned}
\]
In particular, the leading negative pole approaches the physical endpoint \(\omega=-1\) at the exact rate \(j_{1,1}^2/(4t)\). The coefficient is the ground-state eigenvalue of a killed critical-branching diffusion, **not** a lattice random-walk spectral gap.

## Assumptions and scope

The SEP is on the infinite integer lattice with symmetric unit-rate exchange across every nearest-neighbor bond and initially independent Bernoulli occupations at densities \(\rho_-\) for sites \(r\le0\) and \(\rho_+\) for \(r>0\). Its integrated current \(Q_t\) crosses bond \((0,1)\). The physical current bias \(\lambda\) enters the reduction solely through
\[
\omega=[1+\rho_-(e^\lambda-1)][1+\rho_+(e^{-\lambda}-1)]-1.
\]
The one-body equation and its normalization are taken from equations (3), (5), and (14)–(16) of Bénichou and Grabsch; their derivation is not claimed here. The theorem concerns the **universal transformed equation** with \(\omega\) analytically continued to the complex plane, and makes no assertion that all complex values correspond to physical bias. Time is in the original unit-jump-rate microscopic units. The validity is for every finite \(t>0\); the two expansions refer to the indicated limiting regimes.

## Proof

**1. Exact self-adjoint reduction.** The source kernel is
\[
G(T\mid u)=\sqrt{\frac{u}{T}}e^{-(T+u)}I_1(2\sqrt{Tu}).
\]
Set \(\phi_t(T;\omega)=\sqrt T\,\psi_t(T;\omega)\). Multiplying the source equation by \(\sqrt T\) gives
\[
(I+\omega A_t)\phi_t=\omega b_t,
\quad b_t(T)=\sqrt t\,e^{-(T+t)}I_1(2\sqrt{Tt}).
\]
Both \(A_t\) and \(b_t\) are well-defined on \(L^2(0,t)\), and \(b_t(T)>0\) for \(T\in(0,t)\).

**2. Positivity, top eigenvalue and the pole.** The power series for the modified Bessel function yields the **positive Gram expansion**
\[
e^{-(u+v)}I_1(2\sqrt{uv})
=\sum_{k=0}^{\infty}\frac{[e^{-u}u^{k+1/2}][e^{-v}v^{k+1/2}]}{k!(k+1)!}.
\]
On a finite interval this series converges in trace norm. Each summand is positive rank one. The monomials are complete, so the operator has trivial kernel and infinitely many strictly positive eigenvalues tending to zero. Its integral kernel is strictly positive for positive arguments, hence the top eigenvalue is simple and has an everywhere strictly positive eigenfunction (the elementary compact positive-kernel Perron argument). Since \(b_t\) is strictly positive, its top-eigenfunction projection is nonzero. The resolvent therefore has a genuine simple pole at \(-1/\Lambda(t)\), while the other poles lie at \(-1/\Lambda_j(t)\) with \(0<\Lambda_j(t)<\Lambda(t)\). Its Neumann series converges precisely for \(|\omega|<1/\Lambda(t)\).

To see \(\Lambda(t)<1\), recognize \(G(y\mid x)\,dy+e^{-x}\delta_0(dy)\) as the unit-time law of the critical Feller branching diffusion
\[
dX_s=\sqrt{2X_s}\,dB_s,\qquad X_s\ge0,
\]
absorbed at \(0\). Indeed its Laplace transform is
\[
\mathbb E_x e^{-qX_s}=\exp\left(-\frac{xq}{1+sq}\right),
\]
and the series for \(G\) verifies this at \(s=1\), including the atom. The backward Markov semigroup is self-adjoint in \(L^2((0,\infty),dx/x)\), since \(G(y\mid x)=(x/y)G(x\mid y)\). Its restriction to positions in \((0,t)\) at both ends is unitarily equivalent to \(A_t\). A trajectory started in \((0,t)\) has probability at most \(1-e^{-t}<1\) of remaining strictly positive after one step, so reversibility and the two-sided Schur test imply that the restricted operator has norm at most \(1-e^{-t}\). Extending a strictly positive Perron eigenfunction from \((0,t_1)\) to \((0,t_2)\), \(t_2>t_1\), and perturbing it positively on the added interval strictly improves the Rayleigh quotient; thus \(\Lambda(t)\) increases strictly.

**3. Short-time coefficient.** The \(k=0\) rank-one Gram term has eigenvalue
\[
\int_0^t u e^{-2u}\,du
=\frac{1-(1+2t)e^{-2t}}4
=\frac{t^2}{2}-\frac{2t^3}{3}+O(t^4).
\]
The positive remainder starts at \(k=1\) and has trace, and hence operator norm, \(O(t^4)\). Weyl's eigenvalue bound gives the stated expansion for \(\Lambda(t)\). Inverting gives the corresponding expansion for \(R(t)\).

**4. Long-time coefficient and sampled-to-continuous killing.** The branching diffusion has the exact scaling law \(X_{cs}/c\) under an initial state scaled by \(c\). Rescale the interval \((0,t)\) to \(D=(0,1)\) and put \(h=1/t\). The operator \(A_t\) is unitarily equivalent to \(Q_h=\mathbf1_D P_h\mathbf1_D\), where \(P_h\) is the Feller branching semigroup on the half-line in \(L^2(dx/x)\). It is a nonnegative self-adjoint contraction. Its powers \(Q_h^n\) count trajectories whose positions at the \(n\) sampled instants remain in \(D\).

For a fixed \(s>0\), take \(n(h)=\lfloor s/h\rfloor\). Diffusion paths are continuous; any visit to the regular upper boundary \(1\) produces an immediate crossing outside \(D\) almost surely, while \(0\) is absorbing. Hence the sampled survival constraint converges almost surely to the continuously killed constraint. The positive integral kernels of \(Q_h^{n(h)}\) are bounded above by the unrestricted diffusion kernel at time \(n(h)h\). For times in a compact subset of \((0,\infty)\) this dominating kernel is Hilbert–Schmidt on \(D\) in the measure \(dx/x\): its kernel relative to that measure is proportional to \(\sqrt{xy}e^{-(x+y)/s}I_1(2\sqrt{xy}/s)\), which is \(O(xy)\) at the origin. Dominated convergence for diffusion bridges therefore gives **Hilbert–Schmidt and operator-norm convergence**
\[
Q_h^{n(h)}\longrightarrow P_s^D,
\]
where \(P_s^D\) is the continuously killed semigroup. Since \(Q_h\) is nonnegative self-adjoint, \(\|Q_h^{n(h)}\|=\Lambda(t)^{n(h)}\).

The continuously killed generator is \(\mathcal L f=x f''\) with Dirichlet conditions at \(0\) and \(1\), in \(L^2((0,1),dx/x)\). Its ground-state eigenfunction solves \(x f''=-\beta f\); the square-integrable regular solution is \(f(x)=\sqrt{x}J_1(2\sqrt{\beta x})\). The upper Dirichlet condition gives \(\beta=j_{1,1}^2/4\); Sturm oscillation identifies this as the smallest eigenvalue of \(-\mathcal L_D\), so \(\|P_s^D\|=e^{-s\beta}\). Taking norms in the preceding limit gives
\[
\Lambda(t)^{\lfloor st\rfloor}\longrightarrow e^{-s\beta}.
\]
Because \(\lfloor st\rfloor/t\to s\), the logarithm yields \(t[-\log\Lambda(t)]\to\beta\), and hence \(\Lambda(t)=1-\beta/t+o(t^{-1})\). Inversion completes the proof.

## Verification

The standalone `verify_spectral.py` reproduces the modified-Bessel positive Gram expansion, tests the exact branching-semigroup Laplace composition, independently builds the symmetric Nyström matrix using scaled modified Bessel functions, checks the small-time expansion and strict eigenvalue ordering on a finite deterministic sample, and compares the large-time spectral gap with \(j_{1,1}^2/4=3.670492660530974\ldots\). It passed 89 deterministic assertions using Python with NumPy, SciPy, and SymPy. The analytical semigroup and spectral argument above, rather than any finite quadrature, proves the all-time asymptotics and uniqueness of the pole. Run with `python verify_spectral.py` in the same directory.

## Relationship to prior work

Bénichou and Grabsch (2026) establish the microscopic SEP-to-one-body reduction, including the Poisson kernel \(G\), the universal equation and finite-time profile formulas. Those results are **premises**, not new contributions here. Their displayed equations (14)–(22) concern the propagator, a persistence interpretation, determinant representations and the finite-time correction to a hydrodynamic profile; they do not state the sharp spectral radius, its nearest complex resolvent pole, or the Bessel-zero finite-time correction to that pole.

Derrida and Gerschenfeld (2009) established the integrated-current generating function for step-initial SEP, without this current–density resolvent's spectral boundary. Mallick, Moriya and Sasamoto (2022) solved the macroscopic current fluctuation theory, which does not provide the microscopic-time pole \(\omega_*(t)\). General Bessel spectral and branching theory supplies mathematical techniques, but the coupling of the SEP one-body kernel to a **sampled-killing eigenvalue** and the exact two time-regime convergence-radius law is the specific contribution. The parent paper's appendices could not be fully inspected in the available retrieval session; independent priority review remains appropriate.

## Limitations

The radius is in the scalar \(\omega\)-plane of the universal normalized-gradient resolvent, **not** automatically in the physical exponential tilt \(\lambda\)-plane. The leading singularity lies outside the physically allowed real interval \(\omega>-1\), and is obtained by analytic continuation. The claim concerns the infinite-lattice SEP with step Bernoulli data and unit nearest-neighbor exchange rates, not finite periodic systems or asymmetric exclusion. No explicit finite-time elementary formula for \(\Lambda(t)\) is claimed; it is characterized variationally as the top eigenvalue of the stated explicit compact kernel. Numerical quadrature cannot certify the continuous-parameter theorem, and this work has not undergone an independent audit or publication-priority assessment.

## References

1. O. Bénichou and A. Grabsch, *Exact Microscopic One-Body Reduction in the Symmetric Exclusion Process*, arXiv:2610.18626v1 (first posted 2026-10-13), https://arxiv.org/abs/2610.18626 . In particular equations (3)–(5), (11)–(16), and (18)–(22).
2. B. Derrida and A. Gerschenfeld, *Current Fluctuations of the One Dimensional Symmetric Simple Exclusion Process with Step Initial Condition*, arXiv:0902.2364 (2009), https://arxiv.org/abs/0902.2364 .
3. K. Mallick, H. Moriya and T. Sasamoto, *Exact solution of the macroscopic fluctuation theory for the symmetric exclusion process*, arXiv:2202.05213 (2022), https://arxiv.org/abs/2202.05213 .
4. D. S. Grebenkov, *A physicist's guide to explicit summation formulas involving zeros of Bessel functions and related spectral sums*, arXiv:1904.11190 (2019/2021), https://arxiv.org/abs/1904.11190 .
5. NIST Digital Library of Mathematical Functions, §10.21, *Zeros of Bessel and Hankel Functions*, https://dlmf.nist.gov/10.21 .
