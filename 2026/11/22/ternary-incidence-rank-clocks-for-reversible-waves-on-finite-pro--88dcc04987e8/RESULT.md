# Ternary incidence-rank clocks for reversible waves on finite projective planes

## Finding
Let \(\Pi\) be any finite projective plane of order \(s\ge 2\), not necessarily Desarguesian. Put \(v=s^2+s+1\), let \(B\) be its point-by-line incidence matrix, and let \(A\) be the adjacency matrix of its point–line incidence (Levi) graph. Over a finite field \(K=\mathbb F_Q\) of characteristic three, \(Q=3^f\) for any \(f\ge1\), consider the reversible two-time-level neighbor-sum wave
\[
T(u,w)=(Au-w,u),\qquad u,w\in K^{2v}.
\]
The update is a permutation of all \(Q^{4v}\) labelled two-level states. Its **exact order** is
\[
\operatorname{ord}(T)=\begin{cases}
12,&s\equiv0\pmod3,\\
18,&s\equiv1\pmod3,\\
8,&s\equiv2\pmod3.
\end{cases}
\]
Define \(\rho=\operatorname{rank}_{\mathbb F_3}(B)\), \(a(t)=3^{\nu_3(t)}\), and \(\epsilon(t)=\mathbf1_{2\mid t}\). For **every positive integer** \(t\), the exact number of states fixed by \(T^t\) is \(Q^{E(t)}\), where
\[
E(t)=\begin{cases}
(1+\epsilon(t))\min(a(t),2)+\mathbf1_{4\mid t}\bigl(4(v-1)\mathbf1_{3\mid t}+4(v-\rho)\mathbf1_{3\nmid t}\bigr),&s\equiv0\pmod3,\\
(1+\epsilon(t))\bigl[\min(a(t),4)+(v-2)\min(a(t),2)\bigr],&s\equiv1\pmod3,\\
4v\,\mathbf1_{8\mid t}+4\,\mathbf1_{4\mid t,\ 8\nmid t},&s\equiv2\pmod3.
\end{cases}
\]
Consequently, if \(d\) divides the indicated exact order, the population of labelled states of **least** period \(d\) is
\[
P_d=\sum_{e\mid d}\mu(d/e)Q^{E(e)},
\]
and there are exactly \(P_d/d\) distinct temporal cycles of length \(d\). These are not quotiented by graph automorphisms. The realized least-period sets are respectively \(\{1,2,3,4,6,12\}\), \(\{1,2,3,6,9,18\}\), and \(\{1,4,8\}\) in the three order-residue cases above; every listed period occurs.

For \(3\mid s\), the census **determines the ternary incidence-code rank**:
\[
\rho=v+\frac12-\frac14\log_Q\bigl|\operatorname{Fix}(T^4)\bigr|.
\]
In particular, the rank-dependent information first appears in the fourth-iterate fixed population, which is \(Q^{2+4(v-\rho)}\). For \(s\equiv1\) or \(2\pmod3\), the incidence rank is always \(v\) or \(v-1\), respectively, and the complete census depends only on \(s\) and \(Q\).

## Assumptions and scope
A finite projective plane of order \(s\) has \(v=s^2+s+1\) points and the same number of lines. Every point belongs to \(s+1\) lines; every line contains \(s+1\) points; and two distinct points lie on precisely one common line, with the dual statement for lines. The graph has \(2v\) labelled vertices, with an edge joining an incident point and line. Write
\[
 A=\begin{pmatrix}0&B\\B^{\mathsf T}&0\end{pmatrix}.
\]
All graph and incidence matrices are reduced to the indicated finite field; ranks of integer incidence matrices are computed over \(\mathbb F_3\) and remain unchanged under field extension. Two time levels are ordered. The constant zero state is counted, the time origin is not quotiented, and neither is the graph automorphism action. The valuation \(\nu_3(t)\) is the nonnegative exponent of three dividing positive \(t\), and \(\mu\) is the integer Möbius function. No random initialization is assumed.

## Proof
**1. Incidence identities and reversible linearization.** Counting common lines through two points, and dually common points of two lines, yields
\[
BB^{\mathsf T}=B^{\mathsf T}B=sI+J,
\qquad B\mathbf1=B^{\mathsf T}\mathbf1=(s+1)\mathbf1,
\]
where \(J=\mathbf1\mathbf1^{\mathsf T}\) is \(v\)-by-\(v\). The update matrix is \(T=\begin{psmallmatrix}A&-I\\I&0\end{psmallmatrix}\). Its inverse is \(T^{-1}(u,w)=(w,Aw-u)\), and
\[
T+T^{-1}=\operatorname{diag}(A,A),\qquad
T^2-cT+I=T\operatorname{diag}(A-cI,A-cI)
\]
for every field scalar \(c\). This proves that every finite-field state is already periodic and transfers the Jordan structure of \(A\) to that of \(T\).

