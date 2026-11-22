# Dihedral homology of generalized Petersen independence complexes and a mod-twenty quotient law

## Finding
For each integer \(n\ge5\), let \(G_n=\operatorname{GP}(n,2)\) be the cubic graph with vertices \(u_i,v_i\), \(i\in\mathbb Z/n\mathbb Z\), and edges \(u_iu_{i+1},u_iv_i,v_iv_{i+2}\). Let \(X_n=\operatorname{Ind}(G_n)\), the simplicial complex of independent vertex sets, and let \(D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\) act by \(r(u_i)=u_{i+1},r(v_i)=v_{i+1},s(u_i)=u_{-i},s(v_i)=v_{-i}\). Write \(n=5t+e\), \(0\le e\le4\), and set
\[
d_n=\begin{cases}3t-1,&e=0,\\3t+e-2,&1\le e\le4.\end{cases}
\]
The previously established nonequivariant theorem gives one nonzero reduced rational homology degree, \(d_n\), of rank \(b_n=4\) if \(5\mid n\) and \(b_n=1\) otherwise. The complete **newly calculated dihedral homology character** \(\chi_n(g)=\operatorname{tr}(g\mid\widetilde H_{d_n}(X_n;\mathbb Q))\) is as follows.

For every integer \(a\), with \(d=\gcd(n,a)\),
\[
\boxed{\chi_n(r^a)=(-1)^{d_n+d}\bigl(1-5\mathbf1_{5\mid d}\bigr).}
\]
For reflections, if \(n\) is odd, all \(\chi_n(r^as)\) equal \(+1\) for \(n\equiv1,7,13,19\pmod{20}\), equal \(-1\) for \(n\equiv3,9,11,17\pmod{20}\), and equal \(0\) for \(5\mid n\). If \(n\) is even, \(\chi_n(r^as)=(-1)^a\chi_n(s)\), where
\[
\chi_n(s)=\begin{cases}
+1,&n\equiv2,8,14,16\pmod{20},\\
-1,&n\equiv4,6,12,18\pmod{20},\\
0,&n\equiv0,10\pmod{20}.
\end{cases}
\]
In particular, the ordinary geometric quotient has the complete additive rational cohomology description
\[
\boxed{\widetilde H^j(|X_n|/D_n;\mathbb Q)\cong\begin{cases}
\mathbb Q,&j=d_n\ \text{and }n\equiv1,7,13,19\pmod{20},\\
0,&\text{otherwise}.
\end{cases}}
\]
The calculated \(D_n\)-character agrees, for every \(n\), with the previously published character of the different, \(n\)-vertex simplicial complex of cyclic binary words having no four consecutive ones. Consequently their rational homology representations are isomorphic as \(D_n\)-modules. No equivariant homotopy equivalence or explicit geometric map between these complexes is asserted.

## Assumptions and scope
Graphs and complexes are finite and unweighted. The group is the specified canonical dihedral subgroup, not the full automorphism group (which can be larger for some exceptional graphs). Homology is reduced rational homology. A geometric quotient is formed after realization and may have nonfree isotropy; the computation uses rational coefficients. The source leading to the problem is an earlier exact transfer-matrix investigation of independence polynomials of generalized Petersen graphs, first publicly posted on 2026-01-05. The published nonequivariant homotopy classification used to determine degree and rank is from the subsequently posted 2026-11-17 work of Youngsoo Kim and is acknowledged as an input, not a newly proved homotopy theorem.

## Proof
**1. Signed orbit-face formula.** For any simplicial automorphism \(g\) of an independence complex, a setwise fixed face is a union of vertex orbits of \(g\). If it comprises \(h\) complete orbits, its augmented, signed alternating simplicial-chain trace is \((-1)^{h-1}\), because the permutation sign on the face equals \((-1)^{|\sigma|-h}\). Thus, including the empty face,
\[
\widetilde L(g)=-\sum_{J\text{ compatible orbit families}}(-1)^{|J|}=-I(Q_g;-1).
\]
Here \(Q_g\) is the graph of admissible vertex orbits: an orbit containing an original graph edge is discarded; two remaining orbits are joined if some original edge runs between them. Compatibility in \(Q_g\) is exactly independence. Since the one nonzero reduced homology group lies in degree \(d_n\), \(\chi_n(g)=(-1)^{d_n}\widetilde L(g)=(-1)^{d_n+1}I(Q_g;-1)\).

