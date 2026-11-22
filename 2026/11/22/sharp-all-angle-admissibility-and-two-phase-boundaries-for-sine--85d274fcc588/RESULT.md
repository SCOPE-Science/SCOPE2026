# Sharp all-angle admissibility and two phase boundaries for sine-FGM copulas

## Finding

Consider the sine-FGM family at shape exponent one,
\[
 C_{\alpha,\beta}(u,v)=uv+\alpha\sin\!\left(\beta u(1-u)v(1-v)\right),\qquad (u,v)\in[0,1]^2,
\]
with real \(\alpha\) and \(\beta>0\). Define
\[
 h(t)=\cos t-t\sin t,\qquad
 Q(\beta)=\max_{0\le t\le\beta/16}\left(1-4\sqrt{t/\beta}\right)|h(t)|.
\]
Then **the exact full-parameter validity condition**, with no angle restriction, is
\[
 \boxed{C_{\alpha,\beta}\text{ is a copula}\ \Longleftrightarrow\ |\alpha|\beta Q(\beta)\le1.}
\]
The envelope is always at least one. Let
\[
 \boxed{\beta_c=\min_{\substack{t>0\\|h(t)|>1}}
 16t\left(\frac{|h(t)|}{|h(t)|-1}\right)^2.}
\]
The minimum exists, satisfies \(64<\beta_c<106\), and a numerical minimization gives \(\beta_c\approx103.92133496324\) (the decimal is diagnostic, not a certified decimal enclosure). Exactly
\[
 Q(\beta)=1\quad\text{for }0<\beta\le\beta_c,\qquad
 Q(\beta)>1\quad\text{for }\beta>\beta_c.
\]
The second, strictly earlier, boundary is \(\beta_{\mathrm{QD}}=16\pi\). For every *nonzero admissible* \(\alpha\), the copula is positively quadrant dependent if \(\alpha>0\) and \(0<\beta\le16\pi\), negatively quadrant dependent if \(\alpha<0\) and \(0<\beta\le16\pi\), and neither positively nor negatively quadrant dependent for \(\beta>16\pi\). For \(\alpha=0\) the copula is independence for all \(\beta\).

Finally, the sharp admissible amplitude obeys
\[
 Q(\beta)=\frac{\beta}{108}+O(1),\qquad
 \max\{|\alpha|:C_{\alpha,\beta}\text{ is a copula}\}\sim\frac{108}{\beta^2}
 \quad(\beta\to\infty).
\]

## Assumptions and scope

The conclusions hold for all real \(\alpha\) and all strictly positive real \(\beta\), with uniform margins on \([0,1]\). They concern the exponent-one subfamily of the original three-parameter construction, not all positive shape exponents. Validity means two-increasing, grounded, and with the correct uniform margins. The special value \(\beta=0\) yields independence for any finite \(\alpha\) and is omitted from the amplitude formula, which divides by \(\beta\). The rank-dependence classification is pointwise quadrant dependence, not positive association in every order.

## Proof

Set \(f(u)=u(1-u)\), \(a=f(u)\), \(b=f(v)\), and \(t=\beta ab\). The boundary identities \(C(u,0)=C(0,v)=0\), \(C(u,1)=u\), and \(C(1,v)=v\) hold exactly. Direct differentiation gives the continuous mixed density
\[
 c_{\alpha,\beta}(u,v)
 =1+\alpha\beta(1-2u)(1-2v)[\cos t-t\sin t]. \tag{1}
\]
A smooth grounded function with these margins is a copula if and only if its mixed density is nonnegative everywhere.

For each \(t\in[0,\beta/16]\), the feasible pairs satisfy \(a,b\in[0,1/4]\) and \(ab=t/\beta\). By AM-GM,
\[
 |(1-2u)(1-2v)|^2=(1-4a)(1-4b)
 \le (1-4\sqrt{ab})^2.
\]
Equality occurs at \(a=b=\sqrt{t/\beta}\); choosing the two roots of \(u(1-u)=a\) independently makes the sign of \((1-2u)(1-2v)\) either positive or negative. Thus the largest possible absolute perturbation of the density at each fixed \(t\) equals \(|\alpha|\beta(1-4\sqrt{t/\beta})|h(t)|\), with *both signs attainable*. Maximizing over \(t\) proves both directions of the boxed exact validity criterion. At \(t=0\), the two opposite corners attain \(|(1-2u)(1-2v)h(t)|=1\), so \(Q(\beta)\ge1\).

