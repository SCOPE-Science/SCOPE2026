# Optimal entanglement restoration by omitted gates on even hypercubes

## Finding

**Theorem (optimal matching-erasure law).** For every even integer \(n\ge2\), let \(Q_n\) be the ordinary \(n\)-dimensional Boolean hypercube, with vertices \(x\in\mathbb F_2^n\) and edges \(\{x,x+e_i\}\) for each coordinate \(i\). Prepare the pure qubit graph state by applying one controlled-\(Z\) gate on every edge to the product state \(\lvert+\rangle^{\otimes 2^n}\). Consider the balanced bipartition into even and odd Hamming-weight words.

Set
\[
F_n=\bigl\{\{x,x+e_1\}:x_1=x_2=0\bigr\}.
\]
This is a matching of exactly \(2^{n-2}\) cube edges. For every subset \(D\subseteq F_n\), omit precisely the gates indexed by \(D\), leaving all other gates unchanged. Then the bipartite von Neumann entropy and **every** positive-order Rényi entropy, in bits, are exactly
\[
\boxed{S(D)=2^{n-2}+|D|.}
\]
The reduced state has precisely \(2^{S(D)}\) nonzero eigenvalues, all equal to \(2^{-S(D)}\). For the full matching, \(S(F_n)=2^{n-1}\): the state is maximally entangled across the cut. **Optimality:** No set of fewer than \(2^{n-2}\) omitted cube-edge gates, whether or not a matching, can reach maximal entanglement. In particular, **every** subset of the specified matching gains exactly one entanglement bit for each omitted controlled-\(Z\) gate.

For example, the four-cube begins at four ebits and reaches the maximum eight after omitting four specified disjoint gates; the six-cube begins at sixteen and reaches thirty-two after sixteen omissions.

## Assumptions and scope

The integer \(n\) is even, at least two; the graph is the standard simple, unweighted Boolean cube. Each of its \(2^n\) vertices carries one qubit and each edge has exactly one ideal controlled-\(Z\) gate. The omitted set is any subset of the specified matching \(F_n\), except that the optimality lower bound applies to **all** possible omission patterns. The bipartition is specifically even versus odd total Hamming weight, with \(2^{n-1}\) qubits on each side. All matrix ranks in the proof are over \(\mathbb F_2\), not over the reals. Entropies use base-two logarithms; no noise, postselection, or auxiliary qubits are assumed. For odd \(n\), the unmodified full-parity cut is already maximally entangled, so the evenness assumption is essential to the nontrivial erasure threshold.

## Proof

**1. The binary cut-rank lemma.** For any bipartite pure qubit graph state with cross-cut adjacency matrix \(B\) over \(\mathbb F_2\), the Schmidt weights are flat and number \(2^{\operatorname{rank}B}\). Indeed, gates internal to either side are local unitaries for this split and may be ignored. In the computational bases indexed by bit strings \(a,b\), the remaining state amplitudes are \(2^{-N/2}(-1)^{a^TBb}\), where \(N\) is the total number of qubits. Character orthogonality gives
\[
\rho_A(a,a')=2^{-|A|}\mathbf1_{\{B^T(a+a')=0\}}.
\]
This scaled subgroup-convolution matrix has \(2^{\operatorname{rank}B}\) equal nonzero eigenvalues \(2^{-\operatorname{rank}B}\). Consequently all positive-order Rényi entropies and the von Neumann entropy equal \(\operatorname{rank}_{\mathbb F_2}B\) bits. This standard graph-state fact is due to [1] and is restated for completeness.

**2. Exact baseline rank.** Let \(A_n\) be the full \(2^n\)-by-\(2^n\) binary adjacency matrix of \(Q_n\). Every coordinate flip is an involution and distinct flips commute; hence \(A_m^2=mI\) in characteristic two. Split the cube according to its first bit. Then
\[
A_n=\begin{pmatrix}C&I\\I&C\end{pmatrix},\qquad C=A_{n-1}.
\]
Since \(n-1\) is odd, \(C^2=I\) over \(\mathbb F_2\). The image of the displayed linear map is exactly
\[
\{(w,Cw):w\in\mathbb F_2^{2^{n-1}}\}:
\]
indeed its output on \((u,v)\) is \((Cu+v,u+Cv)=(w,Cw)\), and every \(w\) occurs by setting \(u=0\), \(v=w\). Thus \(\operatorname{rank}A_n=2^{n-1}\). The cube is bipartite; ordering vertices by Hamming parity puts \(A_n\) in the form \(\left(\begin{smallmatrix}0&B_n\\B_n^T&0\end{smallmatrix}\right)\), whose rank equals \(2\operatorname{rank}B_n\). Hence the initial entropy is precisely \(\operatorname{rank}B_n=2^{n-2}\).

**3. The prescribed edge deletion yields an invertible matrix.** Regard \(Q_n=Q_2\square Q_{n-2}\), with coordinates one and two forming the first factor. The matching \(F_n\) deletes exactly the edge between \((0,0)\) and \((1,0)\) in *every* \(Q_2\) fiber, leaving a four-vertex path. Thus
\[
Q_n-F_n\cong P_4\square Q_{n-2}.
\]
Let \(H=A(P_4)\) be the binary adjacency matrix of the path. Direct elimination (or the unique perfect matching expansion) gives \(\det H=1\) in \(\mathbb F_2\), so \(H\) is invertible. Let \(T=A(Q_{n-2})\). Because \(n-2\) is even, \(T^2=(n-2)I=0\) over \(\mathbb F_2\), including \(T=0\) for \(n=2\). The full adjacency matrix after deleting \(F_n\) is
\[
A'=H\otimes I+I\otimes T
=(H\otimes I)\bigl(I+H^{-1}\otimes T\bigr).
\]
The second factor is invertible: its nonidentity part \(R=H^{-1}\otimes T\) satisfies \(R^2=0\), and in characteristic two \((I+R)^2=I\). Therefore \(A'\) is invertible. Since deleting cube edges preserves bipartiteness and both color classes have \(2^{n-1}\) vertices, its off-diagonal checkerboard block \(B'\) has full rank \(2^{n-1}\). This proves maximal entanglement after deleting the entire matching.