For any singleton adjacency Jordan block \(J_1(c)\), the associated temporal block has characteristic polynomial \(X^2-cX+1\). For an adjacency block \(J_2(c)\), the temporal characteristic polynomial is \((X^2-cX+1)^2\). In characteristic three the polynomials for \(c=1,-1,0\) are respectively \((X+1)^2\), \((X-1)^2\), and the separable irreducible polynomial \(X^2+1\). When \(c=0\), the identity \(T^2+I=T\operatorname{diag}(A,A)\) is nonzero on a size-two nilpotent adjacency block, so the minimal temporal polynomial is \((X^2+1)^2\), of degree four: the temporal block is cyclic. When \(c=\pm1\), put \(\lambda=-c\). On an adjacency block \(J_2(c)\), solving the temporal eigenvector equation \(T(u,w)=\lambda(u,w)\) yields \(w=\lambda^{-1}u\) and \((A-cI)u=0\). Its solution space is one-dimensional, so the temporal four-space has only one Jordan block at \(\lambda\), necessarily \(J_4(\lambda)\). For a singleton adjacency block the same argument gives one temporal block \(J_2(\lambda)\). These statements, rather than the characteristic polynomial alone, identify the critical nonsemisimple block lengths.

**2. Plane order \(s\equiv2\pmod3\).** Here \(v\equiv1\pmod3\), so each point- or line-coordinate space splits as constants \(U=\langle\mathbf1\rangle\) and the sum-zero space \(W=\ker(\mathbf1^{\mathsf T})\). The incidence matrices vanish on constants because \(s+1=0\), and restrict to mutually inverse maps up to sign on \(W\), since \(BB^{\mathsf T}=-I+J\). Consequently \(A=0\) on the two constant directions and \(A^2=-I\) on the paired sum-zero space of dimension \(2(v-1)\). On the constant sector \(T^2=-I\), so the wave order is four and the fixed-space dimension is four exactly for multiples of four. On the nonzero sum-zero sector the first identity gives \(T^2+T^{-2}=A^2-2I=0\), hence \(T^4=-I\) and the wave has exact order eight there. It has no fixed vectors unless \(8\mid t\). Therefore \(E(t)=0,4,4v\) in the claimed cases, and the global order is eight.

**3. Plane order \(s\equiv1\pmod3\).** Now \(v\equiv0\pmod3\), so \(J^2=0\). Both \(BB^{\mathsf T}\) and \(B^{\mathsf T}B\) equal \(I+J\), which is invertible. Thus \(A^2-I=\operatorname{diag}(J,J)\), a nonzero square-zero matrix of rank two. The characteristic polynomial of \(A\) is
\[
\det(XI-A)=\det((X^2-1)I-J)=(X^2-1)^v,
\]
so each of the distinct eigenvalues \(\pm1\) has generalized multiplicity \(v\). The image of \(A^2-I\) is the two-dimensional constant sector, on which \(A\) has eigenvalues \(\pm(s+1)=\pm2=\pm1\). Because \(A\) commutes with \(A^2-I\), each generalized eigenspace contains exactly one adjacency Jordan block of size two and \(v-2\) singleton blocks. By Step 1 the wave has, for *each* eigenvalue \(\lambda=\pm1\), one temporal block \(J_4(\lambda)\) and \(v-2\) blocks \(J_2(\lambda)\). In characteristic three, on a size-\(m\) block at eigenvalue one the dimension fixed by its \(t\)-th power is \(\min(m,3^{\nu_3(t)})\). The same holds for eigenvalue minus one when \(t\) is even, and its contribution is zero when \(t\) is odd. Adding both sectors proves the second displayed formula for \(E(t)\). The size-four block at eigenvalue minus one has exact order eighteen, while all other blocks divide eighteen, so the global order is exactly eighteen.

**4. Plane order \(s\equiv0\pmod3\).** Here \(v\equiv1\pmod3\) and \(B\mathbf1=\mathbf1\), so the constant and sum-zero sectors are invariant direct summands. On constants, \(A\) swaps the two shore directions and has one adjacency eigenvalue one and one minus one. Their temporal images are a \(J_2(-1)\) block and a \(J_2(1)\) block. On the paired sum-zero spaces \(A^2=0\), and since the restriction of \(B\) has rank \(\rho-1\), the rank of \(A\) there is \(2(\rho-1)\). The nilpotent adjacency Jordan decomposition on that \(2(v-1)\)-dimensional sector consists of
\[
2(\rho-1)\ J_2(0)\text{ blocks and }2(v-2\rho+1)\ J_1(0)\text{ blocks}.
\]
In particular \(\rho\ge2\): otherwise every column of the zero-sum restriction would vanish, making distinct columns of the incidence matrix identical modulo three, impossible for the distinct binary incidence columns of a projective plane. Under the wave map, these become \(2(\rho-1)\) copies of the four-dimensional cyclic module with polynomial \((X^2+1)^2\) and \(2(v-2\rho+1)\) two-dimensional modules with polynomial \(X^2+1\). The respective exact orders are twelve and four. For a time divisible by four but not three, their total fixed dimension is \(4(v-\rho)\); for a time divisible by twelve it is the whole \(4(v-1)\); otherwise it is zero. The two constant temporal blocks add \((1+\mathbf1_{2\mid t})\min(3^{\nu_3(t)},2)\) fixed dimensions. This is the first displayed \(E(t)\) formula. Because \(\rho>1\), a twelve-order block always occurs, and the global order is exactly twelve. Substituting \(t=4\) gives the incidence-rank recovery identity.

