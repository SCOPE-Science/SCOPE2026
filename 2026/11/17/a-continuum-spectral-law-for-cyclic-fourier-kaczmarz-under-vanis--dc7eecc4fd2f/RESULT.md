# A continuum spectral law for cyclic Fourier Kaczmarz under vanishing one-atom bias

## Finding
For a fixed real parameter \(c>0\) and each integer \(m\ge2\), put \(\omega_m=e^{2\pi i/m}\) and form the probability measure
\[
\mu_{m,c}=\frac{1+c}{m+c}\,\delta_1+\frac1{m+c}\sum_{j=1}^{m-1}\delta_{\omega_m^j}.
\]
Let \(e_j(\zeta)=\zeta^j\), \(0\le j<m\), in \(H_{m,c}=L^2(\mu_{m,c})\). Apply sequential orthogonal-complement Kaczmarz error updates against \(e_0,e_1,\ldots,e_{m-1}\), a single complete cycle. In the coordinate basis of these exponentials, the cycle error matrix is exactly
\[
(Q_{m,c})_{ij}=r_m(1-r_m)^{i-j}\mathbf1_{j\le i}-r_m(1-r_m)^i,
\quad r_m=\frac{c}{m+c},\quad 0\le i,j<m.
\]
Define the isometric step-function embedding \(J_m:\mathbb C^m\to L^2[0,1]\) by \((J_mx)(s)=\sqrt m\,x_i\) for \(i/m\le s<(i+1)/m\). As \(m\to\infty\), the coordinate operators \(K_{m,c}=J_mQ_{m,c}J_m^*\) converge in Hilbert–Schmidt norm at the quantitative rate
\[
\boxed{\|K_{m,c}-T_c\|_{\mathcal S_2}=O_c(m^{-1/2})},
\]
where the compact integral operator is
\[
\boxed{(T_cf)(s)=c\int_0^s e^{-c(s-t)}f(t)\,dt-ce^{-cs}\int_0^1 f(t)\,dt.}
\]
This is also a **physical Hilbert-space** limit: if \(G_{m,c}\) is the Gram matrix of the exponential basis and \(D_{m,c}=J_mG_{m,c}^{1/2}Q_{m,c}G_{m,c}^{-1/2}J_m^*\), then
\[
\boxed{\|D_{m,c}-S_cT_cS_c^{-1}\|_{\mathcal S_2}=O_c(m^{-1/2})},\qquad
S_c=I+(\sqrt{1+c}-1)P,
\]
with \(Pf=\int_0^1f(t)dt\), identified with the constant function on \([0,1]\). Consequently every fixed-index singular value of the physical cycle operator converges to the corresponding singular value of \(S_cT_cS_c^{-1}\), with error \(O_c(m^{-1/2})\).

The nonzero eigenvalues of \(T_c\), all algebraically simple, are precisely
\[
\boxed{\lambda_k(c)=\frac{c}{W_k(ce^c)},\qquad k\in\mathbb Z\setminus\{0\},}
\]
where \(W_k\) denotes the \(k\)-th branch of the Lambert \(W\) function. Therefore the spectral radius of a complete finite Kaczmarz cycle has the exact limit
\[
\boxed{\lim_{m\to\infty}\rho(Q_{m,c})=\max_{k\ne0}\frac{c}{|W_k(ce^c)|}\in(0,1).}
\]
Nevertheless the total variation distance of \(\mu_{m,c}\) from the uniform measure on the same regular polygon equals \(c(m-1)/(m(m+c))\to0\). Thus a vanishing, single-atom weight perturbation of an exactly finite-recoverable Fourier system retains a nonzero limiting per-cycle spectral contraction factor, and its entire physical singular spectrum has a nontrivial continuum law.

## Assumptions and scope
The parameter \(c\) is positive and fixed while \(m\to\infty\). All spaces are complex Hilbert spaces with the usual probability-integral norm. The measurement order is \(e_0,e_1,\ldots,e_{m-1}\), and each update is the *unrelaxed orthogonal complement of the measurement line*. The operator \(Q_{m,c}\) acts on Fourier **coefficients**; the physical Gram-conjugate operator \(G_{m,c}^{1/2}Q_{m,c}G_{m,c}^{-1/2}\) acts in an orthonormal representation of the original Hilbert space. The extension of finite-dimensional operators by zero on the orthogonal complement of step functions is understood. No uniformity in \(c\), random ordering, noise stability, or simultaneous limit of the number of cycles is asserted.

