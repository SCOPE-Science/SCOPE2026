# A sharp 25%-loss/50%-gain law for RK3 versus RK2 positivity on directed Markov cycles

## Finding

Let \(n\ge4\), and let \(r_0,\ldots,r_{n-1}>0\) be the exit rates of a clockwise continuous-time Markov chain on a directed \(n\)-cycle (indices modulo \(n\)). Let \(Q\) be its row generator, so that \(Q_{i,i}=-r_i\), \(Q_{i,i+1}=r_i\), and all other entries vanish. For \(p=2,3\), consider the unmodified degree-\(p\) exponential Taylor / explicit \(p\)-stage order-\(p\) Runge–Kutta endpoint
\[
T_p(h)=\sum_{j=0}^{p}\frac{h^jQ^j}{j!},\qquad h\ge0.
\]
Write \(H_p\) for the largest \(h\) for which \(T_p(s)\) is entrywise nonnegative at **every** \(0\le s\le h\). Define the local rate statistics
\[
M=\max_i r_i,\qquad A=\max_i(r_i+r_{i+1}),\qquad C=\max_i(r_i+r_{i+1}+r_{i+2}),
\]
and let \(\rho\in(3/2,2)\) be the unique root of \(1-z+z^2/2-z^3/6=0\), namely \(\rho=1.5960716379833217\ldots\).

**Exact horizons and sharp order comparison:**
\[
\boxed{H_2=\frac2A,\qquad H_3=\min\left\{\frac\rho M,\frac3C\right\}.}
\]
Each method's full nonnegative-timestep set is exactly \([0,H_p]\), with no positivity reentry. For every positive rate vector,
\[
\boxed{\frac34<\frac{H_3}{H_2}<\frac32.}
\]
Both constants are **sharp strict bounds**: the infimum over all such chains is \(3/4\), and the supremum is \(3/2\), already for \(n=4\); neither bound is attained at strictly positive rates. More precisely,
\[
\frac{H_3}{H_2}=\min\left\{\frac{\rho A}{2M},\frac{3A}{2C}\right\},
\]
so RK3 permits a strictly larger positivity-preserving step than RK2 if and only if **both** \(\rho A>2M\) and \(2C<3A\). Reversing either strict inequality to \(<\) yields a smaller RK3 horizon; equality cases follow directly from the displayed minimum.

On the natural single-fast-state family \(r=(R,1,\ldots,1)\), \(R\ge1\), the two methods tie at \(R=1\), RK3 admits a strictly larger step for \(1<R<\rho/(2-\rho)\), ties again at \(R=\rho/(2-\rho)=3.95137303559144\ldots\), and admits a strictly smaller step for all greater contrasts. Thus higher temporal order can *either improve or degrade* endpoint positivity headroom, even within one fixed directed-cycle topology.

## Assumptions and scope

The process is a homogeneous-in-time irreducible directed Markov cycle with \(n\ge4\) and positive rates. Matrices act on probability row vectors on the right. Endpoint nonnegativity is equivalent to preservation of every nonnegative initial row vector; the row sums are one for all \(h\) because \(Q\mathbf1=0\). No claim is made about positivity of the internal RK stages, nonlinear strong-stability-preserving guarantees, error accuracy, spectral stability, optimal computational cost, or cycles of length two or three. The result applies to any explicit two-stage second-order and explicit three-stage third-order Runge–Kutta scheme on this autonomous linear system, since their stability polynomials are respectively \(T_2\) and \(T_3\).

## Proof

**1. Exact entries, including the shortest allowed cycle.** Since at most three moves are possible in \(Q^3\) and \(n\ge4\), different forward jump counts \(0,1,2,3\) reach different destinations. A term with \(k\) forward jumps has the product of the first \(k\) visited exit rates; each diagonal stay contributes the negative rate at its current vertex. Put \(a=r_i\), \(b=r_{i+1}\), and \(c=r_{i+2}\). Direct expansion yields
\[
\begin{aligned}
(T_3)_{ii}&=1-ah+\tfrac12a^2h^2-\tfrac16a^3h^3,\\
(T_3)_{i,i+1}&=ah\left[1-\tfrac12(a+b)h+\tfrac16(a^2+ab+b^2)h^2\right],\\
(T_3)_{i,i+2}&=\tfrac16abh^2[3-(a+b+c)h],\\
(T_3)_{i,i+3}&=\tfrac16abch^3.
\end{aligned}
\]
All remaining entries are zero. The corresponding \(T_2\) entries are the same expressions after deleting cubic terms, with \((T_2)_{i,i+3}=0\). These identities are valid at \(n=4\): forward distances \(0,1,2,3\) still label distinct columns.

