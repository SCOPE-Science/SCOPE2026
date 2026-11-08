# A single pendant leaf creates a universal three-step transient clock on Boolean cubes

## Finding
For each integer \(d\ge 1\), form the graph \(H_d\) by adjoining one new degree-one vertex to an arbitrary vertex of the ordinary \(d\)-dimensional Boolean cube \(Q_d\). Let \(q=2^f\), where \(f\ge1\), and put an element of \(\mathbb F_q\) at every vertex. At each simultaneous time step each vertex replaces its state by the sum of the states at its graph neighbors, with no self-neighbor term. Write \(B_d\) for this linear map, \(N=2^d\) for the number of original cube vertices, and \(D=N+1\) for the full state-space dimension.

**The complete dynamical classification** is as follows. For every \(d\ge1\),
\[
B_d^5=B_d^3,\qquad B_d^3\ne B_d^2.
\]
Every state becomes periodic after at most three updates, the bound is attained, and the eventual least period is one or two. When \(d\) is odd, the zero-primary Jordan partition consists of a single block of length three, the recurrent subspace has dimension \(R=N-2\), and the fixed subspace has dimension \(F=(N-2)/2\). When \(d\) is even, the zero-primary partition is \((3,2^{N/2-2})\), meaning one block of size three and \(N/2-2\) blocks of size two; the recurrent and fixed subspace dimensions are \(R=2\) and \(F=1\), respectively. Here \(d=1\) is allowed: the recurrent space is zero-dimensional, so there are no primitive two-cycles in that case.

For \(t=0,1,2,3\), define integers \(k_0,k_1,k_2,k_3\) by
\[
(k_0,k_1,k_2,k_3)=
\begin{cases}
(0,1,2,3),&d\ \mathrm{odd},\\
(0,N/2-1,N-2,N-1),&d\ \mathrm{even},
\end{cases}
\]
and put \(h_0=1\), \(h_t=q^{k_t}-q^{k_{t-1}}\) for \(1\le t\le3\). Write \(M_{t,p}\) for the number of labeled initial states with exact first-periodic-entry time \(t\) and eventual least period \(p\). Then **every joint entrance-period population** is
\[
M_{t,1}=q^F h_t,\qquad M_{t,2}=(q^R-q^F)h_t.
\]
In particular, for uniform independent vertex states,
\[
\Pr(T=3)=1-\frac1q
\]
**for every cube dimension**, even though the proportion of initially periodic states is \(q^{-3}\) when \(d\) is odd and \(q^{-(N-1)}\) when \(d\) is even. There are exactly \((q^R-q^F)/2\) distinct primitive two-cycle orbits. The number of periodic fixed states is \(q^F\).

## Assumptions and scope
The graph is a simple unweighted hypercube with one additional pendant vertex; any attachment vertex gives an isomorphic graph. The field has characteristic exactly two; the vertex-update rule uses **open** rather than closed neighborhoods. The first-periodic-entry time is the least \(t\ge0\) for which the state at time \(t\) belongs to a periodic orbit of the map. The least period is determined by actual equality of labeled full-graph state vectors, not a graph automorphism or a shift quotient. All formulas hold for every \(d\ge1\) and every \(q=2^f\) with \(f\ge1\).

## Proof
Let \(A\) be the ordinary \(N\times N\) cube adjacency operator over \(\mathbb F_q\), let \(e\) be the unit vector at the attachment vertex, and write \(u=Ae\). A state of the new graph is \((x,s)\in\mathbb F_q^N\oplus\mathbb F_q\), and the update is
\[
B(x,s)=(Ax+se,\,e^{\mathsf T}x).
\]
The standard coordinate dot product is used throughout; the matrix \(A\) is symmetric, and \(e^{\mathsf T}u=0\) since the original graph has no loops.

**Cube adjacency lemma.** For all \(d\ge1\), \(A^2=(d\bmod2)I\). Its entire Jordan structure is \(N/2\) blocks of length two: at eigenvalue zero if \(d\) is even, and at eigenvalue one if \(d\) is odd. To prove this without a spectral-limit argument, identify the cube vertex space with the group algebra of \((\mathbb Z/2\mathbb Z)^d\). If \(g_i\) is the permutation of flipping bit \(i\), set \(\eta_i=g_i+1\), so \(\eta_i^2=0\). Multiplication by \(A\) is multiplication by \((d\bmod2)1+\sum_i\eta_i\). The invertible algebra substitution \(\eta_1' =\sum_i\eta_i\), \(\eta_j'=\eta_j\) for \(j\ge2\), conjugates multiplication by \(\sum_i\eta_i\) to multiplication by \(\eta_1\); the latter is a direct sum of \(N/2\) two-dimensional square-zero blocks. This proves the assertion, including the rank \(\operatorname{rank} A=N/2\) and, for odd \(d\), \(\operatorname{rank}(A+I)=N/2\).

**Odd dimensions.** We have \(A^2=I\), so \(Au=e\). The vectors \(e,u\) are linearly independent, with \(e^{\mathsf T}e=1\), \(e^{\mathsf T}u=0\), and \(u^{\mathsf T}u=d\bmod2=1\). Thus the cube vertex space splits as \(\operatorname{span}\{e,u\}\oplus W\), where \(W=\{x:e^{\mathsf T}x=u^{\mathsf T}x=0\}\) is invariant under \(A\). Write \(w=(0,1)\) for the new leaf impulse, interpreting \(e,u\) as cube-supported vectors with leaf value zero. Then
\[
Bw=e,\quad Be=u+w,\quad B(u+w)=0.
\]
These are the arrows of one nilpotent Jordan block of size three. On the invariant complementary subspace \(W\), the map is \(A\), satisfying \(A^2=I\). Since the matrix of \(A+I\) on \(\operatorname{span}\{e,u\}\) has rank one, the cube lemma gives \(\operatorname{rank}((A+I)|_W)=N/2-1\). As \((A+I)^2=0\), its rank is half the dimension of \(W\). Thus the recurrent subspace has dimension \(R=N-2\), with exactly \((N-2)/2\) blocks of size two at eigenvalue one and fixed dimension \(F=(N-2)/2\). The zero-primary partition is \((3)\).

