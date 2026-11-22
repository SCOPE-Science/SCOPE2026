# A sharp cold-contact bias for reliable work extraction in a two-temperature Brownian Otto cycle

## Finding

In a periodically operated, one-dimensional overdamped harmonic Otto engine with instantaneous stiffness jumps, two thermal contacts of a fixed combined duration, and **equal coordinate-relaxation rates** during the two contacts, the hot-contact duration that maximizes the single-cycle work reliability is unique and is always *strictly shorter than half the available time*. The same allocation uniquely maximizes the **exact probability** that an individual cycle extracts positive mechanical work. In contrast, the mean extracted work is uniquely maximized by equal hot and cold durations. The reliability-optimal split is characterized by one explicitly given cubic root, for every cycle duration and every genuine engine temperature contrast.

Write \(k_h>k_c>0\) for harmonic stiffnesses and \(T_h>T_c>0\) for bath temperatures. Set \(H=T_h/k_h\), \(C=T_c/k_c\), and assume \(h=H/C>1\). For the common coordinate-decay rate \(\lambda>0\) and fixed total contact time \(\tau>0\), put
\[
z=e^{-2\lambda\tau}\in(0,1),\quad a=e^{-2\lambda\tau_h},\quad b=e^{-2\lambda\tau_c}=z/a,\quad 0<\tau_h<\tau,\quad \tau_c=\tau-\tau_h.
\]
Let \(u_*\) be the **unique positive root** of
\[
 u^3-z\bigl[h(1+z)+1\bigr]u-2hz^2=0.
\]
The common unique maximizer of reliability and positive-cycle probability is
\[
 a_* = \frac{z+u_*}{1+u_*},\quad
 \tau_h^*=-\frac{\log a_*}{2\lambda},\quad
 0<\tau_h^*<\frac\tau2<\tau_c^*.
\]
Mean extracted work instead has the unique maximizer \(a=\sqrt z\), or \(\tau_h=\tau_c=\tau/2\).

The short-cycle and long-cycle laws sharpen this separation. With \(u_0=(1+\sqrt{1+8h})/2\),
\[
 \lim_{\tau\downarrow0}\frac{\tau_h^*}{\tau} = \frac{1}{1+u_0}<\frac12,
 \qquad
 \tau_h^*=\frac\tau2-\frac{\log(h+1)}{4\lambda}+o(1)\quad(\tau\to\infty).
\]
The latter offset is dimensionful and applies with fixed \(h,\lambda>0\).

## Assumptions and scope

During the hot and cold contacts, respectively, the position obeys the Itô equations
\[
 dX_t=-\lambda X_t\,dt+\sqrt{\frac{2\lambda T_h}{k_h}}\,dB_t,
 \qquad dX_t=-\lambda X_t\,dt+\sqrt{\frac{2\lambda T_c}{k_c}}\,dB_t,
\]
with independent Brownian increments on disjoint intervals. The bath and stiffness switch simultaneously, without displacement jumps or additional mechanical driving during a contact; the two instantaneous stiffness changes perform the only mechanical work. Equal decay rates can be realized by different mobilities \(\mu_i=\lambda/k_i\), so they are an explicit restriction, not a generic property of fixed-mobility traps. Units are chosen with Boltzmann's constant equal to one. Consider the unique periodic steady Gaussian regime and the mechanical work \(W\) **of one specified cycle**, not the variance rate of the sum of many correlated cycles.

At the beginning of the hot contact let the coordinate be \(X_0\), and at its end let it be \(X_1\). With \(\Delta k=k_h-k_c>0\), the mechanical work extracted during the two instantaneous changes equals
\[
 W=\frac{\Delta k}{2}(X_1^2-X_0^2).
\]
Define the single-cycle reliability \(\mathcal R=\mathbb E W/\sqrt{\operatorname{Var} W}\) and success probability \(\mathcal P=\Pr\{W>0\}\). The engine condition \(H>C\) ensures \(\mathbb E W>0\) for every split strictly inside the interval.

## Proof

