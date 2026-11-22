# Sharp nonreentrant RK4 positivity horizon on every positive-weighted tree

## Finding
Let \(T=(V,E,w)\) be a finite undirected tree with at least two vertices and strictly positive symmetric edge conductances \(w_{uv}\). Put \(d_u=\sum_{v\sim u}w_{uv}\), \(L=\operatorname{diag}(d)-W\), and \(B=\operatorname{diag}(d)+W\). The completed classical fourth-order Runge–Kutta graph-heat step is
\[
K(h)=I-hL+\frac{h^2}{2}L^2-\frac{h^3}{6}L^3+\frac{h^4}{24}L^4,\quad h\ge0.
\]
For each edge \(e=uv\), set \(s_e=d_u+d_v\), \(c_e=(B^3)_{uv}/w_{uv}\), and \(b_e=(B^4)_{uv}/w_{uv}\), and define
\[
g_e(h)=1-\frac{s_eh}{2}+\frac{c_eh^2}{6}-\frac{b_eh^3}{24}.
\]
Every \(g_e\) is strictly decreasing for all real \(h\), with one positive zero \(\rho_e\). For each three-edge simple path \(P=(z_0,z_1,z_2,z_3)\), set \(\eta_P=4/(d_{z_0}+d_{z_1}+d_{z_2}+d_{z_3})\). Write \(H_1=\min_{e\in E}\rho_e\) and \(H_3=\min_{P:\,|P|=3}\eta_P\), defining the minimum over no paths as \(+\infty\). Then the **entire** positivity set is
\[
\boxed{K(h)\text{ is entrywise nonnegative}\quad\Longleftrightarrow\quad 0\le h\le\min\{H_1,H_3\}.}
\]
Whenever nonnegative, the update is also stochastic since \(K(h)\mathbf1=\mathbf1\). No positivity recovery occurs. For every \(h>0\), entries joining vertices at distances two or four are strictly positive, diagonal entries are strictly positive, and entries at distances greater than four vanish. Only edges and distance-three pairs can ever become negative.

Both mechanisms occur with positive, nonuniform weights: on a four-vertex path with weights \((1,1,1)\), distance three controls \(h_*=2/3\). With weights \((4,1,1)\), an edge controls, at the unique positive zero \(h_*=0.3141299625\ldots\) of \(1-9h/2+13h^2-673h^3/24\), strictly less than the distance-three bound \(1/3\).

## Assumptions and scope
All vertex and edge sets are finite; the underlying graph is connected, undirected and acyclic, with strictly positive real conductances. Conductances need not be rational, equal, normalized or bounded away from zero uniformly over different trees. The claim concerns entrywise nonnegativity of the **completed** linear RK4 update, not internal RK stages, nonlinear dynamics or spectral contractivity. There are no restrictions on topology, number of vertices, degrees or the range of \(h\ge0\).

## Proof
**Bipartite sign transform and distance parity.** Choose a diagonal signature \(J\) whose entries are \(+1\) and \(-1\) on the two color classes. Then \(L=JBJ\). The signless Laplacian \(B\) is entrywise nonnegative, and every \(B^k_{uv}\) is a sum of nonnegative weighted walks with optional stays carrying weights \(d_z\). For vertices in opposite colors, \((L^k)_{uv}=-(B^k)_{uv}\), and for vertices in the same color the sign is positive. Terms of order at most four vanish beyond distance four.

**Distance three and four.** On the unique three-edge path \(P=(z_0,z_1,z_2,z_3)\), let \(p_P=\prod_{i=0}^{2}w_{z_i z_{i+1}}>0\). The only allowed contributions through degree four are the three edge traversals, optionally with one degree stay. Consequently
\[
K(h)_{z_0z_3}=\frac{p_Ph^3}{24}\left(4-h\sum_{i=0}^3d_{z_i}\right).
\]
Its sign changes once, exactly at \(\eta_P\). For distance four, the unique four-edge walk gives \(K(h)_{uv}=h^4(B^4)_{uv}/24>0\).

**Distance two.** For the unique two-edge path \((u,z,v)\), let \(p=w_{uz}w_{zv}\), \(s=d_u+d_z+d_v\) and \(H=\sum_{0\le i\le j\le2}d_{z_i}d_{z_j}\), with \((z_0,z_1,z_2)=(u,z,v)\). The two-edge traversal with up to two stays yields
\[
K(h)_{uv}=\frac{ph^2}{24}\left(12-4sh+\frac{(B^4)_{uv}}p h^2\right),\quad \frac{(B^4)_{uv}}p\ge H.
\]
Since \(H=(s^2+d_u^2+d_z^2+d_v^2)/2\ge2s^2/3\), the discriminant of \(12-4sh+Hh^2\) is at most \(-16s^2<0\). Thus every distance-two entry is strictly positive for all positive \(h\).

