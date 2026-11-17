# Logarithmic certificate-degree obstruction at a collapsing positivity interval

## Finding

The minimum matrix sum-of-squares certificate degree for the collapsing-interval family of Jindal and Zalar grows at least logarithmically, with an explicit geometric coefficient. Define \(d_\varepsilon\) as below. Then

\[
\liminf_{\varepsilon\downarrow0}\frac{d_\varepsilon}{\log(1/\varepsilon)}\geq
\frac{1}{\log(3+2\sqrt2)}=0.5672963285\ldots.
\]

In particular, the previously established divergence of these degrees has a quantitative, uniform asymptotic lower bound. No matching upper bound or optimality of the coefficient is asserted.

## Assumptions and scope

Fix \(0<\varepsilon<1/2\) and write

\[
K_\varepsilon=[0,\varepsilon^2]\cup[1/2,1],\quad
q_\varepsilon(x)=(x-\varepsilon^2)(x-1/2),\quad
\theta(x)=x(1-x),\quad \rho_\varepsilon=1+2\varepsilon-\varepsilon^3.
\]

Let the Hermitian matrix polynomial be

\[
F_\varepsilon(x)=
\begin{pmatrix}
\rho_\varepsilon[x^2+\varepsilon\theta(x)] & \rho_\varepsilon\theta(x)\\
\rho_\varepsilon\theta(x) & \varepsilon(1-x)^2+(1-\varepsilon^2)\theta(x)
\end{pmatrix}.
\]

For a Hermitian matrix polynomial \(S\), the notation \(S\in\operatorname{SOS}_2\) means that \(S(x)\) is a finite sum of \(P(x)^*P(x)\) for complex polynomial matrices \(P\), hence \(S(x)\succeq0\) for every real \(x\). The *weighted degree* of \(wS\) is its ordinary matrix-polynomial degree. Define \(d_\varepsilon\) to be the least integer \(d\geq0\) for which there exist \(\Sigma_{abc}\in\operatorname{SOS}_2\), indexed by \(a,b,c\in\{0,1\}\), with

\[
F_\varepsilon(x)=\sum_{a,b,c\in\{0,1\}}
 x^a(1-x)^b q_\varepsilon(x)^c\Sigma_{abc}(x),
\qquad
\deg\bigl(x^a(1-x)^b q_\varepsilon^c\Sigma_{abc}\bigr)\leq d
\]

for every nonzero summand. Existence of such a finite certificate follows from the saturated scalar description and Theorem A of Jindal–Zalar (2026); \(F_\varepsilon\succeq0\) on \(K_\varepsilon\) because \(\det F_\varepsilon=2\rho_\varepsilon\theta q_\varepsilon\), and both diagonal entries are nonnegative there. All logarithms are natural. The claim concerns the complex \(2\times2\) matrix preordering; it also supplies a lower bound for any smaller cone of permitted certificates.

## Proof

**1. Uniform interpolation/derivative estimate.** Fix \(R>R_0:=3+2\sqrt2\). Put \(a=1/2+\delta\), \(b=1-\delta\) for a sufficiently small fixed \(\delta\in(0,1/4)\), and \(I=[a,b]\). The exterior conformal map for this segment is

\[
W_I(z)=t(z)+\sqrt{t(z)^2-1},\qquad t(z)=\frac{2z-a-b}{b-a},
\]

with the square-root branch chosen so that \(|W_I(z)|>1\) outside \(I\). At \(z=0\), its absolute value tends to \(3+2\sqrt2\) as \(\delta\downarrow0\). Choose \(\delta\) and then \(r>0\) so that \(\overline{D(0,r)}\cap I=\varnothing\) and \(\max_{|z|\leq r}|W_I(z)|<R\). The elementary Bernstein–Walsh estimate for a polynomial \(p\) of degree at most \(d\) gives

\[
\max_{|z|\leq r}|p(z)|\leq R^d\max_{x\in I}|p(x)|.
\]

