# Three universal wave periods and spectrally invisible orbit counts on strongly regular graphs

## Finding
Let \(G\) be any finite simple noncomplete strongly regular graph with parameters \((v,k,\lambda,\mu)\), where \(0<k<v-1\). Let \(A\) be its adjacency matrix over a finite field \(\mathbb F_Q\) of characteristic two, and define a reversible two-time-row wave evolution
\[
F(u,w)=(Au+w,u),\qquad (u,w)\in \mathbb F_Q^v\times\mathbb F_Q^v.
\]
Write \(d_0=v-\operatorname{rank}_{\mathbb F_2}(A)\) and \(d_1=v-\operatorname{rank}_{\mathbb F_2}(A+I)\). Exactly three cases occur; all orders below are **exact orders** of \(F\), not merely bounds.

* **Order four.** If \(k,\lambda,\mu\) are all even, \(F\) has order \(4\), and its temporal fixed-point counts are
\[
N(1)=Q^{d_0},\quad N(2)=Q^{2d_0},\quad N(4)=Q^{2v}.
\]
* **Order ten.** If \(k,\lambda\) are even and \(\mu\) is odd, then \(v\) is odd, \(F\) has order \(10\), and
\[
N(1)=Q,\quad N(2)=Q^2,\quad N(5)=Q^{2v-1},\quad N(10)=Q^{2v}.
\]
* **Order six.** In every other feasible parameter-parity case, \(F\) has order \(6\), and
\[
N(1)=Q^{d_0},\quad N(2)=Q^{2d_0},\quad N(3)=Q^{d_0+2d_1},\quad N(6)=Q^{2v}.
\]
Here \(N(t)=|\operatorname{Fix}(F^t)|\); for all positive \(t\), use \(N(t)=N(\gcd(t,L))\), with \(L\in\{4,6,10\}\) as above. The exact number of labelled states with primitive temporal period \(t\mid L\), and the exact number of primitive temporal cycles, respectively, are
\[
P(t)=\sum_{e\mid t}\operatorname{mobius}(t/e)N(e),\qquad C(t)=P(t)/t.
\]
Thus primitive periods belong to \(\{1,2,3,4,5,6,10\}\), uniformly in graph size; all three global orders occur (respectively the \(4\)-rook graph, Petersen graph, and pentagon).

**A spectrally invisible dynamical distinction.** For each integer \(\nu\ge3\), the ordinary-adjacency-cospectral symplectic graph \(\operatorname{Sp}(2\nu,2)\) and its Godsil--McKay switch have identical strongly regular parameters
\[
(v,k,\lambda,\mu)=(2^{2\nu}-1,\;2^{2\nu-1},\;2^{2\nu-2},\;2^{2\nu-2}),
\]
but respective binary adjacency ranks \(2\nu\) and \(2\nu+2\) (Abiad--Haemers). Consequently, their reversible wave permutations have different counts of fixed configurations: \(Q^{v-2\nu}\) and \(Q^{v-2\nu-2}\), a factor of \(Q^2\). These wave systems are not conjugate as permutations despite their graph adjacency spectra agreeing. For the explicit \(63\)-vertex pair, the two counts are \(Q^{57}\) and \(Q^{55}\). The switching and rank difference have also been checked directly in the accompanying finite verifier.

## Assumptions and scope
A strongly regular graph here is a finite, undirected, loopless, noncomplete, nonempty regular graph in which adjacent pairs have \(\lambda\) common neighbors and nonadjacent pairs have \(\mu\) common neighbors. The labelled field coordinates remain distinguished: the primitive-cycle counts are temporal cycles, not graph-automorphism orbits. The field size is \(Q=2^f\), \(f\ge1\); the adjacency matrix has entries in \(\mathbb F_2\), so its rank over \(\mathbb F_Q\) equals its binary rank. There is no assumption that the adjacency matrix is nonsingular. All states are periodic immediately because \(F^{-1}(u,w)=(w,u+Aw)\). In the special case of the \(5\)-cycle, the order-ten branch applies; the \(4\)-rook graph and Petersen graph realize the other two branches.

