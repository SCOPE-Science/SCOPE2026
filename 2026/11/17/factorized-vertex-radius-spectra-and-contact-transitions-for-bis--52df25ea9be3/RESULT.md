# Factorized vertex-radius spectra and contact transitions for bistar edge-diamond polytopes

## Finding
For integers \(p,q\ge1\), let \(B_{p,q}\) denote the **bistar** tree with adjacent hubs \(a,b\), \(p\) distinct leaves adjacent only to \(a\), and \(q\) distinct leaves adjacent only to \(b\). In the standard orthonormal coordinate system indexed by the \(p+q+2\) vertices, form the Minkowski sum of coordinate diamonds
\[
P_{p,q}=\sum_{\{i,j\}\in E(B_{p,q})}\operatorname{conv}\{e_i,-e_i,e_j,-e_j\}\subset\mathbb R^{p+q+2}.
\]
Let \(F_{p,q}(z)=\sum_{x\in\operatorname{Vert}(P_{p,q})}z^{\|x\|_2^2}\) count vertices by **integer squared Euclidean radius**. For \(m\ge1\) and \(\delta\in\{0,1\}\), set
\[
A_{m,\delta}(z)=\sum_{t=0}^{m}\binom mt\,2^{m-t+\mathbf1_{\{t+\delta>0\}}}\,z^{m-t+(t+\delta)^2}.
\]
Then the complete Euclidean vertex-shell spectrum factors as
\[
\boxed{F_{p,q}(z)=A_{p,1}(z)A_{q,0}(z)+A_{p,0}(z)A_{q,1}(z).}
\]
In particular, the exact number of vertices is
\[
\boxed{f_0(P_{p,q})=8\cdot3^{p+q}-2^{q+1}3^p-2^{p+1}3^q.}
\]
The unique smallest ambient Euclidean ball containing \(P_{p,q}\) has center \(0\) and squared radius
\[
\boxed{R(P_{p,q})^2=p^2+q^2+2\max\{p,q\}+1,\qquad
\operatorname{diam}_2(P_{p,q})=2R(P_{p,q}).}
\]
The exact number \(C_{p,q}\) of distinct vertices touching this ball is
\[
\boxed{C_{p,q}=\begin{cases}
16,&p=q=1,\\
8,&p=q\ge2\text{ or }(p\ne q,\ \min\{p,q\}=1),\\
4,&p\ne q,\ \min\{p,q\}\ge2.
\end{cases}}
\]
These are **all** sphere contacts, and the unordered diametral pairs are precisely their \(C_{p,q}/2\) antipodal pairs. For \(p,q\ge2\), balancing the hub leaf counts from unequal to equal doubles the number of outer contacts without altering the construction type. The singleton-leaf case exhibits a second exact contact transition.

## Assumptions and scope
Each graph edge appears once with unit weight. A coordinate diamond associated with \(\{i,j\}\) is the two-dimensional cross polytope \(\operatorname{conv}\{\pm e_i,\pm e_j\}\). The tree is labeled, vertex counts are of distinct points (not symmetry classes), and all norms are standard ambient Euclidean norms. The parameters satisfy \(p,q\in\mathbb Z\) and \(p,q\ge1\). The result counts **vertices**, not all lattice points or all faces, and requires neither a generic metric nor any asymptotic limit.

## Proof
**1. A vertex–orientation bijection for every tree.** Let \(T\) be any finite tree and \(P_T\) the corresponding sum of edge diamonds. Given a generic linear functional \(u\), with every coordinate nonzero and absolute coordinate values different across the endpoints of each edge, the unique maximizing summand vertex for an edge \(\{i,j\}\) is \(\operatorname{sgn}(u_w)e_w\), where \(w\) has greater \(|u|\). Orient this edge toward \(w\). Every orientation of a tree is acyclic, hence can be realized by choosing strictly increasing positive numbers \(|u_v|\) along each oriented edge. The signs of \(u_v\) can be selected independently. Therefore, for every orientation and every sign choice on its positive-indegree vertices, the signed indegree vector is a uniquely exposed vertex of \(P_T\).

