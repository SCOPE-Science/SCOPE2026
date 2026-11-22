# An exceptional two-stage support transition for resistance-optimal priced triangles in complete networks

## Finding
Let \(n\ge5\), and partition the vertex set of \(K_n\) into a distinguished triple \(T\) and a complement \(U\) of \(m=n-3\) vertices. Every edge with both endpoints in \(T\) has per-unit conductance price \(r>0\); every other edge has price one. Under a total cost budget \(B>0\), independently select nonnegative conductances on **all** edges so as to minimize the sum of all pairwise effective resistances, with a disconnected positive-conductance support assigned infinite cost.

There is **exactly one** global optimizer. It assigns common conductances \(a\), \(b\), \(c\), respectively, to the three edges within \(T\), the \(3m\) edges between \(T\) and \(U\), and the \(m(m-1)/2\) edges within \(U\). Always \(b>0\).

For \(n\ge6\), let
\[
r_A(n)=\frac{n(n-2)}{(n-3)(n-1)},\qquad
u=\sqrt{\frac{(n-3)(n-2)n}{n-1}}.
\]
If \(0<r<r_A(n)\), all three conductances are strictly positive. If \(r\ge r_A(n)\), the triangle conductance is exactly \(a=0\) while \(b,c>0\), and the exact optimum satisfies \(c/b=(\nu-3)/(n-3)\). In particular, \(n(r_A(n)-1)\to2\).

The five-vertex case has a different, three-phase support diagram:
\[
\begin{array}{c|c}
\text{Price range}&\text{positive edge classes}\ 
0<r<9/5&a,b,c\\
9/5\le r<45/23&a,b\quad(c=0)\\
r\ge45/23&b\quad(a=c=0).
\end{array}
\]
**An ordinary-price edge is removed while all three more expensive triangle edges are retained:** throughout \(9/5\le r<45/23\), the unique complementary edge within \(U\) is absent but every triangle edge is present. This intermediate phase does not occur for any \(n\ge6\).

The exact optimizer in every phase is as follows. Put \(m=n-3\). In the fully positive regime set
\[
X=\sqrt{n\left(\frac{3(m+1)}r-2m\right)},\qquad
Y=\sqrt r\,X,\qquad
\alpha=\frac{X-m}{3},\qquad \gamma=\frac{Y-3}{m}.
\]
In the \(n\ge6\), \(r\ge r_A(n)\) regime set \(\alpha=0\), \(\gamma=(\nu-3)/m\). In the \(n=5\), \(9/5\le r<45/23\) regime set
\[
X=\sqrt{\frac{45/r-15}{2}},\qquad
\alpha=\frac{X-2}{3},\qquad\gamma=0.
\]
In the remaining \(n=5\), \(r\ge45/23\) regime set \(\alpha=\gamma=0\). Finally, in **every** regime, the optimizer is
\[
b=\frac{B}{3r\alpha+3m+\tfrac12m(m-1)\gamma},\qquad
 a=\alpha b,\qquad c=\gamma b.
\]
These formulas agree at the phase boundaries. An exact formula for the minimized Kirchhoff index is
\[
\mathcal K_*=\frac{n}{B}
\left(3r\alpha+3m+\frac{m(m-1)}2\gamma\right)
\left(\frac2{3\alpha+m}+\frac{m-1}{m\gamma+3}+\frac1n\right).
\]

## Assumptions and scope
The graph is undirected and simple. The conductance on each of its \(\binom n2\) edges is independently variable, subject to the linear equality
\[
r\sum_{\{i,j\}\subseteq T}w_{ij}+\sum_{\{i,j\}\not\subseteq T}w_{ij}=B,
\qquad w_{ij}\ge0.
\]
The underlying graph is a complete graph before allocation; zero optimal conductance means an edge is omitted. The Kirchhoff index is \(\mathcal K(w)=\sum_{i<j}R_{ij}(w)=n\operatorname{tr}(L(w)^+)\), where \(L\) is the combinatorial conductance Laplacian. No row-stochastic normalization, fixed installation charge, or nonlinear price law is assumed. The statement covers every integer \(n\ge5\), all \(r>0\) and all \(B>0\).

