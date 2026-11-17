# Sharp graph-variation instability of simplex projection under edge-connectivity constraints

## Finding

Let \(n\ge2\), \(r>0\), and let \(P_r:\mathbb R^n\to\Delta_{n,r}\) be Euclidean nearest-point projection onto
\[
\Delta_{n,r}=\{x\in\mathbb R^n:x_i\ge0,\ \sum_{i=1}^n x_i=r\}.
\]
For a connected simple unweighted graph \(G=(V,E)\) on \(n\) labelled vertices, set
\[
\operatorname{TV}_G(x)=\sum_{\{u,v\}\in E}|x_u-x_v|,\qquad
L(G)=\sup_{\operatorname{TV}_G(x-y)>0}\frac{\operatorname{TV}_G(P_rx-P_ry)}{\operatorname{TV}_G(x-y)}.
\]
The constant \(L(G)\) is independent of the positive mass \(r\). Denote the edge connectivity (minimum nontrivial cut size) by \(\lambda(G)\), and put
\[
F_n=\begin{cases}
(n^2-1)/16,&n\text{ odd},\\
n^2/16,&n\equiv0\pmod4,\\
(n^2-4)/16,&n\equiv2\pmod4.
\end{cases}
\]
Then every such graph satisfies the **sharp connectivity bound**
\[
\boxed{L(G)\le1+\frac{F_n}{\lambda(G)}.}
\]
For **every pair of integers** \(q\ge1\) and \(n\ge4q\), this bound is attained by an explicit simple graph of edge connectivity exactly \(q\); consequently
\[
\boxed{\max_{\substack{G\text{ simple, connected}\\|V(G)|=n,\ \lambda(G)\ge q}}L(G)=1+\frac{F_n}{q}\quad(n\ge4q).}
\]
For \(q=1\) the same sharp graph-order envelope holds already for \(n=2,3\). Equality for these constructions occurs for **actual pairs of nearby simplex-projection inputs**, not just limiting Jacobians. In particular, the maximum among all connected \(n\)-vertex graphs is asymptotic to \(n^2/16\), while each individual input satisfies \(\operatorname{TV}_G(P_rx)\le\operatorname{TV}_G(x)\).

The theorem also gives a finite exact formula for every fixed connected graph:
\[
\boxed{L(G)=\max_{\varnothing\ne A\subseteq V}\max_{\varnothing\ne S\subsetneq V}
\frac{\operatorname{TV}_G(J_A\mathbf1_S)}{|\partial_G S|},\qquad
(J_Ah)_v=\begin{cases}h_v-|A|^{-1}\sum_{u\in A}h_u,&v\in A,\\0,&v\notin A.\end{cases}}
\]
Here \(\partial_G S\) is the set of edges meeting both \(S\) and its complement. Every ratio in this formula is realized as the ratio for a nearby input pair on a full-dimensional active-support cell.

## Assumptions and scope

Signals and edges are real and undirected, respectively. The graph is finite, simple, connected, and has unit edge weights; no loops, repeated edges, or isolated vertices are allowed. The output simplex is in the full vertex-coordinate space, and the distance defining projection is Euclidean. The quotient uses the unweighted edge-total-variation seminorm, excluding zero denominators. Since \(P_r(x+c\mathbf1)=P_r(x)\), the output difference is zero whenever the input difference has zero graph variation. All claims quantify over every positive simplex mass.

## Proof

**1. Exact active-set linearization.** The simplex KKT conditions yield a threshold \(\tau(x)\) with \((P_rx)_v=(x_v-\tau(x))_+\) and total output mass \(r\). On any open cell with positive support \(A\), the threshold is \((\sum_{v\in A}x_v-r)/|A|\), so the linear part is the displayed \(J_A\). For every nonempty \(A\), the base point given by \(x_v=r/|A|\) on \(A\) and \(x_v=-1\) off \(A\) has exactly this support in an open neighborhood. Since \(P_r\) is continuous piecewise affine, the global seminorm Lipschitz constant is the maximum seminorm norm of its finitely many affine linear parts; the opposite inequality follows from perturbing an interior base point. This uses no differentiability claim on support boundaries.

