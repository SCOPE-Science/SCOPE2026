# Two-stage RKL1 graph diffusion: a degree-only positivity barrier and sharp star reentry

## Finding

For **every** finite simple unweighted undirected graph \(G\), let \(L\) be its combinatorial Laplacian, \(d_v\) each vertex degree, and \(c_{uv}=|N(u)\cap N(v)|\) for distinct vertices. Apply the **unmodified two-stage first-order Runge–Kutta–Legendre** (RKL1) heat endpoint to \(u'=-Lu\):

\[
T_h=P_2(I-hL/3)=I-hL+\frac{h^2}{6}L^2,\qquad h\ge0,\quad P_2(x)=\frac{3x^2-1}{2}.
\]

For each \(d\ge3\) define
\[
h_\pm(d)=\frac{3}{d+1}\left(1\pm\sqrt{\frac{d-2}{3d}}\right),
\qquad
h_E=\min_{uv\in E(G)}\frac{6}{d_u+d_v-c_{uv}},
\]
where \(h_E=+\infty\) if the graph has no edges. Then the **complete endpoint-positivity set** is
\[
\boxed{\{h\ge0:T_h\ge0\text{ entrywise}\}
=[0,h_E]\setminus\bigcup_{v:d_v\ge3}(h_-(d_v),h_+(d_v)).}
\]
The set notation means that equality at a zero entry is permitted.

More strongly, if the graph's maximum degree is \(\Delta\ge3\), its **sharp initial nonnegative-step interval is exactly \([0,h_-(\Delta)]\)**, independently of all triangles, connectivity, and other degree counts. Every such graph admits a strictly larger step for which \(\|T_h\|_2\le1\) but a diagonal entry of \(T_h\) is negative. This separates spectral energy stability from positivity on **every** graph containing a branching vertex.

On a unit star \(K_{1,m}\) with \(m\ge3\), the full scalar-stable interval is \([0,6/(m+1)]\), and its exact positivity set inside that interval is
\[
\boxed{[0,h_-(m)]\;\cup\;[h_+(m),6/(m+1)].}
\]
The first such star is the four-vertex \(K_{1,3}\): at \(h=3/4\) the hub diagonal equals \(-1/8\), although every scalar eigenmode is stable. For \(m=1,2\), the star endpoint is nonnegative throughout its scalar-stable interval. As \(m\to\infty\), the forbidden band occupies the exact limiting fraction \(1/\sqrt3\) of the scalar-stable interval.

## Assumptions and scope

A finite simple undirected unweighted graph has adjacency matrix \(A\), degrees \(d_v\), and \(L=D-A\). Graphs may be disconnected or have isolated vertices. Entries of \(T_h\) are real. Entrywise nonnegativity is required for **all nonnegative initial data** at the **completed timestep** only; intermediate stages are not constrained. As \(L\mathbf1=0\), the endpoint always has row sums one, so entrywise nonnegativity is equivalent to being a stochastic matrix. The stability assertion is ordinary Euclidean norm contraction \(\|T_h\|_2\le1\) for symmetric \(L\).

The RKL1 polynomial here is **not** the modified, positive-spectrum shifted Legendre method. Its first-order two-stage polynomial \(1+z+z^2/6\) must not be confused with the order-two two-stage RKL2 polynomial \(1+z+z^2/2\).

## Proof

**1. All entry signs.** Since \(L=D-A\), exact multiplication gives
\[
(L^2)_{vv}=d_v(d_v+1),\quad
(L^2)_{uv}=c_{uv}-d_u-d_v\quad(uv\in E),\quad
(L^2)_{uv}=c_{uv}\quad(uv\notin E,\ u\ne v).
\]
Indeed \((A^2)_{uv}=c_{uv}\), while \((A^2)_{vv}=d_v\). Consequently
\[
(T_h)_{vv}=1-d_vh+\frac{d_v(d_v+1)}6h^2,
\]
\[
(T_h)_{uv}=h\left[1-\frac{d_u+d_v-c_{uv}}6h\right]\quad(uv\in E),
\]
\[
(T_h)_{uv}=\frac{c_{uv}}6h^2\ge0\quad(uv\notin E,\ u\ne v).
\]
For an edge, \(c_{uv}\le\min(d_u,d_v)-1\) so its denominator in \(h_E\) is positive. Each edge entry is nonnegative precisely up to its displayed bound. Vertex degree \(0\) or \(1\) gives a positive diagonal; at degree \(2\) it is \((1-h)^2\) and is never negative. For integer \(d\ge3\), its discriminant is \(d(d-2)/3>0\); its two positive roots are \(h_\pm(d)\), and the quadratic is negative precisely between them. Intersecting every entry's exact sign condition proves the complete classification (without any numerical root search).

**2. Universal branching horizon.** Both \(d\mapsto3/(d+1)\) and \(d\mapsto1-\sqrt{(d-2)/(3d)}\) are positive and strictly decreasing for \(d\ge3\). Their product \(h_-(d)\) is therefore strictly decreasing. The earliest vertex-diagonal obstruction occurs at a vertex of maximum degree \(\Delta\).

For any edge, \(d_u+d_v-c_{uv}\le 2\Delta\), so \(h_E\ge3/\Delta\). But
\[
0<h_-(\Delta)<\frac3{\Delta+1}<\frac3\Delta\le h_E.
\]
Hence **no off-diagonal entry becomes negative before the first maximum-degree diagonal**, and every \(h\le h_-(\Delta)\) is nonnegative. For every sufficiently small \(\varepsilon>0\), the diagonal at a maximum-degree vertex is negative at \(h=h_-(\Delta)+\varepsilon\), proving sharpness.

The Laplacian is symmetric positive semidefinite, with \(\lambda_{\max}(L)\le2\Delta\) by Gershgorin. For all \(0\le x\le6\), \(|P_2(1-x/3)|\le1\): the Legendre polynomial lies in \([-1/2,1]\) on \([-1,1]\), and the argument \(1-x/3\) runs across that interval. Therefore \(\|T_h\|_2\le1\) whenever \(0\le h\le6/\lambda_{\max}(L)\). Since \(h_-(\Delta)<3/\Delta\le6/\lambda_{\max}(L)\), choose a small enough positive \(\varepsilon\) that \(h_-(\Delta)+\varepsilon\) is both scalar-stable and diagonal-negative. This proves the all-branching spectral-stability/positivity separation.

**3. Sharp star phase diagram and minimality.** For \(K_{1,m}\), each spoke joins degrees \(m\) and \(1\), with zero common neighbors, so \(h_E=6/(m+1)\). The leaf degree-one diagonal is always positive, and the hub diagonal alone has the forbidden interval \((h_-(m),h_+(m))\) when \(m\ge3\). Its right endpoint lies strictly below \(6/(m+1)\), because the square root in \(h_+(m)\) is less than one. The star Laplacian has eigenvalues \(0\), \(1\) with multiplicity \(m-1\), and \(m+1\), so its exact scalar-stability interval is \([0,6/(m+1)]\). Combining yields the displayed two-window formula. At \(m=3\), the hub diagonal at \(h=3/4\) is
\[
1-3(3/4)+\frac{3\cdot4}{6}(3/4)^2=-\frac18.
\]
For \(m\le2\), the hub has no negative diagonal and all edges remain nonnegative through the spectral endpoint. Every graph on at most three vertices has maximum degree at most two; in such graphs all diagonals are nonnegative and each edge transition, once negative, cannot recover at a larger step. Thus a four-vertex graph is minimal for this loss-and-recovery phenomenon. Finally,
\[
\frac{h_+(m)-h_-(m)}{6/(m+1)}=\sqrt{\frac{m-2}{3m}}\longrightarrow\frac1{\sqrt3}.
\]
All quantified claims follow by exact algebra and elementary spectral bounds.

## Verification

The standalone `verify.py` uses only Python standard-library rational arithmetic for matrix products and entrywise signs. It enumerates **1,099 labeled simple graphs through five vertices**, checks 12 nonnegative rational steps on every graph, and verifies exact local entries, row sums and the sharp positivity test. It also tests explicit star orbit formulas for 100 star sizes and the \(-1/8\) four-vertex witness. Replaying `python verify.py` produced: `PASS 1099 labelled simple graphs with n<=5, 40565 exact checks; 100 star sizes and exact witness -1/8`. This is finite regression evidence; the all-graph and all-step assertions are established by the proof above, not by enumeration.

## Relationship to prior work

Tan, Aslam and Bertozzi (2026), Section 3.1 formula (11), define the unmodified RKL1 Legendre stability polynomial studied here. Their maximum-principle analysis concerns particular one-dimensional periodic and Neumann spatial structures; it does **not** characterize branching graph Laplacians, nor assert the universal degree-only initial positivity horizon. Their modified first-order method in Section 4.2.3 is a distinct stability polynomial and is excluded.

An earlier published mathematical study, *A triangle-count law for positive two-stage Euler supersteps on regular graphs* (2026), derives the general identity for entries of \(L^2\) and uses it to optimize arbitrary two-factor Euler updates **on regular graphs**. That algebraic identity is already known and is **not claimed as new** here; the present fixed RKL1 method is equivalently a product of two positive-duration Euler factors. The new assessed claims are instead the maximum-degree universal sharp horizon on **arbitrary, possibly irregular graphs**, spectral-stability separation for every branching graph, and the exact smallest-star reentry diagram. The prior theorem's regular-graph optimization does not state or prove these all-irregular-graph conclusions. Such distinctions do not by themselves establish historical publication priority.

The published *Reentrant endpoint positivity of three-stage RKL2 on a minimal Markov chain* concerns the different **three-stage, second-order** RKL2 polynomial on a directed chain; its result that two-stage RKL2 cannot reenter is consistent with the present two-stage first-order RKL1 example. *Three disjoint positivity windows for two-stage Radau IIA on star networks* concerns a **rational** implicit method, not the Legendre polynomial; it exhibits a different threshold and three windows. Earlier Legendre-super-time-stepping literature, including Meyer–Balsara–Aslam and Dawes, can address related positivity phenomena; not all original full texts were accessible, so a residual historical overlap risk remains.

## Limitations

This is a statement about exact arithmetic and completed linear heat steps on finite **unweighted undirected simple graphs**, not arbitrary finite-state Markov generators, nonlinear Allen–Cahn splitting, variable coefficients, weighted graph Laplacians, floating-point propagation, or individual internal stages. Euclidean spectral nonexpansion is weaker than a discrete maximum principle. The degree-only initial horizon applies when \(\Delta\ge3\); the all-graph exact sign classification also covers maximum degree at most two. The source comparisons cannot prove that unindexed earlier literature lacks the same theorem. No independent mathematical audit has been performed.

## References

1. Z. Tan, T. D. Aslam and A. L. Bertozzi, *Fully Explicit Stabilized Runge–Kutta Methods for Allen–Cahn and Cahn–Hilliard Dynamics*, arXiv:2611.16238v1, first publicly posted 2026-11-12, https://arxiv.org/html/2611.16238v1 .
2. *A triangle-count law for positive two-stage Euler supersteps on regular graphs*, published-finding corpus research record `2026/11/8/SCOPE-a-triangle-count-law-for-positive-two-stage-euler-supersteps-on--395a6d422888`, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-triangle-count-law-for-positive-two-stage-euler-supersteps-on--395a6d422888 .
3. *Reentrant endpoint positivity of three-stage RKL2 on a minimal Markov chain*, published-finding corpus research record `2026/10/25/SCOPE-reentrant-endpoint-positivity-of-three-stage-rkl2-on-a-minimal-m--3730497a7f20`, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-reentrant-endpoint-positivity-of-three-stage-rkl2-on-a-minimal-m--3730497a7f20 .
4. *Three disjoint positivity windows for two-stage Radau IIA on star networks*, published-finding corpus research record `2026/11/2/SCOPE-three-disjoint-positivity-windows-for-two-stage-radau-iia-on-sta--17146a0a41df`, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-three-disjoint-positivity-windows-for-two-stage-radau-iia-on-sta--17146a0a41df .
5. A. S. Dawes, *Some properties of the Runge–Kutta–Legendre super-time-stepping explicit methods*, *Computers & Fluids* 214 (2021), 104762, https://doi.org/10.1016/j.compfluid.2020.104762 (abstract/secondary synopsis only; complete original text not inspected).
