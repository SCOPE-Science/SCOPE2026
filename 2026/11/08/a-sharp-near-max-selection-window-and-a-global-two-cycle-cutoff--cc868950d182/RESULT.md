# A sharp near-max selection window and a global two-cycle cutoff for a separable-field automaton

## Finding

**Theorem (sharp selection window and periodicity classification).** Fix integers \(H,W\ge4\), let \(N=\max\{H,W\}\), and consider the normalized binary separable-field cellular automaton defined below on the periodic \(H\)-by-\(W\) grid. Give the survival and birth rules the *same* closed interval
\[
\mathcal S=\mathcal B=[1-\varepsilon,1],\qquad 0\le\varepsilon\le1.
\]
For every possible nonzero configuration, the update selects **exactly** the cells of maximal unnormalized field if and only if
\[
\boxed{0\le\varepsilon<\frac1{3N}}.
\]
Throughout this sharp, positive-width parameter window, every nonzero trajectory becomes a nonempty binary rectangle in one update and thereafter factors into two independent one-dimensional maximum-neighborhood selectors. **Every orbit is eventually fixed or has primitive period two; no longer cycle is possible.** A period-two orbit exists for every \(H,W\ge4\). The transient has the uniform, explicit quadratic bound
\[
\boxed{1+(3N+1)(4N+2)}
\]
updates before the orbit is periodic, although there are initial rectangles whose transient length grows linearly with \(H\). The zero configuration is fixed. At the endpoint \(\varepsilon=1/(3N)\), the exact maximum-selector description ceases to hold for some configurations; no statement about emergence of longer cycles at that endpoint is asserted.

## Assumptions and scope

Let \(X=(X_{ji})\in\{0,1\}^{H\times W}\), with cyclic row and column indices. Put
\[
r_j=\sum_iX_{ji},\quad c_i=\sum_jX_{ji},\quad
R_j=r_{j-1}+r_j+r_{j+1},\quad
C_i=c_{i-1}+c_i+c_{i+1}.
\]
Write \(F_{ji}=R_jC_i\) and \(F_*=\max_{j,i}F_{ji}\). If \(X\ne0\), then \(F_*>0\), \(q_{ji}=F_{ji}/F_*\), and the output is \(1\) at \((j,i)\) if \(q_{ji}\in\mathcal S\) for a live input or \(q_{ji}\in\mathcal B\) for a dead input, and \(0\) otherwise. Here \(\mathcal S=\mathcal B\), so the old cell state does not enter this last membership test. As in the source model, the all-zero configuration maps to itself.

For any cyclic length \(n\ge4\), let \(K_n\) be the symmetric \(n\)-by-\(n\) binary matrix with \((K_n)_{ij}=1\) exactly when \(j-i\in\{-1,0,1\}\pmod n\). It has row sum three. For each nonempty \(A\subseteq\mathbb Z/n\mathbb Z\), define
\[
m(A)=\max_i\sum_{j\in A}(K_n)_{ij},\qquad
T_n(A)=\left\{i:\sum_{j\in A}(K_n)_{ij}=m(A)\right\}.
\]
Thus \(1\le m(A)\le3\), and \(T_n(A)\ne\varnothing\). All statements about cycles refer to the **full synchronous finite-state update**, not a simulation or a generic infinite-lattice limit.

## Proof

**1. A sharp field gap.** Let \(R_*=\max_jR_j\) and \(C_*=\max_iC_i\). For nonzero \(X\), both are positive, \(R_*\le3W\), \(C_*\le3H\), and \(F_*=R_*C_*\). Therefore
\[
q_{ji}=\frac{R_j}{R_*}\frac{C_i}{C_*}.
\]
If \(q_{ji}<1\), at least one numerator is a *smaller integer* than its positive maximum. If \(R_j<R_*\), then \(q_{ji}\le1-1/R_*\le1-1/(3W)\). If \(C_i<C_*\), then \(q_{ji}\le1-1/C_*\le1-1/(3H)\). In either case \(q_{ji}\le1-1/(3N)\). Hence \(\varepsilon<1/(3N)\) admits precisely \(q_{ji}=1\).