**2. Cut reduction.** Each \(J_A\) annihilates constants. For every real vertex signal \(h\), its discrete layer-cake decomposition modulo a constant is \(h=(\min h)\mathbf1+\int_{\min h}^{\max h}\mathbf1_{\{h>t\}}\,dt\). Taking variation of the image, using the triangle inequality edge by edge and graph coarea gives
\[
\operatorname{TV}_G(J_Ah)\le\left(\max_{\varnothing\ne S\subsetneq V}\frac{\operatorname{TV}_G(J_A\mathbf1_S)}{|\partial_G S|}\right)\operatorname{TV}_G(h).
\]
The reverse inequality follows by testing cut indicators, proving the exact fixed-graph formula.

**3. Sharp universal connectivity inequality.** Fix \(A,S\), put \(k=|A|\), \(a=|A\cap S|\), \(b=k-a\), and \(c=|\partial_G S|\). Then \(J_A\mathbf1_S\) takes only the values \(b/k\) on \(A\cap S\), \(-a/k\) on \(A\setminus S\), and \(0\) off \(A\). Every edge crossing \(S\) contributes at most \(1\) in absolute difference, hence at most \(c\) in total. Every internal edge of \(S\) contributes at most \(b/k\), and there are at most \(a(|S|-a)\) of these joining active to inactive vertices. The complementary side contributes at most \((a/k)b(n-|S|-b)\). Therefore
\[
\operatorname{TV}_G(J_A\mathbf1_S)\le c+\frac{ab}{k}(n-k).
\]
Since \(c\ge\lambda(G)\), all quotients are at most \(1+F_n/\lambda(G)\), where
\[
F_n=\max_{2\le k\le n}\frac{\lfloor k^2/4\rfloor}{k}(n-k).
\]
This inequality is also valid for \(a=0\) or \(b=0\), in which case the output vanishes.

**4. Exact integer optimum.** For every \(k\), with \(\delta_k=0\) for even \(k\) and \(\delta_k=1\) for odd \(k\), write
\[
\frac{\lfloor k^2/4\rfloor}{k}(n-k)
=\frac{(k^2-\delta_k)(n-k)}{4k},\qquad
\frac{n^2}{16}-\frac{(k^2-\delta_k)(n-k)}{4k}
=\frac{(n-2k)^2}{16}+\frac{\delta_k(n-k)}{4k}.
\]
If \(n\) is odd the first term is at least \(1/16\), achieved by an even \(k\) nearest \(n/2\). If \(n\) is divisible by four, \(k=n/2\) achieves zero deficit. If \(n\equiv2\pmod4\), the deficit is at least \(1/4\): for even \(k\), \(|n-2k|\ge2\); for odd \(k=n/2\) the second term equals \(1/4\); and all other odd \(k\) have a larger first term. Equality is achieved by an even \(k\) closest to \(n/2\) (and also by \(k=n/2\) when it is odd). Thus the displayed three-case formula is exact for every \(n\ge2\).

**5. Graphs and inputs attaining the edge-connectivity envelope.** Fix \(n\ge4q\). Choose the even maximizer \(k=2\lfloor(n+1)/4\rfloor\), and put \(a=b=k/2\); then \(a,b\ge q\) and \(n-k\ge2\). Split the \(n-k\) inactive vertices into two nonempty groups of sizes \(u,v\). Form two cliques on \(a+u\) and \(b+v\) vertices and join exactly \(q\) distinct active vertices of the left clique to \(q\) distinct active vertices of the right clique in a matching. Each clique has at least \(q+1\) vertices. The resulting graph has edge connectivity \(q\): the entire left clique gives a cut of \(q\) edges; any cut splitting a clique internally crosses at least \(q\) edges within that clique. Take \(S\) to be the left clique and \(A\) to consist of precisely the \(a+b=k\) designated active vertices. Its cut has \(q\) edges, all joining active vertices, and its internal clique edges contribute exactly \(ab(n-k)/k=F_n\). Hence
\[
\frac{\operatorname{TV}_G(J_A\mathbf1_S)}{|\partial_GS|}=1+F_n/q.
\]
For actual inputs take \(x_i=r/k\) on \(A\), \(x_i=-1\) off \(A\), and \(y=x+\varepsilon\mathbf1_S\), with sufficiently small \(\varepsilon>0\). Both projections have support \(A\) and their difference is \(\varepsilon J_A\mathbf1_S\), giving exact equality. For \(n=2,3\), the same single-bridge construction with the maximizing \(k=2\) yields the unconditional \(q=1\) formula.

