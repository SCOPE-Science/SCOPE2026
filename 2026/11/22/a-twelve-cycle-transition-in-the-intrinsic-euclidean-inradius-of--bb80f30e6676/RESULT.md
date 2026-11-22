# A twelve-cycle transition in the intrinsic Euclidean inradius of cosmological polytopes

## Finding
For every integer \(n\ge3\), let \(P(C_n)\subset\mathbb R^{2n}\) be the canonical cosmological polytope of the simple cycle with its standard Euclidean coordinate metric. Its intrinsic Euclidean inradius is exactly
\[
\rho_n=\begin{cases}
\displaystyle\frac{2\sqrt{2n}}{n(1+\sqrt{6n-9})},&3\le n\le11,\\[5pt]
\displaystyle\frac1{\sqrt{n(n-2)}},&n\ge12.
\end{cases}
\]
There are explicit cyclically invariant inball centers. For \(3\le n\le11\), their active facets are exactly the \(n\) singleton connected-subgraph facets and the single scattering facet. For \(n\ge12\), their active facets are exactly the \(n\) singleton facets and the \(n\) connected-two-vertex path facets. The threshold is sharp and \(n\rho_n\to1\). We do not classify possible nonsymmetric optimal centers.

## Assumptions and scope
The graph is a *simple* cycle \(C_n\), \(n\ge3\). Let \(x_0,\ldots,x_{n-1},y_0,\ldots,y_{n-1}\) be an orthonormal basis of \(\mathbb R^{2n}\), with edge \(e_i=\{i,i+1\pmod n\}\). The polytope is the convex hull, over all edges \(e_i=\{v,w\}\), of the three points
\[
y_i+x_v-x_w,\quad y_i-x_v+x_w,\quad -y_i+x_v+x_w.
\]
It lies in the affine hyperplane \(\sum_i x_i+\sum_i y_i=1\) and has dimension \(2n-1\). Distances and maximal balls are computed *within this affine hull*. We use the connected-subgraph facet theorem of Arkani-Hamed–Benincasa–Postnikov, recalled with full normals by Kühne–Monin [1, Theorem 2.1].

## Proof
**Facet classification.** Every facet is indexed by a nonempty connected subgraph \(H\) of the cycle. Its inward normal has coefficient \(1\) on vertices in \(V(H)\), coefficient \(0\) on edges in \(E(H)\), and on every edge not in \(E(H)\) a coefficient equal to the number of its endpoints in \(V(H)\). Its supporting inequality is \(h_H\cdot z\ge0\). Thus there are \(n\) translates for each proper path with \(k\) vertices, \(1\le k\le n-1\), one scattering facet indexed by the entire cycle, and \(n\) spanning-path facets obtained by deleting a single cycle edge. These exhaust the \(n^2+1\) facets.

**Intrinsic normals.** The affine tangent space is the orthogonal complement of \(\mathbf1_{2n}\). The Euclidean norm of a facet normal restricted to this tangent space is
\[
\|h_H^\perp\|=\sqrt{\|h_H\|^2-\frac{(\sum_j h_{H,j})^2}{2n}}.
\]
Writing a rotationally invariant center as \(z=(a,\ldots,a,b,\ldots,b)\), with \(a+b=1/n\), and putting
\[
c_t=\sqrt{t\left(1-\frac{t}{2n}\right)},\qquad d_n=\sqrt{\frac n2+2-\frac2n},
\]
the distances from \(z\) to the supporting hyperplanes of the three facet families are respectively
\[
L_k(a)=\frac{(k-2)a+2/n}{c_{k+2}}\quad(1\le k\le n-1),\qquad
S(a)=\sqrt{2n}\,a,\qquad
M(a)=\frac{(n-2)a+2/n}{d_n}.
\]
Here the proper path has \(k\) vertex coefficients equal to \(1\) and two boundary-edge coefficients equal to \(1\), the scattering facet has \(n\) vertex coefficients equal to \(1\), and the spanning path has \(n\) vertex coefficients equal to \(1\) and one omitted edge coefficient \(2\). Hence their intrinsic normal lengths are \(c_{k+2}\), \(\sqrt{n/2}\), and \(d_n\).

**Optimality bound.** Any ball center can be averaged over the cyclic rotations of the graph without lowering its admissible radius: every signed facet-distance constraint is affine in the center. Thus some maximum inball has the above invariant form, and it suffices to optimize the minimum of all the displayed distances. Since \(L_1(a)=(2/n-a)/c_3\) decreases strictly and \(S(a)\) increases strictly, their maximum possible minimum is attained at
\[
a_0=\frac{2}{n(1+\sqrt{6n-9})},\qquad R_0=\frac{2\sqrt{2n}}{n(1+\sqrt{6n-9})}.
\]
Also \(L_2(a)=1/\sqrt{n(n-2)}=:R_2\) is constant. Therefore every inscribed ball satisfies \(\rho_n\le\min\{R_0,R_2\}\). Algebra gives \(R_0\le R_2\) precisely when \(n^2-14n+25\le0\), which for integers \(n\ge3\) means \(3\le n\le11\). In particular the strict crossover lies between \(11\) and \(12\).

