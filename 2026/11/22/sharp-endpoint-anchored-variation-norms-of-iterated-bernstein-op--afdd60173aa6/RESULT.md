# Sharp endpoint-anchored variation norms of iterated Bernstein operators

## Finding

Let \(n\ge2\) and \(r\ge1\) be integers. On real functions of Jordan bounded variation on \([0,1]\) satisfying \(f(0)=f(1)=0\), the \(r\)-fold classical Bernstein operator has the **exact attained** total-variation norm
\[
\kappa_{n,r}:=\sup_{\substack{f(0)=f(1)=0\\V(f)>0}}\frac{V(B_n^r f)}{V(f)}
=\Pr_{1/2}\{X_r\in(0,1)\}.
\]
Here \(X\) is the absorbing Wright–Fisher binomial chain with population size \(n\): conditional on \(X_t=x\), \(nX_{t+1}\) has law \(\mathrm{Bin}(n,x)\). Equivalently, the displayed coefficient is the sharp two-input Lipschitz factor on the class of real bounded-variation function pairs with identical endpoint values.

The norm is attained by any minimal-variation interpolation through the nodal profile \((0,c,c,\ldots,c,0)\) with \(c\ne0\). Every nonzero extremizer has this nodal profile, up to a common scale. In particular,
\[
\kappa_{n,1}=1-2^{1-n},\qquad
\kappa_{n,2}=1-\frac{2}{2^n n^n}\sum_{j=0}^{n}\binom nj j^n.
\]
All powers admit a finite exact rational matrix formula. Put \(T_{ij}=\binom nj(i/n)^j(1-i/n)^{n-j}\) for \(1\le i,j\le n-1\), and \(q_j=\binom nj2^{-n}\). Then
\[
\kappa_{n,r}=q^\mathsf{T}T^{r-1}\mathbf 1.
\]
Writing \(\lambda_n=(n-1)/n\), for every \(r\ge1\),
\[
\lambda_n^r\le\kappa_{n,r}\le\frac{n^2}{4(n-1)}\lambda_n^r.
\]
These norms decrease strictly with the number of iterations. For \(n\ge3\) they are also strictly submultiplicative:
\[
\kappa_{n,r+s}<\kappa_{n,r}\kappa_{n,s}\quad(r,s\ge1),
\]
whereas \(\kappa_{2,r}=2^{-r}\) is multiplicative. For each fixed \(n\), the exact large-power asymptotic is
\[
\kappa_{n,r}\sim C_n\lambda_n^r,
\qquad C_n=\frac{1}{4\sum_{j=1}^{n-1}\pi_j\,(j/n)(1-j/n)},
\]
where \(\pi\) is the unique normalized strictly positive left Perron eigenvector of \(T\), satisfying \(\pi^\mathsf{T}T=\lambda_n\pi^\mathsf{T}\) and \(\sum_j\pi_j=1\).

## Assumptions and scope

The classical Bernstein operator is
\[
(B_nf)(x)=\sum_{j=0}^{n}f(j/n)\binom njx^j(1-x)^{n-j},\quad 0\le x\le1.
\]
The notation \(B_n^r\) means composition of this same degree-\(n\) operator \(r\) times. The Jordan variation is
\[
V(f)=\sup_{0=x_0<\cdots<x_k=1}\sum_{i=0}^{k-1}|f(x_{i+1})-f(x_i)|,
\]
with arbitrary finite subdivisions. The restriction to equal endpoint values is essential: unrestricted \(BV\) has sharp coefficient one because Bernstein operators reproduce affine functions. No assumption of continuity is imposed; the operator uses actual values at the sampling nodes. If two inputs have the same (possibly nonzero) endpoints, their difference belongs to the anchored class above.

## Proof

