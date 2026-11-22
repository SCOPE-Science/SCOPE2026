# Two cubic spectra and the exact four-wave census on circular ladders

## Finding

For every integer \(n\ge3\), consider the synchronous four-state Greenberg–Hastings map \(F\) on the labelled circular ladder \(C_n\square K_2\). The number \(Q_n\) of **primitive temporal four-cycle orbits** is exactly \(N_n/4\), where

\[
N_n=A_n+B_n+8(1+(-1)^n)+16\cos(\pi n/2)+2(1+(-1)^n)S_n.
\]

All sequences are integer valued, defined from their initial values by

\[
\begin{aligned}
(A_0,A_1,A_2)&=(3,4,18),& A_n&=4A_{n-1}+A_{n-2}+4A_{n-3}\quad(n\ge3),\\
(B_0,B_1,B_2)&=(3,-4,2),& B_n&=-4B_{n-1}-7B_{n-2}+4B_{n-3}\quad(n\ge3),\\
(S_0,S_1)&=(2,1),& S_n&=S_{n-1}-2S_{n-2}\quad(n\ge2).
\end{aligned}
\]

For \(n=3,4,\ldots,12\), the orbit counts are respectively \(30,66,530,1790,7910,40026,154938,741222,3240974,14050818\). The exponential growth constant is the unique positive dominant root \(\lambda\approx4.42961183\) of \(t^3-4t^2-t-4\):

\[
Q_n\sim\frac{\lambda^n}{4},\qquad
\frac{4Q_n}{16^n}=\left(\frac{\lambda}{16}\right)^n(1+o(1)).
\]

Thus the population of immediate four-phase waves grows exponentially, but their fraction of all initial configurations tends exponentially to zero.

## Assumptions and scope

The simple graph has vertices \((i,r)\), \(i\in\mathbb Z/n\mathbb Z\) and \(r\in\{0,1\}\), with cycle edges \((i,r)(i+1,r)\) and rung edges \((i,0)(i,1)\). All vertices are labelled, and \(n\ge3\) (the \(n=3\) rims are triangles). The state alphabet is \(\{0,1,2,3\}\), with \(0\) resting, \(1\) excited, and \(2,3\) refractory. At each simultaneous update, states \(1\to2\to3\to0\) advance unconditionally, while a resting vertex changes \(0\to1\) if and only if **at least one neighbor currently has state one**. No self-neighbor, thresholds beyond one, stochasticity, or boundary opening is allowed. Primitive temporal orbits are quotiented by time translation only, not by spatial rotations, reflection, or color permutation. Only states satisfying \(F^4(x)=x\) at time zero are counted; no eventual basins are asserted.

## Proof

**Four-periodic local phase criterion.** If a vertex is not permanently resting during a four-periodic trajectory, its forced excursion through states \(1,2,3,0\) has length four. Because this excursion includes an excited phase, at any adjacent permanently resting vertex it would force excitation and contradict permanent rest. Since the graph is connected, every nonzero configuration fixed by \(F^4\) has all vertices traversing the full excursion. It therefore advances every color by one modulo four at each update. Conversely, a phase assignment \(c:V\to\mathbb Z/4\mathbb Z\) rotates coherently if and only if every vertex \(v\) has a neighbor \(w\) with \(c(w)=c(v)+1\pmod4\): at a resting phase, that successor neighbor is excited. A nonzero coherent phase assignment has least period four, so there are exactly four phase-labelled states per temporal orbit.

**Finite-space transfer.** Set the rung alphabet \(\mathcal R=(\mathbb Z/4\mathbb Z)^2\), of cardinality sixteen. For consecutive rungs \(a,b,c\in\mathcal R\), define \(H(a,b,c)=1\) precisely when, for both \(r=0,1\),

\[
 b_{1-r}=b_r+1\pmod4\quad\text{or}\quad
 a_r=b_r+1\pmod4\quad\text{or}\quad
 c_r=b_r+1\pmod4.
\]

Let \(T\) be the integer adjacency matrix on the 256 ordered pairs \((a,b)\in\mathcal R^2\), with \(T_{(a,b),(b,c)}=H(a,b,c)\) and all other entries zero. Every length-\(n\) cyclic closed walk corresponds bijectively to a labelled \(n\)-rung phase configuration satisfying the local criterion, hence

\[
N_n=\operatorname{tr}(T^n)\quad(n\ge3).
\]