**Step 1: period-stationary Gaussian covariance.** For a duration whose squared attenuation factor is \(a\), a contact with equilibrium variance \(H\) maps an incoming variance \(V\) to \(aV+(1-a)H\). Denoting \(V_0=\operatorname{Var}(X_0)\), \(V_1=\operatorname{Var}(X_1)\), periodicity and the cold contact give
\[
 V_1=aV_0+(1-a)H,\qquad V_0=bV_1+(1-b)C.
\]
The unique solution, using \(ab=z\), is
\[
 \frac{V_0}{C}=\frac{1-zh+z(h-1)/a}{1-z},\qquad
 \frac{V_1}{C}=\frac{h-z-a(h-1)}{1-z}.
\]
Both variances are positive. Conditional linear regression in the hot contact also gives
\[
 \operatorname{Cov}(X_0,X_1)=\sqrt a\,V_0.
\]
Thus \((X_0,X_1)\) is a centered, nondegenerate bivariate Gaussian for all \(z<a<1\). Its variance difference equals
\[
 \Delta:=V_1-V_0=C\frac{(h-1)(1-a)(a-z)}{a(1-z)}>0.
\]

**Step 2: mean, reliability, and exact success probability.** Wick's Gaussian fourth-moment identity gives
\[
 \mathbb E W=\frac{\Delta k}{2}\Delta,\qquad
 \operatorname{Var}W=\frac{(\Delta k)^2}{2}T,
 \quad T=V_1^2+V_0^2-2aV_0^2>0.
\]
Hence
\[
 \mathcal R=\frac{\Delta}{\sqrt{2T}}.
\]
The factor \((1-a)(a-z)/a=1+z-a-z/a\) has a unique maximum at \(a=\sqrt z\), proving the statement about mean work.

For the exact non-Gaussian work-sign event, factor \(X_1^2-X_0^2=(X_1-X_0)(X_1+X_0)\). Set \(Y=X_1-X_0\), \(Z_+=X_1+X_0\). These centered Gaussian variables have correlation
\[
 \rho=\frac{V_1-V_0}{\sqrt{(V_1+V_0)^2-4aV_0^2}}
 =\frac{\mathcal R}{\sqrt{1-\mathcal R^2}}\in(0,1).
\]
The Gaussian quadrant formula, obtained by angular integration of a standard bivariate normal, gives
\[
 \mathcal P=\Pr(YZ_+>0)=\frac12+\frac1\pi\arcsin\rho.
\]
The derivative of \(r\mapsto\arcsin(r/\sqrt{1-r^2})\) is positive on \(0<r<1/\sqrt2\). Consequently maximizing reliability and maximizing **the actual one-cycle probability**, not a normal approximation to work, are exactly equivalent.

**Step 3: one critical point and its position.** Since \(\mathcal R>0\), maximize \(\mathcal R^2=\Delta^2/(2T)\). Change variables monotonically via
\[
 u=\frac{a-z}{1-a}\in(0,\infty),\qquad a=\frac{z+u}{1+u}.
\]
Direct differentiation and cancellation using the displayed rational forms for \(V_0,V_1\) yields the **exact identity**
\[
 T^2\frac{d}{da}\left(\frac{\Delta^2}{T}\right)
 =\frac{2h(h-1)^2u(1-z)^2}{a^4(1+u)^6}\,
 \underbrace{\Bigl(2hz^2+z[h(1+z)+1]u-u^3\Bigr)}_{F(u)}\,C^4.
\]
Every factor outside \(F\) is strictly positive. [The factor \(C^4\) follows because both \(\Delta\) and \(T^{1/2}\) have length-squared units.] Now \(F(0)=2hz^2>0\), while
\[
 F'(u)=z[h(1+z)+1]-3u^2
\]
is positive up to one positive point and negative thereafter. Also \(F(u)\to-\infty\) as \(u\to\infty\). Thus \(F\) has exactly one positive root, and reliability strictly increases before, then strictly decreases after it. The endpoints correspond to zero contact time and \(\Delta\to0\), so this is the unique *global* maximizer.

At the mean-optimal split \(a=\sqrt z\), the variable is \(u=\sqrt z\) and
\[
 F(\sqrt z)=hz^{3/2}(1+\sqrt z)^2>0.
\]
The root therefore satisfies \(u_*>\sqrt z\), hence \(a_*>\sqrt z\) and \(\tau_h^*<\tau/2\) strictly. All equalities and inequalities are exact for every allowed parameter.