Indeed, writing \(z=(a+b)/2+(b-a)(w+w^{-1})/4\), the function \(w^{-d}p(z(w))\) is holomorphic on \(|w|>1\), including infinity, and its maximum there is bounded by its maximum on \(|w|=1\); the latter is \(\max_I|p|\). Cauchy's inequalities on the disk therefore bound the first and second derivatives at zero by \(r^{-1}R^d\max_I|p|\) and \(2r^{-2}R^d\max_I|p|\), respectively.

**2. Uniform bounds on certificate matrices.** Fix a certificate of weighted degree \(d=d_\varepsilon\), and suppose \(0<\varepsilon\leq1/4\). On \(I\), each of the eight scalar weights \(x^a(1-x)^bq_\varepsilon^c\) is bounded below by a positive constant depending only on \(\delta\), uniformly over \(\varepsilon\). All weighted summands are positive semidefinite there and sum to \(F_\varepsilon\), whose norm is uniformly bounded on \(I\). Thus \(\|\Sigma_{abc}(x)\|\leq C_I\) for all \(x\in I\). Every entry of \(\Sigma_{abc}\) is a polynomial of degree at most \(d\); applying Step 1 entrywise yields, for \(k=0,1,2\),

\[
\bigl|\Sigma_{abc,ij}^{(k)}(0)\bigr|\leq B,
\qquad B=C_RR^d,
\]

where \(C_R\) is independent of \(\varepsilon\), the certificate, and \(d\). We increase \(C_R\) as necessary without further comment.

**3. Zeros and the matrix positivity jet inequality.** At \(x=0\),

\[
F_\varepsilon(0)=\operatorname{diag}(0,\varepsilon),
\qquad q_\varepsilon(0)=\varepsilon^2/2>0.
\]

