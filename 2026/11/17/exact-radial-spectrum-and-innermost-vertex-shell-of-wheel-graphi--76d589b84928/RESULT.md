# Exact radial spectrum and innermost vertex shell of wheel graphical zonotopes

## Finding

For every integer \(m\ge4\), consider the wheel graph \(W_{m+1}=K_1\vee C_m\), with rim vertices \(0,1,\ldots,m-1\) in cyclic order and hub \(h\). Its **centered standard graphical zonotope** is
\[
 Z_m=\sum_{\{i,j\}\in E(W_{m+1})}
 [-\tfrac12,\tfrac12](e_i-e_j)\subset\mathbb R^{m+1}.
\]
The inner product is the ordinary ambient Euclidean one. Let \(\omega\) be an acyclic orientation of the wheel, \(k(\omega)\) the number of spokes pointing toward the hub, and \(s(\omega)\) the number of rim vertices which are sources or sinks of the **entire wheel orientation**. The corresponding zonotope vertex \(v_\omega\) satisfies the exact radial identity
\[
\boxed{4\|v_\omega\|_2^2=(2k(\omega)-m)^2+m+8s(\omega).}
\]
Moreover, a single fixed four-state transfer matrix counts the entire Euclidean vertex-radius distribution. With states ordered \((0,0),(0,1),(1,0),(1,1)\), put
\[
 M(u,v)=\begin{pmatrix}
 1&1&u&uv\\
 v&1&0&0\\
 0&0&u&uv\\
 v&1&u&u
 \end{pmatrix},\qquad
 F_m(u,v)=\operatorname{tr}\bigl(M(u,v)^m\bigr)-2(1+u^m).
\]
If \(N_m(k,s)=[u^kv^s]F_m(u,v)\), then \(N_m(k,s)\) is the **exact number of vertices** with the given hub-indegree and rim-extrema statistics. In particular, to obtain the multiplicity of any squared radius \(q/4\), sum \(N_m(k,s)\) over pairs satisfying \((2k-m)^2+m+8s=q\). The total number of vertices is \(F_m(1,1)=3^m-3\).

The innermost vertex shell has a particularly simple, sharp classification:
\[
 \boxed{\min_{z\in\operatorname{Vert}(Z_m)}\|z\|_2^2=
 \begin{cases}(m+16)/4,&m\text{ even},\\(m+17)/4,&m\text{ odd},\end{cases}}
\]
and its precise multiplicity is
\[
 \boxed{N_{\mathrm{inner}}(m)=
 \begin{cases}m^3/4,&m\text{ even},\\m(m^2-1)/2,&m\text{ odd}.\end{cases}}
\]
A vertex attains this minimum **exactly when** the hub indegree is as close to \(m/2\) as possible and the orientation has precisely one source and one sink, both on the rim. More precisely, for every \(1\le k\le m-1\),
\[
 \boxed{N_m(k,2)=m k(m-k).}
\]
The innermost **vertex** radius is not the inradius of the convex body: the body contains the origin in its relative interior.

## Assumptions and scope

The graph is simple and unweighted; \(m\ge4\) is an integer. For any simple graph, its centered standard graphical zonotope is the Minkowski sum of the displayed centered edge segments in the zero-sum subspace of its vertex-coordinate space. Every acyclic edge orientation produces one distinct exposed zonotope vertex, and all exposed vertices arise this way. The source/sink condition in \(s\) refers to all three incident edges of a rim vertex, including its spoke; the hub is deliberately not included in \(s\). The radius spectrum concerns **vertices**, not all points of the body. Vertex counts are labeled; no quotient by dihedral or reversal symmetries is taken.

## Proof

