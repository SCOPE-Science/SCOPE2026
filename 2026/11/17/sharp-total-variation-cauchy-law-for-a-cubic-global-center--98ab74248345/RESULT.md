# Sharp total-variation Cauchy law for a cubic global center

## Finding

Let \(\kappa>0\) and consider the **original-time** cubic differential system
\[
\dot x=(1+\kappa x^2)y,\qquad \dot y=-x.
\]
For every \(A>0\), let \(\Gamma_A\) be the periodic trajectory through \((A,0)\). Let \(\mu_A\) be the probability law of \(x(t)\) when \(t\) is uniform over one minimal physical-time period. Set \(L_A=\log(1+\kappa A^2)\), and let \(\mu_\infty\) be the Cauchy law with density
\[
f_\infty(x)=\frac{\sqrt\kappa}{\pi(1+\kappa x^2)}.
\]
The following **sharp first-order convergence in total variation** holds for all fixed \(\kappa>0\):
\[
\lim_{A\to\infty} L_A\,d_{\mathrm{TV}}(\mu_A,\mu_\infty)
=\frac{\operatorname{Cl}_2(\pi/3)}{\pi}
=0.3230659472194505\ldots,
\]
where \(d_{\mathrm{TV}}(\mu,\nu)=\sup_B|\mu(B)-\nu(B)|=\tfrac12\int|f-g|\) and
\[\operatorname{Cl}_2(\theta)=\sum_{n=1}^\infty\frac{\sin(n\theta)}{n^2}\]
is the Clausen function. More strongly, if \(f_A\) is the density of \(\mu_A\) (extended by zero off \((-A,A)\)), then
\[
\left\|L_A(f_A-f_\infty)-\frac{f_\infty}{2}
\left[\log(1+\kappa x^2)-2\log2\right]\right\|_{L^1(\mathbb R)}\longrightarrow0.
\]
The limiting signed density therefore describes the leading error for **every bounded observable simultaneously**, with a universal constant independent of \(\kappa\). Moreover, for all sufficiently large \(A\), the event of maximal positive discrepancy is **exactly** the intermediate strip \(x_*(A)<|x|<A\), where
\[
 u_*=L_A\left[1-\left(\frac{\pi}{J_{L_A}}\right)^2\right],\qquad
 x_*(A)=\frac{\sqrt{e^{u_*}-1}}{\sqrt\kappa},
 \]
with \(J_L\) defined in the proof. Its inner boundary has the explicit limit \(x_*(A)\to\sqrt{3/\kappa}\). This quantitative statement strengthens the known weak Cauchy occupation law; neither global-center existence, its exact finite-energy occupation density, nor the Cauchy weak limit is claimed new.

## Assumptions and scope

Fix any real \(\kappa>0\). Each amplitude \(A>0\) is the positive \(x\)-intercept of the trajectory, and \(L_A\to\infty\) as \(A\to\infty\). The measure uses the original differential-equation time, not a reparametrization. Total variation is on all Borel subsets of \(\mathbb R\), not only on compact test-function supports. The claimed \(L^1\) limit is for densities with respect to Lebesgue measure on the full real line. The endpoint \(\kappa=0\) and parameter-dependent joint limits are excluded.

## Proof

**1. Periodic levels and exact time density.** Direct differentiation proves conservation of
\[
H(x,y)=\frac{y^2}{2}+\frac{\log(1+\kappa x^2)}{2\kappa}.
\]
Every level \(H=E>0\) is a smooth compact oval containing no equilibrium, hence a periodic trajectory. For the level through \((A,0)\), the energy relation is
\[
\kappa y^2=L_A-\log(1+\kappa x^2),\qquad -A\le x\le A.
\]
Each interior \(x\) occurs twice per minimal period. As \(\dot x=(1+\kappa x^2)y\), the normalized original-time density is exactly
\[
f_A(x)=\frac{2\sqrt\kappa\,\mathbf1_{\{|x|<A\}}}{T_A(1+\kappa x^2)\sqrt{L_A-\log(1+\kappa x^2)}},
\]
where \(T_A\) is the minimal period. This exact density is a known starting point, not the new conclusion.

