# Four universal Jordan phases under a single directed hypercube input toggle

## Finding

For each integer \(d\ge2\), let \(Q_d\) have vertex set \(\{0,1\}^d\). Fix two **distinct** vertices \(u,v\), put \(m=2^d\), \(r=m/2\), and let \(q\) be any finite power of two. A state is a vector \(x\in\mathbb F_q^m\). Define the synchronous local update
\[
 F(x)_w=\sum_{z:\operatorname{dist}(z,w)=1}x_z+\mathbf1_{\{w=u\}}x_v.
\]
Thus exactly one directed input \(v\to u\) is toggled: an existing input is removed if \(\rho=\operatorname{dist}(u,v)=1\), and a missing input is added if \(\rho\ge2\). All sums are in characteristic two. Let \(J_s(\lambda)\) denote a size-\(s\) Jordan block. The complete similarity classification is
\[
\begin{array}{c|c|c}
 &\rho=1&2\le\rho\le d\\\hline
 d\ \text{even}&J_2(1)\oplus J_2(0)^{\oplus(r-1)}&J_4(0)\oplus J_2(0)^{\oplus(r-2)}\\
 d\ \text{odd}&J_2(0)\oplus J_2(1)^{\oplus(r-1)}&J_4(1)\oplus J_2(1)^{\oplus(r-2)}
\end{array}
\]
(the right-hand column is available for every \(d\ge2\)). These are four distinct temporal regimes, and the answer is otherwise independent of the endpoints and of their Hamming distance.

Write \(C_t\) for the number of initial states whose *first* entry into their eventual periodic orbit occurs no later than time \(t\), including entry at time zero. Write \(P_\ell\) for the number of **periodic states** of primitive period \(\ell\), rather than the number of orbits. The complete census is as follows:

1. If \(d\) is even and \(\rho=1\), then \((C_0,C_1,C_2)=(q^2,q^{r+1},q^m)\), \(P_1=q\), \(P_2=q^2-q\), and there are no other primitive periods. The sharp maximum first-entry time is two.
2. If \(d\) is even and \(\rho\ge2\), then \((C_0,C_1,C_2,C_3,C_4)=(1,q^{r-1},q^{m-2},q^{m-1},q^m)\). Every state reaches the unique zero fixed point, and the sharp extinction time is four.
3. If \(d\) is odd and \(\rho=1\), then \((C_0,C_1,C_2)=(q^{m-2},q^{m-1},q^m)\), \(P_1=q^{r-1}\), \(P_2=q^{m-2}-q^{r-1}\), and no other primitive periods occur. The sharp maximum first-entry time is two.
4. If \(d\) is odd and \(\rho\ge2\), then every state is already periodic, and \(P_1=q^{r-1}\), \(P_2=q^{m-2}-q^{r-1}\), \(P_4=q^m-q^{m-2}\). The global order of \(F\) is exactly four.

Thus, for example, a *one-way* deleted cube bond supports only fixed points and two-cycles, whereas adding a one-way nonedge in odd dimension creates primitive four-cycles without introducing any transients. If the periodic subspace has dimension \(s\), every individual primitive \(\ell\)-orbit has an attraction basin containing exactly \(\ell q^{m-s}\) initial states, where \(s=2,0,m-2,m\) in the four respective cases above. In particular all primitive orbits of the same length have equal basin sizes.

## Assumptions and scope

The original cube is undirected, with both orientations of every ordinary cube edge present as inputs. The perturbation toggles one *ordered* arc, not a full undirected edge. In characteristic two, addition of an already-present input removes that input. Self-loops are excluded, \(u\ne v\). States update simultaneously and deterministically. A periodic configuration is a state satisfying \(F^\ell x=x\) for some positive integer \(\ell\); a first-entry time is the least nonnegative time when the state is periodic. The symbols \(C_t\) count by-entry-time **cumulatively**; exact shells are \(C_0\) and \(C_t-C_{t-1}\). The orbit count for primitive period \(\ell\) is \(P_\ell/\ell\).

## Proof

