# A zero-\(5\)-rank family with two Cartier strata among genus-six trigonal curves

## Finding

Let \(k\) be an algebraically closed field of characteristic \(5\). For every \(\lambda\in k\) such that \(\lambda^7\ne2\), let \(C_\lambda\) be the smooth projective model of
\[
y^3=x^7+\lambda x+1.
\]
Every \(C_\lambda\) has genus \(6\) and Jacobian \(5\)-rank zero. Yet the \(a\)-number and the ranks of the iterated Cartier operator vary *exactly* at \(\lambda=0\):

| Parameter | \(\operatorname{rank}(\mathcal C^r)\), \(0\le r\le6\) | \(a(C_\lambda)\) | Nilpotence index |
|---|---|---:|---:|
| \(\lambda=0\) | \((6,2,1,0,0,0,0)\) | \(4\) | \(3\) |
| \(\lambda\ne0,\ \lambda^7\ne2\) | \((6,4,3,2,1,0,0)\) | \(2\) | \(5\) |

Here \(\mathcal C\) acts on \(H^0(C_\lambda,\Omega^1)\), and its nilpotence index is the least positive integer \(r\) with \(\mathcal C^r=0\). In particular the entire smooth one-parameter family lies in the zero \(5\)-rank locus, although its \(a\)-number is not constant.

## Assumptions and scope

The assertion holds over the algebraic closure of \(\mathbb F_5\), for *every* smooth parameter, not only for parameters in a finite subfield. The equation defines a function field of degree \(3\) over \(k(x)\); the smooth projective normalization, rather than the singular naive plane model at infinity, is intended. The only singular branch-polynomial parameters are the seven roots of \(\lambda^7-2\). The invariant \(a(C)\) is \(\dim_k\ker\mathcal C\), equivalently the \(a\)-number of the Jacobian. The \(5\)-rank is the stable Cartier rank.

## Proof

**(1) Smooth locus and genus.** Set \(f_\lambda(x)=x^7+\lambda x+1\). Since \(f'_\lambda(x)=2x^6+\lambda\), a common root \(\xi\) of \(f_\lambda\) and \(f'_\lambda\) satisfies \(\lambda=3\xi^6\), hence \(\xi^7=1\) and \(\lambda^7=3^7=2\) in characteristic \(5\). Conversely, if \(\lambda^7=2\), then \(\xi=3/\lambda\) satisfies both equations. Thus \(f_\lambda\) is squarefree exactly when \(\lambda^7\ne2\). For such \(\lambda\), the cyclic degree-three map \(x:C_\lambda\to\mathbb P^1\) ramifies totally at the seven simple roots and at infinity. Riemann--Hurwitz gives \(2g-2=3(-2)+8(3-1)=10\), so \(g=6\), and the curve is geometrically integral.

**(2) A regular differential basis.** With \(e_1=dx/y\), \(e_2=x\,dx/y\), \(e_3=dx/y^2\), \(e_4=x\,dx/y^2\), \(e_5=x^2\,dx/y^2\), and \(e_6=x^3\,dx/y^2\), each differential is holomorphic. Indeed, near a simple root of \(f_\lambda\), \(dx/y^j\) is a unit times \(y^{2-j}dy\) for \(j=1,2\). At the unique point at infinity, \(v(x)=-3\), \(v(y)=-7\), and \(v(dx)=-4\), so the displayed basis differentials have nonnegative valuations. Their different \(x\)-exponents and \(y\)-characters give linear independence; because there are six of them, they are a basis of \(H^0(C_\lambda,\Omega^1)\).

