# Two sign observations of Brownian-bridge energy: exact Bayes risk and strict optimal reflection symmetry

## Finding
Let \(B\) be a standard centered Brownian bridge on \([0,1]\), and estimate its integrated quadratic energy
\[
Q=\int_0^1B(u)^2\,du
\]
from two predetermined noiseless signs \(S_s=\operatorname{sgn}(B(s))\) and \(S_t=\operatorname{sgn}(B(t))\). For \(0<s<t<1\), set
\[
\rho=\sqrt{\frac{s(1-t)}{t(1-s)}},\qquad
m=\frac2\pi\arcsin\rho,\qquad V=S_sS_t.
\]
Then the exact minimum mean-square estimator among all measurable functions of the **two observed signs** is
\[
\widehat Q_{s,t}=\frac16+\frac{2\sqrt{s(t-s)(1-t)}}{3\pi(1-m^2)}(V-m),
\]
and its unconditional squared Bayes risk is
\[
\boxed{R(s,t)=\frac1{45}-\frac{4s(t-s)(1-t)}{9\pi^2\bigl[1-(\frac2\pi\arcsin\rho)^2\bigr]}.}
\]
Every distinct interior pair has positive variance reduction. Any *single* sign, a coincident pair, or a pair containing a pinned endpoint yields no reduction and has risk \(1/45\).

**Strict global placement theorem.** Over *all* nonadaptive ordered pairs \(0\le s\le t\le1\), every Bayes-risk minimizer satisfies
\[
\boxed{s+t=1,\qquad \frac13<s<t<\frac23.}
\]
The global optimum is characterized without a two-variable search: its explained fraction of \(\operatorname{Var}(Q)\) equals
\[
\boxed{\max_{0<\rho<1}\Phi(\rho),\qquad
\Phi(\rho)=\frac{20}{\pi^2}\frac{\rho^2(1-\rho)}{(1+\rho)^3\bigl[1-(\frac2\pi\arcsin\rho)^2\bigr]},}
\]
and each maximizing \(\rho\) gives the pair \((s,t)=(\rho/(1+\rho),1/(1+\rho))\). The maximum is attained in \((1/2,1)\). At the exactly specified trisection pair \((1/3,2/3)\), the explained variance fraction equals \(5/(6\pi^2)\), and the true optimum improves it strictly. **Uniqueness of the one-dimensional maximizer is not asserted.**

## Assumptions and scope
The prior is precisely the zero-endpoint standard Gaussian bridge with covariance \(K(x,y)=\min(x,y)-xy\). Times are fixed before observing the path; there is no measurement noise, adaptation, threshold adjustment, or restriction on the estimator other than measurability with respect to the two signs and finite squared loss. At zero-valued pinned endpoints the sign carries no information, independent of how it is encoded. The target is the unweighted integral of the *squared bridge*, not the integral of the bridge itself. Squared risk means \(\mathbb E[(Q-\widehat Q)^2]\), averaged jointly over the bridge and the signs.

