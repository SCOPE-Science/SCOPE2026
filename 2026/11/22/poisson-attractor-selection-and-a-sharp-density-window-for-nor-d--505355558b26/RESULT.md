# Separated sparse two-cycles selected by NOR dynamics on Boolean cubes

## Finding

Let \(Q_d\) be the Boolean cube of dimension \(d\geq3\), with edges at Hamming distance one, and put \(N=2^d\). For synchronous open-neighborhood NOR, every set \(S\) of minimum pairwise Hamming distance at least five satisfies \(T^2(S)=S\), and its companion phase has exactly \(N-d|S|\) active vertices. For each fixed \(m\geq0\) and all sufficiently large \(d\), the separated \(m\)-sets index distinct primitive two-cycles, of which there are \(\binom Nm(1+O_m(d^4/N))\).

Initialize with independent Bernoulli\((p_d)\) bits, where \(p_d=1/2+c/d\) for fixed real \(c\) and sufficiently large \(d\). With probability tending to one, the first updated set \(U\) is the sparse phase of such a primitive two-cycle, with all its sites pairwise at least five apart and the other phase having \(N-d|U|\) active sites. The sparse phase has tight size, and the limiting basin mass of cycles with sparse phase of size \(m\) is \(e^{-\lambda_c}\lambda_c^m/m!\), where \(\lambda_c=e^{-2c}\). The Poisson law for the first image and the resulting limiting zero/full basin probability \(e^{-\lambda_c}\) are included as supporting consequences of the neighborhood-coverage comparison, not asserted as distinct originality contributions.

## Assumptions and scope

Identify a state with its active set \(A\). Write \(N(v)\) for the open neighborhood of \(v\), \(N(B)=\bigcup_{v\in B}N(v)\), and \(T(B)=V(Q_d)\setminus N(B)\). There are no self-loops. The sparse phase means the phase of smaller cardinality when the two cardinalities are different. The minimum-distance requirement is vacuous for zero or one site. For finite probability estimates, take \(0<p<1\), put \(r=1-p\), \(q=r^d\), \(D=\binom d2\), \(U=T(A)\), \(W=|U|\), and \(\lambda=Nq\). Total variation is \(d_{\rm TV}(\mu,\nu)=\sup_E|\mu(E)-\nu(E)|\). A basin includes initial states that are already periodic.

## Proof

**NOR polarity.** On an undirected graph, \(T\) is order-reversing and \(B\subseteq T^2(B)\): no neighbor of a vertex in \(B\) can lie in \(T(B)\). Applying antitonicity to this inclusion gives \(T^3(B)\subseteq T(B)\), while applying the inclusion to \(T(B)\) gives the reverse. Thus \(T^3=T\) and every first image is periodic with period one or two.

**Geometry and orbit count.** Let \(S\) be separated as in the Finding. The neighborhoods of its vertices are disjoint. Thus \(|T(S)|=N-d|S|\). For \(v\notin S\), its neighborhood intersects \(N(u)\) for \(u\in S\) only if \(v\) has distance two from \(u\), in which case the intersection has size two. It cannot be distance two from two members of \(S\), by the triangle inequality. Since \(d\geq3\), at least one neighbor of \(v\) is not covered by \(N(S)\), i.e. belongs to \(T(S)\); consequently \(v\notin T^2(S)\). Together with the polarity inclusion this gives \(T^2(S)=S\). If \(N-dm>m\), then an \(m\)-set of this type is the unique smaller phase, so its two-cycle is primitive and determines \(S\). In particular each singleton yields a different two-cycle for \(d\geq3\). For fixed \(m\), the probability that a uniformly chosen \(m\)-set contains a pair at distance at most four is at most \(\binom m2(\sum_{j=1}^4\binom dj)/(N-1)=O_m(d^4/N)\), with out-of-range binomial coefficients zero. This proves the orbit count.

**First-image moments and Poisson estimates.** The indicator \(I_v=\mathbf1_{\{v\in U\}}\) has mean \(q\). Distinct open neighborhoods intersect in exactly two vertices for centers at distance two and are otherwise disjoint. Thus the joint inclusion probability is \(r^{2d-2}\) for distance two and \(r^{2d}\) otherwise. Counting the \(ND\) ordered center pairs at distance two gives
\[
\mathbb E W=Nr^d,\qquad
\operatorname{Var} W=Nr^d(1-r^d)+ND(r^{2d-2}-r^{2d}).
\]
At \(p=1/2\) the variance is \(1+(3D-1)/N\). The initial bits determining \(I_v\) are disjoint from all bits determining indicators with centers outside \(B(v)=\{v\}\cup\{u:\operatorname{dist}(u,v)=2\}\). In the notation of Arratia–Goldstein–Gordon [1], \(b_1=N(1+D)r^{2d}\), \(b_2=NDr^{2d-2}\), and \(b_3=0\). Their count bound yields \(d_{\rm TV}(\mathcal L(W),\operatorname{Poisson}(\lambda))\le 2(b_1+b_2)\). A conservative form of their process bound (Theorem 3) gives distance at most \(4(b_1+b_2)+2Nq^2\) from the field of independent Bernoulli\((q)\) indicators.

