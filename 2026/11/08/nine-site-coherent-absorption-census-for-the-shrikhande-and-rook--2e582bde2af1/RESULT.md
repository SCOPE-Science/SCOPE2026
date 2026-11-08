# Nine-site coherent-absorption census for the Shrikhande and rook networks

## Finding
Consider a one-particle continuous-time quantum walk on either the Shrikhande graph \(S\) or the \(4\times4\) rook graph \(R\). Both have \(16\) vertices and strongly regular parameters \((16,6,2,2)\). For any nonempty absorber set \(T\) with an arbitrary strictly positive rate \(\gamma_v\) at every \(v\in T\), take the no-jump Hamiltonian
\[
H_T=J A-i\sum_{v\in T}\gamma_v|v\rangle\langle v|,\qquad J\in\mathbb R\setminus\{0\}.
\]
Complete eventual absorption means \(\lim_{t\to\infty}\|e^{-itH_T}\psi\|^2=0\) for **every** initial vector \(\psi\).

The minimum size of \(T\) allowing complete eventual absorption is exactly \(9\) on both graphs. Of the \(\binom{16}{9}=11{,}440\) nine-vertex absorber sets, exactly \(3{,}936\) work on \(R\), whereas exactly \(7{,}200\) work on \(S\). The complete census, grouped by the dimension \(D_T\) of the nondecaying dark subspace, is

| Graph | \(D_T=0\) | \(D_T=1\) | \(D_T=2\) | Total |
|---|---:|---:|---:|---:|
| \(R\) | 3936 | 6736 | 768 | 11440 |
| \(S\) | 7200 | 4144 | 96 | 11440 |

For an initial maximally mixed state, eventual capture is exactly \(1-D_T/16\), so the three columns give capture probabilities \(1\), \(15/16\), and \(7/8\), independently of \(J\) and the positive site-dependent loss strengths. The fraction of optimal nine-site placements is respectively \(246/715\) and \(90/143\). These are labelled subsets of the fixed sixteen-vertex graphs, not isomorphism classes of subsets.

There is also a structural constraint on this comparison: for any two strongly regular graphs with equal parameters, *matched induced absorber subgraphs* have unitarily equivalent one-particle no-jump Hamiltonians when the hopping and the individual absorber strengths are matched. Thus the distinction above is a difference in the **distribution** of optimal placement patterns, not a claim that the same induced absorber pattern has different dynamics.

## Assumptions and scope
Write vertices as \((a,b)\in\mathbb Z_4^2\). For the rook graph, distinct vertices are adjacent if they share a coordinate. For the Shrikhande graph, vertices are adjacent if their coordinate difference modulo \(4\) is in \(\{\pm(1,0),\pm(0,1),\pm(1,1)\}\). These definitions fix the counted labelled subsets; all counts are invariant under relabelling. The site Hilbert space is \(\mathbb C^{16}\); there is one mobile excitation, coherent uniform adjacency hopping, and no dephasing or additional potentials. Every included detector has \(\gamma_v>0\). The assertion concerns eventual, not finite-time, capture and does not say that every initial state has the same absorption time.