**4. Every partial matching erasure has unit gain per gate.** For \(D\subseteq F_n\), put \(k=|D|\) and \(K=|F_n|=2^{n-2}\). The cross-cut matrix after omitting \(D\) differs from \(B_n\) in only \(k\) entries, so rank subadditivity gives
\[
\operatorname{rank}B_D\le \operatorname{rank}B_n+k=K+k.
\]
It differs from the **full-omission** matrix \(B'\) in only \(K-k\) entries. Because \(\operatorname{rank}B'=2K\), the reverse rank inequality gives
\[
\operatorname{rank}B_D\ge\operatorname{rank}B'-(K-k)=K+k.
\]
The two bounds agree, so \(\operatorname{rank}B_D=K+k\) for all subsets, independent of placement or order within \(F_n\). Step 1 yields the asserted complete flat Schmidt spectrum.

**5. Optimality among all possible gate omissions.** Any single omitted edge changes just one entry of the bipartite cut matrix. Any set of \(s\) omissions can therefore increase its rank by at most \(s\). Starting from rank \(K=2^{n-2}\) and seeking the maximum \(2K\) necessarily requires \(s\ge K\) omissions. The explicit matching \(F_n\) attains this threshold and hence is optimal.

## Verification

The standalone Python 3 standard-library program `VERIFY.py` builds actual cube cut matrices, removes the specified edges, and performs exact binary elimination on integer bitsets. A second, independently oriented column-elimination routine cross-checks selected matrices. It verifies initial and fully deleted ranks in dimensions \(2,4,6,8\); checks **every** subset of the specified matching for dimensions \(2,4,6\) (respectively \(2,16,65{,}536\) subsets); and checks \(240\) deterministic random subsets in dimension eight. The total is \(65{,}794\) exact subset-rank checks. It also checks unmodified odd dimensions \(1,3,5,7\), which already give full cut rank. All checks passed; the captured output is included as `verification_output.txt`. Run `python3 VERIFY.py`. Finite checks corroborate the explicit all-even-dimension proof; they do not establish the infinite statement by themselves.

## Relationship to prior work

Hein, Eisert, and Briegel [1] establish the standard binary cut-rank rule for graph-state entanglement and the at-most-one-bit change for deleting a single edge. These foundational ingredients are not new. The published *Parity-cut Schmidt spectra of antipodally augmented hypercube graph states* [3] includes the same **unmodified** hypercube checkerboard baseline as its comparison case; that baseline is explicitly not claimed as novel here. Its contribution instead concerns *adding* an entire antipodal perfect matching, not optimal **omission** of a sparse square-fiber matching. Hashizume and collaborators [2] analyze hypercube graph states and their scrambling entanglement, without deriving this particular full-parity minimal gate-erasure construction. The published *Paired omitted-bond cancellation in three-dimensional toroidal cluster states* [4] treats a different periodic product graph and correlated two-bond cancellation rather than optimal restoration. The published *Sharp incidence-matching fault threshold for graph-state entanglement on even-order projective planes* [5] is an exact matching-omission law on different incidence networks; its specific binary incidence-code criterion does not directly imply the present hypercube tensor-product construction. The assessed contribution here is the universal **minimum** omission count and the exact unit-gain law for *every* subset of one explicit matching in every even-dimensional hypercube. Search and inspected-source comparisons do not establish historical uniqueness; equivalent older GF(2) matrix-rank formulations remain a priority risk.

## Limitations

The statement is only about ideal pure qubit graph states and one fixed even/odd Hamming-weight bipartition. It does not give an optimal gate-erasure pattern for arbitrary bipartitions, qudits, noisy preparations, hardware fault models or quantum-walk dynamics. A physical gate failure need not be a controlled and selectable omission; the result does not claim omissions are practically advantageous in a particular device. The strict novelty assessment remains provisional because earlier linear-algebra or coding results could contain an equivalent construction. Independent scientific validation has not been performed.

## References

1. M. Hein, J. Eisert, H. J. Briegel, *Multi-party entanglement in graph states*, arXiv:quant-ph/0307130, first public 2003-07-18, Sections III.2–III.3. https://arxiv.org/abs/quant-ph/0307130
2. T. Hashizume, G. Bentsen, S. Weber, A. J. Daley, *Deterministic Fast Scrambling with Neutral Atom Arrays*, arXiv:2102.13117, first public 2021-02-25. https://arxiv.org/abs/2102.13117
3. *Parity-cut Schmidt spectra of antipodally augmented hypercube graph states*, published open result, especially Proof steps 3–5 and Relationship to prior work. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-parity-cut-schmidt-spectra-of-antipodally-augmented-hypercube-gr--ce26ea2d2639
4. *Paired omitted-bond cancellation in three-dimensional toroidal cluster states*, published open result. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-paired-omitted-bond-cancellation-in-three-dimensional-toroidal-c--06ff2b1986a2
5. *Sharp incidence-matching fault threshold for graph-state entanglement on even-order projective planes*, published open result. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-incidence-matching-fault-threshold-for-graph-state-entangl--0f1e8bff6768