**Step 4: asymptotics.** Put \(L=2\lambda\tau\), so \(z=e^{-L}\). As \(L\downarrow0\), the unique positive root converges to the positive root of \(u^3-(2h+1)u-2h=0\), factoring as \((u+1)(u^2-u-2h)=0\). This root is \(u_0=(1+\sqrt{1+8h})/2\). Since \(1-a_*=(1-z)/(1+u_*)\), one obtains \(\tau_h^*/\tau\to 1/(1+u_0)\). As \(z\downarrow0\), the same cubic implies \(u_*/\sqrt z\to\sqrt{h+1}\). Consequently \(a_*/\sqrt z\to\sqrt{h+1}\), and \(-\log a_*=-\tfrac12\log z-\tfrac12\log(h+1)+o(1)\), giving the stated long-period offset.

## Verification

The companion `verify.py` reconstructs the covariance recursion from both contacts, checks the work mean and the exact factorization of the reliability derivative by symbolic algebra, proves algebraically that the derivative's reduced cubic equals the one stated, verifies the sign at the equal-time split, and checks the Gaussian quadrant-correlation identity. It also tests the analytic root against dense interior time splits for 49 independent temperature/duration parameter pairs and checks the physical recursion directly. Running `python verify.py` with Python 3, SymPy, NumPy, and SciPy prints an explicit PASS line (numerical assertions supplement the proof rather than implying exhaustive verification).

For illustration only, let \(h=2\) and \(2\lambda\tau=2\). Then \(a_*\approx0.5020073753\), \(\tau_h^*/\tau\approx0.344570234\), \(\mathcal R_*\approx0.188954834\), and \(\mathcal P_*\approx0.561634\). Equal dwell durations instead yield \(\mathcal R\approx0.176642027\) and \(\mathcal P\approx0.557436\). These are computed from the exact formulas, not used to establish uniqueness.

## Relationship to prior work

The setting is motivated by the established theory of finite-contact Otto cycles and stochastic work fluctuations. Zheng, Hänggi, and Poletti (2016) examine the time allocated to dissipative and work strokes in a **quantum** Otto engine and optimize mean work or efficiency, not the exact sign probability or single-cycle reliability of the equal-decay-rate overdamped model. Iida, Negoro, and Yamada (2022) derive work/heat second moments for a different **continuously breathing** harmonic Brownian engine; they discuss a Gaussian approximation to success probability but do not prove its equality with reliability optimization. Shastri and Venkatesh (2022), in a quantum Otto engine, optimize the asymmetry of the **unitary work strokes**, while fixing hot/cold bath-contact asymmetry in their main fluctuation optimization. General Gaussian and covariance methods are standard; the contribution claimed here is solely the globally unique, explicit cubic cold-biased contact-time allocation, its exact co-optimization of the non-Gaussian work-sign probability, and its strict contrast with the mean-optimal split.

## Limitations

The equal coordinate-relaxation-rate assumption may require independent mobility control when stiffness differs; it is not automatic for a single fixed-mobility particle. The result concerns a single cycle sampled from the periodic stationary regime and does not optimize the variance rate of accumulated correlated work over many cycles. The two stiffness jumps are ideal and costless in duration; switching-device costs, bath setup costs, and mobility control costs are excluded. The model does not cover inertia, nonlinear potentials, unequal relaxation rates, or finite-sample work estimation. The mathematical originality assessment remains vulnerable to a stronger implicit result elsewhere; it does not establish publication priority or independent validation.

## References

- Y. Zheng, P. Hänggi, and D. Poletti, “Occurrence of discontinuities in the performance of finite-time quantum Otto cycles,” *Phys. Rev. E* **94**, 012137 (2016). https://doi.org/10.1103/PhysRevE.94.012137 . Full available text: https://www.physik.uni-augsburg.de/theo1/hanggi/Papers/685.pdf .
- S. Iida, K. Negoro, and K. Yamada, “Second moments of work and heat for a single-particle stochastic heat engine in a breathing harmonic potential,” *Prog. Theor. Exp. Phys.* **2022**, 043A02; first public preprint 2021-05-26 (arXiv:2105.12541); journal publication 2022-03-22. https://arxiv.org/abs/2105.12541 ; https://doi.org/10.1093/ptep/ptac051 ; https://academic.oup.com/ptep/article/2022/4/043A02/6552151 .
- R. Shastri and B. P. Venkatesh, “Optimization of asymmetric quantum Otto engine cycles,” arXiv:2204.04782 (first posted 2022-04-10); *Phys. Rev. E* **106**, 024123 (2022). https://arxiv.org/abs/2204.04782 ; https://doi.org/10.1103/PhysRevE.106.024123 .
