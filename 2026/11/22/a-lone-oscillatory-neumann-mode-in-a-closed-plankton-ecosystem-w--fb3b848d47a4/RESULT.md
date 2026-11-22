# A lone oscillatory Neumann mode in a closed plankton ecosystem with one diffusion contrast

## Finding

For the four-compartment closed nutrient–phytoplankton–zooplankton–detritus reaction–diffusion model, a strictly positive coexistence equilibrium can be stable within its fixed-total-biomass homogeneous state space, yet have **exactly one unstable nonconstant Neumann harmonic**, caused by a **nonreal conjugate eigenpair**, while the constant coefficient of every positive-wavenumber dispersion polynomial stays strictly positive. This occurs when only nutrient diffusion differs from the three identical other diffusion coefficients. A fully rational certificate establishes all infinitely many mode conclusions.

Specifically, on \(0\leq x\leq2\pi\), with homogeneous Neumann boundaries, use \(\nu=22\), \(g=2\), \(\lambda=\delta=1\), \(\alpha=2\), and diffusivities \((d_N,d_P,d_Z,d_D)=(20,1,1,1)\). At total biomass \(35/2\), the equilibrium \((N_*,P_*,Z_*,D_*)=(1,1,10,11/2)\) has stable spatially homogeneous perturbations preserving total biomass; the harmonic \(\cos(x)\) alone has two unstable temporal exponents, which form a nonreal conjugate pair. The harmonics \(\cos(nx/2)\), for every integer \(n=1\) and \(n\geq3\), have all temporal exponents in the open left half-plane. Further, the characteristic determinant of the linearized Fourier matrix is strictly positive at *every* positive continuous squared wavenumber.

## Assumptions and scope

Let \(N,P,Z,D\) be nonnegative densities of dissolved nutrient, phytoplankton, zooplankton and detritus. Consider the deterministic model

\[
\begin{aligned}
\partial_\tau N &= -\nu P\frac{N}{1+N}+\alpha D+d_N\partial_{xx}N,\\
\partial_\tau P &= \nu P\frac{N}{1+N}-gZ\frac{P}{1+P}-\lambda P+d_P\partial_{xx}P,\\
\partial_\tau Z &= gZ\frac{P}{1+P}-\delta Z+d_Z\partial_{xx}Z,\\
\partial_\tau D &= \lambda P+\delta Z-\alpha D+d_D\partial_{xx}D.
\end{aligned}
\]

The spatial domain is \([0,2\pi]\) with no-flux conditions at each endpoint. The total biomass \(\int_0^{2\pi}(N+P+Z+D)\,dx\) is conserved. For the particular rates given in the finding, substitution shows that \((1,1,10,11/2)\) is a positive constant equilibrium. Its density sum is \(35/2\). Stability statements here concern the **spectrum of the linearization**; for the constant harmonic only, the invariant fixed-total-biomass tangent space is used to remove the conservation eigenvalue. No claim is made about nonlinear patterns, periodic solutions, or the viability of the chosen rates for a particular field ecosystem.

## Proof

**1. Exact reaction Jacobian and dispersion polynomial.** Differentiating the reaction vector field at the stated equilibrium gives

\[
J=\begin{pmatrix}
-11/2&-11&0&2\\
11/2&5&-1&0\\
0&5&0&0\\
0&1&1&-2
\end{pmatrix}.
\]

On the Neumann eigenfunction \(\cos(nx/2)\), \(n\geq0\), put \(q=n^2/4\). The associated real matrix is \(M(q)=J-q\operatorname{diag}(20,1,1,1)\). Direct exact expansion of \(\det(sI-M(q))\) yields \(s^4+b_3s^3+b_2s^2+b_1s+b_0\), where

\[
\begin{aligned}
b_3(q)&=(46q+5)/2,\\
b_2(q)&=3(42q^2-33q+26)/2,\\
b_1(q)&=(122q^3-213q^2-34q+185)/2,\\
b_0(q)&=q(40q^3-109q^2-112q+565)/2.
\end{aligned}
\]

For \(q>0\), \(b_0(q)>0\): the cubic in its parenthesis has discriminant \(-5523716316<0\), hence exactly one real root, which must be negative since the cubic has positive value at zero and positive leading coefficient. This establishes that the common diagnostic \(b_0<0\) never detects the instability, not merely that it fails at the unstable discrete mode.

**2. Constant harmonic.** At \(q=0\), the characteristic polynomial factors as

\[
\det(sI-J)=s\bigl(s^3+(5/2)s^2+39s+185/2\bigr).
\]

The zero root is the conserved-total-mass direction. The cubic is Hurwitz: its three positive coefficients satisfy \((5/2)\cdot39>185/2\), the strict cubic Routh–Hurwitz inequality. Thus all eigenvalues tangent to the fixed-total-biomass homogeneous state space have negative real parts.

**3. Exact quartic Routh–Hurwitz diagnostics.** Define

