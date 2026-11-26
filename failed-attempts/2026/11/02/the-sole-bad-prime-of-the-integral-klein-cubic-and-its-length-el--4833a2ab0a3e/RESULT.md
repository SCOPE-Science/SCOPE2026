# The sole bad prime of the integral Klein cubic and its length-eleven singular scheme

## Finding
Let \(\mathcal K\subset\mathbb P^4_{\mathbb Z}\) be the cubic hypersurface defined by
\[
F=\sum_{i\in\mathbb Z/5\mathbb Z}x_i^2x_{i+1}=0.
\]
Every geometric fiber is smooth except the fiber in characteristic \(11\). The exceptional fiber has exactly one geometric singular point, the \(\mathbb F_{11}\)-rational point
\[
P=[1:3:9:5:4].
\]
Its entire projective singular *scheme* is supported at \(P\), has length \(11\), and its local Artin algebra is
\[
\mathcal O_{\operatorname{Sing}(\mathcal K_{\mathbb F_{11}}),P}
\simeq\mathbb F_{11}[t]/(t^{11}).
\]
The affine-chart Hessian at \(P\) has rank \(3\) in the four ambient parameters, so the unique singularity has multiplicity two and quadratic tangent cone of corank one, rather than being an ordinary node. The exceptional fiber is geometrically integral and normal. Thus the set of base primes with smooth geometric fibers is exactly \(\operatorname{Spec}\mathbb Z[1/11]\).

## Assumptions and scope
The displayed homogeneous polynomial has integral coefficients; reduction is coefficientwise, without changing the integral model. All smoothness and singularity assertions concern hypersurface fibers over algebraically closed residue fields, not a modular compactification or a different model. The local algebra is the Tjurina/Jacobian singular-scheme algebra \(\mathcal O/(f,\partial f)\); its length is not asserted to equal a characteristic-zero topological Milnor number.

## Proof
Write the five homogeneous partial derivatives cyclically:
\[
F_i=x_{i-1}^{2}+2x_ix_{i+1}.
\]
In characteristic two these are the five squares \(x_{i-1}^2\), hence have no common projective zero. In any other characteristic, a common zero of the partial derivatives has all five coordinates nonzero: \(x_i=0\) forces \(x_{i-1}=0\), and iteration forces the zero vector. Multiplying the five relations \(x_{i-1}^{2}=-2x_ix_{i+1}\) therefore yields
\[
1=(-2)^5,
\]
which can hold in positive characteristic only for the primes dividing \((-2)^5-1=-33\), namely \(3\) and \(11\). It cannot hold in characteristic zero.

In characteristic three set \(x_0=1\), \(u=x_1\). From \(F_1=F_2=F_3=0\) one obtains \(x_2=u^{-1}\), \(x_3=u^3\), \(x_4=u^{-5}\). The remaining gradient equation imposes \(u^{11}=1\). But on these solutions the original cubic has value
\[
F=u+u^{-10}=2u\ne0
\]
in characteristic three. Thus no point of the cubic is singular in characteristic three, even over an algebraic closure.

In characteristic eleven put \(a=-2=9\), again normalize \(x_0=1\) and put \(u=x_1\). The first three chart gradient equations successively give
\[
x_2=(9u)^{-1},\qquad x_3=u^3,\qquad x_4=(9^3u^5)^{-1}.
\]
All these coordinates are units in the local critical locus. Since \(9^5=1\) in \(\mathbb F_{11}\), direct substitution into the fourth chart derivative and the cubic gives the *exact Laurent identities*
\[
F_4=\frac{u^{11}-3}{u^5},\qquad
F=\frac{2(u^{11}-3)}{u^{10}}.
\]
Consequently, the chart singular scheme is
\[
\operatorname{Spec}\frac{\mathbb F_{11}[u,u^{-1}]}{(u^{11}-3)}.
\]
In characteristic eleven, \(u^{11}-3=(u-3)^{11}\), so this is precisely \(\operatorname{Spec}\mathbb F_{11}[t]/(t^{11})\). There are no singular points on \(x_0=0\), by the nonvanishing argument above. Substitution at \(u=3\) yields \(P=[1:3:9:5:4]\).

The Hessian of the dehomogenized polynomial \(F(1,x_1,x_2,x_3,x_4)\) at \(P\), modulo eleven, is
\[
H=\begin{pmatrix}
7&6&0&0\\6&10&7&0\\0&7&8&10\\0&0&10&2
\end{pmatrix}.
\]
Its determinant is zero, while the leading principal \(3\times3\) minor is \(6\) modulo eleven. Its rank is therefore three. The singular point has multiplicity two and a rank-three quadratic tangent cone.

Finally, a reducible or nonreduced projective cubic threefold in \(\mathbb P^4\) necessarily has a positive-dimensional geometric singular locus (components intersect in a surface, or a repeated component is everywhere singular). Since this fiber has only \(P\), it is geometrically integral. As a hypersurface it is Cohen--Macaulay and smooth in codimension one, hence normal by Serre's criterion. All other geometric fibers are smooth by the preceding analysis.

## Verification
Run \`python3 verify_klein11.py\` using Python's standard library. It checks every projective \(\mathbb F_p\)-point for \(p=2,3,5,7,11\), the rational singular support, the characteristic-eleven Laurent identities at every nonzero base-field parameter, and the Hessian rank. The proof above, rather than those finite samples, establishes smoothness for every prime and uniqueness over every algebraic closure. The algebraic local-length certificate is the exact Laurent elimination with \(u^{11}-3=(u-3)^{11}\).

## Relationship to prior work
The integral cyclic cubic is the classical Klein cubic, which Gross and Popescu identify as a birational model of a moduli space of \((1,11)\)-polarized abelian surfaces in characteristic zero. Roulleau analyzes the smooth complex cubic and its Fano surface. Neither inspected treatment establishes the precise coefficientwise reduction, the single geometric bad prime, or the length-eleven nonreduced singular scheme. This observation does *not* extend the moduli interpretation over characteristic eleven. Searches of mathematical records found no equivalent claim, but an unindexed or historical calculation could predate this one.

## Limitations
No resolution of the exceptional singularity, stable reduction, zeta function, or associated moduli stack is determined. Rank three of the Hessian excludes an ordinary double point; it is not offered as a complete analytic normal form. Historic novelty has not been independently certified. This is a result about the specified integral equation, not every integral form of the Klein cubic.

## References
1. M. Gross and S. Popescu, *The moduli space of (1,11)-polarized abelian surfaces is unirational*, arXiv:math/9902017 (first posted 1999-02-02), especially the defining cyclic equation and introduction. https://arxiv.org/html/math/9902017v1
2. X. Roulleau, *The Fano surface of the Klein cubic threefold*, MPIM Preprint 2008 (13); arXiv:1001.4853 (posted 2010-01-27). https://archive.mpim-bonn.mpg.de/id/eprint/2370/1/preprint_2008_13.pdf
3. A. Adler, *On the automorphism group of a certain cubic threefold*, American Journal of Mathematics 100 (1978), 1275--1280; contextual classical source.