**A compact exact characteristic-polynomial certificate.** The explicitly reconstructed directed graph of \(T\) has exactly five recurrent strongly connected components: four directed quadrilaterals (four nodes and four edges each), and one component of 144 nodes and 496 edges. The combined 160-node recurrent core is invariant under free global addition of a constant color in \(\mathbb Z/4\mathbb Z\). Normalize each state \((a,b)\) by subtracting the color of the first vertex of \(a\), obtaining exactly 40 classes. An edge between normalized classes records its unique outgoing color translation \(g\in\{0,1,2,3\}\). For each fourth root of unity \(\omega_k=i^k\), construct the explicit 40-square matrix \(M_k\) with entries equal to the sum of \(\omega_k^g\) over those edges. The 256-state trace decomposes as \(\operatorname{tr}(T^n)=\sum_{k=0}^3\operatorname{tr}(M_k^n)\); nonrecurrent vertices contribute no positive-length closed walks.

Direct **exact symbolic determinants**, with the full reconstruction given in `verify_transfer.py`, establish

\[
\begin{aligned}
\det(tI-M_0)&=t^{29}(t-1)^6(t+1)^2(t^3-4t^2-t-4),\\
\det(tI-M_2)&=t^{29}(t-1)^2(t+1)^6(t^3+4t^2+7t-4),\\
\det(tI-M_1)&=\det(tI-M_3)\\
 &=t^{28}(t^2+1)^4(t^2-t+2)(t^2+t+2).
\end{aligned}
\]

The trace of a matrix power is the sum of the corresponding eigenvalue powers, including multiplicities. Newton identities for the two cubics give \(A_n\) and \(B_n\). The quadratic \(t^2-t+2\) yields \(S_n\); the roots of \(t^2+t+2\) are their negatives. The indicated multiplicities at roots \(1,-1,i,-i\) yield the remaining periodic terms. This proves the formula for every \(n\ge3\), not just a finite prefix. Every other root has modulus strictly less than the unique positive dominant cubic root \(\lambda\), proving the asymptotics and coefficient one in the leading term.

## Verification

Run `python3 verify_transfer.py` with Python, SymPy and NetworkX installed. It reconstructs the 256-vertex transfer graph from the displayed local criterion, verifies the recurrent-component sizes, builds all four 40-by-40 twisted matrices, and asserts all four characteristic-polynomial identities using exact symbolic algebra. It then independently constructs integer closed-walk traces for each length from three through twelve and matches the closed recurrence formula. These are finite identities constituting a complete all-length certificate, not sequence interpolation.

The separate standard-C++17 source `direct_check.cpp` implements the original simultaneous microscopic update, without using the rung transfer, exhaustively scans all \(4^6+4^8+4^{10}=1{,}118{,}208\) initial states at \(n=3,4,5\), and checks the exact nonzero four-step-return counts \(120,264,2120\). Compile it with `c++ -O2 -std=c++17 direct_check.cpp -o direct_check` and run `./direct_check`. Both verification approaches were successfully executed on the packaged sources. The direct scan is finite corroboration; the unrestricted result comes from the determinant identities and the local equivalence.

## Relationship to prior work

The general theory of finite-graph excitable media (Durrett and Griffeath, 1993; Gravner, Lyu and Sivakoff, 2016) defines the excitation rule and studies winding/activity properties, rather than this four-state cyclic-ladder orbit enumeration. A previously available **three-state** open-ladder period-three count uses a different palette and free longitudinal boundaries, so it does not imply this four-state closed-ladder formula. A complete **four-state complete-bipartite** excitation classification applies to a different adjacency structure. Other enumerations of proper or conflict-free prism colorings impose different color constraints from the successor-neighbor phase condition. A finite pentagonal-prism calculation gives \(530\) period-four temporal orbits, matching the \(n=5\) specialization, but cannot determine the unrestricted cubic trace law. These comparisons were made at the level of hypotheses and implied counts, not title similarity.

## Limitations

The result concerns immediate primitive four-periodic states only, not the number of trajectories eventually attracted to four-cycles, longer least periods, or convergence times. The graph must be a circular two-rail ladder, with labelled vertices and uniform four-state threshold-one dynamics. The use of a generic finite-state transfer does not in itself supply the characteristic-polynomial reduction; those exact identities are specifically verified. Publication priority remains provisional because older unindexed classifications under equivalent coloring terminology could exist. The foundational 1993 paper's abstract, but not its full text, was inspected. Independent external validation has not been performed.

## References

1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, public preprint 1993-03-22, https://arxiv.org/abs/patt-sol/9303002.
2. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, preprint first submitted 2016-10-24, https://arxiv.org/abs/1610.07320.
3. *Exact primitive-three wave census on open ladders*, complete mathematical result available at https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-primitive-three-wave-census-on-open-ladders--c343292238f3.
4. *Exact four-state excitation orbits and basins on complete bipartite graphs*, complete mathematical result available at https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-four-state-excitation-orbits-and-basins-on-complete-bipart--14573b2e63f6.
