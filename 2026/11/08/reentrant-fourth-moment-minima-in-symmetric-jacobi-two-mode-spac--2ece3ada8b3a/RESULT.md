# Reentrant fourth-moment minima in symmetric Jacobi two-mode spaces

## Finding

Let \(\alpha>0\). Give \((-1,1)\) the symmetric Jacobi probability law \(\mu_\alpha\) with density proportional to \((1-x^2)^{\alpha-1}\). The real two-dimensional space of \(\mu_\alpha\)-centered polynomials of degree at most two has a complete, exactly solvable fourth-moment norm geometry. There are **four distinct parameter thresholds**, at which the types of optimizers change:
\[
\alpha_0=\frac{\sqrt{33}-5}{8},\qquad \frac14,\qquad\frac12,\qquad
\beta_0=\frac{\sqrt{97}-5}{8}.
\]
In particular, the minimizing type is *mixed, pure linear, pure quadratic, pure linear again* as \(\alpha\) increases. The quadratic region lies strictly between the circle and two-sphere parameter values, so it is invisible when considering only integer spherical dimensions.

Set
\[
P_1(x)=x,\quad P_2(x)=x^2-\frac1{2\alpha+1},\quad
s_1=\frac1{2\alpha+1},\quad
s_2=\frac{4\alpha}{(2\alpha+1)^2(2\alpha+3)}.
\]
These are orthogonal and centered, with \(\|P_j\|_2^2=s_j\). For \(f=aP_1+bP_2\ne0\), define its normalized linear energy
\[
u=\frac{a^2s_1}{a^2s_1+b^2s_2}\in[0,1],\qquad
K_\alpha(f)=\frac{\|f\|_4^4}{\|f\|_2^4}.
\]
Introduce the explicit rational functions
\[
A=\frac{3(2\alpha+1)}{2\alpha+3},\quad
B=\frac{3(2\alpha+3)(10\alpha^2-3\alpha+2)}{\alpha(2\alpha+5)(2\alpha+7)},\quad
C=\frac{10\alpha+1}{2\alpha+5}.
\]
Then **for every nonzero real \(f\)**,
\[
\boxed{K_\alpha(f)=A u^2+6C u(1-u)+B(1-u)^2.}
\]
Where \(\alpha\in(0,\alpha_0)\cup(1/4,\infty)\), the critical energy
\[
u_*=\frac{B-3C}{A-6C+B}\in(0,1),\qquad
H= B-\frac{(B-3C)^2}{A-6C+B}
\]
is well-defined. Its exact squared-deviation identity is
\[
K_\alpha(f)-H=(A-6C+B)(u-u_*)^2.
\]
The **sharp lower and upper endpoints** are as follows.

* If \(0<\alpha<\alpha_0\), the lower endpoint is \(H\) with \(u=u_*\). If \(\alpha_0\le\alpha<1/2\), the lower endpoint is \(A\) with \(u=1\). If \(1/2<\alpha<\beta_0\), the lower endpoint is \(B\) with \(u=0\). If \(\alpha>\beta_0\), the lower endpoint is \(A\) with \(u=1\). At \(\alpha=1/2\) and \(\alpha=\beta_0\), the lower endpoint is \(A=B\), attained exactly at the two pure modes \(u\in\{0,1\}\).
* If \(0<\alpha\le1/4\), the upper endpoint is \(B\), attained exactly at \(u=0\). If \(\alpha>1/4\), the upper endpoint is \(H\), attained exactly at \(u=u_*\).

Every number between the endpoints is attained. The stated equality conditions are complete: when \(u=0\) or \(u=1\) the nonzero polynomial is a scalar multiple of the respective \(P_j\); when \(u=u_*\in(0,1)\), both coefficients are nonzero and either independent relative sign is permitted. Multiplication by a nonzero real scalar does not change \(K_\alpha\).

At the circle parameter \(\alpha=1/2\), the exact interval is \([3/2,9/4]\). At the two-sphere parameter \(\alpha=1\), the exact interval is \([9/5,375/112]\). As \(\alpha\to\infty\), the endpoints tend to \(3\) and \(15\), respectively.

## Assumptions and scope

All norms are with respect to normalized \(\mu_\alpha\); the coefficient field is \(\mathbb R\), the degree restriction is at most two, and the mean is zero. The Jacobi weight exponent \(\alpha-1\) may be any real number greater than \(-1\). The notation \(\alpha\) denotes the Beta shape, not the classical Jacobi exponent. The zero polynomial is excluded because its ratio is undefined.

## Proof

