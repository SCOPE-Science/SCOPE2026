# Twelve states are the sharp threshold for two geometric-reset splitting extrema

## Finding
Consider a discrete-time nearest-neighbor birth–death chain with states \(\{0,1,\ldots,a\}\), absorbing at both endpoints, and strictly positive nearest-neighbor transition probabilities in every interior state. Start at an interior state \(z\). Before each new step following a nonabsorbing step, independently restart at \(z\) with probability \(1-s\), where \(0<s\le1\). Let \(Q_{a,z}(s)\) be the probability of eventual absorption at zero.

**Theorem.** For every integer \(2\le a\le10\), every interior starting state, and every admissible transition vector, \(Q_{a,z}\) has at most one stationary point in \(0<s<1\), unless it is constant. In particular it cannot have two distinct strict local extrema. This bound is sharp: for \(a=11\) (twelve states including the absorbing endpoints), an explicit strictly positive rational transition vector gives exactly two stationary points in \(0<s<1\), a strict local minimum followed by a strict local maximum. Thus twelve is the **smallest total state count permitting two distinct strict interior extrema** of the endpoint splitting probability as the geometric reset strength varies.

For the sharp example, start at \(z=5\) and take right-step probabilities, indexed by interior states \(1,\ldots,10\), to be
\[
(p_1,\ldots,p_{10})=(95,10,80,30,1,40,75,45,40,10)/100.
\]
With \(t=s^2\), define
\[
L(t)=1-\frac{457}{400}t+\frac{423}{2000}t^2,\qquad
R(t)=1-\frac{287}{200}t+\frac{1197}{2500}t^2.
\]
Then the exact splitting probability is
\[
Q_{11,5}(s)=\frac{231L(s^2)}{231L(s^2)+2sR(s^2)}.
\]
Its only two critical values correspond to squared reset-survival parameters \(t_1\in(4/5,9/10)\) and \(t_2\in(99/100,999/1000)\). More precisely, \(t_1\approx0.828754728626\) and \(t_2\approx0.993911318262\). The first is a strict minimum and the second a strict maximum. The existence of a two-extremum eleven-step example was known; the new assertion is its **global minimality over every shorter inhomogeneous birth–death path and every reset site**.

## Assumptions and scope
For each interior \(i\in\{1,\ldots,a-1\}\), put \(p_i\in(0,1)\) and \(q_i=1-p_i\). The chain moves from \(i\) to \(i+1\) with probability \(p_i\), and from \(i\) to \(i-1\) with probability \(q_i\). There are no holding transitions. The reset clock is independent and identically renewed after each reset; the convention is that an absorption on the just-taken step overrides resetting. The survival weight of the clock through \(n\) steps is proportional to \(s^n\), which is equivalent to \(s^{n-1}\) in the conditional exit quotient. The endpoints are absorbing. A stationary point means a zero of the derivative with respect to \(s\) in the open interval \((0,1)\); identically constant functions are excluded from the count. This theorem makes no assertion for nongeometric or state-dependent reset clocks, chains with holding, or non-nearest-neighbor jumps.

