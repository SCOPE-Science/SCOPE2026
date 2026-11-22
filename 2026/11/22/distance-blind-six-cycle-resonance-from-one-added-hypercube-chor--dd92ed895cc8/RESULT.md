# Distance-blind six-cycle resonance from one added hypercube chord

## Finding

Let \(d\ge3\), let \(Q_d\) be the graph on binary \(d\)-words joined when they differ in one coordinate, and choose any nonadjacent distinct vertices \(u,v\), so their Hamming distance \(r\) satisfies \(2\le r\le d\). Add the one edge \(uv\). On the resulting graph, evolve configurations over any finite field \(\mathbb F_q\) of characteristic two by **synchronous open-neighbor sum**:
\[
 (F x)_w=\sum_{z\sim w}x_z\qquad(\text{in }\mathbb F_q).
\]
Put \(N=2^d\). The complete linear dynamical classification, including exact primitive-orbit and transient populations, is independent of \(r\). In particular, it does not detect whether the inserted chord makes a triangle (\(r=2\)) or preserves bipartiteness (odd \(r\)). This is similarity of transition operators, not merely equality of selected counts.

**Odd \(d\).** The map is invertible, has order exactly six, and every configuration is periodic at time zero. Its invariant primary decomposition has a four-dimensional factor with minimal polynomial \((X^2+X+1)^2\) and \(N/2-2\) two-dimensional factors with polynomial \((X+1)^2\). These are elementary divisors over \(\mathbb F_2\); the description remains a decomposition by the stated polynomials over every characteristic-two extension field. The numbers of points of **least** periods \(1,2,3,6\), respectively, are
\[
\begin{aligned}
 P_1&=q^{N/2-2},\\
 P_2&=q^{N-4}-q^{N/2-2},\\
 P_3&=q^{N/2}-q^{N/2-2},\\
 P_6&=q^N-q^{N-4}-q^{N/2}+q^{N/2-2}.
\end{aligned}
\]
Each primitive orbit count is \(P_j/j\).

**Even \(d\ge4\).** The map has one size-two block at eigenvalue one, two size-three nilpotent blocks and \(N/2-4\) size-two nilpotent blocks. Consequently there are exactly \(q^2\) recurrent configurations: \(q\) fixed points and \((q^2-q)/2\) primitive two-cycles. Every configuration is periodic by update three, and this bound is attained. The numbers periodic by updates \(t=0,1,2,3\) are exactly
\[
 q^2,\quad q^{N/2},\quad q^{N-2},\quad q^N.
\]
The corresponding first-entry shell counts are the successive differences. Under the uniform distribution, the probability of needing the third update is exactly \(1-q^{-2}\).

## Assumptions and scope

The field size is an arbitrary power \(q=2^s\) with \(s\ge1\); the graph is simple, undirected and loopless, and its only modification is the addition of one edge between previously nonadjacent vertices. A period means least temporal period of the entire labelled configuration. First periodic entry time is the least \(t\ge0\) for which \(F^t(x)\) belongs to a temporal cycle. The cases \(d=1\) (no nonedge) and \(d=2\) (degenerate equal neighbor columns) are intentionally excluded.

## Proof

All vector spaces and operations below are over \(\mathbb F_q\). Let \(A\) be the ordinary cube adjacency operator, let \(e_u,e_v\) be unit vectors, and set
\[
 S=e_ue_v^{\mathsf T}+e_ve_u^{\mathsf T},\qquad B=A+S.
\]
Two-step walks in \(Q_d\) that toggle distinct coordinates cancel in pairs; toggling the same coordinate contributes \(d\) copies of the identity. Hence \(A^2=(d\bmod2)I\). Let \(w=Ae_u\) and \(z=Ae_v\). The four vectors \(e_u,e_v,w,z\) are linearly independent: \(w,z\) vanish at \(u,v\) since the selected vertices are nonadjacent, and \(w,z\) are different nonzero neighborhood vectors for \(d\ge3\). Write \(W=\operatorname{span}\{e_u,e_v,w,z\}\). Since \(Se_u=e_v\), \(Se_v=e_u\), and \(Sw=Sz=0\), direct multiplication gives
\[
 B^2=(d\bmod2)I+AS+SA+e_ue_u^{\mathsf T}+e_ve_v^{\mathsf T}.
\]
The rank of the last three terms is exactly four. Indeed, with \(a=x_u\), \(b=x_v\), \(c=(Ax)_u\), \(e=(Ax)_v\), their value on \(x\) is
\[
 (a+e)e_u+(b+c)e_v+bw+az.
\]
The four coefficient functionals are independent because their representing vectors \(e_u,e_v,w,z\) are independent; the displayed coefficient transformation is nonsingular.

We also require a rank lemma. For \(\delta=d\bmod2\), put \(C=A+\delta I\). Then \(C^2=0\) and \(\operatorname{rank}C=N/2\). To see the rank, divide the cube by its first coordinate. In this two-block representation, \(C\) has blocks \(\bigl(\begin{smallmatrix}R&I\\I&R\end{smallmatrix}\bigr)\) with \(R^2=I\), because the remaining \(d-1\) flips and the scalar \(\delta I\) sum to a matrix squaring to the identity. Therefore the image and kernel both have dimension \(N/2\) and coincide. Furthermore \(Ce_u,Ce_v\) are independent, implying \(\operatorname{span}\{e_u,e_v\}\cap\operatorname{im}C=0\). Finally the restriction of the coordinate projection \(\ker C\to\mathbb F_q^2\), \(x\mapsto(x_u,x_v)\), is surjective: a neighbor of \(u\) not adjacent to \(v\), and vice versa, supply the two unit coordinate patterns through vectors of the form \(Ce_p\). Such exclusive neighbors exist for every \(d\ge3\) and \(2\le r\le d\). Thus \(C\) maps \(\{x:x_u=x_v=0\}\) onto its entire image. Since \(B+\delta I=C+S\), its image contains \(\operatorname{im}C\) and projects onto two new independent directions modulo \(\operatorname{im}C\). Hence
\[
 \operatorname{rank}(B+\delta I)=N/2+2.\tag{1}
\]

