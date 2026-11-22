# Sharp worst-jump switching for two-mode Müntz projection

## Finding

For each real exponent \(q>0\), let \(\Pi_q\) denote unweighted Lebesgue-\(L^2(0,1)\) orthogonal projection onto the two-dimensional Müntz space \(\operatorname{span}\{1,x^q\}\). If \(V(f)=|Df|((0,1))\) is ordinary distributional total variation for real \(f\in BV(0,1)\), then the exact sharp squared residual norm is
\[
C_q^2=\sup_{V(f)>0}\frac{\|f-\Pi_q f\|_2^2}{V(f)^2}
=F_q(s_q),\qquad
F_q(s)=s(1-s)-\frac{2q+1}{q^2}\bigl(s-s^{q+1}\bigr)^2.
\]
For \(q>1\), \(s_q\) is the **unique** zero in \((0,1/2)\) of
\[
1-(2+2a_q)s+2a_q(q+2)s^{q+1}-2a_q(q+1)s^{2q+1}=0,
\qquad a_q=(2q+1)/q^2.
\]
For \(0<q<1\), the same equation has a **unique** zero in \((1/2,1)\), denoted \(s_q\). All nonconstant equality cases, and only these, are \(f(x)=b+c\mathbf1_{(s_q,1)}(x)\), with \(b\in\mathbb R\) and \(c\ne0\).

At the classical linear exponent \(q=1\), exactly two knots tie:
\[
s_\pm=\frac{1\pm1/\sqrt3}{2},\qquad C_1^2=\frac1{12}.
\]
At this exponent the equality cases are the individual single jumps at either \(s_-\) or \(s_+\), again up to scaling and additive constants; **nontrivial mixtures of the two jumps are not extremizers**. Thus the optimal knot changes discontinuously from \(s_+\) to \(s_-\) when \(q\) increases across one. The squared sharp constant is continuous but has distinct one-sided derivatives:
\[
\left.\frac{d}{dq}C_q^2\right|_{q=1-}
=\frac19+s_+^2\log s_+=-0.03655418816799499\ldots,
\]
\[
\left.\frac{d}{dq}C_q^2\right|_{q=1+}
=\frac19+s_-^2\log s_-=0.04169625213133872\ldots.
\]
The asymmetric power deformation therefore produces a strict local minimum and an upward cusp at the classical exponent, with a discontinuous change in the worst located discontinuity.

## Assumptions and scope

The domain is \((0,1)\) with ordinary, unweighted Lebesgue measure and real-valued distributional \(BV\) functions identified almost everywhere. Variation excludes the endpoints. Projection is the unique orthogonal \(L^2\) projection, rather than pointwise interpolation, and \(q\) ranges over all positive real exponents (not just integers). Norming single jumps have amplitude one before affine rescaling. No statement concerns higher-dimensional Müntz spaces or other \(L^p\) norms.

## Proof

**Step 1: exact projection of a jump.** Put \(h_s=\mathbf1_{(s,1)}\) and \(v_q(x)=x^q-1/(q+1)\). Direct integration yields
\[
\|h_s-\textstyle\int_0^1 h_s\|_2^2=s(1-s),\quad
\langle h_s,v_q\rangle=\frac{s-s^{q+1}}{q+1},\quad
\|v_q\|_2^2=\frac{q^2}{(2q+1)(q+1)^2}.
\]
Projection onto the orthogonal pair \(1,v_q\) gives \(\|(I-\Pi_q)h_s\|_2^2=F_q(s)\) as stated. In particular, \(F_q(0)=F_q(1)=0\) and it is positive in the interior because a nonconstant jump cannot lie in the continuous Müntz space.

**Step 2: reduction from all bounded-variation data and equality.** Write the distributional derivative as a finite signed measure \(\mu=Df\) and \(f=b+\int_{(0,1)}h_s\,d\mu(s)\) almost everywhere. Since \(\Pi_q\) reproduces constants, the Bochner integral identity and the triangle inequality show
\[
\|(I-\Pi_q)f\|_2
\le\int\|(I-\Pi_q)h_s\|_2\,d|\mu|(s)
\le \sqrt{\max_sF_q(s)}\,|\mu|((0,1)).
\]
A jump at a maximizing knot attains the norm. If there is only one maximizing knot, equality forces \(\mu\) to be concentrated there. When \(q=1\) there are two candidate knots, but their residual images are not proportional: each residual has an unavoidable jump at its own knot while the projected part is continuous. Equality in the Hilbert-space triangle inequality therefore excludes any measure placing nonzero mass at both knots.

**Step 3: choice of winning half.** Write
\[
G_q(s)=\frac{1-s^q}{1-s}=q\int_0^1\bigl(s+(1-s)t\bigr)^{q-1}dt.
\]
This is strictly increasing in \(s\) when \(q>1\) and strictly decreasing when \(0<q<1\). For \(0<s<1/2\), the two subtracted squares in \(F_q(s)\) and \(F_q(1-s)\) are respectively \(s^2(1-s)^2G_q(s)^2\) and \(s^2(1-s)^2G_q(1-s)^2\). Therefore \(F_q(s)>F_q(1-s)\) for \(q>1\), and the inequality reverses for \(q<1\). The global worst knot must lie strictly on the asserted side.