\[
\begin{aligned}
H_2(q)&=b_3(q)b_2(q)-b_1(q),\\
H_3(q)&=b_3(q)b_2(q)b_1(q)-b_1(q)^2-b_3(q)^2b_0(q).
\end{aligned}
\]

An exact expansion gives

\[
H_2(q)=\frac{5552q^3-3498q^2+3161q+20}{4}
\]

and

\[
H_3(q)=\frac{148176q^6-349272q^5+307020q^4-166524q^3-253991q^2+142495q+925}{2}.
\]

The first nonconstant Neumann harmonic has \(q=1/4\), where

\[
(b_3,b_2,b_1,b_0,H_2,H_3)
=(33/4,489/16,5283/64,8493/128,5427/32,4855491/512),
\]

all strictly positive. The quartic Routh–Hurwitz criterion therefore makes this harmonic strictly stable.

The next harmonic has \(q=1\), where

\[
(b_3,b_2,b_1,b_0,H_2,H_3)
=(51/2,105/2,30,192,5235/4,-171171/2).
\]

The first column of the quartic Routh array has signs \((+,+,+,-,+)\): there are exactly two eigenvalues in the open right half-plane. Every polynomial coefficient is strictly positive, so there can be no nonnegative real root. Thus those unstable eigenvalues form a nonreal conjugate pair. No eigenvalue lies on the imaginary axis because \(H_3\neq0\) and all Routh leading pivots are nonzero.

**4. The infinite high-harmonic tail.** Every \(n\geq3\) has \(q\geq9/4\). Set \(q=9/4+u\), \(u\geq0\). In each of the six polynomials \(b_3,b_2,b_1,b_0,H_2,H_3\), *all coefficients in the shifted variable* \(u\) are strictly positive. This is an exact integer/rational coefficient identity, independently checked by the supplied script. Therefore all six quantities are strictly positive at every \(q\geq9/4\). The quartic Hurwitz criterion proves strict stability for the entire infinite tail of Neumann harmonics. In particular, the sole unstable spatial harmonic is \(n=2\), and its instability is oscillatory.

## Verification

Run `python verify_npzd.py` with Python 3 and SymPy installed. The script reconstructs the nonlinear equilibrium residual, Jacobian and complete characteristic coefficients from the original reactions; verifies all printed coefficient identities, the cubic discriminant, the three exact mode tables and sign tests; and *symbolically* verifies strictly positive coefficients after the substitution \(q=9/4+u\) for all six Routh polynomials. This last finite algebraic certificate proves positivity for the full infinite high-mode range: it is not an inference from sampling finitely many harmonics.

## Relationship to prior work

Xu, Campbell and Poulin (2026) formulate this exact conservative NPZD reaction–diffusion model, derive its general linearization and exhibit diffusion-induced instabilities; their main explicit sufficient diagnostic uses a negative dispersion constant term with strongly separated diffusion scales. This finding adds an exact example in the same ecological model where *that determinant is positive at every positive wavenumber*, only nutrient diffusion differs, and precisely one admissible harmonic is unstable through a complex eigenpair. Thus neither the previously derived general Jacobian nor the authors' negative-determinant examples state the particular spectral separation certified here. Earlier NPZD Hopf-bifurcation work concerns a different reaction formulation and/or homogeneous dynamics, not the stated isolated diffusion-driven mode. General conditions for wave instabilities in \(n\)-component reaction–diffusion systems are known (Villar-Sepúlveda and Champneys, 2023), and similar isolated oscillatory modes have been demonstrated in other ecological systems. The present result does not claim wave instability as a new mechanism; its claim is the exact model-specific, single-harmonic certificate with positive determinant on the full continuum.

## Limitations

This is one exact, strictly feasible parameter instance and a linear spectral classification. It does not claim the absence of nonlinear competing attractors, existence of spatially periodic orbits, robustness for arbitrary ecosystem parameters, or empirical calibration of the diffusion ratio. Published general dispersion formulas make such claims decidable in principle, and some relevant priority literature may be unindexed; no claim of comprehensive historical uniqueness is made. The neutral homogeneous eigenvalue comes from a conserved quantity and is not counted as instability.

## References

1. X. Xu, S. A. Campbell and F. J. Poulin, *Turing Instability of a Closed Nutrient-Phytoplankton-Zooplankton-Detritus Model*, arXiv:2611.10221v1 (publicly posted November 6, 2026), https://arxiv.org/html/2611.10221v1.
2. J. C. Macdonald and H. Gulbudak, *Forward hysteresis and Hopf bifurcation in an NPZD model with application to harmful algal blooms*, arXiv:2307.06234 (2023), https://arxiv.org/abs/2307.06234.
3. E. Villar-Sepúlveda and A. R. Champneys, *General conditions for Turing and wave instabilities in reaction–diffusion systems*, Journal of Mathematical Biology **86**, 39 (2023), https://pmc.ncbi.nlm.nih.gov/articles/PMC9884266/.
