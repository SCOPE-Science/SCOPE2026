# Unique positive symmetric cubic-exact four-node quadrature minimizing Jordan-variation error

## Finding

Let \(d_*\) be the unique root of
\[
9d^2-32d^3=\frac1{12},\qquad \frac18<d<\frac17.
\]
Among **all centrally symmetric, nonnegative quadrature rules on \([0,1]\) supported on at most four nodes and exact for every real polynomial of degree at most three**, the unique rule with the smallest worst-case error on the Jordan-variation unit ball is
\[
Q_*f=\left(\frac12-2d_*\right)
\left[f\left(\frac12-3d_*\right)+f\left(\frac12+3d_*\right)\right]
+2d_*\left[f\left(\frac12-d_*\right)+f\left(\frac12+d_*\right)\right].
\]
Its exact operator error norm is
\[
\boxed{\sup_{\operatorname{Var}_{[0,1]}(f)\le1}\left|Q_*f-\int_0^1f(t)\,dt\right|=d_*
=0.13216552074896658\ldots.}
\]
Two distinct normalized step functions attain equality. The design is unique as a probability measure (up to reordering or adding zero-weight nodes).

## Assumptions and scope

A symmetric at-most-four-node positive rule can be written
\[
Qf=w\{f(\tfrac12-b)+f(\tfrac12+b)\}
+v\{f(\tfrac12-a)+f(\tfrac12+a)\},
\]
where \(0\le a\le b\le\frac12\), \(v,w\ge0\), and \(v+w=\frac12\). Degenerate pairs, coincident nodes, and zero weights are allowed. Exactness through degree three is equivalent to
\[
2va^2+2wb^2=\frac1{12}.
\]
For any real pointwise Jordan-bounded-variation function, \(\operatorname{Var}_{[0,1]}(f)\) is the supremum of \(\sum_i|f(t_i)-f(t_{i-1})|\) over finite ordered partitions. Endpoint values and values at quadrature nodes are retained. Constants have zero error because the weights sum to one.

The comparison class is **not** all positive quadrature rules, all four-node rules without symmetry, or all rules of degree seven. Gaussian four-node quadrature is used only as a conventional benchmark.

## Proof

**1. Exact norm as discrepancy.** Put \(v=\frac12-w\). For the atomic probability measure \(\nu_Q\), the difference between its cumulative mass and the uniform cumulative mass is piecewise affine between nodes. Its exact maximum absolute size, allowing both one-sided values at each node, is
\[
D(Q)=\max\left\{\frac12-b,\ b-v,\ v-a,\ a\right\}.
\]
Indeed, the cumulative-mass differences immediately before and after the two left nodes are \(b-\frac12\), \(b-v\), \(a-v\), and \(a\); reflection supplies the remaining values. The signs omitted from the displayed maximum are dominated by its listed positive candidates because \(0\le a\le b\) and \(v\ge0\). The Jordan decomposition of a bounded-variation function into differences of nondecreasing functions, together with upper- and lower-tail step representations, gives \(|Qf-\int f|\le D(Q)\operatorname{Var}(f)\). Conversely, a tail indicator taken strictly after an extremal node (or its left-sided analogue) has variation one and realizes its corresponding discrepancy. This also handles arbitrary point values at jump sites. Thus the error norm equals \(D(Q)\).

**2. Universal four-atom lower bound.** Write \(d=D(Q)\). At each distinct atom, the cumulative discrepancy jumps by its positive mass, while its values immediately before and after have absolute value at most \(d\). Hence every individual atom has mass at most \(2d\). There are at most four distinct atoms, so \(1\le8d\):
\[
d\ge\frac18.
\]

**3. Cubic moment obstruction.** Suppose \(d\le d_*<\frac17\). The four terms in the exact discrepancy formula imply
\[
a\le d,\quad b\ge\frac12-d,\quad v\ge b-d,\quad v\le a+d,
\]
and therefore \(b\le a+2d\le3d\). In particular, \(b\ge\frac12-d>d\), so \(b-d>0\). The required quadratic moment \(M=\frac1{12}\) obeys
\[
\begin{aligned}
M&=b^2-2v(b^2-a^2)\\
&\le b^2-2(b-d)(b^2-a^2)\\
&\le b^2-2(b-d)(b^2-d^2)
=:F_d(b).
\end{aligned}
\]
The first inequality uses \(v\ge b-d\) and \(b\ge a\); the second uses \(a\le d\) and \(b-d>0\). Direct differentiation gives
\[
F_d'(b)=2d^2+2b(1-3b+2d)
\ge2d^2+2b(1-7d)>0
\]
for \(b\le3d\) and \(d<\frac17\). Consequently,
\[
\frac1{12}=M\le F_d(b)\le F_d(3d)=9d^2-32d^3.
\]
The last polynomial is strictly increasing for \(\frac18\le d\le\frac17\), and its value at \(d_*\) equals \(\frac1{12}\). Thus \(d\ge d_*\).