**Even dimensions.** We have \(A^2=0\), \(\operatorname{rank}A=N/2\), and \(u=Ae\ne0\). Because \(A\) is symmetric and \(\operatorname{im}A=\ker A\), the identity \(Ae\ne0\) implies \(e\notin\operatorname{im}A\). For any state let \(a=e^{\mathsf T}x\) and \(b=u^{\mathsf T}x\). Direct multiplication gives
\[
B^2(x,s)=(ae+su,\,b+s),\qquad
B^3(x,s)=(au+(b+s)e,\,a),
\]
\[
B^4(x,s)=((b+s)u+ae,\,b+s),\qquad B^5(x,s)=B^3(x,s).
\]
The independent linear forms \(a,b,s\) show that \(\operatorname{rank}B^2=3\) and \(\operatorname{rank}B^3=2\). Moreover, \(\ker B\) consists of states \((x,0)\) such that \(Ax=0\) and \(e^{\mathsf T}x=0\). The last functional is nonzero on \(\ker A\), because otherwise \(e\in(\ker A)^\perp=\operatorname{im}A\); hence \(\operatorname{rank}B=N/2+2\). The image of \(B^3\) is spanned by \((e,0)\) and \((u,1)\), which \(B\) swaps. It is the two-dimensional recurrent subspace, of which the fixed subspace has dimension one. The successive nullities at times zero through three are
\[
0,\quad N/2-1,\quad N-2,\quad N-1.
\]
Taking successive differences establishes exactly one zero-primary block of length three and \(N/2-2\) blocks of length two. In particular this proof includes the boundary \(d=2\), for which there are no size-two zero blocks.

**Exact census.** In both parity cases the state space splits uniquely into its nilpotent and recurrent components. The nilpotent dimension is \(k_3=D-R\), its first-hit kernel filtration satisfies \(\dim\ker(B^t|_{\mathrm{nil}})=k_t\), and the recurrent map has only cycles of length one or two. Thus there are exactly \(h_t\) nilpotent components whose first time at zero is \(t\), independently paired with \(q^F\) fixed recurrent components or with \(q^R-q^F\) genuinely period-two recurrent components. Multiplication gives the formulas for \(M_{t,p}\). Because there is precisely one size-three nilpotent block, the fraction needing three steps is \((q^{k_3}-q^{k_2})/q^{k_3}=1-q^{-1}\), proving sharpness and the universal probability.

## Verification
The attached `verify_ranks.py` computes binary adjacency matrices and their successive exact GF(2) ranks for \(1\le d\le8\), checks \(B^5=B^3\) and fixed-space dimensions, and compares these outputs to the displayed formulas. The independent `verify_states.py` directly simulates all \(131624\) binary labeled initial configurations for \(1\le d\le4\), checks actual exact entry times and least periods, and reproduces every positive class population. The captured outputs are in `verify_ranks_output.txt` and `verify_states_output.txt`. Run both scripts under Python 3 without external libraries. These finite checks corroborate, but do not replace, the all-dimension proof above.

## Relationship to prior work
Wolfram's 1983 account and Martin, Odlyzko and Wolfram's 1984 analysis supply established foundations for cellular automata and algebraic state-transition methods. The latter analyzes translation-invariant additive rules on finite lattice geometries, including variations of boundary conditions, but not the one-leaf Boolean-cube graph or the present Jordan and first-entry census. Brunnet and Chaté (2004) study totalistic, Game-of-Life-like rules on high-dimensional hypercubes, using numerical investigations of macroscopic dynamics; their rule family and unperturbed cube geometry are different. A published modular parity result on **distance-two** Boolean cubes concerns a different adjacency operator and does not imply the one-leaf, distance-one dynamics here. The contributions claimed here are the exact leaf-perturbation structural dichotomy, uniform sharp three-step clock, and all-class count, not the general use of characteristic-two matrix algebra.

## Limitations
The conclusion is specific to characteristic-two fields, open-neighborhood additive updates and a **single** pendant vertex. It does not classify general leaf attachments, weighted graph rules, nonlinear threshold rules, or arbitrary graph perturbations. Finite checker runs establish only their stated ranges, while the proof supplies the infinite family. Historical priority has not been independently verified; an unindexed equivalent result, especially within algebraic graph dynamics, could alter the originality assessment. No independent audit or external proof certification has been performed.

## References
1. S. Wolfram, *Statistical Mechanics of Cellular Automata*, Reviews of Modern Physics **55** (1983), 601–644. First published 1983-07-01. https://doi.org/10.1103/RevModPhys.55.601
2. O. Martin, A. M. Odlyzko, S. Wolfram, *Algebraic Properties of Cellular Automata*, Communications in Mathematical Physics **93** (1984), 219–258. https://doi.org/10.1007/BF01223745
3. L. G. Brunnet, H. Chaté, *Cellular automata on high-dimensional hypercubes*, Physical Review E **69** (2004), 057201. First published 2004-05-18. https://doi.org/10.1103/PhysRevE.69.057201
4. *A mod-four orbit census for parity automata on distance-two Boolean cubes* (2026), published mathematical research note; this studies a different graph and update operator.
