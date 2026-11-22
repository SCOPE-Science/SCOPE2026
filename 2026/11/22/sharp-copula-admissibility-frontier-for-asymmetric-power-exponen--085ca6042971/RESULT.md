# Sharp copula-admissibility frontier for asymmetric power-exponential survival laws

## Finding

For any \(a,b>0\) and \(\phi\ge0\), consider the bivariate function
\[
C_{a,b,\phi}(u,v)=u+v-1+(1-u)(1-v)
\exp\!\left[-\phi\{-\log(1-u)\}^{a}\{-\log(1-v)\}^{b}\right],\quad (u,v)\in[0,1]^2,
\]
where endpoint values are assigned by continuity. The function is a copula **if and only if** either \(\phi=0\), or \(a,b\ge1\) and
\[
0<\phi\le\Phi(a,b):=
\frac{(a+b-1)^{2(a+b-1)}}
{a^{2a}b^{2b}(a-1)^{a-1}(b-1)^{b-1}}.
\]
Here \(0^0=1\) in the continuous-extension convention. This criterion includes both endpoints. For every \(0<a<1\) or \(0<b<1\), every positive coupling \(\phi\) fails to define a copula. In contrast, \(\Phi(2,2)=729/256\) and \(\Phi(1,3)=1/4\). In particular, genuine asymmetric cases with \(a\ne b\) and \(a,b\ge1\) do exist.

## Assumptions and scope

The parameters \(a,b\) are arbitrary finite positive real numbers, not only integers. The coupling \(\phi\) is a finite nonnegative real number. \(C_{a,b,\phi}\) is a candidate cumulative copula, not a survival copula; its joint survival probability is \(1-u-v+C_{a,b,\phi}(u,v)\). A copula means a grounded continuous two-increasing function with uniform one-dimensional margins. Nonnegativity of the mixed interior derivative is equivalent to two-increasingness here because the candidate is continuous on the closed square and smooth on the open square. The independent \(\phi=0\) case is valid for every \(a,b>0\).

## Proof

For \(u,v\in(0,1)\), write \(x=-\log(1-u)>0\), \(y=-\log(1-v)>0\), and \(t=\phi x^a y^b\). Differentiating the joint survival term twice gives
\[
\partial_{uv}C_{a,b,\phi}(u,v)=
 e^{-t}\left[\left(1+\frac{at}{x}\right)
\left(1+\frac{bt}{y}\right)-\frac{ab t}{xy}\right]
=\frac{e^{-t}}{xy}\,H(x,y),
\]
where
\[
H(x,y)=(x+at)(y+bt)-ab t
=xy+at(y-b)+bt x+ab t^2.
\]
All factors outside \(H\) are positive, so validity is equivalent to \(H(x,y)\ge0\) for all \(x,y>0\). The four boundary conditions are immediate from the original expression: \(C(0,v)=C(u,0)=0\) and \(C(1,v)=v\), \(C(u,1)=u\).

**Necessity of both exponents being at least one.** Fix \(\phi>0\). If \(a<1\), choose any \(0<y<b\) and let \(x\downarrow0\). The leading term of \(H\) is \(\phi a y^b(y-b)x^a\), which is strictly negative. Indeed \(xy=o(x^a)\), \(bt x=o(x^a)\), and \(ab t^2=o(x^a)\), for \(t=\phi x^a y^b\). Hence \(H<0\) at interior points sufficiently near \(x=0\). Exchanging coordinates excludes \(b<1\). These failures remain even for arbitrarily small positive \(\phi\).

