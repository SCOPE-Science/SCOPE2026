# Exact two-layer parity-modal truth profiles on random undirected frames

## Finding
Let \(n\ge2\), and choose uniformly from all simple labelled undirected graphs on vertices \([n]\). Write \(A\) for its symmetric zero-diagonal adjacency matrix over \(\mathbb F_2\), and \(\mathbf1\) for the all-one column vector. Starting with every vertex in state one, update synchronously by the parity of the current states of its neighbors. The first two states are \(d=A\mathbf1\) and \(t=A^2\mathbf1\).

Set \(H=\{x\in\mathbb F_2^n:\mathbf1^Tx=0\}\). For any prescribed labelled pair of states \((d,t)\), the exact number \(N_n(d,t)\) of underlying graphs is

\[
N_n(d,t)=
\begin{cases}
2^{\binom{n-1}{2}}, &(d,t)=(0,0),\\
2^{\binom{n-1}{2}}, &n\text{ even and }(d,t)=(\mathbf1,\mathbf1),\\
2^{\binom{n-2}{2}}, & d\in H\setminus\{0,\mathbf1\},\ t\in H,\ d^Tt=0,\\
0, &\text{otherwise.}
\end{cases}
\]

The vector \(\mathbf1\) in the set difference is excluded only if it lies in \(H\) (equivalently \(n\) is even). Equivalently, the first state is uniform over all even-weight words, and, except for the deterministic trajectories \(0\mapsto0\) and (for even \(n\)) \(\mathbf1\mapsto\mathbf1\), the second state conditional on the first is uniformly distributed over \(H\cap d^{\perp}\).

The marginal second-state law has only two (odd \(n\)) or three (even \(n\)) probability levels. If \(n\) is odd,

\[
\Pr(t=z)=\begin{cases}
(3\cdot2^{n-2}-1)/2^{2n-3},&z=0,\\
(2^{n-2}-1)/2^{2n-3},&z\in H\setminus\{0\},\\
0,&z\notin H.
\end{cases}
\]

If \(n\) is even,

\[
\Pr(t=z)=\begin{cases}
(3\cdot2^{n-2}-2)/2^{2n-3},&z=0\text{ or }z=\mathbf1,\\
(2^{n-2}-2)/2^{2n-3},&z\in H\setminus\{0,\mathbf1\},\\
0,&z\notin H.
\end{cases}
\]

The formulas hold including the small boundary case \(n=2\), where only \(t=0\) and \(t=\mathbf1\) are possible. They are exact for every \(n\), not merely limiting laws.

## Assumptions and scope
All vector spaces, dot products, and matrix products in this result are over \(\mathbb F_2\); a state is a **labelled vector** rather than merely its Hamming weight. The random graph has no loops, no oriented arcs, and independent fair choices for its \(\binom n2\) unordered potential edges. The update uses the **open** neighborhood and no self-state term. The two-step state is obtained from the first-state vector using the same static adjacency matrix; it is not sampled from an independent second graph.

