# Sharp negative-parameter validity of the ratio-logarithmic copula

## Finding

For real \(\alpha>-1\), define \(C_0(x,y)=xy\), and for \(\alpha\ne0\) let the ratio-logarithmic formula be
\[
 C_\alpha(x,y)=xy\,\frac{\log(1+\alpha x)\log(1+\alpha y)}{\log(1+\alpha)\log(1+\alpha xy)},\qquad 0<x,y\le1,
\]
with its continuous zero-coordinate extensions. There is a **unique** \(s_*>0\) satisfying
\[
 (e^{s_*}-1)\bigl((s_*-1)e^{s_*}+1\bigr)=s_*^2.
\]
Put \(t_*=1-e^{-s_*}\). Then
\[
 \boxed{C_\alpha\text{ is a bivariate copula if and only if }\alpha\ge-t_*.}
\]
Numerically, \(s_*=0.77612669196841553859\ldots\) and \(t_*=0.53981499794399051339\ldots\). At \(\alpha=-t_*\), the mixed density vanishes at the upper-right corner and is positive throughout the open square. For every \(-1<\alpha<-t_*\), it is negative on an open neighborhood inside that corner. Consequently, the previously conjectural negative interval is determined sharply; in particular the valid interval extends strictly below \(-1/2\).

## Assumptions and scope

All logarithms are natural and the formula is understood as a real-valued function on \([0,1]^2\). The logarithmic expression has a real, finite interior meaning for \(\alpha>-1\); the value \(\alpha=0\) is defined by its continuous parameter limit. At \(\alpha=-1\) the expression does not extend to a copula: its interior limit as \(\alpha\downarrow-1\) is zero, incompatible with uniform boundary margins. For \(\alpha<-1\) the real logarithms cease to be defined on the whole unit square. No assertion is made about alternative complex-valued or reparameterized definitions.

A copula means a grounded, two-increasing function with unit uniform margins. For a smooth function on the open square and continuous on the closed square, it suffices to check the four boundary identities and nonnegative mixed density on the interior.

## Proof

