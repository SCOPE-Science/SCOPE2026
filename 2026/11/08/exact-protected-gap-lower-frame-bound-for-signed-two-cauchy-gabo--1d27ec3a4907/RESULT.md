# Exact protected-gap lower frame bound for signed two-Cauchy Gabor windows

## Finding

A signed pair of Cauchy kernels can have a *protected, bounded island of critical-density Gabor stability* between two separate non-frame intervals. Throughout this island, the **optimal lower frame bound is exactly the minimum of two explicit quadratics**, not merely bounded below by them. The same formula identifies the unique residue ratio maximizing the lower frame bound with the first residue fixed.

Fix a translation period \(\alpha>0\), two real pole heights \(0<w_1<w_2\), and a nonzero complex coefficient \(a\). For each real \(R>0\), set
\[
 g_R(t)=\frac{a}{t-iw_1}-\frac{aR}{t-iw_2},\qquad
 \mathcal G_R=\{e^{2\pi i n t/\alpha}g_R(t-m\alpha):m,n\in\mathbb Z\}.
\]
Put \(u=e^{-2\pi w_1/\alpha}\), \(v=e^{-2\pi w_2/\alpha}\), so \(0<v<u<1\), and define
\[
 L=\frac{u(1+v)}{v(1+u)},\qquad
 H=\frac{1-v}{1-u},\qquad
 K=\frac{4\pi^2|a|^2}{\alpha}.
\]
There is a nonempty *protected* residue interval \(L<R<H\), between two non-frame intervals, if and only if
\[
 \boxed{u+v+uv>1.}
\]
When this strict inequality holds, the system \(\mathcal G_R\) is a Gabor frame for every \(R\in(L,H)\), and its **largest valid lower squared frame bound**, i.e., the optimal constant \(A_R\) in
\[
 A_R\|f\|_2^2\le\sum_{m,n\in\mathbb Z}
 |\langle f,e^{2\pi i nt/\alpha}g_R(t-m\alpha)\rangle|^2,
 \qquad f\in L^2(\mathbb R),
\]
is exactly
\[
 \boxed{A_R=K\min\left\{
 \left(\frac{v}{1+v}(R-L)\right)^2,
 \left(\frac{H-R}{1-v}\right)^2\right\}.}
\]
Both terms are attained as one-sided limiting Zak fibers, respectively at the anti-periodic point \((\omega,x)=(0,\alpha/2)\) and periodic point \((1/\alpha,0)\). No interior Zak fiber gives a smaller value.

More precisely, on the negative-residue ray \(R>0\) the two *individual* non-frame intervals are
\[
 I_-=[L v/u,L],\qquad I_+=[H,H u/v].
\]
Every parameter \(R\) in their union fails the frame property. They have an intervening positive-length frame interval precisely under \(u+v+uv>1\). This qualitative arrangement serves to specify the domain of the quantitative result; the new point is the **exact, sharp stability law throughout the intervening interval**.

With \(a,\alpha,w_1,w_2\) fixed and \(L<H\), the unique ratio maximizing the lower frame bound *within that interval* is
\[
 \boxed{R_*=\frac{(1+v)H+v(1-v)L}{1+2v-v^2},\qquad
 \max_{L\le R\le H} A_R=K\left(\frac{v(H-L)}{1+2v-v^2}\right)^2.}
\]
These are raw frame bounds with the first coefficient \(a\) fixed, not bounds after renormalizing the window's \(L^2\)-norm. At either endpoint the frame bound vanishes **exactly quadratically on the protected side**, with distinct explicit coefficients.

## Assumptions and scope

The Fourier transform convention is \(\widehat f(\xi)=\int_\mathbb R f(t)e^{-2\pi it\xi}\,dt\). Cauchy kernels are interpreted in \(L^2(\mathbb R)\). Only real positive \(R\) is treated, giving two residues of opposite sign with the same complex overall phase. The lattice is rectangular at the critical product \(\alpha\cdot(1/\alpha)=1\). The two poles are distinct, strictly above the real line. Every assertion is for all \(\alpha>0\), \(a\ne0\), and \(0<w_1<w_2\) satisfying the displayed restrictions; no limit in pole separation is taken.

The two-frame-bound normalization is the standard Gabor analysis inequality above. The theorem determines the **lower** optimal bound, not the upper bound, and its maximizing ratio refers only to the protected interval with fixed first residue.