An interior value of the envelope is greater than one exactly when for some \(t>0\) with \(|h(t)|>1\),
\[
 1-4\sqrt{t/\beta}>\frac1{|h(t)|},
 \quad\text{equivalently}\quad
 \beta>16t\left(\frac{|h(t)|}{|h(t)|-1}\right)^2. \tag{2}
\]
The eligible set is nonempty because \(|h(2)|>1\). The right-hand side tends to infinity as \(|h(t)|\downarrow1\), as \(t\to\infty\), and toward any other finite boundary of the eligible set; hence its minimum exists. Equation (2) proves the exact \(\beta_c\) transition, including equality. To separate it from the quadrant boundary, use
\[
 |h(t)|\le\sqrt{1+t^2},\quad
 \frac{|h(t)|}{|h(t)|-1}\ge\frac{\sqrt{1+t^2}}{\sqrt{1+t^2}-1}>1+\frac1t
\]
whenever \(|h(t)|>1\). Therefore every candidate defining \(\beta_c\) is strictly greater than \(16(t+2+t^{-1})\ge64\). The explicit value at \(t=2\) is less than \(106\). In particular, \(16\pi<64<\beta_c\).

For nonzero \(\alpha\), the difference from independence is \(\alpha\sin t\), with \(t\) covering the entire interval \([0,\beta/16]\) as \((u,v)\) varies. Since \(\sin t\) is nonnegative on \([0,\pi]\), it has the sign of \(\alpha\) throughout the square when \(\beta\le16\pi\). If \(\beta>16\pi\), the interval includes both a strictly positive and a strictly negative sine value; neither quadrant inequality can hold globally. This also proves sharpness at equality.

For the large-angle statement, \(|h(t)|\le t+1\) yields
\[
 Q(\beta)\le 1+\max_{0\le t\le\beta/16}t(1-4\sqrt{t/\beta})
 =1+\frac{\beta}{108},
\]
where the maximum occurs at \(t=\beta/36\). Choose \(t_\beta\) of the form \(\pi/2+k\pi\) within \(\pi/2\) of \(\beta/36\), for sufficiently large \(\beta\). Then \(\cos t_\beta=0\), \(|\sin t_\beta|=1\), and \(|h(t_\beta)|=t_\beta\). Taylor's theorem for \(t(1-4\sqrt{t/\beta})\) at its maximum shows
\[
 Q(\beta)\ge t_\beta(1-4\sqrt{t_\beta/\beta})
 =\frac\beta{108}-O(\beta^{-1}).
\]
These bounds prove \(Q(\beta)=\beta/108+O(1)\) and the sharp amplitude asymptotic.

## Verification

The accompanying standalone `check.py` symbolically verifies (1), all four boundary identities, and numerically checks the extremizing reduction, the scalar onset and several large-angle cases. Its scans are diagnostics, **not** exhaustive or infinite proofs. The exact theorem instead follows from the AM-GM extremal identity, elementary trigonometry, compact minimization and the asymptotic comparison proved above. Reproduce with `python check.py` using Python, SymPy, NumPy and SciPy.

## Relationship to prior work

Chesneau (2023), Proposition 1, introduced the sine-FGM family at arbitrary \(\gamma\ge1\), giving the **sufficient** constraints \(\beta\le8\pi\) and \(|\alpha|\le[\beta(1+\beta^2/256)]^{-1}\) for \(\gamma=1\). The present exact bound becomes \(|\alpha|\le\beta^{-1}\) throughout that original interval, and extends validity characterization to every \(\beta>0\). The earlier paper discusses quadrant dependence only for its restricted nonnegative sine arguments; the second threshold here shows where that property fails on the larger valid family. The 2021 multivariate trigonometric constructions involve products of separate sine factors and a sine/cosine of sums, not this composed sine of products. The 2022 angle-parameter trigonometric constructions are related context, but only an abstract was accessible during the comparison and complete historical priority is not asserted.

## Limitations

The exact envelope involves a one-dimensional maximization rather than an elementary closed form for every \(\beta\). The decimal for \(\beta_c\) is not an independently certified numerical enclosure; its exact defining minimum and phase characterization are rigorous. No uniqueness of the critical minimizing argument is claimed. No three-parameter \(\gamma\ne1\) classification or statistical optimality is claimed. A full historical-priority determination would require broader bibliographic verification, particularly full-text comparison with any unavailable relevant papers.

## References

1. C. Chesneau, *A Collection of New Trigonometric- and Hyperbolic-FGM-Type Copulas*, AppliedMath **3** (2023), 147–174; first public publication 2023-03-03. https://doi.org/10.3390/appliedmath3010010 ; full text https://www.mdpi.com/2673-9909/3/1/10 .
2. C. Chesneau, *On New Types of Multivariate Trigonometric Copulas*, AppliedMath **1** (2021), 3–17. https://doi.org/10.3390/appliedmath1010002 ; full text https://www.mdpi.com/2673-9909/1/1/2 .
3. C. Chesneau, *Theoretical Study of Some Angle Parameter Trigonometric Copulas*, Modelling **3** (2022), 140–163. https://doi.org/10.3390/modelling3010010 (abstract-level comparison only).