## Proof
**1. Unrestricted uniqueness and symmetry.** On the connected domain, \(L(w)\) is strictly positive definite on the fixed subspace \({\bf1}^{\perp}\), and \(\mathcal K(w)=n\operatorname{tr}[(L+{\bf1}{\bf1}^{\mathsf T}/n)^{-1}]-n\). A nonzero perturbation \(D\) of edge weights produces a nonzero symmetric Laplacian perturbation \(H\), since each off-diagonal entry records one edge conductance. The second directional derivative is
\[
2n\operatorname{tr}(A^{-1}HA^{-1}HA^{-1})>0,
\qquad A=L+\frac{{\bf1}{\bf1}^{\mathsf T}}n\succ0.
\]
Indeed, conjugating \(H\) by \(A^{-1/2}\) writes this as a positive weighted trace of the square of a nonzero symmetric matrix. Thus the objective is strictly convex in all independently chosen edge weights. The budget simplex is compact, the objective tends to infinity at a disconnected limit, and a strictly positive feasible allocation exists. Therefore a connected unique optimum exists and must exhaust the budget. Permuting vertices within \(T\) and within \(U\) preserves the optimization problem; uniqueness forces precisely the three edge classes \(a,b,c\). Connectivity forces \(b>0\).

**2. Spectrum and optimization conditions.** The positive Laplacian eigenvalues of the three-class network are
\[
3a+mb\quad (\text{multiplicity }2),\qquad
mc+3b\quad (\text{multiplicity }m-1),\qquad
nb\quad (\text{multiplicity }1).
\]
Hence minimization is equivalent to minimizing
\[
h(a,b,c)=\frac2{3a+mb}+\frac{m-1}{mc+3b}+\frac1{nb}
\]
under \(3ra+3mb+\tfrac12m(m-1)c=B\), \(a,c\ge0\), \(b>0\). Put \(x=3a+mb\) and \(y=mc+3b\). With a multiplier \(\lambda\) for the budget, the necessary and sufficient convex Karush–Kuhn–Tucker conditions are
\[
-\frac6{x^2}+3r\lambda\ge0,
\qquad
m(m-1)\left(\frac\lambda2-\frac1{y^2}\right)\ge0,
\]
\[
-\frac{2m}{x^2}-\frac{3(m-1)}{y^2}-\frac1{nb^2}+3m\lambda=0,
\]
with equality in the first two inequalities whenever the corresponding conductance is positive.

**3. Interior solution.** When \(a,c>0\), the first and second stationarity conditions give \(\lambda=2/(rx^2)=2/y^2\), hence \(y=\sqrt r\,x\). Substitution in the \(b\)-stationarity condition yields
\[
\frac{x^2}{b^2}=n\left(\frac{3(m+1)}r-2m\right)=X^2.
\]
The resulting ratios are \(a/b=(X-m)/3\) and \(c/b=(\sqrt r X-3)/m\). The first stays positive exactly until
\[
r=r_A=\frac{(m+1)(m+3)}{m(m+2)}.
\]
The second stays positive exactly until \(r=r_C=3(m+4)/(2(m+3))\). Elementary subtraction gives
\[
r_C-r_A=\frac{m^3+4m^2-6m-18}{2m(m+2)(m+3)}.
\]
For every integer \(m\ge3\), the numerator is positive, while for \(m=2\), it is negative. Thus the first boundary encountered is \(a=0\) when \(m\ge3\), but \(c=0\) when \(m=2\).

**4. Boundary for \(m\ge3\).** If \(a=0\) and \(c>0\), the \(c\)- and \(b\)-stationarity equations give \(\lambda=2/y^2\) and
\[
\frac{y^2}{b^2}=\frac{m(m+1)(m+3)}{m+2}=\nu^2.
\]
Thus \(c/b=(\nu-3)/m\), positive for every \(m\ge3\). The remaining \(a\)-inequality reduces to \(r\ge\nu^2/m^2=r_A\). Hence this candidate is globally optimal, by convexity, for every \(r\ge r_A\), with no further support transitions.