In a parity-counting modal semantics, let \(P_0(v)\) hold at every vertex and set \(P_{i+1}(v)\) to hold precisely if \(\#\{u:u\sim v,\ P_i(u)\}\) is odd. The characteristic vectors of \(P_1,P_2\) are precisely \(d,t\). The motivating literature studies more general Presburger neighbor aggregation but does **not** itself assert a formula for this random-model distribution; its core syntax omits modulus tests, which its discussion identifies as an available extension. We do not claim that its particular neural-network architecture already implements these parity updates.

## Proof
**Alternating-extension counting lemma.** Let \(1\le r\le n\) and let \(S\in\mathbb F_2^{n\times r}\) have full column rank. For a specified \(Y\in\mathbb F_2^{n\times r}\), the number of symmetric zero-diagonal \(n\times n\) matrices \(A\) with \(AS=Y\) is

\[
\begin{cases}
2^{\binom{n-r}{2}},& S^TY\text{ symmetric with zero diagonal},\\
0,&\text{otherwise.}
\end{cases}
\]

To prove this, extend the columns of \(S\) to a basis, producing invertible \(P\) whose first \(r\) columns are \(S\). The congruence \(B=P^TAP\) is alternating, i.e. symmetric with zero diagonal. The equation \(AS=Y\) becomes \(B[I_r;0]=P^TY\). Therefore its first \(r\) columns are prescribed, its leading \(r\times r\) block is \(S^TY\), its top-right block is forced by symmetry, and its lower-right \((n-r)\times(n-r)\) block is arbitrary alternating. This proves both the necessary-and-sufficient consistency condition and the exact number of completions, without any probabilistic independence assumption.

**First state.** Take \(r=1\), \(S=\mathbf1\) and \(Y=d\). The lemma says that \(A\mathbf1=d\) holds for exactly \(2^{\binom{n-1}{2}}\) graphs if \(\mathbf1^Td=0\), and for none otherwise. Consequently \(d\) is uniform on \(H\) and has probability \(2^{1-n}\) at each admissible point.

**Joint state.** When \(d=0\), the second update forces \(t=0\). When \(n\) is even and \(d=\mathbf1\), it forces \(t=A\mathbf1=\mathbf1\). These give the two exceptional fibers. Otherwise \(d\in H\setminus\{0,\mathbf1\}\), and \(S=[\mathbf1\ d]\) has rank two. Prescribe \(Y=[d\ t]\). Its consistency block is

\[
S^TY=\begin{pmatrix}
\mathbf1^Td & \mathbf1^Tt\\
d^Td & d^Tt
\end{pmatrix}
=\begin{pmatrix}
0 & \mathbf1^Tt\\0 & d^Tt
\end{pmatrix},
\]

because \(d^Td=\mathbf1^Td=0\) in characteristic two. This is alternating if and only if \(\mathbf1^Tt=d^Tt=0\). The lemma then gives exactly \(2^{\binom{n-2}{2}}\) graphs in each such fiber. Since \(\mathbf1\) and \(d\) are independent, the admissible \(t\)'s form a codimension-two subspace, with \(2^{n-2}\) elements. The conditional-uniform statement and the full joint law follow.

**Marginal.** Fix \(z\in H\). Among the \(2^{n-1}\) vectors \(d\in H\), the linear condition \(d^Tz=0\) has \(2^{n-1}\) solutions if \(z\in\operatorname{span}\{\mathbf1\}\), or \(2^{n-2}\) solutions otherwise. From this count remove the exceptional possible \(d=0\) and, when \(n\) is even, \(d=\mathbf1\), whose contribution is not the generic fiber. For each remaining \(d\), joint probability is \(2^{\binom{n-2}{2}-\binom n2}=2^{3-2n}\), and each exceptional deterministic pair has probability \(2^{1-n}\). If \(n\) is odd, only the exceptional \(d=0\) exists and only \(z=0\) belongs to \(H\cap\operatorname{span}\{\mathbf1\}\), yielding the two advertised levels. If \(n\) is even, the two exceptional vectors and the two corresponding exceptional marginal values yield the three advertised levels. For \(z\notin H\), every fiber vanishes. This completes the finite formula, including boundary cases.

## Verification
The accompanying standalone `checker.py` independently enumerates all labelled simple graphs for every \(2\le n\le6\), computes both Boolean-neighborhood updates directly from edges, and compares the count of every ordered pair of binary vectors against the displayed fiber formula. This includes all \(2^{15}=32768\) graphs when \(n=6\), and all \(2^{2n}\) candidate state pairs for every tested \(n\). Expected terminal output: `ALL_TWO_LAYER_EXHAUSTIVE_CHECKS_PASS`. This is an exhaustive finite-domain cross-check, **not** the proof for arbitrary \(n\); the extension lemma supplies the proof for all sizes.

## Relationship to prior work
Benedikt, Lu, Perry, and Tan (2026) investigate decidability for two-variable logics with local and global Presburger aggregation over finite graphs; Section 5 specifically notes that modular count restrictions were not included in the core syntax but can be added. Their statements concern satisfiability and model-theoretic expressiveness, not a probability law for two synchronous modular updates on a uniform random graph.

Balister, Powierski, Scott, and Tan (preprint 2021; journal 2023) count graph partitions constrained by within-part degree congruences. Their Section 5 studies the rank distribution of random symmetric binary matrices and systems involving \(A+D\), with \(D\) the degree-parity diagonal. Those results do not enumerate the joint image \((A\mathbf1,A^2\mathbf1)\) of the *same* alternating matrix under iterative updates.

Janzer and Yip (preprint 2024; journal 2025) explicitly prove **the uniform even first-state law** in their Lemma 3.4, then use a conditional-degree-parity lemma (Lemma 3.5) to study even-decomposability and even-degeneracy. Neither result states the conditional second-state law or the complete two-step joint distribution; the first-state marginal is not claimed new here. Prokip's 2017 theorem describes symmetric solutions to linear matrix equations; alternating zero-diagonal constraints and the resulting nonlinear two-step random-graph law are not supplied by that theorem. These earlier algebraic principles provide techniques and should not be construed as evidence that the general extension lemma in isolation is new.

## Limitations
The theorem is for edge probability exactly \(1/2\), uniformly labelled *undirected* loopless graphs, two updates, and an initially constant-one state. It does not describe nonuniform edge probabilities, directed graphs, three or more parity updates, or non-modular neural-network aggregation. The linear-algebra counting ingredient is elementary and related to established symmetric matrix equations; no novelty is claimed for that ingredient alone. The exact two-state law was not located in the inspected literature, but an earlier equivalent formula under another encoding is a residual priority risk. Exhaustive verification ends at six vertices; independent mathematical audit has not been performed.

## References
- M. Benedikt, C.-H. Lu, A. Perry, T. Tan, *Deciding two-variable logic with global and local Presburger quantification*, arXiv:2610.39108v1 (first publicly posted 2026-10-29), https://arxiv.org/html/2610.39108v1.
- P. Balister, E. Powierski, A. Scott, J. Tan, *Counting partitions of \(G_{n,1/2}\) with degree congruence conditions*, arXiv:2105.12612v1 (2021), *Random Structures & Algorithms* **62** (2023), 564–584, https://doi.org/10.1002/rsa.21115.
- O. Janzer, F. Yip, *The probability that a random graph is even-decomposable*, arXiv:2409.11152v1 (2024), *Random Structures & Algorithms* **67** (2025), e70034, https://doi.org/10.1002/rsa.70034.
- V. M. Prokip, *The Structure of Symmetric Solutions of the Matrix Equation AX = B over a Principal Ideal Domain*, *International Journal of Analysis* (2017), Article 2867354, https://doi.org/10.1155/2017/2867354.