Conversely every polytope vertex admits a generic exposing functional (perturb a functional from the interior of its full-dimensional normal cone away from the finite collection of equality hyperplanes). Thus all vertices arise this way. Two orientations of a tree giving the same indegree vector must coincide: a leaf has indegree either zero or one, which determines the direction of its unique edge; remove that leaf and subtract its edge contribution from the neighbor's indegree, then repeat inductively. Distinct sign choices at nonzero coordinates give distinct points. Hence orientations and independent signs on positive indegrees parameterize \(\operatorname{Vert}(P_T)\) without repetition.

**2. Decompose bistar orientations by the bridge.** Orient exactly \(t\) of the \(p\) left pendant edges into hub \(a\) and exactly \(s\) of the \(q\) right pendant edges into hub \(b\). Let \(\varepsilon=1\) denote the bridge directed into \(a\), and \(\varepsilon=0\) denote the bridge directed into \(b\). The hub indegrees are \(t+\varepsilon\) and \(s+1-\varepsilon\). Each of the remaining \(p+q-t-s\) leaves has indegree one; the others have indegree zero. The squared norm is therefore exactly
\[
p+q-t-s+(t+\varepsilon)^2+(s+1-\varepsilon)^2.
\]
There are \(\binom pt\binom qs\) ways to select the incoming pendant edges. Since \(p+q-t-s+\mathbf1_{\{t+\varepsilon>0\}}+\mathbf1_{\{s+1-\varepsilon>0\}}\) coordinates are nonzero, the corresponding number of independent sign assignments is exactly two raised to that exponent. Grouping by bridge direction and separating the left and right sums proves the displayed factorization of \(F_{p,q}\), with no overcounting by Step 1.

**3. Vertex count.** At \(z=1\), the binomial identity gives
\[
A_{m,1}(1)=2\cdot3^m,\qquad
A_{m,0}(1)=2\cdot3^m-2^m.
\]
Indeed, the only absent hub-sign factor in the latter case is the term \(t=0\). Substituting these evaluations into the factorization yields
\(F_{p,q}(1)=8\cdot3^{p+q}-2^{q+1}3^p-2^{p+1}3^q\).

**4. Highest exponent and contact multiplicity.** For \(t\in\{0,\ldots,m\}\), write \(g_{m,\delta}(t)=m-t+(t+\delta)^2\). This is strictly convex in \(t\). Its maximum on the closed integer interval is achieved at an endpoint; moreover
\[
g_{m,1}(m)=(m+1)^2>g_{m,1}(0)=m+1,
\quad g_{m,0}(m)=m^2\ge g_{m,0}(0)=m,
\]
where equality in the second comparison occurs only at \(m=1\). Thus \(A_{m,1}\) has unique highest-degree term \(2z^{(m+1)^2}\), whereas \(A_{m,0}\) has highest-degree term \(2z^{m^2}\) for \(m\ge2\), or \(4z\) when \(m=1\). It follows that the two bridge contributions have maximum squared radii \((p+1)^2+q^2\) and \(p^2+(q+1)^2\). Their maximum equals \(p^2+q^2+2\max\{p,q\}+1\). Comparing their leading coefficients, including the tied cases \(p=q\) and \(m=1\), yields exactly the three-case contact formula above.

**5. Unique ball, all contacts, all diameters.** Each edge diamond is centrally symmetric, so \(P_{p,q}=-P_{p,q}\). Let \(R\) denote its maximum vertex norm, determined by Step 4. Convexity of the ball of radius \(R\) gives \(P_{p,q}\subseteq R B_2\). Any enclosing ball centered at \(c\) must contain \(v\) and \(-v\) for a vertex satisfying \(\|v\|=R\), so the mean of the squares of the two distances is \(R^2+\|c\|^2\); its radius is at least \(\sqrt{R^2+\|c\|^2}\). Consequently \(c=0\) is the unique optimal center. Strict convexity of squared norm shows that no nonvertex of the convex polytope lies on its outer sphere, so the contacts are precisely those counted in Step 4. Finally, every pair has separation at most \(2R\), with equality if and only if its endpoints are opposite points of this outer sphere. Central symmetry supplies all such pairs and proves the exact diameter and pair counts.

