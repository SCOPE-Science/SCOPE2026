# Signed radial response at the first boundary-distance Bergman zero

## Finding

The transition from zero-free to zero-bearing weighted Bergman kernels for the Euclidean boundary-distance power on the disk has a **signed, spatially nonmonotone first variation**. Specifically, perturbing a weight by a nonnegative bump can advance, delay, or advance again the first Lu Qi-Keng zero, depending on which of three explicit radial bands carries the bump. A natural global linear tilt has the exact, strictly positive threshold derivative \(40/\pi-12\).

Use normalized area measure \(dA=dx\,dy/\pi\) on \(\mathbb D\), and let \(K_{t,\varepsilon,h}(\zeta)\), \(\zeta=z\overline w\), be the scalar reproducing kernel of the analytic Hilbert space with weight
\[
w_{t,\varepsilon,h}(r)=(1-r)^t(1+\varepsilon h(r)).
\]
Here \(t\) is near \(2\), \(\varepsilon\) is real and sufficiently small to keep the weight positive, and \(h\) is a real smooth function supported inside \((0,1)\). There are neighborhoods \(I\) of \(2\) and \(E\) of \(0\) and a unique real-analytic function \(t_h:E\to I\) with \(t_h(0)=2\), such that, for \((t,\varepsilon)\in I\times E\), the kernel has **no** scalar zeros in \(|\zeta|<1\) if \(t\le t_h(\varepsilon)\), and **exactly one simple scalar zero** if \(t>t_h(\varepsilon)\). The neighborhoods may depend on \(h\). Its derivative is
\[
t_h'(0)=-\frac{768}{\pi}\int_0^1\frac{h(r)r(1-r)^2 Q(r^2)}{(1+r^2)^7}\,dr,
\qquad Q(u)=u^4-18u^3+42u^2-18u+1.
\]
Define \(v_1=9+\sqrt{41}\), \(v_2=9-\sqrt{41}\), and \(u_j=(v_j-\sqrt{v_j^2-4})/2\), so \(0<u_1<u_2<1\). For every nonzero \(h\ge0\) supported entirely in the radial bands \((0,\sqrt{u_1})\), \((\sqrt{u_1},\sqrt{u_2})\), and \((\sqrt{u_2},1)\), respectively, the derivative \(t_h'(0)\) is negative, positive, and negative. Thus all three signs arise with strictly positive smooth radial weights; the two thresholds are approximately \(0.2553387\) and \(0.6857276\) in radius.

The same local zero-count classification also holds for the non-compactly supported **linear tilt** \(h(r)=r\). In this case
\[
t_r(\varepsilon)=2+\left(\frac{40}{\pi}-12\right)\varepsilon+O(\varepsilon^2),
\qquad \frac{40}{\pi}-12=0.73239544735\ldots>0.
\]
These are local parameter statements: no assertion is made about all powers or all perturbation strengths.

## Assumptions and scope

The zero count is for the single analytic scalar function \(\zeta\mapsto K_{t,\varepsilon,h}(\zeta)\) in the open disk \(|\zeta|<1\), **not** the cardinality of pairs \((z,w)\) realizing each scalar zero. All kernels use normalized area measure. For compactly supported \(h\), smoothness can be replaced by boundedness and compact support in \([0,b]\) with \(b<1\) for the analytic argument; smoothness is retained to make positive bump tests unambiguous. For the linear tilt the exact moment ratio supplies the necessary continuation and singularity estimates. The zero at the transition lies on \(\zeta=-1\), outside the open scalar domain.

## Proof

**1. Exact unperturbed kernel.** Monomials are orthogonal, with squared norm
\[
m_n(t,\varepsilon,h)=2\int_0^1r^{2n+1}(1-r)^t(1+\varepsilon h(r))\,dr,
\qquad K_{t,\varepsilon,h}(\zeta)=\sum_{n\ge0}\frac{\zeta^n}{m_n(t,\varepsilon,h)}.
\]
At \(\varepsilon=0\), the beta integral gives
\[
m_n(t,0)=2\mathrm B(2n+2,t+1),\quad
\frac1{m_n(t,0)}=\frac{\Gamma(2n+t+3)}{2\Gamma(2n+2)\Gamma(t+1)}.
\]
Summing the odd terms of the binomial expansion, with \(s^2=\zeta\), yields the branch-independent analytic expression
\[
K_{t,0}(\zeta)=\frac{t+1}{4s}\big[(1-s)^{-t-2}-(1+s)^{-t-2}\big].
\]
At the first critical power \(t=2\), it specializes to
\[
K_{2,0}(\zeta)=\frac{6(1+\zeta)}{(1-\zeta)^4}.
\]
Thus its only zero in the closed unit disk away from the pole \(\zeta=1\) is the simple boundary zero \(-1\). The endpoint evaluation and nondegenerate derivatives are
\[
K_{t,0}(-1)=\frac{t+1}{2}2^{-(t+2)/2}\sin\frac{\pi(t+2)}4,\quad
\partial_t K_{2,0}(-1)=-\frac{3\pi}{32},\quad
\partial_\zeta K_{2,0}(-1)=\frac38.
\]

**2. Compactly supported perturbations and exhaustive local zero count.** If \(h=0\) for \(r>b\) and \(b<1\), uniformly for real \(t\) close to \(2\),
\[
m_n(t,0)\asymp (n+1)^{-t-1},\qquad
|m_n(t,\varepsilon,h)-m_n(t,0)|\le C|\varepsilon|b^{2n}.
\]
Therefore the coefficient difference between \(K_{t,\varepsilon,h}\) and \(K_{t,0}\) is \(O(|\varepsilon|(n+1)^M b^{2n})\) for a fixed \(M\). It extends analytically to \(|\zeta|<b^{-2}\), depends real-analytically on parameters, and is bounded on a fixed neighborhood of the closed unit disk. On compact subsets of \(\overline{\mathbb D}\setminus\{-1,1\}\), the baseline kernel stays nonzero and small perturbations preserve that fact. Near \(\zeta=1\), the explicit baseline formula gives the uniform nonzero leading term
\[
K_{t,0}(\zeta)=(t+1)2^t(1-\zeta)^{-t-2}\bigl(1+o(1)\bigr),
\]
for \(t\) near \(2\), within the closed disk. Its unbounded leading magnitude dominates the bounded correction. Near \(\zeta=-1\), the holomorphic implicit-function theorem and Rouché's theorem give exactly one nearby simple zero, real by conjugation symmetry. Its movement has nonzero derivative \(\partial_t\zeta=\pi/4\) at the baseline point. Applying the real implicit-function theorem to \(K_{t,\varepsilon,h}(-1)=0\) yields a unique analytic threshold \(t_h(\varepsilon)\); the root is inside the disk precisely when \(t>t_h(\varepsilon)\). This also proves that the zero count is exhaustive, not a finite truncation.

**3. The exact signed response kernel.** At \(t=2\) the unperturbed reciprocal moments are
\[
a_n=\frac1{m_n(2,0)}=(n+1)(n+2)(2n+3).
\]
Termwise differentiation for \(|\zeta|<1\), followed by inserting the moment integral and summing the rational generating function, gives
\[
\left.\partial_\varepsilon K_{2,\varepsilon,h}(\zeta)\right|_{\varepsilon=0}
=-2\int_0^1r(1-r)^2h(r)\sum_{n\ge0}a_n^2(r^2\zeta)^n\,dr,
\]
\[
\sum_{n\ge0}a_n^2x^n=
\frac{36(x^4+18x^3+42x^2+18x+1)}{(1-x)^7}.
\]
The integral extends continuously to \(\zeta=-1\), yielding
\[
\partial_\varepsilon K_{2,0,h}(-1)
=-72\int_0^1\frac{r(1-r)^2h(r)Q(r^2)}{(1+r^2)^7}\,dr.
\]
Implicit differentiation gives \(t_h'(0)=-\partial_\varepsilon K/\partial_t K\), producing the claimed factor \(-768/\pi\). The reciprocal quartic factors as
\[
\frac{Q(u)}{u^2}=(u+u^{-1})^2-18(u+u^{-1})+40.
\]
Because \(u+u^{-1}\) decreases from infinity to \(2\) on \((0,1)\), its two roots are exactly \(u_1,u_2\). The sign of \(Q\) is positive, negative, positive in the successive three intervals, so nonnegative supported bumps yield the asserted strict signs.

**4. The linear tilt.** For \(h(r)=r\), the moments satisfy
\[
m_n(t,\varepsilon,r)=m_n(t,0)\left(1+\varepsilon\frac{2n+2}{2n+t+3}\right).
\]
Write \(\eta=\varepsilon(t+1)/(1+\varepsilon)\). Summing an elementary integral for the coefficient reciprocal gives the exact identity
\[
K_{t,\varepsilon,r}(\zeta)=\frac1{1+\varepsilon}\left[K_{t,0}(\zeta)+\eta\int_0^1 y^{t+2-\eta}K_{t,0}(y^2\zeta)\,dy\right].
\]
Near \(\zeta=1\) inside the disk, the integral is \(O(|1-\zeta|^{-t-1})\): indeed \(|1-y^2\zeta|\ge c((1-y)+|1-\zeta|)\) for \(\zeta\) near \(1\), \(|\zeta|\le1\). Hence the integral is one singular order weaker than the baseline and cannot create additional local zeros near the pole. The compact-subset and implicit-function arguments of step 2 remain valid. At \(t=2,\zeta=-1\),
\[
\partial_\varepsilon K_{2,0,r}(-1)=
3\int_0^1y^4K_{2,0}(-y^2)\,dy
=18\int_0^1\frac{y^4(1-y^2)}{(1+y^2)^4}\,dy
=\frac{15}4-\frac{9\pi}8.
\]
Combined with \(\partial_tK=-3\pi/32\), this is the stated exact slope.

## Verification

`CHECK.py` reconstructs the moment coefficient polynomial and rational generating function, checks the reciprocal-quartic reduction and both roots, symbolically integrates the linear-tilt derivative, and compares finite-parameter kernels from their integral and monomial-series formulas. Running `python CHECK.py` yields `PASS: 37 independent assertions (symbolic, integral and numerical)`. The exhaustive zero classification is justified analytically in steps 1–4, not by these finite tests.

## Relationship to prior work

The September 21, 2026 work of Marinescu and Xing proves local real-analytic dependence of Euclidean boundary-distance weighted Bergman kernels on the power parameter on general smoothly bounded pseudoconvex domains. It does not formulate radial perturbation sensitivity or the present two-sign-change response kernel. An existing explicit calculation for the **unperturbed** Euclidean-distance family supplies the sharp zero-free threshold \(t=2\); that baseline and its higher zero staircase are not claimed as new. Perälä establishes existence and finiteness results for radial Bergman-kernel zeros, while Zeytuncu constructs radial perturbations with zeros for weights comparable to one. Neither inspected primary discussion determines this precise signed threshold derivative at a boundary-distance transition.

## Limitations

This is a local theorem around the first boundary zero at \(t=2\), not a classification of large perturbations or all higher zero transitions. The compact-bump part requires support bounded away from \(r=1\); the additional noncompact example is the specific linear tilt \(h(r)=r\). The signs classify the first-order threshold shifts, not finite-amplitude monotonicity. Publication-priority searches cannot prove absolute novelty; equivalent first-variation results under other terminology remain possible. No independent audit has been performed.

## References

1. G. Marinescu and X. Xing, *Parameter Dependence of Weighted Bergman Kernels Beyond Smoothness*, arXiv:2609.24258, first submitted September 21, 2026. https://arxiv.org/abs/2609.24258
2. A. Perälä, *Vanishing Bergman kernels on the disk*, arXiv:1703.05976 (2017). https://arxiv.org/abs/1703.05976
3. Y. E. Zeytuncu, *Weighted Bergman Projections and Kernels: Lp Regularity and Zeros*, arXiv:1009.2806 (2010). https://arxiv.org/abs/1009.2806
4. *Sharp Lu Qi-Keng transitions for Euclidean boundary-distance weighted disk kernels* (public research record, October 11, 2026). Earlier unperturbed zero-count classification; compared by statement and scope.
