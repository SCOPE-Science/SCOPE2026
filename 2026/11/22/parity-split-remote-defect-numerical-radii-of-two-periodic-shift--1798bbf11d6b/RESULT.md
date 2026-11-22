# Parity-split remote-defect numerical radii of two-periodic shifts

## Finding
For \(a,b,c>0\), let \(T_m\) be the positive unilateral weighted shift with weights \((a,b,a,b,\ldots)\), except the weight at index \(m\) is replaced by \(c\). Define
\[
\Lambda(c;u,v)=\begin{cases}u+v,&0<c\le u,\\[3pt]
\dfrac{u^2+c^2+\sqrt{(u^2-c^2)^2+4v^2c^2}}{2c},&c>u.
\end{cases}
\]
Then the parity-resolved limits are
\[
\lim_{k\to\infty}w(T_{2k})=\tfrac12\Lambda(c;a,b),\qquad
\lim_{k\to\infty}w(T_{2k+1})=\tfrac12\Lambda(c;b,a).
\]
Both parity subsequences increase non-strictly to their respective limits. The complete sequence converges **if and only if** \(a=b\) or \(c\le\min(a,b)\). Otherwise its even and odd limiting radii are different; the larger is associated with replacement of the smaller background weight. If \(c\le u\), every finite-depth radius for that parity already equals \((a+b)/2\); if \(c>u\), its approach to the limiting radius is \(O(\rho^m)\), with
\[
\rho=\frac{uv}{c\Lambda(c;u,v)-u^2}\in(0,1).
\]
For example, \((a,b,c)=(1,2,3/2)\) gives an even limit of approximately \(1.5631375560\) and an odd limit of exactly \(1.5\), despite the exceptional edge moving arbitrarily far away.

## Assumptions and scope
The Hilbert space is complex \(\ell^2(\mathbb N_0)\), and \(T_m e_j=w_j e_{j+1}\), where \(w_j=a\) for even \(j\) and \(w_j=b\) for odd \(j\), except \(w_m=c\). All three weights are strictly positive, and \(m\in\mathbb N_0\). The numerical radius is \(w(T)=\sup_{\|x\|=1}|\langle Tx,x\rangle|\). The rate claim applies with \(u=a,v=b\) for even \(m\), and \(u=b,v=a\) for odd \(m\), with fixed \(a,b,c\) as \(m\to\infty\) along the stated parity. Neither a uniform estimate as \(c\downarrow u\) nor a finite-depth closed formula is asserted.

## Proof
**1. Half-line reduction and monotonicity.** The phase-diagonal unitary \(e_j\mapsto e^{ij\theta}e_j\) rotates the numerical range of a unilateral weighted shift, while positivity of the weights shows
\[
2w(T_m)=\sup\sigma(J_m),\qquad J_m=T_m+T_m^*.
\]
For arbitrary \(u,v,c>0\) introduce the bilateral Jacobi matrix \(J^{u,v,c}\) on \(\ell^2(\mathbb Z)\) with the single central edge joining sites \(0,1\) having weight \(c\), and all other edges alternating \(u,v\), with the two edges adjacent to the central edge both of weight \(v\). Translate the unique exceptional edge in \(J_m\) to edge \(0,1\). For \(m\) even (respectively odd), the resulting half-line matrix is the compression of \(J^{a,b,c}\) (respectively \(J^{b,a,c}\)) to sites \(\{-m,-m+1,\ldots\}\). As \(m\) advances by two, these subspaces are nested and their union is dense in the bilateral space. Rayleigh quotient density therefore gives the nondecreasing limits
\[
2\lim_{k\to\infty}w(T_{2k})=\sup\sigma(J^{a,b,c}),\quad
2\lim_{k\to\infty}w(T_{2k+1})=\sup\sigma(J^{b,a,c}).
\]
Each unilateral matrix retains a purely periodic right tail, so its essential upper spectral edge is \(u+v=a+b\).

**2. Bilateral top edge when \(c\le u\).** Let \(J^{u,v,u}\) be the unperturbed two-periodic bilateral Jacobi matrix. Its two-site Floquet fibers have eigenvalues \(\pm|u+ve^{it}|\), hence top spectral edge \(u+v\). For any finitely supported \(x\), positivity of the off-diagonal weights yields
\[
\langle J^{u,v,c}x,x\rangle\le
\langle J^{u,v,u}|x|,|x|\rangle\le (u+v)\|x\|^2.
\]
The one-bond perturbation does not remove the periodic essential spectral edge. Consequently \(\sup\sigma(J^{u,v,c})=u+v\). The same upper bound applies to every half-line compression, which also retains essential upper edge \(u+v\), so all its radii equal \((u+v)/2\).