## Proof

**1. Exact Zak fibers and normalization.** Define, for \(0\le x<\alpha\) and \(0<\omega<1/\alpha\),
\[
 Z_\alpha g(x,\omega)=\sum_{m\in\mathbb Z}g(x-m\alpha)e^{2\pi i m\alpha\omega}.
\]
The series is interpreted through its \(L^2\) Fourier-series realization. Since \(\sqrt\alpha Z_\alpha\) is unitary and critical-lattice shifts become the standard Fourier characters on the Zak fundamental rectangle, the sharp lower frame constant equals
\[
 A_R=\alpha\operatorname*{ess\,inf}_{0\le x<\alpha,\ 0<\omega<1/\alpha}|Z_\alpha g_R(x,\omega)|^2.
\]
For \(w>0\), contour integration gives \(\widehat{(t-iw)^{-1}}(\xi)=2\pi i\,e^{2\pi w\xi}\mathbf1_{\{\xi<0\}}\). Geometric summation of the negative-frequency aliases, with \(z=e^{-2\pi i x/\alpha}\), yields
\[
 Z_\alpha g_R=\frac{2\pi ia}{\alpha}e^{2\pi i\omega x}z\,
 \frac{u e^{2\pi w_1\omega}(1-vz)-Rv e^{2\pi w_2\omega}(1-uz)}{(1-uz)(1-vz)}.
\]
This is a bounded continuous function of \(z\) on \(|z|=1\) and of \(\omega\) on the *one-sided closed* interval \([0,1/\alpha]\). Hence its essential extrema are the extrema of that expression on the compact one-sided rectangle. The possible jump between the two Zak-frequency endpoints does not affect this assertion.

**2. The real-ratio failure locus.** Set \(s=e^{2\pi (w_2-w_1)\omega}\), so \(1\le s\le u/v\). A zero of the Zak numerator has \(z\in\{1,-1\}\): its numerator is affine in \(z\) with real coefficients, and a real root on the unit circle can only be \(\pm1\). The two coefficients cannot simultaneously vanish because \(u\ne v\). Evaluating the zero condition at \(z=-1\) gives \(Rs=L\); at \(z=1\), it gives \(Rs=(u/v)H\). Consequently the two zero-bearing residue intervals are exactly \(I_-\) and \(I_+\) above, including the one-sided endpoints. A Zak zero, including a zero approached at the frequency endpoint, makes the sharp lower frame bound zero. Outside their union the continuous one-sided modulus has a positive minimum and the rational Zak fiber has finite maximum. Finally,
\[
 H-L=\frac{(u-v)(u+v+uv-1)}{v(1-u^2)},
\]
proving the strict protected-gap criterion.

**3. A global angular-minimum lemma.** Fix \(\omega\), and write the Zak numerator as \(A-Bz\) for *real* \(A,B\). After dropping a factor independent of \(z\), its squared modulus is
\[
 F(y)=\frac{A^2+B^2-2AB y}
 {(1+u^2-2uy)(1+v^2-2vy)},\qquad y=\cos(2\pi x/\alpha)\in[-1,1].
\]
Let \(m=\min\{F(-1),F(1)\}\). The numerator minus \(m\) times the denominator is a concave quadratic in \(y\): its quadratic coefficient is \(-4muv\le0\), and its values at \(y=\pm1\) are nonnegative. Therefore it is nonnegative throughout \([-1,1]\). The denominator is strictly positive. Thus the **global angular minimum always occurs at** \(z=-1\) or \(z=1\). This argument is valid even if an endpoint fiber has zero value.

**4. Optimize the remaining frequency parameter.** Assume \(L<R<H\). With \(\kappa=w_1/(w_2-w_1)>0\), the two endpoint amplitudes, after removing the common factor \(2\pi|a|/\alpha\), are
\[
 M_-(s)=\frac{v}{1+v}s^\kappa(Rs-L),\qquad
 M_+(s)=\frac{v}{1-v}s^\kappa((u/v)H-Rs),\quad 1\le s\le u/v.
\]
Both bracketed expressions are strictly positive. The first function is strictly increasing, so its minimum occurs at \(s=1\) and equals \(v(R-L)/(1+v)\). The second is a positive constant times \(s^\kappa(C-Rs)\), whose derivative changes sign at most once and only from positive to negative. Its minimum therefore occurs at \(s=1\) or \(s=u/v\). The value at the latter endpoint is \((H-R)/(1-v)\). The value at \(s=1\) is \(v((u/v)H-R)/(1-v)\), which **never beats** the first branch: indeed for \(R\le H\),
\[
 (1+v)(u/v)H+(1-v)L-2R\ \ge\
 \frac{2(u-v)(1-v)}{v(1-u)(1+u)}>0.
\]
Thus the global infimum is the minimum of the two claimed amplitudes. Squaring and multiplying by \(\alpha(2\pi|a|/\alpha)^2=K\) proves the exact optimal lower frame bound, with equality approached at the designated Zak fiber endpoints.

