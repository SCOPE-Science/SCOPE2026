# Exact integer-diffusion two-cycle census on double stars

## Finding
For integers \(a,b\ge1\), form the labelled double star \(D_{a,b}\) from adjacent hubs \(U,V\), with \(a\) distinct leaves attached to \(U\) and \(b\) distinct leaves attached to \(V\). Under synchronous integer chip diffusion, a vertex sends one chip to each neighbor having strictly fewer chips. Let \(N_{a,b}\) denote the number of configurations already periodic, counting configurations modulo addition of a common integer constant to all vertex labels. Put \(h_+=\max\{h,0\}\). Then

\[
\begin{aligned}
N_{a,b}={}&1+2(a+b+1)(a+1)^a(b+1)^b\\
 &+2(a-b+1)_+(a+1)^a(b-1)^b\\
 &+2(b-a+1)_+(a-1)^a(b+1)^b\\
 &+2\mathbf 1_{\{a=b\}}a^{2a}.
\end{aligned}
\]

There is exactly one fixed configuration modulo common translation; all other periodic configurations have primitive period two. Thus the number of distinct primitive-two temporal orbits is \((N_{a,b}-1)/2\). The formula also explicitly classifies all periodic configurations by orientations and independent bounded integer gaps on the edges. In particular, initial equality of the two hub values occurs among nonconstant periodic configurations exactly when \(a=b\), and then accounts for precisely \(2a^{2a}\) configurations.

## Assumptions and scope
Each vertex has an arbitrary integer label (negative labels are permitted). Let \(G=D_{a,b}\), with labelled vertices and \(a,b\ge1\), and define the synchronous map
\[
F(x)_v=x_v+\sum_{w\sim v}\operatorname{sgn}(x_w-x_v),
\qquad \operatorname{sgn}(t)\in\{-1,0,1\}.
\]
All updates use the labels from the preceding step. Common translation commutes with \(F\) and does not change the dynamics. Every translation class has exactly one representative with \(x_U=0\); \(N_{a,b}\) counts such representatives with \(F^2(x)=x\). It does not count transient states or their basins. The vertex labels of a fixed double star are distinguished even when the graph has automorphisms.

