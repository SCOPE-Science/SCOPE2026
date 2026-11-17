# Universal switching statistics and a sharp physical-entropy gap in minimal-rank interval maps

## Finding
For every integer \(n\ge3\) and every orientation word \(\varepsilon=(\varepsilon_0,\ldots,\varepsilon_{n-1})\in\{-1,+1\}^n\) whose **last two orientations coincide**, consider the affine, piecewise-expanding Markov map defined below. Write \(A\) and \(B\) for the numbers of adjacent transitions \(-1\to+1\) and \(+1\to-1\), and let \(\kappa=A+B\), so \(0\le\kappa\le n-2\). Define the branch-switch observable \(w_0=0\) and \(w_j=\mathbf1_{\{\varepsilon_{j-1}\ne\varepsilon_j\}}\) for \(1\le j<n\).

The invariant probability \(\mu\) equivalent to Lebesgue measure has the following exact masses on the \(n\) equal partition intervals:
\[
\pi_0=\frac{n-1-A}{n(n-1)-\kappa},\quad
\pi_j=\frac{n-1}{n(n-1)-\kappa}\ (1\le j\le n-2),\quad
\pi_{n-1}=\frac{n-1-B}{n(n-1)-\kappa}.
\]
It is mixing, and its basin has full Lebesgue measure. For every \(\kappa>0\), the switch sequence \(W_t=w_{X_t}\), where \(X_t\) is the partition label of the \(t\)th iterate, is **exactly a stationary two-state Markov chain under \(\mu\)** with transition matrix (rows and columns indexed by \(0,1\))
\[
Q=\begin{pmatrix}1-\kappa/n&\kappa/n\\1-\kappa/(n-1)&\kappa/(n-1)\end{pmatrix}.
\]
The same transition law holds from a Lebesgue-distributed initial point, with nonstationary initial probability \(\mathbb P(W_0=1)=\kappa/n\). Thus all finite-dimensional switch laws depend **only** on \((n,\kappa)\), regardless of the order of orientations or the split between \(A\) and \(B\).

Let \(p=\kappa(n-1)/(n(n-1)-\kappa)\) and \(\lambda=\kappa/[n(n-1)]\). Under \(\mu\), for every integer lag \(t\ge0\),
\[
\mathbb E W_t=p,\qquad \operatorname{Cov}(W_0,W_t)=p(1-p)\lambda^t.
\]
For a Lebesgue- or \(\mu\)-distributed initial point, the centered switch count obeys a Gaussian central-limit law with variance per iterate
\[
\sigma^2=p(1-p)\frac{1+\lambda}{1-\lambda}.
\]
For \(\kappa=0\), the switch count is identically zero and these formulas hold with \(p=\sigma^2=0\).

The metric entropy of the physical measure and the topological entropy are respectively
\[
h_\mu(F)=(1-p)\log n+p\log(n-1),\qquad
h_{\rm top}(F)=\log\frac{n+\sqrt{n^2-4\kappa}}2.
\]
The entropy gap \(h_{\rm top}(F)-h_\mu(F)\) is **strictly positive for every \(1\le\kappa\le n-2\)**, equals zero for \(\kappa=0\), and for any integer sequence \(n\to\infty\) with \(\kappa_n/n\to\theta\in(0,1)\) satisfies the sharp limit
\[
\lim_{n\to\infty}n^2\bigl(h_{\rm top}(F_n)-h_{\mu_n}(F_n)\bigr)=\frac{\theta(1-\theta)}2.
\]
The assertion is one structural statistical classification for the specified affine realizations; it does not assert analogous laws for arbitrary maps with the same orientation word.

## Assumptions and scope
Let \(c_j=j/n\), \(0\le j\le n\), and \(J_j=(c_j,c_{j+1})\). At an interior cut \(c_i\), prescribe the ordered one-sided values \((F(c_i^-),F(c_i^+))\) by the adjacent orientation pair:

| \((\varepsilon_{i-1},\varepsilon_i)\) | left value | right value |
| --- | --- | --- |
| \((-1,-1)\) | \(0\) | \(1\) |
| \((+1,+1)\) | \(1\) | \(0\) |
| \((-1,+1)\) | \(0\) | \(1/n\) |
| \((+1,-1)\) | \(1\) | \((n-1)/n\) |