**Edge cubics: the weighted inequality.** Fix \(e=uv\), write \(x=d_u\), \(y=d_v\), \(w=w_{uv}\), and let \(U=\sum_{z\sim u,z\ne v}w_{uz}^2\), \(V=\sum_{z\sim v,z\ne u}w_{vz}^2\). The tree has no alternative three-edge path from \(u\) to \(v\). Direct enumeration of one-edge paths with stays and three-edge paths with one stay gives
\[
\begin{aligned}
c_e&=x^2+xy+y^2+w^2+U+V,\\
b_e&=(x+y)(x^2+y^2+2w^2+U+V)\\
&\quad+\sum_{z\sim u,z\ne v}w_{uz}^2(x+d_z)
+\sum_{z\sim v,z\ne u}w_{vz}^2(y+d_z).
\end{aligned}
\]
As \(w^2+U\le x^2\) and \(w^2+V\le y^2\), we have \(3xy\le c_e\le2(x+y)^2-3xy\). Moreover \(b_e\ge(x+y)(c_e-xy)\). Therefore, with \(s=x+y>0\),
\[
\frac{c_e^2}{c_e-xy}=c_e+xy\frac{c_e}{c_e-xy}
\le 2s^2-3xy+\frac32xy<2s^2,
\]
where \(c_e/(c_e-xy)\le3/2\) follows from \(c_e\ge3xy\). Hence \(c_e^2<2sb_e\). The derivative
\[
g'_e(h)=-\frac s2+\frac{c_e h}{3}-\frac{b_e h^2}{8}
\]
has strictly negative discriminant \(c_e^2/9-sb_e/4<0\) and a negative leading coefficient, so it is negative on all of \(\mathbb R\). The cubic decreases from \(g_e(0)=1\) to negative infinity and has exactly one positive zero. The corresponding transition is \(K(h)_{uv}=h w_{uv}g_e(h)\).

**Diagonals and conclusion.** The weighted Laplacian \(L\) is symmetric positive semidefinite. For each \(z\ge0\), its scalar RK4 polynomial satisfies
\[
24\sum_{k=0}^4\frac{(-z)^k}{k!}=(z^2-2z+2)^2+4((z-2)^2+1)>0.
\]
Thus \(K(h)\) is positive definite for all \(h\ge0\), in particular each diagonal is positive. The distance classification exhausts all matrix entries, and each potentially negative entry has one permanent sign transition. Their minimum is the stated exact nonreentrant horizon. This proves the claim for all finite positive-weighted trees and all \(h\ge0\).

## Verification
Run `python3 verify.py` using the Python 3 standard library from the same folder. The supplied script constructs weighted Laplacians and signless Laplacian powers by independent exact rational matrix multiplication, checks all coefficient identities and strict edge discriminants over 629 generated trees, and checks 16,090 exact vertex pairs. Its actual recorded output is in `verification.log`: `VERIFY_OK trees=629 exact_vertex_pairs=16090`. The code's rational samples cannot prove the real-weight or unbounded-tree theorem; those follow from the preceding symbolic inequalities and walk enumeration.

For the four-vertex path with weights \((4,1,1)\), the first edge has \((s,c,b)=(9,78,673)\), so its cubic has a unique root \(0.3141299625\ldots\). Its value at \(h=1/3\) is negative, whereas other edge roots exceed \(1/3\), making it the controlling transition. This is a weighted-only witness distinguishing the two possible obstructions.

## Relationship to prior work
Two closely related published classifications cover **unweighted** graphs: *Exact local RK4 positivity horizons on every finite tree* (2026) and *A local all-step RK4 positivity law for every unweighted bipartite network* (2026). Both explicitly exclude variable positive edge conductances. Their edge/distance-three mechanisms motivate the question but their unit-edge cubic estimates do not imply the weighted discriminant \(c_e^2<2(d_u+d_v)b_e\) or its global monotonicity. The present theorem covers all conductance ratios, including the example with weights \((4,1,1)\).

Horváth–Song–Terlaky (2014) provide general polynomial-invariance threshold machinery, including first-root tests, but do not establish the weighted-tree locality, universal global single crossing or the all-timestep classification here. Blanes–Iserles–Macnamara (2021) study positivity-preserving integrators for graph-Laplacian-structured ODEs but do not give this exact weighted-tree RK4 endpoint characterization. These are implication-level comparisons against inspected material, not a claim of exhaustive priority verification.

## Limitations
The theorem is specific to undirected positively weighted **trees** and completed classical RK4. It does not cover general cyclic graphs, negative conductances, directed chains, state-dependent generators, internal stages or positivity for different time steppers. It does not assert that the RK4 stability region or a forward-Euler CFL bound is sharp here. Potential uncatalogued literature and equivalences through weighted multigraph approximations remain historical-priority risks; an independent mathematical audit has not been performed.

## References
1. S. Blanes, A. Iserles and S. Macnamara, *Positivity-preserving methods for ordinary differential equations*, arXiv:2102.08242, first submitted 2021-02-16, https://arxiv.org/abs/2102.08242 .
2. Z. Horváth, Y. Song and T. Terlaky, *Steplength thresholds for invariance preserving of discretization methods of dynamical systems on a polyhedron*, arXiv:1406.6755, first submitted 2014-06-26, https://arxiv.org/abs/1406.6755 .
3. *Exact local RK4 positivity horizons on every finite tree*, published-finding corpus (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-local-rk4-positivity-horizons-on-every-finite-tree--2042521dfc9d .
4. *A local all-step RK4 positivity law for every unweighted bipartite network*, published-finding corpus (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-local-all-step-rk4-positivity-law-for-every-unweighted-biparti--9b715f55a0bc .