**Sharp bound for \(a,b\ge1\).** Put \(m=a+b-1\ge1\). For any \(\phi>0\), introduce positive coordinates \(r=x/(at)\) and \(s=y/(bt)\). The defining identity for \(t\) becomes
\[
 t^{m}=\{\phi a^a b^b r^a s^b\}^{-1},
 \qquad x=art,\quad y=bst.
\]
Conversely these formulas produce one and only one positive \((x,y)\) for every \((r,s)\in(0,\infty)^2\), so there is no loss in the global search. We have
\[
H=ab t\,\{t(1+r)(1+s)-1\}.
\]
Thus nonnegativity everywhere is exactly equivalent to
\[
\phi\le
\inf_{r,s>0}\frac{(1+r)^m(1+s)^m}{a^a b^b r^a s^b}.
\]
The infimum factors. Differentiation of \(f_{a,b}(r)=(1+r)^m/r^a\) gives the logarithmic derivative
\[
\frac{f'_{a,b}(r)}{f_{a,b}(r)}
=\frac{(b-1)r-a}{r(1+r)}.
\]
For \(b>1\), its unique global minimum is at \(r=a/(b-1)\), and for \(b=1\) its infimum is approached as \(r\to\infty\). In either case
\[
\inf_{r>0}f_{a,b}(r)
=\frac{m^m}{a^a(b-1)^{b-1}}.
\]
Similarly \(\inf_{s>0}(1+s)^m/s^b=m^m/[b^b(a-1)^{a-1}]\). Dividing their product by \(a^a b^b\) proves the displayed \(\Phi(a,b)\). At or below the threshold, the density is nonnegative at every interior point; above it, the definition of infimum yields an interior point where the density is negative. This proves both sufficiency and necessity, including boundary cases \(a=1\) or \(b=1\).

For \(a,b>1\) and \(\phi=\Phi(a,b)\), the density vanishes at the unique interior minimizer in the \((r,s)\) coordinates, while for either exponent equal to one the minimizing configuration occurs at the boundary limit. In the case \(a=b=2\), the zero-density point has \(x=y=4/9\), or \(u=v=1-e^{-4/9}\).

## Verification

A standalone standard-library checker, `CHECK.py`, computes the two-variable mixed-derivative numerator using exact rational arithmetic for selected integer and fractional-parameter witnesses. It verifies the threshold values \(\Phi(1,1)=1\), \(\Phi(1,3)=1/4\), \(\Phi(2,2)=729/256\), and \(\Phi(2,3)=1024/729\). At \((a,b,\phi,x,y)=(2,2,729/256,4/9,4/9)\), it verifies \(H=0\). With the same \(x,y\) and \(\phi=3\), it finds \(H=-37232/4782969<0\). It also verifies negative-density witnesses for \((a,b,\phi)=(1,3,1/3)\) and \((1/2,1,1/2)\). The global theorem rests on the analytic optimization above, **not** on any finite grid or finite set of checks. Run `python3 CHECK.py` from the extracted artifact directory.

## Relationship to prior work

Wu, Dui and Hu (2024), Section 3.1, equation (17), introduced precisely this power-of-negative-log-survival candidate and asserted its copula validity in Proposition 2. Their Section 4 uses the exponent range \((0,1]\); they did not give the sharp necessary-and-sufficient parameter classification stated here. For parameter values with an exponent below one, their generalized density can be negative; the current result identifies the valid domain as well as the positive-coupling frontier. The ordinary Gumbel–Barnett case \(a=b=1\) and \(\phi\le1\) is classical and is not claimed as new.

Díaz and Cuadras (2022) studied a broader two-function extension of the classical Gumbel–Barnett copula. Chesneau (2023) discussed the general template \(uv\exp\{\theta A(u)B(v)\}\) and one-variable-power subfamilies. Those forms include an appropriate survival rotation of the present expression at the level of general families. The specific **sharp all-positive-exponent iff frontier** and the exclusion of all positive coupling for subunit exponents were not identified in the material examined. The former source's full text was not accessible for a complete theorem-by-theorem priority check, so priority beyond the materials inspected remains provisional.

## Limitations

This is a copula-existence classification, not an inference theorem or a new closed-form cumulative bivariate failure-intensity expression. No estimation consistency, robustness, or empirical fit is claimed. The complete-text comparison with Díaz and Cuadras (2022) remains an explicit historical-priority risk because only its abstract and publisher's first-page preview were accessible; the full text could not be obtained from accessible sources. Independent review has not been performed.

## References

1. S. Wu, H. Dui, and L. Hu, “Construction of copulas for bivariate failure rates,” *Annals of Operations Research* **341** (2024), 1177–1189. First online 20 May 2024. https://doi.org/10.1007/s10479-024-06053-x . Full open-access article inspected, especially Section 3.1, equations (17)–(21), and Section 4.
2. W. Díaz and C. M. Cuadras, “An extension of the Gumbel–Barnett family of copulas,” *Metrika* **85** (2022), 913–926. https://doi.org/10.1007/s00184-022-00859-0 . Abstract and first-page publisher preview inspected; full text unavailable.
3. C. Chesneau, “Theoretical Validation of New Two-Dimensional One-Variable-Power Copulas,” *Axioms* **12** (2023), 392. https://doi.org/10.3390/axioms12040392 . Full open-access article inspected, particularly Introduction and Section 2.