## Proof
**Spectral reduction.** Both adjacency matrices satisfy \(A^2=4I+2\mathbf1\mathbf1^{\mathsf T}\), a consequence of degree \(6\) and exactly \(2\) common neighbours of each pair of distinct vertices. Their adjacency eigenspaces have eigenvalues and multiplicities \((6,1)\), \((2,6)\), and \((-2,9)\). With \(E_\lambda\) the orthogonal spectral projector, their explicit formulas are
\[
E_6=\frac{\mathbf1\mathbf1^{\mathsf T}}{16},\quad
E_2=\frac{A+2I}{4}-\frac{\mathbf1\mathbf1^{\mathsf T}}8,\quad
E_{-2}=\frac{2I-A}{4}+\frac{\mathbf1\mathbf1^{\mathsf T}}{16}.
\]
Let \(T\) be any absorber set. The dark modes with energy \(J\lambda\) are exactly the eigenvectors in \(\operatorname{ran}(E_\lambda)\) whose coordinates vanish on \(T\). Their dimension is \(m_\lambda-\operatorname{rank}(E_\lambda[T,T])\), since the latter principal matrix is the Gram matrix of the coordinate restrictions. Consequently
\[
D_T=16-\sum_{\lambda\in\{6,2,-2\}}\operatorname{rank}(E_\lambda[T,T]).
\]
If \(D_T>0\), such a dark eigenvector evolves with constant norm. Conversely, for an eigenpair \(H_Tv=zv\),
\[
\operatorname{Im}z=-\frac{\sum_{x\in T}\gamma_x|v_x|^2}{\|v\|^2}\le0.
\]
Equality would make \(v\) an adjacency eigenvector vanishing on every absorber. If \(D_T=0\), all eigenvalues have strictly negative imaginary part and the finite-dimensional matrix exponential decays for all initial states, including in the presence of Jordan blocks. Thus \(D_T=0\) is necessary and sufficient for complete absorption for all positive rate assignments.

**The sharp lower bound.** The \(-2\) eigenspace has dimension \(9\); fewer than nine monitored coordinates cannot be injective on this eigenspace. Therefore at least nine absorbers are necessary on either graph.

**Exact nine-site reduction.** For \(|T|=9\), write \(A_T=A[T,T]\), \(I_9\) for the identity and \(\mathbf J_9\) for the all-ones matrix. Define integral positive-semidefinite matrices
\[
B_T=2A_T+4I_9-\mathbf J_9=8E_2[T,T],\qquad
C_T=8I_9-4A_T+\mathbf J_9=16E_{-2}[T,T].
\]
Since \(\operatorname{rank}E_6[T,T]=1\),
\[
D_T=15-\operatorname{rank}B_T-\operatorname{rank}C_T.
\]
The complete **joint exact-rank census** is

| \((\operatorname{rank}B_T,\operatorname{rank}C_T)\) | Rook | Shrikhande |
|---|---:|---:|
| \((5,8)\) | 0 | 48 |
| \((5,9)\) | 160 | 112 |
| \((6,7)\) | 768 | 48 |
| \((6,8)\) | 6576 | 4032 |
| \((6,9)\) | 3936 | 7200 |

This table exhausts all \(11{,}440\) nine-element subsets of the sixteen specified vertices for each graph. It is certified by the two independent standalone enumerators in the Verification section, which perform exact integer elimination and a separate Krylov-rank calculation. The \((6,9)\) row supplies constructive existence at the nine-site lower bound. For example, the integer vertex masks \(1915\) on \(R\) and \(4479\) on \(S\), with bit \(4a+b\) representing vertex \((a,b)\), are full-capture configurations; their ranks can also be checked directly using the displayed matrices.