**2. Exact RK2 horizon.** For \(z\ge0\), \(1-z+z^2/2=((z-1)^2+1)/2>0\). The two-hop entry is \(abh^2/2>0\) at positive steps. The one-hop entry is \(ah[1-(a+b)h/2]\), nonnegative if and only if \(h\le2/(a+b)\). Thus the first negative entry occurs at the first exceeded one-hop constraint, and positivity holds exactly on \([0,2/A]\).

**3. Exact RK3 horizon.** For \(z\ge0\), the diagonal scalar \(q_3(z)=1-z+z^2/2-z^3/6\) has derivative
\[
q_3'(z)=-\frac{(z-1)^2+1}{2}<0.
\]
It vanishes uniquely at \(\rho\in(3/2,2)\), since \(q_3(3/2)=1/16>0\) and \(q_3(2)=-1/3<0\). Hence all diagonals stay nonnegative exactly for \(h\le\rho/M\). The one-hop quadratic bracket is strictly positive for every real \(h\), since its discriminant is
\[
\frac{(a+b)^2}{4}-\frac23(a^2+ab+b^2)=-\frac{5a^2+2ab+5b^2}{12}<0.
\]
The three-hop term is positive for every \(h>0\), whereas the two-hop term is nonnegative precisely for \(h\le3/(a+b+c)\). Their intersection proves \(H_3=\min\{\rho/M,3/C\}\) and shows that the relevant violating entry remains negative at every greater step: neither method has positivity reentry.

**4. Sharp universal comparison.** From the definitions and strict positivity,
\[
M<A,\qquad A<C\le A+M<2A.
\]
Therefore
\[
\frac{\rho A}{2M}>\frac\rho2>\frac34,\qquad
\frac34<\frac{3A}{2C}<\frac32.
\]
Taking the minimum establishes the two strict bounds. The displayed formula for \(H_3/H_2\) directly establishes the two-inequality characterization of which order has the larger positivity horizon.

For \(0<\varepsilon\ll1\), the four-cycle rate vector \((1,\varepsilon,1,\varepsilon)\) gives \(M=1\), \(A=1+\varepsilon\), \(C=2+\varepsilon\), and
\[
\frac{H_3}{H_2}=\frac{3(1+\varepsilon)}{2(2+\varepsilon)}\longrightarrow\frac34.
\]
The four-cycle vector \((1,1,\varepsilon,\varepsilon)\) gives \(M=1\), \(A=2\), \(C=2+\varepsilon\), and
\[
\frac{H_3}{H_2}=\frac3{2+\varepsilon}\longrightarrow\frac32.
\]
For both examples, \(3/(2+\varepsilon)<\rho\) when \(\varepsilon\) is sufficiently small; this justifies the active minimum branches. The bounds cannot be improved, and strictness proves they are not attained.

**5. Rate-defect switch.** On the \(n\ge4\) cycle with rates \((R,1,\ldots,1)\) and \(R\ge1\), the statistics are \(M=R\), \(A=R+1\), \(C=R+2\). The inequality \(2C<3A\) is equivalent to \(R>1\), while \(\rho A>2M\) is equivalent to \(R<\rho/(2-\rho)\). Equality cases give the asserted exact two-tie, one-switch classification.

## Verification

The standalone `verify.py` evaluates \(T_2\) and \(T_3\) independently by exact rational matrix powers, then compares the complete matrices with the four claimed entry types. In a deterministic test over cycle lengths \(4\) through \(9\), it performed 52,032 exact entry comparisons and 7,488 exact row-sum checks. It also performed 2,240 two-sided numerical horizon checks, bracketed \(\rho\), and tested the two sharpness families and the single-defect switch. Running `python3 verify.py` reproduces `verification_output.txt`. These finite tests do not replace the universal algebraic argument above.

