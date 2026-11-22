# Complementary golden-ratio responses to one missing rung in majority prisms

## Finding
Let \(G_n=C_n\square K_2\) be the labelled, undirected prism with \(n\ge3\) rungs, and let \(G_n^-\) be obtained by deleting only the rung between its two vertices in column zero. Under simultaneous binary **open-neighbor majority with incumbent retention at ties**, write \(H_n^{\circ},P_n^{\circ}\) for the numbers of fixed states and states fixed by two updates on \(G_n\), and \(H_n^-,P_n^-\) for the analogous numbers on \(G_n^-\). All configurations retain their labels; temporal two-cycle *orbits* number \((P-H)/2\).

Put \(\varphi=(1+\sqrt5)/2\). Then a single missing rung yields the exactly complementary asymptotic responses
\[
\boxed{\begin{aligned}
H_n^{\circ}&\sim\varphi^n,&H_n^-&\sim\frac3{\sqrt5}\varphi^n,\\
P_n^{\circ}&\sim\varphi^{2n},&P_n^-&\sim\left(2-\frac3{\sqrt5}\right)\varphi^{2n}.
\end{aligned}}
\]
Consequently the missing edge increases equilibrium populations by an asymptotic fraction \(3/\sqrt5-1=0.3416407864\ldots\), while it decreases primitive two-cycle populations by **the same asymptotic fraction**, without changing either exponential growth rate. This is a comparison of *initially recurrent configurations*, not attraction-basin populations.

The equilibria on the defective prism also have an exact all-size Fibonacci law:
\[
\boxed{H_n^-=3F_n+\delta_{n\bmod6},\qquad
(\delta_0,\ldots,\delta_5)=(6,5,1,-2,-1,3),}
\]
where \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\).

More strongly, every defective-prism two-cycle count is given exactly by a rational generating function. Define
\[
\begin{aligned}
 d_2(z)={}&(1-z)(1+z)(1-3z+z^2)(1-z-z^2)\\
 &\cdot(1-z+z^2)(1+z-z^2)(1+z+z^2)\\
 &\cdot(1-z+2z^2+z^3+z^4)(1+z+2z^2-z^3+z^4),\\
 Q(z)={}&2+2z-11z^2-9z^3+17z^4+12z^5-154z^6-16z^7\\
 &+104z^8+190z^9-158z^{10}+374z^{12}-22z^{13}\\
 &+29z^{14}-101z^{15}+45z^{16}-28z^{17}+2z^{18}\\
 &-12z^{19}+6z^{20}.
\end{aligned}
\]
Then, as formal power series at zero,
\[
\boxed{\sum_{n\ge1}P_n^-z^n=\frac{2zQ(z)}{d_2(z)}.}
\]
The coefficients at \(n=1,2\) use the purely formal overlapping-column convention; the physical graph claims start at \(n=3\). Likewise the fixed-state series is
\[
\sum_{n\ge1}H_n^-z^n=
\frac{2z(2-4z+2z^2+2z^3-z^4-2z^5)}{(1-z)(1-z+z^2)(1-z-z^2)}.
\]
In particular, the primitive two-cycle orbit count on the defective prism is exactly \((P_n^--H_n^-)/2\) for every \(n\ge3\).

## Assumptions and scope
Vertices are \((i,r)\) with \(i\in\mathbb Z/n\mathbb Z\) and rail \(r\in\{0,1\}\). All rail edges \((i,r)\sim(i+1,r)\) are present, and rungs \((i,0)\sim(i,1)\) are present except at \(i=0\) in \(G_n^-\). At three-neighbor vertices, a site adopts the strict majority of its neighbors. At the two degree-two vertices of the missing rung, equal neighbor opinions are adopted; when the neighbors disagree, the previous site opinion persists. This tie rule is part of the theorem and is not a random choice or a closed-neighborhood majority. All vertices are distinct for \(n\ge3\).

A state has period dividing two exactly when the second synchronous update returns it to itself, regardless of whether it has transient predecessors. Period-one states are included in period-dividing-two counts. Rotation/reflection equivalence classes are not taken.

## Proof
**Eventual period restriction.** Identify binary opinions with \(\{-1,+1\}\). Let \(A\) be the symmetric adjacency matrix of either prism and choose \(0<\varepsilon<1\). The update is precisely \(x(t+1)=\operatorname{sgn}((A+\varepsilon I)x(t))\), since a nonzero integer neighbor sum dominates \(\varepsilon\), and at a zero neighbor sum the incumbent decides. Set \(W=A+\varepsilon I\) and \(E_t=-x(t+1)^\mathsf{T}Wx(t)\). By symmetry,
\[
E_{t-1}-E_t=(x(t+1)-x(t-1))^\mathsf{T}Wx(t)\ge0,
\]
with strict inequality whenever \(x(t+1)\ne x(t-1)\) in any coordinate. There are only finitely many two-time energies, so equality eventually holds, forcing periods one or two. This is the classical symmetric-threshold argument, reproduced here to fix the tie convention.

