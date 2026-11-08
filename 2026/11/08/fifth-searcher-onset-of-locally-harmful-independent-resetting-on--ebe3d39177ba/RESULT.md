# Fifth-searcher onset of locally harmful independent resetting on a five-vertex path

## Finding

Let \(P_5\) be the unweighted path with vertices \(0,1,2,3,4\) in order. Let \(N\) independent continuous-time simple random walks (total jump rate one per walker) start at vertex \(2\). The search ends at the first visit by **any** walker to target vertex \(0\). Each walker is additionally and **independently** reset to vertex \(2\) by its own Poisson clock of rate \(r\ge0\). Write \(M_N(r)\) for the expected completion time.

**Theorem (first independent-reset sign reversal).** For integers \(N\in\{1,2,3,4,5\}\), the right derivative exists at zero and satisfies
\[
M_N'(0+)<0\quad(N=1,2,3,4),\qquad M_5'(0+)>0.
\]
Therefore five is the **first number of searchers** for which sufficiently rare *independent* resetting locally worsens mean first detection on this path. At each smaller positive \(N\), sufficiently rare independent resetting locally improves it. The signs at the two closest population sizes are exactly
\[
M_4'(0+)=-\frac{98437587236766524607457}{4857833711937191749095424},
\qquad
M_5'(0+)=\frac{117715636350470400400957554016380716796973103498302122}{602188558121296962986525429886983883962244425767981445}.
\]
The word *first* is restricted to searching the positive integers in increasing order through \(N=5\): no assertion of a monotone sign for \(N\ge6\) is made. A positive derivative at zero does not exclude a global improvement at a larger reset rate.

## Assumptions and scope

All edge choices are uniformly random among the present vertex's neighbors; holding times before ordinary moves are independent exponential variables of mean one. A reset is instantaneous and does not itself count as detecting the target. Resetting a walker already at vertex \(2\) is a no-op. The independent reset clocks are independent of each other and of the ordinary walk clocks. The target is absorbing for the first-hit search. The theorem concerns the common initial state with every walker at \(2\), one target at \(0\), and only \(N=1,2,3,4,5\). It is not about synchronous/common-clock resets, cover times or discrete-time random walks.

## Proof

Write the four *transient* vertex types in the order \((2,1,3,4)\), and let \(c=(c_2,c_1,c_3,c_4)\in\mathbb N_0^4\) have \(\sum_i c_i=N\). Until any walker hits \(0\), the population count \(c\) is Markov because walkers are exchangeable and clocks are independent. The transient state space has exactly \(\binom{N+3}{3}\) states. The ordinary single-walker transient transitions are
\[
2\to1,3\text{ at rates }\tfrac12,\quad
1\to2\text{ at rate }\tfrac12,\quad
3\to2,4\text{ at rates }\tfrac12,\quad
4\to3\text{ at rate }1.
\]
The remaining transition \(1\to0\), at rate \(1/2\) per walker at \(1\), kills the entire search. For a function \(f\) on count states, define the killed generator \(Q_0\) by the displayed ordinary jumps and the killing rate \(c_1/2\). Equivalently, if \(p_{ij}\) are exactly the transient rates above,
\[
(Q_0f)(c)=\sum_{i\ne j}c_i p_{ij}f(c-e_i+e_j)-Nf(c).
\]
Here \(e_i\) is the unit count vector of transient vertex type \(i\). Define the independent-reset generator
\[
(Bf)(c)=\sum_{i\ne2}c_i\bigl(f(c-e_i+e_2)-f(c)\bigr).
\]
Then \(Q_r=Q_0+rB\). Let \(A=-Q_0\), \(\mathbf1\) be the all-ones column vector, and \(c_\star=(N,0,0,0)\). Every nonabsorbed state can reach the target with positive probability in finite time, so the finite killed chain is transient, \(A\) is invertible, and the mean hitting-time vector is
\[
u_r=(A-rB)^{-1}\mathbf1.
\]
It follows by differentiating this finite matrix inverse that
\[
M_N(0)=u(c_\star),\qquad
M_N'(0+)=v(c_\star),\qquad
Au=\mathbf1,\quad Av=Bu.
\]
These two finite rational linear systems constitute an exact finite certificate. Their dimensions for \(N=1,2,3,4,5\) are \(4,10,20,35,56\), respectively.

