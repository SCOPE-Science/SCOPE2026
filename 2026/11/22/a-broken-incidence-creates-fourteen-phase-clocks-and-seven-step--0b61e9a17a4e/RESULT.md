# A broken incidence creates fourteen-phase clocks and seven-step transients in subdivided cliques

## Finding

For every integer \(n\ge3\), subdivide every edge of the complete graph \(K_n\) once, and then delete just the edge between original vertex \(0\) and the subdividing vertex for \(\{0,1\}\). Let \(T_n\) be the adjacency (open-neighbor sum) update on the resulting graph, acting synchronously over a finite field \(\mathbb F_q\) with \(q=2^h\), \(h\ge1\). Put \(N=n(n+1)/2\).

**Odd order.** If \(n\) is odd, every state is periodic after at most one step and \(T_n^{15}=T_n\), sharply: the recurrent map has exact order \(14\), with genuine least-period \(7\) and \(14\) orbits. Its recurrent state-space dimension is \(2n\). For \(d\in\{1,2,7,14\}\), the number of recurrent configurations fixed by the \(d\)-th iterate is respectively
\[
q^{n-3},\quad q^{2n-6},\quad q^n,\quad q^{2n}.
\]
Thus its numbers of primitive temporal orbits are
\[
\begin{aligned}
C_1&=q^{n-3},\\
C_2&=(q^{2n-6}-q^{n-3})/2,\\
C_7&=(q^n-q^{n-3})/7,\\
C_{14}&=(q^{2n}-q^{2n-6}-q^n+q^{n-3})/14.
\end{aligned}
\]
There are \(q^{2n}\) initially periodic states and \(q^N-q^{2n}\) states entering recurrence at step one. Each primitive orbit of period \(d\) has an attraction basin of size \(d q^{N-2n}\).

**Even order.** If \(n\) is even (necessarily \(n\ge4\)), every state becomes periodic within the **sharp seven-step bound** \(T_n^9=T_n^7\). The recurrent dimension is exactly two, with \(q\) fixed configurations and \((q^2-q)/2\) primitive two-cycles. The complete Jordan form is
\[
T_n\sim J_2(1)\oplus J_7(0)\oplus J_3(0)^{\oplus(n-4)}\oplus J_1(0)^{\oplus(N-3n+3)}.
\]
For \(0\le t\le7\), let \((r_0,\ldots,r_7)=(N,2n,n+3,6,5,4,3,2)\). Then precisely \(q^{N-r_t+2}\) states enter recurrence by time \(t\); the first-entry shell at positive time \(t\) is the difference of this quantity and its predecessor. In particular \(q^N-q^{N-1}\) initial configurations require all seven steps. Each fixed-point basin has size \(q^{N-2}\), and each primitive two-cycle basin has size \(2q^{N-2}\).

Compared with the intact subdivision, whose odd-order recurrent dynamics is a two-cycle involution and whose even-order dynamics extinguishes within three steps, the *same single-edge deletion* generates two distinct parity responses: fourteen-period oscillations or a seven-step delayed oscillatory remnant.

## Assumptions and scope

The graph is finite, simple, undirected, and unweighted. Label original vertices \(0,\ldots,n-1\) and new subdivision vertices by two-element subsets \(\{i,j\}\). The lone missing edge is \(0\)--\(\{0,1\}\), which makes the subdivision vertex for \(\{0,1\}\) a leaf attached to vertex \(1\). Vertex updates sum the states of adjacent vertices *without self-feedback* in \(\mathbb F_q\). There are \(m=\binom n2\) subdivision vertices and \(N=n+m\) total sites. Eventual-periodic entry time is the least nonnegative \(t\) such that \(T_n^t x\) lies on a periodic orbit. A primitive temporal orbit is an orbit under repeated synchronous updating, with cyclic rotations identified but graph automorphisms not identified.

Let \(D\in\mathbb F_q^{n\times m}\) be the incidence matrix whose column for \(\{i,j\}\ne\{0,1\}\) is \(e_i+e_j\), and whose exceptional column is \(e_1\). In the original/subdivision ordering,
\[
T_n=\begin{pmatrix}0&D\\D^{\mathsf T}&0\end{pmatrix},\qquad
K=DD^{\mathsf T}=(n\bmod 2)I+J+E_{00}+E_{01}+E_{10}.
\]
Here \(J\) is the all-ones matrix, and \(E_{ij}=e_i e_j^{\mathsf T}\); all additions are in characteristic two.