Positivity and the \((1,1)\) entry of the certificate identity force \(\Sigma_{0bc,11}(0)=0\) for all \(b,c\). Positive semidefiniteness forces their first columns, and hence their \((1,2)\) entries, to vanish at zero. Global nonnegativity of the scalar polynomials \(\Sigma_{0bc,11}\) also gives \(\Sigma_{0bc,11}'(0)=0\).

For any globally positive-semidefinite \(2\times2\) Hermitian polynomial \(S\) with \(S_{11}(0)=0\), the determinant inequality on the real line implies

\[
|S_{12}'(0)|^2\leq\tfrac12 S_{11}''(0)S_{22}(0).
\]

To see this, \(|S_{12}(x)|^2\leq S_{11}(x)S_{22}(x)\) for real \(x\); divide by \(x^2\) and let \(x\to0\), using \(S_{12}(0)=S_{11}(0)=S_{11}'(0)=0\). The \((2,2)\) entry at zero also implies \(\Sigma_{0b0,22}(0)\leq\varepsilon\) for each \(b\). It follows from Step 2 that

\[
|\Sigma_{0b0,12}'(0)|\leq\sqrt{\varepsilon B/2}.
\]

**4. A positivity restriction on the terms divisible by \(x\).** Set

\[
A=\Sigma_{100}(0)+\Sigma_{110}(0)\succeq0.
\]

Differentiate the \((1,1)\) certificate identity at zero. All terms with \(a=0\) have derivative zero in that entry, by Step 3. The terms with \(a=1,c=0\) contribute \(A_{11}\); those with \(a=c=1\) contribute a nonnegative scalar multiple of a positive-semidefinite \((1,1)\) entry. Consequently

\[
0\leq A_{11}\leq F_{\varepsilon,11}'(0)=\rho_\varepsilon\varepsilon.
\]

As \(A_{22}\leq2B\), positivity gives

\[
|A_{12}|\leq\sqrt{2\rho_\varepsilon\varepsilon B}.
\]

**5. Differentiate the off-diagonal entry.** Since \(F_{\varepsilon,12}'(0)=\rho_\varepsilon\geq1\), differentiating the \((1,2)\) certificate identity at zero and sorting the terms by \((a,c)\) gives four contributions:

- \((a,c)=(0,0)\): \(\Sigma_{000,12}'(0)+\Sigma_{010,12}'(0)\), bounded by \(2\sqrt{\varepsilon B/2}\);
- \((a,c)=(1,0)\): \(A_{12}\), bounded by \(\sqrt{2\rho_\varepsilon\varepsilon B}\);
- \((a,c)=(0,1)\): \(q_\varepsilon(0)(\Sigma_{001,12}'(0)+\Sigma_{011,12}'(0))\), bounded by \(\varepsilon^2B\); the derivatives of the scalar weights multiply zero off-diagonal values at zero;
- \((a,c)=(1,1)\): \(q_\varepsilon(0)(\Sigma_{101,12}(0)+\Sigma_{111,12}(0))\), bounded by \(\varepsilon^2B\).

As \(\rho_\varepsilon\) is bounded above on \((0,1/4]\), the triangle inequality yields a constant \(C_R'>0\), independent of \(d\) and \(\varepsilon\), such that

\[
1\leq C_R'\bigl(\sqrt{\varepsilon R^d}+\varepsilon^2 R^d\bigr).
\tag{*}
\]

**6. Extract the logarithmic coefficient.** If, for fixed \(R>R_0\) and fixed \(\eta>0\), infinitely many \(\varepsilon\downarrow0\) satisfied \(d_\varepsilon\leq(1-\eta)\log(1/\varepsilon)/\log R\), then the right side of (*) would be bounded by a constant times \(\varepsilon^{\eta/2}+\varepsilon^{1+\eta}\), tending to zero. This contradicts (*). Hence

\[
\liminf_{\varepsilon\downarrow0}\frac{d_\varepsilon}{\log(1/\varepsilon)}\geq\frac{1}{\log R}.
\]

Letting \(R\downarrow3+2\sqrt2\) proves the claim.

## Verification

A standalone standard-library script, `CHECKER.py`, verifies exact rational polynomial identities for the stated matrix family (including the determinant and first jets) for a collection of rational parameters, and tests the geometric constant and the stated bounding mechanism numerically. These finite diagnostics are not the proof of the uniform bound; the argument above supplies the analytic justification. The underlying existence and original unquantified divergence claims are cited from the source paper.

## Relationship to prior work

Jindal and Zalar (2026), Section 6.2 and the proof in Section 6.3, introduce precisely \(K_\varepsilon\) and \(F_\varepsilon\) and prove \(d_\varepsilon\to\infty\) by a compactness argument. The present result is exclusively the new *quantitative growth lower bound* for that already-known family. The proof replaces fixed-degree subsequence compactness with exponential polynomial evaluation bounds on the stable interval and a quantitative positive-matrix derivative inequality. The 2015 work of Zalar establishes general one-dimensional matrix Positivstellensätze, and Sun–Zalar (2025) studies degree-preserving certificates on a different degenerate set. Quantitative Putinar-type bounds for positive scalar or matrix polynomials on fixed sets with a positive margin do not imply the stated boundary-vanishing, moving-set result.

## Limitations

This is a lower bound only; no matching upper bound, sharp coefficient, exact value of \(d_\varepsilon\), or universal behavior for other collapsing families is proved. The parameter range is asymptotic \(\varepsilon\downarrow0\), not a finite-parameter explicit degree threshold. Earlier equivalent polynomial-approximation techniques may exist; publication priority has not been exhaustively established, and no independent audit has been performed.

## References

1. A. Jindal and A. Zalar, *Operator Fejér–Riesz Theorems with Gaps and Degree Bounds*, arXiv:2611.02967v1 (first publicly submitted 2026-11-02), especially §§6.2–6.3, https://arxiv.org/html/2611.02967v1.
2. A. Zalar, *Matrix Fejér–Riesz theorem with gaps*, arXiv:1503.06034 (2015), https://arxiv.org/abs/1503.06034.
3. S. Sun and A. Zalar, *Matrix Fejér–Riesz type theorem for a union of an interval and a point*, arXiv:2507.01357 (2025), https://arxiv.org/abs/2507.01357.
4. L. Baldi and L. Slot, *Degree bounds for Putinar's Positivstellensatz on the hypercube*, arXiv:2302.12558 (2023), https://arxiv.org/abs/2302.12558.
