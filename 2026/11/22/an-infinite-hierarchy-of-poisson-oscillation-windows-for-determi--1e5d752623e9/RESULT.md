# An infinite hierarchy of Poisson oscillation windows for deterministic plurality on cliques

## Finding

Let \(n\ge2\) labelled vertices form the complete simple graph \(K_n\), with \(q\ge2\) named colors. At each synchronous update a vertex adopts the **unique** most frequent color in its *open neighborhood*; when there is no unique maximum, it retains its current color. If \(c_a\) is the number of vertices initially colored \(a\), put \(M=\max_a c_a\) and \(J=|\{a:c_a=M\}|\). The complete dynamics is:

* \(J=1\): the first update gives unanimity in the unique plurality color, which is thereafter fixed;
* \(J=2\): the two maximally populated color classes exchange their colors at every update, all remaining vertices retain their colors, and the state is on a primitive two-cycle from time zero;
* \(J\ge3\): the original state is fixed.

There are no other orbits, and no transient state feeds a nonconstant attractor. The exact number \(B(n,q)\) of *labelled initial states* on primitive two-cycles is
\[
B(n,q)=\binom q2 n!\sum_{m=1}^{\lfloor n/2\rfloor}
\frac{[z^{n-2m}]\bigl(\sum_{j=0}^{m-1}z^j/j!\bigr)^{q-2}}{(m!)^2}.
\]
Thus there are exactly \(B(n,q)/2\) distinct primitive two-cycles.

Now choose all initial colors independently and uniformly among the \(q=q_n\) colors. For each **fixed integer \(k\ge2\)** and each fixed \(c>0\), if
\[q_n\sim c\,n^{k/(k-1)},\qquad \lambda_k=\frac{1}{k!c^{k-1}},\]
then the probability \(P_{n,q_n}\) of a nonconstant eventual attractor satisfies
\[
\lim_{n\to\infty} P_{n,q_n}=\frac{\lambda_k^2}{2}e^{-\lambda_k}.
\]
Each of the infinitely many critical palette scales \(n^2,n^{3/2},n^{4/3},\ldots\) therefore has an oscillation peak of identical limiting height \(2e^{-2}\), attained at
\[c=(2k!)^{-1/(k-1)}.\]
For every fixed \(\alpha>1\) different from all critical exponents \(k/(k-1)\), if \(q_n\sim c n^\alpha\), the oscillation probability tends to zero. These are isolated windows on the power-law palette scale; no assertion is made for general \(q_n\) below linear order or for \(\alpha=1\).

## Assumptions and scope

All vertices, colors and time steps are labelled. The graph has no self-loops; every vertex observes all *other* vertices. The unique modal neighbor color is adopted, not a random tie winner; in any tie among two or more modal colors the vertex retains its prior color. The number \(q\) may exceed \(n\). The exponent \(k\) in the critical-window statement is held fixed as \(n\to\infty\). Oscillation probability refers to the initial independent-uniform product distribution on all \(q^n\) configurations. It counts an orbit of least temporal period two rather than an arbitrary color change during a transient.

## Proof

**(1) Exact dynamical trichotomy.** Fix a vertex with current color \(a\). Its open-neighborhood counts are \(c_a-1\) for color \(a\) and \(c_b\) for every other color \(b\). If \(J=1\) with leading color \(b\), every non-\(b\) vertex sees \(b\) uniquely most often and changes to \(b\). A \(b\)-vertex sees at most \(M-1\) counts in every other class, whereas its own neighborhood count is \(M-1\), and therefore either retains \(b\) at a tie or adopts \(b\) uniquely. Hence all vertices are \(b\) after the first update.

If \(J=2\) with maximal colors \(a,b\), each \(a\)-vertex sees \(b\) with count \(M\), uniquely largest; each \(b\)-vertex sees \(a\) uniquely largest. Every vertex with another color sees two classes of size \(M\), tied, and does not change. Swapping these maximal colors leaves their populations equal and the smaller populations unchanged, so repeating once returns the original state, and one step is genuinely different. If \(J\ge3\), a vertex in a maximal color sees at least two *other* maximal colors both at count \(M\), and a vertex outside all maximal classes sees at least three such tied classes: every vertex retains its color. This exhausts the cases and proves the first three assertions.

**(2) Exact finite count.** For a state on a two-cycle choose the two top named colors in \(\binom q2\) ways and their common positive occupancy \(m\). Assign their disjoint size-\(m\) vertex sets with \(n!/(m!m!(n-2m)!)\) possibilities. Every other named color must have occupancy at most \(m-1\). The exponential polynomial \(E_{m-1}(z)=\sum_{j=0}^{m-1}z^j/j!\) gives exactly \((n-2m)![z^{n-2m}]E_{m-1}(z)^{q-2}\) admissible colorings of the remaining labelled vertices. Summation proves \(B(n,q)\). Each two-cycle contributes two distinct states.

