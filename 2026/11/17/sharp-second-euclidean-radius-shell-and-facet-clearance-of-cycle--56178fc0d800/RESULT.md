# Sharp second Euclidean radius shell and facet clearance of cycle Lipschitz polytopes

## Finding
For an integer \(n\ge4\), let \(H_0=\{x\in\mathbb R^n:\sum_{i=0}^{n-1}x_i=0\}\), with the inherited Euclidean metric, and let
\[
Q_n=\left\{x\in H_0:|x_{i+1}-x_i|\le1\ (i\in\mathbb Z/n\mathbb Z)\right\}.
\]
This is the polar, in \(H_0\), of the unweighted cycle's symmetric edge polytope \(P_n=\operatorname{conv}\{\pm(e_i-e_{i+1}):i\in\mathbb Z/n\mathbb Z\}\). Define the largest squared norm of a vertex by \(M_n\), and the second-largest **distinct** squared norm of a vertex by \(S_n\). Then
\[
\boxed{\begin{aligned}
M_{2m}&=\frac{m(m^2+2)}6,&
S_{2m}&=M_{2m}-\frac{2(m-1)^2}{m}&& (m\ge2),\\
M_{2m+1}&=\frac{m(m+1)(m^2+m+1)}{3(2m+1)},&
S_{2m+1}&=M_{2m+1}-\frac{2m(m-1)}{2m+1}&& (m\ge2).
\end{aligned}}
\]
The values \(M_n\) and the maximizers are known from the inradius of \(P_n\); the contribution here is the exact *next* radial shell \(S_n\), its sharp positive deficit and its equality cases.

A vertex \(x\in Q_n\) is identified with its circular step word \(\delta_i=x_{i+1}-x_i\). For even \(n=2m\), the top shell has all cyclic rotations of \(+^m-^m\), and the next shell has exactly those balanced sign words whose \(m\) plus positions, in cyclic order, have excess gaps \((m-1,1,0,\ldots,0)\), up to cyclic permutation of the gaps. For odd \(n=2m+1\), write \(S\) for the \(m+1\) positions with nonnegative steps and \(z\in S\) for the unique zero position. The top shell has \(S\) consecutive and \(z\) at an endpoint. The next shell consists of either (i) \(S\) consecutive with \(z\) immediately next to an endpoint, or (ii) \(S\) obtained from \(m+2\) consecutive positions by deleting the position immediately next to one endpoint, with that endpoint equal to \(z\). Identical cyclic words are counted once. The number of second-shell vertices is \(2\) for \(n=4\), \(2n\) for even \(n\ge6\), \(2n\) for \(n=5\), and \(4n\) for odd \(n\ge7\).

Equivalently, every **non-tangent** facet of \(P_n\) lies at intrinsic distance at least \(S_n^{-1/2}\) from the origin, and some lie at exactly that distance. The nearest facets lie at distance \(M_n^{-1/2}\). Thus the exact strict next-facet clearance is \(S_n^{-1/2}-M_n^{-1/2}>0\). The claim concerns vertices/facets, not arbitrary continuous points of the polytopes.

## Assumptions and scope
All cycles are simple and unweighted, with \(n\ge4\). Edges and coordinates are ordered cyclically, and norms are those of \(H_0\), not a quotient-space coordinate norm. A cyclic word has exactly \(m\) plus and \(m\) minus steps when \(n=2m\), and exactly \(m\) plus, \(m\) minus and one zero step when \(n=2m+1\). These are precisely the vertices of \(Q_n\), by the standard cycle facet-label theorem, or directly by the rank of active edge inequalities with the closure relation \(\sum_i\delta_i=0\). For odd orders the zero step is forced by the vertex condition. The radius \(M_n^{1/2}\) is a previously evaluated extremum; no priority is claimed for it.

## Proof
**1. An exact discrete Green energy.** Put \(f_n(d)=d(n-d)\) for \(0\le d\le n\). The Green kernel of the cyclic Laplacian, on the zero-mean subspace, is
\[
G_{ij}=\frac{n^2-1}{12n}-\frac{f_n(d)}{2n},\qquad d\equiv j-i\pmod n,\quad 0\le d<n.
\]
Indeed \(G\mathbf1=0\), and the cyclic second difference of each column is \(\delta_{ij}-1/n\), so \(G=L_{C_n}^{+}\). For a closed step word \(\delta\) and its unique mean-zero height vector \(x\), we have \(\|x\|^2=\delta^{\mathsf T}G\delta\). Notice that the result is unchanged by reversing cyclic distance because \(f_n(d)=f_n(n-d)\).

