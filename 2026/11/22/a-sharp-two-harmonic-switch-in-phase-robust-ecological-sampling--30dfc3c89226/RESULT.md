# A sharp two-harmonic switch in phase-robust ecological sampling

## Finding

A target species is present throughout an idealized diel monitoring period, but the phase of its signal is unknown. Two identical molecular samples are to be placed at freely chosen times. For positive constants \(a,b,c,\omega\) satisfying \(a>b+c\), suppose each sample taken at time \(t\) independently yields a Poisson target count with conditional mean
\[
\lambda(t;\phi)=a+b\cos(\omega t+\phi)+c\cos(2\omega t+2\phi),
\]
where the unknown phase \(\phi\in[0,2\pi)\) is fixed across both samples. The objective is to maximize, over sampling times, the **minimum over phases** of the probability of detecting at least one target molecule. Define the shorter cyclic sample separation \(\Delta\in[0,\pi]\) in units of angular phase (the two times are equivalent modulo \(2\pi/\omega\)) and \(r=b/c>0\).

**Theorem.** Let \(r_*=4(\sqrt2-1)\). The complete set of optimal separations is
\[
\operatorname*{arg\,max}_{0\le\Delta\le\pi}\inf_\phi
\Pr\{N_1+N_2\ge1\mid\phi\}
=
\begin{cases}
\{\arccos(r/4)\},&0<r<r_*,\\
\{\arccos(\sqrt2-1),\ \pi\},&r=r_*,\\
\{\pi\},&r>r_*.
\end{cases}
\]
The optimal worst-phase success probability is exactly
\[
1-\exp\left[-2a-2c\max\left\{-1,-\frac r2-\frac{r^2}{16}\right\}\right].
\]
Thus the robustly optimal time separation jumps discontinuously at \(r_*\): as \(r\) increases through the threshold, a separation approaching \(\arccos(\sqrt2-1)\), approximately \(4.369\) hours on a 24-hour cycle, is replaced by exactly half a period, or 12 hours. At the threshold both separated designs tie, and no other separation is optimal. **The timing switch occurs while the intensity is still bimodal:** the unshifted signal has two distinct daily local maxima throughout \(0<r<4\), whereas the robust sampling switch already occurs at \(r_*=4(\sqrt2-1)<4\).

## Assumptions and scope

The counts are conditionally independent Poisson random variables given the common unknown \(\phi\); the sampling effort and assay response are equal at the two times. The two harmonics are **phase-aligned** (the second has phase \(2\phi\)), positive and precisely known in amplitude. Neither amplitude is zero. The baseline is constrained by \(a>b+c\) so the count mean is strictly positive at all times; there is no model for false positives, eDNA transport, site heterogeneity, uncertain amplitude, or count dependence beyond the shared unknown phase. Sampling may occur anywhere over a full periodic cycle, with no time-window or travel constraint. The objective is worst-case, not average-over-phase, detection probability. The period need not equal 24 hours; the hour conversions use that illustrative normalization only.

The mathematical setting is a deliberately simplified ecological-monitoring design: a first daily harmonic with an aligned second daily harmonic can represent more than one activity peak without claiming that any particular empirical species has this Fourier profile. The invariant unknown phase models unpredictable alignment between a fixed sampling calendar and a diel signal.

## Proof

1. By independence and the Poisson zero-count formula, for two sample phases \(\alpha\) and \(\beta\),
\[
\Pr\{N_1+N_2\ge1\mid\phi\}
=1-\exp[-\lambda(\alpha/\omega;\phi)-\lambda(\beta/\omega;\phi)].
\]
A common phase shift absorbs the midpoint of \(\alpha\) and \(\beta\). Since the signal is periodic, the shorter angular separation can be written \(\Delta=2\theta\) with \(0\le\theta\le\pi/2\), leaving two sample phases \(\pm\theta\). Their total mean is
\[
2a+2b\cos\theta\cos\phi+2c\cos(2\theta)\cos(2\phi).
\]
Therefore the design problem is to maximize the minimum of the last two normalized harmonic terms; the monotonicity of \(1-e^{-z}\) makes this reduction exact.

2. Set \(q=\cos\theta\in[0,1]\), \(z=2q^2-1\), and \(x=\cos\phi\in[-1,1]\). Dividing the harmonic terms by \(c\) gives the quadratic
\[
F_r(q,x)=rq x+z(2x^2-1).
\]
Every \(x\in[-1,1]\) occurs for some phase. For \(z\le0\) the quadratic is concave and its minimum is attained at \(x=-1\); for \(z>0\) it is convex, with vertex \(x=-rq/(4z)\). Consequently, with \(H_r(q)=\min_{-1\le x\le1}F_r(q,x)\),
\[
H_r(q)=\begin{cases}
2q^2-rq-1,&z\le0\ \text{or}\ rq\ge4z,\\
-z-\dfrac{r^2q^2}{8z},&z>0\ \text{and}\ rq<4z.
\end{cases}
\]
Both formulas agree at their boundary, and they explicitly include \(q=0\) and \(q=1\).

3. On the interior-vertex branch, \(q^2=(z+1)/2\) yields
\[
H_r=-z-\frac{r^2}{16}-\frac{r^2}{16z},\qquad 0<z\le1.
\]
Its derivative with respect to \(z\) is \(-1+r^2/(16z^2)\) and its second derivative is strictly negative. For \(0<r<4\), its unique unrestricted maximizer is \(z=r/4\), with value
\[
M_{\rm int}(r)=-\frac r2-\frac{r^2}{16}.
\]
The corresponding \(q=\sqrt{(1+r/4)/2}<1\) satisfies the interior condition strictly because \(rq<r=4z\); hence this value is attained, at \(2\theta=\arccos(r/4)\). For \(r\ge4\), this branch is absent: \(rq\ge4(2q^2-1)\) for every \(q\le1\).