**2. A universal density ratio.** Put \(L=L_A\), \(U(x)=\log(1+\kappa x^2)\), and
\[
w(u)=\frac{1}{\sqrt{e^u-1}},\qquad
J_L=\int_0^L \frac{w(u)}{\sqrt{1-u/L}}\,du.
\]
Under the Cauchy law \(f_\infty(x)dx\), the variable \(U\) has density \(w(u)/\pi\) on \((0,\infty)\), because \(\theta=\arctan(\sqrt\kappa x)\) is uniform on \((-\pi/2,\pi/2)\) and \(U=-2\log|\cos\theta|\). In particular \(\int_0^\infty w(u)du=\pi\). Normalizing the displayed finite-energy density therefore yields the exact identity
\[
\frac{f_A(x)}{f_\infty(x)}=
\frac{\pi}{J_L}\frac{\mathbf1_{\{U(x)<L\}}}{\sqrt{1-U(x)/L}}.
\tag{1}
\]
Its normalization also gives \(T_A=2J_L/\sqrt L\), consistent with the established period law. Note that only \(L\), not \(\kappa\), appears in the ratio after the energy coordinate change.

**3. An \(L^1\)-accurate first correction.** Define \(W_L(u)=w(u)(1-u/L)^{-1/2}\mathbf1_{(0,L)}(u)\). Then
\[
L\bigl(W_L-w\bigr)\longrightarrow\frac{u}{2}w(u)
\quad\text{in }L^1((0,\infty)).\tag{2}
\]
For each fixed \(u>0\), the pointwise limit follows by Taylor expansion. To justify the moving endpoint, on \(0<u<L/2\) the mean-value theorem gives
\[
0\le L\left[(1-u/L)^{-1/2}-1\right]\le C u,
\]
so domination follows from the integrability of \(u w(u)\). On \(L/2<u<L\), \(w(u)\le C e^{-u/2}\), and
\[
L\int_{L/2}^{L}W_L(u)du\le C L^2e^{-L/4}\longrightarrow0.
\]
The omitted tail \(L\int_L^\infty w(u)du\) also vanishes exponentially. This proves (2) without incorrectly treating a finite cutoff as an infinite proof.

The exact Cauchy logarithmic moment is
\[
m:=\frac1\pi\int_0^\infty u w(u)du=2\log2,
\]
since under the uniform angle coordinate it equals \(-\tfrac4\pi\int_0^{\pi/2}\log\cos\theta\,d\theta=2\log2\). Integrating (2) gives
\[
J_L=\pi\left(1+\frac{\log2}{L}+o(L^{-1})\right).
\]
Combining the normalization with (2) gives the signed-density limit
\[
L\left[\frac{W_L}{J_L}-\frac{w}{\pi}\right]
\longrightarrow \frac{w(u)}{2\pi}(u-m)
\quad\text{in }L^1((0,\infty)).\tag{3}
\]
Because the finite-energy and limiting densities share the same symmetric sign distribution conditional on \(U\), the \(L^1\) distance between their signed-density corrections on \(\mathbb R\) equals the \(L^1\) distance between their counterparts in (3). Thus (3) proves the stronger assertion in Finding.

**4. Sharp total-variation coefficient.** Taking half the \(L^1\) norms in (3),
\[
\lim_{A\to\infty}L_A d_{\mathrm{TV}}(\mu_A,\mu_\infty)
=\frac14\,\mathbb E_{\mu_\infty}\left|U-2\log2\right|.
\]
With \(U=-2\log\cos\theta\), and using \(\int_0^{\pi/2}\log(2\cos\theta)d\theta=0\), the right side is
\[
\frac{2}{\pi}\int_0^{\pi/3}\log(2\cos\theta)d\theta
=\frac{\operatorname{Cl}_2(\pi/3)}{\pi}>0.
\]
The last equality follows by differentiating \(\operatorname{Cl}_2(\pi-2\theta)\): its derivative is \(2\log(2\cos\theta)\) for \(0<\theta<\pi/2\). The positive coefficient proves both that the rate is exactly of order \(1/L_A\) and that it cannot be improved uniformly in this family.

