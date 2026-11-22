# Sharp entrywise matrix-logarithm stability on spectral bands and its critical-width crossover

## Finding
Let \(n\ge1\), \(0<a<b\), and let \(\mathcal K_{n,a,b}\) be the closed convex set of real symmetric matrices satisfying \(aI\preceq A\preceq bI\). Use the maximum absolute-entry matrix norm \(\|H\|_{\max}=\max_{i,j}|H_{ij}|\). For the principal matrix logarithm, the exact global two-input Lipschitz modulus is
\[
\Lambda_n(a,b):=\sup_{\substack{A,B\in\mathcal K_{n,a,b}\\A\ne B}}
\frac{\|\log A-\log B\|_{\max}}{\|A-B\|_{\max}}
=\frac{c_n^2}{a}+\frac{(1-c_n)^2}{b}
+\frac{2c_n(1-c_n)}{b-a}\log\frac ba,
\qquad c_n=\frac{1+\sqrt n}{2}.
\]
The constant is sharp as a supremum of ratios of distinct admissible matrices, with a rank-one low-eigenspace family providing the limiting witnesses. No claim that distinct matrices attain the supremum is made.

The exact formula has two spectral-width regimes. For every fixed ratio \(r>1\),
\[
\lim_{n\to\infty}\frac{\Lambda_n(a,ra)}{n}
=\frac{1}{4a}\left(1+\frac1r-\frac{2\log r}{r-1}\right)>0.
\]
For every fixed \(x>0\), choosing \(b_n=a(1+x/\sqrt n)\) instead gives the finite critical-window law
\[
\lim_{n\to\infty}a\Lambda_n(a,b_n)=1+\frac x2+\frac{x^2}{12}.
\]
The contrast scale \(b/a-1\asymp n^{-1/2}\) therefore separates bounded amplification from linear-in-dimension amplification for a fixed nontrivial relative spectral band.

## Assumptions and scope
All matrices and perturbations are real symmetric; no entrywise sign restriction is placed on inputs, beyond positive definiteness and the spectral bounds. The logarithm is the principal real symmetric matrix logarithm defined by spectral functional calculus. Both the input and output norms are maximum absolute entries, not spectral, Frobenius, or induced matrix-row norms. The formula includes \(n=1\). The strict hypothesis \(a<b\) ensures that the admissible domain contains distinct points; as \(b\downarrow a\), the formula tends to \(1/a\). Only the *global* Lipschitz modulus is characterized, not the local constant at every individual matrix.

## Proof
**1. Sharp row norm of a positive contraction.** For every real symmetric \(P\) with \(0\preceq P\preceq I\), every row satisfies
\[
\sum_{j=1}^n|P_{ij}|\le c_n.
\]
Indeed the row sum equals \(\max_{s\in\{-1,1\}^n}e_i^{\mathsf T}Ps\). For fixed signs, this equals \(\operatorname{tr}(PB_s)\) where \(B_s=(e_is^{\mathsf T}+se_i^{\mathsf T})/2\). The maximum over positive contractions of this trace is the sum of the positive eigenvalues of \(B_s\). Its only potentially nonzero eigenvalues are \((s_i+\sqrt n)/2\) and \((s_i-\sqrt n)/2\), so the positive sum is at most \(c_n\). For \(n=1\) the same statement is immediate. For \(n\ge2\), equality is realized by \(P=uu^{\mathsf T}\), where \(u\) has strictly positive entries and
\[
 u_1^2=\frac{1+n^{-1/2}}2,
 \qquad u_j^2=\frac{1-n^{-1/2}}{2(n-1)}\quad(2\le j\le n).
\]
Then \(\sum_jP_{1j}=c_n\), and all entries of \(P\) are nonnegative. The case \(n=1\) uses \(P=[1]\).

**2. A common resolvent row envelope.** Write \(R_t=(A+tI)^{-1}\), \(t\ge0\), and
\[
 r_a(t)=\frac1{a+t},\qquad r_b(t)=\frac1{b+t},\qquad
 \delta(t)=r_a(t)-r_b(t)>0.
\]
The spectral bounds give \(R_t=r_b(t)I+\delta(t)P_t\) for some positive contraction \(P_t\). Because \((P_t)_{ii}\ge0\), the first step implies, for every row \(i\),
\[
\sum_j |(R_t)_{ij}|\le q(t):=r_b(t)+\delta(t)c_n
=\frac{c_n}{a+t}+\frac{1-c_n}{b+t}.
\]
Note that \(q(t)>0\) although \(1-c_n\le0\).

**3. Global derivative upper bound.** The standard resolvent Fréchet formula for the logarithm is
\[
 D\log(A)[H]=\int_0^\infty R_tHR_t\,dt.
\]
The integral converges absolutely for \(A\succeq aI\). For every two output indices \(i,j\),
\[
 |(D\log(A)[H])_{ij}|
 \le\|H\|_{\max}\int_0^\infty
 \left(\sum_k|(R_t)_{ik}|\right)
 \left(\sum_l|(R_t)_{jl}|\right)dt
 \le\|H\|_{\max}\int_0^\infty q(t)^2dt.
\]
The segment connecting any two admissible matrices remains admissible, so integrating the derivative along this segment establishes the same bound for the global two-input modulus.