**Step 4: uniqueness on the left when \(q>1\).** Differentiation gives
\[
F_q'(s)=1-(2+2a_q)s+2a_q(q+2)s^{q+1}-2a_q(q+1)s^{2q+1}.
\]
Its derivative \(F_q''\) is a nonzero quadratic polynomial in \(s^q\), and thus has at most two positive zeros. Rolle's theorem makes \(F_q'\) have at most three distinct positive zeros. Moreover \(F_q'(0+)=1\), \(F_q'(1/2)<0\), and \(F_q'(1)=-1\). With \(u_q=2^{-1/q}>1/2\), exact substitution gives
\[
F_q'(u_q)=1-2^{-1/q}\left(1+\frac{q+1}{2q^2}\right)>0.
\]
For the final strict inequality set \(z=1/q\in(0,1)\); \(2^z-1-(z+z^2)/2\) is strictly concave, vanishes at \(0,1\), and therefore is positive between them (its second derivative is at most \(2(\log2)^2-1<0\)). Hence \(F_q'\) has one zero in each of \((0,1/2)\), \((1/2,u_q)\), and \((u_q,1)\), and no more. The single left critical point is the unique left maximum; Step 3 makes it globally unique.

**Step 5: uniqueness on the right when \(0<q<1\).** For \(s\ge1/2\), put \(v=s^q\) and write
\[
\frac{F_q'(s)}s=H_q(v)=v^{-1/q}-2-2a_q(1-v)\bigl(1-(q+1)v\bigr).
\]
Here
\[
H_q''(v)=\frac{q+1}{q^2}\bigl(v^{-1/q-2}-4(2q+1)\bigr)<0,
\qquad 2^{-q}\le v\le1.
\]
Indeed, \(v^{-1/q-2}\le2^{1+2q}=2\cdot4^q\le2(1+3q)<4(2q+1)\), where \(4^q\le1+3q\) follows by convexity of the exponential on \([0,1]\). Finally \(H_q(2^{-q})>0\) (equivalently \(F_q'(1/2)>0\)) and \(H_q(1)=-1\). Strict concavity makes the positive superlevel set a single initial interval, hence there is exactly one root on \((1/2,1)\), a strict maximum. Step 3 excludes the other half.

**Step 6: the cusp and its slopes.** For \(q=1\), set \(u=s(1-s)\). Then \(F_1(s)=u-3u^2\), maximized exactly when \(u=1/6\), giving the two stated knots and squared norm. The strict maximizers on the appropriate sides tend to \(s_+\) as \(q\uparrow1\) and to \(s_-\) as \(q\downarrow1\) by compactness and uniqueness. Differentiating \(F_q\) with respect to \(q\) and evaluating at either optimum at \(q=1\) gives
\[
\partial_qF_q(s)|_{q=1}=\frac19+s^2\log s.
\]
The standard envelope argument then yields the stated one-sided derivatives. To see rigorously that the right slope exceeds the left, use the strict increase, in \(s\), of \(\partial_qG_q(s)|_{q=1}=\int_0^1[1+\log(s+(1-s)t)]dt\) in the reflection comparison of Step 3. The two derivatives have the stated opposite signs (also directly bounded by the log series around the displayed algebraic knots).

## Verification

The accompanying standalone script `checker.py` independently integrates the piecewise jump residual, compares it with the projection formula, brackets and bisects the favored-side stationary root, checks finite point grids for thirteen exponents, and confirms the one-sided cusp numerically. Its exact monomial integrations and numerical tests are reproducibility checks; neither the grid nor numerical bisection substitutes for the global analytic proof in Steps 3–5. Run with `python3 checker.py` using the standard library.

## Relationship to prior work

Borwein, Erdélyi and Zhang (1994) provide the underlying Müntz–Legendre orthogonalization and Markov inequalities for general exponent sequences. Ludkowski (first arXiv version May 31, 2016) studies Müntz-space approximation, smoothness classes, and Schauder bases, under conditions distinct from the present worst-case \(BV\) problem. Both give context but their inspected results do not imply sharp jump positions or their switching law. The ordinary linear-exponent \(q=1\) squared constant \(1/12\) is an already understood special case of the classical Legendre projection; it is included here to formulate and prove the two-sided exponent transition, **not claimed as a new standalone result**. Cui–Xu (2024) investigates Müntz–Legendre projection errors for weighted Sobolev classes; its accessible abstract is insufficient to determine full-paper overlap with this variation-endpoint classification, an explicit residual priority risk.

## Limitations

The result is restricted to the two-mode space with a constant and one positive power, real interval \(BV\), and unweighted \(L^2\) error. No optimality over all possible two-dimensional approximation subspaces is asserted. The single-root formulas are implicit for general \(q\), though they are uniquely specified with exact brackets. This is a mathematical proof and self-review only; no independent audit has been performed. Full inspection of the 2024 Cui–Xu article was unavailable, so that potentially relevant source remains a named historical-priority uncertainty.

## References

- P. Borwein, T. Erdélyi and J. Zhang, “Müntz systems and orthogonal Müntz–Legendre polynomials,” *Trans. Amer. Math. Soc.* 342 (1994), 523–542. https://doi.org/10.2307/2154639.
- P. Borwein and T. Erdélyi, “Müntz spaces and Remez inequalities,” *Bull. Amer. Math. Soc.* 32 (1995), 38–42. https://arxiv.org/abs/math/9501225.
- S. V. Ludkowski, “Approximation in Müntz spaces of \(L_p\) functions for \(1<p<\infty\) and bases,” first public arXiv version May 31, 2016. https://arxiv.org/abs/1605.09665.
- T. Cui and C. Xu, “Müntz Legendre polynomials: Approximation properties and applications,” *Math. Comp.* 94 (2025), 1377–1410, electronic publication June 7, 2024. https://doi.org/10.1090/mcom/3987.
