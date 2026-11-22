# An order-invariant optimal timetable for independently cancelled transit services

## Finding

Consider an idealized periodic commuter service with \(n\ge 4\) labeled departures per period \(T>0\). Their cyclic order is fixed, and scheduled service \(i\) operates independently with probability \(p_i\in(0,1]\), with at least one \(p_i=1\). Every successfully operating service can take every waiting passenger immediately. Passenger arrival times are uniformly distributed over a period, independently of service availability. The objective is the unconditional expected waiting time \(W\) to the next operating departure.

**Theorem.** Put \(v_i=p_i/(2-p_i)\) and \(S=\sum_{i=1}^n v_i\), with cyclic indexing \(v_{n+1}=v_1\). Among all schedules preserving the given cyclic order, the unique optimal interdeparture intervals are

\[
\Delta_i^*=\frac{T(v_i+v_{i+1})}{2S},\qquad i=1,\ldots,n.
\]

The exact minimal passenger waiting time is

\[
W_*=\frac{T}{2S}=\frac{T}{2\sum_{i=1}^n p_i/(2-p_i)}.
\]

Consequently, **the minimum is invariant under every permutation of the service reliabilities**, although the unique optimal headway vector depends on their cyclic order. In addition, for every feasible schedule with normalized gaps \(g_i=\Delta_i/T\), there is the exact regret identity

\[
W(g)-W_* = \frac{T}{2}\,\mathbb E\!\left[\sum_{J\in\mathcal A}\left(\sum_{i\in J}(g_i-g_i^*)\right)^2\right]
\ge \frac{T}{2}\left(\prod_{i=1}^n p_i\right)\sum_{i=1}^n(g_i-g_i^*)^2.
\]

Here \(\mathcal A\) is the cyclic partition of elementary gaps into the consecutive intervals between operating departures. The inequality quantifies the penalty of deviating from the optimum.

As an exact example, take ordered reliabilities \((1,1,1/2,1/5)\). Then \(S=22/9\), the optimal normalized gaps are \((9/22,3/11,1/11,5/22)\), and \(W_*/T=9/44\). Equal spacing produces \(W/T=37/160\), a reduction of \(47/407\) (approximately \(11.548\%\)) when optimized. Rearranging these same four reliabilities changes the optimum gaps and generally changes the equal-spacing cost, but not \(9/44\).

## Assumptions and scope

Each scheduled departure time occurs once per period; its Bernoulli availability is independent of all other scheduled departures, and the same reliability applies in repeated periods. Availability is independent of passenger arrivals; there is at least one certain service per period, preventing periods with no departure. The model allows no crowding, capacity constraint, boarding duration, passenger anticipation, fare choice, arrival timing response, delayed actual departure, or correlated cancellations. The objective is mean residual waiting from a time sampled uniformly over the period, not conditional waiting given a particular passenger's preferred trip. All headways may vary over positive real numbers subject to summing to \(T\), and the cyclic order is specified in advance. Allowing all possible orders leaves the minimum unchanged.

## Proof

Normalize \(T=1\) and write \(g_i>0\) for the interval from departure \(i\) to departure \(i+1\), so \(\sum_i g_i=1\). For each realization \(\omega\) of the independent operation indicators, let \(\mathcal A(\omega)\) partition the \(n\) elementary intervals into disjoint consecutive blocks, each block \(J\) lying between two successive operating services. There is at least one operating service in each realization by hypothesis. Uniform arrival and direct integration of the forward waiting time over every such block give

\[
W(g)=\frac12\,\mathbb E\sum_{J\in\mathcal A}\left(\sum_{j\in J}g_j\right)^2.
\tag{1}
\]

Equivalently, \(W(g)=g^{\mathsf T}Hg/2\), where

\[
H_{ij}=\Pr\{\text{elementary gaps }i\text{ and }j\text{ occupy the same active block}\}.
\]

For each fixed operating-service realization, differentiating (1) with respect to \(g_i\) yields the length of the unique active block containing gap \(i\). Thus \((Hg)_i\) is the expected total length of that active block. Also, the all-services-operating event has probability \(\prod_i p_i>0\) and contributes \(\sum_i g_i^2/2\). Therefore \(H\) is positive definite: for every real vector \(z\),

\[
z^{\mathsf T}Hz\ge\left(\prod_i p_i\right)\sum_i z_i^2.
\tag{2}
\]

Set \(q_i=1-p_i\), \(v_i=p_i/(2-p_i)\), and \(S=\sum_i v_i\). Then

\[
q_i=\frac{1-v_i}{1+v_i},\qquad g_i^*=\frac{v_i+v_{i+1}}{2S}.
\]

For each \(i\), let \(A_i\) be the expected forward time from scheduled departure \(i\) to the next *operating* departure strictly following it; let \(B_i\) be the analogous expected backward time to the last operating departure strictly preceding it. At least one certain service makes these distances well-defined without an infinite search. First-step conditioning on the neighboring departure gives the exact recurrences

\[
A_i=g_i+q_{i+1}A_{i+1},\qquad
B_i=g_{i-1}+q_{i-1}B_{i-1}.
\tag{3}
\]