**Square-zero cube reduction.** Let \(A\) be the open-neighborhood adjacency operator of \(Q_d\), and \(S_i\) the permutation of vertices that flips bit \(i\). Since the \(S_i\) commute and satisfy \(S_i^2=I\), in characteristic two
\[
 A^2=\sum_{i=1}^d S_i^2=(d\bmod2)I=\delta I.
\]
Put \(H=A+\delta I\), so \(H^2=0\). Its rank equals \(r=m/2\): split the cube into two opposite \((d-1)\)-cubes and write
\[
 H=\begin{pmatrix}D&I\\I&D\end{pmatrix},\qquad D=A(Q_{d-1})+\delta I.
\]
Here \(D^2=((d-1)+\delta)I=I\). Consequently \(\ker H\) consists precisely of \((y,Dy)\), has dimension \(r\), and \(\operatorname{rank}H=r\). Every column of \(H\) is nonzero (each vertex has at least two distinct neighbors). Because \(H^2=0\), \(\operatorname{im}H=\ker H\).

**Rank-one arc lemma and two distance classes.** Let \(e_u,e_v\) denote vertex basis vectors and put \(E=e_ue_v^{\mathsf T}\). Since \(u\ne v\), \(E^2=0\). Set \(K=H+E\), \(a=He_u\) and \(b=H^{\mathsf T}e_v\). Both \(a,e_u\) and \(b,e_v\) are linearly independent: for example, \(He_u\ne0\) and \(H^2e_u=0\) show that \(e_u\notin\operatorname{im}H\), while \(a\in\operatorname{im}H\). The transposed argument applies to \(b,e_v\). A standard rank-one row/column augmentation (or elementary row and column operations after choosing complements to the image and row space) therefore gives
\[
 \operatorname{rank}K=\operatorname{rank}H+1=r+1.
\]
The only relevant endpoint scalar is
\[
 \varepsilon=e_v^{\mathsf T}He_u=e_v^{\mathsf T}Ae_u
   =\begin{cases}1,&\rho=1,\\0,&\rho\ge2.\end{cases}
\]
Direct multiplication, using \(H^2=E^2=0\), gives
\[
 K^2=ae_v^{\mathsf T}+e_ub^{\mathsf T},\quad
 K^3=ab^{\mathsf T}+\varepsilon E,\quad
 K^4=\varepsilon K^2.
\]
The independent column pair \((a,e_u)\) and row pair \((e_v^{\mathsf T},b^{\mathsf T})\) show that \(\operatorname{rank}K^2=2\).

If \(\varepsilon=0\), then \(K^3=ab^{\mathsf T}\) has rank one and \(K^4=0\). The rank sequence \(m,r+1,2,1,0\) forces exactly one nilpotent Jordan block of length four, no blocks of length three or one, and \(r-2\) of length two. (Indeed the rank of the third power counts length-four blocks; the rank of the second power then excludes length-three blocks; rank of the first power and total dimension determine the rest.) Thus \(K\sim J_4(0)\oplus J_2(0)^{\oplus(r-2)}\).

If \(\varepsilon=1\), then \(P=K^2\) is an idempotent rank-two projection, since \(K^4=K^2\). Its image is \(\operatorname{span}\{e_u,a\}\). Indeed \(Ke_u=a\) and \(Ka=e_u\), so \(K\) exchanges these two vectors: on \(\operatorname{im}P\) it is a single \(J_2(1)\), as the swap matrix is nontrivially unipotent in characteristic two. On the invariant complement \(\ker P\) we have \(K^2=0\) and \(\operatorname{rank}(K|_{\ker P})=(r+1)-2=r-1\). This space has dimension \(m-2=2(r-1)\), hence it consists of exactly \(r-1\) copies of \(J_2(0)\) and no singleton blocks. Therefore \(K\sim J_2(1)\oplus J_2(0)^{\oplus(r-1)}\).

