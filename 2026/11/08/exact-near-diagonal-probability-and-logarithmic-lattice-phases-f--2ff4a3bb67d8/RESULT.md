# Exact near-diagonal probability and logarithmic lattice phases for randomly driven affine interval pairs

## Finding

For two interval points driven by the **same** random composition of an integer expanding map and its inverse branches, the explicit absolutely continuous stationary pair law has a sharp three-regime near-diagonal profile. The result gives an exact finite-scale formula, a logarithmic critical boundary, and a genuinely nonconstant lattice-periodic limit below that boundary.

Fix an integer \(m\geq2\) and \(1/2<p<1\), and set \(r=(1-p)/p\). Let \(\mu\) be the stationary probability constructed in the proof. For \(0<\varepsilon<1\), define
\[
P(\varepsilon)=\mu\{(x,y):|x-y|<\varepsilon\},\quad
n=\lfloor\log_m(1/\varepsilon)\rfloor,\quad
 t=m^n\varepsilon\in(1/m,1],\quad S_n(z)=\sum_{h=0}^n z^h.
\]
Then the **exact law**, valid for every permissible \(m,p,\varepsilon\), is
\[
\boxed{P(\varepsilon)=(1-r)\bigl[2\varepsilon S_n(mr)-\varepsilon^2 S_n(m^2r)\bigr]+r^{n+1}.}
\]
It entails the following complete asymptotic trichotomy.

**Bounded-density range, \(0<r<1/m\)** (equivalently \(p>m/(m+1)\)):
\[
\lim_{\varepsilon\downarrow0}\frac{P(\varepsilon)}{\varepsilon}
=\frac{2(1-r)}{1-mr}.
\]

**Critical boundary, \(r=1/m\)** (equivalently \(p=m/(m+1)\)):
\[
P(\varepsilon)=2(1-1/m)\,\varepsilon\log_m(1/\varepsilon)+O(\varepsilon).
\]

**Singular-density range, \(1/m<r<1\)** (equivalently \(1/2<p<m/(m+1)\)): let \(\alpha=-\log_m r\in(0,1)\). Then
\[
\boxed{P(\varepsilon)=\varepsilon^\alpha\Phi_{m,r}(t)
-\frac{2(1-r)}{mr-1}\varepsilon
+\frac{1-r}{m^2r-1}\varepsilon^2,}
\]
where the explicit positive amplitude is
\[
\boxed{\Phi_{m,r}(t)=t^{-\alpha}\left[r+(1-r)
\left(\frac{2mr\,t}{mr-1}-\frac{m^2r\,t^2}{m^2r-1}\right)\right],\quad 1/m\le t\le1.}
\]
It satisfies \(\Phi_{m,r}(1/m)=\Phi_{m,r}(1)\) and is **nonconstant**. For every fixed \(t\in(1/m,1]\),
\[
\lim_{n\to\infty}\frac{P(t m^{-n})}{(t m^{-n})^\alpha}=\Phi_{m,r}(t).
\]
Consequently there is no single normalized limit \(P(\varepsilon)/\varepsilon^\alpha\) as \(\varepsilon\downarrow0\); instead, the exact set of its subsequential limit values is \(\Phi_{m,r}([1/m,1])\).

## Assumptions and scope

The state space is \([0,1)^2\). At each time, choose one map, independently of previous times, and apply **that identical map to both coordinates**. With probability \(p\) choose \(f_0(x)=mx\pmod1\); with probability \((1-p)/m\) each choose \(f_i(x)=(x+i-1)/m\), \(1\le i\le m\). The positive-average-expansion condition is \((2p-1)\log m>0\), precisely \(p>1/2\). The result concerns the explicitly specified absolutely continuous stationary pair probability \(\mu\), not every stationary law, and uses ordinary Euclidean interval distance, not circular distance.

For each integer \(h\ge0\), partition \([0,1)\) into \(m^h\) half-open intervals
\(I_{h,j}=[j/m^h,(j+1)/m^h)\). Define a probability measure \(\nu_h\) on the square by the density
\[
\frac{d\nu_h}{dx\,dy}=m^h\sum_{j=0}^{m^h-1}{\mathbf{1}}_{I_{h,j}}(x){\mathbf{1}}_{I_{h,j}}(y).
\]
Thus the two coordinates occupy the same uniformly selected level-\(h\) cell and, conditional on that cell, are independent and uniformly distributed. The stationary law used throughout is
\[
\mu=(1-r)\sum_{h=0}^\infty r^h\nu_h.
\]
There is no contribution supported on the exact diagonal: every \(\nu_h\) is absolutely continuous. The geometric-series summation and all identities below are valid for finite integer \(m\ge2\), real \(1/2<p<1\), and \(0<\varepsilon<1\).

