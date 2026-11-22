# Logarithmic aliasing in positivity-preserving fractional heat steps

## Finding

A positive-resolvent approximation of a half-order discrete diffusion operator may satisfy a conservative monotonicity CFL restriction **at every mesh size** while producing two distinct, oppositely biased limiting damping factors on the Nyquist Fourier mode. The precise phenomenon is an aliasing effect of a fixed logarithmic sinc-quadrature spacing, not an instability of the diffusion update.

**Theorem.** For every even integer \(m\ge4\), let \(S_m\) be cyclic translation on \(\mathbb R^m\) and put
\[
 A_m=m^2(2I-S_m-S_m^{\mathsf T}),\qquad
 B_m=\frac8\pi\sum_{\ell=-m}^{m}e^{4\ell}A_m(A_m+e^{8\ell}I)^{-1},\qquad
 P_m=I-\frac{B_m}{4m}.
\]
Then \(P_m\) is an entrywise **strictly positive** row-stochastic matrix, and its step size \(\tau_m=1/(4m)\) satisfies the pure-diffusion sufficient maximum-principle restriction \(\tau_m\Lambda_{m,\mathrm{sinc}}^{1/2}<1/2\) used for the corresponding lumped linear finite-element operator, where
\[
 \Lambda_{m,\mathrm{sinc}}^{1/2}=\frac8\pi\sum_{\ell=-m}^{m}e^{4\ell}\frac{2m^2}{2m^2+e^{8\ell}}.
\]
The alternating vector \(v^{(m)}_j=(-1)^j\) is an eigenvector. Its exact fractional-heat forward-Euler multiplier would be \(1/2\), whereas the actual multiplier of \(P_m\) has the following two limits, along explicitly specified even mesh sizes:
\[
 \begin{aligned}
 m_j^+&=2\left\lfloor e^{4j}/4\right\rfloor,&
 \lim_{j\to\infty}\frac{\langle v^{(m_j^+)},P_{m_j^+}v^{(m_j^+)}\rangle}{\|v^{(m_j^+)}\|_2^2}
 &=1-\tfrac12 R_+,\\
 m_j^-&=2\left\lfloor e^{4j+2}/4\right\rfloor,&
 \lim_{j\to\infty}\frac{\langle v^{(m_j^-)},P_{m_j^-}v^{(m_j^-)}\rangle}{\|v^{(m_j^-)}\|_2^2}
 &=1-\tfrac12 R_-,
 \end{aligned}
\]
where the *exact* constants are
\[
 R_+=1+2\sum_{n=1}^{\infty}\operatorname{sech}\!\left(\frac{\pi^2n}{4}\right)
 =1.3682294188823125\ldots,
 \quad
 R_-=1+2\sum_{n=1}^{\infty}(-1)^n\operatorname{sech}\!\left(\frac{\pi^2n}{4}\right)
 =0.6897194551640786\ldots.
\]
In particular \(R_-<1<R_+\), so the two limiting multipliers are respectively \(0.6551402724\ldots\) and \(0.3158852906\ldots\), on opposite sides of the correct multiplier \(1/2\). This discrepancy persists despite positivity and the published sufficient CFL restriction.

## Assumptions and scope

The grid represents the circle of physical length one, with \(m\) periodic equally spaced nodes and mass-lumped continuous linear finite elements. The stiffness-to-lumped-mass matrix is exactly \(A_m\). The sinc spacing is fixed at \(k=8\) and its two truncation indices equal \(m\); thus its truncation window grows with mesh refinement, but its logarithmic spacing is deliberately **not refined**. Only pure half-order diffusion without transport or source is considered. The base natural logarithm is used, and all exponentials and infinite series in the statement have their conventional real meanings.

## Proof

1. **Sinc multiplier.** For \(\lambda>0\), let
\[
 F_m(\lambda)=\frac8\pi\sum_{\ell=-m}^{m}e^{4\ell}\frac{\lambda}{\lambda+e^{8\ell}},
 \qquad x=\log\lambda.
\]
Each scalar summand increases strictly with \(\lambda\). Rewriting its numerator and denominator gives the exact identity
\[
 \frac{F_m(\lambda)}{\sqrt\lambda}
 =\frac4\pi\sum_{\ell=-m}^{m}\operatorname{sech}\!\left(\frac{8\ell-x}{2}\right).
\]
The corresponding untruncated positive sum \(R(x)\) is continuous and \(8\)-periodic. Applying Poisson summation to \(f(u)=\frac1{2\pi}\operatorname{sech}(u/2)\), whose Fourier transform is \(\widehat f(\omega)=\operatorname{sech}(\pi\omega)\), proves the absolutely convergent identity
\[
 R(x)=1+2\sum_{n=1}^{\infty}\operatorname{sech}\!\left(\frac{\pi^2n}{4}\right)
 \cos\!\left(\frac{\pi nx}{4}\right).
\]
The terms are positive and decrease strictly with \(n\), so \(R(0)>1\) and the strict alternating-series test gives \(R(4)<1\). Positivity of the defining real-space sum gives \(R(4)>0\). For \(a=\pi^2/4\), the bound \(\operatorname{sech}(an)\le 2e^{-an}\) gives
\[
 0<R(x)\le C_*:=1+\frac4{e^a-1}<\sqrt2<2.
\]
The last strict numerical-free comparison follows, for example, from \(\pi>3.14\) and the positive Taylor lower bound for the exponential.

