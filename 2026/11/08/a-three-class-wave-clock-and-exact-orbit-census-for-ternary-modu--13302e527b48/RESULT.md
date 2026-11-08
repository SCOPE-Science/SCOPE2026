# A three-class wave clock and exact orbit census for ternary-modular Hamming graphs

## Finding
Let \(m\ge3\) be divisible by three, \(d\ge1\), and \(q=3^f\) with \(f\ge1\). Let \(H(d,m)\) be the Cartesian product of \(d\) copies of the complete graph \(K_m\). Its \(n=m^d\) vertices are the \(d\)-letter words over an \(m\)-symbol alphabet; two distinct words are adjacent precisely when they differ in one coordinate. Let \(A\) be its loopless adjacency matrix over \(\mathbb F_q\), and evolve *two* successive vertex configurations by
\[
T(u,v)=(Au-v,u),\qquad (u,v)\in\mathbb F_q^n\times\mathbb F_q^n.
\]
Define the following **integers** (not residue-field elements):
\[
a=\frac{(m-1)^d+(m-3)^d}{2},\qquad
b=\frac{(m-1)^d-(m-3)^d}{2},\qquad
c=\frac{m^d-a-2b}{3},
\quad \kappa_1=a+b+c,\quad \kappa_2=a+2b+2c.
\]
Then the global permutation order of \(T\) is **exactly**
\[
\operatorname{ord}(T)=
\begin{cases}
12,&d\equiv0\pmod3,\\
9,&d\equiv1\pmod3,\\
18,&d\equiv2\pmod3.
\end{cases}
\]
The complete nonzero primitive-period populations \(P_j=\#\{(u,v):\text{least positive return time}=j\}\) are:
\[
\begin{array}{ll}
d\equiv0\pmod3:&P_1=1,\quad P_4=q^{2\kappa_1}-1,\quad P_{12}=q^{2n}-q^{2\kappa_1};\\[3pt]
d\equiv1\pmod3:&P_1=q^{\kappa_1},\quad P_3=q^{\kappa_1+\kappa_2}-q^{\kappa_1},\quad P_9=q^{2n}-q^{\kappa_1+\kappa_2};\\[3pt]
d\equiv2\pmod3:&P_1=1,\quad P_2=q^{\kappa_1}-1,\quad P_6=q^{\kappa_1+\kappa_2}-q^{\kappa_1},\quad P_{18}=q^{2n}-q^{\kappa_1+\kappa_2}.
\end{array}
\]
All unlisted \(P_j\) vanish. Every configuration is periodic from time zero. The number of distinct temporal orbits of primitive period \(j\) is \(P_j/j\).

There is also a **full module description** of the temporal map over \(\mathbb F_3[X]\). Put \(J_s(\lambda)\) for a size-\(s\) Jordan block and \(R_s=\mathbb F_3[X]/((X^2+1)^s)\). If \(d\equiv1\pmod3\), then \(T\) is similar to \(J_2(1)^{\oplus a}\oplus J_4(1)^{\oplus b}\oplus J_6(1)^{\oplus c}\). If \(d\equiv2\pmod3\), replace \(1\) by \(-1\). If \(d\equiv0\pmod3\), its temporal module is \(R_1^{\oplus a}\oplus R_2^{\oplus b}\oplus R_3^{\oplus c}\). The corresponding fixed-state counts at every positive iterate follow from these blocks. These descriptions are made over \(\mathbb F_3\); extension of scalars to \(\mathbb F_q\) preserves their kernel dimensions even when \(X^2+1\) splits in the extension field.

## Assumptions and scope
The dimension \(d\) is a positive integer, and \(m\) is a positive multiple of three, necessarily at least three. The *state field* has characteristic three and may have any finite extension degree. The graph is an ordinary simple undirected Cartesian-product graph, not a self-looped product. Vertex states are arbitrary field elements, not Boolean threshold states. Both initial time levels \(u\) and \(v\) are arbitrary. The minus sign in the update is essential in odd characteristic. No assumption of generic initial states is used.

## Proof
**1. Modular adjacency decomposition.** On one clique, the adjacency matrix is \(J_m-I_m\), where \(J_m\) is the all-ones matrix. In characteristic three and with \(3\mid m\), we have \(J_m^2=mJ_m=0\) and \(\operatorname{rank}J_m=1\). Thus, on the natural \(m\)-dimensional vertex space, \(J_m\) has one nilpotent block of size two and \(m-2\) blocks of size one. On the \(d\)-fold tensor product, the Hamming adjacency is
\[
A=-dI+N,\qquad N=\sum_{i=1}^{d}I^{\otimes(i-1)}\otimes J_m\otimes I^{\otimes(d-i)}.
\]
The summands commute, and their cubes vanish, so the characteristic-three Frobenius identity yields \(N^3=0\).

**2. All nilpotent blocks, not merely the eigenvalue.** Write \(J_s(0)\) for a nilpotent Jordan block. Under the tensor-sum action \(D\otimes I+I\otimes E\), the following identities hold in characteristic three:
\[
J_1(0)\otimes J_2(0)\simeq J_2(0),\quad
J_2(0)\otimes J_2(0)\simeq J_3(0)\oplus J_1(0),\quad
J_3(0)\otimes J_2(0)\simeq J_3(0)^{\oplus2}.
\]
For the middle identity, the sum acting on the four-dimensional squarefree algebra \(\mathbb F_3[x,y]/(x^2,y^2)\) has rank two and its square has rank one, giving blocks \(3,1\). For the last identity, put \(t=x+y\) in \(\mathbb F_3[x,y]/(x^3,y^2)\); because \((t-y)^3=t^3\), this is free of rank two over \(\mathbb F_3[t]/(t^3)\). Each trivial factor adds \(m-2\) unchanged copies. Consequently, if \((a_d,b_d,c_d)\) counts blocks of respective sizes \(1,2,3\), then
\[
a_{d+1}=(m-2)a_d+b_d,\qquad b_{d+1}=a_d+(m-2)b_d,\qquad c_{d+1}=b_d+mc_d,
\]
starting at \((a_0,b_0,c_0)=(1,0,0)\). Adding and subtracting the first two recurrences gives \(a_d+b_d=(m-1)^d\) and \(a_d-b_d=(m-3)^d\); dimension \(a_d+2b_d+3c_d=m^d\) determines \(c_d\). Thus the displayed \(a,b,c\) are exact, and
\[
N\simeq J_1(0)^{\oplus a}\oplus J_2(0)^{\oplus b}\oplus J_3(0)^{\oplus c},\qquad
\dim\ker N=\kappa_1,\quad\dim\ker N^2=\kappa_2.
\]

**3. Temporal blocks from the spatial blocks.** For a nilpotent block \(N_j\) of size \(j\in\{1,2,3\}\), restrict \(T\) to the corresponding \(2j\)-dimensional two-time-level subspace. Its characteristic polynomial is \(\det((X^2+dX+1)I_j-XN_j)=(X^2+dX+1)^j\). The identity
\[
T^2+dT+I=NT
\]
holds on this subspace, with \(N\) acting diagonally on the two time levels and commuting with \(T\). If \(d\equiv0\pmod3\), the polynomial \(X^2+1\) is irreducible over \(\mathbb F_3\). Moreover \((T^2+I)^{j-1}=N^{j-1}T^{j-1}\ne0\), whereas \((T^2+I)^j=0\). Since the subspace has dimension \(2j\), its temporal module is exactly \(\mathbb F_3[X]/((X^2+1)^j)\).

If \(d\equiv1\pmod3\), the characteristic polynomial is \((X-1)^{2j}\). Solving \(T(u,v)=(u,v)\) gives \(u=v\) and \(N_ju=0\), so the \(1\)-eigenspace has dimension one. Hence there is exactly one Jordan block \(J_{2j}(1)\). If \(d\equiv2\pmod3\), the characteristic polynomial is \((X+1)^{2j}\), and solving \(T(u,v)=-(u,v)\) similarly identifies the \(-1\)-eigenspace with \(\ker N_j\), giving \(J_{2j}(-1)\).

**4. Fixed counts, sharp orders, and primitive periods.** Over characteristic three, a block \(J_{s}(1)\) has \(\min(s,3^{\nu_3(t)})\) fixed-space dimensions under its \(t\)th power. For \(J_s(-1)\), only even \(t\) admit nonzero fixed vectors, and then the same formula applies. For \(R_j\), only \(4\mid t\) admit nonzero fixed vectors, contributing \(2\min(j,3^{\nu_3(t/4)})\) dimensions. Summing yields, respectively:
\[
\begin{array}{ll}
d\equiv0:& |\operatorname{Fix}(T^4)|=q^{2\kappa_1},\quad |\operatorname{Fix}(T^{12})|=q^{2n};\\
d\equiv1:& |\operatorname{Fix}(T)|=q^{\kappa_1},\quad |\operatorname{Fix}(T^3)|=q^{\kappa_1+\kappa_2},\quad |\operatorname{Fix}(T^9)|=q^{2n};\\
d\equiv2:& |\operatorname{Fix}(T^2)|=q^{\kappa_1},\quad |\operatorname{Fix}(T^6)|=q^{\kappa_1+\kappa_2},\quad |\operatorname{Fix}(T^{18})|=q^{2n}.
\end{array}
\]
There are no other fixed vectors before these relevant divisors except the zero vector in the cases specified by the final census. As \(b>0\) for every allowed \(m,d\), a size-two spatial Jordan block exists; its temporal block forces the claimed maximal order in every case. Subtracting fixed-set counts along divisibility gives exactly the listed primitive populations. Invertibility is immediate from \(T^{-1}(u,v)=(v,Av-u)\), so there are no transients. This completes the proof.

## Verification
The standalone scripts in `proof/verify_matrix.py`, `proof/verify_states.py`, and `proof/verify_tensor.py` use only the Python standard library. Run each with Python 3 from the package root. `verify_matrix.py` calculates exact adjacency matrices over \(\mathbb F_3\), ranks of \(N\) and \(N^2\), fixed-space dimensions, and sharp temporal orders at seven parameter pairs, including \((m,d)=(3,4)\) with \(162\) time-state coordinates. `verify_states.py` exhausts the \(729\) complete states for \(H(1,3)\) and directly iterates independent random states in three larger cases. `verify_tensor.py` checks the integer tensor recurrence against the closed formulas for ten alphabet sizes and forty dimensions each. Captured outputs are included in `proof/*.out`. The proof above, not finite testing, establishes the general statement.

For \((m,d,q)=(3,1,3)\), the exact primitive-period census is \((P_1,P_3,P_9)=(9,234,486)\), summing to \(729\). For \((m,d)=(3,2)\), \((\kappa_1,\kappa_2)=(5,8)\) and the order is \(18\); for \((m,d)=(3,3)\), \((\kappa_1,\kappa_2)=(13,22)\) and the order is \(12\).

## Relationship to prior work
Brunnet and Chaté studied nonlinear binary cellular automata on high-dimensional *binary* hypercubes, rather than reversible three-characteristic waves on \(H(d,m)\). Macfarlane introduced first-order matrix descriptions of reversible second-order one-dimensional binary cellular automata; the accessible abstract does not state modular Hamming-graph spectra or orbit counts. Steeb and Hardy explicitly use the reversible second-order construction and a one-dimensional binary wave example (their Eq. 23 and Eq. 27); their full four-page text does not contain the present modular Hamming module decomposition. Yoshikawa's full six-page January 2003 symposium proceeding (Theorems 2.4 and 3.4 and Proposition 3.1) determines the **modular adjacency algebra** of Hamming association schemes as a quotient of a polynomial algebra and gives a Cartesian-coordinate adjacency recurrence. Those statements do not classify Jordan multiplicities in the natural vertex representation and do not introduce or count temporal orbits of the two-time-level reversible wave. His subsequent 2004 journal article has not been fully inspected, so additional coverage there is an unresolved priority-comparison risk. In particular, the ordinary complex adjacency eigenvalue formula cannot by itself recover the modular Jordan multiplicities because the one-clique all-ones matrix becomes nonzero and square-zero when the alphabet size vanishes in characteristic three.

## Limitations
The conclusions require \(3\mid m\) and characteristic exactly three; they do not assert the same clock for other alphabet sizes or field characteristics, or for nonlinear threshold dynamics. The full text of Yoshikawa's 2003 proceedings was inspected, but a full-text comparison with his subsequent 2004 journal version, and with Macfarlane (2004), was not possible under available access. No claim of historical priority or independent verification is made. The formulas count labelled field-state configurations, not inequivalent configurations modulo graph automorphisms.

## References
1. L. G. Brunnet and H. Chaté, *Cellular automata on high-dimensional hypercubes*, Physical Review E **69**, 057201 (published 18 May 2004), DOI: `10.1103/PhysRevE.69.057201`.
2. A. J. Macfarlane, *Linear reversible second-order cellular automata and their first-order matrix equivalents*, Journal of Physics A **37**, 10791–10814 (published 28 October 2004), DOI: `10.1088/0305-4470/37/45/006`.
3. M. Yoshikawa, *Modular adjacency algebras of the Hamming association schemes*, Proceedings of the 35th Symposium on Ring Theory and Representation Theory (edited January 2003), pp. 133–138, https://ring-theory-japan.com/ring/oldmeeting/old-proc/ring-sympo/%282002%29.pdf. The later journal version is *Modular Adjacency Algebras of Hamming Schemes*, Journal of Algebraic Combinatorics **20**, 331–340 (2004), DOI: `10.1023/B:JACO.0000048521.68503.2b`.
4. W.-H. Steeb and Y. Hardy, *One-Dimensional Cellular Automata, Conservation Laws and Partial Differential Equations*, Zeitschrift für Naturforschung A **62**, 569–572 (2007), DOI: `10.1515/zna-2007-10-1103`.