This width is sharp for **operator equality on all configurations**. Take a configuration containing ones everywhere except one zero cell. Since \(H,W\ge4\), row triples far from the hole have \(R_*=3W\), while triples covering its row have \(R_j=3W-1\); analogously \(C_*=3H\) and some \(C_i=3H-1\). A near-hole row together with a far column gives \(q=1-1/(3W)<1\), and a far row together with a near-hole column gives \(q=1-1/(3H)<1\). One of these equals \(1-1/(3N)\). It is admitted at \(\varepsilon=1/(3N)\), and remains admitted at larger widths, despite not being a maximum-field cell. Thus the stated interval is an if-and-only-if universal selection window, including its strict endpoint.

**2. One-step rectangular compression.** In this window, the next state is
\[
X'_{ji}=1_{\{R_j=R_*\}}\,1_{\{C_i=C_*\}}.
\]
Hence every nonzero state maps to a nonempty outer-product rectangle \(1_A\otimes1_B\). For such a rectangle, \(r_j=|B|1_A(j)\) and \(c_i=|A|1_B(i)\). Reapplying the formula gives
\[
1_A\otimes1_B\longmapsto1_{T_H(A)}\otimes1_{T_W(B)}.
\]
The two coordinates evolve independently and neither can become empty. The one-step image is therefore contained in at most \((2^H-1)(2^W-1)+1\) rectangular states, instead of the full \(2^{HW}\)-state space.

**3. Symmetric maximum-response potential.** It remains to analyze a single \(T_n\). For a trajectory \(A_{t+1}=T_n(A_t)\) with \(A_0\ne\varnothing\), set
\[
e_t=\frac{m(A_t)}{|A_t|}=
\frac{1}{|A_t||A_{t+1}|}\sum_{i\in A_t}\sum_{j\in A_{t+1}}(K_n)_{ij}.
\]
The last equality holds because every \(j\in A_{t+1}\) maximizes the number of links to \(A_t\). By symmetry of \(K_n\), this is also the average neighbor score of vertices of \(A_t\) against \(A_{t+1}\). This average cannot exceed the largest such score, divided by \(|A_{t+1}|\), which is exactly \(e_{t+1}\). Thus \(e_{t+1}\ge e_t\). More precisely, if equality holds, *every* vertex of \(A_t\) must maximize the score against \(A_{t+1}\), so
\[
\boxed{e_{t+1}=e_t\implies A_t\subseteq A_{t+2}.}
\]
Unlike a fixed-threshold argument, this uses the global, time-dependent maximum in the update definition.

**4. No longer cycles and a quadratic settling bound.** Each \(e_t\) lies in the finite set
\[
\left\{\frac{k}{a}:\ 1\le k\le3,\ 1\le a\le n\right\},
\]
which has at most \(3n\) values. Since the sequence is nondecreasing, it eventually becomes constant. From that point both parity subsequences \(A_s\subseteq A_{s+2}\subseteq A_{s+4}\subseteq\cdots\) are increasing. Each can have at most \(n-1\) strict inclusions. Eventually \(A_t=A_{t+2}\) for both consecutive parities, forcing a fixed point or a two-cycle. For an explicit uniform bound, on any constant-energy block at most \(2(n-1)\) inclusions can be strict. If two consecutive inclusions are equalities, the trajectory is already two-periodic. With no two adjacent equality inclusions, a block has at most \(4n-3\) inclusions. There are at most \(3n\) distinct energy levels, so \((3n+1)(4n+2)\) iterations certainly suffice for the one-dimensional trajectory. Applying this bound to both factors, and allowing the initial rectangularization, proves the asserted \(1+(3N+1)(4N+2)\) bound for the full grid.