## Proof
**1. Gaussian sign moments.** Let \((X,Y)\) be a centered standard bivariate Gaussian pair with correlation \(0<\rho<1\), and put \(V=\operatorname{sgn}(X)\operatorname{sgn}(Y)\). The standard Gaussian orthant integral gives \(\mathbb EV=m=(2/\pi)\arcsin\rho\). The second-moment covariance matrix is
\[
\mathbb E\bigl[(ZZ^{\mathsf T}-\Sigma)(V-m)\bigr]
=\frac{2\sqrt{1-\rho^2}}{\pi}
\begin{pmatrix}\rho&1\\1&\rho\end{pmatrix},\qquad
Z=(X,Y)^{\mathsf T},\quad \Sigma=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix}.
\]
To verify the diagonal entry directly, condition on \(X=x\), write \(k=\rho/\sqrt{1-\rho^2}\), and use \((x^2-1)\varphi(x)=-(x\varphi(x))'\):
\[
\mathbb E[(X^2-1)V]
=2\int_0^\infty(x^2-1)\varphi(x)(2\Phi(kx)-1)\,dx
=4k\int_0^\infty x\varphi(x)\varphi(kx)\,dx
=\frac{2\rho\sqrt{1-\rho^2}}\pi.
\]
The off-diagonal entry follows by integrating the conditional folded-normal mean, equivalently from
\(\mathbb E|XY|=2[\sqrt{1-\rho^2}+\rho\arcsin\rho]/\pi\): subtracting \(\rho m\) gives \(2\sqrt{1-\rho^2}/\pi\). The other diagonal is symmetric. Thus the moment identity is derived rather than assumed.

**2. Exact energy-sign covariance.** Standardize the two bridge samples to \(Z=(B(s)/\sqrt{s(1-s)},B(t)/\sqrt{t(1-t)})^{\mathsf T}\) and let
\[
M_{ij}=\int_0^1\operatorname{Cov}(B(u),Z_i)\operatorname{Cov}(B(u),Z_j)\,du.
\]
Gaussian regression gives
\[
\mathbb E[Q\mid Z]=\mathbb EQ-\operatorname{tr}(\Sigma^{-1}M)+Z^{\mathsf T}\Sigma^{-1}M\Sigma^{-1}Z.
\]
Direct piecewise integration of \(K(u,s)K(u,t)\) shows
\[
M_{11}=\frac{s(1-s)}3,\quad M_{22}=\frac{t(1-t)}3,\quad
M_{12}=\frac{\rho(2t-t^2-s^2)}6.
\]
In particular \(2M_{12}-\rho(M_{11}+M_{22})=\rho(t-s)/3\). Taking the covariance of the displayed regression quadratic with \(V\) and using Step 1 yields
\[
\operatorname{Cov}(Q,V)
=\frac{2[2M_{12}-\rho(M_{11}+M_{22})]}{\pi\sqrt{1-\rho^2}}
=\boxed{\frac{2}{3\pi}\sqrt{s(t-s)(1-t)}}.
\]
The final equality follows from \(1-\rho^2=(t-s)/[t(1-s)]\).

**3. Exact conditional decoder and risk.** Reflection \(B\mapsto-B\) leaves \(Q\) fixed and simultaneously flips both signs. Hence \(\mathbb E[Q\mid S_s,S_t]\) has just two possible values, depending on \(V=\pm1\). Orthogonal projection onto \(\operatorname{span}\{1,V\}\) is exactly the conditional expectation, so
\[
\widehat Q=\mathbb EQ+\frac{\operatorname{Cov}(Q,V)}{1-m^2}(V-m).
\]
Here \(\mathbb EQ=\int_0^1u(1-u)\,du=1/6\) and, by Wick's identity and Fubini, \(\operatorname{Var}Q=2\iint K(u,v)^2\,du\,dv=1/45\). Substitution proves the estimator and risk. A single sign has no information about the even functional \(Q\) by the same global reflection. The risk extends continuously to repeated or endpoint placements with zero explained variance: as \(t-s\downarrow0\), \(1-m^2\) has order \(\sqrt{1-\rho}\) while the numerator has order \(t-s\), and away from coincidence the numerator vanishes at either pinned endpoint. Thus no degenerate design can be optimal because distinct interior designs yield a strict improvement.

**4. Every global optimizer is reflection-paired.** Write the three positive gaps as \(a=s\), \(b=t-s\), \(c=1-t\), so \(a+b+c=1\), and define \(z=ac\), \(r=\rho^2\in(0,1)\), \(k=(1-r)/r>0\). The correlation identity becomes
\[
 r=\frac{ac}{ac+b}=\frac z{z+b},\qquad b=kz,\quad a+c=1-kz.
\]
For fixed \(r\), the denominator of the risk improvement is constant, whereas its numerator is \(abc=kz^2\), strictly increasing in \(z\). By AM–GM, feasibility requires \(z=ac\le(1-kz)^2/4\). On \(0<z<1/k\), the right side minus \(z\) is strictly decreasing, so its unique zero is the largest feasible \(z\); equality holds precisely when \(a=c\). Therefore every asymmetric design is strictly dominated by a symmetric design of the **same sign correlation**. Every global optimizer has \(a=c\), hence \(t=1-s\). Solving the correlation relation gives \(s=\rho/(1+\rho)\), \(t=1/(1+\rho)\), and substitution yields the scalar objective \(\Phi\).

**5. Strict improvement over trisection and existence.** Set \(q(\rho)=\rho^2(1-\rho)/(1+\rho)^3\) and \(d(\rho)=1-(2\arcsin\rho/\pi)^2\). For \(0<\rho<1\), \(d\) decreases strictly and
\[
\frac{q'(\rho)}{q(\rho)}=\frac{2(1-2\rho)}{\rho(1-\rho^2)}.
\]
Thus \(\Phi\) increases strictly on \((0,1/2]\), including a positive one-sided derivative at \(1/2\). Also \(\Phi(\rho)\to0\) as \(\rho\downarrow0\) and as \(\rho\uparrow1\) (for the latter, \(d\) is of order \(\sqrt{1-\rho}\), while \(q\) is of order \(1-\rho\)). An interior maximum therefore exists and all maximizing correlations are greater than \(1/2\). This is exactly \(1/3<s<t<2/3\) together with reflection symmetry. At \(\rho=1/2\), \(q=1/27\) and \(d=8/9\), so \(\Phi=5/(6\pi^2)\). Since the derivative there is positive, the optimum is strictly better.

## Verification
Run \(`python verify.py`\) with the versions in \(`requirements.txt`\). The self-contained script checks the kernel convolution by symbolic exact integration; the sign-moment matrix reduction; the bridge cancellation; the fixed-correlation reflection identities; eight high-precision one-dimensional Gaussian integrals for the two needed sign moments; four independent conditional-regression covariance comparisons; and the exact trisection benchmark. An illustrative root of the **scalar stationarity equation** is \(\rho\approx0.56688482933339335\), suggesting approximately \(8.59764\%\) variance recovery. This numerical observation neither proves that the root is the sole stationary point nor replaces the established global reflection-symmetry and trisection-improvement theorems.

## Relationship to prior work
Pronzato and Zhigljavsky (2018) develop Gaussian-kernel quadrature and optimal point designs for **linear integrals of full-valued Gaussian fields**, not quadratic path energy decoded from two binary signs. Dirksen, Maly and Rauhut (2021) treat one-bit covariance recovery and the Gaussian arcsine identity, which is used here but does not supply an integrated-energy Bayes-risk/placement result. Fesl, Koller and Utschick (2022) study conditional-mean reconstruction in one-bit **Gaussian channel** models; their estimation targets are Gaussian input vectors, unlike this quadratic non-Gaussian path functional. A published two-node Brownian-bridge kernel design optimizes an **i.i.d. node distribution** for a **linear** integration target and full point values; it does not imply the present fixed deterministic sign-only design theorem. Another published bridge-energy identity concerns covariance with **local time**, not with two prescribed signs. Exact-value bridge-energy observation designs and two-sign bridge **linear-area** designs are different information models/targets and do not dominate these statements.

## Limitations
No uniqueness of the maximizing scalar correlation \(\rho\) is proved. The displayed numerical stationary point is an illustration only, not a mathematically certified global optimum. The result does not optimize adjusted comparator thresholds, adaptive sensors, random sites, noisy bits, more than two signs, alternative integration weights, or other Gaussian bridges. Historical priority is assessed against the accessible indexed records and inspected literature, not independently certified; unidentified earlier Gaussian quadratic-sign design results remain possible.

## References
1. L. Pronzato and A. Zhigljavsky, *Bayesian quadrature and energy minimization for space-filling design*, arXiv:1808.10722v1, first public 2018-08-31, Sections 2.2 and 4, https://arxiv.org/html/1808.10722v1.
2. S. Dirksen, J. Maly and H. Rauhut, *Covariance estimation under one-bit quantization*, arXiv:2104.01280v1, first public 2021-04-02, Gaussian arcsine moment identity and main covariance estimation sections, https://arxiv.org/html/2104.01280v2.
3. B. Fesl, M. Koller and W. Utschick, *On the Mean Square Error Optimal Estimator in One-Bit Quantized Systems*, arXiv:2212.04470v1, first public 2022-12-08, Sections III–IV, https://arxiv.org/html/2212.04470v2.
4. *Unique optimal i.i.d. two-node design for Brownian-bridge kernel quadrature*, published mathematical record, RESULT.md, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-unique-optimal-i-i-d-two-node-design-for-brownian-bridge-kernel--1c7b05ec88c4/RESULT.md.
5. *Exact local-time covariance hierarchy for Brownian-bridge power energies*, published mathematical record, RESULT.md, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-exact-local-time-covariance-hierarchy-for-brownian-bridge-power--2ef033b22d4d/RESULT.md.