**Exact two-time transfer.** For temporal divisor \(t\in\{1,2\}\), represent a column by a word \(a\) of \(2t\) bits, comprising two rail opinions at each of the \(t\) time phases. Its alphabet has size \(q=4^t\). In the ordinary column, a triple of consecutive column letters \((a,b,c)\) is allowed when each rail at time \(j+1\pmod t\) equals the majority of its same-rail bits in \(a,c\) and its opposite-rail bit in \(b\), for all phases \(j\). In the missing-rung column, the two same-rail neighbor bits vote instead, with incumbent retention when they disagree.

Let \(T_t\) and \(B_t\) be the \(q^2\)-square integer adjacency matrices indexed by ordered pairs \((a,b)\). Their only possible nonzero entry is \((a,b)\to(b,c)\); the entry is one if the indicated ordinary or missing-rung column rule holds at the middle letter \(b\). Reading a closed spatial walk with the missing-rung transition at column zero gives a bijection with configurations satisfying \((F_n^-)^t(x)=x\). Therefore
\[
H_n^-=\operatorname{tr}(B_1T_1^{n-1}),\qquad
P_n^-=\operatorname{tr}(B_2T_2^{n-1})
\]
for all \(n\ge3\). The corresponding intact counts are \(\operatorname{tr}(T_t^n)\).

**Finite polynomial identity with an all-length certificate.** The ordinary transfer graphs have respectively \(16\) and \(256\) vertices, with exactly \(20\) and \(400\) directed arcs. Their cyclic strongly connected component sizes are \((4,1,1)\) and \((16,8,8,2,1,1)\). All these figures follow by enumerating the above local truth tables. Exact integer closed-walk Newton identities compute the characteristic polynomial of each component and hence \(D_t(z)=\det(I-zT_t)\). In both cases the denominators displayed in the finding divide \(D_t(z)\) over the integers.

For any \(N\)-square matrix \(T\) and matrix \(B\), the resolvent formula
\[
\sum_{n\ge1}\operatorname{tr}(BT^{n-1})z^n
=z\operatorname{tr}\bigl(B(I-zT)^{-1}\bigr)
\]
has denominator dividing \(D(z)=\det(I-zT)\), with numerator degree at most \(N\). The standalone `verification/transfer_certificate.py` computes every edge, every cyclic-component determinant, and all \(N+1\) coefficients through degree \(N\). Its integer polynomial checks give exactly the proposed reduced denominators and numerators, including the full degree-twenty \(Q\), and zero residual coefficients through \(N=16\) and \(N=256\). The candidate rational expressions also have numerator degree below \(N\) after multiplication by \(D\). Thus their differences with the exact resolvents, after multiplication by \(D\), are polynomials of degree at most \(N\) with every coefficient zero. This establishes the exact generating functions for **every** ring length; no finite-length extrapolation is made.

**Fibonacci law.** The fixed-state reduced denominator factors into \((1-z-z^2)(1-z)(1-z+z^2)\). The coefficient sequence of the displayed rational function is \(3F_n+\delta_{n\bmod6}\); this follows either by partial fractions or by the annihilating recurrence and the six initial residues. The integer certificate checks that identity against the transfer coefficients, and the rational-function argument establishes it at all sizes.

**Golden coefficients and complementary responses.** The intact ordinary transfer \(T_1\) has a unique dominant eigenvalue \(\varphi\), while \(T_2\) has a unique dominant eigenvalue \(\varphi^2=(3+\sqrt5)/2\). Both occur simply and the intact traces have leading coefficient one; their remaining cyclic-component eigenvalues have modulus at most \(1\) and \(\varphi\), respectively. This is confirmed by their exact component characteristic polynomials, not fitted growth curves.