**Matched-pattern restriction.** In any strongly regular graph, every spectral projector is a linear combination of \(I,A,\mathbf1\mathbf1^{\mathsf T}\), with coefficients determined by the parameters. If two graphs have equal parameters and their labelled induced graphs on \(T\) and \(T'\) agree, then for each eigenvalue \(\lambda\) the Gram matrices \(E_\lambda[T,T]\) and \(E'_\lambda[T',T']\) agree. A Gram-preserving isometry between the spans of \(\{E_\lambda e_t:t\in T\}\) extends to a unitary between their full equal-dimensional eigenspaces. Taking the orthogonal sum over \(\lambda\) yields a unitary \(U\) with \(UAU^*=A'\) and \(Ue_t=e'_{t'}\) for every labelled matched absorber. Hence it conjugates every corresponding \(H_T\), proving the stated restriction on distinguishability.

## Verification
Two mutually independent implementations enumerate the same \(\binom{16}{9}\) sets for each graph.

1. `check_exact.cpp` constructs both graphs from their defining coordinates, checks every entry of \(A^2=4I+2\mathbf1\mathbf1^{\mathsf T}\), constructs \(B_T,C_T\), and computes their **exact rational ranks** by fraction-free symmetric Gaussian elimination. It checks integer divisibility at every elimination step using signed 128-bit intermediate arithmetic and asserts each row of the joint rank table. Run `g++ -O2 -std=c++17 check_exact.cpp -o check_exact && ./check_exact`; expected final line: `EXACT_RANKS_OK`.
2. `check_krylov.cpp` instead computes the rank of the physical bright Krylov matrix with columns \(e_t,Ae_t,A^2e_t\) for all absorbers \(t\), over two prime fields. Because these integral columns have Euclidean norms at most \(\sqrt{96}<10\), Hadamard's inequality bounds the absolute determinant of any square minor by \(10^{16}\). The product of the two distinct primes \(1000000007\) and \(1000000009\) exceeds \(10^{18}\). Thus every nonzero integer minor survives in at least one field, and the larger of the two modular ranks equals the rational rank. Run `g++ -O2 -std=c++17 check_krylov.cpp -o check_krylov && ./check_krylov`; expected final line: `KRYLOV_OK cases=22880 primes=1000000007,1000000009`.

The methods independently agree on all dark-dimension multiplicities. They use different matrices and elimination schemes; neither relies on floating-point thresholds. The finite census is exhaustive because the loop examines every sixteen-bit mask with exactly nine bits set. It is not an extrapolation from a sample.

## Relationship to prior work
Agliari, Mülken and Blumen [1] study local loss and quantum trapping, including nonzero dark-mode survival, on cycles. Gamble and collaborators [2] derive the three-dimensional adjacency algebra and single-particle continuous-time walk limitations for strongly regular graphs. Rudinger and collaborators [3] analyze different quantum-walk graph-isomorphism certificates and specifically report that their single-particle discrete-time certificates did not distinguish the pair with parameters \((16,6,2,2)\). Godsil and collaborators [4] analyze characteristic polynomials and state transfer under a **two-vertex** edge/loop perturbation of strongly regular graphs. Wananiyakul, Steuding and Tongsomporn [5] distinguish the same Shrikhande/rook pair using a generalized adjacency-matrix polynomial, but do not study local absorption or optimal detector placements in their accessible Section 4. These are substantial conceptual predecessors and explain the spectral reduction, but do not state the present complete nine-detector absorption census or its unequal counts. General star-set and observability language can express the rank criterion; that equivalence is not itself claimed as new. The distinguishing invariant is the full distribution of *minimal-size absorbing placements* across this natural cospectral pair, at the sharp multiplicity-imposed sensor threshold.

## Limitations
This is an exact finite, sixteen-site classification, not an asymptotic family result or a phase-transition claim. The tables count labelled nine-site subsets rather than graph isomorphism orbits. They require strict positivity at all selected sites and identical adjacency hopping; zero rates, coherently driven controls on unmonitored vertices, multi-particle interactions and dephasing are not covered. Matched induced absorber subgraphs remain dynamically indistinguishable as proved, so no individual placement comparison with the same induced geometry is asserted to distinguish the graphs. A pre-existing unindexed star-complement enumeration or specialized observability census could affect historical priority; independent literature audit has not been performed.

## References
[1] E. Agliari, O. Mülken and A. Blumen, *Continuous-Time Quantum Walks and Trapping*, first public 2009-03-19, https://arxiv.org/abs/0903.3288.

[2] J. K. Gamble et al., *Two-particle quantum walks applied to the graph isomorphism problem*, first public 2010-02-16, https://arxiv.org/abs/1002.3003.

[3] K. Rudinger et al., *Comparing algorithms for graph isomorphism using discrete- and continuous-time quantum random walks*, first public 2012-07-19, https://arxiv.org/abs/1207.4535.

[4] C. Godsil, K. Guo, M. Kempton and G. Lippner, *State transfer in strongly regular graphs with an edge perturbation*, first public 2017-10-05, https://arxiv.org/abs/1710.02181.

[5] S. Wananiyakul, J. Steuding and J. Tongsomporn, *How to Distinguish Cospectral Graphs*, published 2022-12-16, https://doi.org/10.3390/math10244802. Section 4 available through indexed text; direct complete-page retrieval was rate-limited.