The measure is symmetric, and its even moments satisfy, for all nonnegative integers \(j\),
\[
\mathbb E X^{2j}=\prod_{k=1}^{j}\frac{2k-1}{2\alpha+2k-1},
\qquad\mathbb E X^{2j+1}=0.
\]
Consequently \(\mathbb EP_1^2=s_1\), \(\mathbb EP_2^2=s_2\), and \(\mathbb EP_1P_2=0\). Direct expansion up to the eighth moment yields
\[
\frac{\mathbb E P_1^4}{s_1^2}=A,\quad
\frac{\mathbb E(P_1^2P_2^2)}{s_1s_2}=C,\quad
\frac{\mathbb E P_2^4}{s_2^2}=B.
\]
The odd mixed terms \(\mathbb E P_1^3P_2\) and \(\mathbb E P_1P_2^3\) vanish. Normalizing \(a^2s_1+b^2s_2\) proves the displayed formula for \(K_\alpha\).

The decisive sign identities are
\[
A-3C=\frac{-6(8\alpha^2+10\alpha-1)}{(2\alpha+3)(2\alpha+5)},
\qquad
B-3C=\frac{-18(2\alpha+1)(4\alpha-1)}{\alpha(2\alpha+5)(2\alpha+7)},
\]
\[
B-A=\frac{6(\alpha+1)(2\alpha-1)(8\alpha^2+10\alpha-9)}{\alpha(2\alpha+3)(2\alpha+5)(2\alpha+7)}.
\]
The derivative of the quadratic in \(u\) at the left and right endpoints is, respectively, \(2(3C-B)\) and \(2(A-3C)\).

If \(0<\alpha<\alpha_0\), both \(A-3C\) and \(B-3C\) are positive. Thus \(A-6C+B>0\), the endpoint derivatives have opposite signs, and there is a unique strict interior **minimum** at \(u_*\), while the **maximum** is \(B>A\) at \(u=0\). If \(\alpha_0\le\alpha\le1/4\), both endpoint derivatives are nonpositive. Since the derivative is affine, the quadratic is strictly decreasing in the interior (apart from a possible zero derivative at one endpoint), and its extrema are uniquely \(A\) at \(u=1\) and \(B\) at \(u=0\).

If \(\alpha>1/4\), both \(A-3C\) and \(B-3C\) are negative. Hence \(A-6C+B<0\), the endpoint derivatives have opposite signs in reverse order, and there is a unique strict interior **maximum** at \(u_*\). Its **minimum** lies at the endpoint with smaller value. The last factored identity gives exactly the two changes of minimizing endpoint at \(\alpha=1/2\) and \(\alpha=\beta_0\). Where the endpoints tie, strict concavity excludes every mixture from equality. The formula for \(K_\alpha\) is continuous on the connected interval \([0,1]\), so its image is precisely the closed interval between these attained extremes. This proves all assertions.

## Verification

The standalone `verify_jacobi.py` recomputes the coefficients by exact symbolic moments, separately integrates the raw Beta-binomial moment expansion, checks all derivative and endpoint factorizations, tests the exact quadratic deficit identity, and independently reconstructs thirty-six fourth moments by polynomial integration. Its exact rational finite diagnostics corroborate, but do not replace, the analytical sign proof above. Execute from the package with `python verify_jacobi.py`; SymPy is the only nonstandard Python dependency.

## Relationship to prior work

Jacobi polynomial expansions and hypercontractive semigroups are classical. Nowak and Sjögren (2011) study Jacobi heat-kernel bounds, while Toranzo, Dehesa and Sánchez-Moreno (2014) provide formulas for the \(L^q\) norms of individual hypergeometric orthogonal polynomials. Those moment methods can calculate ingredients of \(A\), \(B\), and \(C\), but their stated theorems do not determine the optimal *mixture* for every positive real shape, nor its reentrant phase diagram. Prior spherical mixed dipole–quadrupole results already provide the upper constant \(375/112\) at \(\alpha=1\); that specialization is not presented as new. At \(\alpha=1/2\), trigonometric identities likewise recover familiar two-tone circle norms. Neither isolated spherical specialization controls the positive real shape intervals separating them.

## Limitations

The theorem is specific to a real two-mode **centered** Jacobi polynomial space and to fourth moments. It does not assert a Banach–Mazur distance, a statement for arbitrary Jacobi asymmetry, higher degrees, other exponents, or complex coefficients. The calculation and phase diagram are exact; novelty beyond the primary literature and indexed comparisons remains subject to possible unindexed equivalent formulations.

## References

1. A. Guerrero, P. Sánchez-Moreno, J. S. Dehesa, *Information-theoretic lengths of Jacobi polynomials*, J. Phys. A 43 (2010), 305203. DOI: https://doi.org/10.1088/1751-8113/43/30/305203 (published publicly 2010-06-28).
2. A. Nowak, P. Sjögren, *Sharp estimates of the Jacobi heat kernel*, arXiv:1111.3145v1 (2011-11-14), https://arxiv.org/abs/1111.3145.
3. I. V. Toranzo, J. S. Dehesa, P. Sánchez-Moreno, *Frequency moments, \(L_q\) norms and Rényi entropies of general hypergeometric polynomials*, J. Math. Chem. 52 (2014), 1372–1385. DOI: https://doi.org/10.1007/s10910-014-0317-1.
