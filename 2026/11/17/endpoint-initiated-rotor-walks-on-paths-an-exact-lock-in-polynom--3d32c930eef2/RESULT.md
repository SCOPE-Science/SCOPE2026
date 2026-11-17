# Endpoint-initiated rotor walks on paths: an exact lock-in polynomial and a Gaussian clock

## Finding
Fix an integer \(n\ge3\). On the labelled path with vertices \(0,1,\ldots,n-1\), put one walker initially at vertex \(0\). Every internal vertex \(i\in\{1,\ldots,n-2\}\) holds a rotor directed either left or right. At each visit the rotor first turns to the other neighbor, then the walker moves in the newly selected direction; the endpoint rotors always point to their unique neighbor. The state records both the walker position and **all** rotors. Define \(\tau\) to be the first time this complete state belongs to a periodic orbit.

Write \(m=n-2\) and let \(S\subseteq\{1,\ldots,m\}\) be the set of initially right-directed internal rotors. If \(S=\varnothing\), then \(\tau=0\). Otherwise
\[
\boxed{\tau(S)=2\sum_{i\in S}i-\max S.}
\]
The full unnormalized distribution polynomial over all \(2^m\) rotor initializations is
\[
\boxed{P_m(q)=\sum_{S\subseteq\{1,\ldots,m\}}q^{\tau(S)}
=1+\sum_{k=1}^{m}q^k\prod_{i=1}^{k-1}(1+q^{2i}).}
\]
Thus the sharp longest initial nonperiodic duration is \(m^2\), achieved by exactly one endpoint-started rotor configuration, in which **all internal rotors initially point right**. Among initial configurations having precisely \(r\) right rotors, \(1\le r\le m\), the sharp minimum and maximum entrance times are respectively
\[
\boxed{r^2\ \le\ \tau\ \le\ (2r-1)m-r(r-1),}
\]
with each extreme attained by exactly one rotor subset of size \(r\).

Under independent, equiprobable initial rotor directions,
\[
\boxed{\mathbb E\tau=\frac{m^2-m+2}{2}-2^{-m},\qquad
\frac{\tau-\mathbb E\tau}{m^{3/2}}\ \xrightarrow{\ d\ }\ \mathcal N\!\left(0,\frac13\right).}
\]
The total recurrent component for the path has exactly \(2(n-1)\) states and is one periodic orbit; this is used to identify first entry, not merely the first time a local orientation condition happens to hold.

## Assumptions and scope
All graph vertices and rotor directions are labelled. The path has exactly one edge between consecutive vertices, and both endpoints have degree one. A **time step** toggles the current internal rotor before traversing the chosen outgoing edge; endpoints do not toggle. The initial walker is specifically at vertex \(0\), not chosen uniformly over the path. The sample space for the distribution is all \(2^{n-2}\) independent internal rotor choices. The result does not assert a formula for an arbitrary interior starting position or for a multiwalker process.

## Proof
**1. Recurrent-state criterion.** The complete state on a path is periodic if and only if every internal rotor strictly to the left of the walker points right and every internal rotor strictly to its right points left. There is no constraint on a rotor at the current walker site. For sufficiency, starting from such a state, successive flip-then-move operations follow the unique depth-first directed Euler tour: each path edge is traversed once in each direction, and after \(2(n-1)\) steps every rotor and the walker position return. To see necessity, consider any periodic state, with the walker at \(p\). In a periodic orbit the walker must visit every vertex: otherwise choose a boundary vertex of its visited interval, which is visited infinitely often yet must eventually send the walker outside that interval by alternating its rotor. For any internal vertex \(i<p\), its last departure before the present time must have been to the right (the unique route to \(p\)); after this departure its rotor points right. Similarly any internal vertex \(i>p\) last departed to the left and its rotor points left. This proves the criterion. The allowed states form a single cycle, since the directed Euler tour has length \(2(n-1)\), equal to their total count.

**2. Excursion decomposition.** Sort the initially right-pointing rotor positions as \(i_1<\cdots<i_r\). If \(r=0\), the initial state already meets the recurrent-state criterion. If \(r>0\), the walker moves from \(0\) rightward along consecutive internal rotors initially pointing left, toggling them right, until reaching \(i_1\). Because the initial rotor at \(i_1\) points right, the next step flips it left and sends the walker back along the exact same interval to \(0\), toggling each intermediate rotor left on its return. This first round trip takes exactly \(2i_1\) steps and restores all rotors at indices at most \(i_1\) to left. The identical argument applies to the next marked position \(i_2\), and so on. Each nonfinal marked position \(i_j\) produces a complete excursion of length \(2i_j\). After the excursions through \(i_1,\ldots,i_{r-1}\), the walker first arrives at \(i_r\) after an additional \(i_r\) steps. At that instant all internal rotors left of \(i_r\) point right and all internal rotors right of \(i_r\) point left, so the recurrent-state criterion holds. Prior to that instant a still-unvisited, right-directed rotor to the right of the walker violates the criterion. Hence this instant is the **first** recurrent one and the claimed clock follows.

