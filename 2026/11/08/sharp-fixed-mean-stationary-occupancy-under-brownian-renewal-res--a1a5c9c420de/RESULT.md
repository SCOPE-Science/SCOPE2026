# Sharp fixed-mean stationary occupancy under Brownian renewal resetting

## Finding
Fix a mean inter-reset duration \(\mu>0\), Brownian variance rate \(\sigma^2>0\), and an observation position \(x\in\mathbb R\setminus\{0\}\). Consider stationary Brownian motion whose independent cycles restart from the origin after i.i.d. strictly positive intervals \(S\) satisfying \(\mathbb ES=\mu\). Write \(f_S(x)\) for its stationary spatial probability density. Define
\[
 p_t(x)=\frac{\exp[-x^2/(2\sigma^2t)]}{\sqrt{2\pi\sigma^2t}},\qquad H_x(s)=\int_0^s p_t(x)\,dt.
\]
Let \(z_*\in(0,1/2)\) be the unique solution of
\[
 2\sqrt{\pi z_*}\,e^{z_*}\operatorname{erfc}(\sqrt{z_*})=1
\]
and let \(s_*(x)=x^2/(2\sigma^2z_*)\). Then
\[
 \boxed{\sup_{S>0,\,\mathbb ES=\mu} f_S(x)
 =\begin{cases}
 p_{s_*(x)}(x),&0<\mu<s_*(x),\\
 H_x(\mu)/\mu,&\mu\ge s_*(x).
 \end{cases}}
\]
For \(\mu\ge s_*(x)\), the unique maximizing inter-reset law is deterministic, \(S\equiv\mu\). For \(\mu<s_*(x)\), the supremum is **not attained** by any strictly positive inter-reset law; it is approached by the two-point laws supported on \(\{\varepsilon,s_*(x)\}\), with \(\varepsilon\downarrow0\) and the unique weights giving mean \(\mu\). Furthermore, for every admissible \(\mu\) and every \(x\ne0\), \(\inf f_S(x)=0\), and this infimum is not attained.

The universal transition is \(\sqrt{2z_*}=0.612003180962\ldots\): deterministic resetting is optimal exactly when \(|x|/(\sigma\sqrt\mu)\le\sqrt{2z_*}\). This is a pointwise stationary-density optimization, **not** a first-passage-time optimization.

## Assumptions and scope
The inter-reset intervals are i.i.d. on \((0,\infty)\) and have finite fixed mean \(\mu\). In each renewal cycle, an independent standard Brownian path starts at the origin and evolves with variance \(\operatorname{Var}(X_t)=\sigma^2t\). The observation occurs under the equilibrium (stationary) version of this regenerative process. It can be constructed for any such strictly positive finite-mean inter-reset law. No density, non-lattice condition, or second moment for \(S\) is needed. The stationary spatial probability measure is absolutely continuous because its equilibrium-age mixture is a mixture of nondegenerate Gaussian distributions. The target position \(x=0\) is excluded: the limiting behavior of \(p_t(0)\) near \(t=0\) differs crucially.

## Proof
**1. Renewal reward and exact density.** For stationary inter-reset duration \(S\), the stationary age \(A\) obeys
\[
 \Pr(A\in dt)=\frac{\Pr(S>t)}{\mu}\,dt.
\]
The Brownian position conditional on age \(t\) has density \(p_t(x)\), so Tonelli gives, for each \(x\ne0\),
\[
 f_S(x)=\frac1\mu\int_0^\infty\Pr(S>t)p_t(x)\,dt
 =\frac1\mu\mathbb E H_x(S).
\]
The mixture is finite: \(p_t(x)\) is bounded on \((0,\infty)\) for every \(x\ne0\), and \(\mathbb ES=\mu\). Direct integration yields
\[
 H_x(s)=\frac{2\sqrt{s}}{\sigma\sqrt{2\pi}}
 \exp\!\left(-\frac{x^2}{2\sigma^2s}\right)
 -\frac{|x|}{\sigma^2}
 \operatorname{erfc}\!\left(\frac{|x|}{\sigma\sqrt{2s}}\right).
\]

