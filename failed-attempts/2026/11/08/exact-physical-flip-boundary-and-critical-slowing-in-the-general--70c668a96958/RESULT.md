# Exact physical flip boundary and critical slowing in the generalized Allee-logistic map

## Finding
Consider the generalized Allee-logistic map
\[
f_r(x)=r x(1-x)(c+m x),\qquad c=1-m(1+h),
\]
with \(r>0\), \(0\le m,h\le1\), and \(c\ge0\). Let
\[
q=(1-v)(c+m v),\qquad
v=\begin{cases}
2/3,&m=0,\\
\dfrac{3(m-c)+\sqrt{9(m-c)^2+32mc}}{8m},&m>0,
\end{cases}\qquad R=q^{-1},
\]
and put
\[
D=3q+mv^2,\qquad
K=\frac4{v^2}+\frac{3m}{q}+\left(\frac{mv}{q}\right)^2.
\]
Then \(2/3\le v\le3/4\), \(D,K>0\), and the positive equilibrium \(v\) of \(f_R\) has multiplier exactly \(-1\). This is the only positive-equilibrium flip for the parameter pair \((m,h)\). For \(r\) close to \(R\), the continuation of this equilibrium is locally attracting on the \(r<R\) side and repelling on the \(r>R\) side. For \(r>R\) sufficiently close to \(R\), exactly one local primitive two-cycle is born; it is attracting, and its two points are
\[
x_*(r)\pm\sqrt{D/K}\,\sqrt{r-R}+O(r-R),
\]
where \(x_*(r)\) is the positive fixed-point continuation. The two-step multiplier of this cycle is \(1-4D(r-R)+O((r-R)^{3/2})\).

At \(r=R\), every sufficiently close nonstationary initial point converges to \(v\) with alternating signs and an exact algebraic constant:
\[
\lim_{k\to\infty}\sqrt{4Kk}\,[f_R^{2k}(x)-v]=\operatorname{sgn}(x-v).
\]
Finally, \(f_R([0,1])\subset[0,1)\), with a uniform margin below \(1\); the same self-map property holds for all nearby growth rates. Thus the flip and its emerging two-cycle are dynamically admissible population states throughout the stated parameter wedge.

## Assumptions and scope
The inequalities \(0\le m,h\le1\) and \(c=1-m(1+h)\ge0\) ensure a nonnegative growth factor on the entire population interval. They include the logistic endpoint \(m=0\) and the cubic endpoint \((m,h)=(1,0)\); they exclude strong-Allee parameters with negative growth at very low positive densities. Constants \(v,R,D,K\) depend on the fixed pair \((m,h)\). Assertions about attraction, repulsion, and uniqueness of the two-cycle are local to the positive equilibrium, not classifications of all basins or all periodic orbits.

