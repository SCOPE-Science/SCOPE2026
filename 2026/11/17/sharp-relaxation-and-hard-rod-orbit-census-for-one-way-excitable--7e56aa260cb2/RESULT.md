# Sharp relaxation and hard-rod orbit census for one-way excitable rings

## Finding
For each integer \(q\ge4\) and each labelled directed cycle of length \(n\ge3\), the one-way \(q\)-state Greenberg–Hastings map has a *sharp* maximal first-periodic-entry time
\[
T_q(n)=q+\min(n,q-1)-2.
\]
Its recurrent configurations are exactly the resting word and the coherent clockwise pulse trains with at least \(q\) sites between successive excited sites. Consequently, for every positive integer \(t\), writing \(d=\gcd(n,t)\),
\[
\#\operatorname{Fix}(F_{q,n}^{t})=R_q(d),\qquad
R_q(d)=1+\sum_{k=1}^{\lfloor d/q\rfloor}
\frac{d}{k}\binom{d-(q-1)k-1}{k-1}.
\]
Every primitive nontrivial temporal period is a divisor \(d\mid n\) with \(d\ge q\), and each such divisor occurs. Its number of primitive-period-\(d\) *states* is
\[
P_q(d)=\sum_{e\mid d}\mu(d/e)R_q(e),
\]
so the number of such temporal *orbits* is \(P_q(d)/d\). As \(n\to\infty\), the recurrent-state growth base is the unique root \(\lambda_q>1\) of \(\lambda_q^q-\lambda_q^{q-1}-1=0\).

A constructive initial-condition test identifies all pulse trains that survive. Let \(x\in\{0,\ldots,q-1\}^n\). An initially excited position \(j\), meaning \(x_j=1\), is a *survivor* if for every \(1\le r\le q-1\), with indices interpreted modulo \(n\), neither \(x_{j+r}=1\) nor \(2\le x_{j+r}\le q-r\) holds. Let \(S(x)\) be the survivor positions. Then \(F_{q,n}^{T_q(n)}(x)\) consists precisely of the wave trains issued by the positions in \(S(x)\), with each surviving excitation at \(j+T_q(n)\) and the successive refractory phases \(2,\ldots,q-1\) immediately behind it. In particular, the trajectory eventually extinguishes if and only if \(S(x)\) is empty.

## Assumptions and scope
The directed ring has labelled vertices \(i\in\mathbb Z/n\mathbb Z\); the only input neighbor of \(i\) is \(i-1\). The fully synchronous update is
\[
(F_{q,n}(x))_i=\begin{cases}
1,&x_i=0\ \text{and}\ x_{i-1}=1,\\
0,&x_i=0\ \text{and}\ x_{i-1}\ne1,\\
x_i+1,&1\le x_i\le q-2,\\
0,&x_i=q-1.
\end{cases}
\]
This is a directed, one-input system, not the undirected two-neighbor Greenberg–Hastings automaton. Time \(t=0\) denotes the initial state. The first-periodic-entry time is the smallest \(t\ge0\) such that \(F_{q,n}^t(x)\) belongs to a periodic temporal orbit.

## Proof
**1. Excitation lines cannot split or be created spontaneously.** Write \(E_t=\{i:(F_{q,n}^t(x))_i=1\}\). Every excitation at positive time has a unique predecessor excitation one site to the left at the previous time. Therefore \(E_{t+1}\subseteq E_t+1\). Each original position \(j\in E_0\) gives one possible particle trajectory \(j,j+1,j+2,\ldots\), moving exactly one edge per update until its next target is nonresting, at which time the line terminates. The number of excitation particles never increases.

**2. Exact local obstruction and bounded particle lifetimes.** Consider the initial particle at \(j\). For each integer \(r\ge1\), if this particle is still excited at \(j+r-1\) at time \(r-1\), it attempts to excite \(j+r\). An initial value \(a=x_{j+r}\ge1\) remains nonresting at time \(r-1\) exactly when \(a+r-1\le q-1\). This produces the two obstructions stated in the survivor test: a value one for \(r\le q-1\), or a value at least two with \(a+r\le q\).

There is no additional earlier obstruction that can kill an unblocked particle: any nonzero state at its proposed target is either unrecovered initial material or the refractory wake of a different initial excitation line. If that other line was initially at forward displacement \(s\) from \(j\), a wake can still be nonzero when the particle at \(j\) arrives only if \(1\le s\le q-1\). But then the initial value at \(j+s\) itself blocks the particle at \(j\) by step \(s\). This is an induction on the earliest attempted arrival, and it includes wraparound by reducing initial displacement modulo \(n\). In particular a particle encountering its own origin for the first time at distance \(n<q\) dies there. Thus every original excitation either continues forever or dies at or before step \(m=\min(n,q-1)\). The continuing excitations are exactly \(S(x)\). Distinct continuing excitations are separated by at least \(q\) sites, since an initially excited site within the next \(q-1\) sites is an obstruction.

**3. Sharp entry time.** A particle that dies at step \(r\le m\) was last excited at time \(r-1\). Its last refractory nonzero phase disappears by time \(r+q-2\le m+q-2\). Initial refractory phases disappear no later than time \(q-2\). Thereafter only coherent surviving pulse trains remain, and they move by one cyclic site at every update. Hence every trajectory is periodic by \(T_q(n)=m+q-2\).

