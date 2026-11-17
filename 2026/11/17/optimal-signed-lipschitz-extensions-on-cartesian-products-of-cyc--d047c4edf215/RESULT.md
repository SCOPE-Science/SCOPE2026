# Optimal signed Lipschitz extensions on Cartesian products of cycles

## Finding

Consider a Cartesian product of finite cycles with their unweighted graph metrics. A point attached at an equal distance from every vertex admits a norm-minimizing real-linear Lipschitz extension operator. The exact operator norm is classical in its symmetry-based form; the contribution here is a classification of **all signed optimizing operators** and of the complete optimizer geometry, including its sharp transition to signed weights.

For integers \(k\ge2\) and \(n_i\ge3\), write
\[
X=\prod_{i=1}^k \mathbb Z/n_i\mathbb Z,\qquad
 d(x,y)=\sum_{i=1}^k\min\{|x_i-y_i|,n_i-|x_i-y_i|\}.
\]
Set
\[
D=\sum_i\lfloor n_i/2\rfloor,\quad
N=\prod_i n_i,\quad
c_i=\frac{\lfloor n_i^2/4\rfloor}{n_i},\quad c=\sum_i c_i.
\]
Adjoin a point \(o\) satisfying \(d(o,x)=R\) for every \(x\in X\), with \(R\ge D/2\) (the exact triangle-inequality condition). Every bounded real-linear extension of all real-valued Lipschitz functions has the form
\[
(E_w f)(o)=\sum_{y\in X}w_yf(y),\qquad
\sum_{y\in X}w_y=1,
\]
and equals \(f\) on \(X\). The coefficients may initially be arbitrary real numbers.

**Theorem.** The smallest extension norm is exactly
\[
\inf_w\|E_w\|=\max\left\{1,\frac cR\right\}.
\]
For each \(R\) with \(D/2\le R\le c\), the *complete* set of optimal coefficients consists of precisely those probability weights \(w\ge0\) whose \(i\)-th coordinate marginal \(\pi_iw\) has the following property:

- if \(n_i\) is odd, \((\pi_iw)(a)=1/n_i\) for every residue \(a\);
- if \(n_i=2m_i\) is even, \((\pi_iw)(a)=(\pi_iw)(a+m_i)\) for every residue \(a\).

No independence of the coordinates is imposed: **arbitrary correlated couplings of these marginals are allowed**. Let \(\mathcal P\) denote this optimizer polytope. Then
\[
\dim\operatorname{aff}(\mathcal P)=
N-1-\sum_{i:n_i\ \mathrm{odd}}(n_i-1)
-\sum_{i:n_i\ \mathrm{even}}\frac{n_i}{2}.
\]
At \(R>c\) the minimizing operator set instead has full affine dimension \(N-1\) and includes negative-coefficient vectors for every arbitrarily small excess \(R-c>0\). At this threshold the minimum norm becomes one. For all-even products, \(c=D/2\); for any product containing an odd factor, \(c>D/2\), creating an admissible interval of extension norms strictly larger than one.

As an example, \(C_5\square C_6\) has \(N=30\), \(D=5\), \(c=27/10\), and a \(22\)-dimensional polytope of optimal coefficients throughout \(5/2\le R\le27/10\). The minimum extension norm at \(R=5/2\) is \(27/25\). Above \(R=27/10\), the optimal set has dimension \(29\) and already contains signed measures.

## Assumptions and scope

The Lipschitz seminorm is \(\operatorname{Lip}(f)=\max_{x\ne y}|f(x)-f(y)|/d(x,y)\). An extension operator means a real-linear map on all real-valued functions on \(X\) that preserves their values on \(X\) and is bounded in this seminorm. Boundedness on constants forces \(E(1)=1\), hence the coefficient sum condition. The statement concerns scalar-valued real Lipschitz functions, not nonlinear extensions, vector-valued simultaneous extensions, or arbitrary vertex-transitive metrics.

## Proof

