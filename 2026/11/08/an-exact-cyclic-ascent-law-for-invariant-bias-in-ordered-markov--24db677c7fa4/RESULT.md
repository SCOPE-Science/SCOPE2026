# An exact cyclic-ascent law for invariant bias in ordered Markov-generator splitting

## Finding

Every deterministic Lie–Trotter sweep of the individual unit-rate jump generators on a directed cycle has an exactly computable stationary bias, determined only by the cyclic ascent pattern of the edge-update order. The bias is strictly nonzero at every positive step size, admits the sharp dimension-free envelope \(\tanh(h/4)\), and disappears **exactly** if the sweep is independently rotated through a uniformly random cyclic origin each iteration.

For every integer \(n\ge2\), every \(h>0\), and every permutation \(\sigma\) of the \(n\) directed edges, put \(u=1-e^{-h}\). Let \(r_i\) be the ordinal position of edge \(i\) in the sweep, and let
\[
 d_i=\mathbf 1_{\{r_{i-1}<r_i\}},\qquad m=\sum_{i=0}^{n-1}d_i,
\]
with vertex indices modulo \(n\). Then \(1\le m\le n-1\), and the unique stationary probability of the splitting step is
\[
 \boxed{\pi_i=\frac{1-u d_i}{n-u m}.}
\]
The exact invariant-measure error against the continuous-time chain's uniform stationary law \(U\) is
\[
 \boxed{\|\pi-U\|_{\mathrm{TV}}=\frac{u m(n-m)}{n(n-u m)}.}
\]
For every finite \(n\), the smallest deterministic-order error occurs exactly at \(m=1\), and equals \(u(n-1)/[n(n-u)]\); the maximum is obtained by one of the two admissible integers bracketing \(n/(1+\sqrt{1-u})\). Across all dimensions and all permutations the sharp supremum is
\[
 \boxed{\sup_{n\ge2,\,\sigma}\|\pi-U\|_{\mathrm{TV}}=\tanh(h/4).}
\]
The supremum is approached by sequences of dimensions and orders; at some step sizes it is also attained by a finite-dimensional order. Independent uniform cyclic rotation of any one fixed ordering before each sweep produces an exactly uniform stationary distribution for every \(h>0\), with exactly the same number of edge evaluations per sweep.

## Assumptions and scope

Use row-vector probability conventions. On vertices \(0,1,\ldots,n-1\) the original continuous-time generator is \(Q=\sum_{i=0}^{n-1}Q_i\), where the only nonzero entries of \(Q_i\) are \((Q_i)_{ii}=-1\) and \((Q_i)_{i,i+1}=1\), with cyclic subscripts. Thus \(Q\) generates the unit-rate, unidirectional continuous-time cycle, whose unique invariant distribution is \(U_i=1/n\).

An ordered Lie–Trotter sweep uses the row-stochastic matrix
\[
 P_\sigma(h)=e^{hQ_{\sigma(1)}}e^{hQ_{\sigma(2)}}\cdots e^{hQ_{\sigma(n)}}.
\]
Each factor transfers the proportion \(u=1-e^{-h}\) of the mass at its source vertex to the next vertex and leaves all other coordinates unchanged. The same fixed ordering is repeated at each sweep for the deterministic assertion; in the randomized assertion, rotations are selected independently from sweep to sweep.

## Proof

**1. Uniqueness and the flux equation.** For \(0<u<1\), the sweep gives every vertex a positive self-transition and a positive transition to its immediate successor: the event that only the selected edge moves has probability at least \(u(1-u)^{n-1}\). Hence the finite chain is irreducible and aperiodic, so its stationary row distribution \(\pi\) is unique.

At stationarity let \(J_i\) be the mass transported by edge \(i\) during one complete sweep. Conservation at vertex \(i\) from sweep start to end gives \(J_{i-1}=J_i\), so all equal a common \(J>0\). Immediately before its outgoing edge \(i\) is processed, vertex \(i\) contains \(\pi_i+Jd_i\): its predecessor has already delivered the common flux if and only if \(r_{i-1}<r_i\). Consequently
\[
 J=u(\pi_i+Jd_i),\qquad \pi_i=J(u^{-1}-d_i).
\]
Summing over vertices yields \(1=J(n/u-m)\), hence \(J=u/(n-u m)\) and the displayed exact stationary law. Conversely the flux identities guarantee stationarity. A strict cyclic permutation of ranks cannot have zero or \(n\) cyclic ascents, proving \(1\le m\le n-1\).

**2. Exact total variation and extreme orders.** Exactly \(m\) vertices have \(\pi_i=(1-u)/(n-u m)<1/n\), and \(n-m\) have \(\pi_i=1/(n-u m)>1/n\). Summing the positive differences gives the displayed total variation. For any \(1\le m\le n-1\), a cyclic rank ordering with exactly \(m\) ascents exists: read cyclically the rank sequence
\[
 1,2,\ldots,m,n,n-1,\ldots,m+1.
\]
The amount of bias depends only on \(m\), not on any other details of the permutation. Its minimum for a fixed \(n\) lies at an endpoint \(m=1\) or \(m=n-1\), and the first is smaller because the numerators agree whereas \(n-u>n-u(n-1)\) for \(n>2\). Both endpoints coincide only when \(n=2\).