Prescribe \(F(0^+)=1\) when \(\varepsilon_0=-1\), and \(F(0^+)=0\) otherwise; prescribe \(F(1^-)=0\) when \(\varepsilon_{n-1}=-1\), and \(F(1^-)=1\) otherwise. Interpolate affinely on each \(J_j\). Values at cuts are immaterial, and assertions about the itinerary exclude the countable set of points whose forward orbit hits a cut. This is exactly the canonical affine realization in Oliveira's Theorem 7.1, restricted to \(\varepsilon_{n-2}=\varepsilon_{n-1}\). The branch entropy uses the symbolic itinerary convention for discontinuous maps.

## Proof
**1. Markov geometry and expansion.** Let \(w_j\) indicate an orientation change at cut \(c_j\) (and set \(w_0=0\)). The one-sided value table shows that each \(F(J_j)\) comprises all \(n\) partition interiors if \(w_j=0\), and all but exactly one of the two extreme partition interiors if \(w_j=1\). More precisely, \(-1\to+1\) omits \(J_0\), while \(+1\to-1\) omits \(J_{n-1}\). Since the last adjacent pair has equal orientations, both extreme branch indices have \(w_j=0\). All \(\kappa\) switching indices therefore lie in \(\{1,\ldots,n-2\}\) and are contained in the image of **every** branch. Each affine slope has absolute value \(s_j=n-w_j\ge n-1\ge2\). Writing \(M_{jk}=\mathbf1_{\{J_k\subset F(J_j)\}}\), its rows have \(n-w_j\) ones. Every row reaches every interior state, and a non-switching extreme state reaches every state. Hence \(M\) is primitive.

**2. Exact Markov law.** On any nonempty cylinder defined by labels \(X_0=j_0,\ldots,X_t=j_t\), the map \(F^t\) is affine and carries that cylinder onto the entire current interval \(J_{j_t}\), since each admissible transition covers its whole target interval. A distribution with constant density on each initial \(J_j\) is therefore conditionally uniform on the current interval, even after conditioning on the complete past labels. The exact branch transition matrix is
\[
P_{jk}=\frac{M_{jk}}{n-w_j}.
\]
This applies to Lebesgue measure and to the piecewise-constant invariant probability constructed next. As every image contains all \(\kappa\) switching states, the sum \(\sum_{k:w_k=1}P_{jk}\) is \(\kappa/(n-w_j)\). It depends only on \(w_j\), proving strong lumpability and the displayed two-state transition matrix. The Lebesgue initial switch probability is exactly \(\kappa/n\).

**3. Physical invariant law.** Put \(D=n(n-1)-\kappa\) and define \(\pi\) by the displayed formulas. Its entries are positive and sum to one. The stationarity equations \(\pi P=\pi\) can be checked directly: every interior target receives \(\sum_j\pi_j/(n-w_j)=(n-1)/D\); target \(0\) lacks contributions from the \(A\) rows of type \(-1\to+1\), and target \(n-1\) lacks contributions from the \(B\) rows of type \(+1\to-1\). The omitted rows are interior, each of stationary mass \((n-1)/D\) and slope \(n-1\), so these omissions subtract \(A/D\) and \(B/D\), respectively. Thus \(\pi P=\pi\) exactly. The probability with density \(n\pi_j\) on \(J_j\) is \(F\)-invariant. Primitivity and shrinking cylinders make its symbolic Markov chain mixing and give an almost-everywhere one-to-one coding. Its density is uniformly positive and bounded, so the measure is equivalent to Lebesgue; ergodicity then makes its basin full Lebesgue measure and rules out any second absolutely continuous invariant probability.

**4. Correlations and fluctuation law.** The stationary one-state probability for the two-state chain is \(p=\kappa(n-1)/D\). Its nontrivial eigenvalue is \(\lambda=\kappa/(n-1)-\kappa/n\), giving the exact covariance at every nonnegative lag. The finite, primitive two-state chain obeys a central-limit theorem for any initial distribution, with Green--Kubo variance \(p(1-p)[1+2\sum_{t\ge1}\lambda^t]=p(1-p)(1+\lambda)/(1-\lambda)\). All normalizations and the \(\kappa=0\) boundary case follow directly.

