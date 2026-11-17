# Sharp total-variation Cauchy occupation law at a cubic nilpotent global center

## Finding

Consider the reversible cubic polynomial flow
\[
\dot x=(1+\gamma x+\alpha x^2)y,\qquad \dot y=-x^3,
\]
with real \(\gamma\ne0\) and \(\alpha>\gamma^2/4\). Write \(\Delta=4\alpha-\gamma^2>0\). Every positive energy \(E\) determines exactly one nonconstant periodic trajectory. If \(T(E)\) is its minimal period **in original physical time** and \(\mu_E\) is the distribution of its \(x\)-coordinate at a uniformly chosen time in one full period, define
\[
 f_\infty(x)=\frac{\sqrt\Delta}{2\pi(1+\gamma x+\alpha x^2)},\qquad \mu_\infty(dx)=f_\infty(x)\,dx.
\]
Then \(\mu_E\to\mu_\infty\) in total variation, with the sharp first-order law
\[
 \boxed{\lim_{E\to\infty}\sqrt E\,d_{\mathrm{TV}}(\mu_E,\mu_\infty)
 =\frac{\sqrt\Delta}{\sqrt2\pi\alpha^{3/2}}.}
\]
More precisely,
\[
 d_{\mathrm{TV}}(\mu_E,\mu_\infty)=
 \frac{\sqrt\Delta}{\sqrt2\pi\alpha^{3/2}\sqrt E}
 +O_{\alpha,\gamma}\!\left(\frac{\log E}{E}\right),
 \qquad
 \sqrt E\,T(E)=\frac{2\sqrt2\pi}{\sqrt\Delta}
 +O_{\alpha,\gamma}\!\left(\frac{\log E}{E}\right).
\]
The event where the \(x\)-coordinate lies *outside* the two current turning points attains the total-variation discrepancy to leading order. The limit is a shifted Cauchy law with location \(-\gamma/(2\alpha)\) and scale \(\sqrt\Delta/(2\alpha)\).

## Assumptions and scope

Define the strictly positive quadratic
\[
 P(x)=1+\gamma x+\alpha x^2,
 \qquad V(x)=\int_0^x\frac{t^3}{P(t)}\,dt,
 \qquad H(x,y)=\frac{y^2}{2}+V(x).
\]
Assume \(\gamma\ne0\), \(\alpha>\gamma^2/4\), and \(E>0\). All asymptotic statements are for \(E\to\infty\) with \(\alpha,\gamma\) fixed; constants need not be uniform as \(\Delta\downarrow0\). The turning points \(x_-(E)<0<x_+(E)\) are uniquely defined by \(V(x_\pm(E))=E\). The probability law is defined by original time, not a Hamiltonian time reparametrization. Total variation uses the convention \(d_{\mathrm{TV}}(\mu,\nu)=\sup_B|\mu(B)-\nu(B)|=\tfrac12\int|f-g|\,dx\).

## Proof