The systems (3) have unique finite cyclic solutions because the product \(\prod_i q_i=0\). Substituting \(g_i=g_i^*\) into either recurrence and using \(q_j(1+v_j)=1-v_j\) shows that

\[
A_i=B_i=\frac{1+v_i}{2S}.
\tag{4}
\]

The length of the active block containing elementary gap \(i\) equals \(g_i\) plus the backward extension beyond departure \(i\), if \(i\) is cancelled, plus the forward extension beyond departure \(i+1\), if \(i+1\) is cancelled. A possibly cancelled endpoint's indicator is independent of the first active departure in the strictly opposite direction: the certain service is elsewhere. If an endpoint is certain, its extension term is zero. Hence

\[
(Hg)_i=g_i+q_i B_i+q_{i+1}A_{i+1}.
\tag{5}
\]

Using (4) and the proposed gaps in (5) yields

\[
(Hg^*)_i=\frac{v_i+v_{i+1}+1-v_i+1-v_{i+1}}{2S}=\frac1S
\]

for every \(i\). Thus \(g^*\) satisfies the Lagrange stationarity conditions under \(\sum_i g_i=1\). It lies strictly inside the simplex because every \(v_i>0\). Positive definiteness (2) proves its unique global optimality, including against boundary schedules. Moreover

\[
W(g^*)=\frac12\sum_i g_i^*(Hg^*)_i=\frac1{2S}.
\]

For arbitrary \(g\) put \(z=g-g^*\), so \(\sum_i z_i=0\). Expanding the quadratic in (1) gives \(W(g)-W(g^*)=z^{\mathsf T}Hz/2\), because \(Hg^*=\mathbf1/S\). Re-expressing this quadratic by (1) and using (2) proves the regret identity and sharp quadratic lower certificate stated above. Multiplication by \(T\) restores physical time units. Since \(S\) is a symmetric sum in the reliabilities, the optimal value is independent of their ordering.

## Verification

The independent standard-library checker `check_reliability.py` enumerates every availability pattern for exact rational reliability vectors and constructs the full active-block quadratic form. It checks its symmetry and diagonal, exact stationarity \(Hg^*=\mathbf1/S\), exact objective value \(1/(2S)\), the quadratic regret identity under perturbation, and the order-invariant optimum across every distinct permutation of \((1,1,1/2,1/5)\). Running `python check_reliability.py` returned `ALL EXACT CHECKS PASSED` for 21 exact-rational configurations (including 12 distinct permutations). The infinite generality rests on the analytic proof above, not on that finite test collection.

## Relationship to prior work

Salzborn (1972) optimizes bus dispatch frequency with passenger-arrival and fleet constraints, and Barnett (1974) studies service control under stochastic headway disturbances. Ceder (2001) contrasts even passenger loads with even headways. Fonzone, Schmöcker and Liu (2015) give a detailed model of passenger arrival choices and unreliable departure times, including integral formulas for expected waiting and dynamical bus bunching; the accessible accepted manuscript was read in its introduction, methods, waiting-time formulas and conclusions. Their results do not supply the present all-size closed-form independent-**cancellation** schedule, its order-invariant optimal value, or its exact quadratic regret. In particular a general expectation integral is not itself a global optimality classification. Some historical scheduling texts were accessible only as abstracts or bibliographic records, leaving possible priority overlap unresolved. The formula also extends algebraically to two and three services, but the main all-size classification is stated for at least four independently available departures.

## Limitations

This is an exact stylized result, not an estimated transit operating policy. Actual systems may have unknown cancellations, demand varying within periods, passenger schedule awareness, capacities, crowding, correlated cancellations, irregular service travel times, or operating costs. The formula relies on the existence of at least one certain service, positive individual reliability, independent operation, and uniform arrival. Without those assumptions neither the optimum nor the quadratic representation is claimed to persist. The cited literature comparison is not an exhaustive priority certificate; independent scientific validation is absent.

## References

1. Salzborn, F. J. M. (1972). *Optimum Bus Scheduling*. Transportation Science 6(2), 137–148. https://doi.org/10.1287/trsc.6.2.137.
2. Barnett, A. (1974). *On Controlling Randomness in Transit Operations*. Transportation Science 8(2), 102–116. https://doi.org/10.1287/trsc.8.2.102.
3. Ceder, A. (2001). *Bus Timetables with Even Passenger Loads as Opposed to Even Headways*. Transportation Research Record 1760, 3–9. https://doi.org/10.3141/1760-01.
4. Fonzone, A., Schmöcker, J.-D., and Liu, R. (2015). *A model of bus bunching under reliability-based passenger arrival patterns*. Transportation Research Part C 59, 164–182. https://doi.org/10.1016/j.trc.2015.05.020 (first publicly online June 16, 2015; accessible accepted manuscript deposited June 19, 2015). Open accepted manuscript: https://eprints.whiterose.ac.uk/id/eprint/85338/1/Fonzone%20et%20al%20-%20ISTTT61-WRR.pdf.
5. Parmigiani, G. (1996). *Optimal Scheduling of Fallible Inspections*. Operations Research 44(2), 360–367. https://doi.org/10.1287/opre.44.2.360 (related, but a different detection-cost objective).
