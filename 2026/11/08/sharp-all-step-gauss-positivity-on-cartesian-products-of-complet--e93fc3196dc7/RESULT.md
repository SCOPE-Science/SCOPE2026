# Sharp all-step Gauss positivity on Cartesian products of complete graphs

## Finding

Let \(d\ge1\) and let \(q_1,\ldots,q_d\ge2\) be arbitrary integers. Form the unweighted Cartesian product
\[
G=K_{q_1}\square\cdots\square K_{q_d},\qquad L=L_G.
\]
For the two-stage, order-four Gauss--Legendre Runge--Kutta end-step map for graph heat flow, put
\[
T(h)=F(hL),\qquad F(z)=\frac{z^2-6z+12}{z^2+6z+12},\qquad h\ge0.
\]
Then the exact unconditional entrywise positivity classification is
\[
\boxed{T(h)\ge0\ \text{entrywise for every }h\ge0\iff
 d=1\quad\text{or}\quad \bigl(d=2\text{ and }q_1,q_2\in\{2,3\}\bigr).}
\]
In all these cases \(T(h)\) is strictly positive entrywise for every \(h>0\). In every excluded case, a neighboring pair of vertices has a **negative** transition entry for every sufficiently large \(h\), despite conservation of row sums and the strictly positive scalar stability function.

A useful structural subresult, proved below, is the exact nearest-neighbor Green-function formula. If \(Q=q_k\), \(N=\prod_iq_i\), and \(x,y\) differ only in coordinate \(k\), then
\[
N L^+_{xy}=-\frac1Q+
Q\sum_{\varnothing\ne S\subseteq\{1,\ldots,d\}\setminus\{k\}}
\frac{\prod_{i\in S}(q_i-1)}{(\sum_{i\in S}q_i)(Q+\sum_{i\in S}q_i)}.
\]
Here \(L^+\) denotes the Moore--Penrose inverse, and an empty sum is zero. This positive Green entry is the obstruction in all excluded cases.

## Assumptions and scope

Each \(K_{q_i}\) is the simple, unweighted complete graph with combinatorial Laplacian \(q_iI-J\). The Cartesian graph has \(N\) vertices; its Laplacian is the Kronecker sum of the factor Laplacians, with positive spectrum indexed by nonempty coordinate subsets. The exact rational end-step map is considered in infinite-precision arithmetic, not internal Runge--Kutta stage positivity or floating-point time stepping. No restrictions are placed on the integers beyond \(q_i\ge2\), nor on the real timestep beyond \(h\ge0\). Entrywise nonnegativity means every matrix element is nonnegative. At \(h=0\), \(T(0)=I\).

## Proof

**1. Spectral decomposition and conservation.** Set \(E_i=J_{q_i}/q_i\), \(H_i=I-E_i\). Both are orthogonal projectors. For \(S\subseteq\{1,\ldots,d\}\), the tensor projector with \(H_i\) at positions in \(S\), and \(E_i\) elsewhere, has Laplacian eigenvalue \(s_S=\sum_{i\in S}q_i\). Thus \(F(hL)\) exists for every \(h\ge0\), since its scalar denominator is positive on \([0,\infty)\). Its row sums equal \(F(0)=1\). For vertices \(x,y\), let \(D(x,y)\) be the set of differing coordinates. The explicit matrix element is
\[
T(h)_{xy}=\frac1N\sum_{S\subseteq[d]}F(hs_S)
\prod_{i\in S}\begin{cases}q_i-1,&i\notin D(x,y),\\-1,&i\in D(x,y).\end{cases}
\]
The product over an empty set equals one. Furthermore \(F(z)=((z-3)^2+3)/(z^2+6z+12)\) lies strictly between zero and one for \(z>0\), and equals one at zero. The positive coefficients of the diagonal projectors imply \(T(h)_{xx}>0\) for every \(h\ge0\).