**3. Polynomial and extrema.** For a nonempty set \(S\), condition on its largest member \(k\). Every smaller index \(i<k\) is either absent or present, contributing respectively time \(0\) or time \(2i\), while \(k\) itself contributes time \(k\). This yields the stated polynomial. If \(S=\{i_1<\cdots<i_r\}\), the time is \(2(i_1+\cdots+i_{r-1})+i_r\). This expression is strictly increasing in every selected index; for fixed \(r\), the unique lower and upper selections are \(\{1,\ldots,r\}\) and \(\{m-r+1,\ldots,m\}\). Their values are \(r^2\) and \((2r-1)m-r(r-1)\). Optimizing over \(r\) yields uniquely \(\tau=m^2\) at \(S=\{1,\ldots,m\}\).

**4. Mean and Gaussian limit.** Let \(B_i\) be independent Bernoulli random variables with parameter \(1/2\), and let \(M=\max\{i:B_i=1\}\), with \(M=0\) if none occurs. By the clock formula,
\[
\tau=2\sum_{i=1}^m iB_i-M,
\qquad \Pr(M=k)=2^{-(m-k+1)}\quad(1\le k\le m),
\]
with \(\Pr(M=0)=2^{-m}\). The finite geometric sum gives \(\mathbb EM=m-1+2^{-m}\), proving the exact mean. Centered weighted Bernoulli sums have variance \(\sum_{i=1}^m i^2=m(m+1)(2m+1)/6\sim m^3/3\); the maximum summand divided by this standard deviation tends to zero. The Lindeberg central limit theorem therefore gives a centered Gaussian with variance coefficient \(1/3\). Since \(0\le M\le m\), the centered correction \((M-\mathbb EM)/m^{3/2}\) vanishes uniformly. Slutsky's theorem proves the stated limit.

## Verification
Three independent integer-only Python programs are provided: `endpoint_exhaustive.py` simulates every endpoint-initialized rotor state for \(3\le n\le18\); `full_graph_recurrence.py` independently strips the full functional graph to identify periodic states for \(3\le n\le14\), without assuming the recurrent-state criterion; and `polynomial_check.py` verifies the generating polynomial and exact mean against all rotor subsets for \(1\le m\le17\). The actual recorded outputs are `endpoint_output.txt`, `graph_output.txt`, `polynomial_output.txt`. They are finite verification checks; the all-length statements follow from the preceding proof, not from the finite computations.

## Relationship to prior work
The earliest checked historical rotor-router account is Yanovski, Wagner and Bruckstein (2003), establishing Euler-tour eventuality and general lock-in bounds. Menc, Pająk and Uznański (2015), Theorem 2.2 and its discussion, establish the exact worst-case **cover time** \((n-1)^2\) for path exploration. The cover clock is a different observable from the **first recurrent-state entrance clock** studied here; in the all-right initialization, the former first visits the far endpoint at time \((n-1)^2\), whereas the latter enters its period at \((n-2)^2\). Chalopin et al. (2014), Section 5.1, give a general efficient phase-decomposition method for single-token rotor walks, but do not present the endpoint-started first-entrance distribution, its entire polynomial, sharp rotor-count extremizers, or the fluctuation law. Thus the general method gives algorithmic computability without containing the stated exact enumerative law. The cyclic rotor-router model is not the path model, because a cycle has no degree-one endpoints and a different recurrent-state structure.

## Limitations
The original 2003 paper was accessible in abstract form only, and an earlier 1996 conference account was known bibliographically but not examined in full. An alternate derivation in unindexed sources remains possible, so historical priority is provisional. The strongest claim is a mathematical exact law under the stated endpoint initialization, not a classification for arbitrary starts. The Gaussian conclusion concerns randomness of the **initial rotor directions**, not stochastic walker moves.

## References
- V. Yanovski, I. A. Wagner and A. M. Bruckstein, *A Distributed Ant Algorithm for Efficiently Patrolling a Network*, Algorithmica 37 (2003), 165–186. DOI: https://doi.org/10.1007/s00453-003-1030-9 ; public date documented at https://d3ccyth396mz21.cloudfront.net/publications/a-distributed-ant-algorithm-for-efficiently-patrolling-a-network .
- A. Menc, D. Pająk and P. Uznański, *Time and Space Optimality of Rotor-Router Graph Exploration*, arXiv:1502.05545, first posted 2015-02-19, https://arxiv.org/abs/1502.05545 ; inspected preprint https://arxiv.org/pdf/1502.05545 .
- J. Chalopin, S. Das, P. Gawrychowski, A. Kosowski, A. Labourel and P. Uznański, *Lock-in Problem for Parallel Rotor-router Walks*, arXiv:1407.3200, first posted 2014-07-12, https://arxiv.org/abs/1407.3200 ; inspected Section 5.1 in https://arxiv.org/pdf/1407.3200 .
