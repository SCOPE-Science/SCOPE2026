# Sharp rate-imbalance threshold and reentrant internal-stage positivity in two-state Gauss collocation

## Finding
For any two-state continuous-time Markov generator with strictly positive transition rates, the fourth-order two-stage Gauss–Legendre Runge–Kutta method has an entrywise strictly positive endpoint map for every positive step size, but its internal stages can fail positivity. The first stage always maps probability vectors into strictly positive probability vectors. The second stage is nonnegative for all initial probability vectors and every positive step size precisely when the larger transition rate divided by the smaller does not exceed
\[
r_*=\frac{4+2\sqrt3+\sqrt{(4+2\sqrt3)^2+4}}{2}=7.59575411272515\ldots.
\]
At equality there is one zero diagonal entry at one positive scaled step size. For larger rate ratios the second stage has one **bounded open interval of scaled step sizes** on which it is not positivity preserving, with positivity restored for all sufficiently large steps. Thus the negative-stage phenomenon cannot be detected by checking the end-step transition alone.

## Assumptions and scope
Fix real rates \(a,b>0\) and the row-vector forward equation \(p'(t)=p(t)Q\), where
\[
Q=\begin{pmatrix}-a&a\\ b&-b\end{pmatrix},\qquad
\lambda=a+b,\qquad r=\max(a,b)/\min(a,b)\ge1.
\]
Here \(p(0)\) ranges over **every** row probability vector in \(\mathbb R^2\) (including the two pure states). Let \(h>0\), \(z=h\lambda\). The two-stage Gauss–Legendre method has coefficient matrix and output weights
\[
A=\begin{pmatrix}\tfrac14&\tfrac14-\tfrac{\sqrt3}{6}\\
\tfrac14+\tfrac{\sqrt3}{6}&\tfrac14\end{pmatrix},\qquad
w=\begin{pmatrix}\tfrac12\\ \tfrac12\end{pmatrix}.
\]
Its internal row-stage values \(Y_i\) and endpoint \(p_+\) solve
\[
Y_i=p+h\sum_{j=1}^2 A_{ij}Y_jQ,\qquad
p_+=p+\frac h2(Y_1+Y_2)Q.
\]
Stage positivity means both stages are nonnegative for **every** initial probability vector, not merely for one initial state; strict positivity means all components strictly positive for all such inputs. This is a statement only for the specified linear two-state generator and classical collocation stages, not for arbitrary nonlinear dynamics or general finite Markov generators.

## Proof
Define the rank-one stationary projection and its complement:
\[
\Pi=\frac1{a+b}\begin{pmatrix}b&a\\b&a\end{pmatrix},\qquad P=I-\Pi.
\]
Then \(\Pi^2=\Pi\), \(P^2=P\), \(\Pi P=P\Pi=0\), and \(Q=-\lambda P\). The constant mode is unchanged at each stage. On the complementary mode, the two internal stage coefficients are the components of \((I+zA)^{-1}(1,1)^\top\). Direct inversion gives, with \(D(z)=1+z/2+z^2/12>0\),
\[
g_1(z)=\frac{1+\frac{\sqrt3}{6}z}{D(z)},\qquad
g_2(z)=\frac{1-\frac{\sqrt3}{6}z}{D(z)}.
\]
Consequently the exact row-stage transition matrices and endpoint matrix are
\[
S_i(z)=\Pi+g_i(z)P,\qquad
E(z)=\Pi+R(-z)P,\qquad
R(-z)=\frac{1-z/2+z^2/12}{D(z)}.
\]
Each has row sums one. For any real \(g\), the matrix \(\Pi+gP\) is entrywise nonnegative exactly when
\[
-\frac1r\le g\le1.
\]
Indeed the two off-diagonal entries are \(a(1-g)/(a+b)\) and \(b(1-g)/(a+b)\), and nonnegativity of both diagonal entries is equivalent to \(g\ge-\min(a/b,b/a)=-1/r\). Strict inequalities give strict positivity.

For all \(z>0\), \(0<g_1(z)<1\): the numerator is positive, while \(D(z)-1-\sqrt3 z/6=z(1/2-\sqrt3/6)+z^2/12>0\). Also \(g_2(z)<1\). Thus the second stage is nonnegative exactly when \(g_2(z)\ge-1/r\), which after multiplication by \(12D(z)>0\) becomes
\[
F_r(z):=z^2+(6-2\sqrt3 r)z+12(1+r)\ge0.
\]
Its discriminant is
\[
\Delta(r)=12\bigl[r^2-(4+2\sqrt3)r-1\bigr].
\]
The unique positive zero of the square bracket is \(r_*\) as displayed in the finding. Since \(r\ge1\), the quadratic is strictly positive on all \(z>0\) when \(r<r_*\). At \(r=r_*\) it has a unique double zero \(z_*=\sqrt3r_*-3>0\), so nonnegativity holds, with a zero diagonal component for a pure initial state.

For \(r>r_*\), the quadratic has two distinct strictly positive roots
\[
z_\pm(r)=\sqrt3r-3\pm\sqrt{3\bigl[r^2-(4+2\sqrt3)r-1\bigr]}.
\]
Positivity fails precisely when \(z_-<z<z_+\), is nonnegative at the two endpoints, and is strict on \(0<z<z_-\) and \(z>z_+\). The roots are positive because their sum is \(2\sqrt3r-6>0\), their product is \(12(1+r)>0\), and the discriminant is positive. In particular the second stage recovers strict positivity as \(h\to\infty\), even though it is unsafe on an intermediate interval.

Finally
\[
0<R(-z)<1\qquad(z>0),
\]
since its numerator is \(((z-3)^2+3)/12>0\), while the denominator exceeds that numerator by \(z>0\). The same entrywise criterion therefore makes \(E(z)\) strictly positive for every positive step size, regardless of the rate ratio. This proves all quantifiers and boundary statements.

As an exact witness, choose \(a=9\), \(b=1\), \(h=1\), so \(z=10\), \(r=9>r_*\). Then the first diagonal entry of the second-stage map is
\[
(S_2)_{11}=\frac{14-9\sqrt3}{86}<0,
\]
while the first row of the end-step transition matrix is \((16/43,27/43)\), with both entries positive. The same second stage is negative in its first component for the strictly interior initial distribution \((99/100,1/100)\).

## Verification
The standalone program `verify_gauss_stages.py` checks the projection identity, exact stage equations, output transition, discriminant, tangency, and witness symbolically using SymPy. It also compares the formulas against independent coupled block-stage solves for fifty rational parameter triples and their exact sign classification. The exact analytic inequalities above, rather than finite experiments, establish the universal result. Run using `python verify_gauss_stages.py` (requires SymPy). The file `verification_output.txt` records the actual successful execution.

## Relationship to prior work
Nüßlein, Ranocha, and Ketcheson (2020), *Positivity-Preserving Adaptive Runge–Kutta Methods*, explain that stage values need not remain positive even when endpoint positivity can be enforced by adapting the weights; see in particular their stage equations and section 5.1. That observation motivates examining a fixed high-order method without modifying its stages. Blanes, Iserles, and Macnamara (2021/2022), *Positivity-preserving methods for ordinary differential equations*, develop positive graph-Laplacian integrators, including exponential, splitting and modified-Patankar constructions; their discussed internal stages belong to different methods. The familiar fourth-order Gauss–Legendre coefficients, and its rational endpoint stability function, are standard. The additional result here is a complete, two-state, rate-ratio-dependent classification of **both internal Gauss stage maps**, including the isolated tangency and recovered positivity past a finite unsafe interval. No assertion of exhaustive prior-art absence is made.

## Limitations
The rate-contrast boundary depends on allowing arbitrary nonnegative initial probabilities and on the precise two-stage Gauss tableau. It is not a guarantee for higher-dimensional chains, positivity of collocation polynomials between stages, nonlinear right-hand sides, or the feasibility of evaluating a nonlinear vector field at a negative stage. The linear test generator is well-defined at all real stage states, so negative intermediate probabilities do not invalidate the numerical calculation itself. The general phenomenon of negative internal Runge–Kutta stages is known; novelty of the exact restricted classification is subject to further specialist review. No independent audit has been performed.

## References
1. S. Nüßlein, H. Ranocha, D. I. Ketcheson, *Positivity-Preserving Adaptive Runge–Kutta Methods* (first public May 13, 2020), https://arxiv.org/abs/2005.06268 .
2. S. Blanes, A. Iserles, S. Macnamara, *Positivity-preserving methods for ordinary differential equations* (first public February 16, 2021; revised 2022), https://arxiv.org/abs/2102.08242 and https://arxiv.org/html/2102.08242v2 .
3. Standard two-stage fourth-order Gauss–Legendre Butcher coefficients, https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_method .
