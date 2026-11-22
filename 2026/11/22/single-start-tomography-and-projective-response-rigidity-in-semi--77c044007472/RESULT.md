# Single-start tomography and projective response rigidity in semi-Markov networks

## Finding
Let a finite semi-Markov network have one unknown outgoing joint waiting-time/transition-law row at a designated state \(n\), with every other row known. Suppose jumps are non-instantaneous, transitions from a state to itself are excluded, and the process starts at a fresh entry into \(n\). The complete family of transient occupation probabilities of the other states uniquely determines every unknown outgoing joint measure.

More precisely, at every real \(s>0\) the Laplace-occupation response \(y(s)\) and the unknown outgoing-kernel transform \(q(s)\) are related by an explicitly invertible projective map,
\[
y=\frac{qB}{1-qh},\qquad
q=\frac{yB^{-1}}{1+yB^{-1}h}.
\]
Here \(B\) and \(h\) are computable solely from the known rows (definitions below). Thus, for any family of local perturbations, the affine dimension of the set of full Laplace-occupation vectors at fixed \(s\) equals the affine dimension of its outgoing-kernel transform vectors. In particular, full-vector mutual linearity holds **if and only if** the outgoing-kernel family lies in an affine line at that \(s\), including the degenerate one-point case.

Equivalently, if the network undergoes independent Poisson resets to \(n\) at a tunable rate \(r>0\), with the waiting clock also reset, then observing all the stationary occupation probabilities for all positive reset rates determines the unknown joint exit measures. No finite prescribed set of reset rates can identify an unrestricted unknown outgoing waiting-time law, even with noiseless full-state occupation observations.

## Assumptions and scope
Fix \(N\ge2\) labelled states and a distinguished state \(n\); let \(S\) be the other \(N-1\) states in a fixed order. The semi-Markov kernel \(Q_{ij}\) is a finite nonnegative Borel measure on strictly positive holding times, recording jointly the time to the next transition and its destination. Self-jumps are absent, and each row has total measure at most one; a deficient row represents a possible infinite holding time (including an absorbing state). Kernels at all \(i\in S\) are known, and the complete row \((Q_{nj})_{j\in S}\) is unknown. The kernel is time-homogeneous and is renewed upon each state entry. Measurements start at age zero in state \(n\).

For \(s>0\), define \(\widehat Q_{ij}(s)=\int_{(0,\infty)}e^{-st}Q_{ij}(dt)\), and partition its matrix as
\[
\widehat Q(s)=\begin{pmatrix}0&q(s)\\r(s)&R(s)\end{pmatrix}.
\]
The row \(q\) has length \(N-1\), \(r\) is a column of length \(N-1\), and \(R\) is square. Let
\[
d_i(s)=\frac{1-\sum_j\widehat Q_{ij}(s)}s\quad(i\in S),\qquad
D_S=\operatorname{diag}(d_i:i\in S),
\]
\[
B=(I-R)^{-1}D_S,\qquad h=(I-R)^{-1}r.
\]
These are known. The observed row is
\[
y(s)=\left(\int_0^\infty e^{-st}\Pr_n\{X_t=j\}\,dt\right)_{j\in S}.
\]
The initial condition is an entry-time condition, not an observation sampled at equilibrium age. The full set of \(N-1\) noninitial-state occupations is used; no event-by-event transition observation is assumed. All formulas hold for every real \(s>0\), even when holding-time means are infinite.

## Proof
**1. Resolvent validity.** For every \(s>0\), each row sum of \(\widehat Q(s)\) is strictly below one: positive finite waits give a strict discount, while infinite waits add no mass. Thus \(I-\widehat Q\) and \(I-R\) are nonsingular, with nonnegative Neumann inverses. Each \(d_i>0\), so \(D_S\) and \(B\) are invertible. With \(\phi_i(t)=1-\sum_jQ_{ij}((0,t])\), the renewal equation for the transition function is \(P_{ij}(t)=\delta_{ij}\phi_i(t)+\sum_k(Q_{ik}*P_{kj})(t)\). Laplace transformation gives
\[
\widehat P(s)=(I-\widehat Q(s))^{-1}\operatorname{diag}\left(\frac{1-\sum_j\widehat Q_{ij}(s)}s\right).
\]
This also applies to absorbing states and arbitrary positive-time atoms. Finite state space and strictly positive holding times rule out explosion: some \(\varepsilon,\delta>0\) give at least probability \(\delta\) of a wait longer than \(\varepsilon\) at each actual jump, uniformly across the finitely many states.

**2. Explicit forward and inverse maps.** Write \(Z=\widehat P_{S,S}\) and \(y=\widehat P_{n,S}\). The two block rows of the renewal equation, restricted to columns \(S\), read
\[
y=qZ,\qquad (I-R)Z=D_S+ry.
\]
Consequently \(Z=B+hy\) and \(y=qB+(qh)y\), proving the first displayed formula. The entries of \(h\) are discounted hitting probabilities of \(n\) starting from \(S\), bounded by one. As \(\sum_jq_j<1\), the denominator \(1-qh\) is strictly positive. Setting \(z=yB^{-1}\) gives \(z=q/(1-qh)\), hence \(q=z/(1+zh)\). No unknown holding-time survival function at \(n\) enters the observed noninitial-state columns.

**3. Identifiability.** If two admissible unknown outgoing rows give the same \(\Pr_n\{X_t=j\}\) for all \(t\) and every \(j\in S\), their Laplace vectors \(y(s)\) agree at all \(s>0\). The inverse formula makes all component transforms \(q_j(s)\) equal. Uniqueness of Laplace transforms of finite Borel measures on \([0,\infty)\) makes every corresponding joint measure identical. This is a noiseless identification statement, not a stable numerical Laplace-inversion theorem.