**2. Even orders.** If \(n=2m\), let \(A\) be the set of \(m\) plus-step positions and write \(\delta=2\mathbf1_A-\mathbf1\). As \(G\mathbf1=0\),
\[
\|x\|^2=C_{n,m}-\frac4n E(A),\qquad
E(A)=\sum_{\{i,j\}\subset A} f_n((j-i)\bmod n),
\]
where the constant depends only on \(n,m\). Arrange the marked positions cyclically and let their \(m\) positive successive gaps be \(g_1,\ldots,g_m\), summing to \(2m\). Put \(r_i=g_i-1\), so \(r_i\ge0\) and \(\sum_i r_i=m\). For fixed cyclic labeling of the marks, \(E\) is a strictly concave quadratic in \(g\): each summand is a positive coefficient times \(f_n\) of a consecutive gap sum; the adjacent marked-pair terms give strictly negative quadratic curvature in every nonzero direction on \(\sum_i g_i=2m\). Therefore \(E\) takes its minimum over the gap simplex at an extreme point \(r=(m,0,\ldots,0)\), corresponding to consecutive plus positions. This yields the known maximum \(M_{2m}\).

For any *nonconsecutive* \(A\), all coordinates satisfy \(r_i\le m-1\). The capped simplex \(r_i\ge0\), \(\sum_i r_i=m\), \(r_i\le m-1\) is exactly the convex hull of its near-vertex vectors \((m-1,1,0,\ldots,0)\), with coordinates permuted. By strict concavity no other admissible gap vector can yield the minimum over this capped domain. Under rotation and reflection, such a near-vertex word has plus set
\[
A_r=\{0,1,\ldots,m-1\}\setminus\{m-r\}\cup\{m\},\qquad 1\le r\le m-1.
\]
Substituting this word into the Green energy (equivalently, summing the centered heights) gives the **exact** loss
\[
M_{2m}-\|x(A_r)\|^2=\frac{2(m-1)r(m-r)}m.
\]
The positive concave integer product \(r(m-r)\) is smallest exactly at \(r=1\) or \(r=m-1\), hence the stated \(S_{2m}\), equality classification and the counts \(2\) at \(n=4\), \(2n\) for even \(n\ge6\).

**3. Odd orders.** Put \(n=2m+1\), and let \(A\) be the \(m\) plus-step positions, \(z\) the one zero-step position, and \(S=A\cup\{z\}\). Then \(\delta=2\mathbf1_S-\mathbf e_z-\mathbf1\). The Green identity becomes
\[
\|x\|^2=C'_n-\frac4n F(S,z),\quad
F(S,z)=\sum_{\{i,j\}\subset S}f_n((j-i)\bmod n)
-\frac12\sum_{i\in S\setminus\{z\}}f_n((i-z)\bmod n).
\]
Each pair of marked positions has a strictly positive weight in \(F\): weight \(1/2\) when one of the pair is \(z\), and weight \(1\) otherwise. For a fixed cyclic ordering of the \(m+1\) marked positions including distinguished \(z\), \(F\) is therefore strictly concave in the positive successive gaps. Their excesses over \(1\) sum to \(m\). Its unrestricted minimum occurs when all excess falls in one gap: \(S\) is consecutive. If \(S\) is not consecutive, the same capped-simplex argument reduces its minimum to a near-vertex excess pattern \((m-1,1,0,\ldots,0)\). Hence it suffices to compare these two classes; strict concavity excludes any additional equality cases.

For consecutive \(S\), take \(S=\{0,\ldots,m\}\) and \(z=h\) with \(0\le h\le m\). Direct evaluation gives
\[
M_{2m+1}-\|x\|^2=\frac{2m h(m-h)}{2m+1}.
\]
The endpoints \(h=0,m\) give the already-known maximum, and the smallest positive loss is \(2m(m-1)/(2m+1)\), attained exactly at \(h=1,m-1\).