## Proof

**1. Stationarity.** Applying a uniform contraction \(f_i\) simultaneously to both coordinates maps \(\nu_h\), after averaging over \(i\), exactly to \(\nu_{h+1}\): its \(m^{h+1}\) level cells all receive the same mass. The common expansion \(f_0\) maps \(\nu_h\) to \(\nu_{h-1}\) when \(h\ge1\), and maps \(\nu_0\) to itself. Thus the pair dynamics closes on the reflected birth-death chain \(h\mapsto\max(0,h-1)\) with probability \(p\), or \(h\mapsto h+1\) with probability \(1-p\). Its normalized geometric weights are \(b_h=(1-r)r^h\). In fact, \(p b_{h+1}=(1-p)b_h\) and \(p(b_0+b_1)=b_0\), the latter being the exact reflecting boundary equation. Hence \(\mu\) is invariant and has mass one.

**2. Conditional separation.** In a level-\(h\) cell of length \(\ell=m^{-h}\), the rescaled coordinates are independent uniforms on \([0,1]\). Elementary triangular-area geometry gives
\[
\nu_h\{|x-y|<\varepsilon\}=H(m^h\varepsilon),\qquad
H(u)=\begin{cases}2u-u^2,&0\le u\le1,\\1,&u\ge1.\end{cases}
\]
The equality cases \(u=1\) agree, and strict versus weak distance inequalities change no mass. For \(n=\lfloor\log_m(1/\varepsilon)\rfloor\), precisely the indices \(0\le h\le n\) use the polynomial branch (allowing equality), while \(h\ge n+1\) contribute one. Substitution into the geometric mixture gives
\[
P(\varepsilon)=(1-r)\sum_{h=0}^{n}r^h(2m^h\varepsilon-m^{2h}\varepsilon^2)
+(1-r)\sum_{h=n+1}^{\infty}r^h,
\]
which is the boxed exact formula because the last sum equals \(r^{n+1}\).

**3. Bounded-density range.** Suppose \(mr<1\). Divide the exact mixture by \(\varepsilon\). For each fixed \(h\), \(H(m^h\varepsilon)/\varepsilon\to2m^h\), and \(0\le H(m^h\varepsilon)/\varepsilon\le2m^h\). The geometric majorant \(2(1-r)\sum_{h\ge0}(mr)^h\) is finite, so dominated convergence proves the stated limit, with no assumption on \(m^2r\).

**4. Critical boundary.** For \(r=1/m\), the first sum in the exact formula is \(2(1-1/m)\varepsilon(n+1)\). The second is \((1-1/m)\varepsilon^2\sum_{h=0}^n m^h=O(\varepsilon)\), since \(m^n\varepsilon\le1\). The last term \(m^{-(n+1)}\) is also \(O(\varepsilon)\). As \(n+1=\log_m(1/\varepsilon)+O(1)\), the logarithmic law follows with the claimed uniform remainder.

**5. Singular range and exact remainder.** If \(mr>1\), then also \(m^2r>1\). Replace each finite sum by \(S_n(z)=(z^{n+1}-1)/(z-1)\) and use \(\varepsilon=t m^{-n}\) and \(r^n=\varepsilon^\alpha t^{-\alpha}\). Terms containing \(r^n\) combine into \(\varepsilon^\alpha\Phi_{m,r}(t)\), while the two nonexponential terms are exactly the displayed linear and quadratic corrections. As \(0<\alpha<1\), these corrections are \(o(\varepsilon^\alpha)\), uniformly for \(t\in[1/m,1]\).

