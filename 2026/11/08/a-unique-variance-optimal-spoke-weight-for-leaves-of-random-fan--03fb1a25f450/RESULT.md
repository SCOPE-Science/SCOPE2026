# A unique variance-optimal spoke weight for leaves of random fan spanning trees

## Finding

For integers \(n\ge 1\), let \(F_n=K_1\vee P_n\) be the fan with one hub and \(n\) path vertices. Give all path edges conductance \(1\), all hub-to-path spokes conductance \(t>0\), and sample a spanning tree with probability proportional to the product of its edge conductances. Write \(L_n(t)\) for the *total* number of degree-one vertices, including the hub when it is a leaf. For \(n\ge1\), the exact unnormalized generating polynomial \(Z_n(z;t)=\sum_T t^{\#\text{spokes}(T)}z^{\#\text{leaves}(T)}\) is

\[
Z_n(z;t)=[u^n]\left[\frac{1}{1-tB(u,z)}+(z-1)tB(u,z)\right],\qquad
B(u,z)=zu+\frac{2zu^2}{1-u}+\frac{z^2u^3}{(1-u)^2}.
\]

In particular, \(\mathbb E[z^{L_n(t)}]=Z_n(z;t)/Z_n(1;t)\). Define \(r=r(t)\in(0,1)\) by
\[
t=\frac{(1-r)^2}{r}\qquad\left(r=\frac{2+t-\sqrt{t^2+4t}}{2}\right).
\]
For every fixed \(t>0\), the leaf count obeys
\[
\begin{split}
\mathbb E[L_n(t)]&=n\mu(r)+O_t(1),\\
\operatorname{Var}(L_n(t))&=nv(r)+O_t(1),\\
\frac{L_n(t)-n\mu(r)}{\sqrt n}&\Longrightarrow N(0,v(r)),
\end{split}
\]
where
\[
\mu(r)=\frac{(1-r)(1+r^2)}{1+r},\qquad
v(r)=\frac{r(1-r)(3r^5+6r^2-3r+2)}{(1+r)^3}>0.
\]
The asymptotic variance per path vertex \(v(r(t))\) has **exactly one global maximizer** \(t_*\in(0,\infty)\). It is \(t_*=(1-r_*)^2/r_*\), where \(r_*\) is the unique root in \((0,1)\) of
\[
p(r)=6r^7+6r^6-9r^5+3r^4+12r^3-16r^2+7r-1.
\]
Numerically, \(r_*\approx0.311946060484497\), \(t_*\approx1.51762847380575\), and \(v(r_*)\approx0.157487678470347\). The maximization is for the *limiting variance density*, not a claim that every finite-\(n\) variance has a unique optimizer.

## Assumptions and scope

Graphs are finite, simple and undirected. A spanning tree is weighted by the product of its spoke conductances; path edges have weight one. Throughout, \(t\) is a fixed positive real number as \(n\to\infty\). Both the hub and path vertices count as leaves if their degrees in the sampled tree equal one. The fan notation here has \(n+1\) vertices; some references instead index fans by their total vertex count. Normal convergence and the \(O_t(1)\) remainders do not claim uniformity as \(t\to0\) or \(t\to\infty\).

## Proof

**1. Exact renewal decomposition.** Every spanning tree determines a set of path edges omitted from the \(n\)-vertex path. Their deletion partitions the path into consecutive nonempty blocks, and exactly one spoke must be selected in each block: at least one spoke connects the block to the hub, and two would create a cycle. Conversely, every ordered block decomposition equipped with one selected spoke per block defines a spanning tree, and a decomposition with \(m\) blocks has weight \(t^m\).

For a block of length \(\ell\), the path vertices contribute \(a_\ell(z)\) to the leaf polynomial. If \(\ell=1\), the sole vertex is a leaf; if \(\ell=2\), exactly one is a leaf, with two choices of spoke; for \(\ell\ge3\), either endpoint spoke choice leaves one path leaf (two choices), or an interior spoke choice leaves both path endpoints as leaves (\(\ell-2\) choices). Thus
\[
a_1(z)=z,\quad a_2(z)=2z,\quad a_\ell(z)=2z+(\ell-2)z^2\ \ (\ell\ge3).
\]
Summing the block polynomials gives \(B(u,z)=\sum_{\ell\ge1}a_\ell(z)u^\ell\) as stated. Ordered compositions yield \(1/(1-tB)\). The hub is a leaf if and only if there is exactly one block, in which case that block's contribution needs one extra factor \(z\). Therefore the correction is precisely \((z-1)tB\), proving the exact generating function for every \(n\ge1\).

**2. Exponential coefficient asymptotics and Gaussian fluctuations.** At \(z=1\), the block series becomes \(B(u,1)=u/(1-u)^2\). For each fixed \(t>0\), the positive solution of \(tB(r,1)=1\) is the displayed \(r\in(0,1)\), and \(B_u(r,1)=(1+r)/(1-r)^3>0\). Because the block coefficients are strictly positive for every positive length, this simple pole is the unique dominant singularity. The implicit function theorem gives a simple analytic dominant pole \(r(s)\) of \(tB(r(s),e^s)=1\) for complex \(s\) near zero, with \(r(0)=r\). Residue extraction, uniformly on a small complex disk, gives
\[
\mathbb E[e^{sL_n(t)}]=C(s)\left(\frac{r}{r(s)}\right)^n\left(1+O_t(\eta^n)\right),\quad \eta\in(0,1),\quad C(0)=1,
\]
where \(C\) is analytic and nonzero near zero. The polynomial single-block hub correction is exponentially smaller than the simple-pole coefficient at fixed \(t\). Taylor expansion of the logarithm around \(s=0\) gives the two moment expansions and, after replacing \(s\) with \(s/\sqrt n\), the Gaussian limit by moment-generating functions.

Set \(q(s)=r(s)\), and let \(K(s)=\log r-\log q(s)\). Differentiation of \(tB(q(s),e^s)=1\) yields
\[
K'(s)=\frac{e^s B_z(q(s),e^s)}{q(s)B_u(q(s),e^s)},\qquad
q'(s)=-\frac{e^s B_z(q(s),e^s)}{B_u(q(s),e^s)}.
\]
At \(s=0\), using \(B_z(r,1)=r(1+r^2)/(1-r)^2\) and \(B_u(r,1)=(1+r)/(1-r)^3\) gives \(K'(0)=\mu(r)\). A second differentiation of the same displayed quotient, followed by simplification, gives \(K''(0)=v(r)\). The numerator of \(v(r)\) is strictly positive on \((0,1)\), since \(6r^2-3r+2>0\) and \(3r^5\ge0\).

**3. Unique global variance optimizer.** Direct differentiation gives the exact identity
\[
\frac{dv}{dr}=-\frac{2p(r)}{(1+r)^4}.
\]
A rational Sturm sequence for \(p\), obtained by taking its derivative and successive negative Euclidean remainders, has degrees \((7,6,5,4,3,2,1,0)\). Its signs at \(r=0\) are \((- + + + - + + -)\), with four variations; at \(r=1\) they are \((+ + + - - + - -)\), with three variations. No endpoint sign is zero. Sturm's theorem therefore proves **exactly one distinct root** \(r_*\in(0,1)\). Moreover \(p(0)=-1\), \(p(1)=8\), and \(v(r)\to0\) at both endpoints. Thus \(v\) increases and then decreases, attaining a unique global maximum at \(r_*\). Since \(t=(1-r)^2/r\) is a strictly decreasing bijection from \((0,1)\) onto \((0,\infty)\), the positive conductance optimizer \(t_*\) is unique as well. The numerical values are only approximations to this exact algebraic characterization.

## Verification

The accompanying \(\texttt{verify_fan.py}\) is a Python-standard-library-only checker. It independently enumerates all edge subsets of appropriate size in fans with \(1\le n\le7\), tests acyclicity and leaf counts, and matches their exact rational weighted leaf polynomials against the ordered-block recurrence at four conductances \(t\in\{1/2,1,2,5/3\}\). It separately computes moment recurrences, executes exact rational Sturm divisions and verifies the derivative polynomial identity. The present package replay passes 36 check groups; finite tests are illustrative checks and do not replace the analytic proof for arbitrary \(n\). Numerical moment ratios at \(n=20,50,100,150\) also approach the displayed variance density. Run \(\texttt{python3 verify_fan.py}\) with Python 3 and no third-party packages.

## Relationship to prior work

Cameron, Grubb and Sawada (2021) study generation, ranking and unranking of fan spanning trees, including their known Fibonacci total counts; their material gives neither this weighted leaf bivariate series nor the optimum of its variance density. Gao, Lu, Wei and Zhu (2023) give recurrences and formulas for total spanning-tree *counts* on generalized fans, not for the total number of leaves under weighted sampling. General uniform-spanning-tree degree-probability formulas, including Rapoport (2023), cover arbitrary finite graphs but do not state the evaluated fan leaf-renewal formula or the global algebraic variance optimizer. Blanco and Zeilberger (2025) obtain total leaf counts and mean-density asymptotics for specified path/cycle-power graph families, a different graph class and first-moment objective. These sources provide background tools, not the specialized asymptotic optimization statement. No claim is made that the general mechanisms of weighted spanning-tree enumeration or analytic combinatorics are new.

## Limitations

The optimization concerns \(\lim_{n\to\infty}\operatorname{Var}(L_n(t))/n\) at fixed \(t\), not a uniform-in-\(t\) finite-size optimization or an exact formula for every finite-size optimizing conductance. No Berry--Esseen rate or uniform double-scaling limit is claimed. Generic determinant/transfer-matrix methods may permit alternate derivations; historical priority for the evaluated algebraic optimizer remains subject to further literature review. Numerical experiments do not establish infinite statements or publication priority.

## References

- B. Cameron, A. Grubb and J. Sawada, *A Pivot Gray Code Listing for the Spanning Trees of the Fan Graph* (first arXiv release 2021-08-20), https://arxiv.org/abs/2108.09363 ; lawful full text: https://ar5iv.labs.arxiv.org/html/2108.09363 .
- G. Zhinan, L. Xingyan, W. Yuxuan and Z. Feng, *The Number of Spanning Trees of General Fan Graphs* (2023), https://doi.org/10.9734/arjom/2023/v19i11755 .
- A. Rapoport, *Correlations in uniform spanning trees: a fermionic approach* (2023), https://arxiv.org/abs/2312.14992 .
- P. Blanco and D. Zeilberger, *Automatic Generation of Generating Functions for Enumerating Spanning Trees* (written 2025-06-25), https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimhtml/spt.html .
