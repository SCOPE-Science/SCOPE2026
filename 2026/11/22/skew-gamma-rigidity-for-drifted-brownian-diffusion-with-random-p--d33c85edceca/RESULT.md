# Skew-gamma rigidity for drifted Brownian diffusion with random proportional resets

## Finding

**Theorem (complete inverse classification for a two-sided gamma target).** Let \(q,\sigma>0\), \(\mu\in\mathbb R\setminus\{0\}\), and consider a real process moving as \(dX_t=\mu\,dt+\sigma\,dB_t\) between independent rate-\(q\) Poisson epochs. At each epoch replace its state by \(CX\), where the multipliers are independent copies of a random variable \(C\in[0,1]\), independent of the diffusion, and \(\Pr(C<1)>0\). Put
\[
a=\frac{\sqrt{\mu^2+2q\sigma^2}+\mu}{2q},\qquad
b=\frac{\sqrt{\mu^2+2q\sigma^2}-\mu}{2q}.
\]
Thus \(a,b>0\), \(a\ne b\), \(a-b=\mu/q\), and \(ab=\sigma^2/(2q)\). Write \(G(s,c)\) for a gamma variable of shape \(s>0\) and scale \(c>0\), and assume independent gamma variables when taking differences. For prescribed \(p,r>0\), the unique stationary distribution is
\[
\mathcal L(X_\infty)=\mathcal L\bigl(G(p,a)-G(r,b)\bigr)
\]
**if and only if** one of these mutually exclusive cases holds:

1. \(p=r=1\), and necessarily \(C=0\) almost surely (full resetting).
2. \(p,r>1\) and \(\frac{p-1}{a}=\frac{r-1}{b}>0\). In this case the **only** admissible multiplier distribution is \(C\sim\operatorname{Beta}(p+r-2,1)\), i.e. its density is \((p+r-2)c^{p+r-3}\) on \((0,1)\).

Equivalently, all nontrivial attainable shape pairs form exactly the ray
\[
(p,r)=\left(1+\frac{\theta a}{a+b},\ 1+\frac{\theta b}{a+b}\right),\qquad\theta>0,
\]
with uniquely determined \(\operatorname{Beta}(\theta,1)\) contraction. Since \(\mu\ne0\), the attainable nontrivial shapes are necessarily unequal. In particular a nonzero drift constrains both gamma shapes jointly, not independently.

## Assumptions and scope

The state space is all of \(\mathbb R\) without a reflecting boundary. All Poisson event times, multiplier marks, and Brownian increments are mutually independent. There are no additive reset kicks or state-dependent multipliers. The gamma variables use the *scale* convention, with Laplace transform \(\mathbb E[e^{-sG(p,a)}]=(1+as)^{-p}\). All shape parameters are strictly positive and all claims concern a fixed \(q,\sigma,\mu\) and a fixed reset distribution. No assertion is made for more general signed coefficients, affine shifts, non-Poisson reset epochs, or gamma-component scales different from the Brownian excursion scales \(a,b\).

## Proof

