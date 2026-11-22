# Parity-locked synchronization and exact covariance under shared-noise sign gradient descent

## Finding

A separable quadratic can exhibit almost-sure, finite-time *coordinate synchronization* when its sign-gradient oracle uses one common uniform random perturbation. In the commensurate finite-state model below, all coordinates initialized in the same lattice-parity class become identical after a finite random time, and coordinates from opposite classes become permanently adjacent. The full multivariate stationary law and the variance of the coordinate average are explicit.

**Theorem.** Fix integers \(d\ge2\) and \(m\ge1\), and numbers \(\delta>0\), \(B=m\delta\). Let \(f(x)=\|x\|_2^2/2\) on \(\mathbb R^d\). Independently for each iteration \(t\), draw a *single* \(U_t\sim\operatorname{Unif}[-B,B]\), use the unbiased stochastic gradient \(\widetilde g_t=x_t+U_t\mathbf 1\), and update every coordinate simultaneously by
\[
x_{t+1}^{(i)}=x_t^{(i)}-\delta\operatorname{sgn}(x_t^{(i)}+U_t).
\]
Assume every initial coordinate belongs to \(\{-B,-B+\delta,\ldots,B\}\), and define \(K_{t,i}=(x_{t,i}+B)/\delta\in\{0,\ldots,2m\}\). The probability-zero case of a vanishing noisy gradient may be assigned either sign.

For every pair \(i,j\), put \(G_t=|K_{t,i}-K_{t,j}|\). When \(g\ge2\),
\[
\Pr(G_{t+1}=g-2\mid G_t=g)=\frac{g}{2m},\qquad
\Pr(G_{t+1}=g\mid G_t=g)=1-\frac{g}{2m}.
\]
The gaps \(g=0,1\) are absorbing. In particular, if \(G_0=2k\), the exact time \(T\) to equal coordinates has the distribution
\[
T\ \stackrel d=\ \sum_{j=1}^{k}\operatorname{Geom}(j/m),\qquad
\mathbb ET=m\sum_{j=1}^{k}\frac1j,
\]
with independent geometric variables on \(\{1,2,\ldots\}\), and empty sum zero. If \(G_0=2k+1\), the exact time to permanent adjacency has distribution
\[
T\ \stackrel d=\ \sum_{j=1}^{k}\operatorname{Geom}\left(\frac{2j+1}{2m}\right),\qquad
\mathbb ET=2m\sum_{j=1}^{k}\frac1{2j+1}.
\]
If all \(d\) initial coordinates have the same parity and initial index span \(2k\), **the first time all \(d\) coordinates agree has exactly the first distribution above**, regardless of \(d\). For arbitrary parity patterns, the process almost surely reaches and forever remains in a set consisting of at most two distinct coordinate values, separated by exactly one lattice step if both parities are represented.

The chain on the recurrent class specified by the initial parity pattern has a unique invariant probability measure, though it has period two. When only one parity class occurs, every coordinate shares a common \(K\sim\operatorname{Bin}(2m,1/2)\). When both parity classes occur, there are independent random variables
\[
L\sim\operatorname{Bin}(2m-1,1/2),\qquad R\sim\operatorname{Bernoulli}(1/2),
\]
and coordinates in the first class have \(K=L+R\), while those in the other class have \(K=L+1-R\). Thus every coordinate has stationary variance \(m\delta^2/2=B\delta/2\); distinct coordinates in the same parity class have stationary correlation \(1\), while those in opposite parity classes have correlation
\[
\boxed{1-\frac1m=1-\frac{\delta}{B}}.
\]
If the first class contains \(r\) coordinates and the second contains \(d-r\), the exact stationary variance of the coordinate average is
\[
\boxed{\operatorname{Var}_\pi\left(\frac1d\sum_{i=1}^d x_i\right)
=\frac{B\delta}{2}-\frac{r(d-r)}{d^2}\delta^2.}
\]
In particular, for all initial coordinates in one parity class, this variance is \(B\delta/2\), **independent of the number of coordinates**; under independent coordinate-wise noise of the same marginal law, the stationary variance would instead be \(B\delta/(2d)\). These statements concern the unique invariant law or Cesàro time averages, not unqualified one-time distributional convergence.

## Assumptions and scope