**2. All rotations.** For \(g=r^a\) and \(d=\gcd(n,a)\), orbits in each of the two vertex layers are residue classes modulo \(d\). For \(d\ge5\), the orbit graph is precisely \(\operatorname{GP}(d,2)\). For \(d=1,2,3,4\), direct inspection after deleting any internally adjacent orbits gives signed independence evaluations \(1,-1,1,-1\), respectively. For \(d\ge5\), the nonequivariant sphere-wedge theorem yields
\[
I(\operatorname{GP}(d,2);-1)=(-1)^{d+1}\bigl(1-5\mathbf1_{5\mid d}\bigr).
\]
Indeed when \(5\nmid d\) the sphere dimension has the same parity as \(d\), and when \(d=5t\), four spheres in degree \(3t-1\) give signed independence evaluation \(4(-1)^t\). The same formula holds at \(d=1,2,3,4\). Combining with the preceding orbit-face identity gives the rotation character.

**3. Reflection orbit graph as a bounded-width strip.** For \(s_a=r^as\), every orbit pairs cyclic index \(i\) with \(a-i\), separately in the outer and inner layers. Odd \(n=2m+1\) has one reflection type; take \(a=0\) and columns \(0,\ldots,m\). Even \(n=2m\) has a vertex-axis type \(a=0\) with columns \(0,\ldots,m\) and an edge-axis type \(a=1\) with columns \(1,\ldots,m\). In every case the bulk orbit graph has edges \(u_ju_{j+1},u_jv_j,v_jv_{j+2}\). Its entire boundary alteration is:

* odd cycle: delete \(v_1,u_m\), add the edge \(v_{m-1}v_m\);
* even vertex axes: delete \(v_1,v_{m-1}\), with no extra edges;
* even edge axes: delete \(u_1,u_m\), add \(v_1v_2,v_{m-1}v_m\).

These statements follow by checking the two ends of the folded original outer cycle and step-two inner cycle. Edges incident to deleted vertices are also deleted. They apply without overlapping ends for odd \(n\ge11\) and even \(n\ge10\); smaller cases are separately included among exact base evaluations.

**4. Exact transfer identity and all-length recurrence.** On a bulk strip with successive choices \((u_j,v_j)\in\{(0,0),(1,0),(0,1)\}\), weight each occupied vertex by \(-1\). Immediately before column \(j\), the three-bit state is \((u_{j-1},v_{j-2},v_{j-1})\). A transition to \((u_j,v_j)\) is legal if \(u_ju_{j-1}=0\), \(v_jv_{j-2}=0\), and \(u_jv_j=0\). The new state is \((u_j,v_{j-1},v_j)\), and the transition weight is \((-1)^{u_j+v_j}\). This explicitly defines an integer \(8\times8\) transfer matrix \(T\), including the zero transitions. Direct integer multiplication proves
\[
\boxed{T^4(T^5+I_8)=0.}
\]
Equivalently, its characteristic polynomial is \(\lambda^4(\lambda^4-\lambda^3+\lambda^2-\lambda+1)\); Cayley–Hamilton and \((\lambda+1)(\lambda^4-\lambda^3+\lambda^2-\lambda+1)=\lambda^5+1\) imply the identity. The first and last two orbit columns determine fixed endpoint vectors \(\alpha,\beta\) for each reflection type, since all altered edges are supported there. If \(L\) is the total number of columns, their signed independent-set sum is \(\alpha T^{L-4}\beta\). Consequently it changes sign when five bulk columns are added whenever \(L\ge8\). Increasing \(n\) by ten adds exactly five columns of the same type; therefore
\[
I(Q_{s_a}(n+10);-1)=-I(Q_{s_a}(n);-1)
\]
for odd \(n\ge15\) and both even reflection types for \(n\ge16\). The finite remaining pairs below these bounds (\(n=11,12,13,14,15\)) are checked directly in the standalone script. Since \(d_{n+10}=d_n+6\), the reflection character also changes sign under \(n\mapsto n+10\). Hence it is periodic modulo twenty.

**5. Finite bases and character table.** The standalone checker computes the exact signed independent-set sum of the orbit graph, using deletion recurrence over all remaining vertices, for both reflection types at every \(5\le n\le24\). Applying \((-1)^{d_n+1}\) yields, in successive order \(n=5,6,\ldots,14\), the \(a=0\) character seeds
\[
(0,-1,1,1,-1,0,-1,-1,1,1),
\]
and for \(n=15,16,\ldots,24\),
\[
(0,1,-1,-1,1,0,1,1,-1,-1).
\]
When \(n\) is even, the \(a=1\) seed is the negative of the \(a=0\) seed; when \(n\) is odd, all reflections are conjugate. The strip recurrence propagates these exact seeds to every \(n\ge5\), proving the reflection table.

