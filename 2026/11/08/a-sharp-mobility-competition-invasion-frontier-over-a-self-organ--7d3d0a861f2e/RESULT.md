# A sharp mobility–competition invasion frontier over a self-organized nonlocal resident pattern

## Finding

For the symmetric, finite-range Lotka–Volterra competition system on the periodic habitat \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), a resident species can create an endogenous spatial pattern that permits a more strongly suppressed invader to grow when—and, on the invasion boundary, exactly when—the invader diffuses more slowly than the resident. The statement concerns **linear invasion at the resident-only equilibrium**, not established nonlinear coexistence.

More precisely, for sufficiently small real \(t\ne0\), there is a strictly positive, nonconstant resident profile \(U_t\), with resident diffusion \(D(t)>0\), such that
\[
U_t(x)=1+t\cos(3x)+t^2\left(\frac{1}{3\pi}+\frac18\cos(6x)\right)+O_{H^2}(t^3),
\]
\[
D(t)=\frac{2}{27\pi}+\frac{16-21\pi}{648\pi^2}\,t^2+O(t^4).
\]
The pattern is locally attracting among scalar resident profiles, modulo spatial translation. For each fixed \(t\ne0\) in this family and every invader diffusion \(d>0\), there is precisely one positive competition threshold \(a_c(d;t)\). The linearized invader grows for \(0<a<a_c(d;t)\), decays for \(a>a_c(d;t)\), and is spectrally neutral at equality. The map \(d\mapsto a_c(d;t)\) is smooth and strictly decreasing, with
\[
 a_c(D(t);t)=1,\qquad
\lim_{d\downarrow0}a_c(d;t)=\frac{1}{\min_x(KU_t)(x)}>1,
\qquad \lim_{d\to\infty}a_c(d;t)=\frac{1}{\langle U_t\rangle}<1.
\]
Consequently, for **every** \(0<d<D(t)\) there is a nonempty interval \(1<a<a_c(d;t)\) of competition strengths exceeding the conventional homogeneous exclusion value \(1\), yet admitting positive rare-invader growth. For \(d>D(t)\), the cutoff is below \(1\).