For **even** \(d\), we have \(A^2=0\), so \(B^2\) has rank four. On \(W\), the action is
\[
 Be_u=e_v+w,\quad Be_v=e_u+z,\quad Bw=Bz=0.
\]
Writing \(p=e_u+z\) and \(h=e_v+w\), one obtains \(\operatorname{im}B^3=\operatorname{span}\{p,h\}\), and \(Bp=h\), \(Bh=p\). This image has dimension two, and \(B^5=B^3\), whereas \(B^4\ne B^3\). By (1), the ranks of powers at exponents \(0,1,2,3\) are \(N,N/2+2,4,2\); thereafter the rank remains two. The invertible part is a two-dimensional involution with one size-two Jordan block at eigenvalue one. The nilpotent part has dimension \(N-2\), with two size-three blocks and \(N/2-4\) size-two blocks, as the successive rank losses show. Counting the kernel of the nilpotent part at times \(0,1,2,3\) gives dimensions \(0,N/2-2,N-4,N-2\), proving the cumulative and primitive-period formulas.

For **odd** \(d\), \(A^2=I\); therefore \(B^2+I\) has image \(W\) and rank four. On \(W\),
\[
 Be_u=e_v+w,\quad Be_v=e_u+z,\quad Bw=e_u,\quad Bz=e_v.
\]
The map \(B^2+I\) is invertible on \(W\), so \(\mathbb F_q^N=W\oplus\ker(B^2+I)\). In the ordered pairs \((e_u,z)\) and \((e_v,w)\), the operator \(B\) exchanges the two pairs through the same matrix \(\bigl(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\bigr)\), whose cube is the identity in characteristic two. Thus \(B^6=I\) on \(W\), but \(B^3\ne I\); the four-dimensional factor has characteristic and minimal polynomial \((X^2+X+1)^2\). On the complementary kernel, \(B^2=I\). Equation (1) with \(\delta=1\) gives a fixed subspace of dimension \(N/2-2\), exactly half the dimension of this complement; hence it consists of \(N/2-2\) blocks of size two at eigenvalue one. It follows that the fixed-subspace dimensions of \(B^t\) at \(t=1,2,3,6\) are \(N/2-2,N-4,N/2,N\). Taking \(q\) to those powers and applying period-divisor subtraction proves the four exact formulas. All assertions hold for any added nonedge and any finite characteristic-two field.

## Verification

The standalone programs `check_chord.py` and `check_field4.py` contain complete, dependency-free finite cross-checks. Execute `python3 check_chord.py` and `python3 check_field4.py` in a directory containing both programs. `check_chord.py` checks independently constructed bit-packed matrix ranks and power identities for every distance in dimensions three through seven and exhaustively evolves all binary states for dimensions three and four. `check_field4.py` exhaustively evolves all \(4^8\) configurations for both possible chord distances in dimension three using the additive \(\mathbb F_2^2\) representation of \(\mathbb F_4\). Both programs were executed successfully. Finite checks support but do not replace the general proof.

## Relationship to prior work

Finite-field linear cellular automata are a well-established subject; the structural algebraic framework is present, for example, in Ceccherini-Silberstein and Coornaert (2009) and Rowland and Yassawi (2012). Batal (2021) studies how *closed-neighborhood Lights Out nullity* changes under edge insertion/removal; that quantity does not determine the powers or primitive orbit statistics of the **open-neighbor synchronous evolution** here. Published hypercube parity studies of removing an existing bond, puncturing vertices, and adding self-feedback address different graph changes. Their parity-dependent outcomes do not imply this distance-blind similarity classification for insertion of a previously absent bond. References below identify comparable background and closest variants, not claims of external independent certification.

## Limitations

The proof requires characteristic two and one added nonedge. The claim does not cover edge deletion, self-loops, multiple added chords, or dimensions below three. The algebraic proof is complete, but external independent validation has not been performed. Prior-art searches did not identify an equivalent result; unindexed work and full text unavailable from certain indexed records remain historical-priority risks.

## References

- T. Ceccherini-Silberstein and M. Coornaert, *On a characterization of locally finite groups in terms of linear cellular automata*, arXiv:0906.4891, first submitted 2009-06-26, https://arxiv.org/abs/0906.4891.
- E. Rowland and R. Yassawi, *A characterization of p-automatic sequences as columns of linear cellular automata*, arXiv:1209.6008, first submitted 2012-09-26, https://arxiv.org/abs/1209.6008.
- A. Batal, *Effects of edge addition or removal on the nullity of a graph in the Lights Out game*, arXiv:2108.03059, first submitted 2021-08-06, https://arxiv.org/abs/2108.03059.
- *A missing-edge parity transition in hypercube XOR dynamics*, public published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-missing-edge-parity-transition-in-hypercube-xor-dynamics--0ddebf65b6fe.
- *A one-site feedback defect creates periods three and six on Boolean hypercubes*, public published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-one-site-feedback-defect-creates-periods-three-and-six-on-bool--a9a2b0b84ed9.
