# Exact negative-parameter frontier and diagonal validity test for the OR3 copula

## Finding

Consider the original ratio-type 3 (OR3) expression

\[
C_{a,b}(x,y)=\frac{(b+1)xy}{b+\exp(a(1-x)(1-y))},\qquad (x,y)\in[0,1]^2,
\]

with \(b\ge0\) and \(a\in\mathbb R\). The following is an exact copula-admissibility criterion.

**Theorem.**

1. On the nonpositive-parameter half-plane, \(C_{a,b}\) is a copula **if and only if** \(-(b+1)\le a\le0\). Both bounds are included.
2. On the positive-parameter half-plane, define for \(0\le v\le1\)

   \[
   \begin{aligned}
   z&=\exp(av^2),\\
   F_{a,b}(v)&=(b+z)^2+a z(b+z)(1-v)(3v-1)\\
    &\quad+a^2z(z-b)v^2(1-v)^2.
   \end{aligned}
   \]

   For every \(a>0\), \(C_{a,b}\) is a copula **if and only if** \(F_{a,b}(v)\ge0\) for **all** \(v\in[0,1]\). Thus a two-dimensional mixed-density test reduces without loss to a one-dimensional diagonal test. In particular \(F_{a,b}(0)=(b+1)(b+1-a)\), so \(a\le b+1\) is necessary but, as shown below, not sufficient.
3. The previously unlisted parameter \((a,b)=(2,1)\) is admissible. In contrast, \((a,b)=(21,20)\) is not admissible, even though \(a=b+1\) obeys the necessary corner bound. Consequently the valid positive and negative sides of the parameter range have genuinely different behavior.

## Assumptions and scope

Only the original bivariate OR3 formula is considered. The ratio parameter is \(b\ge0\), and the exponential parameter is any finite real \(a\). The theorem concerns the genuine two-increasing copula property, not merely pointwise Fréchet bounds, correlation signs, or a sampled numerical approximation. The positive-side criterion is exact but remains a continuous one-variable inequality; no closed elementary formula for its boundary as a function of \(b\) is asserted.

## Proof

**1. Mixed density and boundary conditions.** All denominators are positive. Direct substitution gives \(C(x,0)=C(0,y)=0\), \(C(x,1)=x\), and \(C(1,y)=y\). Set

\[
 t=(1-x)(1-y),\quad z=\exp(at),\quad h=x+y-3xy,\quad u=xy t.
\]

Twice differentiating yields

\[
\frac{\partial^2 C_{a,b}}{\partial x\partial y}
=\frac{b+1}{(b+z)^3}N,
\quad N=(b+z)^2+az(b+z)h+a^2z(z-b)u.
\]

Consequently the expression is a copula exactly when \(N\ge0\) on the closed unit square.

**2. Reduction to diagonal and coordinate axes.** Put \(p=1-x\), \(q=1-y\), \(s=p+q\) and \(t=pq\). For fixed \(t\in[0,1]\), the feasible sum is exactly

\[
2\sqrt t\le s\le1+t.
\]

Also \(h=-1+2s-3t\) and \(u=t(1-s+t)\). Since \(z=\exp(at)\) is fixed when \(t\) is fixed, \(N\) is **affine in \(s\)**. Its minimum must therefore lie at one of the two endpoints. The endpoint \(s=2\sqrt t\) is the diagonal point \(x=y=1-\sqrt t\) and gives the formula \(F_{a,b}(\sqrt t)\). The other endpoint \(s=1+t\) is a coordinate-axis point, where \(u=0\), \(h=1-t\), and

\[
N_{\mathrm{axis}}=(b+z)\bigl[b+z+az(1-t)\bigr].
\]

For \(a>0\), this axis expression is strictly positive. Therefore positivity at every diagonal point is both necessary and sufficient for the entire square, proving part 2. At \(v=0\) the stated necessary corner bound follows.

**3. Exact nonpositive half-plane.** Write \(a=-k\), with \(k\ge0\). At \((x,y)=(0,1)\), \(t=0\), \(h=1\), \(u=0\) and \(N=(b+1)(b+1-k)\). Hence \(k\le b+1\) is necessary. We prove it sufficient for every \(x,y\).

Let \(w=kt\), \(z=e^{-w}\), and set

\[
P=\frac{kz}{b+z}=\frac{k}{1+b e^w}.
\]

Because \(0\le w\le k\le b+1\), we have \(0\le P\le1\), and also

\[
Pw=\frac{kw}{1+b e^w}
\le\frac{(b+1)w}{1+b(1+w)}\le1.
\]

The first inequality uses \(k\le b+1\) and \(e^w\ge1+w\); the second uses \(w\le b+1\). The density numerator satisfies

\[
\frac{N}{(b+z)^2}=1-Ph+Pw\frac{z-b}{b+z}xy.
\]

If \(z\ge b\), the final term is nonnegative, while \(h\le1\), so this quantity is at least \(1-P\ge0\). If \(z<b\), use \((b-z)/(b+z)\le1\) and the identity \(h\le1-xy\) (equivalently \((1-x)(1-y)+xy\ge0\)). We obtain

