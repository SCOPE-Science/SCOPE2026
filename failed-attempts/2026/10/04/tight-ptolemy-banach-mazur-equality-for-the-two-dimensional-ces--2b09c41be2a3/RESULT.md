# Tight Ptolemy–Banach–Mazur equality for the two-dimensional Cesàro plane
## Finding
Let \(X=\mathrm{{ces}}^{{(2)}}_2\) be \(\mathbb R^2\) with
\[
\|(x,y)\|=\left(x^2+\left(\frac{{|x|+|y|}}{{2}}\right)^2\right)^{{1/2}}.
\]
Then
\[
C_P(X)=d_{{\mathrm{{BM}}}}(X,\ell_2^2)^2=1+\frac1{{\sqrt5}}.
\]
An optimal Euclidean pullback norm is
\[
|(x,y)|_*=\sqrt{{5x^2+y^2}},
\]
up to multiplication by a positive scalar.

## Assumptions and scope
The space is real and two-dimensional. Here \(C_P(X)\) is the Ptolemy constant and \(d_{{\mathrm{{BM}}}}(X,\ell_2^2)\) is the Banach–Mazur distance to the Euclidean plane. No claim is made for higher-dimensional Cesàro sections or for \(\mathrm{{ces}}_p^{(2)}\) with \(p\ne2\).

## Proof
Zuo computed
\[
C_P(\mathrm{{ces}}_2^{(2)})=1+\frac1{{\sqrt5}}.
\]
The same article proves the norm-comparison inequality: if two equivalent norms satisfy \(a|z|\le \|z\|\le b|z|\), then their Ptolemy constants differ by at most the factor \((b/a)^2\). Applying this with a Hilbert pullback and using \(C_P(\ell_2^2)=1\) gives, after taking the infimum over all linear isomorphisms,
\[
C_P(X)\le d_{{\mathrm{{BM}}}}(X,\ell_2^2)^2.
\]

For the reverse inequality, take
\[
|(x,y)|_*^2=5x^2+y^2.
\]
Because the Cesàro norm is absolute, it is enough to set \(t=|y|/|x|\ge0\) when \(x\ne0\). Then
\[
\frac{\|(x,y)\|^2}{|(x,y)|_*^2}
=\frac{5+2t+t^2}{4(5+t^2)}.
\]
The derivative of the factor without \(1/4\) has numerator \(2(5-t^2)\), so the maximum occurs at \(t=\sqrt5\), while the minimum occurs at the axis limits \(t=0\) and \(t\to\infty\). Hence
\[
\frac14 |(x,y)|_*^2\le \|(x,y)\|^2
\le \frac{5+\sqrt5}{20}|(x,y)|_*^2.
\]
Therefore
\[
d_{{\mathrm{{BM}}}}(X,\ell_2^2)^2
\le \frac{(5+\sqrt5)/20}{1/4}
=1+\frac1{{\sqrt5}}.
\]
Combining this with the Ptolemy lower bound proves equality and proves that the displayed Euclidean pullback is globally optimal.

## Verification
The critical one-variable quotient is
\[
f(t)=\frac{5+2t+t^2}{5+t^2},\qquad t\ge0.
\]
Its derivative has the sign of \(5-t^2\), so \(f\) increases on \([0,\sqrt5]\) and decreases on \([\sqrt5,\infty)\). Direct substitution gives \(f(0)=1\), \(\lim_{{t\to\infty}}f(t)=1\), and \(f(\sqrt5)=1+1/\sqrt5\). Equivalently,
\[
\left(1+\frac1{{\sqrt5}}\right)(5+t^2)-(5+2t+t^2)
=\frac1{{\sqrt5}}(t-\sqrt5)^2\ge0.
\]
The Ptolemy value and the norm-comparison lemma were checked in the full open article text, including Example 2.10 and Lemma 2.5.

## Relationship to prior work
Zuo's 2012 article gives the exact Ptolemy constant of \(\mathrm{{ces}}_2^{(2)}\) and exhibits an isometric normalization used to compare this norm with the Euclidean norm. The present finding identifies that Euclidean comparison as globally Banach–Mazur optimal: no other linear change of coordinates can reduce the distortion below \(\sqrt{{1+1/\sqrt5}}\). Searches for the object together with “Banach–Mazur distance”, “optimal ellipse”, and the exact constant did not locate a published statement of this equality.

## Limitations
The originality check is literature-search based and cannot prove nonexistence of an obscure prior statement. A closely related 2010 paper on Ptolemy and Zbăganu constants was inspected through its available abstract and section preview; no Cesàro-plane Banach–Mazur statement was visible there. The mathematical proof itself is exact and finite-dimensional.

## References
Z. Zuo, “The Ptolemy constant of absolute normalized norms on \(\mathbb R^2\),” Journal of Inequalities and Applications 2012, Article 107, DOI 10.1186/1029-242X-2012-107. First verified public date: 2012-05-17.