**Selection of separated cycles.** By the joint inclusion probabilities and a union bound, the probability of a pair in \(U\) at distance at most four is at most
\[
\frac N2\left[D r^{2d-2}+\left(\sum_{j=1}^4\binom dj-D\right)r^{2d}\right].
\]
In the critical window, \(\lambda=(1-2c/d)^d\to\lambda_c\); the count and field error bounds are \(O_c(d^2/N)\), and the separation error is \(O_c(d^4/N)\). Hence \(W\) converges in total variation to \(\operatorname{Poisson}(\lambda_c)\). In addition, \(\Pr((d+1)W\geq N)\leq(d+1)\lambda/N\) by Markov's inequality. Outside these two exceptional events, \(U\) is separated and is strictly the smaller phase, the other phase having \(N-dW\) active sites. This identifies the limiting basin mass for every fixed sparse-phase size and the limiting concentration on these two-cycles. The initial state has size \(N/2+o_{\Pr}(N)\), by independence, whereas the two periodic phase sizes are \(O_{\Pr}(1)\) and \(N-O_{\Pr}(d)\). Therefore the probability of already being periodic initially tends to zero.

**Universal orbit.** The zero/full cycle is reached if and only if \(U=\varnothing\) or \(U=V(Q_d)\). Here \(U=V(Q_d)\) holds if and only if \(A=\varnothing\), because each vertex has neighbors. Thus the exact basin probability is \(\Pr(W=0)+r^N\), tending to \(e^{-\lambda_c}\) in the window. For fixed \(p>1/2\) it tends to one since \(\lambda\to0\). For fixed \(0<p<1/2\), \(\lambda\to\infty\) and the variance formula gives \(\operatorname{Var}(W)/\lambda^2\leq1/\lambda+3D/N\to0\); Chebyshev and \(r^N\to0\) yield a limit of zero.

## Relationship to prior work

Aledo, Martínez, and Valverde [2] establish a fixed/period-two restriction for undirected NOR. Arratia, Goldstein, and Gordon [1] give the general local-dependence bounds used above. The open-neighbor OR study [3] obtains a Poisson limit for the number of time-one zeros and the Gumbel limit for one-step consensus in this same window. The time-one zero set for OR is exactly \(T(A)\) for NOR. In particular the limiting universal-orbit probability is already implied by that coverage limit and the elementary basin identity; the change of dynamical interpretation does not make it a separate asymptotic discovery. The distinct content pursued here is the separation of the random sparse phase, its exact dense companion size, and the corresponding family and census of primitive NOR two-cycles. No priority order is asserted between the two same-date records.

## Reproduction and limitations

The accompanying `verify_nor_cube.py` is a standard-library verifier for all initial states in dimensions one through four. It separately compares direct trajectories and a neighborhood-union polynomial and checks the first-image moments, basin identity and small-dimensional singleton cycles. These finite tests are not a proof of the asymptotic selection theorem or a complete deterministic attractor classification. The formula for separated orbits does not claim to count other two-cycles. The fixed-density limits are for interior Bernoulli parameters, not the deterministic all-zero endpoint.

## References

1. R. Arratia, L. Goldstein and L. Gordon, *Poisson Approximation and the Chen–Stein Method*, Statistical Science 5 (1990), 403–434, Theorems 1 and 3. https://doi.org/10.1214/ss/1177012015
2. J. A. Aledo, S. Martínez and J. C. Valverde, *Graph Dynamical Systems with General Boolean States*, Applied Mathematics & Information Sciences 9 (2015), 1803–1808, Corollary 3.3. https://doi.org/10.12785/amis/090417
3. *A Gumbel consensus window and exact terminal shells for Boolean-cube OR dynamics*, Resultary record `ce6906b9edb4`, 2026-11-22. https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-a-gumbel-consensus-window-and-exact-terminal-shells-for-boolean--ce6906b9edb4
