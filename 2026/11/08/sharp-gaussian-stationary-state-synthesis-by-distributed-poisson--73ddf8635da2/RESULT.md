# Sharp Gaussian stationary-state synthesis by distributed Poisson resetting

## Finding

**Theorem (complete Gaussian synthesis and sharp reset-frequency threshold).** Fix a dimension \(d\ge1\), a real symmetric positive-definite matrix \(K\), scalar diffusivity \(D>0\), and a desired nondegenerate Gaussian stationary density \(p=\mathcal N(m,\Sigma)\), where \(m\in\mathbb R^d\) and \(\Sigma\succ0\). Between resets the particle solves
\[
 dX_t=-KX_t\,dt+\sqrt{2D}\,dW_t.
\]
At independent Poisson times of rate \(r>0\), it is relocated to a fresh, independent sample from an arbitrary probability distribution \(\rho\) on \(\mathbb R^d\). Define
\[
 B=\tfrac12(K\Sigma+\Sigma K)-DI_d,\quad
 a=Km,\quad c=\operatorname{tr}K-D\operatorname{tr}(\Sigma^{-1}).
\]
There is **some** positive reset rate and probability reset distribution yielding exactly \(p\) as the stationary law **if and only if** \(B\succeq0\) and \(a\in\operatorname{ran}B\). When these conditions hold, set
\[
 r_*=c+\tfrac14a^\top B^\dagger a\ \ge0.
\]
For a **specified** rate \(r>0\), the target \(p\) is attainable if and only if \(r\ge r_*\). The resetting distribution is then unique, with the absolutely continuous density
\[
 \rho_r(x)=\frac{p(x)}r\left[r-c+a^\top v+v^\top Bv\right],\qquad v=\Sigma^{-1}(x-m).
\]
If \(r_*>0\), the minimal-rate resetting density factors into a positive quadratic form:
\[
 \rho_{r_*}(x)=\frac{p(x)}{r_*}
  (v+\tfrac12B^\dagger a)^\top B(v+\tfrac12B^\dagger a),
\]
and for every \(r>r_*\),
\[
 \rho_r=(1-r_*/r)p+(r_*/r)\rho_{r_*}.
\]
The unique zero-threshold case is \(B=0\) and \(m=0\), equivalently the unreset thermal Gaussian \(p=\mathcal N(0,DK^{-1})\); then every \(r>0\) is feasible and \(\rho_r=p\).

These conditions can be stricter than ordinary covariance domination. In two dimensions, take \(K=\operatorname{diag}(1,4)\), \(D=1\), and
\[
 \Sigma=\operatorname{diag}(1,1/4)+
 \begin{pmatrix}1&9/10\\9/10&1\end{pmatrix}.
\]
Although \(\Sigma-DK^{-1}\succ0\), the corresponding \(B\) has determinant \(-17/16\). Consequently **no finite reset rate and no reset-location probability law** can synthesize this centered Gaussian. The attainable covariance set is instead the matrix region \(K\Sigma+\Sigma K\succeq2DI_d\).

## Assumptions and scope

The Brownian motion is standard \(d\)-dimensional, reset times form an independent homogeneous Poisson process, and after each reset the position is resampled independently of all history from the same probability law. The potential and diffusivity are fixed and known. The reset law need not be Gaussian, smooth, or bounded a priori. The required stationary law is the complete joint Gaussian \(\mathcal N(m,\Sigma)\), not just matching its first two moments. All matrices are real; \(B^\dagger\) is the Moore--Penrose inverse; \(\operatorname{ran} B\) is its range. For \(r_*=0\) the minimal-rate formula is not used; the separate thermal case applies. The classification is exact for every finite \(d\) and every finite \(r>0\).

## Proof

**1. Stationarity implies a unique reset source.** The reset-free Fokker--Planck adjoint is
\[
 \mathcal L^* f=\nabla\cdot(Kxf)+D\Delta f.
\]
For stationary probability density \(p\), the reset generator imposes \(0=\mathcal L^*p-rp+r\rho\) as an equality of measures. Consequently the *only possible* resetting law is the signed measure \(\rho=p-r^{-1}\mathcal L^*p\). In particular, even allowing arbitrary singular reset laws cannot circumvent its pointwise density positivity.

