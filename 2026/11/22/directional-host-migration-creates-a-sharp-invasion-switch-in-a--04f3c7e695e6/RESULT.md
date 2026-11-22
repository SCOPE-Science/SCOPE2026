# Directional host migration creates a sharp invasion switch in a two-patch vector–host epidemic

## Finding

Consider a two-patch, two-infected-class epidemic in which infected hosts and infected vectors migrate separately. The two isolated patches have the same subcritical reproduction number, yet their host-to-vector and vector-to-host transmission rates have reciprocal spatial contrasts. A fixed positive vector migration rate and varying host migration strength produce a sharp **increase, decrease, or exact invariance** of the global invasion reproduction number, determined by one explicit inequality in the stationary host migration bias. In the increasing regime a unique finite migration rate can turn two locally subcritical patches into a supercritical coupled system; neither mobility mechanism by itself can do so in this model.

**Theorem.** Let \(c>0\), \(\xi>1\), \(p,q>0\), and \(n>0\) be fixed, and let \(m\ge0\). Define \(h,v\in\mathbb R^2\) by the disease-free linearized infection system
\[
\dot h=A v-(I+mL_h)h,\qquad
\dot v=B h-(I+nL_v)v,
\]
where
\[
L_h=\begin{pmatrix}p&-q\\-p&q\end{pmatrix},\quad
L_v=\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\quad
A=c\operatorname{diag}(\xi,\xi^{-1}),\quad
B=c\operatorname{diag}(\xi^{-1},\xi).
\]
The host and vector removal rates are both normalized to one, the off-diagonal migration rates are strictly positive for \(m,n>0\), and the two diagonal infection matrices are strictly positive. Define the basic reproduction number \(R(m)\) as the spectral radius of the four-dimensional next-generation matrix. Set
\[
P=p+q,\qquad a=\frac{1+n}{1+2n},\qquad b=\frac{n}{1+2n},\qquad
T=\frac{q\xi^{-2}+p\xi^2}{p+q}.
\]
Then
\[
R(m)^2=\frac{S_m+\sqrt{S_m^2-4D_m}}2,\quad
S_m=\frac{c^2[2a+mP(a+bT)]}{1+mP},\quad
D_m=\frac{c^4}{(1+2n)(1+mP)}.
\]
For all finite \(m\ge0\), \(R(m)\) is strictly increasing if \(p\xi^2>q\), strictly decreasing if \(p\xi^2<q\), and exactly constant if \(p\xi^2=q\). Equivalently, the monotonicity switches at stationary host weight \(p/(p+q)=1/(1+\xi^2)\), independently of the *magnitude* of the positive vector migration rate \(n\).

Moreover
\[
R(0)=c,\qquad \lim_{m\to\infty}R(m)^2=c^2(a+bT).
\]
If \(0<c<1\), a finite unique crossing \(R(m_*)=1\) occurs exactly when \(c^2(a+bT)>1\), and then
\[
m_* = \frac{(1-c^2)[1-c^2/(1+2n)]}{(p+q)[c^2(a+bT)-1]};
\]
\(R(m)<1\) for \(0\le m<m_*\) and \(R(m)>1\) for \(m>m_*\). If \(c^2(a+bT)\le1\), no finite supercritical migration threshold exists. With \(n=0\), \(R(m)=c\) for every \(m\ge0\), so the strict effects require migration of **both** infected classes.

**Exact rational example.** With
\[
(c,\xi,n,p,q)=(1/2,4,1,9,1),
\]
both isolated patch reproduction numbers are \(1/2\); vector migration alone and host migration alone each leave this value unchanged. Coupled movement has
\[
R(0)^2=\tfrac14,\qquad
\lim_{m\to\infty}R(m)^2=\frac{175}{128}>1,
\quad
m_*=\frac{44}{235},
\]
and, writing \(K(m)=(I+mL_h)^{-1}A(I+nL_v)^{-1}B\),
\[
\det(I-K(m))=\frac{44-235m}{64(1+10m)}.
\]
Thus there is exactly one invasion threshold, and the two-patch system is supercritical for every \(m>44/235\) despite both isolated patches being subcritical.

## Assumptions and scope

All claims concern the **local invasion threshold of the explicitly stated, constant-coefficient infection linearization**. The columns of the migration generators sum to zero. The constants \(A\) and \(B\) represent effective per-capita transmission *rates*, not probabilities, and can differ by patch even when the products of opposite transmission rates agree. Stationary susceptible demographics are assumed fixed as the common host migration scaling \(m\) varies; their stationary proportions depend on \(p/q\), not on \(m\). The next-generation construction counts one host-to-vector or vector-to-host event as one generation, giving the usual square-root convention for vector–host reproduction numbers.