**5. Two boundary changes for \(m=2\).** The full-support solution first reaches \(c=0\) at \(r=r_C=9/5\). When \(c=0\) but \(a>0\), put \(X=(3a+2b)/b\). The \(a\)- and \(b\)-stationarity equations give
\[
X^2=\frac{45/r-15}{2},\qquad \frac ab=\frac{X-2}{3}.
\]
The \(c\)-inequality is \(rX^2\le9\), which is exactly \(r\ge9/5\). Positivity of \(a\) is exactly \(r<45/23\). When \(a=c=0\), only six cross edges remain and \(b=B/6\). The \(b\)-stationarity multiplier is \(\lambda=23/(90b^2)\); the two missing-edge KKT slacks are
\[
\left(-\frac6{x^2}+3r\lambda\right)=\frac{23r-45}{30b^2},\qquad
m(m-1)\left(\frac\lambda2-\frac1{y^2}\right)=\frac1{30b^2}.
\]
They are nonnegative exactly when \(r\ge45/23\). Therefore the formulas establish the entire five-vertex phase diagram. Every candidate satisfies all unrestricted KKT conditions, and strict convexity proves it is the unique global optimizer. The budget substitution and eigenvalues above yield the exact minimum formula.

## Verification
Run `python3 verify_triangle.py` with Python, NumPy and SymPy installed. The script directly builds full weighted Laplacians, checks exact characteristic polynomials and inverse traces using rational data, and checks all individual-edge KKT gradients (not just group derivatives) at independently calculated optimal designs. It reports 3007 assertions/counted checks in the packaged version. These finite tests do not establish the all-size and all-price theorem; that follows from the analytic spectral reduction and convex KKT proof above.

## Relationship to prior work
Ghosh, Boyd and Saberi [1] established the convex total-effective-resistance formulation and gave analytic examples for equal-price graphs, including complete networks, as well as wheels and barbells. Johnson and Chertkov [2] considered cost-weighted resistance optimization and sparse power-network design with additional nonlinear objectives. Neither inspected treatment gives the priced-triangle full-support classification or the two five-vertex thresholds.

The previously published priced-perfect-matching complete-network theorem [3] has a different marked-edge incidence pattern and two edge orbits. It determines a single marked-class deletion frontier, but cannot by graph specialization or implication produce the three-orbit, unmarked-before-marked deletion phenomenon here. The published priced complete-tripartite theorem [4] concerns edges **between** independent vertex classes and another two-orbit design; its own small-size exception does not imply the present complete-graph formulas. The main novelty claimed here is the **exact three-class phase diagram and exceptional sequential support deletion**; convexity, general KKT theory and uniform-price resistances are antecedents, not claimed as new.

## Limitations
Only the specified complete-graph geometry and a single uniform triangle premium are covered. The result does not describe arbitrary tariff subsets, nonlinear prices, electrical safety after line failure, or all graphs containing triangles. The strict convexity proof requires ordinary nonnegative conductances and a linear budget. A literature search and inspections cannot rule out every differently named equivalent earlier calculation; independently indexed historical classifications remain a priority risk. No external mathematical audit is asserted.

## References
[1] A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, MTNS 2006, July 24–28, 2006, original conference version, https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf ; expanded SIAM Review **50** (2008), 37–66, https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf.

[2] J. K. Johnson and M. Chertkov, *A Majorization-Minimization Approach to Design of Power Transmission Networks*, arXiv:1004.2285 (first public version April 13, 2010), https://arxiv.org/html/1004.2285v2.

[3] *A sharp matching-price transition in resistance-optimized complete networks*, published October 13, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-a-sharp-matching-price-transition-in-resistance-optimized-comple--cf3b1355b128.

[4] *Priced complete-tripartite resistance design: exact edge deletion and the critical \(1/m\) price window*, published November 2, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-priced-complete-tripartite-resistance-design-has-an-exact-shortc--93a220470d32.