**4. Unique equality and attainment.** For \(d=d_*\), equality in the strictly increasing \(F_d\) forces \(b=3d_*\). Since \(b\le a+2d_*\le3d_*\), this forces \(a=d_*\). Equality in the first moment bound then forces \(v=b-d_*=2d_*\), hence \(w=\frac12-2d_*\). All coefficients are strictly positive and \(3d_*<\frac12\). These parameters satisfy
\[
2(2d_*)d_*^2+2(\tfrac12-2d_*)(3d_*)^2
=9d_*^2-32d_*^3=\frac1{12},
\]
so the rule is admissible. Its discrepancy is
\[
D(Q_*)=\max\left\{\frac12-3d_*,d_*,d_*,d_*\right\}=d_*,
\]
because \(d_*\ge\frac18\). For either \(s=\frac12-3d_*\) or \(s=\frac12-d_*\), the step \(f_s(t)=\mathbf1_{(s,1]}(t)\) has variation one and \(Q_*f_s-\int f_s=-d_*\). This proves optimality, uniqueness, and sharp attainment.

The root exists uniquely in \((\frac18,\frac17)\) because the polynomial minus \(\frac1{12}\) is negative at \(\frac18\), positive at \(\frac17\), and has derivative \(18d-96d^2>0\) on that interval.

## Verification

Run `python3 check_quadrature.py` with Python 3. The standalone program checks an exact rational enclosure of the cubic root, all four polynomial moment equations, two attaining steps, over twelve thousand randomly sampled admissible rules, ten thousand tests of the explicit moment envelope, and the conventional four-node Gauss comparison. The universal proof above is analytic; the numerical enumerations do **not** purport to enumerate the uncountable admissible family.

The optimizer has offsets \(a=0.13216552074896658\ldots\), \(b=0.39649656224689975\ldots\), inner weight \(v=0.26433104149793317\ldots\) per node, and outer weight \(w=0.23566895850206683\ldots\) per node. The degree-seven Gauss-Legendre rule with four nodes has Jordan-variation worst-case error \(0.16999052179242813\ldots\); the degree-three constrained optimizer reduces that specific worst-case error by about \(22.25\%\), with the explicitly stated loss of higher-degree exactness.

## Relationship to prior work

The one-dimensional Koksma–Hlawka discrepancy principle is classical. Aistleitner–Dick (2014) give a general bounded-variation/measure framework, but their stated main theorem does not specify the positive symmetric degree-three exact four-atom optimizer. The accessible full article of Komisarski–Wąsowicz (2022) concerns symmetric at-most-three-node cubic-exact rules and inequalities for 3-convex functions, a different objective and node class. Förster–Petras (1991) explicitly treats sharp BV quadrature errors and the quality of Gaussian rules, making it the most relevant historical-priority risk; the available abstract alone does not resolve whether its full text contains the present constrained four-node extremal rule.

## Limitations

The uniqueness theorem is restricted to positive centrally symmetric quadrature measures supported at no more than four nodes, exact through cubic degree, on the uniform interval. It does not assert optimality among asymmetric rules, rules with additional nodes, signed weights, nonuniform target measures, or higher-degree-exact formulas. One historically relevant 1991 primary article could not be examined in full, leaving a material but nondecisive priority risk.

## References

- C. Aistleitner and J. Dick, *Functions of bounded variation, signed measures, and a general Koksma–Hlawka inequality*, first submitted 2 June 2014, https://arxiv.org/abs/1406.0230.
- K.-J. Förster and K. Petras, *Error Estimates in Gaussian Quadrature for Functions of Bounded Variation*, SIAM J. Numer. Anal. **28** (1991), 880–889, https://doi.org/10.1137/0728047.
- A. Komisarski and S. Wąsowicz, *On optimal inequalities between three-point quadratures*, Aequationes Math. **96** (2022), 621–638, https://doi.org/10.1007/s00010-022-00868-4.
- NIST Digital Library of Mathematical Functions, Section 3.5, *Quadrature*, https://dlmf.nist.gov/3.5.
