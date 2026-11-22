# Arbitrarily many opinion-order reversals before finite consensus with three directed trust bounds

## Finding
For every integer \(m\geq0\), a three-agent unsigned edge-heterogeneous bounded-confidence system exists with fixed strictly positive confidence bounds, fixed step \(\tau=1/3\), and initial opinions independent of \(m\), in which **each of the three agent pairs reverses its strict opinion ranking at least \(2m+2\) times**, yet all three opinions become exactly equal for the first time at update
\[
T_m=12m+17.
\]
The construction uses reverse-direction confidence \(\delta_m=1/(5832\cdot729^m)\); its final unanimous opinion is exactly
\[
c_m=\frac13+\frac{17}{708588\cdot729^m}.
\]
Three agents are minimal: in the same update model, two agents can never strictly reverse their relative order at any admissible step size. This result concerns **temporal ranking**, not periodic or recurrent opinion dynamics: every constructed trajectory reaches exact consensus.

## Assumptions and scope
Consider the unsigned, synchronous, edge-heterogeneous fixed-step bounded-confidence rule for \(n\) agents:
\[
x_i(t+1)=x_i(t)+\tau\sum_{j\ne i:\;|x_j(t)-x_i(t)|<\varepsilon_{ij}}(x_j(t)-x_i(t)),\qquad0<\tau\leq1/n,
\]
with scalar opinions in \([0,1]\) and fixed strictly positive ordered-pair confidence thresholds \(\varepsilon_{ij}\). A strict order reversal for agents \(i,j\) occurs between consecutive observations when the signs of their nonzero opinion differences change; consequently, opposite signs at endpoints of a time interval force at least one strict ordering reversal during the interval, since the construction has no intervening equality in its first phase.

For each \(m\geq0\), take \(n=3\), \(\tau=1/3\), initial opinions \(x(0)=(0,1/4,3/4)^\top\), forward confidence thresholds
\[
\varepsilon_{12}=\varepsilon_{23}=\varepsilon_{31}=1,
\]
and reverse thresholds
\[
\varepsilon_{21}=\varepsilon_{32}=\varepsilon_{13}=\delta_m=\frac{1}{5832\cdot729^m}>0.
\]
All updates use the strict confidence inequality, and the opinion diameter always stays at most \(3/4\), so all three forward arcs remain active. Reverse arcs may activate as opinions approach each other.

## Proof
Write \(J=\mathbf1\mathbf1^\top/3\) and let \(P\) be the matrix that cyclically shifts the three coordinates forward. While the three reverse arcs are inactive, the one-step update matrix is
\[
W=\frac{2I+P}{3}
=\begin{pmatrix}2/3&1/3&0\\0&2/3&1/3\\1/3&0&2/3\end{pmatrix}.
\]
Direct rational multiplication, or the relation \(P^2+P+I=3J\), gives the exact identities
\[
W^6=J-\frac1{27}(I-J),\qquad
W^{12}=J+\frac1{729}(I-J).
\]
Therefore every nonzero pairwise difference changes sign between time \(t\) and time \(t+6\) during the one-way phase, and every difference is scaled by \(729^{-k}\) after \(12k\) one-way steps.

For the first twelve iterates \(W^t x(0)\), \(0\leq t\leq11\), exact rational evaluation yields
\[
\min_{0\leq t\leq11}\min_{i<j}|(W^tx(0))_i-(W^tx(0))_j|=\frac1{2916}.
\]
In particular there are no ties. At any \(0\leq t\leq12m+11\), write \(t=12k+r\) with \(k\leq m\) and \(0\leq r\leq11\). The minimum pair gap of the hypothetical one-way orbit is at least \(729^{-m}/2916=2\delta_m\), so all reverse arcs are in fact inactive at every update through \(12m+11\). Induction validates the hypothetical orbit. All three pairwise rankings reverse in each six-step interval ending at times \(6,12,\ldots,12m+12\), giving at least \(2m+2\) reversals for every pair.

For the exact stopping time, let \(y(t)\) denote the **full** confidence-gated trajectory with \(m=0\). Since \(x(12m)=\frac13\mathbf1+729^{-m}(x(0)-\frac13\mathbf1)\), the fixed-threshold and convex-combination rule implies the exact scaling conjugacy
\[
x_m(12m+s)=\frac13\mathbf1+729^{-m}\bigl(y(s)-\frac13\mathbf1\bigr),\qquad s\geq0,
\]
because the reverse thresholds scale by the same factor and all forward arcs remain active. It suffices to solve the single rational base trajectory.

