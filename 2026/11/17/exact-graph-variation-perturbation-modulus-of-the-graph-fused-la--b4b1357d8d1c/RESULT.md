# Exact graph-variation perturbation modulus of the graph fused-lasso denoiser

## Finding

Let \(G=(V,E,w)\) be a finite connected undirected graph with \(|V|=n\geq 2\) and strictly positive edge weights \(w_e\). For any \(\lambda>0\), let the graph total-variation denoiser be
\[
T_\lambda(y)=\operatorname*{argmin}_{x\in\mathbb R^V}
\left\{\frac12\sum_{v\in V}(x_v-y_v)^2+\lambda J_w(x)\right\},\qquad
J_w(x)=\sum_{\{u,v\}\in E}w_{uv}|x_u-x_v|.
\]
For a partition \(\pi\) of \(V\) into nonempty blocks each inducing a connected subgraph, let \(B_\pi(v)\) be the block containing \(v\), and put
\[
\alpha_{\pi,S}(v)=\frac{|S\cap B_\pi(v)|}{|B_\pi(v)|}
\quad (S\subset V).
\]
Here the cut is \(\partial S=\{\{u,v\}\in E:u\in S,\ v\notin S\}\). Then the **sharp two-input graph-variation modulus**, independent of the positive regularization parameter, is
\[
\boxed{\displaystyle
\sup_{J_w(y-z)>0}\frac{J_w(T_\lambda(y)-T_\lambda(z))}{J_w(y-z)}
=\max_{\substack{\pi\text{ a connected-block partition}\\
\emptyset\ne S\subsetneq V}}
\frac{\displaystyle\sum_{\{u,v\}\in E} w_{uv}
\left|\alpha_{\pi,S}(u)-\alpha_{\pi,S}(v)\right|}
{\displaystyle\sum_{\{u,v\}\in\partial S}w_{uv}}.}
\]
Every ratio inside the maximum is obtained **exactly** by the quotient of two sufficiently close inputs; the result is a maximum, not merely an unattained supremum. No restrictions on graph cycles or degrees are imposed.

For unweighted simple connected graphs of order \(n\), the largest possible modulus over all graphs of order \(n\) grows quadratically: a universal bound is \(n(n-1)/2\), while the barbell consisting of two \(q\)-cliques joined by a single bridge has modulus at least \(\lfloor q^2/4\rfloor\), with \(n=2q\). For \(q\) even the latter witness equals \(n^2/16\). Thus Euclidean nonexpansivity of total-variation denoising does not prevent quadratic amplification of the variation of *differences*.

## Assumptions and scope

All vertex signals are real; the least-squares fidelity uses ordinary unweighted counting measure, while graph total variation uses positive edge weights. The graph is finite, connected and undirected; parallel edges may be consolidated by summing weights. The parameter \(\lambda\) is fixed and positive. The seminorm \(J_w\) vanishes precisely on constant vertex signals; the quotient excludes constant input differences. The theorem does not assert that \(J_w(T_\lambda(y))\) itself exceeds \(J_w(y)\); it concerns perturbations \(T_\lambda(y)-T_\lambda(z)\).

## Proof

**1. Local affine branches.** Choose any orientation and incidence matrix \(D\), so \(J_w(x)=\sum_e w_e|(Dx)_e|\). The optimality conditions for \(x=T_\lambda(y)\) are
\[
y-x=D^{\mathsf T}s,\quad s_e=\lambda w_e\operatorname{sgn}((Dx)_e)
\text{ when }(Dx)_e\ne0,\quad |s_e|\le\lambda w_e\text{ otherwise}.
\]
The objective is a strictly convex quadratic plus a polyhedral convex function, so its proximal map is continuous and piecewise affine, with finitely many polyhedral pieces. In any full-dimensional piece, the nonsaturated dual edges can be fixed as an edge set \(F\); the corresponding equalities \(D_Fx=0\) persist there, while the signs on the remaining edges are fixed. Orthogonally projecting the optimality equation onto \(\ker D_F\) gives an affine expression for \(x\) whose linear part is \(P_F\), orthogonal projection onto \(\ker D_F\). The connected components of \((V,F)\) are connected blocks of a partition \(\pi\), and \(P_F=P_\pi\) is exactly **blockwise arithmetic averaging**. Boundary pieces do not affect the global bound: any line segment is approximable by generic line segments passing through finitely many full-dimensional pieces, and continuity passes the estimate to the limit. Hence, denoting the displayed finite partition maximum by \(K\), it is enough to prove \(J_w(P_\pi h)\le KJ_w(h)\) for every connected-block partition \(\pi\) and signal \(h\).

**2. The cut test is exact.** For a signal \(h\) with minimum \(a\) and maximum \(b\), the coordinatewise layer-cake representation is
\[
h=a\mathbf1+\int_a^b\mathbf1_{\{h>t\}}\,dt.
\]
Block averaging preserves constants, so linearity and the triangle inequality yield
\[
J_w(P_\pi h)\le\int_a^b J_w(P_\pi\mathbf1_{\{h>t\}})\,dt
\le K\int_a^b J_w(\mathbf1_{\{h>t\}})\,dt=KJ_w(h).
\]
The last identity is the finite graph coarea formula. Conversely, testing \(h=\mathbf1_S\) realizes exactly the ratio in the theorem for any fixed \(\pi\) and proper nonempty cut \(S\). This proves the induced operator seminorm of each block-averaging projection is the stated cut maximum.