**1. Global ovals and original-time density.** The identity \(P(x)>0\) follows from the negative quadratic discriminant. Direct differentiation gives
\[
 \frac{dH}{dt}=\frac{x^3}{P(x)}P(x)y+y(-x^3)=0.
\]
Moreover \(V'(x)=x^3/P(x)\), so \(V\) decreases strictly from \(+\infty\) to zero on the negative half-line and increases strictly from zero to \(+\infty\) on the positive half-line. Indeed polynomial division yields
\[
 \frac{x^3}{P(x)}=\frac{x}{\alpha}-\frac{\gamma}{\alpha^2}
 +O_{\alpha,\gamma}(|x|^{-1})\quad (|x|\to\infty),
\]
whence \(V(x)=x^2/(2\alpha)-\gamma x/\alpha^2+O_{\alpha,\gamma}(\log(2+|x|))\). Thus each \(E>0\) is a regular, simple closed oval in the phase plane. It carries a unique periodic orbit, with turning points \((x_-(E),0)\) and \((x_+(E),0)\).

On either velocity branch \(y=\pm\sqrt{2(E-V(x))}\), so original time satisfies \(|dt/dx|=[P(x)\sqrt{2(E-V(x))}]^{-1}\). Introduce
\[
 J(E)=\int_{x_-(E)}^{x_+(E)}\frac{dx}{P(x)\sqrt{1-V(x)/E}},
 \qquad C=\int_{-\infty}^{\infty}\frac{dx}{P(x)}=\frac{2\pi}{\sqrt\Delta}.
\]
Both velocity branches together give the *exact* minimal period and occupation density
\[
 T(E)=\sqrt{\frac2E}\,J(E),\qquad
 f_E(x)=\frac{\mathbf 1_{\{V(x)<E\}}}{J(E)P(x)\sqrt{1-V(x)/E}}.
\]
The proposed \(f_\infty(x)=1/[CP(x)]\) is a normalized density; completing the square in \(P\) gives the stated shifted-Cauchy parameters.

**2. Energy-shell weight.** For \(v>0\), let \(x_\pm(v)\) be the inverse branches of \(V\), and define
\[
 W(v)=\frac1{x_+(v)^3}+\frac1{|x_-(v)|^3}.
\]
Using \(dv=x^3dx/P(x)\) on each half-line, including orientation reversal on the negative branch, yields the exact identities
\[
 C=\int_0^\infty W(v)\,dv,\qquad
 J(E)=\int_0^E\frac{W(v)}{\sqrt{1-v/E}}\,dv.
\]
Since \(V(x)=x^4/4+O(x^5)\) near zero, \(W(v)=O(v^{-3/4})\) near \(v=0\). The large-\(|x|\) expansion in step 1 implies
\[
 x_\pm(v)=\pm\sqrt{2\alpha v}+O_{\alpha,\gamma}(1),
 \qquad W(v)=c v^{-3/2}+O_{\alpha,\gamma}(v^{-2}),
 \quad c=\frac{2}{(2\alpha)^{3/2}}=\frac1{\sqrt2\alpha^{3/2}}.
\]
In particular, the limiting law's mass outside the turning points is
\[
 \frac{Q(E)}C,\qquad
 Q(E)=\int_E^\infty W(v)\,dv
 =\frac{2c}{\sqrt E}+O_{\alpha,\gamma}(E^{-1}).
\]

**3. Cancellation in the square-root Abel transform.** For \(E\ge2\), decompose
\[
 W(v)=c\,\mathbf 1_{\{v\ge1\}}v^{-3/2}+R(v).
\]
Then \(R\in L^1(0,\infty)\), \(R(v)=O(v^{-3/4})\) as \(v\downarrow0\), and \(R(v)=O(v^{-2})\) as \(v\to\infty\). Directly integrating the leading tail, with \(v=E\sin^2\theta\), gives
\[
 \int_1^E\frac{c v^{-3/2}}{\sqrt{1-v/E}}\,dv
 =2c\sqrt{1-E^{-1}},\quad
 \int_1^\infty c v^{-3/2}\,dv=2c.
\]
Their difference is \(O(E^{-1})\), **not** \(O(E^{-1/2})\). For the remainder, use \(|(1-s)^{-1/2}-1|\le K s\) on \(0\le s\le1/2\). Consequently, the integral of \(R(v)[(1-v/E)^{-1/2}-1]\) over \((0,E/2)\) is bounded by
\[
 \frac K E\int_0^{E/2}v|R(v)|\,dv
 =O_{\alpha,\gamma}(\log E/E).
\]
On \((E/2,E)\), the bound \(|R(v)|=O(E^{-2})\) and integrability of the square-root endpoint singularity yield \(O(E^{-1})\). The missing remainder tail \(\int_E^\infty|R(v)|\,dv\) is also \(O(E^{-1})\). Therefore
\[
 \boxed{J(E)-C=O_{\alpha,\gamma}(\log E/E)}.
\]
Substitution into the exact period formula proves the stated two-term period estimate.

**4. Exact normalization comparison and sharp total variation.** Set
\[
 \widetilde f_E(x)=\frac{\mathbf1_{\{V(x)<E\}}}{CP(x)\sqrt{1-V(x)/E}}.
\]
Its total mass is \(J(E)/C\), and on the turning interval \(\widetilde f_E\ge f_\infty\), whereas outside it \(\widetilde f_E=0\). Thus direct integration of its positive and negative discrepancies gives
\[
 \|\widetilde f_E-f_\infty\|_{L^1}
 =\frac{J(E)-C+2Q(E)}C,
\qquad
 \|f_E-\widetilde f_E\|_{L^1}=\frac{|J(E)-C|}C.
\]
The triangle inequality, also in reverse, now shows
\[
 \left|d_{\mathrm{TV}}(\mu_E,\mu_\infty)-\frac{Q(E)}C\right|
 \le\frac{|J(E)-C|}C.
\]
Using steps 2 and 3 yields
\[
 d_{\mathrm{TV}}(\mu_E,\mu_\infty)
 =\frac{2c}{C\sqrt E}+O_{\alpha,\gamma}(\log E/E)
 =\frac{\sqrt\Delta}{\sqrt2\pi\alpha^{3/2}\sqrt E}
 +O_{\alpha,\gamma}(\log E/E).
\]
Finally, \(\mu_E(\{V>E\})=0\), while \(\mu_\infty(\{V>E\})=Q(E)/C\). Hence the event outside the current turning interval achieves the total-variation supremum to first order. This proves all statements.

## Verification

The proof is analytical, including the global phase portrait, the exact original-time normalization, and the Abel remainder. The accompanying standard-library program `CHECK.py` independently checks the elementary potential derivative, the Cauchy normalization, the dominant Abel-tail identity, and numerical convergence for the non-symmetric example \((\alpha,\gamma)=(1,1)\). Its numerical quadratures are diagnostics, not certificates for the infinite limit.

## Relationship to prior work

Corbera and Valls, *Global Nilpotent Reversible Centers with Cubic Nonlinearities Symmetric with Respect to the x-Axis* (2024), classify global-center parameters for a general cubic family; their system (5) contains this subfamily after normalization. Center existence and the originating dynamical family are not claimed as new. Their Theorem 2 and appendices concern global-center classification and do not give the present physical-time period and occupation estimates. Earlier cubic Hamiltonian phase-portrait papers address a structurally different (canonical Hamiltonian) subclass. Related period-function theory for separable Hamiltonians does not directly imply the present noncanonical original-time occupation law. Other cubic global-center Cauchy laws involve different vector fields and convergence scales. The new contribution is a sharp total-variation coefficient and the leading maximizing event for this skew nilpotent family.

## Limitations

This is a result for fixed real \((\alpha,\gamma)\) with \(\gamma\ne0\) and \(\alpha>\gamma^2/4\). The theorem does not establish parameter-uniform asymptotics at the discriminant boundary, perturbative persistence, higher-order coefficients, or uniqueness of an exactly maximizing event at finite energy. The originality assessment is based on accessible literature and mathematical search records; it cannot rule out unindexed equivalent formulations. Independent mathematical audit has not been performed.

## References

1. M. Corbera and C. Valls, *Global Nilpotent Reversible Centers with Cubic Nonlinearities Symmetric with Respect to the x-Axis*, Results in Mathematics **79** (2024), article 129. DOI: https://doi.org/10.1007/s00025-024-02163-x. First publicly available 2024-04-13.
2. F. S. Dias, J. Llibre and C. Valls, *Polynomial Hamiltonian systems of degree 3 with symmetric nilpotent centers*, Mathematics and Computers in Simulation **144** (2018), 60–77. DOI: https://doi.org/10.1016/j.matcom.2017.06.002.
3. M. Corbera and C. Valls, *Global nilpotent reversible centers with cubic nonlinearities symmetric with respect to the y-axis*, Rendiconti del Circolo Matematico di Palermo **73** (2024), 2383–2398. DOI: https://doi.org/10.1007/s12215-024-01046-y.