**1. Euclidean norm from indegrees.** For a graph orientation let \(d_i\) be the indegree of vertex \(i\) and let \(\deg(i)\) be its undirected degree. The signed endpoint of the centered zonotope is
\[
 v_\omega=\tfrac12\sum_{i\in V}\bigl(2d_i-\deg(i)\bigr)e_i.
\]
For the wheel, the hub degree is \(m\) and each rim vertex has degree three. The hub term is \((2k-m)^2\). The squared rim contribution \((2d_i-3)^2\) equals nine when \(d_i=0\) or \(3\), and one when \(d_i=1\) or \(2\). As the extreme cases are exactly rim sources and sinks, summing proves the radial identity. The correspondence between vertices and acyclic orientations is the standard graphical-hyperplane-arrangement correspondence: a generic linear functional determines an acyclic orientation through its signs on edge differences, and conversely every acyclic orientation has a topological-order potential exposing the corresponding signed endpoint.

**2. Acyclic wheel orientations in four local states.** For indices modulo \(m\), write \(a_i=1\) when spoke \(i\to h\), and \(a_i=0\) when \(h\to i\); write \(b_i=1\) when rim edge \(i\to i+1\), and \(b_i=0\) otherwise. A triangle \((i,h,i+1)\) is acyclic exactly when, whenever \(a_i\ne a_{i+1}\), one has \(b_i=a_i\). This excludes directed triangles. If the spoke word \((a_i)\) contains both signs, every directed rim path from a vertex with spoke \(h\to i\) to a vertex with spoke \(j\to h\) would have to cross a boundary \(a_i=0\), \(a_{i+1}=1\) against its rim arrow; hence no directed cycle can use the hub. The only remaining potential directed cycles are the two uniformly directed full rim cycles. They are possible only when every spoke sign agrees, and then occur for each of the two constant rim-edge words. Accordingly, four exceptional orientation words must be removed.