**3. All connected partitions are genuine active branches.** Fix an arbitrary connected-block partition \(\pi\). Choose vertex levels \(u_v=c_B\) constant on each block \(B\), with different constants on every two blocks (and thus on every cross-block edge). Choose an edge dual field \(s^0\) equal to zero on within-block edges and to \(\lambda w_e\operatorname{sgn}((Du)_e)\) on cross-block edges. Then \(y^0=u+D^{\mathsf T}s^0\) has \(T_\lambda(y^0)=u\) by the optimality conditions and strict convexity. For an arbitrary \(h\), define \(u^\varepsilon=u+\varepsilon P_\pi h\) and \(y^\varepsilon=y^0+\varepsilon h\). Within each connected block, the residual \(h-P_\pi h\) has zero sum. A flow supported on a spanning tree of that block has divergence \(h-P_\pi h\). Adjust the internal dual edges by \(\varepsilon\) times this flow; leave cross-block dual edges unchanged. For sufficiently small \(\varepsilon>0\), the internal dual variables stay strictly inside their intervals, and all cross-block signs remain unchanged. Consequently the adjusted dual variable satisfies
\[
y^\varepsilon-u^\varepsilon=D^{\mathsf T}s^\varepsilon
\]
and the exact optimality conditions. Therefore
\[
T_\lambda(y^0+\varepsilon h)-T_\lambda(y^0)=\varepsilon P_\pi h.
\]
Take \(h=\mathbf1_S\) for a maximizing cut. Its input variation is positive by connectedness, so the ratio equals the finite maximum \(K\) exactly. This proves both sharpness and independence of \(\lambda>0\).

**4. Quadratic barbell amplification.** Let two copies of \(K_q\) be joined by precisely one bridge, and let \(L\) be the entire left clique. For \(1\le t\le q\), choose a fused block containing \(t\) left-clique vertices and \(t\) right-clique vertices, including both bridge endpoints, and put every other vertex in a singleton block. For \(h=\mathbf1_L\), the input variation is \(J(h)=1\). The block average equals \(1/2\) on the fused block, \(1\) on the other left vertices and \(0\) on the other right vertices. Its graph variation is
\[
J(P_\pi h)=\frac12t(q-t)+\frac12t(q-t)=t(q-t).
\]
Taking \(t=\lfloor q/2\rfloor\) yields \(\lfloor q^2/4\rfloor\), and Step 3 gives an actual attaining pair of denoising inputs. Conversely, for every unweighted connected graph and every block averaging map, \(\operatorname{osc}(P_\pi h)\le\operatorname{osc}(h)\le J(h)\); hence \(J(P_\pi h)\le |E|J(h)\), and \(|E|\le n(n-1)/2\) for a simple graph. The general formula then gives the asserted universal order bound.

## Verification

The self-contained `check.py` uses exact rational arithmetic. It enumerates connected partitions for paths, cycles, stars and cliques of sizes three through five; compares the cut formula against an independently enumerated ternary-potential optimization; and constructs exact primal-dual KKT certificates for the corresponding active-partition witnesses. It additionally tests three weighted paths and explicit barbell witnesses at five sizes, checking the exact cut ratios and local KKT systems. Execute `python check.py` in the same directory as this document. The finite tests are supporting checks, not a substitute for the proof above.

## Relationship to prior work

Tibshirani and Taylor (first public preprint May 11, 2010) prove a general locally affine projection description for the generalized lasso (Lemma 3, Section 10) and identify connected fused groups on graphs (Section 6). Those are foundational ingredients of Step 1; their published statements do not give the global input-difference graph-variation modulus, the reduction to all connected partitions and all cuts, the realization of every partition as a stable active face, or quadratic barbell witnesses. Madrid Padilla et al. (August 11, 2016) develop graph bounded-variation estimation rates and a DFS comparison for the fused lasso, not this two-input operator modulus. Kirisits, Scherzer and Setterqvist (2018 preprint, 2019 journal article) establish a universal convex-minimality property of the ROF denoiser for each data input. Such a property does not imply a bound for \(J_w(T_\lambda(y)-T_\lambda(z))\) in terms of \(J_w(y-z)\). Related tree block-averaging sensitivities may coincide numerically in certain special families, but do not supply the present all-graph result or the barbell effect. No claim of exhaustive bibliographic priority is made.

## Limitations

The cut-and-partition expression is finite and exact but generally exponential to evaluate; no polynomial-time evaluation algorithm is claimed. The quadratic lower bound does not determine the optimal leading coefficient over all connected graphs of fixed order. The theorem does not address isotropic (Euclidean grouped) graph variation, directed graph penalties, nonquadratic fidelity, zero-weight edges or infinitely many vertices. Prior work on polyhedral projections could contain an equivalent implicit statement; independent audit is not performed.

## References

1. R. J. Tibshirani and J. Taylor, *The Solution Path of the Generalized Lasso*, arXiv:1005.1971, first posted May 11, 2010; *Annals of Statistics* 39 (2011), 1335–1371. https://arxiv.org/abs/1005.1971
2. O. H. Madrid Padilla, J. G. Scott, J. Sharpnack and R. J. Tibshirani, *The DFS Fused Lasso: Linear-Time Denoising over General Graphs*, arXiv:1608.03384, first posted August 11, 2016. https://arxiv.org/abs/1608.03384
3. C. Kirisits, O. Scherzer and E. Setterqvist, *Invariant \(\varphi\)-Minimal Sets and Total Variation Denoising on Graphs*, RICAM Report 2018-24 (July 27, 2018), subsequently *SIAM Journal on Imaging Sciences* 12 (2019), 1643–1668. https://www.ricam.oeaw.ac.at/files/reports/18/rep18-24.pdf