The linearized system is a finite-patch analogue of spatially structured host/vector models with distinct dispersal rules. It is **not** the full nonlocal, nonlinear model of the initiating publication. No theorem about nonlinear endemic equilibria, incidence data, or policy effectiveness follows from the present spectral result alone.

## Proof

**1. Next-generation reduction.** The new-infection and transfer matrices are
\[
F=\begin{pmatrix}0&A\\B&0\end{pmatrix},\qquad
V=\operatorname{diag}(I+mL_h,I+nL_v).
\]
Both diagonal blocks of \(V\) are invertible nonsingular \(M\)-matrices. The square of \(FV^{-1}\) is block diagonal, with nonzero spectrum given by the two cyclically permuted two-step products. Therefore
\[
R(m)^2=\rho(K(m)),\qquad K(m)=(I+mL_h)^{-1}A(I+nL_v)^{-1}B.
\]
For fixed \(n>0\), put \(Q=A(I+nL_v)^{-1}B\). Direct inversion yields
\[
Q=c^2\begin{pmatrix}a&b\xi^2\\b\xi^{-2}&a\end{pmatrix},
\]
which has strictly positive entries, positive determinant \(c^4/(1+2n)\), eigenvalues \(c^2\) and \(c^2/(1+2n)\), and Perron eigenvalue \(c^2\).

**2. Exact trace and determinant.** The host migration resolvent is
\[
(I+mL_h)^{-1}=\frac{1}{1+mP}\begin{pmatrix}1+mq&mq\\mp&1+mp\end{pmatrix}.
\]
Taking trace and determinant of its product with \(Q\) gives the stated \(S_m,D_m\). The characteristic polynomial is \(\lambda^2-S_m\lambda+D_m\); positivity and Perron–Frobenius yield the claimed radical.

