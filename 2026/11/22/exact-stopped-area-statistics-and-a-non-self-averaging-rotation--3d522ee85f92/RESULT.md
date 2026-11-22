# Exact stopped-area statistics and a non-self-averaging rotation estimate at circular escape

## Finding
For a planar diffusion with rigid rotation, the stochastic signed area accumulated before first exit from a circle has an exact Bessel-transform law and, when its random radial exposure is not observed, produces an unbiased angular-speed estimate with a strictly nonzero large-domain noise floor. Recording a single additional radial occupation integral is sufficient for the full stopped-trajectory likelihood.

Let \(\tau\) be the first exit from a circle of radius \(R\), let \(\mathcal A\) be the signed Stratonovich area, and let \(Q\) be accumulated squared radius, as defined below. With \(q=t+Dk^2/4-i\omega k/2\), the entire joint transform is
\[
\mathbb E_s e^{ik\mathcal A-tQ}
=\frac{I_0(\tfrac{s^2}{2}\sqrt{q/D})}{I_0(\tfrac{R^2}{2}\sqrt{q/D})},\quad k\in\mathbb R,\ t\ge0.
\]
Here \(I_0\) is the modified Bessel function (the ratio is extended continuously at \(q=0\)). Define the area-only estimator \(\widehat\omega_A=2\mathcal A/\mathbb E_sQ\). Its exact precision relative to the full stopped-path Fisher-information bound is
\[
\boxed{\operatorname{Var}_s(\widehat\omega_A)\,\mathcal I_{\rm full}
=1+\frac{\omega^2(R^4+s^4)}{64D^2},\qquad
\mathcal I_{\rm full}=\frac{R^4-s^4}{32D^2}.}
\]
In particular, for fixed \(s,D,\omega\ne0\), the area-only estimator has the nonzero variance limit \(\omega^2/2\) as \(R\to\infty\), while the estimator \(\widehat\omega_{A,Q}=2\mathcal A/Q\) based on the two statistics converges in probability to \(\omega\). The latter statement does not claim exact finite-sample efficiency.

## Assumptions and scope
Let \(D>0\), \(\omega\in\mathbb R\), \(R>0\), and \(0\le s<R\). On the plane let
\[
 dZ_t=\omega JZ_t\,dt+\sqrt{2D}\,dW_t,
 \qquad J(x,y)=(-y,x),\qquad |Z_0|=s,
\]
with standard two-component Brownian motion and continuous observation up to \(\tau=\inf\{t\ge0:|Z_t|=R\}\). Put
\[
 Q=\int_0^\tau |Z_t|^2dt,\qquad
 \mathcal A=\tfrac12\int_0^\tau(X_t\circ dY_t-Y_t\circ dX_t).
\]
The Stratonovich and Itô integrals coincide here since the coordinate cross-quadratic variation vanishes. \(D,R,s\) are known; \(\omega\) is the unknown rotation parameter. The domain is absorbing, not reflecting. No confining radial potential or reset mechanism is assumed.

## Proof
**1. Radial independence and the area mixture.** The generator applied to a radial test function is \(D(\partial_{rr}+r^{-1}\partial_r)\), since the rotational drift is tangent to circles. Splitting the Brownian driver into radial and angular orthonormal components (with an arbitrary predictable orthonormal convention at the origin), Lévy's characterization gives independent radial and angular Brownian motions; the radial squared process and its first-exit time depend only on the radial driver. Direct substitution in the area integral yields
\[
 \mathcal A=\frac\omega2 Q+\sqrt{\frac D2}\int_0^\tau |Z_t|\,dB_t^{\rm ang}.
\]
Conditioning on the full radial history, the last integral is centered Gaussian with variance \(Q\). Thus \(\mathcal A\mid Q\sim N(\omega Q/2,DQ/2)\), and the radial law does not depend on \(\omega\). This also holds when \(s=0\), by the squared-radius construction.