**1. Single-block decomposition.** Write \(a_j=f(j/n)\), \(d_i=a_{i+1}-a_i\), so \(\sum_{i=0}^{n-1}d_i=0\). Match all positive and negative charges in the finite signed vector \((d_i)\). A match between positions \(p<q\) is a positive constant times the indicator of nodal indices \(p+1,\ldots,q\); a match in the opposite order is the negative of such an indicator. Thus the nodal vector is a signed combination \(\sum_{I}c_I\mathbf 1_I\) of indicators of nonempty contiguous sets of interior nodes, with
\[
\sum_I|c_I|=\frac12\sum_{i=0}^{n-1}|d_i|\le\frac12V(f).
\]
Every such indicator is zero at the two endpoints.

**2. Variation shape of each block.** If a nodal sequence rises, then falls, its first differences have at most one change of sign, from positive to negative. The derivative of its Bernstein polynomial is \(n\sum_{i=0}^{n-1}d_i\binom{n-1}{i}x^i(1-x)^{n-1-i}\). After setting \(t=x/(1-x)\), the coefficient signs in this polynomial change at most once. Descartes' sign rule, together with the derivative signs near the endpoints, shows the polynomial is unimodal. Sampling a unimodal function preserves that ordering, so every iterate of a block indicator is nonnegative and unimodal, and vanishes at both endpoints. It follows that
\[
V(B_n^r\mathbf 1_I)=2\max_{0\le x\le1}(B_n^r\mathbf 1_I)(x).
\]

**3. Sharp survival domination.** The binomial chain represents \((B_n^r\mathbf 1_I)(x)\) as \(\Pr_x\{X_r\in I/n\}\), which is no greater than the full interior survival probability
\[
S_r(x)=(B_n^r u)(x),\qquad
u(j/n)=\begin{cases}1,&1\le j\le n-1,\\0,&j=0,n.\end{cases}
\]
The full-interior nodal sequence is symmetric and unimodal. The Bernstein construction preserves symmetry, and its polynomial derivative has strictly positive sign on \((0,1/2)\) and strictly negative sign on \((1/2,1)\). One direct verification pairs opposite binomial basis terms \(i\) and \(n-1-i\) in the derivative; for \(x<1/2\) the lower-index term dominates and the corresponding nodal difference is nonnegative, with one strictly positive pair. Hence \(\max_xS_r(x)=S_r(1/2)\). The decomposition and the triangle inequality now give
\[
V(B_n^rf)\le\sum_I|c_I|V(B_n^r\mathbf 1_I)
\le2S_r(1/2)\sum_I|c_I|\le S_r(1/2)V(f).
\]
Taking \(f\) to interpolate the full-interior nodal plateau with variation \(2|c|\) yields equality, proving the exact norm and the two-input version.

If \(I\) is a proper interior subinterval, every interior state of the chain has strictly positive transition probability to every other interior state at each positive time. Thus \(B_n^r\mathbf1_I(x)<S_r(x)\) for \(0<x<1\); taking maxima on a compact interval gives a strict norm gap. Equality in the decomposition therefore requires only the full-interior indicator, proving the nodal extremizer rigidity, and the original function must have no extra variation between the nodes.

**4. Exact formulas and rates.** Since the two boundary states are absorbing, \(S_r(1/2)\) is the probability of remaining interior after \(r\) steps, yielding the finite transient-matrix formula. One binomial step gives \(1-2^{1-n}\); conditioning on the first binomial step gives the stated formula for two steps. Put \(h(x)=x(1-x)\). Direct binomial moment evaluation yields \(B_nh=\lambda_n h\). At every node, \(4h(j/n)\le u(j/n)\le[n^2/(n-1)]h(j/n)\). Positivity of all powers, evaluated at \(x=1/2\), gives the two exponential bounds. The positive transient matrix \(T\) has Perron eigenvalue \(\lambda_n\), because the positive vector \((h(j/n))_{j=1}^{n-1}\) is its right eigenvector. Perron–Frobenius convergence gives \(T^{r-1}\mathbf1\sim\lambda_n^{r-1}h/(\pi^\mathsf{T}h)\); using \(q^\mathsf{T}h=\lambda_n/4\) proves the constant \(C_n\).