## Proof
### 1. Discounted two-exit identity
Let \(P\) be the transient matrix on \(\{1,\ldots,a-1\}\). For a contiguous subinterval \(I\), write \(D_I(s)=\det(I-sP_I)\), with \(D_\varnothing=1\). By the tridiagonal cofactor formula, the first-passage generating functions from \(z\) to the endpoints are
\[
F_0(s)=\frac{s^z\big(\prod_{i=1}^{z}q_i\big)D_{\{z+1,\ldots,a-1\}}(s)}{D_{\{1,\ldots,a-1\}}(s)},\quad
F_a(s)=\frac{s^{a-z}\big(\prod_{i=z}^{a-1}p_i\big)D_{\{1,\ldots,z-1\}}(s)}{D_{\{1,\ldots,a-1\}}(s)}.
\]
This identity also follows directly by solving the second-order discounted hitting-probability recurrence with the boundary conditions. Restart renewal yields \(Q=F_0/(F_0+F_a)\). Consequently, with \(C=\prod_{i=1}^z q_i/\prod_{i=z}^{a-1}p_i>0\),
\[
\frac{Q_{a,z}(s)}{1-Q_{a,z}(s)}=
C s^{2z-a}\frac{D_{\{z+1,\ldots,a-1\}}(s)}{D_{\{1,\ldots,z-1\}}(s)}.\tag{1}
\]
All factors in this expression are strictly positive for \(0<s\le1\), by the killed-chain resolvent or the next spectral factorization. Therefore the zeros and signs of the derivative of the odds agree with those of \(Q'\).

### 2. Spectral factorization
A killed nearest-neighbor path matrix on a contiguous interval of \(h\) interior vertices is symmetrizable to a real symmetric tridiagonal matrix with strictly positive adjacent entries and zero diagonal. Its eigenvalues occur in pairs \(\pm\sqrt{\lambda_j}\), together with a zero when \(h\) is odd. Irreducibility inside the finite killed interval and positive probability of eventual boundary escape imply that all \(0<\lambda_j<1\). Thus
\[
D_I(s)=\prod_{j=1}^{\lfloor h/2\rfloor}(1-\lambda_j s^2).\tag{2}
\]
By reflecting the state space, it suffices to consider \(z\le a/2\). Write \(t=s^2\), \(k=2z-a\le0\), let \(\lambda_1\ge\cdots\ge\lambda_m\) be the right-block parameters in (2), and \(\mu_1\ge\cdots\ge\mu_r\) the left-block parameters, where
\[
m=\left\lfloor\frac{a-z-1}{2}\right\rfloor,\qquad r=\left\lfloor\frac{z-1}{2}\right\rfloor.
\]
The logarithmic derivative of the odds in (1), multiplied by \(s\), is
\[
H(t)=k+2t\left(\sum_{j=1}^{r}\frac{\mu_j}{1-\mu_jt}-\sum_{i=1}^{m}\frac{\lambda_i}{1-\lambda_it}\right).\tag{3}
\]

### 3. Excluding two critical values on every shorter path
Suppose first that \(z<a/2\), so \(k<0\). For \(a\le10\), one has \(r\le1\), irrespective of the number \(m\) of right-block parameters. If \(r=0\), then \(H<0\). If \(r=1\), write the sole left parameter as \(\mu\). When \(\mu\le\lambda_1\) (and \(m\ge1\)), the monotonicity of \(x/(1-xt)\) in \(x\) again gives \(H<0\). If \(m=0\), necessarily \(r=0\) because \(z<a/2\).

It remains to consider \(\mu>\lambda_1\). The identity
\[
\frac{\mu}{1-\mu t}-\frac{\lambda_1}{1-\lambda_1t}
=\frac{\mu-\lambda_1}{(1-\mu t)(1-\lambda_1t)}
\]
reduces the equation \(H(t)=0\) to \(X(t)=Y(t)\), where
\[
X(t)=\frac{(\mu-\lambda_1)t}{(1-\mu t)(1-\lambda_1t)},\qquad
Y(t)=\frac{-k}{2}+\sum_{i=2}^{m}\frac{\lambda_i t}{1-\lambda_it}.
\]
Now \(X(t)\) is strictly increasing, and for every \(i\ge2\),
\[
\frac{X(t)}{\lambda_i t/(1-\lambda_it)}
=\frac{\mu-\lambda_1}{\lambda_i}\,
\frac{1-\lambda_it}{(1-\mu t)(1-\lambda_1t)}
\]
is strictly increasing because \(\mu>\lambda_1\ge\lambda_i\). The quotient of \(X\) by the positive constant \(-k/2\) is also strictly increasing. It follows by taking reciprocals and summing that \(Y/X\) is strictly decreasing. Hence \(H\) has at most one zero on \((0,1)\).

The remaining case is the exact midpoint \(z=a/2\), possible only for even \(a\). For \(a\le10\), (2) has the same number \(r=m\le2\) of parameters on both sides and \(k=0\). With \(r=m\le1\), the sign of (3) is constant or the derivative vanishes identically. With two parameters on each side, sort both pairs decreasingly. If one pair dominates the other coordinatewise, the sign of (3) is constant. Otherwise, after possibly interchanging the pairs, assume \(\mu_1>\lambda_1\) and \(\mu_2<\lambda_2\). Then the difference of the sums in (3) is
\[
\frac{\mu_1-\lambda_1}{(1-\mu_1t)(1-\lambda_1t)}-
\frac{\lambda_2-\mu_2}{(1-\lambda_2t)(1-\mu_2t)}.
\]
The ratio of these two positive summands is strictly increasing for \(0<t<1\): its logarithmic derivative is
\[
\frac{\mu_1}{1-\mu_1t}+\frac{\lambda_1}{1-\lambda_1t}
-\frac{\lambda_2}{1-\lambda_2t}-\frac{\mu_2}{1-\mu_2t}>0,
\]
by \(\mu_1>\lambda_2\) and \(\lambda_1>\mu_2\). Hence the difference vanishes at most once. This proves the universal upper bound for every \(a\le10\), including arbitrary inhomogeneous transition probabilities and starts. Reflection preserves the number of critical values.

### 4. Exact sharpness at eleven steps
For the displayed rational transition vector, direct substitution in (1) gives \(C=231/2\) and the indicated \(L\), \(R\). Differentiation shows that the derivative has the sign of \(-N(s^2)\), with
\[
N(t)=1012662t^4-13375845t^3+33989875t^2-31625000t+10000000.\tag{4}
\]
Exact rational substitution gives
\[
N(4/5)>0,\quad N(9/10)<0,\quad N(99/100)<0,\quad N(999/1000)>0.
\]
Thus two different critical values exist and have the asserted minimum/maximum character. To rule out any further values in \((0,1)\), substitute \(t=u/(1+u)\). Then
\[
(1+u)^4N\!\left(\frac{u}{1+u}\right)
=1692u^4-271095u^3-885125u^2+8375000u+10000000.
\]
The displayed coefficient sequence has exactly two sign changes, so Descartes' rule bounds its positive real roots, counted with multiplicity, by two. The two sign-change brackets already exhibit two distinct roots. The example therefore has exactly two interior extrema, completing sharpness.

## Verification
Run the standalone \(\texttt{check.py}\) with Python 3 and SymPy to reproduce the exact continuants, the full discounted-resolvent expression, the derivative polynomial, four rational sign brackets, the transformed polynomial's sign variation, and independent rational-matrix checks at several reset-survival values. The proof of the universal bound uses spectral factorization and monotone ratios for arbitrary positive transition rates; finite tests are sanity checks rather than the infinite argument.

## Relationship to prior work
Newton and Vega Coso (2026) analyze stochastic ordering of exit-time/exit-side pairs in finite birth–death chains and explicitly pose the classification of interior reset-rate extrema as an open direction. Their rational example concerns oscillations in **exit-time log odds**, not the minimal state count for multiple extrema of the **geometrically reset splitting probability**. Earlier results include an explicit one-extremum example on an eight-state path and an explicit two-extremum example on a twelve-state path. Neither establishes the present global exclusion for every smaller state space. The sharpness witness is reproduced here; the substantive new implication is that no intermediate size can have two such extrema. Pal and Prasad (2019) study a continuously diffusing Brownian particle with reset in an interval and therefore do not provide an inhomogeneous finite-state minimum. No historical-priority claim beyond the inspected literature and database comparisons is made.

## Limitations
The minimum is specific to discrete-time nearest-neighbor birth–death chains without holding, with independent geometric resetting to the same starting site and positive transition probabilities. It does not classify the maximum number of extrema for larger chains, nor general renewal clocks. There remains a risk of an older equivalent theorem in work not found by the searches. The review is not an independent mathematical audit.

## References
1. Tony Newton and Juan Antonio Vega Coso, *Stochastic Orders of the Exit Pair and the Monotone Response to Resetting*, arXiv:2611.01756, publicly submitted 2026-11-01. https://arxiv.org/html/2611.01756v1
2. Arnab Pal and V. V. Prasad, *First passage under stochastic resetting in an interval*, arXiv:1812.03009 (2018), Physical Review E 99, 032123 (2019). https://arxiv.org/abs/1812.03009
