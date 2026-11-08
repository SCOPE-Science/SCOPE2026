# A vertex puncture creates a parity-dependent Jordan defect in hypercube neighbor-sum dynamics

## Finding

For every \(d\ge2\) and every finite field \(\mathbb F_q\) of characteristic two (\(q=2^f\), \(f\ge1\)), delete one vertex from the ordinary Boolean cube \(Q_d\), obtaining \(H_d\). Let \(B\) be its \((2^d-1)\)-square, loopless adjacency matrix over \(\mathbb F_q\), so the parallel graph automaton is \(x(t+1)=Bx(t)\). Write \(N=2^d\), and use \(J_k(\lambda)\) for a single size-\(k\) Jordan block at eigenvalue \(\lambda\).

The exact Jordan type is
\[
B\sim
\begin{cases}
J_3(0)\oplus J_2(0)^{\oplus(N/2-2)},&d\text{ even},\\
J_1(0)\oplus J_2(1)^{\oplus(N/2-1)},&d\text{ odd}.
\end{cases}
\]
The multiplicity \(N/2-2\) is zero when \(d=2\). The Jordan type, not merely the characteristic polynomial, is asserted for every finite characteristic-two field.

For even \(d\), there is only the zero periodic state. If \(\tau(x)=\min\{t\ge0:B^t x=0\}\), the exact census is
\[
\begin{array}{c|cccc}
t&0&1&2&3\\\hline
\#\{x:\tau(x)=t\}&1&q^{N/2-1}-1&q^{N-2}-q^{N/2-1}&q^{N-1}-q^{N-2}.
\end{array}
\]
For odd \(d\), let \(T(x)\) be the least time when \(B^{T(x)}x\) is periodic. Then \(\#\{T=0\}=q^{N-2}\), \(\#\{T=1\}=(q-1)q^{N-2}\); the number of fixed configurations is \(q^{N/2-1}\), and the number of distinct primitive two-cycle orbits is \((q^{N-2}-q^{N/2-1})/2\). For odd \(d\ge3\) both times zero and one, and both eventual periods one and two, occur.

## Assumptions and scope

Vertices of \(Q_d\) are binary words of length \(d\); two vertices are adjacent when they differ in exactly one coordinate. Vertex transitivity lets us delete \(0^d\) without loss. Each vertex holds one field element. Addition is field addition (no firing threshold, clipping, or self-loop). The local update is **simultaneous**, over a finite field of characteristic exactly two, and the assertions hold uniformly in \(d\) and \(q\). No assertion is made for fields of odd characteristic or for deletion of two or more vertices.

## Proof

**1. The full cube.** Write \(A\) for adjacency of the *unpunctured* \(d\)-cube. If \(S_i\) flips coordinate \(i\), then \(A=\sum_{i=1}^d S_i\). The flips commute, square to the identity, and cross terms cancel in characteristic two; hence \(A^2=dI\), with \(d\) read in the field. Thus \(A^2=0\) for even \(d\), while \((A+I)^2=0\) for odd \(d\). Splitting the cube into two opposite \((d-1)\)-subcubes yields
\[
A=\begin{pmatrix}A_{d-1}&I\\ I&A_{d-1}\end{pmatrix}.
\]
The columns obtained by applying \(A\) to the first half-space have linearly independent second components; the same is true of \(A+I\). Therefore \(\operatorname{rank}A\ge N/2\) and \(\operatorname{rank}(A+I)\ge N/2\). A square-zero \(N\)-square matrix has rank at most \(N/2\). Consequently
\[
\operatorname{rank}A=N/2\quad(d\text{ even}),\qquad
\operatorname{rank}(A+I)=N/2\quad(d\text{ odd}).
\]

**2. Rank-one boundary identity.** Order the removed vertex first and write
\[
A=\begin{pmatrix}0&b^{\mathsf T}\\b&B\end{pmatrix},
\]
where \(b\) is the indicator of its \(d\) neighbors in the remaining cube. Thus \(b\ne0\) and \(b^{\mathsf T}b=d\) in characteristic two. Comparing blocks in \(A^2=dI\) gives
\[
Bb=0,\qquad b^{\mathsf T}B=0,\qquad B^2=dI+bb^{\mathsf T}.
\]
All three identities hold in every allowed field.

**3. Even dimension.** Here \(b^{\mathsf T}b=0\), \(B^2=bb^{\mathsf T}\) has rank one, and \(B^3=Bbb^{\mathsf T}=0\). In particular exactly one nilpotent Jordan block has length three, and all blocks have length at most three. To determine the remaining blocks, first observe that \(b\in\operatorname{im}B\): take \(u\) with \(b^{\mathsf T}u=1\); then \(B^2u=b\). Since \(B\) is symmetric, \(\ker B\subseteq b^\perp\). Choose \(w\) with \(Bw=b\). From \(B^2w=Bb=0\), the identity \(B^2=bb^{\mathsf T}\) forces \(b^{\mathsf T}w=0\).

A pair \((\alpha,v)\) belongs to \(\ker A\) precisely when \(b^{\mathsf T}v=0\) and \(Bv=\alpha b\). For \(\alpha=0\) this is \(v\in\ker B\); for \(\alpha=1\) it is \(v\in w+\ker B\). Hence \(\dim\ker A=\dim\ker B+1\). By Step 1, \(\dim\ker A=N/2\), so \(\dim\ker B=N/2-1\) and \(\operatorname{rank}B=N/2\). One \(J_3(0)\) contributes rank two; each \(J_2(0)\) contributes rank one. Thus precisely \(N/2-2\) two-blocks remain, and their dimensions together with the three-block occupy all \(N-1\) coordinates. No singleton blocks are possible. Kernel dimensions of \(B\), \(B^2\), \(B^3\) are \(N/2-1\), \(N-2\), \(N-1\), respectively. Their field-cardinality differences give the stated exact first-extinction populations. The final population is positive, so extinction time three is sharp.

**4. Odd dimension.** Here \(b^{\mathsf T}b=1\), \(B^2=I+bb^{\mathsf T}\) is the projection onto \(W=b^\perp\) along \(\mathbb F_q b\), and \(Bb=0=b^{\mathsf T}B\). Thus \(B\) maps into \(W\), and \(B^2\) is the identity on \(W\); the restriction \(B|_W\) is an involution, while \(B\) vanishes on the one-dimensional complementary line \(\mathbb F_q b\). Moreover the full-cube space decomposes as
\[
\mathbb F_q^{N}=\operatorname{span}\{e_{0^d},b\}\oplus W.
\]
On its two-dimensional first summand \(A\) swaps \(e_{0^d}\) and \(b\) (since \(Ae_{0^d}=b\), \(Ab=e_{0^d}\)), and on \(W\) it equals \(B|_W\). The swap is a single \(J_2(1)\) in characteristic two, so Step 1 gives \(\operatorname{rank}(B|_W+I)=N/2-1\). As \((B|_W+I)^2=0\) and \(\dim W=N-2=2(N/2-1)\), the complete restriction consists of exactly \(N/2-1\) blocks \(J_2(1)\), with no \(J_1(1)\) blocks. The complementary line is \(J_1(0)\), proving the odd-dimensional Jordan form.

Every state in \(W\) is periodic with period one or two, since \(B^2=I\) there; no state outside \(W\) is initially periodic, but its first iterate lies in \(W\). The cardinalities of \(W\) and its complement give the entry-time census. The fixed space has dimension \(N/2-1\); subtracting its \(q^{N/2-1}\) elements from the \(q^{N-2}\) periodic states and dividing by two gives the number of primitive two-cycle orbits. Since \(N/2-1>0\) for odd \(d\ge3\), both orbit lengths occur, and the nonempty complement of \(W\) shows the entry bound is sharp.

**5. Contrast with the unpunctured cube.** For even \(d\) the square-zero full-cube operator reaches zero in at most two steps, while its one-vertex deletion requires three for some states. For odd \(d\), the full-cube operator satisfies \(A^2=I\) and every state is initially periodic; the vertex-deleted system has precisely one nonperiodic direction and reaches the periodic part in one step. This completes the claim. \(\square\)

## Verification

Execute from a directory containing the supplied verification code:

```sh
python3 check_jordan.py
python3 check_orbits.py
```

The first checker uses exact binary bit-matrix arithmetic to test the rank and polynomial identities for \(2\le d\le8\); these ranks are unchanged over any characteristic-two field extension. The second independently enumerates all labelled states for \((d,q)=(2,2),(3,2),(4,2),(2,4),(3,4)\), using coordinatewise XOR to implement finite-field addition. Outputs recorded in `check_jordan.out` and `check_orbits.out` come from direct execution of these source files. The infinite-parameter statements follow from the proof rather than from these finite checks.

## Relationship to prior work

Linear finite-state systems and their state diagrams are a standard subject; Moreno, Bollman, and Aviño-Díaz (2006) develop such a framework without a vertex-deleted hypercube classification. Istrate (2011) considers an asynchronous, largely odd-modulus annihilating-walk and lights-out process, rather than the present synchronous characteristic-two map. Kim, Reiner, and Schoenzeit (2026) determine *real* adjacency spectra and eigenspaces of hypercubes after removing one or two vertices, but their characteristic-zero decomposition does not give modular Jordan blocks or the orbit-entry census. Lu (2026) studies real adjacency-degree algebras of such punctured product graphs; the resulting algebra problem is different from the characteristic-two temporal dynamics studied here.

For the unpunctured cube the involution/square-zero split follows directly from commuting coordinate-flip operators. This work identifies the exact one-vertex boundary defect, including the nontrivial \(J_3(0)\) or \(J_1(0)\) block and every transient and periodic population. Results for deleting an *edge* of the hypercube, or for distance-two/three neighbor rules, use different matrices and do not supply these formulas.

## Limitations

The result is restricted to finite fields of characteristic two and a single deleted vertex, not arbitrary boundary deletions or random asynchronous updates. Explicit small-dimensional computations only test instances; they are not a proof of the family-wide statement. A priority risk remains from potentially unindexed modular spectral studies of punctured hypercubes; the identified 2026 real-spectral papers do not settle this modular problem. No claim of independent validation is made.

## References

1. O. Moreno, D. Bollman, M. A. Aviño-Díaz, “Finite Dynamical Systems, Linear Automata, and Finite Fields,” arXiv:math/0604534v1, submitted 2006-04-25; full text: https://arxiv.org/pdf/math/0604534.
2. G. Istrate, “Reachability and Recurrence in a Modular Generalization of Annihilating Random Walks (and Lights-out Games) on Hypergraphs,” arXiv:1102.1440v1, submitted 2011-02-07; https://arxiv.org/abs/1102.1440.
3. J. S. Kim, V. Reiner, L. Schoenzeit, “Note on adjacency spectra for twice punctured hypercubes,” arXiv:2608.27887v1, submitted 2026-08-28; https://arxiv.org/abs/2608.27887.
4. Z. Lu, “Punctured adjacency-degree algebras of Cartesian products,” arXiv:2609.06747v1, submitted 2026-09-06; https://arxiv.org/abs/2609.06747.