**3. Sharp dimension-free envelope.** Set \(t=m/n\). The exact error is
\[
 F_u(t)=\frac{u t(1-t)}{1-u t},\qquad 0<t<1.
\]
Its derivative has the sign of \(1-2t+u t^2\), so it is strictly increasing up to \(t_*=1/(1+\sqrt{1-u})\) and strictly decreasing thereafter. At the maximizer,
\[
 F_u(t_*)=\frac{1-\sqrt{1-u}}{1+\sqrt{1-u}}
 =\frac{1-e^{-h/2}}{1+e^{-h/2}}=\tanh(h/4).
\]
The fixed-dimension maximizer is one of the admissible adjacent integers bracketing \(nt_*\). Every ascent count is realizable and rational proportions \(m/n\) can approach \(t_*\) as \(n\to\infty\), so the universal bound is a sharp supremum. At finite \(n\), \(t_*\) may equal \(m/n\) for specially chosen \(h\), in which case the bound is *attained*; the universal supremum is therefore sharp and may be attained at such step sizes and dimensions.

**4. Exact symmetry restoration.** Let \(R\) cyclically permute vertices and edges. Fix any ordering \(\sigma\) and at each iteration choose a fresh uniformly random rotation \(R^k\sigma\) of it. The averaged transition matrix
\[
 \overline P=\frac1n\sum_{k=0}^{n-1}R^{-k}P_\sigma R^k
\]
commutes with \(R\), hence is circulant. Being row stochastic, a circulant matrix is also column stochastic, so \(U\overline P=U\). Positive nearest-neighbor and self transitions make \(\overline P\) irreducible and aperiodic; its invariant probability is therefore uniquely \(U\). No extra edge factor is applied.

## Verification

The independent-of-floating-point checker `checker.py` explicitly multiplies exact rational edge matrices, solves the claimed stationarity equations by verification, checks the total-variation expression, and verifies uniform invariance for rotationally averaged sweeps. It enumerates all permutations for sizes \(2\le n\le6\), deterministic representative orders for size \(7\), three rational transfer probabilities, all possible cyclic ascent counts in the tested sizes, the exact five-state witness, and more than 21,000 exact rational assertions. A supplementary rational case \(u=3/4\) verifies the sharp envelope and the discrete maximizing rule for sizes through \(79\). Execute `python checker.py`; the included `check_output.txt` gives the actual replay output.

As a transparent witness, for \(n=5\), \(u=1/2\), and order \((0,1,2,3,4)\), the stationary vector is \((1/3,1/6,1/6,1/6,1/6)\), with total-variation error \(2/15\). Reversing the edge order reduces the error to \(4/45\). The universal statements follow from the preceding proof, not from finite enumeration.

## Relationship to prior work

Numerical splitting of Markov generators and its long-time invariant-measure error are well-motivated by Bertazzi, Dobson and Monmarché's work on piecewise-deterministic sampling and by Gourgoulias, Katsoulakis and Rey-Bellet's information-theoretic analysis of splitting errors in kinetic Monte Carlo. The former establishes methods and invariant-bias expansions for continuous-state velocity-jump samplers, while the latter studies entropy-rate and commutator measures of splitting error. Neither inspected treatment states the present directed-cycle, arbitrary-order exact invariant formula, its cyclic-ascent extremal law, or the exact correction by random cyclic rotation. These comparisons do not establish absolute absence from all other literature; the update-schedule and exclusion-process literatures remain relevant possible historical overlap.

## Limitations

The classification applies to **unit-rate unidirectional cycles** with one complete edge-exponential sweep and fixed positive step size; it is not a theorem about arbitrary finite Markov generators, unequal edge rates, continuously varying schedules, or finite-time mixing rates. Independently randomizing rotations makes the *invariant distribution* exact, not necessarily the finite-time transition law or higher-order weak accuracy. All verification is mathematical and computational rather than independent external certification.

## References

1. A. Bertazzi, P. Dobson and P. Monmarché, *Piecewise deterministic sampling with splitting schemes*, arXiv:2301.02537v1 (first public 2023-01-06); Journal of Machine Learning Research 26 (2025), article 243. https://arxiv.org/abs/2301.02537 ; https://www.jmlr.org/papers/volume26/23-0036/23-0036.pdf
2. K. Gourgoulias, M. A. Katsoulakis and L. Rey-Bellet, *Information metrics for long-time errors in splitting schemes for stochastic dynamics and parallel kinetic Monte Carlo*, arXiv:1511.08240 (2015); SIAM Journal on Scientific Computing 38 (2016), A3808–A3832. https://arxiv.org/abs/1511.08240 ; https://doi.org/10.1137/15M1047271
3. *On the number of update digraphs and its relation with the feedback arc sets and tournaments*, Discrete Applied Mathematics (2013), https://doi.org/10.1016/j.dam.2012.12.018 (related update-order equivalence; only accessible abstract was compared).