**3. Strict monotonicity.** Let \(\pi=(q/P,p/P)^\mathsf T\) and \(\Pi=\pi(1,1)\). Since \(L_h=P(I-\Pi)\), set \(w=mP/(1+mP)\in[0,1)\). Then
\[
K(m)=M(w):=[(1-w)I+w\Pi]Q.
\]
For *any* strictly positive two-by-two matrix \(Q\), the characteristic polynomial of \(M(w)\) is affine in \(w\): its trace is affine and its determinant is \((1-w)\det Q\). Its Perron root \(\lambda(w)\) is analytic and simple for \(0\le w\le1\). If \(\lambda'(w_0)=0\), differentiating the affine characteristic equation shows that the characteristic polynomial, evaluated at \(\lambda(w_0)\), vanishes for **every** \(w\). By simplicity and analytic continuation the Perron root must then be constant. Consequently, otherwise its derivative is nowhere zero and its direction is determined by its endpoints. Here those endpoints are \(\lambda(0)=c^2\) and \(\lambda(1)=\mathbf1^\mathsf TQ\pi=c^2(a+bT)\). Since \(b>0\), the strict direction is the sign of \(T-1\), which is the sign of \(p\xi^2-q\). At equality the Perron root is constant. Continuity covers \(m=0\).

**4. Finite invasion crossing.** If \(0<c<1\), then \(R(0)<1\). The strict monotonicity just proved guarantees a unique finite crossing if and only if the limiting square is strictly above one. Substituting \(\lambda=1\) into \(\lambda^2-S_m\lambda+D_m=0\), multiplying by \(1+mP\), and solving the linear equation in \(m\) yields the displayed formula. At the crossing the other eigenvalue is \(D_m<1\), so the unit eigenvalue is the Perron root. No extraneous root arises. If \(n=0\), the product is \(c^2(I+mL_h)^{-1}\), whose Perron eigenvalue is exactly \(c^2\) for all \(m\).

**5. Witness.** Exact substitution gives \(\operatorname{tr}K=(1/3+(875/64)m)/(1+10m)\) and \(\det K=1/[48(1+10m)]\). Their characteristic polynomial at one is \((44-235m)/[64(1+10m)]\); its single positive zero is \(44/235\). The limit is \(175/128\). This proves every asserted rational boundary.

## Verification

Run \(\texttt{python3 verify.py}\) with Python 3 (standard library only). The checker independently constructs and inverts the host and vector migration matrices with exact rational arithmetic, multiplies their next-generation factors, and verifies the trace and determinant identities in 1,080 rational cases. It checks the strictly increasing, decreasing and constant regimes numerically as **diagnostics**, verifies that immobile vectors remove the effect, and checks the exact witness, unique threshold and factorized determinant. The finite checks are **not** a replacement for the all-parameter analytic proof above.

## Relationship to prior work

Dey, Kar and Tridane (2026) motivate distinct host and vector nonlocal dispersal and give an abstract reproduction operator, global threshold results and numerical mobility experiments. The paper's accessible bibliographic abstract does not establish the explicit finite-patch result; however, its full text was not available for a definitive exclusion, which remains a priority risk.

Gao, van den Driessche and Cosner (2019) rigorously examine **epidemiologically identical patches** and derive a different movement effect; their source manuscript and numerical section were compared. Identical *products* of the two directed transmission coefficients in the present theorem do **not** make its patches epidemiologically identical: here the coefficients themselves are reciprocally heterogeneous. Gao and Dong (2019) prove decreasing reproduction numbers for a **single moving infected class and a diagonal infection matrix**; here both infected classes move and the reduced infection matrix \(Q\) is strictly positive and nondiagonal. Gao and Lou (2025) give monotonic host dispersal results with vectors immobile, not the simultaneous-mobility effect. Ruktanonchai, Smith and De Leenheer (2016) **already prove the qualitative phenomenon** that making all local patch reproduction numbers subcritical need not ensure eradication when both hosts and vectors move; their Lagrangian movement model and source–sink bounds do not supply the present exact Eulerian host-rate monotonicity switch or finite crossing formula. Cosner et al. (2009) and Gao and Yuan (2024) establish general vector-host mobility models, invasion reproduction methods and movement-driven effects but do not directly imply this exact directional-bias classification under their respective mobility assumptions.

Thus the claimed contribution is the **sharp all-rate monotonicity sign, equality case, and closed-form joint-mobility crossing** for the stated reciprocally heterogeneous two-patch linearization—not the previously established qualitative possibility of spread across locally subcritical patches. Unlocated equivalent older two-state positive-matrix or vector-host results remain possible.

## Limitations

This is an exact result in a simplified two-patch linear invasion model with normalized equal class removal and special reciprocal transmission contrasts. It is not a general theorem for arbitrary migration networks, unequal removal rates, susceptible feedback, or spatial integro-differential operators. The full initiating 2026 article and at least one plausible older source were not compared in full, leaving residual historical-priority uncertainty. Neither a nonlinear endemic attractor nor a practical vaccination/travel recommendation is claimed. Independent validation has not been conducted.

## References

- Dey, S., Kar, T. K. & Tridane, A. (2026). *Dynamics of a vector-host epidemic model with generalized nonlinear incidence functions and distinct dispersal kernels.* Mathematical Biosciences 403, 109856. First publicly online 2026-11-12. https://doi.org/10.1016/j.mbs.2026.109856 ; https://pubmed.ncbi.nlm.nih.gov/43020195/ .
- Gao, D., van den Driessche, P. & Cosner, C. (2019). *Habitat fragmentation promotes malaria persistence.* Journal of Mathematical Biology 79, 2255–2280. Author manuscript: https://www.math.miami.edu/~dzgao/GvdDC-JMB2019.pdf . DOI: https://doi.org/10.1007/s00285-019-01428-2 .
- Gao, D. & Dong, C.-P. (2019). *Fast Diffusion Inhibits Disease Outbreaks.* Proceedings of the American Mathematical Society. https://arxiv.org/html/1907.12229v1 .
- Gao, D. & Lou, Y. (2025). *Effect of host movement on the prevalence of vector-borne diseases.* Journal of Mathematical Biology 91, 33. https://doi.org/10.1007/s00285-025-02254-5 .
- Cosner, C., et al. (2009). *The effects of human movement on the persistence of vector-borne diseases.* Journal of Theoretical Biology 258, 550–560. https://pmc.ncbi.nlm.nih.gov/articles/PMC2684576/ .
- Gao, D. & Yuan, X. (2024). *A hybrid Lagrangian–Eulerian model for vector-borne diseases.* Journal of Mathematical Biology 89, 16. https://doi.org/10.1007/s00285-024-02109-5 .
- Ruktanonchai, N. W., Smith, D. L. & De Leenheer, P. (2016). *Parasite sources and sinks in a patched Ross–Macdonald malaria model with human and mosquito movement: Implications for control.* Mathematical Biosciences 279, 90–101. Author manuscript: https://scispace.com/pdf/parasite-sources-and-sinks-in-a-patched-ross-macdonald-32xrm01p8i.pdf ; DOI: https://doi.org/10.1016/j.mbs.2016.06.012 .
