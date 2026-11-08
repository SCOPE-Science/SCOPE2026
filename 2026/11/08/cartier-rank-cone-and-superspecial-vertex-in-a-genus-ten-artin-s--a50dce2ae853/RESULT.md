# Cartier-rank cone and superspecial vertex in a genus-ten Artin–Schreier family

## Finding
Let \(k\) be an algebraically closed field of characteristic \(5\). For any \(a,b,c,d\in k\), let \(C_{a,b,c,d}\) denote the smooth projective model of
\[
y^5-y=x^6+a x^4+b x^3+c x^2+d x.
\]
Its genus is \(10\), and its Jacobian has \(5\)-rank zero. Define \(\Delta=b^2-ac+2a^3\). The exact ranks of the Cartier operator \(\mathcal C:H^0(C,\Omega_C^1)\to H^0(C,\Omega_C^1)\) are
\[
\operatorname{rank}\mathcal C=
\begin{cases}
4,&\Delta\ne0,\\
3,&\Delta=0\text{ and }(a,b,c)\ne(0,0,0),\\
0,&a=b=c=0.
\end{cases}
\]
Consequently, the Jacobian \(a\)-number \(\dim_k\ker\mathcal C\) is \(6,7,10\) in the respective cases. No \(a\)-number \(8\) or \(9\) occurs. The rank-jump hypersurface is the geometrically integral hypersurface \(b^2-ac+2a^3=0\) in the four-dimensional coefficient space; its singular scheme is supported precisely on the superspecial parameter line \(a=b=c=0\). The curve at each point of this line is isomorphic over \(k\) to the standard degree-six Hermitian model \(y^5-y=x^6\).

## Assumptions and scope
The field is algebraically closed of characteristic \(5\); all coefficients are unrestricted. The curve means the smooth projective normalization of the displayed affine model, not the possibly singular plane completion. The degree-six pole at infinity is fixed, and the equation is in standard one-pole Artin–Schreier normal form (the constant and degree-five terms have been removed). The stratification is an exact assertion for this marked parameter space, not a claim about the quotient by the full unmarked isomorphism relation.

## Proof
**Genus and regular forms.** The Artin–Schreier map has exactly one branch pole at infinity, of order \(6\) prime to \(5\). Riemann–Hurwitz gives \(g=(5-1)(6-1)/2=10\). The Deuring–Shafarevich formula gives \(5\)-rank \(0\). At the unique point at infinity, the pole orders of \(x\) and \(y\) are \(5\) and \(6\). The divisor of \(dx\) is \(18P_\infty\). Hence all monomials \(x^i y^j dx\) with \(5i+6j\le18\), \(0\le j\le3\), are regular; their pole orders and distinct \(k(x)\)-basis exponents show linear independence. There are exactly ten:
\[
\mathcal B=(dx,x\,dx,x^2dx,x^3dx,y\,dx,xy\,dx,x^2y\,dx,y^2dx,xy^2dx,y^3dx).
\]
As the genus is ten, this is a basis.

**Cartier matrix.** Write \(f=x^6+a x^4+b x^3+c x^2+d x\). Using \(y=y^5-f\), \(\mathcal C(g^5\omega)=g\mathcal C(\omega)\), and \(\mathcal C(x^{5m+4}dx)=x^m dx\), we obtain
\[
\mathcal C(x^iy^jdx)=\sum_{h=0}^j(-1)^{j-h}\binom jh y^h\mathcal C(x^i f^{j-h}dx).
\]
Since \(k\) is perfect, taking the fifth power of each Cartier-matrix entry does not change the rank. Indexing the above basis from \(0\) to \(9\), the entire nonzero-entry list of this fifth-power matrix \(M\) is
\[
\begin{array}{c|l}
\text{column}&(\text{row},M_{\text{row},\text{column}})\\ \hline
4&(0,-a)\\
5&(0,-b)\\
6&(0,-c)\\
7&(0,2bd+c^2),(1,2b),(4,-2a)\\
8&(0,2cd),(1,a^2+2c),(4,-2b)\\
9&(0,2cd^2),(1,2a^2d-abc-b^3-cd),(2,2a^2+2c),
(4,bd-2c^2),(5,b),(7,2a).
\end{array}
\]
All omitted entries vanish; the coefficients are interpreted in characteristic five. This list follows by selecting the coefficients of exponents congruent to \(4\pmod5\) in the relevant powers of \(f\); it is also independently reconstructed in `verify_cartier.py`.

