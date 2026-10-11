# Exact one-parameter law for the illuminating center of every isosceles triangle

## Finding
For every nondegenerate isosceles triangle
\[
T_{a,h}=\operatorname{conv}\{(-a,0),(a,0),(0,h)\},\qquad a,h>0,
\]
write \(\lambda=h/a\). The planar illuminating center is
\[
P=(0,qh),
\]
where \(q\in(0,1/2)\) is the unique solution of
\[
\lambda q\tan(\pi q)=1.
\]
The altitude fraction \(q\) is strictly decreasing as the aspect ratio \(\lambda\) increases. Its endpoint behavior is
\[
q=\frac12-\frac{\lambda}{2\pi}+O(\lambda^2)\quad(\lambda\downarrow0),
\qquad
q\sim\frac1{\sqrt{\pi\lambda}}\quad(\lambda\to\infty).
\]
For the right-isosceles triangle \(\operatorname{conv}\{(0,0),(1,0),(0,1)\}\), one has \(\lambda=1\). If its center is \((t,t)\), then \(t=(1-q)/2\), hence
\[
t=0.308275698614655042256720655\ldots,
\]
which reproduces the numerical value reported by Finch.

## Assumptions and scope
The illuminating center here is the planar zero-height center obtained from the renormalized inverse-square potential. O'Hara identifies Shibata's illuminating center with the \(r^{-2}\)-center and proves uniqueness of \(r^{\alpha-m}\)-centers for convex bodies when \(\alpha\le1\); in the planar inverse-square case \(m=2\) and \(\alpha=0\). Finch records Shibata's triangle characterization: at the maximizing point \(P\), the three ratios \(\angle APB/|APB|\), \(\angle BPC/|BPC|\), and \(\angle CPA/|CPA|\) are equal.

The theorem concerns only isosceles triangles and the planar renormalized center. It does not assert a closed elementary expression for \(q\), nor does it treat a positive-height physical lamp model.

## Proof
Reflection in the symmetry altitude preserves \(T_{a,h}\) and its renormalized inverse-square potential. By uniqueness, the center is fixed by this reflection, so write it as \(P=(0,y)\), with \(0<y<h\), and put \(q=y/h\).

The subtriangle with base \(AB\) has area
\[
|APB|=ay=q\,ah=q|ABC|.
\]
Because the three angles about \(P\) sum to \(2\pi\), while the three subtriangle areas sum to \(|ABC|\), equality of Shibata's three angle-to-area ratios forces the common ratio to be \(2\pi/|ABC|\). Therefore
\[
\angle APB=2\pi q.
\]
On the other hand, symmetry gives
\[
\angle APB=2\arctan\!\left(\frac a y\right)
=2\arctan\!\left(\frac1{\lambda q}\right).
\]
Thus
\[
\arctan\!\left(\frac1{\lambda q}\right)=\pi q.
\]
The left side lies in \((0,\pi/2)\), so necessarily \(0<q<1/2\), and taking tangents yields
\[
\lambda q\tan(\pi q)=1.
\]
Conversely, the actual illuminating center must satisfy this equation, and the function \(q\mapsto\lambda q\tan(\pi q)\) is continuous and strictly increasing from \(0\) to \(+\infty\) on \((0,1/2)\). Hence the equation has exactly one solution and therefore determines the unique center.

Implicit differentiation gives
\[
\frac{dq}{d\lambda}
=-\frac{q\tan(\pi q)}{\lambda\left(\tan(\pi q)+\pi q\sec^2(\pi q)\right)}<0.
\]
For \(\lambda\downarrow0\), write \(q=1/2-\varepsilon\) and use \(\tan(\pi q)=\cot(\pi\varepsilon)\); expansion gives \(\varepsilon=\lambda/(2\pi)+O(\lambda^2)\). For \(\lambda\to\infty\), the defining equation forces \(q\to0\), and \(\tan(\pi q)\sim\pi q\) gives \(q\sim(\pi\lambda)^{-1/2}\).

For \(\operatorname{conv}\{(0,0),(1,0),(0,1)\}\), use its hypotenuse as the base. Then \(\lambda=1\), and a point a fraction \(q\) of the altitude from the hypotenuse toward the right-angle vertex has coordinates \(((1-q)/2,(1-q)/2)\). The unique root gives the displayed value of \(t\).

## Verification
The accompanying `verify.py` independently bisects the scalar equation, verifies the published right-isosceles decimal, checks the angle-to-area identity on several aspect ratios, and checks the predicted monotonic ordering. These finite checks are diagnostic only; uniqueness, monotonicity, and asymptotics are proved analytically above.

## Relationship to prior work
O'Hara's renormalized-potential framework identifies the planar illuminating center as an \(r^{-2}\)-center and supplies the needed uniqueness for convex bodies. Finch later records Shibata's equal angle-to-area characterization and gives a decimal solution for a right-isosceles triangle, but no inspected source states the dimensionless equation \(\lambda q\tan(\pi q)=1\), its all-isosceles uniqueness reduction, or the resulting monotone aspect-ratio law.

The closest potentially covering source is Shibata's 2009 unpublished manuscript cited by both O'Hara and Finch. Its historical URL was not retrievable during this check, so whether it contains this isosceles-family reduction remains a residual originality risk.

## Limitations
The result does not claim novelty for the general definition, existence, uniqueness, or Shibata angle/area characterization; those are prior inputs. It only claims the exact one-parameter reduction and its consequences for the isosceles family. The original Shibata manuscript could not be materially inspected. The first exact public timestamp verified among the inspected sources is O'Hara's arXiv posting of 2010-08-16; Shibata's cited manuscript is labeled only by the year 2009 in the accessible references, so no day-level public date is asserted for it.

## References
1. J. O'Hara, *Renormalization of potentials and generalized centers*, arXiv:1008.2731, first posted 2010-08-16; later Adv. Appl. Math. 48 (2012), 365-392.
2. S. R. Finch, *In Limbo: Three Triangle Centers*, arXiv:1406.0836, first posted 2014-06-03.
3. K. Shibata, *Where should a streetlight be placed in a triangle-shaped park? Elementary integro-differential geometric optics*, unpublished manuscript (cited as 2009 by Finch); historical URL cited in the literature, unavailable during this check.
