# Jacobi-root law for sharp curvature-variation error of Legendre projections

## Finding
For each integer \(n\geq1\), let \(\Pi_n\) be the unweighted \(L^2(0,1)\)-orthogonal projector onto real algebraic polynomials of degree at most \(n\). For real \(f\in W^{1,1}(0,1)\) with \(f'\in BV(0,1)\), put \(\mathcal V_2(f)=|D^2f|((0,1))\). Define
\[
 C_n^2=\sup_{\mathcal V_2(f)>0}\frac{\|(I-\Pi_n)f\|_{L^2(0,1)}^2}{\mathcal V_2(f)^2}.
\]
Write \(h_t(x)=(x-t)_+\), \(L_j(x)=P_j(2x-1)\), and \(F_n(t)=\|(I-\Pi_n)h_t\|_2^2\). The exact sharp norm for every \(n\geq1\) is
\[
 C_n^2=\max_{0\leq t\leq1} F_n(t),\qquad
 F_n(t)=\frac{(1-t)^3}{3}-\sum_{j=0}^n(2j+1)\left[\int_t^1(x-t)L_j(x)\,dx\right]^2.
\]
Its *entire interior stationary set* is explicitly given by the zeros of two consecutive Jacobi polynomials:
\[
 \boxed{F_n'(t)=-\frac{t^2(1-t)^2}{n(n+1)}P_{n-1}^{(1,1)}(2t-1)P_n^{(1,1)}(2t-1).}
\]
These \(2n-1\) distinct roots all lie in \((0,1)\), interlace, and constitute a finite algebraic prescription for \(C_n^2\) at every degree. All nonaffine equality cases are \(f(x)=a+bx+c(x-t)_+\) with \(c\ne0\) and \(t\) a global maximizer of \(F_n\).

The midpoint \(t=1/2\) is a **strict local maximum for every odd degree** and a **strict local minimum for every even degree**. The first three *global* constants and equality locations are
\[
\begin{array}{c|c|c}
n&C_n^2&\text{all maximizing knots}\cr\hline
1&1/192&1/2\cr
2&1/1500&(5-\sqrt5)/10,\ (5+\sqrt5)/10\cr
3&1/3072&1/2
\end{array}
\]
Thus degree-two spectral approximation is uniquely worst at a pair of displaced curvature singularities, unlike the adjacent odd degrees. The all-degree statement does **not** assert global midpoint optimality for every odd degree or global two-knot uniqueness for every even degree.

## Assumptions and scope
Lebesgue \(L^2(0,1)\) and ordinary distributional total variation are used; functions are identified up to almost-everywhere equality. \(P_j\) is the classical Legendre polynomial with \(P_j(1)=1\); \(P_j^{(\alpha,\beta)}\) is the classical Jacobi polynomial normalized by \(P_j^{(\alpha,\beta)}(1)=\binom{j+\alpha}{j}\). The derivative \(f'\) is an \(L^1\) representative of bounded variation and \(D^2f\) is its distributional derivative measure on the open interval. Affine functions are exactly the null space of \(\mathcal V_2\) and are reproduced by \(\Pi_n\) for \(n\geq1\). No boundary atoms enter the seminorm.

## Proof
**1. Sharp hinge reduction and rigidity.** The one-dimensional BV integration formula gives a finite signed measure \(\mu=D^2f\), real \(a,b\), and
\[
 f(x)=a+bx+\int_{(0,1)}(x-t)_+\,d\mu(t)
\]
in \(L^2(0,1)\). Because \((I-\Pi_n)\) annihilates affine functions, the Bochner integral and triangle inequality imply
\[
\|(I-\Pi_n)f\|_2\leq\int\|(I-\Pi_n)h_t\|_2\,d|\mu|(t)
\leq (\max_t\sqrt{F_n(t)})\,|\mu|((0,1)).
\]
Each one-atom measure realizes its hinge, proving sharpness. If a nonzero finite measure attains equality then the nonzero normalized residual vectors for \(|\mu|\)-almost every \(t\) must be collinear (including the signed phase). Distinct \(t\) cannot have proportional residual vectors: applying the second distributional derivative to \((I-\Pi_n)h_t\) produces \(\delta_t\) minus the smooth polynomial \((\Pi_nh_t)''\), so the singular atomic locations distinguish \(t\). Hence equality requires a single atom, establishing the full equality classification.

**2. Exact coefficients.** Since \(\|L_j\|_2^2=(2j+1)^{-1}\), orthogonality yields the displayed formula for \(F_n\). Put \(c_j(t)=\int_t^1(x-t)L_j(x)\,dx\). In particular \(c_0=(1-t)^2/2\). The shifted Rodrigues formula for \(L_j\) and two integrations by parts, for \(j\geq2\), give
\[
 c_j(t)=\frac{t^2(1-t)^2}{j(j-1)}P_{j-2}^{(2,2)}(2t-1),
\qquad c_j'(t)=-\frac{t(1-t)}{j}P_{j-1}^{(1,1)}(2t-1)\quad(j\geq1).
\]
The derivative formula also follows directly by integrating the shifted Legendre polynomial once.

**3. A Jacobi connection formula.** For \(j\geq2\), the identity
\[
 \frac{P_{j-2}^{(1,1)}(2t-1)}{j-1}-\frac{P_j^{(1,1)}(2t-1)}{j+1}
 =\frac{2(2j+1)t(1-t)}{j(j-1)}P_{j-2}^{(2,2)}(2t-1)
\]
has a short proof without induction. In the coordinate \(z=2t-1\), the polynomial on the left vanishes at both \(z=\pm1\), by the Jacobi endpoint values and parity. After division by \(1-z^2\), it is a polynomial of degree \(j-2\) orthogonal to every polynomial of degree at most \(j-3\) under the weight \((1-z^2)^2\), by the \((1-z^2)\)-orthogonality of each original Jacobi polynomial. It is therefore proportional to \(P_{j-2}^{(2,2)}(z)\). Comparing the leading coefficients \(2^{-k}\binom{2k+\alpha+\beta}{k}\) fixes the coefficient to \((2j+1)/(2j(j-1))\) in the \(z\)-coordinate, yielding the displayed identity.

**4. Derivative factorization for all degrees.** Direct expansion shows \(F_1(t)=t^3(1-t)^3/3\), whose derivative is the asserted Jacobi product at \(n=1\). Assume the identity at degree \(j-1\). Using \(F_j-F_{j-1}=-(2j+1)c_j^2\), differentiate, insert the two coefficient formulas from Step 2, and apply the connection identity from Step 3. The expression telescopes to
\[
F_j'(t)=-\frac{t^2(1-t)^2}{j(j+1)}P_{j-1}^{(1,1)}(2t-1)P_j^{(1,1)}(2t-1).
\]
This completes induction. Consecutive Jacobi polynomials for \(\alpha=\beta=1\) have simple interlacing zeros and no common root, proving the stationary-set claim and finite root maximization. At the midpoint, Jacobi parity gives a sign of \((-1)^{j-1}\) for the product's first derivative; with the leading minus sign in \(F'_j\), its second derivative is negative for odd \(j\) and positive for even \(j\). The sign is strict because each relevant Jacobi value or derivative at zero is nonzero.

**5. Three global examples.** With \(q=t(1-t)\in[0,1/4]\), direct orthogonality gives
\[
F_1=q^3/3,\qquad F_2=q^3(4-15q)/12,\qquad
F_3=q^3(1-9q+21q^2)/3.
\]
For \(F_2\), the only interior \(q\)-maximum is \(q=1/5\), with value \(1/1500\), exceeding its midpoint value \(1/3072\) and the zero endpoint value. For \(F_3\), the complete Jacobi stationary set has \(q=1/5\), \(q=1/7\), and the midpoint \(q=1/4\), with respective values \(1/9375\), \(1/7203\), and \(1/3072\), plus zero at endpoints. This proves all listed global optimizers and values.

## Verification
The standalone `checker.py` uses exact SymPy rational and Jacobi polynomial arithmetic. It derives the hinge coefficients by integration and confirms, for each degree \(1\) through \(10\), the coefficient identities, differentiated norm formula and (from degree two) the Jacobi connection relation, alongside exact first-three-degree expressions and constants. The run produced **126 passing symbolic assertions** on SymPy 1.14.0. These tests corroborate the formulas; the proof of their validity for *all* degrees is Steps 1–5, not an extrapolation from the ten cases. Reproduce with `python checker.py` in an environment with SymPy installed.

## Relationship to prior work
The 2011 Wang–Xiang paper studies coefficient decay, uniform-norm convergence and interpolation for Legendre expansions, not the exact \(\mathcal V_2\)-to-\(L^2\) norm. Xiang's 2014 interpolation paper uses Peano kernels for pointwise interpolation estimates, a different approximation operator and objective. Liu–Wang–Wu (2020, especially coefficient formulas and Theorem 3.4) is the closest inspected work: it treats Legendre approximations of singular functions including hinges and gives general \(L^2\) error estimates for bounded-variation derivatives, but does not state the exact best constant over the full \(\mathcal V_2\) ball, the Jacobi-product stationary-root law, or the global knot extremizer classification established here. Earlier pointwise \(p\)-FEM singularity studies concern different error objectives. These are statement-level distinctions, not a claim that no inaccessible or unindexed equivalent exists.

## Limitations
No all-degree closed formula selecting *which* of the \(2n-1\) roots is globally optimal beyond the prescribed finite comparison is proved. No all-degree global odd/even knot classification, asymptotic expansion, other weight, other error norm, or independent validation is claimed. The complete full text of every historical possibly relevant article was not obtained. Historical priority remains a residual risk; the result is a self-contained mathematical claim pending independent review.

## References
1. H. Wang and S. Xiang, “On the convergence rates of Legendre approximation,” *Mathematics of Computation* 81 (2012), 861–877; electronically published 18 October 2011. https://doi.org/10.1090/S0025-5718-2011-02549-4
2. S. Xiang, “On Interpolation Approximation: Convergence rates for polynomial interpolation for functions of limited regularity,” arXiv:1411.7746 (28 November 2014). https://arxiv.org/abs/1411.7746
3. W. Liu, L.-L. Wang and B. Wu, “Optimal error estimates for Legendre expansions of singular functions with fractional derivatives of bounded variation,” arXiv:2006.00667 (1 June 2020). https://arxiv.org/abs/2006.00667
4. I. Babuška and H. Hakula, “On the \(p\)-version of FEM in one dimension: The known and unknown features,” arXiv:1401.1483 (7 January 2014). https://arxiv.org/abs/1401.1483
