# Parity and long transients in majority dynamics on cycle complements

## Finding

Let \(G_N=\overline{C_N}\) denote the simple graph obtained from the complete graph on a cyclically ordered set of \(N\) vertices by deleting precisely the edges of the cycle. Apply synchronous binary strict majority among **open neighbors**, retaining the present bit at a tie. Write
\[
\tau(x)=\min\{t\ge0:F_N^{t+2}(x)=F_N^t(x)\}.
\]
For every **odd** \(N=2m+1\ge7\), all configurations enter a fixed point within two updates, the sharp worst-case entrance time is \(\max_x\tau(x)=2\), and the exact number of fixed configurations is \(2N+2\). The fixed configurations are the two unanimous strings and the \(2N\) near-alternating strings with exactly one cyclic equal-bit bond (a single \(00\) pair or a single \(11\) pair).

For every **even** \(N=2m\ge8\), the explicit balanced initial word
\[
w_m=11(01)^{m-2}00
\]
has **exact first-periodic-entry time** \(\tau(w_m)=m-2=N/2-2\). More precisely, for \(0\le t\le m-2\) its successive words, read in the same fixed vertex order, are
\[
F_{2m}^{t}(w_m)=
\begin{cases}
1^{t+2}(01)^{m-t-2}0^{t+2}, &t\text{ even},\\
0^{t+2}(10)^{m-t-2}1^{t+2}, &t\text{ odd}.
\end{cases}
\]
At time \(m-2\), the trajectory enters the primitive two-cycle \(1^m0^m\longleftrightarrow0^m1^m\) (with orientation determined by the parity of \(m\)). In particular, no universal constant bounds the worst-case majority entrance time for the vertex-transitive, diameter-two graphs \(G_N\), despite their minimum degree \(N-3\). **No claim is made that \(m-2\) is the global maximum for even \(N\).**

## Assumptions and scope

The vertices are \(\{0,1,\ldots,N-1\}\) modulo \(N\); two distinct vertices are adjacent in \(G_N\) precisely when they are *not* consecutive on the original cycle. A word \(x\in\{0,1\}^N\) has \(K=\sum_i x_i\) occupied sites. Vertex \(i\) sees \(K-q_i\) occupied neighbors, where \(q_i=x_{i-1}+x_i+x_{i+1}\), among \(N-3\) neighbors. Thus
\[
(F_Nx)_i=\begin{cases}
1,&2(K-q_i)>N-3,\\
0,&2(K-q_i)<N-3,\\
x_i,&2(K-q_i)=N-3.
\end{cases}
\]
This formula defines all quantifiers and the tie rule. For \(N\ge7\), each deleted cycle edge has a common neighbor in the complement, so the graph is connected and has diameter two; it is also regular of degree \(N-3\) and vertex-transitive.

## Proof

**Odd order.** Put \(N=2m+1\ge7\). Every state with \(K\le m-1\) becomes all zero in one update: for an original 1, its neighbor-one count is at most \(K-1\le m-2\), below the tie threshold \(m-1\), whereas an original 0 sees at most \(m-1\) ones and cannot turn to 1. By complement symmetry, every state with \(K\ge m+2\) becomes all one in one update.

Suppose \(K=m\). The local rule gives \((F_Nx)_i=1\) exactly when the centered length-three word is \(000\) or \(010\). There are \(r\) cyclic zero runs and \(r\) cyclic one runs. Let \(a\) count one runs of length at least two and \(b\) count zero runs of length at least two. An isolated one gives one \(010\) center, and a zero run of length \(z\) supplies \(\max(z-2,0)\) centers \(000\). Since the total zero count is \(m+1\),
\[
|F_Nx|=(r-a)+\sum_{\mathrm{zero\ runs}}(z-2)_+
=(r-a)+(m+1-r-b)=m+1-a-b.
\]
As \(N\) is odd, not all runs can be singletons; \(a+b\ge1\). If \(a+b\ge2\), the next state has at most \(m-1\) ones and is all zero one update later. If \(a+b=1\), there cannot be a nonsingleton one run with all zero runs singletons: that would require \(r=m+1>m\) one runs, impossible. Hence every one run is a singleton and precisely one zero run has length two; all others have length one. These \(N\) near-alternating words are each fixed by direct inspection of centered triples. By bit complement, the \(K=m+1\) layer has exactly \(N\) additional fixed points and otherwise reaches all ones in two updates. Together with two unanimous states this gives exactly \(2N+2\) fixed configurations, no primitive two-cycle, and \(\tau\le2\). The initial string \(1^m0^{m+1}\) has \(a=b=1\), whence its first image contains \(m-1>0\) ones and its second image is all zero. Therefore \(\tau=2\) occurs.