The exact leading quantitative cutoff, for each fixed \(d>0\), is
\[
 a_c(d;t)=1+\left(\frac{2}{81\pi^2d}-\frac{1}{3\pi}\right)t^2+O_d(t^4).
\]
At the resident diffusion the cutoff has exact derivative
\[
 \left.\frac{\partial a_c}{\partial d}\right|_{d=D(t)}
 =-\frac{\int_{\mathbb T}|U_t'(x)|^2\,dx}{\int_{\mathbb T}U_t(x)^2(KU_t)(x)\,dx}
 =-\frac92t^2+O(t^4).
\]

## Assumptions and scope

Let \(K\) be the normalized positive top-hat averaging operator
\[
 (Kf)(x)=\frac1\pi\int_{x-\pi/2}^{x+\pi/2}f(y)\,dy,
\]
interpreted periodically. Define \(\langle f\rangle=(2\pi)^{-1}\int_{\mathbb T}f\). Fix the same bounded interaction radius for all intraspecific and cross-species interactions, common intrinsic growth rates \(1\), and symmetric competition strength \(a>0\). The two densities solve
\[
 \partial_su=D\,\partial_{xx}u+u(1-Ku-aKv),\qquad
 \partial_sv=d\,\partial_{xx}v+v(1-Kv-aKu),
\]
with periodic boundary conditions and \(D,d>0\). The resident-only steady state is \((u,v)=(U_t,0)\), where \(U_t\) solves \(D(t)U_t''+U_t(1-KU_t)=0\). Only sufficiently small \(|t|>0\) is claimed. The expansions are uniform in \(x\) for the displayed functions; the \(O_d(t^4)\) coefficient is for fixed \(d>0\), **not** uniformly as \(d\downarrow0\). The word “invasion” means the sign of the principal growth exponent of the linearized rare species, not eventual coexistence or global dynamics.

## Proof

**1. First resident pattern.** The Fourier multiplier of the normalized top-hat kernel is \(\kappa_0=1\) and
\[
 \kappa_n=\frac{2\sin(n\pi/2)}{n\pi}\quad(n\ne0).
\]
At \(u=1\), the scalar resident linearization has eigenvalues \(\nu_n(D)=-Dn^2-\kappa_n\). The constant mode is \(-1\); even nonzero modes have negative eigenvalues; modes congruent to \(1\pmod4\) also do. For negative-multiplier modes \(n\equiv3\pmod4\), the crossing diffusivity is \(2/(\pi n^3)\), maximal at \(n=3\). Hence the first critical point is \(D_c=2/(27\pi)\). At \(D_c\), precisely modes \(n=\pm3\) are neutral and all others are strictly damped, with a spectral gap. This is a statement about **every integer Fourier mode**, not a finite Fourier experiment.

Write the even, phase-fixed branch as \(U=1+t\cos3x+t^2(A_0+A_6\cos6x)+O_{H^2}(t^3)\). The steady equation is
\[
 F(U,D)=D U''-K(U-1)-(U-1)K(U-1)=0.
\]
At quadratic order, direct Fourier comparison gives \(A_0=-\kappa_3/2=1/(3\pi)\) and \(A_6=1/8\). Lyapunov–Schmidt reduction, using invertibility of the complementary Fourier linearization, gives the cubic resonant coefficient
\[
 C=-A_0(1+\kappa_3)-\frac{\kappa_3A_6}{2}
   =\frac{16-21\pi}{72\pi^2}<0.
\]
Since the linear eigenvalue in the critical mode is \(-9(D-D_c)\), the stationary amplitude balance is \(0=-9(D-D_c)t+Ct^3+O(t^5)\). This yields the displayed \(D(t)=D_c+(C/9)t^2+O(t^4)\). The full equation is invariant under translations, and translation by \(\pi/3\) changes the sign of \(t\). The center-manifold dynamics in the complex critical amplitude has the negative cubic radial coefficient \(C\); therefore the nonzero small-amplitude branch is radially locally attracting, with one neutral translation direction and all other resident eigenvalues in the open left half-plane. The branch is positive because it converges uniformly to \(1\).

**2. The strict invasion boundary.** At \((U_t,0)\), the invader linearization decouples:
\[
 \partial_sv=\mathcal L_{d,a}v,\qquad
 \mathcal L_{d,a}=d\partial_{xx}+1-aW_t(x),\quad W_t=KU_t>0.
\]
For \(d>0\), the periodic elliptic operator is self-adjoint and its largest eigenvalue \(\lambda(d,a)\) is simple, with a strictly positive normalized eigenfunction \(\psi_{d,a}\). Its Rayleigh quotient is
\[
 \lambda(d,a)=\sup_{\phi\in H^1(\mathbb T)\setminus\{0\}}
 \frac{\int(1-aW_t)\phi^2-d\int|\phi'|^2}{\int\phi^2}.
\]
The strict derivative \(\partial_a\lambda=-\int W_t\psi_{d,a}^2<0\) follows from the Hellmann–Feynman identity, while \(\lambda(d,0)=1\) and \(\lambda(d,a)\to-\infty\) as \(a\to\infty\), since \(\min W_t>0\). This proves uniqueness and positivity of \(a_c(d;t)\). Moreover, \(W_t\) is nonconstant for \(t\ne0\), so the principal eigenfunction cannot be constant; thus \(\partial_d\lambda=-\int|\psi'|^2<0\). The implicit-function theorem implies that \(a_c(d;t)\) is smooth and strictly decreasing for all \(d>0\).

The resident equation gives \(\mathcal L_{D(t),1}U_t=0\). As \(U_t>0\), this zero eigenvalue is principal: \(a_c(D(t);t)=1\). Strict monotonicity immediately establishes the slower/faster invader dichotomy. By testing localized \(H^1\) bumps in the Rayleigh formula, the \(d\downarrow0\) principal eigenvalue tends to \(\max_x(1-aW_t(x))\); hence the first endpoint is the inverse of the minimum of \(W_t\). For \(d\to\infty\), Poincaré’s inequality forces normalized maximizers to converge to a constant, yielding \(\lambda(d,a)\to1-a\langle W_t\rangle\), and hence the second endpoint. Because \(\langle W_t\rangle=1+t^2/(3\pi)+O(t^4)>1\) and \(\min W_t=1-2|t|/(3\pi)+O(t^2)<1\), the endpoint inequalities follow.

**3. Exact small-pattern expansion of the boundary.** For fixed \(d>0\), write \(a_c(d;t)=1+c_dt^2+O_d(t^4)\). In the potential \(1-aW_t\), the first Fourier harmonic is \(-\kappa_3t\cos3x\) and the mean second-order term is \(-(c_d+A_0)t^2\). At \(t=0\) the principal eigenfunction is the constant mode. Standard second-order self-adjoint perturbation theory couples this mode only to \(n=\pm3\), and the two contributions total \(\kappa_3^2/(18d)\). The eigenvalue-zero condition therefore gives
\[
 c_d=\frac{\kappa_3^2}{18d}-A_0
   =\frac{2}{81\pi^2d}-\frac{1}{3\pi}.
\]
The branch at \(-t\) is a translate of the one at \(t\), so the simple principal eigenvalue, and hence \(a_c\), is even in \(t\), giving the stated fourth-order remainder.

Finally, implicit differentiation of \(\lambda(d,a_c(d;t))=0\) at \((d,a)=(D(t),1)\) gives the slope with \(\psi=U_t/\|U_t\|_2\). Multiplying the stationary resident equation by \(U_t\) and integrating provides \(\int U_t^2W_t=\int U_t^2-D(t)\int|U_t'|^2>0\); substitution of the expansion gives \(-9t^2/2+O(t^4)\).

## Verification

`verify.py` reconstructs the kernel Fourier symbols, the exact quadratic and cubic Lyapunov–Schmidt identities, the sign of \(C\), and the coefficient of the invader threshold using symbolic arithmetic. It prints `VERIFY_OK` when all asserted identities hold. The code also checks sample Fourier eigenvalues as a diagnostic; **the all-mode sign assertion is proved analytically in step 1**, and the eigenvalue monotonicity/limits in step 2 rely on the variational and elliptic arguments, not finite computation. Independent numerical spectral collocation at a moderate branch amplitude gave consistent, illustrative values: at \(t=0.2\), \(D\simeq0.0232680\), the threshold is about \(1.0038784\) for \(d=D/2\), exactly \(1\) at \(d=D\), and about \(0.9986164\) for \(d=3D/2\). These decimals are not substituted for the proof.

## Relationship to prior work

Simoy and Kuperman [1] introduce the finite-range, top-hat, periodic two-competitor equations with separate diffusion coefficients and numerically exhibit spatial structures and reversals of the local competition-exclusion picture. Their competitive experiments set both diffusion coefficients equal and do not derive this branch-specific, all-diffusivity principal-eigenvalue invasion frontier. Maciel and Martinez-Garcia [2] already derive analytical invasion conditions into patterned residents and demonstrate that nonlocal interactions can favor a weaker competitor. Their analytical patterned-resident invasion criteria set diffusion to zero and give pointwise inequalities; Section 3.3 also tests finite positive diffusion numerically and observes reduced coexistence. Neither component yields the present all-positive-invader-diffusion spectral threshold, its strict mobility monotonicity or its exact near-bifurcation coefficient. Thus **neither weaker-competitor invasion nor nonlocal-pattern creation is claimed to be new by itself**.

Kuehn and Tkachov [3] and Needham and collaborators [4] supply substantial prior scalar nonlocal Fisher–KPP pattern-bifurcation theory, so the scalar existence lemma alone is not being presented as an independent general discovery. Classical research on diffusion-dependent species competition [5] and on spatial heterogeneity [6] also precedes the present mechanism. The distinctive contribution is the explicit, endogenous, finite-radius top-hat resident branch **joined to** a sharp, smooth two-parameter diffusion/competition invasion threshold with its crossing and asymptotic coefficients. This assessment is best-knowledge only; equivalent unindexed results remain possible.

## Limitations

The result proves a **linearized rare-invader growth/decay criterion** and scalar resident local stability modulo translations. It does not imply that positive invaders ultimately coexist, establish nonlinear stability of two-species coexistence states, or classify arbitrary resident patterns. The exact expansion of \(a_c(d;t)\) is only for each fixed \(d>0\) as \(t\to0\), not for a uniform small-diffusion scaling. More general kernels, unsymmetrical competition coefficients, nonperiodic domains and stochastic populations are not covered. Previously published generic principal-eigenvalue methods and slow-diffuser arguments are explicitly antecedents. A full independent publication-priority audit has not been performed.

## References

[1] M. I. Simoy and M. N. Kuperman, *Non-local interaction effects in models of interacting populations*, arXiv:2209.09761v1 (first posted 2022-09-20), https://arxiv.org/html/2209.09761v1 ; later published in *Chaos, Solitons & Fractals* 167 (2023), 112993.

[2] G. A. Maciel and R. Martinez-Garcia, *Enhanced species coexistence in Lotka-Volterra competition models due to nonlocal interactions*, arXiv:2012.06249 (2020), https://arxiv.org/abs/2012.06249 ; *Journal of Theoretical Biology* 530 (2021), 110872.

[3] C. Kuehn and P. Tkachov, *Pattern formation in the doubly-nonlocal Fisher-KPP equation*, arXiv:1805.02116 (2018), https://arxiv.org/abs/1805.02116.

[4] D. J. Needham, J. Billingham, N. M. Ladas and J. C. Meyer, *The evolution problem for the 1D nonlocal Fisher-KPP equation with a top hat kernel. Part 1*, arXiv:2304.10922 (2023), https://arxiv.org/abs/2304.10922.

[5] S. Liu, Y. Lou and S. Ma, *Persistence, Nonlocal Competition and Evolution of Movement: The Role of Principal Eigenvalues*, *CSIAM Transactions on Life Sciences* 1 (2025), 67–92, https://doi.org/10.4208/csiam-ls.SO-2024-0005.

[6] P. Amarasekare and R. M. Nisbet, *Spatial Heterogeneity, Source–Sink Dynamics, and the Local Coexistence of Competing Species*, *The American Naturalist* 158 (2001), 572–584, https://doi.org/10.1086/323586.
