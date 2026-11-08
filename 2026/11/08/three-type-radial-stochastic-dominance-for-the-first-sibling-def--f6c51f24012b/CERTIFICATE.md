# Exact positive-coefficient certificate

For positive rates ordered as \(a\ge b\ge c>0\), set \(a=x+y+z\), \(b=y+z\), \(c=z\) with \(x,y\ge0\), \(z>0\). Define \(s=a+b+c\) and \(H\) as in `RESULT.md`. The following is a polynomial identity:

\[
-\sum_{v\in\{a,b,c\}}\left(v-\frac{s}{3}\right)\partial_v H
=\frac{\sum_{k=0}^{10} z^k B_k(x,y)}{3s^3(a+b)^3(a+c)^3(b+c)^3}.
\]

The coefficient polynomials are:

\[B_{0}(x,y)=2 y^{2} \left(x + y\right)^{2} \left(x + 2 y\right)^{4} \left(x^{4} + 7 x^{3} y + 18 x^{2} y^{2} + 22 x y^{3} + 11 y^{4}\right).\]

\[B_{1}(x,y)=12 y^{2} \left(x + y\right)^{2} \left(x + 2 y\right)^{3} \left(4 x^{4} + 29 x^{3} y + 82 x^{2} y^{2} + 106 x y^{3} + 53 y^{4}\right).\]

\[B_{2}(x,y)=12 y^{2} \left(x + y\right)^{2} \left(x + 2 y\right)^{2} \left(43 x^{4} + 341 x^{3} y + 1023 x^{2} y^{2} + 1364 x y^{3} + 682 y^{4}\right).\]

\[B_{3}(x,y)=8 y^{2} \left(x + y\right)^{2} \left(x + 2 y\right) \left(467 x^{4} + 3795 x^{3} y + 11509 x^{2} y^{2} + 15428 x y^{3} + 7714 y^{4}\right).\]

\[B_{4}(x,y)=6 y \left(x + y\right) \left(80 x^{6} + 3739 x^{5} y + 29998 x^{4} y^{2} + 102838 x^{3} y^{3} + 177219 x^{2} y^{4} + 150960 x y^{5} + 50320 y^{6}\right).\]

\[B_{5}(x,y)=48 \left(x + 2 y\right) \left(4 x^{6} + 134 x^{5} y + 1909 x^{4} y^{2} + 8765 x^{3} y^{3} + 17420 x^{2} y^{4} + 15645 x y^{5} + 5215 y^{6}\right).\]

\[B_{6}(x,y)=16 \left(128 x^{6} + 2295 x^{5} y + 18345 x^{4} y^{2} + 67718 x^{3} y^{3} + 122904 x^{2} y^{4} + 106854 x y^{5} + 35618 y^{6}\right).\]

\[B_{7}(x,y)=48 \left(x + 2 y\right) \left(182 x^{4} + 1643 x^{3} y + 6224 x^{2} y^{2} + 9162 x y^{3} + 4581 y^{4}\right).\]

\[B_{8}(x,y)=192 \left(97 x^{4} + 659 x^{3} y + 1806 x^{2} y^{2} + 2294 x y^{3} + 1147 y^{4}\right).\]

\[B_{9}(x,y)=320 \left(x + 2 y\right) \left(62 x^{2} + 101 x y + 101 y^{2}\right).\]

\[B_{10}(x,y)=8448 \left(x^{2} + x y + y^{2}\right).\]

The expansion contains exactly **79 nonzero integer monomial coefficients** and every coefficient is positive. In particular, \(B_{10}=8448(x^2+xy+y^2)\), so the whole numerator is strictly positive whenever \(x+y>0\) and \(z>0\). The displayed identity is verified by differentiating the rational expression for \(H\), multiplying by the positive denominator, and expanding exactly; `verify.py` independently performs those steps and tests all coefficient signs.