**5. Strict decay and submultiplicativity.** Strict positivity of the chance of absorption at the next step implies \(\kappa_{n,r+1}<\kappa_{n,r}\). The operator-norm inequality gives \(\kappa_{n,r+s}\le\kappa_{n,r}\kappa_{n,s}\). For \(n\ge4\), \(B_n^su\) has unequal interior nodal values (strictly increasing toward \(1/2\)), so it cannot attain the \(r\)-th iterate's norm, by the rigidity in step 3; hence the inequality is strict. For \(n=3\) one calculates \(\kappa_{3,r}=\tfrac34(\tfrac23)^{r-1}\), making strictness immediate. For \(n=2\), \(\kappa_{2,r}=2^{-r}\) gives equality.

## Verification

The accompanying `check.py` independently constructs exact rational binomial transition matrices and verifies the survival formulas, exponential inequalities and strict submultiplicativity for degrees \(2\) through \(8\), through five powers. It also checks 1,662 randomized anchored nodal profiles for the variation inequality, using a polynomial-derivative root calculation. These finite tests are not used to infer the all-degree or all-power claims; those are proven above by finite-charge decomposition, positivity, unimodality and Perron–Frobenius theory.

Execute `python3 check.py` in a Python environment with the standard library and NumPy. The output ends with `ALL_ANCHORED_BERNSTEIN_CHECKS_PASS` when all checks succeed.

## Relationship to prior work

The standard variation-diminishing inequality \(V(B_nf)\le V(f)\), attributed to Lorentz and extended to generalized \(\Lambda\)-variation by Czudek, does not give a strictly smaller optimal coefficient on endpoint-anchored functions. Kelisky–Rivlin and Cooper–Waldron analyze iteration limits and eigenstructure, providing key context for the spectral rate but not the sharp anchored variation norm and its unique maximizing plateau. Manté analyzes iterated Bernstein operators for distribution and density estimation, and Gonska–Raşa study composite and iterated local Bernstein approximation with modulus-of-continuity estimates rather than this norm. The new identification combines exact operator-norm geometry with the interior survival of the absorbing binomial chain. Search-based originality is qualified; older and unindexed equivalent estimates remain possible.

## Limitations

Only the classical fixed-degree binomial Bernstein operator on a one-dimensional interval is studied, for real data and Jordan variation with both input endpoint values matched. The Perron asymptotic holds at fixed degree as power tends to infinity; no uniform joint degree–power asymptotic or sharp short-time continuum limit is established. No claim is made about generalized Bernstein–Durrmeyer operators, different endpoints, multidimensional Bernstein operators, or arbitrary variation norms.

## References

1. R. P. Kelisky and T. J. Rivlin, “Iterates of Bernstein Polynomials,” *Pacific Journal of Mathematics* **21** (1967), 511–520. https://msp.org/pjm/1967/21-3/pjm-v21-n3-p12-p.pdf
2. S. Cooper and S. Waldron, “The Eigenstructure of the Bernstein Operator,” *Journal of Approximation Theory* **105** (2000), 133–165. https://doi.org/10.1006/jath.2000.3464
3. C. Manté, “Iterated Bernstein operators for distribution function and density estimation,” HAL preprint hal-01092713, publicly deposited 2014-12-10; subsequently *Computational Statistics & Data Analysis* **84** (2015), 68–84. https://hal.science/hal-01092713
4. H. Gonska and I. Raşa, “Sur la suite des opérateurs Bernstein composés,” arXiv:1402.2520, first posted 2014-02-11. https://arxiv.org/abs/1402.2520
5. K. Czudek, “Bernstein and Kantorovich Polynomials Diminish the \(\Lambda\)-Variation,” arXiv:1609.00973, first posted 2016-09-04. https://arxiv.org/abs/1609.00973
