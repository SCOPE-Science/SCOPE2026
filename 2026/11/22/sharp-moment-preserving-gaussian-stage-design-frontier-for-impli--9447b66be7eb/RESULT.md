# Sharp moment-preserving Gaussian stage-design frontier for implicit Runge–Kutta decay

## Finding

Consider either scalar version of the randomized semi-implicit and implicit two-stage Runge–Kutta updates motivated by Bochacik and Przybyłowicz [1]. On the test equation \(y'=-\gamma y\), with \(\gamma>0\) and step \(h>0\), write \(r=\gamma h\). Let the independent stage fractions \(T_j\in[0,1]\) have a common arbitrary Borel probability law \(\mu\), and require that its first three nonconstant moments match those of a uniform stage:
\[
\int_0^1 t^k\,d\mu(t)=\frac1{k+1},\qquad k=1,2,3.
\]
The associated squared one-step amplification is
\[
F_\mu(r)=\int_0^1\left(\frac{1-r(1-t)}{1+rt}\right)^2d\mu(t).
\]
Define the two-node Gauss–Legendre law \(\mu_G=\tfrac12(\delta_a+\delta_b)\), where \(a=\tfrac12-\tfrac1{2\sqrt3}\), \(b=\tfrac12+\tfrac1{2\sqrt3}\). Let \(r_c\) denote the unique positive root of
\[
11r^3+28r^2+6r-12=0,\qquad r_c=0.514568548894944\ldots.
\]
**Sharp stage-law frontier.** Among **all** moment-matched probability laws, \(\mu_G\) uniquely minimizes \(F_\mu(r)\) for every fixed \(r\ge r_c\). For every fixed \(0<r<r_c\), it does **not** minimize \(F_\mu(r)\): a positive three-atom moment-matched law has strictly smaller mean-square amplification. No support-size restriction is imposed on the competing laws.

**Sharp stability radius.** The law \(\mu_G\) is also the unique law in this moment class maximizing the initial interval of strict real-negative-axis mean-square stability. The maximum radius is the unique positive root
\[
R_G^3-2R_G^2-12R_G-12=0,\qquad R_G=4.928704239327397\ldots.
\]
For \(\mu_G\), \(F_{\mu_G}(r)<1\) exactly when \(0<r<R_G\), and equality holds at \(r=R_G\). Every other admissible \(\mu\) has \(F_\mu(R_G)>1\) and therefore a strictly shorter initial interval of strict stability. The uniform law has radius \(R_U=4.033610469357736\ldots\), so matching the same first three stage moments with \(\mu_G\) enlarges that radius by \(22.19088275\ldots\) percent.

## Assumptions and scope

The dynamics are the scalar deterministic Dahlquist decay test, not a stochastic differential equation. Independent stage fractions are sampled anew at each step. A positive step \(h\) and decay \(\gamma>0\) are fixed; \(r=h\gamma\) is dimensionless. The Borel probability law is supported on the closed interval \([0,1]\). The three moment equalities above, together with unit total mass, are the *only* distributional constraints. These constraints do not assert equal behavior of the corresponding methods on nonlinear or nonautonomous equations.

The amplification of both scalar updates is \(A(r,t)=1-r/(1+rt)\). Hence for deterministic nonzero initial data, independence gives \(\mathbb E|Y_N|^2=|Y_0|^2F_\mu(r)^N\). The *initial strict mean-square stability radius* of \(\mu\) means the supremum of \(R\ge0\) such that \(F_\mu(r)<1\) for every \(0<r<R\); it does not assume that any disconnected later stable islands are absent for a general law. The optimization is of this scalar real-axis criterion, not complex-half-plane A-stability.

## Proof

**1. The candidate law and an exact cubic contact formula.** The two roots \(a,b\) of \(t^2-t+\tfrac16=0\), each with weight \(\tfrac12\), reproduce uniform moments through degree three. For fixed \(r>0\), put
\[
f_r(t)=\left(\frac{1-r+rt}{1+rt}\right)^2,\quad
C(r)=r^3+16r^2+18r-12,\quad
B(r)=10r^3+12r^2-12r.
\]
Let \(H_r(t)\) be the unique polynomial of degree at most three interpolating both \(f_r\) and its first derivative at \(a,b\). Clearing the denominators and dividing the corresponding polynomial yields the **exact identity**
\[
\boxed{\quad
f_r(t)-H_r(t)=
\frac{r^5(6t^2-6t+1)^2\,[C(r)+B(r)t]}
{(1+rt)^2(r^2+6r+6)^3}.\quad}
\tag{1}
\]
One can verify (1) directly without knowing the coefficients of \(H_r\): subtract the displayed rational expression from \(f_r\), cancel \((1+rt)^2\), and check that the result is a cubic in \(t\). The squared factor ensures value and derivative matching at the two distinct Gauss nodes, which proves it is \(H_r\). The accompanying exact symbolic checker performs these cancellations independently.

For any admissible law \(\mu\), cubic moment matching and the interpolation conditions give
\[
\int H_r\,d\mu=\int H_r\,d\mu_G=\int f_r\,d\mu_G,
\qquad
F_\mu(r)-F_{\mu_G}(r)=\int(f_r-H_r)\,d\mu.
\tag{2}
\]

**2. A sharp sign change and global optimality.** Define \(J(r)=C(r)+B(r)=11r^3+28r^2+6r-12\). Both \(J\) and \(C\) are strictly increasing for \(r>0\). Since \(J(\tfrac12)=-\tfrac58<0\) and \(J(\tfrac35)>0\), the unique positive root \(r_c\) lies in \((\tfrac12,\tfrac35)\). Also \(C(\tfrac12)=\tfrac98>0\). For every \(r\ge r_c\) and \(t\in[0,1]\),
\[
C(r)+B(r)t=(1-t)C(r)+tJ(r)\ge0,
\]
with strict positivity except possibly at \(r=r_c,t=1\). Equations (1)–(2) prove \(F_\mu(r)\ge F_{\mu_G}(r)\) for every admissible law. For \(r>r_c\), equality implies \(\mu\) is supported on \(\{a,b\}\), and its first moment fixes the weights at \(\tfrac12\). At \(r=r_c\), the zero set additionally permits \(t=1\); however the degree-two polynomial \(g(t)=t^2-t+\tfrac16\) integrates to zero under every admissible law, and on \(\{a,b,1\}\) it is zero at \(a,b\) and strictly positive at \(1\). Thus any equality law puts zero mass at \(1\), and again equals \(\mu_G\). Uniqueness follows even at the boundary.

**3. The transition is necessary, not just sufficient.** Fix \(0<r<r_c\). Then \(J(r)<0\), so equation (1) gives \(f_r(1)-H_r(1)<0\). Start from Gauss's two nodes with weights \(\tfrac12,\tfrac12\), and introduce a small new mass \(\varepsilon>0\) at \(1\). Choose perturbed weights \(w_1(\varepsilon),w_2(\varepsilon)\) and locations \(a(\varepsilon),b(\varepsilon)\) to satisfy exactly
\[
w_1(\varepsilon)a(\varepsilon)^k+w_2(\varepsilon)b(\varepsilon)^k+\varepsilon=\frac1{k+1},\qquad k=0,1,2,3.
\tag{3}
\]
At \(\varepsilon=0\), these are the Gauss weights and nodes. The Jacobian of the four moment equations with respect to the four unknown weights and locations is a nonsingular confluent Vandermonde matrix because \(a\ne b\) and both weights are positive. The implicit-function theorem therefore supplies a smooth solution to (3) for all sufficiently small positive \(\varepsilon\), with both weights positive and both locations strictly inside \((0,1)\). This constructs a bona fide three-atom probability law.

Differentiate the objective of this law at \(\varepsilon=0\). Since \(H_r\) matches \(f_r\) and its first derivative at the two moving Gauss nodes, and (3) fixes all cubic moments, the derivative is exactly
\[
\left.\frac{d}{d\varepsilon}F_{\mu_\varepsilon}(r)\right|_{\varepsilon=0}
=f_r(1)-H_r(1)<0.
\]
Consequently \(F_{\mu_\varepsilon}(r)<F_{\mu_G}(r)\) for every sufficiently small positive \(\varepsilon\). This proves the *if and only if* threshold for Gauss optimality.

**4. Exact stability radius and unique optimal law.** Direct substitution of the two Gaussian nodes gives
\[
F_{\mu_G}(r)-1=
\frac{r(r^3-2r^2-12r-12)}{6(1+r+r^2/6)^2}.
\tag{4}
\]
The cubic in (4) has exactly one positive root by Descartes' rule of signs and changes sign from negative near zero to positive at infinity. This establishes the strict stable interval \((0,R_G)\). Since \(R_G>r_c\), step 2 yields \(F_\mu(R_G)>F_{\mu_G}(R_G)=1\) for **every** admissible \(\mu\ne\mu_G\); continuity in \(r\) makes its initial strict stability radius strictly less than \(R_G\). Conversely, Gauss attains the stated radius. Finally, integrating \(f_r\) over the uniform law gives
\[
F_U(r)-1=\frac{r^2}{1+r}-2\log(1+r),
\]
whose derivative is \((r^2-2)/(1+r)^2\). It therefore has exactly one positive zero after \(\sqrt2\), at the quoted \(R_U\), and \(R_U<R_G\) also follows from the strict uniqueness in step 2.

## Verification

The standalone `verify.py` uses exact symbolic algebra to reconstruct (1), check that the candidate \(H_r\) has degree at most three, reproduce all Gauss moment identities, and derive (4) without floating-point fitting. It also executes 808 supplemental exact-rational sign comparisons over selected step sizes and stage locations and evaluates both positive cubic roots numerically. Run `python3 verify.py` using the dependency specified in `requirements.txt`. The global optimization across Borel probability laws follows from equations (1)–(3), the sign argument, and the implicit-function theorem; finite tests alone do not establish it.

## Relationship to prior work

The original independently uniform randomized implicit RK2 schemes and their scalar mean-square stability region were analyzed by Bochacik and Przybyłowicz [1], and subsequently in a journal version [2]. Those results motivate replacing the uniform stage law, but do not optimize over all laws matching the uniform distribution's first three moments.

A published mathematical treatment of random-coefficient theta integration [3] proves a sharp mean-square A-stability condition for arbitrary **two-point** coefficients, and a centered-law obstruction for arbitrary coefficient distributions; its symmetric two-point stability inequality implies the Gauss law's one-dimensional cubic (4). Thus (4) alone is **not** claimed as a novel result. The claim here is instead the globally sharp, **all-Borel-law** moment-constrained minimization threshold \(r_c\), its necessary three-atom perturbation, and the resulting distributionally unique largest initial decay-stability radius. The cited two-point theorem does not impose three-moment constraints or optimize against laws with arbitrary support. Classical Gaussian quadrature and Hermite interpolation underlie the proof [4]; the sharp sign transition for this rational stability objective is the additional assertion. A specialized prior treatment under moment-problem or optimal-design terminology might still cover it.

## Limitations

The result is scalar and on the **negative real axis only**. It does not claim mean-square A-stability on the entire complex left half-plane, general nonlinear accuracy, preservation of convergence order for nonautonomous equations, or stability under temporally dependent stage choices. The order-three stage moment constraints are a chosen natural calibration class, not an assumption required by the original algorithms. For \(0<r<r_c\), the proof constructs improving laws but **does not classify** the global minimizers. The numerical constants are supplementary to the exact polynomial statements. Independent review and exhaustive publication-priority determination have not been performed.

## References

[1] T. Bochacik and P. Przybyłowicz, *Convergence and stability of randomized implicit two-stage Runge–Kutta schemes*, arXiv:2404.19059v1, first public 2024-04-29. https://arxiv.org/abs/2404.19059

[2] T. Bochacik, P. Przybyłowicz, and Ł. Stępień, *Convergence and stability of randomized implicit two-stage Runge–Kutta schemes*, BIT Numerical Mathematics 65 (2025), article 7. https://doi.org/10.1007/s10543-024-01050-9

[3] *Sharp mean-square A-stability for two-point randomized theta integration*, publicly available mathematical note, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-mean-square-a-stability-for-two-point-randomized-theta-int--b50d9b3e1e32

[4] L. N. Trefethen, *Exactness of Quadrature Formulas*, SIAM Review 64 (2022), 132–150. https://doi.org/10.1137/20M1389522