Exact Gaussian elimination, using rational arithmetic without numerical approximation, gives:

| \(N\) | \(M_N(0)\) | \(M_N'(0+)\) |
|---:|---:|---:|
| 1 | \(12\) | \(-10\) |
| 2 | \(1555/272\) | \(-44679/18496\) |
| 3 | \(629176456/168587283\) | \(-5826055874237962/9473890663107363\) |
| 4 | \(98335794451053/35264790234112\) | \(-98437587236766524607457/4857833711937191749095424\) |
| 5 | \(779533184020835725901911436/347041368750556008691694017\) | \(117715636350470400400957554016380716796973103498302122/602188558121296962986525429886983883962244425767981445\) |

Every denominator is positive; the numerators have exactly the asserted signs. The complete algorithm and exact residual tests are included in `verify.py`. Invertibility of \(A\) ensures the displayed rational solutions are unique. Since \(M_N(r)\) is analytic near zero, each nonzero derivative implies a strict improvement or worsening for all sufficiently small positive \(r\), as claimed. \(\square\)

## Verification

Run `python verify.py` with Python 3; only the standard library is required. The checker independently constructs the count generator, solves \(Au=\mathbf1\) and \(Av=Bu\) exactly using rational Gaussian elimination, checks the residual of **every equation** for all five values of \(N\), and compares the results to the five rational fractions given above. A second, *uncompressed labeled-walker* construction checks both quantities independently for \(N=1,2,3\). No floating-point numerics, random sampling, external files or downloaded data are required for the certificate. Exact arithmetic certifies the finite theorem, rather than extrapolating a pattern from a sample.

## Relationship to prior work

Biroli, Majumdar and Schehr (2023) study search-team resetting under independent and common-clock protocols for Brownian motion on an unbounded line. Their Brownian critical searcher numbers are not the present exact discrete-network values. Bonomo and Pal (2021) study discrete-time restart for confined one-dimensional lattice walks, primarily with a single searcher. Michelitsch and coauthors (2024) develop a network resetting framework in discrete time, also focusing on single-walker first-passage observables. Their general renewal and generator ideas are useful background, but the inspected results do not state this continuous-time five-vertex exact independent-clock sign classification. A common-clock calculation on the same path does not imply the independent-clock calculation: the latter has generator \(B\) with separate reset terms for each occupied position rather than one joint reset term. No general originality or priority theorem follows from unsuccessful searches.

## Limitations

The theorem concerns only local behavior as \(r\downarrow0\), not global minimization over all reset rates; the sign for \(N\ge6\) is not determined here. It is specific to the path, target, start, independent Poisson reset clocks and fixed unit-rate continuous-time walk. Existing generic restart identities provide the conceptual framework; the contribution is this specific exact population cutoff under independent resetting. Independent mathematical review and historical-priority verification remain outstanding.

## References

1. M. Biroli, S. N. Majumdar and G. Schehr, *Critical number of walkers for diffusive search processes with resetting*, arXiv:2303.18012, first public 2023-03-31. https://arxiv.org/abs/2303.18012
2. O. Lauber Bonomo and A. Pal, *First passage under restart for discrete space and time: application to one dimensional confined lattice random walks*, arXiv:2102.00895, first public 2021-02-01. https://arxiv.org/abs/2102.00895
3. T. M. Michelitsch, G. D'Onofrio, F. Polito and A. P. Riascos, *Random walks with stochastic resetting in complex networks: a discrete time approach*, arXiv:2409.08394, first public 2024-09-12. https://arxiv.org/abs/2409.08394