The bound is attained. If \(n<q\), take exactly one initially excited site and all other sites resting; it travels \(n-1\) steps, is blocked on returning to its own still-refractory origin, and its last nonzero remnant survives through time \(q+n-3\). If \(n\ge q\), initially excite sites \(0\) and \(q-1\) and rest all other sites. The excitation from \(0\) is blocked at step \(q-1\) by the unrecovered original excitation at \(q-1\); the final remnant at site \(q-2\) is nonzero at time \(2q-4\) and cannot belong to the coherent wave from the other seed (if that seed survives). Thus no earlier uniform bound is possible.

**4. All recurrent states.** In a temporal periodic trajectory the cardinality of \(E_t\) cannot strictly decrease, so \(E_{t+1}=E_t+1\). If an excitation returns to a site in fewer than \(q\) time steps, that site is still refractory and rejects it; hence excited sites in each temporal snapshot must have cyclic gaps at least \(q\). Each refractory phase at a recurrent snapshot is uniquely determined by the corresponding excitation at one of the preceding \(q-2\) times. Conversely, any cyclic set of pulse positions with gaps at least \(q\) defines a coherent wave, which advances by one position forever. The all-rest state is the only fixed point.

**5. Enumerating the hard-rod language.** For \(k\ge1\) selected excited sites, the cyclic clockwise gap lengths \(g_1,\ldots,g_k\) satisfy \(g_i\ge q\) and \(\sum_i g_i=n\). Choosing a distinguished excited site in \(n\) ways, distributing the remaining \(n-qk\) units among \(k\) gaps in \(\binom{n-(q-1)k-1}{k-1}\) ways, and dividing by \(k\) yields the displayed \(R_q(n)\). A state returns after \(t\) iterations precisely when its excited positions are invariant under spatial shift by \(t\), equivalently when its wave has period dividing \(d=\gcd(n,t)\); cyclic gap constraints on the repeated block are exactly the same, giving \(R_q(d)\). Möbius inversion proves \(P_q(d)\) and the orbit counts. A single excitation repeated with spatial period \(d\ge q\) realizes each permitted least period. Finally the hard-rod transfer with states recording the capped distance since the previous pulse has characteristic growth equation \(\lambda^q=\lambda^{q-1}+1\), and its positive primitive transition matrix supplies the stated growth base.

## Verification
The accompanying standalone programs use direct full-state dynamics, independent transfer-matrix counting, and a local survivor reconstruction. Exhaustive dynamics tested 312,593 initial configurations over \(4\le q\le7\) and selected \(3\le n\le7\), matching the sharp transient bound and recurrent counts. A separate transfer computation checked 112 combinations of color and circumference and checked direct temporal fixed-point counts for \(4\le q\le7\), \(3\le n\le5\), and \(1\le t\le2n\). A third verifier checked the survivor reconstruction on 218,084 configurations and independently tested the two sharp witness families. These are finite checks of the all-parameter proof, not replacements for it. Run the included Python scripts with Python 3; no external packages are required.

## Relationship to prior work
The Greenberg–Hastings excitation model originated in work of Greenberg and Hastings, and Fisch and Gravner developed general one-dimensional multi-state symmetric-neighborhood theory. Their 1995 paper uses symmetric neighborhoods and predominantly infinite-lattice probabilistic dynamics; the present directed one-input ring has a different collision geometry and an explicit sharp finite-time clock. Gravner, Lyu and Sivakoff study the three-state model on arbitrary undirected graphs rather than the directed, multi-refractory-state family here. A separate three-state directed-cycle calculation is already available; no priority is claimed for that special case. The contribution here is the all-\(q\ge4\) sharp clock, constructive survivor criterion, and exact multi-state temporal orbit census together.

## Limitations
The result concerns only the specified directed single-input ring with fully synchronous updating and deterministic state progression. It does not apply to undirected rings, more than one input neighbor, stochastic activation, or contact thresholds exceeding one. The asymptotic describes recurrent-state counts, not extinction basin weights. A priority search did not establish absolute novelty, and a full-text historical comparison for the 1978 foundational article was not completed. Numerical checks cover only finite parameter ranges. No independent external validation has been performed.

## References
- Greenberg, J. M., and Hastings, S. P., *Spatial patterns for discrete models of diffusion in excitable media*, SIAM Journal on Applied Mathematics **34** (1978), 515–523. DOI: https://doi.org/10.1137/0134040.
- Fisch, R., Gravner, J., and Griffeath, D., *Threshold-range scaling of excitable cellular automata*, 1993 preprint, https://arxiv.org/abs/patt-sol/9304001 (original submission 1993-04-02 UTC).
- Fisch, R., and Gravner, J., *One-dimensional deterministic Greenberg–Hastings models*, Complex Systems **9** (1995), 329–348. Full text: https://content.wolfram.com/sites/13/2018/02/09-5-1.pdf.
- Gravner, J., Lyu, H., and Sivakoff, D., *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320v1 (2016), https://arxiv.org/html/1610.07320v1.
