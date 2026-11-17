# Three-residue temporal clocks for reversible ternary crown waves

## Finding
Let \(n\ge5\) and \(q=3^f\), where \(f\ge1\). Let \(C_n=K_{n,n}\setminus M\) be the crown graph on labelled vertices \(x_1,\ldots,x_n,y_1,\ldots,y_n\), with \(x_i\) adjacent to \(y_j\) exactly when \(i\ne j\). Write \(A_n\) for its adjacency operator over \(\mathbb F_q\), and evolve two independent vertex configurations by the invertible update
\[
T_n(u,v)=(A_nu-v,u),\qquad (u,v)\in\mathbb F_q^{2n}\times\mathbb F_q^{2n}.
\]
Every state is periodic from the initial instant. The **least global order** of this permutation is exactly
\[
\boxed{\operatorname{ord}(T_n)=\begin{cases}18,&n\equiv0\pmod3,\\12,&n\equiv1\pmod3,\\6,&n\equiv2\pmod3.\end{cases}}
\]
More strongly, for every positive integer \(t\), the exact number of states fixed after \(t\) updates is \(q^{E_n(t)}\), where \(\mathbf1_P\) denotes the indicator of a proposition \(P\) and
\[
\begin{aligned}
e_2(t)&=\mathbf1_{2\mid t},&e_3(t)&=\mathbf1_{3\mid t},&e_4(t)&=\mathbf1_{4\mid t},\\
h(t)&=\begin{cases}1,&3\nmid t,\\3,&3\mid t,\ 9\nmid t,\\4,&9\mid t,\end{cases}
\end{aligned}
\]
\[
\boxed{E_n(t)=\begin{cases}
(1+e_2(t))\bigl(h(t)+(n-2)(1+e_3(t))\bigr),&n\equiv0\pmod3,\\
(n-1)(1+e_2(t))(1+e_3(t))+4e_4(t),&n\equiv1\pmod3,\\
n(1+e_2(t))(1+e_3(t)),&n\equiv2\pmod3.
\end{cases}}
\]
For any \(d\) dividing the corresponding global order, the exact population of states with **least** period \(d\) and the number of distinct time-orbits of that period are respectively
\[
P_n(d)=\sum_{e\mid d}\mu(d/e)q^{E_n(e)},\qquad O_n(d)=P_n(d)/d.
\]
For \(d\) not dividing the global order, both quantities are zero. Counts are for labelled full configurations, without identifying graph automorphisms or time-phase shifts.

## Assumptions and scope
The vertex labels, deleted matching and simple undirected graph are fixed as above. Each time-level vector has \(2n\) components; both are arbitrary. The field has characteristic exactly three and can be any finite extension of \(\mathbb F_3\). The subtraction of the previous time level is part of the rule. The claims apply for every integer \(n\ge5\), extension degree \(f\ge1\), and update count \(t\ge1\). Small crown graphs with \(n=3,4\) are outside the claim because their underlying graphs coincide with a cycle and a Boolean cube, respectively; those geometries have been studied separately.

## Proof
**1. Two spatial blocks.** In shore order, the adjacency matrix is \(A_n=\left(\begin{smallmatrix}0&B\\B&0\end{smallmatrix}\right)\), with \(B=J_n-I_n\) and \(J_n\) the all-ones matrix. Because two is a unit in characteristic three, the invertible change \((x,y)\mapsto(x+y,x-y)\) makes \(A_n\) similar to \(B\oplus(-B)\). On \(\mathbb F_q^n\), \(J_n\) has rank one and obeys \(J_n^2=nJ_n\). Its kernel has dimension \(n-1\). If \(3\nmid n\), the constant vector splits off and \(B\) has eigenvalue \(n-1\) on that line and eigenvalue \(-1\) on the kernel. If \(3\mid n\), then \(J_n\ne0\) but \(J_n^2=0\); its Jordan form comprises one block of size two and \(n-2\) blocks of size one. Thus \(B\) has one length-two Jordan block at \(-1\) and \(n-2\) simple blocks there, while \(-B\) has the corresponding blocks at \(+1\).

**2. Exact temporal conversion.** For a spatial eigenvalue \(a\), a one-dimensional spatial block lifts to the two-time-level matrix \(\left(\begin{smallmatrix}a&-1\\1&0\end{smallmatrix}\right)\), with characteristic polynomial \(X^2-aX+1\). At \(a=0\) it is an irreducible quadratic over \(\mathbb F_3\), of exact order four. At \(a=1\) the polynomial is \((X+1)^2\), and the temporal block is non-scalar, hence \(J_2(-1)\). At \(a=-1\), it is \((X-1)^2\), hence \(J_2(1)\). The latter two blocks have orders six and three, respectively.

For a size-two spatial Jordan block \(aI+N\), \(N^2=0\ne N\), the temporal characteristic polynomial is \((X^2-aX+1)^2\). At \(a=\pm1\), it is the fourth power of the appropriate linear factor. To determine its Jordan structure rather than only its spectrum, solve \(T(u,v)=\lambda(u,v)\): the second time-level equation forces \(u=\lambda v\) and the first becomes \(((\lambda+\lambda^{-1})I-A)v=0\). At the relevant repeated root \(\lambda=\mp1\), the last kernel is \(\ker N\), of dimension one. Consequently the four-dimensional temporal block has exactly one Jordan block and must be \(J_4(\mp1)\).

