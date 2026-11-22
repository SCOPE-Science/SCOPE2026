# A semicubical period-two cusp, a resonant continuum, and an exact sink window in an affine cubic map

## Finding

Consider the real polynomial map
\[
F_{c,b,m}(x,y)=\bigl(y,(c+x)y^2+bx+m\bigr),\qquad c\ne0,\quad b,m\in\mathbb R.
\]
It is a normalized affine-coefficient member of the non-invertible planar polynomial family investigated by Wei, Zhang, Zhang, and Grebogi [1]. A *primitive two-cycle* is an unordered pair of distinct points \((x,y)\) and \((y,x)\) interchanged by \(F\). The following is a complete real-plane classification, not a restriction to a trapping square.

Put
\[
L=b+c^2-1,\qquad N=c(b-1)-m.
\]

**Theorem (exact primitive-two classification and Floquet data).**

1. If \(L\ne0\), put
\[
S=\frac NL,\qquad P=b-1-cS,\qquad \Delta=(S+2c)^2-4L.
\]
There is exactly one primitive real two-cycle if \(\Delta>0\), with coordinates
\[
x_\pm=\frac{S\pm\sqrt\Delta}{2},\qquad
\{(x_+,x_-),(x_-,x_+)\}.
\]
There are none if \(\Delta\le0\). The equality case gives a fixed point, not a primitive two-cycle. Equivalently, for \(L<0\) there is exactly one such cycle for every real \(m\); for \(L>0\), there is exactly one precisely when
\[
\bigl(N+2cL\bigr)^2>4L^3.
\]
The last condition defines an exact semicubical exclusion cusp in the coordinates \((L,N+2cL)\).

2. If \(L=0\) and \(N\ne0\), there is no primitive two-cycle. If \(L=N=0\) (equivalently \(b=1-c^2\) and \(m=-c^3\)), there is a whole one-parameter family, and it is complete:
\[
\bigl\{\{(-c,t),(t,-c)\}:t\in\mathbb R,\ t\ne-c\bigr\}.
\]
The excluded value \(t=-c\) is a fixed point.

3. For the unique primitive two-cycle in part 1, the two-step Jacobian has characteristic polynomial \(\lambda^2-T\lambda+D\), where
\[
D=(b+c^2)S^2+2cS+1,\qquad
T=1+D-L\Delta.
\]
It is a locally exponentially attracting sink if and only if
\[
L>0,\quad \Delta>0,\quad D<1,\quad 2(1+D)>L\Delta.
\]
In particular, every primitive two-cycle for \(L<0\) has a real multiplier strictly greater than one.

4. On the explicit nondegenerate slice \(c=1,\ b=1/2\), a primitive two-cycle is a hyperbolic sink **exactly** for
\[
\boxed{-\frac12<m<\frac{1-\sqrt2}{2}.}
\]
At \(m=-1/2\), the two-step multipliers are \(e^{\pm i\pi/3}\); at \(m=(1-\sqrt2)/2\), the two points merge at a fixed point and no primitive two-cycle remains. Outside the displayed interval, any existing primitive two-cycle is not an attracting sink.

5. On the resonant slice \(c=1,\ b=0,\ m=-1\), the family is \(\{(-1,t),(t,-1)\}\), and the two return multipliers are exactly \(1\) and \(t^2\). Its primitive cycles are normally contracting for \(|t|<1\) and normally expanding for \(|t|>1\), with no assertion of attraction to an *individual* cycle because the tangent multiplier equals one.

## Assumptions and scope

The ambient phase space is the full real plane. All assertions hold for every real \(c\ne0\) and every real \(b,m\), except the two named slices that are stated with their exact fixed parameters. Distinct cycles are counted modulo the interchange of their two phase points; fixed points do not count. Floquet multipliers are eigenvalues of \(DF^2\) evaluated at either point of the cycle. "Sink" means both multiplier moduli are strictly below one, so local exponential stability follows from differentiability. No global basin or higher-period classification is asserted.

## Proof

**Complete orbit equations.** If \((x,y)\) is a two-cycle point then necessarily \(F(x,y)=(y,x)\) and \(F(y,x)=(x,y)\). Writing
\[
A=(c+x)y^2+(b-1)x+m,\qquad
B=(c+y)x^2+(b-1)y+m,
\]
both conditions are precisely \(A=B=0\). Direct factorization gives
\[
A-B=(x-y)\bigl[(b-1)-xy-c(x+y)\bigr].
\]
For a primitive cycle \(x\ne y\), put \(S=x+y\) and \(P=xy\). The difference equation forces \(P=b-1-cS\). The sum equation is
\[
A+B=c(S^2-2P)+PS+(b-1)S+2m=2(LS-N).
\]
Thus \(LS=N\). Conversely, any distinct real roots of \(z^2-Sz+P=0\) with these two equations satisfy both orbit equations; this supplies the necessary *and sufficient* global reduction.

When \(L\ne0\), the sum \(S\) and product \(P\) are uniquely determined. The quadratic has two distinct real roots exactly when \(\Delta=S^2-4P=(S+2c)^2-4L>0\), and these two roots give a single unordered cycle. Multiplying by \(L^2\) proves the cusp condition
\[
L^2\Delta=(N+2cL)^2-4L^3.
\]
If \(L<0\) then \(\Delta=(S+2c)^2-4L>0\) automatically. If \(L=0\), the sum equation requires \(N=0\); otherwise no primitive cycle is possible. At \(L=N=0\), the product equation becomes
\[
(x+c)(y+c)=P+cS+c^2=0.
\]
Every solution with one coordinate \(-c\) is indeed interchanged, since \(F(-c,t)=(t,-c)\) and \(F(t,-c)=(-c,t)\). This proves completeness of the resonant family.