## Relationship to prior work

Blanes, Iserles and Macnamara (first public preprint 2021-02-16, subsequent journal version 2022) develop positivity-preserving methods for graph-Laplacian population models and explain why standard higher-order integrators can violate positivity, but the inspected main analysis does not supply the present sharp comparison of two unmodified polynomial RK orders on heterogeneous directed cycles. Horváth, Song and Terlaky (2014) provide general polynomial-root procedures for invariance-preserving step thresholds, rather than an evaluated, all-rates two-method frontier or the sharp \(3/4\)-to-\(3/2\) ratio theorem. Horváth (2005, Sections 2–4) proves universal RK positivity thresholds for function classes and studies larger invariant cones, but does not derive these directed-cycle formulas or a two-method rate-profile comparison. Gerisch and Weiner (1999/2003) compare low-order explicit RK schemes for positivity in splitting methods, not an exact two-polynomial, all-rate Markov-cycle endpoint classification.

The published result *Exact RK4 positivity on heterogeneous directed cycles and a sharp CFL gain* gives an exact degree-four positivity classification on cycles of length at least five and a general walk-expansion identity. This algebraic identity also explains why local rate sums appear here, but its fourth-order one-/three-hop constraints do **not** imply the second- versus third-order step comparison, its dimension-four cases, or the pair/triple-based sharp ratio. The published *Exact positivity radii and an order-three reversal for Taylor Runge–Kutta diffusion on complete multipartite graphs* concerns symmetric, uniform-rate complete multipartite graph Laplacians, not directed cycles with arbitrary rates. Its order-reversal phenomenon motivates checking whether either order dominates; it does not settle the present two-sided bound or defect contrast.

## Limitations

The comparison is about endpoint nonnegativity rather than internal-stage feasibility, time-integration accuracy, cost efficiency, or nonlinear SSP coefficients. It cannot be extrapolated to general directed graphs, other RK stages/orders, or cycles of length two or three. At the two sharp ratio extremes some rates tend to zero: the infimum and supremum are never attained by an irreducible strictly positive-rate cycle. Although the primary results and accessible same-object claims were compared, publication-priority certainty is limited by the bounded literature coverage; specialist older RK positivity work may contain differently phrased statements. No independent mathematical audit has been performed.

## References

1. S. Blanes, A. Iserles and S. Macnamara, *Positivity-preserving methods for population models*, arXiv:2102.08242, first publicly posted 2021-02-16; journal title *Positivity-preserving methods for ordinary differential equations*, ESAIM M2AN 56 (2022), 1843–1870, https://arxiv.org/abs/2102.08242, https://doi.org/10.1051/m2an/2022042.
2. Z. Horváth, Y. Song and T. Terlaky, *Steplength thresholds for invariance preserving of discretization methods of dynamical systems on a polyhedron*, arXiv:1406.6755, 2014-06-26, https://arxiv.org/abs/1406.6755, https://doi.org/10.3934/dcds.2015.35.2997.
3. *Exact RK4 positivity on heterogeneous directed cycles and a sharp CFL gain*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-rk4-positivity-on-heterogeneous-directed-cycles-and-a-shar--36d0a038ee0c.
4. *Exact positivity radii and an order-three reversal for Taylor Runge–Kutta diffusion on complete multipartite graphs*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-positivity-radii-and-an-order-three-reversal-for-taylor-ru--0aa3ec090e79.
5. Z. Horváth, *On the positivity step size threshold of Runge–Kutta methods*, Appl. Numer. Math. 53 (2005), 341–356, https://doi.org/10.1016/j.apnum.2004.08.026 (Sections 2–4 address positive IVP classes and invariant cones).
6. A. Gerisch and R. Weiner, *On the positivity of low order explicit Runge–Kutta schemes applied in splitting methods*, 1999 preprint, https://www2.mathematik.uni-halle.de/reports/sources/1999/99-35report.pdf (comparison of explicit schemes for splitting rather than directed-cycle horizons).

