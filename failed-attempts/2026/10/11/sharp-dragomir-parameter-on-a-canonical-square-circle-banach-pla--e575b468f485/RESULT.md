# Sharp Dragomir parameter on a canonical square--circle Banach plane
## Finding
Let \(X=(\mathbb R^2,N)\) be the real Banach plane
\[
N(s,t)=
\begin{cases}
\max\{|s|,|t|\},&st\ge0,\\
\sqrt{s^2+t^2},&st\le0.
\end{cases}
\]
For \(\varepsilon\in[0,1)\), write \(u\perp_D^\varepsilon v\) when
\[
N(u+\lambda v)\ge\sqrt{1-\varepsilon^2}\,N(u)
\qquad(\lambda\in\mathbb R).
\]
Then the least \(\varepsilon\) such that
\[
x\perp_B y\Longrightarrow y\perp_D^\varepsilon x
\qquad(x,y\in X)
\]
is
\[
\varepsilon_D(X)=\frac1{\sqrt2}.
\]
Equivalently,
\[
\inf_{\substack{x,y\in S_X\\x\perp_B y}}
\inf_{\lambda\in\mathbb R}N(y+\lambda x)
=
\frac1{\sqrt2}.
\]
Equality is attained by
\[
x=(1,1),\qquad y=(1,0),
\]
and by the norm symmetries. Thus this canonical mixed square--circle example has a sharp global modified-Dragomir symmetry constant even though the same example is used in the literature to show complete failure of global Chmieliński approximate symmetry.

## Assumptions and scope
The scalar field is real. Birkhoff--James orthogonality means
\[
x\perp_B y
\quad\Longleftrightarrow\quad
N(x+\lambda y)\ge N(x)
\qquad(\lambda\in\mathbb R).
\]
The approximate relation is the modified Dragomir relation
\[
u\perp_D^\varepsilon v
\quad\Longleftrightarrow\quad
N(u+\lambda v)\ge\sqrt{1-\varepsilon^2}\,N(u)
\qquad(\lambda\in\mathbb R).
\]
Only the displayed two-dimensional real norm is treated.

## Proof
The dual norm is
\[
N^*(a,b)=
\begin{cases}
|a|+|b|,&ab\ge0,\\
\sqrt{a^2+b^2},&ab\le0.
\end{cases}
\]
This follows directly from the polar unit ball: in same-sign dual quadrants the square corner contributes the sum, while in opposite-sign dual quadrants the circular arc gives the Euclidean norm.

For a unit Birkhoff pair define the reverse line distance
\[
d(x,y)=\inf_{\lambda\in\mathbb R}N(y+\lambda x).
\]
If a nonzero functional \(\phi\) annihilates \(x\), then the two-dimensional quotient formula gives
\[
d(x,y)=\frac{|\phi(y)|}{N^*(\phi)}.
\]

There are three sphere strata up to global sign change and coordinate interchange.

First, let \(x=(1,t)\) with \(0<t<1\), a smooth square-edge point. Its unique norming functional is \((1,0)\), so every unit Birkhoff direction is \(y=(0,\pm1)\). Taking \(y=(0,1)\) and the annihilator \(\phi=(t,-1)\),
\[
d(x,y)=\frac1{\sqrt{1+t^2}}\ge\frac1{\sqrt2}.
\]

Second, let \(x=(c,-s)\) be a smooth circular-arc point with
\[
c^2+s^2=1,\qquad c\ge s>0.
\]
Its unique norming functional is \((c,-s)\). Hence the unit Birkhoff direction is
\[
y=\left(\frac{s}{c},1\right).
\]
The annihilator \(\phi=(s,c)\) has \(N^*(\phi)=s+c\), and therefore
\[
d(x,y)=\frac1{c(s+c)}.
\]
Writing \(r=s/c\in(0,1]\) gives
\[
d(x,y)=\frac{1+r^2}{1+r}.
\]
The minimum is attained at \(r=\sqrt2-1\) and equals
\[
2(\sqrt2-1)>\frac1{\sqrt2}.
\]

Third, take the square corner \(x=(1,1)\). Its norming functionals are exactly
\[
f_\alpha(s,t)=\alpha s+(1-\alpha)t,
\qquad0\le\alpha\le1.
\]
Thus the unit Birkhoff directions are precisely the opposite-sign Euclidean unit vectors
\[
y=(c,-s),
\qquad c,s\ge0,\qquad c^2+s^2=1,
\]
together with their signs. The functional \(\phi=(1,-1)\) annihilates \(x\), has
\[
N^*(\phi)=\sqrt2,
\]
and yields
\[
d(x,y)=\frac{c+s}{\sqrt2}\ge\frac1{\sqrt2}.
\]
Equality occurs exactly when \(c=0\) or \(s=0\). In particular,
\[
x=(1,1),\qquad y=(1,0)
\]
is extremal, and directly
\[
\inf_{\lambda\in\mathbb R}N((1,0)+\lambda(1,1))
=
\frac1{\sqrt2},
\]
with the minimum at \(\lambda=-1/2\).

The three strata exhaust the unit sphere, so the sharp reverse line distance is \(1/\sqrt2\). Therefore
\[
\varepsilon_D(X)=\sqrt{1-\frac12}=\frac1{\sqrt2}.
\]

## Verification
The proof uses the complete norming-functional set at the only nonsmooth stratum, the square corners. Smooth square-edge and circular-arc points have unique norming functionals, so their Birkhoff directions are forced.

The circular branch reduces to minimizing
\[
\frac{1+r^2}{1+r},
\qquad0<r\le1,
\]
whose unique interior critical point is \(r=\sqrt2-1\). The corner branch reduces to
\[
\frac{c+s}{\sqrt2}\ge\frac1{\sqrt2}
\]
under \(c,s\ge0\) and \(c^2+s^2=1\).

No finite sampling or numerical optimization is used as proof.

## Relationship to prior work
Alonso's 2011 open-access paper defines the full Day--James \(\ell_p-\ell_q\) family and recalls Birkhoff orthogonality in dimension two; the displayed norm is one of these mixed two-dimensional norms after choosing the corresponding \(\ell_\infty\) and \(\ell_2\) branches.

Chmieliński, Khurana, and Sain define the modified Dragomir relation, prove that every finite-dimensional Banach space is globally D-approximately symmetric, and later single out this same square--circle unit-ball geometry in their discussion of C-approximate symmetry. Their Remark 3.15 uses the example to show that global C-approximate symmetry can fail for every parameter \(\varepsilon<1\). Their inspected full text does not give the sharp D-parameter of this example.

Targeted searches using both square--circle and Day--James descriptions, modified Dragomir terminology, reverse line distance, and the value \(1/\sqrt2\) did not locate an equivalent exact evaluation.

## Limitations
The theorem concerns the modified Dragomir approximation on this real two-dimensional mixed norm. It does not compute the distinct Chmieliński approximation parameter, which the cited example shows can fail globally altogether.

Search nonappearance is not a proof of uniqueness. A differently notated exact D-parameter calculation outside the checked sources remains a bibliographic risk.

## References
1. J. Alonso, “Any two-dimensional normed space is a generalized Day--James space,” *Journal of Inequalities and Applications* 2011, Article 2, DOI 10.1186/1029-242X-2011-2; published 2011-06-15.
2. J. Chmieliński, D. Khurana, and D. Sain, “Local approximate symmetry of Birkhoff--James orthogonality in normed linear spaces,” arXiv:2012.08162, first posted 2020-12-15.