**(3) Exact Cartier matrix.** The Cartier rule \(\mathcal C(h^5x^{5b-1}dx)=h x^{b-1}dx\), together with \(y^{-j}=y^{-5j'}f_\lambda(x)^c\), where \(j'\in\{1,2\}\) satisfies \(5j'\equiv j\pmod3\) and \(c=(5j'-j)/3\), reduces each column to coefficients of \(f_\lambda^c\). Here \((j,j',c)=(1,2,3)\) or \((2,1,1)\). In the ordered basis \((e_1,\ldots,e_6)\), the matrix entries \(H_{ij}\) defined by
\[
\mathcal C(e_j)=\sum_{i=1}^6 H_{ij}^{1/5} e_i
\]
are exactly
\[
H_\lambda=\begin{pmatrix}
0&0&0&0&0&\lambda\\
0&0&0&0&1&0\\
0&\lambda^3&0&0&0&0\\
3\lambda^2&\lambda&0&0&0&0\\
3&0&0&0&0&0\\
0&0&0&0&0&0
\end{pmatrix}.
\]
Each entry follows by extracting the coefficient of \(x^{5b-a}\) in \(f_\lambda^{(5j'-j)/3}\), where the source differential is \(x^{a-1}dx/y^j\) and the target is \(x^{b-1}dx/y^{j'}\). The fifth roots are unique in the perfect field \(k\). In particular, the matrix is *not* to be iterated as an ordinary linear matrix over a nonprime subfield: Cartier is \(1/5\)-semilinear.

**(4) Exact ranks for every parameter.** If \(\lambda=0\), then \(\mathcal C(e_1)=3e_5\), \(\mathcal C(e_5)=e_2\), and \(\mathcal C(e_2)=0\), while the other three basis vectors are killed. Thus the successive image dimensions are \((6,2,1,0,0,0,0)\).

Suppose now \(\lambda\ne0\). The matrix gives \(\mathcal C(e_6)=\lambda^{1/5}e_1\), \(\mathcal C(e_1)=3\lambda^{2/5}e_4+3e_5\), \(\mathcal C(e_5)=e_2\), and \(\mathcal C(e_2)=\lambda^{3/5}e_3+\lambda^{1/5}e_4\), with \(\mathcal C(e_3)=\mathcal C(e_4)=0\). The five vectors \(e_6,\mathcal C(e_6),\ldots,\mathcal C^4(e_6)\) are linearly independent, because they have respective nonzero leading components in \(e_6,e_1,e_5,e_2,e_3\); adjoining \(e_4\) yields a basis. In this basis, the semilinear Cartier action consists of one nilpotent chain of length five and one killed vector. This proves the rank profile \((6,4,3,2,1,0,0)\), including the asserted nilpotence index. Nonvanishing of the coefficients is all that is required, so the conclusion applies to **every** nonzero smooth \(\lambda\) over \(k\).

Since both profiles terminate at zero, the Jacobian \(5\)-rank is zero throughout the smooth family. Finally \(a(C_\lambda)=6-\operatorname{rank}\mathcal C\), which yields \(4\) at zero and \(2\) elsewhere. This completes the proof.

## Verification

The standalone Python program `verify_genus6_deformation.py` expands the relevant powers of \(1+\lambda x+x^7\) as polynomials in two indeterminates modulo \(5\), verifying all six nonzero entries of \(H_\lambda\) and all its remaining zero entries without using a symbolic algebra package. Independently, it implements \(\mathbb F_{25}=\mathbb F_5[z]/(z^2+2)\), enumerates all 25 parameters, excludes the single singular one \(\lambda=3\), computes each Cartier matrix and all semilinearly twisted powers, and checks their exact ranks by finite-field elimination. The 24 smooth parameters consist of one exceptional \(\lambda=0\) and 23 with the generic profile. To reproduce: run `python3 verify_genus6_deformation.py` with Python 3 and no external dependencies. Successful completion prints `GENUS6_TRIGONAL_DEFORMATION_F25_CARTIER_PASS`.

The infinite-field assertion is proved by the symbolic matrix and basis-chain argument, **not** by extrapolation from the finite-field enumeration.

## Relationship to prior work

Borges--Gonçalves establish general \(p\)-rank formulas for Fermat-type curves \(y^m=x^n+1\), including the undeformed member at \(\lambda=0\); their Theorem 3.1 and proof concern stable Cartier ranks, not this coefficient-dependent family or the two full iterate profiles. Pries--Ulmer determine richer \(p\)-torsion information for Fermat curves and selected Fermat quotients; that broader theory must be considered for the undeformed member, but the source does not provide this stratification under the added linear perturbation. Nourozi--Rahmati give Cartier ranks for certain degree-four Picard models, while Montanucci--Speziali treat Fermat and Hurwitz curves. Those investigations motivate, but do not state, the positive-dimensional smooth characteristic-five stratum described here. The family specializes to a classical Fermat-type curve, so its exact \(a\)-number jump is a deformation-sensitive refinement rather than a claim of novelty for the special fiber's existence or \(p\)-rank.

## Limitations

This theorem applies only to the displayed genus-six one-parameter family in characteristic \(5\). It does not classify all zero-\(5\)-rank trigonal curves, prove supersingularity of the Jacobians, determine Newton polygons or full Ekedahl--Oort types, or assert that the family is a universal deformation. Priority risk remains from differently parameterized trigonal-curve computations or older unindexed Cartier matrices.

## References

1. Herivelto Borges and Cirilo Gonçalves, *The p-rank of curves of Fermat type*, arXiv:2212.03987, first posted 2022-12-07. https://arxiv.org/abs/2212.03987
2. Rachel Pries and Douglas Ulmer, *On BT_1 group schemes and Fermat Jacobians*, arXiv:2010.15160, first posted 2020-10-28. https://arxiv.org/abs/2010.15160
3. Vahid Nourozi and Farhad Rahmati, *The Rank of the Cartier operator on Picard Curves*, arXiv:2306.07823, first posted 2023-06-13. https://arxiv.org/abs/2306.07823
4. Maria Montanucci and Pietra Speziali, *The a-numbers of Fermat and Hurwitz curves*, arXiv:1603.03604, first posted 2016-03-11. https://arxiv.org/abs/1603.03604
5. Elisa Lorenzo García, *Twists of non-hyperelliptic curves*, arXiv:1503.03281, first posted 2015-03-11. https://arxiv.org/abs/1503.03281