2. **Markov property and CFL.** For every \(t>0\), \((A_m+tI)^{-1}\) has strictly positive entries (irreducible symmetric \(M\)-matrix). Since
\[
 A_m(A_m+tI)^{-1}=I-t(A_m+tI)^{-1},
\]
all off-diagonal entries of \(B_m\) are strictly negative. Also \(B_m\mathbf1=0\). The largest eigenvalue of \(A_m\) is \(4m^2\), hence monotonicity of \(F_m\) yields
\[
 0\le(B_m)_{ii}\le\|B_m\|_2=F_m(4m^2)
 \le2m C_*<4m.
\]
Thus every entry of \(P_m\) is strictly positive and each row sums to one. The nodal stiffness/mass diagonal is \(\Lambda_m=2m^2\). The sinc CFL contribution in the stated pure-diffusion criterion is \(F_m(2m^2)\), so
\[
 \tau_m\Lambda_{m,\mathrm{sinc}}^{1/2}
 \le\frac{\sqrt2}{4}C_*<\frac12.
\]
This is the sufficient restriction from the cited finite-element maximum-principle construction; the proof of entrywise positivity above does not require that result.

3. **Distinct mesh subsequences.** The Nyquist vector has \(A_mv^{(m)}=4m^2v^{(m)}\). Consequently
\[
 P_mv^{(m)}=\left(1-\tfrac12r_m\right)v^{(m)},\quad
 r_m=\frac{F_m(4m^2)}{2m},\quad x_m=\log(4m^2).
\]
The difference \(0\le R(x_m)-r_m\) is bounded by
\[
 \frac8\pi\frac{e^{-[8(m+1)-x_m]/2}+e^{-[8(m+1)+x_m]/2}}{1-e^{-4}},
\]
which tends to zero because \(x_m=O(\log m)\). Explicitly \(m_j^+=e^{4j}/2+O(1)\) and \(m_j^-=e^{4j+2}/2+O(1)\), so \(x_{m_j^+}=8j+o(1)\) and \(x_{m_j^-}=8j+4+o(1)\). Periodicity and continuity of \(R\) yield \(r_{m_j^+}\to R(0)=R_+\) and \(r_{m_j^-}\to R(4)=R_-\). Finally \(A_m^{1/2}v^{(m)}=2m v^{(m)}\), giving the exact target step multiplier \(1-\tau_m2m=1/2\). This proves all claims.

## Verification

Run `python checker.py` with `mpmath` installed. The checker independently evaluates the shifted real-space sinc sum and its Fourier series, reconstructs several small-cycle update matrices from all Fourier eigenvalues, checks positive weights and row sums, bounds quadrature truncation, and tests the two explicit mesh subsequences. Its successful execution prints `VERIFY_OK 98 checks` and the constants stated above. These finite computations are corroboration, not a substitute for the general analytic proof.

## Relationship to prior work

The resolvent-based half-order sinc representation and conservative positivity CFL are taken from Bonito, Guermond and Nazarov [1], especially their Sections 2.2--2.3 and 3.3--3.4. Bonito, Lei and Pasciak [2] and Bonito and Pasciak [3] provide prior exponential sinc-quadrature error bounds and systematic treatment of truncation. Those bounds prescribe refining the quadrature spacing for convergence and do not, in their inspected claims or error analyses, identify these two opposite-signed Nyquist subsequential limits **within positive CFL-admissible heat steps**. The Poisson-summation identity is standard mathematical machinery; the claimed contribution is its exact combination with a mesh-dependent monotone fractional-heat update and explicit phase-locked subsequences, not an invention of sinc quadrature or Fourier sampling.

## Limitations

This is a sharply specified mesh-scale spectral benchmark, not a failure claim about the fully coupled high-order method in [1]. Its quadrature spacing is deliberately fixed at eight, unlike the refined spacing required by convergent sinc algorithms. It concerns the Nyquist vector, which is not a fixed smooth initial datum under mesh refinement; it does not establish inconsistency for fixed smooth data when quadrature parameters are appropriately refined. The proof gives no error bounds for nonlinear fluxes, unstructured meshes, other fractional orders or incomplete resolvent solves. A traditional independent review and a global historical priority determination have not been performed.

## References

[1] A. Bonito, J.-L. Guermond, M. Nazarov, *Maximum principle preserving approximation of scalar conservation equations with a fractional Laplacian*, arXiv:2611.20833v1, publicly posted 2026-11-16, https://arxiv.org/html/2611.20833v1.

[2] A. Bonito, W. Lei, J. E. Pasciak, *On Sinc Quadrature Approximations of Fractional Powers of Regularly Accretive Operators*, arXiv:1709.06619, https://arxiv.org/pdf/1709.06619.

[3] A. Bonito, J. E. Pasciak, *Numerical Approximation of Fractional Powers of Regularly Accretive Operators*, arXiv:1508.05869, https://arxiv.org/pdf/1508.05869.
