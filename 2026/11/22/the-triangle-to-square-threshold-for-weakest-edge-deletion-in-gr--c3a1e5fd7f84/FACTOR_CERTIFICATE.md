# Exact positive-polynomial certificate

The following coefficients are exact integers, not fitted or sampled values. In the triangle proof,

\[
E_b-E_a=\frac{(b-a)P(a,b,c)}{D(a,b,c)}.
\]

For strictly positive conductances, every displayed monomial in each polynomial is positive; hence so are the sums and their product.

\[
P(a,b,c)=152 a^{5} b^{3} + 448 a^{5} b^{2} c + 312 a^{5} b c^{2} + 112 a^{5} c^{3} + 305 a^{4} b^{4} + 1574 a^{4} b^{3} c + 2193 a^{4} b^{2} c^{2} + 1208 a^{4} b c^{3} + 352 a^{4} c^{4} + 152 a^{3} b^{5} + 1574 a^{3} b^{4} c + 3844 a^{3} b^{3} c^{2} + 3638 a^{3} b^{2} c^{3} + 1560 a^{3} b c^{4} + 368 a^{3} c^{5} + 448 a^{2} b^{5} c + 2193 a^{2} b^{4} c^{2} + 3638 a^{2} b^{3} c^{3} + 2497 a^{2} b^{2} c^{4} + 728 a^{2} b c^{5} + 128 a^{2} c^{6} + 312 a b^{5} c^{2} + 1208 a b^{4} c^{3} + 1560 a b^{3} c^{4} + 728 a b^{2} c^{5} + 64 a b c^{6} + 112 b^{5} c^{3} + 352 b^{4} c^{4} + 368 b^{3} c^{5} + 128 b^{2} c^{6}\ .
\]

\[
D(a,b,c)=168 a^{6} b^{4} + 768 a^{6} b^{3} c + 1032 a^{6} b^{2} c^{2} + 336 a^{6} b c^{3} + 339 a^{5} b^{5} + 2562 a^{5} b^{4} c + 5859 a^{5} b^{3} c^{2} + 4680 a^{5} b^{2} c^{3} + 1056 a^{5} b c^{4} + 168 a^{4} b^{6} + 2562 a^{4} b^{5} c + 9756 a^{4} b^{4} c^{2} + 13602 a^{4} b^{3} c^{3} + 7272 a^{4} b^{2} c^{4} + 1104 a^{4} b c^{5} + 768 a^{3} b^{6} c + 5859 a^{3} b^{5} c^{2} + 13602 a^{3} b^{4} c^{3} + 12723 a^{3} b^{3} c^{4} + 4584 a^{3} b^{2} c^{5} + 384 a^{3} b c^{6} + 1032 a^{2} b^{6} c^{2} + 4680 a^{2} b^{5} c^{3} + 7272 a^{2} b^{4} c^{4} + 4584 a^{2} b^{3} c^{5} + 960 a^{2} b^{2} c^{6} + 336 a b^{6} c^{3} + 1056 a b^{5} c^{4} + 1104 a b^{4} c^{5} + 384 a b^{3} c^{6}\ .
\]

`CHECK.py` reconstructs the polynomial identity by solving the original \(2\times2\) Sylvester system, then checks every nonzero numerator and denominator coefficient is strictly positive. For the comparison \(a\) versus \(c\), exchange the vertex labels that interchange the corresponding triangle edges, or use the separate exact symbolic check.
