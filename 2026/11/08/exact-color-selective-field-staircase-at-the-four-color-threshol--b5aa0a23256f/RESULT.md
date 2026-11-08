# Exact color-selective field staircase at the four-color threshold of the icosahedron

## Finding
Place four named Potts states \(0,1,2,3\) on the vertices of the twelve-vertex icosahedral graph \(I\), with uniform antiferromagnetic interaction \(J>0\) and external field \(h\ge0\) favoring color \(0\):
\[
 H_{J,h}(\sigma)=J\sum_{\{u,v\}\in E(I)}\mathbf1_{\sigma_u=\sigma_v}-h\sum_{v\in V(I)}\mathbf1_{\sigma_v=0}.
\]
Put \(x=h/J\). Its exact ground energy for every real \(x\ge0\) is
\[
 rac{E_0(h)}J=\min\{-3x,\;1-4x,\;5-6x,\;11-8x,\;15-9x,\;30-12x\}.
\]
The only transition fields are \(x=1,2,3,4,5\). On the successive open plateaux \(0<x<1,1<x<2,2<x<3,3<x<4,4<x<5,x>5\), the favored-color populations are respectively \(3,4,6,8,9,12\), and the exact numbers of labeled ground configurations are \(240,1080,6840,1620,540,1\). At the five transition fields, the complete counts of degenerate ground configurations are \(1320,15480,17100,2160,901\), respectively. At \(x=2\), the only additional intermediate favored-color sector is \(5\) with multiplicity \(7560\); at \(x=3\), it is \(7\) with multiplicity \(8640\); at \(x=5\), sectors \(10\) and \(11\) contribute \(324\) and \(36\). At zero field, all \(240\) proper four-colorings are ground states and each named color occurs exactly three times.

## Assumptions and scope
The icosahedral graph is the simple, undirected, twelve-vertex, thirty-edge, five-regular graph; vertices and colors are labeled. The field is nonnegative and couples to occupancy of a single distinguished color, not to a vector spin. There is no bulk/thermodynamic-limit phase transition claim. Ground-state degeneracies count every labeled assignment exactly once (no quotient by automorphisms or color permutations).

## Proof
For a coloring \(\sigma\), define integer observables \(f(\sigma)=|\{v:\sigma_v=0\}|\) and \(c(\sigma)=|\{uv\in E(I):\sigma_u=\sigma_v\}|\). At fixed \(f\), minimize \(c\) and denote the result \(m_f\) and its number of achieving assignments \(d_f\). The complete exact constrained profile, listed in increasing \(f=0,1,\ldots,12\), is
\[
(m_f)=(3,2,1,0,1,3,5,8,11,15,20,25,30),
\]
\[
(d_f)=(120,720,1080,240,1080,7560,6840,8640,1620,540,324,36,1).
\]
For mathematical completeness, this finite profile follows from the exhaustive recurrence: enumerate vertex colors in the fixed order \(0,1,\ldots,11\); after assigning vertex \(i\) color \(a\in\{0,1,2,3\}\), increment \(f\) by \(\mathbf1_{a=0}\) and increment \(c\) by \(\sum_{j<i,\{i,j\}\in E(I)}\mathbf1_{\sigma_j=a}\). At depth \(12\), update the exact minimum and equality count for the resulting value of \(f\). Every labeled assignment appears exactly once, and each edge is counted once upon adding its later endpoint. The full recurrence is executed by `ico_q4_check_a.cpp` with the complete thirty-edge table. Independently, `ico_q4_check_b.cpp` generates all thirty edges from two staggered pentagons and the two polar vertices, enumerates all \(4^{12}=16,777,216\) colorings using packed two-bit symbols, and obtains the identical profile. Both programs terminate with exact integer assertions.

At any \(x\ge0\), minimizing \(H/J=c-xf\) is equivalent to minimizing the thirteen affine functions \(m_f-xf\). The lower envelope is exactly the six displayed lines, as verified by comparing the thirteen integer slopes/intercepts. The successive intersections are \(x=1,2,3,4,5\). The constrained counts \(d_f\) add at equality. In particular, intermediate sectors \(f=5,7,10,11\) touch the envelope only at the stated crossings, and no other sectors can minimize. This proves the energy formula, every interval, and all critical-field counts.

## Verification
Two independent exact enumerators are embedded. Run `g++ -O3 -std=c++17 ico_q4_check_a.cpp -o check_a && ./check_a` and analogously compile/run `ico_q4_check_b.cpp`. One is recursive with an explicit edge table, the other a packed-color integer sweep with a separate geometric construction. Both independently confirm every one of the thirteen minimizing edge penalties and corresponding degeneracies. A geometric isomorphism check of the two graph constructions against the canonical icosahedral graph also passed. The finite exhaustive recurrence proves this finite-graph result; no infinite-size extrapolation is inferred.

## Relationship to prior work
Park's three-state triangular-lattice Potts study concerns a periodic lattice and a different number of colors. Konstantinidis's icosahedral articles analyze classical or quantum *Heisenberg* spins and their field-induced magnetization structure; those continuously oriented/quantum spins are not the discrete four-state Potts assignments counted here. Earlier three-color calculations on the icosahedral graph use a *frustrated* alphabet with \(q=3\); they do not determine this chromatic-threshold \(q=4\) enumeration, where proper zero-energy colorings exist and have the rigid population vector \((3,3,3,3)\). The result is a complementary finite-cluster benchmark, not an assertion about uniqueness among all unpublished graph-coloring databases.

## Limitations
This is one twelve-site cluster, at zero temperature and nonnegative field. It does not determine a positive-temperature critical point or the general \(q\)-state field model. A previously unindexed four-color partition-function table might independently encode some coefficients; independent historical-priority assessment remains necessary. Scientific correctness of finite enumeration is distinct from historical novelty.

## References
- H. Park, *The three-state Potts model on a triangular lattice*, arXiv:cond-mat/9311055, first posted 1993-11-24, https://arxiv.org/abs/cond-mat/9311055.
- N. P. Konstantinidis, *The Antiferromagnetic Heisenberg Model on Clusters with Icosahedral Symmetry*, arXiv:cond-mat/0503658, first posted 2005-03-29, https://arxiv.org/abs/cond-mat/0503658.
- N. P. Konstantinidis, *Antiferromagnetic Heisenberg Model on the Icosahedron: Influence of Connectivity and the Transition from the Classical to the Quantum Limit*, arXiv:1410.3444, first posted 2014-10-13, https://arxiv.org/abs/1410.3444.