**5. Entropy and strict gap.** Since \(F\) is a generating expanding Markov map, its metric entropy equals the entropy rate of the branch chain. Each branch row contains \(n-w_j\) equiprobable transitions, so \(h_\mu(F)=\sum_j\pi_j\log(n-w_j)=(1-p)\log n+p\log(n-1)\). Oliveira's Corollary 7.3 gives the topological entropy formula. To prove strict inequality when \(\kappa>0\), the primitive Markov graph has a unique maximal-entropy (Parry) chain with transitions \(M_{jk}v_k/(\rho v_j)\), for positive Perron eigenvector \(v\). If the physical chain \(P\) coincided with it, the all-one row for state \(0\) would force \(v_k\) to be constant in \(k\). That contradicts the unequal row sums \(n\) and \(n-1\) of \(M\). Hence the physical chain is not the unique entropy maximizer. At \(\kappa=0\), all rows are full and the physical measure has entropy \(\log n\).

**6. Sharp large-alphabet limit.** With \(r=\kappa/n\), \(x=1/n\), the exact gap is
\[
\log\frac{1+\sqrt{1-4rx}}2
-\frac{r(1-x)}{1-(1+r)x}\log(1-x).
\]
Taylor expansion uniformly for \(0\le r\le1\) gives \(\tfrac12r(1-r)x^2+O(x^3)\). If \(r\to\theta\in(0,1)\), multiplication by \(n^2\) proves the stated asymptotic limit.

## Verification
Run the standalone Python 3 program `check.py` with no third-party packages. It independently reconstructs affine branch endpoints from the cut-value table, generates the Markov matrix by exact rational containment tests, and checks the stationary distribution, the two-state transition sums, the first eight exact autocovariances, and arrangement-independent results for **every** \(n\)-letter orientation word ending in equal signs, for \(3\le n\le11\). It also checks the asymptotic entropy gap at five larger alphabet sizes. All of these are finite checks; the universal claims above are established by the proof, not by enumeration.

## Relationship to prior work
Oliveira, *Homological reduction and entropy of discontinuous interval maps*, arXiv:2611.03287v1 (November 2, 2026), Theorems 7.1--7.2 and Corollary 7.3, supplies the canonical affine construction, its homological rank, the form of the unweighted Markov matrix, and its topological entropy. Those are not new claims here. The added result identifies the physical invariant law, an arrangement-independent **stochastic factor**, its exact fluctuations, and the strictly positive yet asymptotically small physical-versus-topological entropy gap. General existing theorems on piecewise-linear invariant densities and strong lumpability provide background tools but do not identify this parameter-uniform factor and asymptotic coefficient without the present analysis. Priority against unindexed equivalent calculations is not established independently.

## Limitations
Only the canonical affine maps associated with orientation words ending in equal signs are covered. A different Markov realization of the same orientation word need not have the asserted switch process. The central-limit theorem is a distributional statement for random initial conditions, not an almost-sure Gaussian limit for an individual trajectory. The cut values and their preimages have no role in the absolutely continuous statistical assertions. The claim neither establishes a full transfer-operator spectrum nor classifies arbitrary invariant or equilibrium measures.

## References
1. H. M. Oliveira, *Homological reduction and entropy of discontinuous interval maps*, arXiv:2611.03287v1, posted November 2, 2026, especially Sections 7.1--7.2 and Corollary 7.3. https://arxiv.org/abs/2611.03287
2. P. Góra, *Invariant densities for piecewise linear maps of the unit interval*, Ergodic Theory and Dynamical Systems (2009). https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/abs/invariant-densities-for-piecewise-linear-maps-of-the-unit-interval/97E6074A0AC5A757F3A68F7C0B3B6063
3. J. G. Kemeny and J. L. Snell, *Finite Markov Chains*, second edition, Springer, 1978, on lumpability and finite-state stochastic reductions.
