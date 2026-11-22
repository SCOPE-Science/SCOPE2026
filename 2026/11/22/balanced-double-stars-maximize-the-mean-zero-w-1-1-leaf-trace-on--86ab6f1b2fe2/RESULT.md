# Balanced double-stars maximize the mean-zero \(W^{1,1}\) leaf trace on unit metric trees

## Finding

For a finite, connected, acyclic metric graph \(T\) with \(N\ge1\) unit-length edges, let \(L(T)\) be its degree-one vertices. Give \(T\) arclength measure and, for real continuous edgewise-\(W^{1,1}\) functions \(f\), write
\[
\bar f=\frac1N\int_T f\,ds,\qquad
\mathcal B_T(f)=\left(\sum_{v\in L(T)}|f(v)-\bar f|^2\right)^{1/2},\qquad
\mathcal V_T(f)=\sum_{e\in E(T)}\int_e|f'|\,ds.
\]
The sharp boundary trace constant is \(C(T)=\sup_{\mathcal V_T(f)>0}\mathcal B_T(f)/\mathcal V_T(f)\). For each oriented edge \(e=uv\), let \(U_{e,u}\) be the vertex component containing \(u\) after deletion of \(e\); put \(s_{e,u}=|E(U_{e,u})|\), \(r_{e,u}=|L(T)\cap U_{e,u}|\), and \(q_{e,u}=|L(T)\setminus U_{e,u}|\). Then the exact finite cut formula is
\[
\boxed{C(T)^2=\max_{e=uv}\max_{w\in\{u,v\}}\left[r_{e,w}\left(1-\frac{s_{e,w}}N\right)^2+q_{e,w}\left(\frac{s_{e,w}}N\right)^2\right].}
\]
For every \(N\), the maximum across **all** unit-edge trees with \(N\) edges is
\[
\boxed{\mathcal C_N^2=\begin{cases}
1,&1\le N\le4,\\
\dfrac{N-1}{4},&N\ge6\text{ even},\\
\dfrac{(N-1)(N^2+1)}{4N^2},&N\ge5\text{ odd}.
\end{cases}}
\]
For \(N\ge5\), equality \(C(T)=\mathcal C_N\) holds **if and only if**, up to graph isomorphism, \(T\) is the double-star obtained by joining two star centers carrying \(\lfloor N/2\rfloor\) and \(\lceil N/2\rceil-1\) pendant edges, respectively. In particular the first nontrivial topology-sensitive norm increase occurs at five edges, where \(\mathcal C_5^2=26/25\); moreover \(\mathcal C_N/\sqrt N\to1/2\). For every nontrivial \(T\), the sharp norm \(C(T)\) is **not attained** by a nonconstant continuous edgewise-\(W^{1,1}\) function, but is approached by unit-variation ramps supported on arbitrarily short edge segments.

## Assumptions and scope

Each graph edge is a distinct interval isometric to \([0,1]\), and all incident edge functions take a common value at each vertex. The derivative energy \(\mathcal V_T\) is the unweighted sum of edgewise \(L^1\) norms. Leaves are exactly degree-one vertices of the original combinatorial tree; degree-two subdivisions count as separate unit edges. The boundary norm is **unweighted Euclidean \(\ell^2\)** over all original leaves, and the centering mean uses continuous arclength over the **entire** tree, not the leaf average. Arbitrary additive constants cancel. Only real-valued functions are asserted.

## Proof

