# Two risk classes suffice for recurrent incidence crests during rising SIR prevalence

## Finding

In the deterministic, homogeneously mixing susceptible–infected–removed (SIR) epidemic with **fixed individual susceptibility**, homogeneous infectiousness, constant transmission and recovery rates, and no exposed compartment, two susceptibility classes can produce **at least two distinct strict local maxima of total new-infection incidence before infectious prevalence reaches its unique maximum**. One susceptibility class cannot produce two strict incidence maxima. Consequently **two distinct positive susceptibility classes are the sharp minimum for this incidence–prevalence separation** in this model class.

An exact admissible witness is transmission rate \(\beta=2\), recovery rate \(\gamma=1\), initial infectious fraction \(I(0)=1/1000\), and initial susceptible fractions
\[
S_1(0)=\frac{999}{1000}\frac{11}{12},\qquad
S_2(0)=\frac{999}{1000}\frac1{12},
\]
with fixed susceptibilities \(\lambda_1=1\) and \(\lambda_2=20\). The incidence is \(J(t)=\beta I(t)(S_1(t)+20S_2(t))\). In particular, the conclusion holds on a nonempty **open neighborhood** of this parameter set, not just at one isolated point.

## Assumptions and scope

For \(m\ge1\), consider population fractions \(S_j(t)\ge0\), \(I(t)>0\), and \(R(t)\ge0\) satisfying
\[
\dot S_j=-\beta\lambda_j S_j I,\quad
\dot I=\beta I\sum_{j=1}^m\lambda_j S_j-\gamma I,\quad
\dot R=\gamma I,
\]
where \(\beta,\gamma,\lambda_j>0\), \(\sum_jS_j(0)+I(0)+R(0)=1\), and no susceptible class changes risk type. The infective pool is shared and each infectious individual transmits at the same rate. The output called *incidence* is the rate of newly acquired infections, not prevalence or the rate of new symptomatic diagnoses.

The minimum number of susceptibility *values* is meant in this exact class, including any number of individuals of each value; one-class incidence is either strictly unimodal or decreasing. The example has \(R(0)=0\). It makes no claim about a stochastic finite-population realization, observed outbreaks, or the exact total number of local extrema of incidence in the witness; the proved lower bound is two strict local maxima separated by a strict local minimum.

## Proof