The objective is isotropic and separable. The stochastic gradient oracle has unbiased perfectly correlated additive noise with covariance \((B^2/3)\mathbf1\mathbf1^\mathsf T\). The common perturbation is freshly drawn independently at every iteration, not separately for each coordinate. The amplitude-step commensurability \(B=m\delta\) and support-aligned starting lattice are essential for the exact binomial formulas. The model is not an adaptive stochastic-optimization schedule, and it does not represent arbitrary correlated gradient-noise distributions.

The parity of the initial index \(K_{0,i}\) distinguishes classes. At each update every index changes by exactly one, so these *relative* parity classes persist. A physical coordinate can change between the two neighboring values in the mixed-class regime; its fixed parity-group identity refers to initialization, not to which value is currently larger.

## Proof

**1. Exact lattice map.** The state band is forward invariant: at \(K=0\) the stochastic gradient is negative almost surely and at \(K=2m\) it is positive almost surely. At index \(k\), the downward step probability is \(k/(2m)\) and upward step probability \((2m-k)/(2m)\), giving a classical \(2m\)-ball Ehrenfest marginal. In particular its unique invariant marginal is \(2^{-2m}\binom{2m}{k}\).

**2. Exact pair coupling.** Suppose \(k<\ell\). A common uniform perturbation falls between the two noisy-gradient sign thresholds, a length \((\ell-k)\delta\) subinterval of \([-B,B]\), with probability \((\ell-k)/(2m)\). Only on this event do the lower and upper coordinates move toward each other; the gap shrinks by two, or if it is one the two values swap positions. Otherwise the two coordinates move in the same direction and the gap stays unchanged. Hence \(G\) has the asserted pure-death transition rule, and its parity is invariant. Positive decrease probability at every \(g\ge2\) gives almost-sure absorption. Strong Markov renewal at each successive gap level gives independent geometric holding times, proving both distributions, including all endpoints.

**3. Simultaneous synchronization.** Two indices with the same parity cannot cross without first becoming equal: every positive even gap either remains the same or decreases by two. Therefore the smallest and largest *initial* members of a parity class remain its extrema until they meet. Every member lies between them at each iteration. Their meeting time is thus exactly the whole-class coalescence time and has the geometric-sum law determined only by their initial span. In a finite number of classes (at most two), within-class coalescence happens almost surely. An opposite-parity pair must also reach gap one almost surely, so the final two class values are permanently adjacent.

**4. Mixed-class invariant law.** In the two-class recurrent set write the lower index as \(L\in\{0,\ldots,2m-1\}\) and record by \(R\in\{0,1\}\) which fixed class has the higher index. The transitions are: \(L\mapsto L-1\), orientation unchanged, with probability \(L/(2m)\); \(L\mapsto L+1\), orientation unchanged, with probability \((2m-1-L)/(2m)\); or \(L\) unchanged and orientation reversed with probability \(1/(2m)\). At boundaries the impossible moves have probability zero. The proposed measure
\[
\pi(L=\ell,R=r)=\frac12\,2^{-(2m-1)}\binom{2m-1}{\ell}
\]
satisfies detailed balance for both adjacent-lower-index transitions, using the binomial recursion, and for each orientation reversal, by symmetry. The finite chain is irreducible: lower indices communicate by nearest-neighbor moves and orientations can flip at any lower index. Thus this is its unique invariant law. When only one class is represented, all coordinates coincide after absorption and the standard irreducible Ehrenfest chain has its unique binomial invariant law.

Every state update flips the parity of each individual index. Consequently all these recurrent chains have period two. They possess unique invariant laws and converge to them in Cesàro mean, but a deterministic initial state cannot converge in distribution to a parity-mixing invariant law at ordinary integer times.

**5. Covariance and averaging cost.** In the mixed case \(K_i=L+R\) and \(K_j=L+1-R\) for opposite classes. The independent components have \(\operatorname{Var}L=(2m-1)/4\) and \(\operatorname{Var}R=1/4\). Hence \(\operatorname{Var}K_i=m/2\) and \(\operatorname{Cov}(K_i,K_j)=(m-1)/2\). Within a class the two indices agree identically at stationarity, giving covariance \(m/2\). Multiplying by \(\delta^2\) and summing the \(d^2\) covariance terms gives
\[
\operatorname{Var}_\pi(\overline x)=\frac{m\delta^2}{2}-\frac{r(d-r)}{d^2}\delta^2.
\]
With separate iid uniform noises, the \(d\) scalar Ehrenfest chains are independent under their product invariant law, so the variance is \(m\delta^2/(2d)\). The variance contrast is therefore an exact effect of using one shared stochastic perturbation, not of cross-coordinate curvature.

