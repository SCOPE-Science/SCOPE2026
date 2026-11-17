# Unique globally variation-optimal four-node cubic interpolation with fixed endpoints

## Finding
Let \(-1=x_0<x_1<x_2<x_3=1\) and let \(I_X:\mathbb R^4\to\mathcal P_3\) be ordinary real Lagrange interpolation at these four nodes. For any vector \(y\), set \(V_X(y)=\sum_{j=0}^2|y_{j+1}-y_j|\), and for a differentiable function \(p\) let \(V(p)=\int_{-1}^1|p'(t)|\,dt\). Define the exact interpolation variation gain
\[
K(X)=\sup_{V_X(y)>0}\frac{V(I_Xy)}{V_X(y)}.
\]
This gain has a closed expression for **every** pair of strictly ordered interior nodes, and its unique global minimizer among all such endpoint-fixed four-node grids is symmetric.

Write \(x_1=m-a\), \(x_2=m+a\), so that \(a>0\) and \(|m|+a<1\). Set
\[
\begin{aligned}
B_L(m,a)&=1+\frac{4((1-m)^2+3a^2)^{3/2}}{27((1+m)^2-a^2)},\\
B_R(m,a)&=1+\frac{4((1+m)^2+3a^2)^{3/2}}{27((1-m)^2-a^2)},\\
B_C(m,a)&=\frac{4(1+a+a^2)^{3/2}[3(1+a)^2+m^2]^{3/2}}{27a(1+a)^2((1+a)^2-m^2)}-1.
\end{aligned}
\]
Then
\[
\boxed{K(X)=\max\{B_L(m,a),B_C(m,a),B_R(m,a)\}.}
\]
Each branch is realized exactly by a data vector with one nonzero adjacent jump (one of \((0,1,1,1)\), \((0,0,1,1)\), \((0,0,0,1)\)).

Define, for \(0<a<1\),
\[
E(a)=1+\frac{4(1+3a^2)^{3/2}}{27(1-a^2)},\qquad
F(a)=\frac{4(1+a+a^2)^{3/2}}{3\sqrt3\,a(1+a)}-1.
\]
There is exactly one \(a_*\in(0,1)\) satisfying \(E(a_*)=F(a_*)\). Among **all** grids with endpoints \(-1,1\), the unique minimizing grid and sharp gain are
\[
\boxed{X_*=(-1,-a_*,a_*,1),\qquad \min_X K(X)=E(a_*)=F(a_*).}
\]
A rational radical enclosure and numerical evaluation give
\[
0.4801369262<a_*<0.4801369264,\qquad K(X_*)=1.423593925054415\ldots.
\]
All three one-jump patterns are norming at the optimal grid. In comparison, Chebyshev–Lobatto's four-node grid (interior parameter \(1/2\)) has gain \(1.4572903500\ldots\), while the equispaced four-node grid (parameter \(1/3\)) has gain \(2.0068508881\ldots\).

## Assumptions and scope
The nodes are real and strictly ordered on the entire closed interval \([-1,1]\); the **outer two nodes must equal the endpoints**. Both interior nodes may otherwise be chosen freely, including asymmetrically. The input is an arbitrary real four-vector, with no monotonicity, positivity or boundedness assumption. Output variation is classical unweighted total variation on the **full interpolation interval**; input variation is the sum of adjacent sample differences. Constants are quotiented out automatically by these seminorms. All finite optimal coefficients are attained, not merely approached. The theorem is invariant under simultaneous affine changes of the interpolation interval and the node locations.

## Proof
**Step 1: Reduction to three jumps.** Denote the Lagrange cardinal polynomials by \(\ell_0,\ldots,\ell_3\), so \(\sum_j\ell_j=1\). Introduce the three step interpolants
\[
S_k(t)=\sum_{j=k}^3\ell_j(t),\qquad k=1,2,3.
\]
Writing \(d_k=y_k-y_{k-1}\) gives the identity
\[
I_Xy(t)=y_0+\sum_{k=1}^3 d_k S_k(t).
\]
Consequently \(V(I_Xy)\le\sum_k|d_k|V(S_k)\le (\max_k V(S_k))V_X(y)\). Equality is achieved by making exactly one \(d_k\) nonzero. Thus \(K(X)=\max_k V(S_k)\), without requiring any finite-sample conjecture.

**Step 2: Exact cubic critical-point variation.** For a real cubic \(p(t)=At^3+Bt^2+Ct+D\), \(A\ne0\), whose derivative has roots \(r_-<r_+\), direct integration of \(p'(t)=3A(t-r_-)(t-r_+)\) gives the absolute difference between its two critical values as \(|A|(r_+-r_-)^3/2\). By Rolle's theorem, each endpoint-step interpolant has its two derivative roots in the two open gaps where its sampled values repeat, while the middle-step derivative roots lie respectively in \((-1,x_1)\) and \((x_2,1)\). There are exactly two quadratic derivative roots. Therefore the two endpoint-step variations equal \(1+|A|(r_+-r_-)^3\), whereas the middle-step variation equals \(|A|(r_+-r_-)^3-1\). This uses the actual endpoint values and the alternating derivative signs, so it includes the full interval rather than only one interpolation cell.

The endpoint steps are \(S_1=1-\ell_0\) and \(S_3=\ell_3\), with
\[
\ell_0(t)=\frac{(t-x_1)(t-x_2)(t-1)}{(-1-x_1)(-1-x_2)(-2)},\qquad
\ell_3(t)=\frac{(t+1)(t-x_1)(t-x_2)}{2(1-x_1)(1-x_2)}.
\]
The above discriminant identity yields exactly \(V(S_1)=B_L\) and \(V(S_3)=B_R\). For \(S_2=\ell_2+\ell_3\), its cubic leading coefficient has absolute value \((1+a)/(2a((1+a)^2-m^2))\), and its derivative-root separation satisfies
\[
(r_+-r_-)^2=\frac{4(1+a+a^2)[3(1+a)^2+m^2]}{9(1+a)^2}.
\]
Substitution gives \(V(S_2)=B_C\). The formulas hold for every \(a>0\), \(|m|+a<1\), and their denominators are strictly positive there.

**Step 3: Symmetry is globally optimal, not assumed.** Fix \(a\) and vary the center \(m\) over its admissible interval. The middle branch satisfies the exact factorization
\[
\frac{B_C(m,a)+1}{B_C(0,a)+1}
=\frac{\bigl(1+m^2/[3(1+a)^2]\bigr)^{3/2}}{1-m^2/(1+a)^2}\ge1,
\]
with equality only at \(m=0\). Moreover, when \(m\ge0\), \(B_R(m,a)\ge B_R(0,a)\) since its numerator increases and its positive denominator decreases; when \(m\le0\), similarly \(B_L(m,a)\ge B_L(0,a)\). Hence
\[
K(m,a)\ge K(0,a)=\max\{E(a),F(a)\},
\]
and the inequality is strict for every nonzero admissible \(m\). Thus no asymmetric grid can minimize the gain, irrespective of what the symmetric optimum is.

**Step 4: Unique spacing and equality.** Differentiating yields
\[
E'(a)=\frac{4a(11-3a^2)\sqrt{1+3a^2}}{27(1-a^2)^2}>0,
\]
\[
F'(a)=\frac{2\sqrt3\,(a-1)(a+2)(2a+1)\sqrt{1+a+a^2}}{9a^2(1+a)^2}<0
\]
for \(0<a<1\). Furthermore \(F(a)\to\infty\) as \(a\downarrow0\) and \(E(a)\to\infty\) as \(a\uparrow1\), while their opposite endpoint limits are finite. Their graphs cross exactly once. Before the crossing, \(\max\{E,F\}=F\) strictly decreases; after it, \(\max\{E,F\}=E\) strictly increases. This proves existence and uniqueness of the stated global minimizer. At the crossing \(B_L=B_C=B_R\), providing three independent exact norming jump witnesses.

## Verification
The standalone `verify.py` reconstructs the Lagrange basis symbolically, checks each derivative discriminant and the squared radical identities, checks strict derivative formulas and the symmetrization factor, and certifies the displayed root enclosure using **integer-square-root rational interval arithmetic** (not just floating-point root finding). A separate calculation evaluates the actual variation at derivative critical points for hundreds of asymmetric grids and arbitrary input vectors, comparing to the symbolic formulas. Running `python verify.py` with Python 3.10+, SymPy and NumPy reproduces the stated outputs. The analytical proof above—not the numerical tests—establishes the all-grid and all-vector claims.

## Relationship to prior work
Berrut–Trefethen (2004) give general Lagrange/barycentric formulas and discuss interpolation stability in the uniform norm, but not the induced adjacent-variation-to-continuous-variation norm or its node design. Rack–Vajda (2015) classify **Lebesgue-constant** optimal cubic grids; their unique endpoint-fixed optimal interior parameter is about \(0.4177913013\), rather than the present variation-optimal \(0.4801369263\). This is a different norm, and their extremal family is not a theorem about variation amplification.

A published *Optimal symmetric four-node cubic interpolation for monotone range control* finds the parameter \(0.4458209225\) minimizing **range excursion of monotone data**, using the same cubic interpolants and some of the same step data. Its range-bound formulas do not supply the total derivative variation: the endpoint-step variation also counts a distinct interior hump. The present result gives an exact variation formula for **arbitrary, including asymmetric, endpoint-fixed grids** and proves their unique minimax design, neither of which follows as a specialization of a range-excursion bound. Nochetto–Salgado (2012) design a different piecewise-multilinear **averaged** finite-element interpolation operator satisfying a variation-diminishing inequality; it is not the unmodified global cubic interpolant. Mastroianni–Russo (2011) discuss convergence and error estimates for Jacobi-node interpolation of functions of bounded variation rather than the present finite-data exact norm and node minimization. These comparisons distinguish the quantified operator norm from the mere occurrence of bounded variation in interpolation literature.

## Limitations
Only four real nodes and cubic Lagrange interpolation with the two fixed at interval endpoints are covered. Nothing is asserted about configurations in which even the endpoint nodes can move, higher polynomial degrees, Hermite or spline interpolation, weighted input variation, interpolation approximation error, uniform-norm Lebesgue optimality, or automatic preservation of monotonicity. This is a mathematical self-review and not independent external validation. Priority risk remains from unindexed older work on variation-norm optimal sampling, notwithstanding the specific published-source comparisons.

## References
1. J.-P. Berrut and L. N. Trefethen, *Barycentric Lagrange Interpolation*, SIAM Review 46 (2004), 501–517, DOI: 10.1137/S0036144502417715. Author full text: https://people.maths.ox.ac.uk/trefethen/barycentric.pdf (first electronically published 2004-07-30, as stated on page 501).
2. H.-J. Rack and R. Vajda, *Optimal cubic Lagrange interpolation: Extremal node systems with minimal Lebesgue constant*, Studia Universitatis Babeș–Bolyai Mathematica 60 (2015), 151–171. Full text: https://studia.reviste.ubbcluj.ro/index.php/subbmathematica/article/download/5710/5405/10662.
3. R. H. Nochetto and A. J. Salgado, *A Total Variation Diminishing Interpolation Operator and Applications*, first arXiv posting 2012-11-05, https://arxiv.org/abs/1211.1069.
4. G. Mastroianni and M. G. Russo, *The Lagrange interpolation for bounded variation functions*, SC2011 conference slides, October 2011, https://bugs.unica.it/sc2011/slides/slides/russo.pdf.
5. *Optimal symmetric four-node cubic interpolation for monotone range control*, published 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-optimal-symmetric-four-node-cubic-interpolation-for-monotone-ran--7f9a4d5c7ee7/.