## Proof
**Exact Gram reduction and sweep.** Orthogonality of distinct characters on the regular polygon and the extra mass at \(1\) give
\[
G_{m,c}=(1-r_m)I_m+r_m\mathbf1_m\mathbf1_m^*,\qquad r_m=\frac{c}{m+c}.
\]
All its eigenvalues are positive. A Kaczmarz error update against the \(i\)-th unit vector sends the coefficient of that basis vector to minus the off-diagonal Gram contribution while leaving all other coefficients unchanged. With \(L\) and \(U\) the strictly lower and upper all-ones matrices, the full sweep is Gauss–Seidel error propagation
\[
Q_{m,c}=-(I_m+r_mL)^{-1}r_mU.
\]
The lower-triangular inverse has entries \(1\) on the diagonal and \(-r_m(1-r_m)^{i-j-1}\) for \(i>j\). Summing its first \(j\) entries against \(U\) yields the displayed closed formula for each matrix entry. As the first \(m\) exponentials form a basis of \(H_{m,c}\), this matrix represents the entire one-cycle Hilbert error operator, not a restricted action.

**Quantitative continuum limit.** The kernel of \(J_mQ_{m,c}J_m^*\) on the product of cells \(i,j\) is \(m(Q_{m,c})_{ij}\). Since \(mr_m=c+O_c(m^{-1})\) and \(\log(1-r_m)=-c/m+O_c(m^{-2})\), on every pair of *different* cells the step kernel differs uniformly by \(O_c(m^{-1})\) from
\[
k_c(s,t)=ce^{-c(s-t)}\mathbf1_{t\le s}-ce^{-cs}.
\]
On the \(m\) diagonal cell squares, of total area \(1/m\), both kernels are bounded by constants depending on \(c\); this contributes \(O_c(m^{-1})\) to the squared Hilbert–Schmidt error. The off-diagonal squares contribute \(O_c(m^{-2})\). Hence the total error is \(O_c(m^{-1/2})\), exactly as claimed.

**Physical Hilbert norm.** Put \(P_m^{\mathrm{av}}=\mathbf1_m\mathbf1_m^*/m\). The positive square root is
\[
G_{m,c}^{1/2}=a_mI_m+(d_m-a_m)P_m^{\mathrm{av}},\qquad
a_m=\sqrt{1-r_m},\quad d_m=\sqrt{1+(m-1)r_m}.
\]
On \(L^2[0,1]\), let \(\widetilde S_m=a_mI+(d_m-a_m)P\). Because the constant function belongs to every step-function space, \(J_mG_{m,c}^{1/2}=\widetilde S_mJ_m\) and likewise for the inverse. Thus \(D_{m,c}=\widetilde S_mK_{m,c}\widetilde S_m^{-1}\). As \(a_m\to1\), \(d_m\to\sqrt{1+c}\), and all inverse norms stay bounded, \(\|\widetilde S_m-S_c\|=O_c(m^{-1})\); the ideal property of Hilbert–Schmidt operators completes the physical convergence estimate. The variational characterization of singular values implies the stated fixed-index error bound.

