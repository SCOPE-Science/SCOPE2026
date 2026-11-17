# A modulo-three Jordan resonance and exact wave clocks on triangular Johnson graphs

## Finding

Let \(n\ge3\), \(q=3^f\) for an integer \(f\ge1\), and \(N=\binom n2\). Write \(J(n,2)=L(K_n)\) for the graph whose \(N\) vertices are the pairs of distinct elements of \(\{1,\ldots,n\}\), two pairs being adjacent if they intersect in one element. Let \(A\) be its ordinary loopless adjacency matrix over \(\mathbb F_q\). Consider the reversible two-time-level wave
\[
T_n(u,v)=(Au-v,u),\qquad (u,v)\in\mathbb F_q^N\times\mathbb F_q^N.
\]
Every state is periodic already at time zero. The exact order of this permutation is
\[
\boxed{L_n=\begin{cases}
9,&n=3,\\
18,&n\ge6\text{ and }n\equiv0\pmod3,\\
36,&n\equiv1,2\pmod3.
\end{cases}}
\]
The order is attained by an individual state in every case.

Here is an exact formula for the complete periodic-point census at **every positive integer** \(t\). Put \(g(t)=3^{\nu_3(t)}\), \(c_j(t)=\mathbf1_{j\mid t}\), and \(E_n(t)=\dim_{\mathbb F_q}\ker(T_n^t-I)\). Then
\[
\boxed{E_n(t)=\begin{cases}
\min(4,g)+(n-2)\min(2,g)+(N-n)c_2(t)\min(2,g),&n\equiv0\pmod3,\\
2(n-1)c_4(t)+c_2(t)\bigl[\min(4,g)+(N-n-1)\min(2,g)\bigr],&n\equiv1\pmod3,\\
2c_4(t)+c_2(t)\bigl[(n-1)\min(4,g)+(N-2n+1)\min(2,g)\bigr],&n\equiv2\pmod3.
\end{cases}}
\]
The argument \(t\) in \(g\) is suppressed on the right. In particular,
\[
\#\operatorname{Fix}(T_n^t)=q^{E_n(t)}.
\]
For any positive divisor \(d\mid L_n\), the exact number of labelled states of *least* temporal period \(d\) is
\[
P_n(d)=\sum_{e\mid d}\mu(d/e)q^{E_n(e)},
\qquad\text{and the number of distinct temporal cycles is}\quad P_n(d)/d.
\]
These formulas vanish at all unlisted periods and are strictly positive at exactly the following periods:
\[
\begin{array}{c|l}
n=3&1,3,9\\
n\equiv0\pmod3,\ n\ge6&1,2,3,6,9,18\\
n\equiv1,2\pmod3&1,2,4,6,12,18,36.
\end{array}
\]
For example, on the smallest triangular graph \(J(3,2)=K_3\), the respective populations at periods \(1,3,9\) are \(9,234,486\) when \(q=3\). Their sum is the complete \(729\)-state space.

## Assumptions and scope

The graph is simple, undirected and labelled: pairs are not identified under graph symmetries, and both time slices are arbitrary independent vectors. All calculations are in characteristic **three**, over any finite extension \(\mathbb F_{3^f}\). The minus sign in the update is essential; ordinary first-order adjacency iteration and characteristic-two previous-state addition are different systems. Period means the least positive temporal return time of the ordered pair \((u,v)\), not the time for the first coordinate alone to return. The convention \(n\ge3\) ensures a full-rank unsigned incidence matrix. The indicated \(\nu_3\) is the exponent of three in a positive integer.

## Proof

**1. Incidence factorization in characteristic three.** Index columns by pairs \(\{i,j\}\), and let \(B\) be the unsigned vertex-edge incidence matrix of \(K_n\) over \(\mathbb F_q\): its column for \(\{i,j\}\) has ones at coordinates \(i,j\). Thus
\[
B^\mathsf{T}B=A+2I,\qquad C:=B^\mathsf{T}B,
\qquad A=C-2I=C+I \quad\text{in characteristic three}.
\]
The rows of \(B\) are linearly independent: a linear dependence would give \(z_i+z_j=0\) for every distinct \(i,j\); applying this on a triangle gives \(2z_i=0\), hence \(z_i=0\) for every \(i\), since two is invertible. Consequently \(\operatorname{rank} B=n\). The vertex Gram matrix is
\[
BB^\mathsf T=(n-2)I+J,
\]
where \(J\) is the all-ones \(n\)-square matrix, with \(J^2=nJ\). As \(B\) is surjective and \(B^\mathsf T\) is injective, for each positive integer \(r\),
\[
\operatorname{rank}C^r=\operatorname{rank}(BB^\mathsf T)^{r-1}.
\]
(The case \(r=1\) reads \(\operatorname{rank}C=n\); in general \(C^r=B^\mathsf T(BB^\mathsf T)^{r-1}B\).)