**2. Evaluate the Gaussian adjoint without a commutativity assumption.** Put \(v=\Sigma^{-1}(x-m)\). Gaussian differentiation gives \(\nabla p=-pv\) and \(\Delta p/p=v^\top v-\operatorname{tr}\Sigma^{-1}\). Since \(x=m+\Sigma v\),
\[
 \frac{\mathcal L^*p}p
 =\operatorname{tr}K-(Km)^\top v-v^\top\tfrac12(K\Sigma+\Sigma K)v
   +D(v^\top v-\operatorname{tr}\Sigma^{-1})
 =c-a^\top v-v^\top Bv.
\]
The proposed formula for \(\rho_r\) follows. Integration by parts against the rapidly decreasing Gaussian gives \(\int\mathcal L^*p\,dx=0\), so \(\int\rho_r=1\) for all positive \(r\); feasibility is exactly nonnegativity of its bracket for every \(v\in\mathbb R^d\).

**3. Classify positivity of the quadratic source.** Write \(q_r(v)=r-c+a^\top v+v^\top Bv\). If \(B\) has a negative direction, \(q_r(tv)\to-\infty\). If \(B\succeq0\) but \(a\notin\operatorname{ran}B\), then the projection of \(a\) onto \(\ker B\) is nonzero and \(q_r\) is unbounded below on this kernel. If \(B\succeq0\) and \(a\in\operatorname{ran}B\), the exact completion of squares is
\[
 q_r(v)=r-r_*+(v+\tfrac12B^\dagger a)^\top B(v+\tfrac12B^\dagger a).
\]
It is everywhere nonnegative exactly when \(r\ge r_*\). Moreover
\[
 c=\operatorname{tr}(B\Sigma^{-1})\ge0
\]
with equality only when \(B=0\): use \(\operatorname{tr}(\Sigma^{-1/2}B\Sigma^{-1/2})\) and positive definiteness of \(\Sigma\). If also \(a\in\operatorname{ran}B\), the zero-threshold case forces \(B=0\), \(a=0\), hence \(m=0\); the Lyapunov equation \(K\Sigma+\Sigma K=2DI_d\) for positive-definite symmetric \(K\) has unique solution \(\Sigma=DK^{-1}\), seen in an eigenbasis of \(K\).

**4. Construct the stationary law and prove sufficiency.** If \(q_r\ge0\), the density \(\rho_r\) is nonnegative and normalized, hence a probability law. The no-reset Ornstein--Uhlenbeck semigroup is \(P_t\). By conditioning on the age of the last reset, the process has unique stationary probability
\[
 \pi_r=r\int_0^\infty e^{-rt}\,\rho_r P_t\,dt.
\]
Its generator equation is \((r-\mathcal L^*)\pi_r=r\rho_r\). The constructed Gaussian \(p\) satisfies that same equation by Step 1. Uniqueness follows either by the resolvent identity or by coupling two copies at their first common reset time: the total-variation distance decays at least as \(e^{-rt}\). Therefore \(\pi_r=p\). This proves both necessity and sufficiency for *arbitrary* reset probability measures, including the singular possibilities already ruled out by Step 1.

**5. Boundary factorization and increasing-rate family.** With \(r=r_*>0\), Step 3 gives the stated sum-of-squares reset density. Since \(\rho_r=p-r^{-1}\mathcal L^*p\), direct interpolation gives \(\rho_r=(1-r_*/r)p+(r_*/r)\rho_{r_*}\) for \(r>r_*\). This also shows that, unless the Gaussian is the unreset equilibrium, the stationary observation \(p\) alone does not identify the event rate: distinct rates above the threshold require different resetting laws but yield the same Gaussian.

