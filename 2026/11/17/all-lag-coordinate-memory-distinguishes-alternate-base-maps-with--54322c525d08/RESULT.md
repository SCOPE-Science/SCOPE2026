# All-lag coordinate memory distinguishes alternate-base maps with identical invariant measures

## Finding

An infinite family of alternating interval maps has exactly the same stationary measure yet different temporal coordinate statistics. For every coprime pair of integers \(p>q>1\) and every integer \(k\ge1\), put \(\beta=p/q\), \(n=kq\), and \(N=kp=n\beta\). Define the two-phase map
\[
K(i,x)=\begin{cases}(1,\{\beta x\}),&i=0,\\(0,\{nx\}),&i=1,\end{cases}\qquad x\in[0,1),
\]
where \(\{z\}=z-\lfloor z\rfloor\). Let \(X_j\) be the interval coordinate of the stationary process, including its uniformly randomized initial phase. Define
\[
a=\lfloor\beta\rfloor,\quad r=\beta-a\in(0,1),\quad
A=\frac{a(1-3r+3r^2)+r^3}{12\beta^2},\quad
\delta=\frac{r(1-r)}{4\beta}.
\]
Then the entire positive-lag coordinate covariance is
\[
\operatorname{Cov}(X_0,X_{2t})=\delta^2+\left(\frac1{24}+\frac{\beta A}{2}\right)N^{-t},\qquad t\in\mathbb N,\ t\ge1,
\]
\[
\operatorname{Cov}(X_0,X_{2t+1})=-\delta^2+\left(\frac A2+\frac{\beta}{24N}\right)N^{-t},\qquad t\in\mathbb Z,\ t\ge0.
\]
Both \(A\) and \(\delta\) are strictly positive. In particular, a common stationary measure does **not** imply identical coordinate autocorrelation. The lag-two statistic identifies the even-step expansion factor exactly:
\[
N=\frac{1/24+\beta A/2}{\operatorname{Cov}(X_0,X_2)-\delta^2},\qquad n=N/\beta.
\]
All even-lag covariances approach \(+\delta^2\), whereas all odd-lag covariances approach \(-\delta^2\); both approaches are geometric. The lag-one covariance is positive, so the odd-lag covariance changes sign at a finite lag, with at most one zero. The full zero-lag variance is
\[
\operatorname{Var}(X_0)=\delta^2+\frac12\left(\frac1{12}+\frac{a+r^3}{3\beta}-\left(\frac{a+r^2}{2\beta}\right)^2\right).
\]

## Assumptions and scope

All parameters are integers \(p>q>1\), \(\gcd(p,q)=1\), \(k\ge1\); \(\beta=p/q\) is therefore nonintegral. The state space carries its Borel sigma algebra. The stationary measure is the unique absolutely continuous \(K\)-invariant probability, already established in the literature. Correlation is ordinary centered covariance of the real interval coordinates, not circular distance, phase-conditional covariance, or a digit observable. The phase at time zero is selected with probability one half each.

Writing \(U\) for uniform Lebesgue measure on \([0,1)\) and \(f(u)=\{\beta u\}\), the stationary measure is explicitly
\[
\mu=\frac12\bigl(\delta_0\otimes\mathcal L(U)+\delta_1\otimes\mathcal L(f(U))\bigr).
\]
For all positive \(k\), this probability is identical, although the maps are different. The two-step phase-zero map is \(F(u)=\{Nu\}\) and the two-step phase-one map is its factor through \(f\).

## Proof

**1. Invariant measure and phase trajectories.** Since \(n\) is an integer and \(n\beta=N\in\mathbb N\),
\[
\{n\{\beta u\}\}=\{Nu\}=F(u).
\]
Lebesgue measure is invariant under the integer map \(F\). From phase zero, the successive coordinates are \(U,f(U),F(U),f(F(U)),\ldots\). From phase one, they are \(f(U),F(U),f(F(U)),F^2(U),\ldots\). Averaging the two initial phases therefore produces the displayed stationary measure. The known uniqueness of an absolutely continuous stationary probability identifies it as the distinguished invariant measure. Its law is independent of \(k\).

**2. Elementary sawtooth moments.** Write \(\beta=a+r\), with \(a\in\mathbb N\) and \(0<r<1\). Splitting the interval at the finitely many discontinuities \(j/\beta\) and integrating the affine formula \(f(u)=\beta u-j\) yields
\[
\mathbb E[f(U)]=\mu_1=\frac{a+r^2}{2\beta},\quad
\mathbb E[f(U)^2]=\frac{a+r^3}{3\beta},\quad
\operatorname{Cov}(U,f(U))=A.
\]
Since \(\mathbb E U=1/2\), the phase-mean half-gap is \(\delta=(1/2-\mu_1)/2=r(1-r)/(4\beta)\). The polynomial \(1-3r+3r^2=3(r-1/2)^2+1/4\) gives \(A>0\).