**1. Cumulative-pressure reduction.** Define
\[
x(t)=\beta\int_0^t I(s)\,ds,\quad c=\frac\gamma\beta,
\quad A(x)=\sum_j\lambda_j S_j(0)e^{-\lambda_jx},\quad
B(x)=\sum_j\lambda_j^2S_j(0)e^{-\lambda_jx}.
\]
Then \(dx/dt=\beta I>0\), \(S_j(t)=S_j(0)e^{-\lambda_jx(t)}\), and division of the infectious equation by \(dx/dt\) gives
\[
I(x)=I(0)+\sum_jS_j(0)(1-e^{-\lambda_jx})-cx.
\]
In particular, \(I'(x)=A(x)-c\), \(I''(x)=-B(x)<0\). As \(J=\beta I A\), differentiation gives the exact sign identity
\[
\frac{dJ}{dx}=\beta F(x),\qquad
F(x)=A(x)[A(x)-c]-I(x)B(x).
\]
Since \(dx/dt>0\) along the nonzero-infection trajectory, the sign of \(dJ/dt\) equals that of \(F(x)\). No numerical time stepping is needed to determine the certified sign changes.

**2. Four exact sign observations for the two-class example.** Put \(x=\log r\). At each positive rational \(r\), the class fractions are rational:
\[
S_1(\log r)=\frac{999}{1000}\frac{11}{12}r^{-1},\qquad
S_2(\log r)=\frac{999}{1000}\frac1{12}r^{-20}.
\]
Thus \(A\) and \(B\) are rational at the four chosen points, and \(I(\log r)=1-S_1-S_2-\frac12\log r\). The bounds proved by the elementary positive-series certificate in `check_incidence.py` give the following rigorous alternating signs:

| \(r\) | \(F(\log r)\) | Approximate value (for orientation only) |
|---|---|---|
| \(1\) | \(>0\) | \(5.3356798125\) |
| \(9/8\) | \(<0\) | \(-0.0148713941\) |
| \(5/4\) | \(>0\) | \(0.0163852409\) |
| \(3/2\) | \(<0\) | \(-0.0480548144\) |

The exact certificate evaluates each rational part as a `fractions.Fraction` and bounds its only logarithm by
\[
2\sum_{n=0}^{N-1}\frac{z^{2n+1}}{2n+1}
\le \log r\le
2\sum_{n=0}^{N-1}\frac{z^{2n+1}}{2n+1}
+\frac{2z^{2N+1}}{(2N+1)(1-z^2)},\quad
z=\frac{r-1}{r+1},\quad N=12.
\]
This bound follows from \(\log r=2\operatorname{artanh}z\) and the geometric-series bound on its nonnegative tail; it is an exact inequality, not a floating-point evaluation. The certificate rigorously tests that the upper or lower bound for \(F\) has the stipulated strict sign, and that \(I(\log r)>0\) at every point.

**3. All three changes occur while prevalence is increasing.** At the last point \(r=3/2\), the lower-susceptibility group alone gives
\[
A(\log(3/2))\ge
\frac{999}{1000}\frac{11}{12}\frac23
=\frac{10989}{18000}>\frac12=c.
\]
Since \(A'(x)=-B(x)<0\), \(I'(x)=A(x)-c>0\) throughout \(0\le x\le\log(3/2)\). Hence \(I(x)\ge I(0)>0\) there, the cumulative-pressure points are reached in finite physical time, and infectious prevalence is strictly rising across the whole interval. The analytic function \(F\) has the signs \(+,-,+,-\) at four increasing cumulative-pressure values. Continuity and analyticity produce a strict local maximum, a strict local minimum, then a second strict local maximum of \(J\) between these landmarks. Since \(A(x)\downarrow0\) and \(I(x)\) is strictly concave with a positive initial slope, infectious prevalence has exactly one maximum later along the physical trajectory.

The strict signs and the inequalities \(I(0)>0\), \(A(\log(3/2))>c\) persist under sufficiently small simultaneous changes to the positive model parameters and class fractions, proving an open parameter region with the same phenomenon.

**4. One susceptibility value cannot do this.** If all susceptibles share \(\lambda>0\), set \(S(x)=S(0)e^{-\lambda x}\). Then
\[
\frac{dJ}{dx}=\beta\lambda S(x)
\big[\lambda(S(x)-I(x))-c\big].
\]
Whenever \(\lambda S(x)\le c\), the bracket is negative. On the earlier interval where \(\lambda S(x)>c\), the bracket has derivative
\[
\frac d{dx}\big[\lambda(S-I)-c\big]
=\lambda(c-2\lambda S(x))<0.
\]
It therefore can cross zero at most once, from positive to negative. A zero-susceptibility class has identically zero incidence. Thus one distinct susceptibility value admits at most one strict incidence maximum, whereas the two-class witness has at least two. This proves the sharp minimum.

## Verification

Run `python3 check_incidence.py` from the directory containing this document. The checker uses the Python standard library only. It evaluates the rational \(A\), \(B\), and exponential terms at the four rational \(r\), encloses \(\log r\) using twelve exact positive atanh-series terms, and asserts the alternating strict signs, positive prevalence, and the rising-prevalence inequality at the last point. The actual run printed `PASS: four exact derivative-sign certificates and rising prevalence endpoint.` Its output supplies the rational-interval finite certificates used above. The infinite statements additionally use the stated analytic arguments, not numerical sampling.

## Relationship to prior work

The 2026 mixed-Sellke limit establishes the Laplace-transform model, monotone selection of susceptibility, and the finite-discrete-risk closure used here; it does not state two total-incidence crests while total infectious prevalence increases. Bootsma–Chan–Diekmann–Inaba (2023/2024), Section 10.1, document double incidence peaks due to *latent-period differences* or *weak coupling*, while the present construction has neither. Alutto–Cianfanelli–Como–Fagnani (2023), Sections 3–4, establish unimodality of an appropriate weighted aggregate of *infectious prevalence* in rank-one network SIR models and possible multimodality in *individual subpopulation prevalence*; these results are compatible with, but do not imply, the present total **new-infection incidence** counterexample. Multiple peaks in multilayer contact networks (Zheng et al., 2017) likewise involve different contact structure and delays.

No general historical uniqueness claim is made. The mathematical comparison concerns incidence versus infectious prevalence and the specific model hypotheses, not merely matching the keywords “two peaks” or “heterogeneity”. A more comprehensive historical-priority review may identify a broader incidence-shape result covering the example.

## Limitations

The result certifies **at least** two strict incidence maxima, not exactly two; it gives no closed formula for their times or magnitudes. The perfectly mixed, closed, deterministic SIR assumptions and initially infected fraction \(1/1000\) are essential to the displayed model, and this stylized example is not a fitted epidemic forecast. The finite-size stochastic model need not show visually distinguishable peaks in one realization. Historical-priority assessment is literature-bounded and requires independent checking.

## References

1. O. Izyumtseva, W. R. KhudaBukhsh, M. G. M. Gomes, G. A. Rempala, *From Individual-Based Stochastic Epidemics to Heterogeneous SIR Equations*, arXiv:2608.22122, first version 2026-08-22, https://arxiv.org/abs/2608.22122 (Sections 3 and 4, including finite discrete susceptibility).
2. M. Bootsma, D. Chan, O. Diekmann, H. Inaba, *The effect of host population heterogeneity on epidemic outbreaks*, arXiv:2308.06593, 2023; *Mathematics in Applied Sciences and Engineering* 5 (2024), https://arxiv.org/abs/2308.06593 (Section 10.1).
3. M. Alutto, L. Cianfanelli, G. Como, F. Fagnani, *On the dynamic behavior of the network SIR epidemic model*, arXiv:2309.14583, 2023, https://arxiv.org/abs/2309.14583 (Theorem 3.8 and Section 4).
4. M. Zheng, W. Wang, M. Tang, J. Zhou, S. Boccaletti, Z. Liu, *Multiple peaks patterns of epidemic spreading in multi-layer networks*, arXiv:1706.05780, 2017, https://arxiv.org/abs/1706.05780.