## Verification

The supplied standalone `verify.py` uses only Python standard-library exact rationals. It exhaustively enumerates the \(2m\) equiprobable noise subintervals for every ordered pair of lattice states for \(m=1,\ldots,11\), checking the full gap kernel, the scalar binomial detailed-balance identities, the oriented-adjacent invariant distribution, covariances, and exact mean hitting-time recurrences. It also checks the proposed complete stationary distributions under all distinct three-coordinate parity patterns for \(m=1,\ldots,6\). Running `python verify.py` produced `PASS 11056 exact-rational assertions; pair M=1..11 and three-coordinate M=1..6`. This finite check is corroboration; the all-dimension theorem follows from the analytical arguments above, not finite extrapolation.

## Relationship to prior work

Bernstein, Wang, Azizzadenesheli, and Anandkumar (2018) introduce signSGD and convergence analyses under unbiased stochastic-gradient noise. Their algorithm includes this sign update as an instance, but their results do not specify a shared-uniform lattice coupling or exact multivariate stationary law. Balles, Pedregosa, and Le Roux (2020) analyze deterministic and stochastic sign-gradient geometry under smoothness assumptions rather than the joint stationary distribution induced by common noise.

The existing published scalar additive-uniform signSGD Ehrenfest result [3] already gives every one-coordinate binomial marginal, period-two behavior, and the linear stationary objective floor. **None of those scalar facts is asserted as new here.** It explicitly excludes multidimensional coupling. The new mathematical object is the *joint* shared-uniform-noise transition kernel: its pure-death gap, finite-time coalescence law, two-class invariant coupling and exact averaged-iterate variance. Standard Ehrenfest and Markov-coupling textbook results [4] supply the scalar birth-death and coupling concepts but do not, in the inspected relevant sections, establish this particular common-threshold sign-gradient joint law and its averaging penalty. The geometric waiting-time distributions follow from a familiar pure-death argument once the joint kernel has been identified; no new abstract Markov-chain coupling principle is claimed.

## Limitations

The results require a single perfectly shared, bounded uniform perturbation at every step, exactly equal isotropic quadratic curvatures, fixed step size, and support-aligned lattice initialization. They do not extend automatically to general quadratics, independent or partially shared noise, continuous unaligned initial coordinates, arbitrary noise laws, momentum, or decreasing steps. All deterministic initializations discussed are within the stated finite support. The invariant law is periodic in discrete time; Cesàro, stationary, and parity-subsequence statements must not be conflated. The one-coordinate Ehrenfest identification and standard finite-state coupling methods are prior art; an undiscovered mathematically equivalent coupled-Ehrenfest statement in older Markov-chain literature remains a historical-priority risk. No independent mathematical audit is claimed.

## References

1. J. Bernstein, Y.-X. Wang, K. Azizzadenesheli, and A. Anandkumar, “signSGD: Compressed Optimisation for Non-Convex Problems,” arXiv:1802.04434v1 (first public 2018-02-13), https://arxiv.org/abs/1802.04434 ; published in Proceedings of Machine Learning Research 80 (2018), https://proceedings.mlr.press/v80/bernstein18a/bernstein18a.pdf .
2. L. Balles, F. Pedregosa, and N. Le Roux, “The Geometry of Sign Gradient Descent,” arXiv:2002.08056v1 (2020), https://arxiv.org/html/2002.08056v1 .
3. “Exact Ehrenfest law and linear noise floor for additive-noise signSGD,” public research record (2026-10-04), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-ehrenfest-law-and-linear-noise-floor-for-additive-noise-si--91e3f2750878 .
4. U. Porod, *Dynamics of Markov Chains for Undergraduates* (2024), sections 11.2.4 and 11.3, https://www.math.northwestern.edu/documents/book-markov-chains.pdf .