**3. The isolated upper eigenvalue when \(c>u\).** Put \(\lambda=\Lambda(c;u,v)\), the larger root of
\[
F_u(z)=cz^2-(u^2+c^2)z+c(u^2-v^2)=0.
\]
At \(z=u+v\), one has \(F_u(u+v)=-(u+v)(c-u)^2<0\). Since the polynomial opens upward, \(\lambda>u+v\). Define
\[
\rho=\frac{uv}{c\lambda-u^2},\qquad
r=\frac{\lambda-c}{v}.
\]
Both quantities are positive, and \(\rho<1\) because \(c>u\) and \(\lambda>u+v\). The characteristic equation rearranges to \((\lambda-c)(c\lambda-u^2)=cv^2\), equivalently \(\rho=ur/cv\). Set an everywhere positive vector \(\phi\) by the symmetric assignments
\[
\phi_0=\phi_1=1,\quad
\phi_{-1}=\phi_2=r,\quad
\phi_{-2j}=\phi_{2j+1}=\rho^j\ (j\ge1),\qquad
\phi_{-(2j+1)}=\phi_{2j+2}=r\rho^j\ (j\ge0).
\]
The recurrence at the central and successive alternating edges follows from \(\lambda=c+vr\), \(\lambda r=v+u\rho\), and \(\lambda\rho=(u+v\rho)r\). Thus \(J^{u,v,c}\phi=\lambda\phi\). Since \(0<\rho<1\), \(\phi\in\ell^2(\mathbb Z)\). For finitely supported \(x\), the ground-state identity
\[
\lambda\|x\|^2-\langle J^{u,v,c}x,x\rangle
=\sum_{j\in\mathbb Z}t_j\phi_j\phi_{j+1}
\left|\frac{x_j}{\phi_j}-\frac{x_{j+1}}{\phi_{j+1}}\right|^2\ge0
\]
holds, with \(t_j\) the positive edge weights of \(J^{u,v,c}\). Hence \(\lambda=\sup\sigma(J^{u,v,c})\). Density extends this bound to arbitrary \(\ell^2\) vectors.

**4. Two distinct limits and their ordering.** Assume \(a<b\). When \(a<c\le b\), the even limit strictly exceeds \((a+b)/2\) while the odd limit equals it. When \(c>b\), write \(\lambda_a=\Lambda(c;a,b)\) and \(\lambda_b=\Lambda(c;b,a)\). Both exceed \(a+b\) and both are less than \(2c\): indeed \(2c>a+b\), \(F_a(2c)=F_b(2c)=c(2c^2-a^2-b^2)>0\), and each larger root lies between \(a+b\) and \(2c\). Subtracting the polynomials gives \(F_a(z)-F_b(z)=(b^2-a^2)(z-2c)\); therefore \(F_a(\lambda_b)<0\), yielding \(\lambda_a>\lambda_b\). Interchanging \(a,b\) covers the opposite order. When \(a=b\), symmetry makes the two limits coincide for every \(c\). These implications prove the stated necessary and sufficient convergence criterion.

**5. Rate.** For \(c>u\), project the explicit positive eigenvector onto the corresponding half-line \(\{-m,-m+1,\ldots\}\). The missing bond term in its Rayleigh quotient is exactly \(t_{-m-1}\phi_{-m-1}\phi_{-m}\). The norm of the retained vector is bounded below independently of \(m\), and the two omitted/retained boundary amplitudes have product \(O(\rho^m)\). Consequently
\[
0\le\Lambda(c;u,v)-2w(T_m)
\le\frac{t_{-m-1}\phi_{-m-1}\phi_{-m}}{\|\mathbf1_{[-m,\infty)}\phi\|^2}=O(\rho^m).
\]
This completes the proof.

## Verification
The proof is analytic and applies to every positive real \(a,b,c\) and every nonnegative defect index. To check algebra and representative boundaries, run `python check.py` with NumPy and SciPy installed. The checker constructs sufficiently long finite tridiagonal sections and compares their top eigenvalues to the two exact limits, including both subcritical and supercritical phases. The finite tests are diagnostics, **not** proofs of the infinite-dimensional or rate statements. Exact arithmetic formulas and the ground-state identity, rather than sampled numerical approximations, establish the theorem.

## Relationship to prior work
Ghosh–Birbonshi–Ojha (2026) develop numerical-radius techniques for other positive modulated weighted shifts. Wang–Wu (2011, Theorem 4.9) compute the one-spike bilateral constant-background radius; setting \(a=b\) recovers that established case. Chakraborty–Ojha–Birbonshi (2022) develop determinantal techniques for fixed finite patterns. Marionnet (2026, Proposition 3.3) computes the exact **finite-depth band-edge threshold** for a one-bond perturbation of an alternating unilateral tail, and Proposition 3.6 gives the constant-background remote-defect limit. Those statements already imply where a sufficiently remote defect may cross the essential edge, and are expressly credited. The additional assertion assessed here is the **exact two different phase-dependent remote-defect radii, their complete convergence dichotomy, and explicit supercritical geometric approach**, not the threshold, the general compression idea, or the homogeneous formula. A broader Jacobi transfer-matrix or dimerized-defect result might implicitly contain the calculations; see limitations.

## Limitations
The theorem concerns real positive two-periodic weights and one changed edge, not multiple defects, signed or complex varying weights, or more general periodicity. The geometric rate is pointwise in the parameters and not uniform as the defect strength approaches its phase-specific threshold. The result has received only self-review; independent validation has not been performed. A legacy spectral/SSH-style formulation of the same upper outlier and its implications is a residual originality risk.

## References
- A. Ghosh, R. Birbonshi, S. Ojha, *On the numerical radius of a class of weighted shift operators*, arXiv:2608.17486v1 (first public 2026-08-18), https://arxiv.org/abs/2608.17486.
- P. Y. Wu and K. Z. Wang, *Numerical ranges of weighted shifts*, 2011, Theorem 4.9, https://ir.lib.nycu.edu.tw/bitstream/11536/19226/1/000290972700040.pdf.
- B. Chakraborty, S. Ojha and R. Birbonshi, *Numerical radii of weighted shift operators using determinantal polynomials*, *Operators and Matrices* 16 (2022), 1155–1174, https://files.ele-math.com/articles/oam-16-75.pdf.
- S. Marionnet, *Numerical range of finite perturbations of a 2-periodic weighted shift*, arXiv:2611.21280v1 (first public 2026-11-16), https://arxiv.org/html/2611.21280v1.