\[
\frac{N}{(b+z)^2}\ge1-P+Pxy(1-w).
\]

For \(w\le1\), the right side is at least \(1-P\ge0\); for \(w>1\), its minimum over \(0\le xy\le1\) is \(1-Pw\ge0\). Hence the mixed density is nonnegative everywhere, including the sharp endpoint \(k=b+1\). This proves part 1.

**4. Explicit strict enlargement and interior obstruction.** To verify \((a,b)=(2,1)\), the diagonal reduction suffices. For \(v\in[0,1]\) let \(z=e^{2v^2}\ge1\). The diagonal \(h=(1-v)(3v-1)=-1+4v-3v^2\ge-1+v\), since \(3v(1-v)\ge0\). The \(a^2z(z-b)u\) term is nonnegative, and

\[
\begin{aligned}
F_{2,1}(v)&\ge(1+z)\,[1+z+2z(-1+v)]\\
&=(1+z)z\,[2v-(1-e^{-2v^2})]\ge0,
\end{aligned}
\]

since \(1-e^{-r}\le r\) for \(r\ge0\) and \(2v^2\le2v\). Thus \((2,1)\) is valid, beyond the original published parameter rectangle.

For \((a,b)=(21,20)\), set \(x=y=2/3\). Then \(t=1/9\), \(h=0\), \(u=4/81\), and, with \(z=e^{7/3}\),

\[
N=\frac{3600-3560z+205z^2}{9}.
\]

The exact rational Taylor bounds

\[
\frac{1071641}{104976}<e^{7/3}<\frac{1106737}{106920}
\]

imply \(10<z<11\). The quadratic numerator is strictly convex and takes the negative values \(-11500\) at \(z=10\) and \(-10755\) at \(z=11\); it is therefore negative throughout \([10,11]\). Hence the mixed density is negative at that interior point. This completes the proof.

## Verification

The accompanying `verify_or3.py` reproduces the exact mixed-derivative identity, the fixed-product affine reduction, the axis and diagonal substitutions, and the rational exponential interval that certifies the interior counterexample. Run it with `python verify_or3.py` in an environment with SymPy. It checks symbolic identities and a rational negative witness; the universal infinite-continuum sufficiency statements are justified by the inequalities above rather than by finite numerical sampling.

## Relationship to prior work

Chesneau (2023, *Symmetry*, Proposition 3) introduced precisely this OR3 ratio-exponential copula and proved the sufficient region \(-1\le a\le1\), \(b\ge0\), displaying the same mixed derivative. That construction and derivative are prior results. The source does not determine the full negative-parameter frontier or the above admissible and inadmissible pairs. Manstavičius and Bagdonas (2022) already provide a **general** twice-differentiable characterization for functions of the form \(xy f((1-x)(1-y))\). That broader characterization is prior work and may implicitly entail scalar testing; no novelty of a universal transformation criterion is claimed. The family-specific contribution here is evaluating the entire negative parameter side sharply and distinguishing its behavior from the positive side, with the concrete diagonal formula and certified examples.

The Celebioglu–Cuadras exponential copula at \(b=0\), as well as subsequent generalized exponential copulas and multiplicative ratio copulas, are related but have different denominators or parameterizations; the cited full-text sources do not supply this OR3 parameter-domain criterion. The broad 2022 ratio-copula paper addresses a different base construction. The full text of the relevant 2022 general characterization was not available during this review; whether it already gives an equivalent simplified OR3 frontier remains a historical-coverage risk. These comparisons do not constitute an independent certification of historical priority.

## Limitations

The positive-parameter boundary remains an explicit univariate inequality, not a closed-form endpoint function. No values of \(b<0\), multivariate validity, statistical efficiency, or stronger stochastic-order statements are claimed. The full text of the 2022 general smooth-transform criterion could not be inspected (institutional access unavailable); its explicit examples and implications remain a residual priority risk. No independent external mathematical review has been performed, and searches cannot establish absolute novelty against unindexed literature.

## References

1. C. Chesneau, *A Collection of Two-Dimensional Copulas Based on an Original Parametric Ratio Scheme*, **Symmetry** 15 (2023), 977, published 25 April 2023. https://doi.org/10.3390/sym15050977 . In particular Proposition 3 and its density formula.
2. C. Chesneau, *Theoretical Contributions to Three Generalized Versions of the Celebioglu–Cuadras Copula*, **Analytics** 2 (2023), 31–54. https://doi.org/10.3390/analytics2010003 .
3. C. Chesneau, *Theoretical Advancements on a Few New Dependence Models Based on Copulas with an Original Ratio Form*, **Modelling** 4 (2023), 102–132. https://doi.org/10.3390/modelling4020008 .
4. C. Chesneau, *Some new ratio-type copulas: theory and properties*, **Applicationes Mathematicae** 49 (2022), 79–101. https://doi.org/10.4064/am2436-12-2021 .
5. M. Manstavičius and G. Bagdonas, *A class of bivariate independence copula transformations*, **Fuzzy Sets and Systems** 428 (2022), 58–79. https://doi.org/10.1016/j.fss.2020.12.022 . General twice-smooth characterization; abstract checked, full text unavailable.