**2. The three exact modular Jordan structures.** Write \(J_s(\lambda)\) for one Jordan block of length \(s\) at eigenvalue \(\lambda\), with multiplicities interpreted as direct sums. All eigenvalues below are elements of \(\mathbb F_3\).

If \(n\equiv0\pmod3\), then \(BB^\mathsf T=I+J\) and \(J^2=0\) with rank one. The matrix \(C\) is the direct sum of the invertible restriction \(J_2(1)\oplus J_1(1)^{\oplus(n-2)}\) and a zero block of dimension \(N-n\). Translating its eigenvalues by one gives
\[
A\simeq J_2(2)\oplus J_1(2)^{\oplus(n-2)}\oplus J_1(1)^{\oplus(N-n)}.
\]

If \(n\equiv1\pmod3\), the vertex Gram matrix is \(2I+J\), where \(J^2=J\). Hence it has eigenvalues two with multiplicity \(n-1\) and zero with multiplicity one. Now \(\operatorname{rank} C=n\), \(\operatorname{rank} C^2=n-1\), and \(\operatorname{rank} C^3=\operatorname{rank} C^2\), excluding larger zero Jordan blocks. Thus the zero-primary part of \(C\) has one block of size two and \(N-n-1\) singleton blocks. Shifting eigenvalues yields
\[
A\simeq J_2(1)\oplus J_1(1)^{\oplus(N-n-1)}\oplus J_1(0)^{\oplus(n-1)}.
\]

If \(n\equiv2\pmod3\), the vertex Gram matrix is \(J\) and \(J^2=2J\). It has eigenvalue two once and zero \(n-1\) times. Thus \(\operatorname{rank}C=n\), \(\operatorname{rank} C^2=1\), with \(\operatorname{rank}C^3=\operatorname{rank}C^2\); consequently there are \(n-1\) length-two zero-Jordan blocks and \(N-2n+1\) length-one zero blocks. Therefore
\[
A\simeq J_2(1)^{\oplus(n-1)}\oplus J_1(1)^{\oplus(N-2n+1)}\oplus J_1(0).
\]
All multiplicities are nonnegative for their stipulated ranges: the smallest cases are \(n=3\), \(n=4\), and \(n=5\), respectively. These are explicit modular decompositions, not reductions of the usual real adjacency eigenvalue formula, which loses Jordan information on resonance.

**3. Exact temporal primary blocks.** Clearly
\[
T_n^{-1}(u,v)=(v,Av-u),
\]
so the map is a permutation on a finite set. An adjacency Jordan block \(J_s(\lambda)\), for \(s=1,2\) in this theorem, induces a \(2s\)-dimensional temporal block with characteristic polynomial \((X^2-\lambda X+1)^s\). For \(\lambda=2\), this is \((X-1)^{2s}\); the fixed eigenspace has dimension \(\dim\ker(J_s(2)-2I)=1\), so the temporal block is the *single* block \(J_{2s}(1)\). For \(\lambda=1\), it is likewise the single block \(J_{2s}(-1)\), since \(X^2-X+1=(X+1)^2\) in characteristic three. Finally \(\lambda=0\), present only with \(s=1\), gives \(X^2+1\), with a two-dimensional block of exact order four.

A block \(J_r(1)\) contributes \(\min(r,3^{\nu_3(t)})\) fixed dimensions at time \(t\); a block \(J_r(-1)\) contributes the same only if \(2\mid t\); and a two-dimensional zero-adjacency temporal block contributes exactly two dimensions when \(4\mid t\). These facts follow from the Frobenius identity \((I+H)^{3^a}=I+H^{3^a}\) for nilpotent \(H\), together with the order of the scalar eigenvalue. Substituting the three spatial decompositions of step two proves every displayed formula for \(E_n(t)\). Field extension preserves all the kernel dimensions.

**4. Sharp temporal orders and all least periods.** In the divisible-by-three case, the length-two adjacency block at eigenvalue two yields a temporal \(J_4(1)\) of exact order nine. If \(n=3\), the other block is \(J_2(1)\), so the exact global order is nine. If \(n\ge6\), at least one \(J_2(-1)\) block is also present and has order six, giving least common multiple eighteen. In each of the other two residues, there is at least one \(J_4(-1)\) of order eighteen and one order-four zero-adjacency temporal block, giving exactly 36. A direct-sum state with nonzero components of maximal orders attains each least common multiple.

