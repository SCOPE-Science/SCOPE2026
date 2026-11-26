# Explicit Euclidean mass and strict barycentric majorization for simplex Hilbert balls

## Finding

Let \(S\) be a nondegenerate Euclidean simplex with \(n\ge2\) vertices. For an interior center with barycentric coordinates \(x=(x_1,\dots,x_n)\), and a uniform Euclidean-volume point \(Y\) in \(S\), define \(Q_n(x,r)=\Pr(d_H(x,Y)\le r)\). Use the logarithm of the Hilbert cross-ratio, without a factor of one half. For every \(r>0\), with \(c=e^r-1\),
\[
Q_n(x,r)=\frac{1+c}{c}\int_0^\infty e^{-s}\prod_{i=1}^n(1-e^{-c x_is})\,ds
=\frac{1+c}{c}\sum_{A\subseteq\{1,\dots,n\}}\frac{(-1)^{|A|}}{1+c\sum_{i\in A}x_i}.
\]
For fixed \(r>0\) this function is strictly Schur-concave in the **barycentric coordinates**: if \(x\) majorizes \(z\), then \(Q_n(x,r)\le Q_n(z,r)\), with equality precisely for permutations. At fixed interior \(x\) the resulting small-radius law is \(Q_n(x,r)\sim n!r^{n-1}\prod_i x_i\).

The mass here is a ratio of Euclidean volumes in the affine span of \(S\), not an intrinsic Busemann or Holmes–Thompson measure. The result addresses every interior center, rather than just calculating the maximum mass or identifying its center.

## Proof

Affine maps preserve both the cross-ratio and the normalized Euclidean volume. On the probability simplex, with \(q_i=y_i/x_i\), the two line-boundary parameters for \(x+t(y-x)\) are \(1/(1-\max_i q_i)\) and \(1/(1-\min_i q_i)\) for \(x\ne y\). They yield \(d_H(x,y)=\log(\max_i q_i/\min_i q_i)\); the same formula gives zero for \(x=y\).

The normalized vector of \(n\) independent unit-rate exponentials \(E_i\) has uniform simplex law. This follows by changing variables \(E_i=T Y_i\), with Jacobian \(T^{n-1}\) when using \(Y_1,\dots,Y_{n-1}\); the joint density depends only on \(T\). Thus the ratio event is equivalent to \(\max_i Z_i\le(1+c)\min_i Z_i\), where \(Z_i=E_i/x_i\) are independent exponentials of rates \(x_i\). Ties are null. The term for \(Z_i=s\) giving the minimum and all other variables lying between \(s\) and \((1+c)s\) has density
\[
x_i e^{-s}\prod_{j\ne i}(1-e^{-c x_js}).
\]
With \(P(s)=\prod_i(1-e^{-cx_i s})\) the sum of these densities is \(e^{-s}[P(s)+P'(s)/c]\). Here the identity uses \(\sum_i x_i=1\). Integrating by parts, using \(P(0)=0\) and boundedness of \(P\), yields the integral formula. Finite expansion of the product yields the rational formula.

For each \(s>0\), \(u\mapsto\log(1-e^{-csu})\) has second derivative \(-(cs)^2e^{csu}/(e^{csu}-1)^2<0\). Strict Karamata implies the stated product inequality at every \(s>0\), strictly for non-permutation comparisons. Integration preserves strictness. As \(c\downarrow0\), divide each factor by \(c x_i s\) and apply dominated convergence to the product against \(e^{-s}s^n\). The resulting integral is \(n!\); using \(c\sim r\) proves the small-radius coefficient.

## Relation to established results

The Hilbert distance in simplex coordinates and the ball shape are established (Foertsch–Karlsson, arXiv:math/0407197, Theorems 1–2; Nielsen–Sun, arXiv:1704.00454, §3). Vernicos (arXiv:1207.1142) studies intrinsic Hilbert volume instead. The earlier [exact central-ball and distance law](https://github.com/Resultary/2026/blob/main/2026/11/1/SCOPE-exact-uniform-hilbert-geometry-of-simplices-central-balls-median--185776c2c88a/RESULT.md) already gives the unique optimal centroid, the exact central mass, and the centroid-anchored Gumbel limit. Its central product equals \((n/c)B(n/c,n)\), recovered here by substituting \(e^{-cs/n}\) at equal coordinates. None of these central conclusions is claimed as new. That earlier record's positional log-concavity proof uses centered **logarithmic** coordinates and a convolution; the present ordering compares the barycentric coordinates themselves and the integral evaluates the Euclidean mass away from the centroid.

## Reproducibility and scope

The supplied `check.py` (NumPy/SciPy) includes quadrature, direct sampling, checks at unequal centers, pair balancings, and short-radius checks. Its beta and Gumbel comparisons concern the established central special case. These finite checks do not replace the analytical proof. The measure, metric convention, interior-center condition and simplex restriction are essential to the statements above.