**1. Reduction to free-space distances.** For an arbitrary signed coefficient vector summing to one, define
\[
\rho(w)=\max_{x\in X}
\left\|\delta_x-\sum_{y\in X}w_y\delta_y\right\|_{\mathcal F(X)}
=\max_x\sup_{\operatorname{Lip}(f)\le1}
\left(f(x)-\sum_yw_yf(y)\right).
\]
The unit ball of scalar Lipschitz functions is symmetric, so the supremum also controls the absolute value. Since only the \(o\)-to-\(X\) pairs are new,
\[
\|E_w\|=\max\{1,\rho(w)/R\}.
\]
Define \(S_x(w)=\sum_yw_yd(x,y)\). Testing with the potential \(f_x(y)=-d(x,y)\) gives \(\rho(w)\ge S_x(w)\) for every \(x\). Transitivity of the product cycles implies
\[
\frac1N\sum_x S_x(w)=\sum_i c_i=c,
\]
because the average distance from a fixed vertex on \(C_{n_i}\) is \(\lfloor n_i^2/4\rfloor/n_i\). Consequently \(\rho(w)\ge c\) for every signed coefficient vector.

The uniform probability vector \(u_y=1/N\) has \(S_x(u)=c\) for every \(x\). Since \(\delta_x-u=\sum_yu_y(\delta_x-\delta_y)\), the triangle inequality and the test function \(f_x\) yield exactly \(\rho(u)=c\). This proves the minimum norm formula.

**2. Strict positivity screening.** Suppose \(\rho(w)=c\). Since every \(S_x(w)\le c\) and their average is \(c\), one has \(S_x(w)=c\) for all \(x\). If \(w_z<0\), select \(x\) with \(d(x,z)=D\), possible in a product of cycles. The function \(f_x=-d(x,\cdot)\) has a minimum at \(z\). Increasing *only* its value at \(z\) by any \(\varepsilon\in(0,1)\) preserves the edgewise \(1\)-Lipschitz constraints: every neighbor of \(z\) has distance from \(x\) either \(D\) or \(D-1\), so the modified edge differences are \(\varepsilon\) or \(1-\varepsilon\). Edgewise feasibility implies global Lipschitz feasibility in the graph metric. Evaluating the perturbed potential gives
\[
\rho(w)\ge S_x(w)-\varepsilon w_z>c,
\]
a contradiction. Thus **every** minimizer of \(\rho\) is a nonnegative probability vector, even though signed coefficients were allowed.

Conversely, for every nonnegative \(w\) of total mass one, the triangle inequality \(\rho(w)\le\max_x S_x(w)\) is sharp by the same distance functions: \(\rho(w)=\max_x S_x(w)\). Hence \(\rho(w)=c\) exactly when the distance-profile vector \(S_x(w)\) is constant in \(x\).

**3. Marginal classification.** Write \(v_i=\pi_iw\) and
\[
g_i(a)=\sum_{b\in\mathbb Z/n_i\mathbb Z}v_i(b)\,d_{C_{n_i}}(a,b).
\]
Then \(S_x(w)=\sum_i g_i(x_i)\). Varying one independent coordinate at a time proves that \(S_x(w)\) is constant exactly when each \(g_i\) is constant. The average value of \(g_i\) is necessarily \(c_i\).

Take cyclic second differences \((\Delta^2g)_a=g(a-1)-2g(a)+g(a+1)\). If \(n=2m\), the cycle-distance kernel has second differences \(2\delta_0-2\delta_m\), giving
\[
(\Delta^2g)_a=2v(a)-2v(a+m).
\]
Thus constant \(g\) forces antipodal equality. Conversely, if \(v(a)=v(a+m)\), pairing opposite vertices and using \(d(a,b)+d(a,b+m)=m\) proves \(g\equiv m/2\).

If \(n=2m+1\), second differences of the distance kernel are \(2\delta_0-\delta_m-\delta_{m+1}\), so constant \(g\) gives
\[
2v(a)=v(a-m)+v(a+m).
\]
At a maximum of \(v\), both neighbors by steps \(\pm m\) must have the same value. Since \(\gcd(m,2m+1)=1\), those steps connect every residue and \(v\) must be uniform. Uniformity conversely makes \(g\) constant by translation symmetry. This completes the exact characterization of \(\rho(w)=c\) and the optimizer classification whenever \(R\le c\).