**4. Exact affine-dimension preservation.** Represent a row \(q\) by homogeneous coordinates \((q,1)\). The invertible matrix
\[
M=\begin{pmatrix}B&-h\\0&1\end{pmatrix}
\]
sends \((q,1)\) to \((qB,1-qh)\), which is a positive scalar multiple of \((y,1)\). For any finite selection of parameter values, the rank of the matrix whose rows are \((q,1)\) is therefore exactly the rank of the corresponding matrix of \((y,1)\): multiplication by \(M\) and nonzero row rescaling preserve rank. Subtracting one gives equality of affine-hull dimensions. Taking the supremum over finite selections proves the same for arbitrary parameter families, including constant families. The same proof establishes the line criterion in both directions; it does not assert pairwise linearity from observations of just two components when there are additional unobserved components.

**5. Reset-rate tomography and sharp finite-sample limit.** With independent Poisson resets to an age-zero entry into \(n\), the age since the last reset in stationarity is exponential of rate \(r\), so for each \(j\in S\), \(\pi_j(r)=r y_j(r)\). A complete positive-rate stationary scan therefore supplies all \(y(s)\), and step 3 identifies the unknown measures. Conversely, fix any finite distinct positive rates \(r_1,\ldots,r_K\). Choose \(K+2\) distinct strictly positive times \(t_1,\ldots,t_{K+2}\). The \((K+1)\)-by-\((K+2)\) matrix with first row all ones and remaining rows \((e^{-r_kt_l})_l\) has a nonzero null vector \(v\). In particular \(\sum_lv_l=0\). The two strictly positive weight vectors \((1/(K+2)\pm\epsilon v_l)_l\), for sufficiently small \(\epsilon>0\), give different probability distributions of positive holding times with equal Laplace transforms at every prescribed rate. Use either distribution in one positive-probability exit channel while leaving all other channels and rows unchanged. The resulting distinct semi-Markov models have identical \(q(r_k)\) and hence identical full stationary occupation vectors at all observed rates. Thus any finite prescribed scan is nonidentifying on the unrestricted kernel class.

## Verification
The accompanying standalone `verify.py` uses finite networks with non-exponential gamma-distributed, destination-dependent sojourn times. It independently constructs the full renewal resolvent, extracts one-start Laplace occupations, applies the reconstruction, and compares the two expressions across network sizes and Laplace arguments. It also checks straight and curved local-kernel families and equality of ranks of homogeneous vectors. The deterministic checker reports 210 passing consistency checks. These numerical checks are finite corroboration only; the proof above establishes the universal assertions.

Run with `python verify.py` (requires Python 3 and NumPy). No data download is required.

## Relationship to prior work
Voits and Schwarz (2026, arXiv:2611.06490v1) established global affine Laplace-occupation response under a one-dimensional affine perturbation of local semi-Markov transition laws and identified failures under unrestricted perturbations. Its main text and supplement provide the sufficient forward response relation and the underlying renewal-memory-kernel algebra. The result here instead derives a complete inverse of the locally perturbed outgoing *joint-law* row from one starting state's complete occupation vector, establishes the **converse** of the full-vector affine criterion, preserves *all* affine dimensions, and gives a finite-versus-complete reset-scan identifiability boundary. The sufficiency of affine-response behavior and the Poisson resetting identity are prior results and not claimed anew.

Voits (2026, arXiv:2610.13505v1) gives a general **forward** graph-theoretic description of semi-Markov occupations and passage statistics; Bradley, Dingle and Knottenbelt (2003) develop **forward** transient-state formulas and exact aggregation. These papers supply related transform methodology but do not state the single-start local-kernel inversion and full affine-dimension equivalence established here. A general forward resolvent makes the short algebraic derivation possible; an equivalent inverse statement implicit in older renewal-system or inverse-process literature remains a publication-priority risk. The new theorem is motivated by complete information recovery from stationary reset-response measurements without observing individual transitions.

## Limitations
The unperturbed background kernels must be exactly known; a fresh-entry initial state and full occupation profiles of the other states are required. The result does not identify simultaneous unknown changes at multiple states or allow invisible self-jumps. It does not claim recoverability from finitely many noisy or discretized observations. Real-axis Laplace inversion can be severely ill-conditioned. The affine-dimension conclusion refers to a complete occupation vector at each fixed Laplace argument, not to every arbitrarily selected pair of its components or to untransformed time-domain paths.

## References
1. J. B. Voits and U. S. Schwarz, *Mutual linearity in semi-Markov networks*, arXiv:2611.06490v1, first public 2026-11-04, https://arxiv.org/abs/2611.06490.
2. J. B. Voits, *Graph-theoretic framework for semi-Markov networks: transient and stationary occupation probabilities, hitting times and weak ergodicity breaking*, arXiv:2610.13505v1, first public 2026-10-09, https://arxiv.org/abs/2610.13505.
3. J. T. Bradley, N. J. Dingle and W. J. Knottenbelt, *Exact aggregation strategies for semi-Markov performance models* (2003), https://www.academia.edu/521204/Exact_aggregation_strategies_for_semi_Markov_performance_models.
4. J. van der Meer, B. Ertel and U. Seifert, *Thermodynamic inference in partially accessible Markov networks: A unifying perspective from transition-based waiting time distributions* (2022), arXiv:2203.12020, https://arxiv.org/abs/2203.12020.
