# Exact majority clocks on wheel graphs and the hub-flip run polynomial

## Finding
For every integer \(n\ge4\), synchronous open-neighbor binary majority with tie retention on the wheel \(W_n=K_1\vee C_n\) has exactly two fixed configurations and no primitive periods other than two. Its exact number of primitive period-two temporal orbits is
\[
C_2(n)=A_n+2\mathbf1_{2\mid n},
\qquad
A_n=\sum_{\substack{2k>n\\2e<n}}[u^k v^e]P_n(u,v),
\]
where
\[
P_n(u,v)=\begin{cases}R_n(u,v),&n\text{ odd},\\R_{n/2}(u,v)^2,&n\text{ even},\end{cases}
\]
and, for each integer \(m\ge2\),
\[
R_m(u,v)=1+u^m v^m+
\sum_{k=2}^{m-1}\ \sum_{r=1}^{\min(\lfloor k/2\rfloor,m-k)}
\frac mr\binom{k-r-1}{r-1}\binom{m-k-1}{r-1}
 u^k v^{k-r}.
\]
In particular, the exact number of initially periodic labelled configurations is \(2+2C_2(n)\), and the exact numbers of primitive temporal cycles are \(C_1(n)=2\), \(C_2(n)\), and zero at all other periods. The term \(A_n\) counts hub-flipping two-cycles; when \(n\) is even there are exactly two additional hub-preserving two-cycles, and when \(n\) is odd there are none.

## Assumptions and scope
Let rim vertices be \(i\in\mathbb Z/n\mathbb Z\), with binary opinions \(x_i\), and let \(h\in\{0,1\}\) be the hub opinion. Every vertex simultaneously adopts the strict majority of its *open* neighbors; when these votes tie, it retains its prior opinion. Thus, the rim update is
\[
(T_h(x))_i=\begin{cases}x_{i-1}x_{i+1},&h=0,\\x_{i-1}\vee x_{i+1},&h=1,\end{cases}
\]
while the hub updates to one when \(2|x|>n\), to zero when \(2|x|<n\), and retains \(h\) at equality. Products and disjunctions here are Boolean, not operations in an arbitrary field. Graphs are labelled; temporal cycles are quotiented only by time translation, not graph automorphisms.

For integers \(k,e\), the coefficient \([u^k v^e]P_n\) counts rim strings having \(k\) ones and \(e\) directed occupied edges in the step-two graph whose edges connect \(i\) to \(i+2\), subject to no isolated one in that graph. An all-one component of length two has two directed occupied edges; this agrees with \(e=\sum_i x_i x_{i+2}\).

## Proof
**1. No primitive periods longer than two.** Replace binary opinions by spins \(y_i\in\{-1,+1\}\). Write \(A\) for the symmetric adjacency matrix of the wheel and set \(M=A+\varepsilon I\) for any fixed \(0<\varepsilon<1\). Since each open-neighbor sum is an integer, updating by \(y_i(t+1)=\operatorname{sign}((My(t))_i)\) exactly encodes strict majority with tie retention; no local field vanishes. Define the two-time energy
\[
E_t=-y(t+1)^\mathsf T M y(t).
\]
By symmetry,
\[
E_t-E_{t-1}=-\sum_i(y_i(t+1)-y_i(t-1))(My(t))_i\le0.
\]
A differing pair of spins contributes a strictly negative amount because \(y_i(t+1)\) has the sign of the nonzero local field. There are finitely many possible energies, so eventually no such difference remains. Therefore \(y(t+1)=y(t-1)\) at all sufficiently late times, proving eventual period one or two. This self-contained argument is a finite symmetric-threshold version of the classical period-two theorem.

**2. Fixed configurations.** For \(h=0\), a rim one fixed under \(T_0\) forces both cyclic neighbors to be one, hence forces the entire rim to be one, contradicting the fixed hub opinion. Thus the only fixed configuration with \(h=0\) is all zeros. Complementing bits shows that the only fixed configuration with \(h=1\) is all ones.

**3. Two-cycles with a constant hub.** The rim maps satisfy
\[
(T_0^2(x))_i=x_{i-2}x_ix_{i+2},\qquad
(T_1^2(x))_i=x_{i-2}\vee x_i\vee x_{i+2}.
\]
A rim fixed by either square must be constant on every connected component of the step-two graph (use occupied vertices for \(T_0\), and unoccupied vertices for \(T_1\)). For odd \(n\), that graph is one cycle and the only possible rim strings are all zero or all one, leading only to fixed configurations. For even \(n\), it consists of two parity cycles. The nonconstant possible strings alternate zero and one around the rim. They swap under either rim map, and have exactly \(n/2\) occupied vertices, so the hub retains either value. These give one primitive two-cycle for \(h=0\) and one for \(h=1\). The all-constant cases cannot supply further two-cycles with unchanged hubs.