**1. Sharp vector-valued cut kernel.** Choose any root and orient every edge away from it. The map sending \(f\) modulo constants to its edgewise derivative is an isometric bijection onto real \(L^1(T,ds)\): on a tree, every integrable edge derivative can be integrated along the unique paths from the root, and the integration constant is fixed by any prescribed mean. Consider a point \(z\) in the interior of an edge and its two connected sides after cutting that edge at \(z\). Let one side have arclength \(a\) and contain \(r\) original leaves, while the opposite side contains \(q\) original leaves. A unit derivative concentrated in a short interval about \(z\) changes all \(r\) leaf values on the first side relative to all \(q\) on the other by one. Centering by the volume mean gives, up to a common sign, a vector with \(r\) entries \(1-a/N\) and \(q\) entries \(-a/N\). Hence the vector kernel has squared Euclidean length
\[
Q_{r,q}(a)=r\left(1-\frac aN\right)^2+q\left(\frac aN\right)^2.
\]
Minkowski's inequality gives \(\mathcal B_T(f)\le (\operatorname*{ess\,sup}_{z\in T}|K(z)|)\mathcal V_T(f)\). Conversely, an edge derivative equal to a constant on a vanishing interval about any interior \(z\) approaches its kernel-vector norm, so this is precisely the operator norm. On any fixed edge, \(r,q\) are fixed and \(a\) ranges through an interval of length one. Since \(Q_{r,q}''(a)=2(r+q)/N^2>0\), its maximum occurs at the two limiting vertex-side cuts. This proves the displayed finite cut formula, including the convention that the deleted edge itself is not included in \(s_{e,w}\).

**2. Reduction of the all-tree problem to a quadratic in an integer.** Every tree has a leaf edge. Cutting just inside its terminal leaf gives the limiting kernel length \(1\), so \(C(T)^2\ge1\). Fix a limiting cut at an endpoint of an edge \(e\). Let \(s\) count the complete edges on the chosen side, so the opposite side has \(t=N-s-1\) complete edges. If \(s=0\), that side is an original leaf and the squared kernel is \(1\). Similarly, when \(t=0\), the opposite side is an original leaf; the bound \(r\le N-1\) gives \(Q\le (N-1)/N<1\) for the orientation with \(s=N-1\). If \(s,t\ge1\), the leaf counts satisfy \(r\le s\) and \(q\le t\): each original leaf in one side requires its distinct pendant edge in that side, because the cut endpoint is not an original leaf. Both coefficients in \(Q\) are nonnegative. Thus
\[
Q\le s\left(1-\frac{s}{N}\right)^2+(N-s-1)\frac{s^2}{N^2}
=:\Phi_N(s)=\frac{s\{N^2-(N+1)s\}}{N^2},\qquad 1\le s\le N-2.
\]
Consequently \(C(T)^2\le\max\{1,\max_{1\le s\le N-2}\Phi_N(s)\}\). Every positive integer \(s\) in this range realizes equality in the cut bound: take a double-star with \(s\) leaves on its first center and \(N-s-1\) on the second, and concentrate the derivative on the joining edge adjacent to the first center. Therefore the bound is the exact universal maximum.

**3. The finite optimum and graph rigidity.** The quadratic \(\Phi_N\) is strictly concave. Its real vertex is \(N^2/[2(N+1)]\), and its uniquely maximizing integer in \(1\le s\le N-2\), when nonempty, is \(s=\lfloor N/2\rfloor\) for \(N\ge4\) (for \(N=3\) the only admissible value is \(s=1\)). Substitution yields \(\Phi_N(N/2)=(N-1)/4\) for even \(N\) and \(\Phi_N((N-1)/2)=(N-1)(N^2+1)/(4N^2)\) for odd \(N\). These values first exceed one at \(N=5\), establishing the piecewise formula and the asymptotic growth. For \(N\ge5\), equality in the universal bound must have \(s,t\ge1\) and saturate both leaf bounds \(r=s\) and \(q=t\). Accordingly every complete edge on either side is incident to a distinct original leaf, so each component is a star rooted at its cut endpoint. The original tree is therefore precisely the stated double-star, with the unique maximizing integer counts (up to swapping the two centers). Conversely these double-stars attain the universal sharp constant in the supremum sense.

