# A degree-nine extremal-cell transition for quadratic-reproducing Bernstein sampling

## Finding

For every integer \(n\ge1\), consider the King modification of Bernstein sampling
\[
(V_nf)(x)=\sum_{k=0}^{n}\binom nk\rho_n(x)^k(1-\rho_n(x))^{n-k}f(k/n),\qquad 0\le x\le1,
\]
where \(\rho_n\colon[0,1]\to[0,1]\) is the unique increasing solution of
\[
\rho_n(x)+(n-1)\rho_n(x)^2=nx^2.
\]
In particular, \(\rho_1(x)=x^2\). On real right-continuous Jordan-BV inputs satisfying \(f(0)=f(0+)\), with arbitrary allowed endpoint value \(f(1)\), set
\[
C_n=\sup_{V(f)>0}\frac{\|V_nf-f\|_{L^1(0,1)}}{V(f)},\qquad V(f)=\operatorname{Var}_{[0,1]}(f).
\]
For \(1\le j\le n\), let \(U_{n,j}\sim\operatorname{Beta}(j,n-j+1)\), and put
\[
X_{n,j}=\sqrt{U_{n,j}^2+\frac{U_{n,j}(1-U_{n,j})}{n}},\quad
R_{n,j}=\mathbb E\left|X_{n,j}-\frac{j-1}{n}\right|,\quad
L_{n,j}=\mathbb E\left|X_{n,j}-\frac jn\right|.
\]
The **exact formula for every degree** is
\[
\boxed{C_n=\max_{1\le j\le n}\max\{R_{n,j},L_{n,j}\}.}
\]
The finite-degree extremal-cell transition is **rigorously localized**:
\[
\boxed{C_n=R_{n,1}>\max_{(j,E)\ne(1,R)}E_{n,j}\quad(1\le n\le8),}
\]
\[
\boxed{C_9=R_{9,4}>\max_{(j,E)\ne(4,R)}E_{9,j}.}
\]
Thus for degrees one through eight the unique maximizing cell-side is a jump approaching the left endpoint from the interior; at degree nine it is instead a jump approaching \(1/3\) **from the right**. The inequalities are between all \(2n\) listed candidates, and both maxima are strict. For the specified right-continuous representative class, none of the sharp norms \(C_1,\ldots,C_9\) is attained by a nonconstant input, although each is approached by single jumps.

The asymptotic constant and limiting location are
\[
\boxed{\lim_{n\to\infty}\sqrt n\,C_n=\frac1{\sqrt{2\pi}}.}
\]
Every sequence of single jumps whose errors are asymptotic to \(C_n\) has jump positions converging to \(1/2\). No claim is made that the degree-nine interior candidate remains maximal at every higher finite degree, or that each higher-degree maximizing grid index is unique.

## Assumptions and scope

Input functions are real-valued and have finite Jordan variation on \([0,1]\). They are right-continuous on \([0,1)\) and match their right trace at zero; the value at one is an allowed endpoint jump. These conventions fix all sampled values. The operator is point sampling, not the Kantorovich or Durrmeyer integral modification. Its positive basis sums to one and reproduces the function \(x\mapsto x^2\). Lebesgue measure defines the output norm, with no mass normalization beyond the unit interval. The sample lattice is \(\{0,1/n,\ldots,1\}\).

## Proof

**1. Beta-quantile representation.** The inverse mapping is
\[
\rho_n^{-1}(u)=\sqrt{u^2+u(1-u)/n}.
\]
For a right-continuous jump \(h_s(t)={\bf1}_{\{t\ge s\}}\) and \((j-1)/n<s\le j/n\), the binomial-tail identity gives
\[
(V_n h_s)(x)=\Pr\{\mathrm{Bin}(n,\rho_n(x))\ge j\}
 =\Pr\{U_{n,j}\le\rho_n(x)\}
 =\Pr\{X_{n,j}\le x\}.
\]
Tonelli's theorem then yields the exact integrated error
\[
\|V_nh_s-h_s\|_1=\mathbb E|X_{n,j}-s|.
\]

**2. Sharp BV reduction and candidate endpoints.** Every admissible \(f\) has a finite signed Stieltjes derivative measure \(\mu\) on \((0,1]\), with \(f(t)=f(0)+\int_{(0,1]}h_s(t)\,d\mu(s)\) and \(V(f)=|\mu|((0,1])\). By positivity, linearity and Fubini,
\[
\|V_nf-f\|_1\le\int_{(0,1]}\|V_nh_s-h_s\|_1\,d|\mu|(s).
\]
For each \(j\), the function \(s\mapsto\mathbb E|X_{n,j}-s|\) is strictly convex on \(((j-1)/n,j/n]\), since \(X_{n,j}\) has strictly positive interior density. Its supremum on that half-open interval is the maximum of its right-hand limit at \((j-1)/n\) and its value at \(j/n\), namely \(R_{n,j}\) and \(L_{n,j}\). Single jumps tending to these endpoints establish the matching lower bound, proving the finite exact formula.