**2. Exact radial transform.** For \(\Re q\ge0\), the Feynman–Kac function \(F_q(r)=\mathbb E_r e^{-qQ}\) is the unique bounded regular solution of
\[
 D(F_q''+r^{-1}F_q')=qr^2F_q,\qquad F_q(R)=1.
\]
The regular solution is \(I_0(\tfrac{r^2}{2}\sqrt{q/D})\), normalized by its value at \(R\). Conditioning the Gaussian mixture and taking \(q=t+Dk^2/4-i\omega k/2\) gives the stated joint transform. The solution is valid at \(q=0\) by analytic continuation. An independent radial Poisson-equation derivation avoids differentiating an unverified formal series.

**3. Exact radial exposure moments.** With \(u(r)=\mathbb E_r Q\) and \(v(r)=\mathbb E_r Q^2\), Dynkin's formula gives
\[
 D\Delta_ru=-r^2,\qquad D\Delta_rv=-2r^2u,\qquad u(R)=v(R)=0,
\]
where \(\Delta_rf=f''+f'/r\), with regularity at zero. Since \(\Delta_r r^m=m^2r^{m-2}\), these equations yield
\[
 u(s)=\frac{R^4-s^4}{16D},\qquad
 v(s)=\frac{3R^8-4R^4s^4+s^8}{512D^2},\qquad
 \operatorname{Var}_s(Q)=\frac{R^8-s^8}{512D^2}.
\]
The conditional normal law therefore gives \(\mathbb E_s\mathcal A=\omega u(s)/2\) and
\[
 \operatorname{Var}_s(\widehat\omega_A)
 =\frac{2D}{u(s)}+\omega^2\frac{\operatorname{Var}_s(Q)}{u(s)^2}
 =\frac{32D^2}{R^4-s^4}
  +\frac{\omega^2(R^4+s^4)}{2(R^4-s^4)}.
\]

**4. Full-path likelihood and information.** On the stopped canonical path, the likelihood relative to zero rotation follows from bounded-drift localization before disk exit (or directly from the conditional Gaussian radial/area decomposition):
\[
 \log\frac{d\mathbb P_\omega}{d\mathbb P_0}
 =\frac{\omega}{D}\mathcal A-\frac{\omega^2}{4D}Q.
\]
The log-likelihood depends on the stopped trajectory only through \((\mathcal A,Q)\), so this pair is sufficient for \(\omega\). Its score is \((\mathcal A-\omega Q/2)/D\), and conditional Gaussian variance gives the exact Fisher information \(\mathcal I_{\rm full}=u(s)/(2D)\). Multiplication by the previous variance gives the boxed identity. The positive excess term is a risk comparison for this specified unbiased area-only estimator, not an area-only optimality bound over all estimators.

**5. The large-domain contrast.** At fixed \(s,D\) and \(R\to\infty\), \(\operatorname{Var}(\widehat\omega_A)\to\omega^2/2\) for \(\omega\ne0\). The decomposition \(\widehat\omega_A=\omega Q/u(s)+2M/u(s)\), with \(\mathbb E M^2=Du(s)/2\), shows that the noise term vanishes in \(L^2\). Brownian scaling gives \(Q_R/(R^4/D)\) convergent in law to a strictly positive nondegenerate disk-exposure random variable, hence the area-only estimate has a nondegenerate limit. Conversely, \(\widehat\omega_{A,Q}-\omega=2M/Q\) is conditionally normal with variance \(2D/Q\). Scaling and strict positivity of the limiting exposure imply \(Q\to\infty\) in probability, so this error converges in probability to zero.

## Verification
The included standalone \(checker.py\) independently verifies the radial Poisson polynomials, the exact second-moment decomposition, and the algebraic Fisher-information/variance identity with 327 exact rational assertions, over multiple nonzero and zero starting radii and signed rotation parameters. A separate direct symbolic evaluation of the radial Bessel differential equation confirmed its Feynman–Kac solution. These computations are checks, not substitutes for the stochastic independence and likelihood proofs above. Run `python checker.py` using Python 3 with no external packages.

## Relationship to prior work
Wen and Thiffeault (2019) analyze winding under tangential point-vortex drift, including annular geometries; their drift is radial-dependent and their observable is winding rather than rigid-rotation stopped signed area or parameter-information loss. Boedihardjo, Diehl, Mezzarobba and Ni (first published 2020) study the full expected signature of planar Brownian paths stopped at a disk boundary, not rotation-rate estimation. Du Buisson, Mnyulwa and Touchette (first posted 2023) derive fixed-time stochastic-area large deviations for linear diffusions, including the irreversible gyrator, not the absorbing-disk stopping law and its radial-exposure mixture. The Gaussian likelihood and radial Dirichlet techniques are classical; novelty is claimed only for the evaluated joint stopped law and exact inference contrast, not for these individual methods.

## Limitations
This is a theorem for ideal continuously observed free diffusion with constant solid-body rotation stopped at the first absorbing circular boundary, with \(D\), starting radius and boundary radius known. It is not a result for finite sampling, localization noise, heterogeneous rotational profiles, traps, reflecting walls or arbitrary observation domains. The non-self-averaging conclusion concerns the explicitly defined unbiased area-only estimator; no minimax lower bound for all estimators based solely on the area is asserted. The sufficiency statement concerns the ideal stopped path. Independent expert validation and priority assessment have not been performed.

## References
1. H. Wen and J.-L. Thiffeault, *Winding of a Brownian particle around a point vortex*, Philosophical Transactions of the Royal Society A (first published 2019-09-30), https://doi.org/10.1098/rsta.2018.0347.
2. H. Boedihardjo, J. Diehl, M. Mezzarobba and H. Ni, *The expected signature of Brownian motion stopped on the boundary of a circle has finite radius of convergence*, Bulletin of the London Mathematical Society (first published 2020-10-28), https://doi.org/10.1112/blms.12420.
3. J. du Buisson, T. D. P. Mnyulwa and H. Touchette, *Large deviations of the stochastic area for linear diffusions* (first posted 2023-07-12), https://arxiv.org/abs/2307.06245.