**2. The unique positive tangent-from-the-origin point.** Put \(a=x^2/\sigma^2\) and \(h(s)=p_s(x)\). Differentiation shows
\[
 \frac{h'(s)}{h(s)}=\frac{a-s}{2s^2}.
\]
Thus \(h\) is strictly increasing on \((0,a)\) and strictly decreasing on \((a,\infty)\), while \(H_x'(s)=h(s)\). Define \(R(s)=H_x(s)-s h(s)\). Then \(R'(s)=-s h'(s)\): \(R\) decreases strictly from \(R(0+)=0\) on \((0,a)\), then increases strictly on \((a,\infty)\). Since
\[
 H_x(s)\sim\frac{2\sqrt{s}}{\sigma\sqrt{2\pi}},\qquad
 s h(s)\sim\frac{\sqrt{s}}{\sigma\sqrt{2\pi}}
 \quad(s\to\infty),
\]
we have \(R(s)\to+\infty\). There is exactly one root \(s_*>a\), and \(H_x(s_*)=s_*h(s_*)\). The explicit expression for \(H_x\) gives
\[
 2\sqrt{\pi z}\,e^z\operatorname{erfc}(\sqrt z)=1,
 \quad z=\frac{x^2}{2\sigma^2s_*}\in(0,1/2).
\]
Existence/uniqueness of this \(z_*\) follows from the unique root just proved, without assuming special-function monotonicity.

**3. Exact concave majorant.** Since
\[
 \left(\frac{H_x(s)}s\right)'=-\frac{R(s)}{s^2},
\]
the ratio strictly increases up to \(s_*\) and strictly decreases thereafter. The function
\[
 G(s)=\begin{cases}s h(s_*),&0\le s\le s_*,\\
 H_x(s),&s\ge s_*,\end{cases}
\]
is concave: the left branch is linear; at \(s_*\), its slope \(h(s_*)\) agrees with \(H_x'(s_*)\); and \(H_x''(s)=h'(s)<0\) for \(s\ge s_*>a\). Also \(G(s)\ge H_x(s)\), strictly for \(0<s<s_*\); both equal at \(0\) and from \(s_*\) onward. Consequently, for any allowed reset law,
\[
 \mathbb EH_x(S)\le\mathbb EG(S)\le G(\mathbb ES)=G(\mu).
\]
Dividing by \(\mu\) gives the stated upper envelope. When \(\mu\ge s_*\), \(S=\mu\) attains it. Equality requires \(S\) to avoid \((0,s_*)\), and Jensen equality for \(G\). As \(G\) is strictly concave on \((s_*,\infty)\) and linear only up to \(s_*\), these requirements and \(\mathbb ES\ge s_*\) force \(S\equiv\mu\); uniqueness holds also at \(\mu=s_*\).

**4. Sharpness and nonattainment below threshold.** For \(0<\mu<s_*\), select \(0<\varepsilon<\mu\), let
\[
 \Pr(S=s_*)=\frac{\mu-\varepsilon}{s_*-\varepsilon},\qquad
 \Pr(S=\varepsilon)=\frac{s_*-\mu}{s_*-\varepsilon}.
\]
As \(\varepsilon\downarrow0\), \(H_x(\varepsilon)\to0\), and the stationary density tends to
\[
 \frac{\mu H_x(s_*)/s_*}{\mu}=h(s_*).
\]
Every strictly positive law with mean below \(s_*\) assigns positive probability to \((0,s_*)\), where \(H_x<G\); hence it cannot attain the bound.

**5. Exact lower infimum.** For \(0<\varepsilon<\mu<M\), take the unique two-point law on \(\{\varepsilon,M\}\) with mean \(\mu\). Choose \(\varepsilon\downarrow0\), \(M\to\infty\). Since \(H_x(\varepsilon)\to0\) and \(H_x(M)=O(\sqrt M)\), the resulting \(f_S(x)\to0\). But \(H_x(s)>0\) for every \(s>0\), so no admissible reset law attains zero.

## Verification
The companion standalone `verify_envelope.py` evaluates the special-function root, checks the tangency identity, compares the explicit integrated Gaussian kernel with independent numerical quadrature, and tests the sharp upper envelope against many admissible two-point laws. In the baseline \(x=\sigma=\mu=1\), the optimized stationary density is approximately \(0.202456490188025\), whereas deterministic resetting gives \(0.166630941175373\). The 430 numerical assertions passed in a local execution using Python 3 and SciPy. These are diagnostics; the arbitrary-law theorem follows from the proof above.

## Relationship to prior work
Assefa, Keller-Ressel and Palmowski (2026) prove general polynomial-process moment and cross-moment formulas for independent renewal resetting. This result studies a distinct stationary pointwise density objective, not addressed by their polynomial-moment formulas. Eule and Metzger (2016) and Masoliver and Montero (2019) already derive general renewal-reset stationary-distribution representations. The renewal-reward identity above is therefore **not** claimed as novel; the addition is the exact distribution-free fixed-mean optimization, tangent threshold, extremizers, and attainment/nonattainment classification. The 2016 work also compares stationary density profiles in Gamma/Weibull subfamilies and optimizes mean first-passage time, a different functional. Existing general concave-envelope moment theory may subsume the abstract optimization technique; the model-specific threshold and physical interpretation are the targeted new facts.

## Limitations
This is an exact pointwise result for one-dimensional driftless Brownian motion, origin resetting, a single specified nonzero target position, and a fixed positive finite mean inter-reset duration. It does not find one reset law simultaneously maximizing density at all positions, does not optimize hitting times, and does not cover spatially dependent, state-triggered or correlated reset clocks. At the far-field optimum, the maximizing law is a supremum limit involving vanishing reset intervals, rather than an admissible strictly positive law. Prior-art comparison was targeted rather than exhaustive; a more general unknown extremal-occupation theorem could affect historical priority. Independent mathematical verification has not been performed.

## References
- J. Assefa, M. Keller-Ressel and Z. Palmowski, *Moments of polynomial processes under affine resetting*, arXiv:2610.01363v1 (first public 2026-10-01), https://arxiv.org/html/2610.01363v1.
- S. Eule and J. J. Metzger, *Non-equilibrium steady states of stochastic processes with intermittent resetting*, New Journal of Physics 18 (2016), 033006, arXiv:1510.07876, https://arxiv.org/abs/1510.07876.
- J. Masoliver and M. Montero, *Anomalous diffusion under stochastic resettings: A general approach*, Physical Review E 100 (2019), 042103, https://doi.org/10.1103/PhysRevE.100.042103.