**3. Conditional-affine identities.** For any integer \(Q\ge1\), define \(V_Q(u)=\{Qu\}\). Given \(V_Q(U)=y\), the \(Q\) inverse points \((j+y)/Q\), with \(j=0,\ldots,Q-1\), have equal conditional weights. Consequently,
\[
\mathbb E[U\mid V_Q(U)=y]=\frac{Q-1}{2Q}+\frac yQ,
\]
and, for any integrable function \(g\) with finite covariance,
\[
\operatorname{Cov}(U,g(V_Q(U)))=\frac1Q\operatorname{Cov}(U,g(U)). \tag{1}
\]
If additionally \(p\mid Q\), every discontinuity of \(f\) lies on a \(1/Q\) grid line, because the discontinuities are \(j/\beta=jq/p\). Thus on each inverse cell \(f((j+y)/Q)\) has slope \(\beta/Q\) in \(y\), independently of \(j\). Their conditional average, with the correct unconditional mean, is
\[
\mathbb E[f(U)\mid V_Q(U)=y]=\mu_1+\frac\beta Q(y-1/2).
\]
It follows that
\[
\operatorname{Cov}(f(U),g(V_Q(U)))=\frac\beta Q\operatorname{Cov}(U,g(U)). \tag{2}
\]
There are no boundary complications: grid boundaries form a null set.

**4. Even and odd covariance laws.** For \(t\ge1\), apply (1) with \(Q=N^t\), \(g(u)=u\), to get
\(\operatorname{Cov}(U,F^t(U))=1/(12N^t)\). Since \(p\mid N^t\), applying (2) with \(g=f\) gives
\(\operatorname{Cov}(f(U),f(F^t(U)))=\beta A/N^t\).
For \(t\ge0\), (1) with \(Q=N^t\) and \(g=f\) gives
\(\operatorname{Cov}(U,f(F^t(U)))=A/N^t\). Applying (2) with \(Q=N^{t+1}\) and \(g(u)=u\) gives
\(\operatorname{Cov}(f(U),F^{t+1}(U))=\beta/(12N^{t+1})\).

The law of total covariance over the equiprobable initial phases gives one half the sum of the two phase-conditional covariances plus the covariance of their conditional means. The latter equals \(+\delta^2\) at even lags and \(-\delta^2\) at odd lags. Substituting the four identities proves the formulas for all stated lags. The zero-lag variance follows by the same decomposition.

**5. Identifiability and sign transition.** The even-lag coefficient \(1/24+\beta A/2\) is strictly positive, so the lag-two formula uniquely determines \(N\), hence \(n\), for fixed \(\beta\). The odd-lag correction is positive and strictly decreases with \(t\). Moreover \(A/2\ge1/(96\beta^2)\) while \(\delta^2\le1/(256\beta^2)\), so \(\operatorname{Cov}(X_0,X_1)>0\). Its odd-lag limit is \(-\delta^2<0\). Thus the odd-lag sequence crosses zero exactly once in the sense of changing sign between successive terms; a single term may itself vanish.

## Verification

The standard-library checker `verify_alternate_base.py` constructs exact rational piecewise-affine branches and independently integrates products of coordinate observables. Execute with `python verify_alternate_base.py`. It verifies the stationary component mean, lag-zero input covariance, and the two formulas at lags one through four for ten combinations of rational bases and multiples of their denominators. Its output is `VERIFY_OK rational_base_cases=10 exact_affine_integral_checks=60 lags=1..4 stationary_component_means=verified`. These finite tests are corroboration, not the proof for all parameters and lags; the conditional identities (1) and (2) supply that proof.

For example, with \(\beta=3/2\), one has \(A=1/72\), \(\delta^2=1/576\), \(N=3k\), and
\[
C_{2t}=\frac1{576}+\frac5{96}(3k)^{-t},\qquad
C_{2t+1}=-\frac1{576}+\left(\frac1{144}+\frac1{48k}\right)(3k)^{-t}.
\]

## Relationship to prior work

Dajani and Langeveld [1], especially Proposition 3.1 and Theorems 1.2 and 3.6, establish exactly when the absolutely continuous invariant measures of the alternating maps coincide. The component decomposition in [1] gives the stationary law used here. The earlier Charlier–Cisternino–Dajani study [2] establishes invariant measures, ergodicity, entropy, and digit frequencies for more general alternate bases. Neither inspected treatment provides an explicit all-lag coordinate-covariance law or proves that the coincident-measure family can be identified by its lag-two coordinate correlation. The proof here uses the special arithmetic relation \(n\beta\in\mathbb N\) and does not claim a corresponding law for generic alternate bases.

## Limitations

This theorem concerns deterministic period-two maps with nonintegral rational first base and second base an integer multiple of the reduced denominator. It does not provide covariance formulas for general irrational bases, for other integer multipliers, or for digit observables. The stationary coordinate process is not mixing because the deterministic two-phase mean persists; the formulas quantify the remaining geometric within-phase decay. The priority comparison uses accessible primary sources and mathematical-index searches; an unindexed equivalent calculation cannot be excluded and independent verification remains outstanding.

## References

[1] K. Dajani and N. Langeveld, *Coincidence of invariant measure for the alternate base transformations*, arXiv:2603.12877v1 (first posted 2026-03-13), https://arxiv.org/abs/2603.12877.

[2] É. Charlier, C. Cisternino, and K. Dajani, *Dynamical behavior of alternate base expansions*, arXiv:2102.08627v1 (2021); *Ergodic Theory and Dynamical Systems* **43** (2023), 827–860, https://arxiv.org/abs/2102.08627.
