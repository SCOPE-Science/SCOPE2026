# Exact essential spectrum and a midpoint jump for symmetric two-atom generalized Hilbert matrices

## Finding
For \(0<t<1\), let \(A_t\) be the bounded operator on \(\ell^2(\mathbb N_0)\), identified with the coefficient Hardy space \(H^2(\mathbb D)\), with matrix
\[
 (A_t)_{n,k}=\binom{n+k}{k}\big[t^k(1-t)^n+(1-t)^k t^n\big],\qquad n,k\geq0.
\]
This is the generalized Hilbert operator for the symmetric two-point measure \(\delta_t+\delta_{1-t}\). It has strictly positive matrix entries and is self-adjoint. Its **entire spectrum equals its Fredholm essential spectrum** and is
\[
\boxed{\sigma(A_t)=\sigma_{\mathrm{ess}}(A_t)=
\begin{cases}
[-2/\sqrt{t(1-t)},\;2/\sqrt{t(1-t)}],&t\ne\tfrac12,\\
[0,4],&t=\tfrac12.
\end{cases}}
\]
The (already-known from the general positive-measure norm formula) exact norm is \(\|A_t\|=2/\sqrt{t(1-t)}\), and no nonzero vector attains it. For every \(t\ne1/2\), the entire negative band is essential spectrum despite strict positivity of every matrix entry. As \(t\to1/2\), the operators converge **strongly**, but not in operator norm, to \(A_{1/2}\); more precisely,
\[
\|A_t-A_{1/2}\|\geq\frac{2}{\sqrt{t(1-t)}}\quad(t\ne1/2).
\]
Thus the bottom of the spectrum jumps from the limiting value \(-4\) to \(0\) at the midpoint.

## Assumptions and scope
The parameter is any fixed real \(t\in(0,1)\). The space is the complex Hilbert space \(\ell^2(\mathbb N_0)\), or equivalently \(H^2(\mathbb D)\) with its coefficient norm. Essential spectrum means failure of Fredholm invertibility of the shifted bounded operator. Operator convergence is in the strong topology unless otherwise indicated. The symbol \(\delta_t\) denotes the unit point mass at \(t\), so at \(t=1/2\) the measure has total mass two (not one).

## Proof
**1. Weighted-composition representation.** For \(0<t<1\), define on \(H^2(\mathbb D)\)
\[
(T_tf)(z)=\frac{1}{1-(1-t)z}\,f\!\left(\frac{t}{1-(1-t)z}\right).
\]
By the negative-binomial generating series, its matrix in the monomial basis is
\(\bigl[\binom{n+k}{k}(1-t)^nt^k\bigr]_{n,k\geq0}\).
Its adjoint is \(T_t^*=T_{1-t}\) by transposition of the real matrix entries. Hence \(A_t=T_t+T_t^*\), a bounded self-adjoint operator with strictly positive entries. Boundedness also follows from the exact unitary model in Step 2.

**2. Exact unitary model.** Set \(u=(1-z)^{-1}-1/2\). This is a conformal map from the disk to the right half-plane. The standard Hardy-space Cayley isometry followed by the Paley–Wiener Laplace isometry gives a unitary \(\mathcal U:H^2(\mathbb D)\to L^2(0,\infty)\) characterized by
\[
 f(z)=\left(u+\tfrac12\right)\int_0^\infty e^{-ux}\,(\mathcal Uf)(x)\,dx,
 \qquad u=\frac1{1-z}-\frac12.
\]
Indeed the disk boundary normalized measure transforms to \((2\pi)^{-1}\) times boundary Lebesgue measure in the half-plane, while Plancherel proves the Laplace isometry (the normalization is fixed by \(f=1\), corresponding to \(g(x)=e^{-x/2}\) of unit norm). Write \(q=t/(1-t)\) and \(c=1/[2(1-t)]\). Substitution into \(T_t\) sends \(u\) to \(qu+c\) and multiplies the transformed half-plane function by \((1-t)^{-1}\). Changing Laplace variables therefore yields
\[
 (\mathcal UT_t\mathcal U^{-1}g)(x)=t^{-1}e^{-x/(2t)}g\!\left(\frac{1-t}{t}x\right).
\]
Let \(\mathcal L:L^2(0,\infty)\to L^2(\mathbb R)\) be the logarithmic isometry \((\mathcal Lg)(y)=e^{y/2}g(e^y)\). Put
\[
 L=\log\frac{1-t}{t},\qquad r=\frac1{\sqrt{t(1-t)}},\qquad w_t(y)=\exp\!\left(-\frac{e^y}{2t}\right).
\]
For translation \((U_Lh)(y)=h(y+L)\), direct substitution gives the exact identity
\[
\mathcal L\mathcal UT_t\mathcal U^{-1}\mathcal L^{-1}=rM_{w_t}U_L,
\]
and hence \(A_t\) is unitarily equivalent to
\[
B_t=r\big(M_{w_t}U_L+U_L^*M_{w_t}\big).
\]
The strictly positive function \(w_t\) is strictly less than \(1\) at every finite \(y\), tends to \(1\) at \(-\infty\), and tends to \(0\) at \(+\infty\).

**3. Upper spectral bound and nonattainment.** Since \(\|M_{w_t}U_L\|=1\), self-adjointness gives \(\sigma(B_t)\subset[-2r,2r]\) and \(\|B_t\|\leq2r\). The strict pointwise inequality \(w_t<1\) implies, for every nonzero \(h\in L^2(\mathbb R)\),
\[
\|M_{w_t}U_Lh\|<\|h\|,
\qquad \|U_L^*M_{w_t}h\|<\|h\|.
\]
Consequently \(\|B_th\|<2r\|h\|\). This proves that the upper bound, when shown sharp, cannot be attained by a nonzero vector.