**5. Primitive-period census and occurrence.** For a finite permutation, the numbers \(F_t=|\operatorname{Fix}(T^t)|\) satisfy \(F_t=\sum_{d\mid t}P_d\). Möbius inversion gives \(P_d\) as stated. The temporal module decompositions above provide vectors of exact period equal to each listed divisor of the global order: for example, a full length-four unipotent block has order nine (respectively eighteen at eigenvalue minus one), an \((X^2+1)^2\)-block has period twelve, and direct sums realize the least common multiples of component orders. Nonzero vectors in the shorter Jordan layers realize the smaller listed divisors. There are no other possible periods because each divides the exact order of \(T\). The total is \(F_{\operatorname{ord}(T)}=Q^{4v}\), proving completeness.

## Verification
The package includes two independently constructed exact checker scripts. Run `python3 verify_planes.py` with NumPy to build homogeneous-coordinate Desarguesian planes of orders \(2,3,4,5,7\), including an explicit four-element field; check the projective incidence identities and the full finite-field wave matrix; and compare ranks of \(T^t-I\) at each divisor of the predicted order. Run `python3 verify_affine.py` using only the Python standard library to build projective planes independently from affine points, slopes and points at infinity at prime orders \(2,3,5\). The second script updates every basis configuration directly through the wave, performs its own pure-Python elimination, and verifies all required fixed-space dimensions. Both have been run successfully. Representative exact nullity vectors for \(t\) in ascending divisor order are: at \(s=2\), \((0,0,4,28)\); at \(s=3\), \((1,2,2,26,4,52)\); at \(s=4\), \((20,40,41,82,42,84)\); at \(s=5\), \((0,0,4,124)\); and at \(s=7\), \((56,112,113,226,114,228)\). These finite checks corroborate the universal proof, not replace it; no exhaustive enumeration of \(Q^{4v}\) states is asserted.

## Relationship to prior work
The second-order reversible cellular automaton construction (including the subtraction of the prior state) is established in Vlasov's 2013 treatment. The projective incidence-code literature, including Lavrauw, Storme and Van de Voorde, studies modular codewords and duals, not this two-level temporal system. A previously published *characteristic-two* incidence-rank wave classification on the very same family of projective-plane Levi graphs has orders six and twelve and derives a fixed-point formula using binary incidence rank; the present argument acknowledges this close methodological precedent. Characteristic three cannot be obtained by substituting a field size into its binary-period formulas: the order of the plane modulo three produces the new exact three-way period transition \(8,12,18\), and the incidence rank becomes recoverable at the fourth iterate rather than the first. A separate characteristic-three wave classification for Hamming graphs addresses Cartesian powers of cliques, not finite-plane incidence graphs. The theorem does not claim that modular spectral methods themselves are new.

## Limitations
The result is specifically for the linear neighbor-sum, **two-time-level** reversible update in characteristic three; it does not cover nonlinear excitation, majority rules, other characteristics or spatial symmetry quotients. For plane orders divisible by three, the formulas retain the ternary incidence rank \(\rho\) as a parameter; they do not classify possible ranks for non-Desarguesian planes or claim the rank distinguishes all plane isomorphism classes. Independent peer review has not been performed, and unindexed equivalent historical treatments of finite-field wave modules remain a priority risk. The executable examples cover only the stated small Desarguesian planes; the all-plane statement rests on the algebraic proof.

## References
1. A. Yu. Vlasov, *On generalization of reversible second-order cellular automata*, arXiv:1311.4297, first posted 18 November 2013. https://arxiv.org/abs/1311.4297 . The full accessible HTML was inspected, especially Sections 2–4.
2. M. Lavrauw, L. Storme, G. Van de Voorde, *On the code generated by the incidence matrix of points and hyperplanes in PG(n,q) and its dual*, arXiv:1201.3290, first posted 16 January 2012. https://arxiv.org/abs/1201.3290 . The full accessible HTML was inspected, especially Sections 1–2.
3. *The incidence-rank clock of reversible waves on finite projective planes*, published research record (characteristic two only), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-incidence-rank-clock-of-reversible-waves-on-finite-projectiv--fe075b4d8619 . Its full RESULT was inspected.
4. *A three-class wave clock and exact orbit census for ternary-modular Hamming graphs*, published research record (Hamming graphs), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-three-class-wave-clock-and-exact-orbit-census-for-ternary-modu--13302e527b48 . Its full RESULT was inspected.