## Proof
**1. The two-row identity and parameter reduction.** Over characteristic two the strongly regular adjacency identity becomes
\[
A^2=(k-\mu)I+(\lambda-\mu)A+\mu J,\quad AJ=kJ,
\]
with coefficients interpreted modulo two. With \(B=\begin{pmatrix}A&I\\ I&0\end{pmatrix}\), direct multiplication yields
\[
B^{-1}=\begin{pmatrix}0&I\\ I&A\end{pmatrix},\qquad B+B^{-1}=\operatorname{diag}(A,A).
\]
Also \(B^2+I=B\operatorname{diag}(A,A)\) and \(B^3+I=(B+I)B\operatorname{diag}(A+I,A+I)\).

**2. The order-four case.** If all three parameters are even, \(A^2=0\). Commutativity with \(B\) gives
\(B^4+I=(B^2+I)^2=B^2\operatorname{diag}(A^2,A^2)=0\).
But \(A\ne0\) by \(k>0\), so \(B^2\ne I\). Thus the order is four.

**3. The order-ten case.** If \(k,\lambda\) are even and \(\mu\) is odd, the counting identity \((v-k-1)\mu=k(k-\lambda-1)\) implies \(v\) is odd. Hence \(V=\mathbb F_Q^v=\langle\mathbf1\rangle\oplus H\), \(H=\ker J\), is an \(A\)-invariant decomposition. On constants \(A=0\), and \(B\) is the coordinate swap, of order two. On \(H\), the SRG identity gives \(A^2=A+I\), and \(A\) is invertible. Hence
\[
B^5+I=(B+I)(B^4+B^3+B^2+B+I)=0
\]
on \(H\); writing \(D=\operatorname{diag}(A,A)\), the recurrence \(B^2=DB+I\), together with \(D^2=D+I\), gives \(B^3=DB+D\), \(B^4=B+D\), and \(B^5=I\). Since \(A\ne0\) and the \(H\)-component is nonzero, the order on \(H\) is five. Thus global order ten. On \(H\), \(B^5\) is the identity, while on the constant component \(B^5=B\), giving fixed-space dimension \(2(v-1)+1=2v-1\). On constants alone \(B\) has one fixed dimension, yielding the stated \(N(1)\) and \(N(2)\).

**4. All remaining cases and their order.** All feasible parameter parities other than the preceding cases are:
(a) even \(k\), odd \(\lambda\), even \(\mu\), for which \(A^2=A\);
(b) odd \(k\), even \(\lambda\), even \(\mu\), for which \(A^2=I\);
(c) even \(k\), odd \(\lambda\), odd \(\mu\), for which \(v\) is odd and \(A\) restricts to zero on constants and obeys \(A^2=I\) on \(H\);
(d) odd \(k\), even \(\lambda\), odd \(\mu\), for which \(A^2=A+J\), \(AJ=J\), hence \(A^3=A\).
The excluded parity \(k,\lambda\) both odd is impossible because each vertex neighborhood is a \(\lambda\)-regular simple graph on \(k\) vertices, and \(k\lambda\) must be even. In cases (a)--(c), \(A(A+I)^2=0\); in (d), \(A^3=A\) gives the same relation. The identity \(B+B^{-1}=\operatorname{diag}(A,A)\) implies
\[
B^3+B^{-3}=\operatorname{diag}(A^3+A,A^3+A)=0,
\]
so \(B^6=I\). The block-power identities \(B^2=\begin{pmatrix}A^2+I&A\\A&I\end{pmatrix}\) and \(B^3=\begin{pmatrix}A^3&A^2+I\\A^2+I&A\end{pmatrix}\) show that \(B^2\ne I\) since \(A\ne0\), and \(B^3\ne I\) since \(A\ne I\) (the diagonal of a simple graph adjacency matrix is zero). As the only proper divisors of six are one, two, and three, the order is exactly six.

**5. Fixed-space dimensions.** For arbitrary adjacency \(A\), eliminating one coordinate from \((B+I)(u,w)=0\) gives \(w=u\), \(Au=0\); therefore \(\dim\ker(B+I)=d_0\). Since \(B^2+I=B\operatorname{diag}(A,A)\) and \(B\) is invertible, \(\dim\ker(B^2+I)=2d_0\).
For order-six graphs, \(A(A+I)^2=0\); the zero-primary \(A\)-space is exactly \(\ker A\), and the complementary one-primary space is \(\ker(A+I)^2\). On the zero-primary subspace the two-row map swaps its coordinates, so \(B^3\) has fixed dimension \(d_0\). On the one-primary subspace \(B+I\) is invertible (a fixed state for \(B\) would have \(Au=0\)); using \(B^3+I=(B+I)B\operatorname{diag}(A+I,A+I)\), its fixed dimension is \(2d_1\). Hence \(\dim\ker(B^3+I)=d_0+2d_1\). For order ten, the block decomposition in step 3 gives the other exponents. Möbius inversion recovers exact primitive populations and division by \(t\) gives primitive cycles.