**4. Saturation and finite-input witnesses.** Let \(P=uu^{\mathsf T}\) be the positive rank-one projector from step 1, and choose \(A_*=aP+b(I-P)\). Its resolvent is \(R_t=r_b(t)I+\delta(t)P\), entrywise nonnegative, with first-row sum exactly \(q(t)\). Put \(J={\bf1}{\bf1}^{\mathsf T}\), so \(\|J\|_{\max}=1\). Then
\[
 (D\log(A_*)[J])_{11}=\int_0^\infty q(t)^2dt.
\]
Although \(A_*\) lies on the spectral boundary, \(A_\varepsilon=(a+\varepsilon)P+(b-\varepsilon)(I-P)\) is an interior point for \(0<\varepsilon<(b-a)/2\), and \(A_\varepsilon+hJ\) remains admissible whenever \(0<h<\varepsilon/n\). First let \(h\downarrow0\), then \(\varepsilon\downarrow0\). The resulting ratios of **distinct admissible matrices** converge to the upper bound, establishing global sharpness. For \(n=1\), use \(P=I\) and the same perturbation argument.

**5. Explicit integration.** Expanding \(q(t)^2\) and integrating gives
\[
 \int_0^\infty\frac{dt}{(a+t)^2}=\frac1a,\quad
 \int_0^\infty\frac{dt}{(b+t)^2}=\frac1b,\quad
 \int_0^\infty\frac{dt}{(a+t)(b+t)}=\frac{\log(b/a)}{b-a}.
\]
This yields the displayed exact closed form.

**6. Dimension and spectral-band regimes.** With \(b=ra\), divide the closed form by \(n\), and use \(c_n/\sqrt n\to1/2\) and \((1-c_n)/\sqrt n\to-1/2\) to obtain the fixed-ratio coefficient. Its bracket is strictly positive for \(r>1\), as it is \(a\) times the integral of a nonzero squared resolvent difference. In the critical window \(b_n=a(1+x/\sqrt n)\), change variables \(t\mapsto at\) in the integral. The normalized integrand is
\[
 \left[\frac1{1+t}+\frac{(c_n-1)(x/\sqrt n)}{(1+t)(1+t+x/\sqrt n)}\right]^2.
\]
It converges pointwise to \([1/(1+t)+(x/2)/(1+t)^2]^2\), and is dominated by a constant times \((1+t)^{-2}\) for fixed \(x>0\). Dominated convergence and elementary integrals \(\int_0^\infty (1+t)^{-k}dt=1/(k-1)\), \(k=2,3,4\), give \(1+x/2+x^2/12\).

## Verification
The analytic proof above establishes all quantified infinite-dimensional-index and limiting statements. The supplementary executable `checker.py` separately checks 625 floating-point assertions/comparisons, including the sharp contraction row witness, resolvent-integral/closed-form agreement, independent eigenbasis divided-difference derivatives, arbitrary admissible symmetric perturbations, distinct-input witnesses, and the two asymptotic regimes. Run `python checker.py` with NumPy and SciPy installed. These experiments are illustrative and do not replace any infinite proof step.

## Relationship to prior work
Kandolf, Koskela, Relton and Schweitzer developed low-rank computations and convergence analysis for Fréchet derivatives of matrix functions, including the logarithm, in their 2020 preprint and subsequent 2021 journal article (Section 4). Their resolvent formulas supply analytic context, but their theorem is an approximation/error bound, not this optimized maximum-entry global modulus. Crouzeix and Kressner (2020) proved numerical-range-based *spectral*-norm bounds for bivariate matrix functions and Fréchet derivatives, not a sharp maximum-entry norm on a real positive spectral band. Higham and Relton (2014) studied condition estimates for matrix-function Fréchet derivatives and numerical 1-norm tests, not the stated two-input entrywise logarithm optimization. The single-endpoint bound obtained by replacing the finite upper spectral boundary with infinity is weaker than the exact band-sensitive coefficient above. A preexisting equivalent entrywise result outside the inspected literature remains possible.

## Limitations
The theorem concerns real symmetric positive-definite matrices and spectral interval constraints only; extensions to nonnormal, complex Hermitian, entrywise nonnegative, or sparsity-constrained families require separate analysis. It gives sharp **supremum**, not attainment by two different matrices. It does not measure the induced matrix infinity norm or Frobenius norm. It does not assert publication priority: historical discovery and unindexed sources remain possible. Numerical checks are not independent mathematical validation.

## References
1. P. Kandolf, A. Koskela, S. D. Relton, M. Schweitzer, *Computing low-rank approximations of the Fréchet derivative of a matrix function using Krylov subspace methods*, arXiv:2008.12926, first posted August 29, 2020; *Numerical Linear Algebra with Applications* 28 (2021), e2401, DOI:10.1002/nla.2401, especially Section 4, https://onlinelibrary.wiley.com/doi/full/10.1002/nla.2401.
2. M. Crouzeix, D. Kressner, *A bivariate extension of the Crouzeix-Palencia result with an application to Fréchet derivatives of matrix functions*, arXiv:2007.09784, first posted July 19, 2020, https://arxiv.org/abs/2007.09784.
3. N. J. Higham, S. D. Relton, *Estimating the Condition Number of the Fréchet Derivative of a Matrix Function*, *SIAM Journal on Scientific Computing* 36 (2014), C617–C634, DOI:10.1137/130950082, https://eprints.maths.manchester.ac.uk/2197/1/130950082.pdf.