**1. Excursion law and uniqueness of the stationary solution.** Let \(E\sim\operatorname{Exp}(q)\), independent of Brownian motion. A Brownian displacement \(\xi=\mu E+\sigma B_E\) has moment generating function, near the origin,
\[
M_\xi(s)=\frac{q}{q-\mu s-\sigma^2s^2/2}=\frac1{(1-as)(1+bs)}.
\]
Therefore \(\xi\stackrel d=G(1,a)-G(1,b)\), the difference of independent exponential variables. At a stationary independent observation time, the last Poisson age is exponential and independent of the past state and marks; hence the stationary distribution obeys
\[
Y\stackrel d=\xi+CY', \tag{1}
\]
with all terms on the right independent and \(Y'\stackrel d=Y\). Conversely, writing the infinite backward perpetuity \(Y=\sum_{j\ge0}\xi_j\prod_{i=1}^jC_i\) gives a convergent \(L^2\) series because \(\mathbb EC^2<1\) and \(\mathbb E\xi^2<\infty\). A coupling with identical Poisson times, increments and multipliers contracts the distance of any two starts as the product of the first \(n\) multipliers, which tends to zero almost surely, so (1) determines the unique stationary distribution even without moment assumptions on an initial law.

**2. Every admissible gamma shape is at least one.** Suppose \(Y\) has the proposed target law, and write \(Z=CY'\) independently of \(\xi\). Since \(Z\) is a finite real random variable, there is \(M<\infty\) with \(\Pr(Z\ge -M)>0\) and \(\Pr(Z\le M)>0\). As \(\xi=E_a-E_b\) is an asymmetric bilateral exponential,
\[
\Pr(Y>x)\ge \Pr(Z\ge-M)\Pr(\xi>x+M)\ge c_+e^{-x/a},
\]
and analogously \(\Pr(Y<-x)\ge c_-e^{-x/b}\), for strictly positive constants and all sufficiently large \(x\). On the other hand, elementary gamma tail integration and independence give
\[
\Pr(G(p,a)-G(r,b)>x)\sim
\frac{x^{p-1}e^{-x/a}}{\Gamma(p)a^{p-1}}(1+b/a)^{-r},
\]
with its negative-tail counterpart \(\Pr(Y<-x)\sim x^{r-1}e^{-x/b}(1+a/b)^{-p}/(\Gamma(r)b^{r-1})\). The lower bounds rule out \(p<1\) and \(r<1\).

**3. The sign-balance obstruction.** Taking characteristic functions in (1), using the independent asymmetric exponential law, uniquely identifies the characteristic function of \(Z=CY'\):
\[
\phi_Z(t)=\frac{\phi_Y(t)}{\phi_\xi(t)}
=(1-iat)^{-(p-1)}(1+ibt)^{-(r-1)}.\tag{2}
\]
When \(p,r\ge1\), this identifies \(Z\) as the difference of independent gamma variables of shapes \(p-1,r-1\), interpreting zero shape as a point mass at zero. Because \(Y'\) has a positive density on each half-line, \(\Pr(Y'>0)>0\) and \(\Pr(Y'<0)>0\). If exactly one of \(p,r\) equals one, (2) makes \(Z\) supported on only one half-line and nonzero, contradicting \(Z=CY'\) for \(C\ge0\). If both equal one, (2) gives \(Z=0\), so \(C=0\) almost surely.

Now suppose \(p,r>1\). Formula (2) describes a continuously distributed \(Z\) with \(\Pr(Z=0)=0\); therefore \(\Pr(C=0)=0\). It follows that \(Z=CY'\) and \(Y'\) have the same sign almost surely. Put \(x_0=b/(a+b)\). The ratio of independent unit-scale gamma variables is beta, giving
\[
\Pr(Y>0)=1-I_{x_0}(p,r),\qquad
\Pr(Z>0)=1-I_{x_0}(p-1,r-1),
\]
where \(I_x\) is the regularized beta integral. By differentiating both sides in \(x\) and checking that they vanish at \(x=0\), for all \(p,r>1\) and \(0<x<1\) one has the exact identity
\[
I_x(p,r)-I_x(p-1,r-1)
=\frac{x^{p-1}(1-x)^{r-1}}{(p+r-1)B(p,r)}
\left(x-\frac{r-1}{p+r-2}\right).\tag{3}
\]
All factors outside the final parenthesis are strictly positive. Equality of the two sign probabilities therefore forces \(b/(a+b)=(r-1)/(p+r-2)\), or equivalently \(b(p-1)=a(r-1)\). This proves the shape-balance necessity.

**4. Existence for the balanced ray.** Fix \(\theta>0\), set \(p-1=\theta a/(a+b)\), \(r-1=\theta b/(a+b)\), and choose \(C\sim\operatorname{Beta}(\theta,1)\). For the target moment generating function
\[
V(s)=(1-as)^{-p}(1+bs)^{-r}
\]
write \(H(s)=\mathbb E[V(Cs)]\). The beta integral gives
\[
H(s)=\theta s^{-\theta}\int_0^s u^{\theta-1}V(u)\,du,
\qquad sH'(s)=\theta(V(s)-H(s)). \tag{4}
\]
Define \(M(s)=((1-as)(1+bs))^{-1}\). Direct logarithmic differentiation of
\[
H_*(s)=(1-as)^{-(p-1)}(1+bs)^{-(r-1)}
\]
under the balanced shape relation gives \(sH_*'(s)=\theta(M(s)-1)H_*(s)\), \(H_*(0)=1\). Since \(V=M H_*\), (4) holds for \(H_*\). Analytic uniqueness of the differential equation near zero (or coefficient recursion) gives \(H=H_*\); thus \(V=M\mathbb E[V(Cs)]\), precisely the stationary fixed-point relation (1). Stationary uniqueness from Step 1 proves sufficiency. For \(p=r=1\), taking \(C=0\) gives \(Y\stackrel d=\xi\), proving the remaining case.

**5. The reset distribution is unique.** In (2), the law of \(Z\) is already determined by the target and the excursion. For each integer \(n\ge1\), independence and finite moments yield
\[
\mathbb E[C^{2n}]=\frac{\mathbb E[Z^{2n}]}{\mathbb E[Y^{2n}]},
\]
with the denominator strictly positive. The even moments uniquely determine the law of \(C^2\) on \([0,1]\) by density of polynomials in continuous functions; since \(C\ge0\), they uniquely determine the law of \(C\). The beta law constructed in Step 4 is therefore the only possible one. In the full-reset case the zero law is already forced in Step 3. This completes the classification.

## Verification

The standalone `verify.py` requires only Python 3 standard libraries and reproduces 3,204 exact rational assertions: the full stationary moment recurrence through order nine for 252 choices of distinct integer excursion scales and beta shapes, plus finite integer-shape instances of the sign-balance identity and its strictly opposing signs on the two sides of the unique root. Execute `python3 verify.py` in the same directory. It prints `PASS 3204 exact rational moment and beta-CDF checks`. The infinite-dimensional statement, the gamma tail comparison, sign-rigidity, and uniqueness all rely on the analytic proof, not the finite tests. Example: with \(q=1\), \(\mu=1\), \(\sigma=2\), \(a=2\), \(b=1\), and \(\theta=3\), the unique reset distribution is \(\operatorname{Beta}(3,1)\) and the invariant law is \(G(3,2)-G(2,1)\).

## Relationship to prior work

Palmowski and Vlasiou (arXiv:2611.14692v1, November 10, 2026) establish the general stationary fixed-point framework for Lévy processes under resetting, give a drifted-Brownian example with **fixed** affine contraction, and discuss random-coefficient mechanisms in other settings. This theorem does not claim that fixed-point equation as new; it solves a distinct *inverse two-sided gamma law* question for an arbitrary random contraction and proves the sign-balance obstruction and uniqueness of its beta law. Tal-Friedman, Roichman, and Reuveni (arXiv:2205.03363) establish drifted diffusion under a **deterministic** proportional reset and an infinite-product stationary representation. Pierce (arXiv:2204.07215) likewise studies deterministic proportional resetting.

The published published-finding corpus theorem *Inverse design of multivariate variance-gamma equilibria by random Brownian resetting* (October 26, 2026, exact identifier in References) classifies **zero-drift, symmetric** gamma/variance-gamma equilibria with \(a=b\), and their reset factors, but its hypotheses exclude \(\mu\ne0\), \(a\ne b\) and the unequal gamma shapes classified here. The standard beta-gamma integral and gamma ratio identity are classical tools, not themselves claimed as novel. The new content is the necessity-and-sufficiency *asymmetric* shape balance and unique contraction law.

## Limitations

Only gamma differences whose two scales coincide with the innovation's exponential scales \(a,b\) are considered; gamma targets with other scales, general variance-gamma parameterizations, state-dependent reset rules, and arbitrary Lévy innovations remain unclassified here. Priority is provisional: a more abstract pre-existing beta-gamma perpetuity theorem could imply this classification, notwithstanding the targeted comparisons. Independent validation has not been conducted. The finite checker tests selected parameter cases and is not an independent proof of the continuous classification.

## References

1. Z. Palmowski and M. Vlasiou, *Steady-state of Lévy process with general resetting: unreflected and reflected cases*, arXiv:2611.14692v1 (first public 2026-11-10), https://arxiv.org/html/2611.14692v1.
2. O. Tal-Friedman, Y. Roichman, and S. Reuveni, *Diffusion with Partial Resetting*, arXiv:2205.03363 (first public 2022-05-06), https://arxiv.org/html/2205.03363v2.
3. J. K. Pierce, *An advection-diffusion process with proportional resetting*, arXiv:2204.07215 (first public 2022-04), https://arxiv.org/abs/2204.07215.
4. *Inverse design of multivariate variance-gamma equilibria by random Brownian resetting*, published-finding corpus record `2026/10/26/SCOPE-inverse-design-of-multivariate-variance-gamma-equilibria-by-rand--7cea38ad1d45`, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-inverse-design-of-multivariate-variance-gamma-equilibria-by-rand--7cea38ad1d45.