**5. The exact extremal event.** For \(L\) large, \(J_L>\pi\) by Step 3. On \(0<U<L\), the ratio (1) increases strictly from \(\pi/J_L<1\) to infinity; it equals one uniquely at \(u_*=L[1-(\pi/J_L)^2]\). Consequently \(\{x:x_*(A)<|x|<A\}\) is the positive set of the signed measure \(\mu_A-\mu_\infty\), and it attains the total-variation supremum. Let \(F_\infty(u)=\frac2\pi\arctan\sqrt{e^u-1}\), and let \(F_L(u)=J_L^{-1}\int_0^u w(v)(1-v/L)^{-1/2}dv\) for \(0\le u\le L\). The exact finite-energy formula, including the Cauchy tail outside the orbit support, is
\[
 d_{\mathrm{TV}}(\mu_A,\mu_\infty)
 =F_\infty(u_*)-F_L(u_*)+1-F_\infty(L).
\]
Finally Step 3 gives \(u_*\to2\log2\) and hence \(x_*(A)\to\sqrt{3/\kappa}\). This exact optimizing event makes the signed error geographically explicit.

## Verification

The supplied standard-library program `tools/verify.py` numerically integrates the **exact** finite-energy density after an endpoint-regularizing substitution, computes its unique likelihood-ratio crossing, and evaluates the exact total-variation distance at five increasing \(L\). Its reported rescaled distances converge toward the independently evaluated constant \(0.3230659472194505\ldots\). Exact conservation and normalization are established algebraically in the proof. The finite numerical checks are diagnostics only; convergence in (2)–(3) and the positive limiting constant are proved analytically.

## Relationship to prior work

Llibre and Rondón (2023), Theorem 2(g), provide the global-center classification for this cubic system (with \(\kappa=2d_1\) in their notation). Appis and Llibre (2024), Theorem 4(c), classify a **linearly conjugate** cubic center. Neither originating center-classification treatment states a sharp total-variation convergence law. A previously published result, *Cauchy time concentration and the order-one moment threshold in a cubic global center*, gives the **same** physical-time density, the weak Cauchy limit and sharp moment thresholds. These are acknowledged as prior conclusions; the novel assertion is the full first-order signed \(L^1\) expansion and its positive, exact total-variation coefficient. Those statements are not contained in its displayed theorems, its proof of weak convergence, or its stated limitations. The rate requires handling a moving integrable singularity at the finite-energy turning point, and does not follow from weak convergence or period asymptotics alone. Other available cubic-center occupation results concern different vector fields and limiting coordinates.

## Limitations

The leading first-order correction relies on fixed \(\kappa>0\) and \(A\to\infty\). The result is not a new global-center classification, Cauchy weak-limit theorem, moment classification, or period asymptotic. No uniform perturbation theorem or second-order total-variation coefficient is claimed. The novelty comparison covers accessible sources and mathematically relevant indexed records, but cannot exclude all unpublished or unindexed equivalent estimates; an independent audit has not been performed.

## References

1. J. Llibre and G. Rondón, *Global centers of a class of cubic polynomial differential systems*, arXiv:2310.07454v1 (first public 2023-10-11), Theorem 2(g), 2020 MSC primary 34C05, https://arxiv.org/abs/2310.07454; author preprint at https://ddd.uab.cat/pub/artpub/2024/303176/LliRon2023-preprint.pdf.
2. R. F. Appis and J. Llibre, *Global centers of a family of cubic systems*, Aequationes Mathematicae 98 (2024), 1373–1389, DOI:10.1007/s00010-024-01051-7; first publicly released 2024-04-05, full open article at https://link.springer.com/article/10.1007/s00010-024-01051-7.
3. *Cauchy time concentration and the order-one moment threshold in a cubic global center*, published research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-cauchy-time-concentration-and-the-order-one-moment-threshold-in--0ac06783efe2.
4. *Sharp logarithmic phase and time statistics in a cubic global center*, published research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-logarithmic-phase-and-time-statistics-in-a-cubic-global-ce--35ffbf168a22.
5. *Two-term boundary-period law and velocity skew for a cubic global center*, published research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-two-term-boundary-period-law-and-velocity-skew-for-a-cubic-globa--c61200f602fe.