## Proof

**Step 1: full row rank and the two-shore reduction.** The columns from the edges of \(K_n\setminus\{0,1\}\) span the even-coordinate-sum subspace, because that graph is connected for \(n\ge3\). The exceptional column \(e_1\) has odd coordinate sum. Thus \(D\) has full row rank \(n\); \(D^{\mathsf T}\) is injective. The image of \(T_n\) is the \(2n\)-dimensional invariant space
\[
U=\{(x,D^{\mathsf T}y):x,y\in\mathbb F_q^n\}.
\]
In the unique coordinates \((x,y)\) on \(U\), the restricted map acts as \((x,y)\mapsto(Ky,x)\), and its square acts as \((Kx,Ky)\). For all \(k\ge0\) the odd-power rank is \(\operatorname{rank}T_n^{2k+1}=2\operatorname{rank}K^k\), while for \(k\ge1\) the even-power rank is \(\operatorname{rank}T_n^{2k}=\operatorname{rank}K^k+\operatorname{rank}K^{k-1}\). These identities follow by block multiplication and the surjectivity/injectivity of \(D,D^{\mathsf T}\).

**Step 2: odd parity.** Assume \(n\) odd and write \(r=\sum_{j=2}^{n-1}e_j\). The \((n-3)\)-dimensional subspace \(W=\{x:x_0=x_1=0,\sum_{j\ge2}x_j=0\}\) is fixed pointwise by \(K\). Its complement \(\langle e_0,e_1,r\rangle\) is invariant, and relative to that ordered basis \(K\) has matrix
\[
M=\begin{pmatrix}1&0&1\\0&0&1\\1&1&0\end{pmatrix},
\qquad \det(zI-M)=z^3+z^2+1.
\]
The cubic is irreducible over \(\mathbb F_2\) and its roots have order seven, so \(M\) has order exactly seven over every characteristic-two extension. Hence \(K^7=I\), its fixed subspace has dimension \(n-3\), and \(K\) is invertible. The whole space splits as \(U\oplus\ker T_n\); thus every state enters \(U\) after at most one update and \(T_n\) acts as a permutation on \(U\) of order exactly fourteen. Indeed, squaring gives the nontrivial order-seven map \(K\oplus K\), while odd powers exchange the two \(n\)-dimensional coordinate shores and cannot be identity.

On \(U\), the fixed spaces of powers one and two have dimensions \(n-3\) and \(2n-6\). The seventh iterate sends \((x,y)\) to \((K^4y,K^3x)\). Since \(K^7=I\), its fixed states are parameterized by arbitrary \(x\), with \(y=K^3x\), giving dimension \(n\). The four fixed-space populations in the finding follow; Möbius subtraction across divisors of fourteen yields the displayed primitive-orbit counts. Each periodic point has \(q^{N-2n}\) initial states in its phase fiber, since \(T_n:V\to U\) is surjective and acts invertibly on \(U\), giving the claimed basin sizes.

**Step 3: even parity.** Assume \(n\ge4\) even. Put \(r=\sum_{j=2}^{n-1}e_j\). The vector subspace \(\{x:x_0=x_1=0,\sum_{j\ge2}x_j=0\}\) has dimension \(n-3\) and lies in \(\ker K\). The four-dimensional space spanned by \(e_0,e_1,e_2,r\) is invariant. On those generators,
\[
K e_0=r,\qquad K e_1=e_1+r,\qquad
K e_2=e_0+e_1+r,\qquad K r=0.
\]
The span of \(e_0,e_1,e_2,r\) meets that kernel in precisely \(\langle r\rangle\), and a complementary \((n-4)\)-space lies in \(\ker K\). Directly from the displayed four generator images,
\[
\operatorname{rank} K=3,\quad
\operatorname{rank}K^2=2,\quad
\operatorname{rank}K^j=1\ (j\ge3),\quad K^4=K^3.
\]
Moreover \(K^3\) is a rank-one projection, so its stable one-dimensional image supports the identity. On the stable two-dimensional subspace of \(T_n\), the map swaps two copies of this line and therefore has exactly \(q\) fixed states and \(q^2-q\) states of least period two. The rank identities in Step 1 now give
\[
(\operatorname{rank}T_n^0,\ldots,\operatorname{rank}T_n^7)
=(N,2n,n+3,6,5,4,3,2),
\]
with rank two thereafter. The consecutive rank drops uniquely determine one nilpotent Jordan chain of length seven, \(n-4\) chains of length three, and \(N-3n+3\) chains of length one. In particular the seven-step cutoff is sharp. The periodic/stable direct-sum decomposition gives \(q^{2+\dim\ker T_n^t}=q^{N-r_t+2}\) states periodic by step \(t\). Taking successive differences proves all first-entry counts; the rank-one final drop implies the seven-step population \(q^N-q^{N-1}\). The dimension of the nilpotent summand is \(N-2\), giving the basin factors.