**Exact return spectrum.** The one-step derivative is
\[
DF(x,y)=\begin{pmatrix}0&1\\y^2+b&2(c+x)y\end{pmatrix}.
\]
Multiplication at the two cyclic points gives
\[
\begin{aligned}
\det DF^2&=(x^2+b)(y^2+b)
=P^2+b(S^2-2P)+b^2,\\
\operatorname{tr}DF^2&=S^2-2P+2b+4(c+x)(c+y)P.
\end{aligned}
\]
On any primitive cycle, \((c+x)(c+y)=P+cS+c^2=L\). Substituting \(P=b-1-cS\) gives the stated formula for \(D\), and the exact identity \(1-T+D=L\Delta\).

For a real quadratic \(\lambda^2-T\lambda+D\), both zeros lie strictly within the open unit disk if and only if the three strict Schur inequalities \(1-D>0\), \(1-T+D>0\), and \(1+T+D>0\) hold. Substituting \(1-T+D=L\Delta\) proves the stated sink criterion. If \(L<0\), then \(1-T+D<0\), and the real characteristic polynomial is negative at \(\lambda=1\), positive for sufficiently large positive \(\lambda\), so some real multiplier is strictly greater than one.

**Sharp explicit stability interval.** With \(c=1,b=1/2\), write
\[
S=-1-2m,\quad \Delta=S^2+4S+2,\quad
T=1+S^2,\quad D=\frac{3S^2+4S+2}{2}.
\]
Here \(1+T+D=(5S^2+4S+6)/2>0\) for every real \(S\), since the quadratic has negative discriminant and positive leading coefficient. The condition \(D<1\) is exactly \(-4/3<S<0\). The condition \(\Delta>0\) is exactly \(S<-2-\sqrt2\) or \(S>-2+\sqrt2\). Their intersection is \(-2+\sqrt2<S<0\), which becomes the displayed sharp interval in \(m\). At \(S=0\), \(D=T=1\), so the return eigenvalues solve \(\lambda^2-\lambda+1=0\); at \(S=-2+\sqrt2\), \(\Delta=0\) and the two phase coordinates coincide. The global necessity of the inequalities proves the "only if" direction, including all other primitive cycles on this slice.

**Resonant normal dynamics.** At \((c,b,m)=(1,0,-1)\), direct differentiation of \(F^2\) at \((-1,t)\) yields
\[
DF^2(-1,t)=\begin{pmatrix}t^2&0\\-2(1+t)t^2&1\end{pmatrix}.
\]
Thus its multipliers are \(t^2\) and \(1\). The latter is the tangent multiplier along the continuum of periodic points. This proves the normal contracting and expanding assertions without claiming asymptotic convergence to a particular periodic pair.

## Verification

Run `python verify.py` from the unpacked finding directory (Python 3 with SymPy). The included script checks the subtraction and sum identities, the discriminant cusp, the return trace and determinant in symmetric coordinates, the Schur boundary polynomials, exact resonant interchange and normal multiplier, and several exact sample phase points. Its expected last line is `AFFINE_CUBIC_PERIOD_TWO_VERIFY_OK`. Symbolic checks support the identities; quantifiers and stability-range implications are supplied by the preceding proof rather than inferred from finite samples.

## Relationship to prior work

Wei, Zhang, Zhang and Grebogi [1] define the same polynomial family, derive its Jacobian, and prove existence of horseshoe invariant sets with symbolic dynamics under specified parameter constraints. Their full accessible article text, including its affine section and numerical experiments, does not give this complete full-plane primitive-two census, its semialgebraic cusp, the continuum at \(L=N=0\), or the exact attracting interval above. Their symbolic two-shift does imply a two-cycle *inside its horseshoe* when its hypotheses hold; existence alone is not claimed as new here. The classification proved here spans all real \(b,m\) in the normalized affine family and includes parameters outside those horseshoe hypotheses. Existing classifications for other planar quadratic or piecewise maps do not yield this formula by substitution: their orbit equations are different.

## Limitations

No global attractor claim, structural-stability assertion at neutral endpoints, nonlinear Neimark–Sacker bifurcation claim, or full high-period census is made. The proof is a self-review, not independent certification. Publication-priority comparisons are limited to the named originating work and searched/indexed related literature; unindexed equivalent results remain possible. The earliest publicly listed date is November 3, 2024 in the author institution's record [2], while the journal page itself reports November 18, 2024, an unresolved bibliographic difference that does not affect the algebraic proof.

## References

[1] Z. Wei, L. Zhang, X. Zhang, and C. Grebogi, *A class of non-invertible chaotic polynomial maps and Smale horseshoes of new types*, Discrete and Continuous Dynamical Systems - B **30** (2025), 2258–2276, DOI: https://doi.org/10.3934/dcdsb.2024163. Accessible full article text: https://www.researchgate.net/publication/385910515_A_class_of_non-invertible_chaotic_polynomial_maps_and_Smale_horseshoes_of_new_types.

[2] University of Aberdeen institutional record for [1], early online date 2024-11-03: https://abdn.elsevierpure.com/en/publications/a-class-of-non-invertible-chaotic-polynomial-maps-and-smale-horse/.