**6. Geometric quotient and comparison with a distinct cycle model.** A finite simplicial group action becomes admissible upon barycentric subdivision. Over \(\mathbb Q\), averaging makes invariants exact, so rational cohomology of the ordinary geometric quotient is the invariant cohomology of \(X_n\). If \(n\) is even, the nontrivial rotation parity, or the nontrivial five-point augmentation constituent when \(5\mid n\), gives no invariant. If \(n\) is odd and divisible by five, the four-dimensional rotation character has average zero. Otherwise the rotation action is trivial, and the invariant dimension is one precisely when the reflection trace is \(+1\). This gives exactly \(n\equiv1,7,13,19\pmod{20}\). The already published dihedral character for the *different* no-four-consecutive cycle complex has the same rotation and reflection values; equality of characters over \(\mathbb Q\) implies isomorphic representations, not an equivariant homotopy equivalence.

## Verification
Run `python3 verify_gp_dihedral.py` with Python 3 and the standard library only. It verifies the exact \(8\times8\) transfer identity, matches the reflection-quotient graph with the explicit strip model across 40 independent configurations, evaluates all reflection seeds and exceptional recurrence pairs exactly, and checks rotations for every dihedral rotation at \(5\le n\le22\), plus reflections at \(5\le n\le27\). `verification_output.txt` is the actual captured output from the included script. Finite tests do not prove the infinite theorem: its all-length step is the matrix identity plus the stated finite-range cap decomposition, and homology concentration is taken from the cited nonequivariant theorem.

## Relationship to prior work
Pandey introduced an exact transfer-matrix framework for independence polynomials of generalized Petersen graphs and reported finite numerical experiments; this does not calculate equivariant homology or geometric quotient cohomology. Youngsoo Kim subsequently determined the nonequivariant homotopy types of \(\operatorname{Ind}(\operatorname{GP}(n,2))\) for all \(n\ge5\); those homotopy types and dimensions are explicitly used as prior inputs. Earlier exact finite studies gave the dihedral character for \(\operatorname{GP}(7,2)\) and the orientation character for \(\operatorname{GP}(9,2)\). Another published theorem computes the complete dihedral character of the *distinct* cyclic no-four-consecutive complex and obtains the same mod-twenty invariant criterion. That theorem alone does not identify the dihedral action on the two-layer graph complex, and no equivariant equivalence between the two complexes is claimed or assumed. The new contribution is the uniform dihedral calculation for \(\operatorname{GP}(n,2)\) using its own orbit graphs and transfer identity, and the resulting representation coincidence. Unindexed equivariant equivalences or earlier graph-specific transfer calculations remain possible.

## Limitations
The statement is limited to the canonical \(D_n\) action, rational characters and additive rational quotient cohomology. It does not determine integral homology representation lattices, torsion or homotopy types of the quotient, or full automorphism-group representations for exceptional generalized Petersen graphs. It relies on a separately published nonequivariant homotopy classification and does not assert an equivariant collapse or map to the cycle no-four-run model. An independent mathematical audit and exhaustive historical-priority certification have not been performed.

## References
1. R. Pandey, *Parity-Dependent Real-Rootedness in Independence Polynomials of Generalized Petersen Graphs*, arXiv:2601.03293, first public 2026-01-05. https://arxiv.org/abs/2601.03293
2. Y. Kim, *Perfect matching complexes of antiprism graphs and independence complexes of generalized Petersen graphs \(GP(n,2)\)*, arXiv:2611.22021, first public 2026-11-17, Theorem 4.6. https://arxiv.org/abs/2611.22021
3. *Dihedral characters and mod-twenty quotient cohomology of three-independence cycle complexes*, publicly available 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-dihedral-characters-and-mod-twenty-quotient-cohomology-of-three--9cd4a2926fbd
4. *Equivariant higher-independence topology and persistence of \(GP(7,2)\)*, publicly available 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-equivariant-higher-independence-topology-and-persistence-of-gp-7--e4f2aa8011ee
5. *A vertex-essential \(5\)-sphere in the generalized Petersen independence complex*, publicly available 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-vertex-essential-5-sphere-in-the-generalized-petersen-independ--ff22c9a5b5b6