**4. Dimension and sharp signed transition.** Each odd-factor uniform marginal supplies \(n_i-1\) independent affine constraints. Each even-factor antipodal marginal supplies \(n_i/2\) independent affine constraints. These groups are mutually independent modulo total mass: any linear relation between functions depending on distinct individual coordinates forces each such function to be constant; a zero-mean, antipodally antisymmetric constraint function cannot be nonzero constant. The everywhere-positive uniform vector lies in the feasible set, so the nonnegativity constraints do not decrease its affine dimension. This gives the displayed dimension formula.

If \(R>c\), the norm-one optimizer set is exactly \(\{w:\sum_yw_y=1,\rho(w)\le R\}\). Continuity of \(\rho\), together with \(\rho(u)=c<R\), shows that this polytope has full affine dimension \(N-1\). To see that it contains signed weights at every excess, begin with \(u\), and on any \(2\times2\) rectangle of distinct values in the first two coordinates (other coordinates fixed), add \(1/N\) at the two diagonal cells and subtract \(1/N\) at the other two. This produces a nonnegative vector \(w^0\) preserving all coordinate marginals, with some zero entry and some positive entry. Let \(a\) index a positive entry and \(b\) a zero entry. For \(\varepsilon>0\), put \(w^\varepsilon=w^0+\varepsilon(\delta_a-\delta_b)\). It has a negative entry at \(b\), and
\[
\rho(w^\varepsilon)\le\rho(w^0)+\varepsilon d(a,b)
=c+\varepsilon d(a,b).
\]
Choosing \(\varepsilon<(R-c)/d(a,b)\) produces a signed norm-one extension. This proves the full-dimensional and signed-transition claims.

## Verification

The included standalone file `check_torus.py` performs separate finite linear-programming checks of the Kantorovich–Rubinstein dual norm on eight products with even, odd, and mixed factors. It checks exact rational average-distance identities and the predicted affine constraint ranks, and numerically optimizes Lipschitz potentials subject to every graph-edge inequality using HiGHS. The tested products are \(C_3\square C_4\), \(C_4\square C_4\), \(C_4\square C_5\), \(C_4\square C_6\), \(C_5\square C_5\), \(C_5\square C_6\), and \(C_3\square C_4\square C_4\). The calculations are finite corroboration, not the proof of the statement for all \(n_i\).

## Relationship to prior work

Ambrosio–Puglisi (2016) establish the connection between bounded linear Lipschitz extensions and random projections in the Lipschitz-free/Kantorovich–Rubinstein setting. Bruè–Di Marino–Stra (2018) give general linear Lipschitz extension constructions using random projections. Their results supply the functional-analytic framework but do not specify the entire signed equality set for equidistant attachments to products of cycles. The known one-factor cycle equality problem concerns only one marginal and does not resolve multivariate correlations, full signed-optimizer rigidity, or the exponentially large optimizer-polytope dimension for \(k\ge2\). The exact minimum norm here also follows from vertex-transitive averaging and is not asserted to be new in isolation.

## Limitations

The classification relies on shortest-path **unit-edge** cycle factors and real scalar coefficients. It does not claim the same marginal conditions for weighted cycles or arbitrary vertex-transitive graphs, nor any classification of the individual vertices of the multi-marginal optimizer polytope. No independent external mathematical audit has been performed. Historical priority under alternative Wasserstein-center or random-projection terminology remains uncertain.

## References

1. E. Bruè, S. Di Marino, F. Stra, *Linear Lipschitz and \(C^1\) extension operators through random projection*, arXiv:1801.07533 (first public preprint 2018-01-23), sections 3–4, especially Theorem 4.1. https://arxiv.org/abs/1801.07533
2. L. Ambrosio and D. Puglisi, *Linear extension operators between spaces of Lipschitz maps and optimal transport*, arXiv:1609.01450 (2016-09-06), especially Theorems 2.14 and 2.15. https://arxiv.org/abs/1609.01450