The possible primitive periods of a direct sum are least common multiples of the primitive periods of its primary blocks. A \(J_4(1)\) admits periods \(1,3,9\); a \(J_2(1)\) admits \(1,3\); a \(J_4(-1)\) admits \(1,2,6,18\); a \(J_2(-1)\) admits \(1,2,6\); and a zero-adjacency temporal block admits \(1,4\). Selecting components gives precisely the three lists in the theorem, and supplies a state for each listed period. Finally the fixed-set identity \(q^{E_n(t)}=\sum_{d\mid t}P_n(d)\) and Möbius inversion yield all primitive populations and their cycle counts. This completes the unrestricted proof. \(\square\)

## Verification

The standalone `verify_johnson.py` constructs the graph from pair intersections and its full \(2N\)-dimensional two-time-step transition matrix. With exact integer reduction modulo three, it recomputes the fixed-space nullities for **every time index through the full global period**, and checks the sharp matrix order, at each \(n=3,4,\ldots,10\). The script uses Python 3 with NumPy; running `OPENBLAS_NUM_THREADS=1 python verify_johnson.py` reproduces `matrix_output.txt`.

The independent standard-library `verify_direct.py` implements neighbor-by-neighbor synchronous evolution without matrix powers. It exhausts all \(3^6=729\) initial two-time-level states for \(n=3\), obtaining the exact primitive populations \(9,234,486\). It additionally follows 120 deterministically seeded independent initial states at each \(n=4,\ldots,8\); all return by the stated global period. Running `python verify_direct.py` reproduces `direct_output.txt`.

The finite tests corroborate the unrestricted theorem; they are **not** the reason the theorem holds for every \(n\). The all-length conclusion follows from the incidence factorization, rank computations, and explicit temporal block structure in the proof.

## Relationship to prior work

Macfarlane (2004) develops matrix equivalents for reversible *one-dimensional binary* second-order automata and studies temporal weight statistics, not the triangular Johnson graph or characteristic-three orbit census. Vlasov (2013), especially its general second-order update construction and ternary-state discussion, establishes that such reversible constructions are already standard; the present result does not claim the construction, the fact of reversibility, or the Johnson graph's ordinary eigenvalues as new. Standard Johnson-graph references identify \(J(n,2)\) with the triangular line graph of a clique.

Previously published exact reversible-wave results for complete bipartite graphs in characteristic three and for Hamming graphs of alphabet divisible by three use related modular methods, but their graph modules are not the edge-incidence Gram module of \(K_n\) treated here. A result for arbitrary strongly regular graphs in characteristic two likewise cannot imply a characteristic-three Jordan decomposition. The new assertion is the explicit **all-size modulo-three resonance, sharp 9/18/36 order law, and fixed-space and least-period formulas** for this particular natural graph family; a general algorithm for finite matrix powers is not equivalent to these formulas.

## Limitations

The theorem is restricted to the specified reversible neighbor-sum rule, complete-graph line graphs, and finite fields of characteristic three. It does not address unrelated nonlinear updates, different field characteristics, graph-automorphism orbit quotients, or attraction basins (which are absent here because the map is invertible). The literature check is finite, and unindexed equivalent modular Johnson-scheme treatments cannot be excluded. There has been no independent mathematical audit. A reading of Macfarlane's available document and Vlasov's full preprint supports the comparison; historical coverage beyond those sources remains a priority risk.

## References

1. A. J. Macfarlane, *Linear reversible second-order cellular automata and their first-order matrix equivalents*, Journal of Physics A: Mathematical and General **37** (2004), 10791–10814, published **2004-10-28**. DOI: 10.1088/0305-4470/37/45/006. https://doi.org/10.1088/0305-4470/37/45/006.
2. A. Yu. Vlasov, *On generalization of reversible second-order cellular automata*, initial arXiv version **2013-11-18**. https://arxiv.org/abs/1311.4297.
3. E. W. Weisstein, *Triangular Graph*, MathWorld, https://mathworld.wolfram.com/TriangularGraph.html; definition of the triangular Johnson graph and the clique line graph.
4. *Mod-three resonance trichotomy for reversible waves on complete bipartite graphs*, publicly available mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-mod-three-resonance-trichotomy-for-reversible-waves-on-complete--167b2c8980f2.
5. *A three-class wave clock and exact orbit census for ternary-modular Hamming graphs*, publicly available mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-three-class-wave-clock-and-exact-orbit-census-for-ternary-modu--13302e527b48.
6. *Three universal wave periods and spectrally invisible orbit counts on strongly regular graphs*, publicly available mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-three-universal-wave-periods-and-spectrally-invisible-orbit-coun--6be21916ed4f.