**4. Essential spectral saturation for \(t\ne1/2\).** Then \(L\ne0\). For any \(\lambda\in[-2r,2r]\), choose real \(\xi\) satisfying \(\lambda=2r\cos(\xi L)\). Define
\[
h_N(y)=N^{-1/2}e^{i\xi y}\boldsymbol{1}_{[-N^2-N,\,-N^2]}(y),\qquad N\ge1.
\]
Each \(h_N\) has norm one and \(h_N\rightharpoonup0\) weakly as its support escapes to \(-\infty\). Its shift discrepancy satisfies
\[
\big\|[r(U_L+U_L^*)-\lambda]h_N\big\|
 \leq 2r\sqrt{2|L|/N}
\]
for \(N>2|L|\), because the plane-wave identity holds except on boundary strips of total measure at most \(4|L|\). Also \(w_t\to1\) uniformly on the support of \(h_N\) and its fixed translations, so
\[
\big\|[B_t-r(U_L+U_L^*)]h_N\big\|\longrightarrow0.
\]
Thus \(\|(B_t-\lambda)h_N\|\to0\). A weakly-null normalized approximate eigenvector is a singular Weyl sequence and puts \(\lambda\) in the Fredholm essential spectrum of the bounded self-adjoint operator. Every point of the full interval belongs to it; Step 3 excludes all outside points. The spectral formula follows, along with sharpness of \(\|A_t\|=2r\).

**5. Midpoint and strong-limit discontinuity.** At \(t=1/2\), the dilation factor becomes one, so \(\mathcal UT_{1/2}\mathcal U^{-1}\) is multiplication by \(2e^{-x}\), and \(A_{1/2}\) corresponds to multiplication by \(4e^{-x}\) on \(L^2(0,\infty)\). Its spectrum and Fredholm essential spectrum both equal the essential range \([0,4]\). It has no norming vector because \(4e^{-x}<4\) almost everywhere. For fixed \(g\in L^2(0,\infty)\), the model operators \(t^{-1}e^{-x/(2t)}g(((1-t)/t)x)\) converge in norm to \(2e^{-x}g(x)\) as \(t\to1/2\), by strong continuity of dilations, dominated multiplier convergence, and local uniform boundedness. The same is true of the adjoints, proving \(A_t\to A_{1/2}\) strongly. Finally, because \(A_{1/2}\geq0\) while \(-2r\in\sigma(A_t)\) for \(t\ne1/2\), approximate lower-edge spectral vectors show
\[
\|A_t-A_{1/2}\|\geq2r.
\]
This proves the discontinuity and completes the claim.

## Verification
All spectral statements above follow from the explicit unitary equivalence, norm bounds and singular Weyl sequences; no numerical finite section is used to certify an infinite spectral interval. A stand-alone supplementary program, `checks/finite_sections.py`, constructs the matrices using log-binomial coefficients, verifies symmetry and finite-section spectral containment for seven parameters, checks finite-section negative eigenvalues away from \(t=1/2\), and verifies the dilation adjoint scalar identity. Run `python checks/finite_sections.py` with NumPy and SciPy. Successful output was obtained at matrix order 200 for all seven parameter values, but finite sections cannot establish the full essential spectrum.

## Relationship to prior work
Bellavita, Chalmoukis, Daskalogiannis and Stylogiannis (2023) define exactly these Hausdorff-generated generalized Hilbert operators and establish the adjoint relation \(T_t^*=T_{1-t}\), the exact positive-measure norm and noncompactness. **The norm identity is prior work**; it is not claimed as original here. Their inspected complete preprint does not identify the symmetric two-atom operator's full signed Fredholm essential spectrum or the midpoint spectral discontinuity.

The published *A sharp midpoint-support obstruction to positivity of generalized Hilbert matrices* already proves that symmetric two-atom matrices off the midpoint are not positive semidefinite, by an exponentially growing violation of a two-coordinate Cauchy–Schwarz condition. That qualitative sign obstruction is likewise prior work. Its inspected theorem, proof and limitations expressly do not determine the full negative spectrum or its multiplicities. Here the new conclusion is that **every point of the entire negative-to-positive sharp interval is essential spectrum**, with a sudden collapse of the negative spectral band at exactly the midpoint. A published result on two-atom Hausdorff matrices in BMOA/Bloch concerns a different triangular operator and different Banach spaces; it does not imply this self-adjoint Hardy-space spectral interval.

## Limitations
The theorem concerns exactly two reflection-paired atoms of equal unit mass on \((0,1)\). It does not classify arbitrary reflection-symmetric measures or unequal atomic weights, nor does it determine the point-versus-continuous spectral type at every interior point. The bound on norm difference is a lower bound, not an exact formula. The full spectral claim has not undergone independent mathematical validation, and specialist historical literature may contain a more general equivalent result.

## References
1. C. Bellavita, N. Chalmoukis, V. Daskalogiannis and G. Stylogiannis, *Generalized Hilbert operators arising from Hausdorff matrices*, arXiv:`2307.15334`, first public July 28, 2023. https://arxiv.org/abs/2307.15334.
2. *A sharp midpoint-support obstruction to positivity of generalized Hilbert matrices*, published mathematical research result, November 2, 2026. https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-a-sharp-midpoint-support-obstruction-to-positivity-of-generalize--cb3fe6556dcf/RESULT.md.
3. *Arithmetic filling and polynomial spectral regions for two-atom Hausdorff matrices*, published mathematical research result, November 2, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-arithmetic-filling-and-polynomial-spectral-regions-for-two-atom--b381f6ad0c16.