**(3) Poisson law at a critical window.** Let \(X_{n,j}\) be the number of named colors occurring exactly \(j\) times. For any fixed positive integer \(r\), under \(q_n\sim c n^{k/(k-1)}\), direct multinomial counting gives
\[
\mathbb E (X_{n,k})_r=\frac{(q_n)_r(n)_{kr}}{(k!)^r q_n^{kr}}\left(1-\frac r{q_n}\right)^{n-kr}\ \longrightarrow\ \lambda_k^r.
\]
Thus \(X_{n,k}\) converges in distribution to a Poisson variable of mean \(\lambda_k\) by the factorial-moment method. Also \(\mathbb E\sum_{j\ge k+1}X_{n,j}\le\binom n{k+1}q_n^{-k}=O(n^{-1/(k-1)})\to0\), because any color with at least \(k+1\) occurrences contains a selected \((k+1)\)-subset. For \(k\ge3\), \(\mathbb E X_{n,k-1}\sim n^{1/(k-1)}/((k-1)!c^{k-2})\to\infty\); the same two-factorial-moment calculation proves \(\operatorname{Var}(X_{n,k-1})=o((\mathbb E X_{n,k-1})^2)\). For \(k=2\), at least \(n-2Z_n\) vertices are in singleton bins, where \(Z_n\) is the number of same-color vertex pairs and \(\mathbb E Z_n=\binom n2/q_n=O(1)\), so \(X_{n,1}\to\infty\) in probability. Consequently the event \(J=2\) differs with probability \(o(1)\) from \(\{X_{n,k}=2\}\), and its probability tends to \(\lambda_k^2e^{-\lambda_k}/2\).

**(4) Isolation of the power-law windows.** Let \(\alpha>1\) be a fixed exponent outside \(\{k/(k-1):k\ge2\}\) and \(q_n\sim c n^\alpha\). If \(\alpha>2\), the expected number of vertex pairs sharing a color is \(O(n^{2-\alpha})\to0\), so the top occupancy equals one and is attained by \(n\to\infty\) colors. Otherwise there is a unique integer \(k\ge2\) such that \((k+1)/k<\alpha<k/(k-1)\). Then \(\mathbb E X_{n,k}\to\infty\), its relative variance tends to zero by the same factorial-moment calculation, and the expected number of occupied color classes with at least \(k+1\) vertices tends to zero by the subset union bound. Hence the maximal occupancy is \(k\) with an unbounded number of maximizers, so \(\mathbb P(J=2)\to0\).

**(5) Sharp peak.** The function \(\lambda\mapsto\lambda^2 e^{-\lambda}/2\) has derivative \(\lambda(2-\lambda)e^{-\lambda}/2\), and hence its unique positive maximum is attained at \(\lambda=2\) with value \(2e^{-2}\). Solving \(1/(k!c^{k-1})=2\) yields the stated maximizing constant.

## Verification

The standalone `check_dynamics.py` verifies the update rule directly, and compares the exact coefficient formula with the number of actual primitive two-periodic initial states, for **all** \(q\in\{2,3,4,5\}\), \(n\in\{2,3,4,5,6,7,8\}\), a total of \(\sum_{q=2}^5\sum_{n=2}^8 q^n\) configurations. Each trajectory is checked by direct graph-neighborhood evaluation, without assuming the claimed trichotomy in the transition function. The run's `check_dynamics.out` records each count and terminates with `ALL_CHECKS_PASSED`. This finite verification checks the small-domain combinatorics; it does not prove the asymptotic statements, which use factorial moments and second moments above.

## Relationship to prior work

Classical symmetric binary threshold dynamics has period at most two [1]. Studies of plurality consensus on cliques [2,3] treat random-sample or undecided-state protocols, unlike the deterministic full-neighborhood unique-mode rule here. Binary tie-retaining majority [4] has a different state space, and multistate deterministic models [5] consider different update rules. Occupancy extreme-value and tie statistics [6] provide related probabilistic machinery but study urn stopping times rather than the exact link between two maximally occupied opinions and temporal oscillation. The finite coefficient formula and infinite sequence of power-law critical windows are claimed only for the exact dynamics defined above; the Poisson factorial-moment calculation uses standard occupancy methods, not a new general Poisson limit theorem.

## Limitations

The graph family is restricted to loopless complete graphs. The limiting formula holds for each **fixed** critical index \(k\), not for indices increasing with \(n\). There is no assertion of a uniform approximation across infinitely many windows at one finite network size. Existing general results about occupancy maxima and ties may yield the probabilistic portion after an additional argument; the claim of originality concerns the full dynamical identification, exact finite census and all-index phase hierarchy together. Unindexed prior equivalences cannot be ruled out by the bounded literature comparison.

## References

1. E. Goles and J. Olivos, "Periodic behaviour of generalized threshold functions," *Discrete Mathematics* 30 (1980), 187–189, doi:10.1016/0012-365X(80)90121-1.
2. L. Becchetti et al., "Simple Dynamics for Plurality Consensus," arXiv:1310.2858, first submitted 2013-10-10, https://arxiv.org/abs/1310.2858.
3. L. Becchetti et al., "Plurality Consensus in the Gossip Model," arXiv:1407.2565, first submitted 2014-07-09, https://arxiv.org/abs/1407.2565.
4. A. N. Zehmakan, "Majority opinion diffusion: when tie-breaking rule matters," *Autonomous Agents and Multi-Agent Systems* 38 (2024), article 21, doi:10.1007/s10458-024-09651-y.
5. M. Di Ianni, "Three Majority-Based Deterministic Dynamics for Three Opinions," *AppliedMath* 5 (2025), article 147, doi:10.3390/appliedmath5040147.
6. A. Gnedin, S. Janson and Y. Malinovsky, "Maximal Counts in the Stopped Occupancy Problem," arXiv:2506.20411, first submitted 2025-06-25, https://arxiv.org/abs/2506.20411.