**5. Genuine cycles and growing transients.** For \(n\ge4\), \(T_n\) maps a singleton \(\{i\}\) to the cyclic three-site interval \(\{i-1,i,i+1\}\), and maps that interval back to the singleton. Hence a one-cell grid configuration alternates with its \(3\)-by-\(3\) block, giving a genuine two-cycle for all \(H,W\ge4\). For \(H\ge8\), fix \(W\ge4\), take all columns live on a contiguous block of \(L=H-3\) rows, and all other rows empty. While the block has length at least three, its maximum-neighborhood update erodes one live row from each end, replacing length \(\ell\) by \(\ell-2\). The transient therefore contains at least \(\lfloor(H-5)/2\rfloor\) genuine shrinking steps, proving a lower bound linear in grid height. This completes the theorem.

## Verification

The standalone standard-library program `verify.py` implements the full two-dimensional normalized update and an independently specified maximum-field update, using exact integer or rational comparisons. Running `python3 verify.py` prints `VERIFY_OK checks=238104`. It enumerates all nonzero cyclic one-dimensional seeds for lengths \(4\) through \(14\), checks symmetric-potential monotonicity and the inclusion condition, and classifies each eventual cycle. It also checks all \(65,536\) four-by-four binary matrices for exact one-step reduction, samples larger rectangles, tests both sides of the sharp threshold, and verifies period-two and linear-transient witnesses. These are finite diagnostics; steps 1–5 constitute the universal proof.

## Relationship to prior work

Shi and Huang [1] introduce this precise normalized rank-one field automaton and investigate its outcome phase diagram numerically. The present sharp, positive-width maximum-selection phase and its all-configuration two-cycle cutoff concern a parameter region not identified in the accessible abstract and extracted introductory model text. The full primary manuscript was not accessible during this literature check, so the possibility of additional material in later sections remains an explicit priority risk.

A separately published analysis [2] embeds Rule 54 and Rule 18 in a stripe subsystem of the same model for threshold ranges placing survival around \(1/3\) and births around \(1/3,2/3\); it obtains long primitive cycles at those **different thresholds**. Its statements do not imply the present full-state-space classification for coincident near-one birth and survival intervals. Conversely, our theorem makes no claim about those other parameters.

Goles and Olivos [3,4] establish classical period-at-most-two results for synchronous networks with *fixed symmetric threshold functions*. The selector here has a moving global maximum, so their hypotheses are not directly satisfied, and they do not give the new sharp threshold width or the one-step rectangular factorization. The monotone reciprocal-score argument resembles established potential-game reasoning; that mechanism itself is not claimed as new. The new assertion is the full-grid finite-size phase theorem with its sharp operator boundary and quantitative settling bound.

## Limitations

The parameter window \(\varepsilon<1/(3\max\{H,W\})\) depends on grid size, and its endpoint is sharp **only for equivalence to the exact maximum selector**; the behavior of the original automaton just above this boundary is not classified. The quadratic settling-time bound is deliberately conservative and not claimed optimal. The long-transient construction is a lower bound, not a complete basin census. The theorem is for periodic finite grids, common survival and birth intervals, and exact synchronous updates; it does not extend the conclusion to distinct intervals, noisy updates, or infinite grids. The mathematical proof has not undergone independent validation. A fully inaccessible portion of the motivating source leaves a residual historical-priority risk.

## References

[1] X. Shi and M. Huang, *Dynamics in a Low-Rank Separable Field Cellular Automaton*, arXiv:2606.08983, first public version 8 June 2026, https://arxiv.org/abs/2606.08983; extracted introductory model text at https://paperity.org/p/373803123/dynamics-in-a-low-rank-separable-field-cellular-automaton.

[2] *An irreversible Rule-54/Rule-18 phase filtration in a normalized separable-field automaton*, public research result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-an-irreversible-rule-54-rule-18-phase-filtration-in-a-normalized--ac12be561c8d.

[3] E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, *Discrete Mathematics* **30** (1980), 187–189, doi:10.1016/0012-365X(80)90121-1.

[4] E. Goles and J. Olivos, *Comportement périodique des fonctions à seuil binaires et applications*, *Discrete Applied Mathematics* **3** (1981), 93–105, doi:10.1016/0166-218X(81)90034-2.