**3. Exact finite-degree certificate.** `CHECKER.py` uses only integer arithmetic. It sets \(Q=2^{20}\), \(M=10080\) (divisible by every \(1\le n\le9\)) and brackets each \(\rho_n(i/M)\) by consecutive multiples of \(1/Q\), using
\[
M^2\bigl(kQ+(n-1)k^2\bigr)\le ni^2Q^2
\]
to select the maximal lower integer \(k\). Binomial-tail probabilities at these rational endpoints are computed exactly as integer numerators over \(Q^n\). Monotonicity in the evaluation argument supplies left- and right-Riemann enclosures for the integrals defining all \(R_{n,j},L_{n,j}\). Every comparison uses the strict inequality “target lower numerator greater than competitor upper numerator” with the **same denominator** \(MQ^n\). The checker confirms all \(2n-1\) comparisons for degrees one through nine: degree \(n\le8\) targets \(R_{n,1}\); degree nine targets \(R_{9,4}\). Its interval outputs include
\[
0.1511371<C_8<0.1512377,\qquad
0.1369256<C_9<0.1370258,
\]
and the degree-nine left-boundary candidate lies in \((0.1360705,0.1361711)\). These intervals and all strict rankings are certified by exact integer inequalities, not floating-point rounding. Uniqueness of the cell-side candidates and strict convexity imply that none of the corresponding right-side endpoint suprema is attained by any individual admissible step. Since the error of every step is then strictly below \(C_n\), the signed-measure bound excludes norm attainment by any nonconstant admissible BV input for \(n\le9\).

**4. Universal asymptotic.** On one probability space couple \(X_{n,j}\) and \(U_{n,j}\) by their displayed formula. For every \(u\in[0,1]\),
\[
0\le\sqrt{u^2+u(1-u)/n}-u\le1/n,
\]
so each King step error differs from its classical Bernstein counterpart by at most \(1/n\), uniformly over all \(j\) and all admissible \(s\). Consequently their sharp constants differ by at most \(1/n\). For a sequence \(j/n\to a\in(0,1)\) and \((j-1)/n<s\le j/n\), the beta central limit theorem with bounded second moments gives
\[
\sqrt n\,\mathbb E|U_{n,j}-s|\to\sqrt{\frac{2a(1-a)}{\pi}}.
\]
For \(a=0\) or \(1\), the same limit is zero by the beta variance bound and the fact that the mean differs from \(s\) by \(O(1/n)\). Subsequential compactness and the unique maximum of \(a(1-a)\) at \(1/2\) establish the sharp \(1/\sqrt{2\pi}\) constant and all asymptotically maximizing single-jump locations.

## Verification

Run `python3 CHECKER.py` in a Python 3 standard-library environment. Expected terminal line: `EXACT_INTEGER_RIEMANN_ENCLOSURE_PASS`. It tests **81 strict candidate comparisons** across the nine degrees, plus all interval bounds. Each binomial-tail enclosure comes from a polynomial with integer coefficients and integer root bracketing. The asymptotic theorem is proved analytically, not by the finite checker.

## Relationship to prior work

King's 2003 quadratic-reproducing Bernstein modification defines the source operator. Gonska and Piţul (2005) give its exact defining function, modulus-of-continuity estimates, iteration limit and moment considerations. Their proof does not contain the present integrated \(BV\)-to-\(L^1\) sharp coefficient or finite jump-cell rankings. Braica, Pop and Indrea (online January 1, 2012) investigate a distinct King-type operator fixing both linear and quadratic functions. Acar et al. (2019) survey positive approximation and comparison results, not the claimed exact BV coefficient. Adell, Garrancho and Martínez-Sánchez (first online November 25, 2025) provide general probabilistic local error estimates for discontinuous inputs, including classical Bernstein examples; these estimates do not compute the present global integrated King coefficient or its degree-nine grid-cell comparison. Existing exact BV approximation results for the **classical** Bernstein operator have a different kernel, corresponding to \(\rho_n(x)=x\), and do not imply the present numeric rankings without the new time change and certified comparisons.

## Limitations

The finite transition is proved for **degrees one through nine**; no assertion is made about the finite-degree winning cell at \(n\ge10\). The all-degree result is the finite beta-moment formula and its asymptotic law. Point samples require the specified representative convention; admitting arbitrary point values at jumps can change norm-attainment statements. No weighted intervals, multivariate settings, integral sampling modifications or complete higher-degree maximizing-index classification are included. The 2003 original full text could not be obtained during this literature comparison; the 2005 full-text follow-up directly reproduces the operator's exact definition. Historical priority beyond inspected sources remains unverified.

## References

1. J. P. King, “Positive linear operators which preserve \(x^2\),” *Acta Math. Hungar.* 99 (2003), 203–208. https://doi.org/10.1023/A:1024571126455
2. H. Gonska and P. Piţul, “Remarks on an article of J. P. King,” *Comment. Math. Univ. Carol.* 46 (2005), 645–652. https://dml.cz/dmlcz/119556
3. P. I. Braica, O. T. Pop and A. D. Indrea, “About a King-type operator,” *Appl. Math. Inf. Sci.* 6 (2012), 145–148; first publicly available online January 1, 2012. https://www.naturalspublishing.com/files/published/9m5vu24e94bq6e.pdf
4. T. Acar, M. Cappelletti Montano, P. Garrancho and V. Leonessa, “On Sequences of J. P. King-Type Operators,” *Journal of Function Spaces* (2019), article 2329060. https://doi.org/10.1155/2019/2329060
5. J. A. Adell, P. Garrancho and F. J. Martínez-Sánchez, “Approximation of Discontinuous Functions by Positive Linear Operators. A Probabilistic Approach,” *Math. Methods Appl. Sci.*, first online November 25, 2025. https://doi.org/10.1002/mma.70341
6. M. A. Özarslan, O. Duman and C. Kaanoğlu, “Rates of convergence of certain King-type operators for functions with derivative of bounded variation,” *Math. Comput. Model.* 52 (2010), 334–345. https://doi.org/10.1016/j.mcm.2010.02.048