**Attaining both bounds.** The function \(c_t=\sqrt{t(1-t/(2n))}\) is strictly concave for \(3\le t\le n+1\). In the first regime take \(a=a_0\), so \(L_1=S=R_0\) and \(L_2\ge R_0\). The latter implies \(a_0\ge R_0(c_4-c_3)\). By decreasing increments of \(c_t\), for every \(k\ge2\),
\[
(k-2)a_0+\frac2n\ge R_0\bigl(c_3+(k-1)(c_4-c_3)\bigr)\ge R_0c_{k+2}.
\]
In the second regime take \(a=a_1=R_2(c_4-c_3)\), equivalently
\[
a_1=\frac2n\left(1-\sqrt{\frac{3(2n-3)}{8(n-2)}}\right).
\]
Now \(L_1=L_2=R_2\), and strict concavity gives \(L_k>R_2\) for every \(k\ge3\). The crossover inequality guarantees \(S(a_1)>R_2\) (because \(a_1>a_0\) for \(n\ge12\)); in the first regime \(S(a_0)=R_0\).

It remains to check the spanning-path facets in both regimes. Both choices have \(0<a\le1/(2n)\), hence \(b=1/n-a\ge a\). Consequently their unnormalized spanning-path slack is \(na+2b\ge(n+2)a\). Since
\[
\frac{d_n}{\sqrt{n/2}}=\sqrt{1+\frac4n-\frac4{n^2}}<1+\frac2n,
\]
we get \(M(a)>S(a)\) whenever \(a>0\). The spanning-path facets cannot obstruct either candidate. Thus each candidate is feasible at the asserted upper-bound radius. The strict inequalities and concavity also give precisely the stated facet-contact sets.

**Scaling.** In the second regime \(n\rho_n=\sqrt{n/(n-2)}\to1\).

## Verification
The companion source file `CHECK.py` independently constructs every canonical vertex and every connected-subgraph facet normal for each \(n=3,4,\ldots,15,20,24\), checks incidence inequalities and full affine dimension, then solves a *full* \((2n+1)\)-variable Chebyshev linear program without imposing rotational symmetry. Its numerical optimal radii and the contact families agree with the formula at every tested size, including \(n=11,12\). It requires Python, NumPy, and SciPy and prints `CYCLE_COSMO_INBALL_INDEPENDENT_LP_PASS`. These finite numerical checks are corroboration, not an infinite proof.

## Relationship to prior work
Kühne and Monin [1] give the combinatorial face structure and recall the full connected-subgraph facet-normal theorem, which supplies the crucial geometric input. Their work does not state an intrinsic Euclidean inradius or the twelve-cycle contact transition. Birkemeyer et al. [2] develop a dual and triangulations, including explicit facet normals, without the metric Chebyshev calculation. Related previously indexed results give Euclidean inballs for *star* and *path* cosmological polytopes [3–4], not for cycles; the connected-graph circumradius theorem [5] concerns a different extremal metric problem. The present theorem evaluates the symmetrized facet-distance optimization for the simple cycles and proves the sharp transition. This novelty assessment is based on inspected texts and searches, not a claim that all mathematical literature has been exhausted.

## Limitations
The theorem covers simple, unweighted cycle graphs in the canonical coordinate metric, not weighted cycles, arbitrary graph realizations, or arbitrary graphs. It constructs optimal cyclically invariant centers but does not determine the entire (possibly nonunique) incenter locus. The cited face theorem is taken as established prior work. Mathematical priority remains subject to uncatalogued equivalent results, and no independent mathematical audit has been performed.

## References
[1] Lukas Kühne and Leonid Monin, *Faces of Cosmological Polytopes*, arXiv:2209.08069, first submitted 16 September 2022, Theorem 2.1 and Section 5. https://arxiv.org/pdf/2209.08069

[2] *On cosmological polytopes, their canonical forms and their duals*, arXiv:2603.03894, 2026, Sections 1–3. https://arxiv.org/html/2603.03894

[3] *Every star cosmological polytope is tangential with an exact unique inball*, published research summary, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-every-star-cosmological-polytope-is-tangential-with-an-exact-uni--22da9e5835c2

[4] *Exact Euclidean inballs and cubical incenter loci of path cosmological polytopes*, published research summary, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-euclidean-inballs-and-cubical-incenter-loci-of-path-cosmol--d78cc4c4e2be

[5] *Every connected cosmological polytope has graph-independent Euclidean circumradius*, published research summary, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-every-connected-cosmological-polytope-has-graph-independent-eucl--099bd090b126