**Even order.** Put \(N=2m\ge8\). If \(K=m\), the update reduces exactly to the *three-neighbor minority* rule
\[
(F_{2m}x)_i=1\quad\Longleftrightarrow\quad q_i\le1,
\]
because the degree \(2m-3\) is odd. Each listed word \(W_t\) in the theorem has the reflection-complement symmetry \((W_t)_i=1-(W_t)_{2m-1-i}\), so it has exactly \(m\) ones. Hence the reduction is valid at every claimed time. A direct inspection of cyclic length-three neighborhoods proves
\[
1^a(01)^k0^a\ \mapsto\ 0^{a+1}(10)^{k-1}1^{a+1},\quad
0^a(10)^k1^a\ \mapsto\ 1^{a+1}(01)^{k-1}0^{a+1}
\]
for integers \(a\ge2\), \(k\ge1\), under this minority rule (all words have the same even total length). Induction from \(a=2,k=m-2\) gives the displayed formula through \(t=m-2\). For \(k=0\), every cyclic triple in \(1^m0^m\) is majority-one on the first half and majority-zero on the second half, so the minority rule exchanges the two halves on every subsequent update.

For \(0\le t\le m-2\), the number of cyclic equal-neighbor bonds in \(W_t\) is exactly \(2(t+1)\); afterward it is \(2(m-1)\). This count strictly increases before \(t=m-2\), so no earlier \(W_t\) can equal \(W_{t+2}\). At \(t=m-2\), period two begins; therefore the first entrance time is exactly \(m-2\). This argument also verifies that the long transient occurs entirely at exactly half occupation; no balancing assumption is left unproved.

## Verification

The standalone program `check_exhaustive.cpp` independently computes all neighbor votes by enumerating graph edges; it exhaustively checks every configuration for odd orders \(N=7,9,\ldots,19\), verifies the exact fixed count and the sharp two-update bound, and checks the explicit even witnesses through \(N=20\). The separate `check_symbolic.py` tests the full even trajectory identity through \(m=40\) and the odd cyclic-run identity through \(N=15\). The results are captured as `check_exhaustive.out` and `check_symbolic.out`. These finite checks are diagnostics; the induction and cyclic-run argument above supply the proofs for all stated orders.

## Relationship to prior work

Goles and Olivos (1980) established eventual fixed-point-or-two-cycle behavior for general symmetric threshold systems. Benjamini, Chan, O'Donnell, Tamuz and Tan (arXiv:1405.2486v1, posted May 11, 2014) study unimodular and random-graph majority dynamics, while Fountoulakis, Kang and Makai (2020) prove rapid unanimity for sufficiently dense *random* graphs with random initial conditions. These theorems neither classify the odd complements of cycles nor forbid long specially prepared orbits on dense deterministic vertex-transitive graphs.

The even balanced reduction is algebraically related to three-neighbor cyclic majority by toggling every bit after each majority update. A pre-existing exact transient census for the ordinary radius-one cyclic majority rule therefore supplies useful comparison information for the *local* dynamics, but does not by itself assert the graph-complement parity dichotomy or its odd-order fixed-point classification. This relationship limits the novelty attributable to the even block-eroding mechanism alone. The contribution assessed here is the combined exact odd-order classification and explicit dense-graph slow trajectory, with their rigorous global-to-local derivation.

## Limitations

The even-order theorem proves a linear **lower** bound via an explicit configuration; it does not prove a matching global upper bound or count all even-order periodic or transient states. The short odd-order bound is deterministic and exact for all initial configurations. The examples do not contradict probabilistic rapid-convergence theorems, which impose randomness on the graph and/or initial state. Earlier unindexed results specifically on cycle-complement majority dynamics may exist. No independent audit is claimed.

## References

1. E. Goles and J. Olivos, “Periodic behaviour of generalized threshold functions,” *Discrete Mathematics* **30** (1980), 187–189, doi:10.1016/0012-365X(80)90121-1.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, L.-Y. Tan, “Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs,” arXiv:1405.2486v1 (May 11, 2014); *Stochastic Processes and their Applications* **126** (2016), 2719–2733.
3. N. Fountoulakis, M. Kang, T. Makai, “Resolution of a conjecture on majority dynamics: Rapid stabilization in dense random graphs,” *Random Structures & Algorithms* **57** (2020), 1134–1156, doi:10.1002/rsa.20970.