**4. Nonattainment.** Inside any open edge, the kernel norm is strictly below the maximum of its endpoint limiting norms by strict convexity of \(Q_{r,q}\). A nonzero \(L^1\) derivative is nonzero on a set of positive arclength, hence the integrated triangle bound is strictly smaller than \(C(T)\mathcal V_T(f)\). Concentrated continuous ramps approach the supremum, completing the proof.

## Verification

The standalone `check_leaf_trace.py` reconstructs the cut norm with exact rational arithmetic for **every labeled tree having one through seven edges**, using all Prüfer sequences (including \(262144\) labeled trees with seven edges). It checks the universal expression and its sharp attainment by double-stars through eighty edges, verifies each integer quadratic bound through three hundred edges, and checks convergence of explicit short-ramp witnesses. Execution reported `ALL_EXACT_TREE_TRACE_TESTS_PASSED 325330`. These finite calculations are diagnostic; the universal argument is the vector cut kernel, leaf-count inequality, integer quadratic maximization and equality analysis above.

## Relationship to prior work

Cianchi–Ferone–Nitsch–Trombetti (2013) study sharp \(BV\) boundary trace inequalities and shape optimization on **Euclidean domains**, principally with boundary centering in \(L^1\). Lahti–Shanmugalingam (2015) establish existence and \(L^1\) trace estimates for \(BV\) on general metric spaces, without this finite-tree Euclidean leaf-vector constant or all-tree extremal topology. Björn–Björn–Gill–Shanmugalingam (2013) analyze Sobolev traces on **infinite rooted-tree boundaries** and Besov identifications. A published metric-tree result on mean-zero \(H^1\)-to-point-evaluation norms (2026) has a different derivative exponent and a scalar \(L^\infty\) target, and its sharp **star-minimum/path-maximum** topology theorem does not imply the present balanced-double-star \(W^{1,1}\)-to-\(\ell^2\) leaf-trace maximum. Another published tree trace result (2026) optimizes linear leaf-to-interior **right inverses** on a depth-two weighted tree, not the volume-centered leaf trace over arbitrary finite trees. The elementary \(L^1\) kernel operator-norm principle is not claimed as new; the claim is the full cut formula together with the exact all-tree phase transition and if-and-only-if maximizing topologies.

## Limitations

Only unit-edge metric trees, real continuous edgewise-\(W^{1,1}\), unweighted arclength centering, and Euclidean norm on all original leaves are covered. No assertion extends automatically to cyclic graphs, weighted/arbitrary edge lengths, atomic vertex measures, \(L^p\) derivative energies for \(p>1\), or other boundary norms. The supremum is not attained within the specified function class. Novelty is a best-knowledge comparison; an implicit equivalent result in broader metric-graph endpoint trace theory remains possible. No independent external mathematical audit has been performed.

## References

1. A. Cianchi, V. Ferone, C. Nitsch, C. Trombetti, *Balls minimize trace constants in BV*, arXiv:1301.5770v1, first posted 2013-01-24, https://arxiv.org/abs/1301.5770 (Sections 1–2).
2. P. Lahti and N. Shanmugalingam, *Trace theorems for functions of bounded variation in metric spaces*, arXiv:1507.07006v1, first posted 2015-07-24, https://arxiv.org/abs/1507.07006 (Sections 3 and 5).
3. A. Björn, J. Björn, J. T. Gill, N. Shanmugalingam, *Geometric analysis on Cantor sets and trees*, arXiv:1304.0566v1, first posted 2013-04-02, https://arxiv.org/abs/1304.0566 (Sections 4 and 6).
4. *Sharp star–path extremals and a subtree-cut formula for Sobolev evaluation on metric trees*, published research record, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-star-path-extremals-and-a-subtree-cut-formula-for-sobolev--c77435a98c36.
5. *Sharp endpoint linear trace extensions on a two-generation weighted binary tree*, published research record, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-endpoint-linear-trace-extensions-on-a-two-generation-weigh--3dc47ecf9a04.