**6. Exact examples and anisotropic obstruction.** For \(K=\operatorname{diag}(1,4)\), \(D=1\), \(\Sigma=\operatorname{diag}(2,1/2)\), \(m=(1,0)^\top\), direct calculation gives \(B=I_2\), \(a=(1,0)^\top\), \(c=5/2\), and \(r_*=11/4\). The minimum source is \(\rho_{11/4}(x)=\frac4{11}p(x)[(v_1+1/2)^2+v_2^2]\), so equality at the rate threshold is achieved by a valid non-Gaussian resetting law. A genuinely noncommuting feasible covariance \(\Sigma=\left(\begin{smallmatrix}2&1/4\\1/4&5/4\end{smallmatrix}\right)\), with \(m=(1,1/2)^\top\), instead gives \(B=\left(\begin{smallmatrix}1&5/8\\5/8&4\end{smallmatrix}\right)\succ0\) and \(r_*=85/21\). Finally, for the covariance in the Finding, \(\Sigma-DK^{-1}=\left(\begin{smallmatrix}1&9/10\\9/10&1\end{smallmatrix}\right)\succ0\) but \(B=\left(\begin{smallmatrix}1&9/4\\9/4&4\end{smallmatrix}\right)\) has determinant \(-17/16\). Step 3 thus rules out *every* rate, completing the claimed strict anisotropic obstruction.

## Verification

Run `python verify_gaussian_reset.py` with SymPy 1.12 or later. The checker uses exact rational algebra: it verifies the complete quadratic factorization, normalizations, 55 stationary-generator polynomial identities (monomials of total degree at most nine) for a noncentral two-dimensional example, characteristic-function consistency, two noncommuting covariance matrices, the rational threshold \(85/21\), and the indefinite Lyapunov defect determinant \(-17/16\). Its observed output is `PASS: 55 exact polynomial stationarity identities; threshold 11/4; noncommuting threshold 85/21; indefinite defect -17/16.` The universal statement for every dimension and every rate is established by the proof, not by a finite check.

## Relationship to prior work

Olsen (2023), *Steady-state moments under resetting to a distribution*, studies the **forward** relationship between an arbitrary resetting distribution and stationary moments, including one-dimensional harmonic drift and Gaussian-reset examples; its renewal equation and reset master equation are prerequisites, not new results here. The present theorem instead fixes the **desired complete Gaussian steady state**, allows *arbitrary* resetting laws, and derives the sharp all-dimensional feasibility criterion, rate threshold and unique reset-source density. Trajanovski et al. (2023) examine Ornstein--Uhlenbeck resetting to a fixed point and extensions on a comb; their stationary-state calculations do not classify reset-source synthesis of prescribed multivariate Gaussians. General resetting and stationary resolvents appear earlier in Evans--Majumdar and in Rose et al.; no claim of novelty is made for those identities. The new claim is the matrix-semidefinite feasibility and noncentral minimal-rate classification together with the strict noncommutative obstruction. An unindexed inverse-design theorem with stronger generality could imply this claim; literature searches do not rule out that priority risk.

## Limitations

The result assumes symmetric strictly confining linear drift and isotropic thermal noise; it does not classify nonsymmetric drift, state-dependent resetting rate, partial resets, nonlinear confinement, or statistical estimation from noisy samples. The rate is an exact mathematical parameter, not a physically optimized energy budget. Noncommutativity must be treated through the symmetrized Lyapunov defect; a covariance-only comparison with equilibrium is not sufficient. The theorem establishes no guarantee of novelty beyond the inspected literature; it is not independently certified.

## References

1. K. S. Olsen, *Steady-state moments under resetting to a distribution*, Physical Review E **108**, 044120 (2023), arXiv:2310.04840 (first publicly posted 2023-10-07). https://arxiv.org/abs/2310.04840 ; https://doi.org/10.1103/PhysRevE.108.044120 .
2. S. Trajanovski et al., *Ornstein--Uhlenbeck process and generalizations: Particle dynamics under comb constraints and stochastic resetting*, Physical Review E **107**, 054129 (2023), arXiv:2301.12304. https://arxiv.org/abs/2301.12304 .
3. M. R. Evans and S. N. Majumdar, *Diffusion with Stochastic Resetting*, Physical Review Letters **106**, 160601 (2011), arXiv:1102.2704. https://arxiv.org/abs/1102.2704 .
4. D. C. Rose, H. Touchette, I. Lesanovsky and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, Physical Review E **98**, 022129 (2018), https://doi.org/10.1103/PhysRevE.98.022129 .