Let \(\Delta(t)=(y_1(t)-y_2(t),y_1(t)-y_3(t),y_2(t)-y_3(t))/\delta_0\), with \(\delta_0=1/5832\). Exactly evaluating the gated update gives:

| \(t\) | \(\Delta(t)\) | Active reverse arcs at \(t\) |
|---|---|---|
| 12 | \((-2,-6,-4)\) | none |
| 13 | \((-8/3,-10/3,-2/3)\) | \(3\to2\) |
| 14 | \((-2,-10/9,8/9)\) | \(3\to2\) |
| 15 | \((-28/27,-10/27,2/3)\) | \(1\to3,3\to2\) |
| 16 | \((-28/81,0,28/81)\) | all three |
| 17 | \((0,0,0)\) | all three |

For \(0\leq t\leq11\) all reverse arcs are inactive, as already proved. The displayed gaps show that \(y(t)\) is nonunanimous for every \(12\leq t\leq16\); at time 16 the interaction digraph is complete and \(\tau=1/3\), so the next update gives exact consensus at time 17. Its rational value is \(236213/708588=1/3+17/708588\). The scaling conjugacy yields \(T_m=12m+17\) and the stated value \(c_m\) for all \(m\).

For minimality, when \(n=2\), write \(a_{ij}(t)\in\{0,1\}\) for the active trust indicator. Then
\[
x_1(t+1)-x_2(t+1)
=\bigl[1-\tau(a_{12}(t)+a_{21}(t))\bigr](x_1(t)-x_2(t)),
\]
and its coefficient is nonnegative because \(\tau\leq1/2\). Hence no pair can strictly reverse its opinion ordering with at most two agents.

## Verification
The standalone `checker.py` reconstructs both matrix-power identities over exact rational numbers, exhausts the twelve one-way phase gaps, evaluates all actual confidence gates and trajectories for \(m=0,1,2,3\), and checks all 64 possible products of two admissible three-agent one-way-plus-optional-reverse update matrices. It prints a PASS verdict. The displayed finite computations establish the necessary finite base-case identities; the proof's scaling argument—not enumeration over \(m\)—establishes the statement for every integer \(m\geq0\). A general contraction bound also follows because every two-step transition matrix has entries at least \(1/9\), so the opinion diameter contracts by at least a factor \(2/3\) every two steps until the one-step complete-graph consensus. The proof above supplies the sharper exact stopping time for this family.

## Relationship to prior work
Huang, Ma, Shi and Chen introduce the ordered-pair confidence thresholds and fixed-step unsigned model (their equations (3)–(4)), and prove conditional sufficient statements for convergence of separated opinion clusters; they do not state the above exact temporal-ranking construction or its unbounded reversal count. General bounded-confidence convergence theory already supplies many finite-consensus criteria, and standard spectral theory predicts damped oscillatory modes on directed cycles: neither of those generic ingredients is claimed as new. The present contribution isolates the smallest strictly-positive-trust social system with arbitrarily long **pre-consensus ranking instability**, and calculates exact reversal lower bounds, activation pattern, stopping times, and biased unanimous values within that specific endogenous threshold model.

## Limitations
This is an explicit family and a sharp minimum-agent result, not an upper bound on all possible ranking reversals at fixed thresholds or a classification of arbitrary directed social networks. It does not assert that individual beliefs oscillate indefinitely: the opinion vector becomes constant in finite time. The confidence asymmetry and very small reverse thresholds are idealized; the result makes no empirical causal claims about social platforms. While related results were compared, a full historical priority certification is not available; no independent validation has been performed.

## References
1. Z. Huang, Z. Ma, L. Shi and L. Chen, “Opinion Dynamics in Social Networks with Edge-Heterogeneous Confidence Bounds: Clustering, Polarization, and Implications for Online Platforms,” *Future Internet* **18** (2026), 355, first public 9 July 2026. https://doi.org/10.3390/fi18070355
2. G. J. Li, J. Luo and M. A. Porter, “Bounded-Confidence Models of Opinion Dynamics with Adaptive Confidence Bounds,” *SIAM Journal on Applied Dynamical Systems* **24** (2025), 994–1041; first preprint March 2023. https://arxiv.org/abs/2303.07563
3. “Bounded confidence opinion dynamics: A survey,” *Automatica* (2023). https://doi.org/10.1016/j.automatica.2023.111302