The formula at \(t=1/m\) equals that at \(t=1\) after rescaling \(n\mapsto n+1\), since the conditional mass at its joining point is \(H(1)=1\). This gives \(\Phi_{m,r}(1/m)=\Phi_{m,r}(1)\) (or follows by direct substitution). Positivity is immediate from the exact mixture: for every \(\varepsilon=t m^{-n}\), \(P(\varepsilon)\ge r^{n+1}=r t^{-\alpha}\varepsilon^\alpha\), so \(\Phi_{m,r}(t)\ge r t^{-\alpha}>0\). If \(\Phi_{m,r}\) were constant \(c>0\), the displayed formula would imply a quadratic polynomial in \(t\) equals \(c t^\alpha\) on an interval, impossible because the latter has nonzero third derivative for \(0<\alpha<1\). Thus the amplitude is nonconstant. Every sequence of scales has a subsequence with \(t\) convergent in the compact interval \([1/m,1]\), and every value there arises from the sequence \(\varepsilon_n=t m^{-n}\). This proves the exact subsequential-limit statement.

## Verification

The standalone standard-library program `verify.py` reconstructs the mass independently by summing the conditional triangular laws and the geometric tail, compares that exact rational expression with the closed formula across several integer bases, probabilities and scales, tests stationary birth-death balance, and checks critical and noncritical asymptotics. It passed **1,392 finite checks** when executed from the accompanying package. These checks are not substitutes for the infinite-series and limit arguments above.

## Relationship to prior work

Homburg and Kalle [1,2] introduced the common-noise affine interval-pair system. Their Theorem 3.10 and Example 3.12 (2025 journal numbering) provide stationary two-point mixtures on nested equal cells; Remark 3.13 identifies a bounded-density condition; Theorem 3.15 gives near-diagonal frequency information using a power exponent. Importantly, their paper **defines** the symbol \(\sim\) in this context as a ratio bounded above and away from zero, rather than standard ratio-one equivalence. The new exact profile agrees with the source's two-sided power order **in the singular-density range** \(r>1/m\), while refining it with a nonconstant periodic amplitude. At the boundary \(r=1/m\), the necessary logarithm prevents bounded-ratio comparison with \(\varepsilon\). On the bounded-density side \(r<1/m\), the exact leading order is linear and not \(\varepsilon^\alpha\) with \(\alpha>1\): indeed the nonzero \(\nu_0\) component by itself gives \(P(\varepsilon)\ge(1-r)(2\varepsilon-\varepsilon^2)\). Hence the published universal power-order wording cannot apply unchanged in those latter regimes to this explicit stationary measure. This distinction is part of the exact boundary result; the normalization of the mixture and all conclusions are established independently here.

A subsequent study of random circle endomorphisms [3] gives near-diagonal growth inequalities for a different, nonlinear model. Its hypotheses and results do not specify the exact distribution for the affine pair system. The exact cell-mixture computation is specific to this arithmetic equal-expansion/equal-contraction family; the usual lattice-renewal mechanism suggests analogues but does not itself imply these coefficients.

## Limitations

The theorem applies only to equal integer expansion and contraction base \(m\), uniform choice among the inverse branches, and a common random driver for both coordinates. It concerns the explicit absolutely continuous stationary probability \(\mu\); no uniqueness of all stationary measures is asserted. No claim is made for \(p\le1/2\), nonmultiplicatively-dependent branch numbers, arbitrary observables, or circular distance. As with any literature comparison, unindexed parallel derivations of the exact formula cannot be excluded. The numerical checks are finite, while the infinite statement is analytical.

## References

[1] A. J. Homburg and C. Kalle, *Iterated function systems of affine expanding and contracting maps on the unit interval*, arXiv:2207.09987v1 (public 20 July 2022), https://arxiv.org/abs/2207.09987 . Primary MSC2020 includes 37H20.

[2] A. J. Homburg and C. Kalle, *Iterated function systems of affine expanding and contracting maps on the unit interval*, Advances in Mathematics 482 (2025), 110605, https://doi.org/10.1016/j.aim.2025.110605 . Open full text: https://pure.uva.nl/ws/files/297456680/Iterated_function_systems_of_affine_expanding_and_contracting_maps_on_the_unit_interval.pdf . Relevant material: §3, Theorem 3.10, Example 3.12, Remark 3.13, Theorem 3.15.

[3] *Intermittent Two-Point Dynamics at the Transition to Chaos for Random Circle Endomorphisms*, Communications in Mathematical Physics (2026), https://doi.org/10.1007/s00220-026-05565-w . Relevant material: §5, Proposition 5.5.