## Verification
The standalone `verify.py` uses only standard Python and exact integer arithmetic. For each \((p,q)\in\{1,2,3\}^2\), it independently constructs the signed indegree vectors of every tree orientation, enumerates all four signed endpoint choices for every coordinate diamond (up to \(4^7\) choices), checks every squared-radius multiplicity against the factorized enumerator, checks the closed vertex count, checks the maximum squared radius and the full contact set, and tests explicit integer exposing-functionals for orientations. It reports **3,535 exact assertions across nine parameter instances**. The program checks finite cases only; the all-parameter result is established by Steps 1–5 and does not rely on extrapolation from these computations.

For illustration, \(P_{1,1}\) has \(48\) vertices, squared enclosing radius \(5\), and \(16\) contacts; \(P_{2,2}\) has \(504\) vertices, squared radius \(13\), and \(8\) contacts; \(P_{2,3}\) has \(1{,}584\) vertices, squared radius \(20\), and \(4\) contacts. To reproduce: run `python3 verify.py` in the directory containing the extracted file.

## Relationship to prior work
Dai, Hou, Liu, Thawinrak, and Wang (2026, arXiv:2608.16037) introduce the cross-polytope Minkowski-sum framework and prove lattice-point, Ehrhart and volume identities. Their Section 5, Problem 5.4 explicitly asks about face numbers and face posets. The present result takes the first face number for a natural two-parameter tree family, while additionally determining its **complete Euclidean vertex-radius spectrum and outer-contact strata**. The new formulas are not its draconian-sequence support enumerators or \(h^*\)-polynomials and do not follow by reading off those polynomials.

The published result *The complete Euclidean vertex-shell spectrum of cyclic cross-polytope sums* treats unit-edge diamonds for cycle graphs \(C_n\), \(n\ge5\), but its cycle orientation classification does not imply the bistar tree count. The published result *Sharp Euclidean outer spheres and contact multiplicities for complete-multipartite edge-diamond sums* treats complete multipartite graphs. A bistar with both \(p,q\ge1\) is a diameter-three tree and thus cannot be complete multipartite (a complete multipartite tree is necessarily a star). It supplies a useful general indegree-norm viewpoint, but neither its multipartite cloning lemma nor its class-order formula applies to the bistar. Studies of standard **symmetric edge polytopes** and **graphical zonotopes** concern different objects (respectively convex hulls of edge roots and sums of edge segments rather than sums of four-vertex coordinate diamonds).

## Limitations
The theorem assumes unweighted edge diamonds, a bistar with two nonempty leaf classes, and standard Euclidean coordinates. It does not give face counts beyond the number of vertices, arbitrary-tree radial spectra, weighted graph versions or complete lattice-point enumerators. Source comparisons were extensive but are not an independent historical-priority certification; an equivalent older result expressed through graphic orientations or signed arrangements remains possible. Independent mathematical validation has not been performed.

## References
1. Z. Dai, Q. Hou, Z. Liu, W. Thawinrak, H. Wang, *Counting Lattice Points in Minkowski Sums of Cross Polytopes*, arXiv:2608.16037v1, first posted 2026-08-17; accessible revised full text arXiv:2608.16037v2 (2026-08-27), https://arxiv.org/abs/2608.16037.
2. *The complete Euclidean vertex-shell spectrum of cyclic cross-polytope sums*, mathematical research record (2026), identifier `2026/11/8/SCOPE-the-complete-euclidean-vertex-shell-spectrum-of-cyclic-cross-pol--8120a5ffa59c`.
3. *Sharp Euclidean outer spheres and contact multiplicities for complete-multipartite edge-diamond sums*, mathematical research record (2026), identifier `2026/11/8/SCOPE-sharp-euclidean-outer-spheres-and-contact-multiplicities-for-com--6724dd3b50db`.
4. N. A. Borsik, P. Madarasi, *Separable convex optimization over indegree polytopes*, arXiv:2509.06182, first posted 2025-09-07, https://arxiv.org/abs/2509.06182.