## Proof
**1. Edge reversal lemma.** Write \(x'=F(x)\). For every edge \(e=\{u,v\}\) choose an arbitrary orientation, put \(d_e=x_v-x_u\), \(d'_e=x'_v-x'_u\), and set \(s_e=\operatorname{sgn}(d_e)\), \(s'_e=\operatorname{sgn}(d'_e)\). If \(F^2(x)=x\), the increments \(\Delta=x'-x\) and \(\Delta'=F(x')-x'\) satisfy \(\Delta+\Delta'=0\). Summing the resulting vertex identity after multiplication by \(x_v+x'_v\) yields
\[
0=\sum_{e\in E(G)}(d_e+d'_e)(s_e+s'_e).
\]
Every summand is nonnegative: if the signs are opposite (or both zero) it vanishes, and in every other case the product is positive. Consequently every edge either stays tied in both states or switches strict sign. Conversely, if this edgewise condition holds, all edge transfers reverse on the second step or vanish on both steps, so \(F^2(x)=x\). This proves the equivalence without assuming eventual periodicity.

**2. Integer gap multiplicities on a tree.** For a proposed edge-sign pattern \(s_{uv}=\operatorname{sgn}(x_v-x_u)\), define
\[\Delta_u=\sum_{v\sim u}s_{uv},\qquad s_{vu}=-s_{uv}.\]
On an edge \((u,v)\) with \(s_{uv}\ne0\), the strict sign reverses precisely when its signed positive initial gap lies in the integer interval
\[
1\le s_{uv}(x_v-x_u)\le s_{uv}(\Delta_u-\Delta_v)-1.
\]
The number of choices is therefore \(\big(s_{uv}(\Delta_u-\Delta_v)-1\big)_+\). On a tied edge, the endpoints remain tied precisely when \(\Delta_u=\Delta_v\). For a tree, integer edge gaps specify a vertex labeling uniquely after fixing one hub label: there are no cycle-consistency constraints. Thus multiplying these local counts and summing over sign patterns gives an exact, finite census.

**3. Leaf rigidity.** Orient the hub edge from \(U\) to \(V\). Let \(s=\operatorname{sgn}(x_V-x_U)\), let \(t_i=\operatorname{sgn}(x_{L_i}-x_U)\) for the \(a\) leaves at \(U\), and let \(r_j=\operatorname{sgn}(x_{R_j}-x_V)\) for the \(b\) leaves at \(V\). The hub increments are
\[\Delta_U=s+\sum_{i=1}^a t_i,\qquad \Delta_V=-s+\sum_{j=1}^b r_j.\]
Each \(U\)-leaf has increment \(-t_i\). If \(t_i\ne0\), the number of admissible edge gaps is \((t_i\Delta_U)_+\); if \(t_i=0\), admissibility instead requires \(\Delta_U=0\). Hence any admissible pattern on a hub's leaves has either every leaf tied with that hub or all leaves strictly on one and the same side of that hub. The same holds at \(V\). The all-tied option is possible only when its hub increment vanishes.

**4. Enumeration by hub sign.** Suppose first that \(s=0\). The hub edge can stay tied only if \(\Delta_U=\Delta_V\). The leaf-rigidity condition leaves the all-tied configuration (one class), plus (only if \(a=b\)) the two patterns in which all leaves at both hubs are higher, respectively lower, than their hubs. Each of these two patterns contributes \(a^{2a}\) labelings: every leaf independently has one of \(a\) allowable signed gaps.

For \(s=+1\), neither hub may have tied leaves. Denote by \(t,r\in\{-1,+1\}\) the common signs on the two leaf sets. Their respective multiplicities are \((1+at)^a\) when \(t=+1\), \((a-1)^a\) when \(t=-1\), and correspondingly \((b-1)^b\) for \(r=+1\), \((b+1)^b\) for \(r=-1\), with a zero multiplicity if a required positive hub increment is unavailable. The hub edge admits exactly \((1+at-br)_+\) positive-gap choices. Of the four sign pairs, only three can contribute:

\[
\begin{array}{c|c}
(t,r)&\text{number of configurations}\; (s=+1)\\\hline
(+1,-1)&(a+b+1)(a+1)^a(b+1)^b\\
(+1,+1)&(a-b+1)_+(a+1)^a(b-1)^b\\
(-1,-1)&(b-a+1)_+(a-1)^a(b+1)^b.
\end{array}
\]

The missing pair \((-1,+1)\) has a nonpositive hub-edge gap factor. Negating every chip label bijects the \(s=+1\) and \(s=-1\) cases. Combining the three hub-sign cases proves the formula.

**5. Primitive periods.** The universal finite-graph diffusion theorem of Long and Narayanan [2] proves that every initially periodic configuration has least period at most two. Therefore the above \(F^2(x)=x\) census includes every initially periodic configuration. On a connected graph, a fixed point satisfies \(0=\sum_v x_v(F(x)_v-x_v)=-\sum_{\{u,v\}\in E}|x_u-x_v|\), so every vertex has the same label. Therefore the all-equal translation class is the unique fixed point. All other configurations counted by the formula have least period two and occur in pairs under \(F\). This proves the orbit count.

## Verification
Two reproducible checks accompany the result. The independently programmed `verify_direct.cpp` enumerates integer edge-gap arrays, constructs actual vertex labels, applies the diffusion rule twice, and compares the resulting fixed-point counts with the formula on six parameter pairs \((a,b)\in\{(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)\}\). This directly checks \(31{,}946{,}794\) normalized labelled initial configurations. Its finite bounds exceed the maximum possible periodic gap on each edge, given by the sum of the endpoint degrees minus one.

The separate `verify_orientation.py` enumerates all three-valued edge-sign patterns, independently multiplies admissible gap counts, and checks all \(25\) pairs \(1\le a,b\le5\). Both programs passed and their captured text outputs are provided. These finite tests check arithmetic and low-order cases; the unrestricted theorem follows from the edge-reversal and leaf-rigidity proofs above.

Illustrative totals are \(N_{1,1}=27\), \(N_{1,2}=145\), \(N_{2,2}=879\), and \(N_{3,3}=60{,}851\).

## Relationship to prior work
Duffy, Lidbetter, Messinger and Nowakowski introduced the diffusion game and proved eventual periodicity and a transient bound for ordinary stars, among other graph classes [1]. Long and Narayanan subsequently proved that every finite graph diffusion game eventually reaches period at most two [2]. Neither source gives the exact already-periodic point census for double stars. In particular, the universal period bound does not determine the size of the recurrent set, and the one-hub star argument does not account for the additional hub-edge gap and the equal-arm central tie family. The present result is an exact graph-family count, not a claim to rediscover eventual period-two behavior.

## Limitations
The theorem counts states already periodic modulo common integer translation, not their full attraction basins or the time needed for transient convergence. It is specific to double-star trees with at least one leaf at each hub; no formula for arbitrary trees or complete bipartite graphs is asserted. Literature-priority searches did not locate an identical formula, but indexing limitations and unexamined publications leave residual uncertainty; independent audit has not been performed.

## References
[1] C. Duffy, T. F. Lidbetter, M. E. Messinger, R. J. Nowakowski, *A Variation on Chip-Firing: the diffusion game*, arXiv:1609.05792 (first posted 2016-09-19), published in *Discrete Mathematics & Theoretical Computer Science* 20(1), 2018. https://arxiv.org/abs/1609.05792

[2] J. Long and B. Narayanan, *Diffusion on graphs is eventually periodic*, arXiv:1704.04295 (first posted 2017-04-13), *Journal of Combinatorics* 10(2), 2019. https://arxiv.org/abs/1704.04295