## Proof
**Unique flip location.** Write \(Q(x)=(1-x)(c+mx)\), so positive fixed points satisfy \(rQ(x)=1\). At such a point the multiplier is \(1+xQ'(x)/Q(x)\). It equals \(-1\) precisely when
\[
2Q(x)+xQ'(x)=2c+3(m-c)x-4mx^2=0.
\]
For \(m=0\) the only positive solution is \(x=2/3\). For \(m>0\) the displayed quadratic has a unique positive root, given by \(v\) above (the other root is nonpositive). Its value is nonnegative at \(x=2/3\), where it equals \(2m/9\), and nonpositive at \(x=3/4\), where it equals \(-c/4\). Hence \(2/3\le v\le3/4\), and \(q=Q(v)>0\). The positive equilibrium at \(r=R\) is \(v\), and it is the only positive equilibrium with multiplier \(-1\) at any growth rate.

**Transverse multiplier crossing.** Since \(Q'(v)=-2q/v<0\), the implicit function theorem supplies a smooth upper fixed-point branch \(x_*(r)\) near \(r=R\), with \(x_*'(R)=vq/2\). Differentiating \(\lambda(r)=1+x_*(r)Q'(x_*(r))/Q(x_*(r))\) gives
\[
\lambda(R)=-1,\qquad \lambda'(R)=-D=-(3q+mv^2)<0.
\]
This proves the local fixed-point stability assertions.

**Supercritical normal form and cycle.** Center at \(x_*(r)\), writing \(u=x-x_*(r)\). At \(r=R\) the cubic map is exactly \(-u+a u^2+b u^3\), where
\[
a=R(m-c-3mv)=-\frac2v-\frac{mv}{q},\qquad b=-\frac mq.
\]
Therefore \(a^2+b=K>0\), using the formula for \(K\) above. Composition yields the two-step return near the fixed branch, for \(\delta=r-R\),
\[
f_r^2(x_*(r)+u)-x_*(r)-u
=2D\delta u-2K u^3+O(\delta^2|u|+|\delta|u^2+|u|^4).
\]
After dividing by \(u\) and rescaling \(u=\sqrt\delta\,w\), the implicit function theorem produces precisely two small nonzero roots \(w=\pm\sqrt{D/K}+O(\sqrt\delta)\) when \(\delta>0\); these are interchanged by \(f_r\). The derivative of the two-step return there is \(1-4D\delta+O(\delta^{3/2})\), so the cycle is attracting. For \(\delta<0\) the return has no small nonzero roots. These local conclusions require no assertion about distant cycles.

**Sharp critical relaxation.** At \(\delta=0\), the two-step map in centered coordinates is \(u\mapsto u-2K u^3+O(u^4)\). For sufficiently small nonzero \(u\), this map preserves the sign and strictly contracts its magnitude. Writing \(u_k=f_R^{2k}(x)-v\), it follows that \(u_k\to0\) and
\[
\frac1{u_{k+1}^{2}}-\frac1{u_k^{2}}=4K+O(|u_k|)\longrightarrow4K.
\]
Cesàro summation gives \((ku_k^2)^{-1}\to4K\), preserving the initial sign and proving the stated limit. Odd iterates have the opposite sign because \(f_R'(v)=-1\).

**Admissibility.** At \(r=R\), set \(w=c/(c+mv)\in[0,1]\). A direct convex decomposition gives
\[
f_R(x)=w\frac{x(1-x)}{1-v}+(1-w)\frac{x^2(1-x)}{v(1-v)}.
\]
Both summands are nonnegative on \([0,1]\). Their maxima are bounded by \(1/[4(1-v)]\le1\) and \(4/[27v(1-v)]\le64/81<1\), respectively. If \(v<3/4\), the first bound is also strict; if \(v=3/4\), then \(c=0\) and \(w=0\). Hence \(\max_{[0,1]}f_R<1\). Continuity in \(r\) preserves this strict bound for nearby \(r\), completing the proof.

## Verification
Run `python verify.py` from the same directory. The script symbolically checks polynomial, flip, cubic, and two-iterate identities; it also evaluates seven endpoint/interior parameter pairs, 1,407 mesh points in the physical interval, critical relaxation after 22,000 two-step iterations per sample, and the two-cycle square-root expansion after 45,000 iterates per sample. The numerical tests are diagnostics, not a substitute for the proof of the all-parameter statement.

## Relationship to prior work
Pires, Andrade, and Herrmann (2026, arXiv:2606.05351v1) introduce this precise map and analytically study extinction, fixed-point collision, tricritical scaling, and numerical onset of chaotic dynamics. Their Sections II–III and regime/period-doubling discussion do not state the positive-equilibrium flip surface, its sign-uniform cubic normal form, the exact flip-critical relaxation coefficient, or the physical admissibility lemma established here. Logistic-map period doubling at \(m=0\) is classical and is included as a normalization check, not separately claimed as new. Rocha and Taha (2019) analyze a different four-parameter generalized logistic-map family and local/global bifurcations; their accessible abstract does not resolve exact implication of their results for the formula above. Their full text could not be inspected and remains a priority risk. Jung et al. (2020) numerically investigate Allee-modified population-map bifurcations; the available abstract does not provide the present uniform formulas. Standard scalar flip normal-form methods justify the mechanism, but their generic positivity criteria do not by themselves imply positivity of \(K\) for this whole constrained family.

## Limitations
The theorem is local near the positive equilibrium. The weak/nonnegative-growth wedge \(c\ge0\) does not include all parameter values studied in the motivating paper. In particular, it does not claim uniqueness of global attractors, first onset of chaotic dynamics, all-period classification, or dynamics with negative population-update values. The literature comparison is provisional; the potentially relevant 2019 full text was inaccessible. Independent mathematical review has not been performed.

## References
- M. A. Pires, J. S. Andrade Jr., H. J. Herrmann, *Tricriticality and chaos in a generalized Allee-logistic map*, arXiv:2606.05351v1 (first public 2026-06-03), https://arxiv.org/abs/2606.05351 .
- J. L. Rocha, A.-K. Taha, *Allee's Effect Bifurcation in Generalized Logistic Maps*, International Journal of Bifurcation and Chaos 29 (2019), 1950039, https://doi.org/10.1142/S0218127419500391 .
- N. Jung et al., *Chaotic Dynamics of a Simple Population Model under the Allee Effect*, Journal of the Korean Physical Society 76 (2020), 533–536, https://doi.org/10.3938/jkps.76.533 .
