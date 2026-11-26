# Fifteen rank-zero parameters and two quaternionic isomorphism classes in characteristic eleven

## Finding

Let \(k=\overline{\mathbf F}_{11}\). For \(a\in k\) with \(a^2\ne4\), let \(H_a\) be the smooth projective curve with equation
\[
y^2=x(x^4-1)(x^4+a x^2+1)=x^9+a x^7-a x^3-x.
\]
Its genus is four and its Jacobian has \(a\)-number two. The geometric \(11\)-rank is zero exactly at the roots of
\[
J(a)=a^{15}-2a^{13}-4a^{11}+a\in\mathbf F_{11}[a],
\]
and is two elsewhere. There are fifteen distinct roots, all smooth parameters. Twelve of them have full geometric automorphism group \(Q_8\) and form two geometric isomorphism classes. The other three, \(0,6,-6\), form one geometric isomorphism class with full automorphism group \(C_{16}\rtimes C_2\). None of these curves is superspecial.

## Assumptions and scope

Ranks and curve isomorphisms are geometric. The \(a\)-number is the genus minus the rank of Cartier on regular differentials. The \(11\)-rank of a Jacobian is the stable rank of Cartier, dual to Frobenius on \(H^1(H_a,\mathcal O_{H_a})\). The enumeration concerns this family only and does not determine Newton polygons or full Ekedahl–Oort types.

## Proof

The finite branch points are the nine roots of the defining polynomial. The factors are individually separable and mutually disjoint when \(a^2\ne4\): the quadratic in \(x^2\) then has distinct nonzero roots, and its sharing a root with \(x^4-1\) forces \(a=\pm2\). Infinity is the tenth branch point, giving genus four by Riemann–Hurwitz.

Write \(f_a(x)^5=\sum_t c_t x^t\). On the basis \(\omega_j=x^{j-1}dx/y\), one has \(\omega_j=y^{-11}x^{j-1}f_a(x)^5dx\). Cartier keeps the terms with exponent \(11i-1\) in the numerator differential, taking their coefficient eleventh roots. For a coefficient **column** \(v\), this gives
\[
\mathcal C(v)=(M v)^{(1/11)},\qquad M_{ij}=c_{11i-j}.
\]
Here the parenthesized exponents on matrices or vectors are entrywise. Expansion gives
\[
M=\begin{pmatrix}
0&a^2&0&6a\\
C&0&2aC&0\\
0&-2aC&0&-C\\
-6a&0&-a^2&0
\end{pmatrix},\qquad C=1-5a^2-3a^4.
\]
In the order \((1,3,2,4)\), write \(M=\begin{pmatrix}0&P\\Q&0\end{pmatrix}\), where
\[
 P=\binom{6a}{-C}(2a,1),\qquad Q=\binom{C}{-6a}(1,2a).
\]
Both blocks have rank one at every parameter: the row factors never vanish, and the column factors are nonzero by \(6a\ne0\) when \(a\ne0\) and \(C(0)=1\) otherwise. Thus Cartier has rank two and the \(a\)-number is two.

The second iterate is \(\mathcal C^2(v)=(M^{(11)}M v)^{(1/121)}\), with the order of the two factors determined by inverse-Frobenius semilinearity. The diagonal blocks of \(M^{(11)}M\) are \(P^{(11)}Q\) and \(Q^{(11)}P\). These are nonvanishing outer-product factors multiplied respectively by the scalars \(2a^{11}C-6a\) and its negative. In characteristic eleven, \(2a^{11}C-6a=5J(a)\). When \(J\) vanishes, Cartier squares to zero. Otherwise its first and second images have dimension two, so Cartier maps its first image onto itself and all its further iterates have rank two.

Polynomial Euclidean division over \(\mathbf F_{11}\) gives
\[
\gcd(J,J')=1,\qquad J(2)=-1,\quad J(-2)=1,\qquad
\gcd(J,a^2+12)=1,\quad \gcd(J,a(a^2-36))=a(a^2-36).
\]
The automorphism classification of Taniguchi–Ohashi–Takagi (arXiv:2505.00241, Corollary 3.1) gives \(\mathrm{SL}_2(\mathbf F_3)\) at \(a^2=-12\), \(C_{16}\rtimes C_2\) at \(0,6,-6\), and \(Q_8\) otherwise. Their Theorem 3.1 identifies precisely the isomorphic parameters by the six expressions
\[
\pm a,\qquad \pm\left(2-\frac{16}{a+2}\right),\qquad \pm\left(2+\frac{16}{a-2}\right).
\]
Evaluating at zero gives the three enhanced parameters. For each other root of \(J\), the six expressions are distinct: a gcd test with \(J/[a(a^2-36)]\) and each pairwise difference after clearing denominators gives one. The twelve remaining parameters therefore split into two classes. Since a superspecial genus-four Jacobian has \(a\)-number four, none of these is superspecial.

## Verification and relation to prior work

`python3 verify_frobenius.py` (Python 3 with SymPy) checks coefficient extraction, the second Cartier iterate, gcds, orbit size, and invariance of the root locus. The coefficient-only check `verify_coefficients.py` remains unchanged. The general automorphism classification is due to Kudo–Nakagawa–Takagi, https://arxiv.org/abs/2210.14822, Theorem C and Table 6. Taniguchi–Ohashi–Takagi, *Enumeration algorithm for genus-4 superspecial hyperelliptic curves with automorphism group \(Q_8\)*, https://arxiv.org/abs/2505.00241, provide the coefficient and parameter-equivalence framework and treat superspeciality. Ohashi–Kudo, *Computing superspecial hyperelliptic curves of genus 4 with automorphism group properly containing the Klein 4-group*, https://arxiv.org/abs/2312.16858, also treat superspeciality. The exact finite locus above uses the stable rank, not the rank-zero condition on the one-step Cartier operator used for superspeciality.