**6. The cospectral-pair corollary.** The Abiad--Haemers theorem supplies a symplectic strongly regular graph and its switched mate of equal spectra and parameter tuple, with respective binary ranks \(2\nu\) and \(2\nu+2\) for each \(\nu\ge3\). All their parameters are even; the already-proved order-four formula gives two distinct fixed-point numbers. Conjugate permutations have equal fixed-point populations, proving nonconjugacy. Nothing here claims that the graph switching or binary-rank change is new.

## Verification
The standalone Python scripts `verify_wave.py` and `verify_bruteforce.py` use only the standard library and may be run as `python3 verify_wave.py` and `python3 verify_bruteforce.py`. The first constructs 11 named strongly regular graphs, including the explicit 63-vertex symplectic pair and a Godsil--McKay switching set, verifies each graph's parameters, computes exact binary ranks of \(A\) and \(A+I\), and independently tests each claimed fixed-space nullity and exact order from full binary wave matrices. The second explicitly iterates every labelled binary state for the 5-cycle, \(K_{2,2}\), and \(K_{3,3}\), checking period populations without using matrix-power arguments. Captured outputs accompany the scripts. These finite checks support, but do not replace, the all-graph proof above.

## Relationship to prior work
Wolfram (1983) and Martin--Odlyzko--Wolfram (1984) establish classical algebraic and orbit-count techniques for finite additive automata. Macfarlane (2004) uses first-order matrix equivalents of one-dimensional reversible second-order automata; the graph-wide reversible two-row setup is consonant with that earlier work and is not claimed as novel. Brouwer--van Eijl (1992) study strongly regular graph adjacency ranks. Abiad--Haemers (first posted 2014) construct the cospectral switched symplectic graph families with differing binary ranks. The present contribution is the **specific sharp SRG parameter-parity trichotomy of temporal orders and fixed-point populations**, and the induced dynamical nonconjugacy of these cospectral graph pairs. In particular, a general algebraic framework or the known rank distinction alone does not state these simultaneous formulas or their primitive temporal-cycle consequences.

## Limitations
The theorem concerns characteristic-two two-row linear waves on simple nontrivial strongly regular graphs. It does not cover arbitrary graphs, nonlinear local updates, or odd characteristics. In the order-four and order-six branches, absolute orbit counts require graph-specific binary ranks; the SRG parameters alone do not determine them. The symplectic switching construction and 2-rank results are established earlier work, not an independent new graph construction. Historical literature could contain an equivalent reformulation not identified in the examined sources; no independent mathematical audit has been performed.

## References
1. S. Wolfram, *Statistical Mechanics of Cellular Automata*, Rev. Mod. Phys. 55 (1983) 601–644, DOI:10.1103/RevModPhys.55.601; public dated source 1983-07-01.
2. O. Martin, A. M. Odlyzko, S. Wolfram, *Algebraic Properties of Cellular Automata*, Commun. Math. Phys. 93 (1984), 219–258, DOI:10.1007/BF01223745; full text https://content.wolfram.com/sw-publications/2020/07/algebraic-properties-cellular-automata.pdf .
3. A. J. Macfarlane, *Linear reversible second-order cellular automata and their first-order matrix equivalents*, J. Phys. A 37 (2004), 10791–10814, DOI:10.1088/0305-4470/37/45/006.
4. A. Abiad, W. H. Haemers, *Switched symplectic graphs and their 2-ranks*, arXiv:1412.2945v1 (publicly posted 2014-12-09), https://arxiv.org/abs/1412.2945 .
5. A. E. Brouwer, C. A. van Eijl, *On the p-rank of the adjacency matrices of strongly regular graphs*, DOI:10.1023/A:1022438616684 (1992).