**5. The uniquely best protected ratio.** One amplitude is strictly increasing from zero and the other strictly decreasing to zero on \([L,H]\). Their minimum has exactly one maximum, at the unique ratio where the two amplitudes agree. Solving that linear equation gives \(R_*\), and substitution yields the displayed maximum. Quadratic vanishing at both endpoints is exact, not just asymptotic.

## Verification

Run `python3 check_two_cauchy.py` in the same directory as this document. The standalone test script uses only Python's standard library and checks the Zak formula against truncated Fourier series, the protected-gap identity, the two endpoint values, the exact lower-bound formula against a deterministic sampling of interior Zak fibers, and the maximizing-ratio identity. The recorded run printed `TWO_CAUCHY_PROTECTED_GAP_CHECKS_PASS 154988 cases 139`. This is a finite reproducibility test, **not** an exhaustive search or a replacement for the universal proof above.

For example, when \(u=4/5\), \(v=1/5\), \(a=1\), and \(\alpha=1\), the protected interval is \((8/3,4)\), and
\[
 A_R=4\pi^2\min\left\{\left(\frac{R-8/3}{6}\right)^2,\left(\frac{5(4-R)}4\right)^2\right\}.
\]
The unique maximizing ratio is \(R_*=196/51\), with \(\max A_R=4\pi^2(10/51)^2\). (Both fractions follow by exact substitution, without a numerical fit.)

## Relationship to prior work

Belov, Kulikov, and Lyubarskii established the rational-Cauchy Gabor frame framework and the Herglotz positive-residue frame theorem, and explicitly noted in their Section 1.7.2 that the full *qualitative* two-kernel frame set can be described, with detailed proofs intended elsewhere [1]. Thus **no novelty is claimed for Zak diagonalization, the general qualitative frame criterion, or the mere possibility of classifying two kernels**. The result here is instead the sharp, pointwise **optimal lower frame bound on a nontrivial signed reentrant component** and its exact optimal residue. The endpoint-minimum mechanism supplies an explicit global proof beyond checking the existence of frame zeros.

The single-Cauchy operator and frame-bound analysis [2] covers a one-pole window, not this signed two-pole protected interval. The cited generic frame stability literature concerns different windows or inequality bounds and supplies no covering exact two-pole lower-bound identity identified in the searches. Historical priority of the quantitative identity remains provisional: an unlocated later detailed two-kernel treatment, or another explicit Zak bound calculation, could cover it.

## Limitations

The proof is restricted to two simple imaginary-axis poles of distinct positive heights, opposite real residue signs, rectangular critical density, and the interior of the protected interval. It does **not** determine sharp upper frame bounds, complex relative-residue phase diagrams, arbitrary signed sums with three or more poles, noncritical lattices, or normalized-by-window-energy optimal condition numbers. The maximum is for fixed first residue and varies if the overall window is renormalized. The exhibited source comparison is not an independent historical-priority certification.

## References

[1] Y. Belov, A. Kulikov, Y. Lyubarskii, *Gabor frames for rational functions*, first posted 16 March 2021, arXiv:2103.08959; Invent. Math. 231 (2023), 431–466, doi:10.1007/s00222-022-01151-8. The public full text explicitly discusses the two-kernel qualitative frame set in Section 1.7.2.

[2] Y. Belov, A. Kulikov, Y. Lyubarskii, *Gabor frame operator for the Cauchy kernel*, first posted 17 December 2022, arXiv:2212.08915; St. Petersburg Math. J. 35 (2024), 741–747.

[3] K. Gröchenig, *Foundations of Time-Frequency Analysis*, Birkhäuser, 2001, for the standard critical-density Zak-transform frame criterion.