**4. Hub-flipping two-cycles.** Every such cycle has a unique point \((x,0)\). Its next point is \((y,1)\) with \(y_i=x_{i-1}x_{i+1}\). The hub moves zero-to-one precisely when \(2k>n\), where \(k=\sum_i x_i\); it returns one-to-zero precisely when \(2e<n\), where \(e=\sum_i y_i=\sum_i x_i x_{i+2}\). The rim returns after the second update exactly when
\[
(T_1(T_0(x)))_i=x_i(x_{i-2}\vee x_{i+2})=x_i
\quad\text{for all }i.
\]
Equivalently, no occupied vertex is isolated in the step-two graph. These three conditions are necessary and sufficient, with no multiplicities from phase choice because the representative has the unique hub value zero.

**5. Exact enumeration.** The step-two graph is a single cycle of length \(n\) for odd \(n\), and two disjoint cycles of length \(n/2\) for even \(n\). On a cyclic component of length \(m\), let \(k\) count ones and \(e\) count directed adjacent occupied pairs. Besides the empty and full configurations, a valid word has \(r\ge1\) cyclic runs of ones, each of length at least two, separated by positive runs of zeros. Therefore \(k\ge2r\), \(m-k\ge r\), and \(e=k-r\). The numbers of compositions of one-run lengths and zero-run lengths are respectively
\[
\binom{k-r-1}{r-1},\qquad\binom{m-k-1}{r-1}.
\]
Marking an initial run boundary among the \(m\) labelled cyclic positions counts each cyclic string \(r\) times, so its multiplicity is \(m/r\) times the product. This proves the displayed \(R_m\); the two components multiply for even \(n\), producing \(P_n\). Filtering by the strict inequalities in Step 4 proves \(A_n\), and Steps 1–3 prove the complete cycle census.

## Verification
Run `python3 verify_generating.py` to reproduce the coefficient extraction and an independent direct bitstring test for \(3\le n\le19\), plus exhaustive run-polynomial coefficients through component length fifteen. Compile `verify_orbits.cpp` with `c++ -O2 -std=c++17 verify_orbits.cpp -o verify_orbits` and execute `./verify_orbits`: it enumerates all \(2^{n+1}\) labelled wheel configurations for \(3\le n\le19\), applying the graph-level synchronous rule twice and counting exact fixed and primitive two-cycle states. The scripts use different constructions, agree at every tested length, and verify the first nontrivial values
\[
(A_4,A_5,A_6,A_7,A_8,A_9,A_{10},A_{11},A_{12})
=(0,5,9,21,32,66,75,220,225).
\]
The included text outputs record actual executions. These finite checks corroborate, but do not replace, the infinite proof above.

## Relationship to prior work
Goles and Olivos (1980) proved the general period-at-most-two property for symmetric threshold dynamics; that general conclusion is not claimed as novel. Agur, Fraenkel and Klein (1988) counted fixed points of the *self-inclusive radius-one majority rule* on binary cyclic strings, not wheel majority with a dynamically updated hub. Tamuz and Tessler (2013) and Kaaser, Mallmann-Trenn and Natale (2015) developed general majority-voting dynamics and convergence theory; their inspected treatments do not give this wheel-specific exact temporal census. The new component is the hub-flipping return criterion and its exact two-parameter cyclic-run enumeration, along with the two exceptional hub-preserving cycles. Historical mathematical priority beyond the inspected literature is not independently certified.

## Limitations
The result counts the eventual primitive periods and initially periodic configurations, **not** the number of transient states in each basin or their first-entry times. It assumes simple wheel graphs with \(n\ge4\), binary synchronous open-neighbor majority, and retention on ties; other voting conventions, asynchronous updates, or graph families are not covered. A complete historical-priority audit is not available, particularly for inaccessible earlier threshold-dynamics sources. Program checks are finite and do not independently certify infinite claims.

## References
- E. Goles and J. Olivos, “Periodic behaviour of generalized threshold functions,” *Discrete Mathematics* **30** (1980), 187–189, DOI `10.1016/0012-365X(80)90121-1`.
- Z. Agur, A. S. Fraenkel, and S. T. Klein, “The number of fixed points of the majority rule,” *Discrete Mathematics* **70** (1988), 295–302, DOI `10.1016/0012-365X(88)90005-2`. Lawful author-posted text: https://u.cs.biu.ac.il/~tomi/Postscripts/majority.pdf.
- O. Tamuz and R. J. Tessler, “Majority Dynamics and the Retention of Information,” arXiv:1307.4035v1, first posted 2013-07-15, https://arxiv.org/abs/1307.4035.
- R. Kaaser, T. Mallmann-Trenn, and E. Natale, “On the voting dynamics in social networks,” arXiv:1508.03519v1 (2015), https://arxiv.org/abs/1508.03519.