**3. Temporal Jordan forms.** If \(n\equiv0\pmod3\), the whole temporal operator has
\[
J_4(1)\oplus J_4(-1)\oplus J_2(1)^{\oplus(n-2)}\oplus J_2(-1)^{\oplus(n-2)}.
\]
If \(n\equiv1\pmod3\), the constant-line adjacency eigenvalues are both zero, while the \(2(n-1)\) remaining adjacency eigenlines split evenly between \(\pm1\). Thus the temporal operator consists of \(n-1\) blocks \(J_2(1)\), \(n-1\) blocks \(J_2(-1)\), and **two** two-dimensional blocks with minimal polynomial \(X^2+1\). If \(n\equiv2\pmod3\), the constant-line adjacency eigenvalues \(\pm1\) join the \(n-1\) other lines: there are exactly \(n\) blocks \(J_2(1)\) and \(n\) blocks \(J_2(-1)\).

**4. Fixed spaces and least periods.** For any \(s\ge1\), a block \(J_s(1)\) has \(\min(s,3^{\nu_3(t)})\) fixed dimensions under its \(t\)-th power. A block \(J_s(-1)\) contributes only when \(t\) is even, then with the same dimension; and \(X^2+1\) contributes two fixed dimensions precisely when \(4\mid t\). Applying these rules to the three explicitly listed Jordan forms yields the displayed expressions for \(E_n(t)\). In the first residue class, the presence of \(J_4(-1)\) forces order eighteen; in the second, \(J_2(-1)\) and the quadratic order-four blocks together force order twelve; in the third, \(J_2(-1)\) forces order six. The maximum orders are attained because each requisite block is present for all \(n\ge5\). The inverse is \(T_n^{-1}(u,v)=(v,A_nv-u)\), proving immediate periodicity. Lastly \(q^{E_n(t)}=\sum_{d\mid t}P_n(d)\) for this permutation, so Möbius inversion and division by period give the asserted exact orbit census. \(\square\)

## Verification
The standalone standard-library Python script `verification/verify_matrix.py` constructs the full temporal matrix over \(\mathbb F_3\) directly from the labelled graph for each \(5\le n\le10\). Exact modular Gaussian elimination checks all \(216\) pairs \((n,t)\) with \(1\le t\le36\) against the claimed nullity, as well as exact global-order identities and their strictness. A separately coded neighbor-by-neighbor rule tests \(360\) pseudorandom full configurations, \(60\) per graph, against the predicted global period. Actual execution output is in `verification/verified_output.txt`. These finite tests corroborate the all-parameter proof; they do not prove it independently. The result remains valid over arbitrary finite characteristic-three extensions because the displayed Jordan forms and fixed-space ranks are obtained over the prime field.

## Relationship to prior work
General reversible second-order cellular automata and previous-state subtraction are established in Vlasov (2013), Section 3, and earlier literature; the reversible construction itself is not claimed as new. Klee and Stamps (2020), Section 3.3, derive the crown graph **Laplacian characteristic polynomial** over the reals using rank-one perturbations. That determines ordinary spectral multiplicities but does not establish characteristic-three Jordan block sizes at the exceptional residue \(3\mid n\), nor a time-dependent fixed-point or primitive-period census. Published finite-field wave classifications on complete bipartite graphs and on cycles concern different spatial modules; indeed the present matching-deleted bicliques have a three-residue order of six, twelve or eighteen rather than the intact bipartite graph's eight/twelve dichotomy. The separate small cases \(n=3,4\) are excluded because they correspond to previously investigated graph families. The new assertion is the combined all-size modular temporal block classification and orbit census for \(n\ge5\).

## Limitations
No result is asserted for characteristics other than three, weighted edges, nonlinear threshold updates, or first-order dynamics. The numbers count individual labelled states and time orbits, not graph-automorphism classes. The reviewed research search is finite and cannot exclude an unindexed older equivalent result. The journal-only full text of one older general reversible-automaton reference was not inspected. A full independent mathematical audit has not been performed.

## References
1. Alexander Yu. Vlasov, *On generalization of reversible second-order cellular automata*, arXiv:1311.4297, first posted 2013-11-18. https://arxiv.org/abs/1311.4297
2. Steven Klee and Matthew T. Stamps, *Eigenvalues of graph Laplacians via rank-one perturbations*, arXiv:2008.01669, first posted 2020-08-04, especially Section 3.3. https://arxiv.org/abs/2008.01669
3. A. J. Macfarlane, *Linear reversible second-order cellular automata and their first-order matrix equivalents*, Journal of Physics A **37** (2004), 10791–10814, DOI:10.1088/0305-4470/37/45/006.
4. Published research records on finite-field reversible waves for complete bipartite graphs and cycles, published-finding corpus research archive (2026), record identifiers `167b2c8980f2` and `6f3d55fba7da`. https://github.com/published-finding corpus/2026
