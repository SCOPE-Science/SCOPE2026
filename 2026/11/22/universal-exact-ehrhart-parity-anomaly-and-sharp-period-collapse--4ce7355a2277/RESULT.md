# Universal exact Ehrhart parity anomaly and sharp period collapse for alternating odd cycles

## Finding
Let \(d\ge3\) be odd, let \(b_1,\ldots,b_d\) be positive integers, and define the bounded rational polytope
\[
Q(b)=\{x\in\mathbb R^d_{\ge0}:x_i+x_{i+1}\le b_i\quad(1\le i\le d)\},\qquad x_{d+1}=x_1.
\]
Write \(L_b(q)=\#(qQ(b)\cap\mathbb Z^d)\) for integers \(q\ge0\). By rational Ehrhart theory, the counting function has even and odd constituent polynomials \(E_b(t),O_b(t)\). Let \(B\) be the \(d\times d\) cyclic adjacent-sum matrix, \((Bx)_i=x_i+x_{i+1}\), and set \(h=B^{-1}b\).

**Theorem (exact parity classification).** For every such \(d,b\),
\[
E_b(t)-O_b(t)=
\begin{cases}
2^{-d},&h_i>0\text{ for every }i\text{ and }\sum_i b_i\text{ is odd},\\
0,&\text{otherwise}.
\end{cases}
\]
In the first case the *minimal* Ehrhart quasiperiod is two, and in the second case the counting function is a polynomial (minimal quasiperiod one). The nonzero constituent difference is a **constant**, independent of every capacity and of the dilation variable.

For the period-two capacities \(d=2m+1\), \(b_i=s+1\) at odd \(i\) and \(b_i=s\) at even \(i\), with \(s\ge1\) integral, this specializes to the sharp phase diagram
\[
E_{d,s}(t)-O_{d,s}(t)=
\begin{cases}
2^{-(2m+1)},&s\ge m\text{ and }s\equiv m\pmod2,\\
0,&\text{otherwise}.
\end{cases}
\]
Thus increasing \(s\) alternates between polynomial Ehrhart counting and exact quasiperiod two after the sharp geometric threshold \(s=m\).

## Assumptions and scope
All capacities are **positive integers**, \(d=2m+1\ge3\) is odd, and all indices are cyclic. The polytope is full-dimensional because it contains a sufficiently small positive cube and bounded because \(0\le x_i\le\min(b_{i-1},b_i)\). The corresponding lattice is the standard \(\mathbb Z^d\). The constituent polynomials are the unique degree-at-most-\(d\) polynomials agreeing with \(L_b(q)\) on positive even and positive odd integers, respectively. Quasiperiod refers to the Ehrhart coefficient functions, not the numerical sequence \(q\mapsto L_b(q)\).

## Proof
**1. Exactly one possible fractional vertex.** Deleting any coordinate at which \(x_i=0\) breaks the odd cycle into a path. The remaining adjacent-sum constraint matrix together with coordinate inequalities is totally unimodular, because a path is bipartite. Thus every vertex having a zero coordinate is integral. Any vertex with all coordinates positive has no active coordinate inequalities; it needs \(d\) independent active edge inequalities and hence all \(d\) must be tight. The unique solution is \(h=B^{-1}b\). Since \(d\) is odd, \(\det B=2\). Moreover,
\[
B\mathbb Z^d=\{z\in\mathbb Z^d:\sum_i z_i\equiv0\pmod2\}.
\]
Indeed containment follows by summing the coordinates of \(Bx\); equality follows from the index \(|\det B|=2\). Consequently \(h\) is integral exactly when \(\sum_i b_i\) is even. If \(h\) has strictly positive coordinates it is a (simple) vertex, since its \(d\) active edge normals are independent and all nonnegativity constraints are strict. If it is not strictly positive it is not a nonintegral vertex, and all vertices are integral. This establishes that all vertex denominators divide two and proves polynomiality in the absence of a positive half-integral \(h\).

**2. Cone-parity identity at the exceptional vertex.** Suppose now \(h_i>0\) for all \(i\) and \(H:=\sum_i b_i\) is odd. In the tangent cone of \(qQ(b)\) at \(qh\), write the slack variables \(\ell=qb-Bx\ge0\). For integer \(x\), the vector \(\ell\) is integral and, by the displayed lattice-image identity,
\[
\sum_i\ell_i\equiv qH\equiv q\pmod2.
\]
Conversely every nonnegative integer \(\ell\) of this parity gives exactly one lattice point \(x=B^{-1}(qb-\ell)\) in this tangent cone. For independent generic exponential variables \(z=(z_1,\ldots,z_d)\), let \(u_j(z)=\exp(-\langle z,B^{-1}e_j\rangle)\). The vertex-cone exponential generating function, interpreted first where convergent and then as a rational meromorphic function, is
\[
\mathcal C_{h,q}(z)=\frac{e^{q\langle h,z\rangle}}2\left[
\prod_{j=1}^d\frac1{1-u_j(z)}+(-1)^q\prod_{j=1}^d\frac1{1+u_j(z)}\right].
\]
The first factor in brackets is parity-independent; the second is **analytic at \(z=0\)**, with value \(2^{-d}\). Hence the even and odd symbolic vertex-cone constituents differ by the analytic germ
\[
e^{t\langle h,z\rangle}\prod_{j=1}^d(1+u_j(z))^{-1},
\]
whose value at \(z=0\) is exactly \(2^{-d}\), independently of \(t\) and \(b\).

**3. Global Ehrhart counting.** Brion's exact rational-cone identity decomposes the exponential lattice-point sum of \(qQ(b)\) into the exponential generating functions of all its vertex tangent cones. The tangent cone at any integral vertex \(v\) contributes \(e^{q\langle v,z\rangle}\) times a fixed rational function of \(z\). The constant term of its Laurent expansion at \(z=0\) is consequently a polynomial in \(q\), independent of dilation parity. The same holds for the parity-independent part of the exceptional cone, since its sole dependence on \(q\) is the exponential factor. Thus the entire parity difference in the Ehrhart constituent polynomials is the regular difference isolated in Step 2, namely \(2^{-d}\). The rational-vertex denominator divides two, so no other coefficient period occurs. Nonzero difference excludes period one. If the exceptional cone is absent or integral, every vertex contribution is polynomial and the Ehrhart count is polynomial. This proves the theorem, including the minimal periods.

**4. Alternating capacities.** Let \(d=2m+1\) and \(s\ge1\). The unique all-tight solution has
\[
h_{2k+1}=\frac{s+m+1-2k}{2}\quad(0\le k\le m),\qquad
h_{2k}=\frac{s-m+2k-1}{2}\quad(1\le k\le m).
\]
Its smallest coordinate is \((s-m+1)/2\), so it is strictly positive exactly when \(s\ge m\). Also \(\sum_i b_i=(2m+1)s+m+1\) is odd exactly when \(s\equiv m\pmod2\). Substitution yields the claimed sharp phase diagram.

## Verification
The accompanying `checker.py` performs exact integer dynamic-programming counts of lattice points at enough dilations to interpolate both degree-at-most-\(d\) constituents over \(\mathbb Q\). It checks the all-tight solution and verifies the predicted constant difference, including integral and infeasible exceptional-corner regimes. Sixteen parameter vectors were successfully checked, including nonalternating positive capacities and dimensions three, five, and seven. These finite computations are corroboration only. The universal assertion follows from the exact cone-parity argument and Brion's theorem.

## Relationship to prior work
Zhou (arXiv:2611.15122, initially public November 11, 2026) studies precisely this *alternating path and cyclic family* and derives dimension-generating functions for fixed capacities, but does not determine the fixed-dimensional cyclic **Ehrhart quasiperiod** or its amplitude. Jiang, Wen and Zhong (arXiv:2607.14887) analyze the opposite-phase alternating pattern through transfer matrices, including cyclic counts at one dilation; their dimension-variable trace identities do not imply the claimed complete parity classification without additional geometric work.

Jiang, Yang and Zhong (arXiv:2607.22008) show that **uniform-capacity** odd cyclic block polytopes have denominator two and quasiperiod dividing two. The published result *Exact parity degree and minimal quasiperiod of odd cyclic block polytopes* establishes that for unit capacities and block size one, the parity discrepancy is \(2^{-d}\). That **special case is credited**. The new theorem extends the quantitative law to arbitrary positive integral capacities and, importantly, gives a necessary-and-sufficient *presence/collapse* criterion. The alternating specialization has distinct geometric and arithmetic phases, none of which follows from a statement limited to unit capacities.

Hamano–Hibi–Ohsugi (arXiv:1603.09613) study the **unit-capacity** fractional stable-set polytope for arbitrary finite graphs. Their unweighted Ehrhart results do not supply this RHS-dependent phase diagram.

## Limitations
The proof invokes Brion's exact cone decomposition as an external theorem. It does not compute the full polynomial part of the Ehrhart quasipolynomial, nor claim a nontrivial oscillation for even cycles (whose constraint matrix is totally unimodular). The new result is closely related methodologically to the published uniform-capacity parity-cone calculation: its mathematical advance is the general integer-capacity classification and the sharp alternating-parameter threshold, not discovery of the basic parity-filter technique. Historical priority for an exact weighted-capacity version remains provisional, especially if described elsewhere under vertex-capacitated fractional matching terminology. Independent mathematical audit has not been performed.

## References
- Yangbiao Zhou (2026). *Ehrhart Series and Transfer Matrices for Period-Two Polytopes with Consecutive Inequalities*, arXiv:2611.15122, first public 2026-11-11. https://arxiv.org/abs/2611.15122
- Xinru Jiang, Suzhen Wen, Yueming Zhong (2026). *Alternating adjacent-sum polytopes: transfer matrices and Ehrhart series*, arXiv:2607.14887. https://arxiv.org/abs/2607.14887
- Xinru Jiang, Shuai Yang, Yueming Zhong (2026). *Transfer Matrices and Ehrhart Theory for Path and Cyclic Block Polytopes*, arXiv:2607.22008. https://arxiv.org/abs/2607.22008
- *Exact parity degree and minimal quasiperiod of odd cyclic block polytopes* (2026). Public record https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-parity-degree-and-minimal-quasiperiod-of-odd-cyclic-block--c9d98c9238ae
- Ginji Hamano, Takayuki Hibi, Hidefumi Ohsugi (2018). *Ehrhart series of fractional stable set polytopes of finite graphs*, Annals of Combinatorics 22, 563–573; arXiv:1603.09613.
- Michel Brion (1988). *Points entiers dans les polyèdres convexes*. Annales scientifiques de l'École Normale Supérieure 21, 653–663.