## Verification

Run `python3 check_matrix.py` and `python3 check_states.py` using only the Python standard library. The first program independently constructs the edited adjacency as bit rows, computes matrix ranks and powers for every \(3\le n\le34\), checks all predicted iterate-rank profiles, periodic fixed-space dimensions, and exact power identities. The second constructs neighbor lists directly, follows every individual binary state trajectory for \(n=3,4,5\), and checks each period, first-entry population, and temporal-orbit count. The complete stdout transcripts are `matrix_checks.txt` and `state_checks.txt`, respectively. These finite checks are corroboration, not a substitute for the universally quantified field-independent proof above.

For example, at \(n=3\) the modified graph is a six-vertex path and all \(64\) binary states are periodic, comprising one fixed point, one seven-cycle, and four fourteen-cycles. At \(n=4\), only four of the \(1024\) states are initially recurrent; \(512\) require all seven updates.

## Relationship to prior work

Moreno, Bollman and Aviño-Díaz [1] develop the linear finite-dynamical-system viewpoint and orbit decomposition. Barrett and collaborators [2] examine the minimum rank over *variable* symmetric matrices on complete-subdivision graphs; their Theorem 4.1 is not an iterate classification for the prescribed zero-diagonal adjacency, nor does it treat the specified missing incidence. A published classification [3] proves that the *intact* subdivision of an even-order clique is three-step nilpotent and that the odd-order intact subdivision has only fixed points and two-cycles; neither statement determines the edited graph. A related exact fourteen-cycle theorem [4] treats an *added nonincidence* in the square point-line matrix of an even-order projective plane; a deletion there causes nilpotence in five steps. The present rectangular complete-graph incidence model, whose deleted edge causes a seven-step transient for even \(n\) and order fourteen for odd \(n\), is neither the graph family nor the incidence operation claimed in [4]. None of these results directly implies the full classification here. Search-based priority assessment is not a proof of uniqueness.

## Limitations

The conclusion is restricted to one deleted incidence of the ordinary subdivision of a complete graph, the unweighted synchronous *open-neighbor sum* rule, and finite fields of characteristic two. It does not cover other faults, weighted updates, odd-characteristic fields, asynchronous schedules, or arbitrary base graphs. The result gives complete temporal-period and entry-depth populations and individual orbit basin sizes; it does not enumerate graph-automorphism classes of cycles. The proof is mathematical and the finite computations are supplemental. An unindexed or inaccessible earlier computation may contain an equivalent statement; independent expert validation has not been performed.

## References

[1] O. Moreno, D. Bollman, M. A. Aviño-Díaz, *Finite Dynamical Systems, Linear Automata, and Finite Fields*, arXiv:math/0604534v1, first public arXiv date 2006-04-25, https://arxiv.org/html/math/0604534v1.

[2] W. Barrett, R. Bowcutt, M. Cutler, S. Gibelyou, K. Owens, *Minimum Rank of Edge Subdivisions of Graphs*, *Electronic Journal of Linear Algebra* 18 (2009), 530–563, https://journals.uwyo.edu/index.php/ela/article/download/661/661/661.

[3] *Three-step extinction rigidity and parity-swapped cycles on subdivided cliques*, public repository result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-three-step-extinction-rigidity-and-parity-swapped-cycles-on-subd--88cbaceccac4.

[4] *A universal five-step extinction versus fourteen-cycle dichotomy from one incidence toggle*, public repository result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-universal-five-step-extinction-versus-fourteen-cycle-dichotomy--be1f8ac45d72.