**2. Exact large-timestep obstruction.** For \(z>0\), \(F(z)=1-12z/(z^2+6z+12)\). By the spectral theorem, for all distinct \(x,y\),
\[
\lim_{h\to\infty}hT(h)_{xy}=-12L^+_{xy}.
\]
Indeed each positive eigenvalue contributes \(-12/(h\lambda)+O(h^{-2})\), while the zero-eigenvalue projector contributes no off-diagonal term after summing the limiting identity matrix.

The heat semigroup representation \(L^+=\int_0^\infty(e^{-tL}-J/N)\,dt\), valid for each finite connected graph here, gives an exact formula. If \(x,y\) differ only at coordinate \(k\), writing \(Q=q_k\), the Cartesian heat kernel is
\[
(e^{-tL})_{xy}=\frac{1-e^{-Qt}}{Q}\prod_{i\ne k}
\frac{1+(q_i-1)e^{-q_it}}{q_i}.
\]
After expanding the product, integrating each exponential and subtracting the equilibrium term, one obtains
\[
N L^+_{xy}=-\frac1Q+
Q\sum_{\varnothing\ne S\subseteq[d]\setminus\{k\}}
\frac{\prod_{i\in S}(q_i-1)}{s_S(Q+s_S)}.
\]
Every summand is positive.

**3. Excluded products with at least three factors.** Choose \(k\) so that \(Q=q_k=\max_iq_i\), and take two other factors with orders \(a,b\) (both at most \(Q\)). Keeping their two singleton terms yields
\[
NL^+_{xy}\ge -\frac1Q+
\frac{Q(a-1)}{a(Q+a)}+
\frac{Q(b-1)}{b(Q+b)}+
\frac{Q(a-1)(b-1)}{(a+b)(Q+a+b)}.
\]
Because \(Q\ge a,b\ge2\), each singleton term is at least \(1/4\). Since \(Q\ge2\), the first three terms total at least zero, while the displayed last term is strictly positive. Consequently \(L^+_{xy}>0\). By Step 2 the nearest-neighbor element \(T(h)_{xy}\) is negative for every sufficiently large \(h\), for **every** set of factor orders whenever \(d\ge3\).

**4. Excluded two-factor products.** Suppose \(d=2\), and write \(Q=\max(q_1,q_2)\), \(a=\min(q_1,q_2)\). For neighbors differing in the \(Q\)-coordinate, Step 2 reduces to
\[
NL^+_{xy}=-\frac1Q+\frac{Q(a-1)}{a(a+Q)}.
\]
This is positive precisely when \((a-1)Q^2>a(Q+a)\). If \(Q\ge4\), that inequality holds: for \(a=2\) its left-minus-right expression at \(Q=4\) is \(4>0\), for \(a=3\) it is \(11>0\), and for \(a\ge4\) the expression at \(Q=a\) is \(a^2(a-3)>0\). In each case it is strictly increasing in \(Q\ge\max(a,4)\), as its derivative is \(2(a-1)Q-a>0\). Thus every two-factor product with one factor of order at least four fails unconditional positivity.

**5. All surviving cases.** For \(d=1\), the projectors give
\[
T(h)=E_1+F(hq_1)H_1,
\]
whose off-diagonal entries are \((1-F(hq_1))/q_1>0\) for \(h>0\), and diagonal entries are positive.

For \(d=2\) write \(p=q_1,q=q_2\) and \(D_r(h)=r^2h^2+6rh+12\). The only remaining pairs, up to swapping coordinates, are \((p,q)=(2,2),(2,3),(3,3)\). The three distinct off-diagonal orbit values (different in the first coordinate only, the second coordinate only, or both) are respectively
\[
\frac{1-F(ph)+(q-1)[F(qh)-F((p+q)h)]}{pq},
\]
\[
\frac{1-F(qh)+(p-1)[F(ph)-F((p+q)h)]}{pq},
\]
\[
\frac{1-F(ph)-F(qh)+F((p+q)h)}{pq}.
\]
Their common positive denominator is \(pqD_p(h)D_q(h)D_{p+q}(h)\). After clearing this denominator, the coefficient arrays (constant term first) of their three numerators are:

| \((p,q)\) | First-coordinate neighbors | Second-coordinate neighbors | Distance-two neighbors |
|---|---|---|---|
| \((2,2)\) | \((0,6912,13824,11520,4608,768)\) | same | \((0,0,6912,13824,9216,2304)\) |
| \((2,3)\) | \((0,10368,20736,16416,8640,2520)\) | \((0,10368,25920,25056,8640,360)\) | \((0,0,10368,25920,21600,6840)\) |
| \((3,3)\) | \((0,15552,38880,34992,11664)\) | same | \((0,0,15552,46656,46656,17496)\) |

Each entry is strictly positive for \(h>0\), because the numerator is a polynomial with nonnegative coefficients and at least one positive nonconstant coefficient; the denominator is positive. The diagonal entries are positive by Step 1. This proves the stated if-and-only-if classification and strict positivity in exactly the permitted cases. \(\square\)

## Verification

The standalone standard-library script `artifacts/verify.py` reconstructs the polynomial numerators from products of the exact Padé numerator and denominator, checks their coefficient signs, evaluates the tensor-projector kernel with exact rational numbers, verifies row sums, independently compares the Green function with the integrated heat-kernel formula, and tests large-step sign witnesses. The script completed with

`VERIFY_OK polynomial_certificates 9 rational_kernels 320 row_sums 55 green_identities 246 positive_green 243 large_step_witnesses 12`.

These finite exact checks supplement, but do not replace, the symbolic all-parameter proof above. The proof establishes eventual negativity without providing a uniform finite timestep applicable to all excluded graph orders.

## Relationship to prior work

Zappavigna, Colaneri, Kirkland and Shorten studied Padé discretizations of positive linear systems and demonstrated general positivity failures, including a nilpotent eight-state construction. Their general sufficient finite-step conditions do not provide this all-timestep classification of **undirected Cartesian clique products**. Lóczi and Ketcheson analyzed absolute monotonicity of rational stability functions, which is a method-wide concept and does not by itself classify special network families on which positivity holds at all steps. Fontan and Altafini studied sign patterns and eventual exponential positivity of Laplacian pseudoinverses, without the Gauss--Legendre end-step threshold in this theorem.

Related published studies include an eight-state pure-birth-chain Padé positivity obstruction (a non-symmetric generator and a small-step question) and special-graph Gaussian end-step statements on cycles or complete multipartite graphs. The four-cycle overlap \(K_2\square K_2\) is previously covered. The present finding classifies **all finite Cartesian products of complete graphs with independently varying factor orders** and uses an exact Green-function nearest-neighbor test for all excluded products; the mixed \(K_2\square K_3\) and square rook \(K_3\square K_3\) positive cases are not inferred from the known cycle or complete-multipartite results. No claim of universal publication priority is made.

## Limitations

The claim is about a fixed exact fourth-order rational end-step map on finite unweighted Cartesian products of cliques. It does not assert that arbitrary graph Laplacians obey this threshold, that internal stages remain nonnegative, or that general nonlinear discretizations preserve positivity. The negative-step conclusion concerns sufficiently large finite \(h\) depending on the graph, not all timesteps. The literature search is bounded; independently discovering or indexing an equivalent specialist result remains possible. Independent mathematical validation has not been performed.

## References

1. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, *Essentially Negative News About Positive Systems*, preprint, university repository deposited 19 June 2012; https://mural.maynoothuniversity.ie/id/eprint/3761/ ; published in *Linear Algebra Appl.* 436 (2012), 3425–3442, https://doi.org/10.1016/j.laa.2011.12.021 .
2. L. Lóczi and D. I. Ketcheson, *Rational Functions with Maximal Radius of Absolute Monotonicity*, initial preprint 26 March 2013, https://arxiv.org/abs/1303.6651 .
3. A. Fontan and C. Altafini, *On the Properties of Laplacian Pseudoinverses*, preprint 29 September 2021, https://arxiv.org/abs/2109.14587 .
4. *Eight-state barrier for Markov positivity of the [2/2] Padé map*, published research record, https://github.com/published-finding corpus/2026/blob/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab/RESULT.md .