**Translate to dynamics.** The actual operator is \(F=A+E=K+\delta I\). When \(d\) is even, \(\delta=0\); when odd, \(\delta=1\). Adding \(I\) switches the eigenvalues zero and one but not the Jordan lengths, yielding the four decompositions in the Finding. On a size-two unipotent block over characteristic two, every state returns in at most two steps; on a size-four unipotent block, every state returns in at most four. A nilpotent block of length \(s\) first reaches zero by step \(s\). Consequently the fixed-space dimensions and the Fitting decomposition give exactly the stated \(P_1,P_2,P_4\) and \(C_t\) formulas. More explicitly, for the nonneighbor odd case the dimensions of \(\ker(F-I)\), \(\ker(F^2-I)\), \(\ker(F^4-I)\) are \(r-1,m-2,m\); subtracting nested fixed spaces gives the primitive-period state populations. For the two adjacent-arc cases, the nilpotent component is one direct sum of size-two blocks (or one size-two block), so the cumulative first-entry counts follow from the dimensions of their power kernels. For the even nonneighbor case, \(F\) is nilpotent and its powers have ranks \(m,r+1,2,1,0\), giving the five successive cumulative extinction counts.

Finally, every linear endomorphism of a finite-dimensional space has a Fitting decomposition into periodic and nilpotent parts. The periodic motion is invertible; for a fixed periodic orbit of length \(\ell\), its attraction basin is the disjoint union of \(\ell\) affine copies of the nilpotent component. Each copy has \(q^{m-s}\) states, giving the claimed individual basin formula. This also proves every asserted sharpness (the final successive counts differ strictly whenever a positive-time shell is claimed).

## Verification

Two independent, standalone standard-library Python programs are included. `check_rank.py` constructs the full binary hypercube adjacency matrix, toggles the ordered arc, and computes matrix-power ranks by independent row elimination and multiplication. It verifies \(27\) dimension/distance cases over dimensions \(2\) through \(7\), including the required power identities. `check_dynamics.py` independently enumerates full trajectories and uses recurrence detection to classify first periodic-entry times and primitive periods. It covers every pair of endpoints up to cube symmetry (one representative of each Hamming distance) for \(d=2,3,4\) over \(\mathbb F_2\) and \(d=2,3\) over \(\mathbb F_4\): a total of \(14\) exhaustive parameter checks. The \(\mathbb F_4\) update is realized as two bit planes, which is valid because all interaction coefficients are zero or one. Exact stdout from successful executions is included. These finite checks corroborate, but do not substitute for, the all-dimension proof.

## Relationship to prior work

Ciandrini, Maffi, Motta, Bassetti and Cosentino Lagomarsino (first publicly posted 2008-09-09) describe linear XOR dynamics and its relationship to feedback structure, attractors and basins for random Boolean-network ensembles. Their general framework underlies the choice of invariants, but their paper does not give a universal ordered-arc toggle classification on hypercubes. Batal's edge-perturbation paper treats the **symmetric** closed-neighborhood matrix of an undirected graph and its nullity, not directed rank-one updates, Jordan structure, or temporal basins. Published one-bond-deletion hypercube work studies the **two-sided** perturbation \(e_ue_v^{\mathsf T}+e_ve_u^{\mathsf T}\). It has a different characteristic polynomial, and (depending on parity) three-/six-cycles or four-cycles with one-step transients. The present **one-sided** perturbation has only periods one, two and four and the exact four-regime table above. Neither the all-matrix linearity formalism nor the symmetric-edge special results imply this specific rank-one two-distance, two-parity classification without additional analysis.

## Limitations

The result assumes one ordered-arc toggle, distinct endpoints, complete uniform cube coupling otherwise, synchronous iteration, and fields of characteristic two. It says nothing about multiple arc changes, arbitrary arc weights, asynchronous dynamics, noisy updates, or other characteristics. Novelty comparisons are limited to the cited and searchable literature; unindexed and inaccessible equivalent work may exist. All verification and review described here is internal mathematical checking; no independent audit has been performed.

## References

- L. Ciandrini, C. Maffi, A. Motta, B. Bassetti and M. Cosentino Lagomarsino, “Feedback topology and XOR-dynamics in Boolean networks with varying input structure,” arXiv:0809.1526 (first posted 2008-09-09), https://arxiv.org/abs/0809.1526 .
- A. Batal, “Effects of edge addition or removal on the nullity of a graph,” arXiv:2108.03059 (first posted 2021-08-06), https://arxiv.org/html/2108.03059v2 .
- “A missing-edge parity transition in hypercube XOR dynamics,” published mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-missing-edge-parity-transition-in-hypercube-xor-dynamics--0ddebf65b6fe .