**Rank calculation.** If \(a\ne0\), translate \(x\) by \(h=b/a\), then remove the resulting \(x^5\) term by an Artin–Schreier change of \(y\). The new coefficients of \(x^4,x^3,x^2\) are \((a,0,c')\) with \(c'=c-b^2/a\). This does not change the curve or Cartier rank. In the displayed matrix, columns \(4,7,9\) are independent because their images introduce, in order, nonzero rows \(0,4,7\); column \(8\) increases the rank precisely when \(a^2+2c'\ne0\). Every other column lies in their span, so the rank is \(3\) or \(4\). In characteristic five, \(a^2+2c'=0\) is equivalent to \(c'=2a^2\), namely \(\Delta=b^2-ac+2a^3=0\).

If \(a=0\) and \(b\ne0\), columns \(5,7,8,9\) are independent, by their successive nonzero rows \(0,1,4,5\), and all other columns are in their span. The rank is \(4\), while \(\Delta=b^2\ne0\). If \(a=b=0\) and \(c\ne0\), columns \(6,8,9\) have pivots in rows \(0,1,2\), and all others are in their span, so rank \(3\). Finally, if \(a=b=c=0\), every matrix entry vanishes, hence rank \(0\). This proves all three cases without any finite-field assumption.

**Geometry of the jump locus.** The polynomial change \(c'=c-2a^2\) transforms the equation \(\Delta=0\) into \(b^2-ac'=0\). This polynomial is irreducible in \(k[a,b,c']\) (it is primitive and linear in \(c'\) over the UFD \(k[a,b]\)); it defines an irreducible quadratic cone times the free affine \(d\)-line. Its derivatives with respect to \(a,b,c'\) are \(-c',2b,-a\), so its singular locus is exactly \(a=b=c'=0\), equivalently \(a=b=c=0\). The rank-zero stratum is therefore exactly the cone's singular line. For \(a=b=c=0\), a translation \(x\mapsto x+h\) and compensating Artin–Schreier linear change of \(y\) remove \(dx\) whenever \(h\) satisfies a polynomial equation \(u^{25}+u+d=0\) with \(u^5=h\), which has a solution in \(k\). Thus every vertex curve is isomorphic to the Hermitian model, as claimed.

## Verification
The standalone, standard-library-only program `verify_cartier.py` reconstructs the Cartier matrix from polynomial convolution and binomial coefficients without hard-coding the displayed matrix. It computes modular Gaussian ranks for all \(5^4=625\) coefficient tuples over \(\mathbb F_5\) and tests every translation by \(h\in\mathbb F_5\). It reports ranks \(0,3,4\) for \(5,120,500\) tuples respectively, and confirms \(3125\) translation checks, ending `ALL_CHECKS_PASSED`. The exact recorded terminal output appears in `verification_output.txt`. These finite computations are corroboration, not a proof of the theorem for arbitrary algebraically closed fields.

## Relationship to prior work
Pries–Zhu (2006) study \(p\)-rank strata of Artin–Schreier curves, not this finer Cartier-rank stratification inside a fixed \(p\)-rank-zero family. Farnell's 2010 thesis develops a Cartier-operator algorithm and includes related monomial examples and a degree-six basis picture; it does not in the inspected portions supply the full four-parameter cone equation or the three exact ranks. Farnell–Pries (2012) prove a constant-Cartier-rank theorem when \(p\equiv1\pmod L\), inapplicable to \(p=5\) and pole order \(L=6\). Pries–Weir (2013) analyze the Hermitian curve, corresponding here to the known rank-zero vertex, not the whole deformation locus. Montanucci–Speziali (2016) treat Fermat/Hurwitz families. Booher–Cais (2018/2020) give general Artin–Schreier bounds and examples with other pole orders, but their checked examples do not supply this precise cone stratification. The novelty assertion is therefore confined to the complete coefficient-level rank classification and the geometry of its jump locus, not to the classical Hermitian or general Artin–Schreier formulas.

## Limitations
This is a statement for the indicated normal form and marked one-pole cover. It does not calculate Newton polygons, complete Ekedahl–Oort types, moduli-stack multiplicities, or the orbit classification under all isomorphisms. The independent finite-field verifier does not establish the infinite-field claim by enumeration. Specialized historical literature or implicit computer tables could contain equivalent data; no independent historical-priority or scientific audit has been performed.

## References
- R. Pries and H. J. Zhu, *The p-rank stratification of Artin–Schreier curves*, arXiv:math/0609657 (first submitted 2006-09-22), https://arxiv.org/abs/math/0609657.
- S. Farnell, *Artin–Schreier Curves*, PhD dissertation (2010), https://mountainscholar.org/bitstreams/b29bf91f-4848-4aca-b33f-e67f23037554/download.
- S. Farnell and R. Pries, *Families of Artin–Schreier curves with Cartier–Manin matrix of constant rank*, arXiv:1202.4183 (first submitted 2012-02-19), https://arxiv.org/abs/1202.4183.
- R. Pries and C. Weir, *The Ekedahl–Oort type of Jacobians of Hermitian curves*, arXiv:1302.6261 (2013), https://arxiv.org/abs/1302.6261.
- M. Montanucci and P. Speziali, *The a-numbers of Fermat and Hurwitz curves*, arXiv:1603.03604 (2016), https://arxiv.org/abs/1603.03604.
- J. Booher and B. Cais, *a-numbers of curves in Artin–Schreier covers*, arXiv:1807.10313 (2018), https://arxiv.org/abs/1807.10313.