For a nonconsecutive near-vertex \(S\), cyclic rotation puts
\[
S=\{0,1,\ldots,q\}\setminus\{h\},\quad q=m+1,\quad 1\le h\le q-1.
\]
For fixed \(S\), minimizing \(F\) in the choice of \(z\) is equivalent to maximizing \(T_j=\sum_{i\in S\setminus\{j\}}f_n(|j-i|)\) over \(j\in S\). Define \(A(t)=\sum_{d=1}^t d(2q-1-d)\). An exact expression is
\[
T_j=A(j)+A(q-j)-f_n(|j-h|),\qquad j\in S.
\]
On each of the integer intervals \([0,h-1]\) and \([h+1,q]\), this is strictly convex (its quadratic second difference is \(2(q-1)>0\)). Its maxima there are endpoints. The endpoint comparisons are
\[
T_0-T_{h-1}=(q-h)(h-1)(q-3)\ge0,\qquad
T_q-T_{h+1}=h(q-h-1)(q-3)\ge0,
\]
for \(q\ge3\). Thus a global maximizing zero position may always be taken at one of the outer endpoints \(0,q\). By reflection, take \(z=0\). The exact loss then is
\[
M_{2m+1}-\|x\|^2=
\frac{2(m+1-h)(h(2m-1)-m)}{2m+1}.
\]
This expression is concave in \(h\in[1,m]\). Its two endpoint values are \(2m(m-1)/(2m+1)\) and \(4m(m-1)/(2m+1)\); hence the unique minimum is at \(h=1\). Reflection gives the counterpart with \(z=q\). For \(m=2\), the two descriptions of the second-shell step words coincide cyclically, yielding \(2n\) distinct words; for \(m\ge3\) they form disjoint cyclic families, each of size \(2n\), yielding \(4n\). This establishes the odd assertion.

**4. Facet clearance.** Polarity gives an inclusion-reversing bijection between vertices \(x\) of \(Q_n\) and facets \(\{y\in P_n:\langle x,y\rangle=1\}\). Its hyperplane has intrinsic distance \(1/\|x\|\) from the origin. Applying the exact first and second vertex-norm shells proves the claimed two nearest facet-distance values and the strict clearance. \(\square\)

## Verification
The standalone Python 3 checker `artifacts/verify.py` uses exact rational arithmetic. For each order \(4\le n\le15\), it enumerates **every** allowed cyclic step word and verifies the two distinct leading squared norms and all corresponding multiplicities. It additionally evaluates the three representative deficit identities for \(2\le m\le30\). Successful replay prints `CYCLE_SECOND_RADIAL_SHELL_CHECKS_PASSED exhaustive_vertex_profiles=71768 gap_formula_profiles=1334 orders=12`. The all-order claims follow from the proof, not from these finite checks.

## Relationship to prior work
D'Alì, Delucchi and Michałek give the cycle facet-label combinatorics and explain the identification with graph-metric Lipschitz/Kantorovich--Rubinstein polytopes. Jevtić, Timotijević and Živaljević study weighted-cycle Kantorovich--Rubinstein polytopes, primarily through their Bier-sphere boundary combinatorics; Chen, Davis and Korchevskaia study facet-subgraph structure. None of those inspected cycle discussions evaluates the next Euclidean radial shell. A directly related earlier result, *Cycle symmetric edge polytopes have a parity-split exact Euclidean inradius*, establishes the **largest** normal norm \(M_n\), its maximizing walks, the inradius and its tangent facets. That work is strictly stronger on maximal-ball center structure, but does not determine \(S_n\), the sharp non-tangent clearance, or the next-shell equality configurations. The present work credits rather than claims the leading shell. The new strict deficit is not implied by merely knowing its maximizers and radius.

## Limitations
The strict gap applies only to the **finite set of vertices** of \(Q_n\) (equivalently, facets of \(P_n\)). Continuous interior points can have all intermediate squared norms. The formulas concern unit edge lengths in the standard root realization and do not automatically extend to weighted cycles or different Euclidean embeddings. The literature check cannot rule out a differently named second-extremal cyclic-walk variance identity. Independent mathematical verification has not been performed.

## References
1. A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193, first public version 2019-10-11; especially the facet theorem and even-cycle section.
2. F. D. Jevtić, M. Timotijević and R. T. Živaljević, *Polytopal Bier spheres and Kantorovich--Rubinstein polytopes of weighted cycles*, arXiv:1812.00397, first public version 2018-12-02.
3. T. Chen, R. Davis and E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315, first public version 2021-07-26.
4. *Cycle symmetric edge polytopes have a parity-split exact Euclidean inradius*, available at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-cycle-symmetric-edge-polytopes-have-a-parity-split-exact-euclide--07f34c5bcbf4 (prior maximum-shell result; not independently audited here).