For a rational series \(N(z)/d(z)\) with simple dominant positive pole \(r\), its coefficients are asymptotic to \(-N(r)/(r d'(r))\cdot r^{-n}\). The poles here are \(r_1=(\sqrt5-1)/2\) and \(r_2=(3-\sqrt5)/2\). Substitution in the exact rational functions yields the respective residues
\[
-\frac{N_1(r_1)}{r_1d_1'(r_1)}=\frac3{\sqrt5},\qquad
-\frac{N_2(r_2)}{r_2d_2'(r_2)}=2-\frac3{\sqrt5}.
\]
The package checks these as *exact polynomial congruences* modulo the two quadratic minimal polynomials. Subtracting fixed from period-dividing-two populations shows that primitive two-cycle orbits have the stated asymptotic fractional decrease. The equality of the absolute fractional responses follows from \((3/\sqrt5-1)-(1-[2-3/\sqrt5])=0\).

## Verification
`verification/transfer_certificate.py` is a standalone Python standard-library checker. It independently builds the complete ordinary and missing-rung transfer graphs from their Boolean truth tables; finds all cyclic strongly connected components; obtains exact determinants through integer Newton identities; proves divisibility of the proposed reduced denominators into the full determinants; and compares the numerator identities through the full Cayley–Hamilton bounds (degrees sixteen and 256). It additionally verifies the two dominant-pole residues as exact quadratic-field congruences. The successful completion marker is `EXACT_TRANSFER_CERTIFICATE_OK`.

`verification/direct_check.py` independently iterates the binary majority update on **every** original state for each \(3\le n\le9\), for both the intact and defective prisms. Its complete direct counts agree with the transfer results, and the success marker is `DIRECT_ENUMERATION_OK`. Both programs have been executed from the complete package contents. Direct enumeration tests are not substituted for the all-length determinant proof.

## Relationship to prior work
Goles and Olivos (1980) established the general eventual-period restriction for symmetric binary threshold systems. Agur, Fraenkel and Klein (1988) treated the **one-rail self-inclusive** cyclic majority model, whose local rule differs here. Jen (1988) developed the general cylindrical transfer-matrix method for arbitrary cellular-automaton rules; the accessible full text develops the technique and classifies two-input rules, but does not evaluate the present two-rail **one-rung defect** response. The 2014 preprint by Benjamini and collaborators studies convergence, unanimity, and disagreement on random or unimodular graphs, not this exact family.

A closely relevant published **minority-rule** result already shows that removing a rung multiplies the minority-equilibrium population asymptotically by \(3/\sqrt5\), with an explicit all-size Fibonacci correction. That earlier coefficient is **not** independently novel here. When \(n\) is even, the defective prism is bipartite and complementing spins on one shore conjugates majority to minority, so its **entire even-circumference fixed-point formula is already implied by that publication**. When \(n\) is odd, that bipartite conjugacy fails; the majority fixed corrections differ from the published minority corrections. Crucially, the earlier result explicitly treats **only one-update fixed states** and gives no period-two return polynomial or opposite oscillatory response. The accepted new contribution is the evaluated all-size two-step census and the equality of the opposite asymptotic *majority* response magnitudes, with the odd-circumference majority fixed correction as a refinement.

A previously published complete Lucas-number census on intact prisms establishes the baseline \(H_n^{\circ}\) and \(P_n^{\circ}\); its exact statements do **not** imply the missing-rung generating function, because the defective vertices have a different local tie condition. Previously published open-ladder and prism/Möbius seam-twist results concern missing *rail edges*, boundary ends, or altered seam identifications, not one absent vertical rung. The new claim is the explicit defect response, its exact all-length census, and the complementary algebraic asymptotic coefficients; the transfer technique and intact baseline are not claimed as new.

## Limitations
The theorem counts initially recurrent states rather than attraction basins, and makes no statement about worst-case transient lengths. It requires incumbent-retaining ties at the two degree-two defect vertices and an otherwise intact simple prism. The rational numerator is a finite symbolic result supported by an executable exact certificate, not a short hand-derived recurrence; although all polynomial checks are exact, independent mathematical validation has not occurred. A historically unindexed source might have an equivalent defect formula. A search result or lack of a match cannot establish absolute priority.

## References
1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189. https://doi.org/10.1016/0012-365X(80)90121-1 .
2. Z. Agur, A. S. Fraenkel and S. T. Klein, *The number of fixed points of the majority rule*, Discrete Mathematics 70 (1988), 295–302. https://u.cs.biu.ac.il/~tomi/Postscripts/majority.pdf .
3. E. Jen, *Cylindrical cellular automata*, Communications in Mathematical Physics 118 (1988), 569–590. https://doi.org/10.1007/BF01221109 ; accessible text https://www.academia.edu/72440176/Cylindrical_cellular_automata .
4. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, first public 2014-05-11. https://arxiv.org/abs/1405.2486 .
5. *A Lucas-number orbit census for synchronous majority on prism graphs*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-lucas-number-orbit-census-for-synchronous-majority-on-prism-gr--f39104b86e05 .
6. *A single missing rung amplifies minority fixed states on cyclic ladders by \(3/\sqrt5\)*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-single-missing-rung-amplifies-minority-fixed-states-on-cyclic--7acb4d6f373b .
7. *A mod-three resonance in the majority clocks of open ladders*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-mod-three-resonance-in-the-majority-clocks-of-open-ladders--1a0c668701cb .