Finally, for each fixed input \(x\), the scalar map \(t\mapsto(t-\tau(x))_+\) is 1-Lipschitz. Applied to both endpoints of every edge, it proves \(\operatorname{TV}_G(P_rx)\le\operatorname{TV}_G(x)\).

## Verification

The standalone `checker.py` implements the simplex threshold rule in exact rational arithmetic. It enumerates every connected labelled simple graph and every active-set/cut pair for orders \(2\) through \(5\), additionally tests 45,000 rational active-cut inequalities on randomized connected graphs of orders \(6\) to \(11\), checks 45 exact connectivity-stratified sharpness constructions, and verifies actual simplex-projection input pairs on explicit witness graphs through order \(60\). The proof above is independent of these finite calculations; larger orders and all integer connectivity parameters are covered by the analytical construction.

Run `python3 checker.py` from the directory containing the script. It requires Python's standard library only.

## Relationship to prior work

Duchi, Shalev-Shwartz, Singer and Chandra [1] develop simplex and \(\ell_1\)-ball projection algorithms; Condat [2] analyzes the simplex threshold and algorithmic complexity. Martins and Astudillo [3] identify the active-support Jacobian in their sparsemax formulation. These ingredients do not provide graph-total-variation stability constants. Lellmann et al. [4] use *spatial* total variation with simplex constraints for vector-valued image labeling, not a two-input total-variation norm for a single simplex projection across the coordinates of one graph signal.

A published exact calculation [5] concerns the **same nonlinear map** but the cyclic-edge seminorm on one fixed cycle, with worst-case growth linear in \(n\); that result expressly leaves arbitrary graphs outside scope. For contrast, graph-total-variation proximal denoising is a different nonlinear operator with connected-block averaging branches, unlike the active-coordinate centering branches of simplex projection. These published and related mechanisms do not supply the graph-connectivity envelope or its attained matching-bridge examples. The novelty comparison is limited to inspected primary sources and indexed mathematical records, not an exhaustive guarantee of priority.

## Limitations

The result concerns finite simple unweighted undirected graphs, real signals, positive simplex mass, and Euclidean projection. The sharp connectivity envelope for prescribed \(q\) is proved for \(n\ge4q\); no exact universal envelope is claimed here for \(n<4q\). The fixed-graph cut/active-set formula is exact but may be exponentially costly to evaluate. The theorem does not cover arbitrary positive edge weights or non-Euclidean simplex projection.

## References

[1] J. Duchi, S. Shalev-Shwartz, Y. Singer, T. Chandra, *Efficient Projections onto the \(\ell_1\)-Ball for Learning in High Dimensions*, ICML 2008, first verified publication July 5, 2008, https://doi.org/10.1145/1390156.1390191 ; lawful author manuscript https://web.stanford.edu/~jduchi/projects/DuchiShSiCh08.pdf.

[2] L. Condat, *Fast Projection onto the Simplex and the \(\ell_1\) Ball*, HAL-01056171v1, publicly posted August 17, 2014, https://optimization-online.org/wp-content/uploads/2014/08/4498.pdf.

[3] A. F. T. Martins, R. F. Astudillo, *From Softmax to Sparsemax: A Sparse Model of Attention and Multi-Label Classification*, arXiv:1602.02068v1, publicly posted February 5, 2016, https://arxiv.org/abs/1602.02068.

[4] J. Lellmann, J. Kappes, J. Yuan, F. Becker, C. Schnörr, *Convex Multi-Class Image Labeling by Simplex-Constrained Total Variation*, SSVM 2009, https://www.lellmann.net/work/_media/files/lellmann_ssvm09.pdf.

[5] *Sharp Cyclic-Variation Amplification of Euclidean Simplex Projection*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-cyclic-variation-amplification-of-euclidean-simplex-projec--95284892279a.