4. On the other branch, \(H_r=2q^2-rq-1\), a strictly convex quadratic in \(q\). In \(0\le q\le1/\sqrt2\), its maximum is at \(q=0\) or \(q=1/\sqrt2\), with values \(-1\) and \(-r/\sqrt2\). In \(1/\sqrt2\le q\le1\), the boundary-branch feasible set is an interval; the positive solution to \(rq=4(2q^2-1)\) is its upper endpoint when \(r<4\). By convexity the maximum is again at an endpoint: \(-r/\sqrt2\), or the value at the branch junction, which cannot exceed the already established interior-branch bound \(M_{\rm int}(r)\). If \(r\ge4\), the other endpoint is \(q=1\), giving \(1-r<-1\).

5. Define \(r_*=4(\sqrt2-1)\), the unique positive root of \(r^2+8r-16=0\). When \(0<r<r_*\), one has
\[
M_{\rm int}(r)>-1,\qquad M_{\rm int}(r)>-r/\sqrt2;
\]
the second inequality holds because \(r_*<8(\sqrt2-1)\). Hence the unique maximizer is the interior point in step 3. For \(r>r_*\), \(M_{\rm int}(r)<-1\) whenever the branch exists, \(-r/\sqrt2<-1\), and \(1-r<-1\) when relevant. Therefore only \(q=0\), corresponding to \(\Delta=\pi\), maximizes the minimum. Exactly at \(r_*\), the interior point and \(q=0\) have equal value \(-1\), and the strict branch inequalities rule out other optima. Substituting the optimal minimum into step 1 gives the claimed probability and proves all cases. The unshifted intensity derivative is \(-\sin\phi(b+4c\cos\phi)\), with local maxima at \(\phi=0\) and \(\phi=\pi\) precisely when \(0<r<4\); thus the switch at \(r_*<4\) is not merely a transition from a bimodal to a unimodal source.

## Verification

The accompanying standalone standard-library program `checker.py` carries out exact rational checks of the core low-ratio identity, verifies the quadratic transition polynomial for rational parameter examples, and numerically challenges the theorem on a dense deterministic phase-and-separation grid. The proof above, not the finite grid, establishes the global continuum and uniqueness statements. As illustrative exact parameters, take \((a,b,c)=(21/10,1,1)\). Then \(r=1\), the unique optimal gap is \(\Delta=\arccos(1/4)\), the worst normalized harmonic contribution is \(-9/16\), and the worst-case detection probability is \(1-\exp(-123/40)\), approximately \(0.95381037\); a half-period gap yields \(1-\exp(-11/5)\), approximately \(0.88919684\). For \((a,b,c)=(31/10,2,1)\), the half-period gap is uniquely optimal, with worst-case detection \(1-\exp(-21/5)\), approximately \(0.98500442\).

## Relationship to prior work

West et al. (2024) report that marine eDNA remained detectable across day and night at their sampled reefs despite pronounced activity differences observed visually, and recommend substantial replication; they do not supply a phase-adversarial two-harmonic timing optimization. Jensen et al. (2022) analyze hourly marine eDNA variation and highlight temporal sampling effects, rather than a worst-phase minimax theorem. Bedwell and Goldberg (2020) experimentally compare sampling volumes, seasons, and spatial replication in eDNA surveys, rather than deriving a two-visit harmonic design. Related general harmonic sampling and unknown-phase signal detection frameworks (for example Kay and Gabriel, 2002, and Dilmaghani et al., 2007) concern statistical parameter detection or harmonic estimation, not the precise Poisson zero-count objective and the stated discontinuous optimizer switch. The elementary identity \(\cos2\phi=2\cos^2\phi-1\), Poisson zero-count formula, and standard convexity calculus are established ingredients, not claimed to be original.

A separate semantic lookup against published mathematical findings included broad periodic sampling, ecological Poisson detection, two-frequency design, and exact \(4(\sqrt2-1)\) threshold aliases. None of the returned closest claims implied this specific minimax law. This is evidence of limited overlap, not a proof of absolute historical novelty.

## Limitations

The result is conditional on an exact positive, phase-aligned two-harmonic intensity and equal independent Poisson measurement increments. It does not optimize sampling under average unknown-phase priors, assay saturation, variable effort, phase-varying false positives, extra measurement noise, correlation, or incomplete access to a 24-hour cycle. It is not a calibrated environmental prediction. General periodic-design and trigonometric-polynomial literature remains a plausible historical-priority risk. The analytic global theorem is proved for the stated model only; no empirical validation or independent external review is claimed.

## References

1. West, K. M. et al. (2024), “Continual Day–Night eDNA Detectability Amidst Diel Reef Species Fluctuations on Diver Transects,” *Environmental DNA*, first online 18 October 2024, https://doi.org/10.1002/edn3.70018.
2. Jensen, M. R. et al. (2022), “Short-term temporal variation of coastal marine eDNA,” *Environmental DNA*, first online 23 February 2022, https://doi.org/10.1002/edn3.285.
3. Bedwell, M. E. and Goldberg, C. S. (2020), “Spatial and temporal patterns of environmental DNA detection to inform sampling protocols in lentic and lotic systems,” *Ecology and Evolution*, https://doi.org/10.1002/ece3.6014.
4. Kay, S. M. and Gabriel, J. R. (2002), “Optimal invariant detection of a sinusoid with unknown parameters,” *IEEE Transactions on Signal Processing*, https://doi.org/10.1109/78.972479.
5. Dilmaghani, S. et al. (2007), “Harmonic Analysis of Environmental Time Series with Missing Data or Irregular Sample Spacing,” *Environmental Science & Technology*, https://doi.org/10.1021/es0700247.