**Entire nonzero spectrum.** If \(T_cf=\lambda f\) with \(\lambda\ne0\), then \(T_cf\) is absolutely continuous and differentiation gives \((T_cf)'=cf-c(T_cf)\), so \(f(s)=Ae^{zs}\) with \(A\ne0\) and \(z=c(1-\lambda)/\lambda\). At \(s=0\), the defining integral gives \(\lambda=-c(e^z-1)/z\) if \(z\ne0\), and the limiting formula \(\lambda=-c\) if \(z=0\). But \(z=0\) forces \(\lambda=1\) from the differential equation and is therefore impossible for \(c>0\). Eliminating \(\lambda\) gives
\[
(z+c)e^z=c,\quad z\ne0.
\]
Writing \(w=z+c\) transforms this into \(we^w=ce^c\). The principal real solution \(w=c\) corresponds to the excluded \(z=0\); the other Lambert branches give all eigenvalues stated. Conversely, substitution of each nonzero root into the integral formula produces its exponential eigenfunction. The derivative of \((z+c)e^z-c\) does not vanish at any nonzero root: a multiple root would force \(z=-c-1\), at which the left-hand side is negative. Thus each nonzero eigenvalue is algebraically simple (the associated scalar resolvent boundary equation has a simple zero). Since \(T_c\) is compact, there are no additional nonzero spectral values.

For each nonprincipal Lambert value \(w\), \(|w|e^{\operatorname{Re}w}=ce^c\). If \(|w|\le c\), then \(\operatorname{Re}w\ge c\), whereas \(\operatorname{Re}w\le|w|\le c\); equality would imply \(w=c\), a contradiction. Therefore all nonzero eigenvalues have modulus strictly below one. The branches satisfy \(|W_k(ce^c)|\to\infty\) as \(|k|\to\infty\), so the positive spectral-radius maximum is attained and lies strictly below one. Hilbert–Schmidt convergence implies operator-norm convergence; by compact-operator spectral approximation, isolated nonzero eigenvalues converge with multiplicity and no spectral values can remain bounded away from the limiting spectrum. Therefore \(\rho(Q_{m,c})\to\rho(T_c)\).

**Vanishing perturbation.** At the distinguished atom, the excess above uniform mass is \(c(m-1)/(m(m+c))\), while every other atom has deficit \(c/(m(m+c))\). Half the total absolute discrepancy equals the displayed total variation distance. For the uniform measure, the Gram matrix is the identity and one Kaczmarz cycle has zero error. The limiting positive radius above is therefore a genuine singular stability effect, not a continuity statement for fixed finite dimension.

## Verification
Run `python3 verify.py` using NumPy and SciPy. The standalone checker compares the exact sweep formula with independent triangular solves for dimensions \(2\) to \(27\) over five positive parameters; checks decreasing step-kernel errors across four dimensions for four parameters; compares the leading nonzero eigenvalue to the Lambert expression; and tests the physical Gram-square-root similarity. It reports `PHYSICAL_CHECKS_PASSED 161`. These finite diagnostics are supplementary; the proofs of the infinite limits, completeness of the spectrum, and universal parameter quantifiers are analytic.

## Relationship to prior work
Berner, Herr and Jorgensen establish unconditional convergence for finite atomic stationary sequences (Theorem 4.1) and qualitative spectral-radius decay for a finite-atom compressed unitary (Lemma 5.7). A separate published result, *Regular-polygon finite-step rigidity and an explicit spectral rate for Fourier Kaczmarz recovery*, supplies a weighted root-derivative polynomial for the exact finite-dimensional exponential error rate and proves finite-step rigidity. Those facts already cover qualitative decay and finite-dimensional rate descriptions, and **are not presented as new**. The new claim concerns the critical dimension-dependent defect, the Hilbert–Schmidt continuum limit in both coefficient and physical Hilbert geometry, convergence of every physical singular value, the explicit Lambert-branch spectral limit, and the vanishing-total-variation discontinuity. The published *A fixed-sweep Gauss–Seidel residual illusion for rank-one Gram systems* treats fixed, nonvanishing coherence and a fixed-sweep residual/energy discrepancy; it does not provide the present weak-coherence limit or spectral classification.

## Limitations
The continuum scaling keeps \(c\) fixed and uses precisely one distinguished atomic mass and the given deterministic order. The coefficient operator and physical error operator are related by a nonunitary Gram similarity; their singular values must **not** be interchanged. Although the spectrum is explicit, no elementary closed form for all singular values of the limiting nonnormal integral operator is claimed. No claim of absolute publication priority is made: older texts on nonnormal Volterra rank-one perturbations, finite products of projections, or Gauss–Seidel continuum limits could contain equivalent formulations. Independent review remains outstanding.

## References
1. C. Berner, J. E. Herr, and P. E. T. Jorgensen, *Frame Properties of Effective Stationary Sequences*, arXiv:2611.03358v1 (first public 2026-11-02), https://arxiv.org/abs/2611.03358; particularly Theorem 4.1 and Lemma 5.7 in the available version 2.
2. *Regular-polygon finite-step rigidity and an explicit spectral rate for Fourier Kaczmarz recovery*, published November 8, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-regular-polygon-finite-step-rigidity-and-an-explicit-spectral-ra--03f0340e1b7f.
3. *A fixed-sweep Gauss–Seidel residual illusion for rank-one Gram systems*, published October 18, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-fixed-sweep-gauss-seidel-residual-illusion-for-rank-one-gram-s--65682c1c69b9.
4. W. Czaja and J. Tanis, *Kaczmarz Algorithm and Frames*, arXiv:1409.8310 (2014), https://arxiv.org/abs/1409.8310.