The local rim-extremum indicator is
\[
 s_i=\mathbf1_{\{(a_i,b_{i-1},b_i)=(1,0,1)\}}
 +\mathbf1_{\{(a_i,b_{i-1},b_i)=(0,1,0)\}}.
\]
Use \((a_{i-1},b_{i-1})\) as the previous state and \((a_i,b_i)\) as the new state. The transition weight is \(u^{a_i}v^{s_i}\) when the triangle condition at the preceding rim edge holds, and zero otherwise. In the stated four-state ordering, this gives precisely \(M(u,v)\). Tracing its \(m\)-th power sums the weights of all cyclic assignments. Removing the two constant rim words for each of the two constant spoke words subtracts \(2(1+u^m)\). Thus the coefficient of \(u^kv^s\) in \(F_m\) is exactly \(N_m(k,s)\). At \(u=v=1\), each spoke word that is not constant has \(2^{m-r}\) compatible rim words when it has \(r\) changes; direct two-state transfer evaluation (or the wheel's chromatic polynomial at \(-1\)) gives \(3^m-3\) acyclic orientations. This last total is included as a consistency check, not presented as a new enumeration theorem.

**3. At least two rim extrema for mixed spokes.** Suppose \(0<k<m\). Every finite acyclic directed graph has a source and a sink. Since the hub has both incoming and outgoing spokes, it can be neither; thus \(s\ge2\). A more precise argument refines this lower bound. In the cyclic spoke word, write \(r\ge1\) for the number of runs of ones; the number of zero runs is also \(r\). At a boundary from zero to one, the triangle constraint forces the rim-edge bit to be zero; at a boundary from one to zero, it forces the bit to be one. Hence along every one-run the successive rim bits must change from zero to one at least once, producing a rim source; along every zero-run they must change from one to zero at least once, producing a rim sink. Thus \(s\ge2r\).

Equality \(s=2\) requires exactly one run of \(k\) ones and exactly one run of \(m-k\) zeros, with exactly one bit change within each run. There are \(m\) choices of the starting point of the one-run, \(k\) choices for its unique zero-to-one bit transition, and \(m-k\) choices for the unique one-to-zero transition in the other run. These choices are bijective with orientations counted by \(N_m(k,2)\), proving \(N_m(k,2)=mk(m-k)\).

**4. Boundary spokes and global minimization.** If \(k=0\) or \(k=m\), the hub is a source or a sink and acyclicity of the rim forces at least one rim sink or source, respectively. Hence \(s\ge1\) and
\[
4\|v\|^2\ge m^2+m+8.
\]
For every \(m\ge4\), this bound is strictly greater than \(m+16\) when \(m\) is even and than \(m+17\) when \(m\) is odd. For mixed spokes, \(s\ge2\) and
\[
4\|v\|^2\ge(2k-m)^2+m+16.
\]
Its minimum over integral \(k\) with \(1\le k<m\) is \(m+16\) when \(m\) is even (at \(k=m/2\)) and \(m+17\) when \(m\) is odd (at the two nearest half-integers). The one-run constructions of Step 3 attain \(s=2\) at all those \(k\), proving sharpness, classification, and the displayed minimum-radius formulas. At an even \(m\), their count is \(m(m/2)^2=m^3/4\); at odd \(m\), the two values of \(k\) contribute a combined \(2m(m^2-1)/4=m(m^2-1)/2\). No other vertices attain the same minimum because all inequalities were sharp only in these cases.

## Verification

The included file `verify_wheel.py` uses standard Python 3 only and directly enumerates **all** orientations of the \(2m\) wheel edges for each \(4\le m\le9\). Acyclicity is checked independently by Kahn's topological algorithm; Euclidean squared norms are computed from direct graph indegrees, while a separate transfer-matrix dynamic program computes \(F_m\). The program verifies the complete coefficient table \(N_m(k,s)\), the one-source/one-sink count, first-shell radius, first-shell multiplicity and total vertex count. Run in this directory using `python3 verify_wheel.py`.

The run checked **349,440 directed-edge assignments**, of which **29,466 were acyclic**, together with **231 polynomial and boundary assertions**. For \(m=4,5,6,7,8,9\), the innermost counts are respectively \(16,60,54,168,128,360\). These finite checks do not replace the all-dimensional proof.

## Relationship to prior work

The known bijection between acyclic orientations and vertices of graphical zonotopes supplies the starting point; classical results count all acyclic orientations or orientations with prescribed sources and sinks. Mühlherr and Poullot (2026) study the flip graph and acyclic polynomials, not a Euclidean vertex-radius invariant in the available abstract. The general graphical-zonotope framework is developed by Padrol, Pilaud and Poullot. A previously published universal cone theorem determines the **maximum** Euclidean radius and its farthest-vertex equality cases for \(K_1\vee H\), but its maximum-radius implication does not determine the **minimum among vertex norms** or the complete two-variable wheel radius generating function proved here. The earlier wheel symmetric-edge-polytope results concern a different convex body, not the Minkowski sum of edge segments used here. The overall count \(3^m-3\) is known and not claimed as independently new.

## Limitations

The theorem applies to unit-weight wheels with at least four rim vertices and the standard Euclidean inner product. It does not classify the inradius, arbitrary weighted wheels, or other graph joins. Radius multiplicities for coincident values of \((2k-m)^2+m+8s\) must be aggregated from the displayed coefficient table. The original full-length 2026 motivating preprint was not available for complete manuscript inspection during this comparison, and novelty cannot be certified solely by searches or abstracts. No independent mathematical audit has been performed.

## References

1. L. Mühlherr and G. Poullot, *Hamiltonicity of graphs of acyclic orientations and acyclic polynomials*, arXiv:2609.02249, first public version 2026-09-02, https://arxiv.org/abs/2609.02249.
2. A. Padrol, V. Pilaud and G. Poullot, *Deformed graphical zonotopes*, Discrete & Computational Geometry (2023), arXiv:2111.12422, https://arxiv.org/abs/2111.12422.
3. F. Chapoton and V. Pilaud, *Shuffles of deformed permutahedra, multiplihedra, constrainahedra, and biassociahedra*, arXiv:2201.06896, https://arxiv.org/abs/2201.06896.
4. Prior published finding, *Universal Euclidean cone law and farthest-point rigidity for graphical zonotopes*, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-universal-euclidean-cone-law-and-farthest-point-rigidity-for-gra--19096c28cee4/RESULT.md.
5. C. Greene and T. Zaslavsky, *On the interpretation of Whitney numbers through arrangements of hyperplanes, zonotopes, non-Radon partitions, and orientations of graphs*, Transactions of the AMS 280 (1983), 97–126.