**1. Common density identity.** For \(\alpha\ne0\) define the positive function
\[
 H_\alpha(z)=\frac{\log(1+\alpha z)}{\alpha z},\qquad H_\alpha(0)=1,
\]
and write \(g_\alpha(z)=z\,\frac{d}{dz}\log H_\alpha(z)\), with \(g_\alpha(0)=0\). Cancellation of \(\alpha z\) factors gives
\[
 C_\alpha(x,y)=xy\frac{H_\alpha(x)H_\alpha(y)}{H_\alpha(1)H_\alpha(xy)}.
\]
Set \(q=xy\). Logarithmic differentiation twice gives, for \(x,y>0\),
\[
 \boxed{\frac{xy}{C_\alpha(x,y)}\frac{\partial^2C_\alpha}{\partial x\partial y}
 =\bigl[1+g_\alpha(x)-g_\alpha(q)\bigr]\bigl[1+g_\alpha(y)-g_\alpha(q)\bigr]-qg_\alpha'(q).}\tag{1}
\]
The boundary identities follow by \(H_\alpha(0)=1\) and cancellation at \(x=1\), \(y=1\); continuity holds for \(\alpha>-1\).

**2. Positive parameters.** Set \(u=\alpha z>0\) and \(L=\log(1+u)\). Then
\[
 1+g_\alpha(z)=a_+(u):=\frac{u}{(1+u)L}.
\]
The elementary inequalities \(u/(1+u)<L<u\) give \(0<a_+(u)<1\) and
\[
 a_+'(u)=\frac{L-u}{(1+u)^2L^2}<0.
\]
Thus \(g_\alpha\) is decreasing, takes values in \((-1,0)\), and \(g_\alpha'(q)<0\). Since \(q\le x,y\), each factor in (1) is at least \(1+g_\alpha(x)>0\) or \(1+g_\alpha(y)>0\). The last term in (1) is positive. The density is therefore positive for every \(\alpha>0\). For \(\alpha=0\), \(C_0=xy\).

**3. Negative parameters: universal sufficiency.** Write \(\alpha=-t\), with \(0<t<1\), and \(u=tz\), \(s=-\log(1-u)\). The analogous function is
\[
 1+g_{-t}(z)=a_-(u)=\frac{u}{(1-u)[-\log(1-u)]}=\frac{e^s-1}{s}=\int_0^1e^{sr}\,dr.
\]
It is strictly increasing in \(z\), so \(g_{-t}(x)\ge g_{-t}(q)\) and \(g_{-t}(y)\ge g_{-t}(q)\), and both bracketed factors in (1) are at least one. Moreover,
\[
 qg_{-t}'(q)=F\bigl(-\log(1-tq)\bigr),\qquad
 F(s)=(e^s-1)\int_0^1 r e^{sr}\,dr.
\]
The function \(F\) is continuous and strictly increasing from \(F(0)=0\) to \(+\infty\): both positive factors strictly increase for \(s>0\). In particular
\[
 qg_{-t}'(q)\le F\bigl(-\log(1-t)\bigr).
\]
If \(F(-\log(1-t))\le1\), identity (1) is nonnegative at every interior point, so the model is a copula. Uniqueness of the solution \(F(s_*)=1\) follows from strict monotonicity. Evaluating the elementary integral yields
\[
 F(s)=\frac{(e^s-1)((s-1)e^s+1)}{s^2}.
\]
Hence the sufficiency condition is exactly \(t\le t_*\). Also \(F(\log2)=(2\log2-1)/(\log2)^2<1\), because \((1-\log2)^2>0\), proving \(t_*>1/2\) without numerical computation.

**4. Necessity and the sharp boundary.** The right-hand side of (1) has a continuous extension to \((x,y)=(1,1)\) for each \(0<t<1\). At that corner, both factors equal one and
\[
 \frac{\partial^2 C_{-t}}{\partial x\partial y}(1,1)
 =1-F\bigl(-\log(1-t)\bigr).
\]
If \(t>t_*\), this number is negative. By continuity, the mixed derivative is negative at some interior points close to \((1,1)\), which contradicts two-increasingness. For \(t=t_*\), the density is zero at the corner, but for \(0<x,y<1\) we have \(xy<1\), hence \(qg_{-t}'(q)<1\), and (1) is strictly positive. This proves necessity, inclusion of the boundary, and its uniqueness. Together with steps 2–3 and the real-definition restrictions, it proves the theorem.

## Verification

The standalone `check.py` (Python plus `mpmath`) independently evaluates both the original two-variable formula and the factored mixed derivative at deterministic interior points, tests the corner obstruction and positive-region samples, and calculates the unique scalar root at 70-digit precision. It passed **135 supporting checks**. Reproduce with `python check.py` in a directory containing that file. The numerical grid is *not* the proof of continuum-wide nonnegativity or root uniqueness; those follow from the monotonicity and identities above. The interval of displayed decimal digits is numerical, whereas the exact defining equation fully specifies the boundary.

## Relationship to prior work

Chesneau (2023), *Theoretical Advancements on a Few New Dependence Models Based on Copulas with an Original Ratio Form*, Section 6, introduced this exact ratio-logarithmic formula. Its Proposition 5 proved copula validity for \(\alpha\ge0\); the paper explicitly left negative-parameter validity unresolved, conjecturing the region around \(\alpha=-1/2\) based on numerical evidence. The present result confirms a negative region, sharpens the conjectural endpoint to \(-t_*\), and establishes the converse invalidity beyond it. The density formula (1), exponential-integral monotonicity and corner obstruction are the new analytical mechanism.

A distinct 2023 study by Chesneau on ratio-type constructions uses functions such as \(1+a\log(x)\log(y)\) *in a different denominator*; its copulas do not imply the classification here. The 2024 paper by El Ktaibi, Bentoumi and Mesfioui studies broad ratio forms such as \(uv/[1-\theta f(u)g(v)]\); no exact negative parameter cutoff for the present nonseparable ratio-logarithmic formula was established from the material accessible during comparison. General copula positivity criteria are acknowledged and used, not presented as discoveries.

## Limitations

This theorem concerns only the real-valued bivariate ratio-logarithmic family as defined above, not its multivariate extensions, parameter estimation, or optimal dependence bounds. Historical priority is subject to any later publication or difficult-to-index source containing the same sharp threshold; one broadly related 2024 paper was available only through its abstract and bibliographic description, not fully inspected. The analytic proof does not depend on that paper. Independent external mathematical validation has not been performed.

## References

1. C. Chesneau, *Theoretical Advancements on a Few New Dependence Models Based on Copulas with an Original Ratio Form*, **Modelling** 4 (2023), 102–132, Section 6 and Table 7. First published 29 March 2023. DOI: https://doi.org/10.3390/modelling4020008 . Full text: https://www.mdpi.com/2673-3951/4/2/8 .
2. C. Chesneau, *A Collection of Two-Dimensional Copulas Based on an Original Parametric Ratio Scheme*, **Symmetry** 15 (2023), 977. DOI: https://doi.org/10.3390/sym15050977 .
3. F. El Ktaibi, R. Bentoumi, and M. Mesfioui, *On the Ratio-Type Family of Copulas*, **Mathematics** 12 (2024), 1743. DOI: https://doi.org/10.3390/math12111743 .
