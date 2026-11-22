# Complete characteristic-three Cartier strata of cyclic tetragonal genus-six curves

## Finding
Let \(k\) be algebraically closed of characteristic \(3\). Consider the smooth projective curve \(X\) with affine equation
\[
 y^4=f(x),\qquad f(x)=x^5+Ax^3+Bx^2+Cx+D,\qquad A,B,C,D\in k,
\]
where \(f\) is squarefree. Its genus is \(6\). Its geometric Jacobian \(3\)-rank \(\rho\) and Cartier \(a\)-number \(a\) are exactly
\[
\rho=2\mathbf1_{A\ne0}+2\mathbf1_{C\ne0}+\mathbf1_{C=0,\ B\ne0},\qquad
 a=\begin{cases}2&C\ne0,\\3&C=0.\end{cases}
\]
In particular the generic rank is \(4\), never \(5\) or \(6\), and all ranks from \(0\) through \(4\) occur. The **complete Cartier-power ranks** (starting with the first power) are:

| Conditions on coefficients (and squarefree \(f\)) | \(\rho\) | \(a\) | \(\operatorname{rank}(\mathcal C^n)\), \(n=1,2,3,4,\ldots\) |
|---|---:|---:|---|
| \(A\ne0,C\ne0\) | 4 | 2 | \(4,4,4,4,\ldots\) |
| \(A=0,C\ne0\) | 2 | 2 | \(4,3,2,2,\ldots\) |
| \(A\ne0,C=0,B\ne0\) | 3 | 3 | \(3,3,3,3,\ldots\) |
| \(A=0,C=0,B\ne0\) | 1 | 3 | \(3,2,1,1,\ldots\) |
| \(A\ne0,B=C=0\) | 2 | 3 | \(3,2,2,2,\ldots\) |
| \(A=B=C=0\) | 0 | 3 | \(3,1,0,0,\ldots\) |

## Assumptions and scope
All assertions are over an algebraically closed field of characteristic exactly \(3\); the polynomial must have five distinct roots, equivalently \(\gcd(f,f')=1\). The unique point above infinity is totally ramified, as are the five finite roots. Riemann–Hurwitz gives \(2g-2=4(-2)+6(4-1)=10\), hence \(g=6\). Every monic separable quintic can be translated uniquely to the displayed centered form: in characteristic \(3\) the coefficient of the fourth power under translation changes by twice the translation amount. This is the natural centered coefficient family, not a restriction to a special pencil.

We define \(\rho\) as the stable rank of the Cartier operator on regular differentials, and \(a\) as the dimension of its kernel (the Jacobian \(a\)-number). Cartier is semilinear; ranks, rather than arbitrary matrix entries, are intrinsic.

## Proof
A basis for \(H^0(X,\Omega_X^1)\) is
\[
\omega_0=dx/y,\quad \omega_1=dx/y^2,\quad\omega_2=x\,dx/y^2,\quad
\omega_3=dx/y^3,\quad\omega_4=x\,dx/y^3,\quad\omega_5=x^2\,dx/y^3.
\]
Indeed, at infinity \(\operatorname{ord}(x)=-4\), \(\operatorname{ord}(y)=-5\), and \(\operatorname{ord}(dx)=-5\); the six indicated forms have nonnegative orders, and the genus count shows they are a basis.

In characteristic three, \(\mathcal C(g^3\eta)=g\mathcal C(\eta)\) and \(\mathcal C(x^r dx)\) vanishes except for \(r\equiv2\pmod3\), when it equals \(x^{(r-2)/3}dx\). Using
\[
y^{-1}=f^2y^{-9},\qquad y^{-2}=fy^{-6},\qquad y^{-3}=y^{-3},
\]
write \(c^{1/3}\) for the unique cube root of \(c\in k\). Direct coefficient extraction gives:
\[
\begin{aligned}
\mathcal C(\omega_0)&=(C^2-BD)^{1/3}\omega_3-(D+AB)^{1/3}\omega_4+(-A)^{1/3}\omega_5,\\
\mathcal C(\omega_1)&=B^{1/3}\omega_1+\omega_2,\\
\mathcal C(\omega_2)&=C^{1/3}\omega_1,\\
\mathcal C(\omega_3)&=0,\quad\mathcal C(\omega_4)=0,\quad\mathcal C(\omega_5)=\omega_0.
\end{aligned}
\]
The coefficient identities behind the first line are \([x^2]f^2=C^2-BD\), \([x^5]f^2=-(D+AB)\), and \([x^8]f^2=-A\), all in characteristic three.

The invariant subspace \(\langle\omega_1,\omega_2\rangle\) has Cartier matrix, up to entrywise inverse Frobenius, \(\left(\begin{smallmatrix}B&C\\1&0\end{smallmatrix}\right)\). It has first rank two when \(C\ne0\), otherwise one. Its stable rank is two if \(C\ne0\), one if \(C=0,B\ne0\), and zero if \(B=C=0\). The complementary invariant subspace \(\langle\omega_0,\omega_3,\omega_4,\omega_5\rangle\) has first rank two because its displayed vector from \(\omega_0\) cannot vanish on the squarefree locus: vanishing forces \(A=D=C=0\), so \(f=x^2(x^3+B)\), contrary to separability. The only return arrow from the span of \(\omega_3,\omega_4,\omega_5\) goes from \(\omega_5\) to \(\omega_0\), with return coefficient \((-A)^{1/3}\). Thus if \(A\ne0\), all positive powers on this block have rank two; if \(A=0\), its first three power ranks are \(2,1,0\), and it is nilpotent of order three. Summing the ranks of these two blocks proves the entire table, the stable ranks, and the \(a\)-numbers.

All six strata contain smooth curves, witnessed by the following coefficient tuples \((A,B,C,D)\) over \(\mathbb F_3\), in table order:
\[
(1,0,1,1),\quad(0,0,1,0),\quad(1,1,0,2),\quad
(0,1,0,1),\quad(1,0,0,1),\quad(0,0,0,1).
\]
For each witness, direct Euclidean calculation gives \(\gcd(f,f')=1\); the standalone verifier checks these and the announced Cartier-power profiles. This proves nonemptiness over the algebraic closure and completes the classification.

## Verification
Run `python3 verify_cartier.py` with standard Python 3. The script independently recomputes the six-dimensional Cartier matrix from polynomial coefficient convolution, tests squarefreeness via Euclidean polynomial arithmetic, exhaustively evaluates all \(3^4=81\) centered coefficient tuples over \(\mathbb F_3\), and checks first-eight-power ranks, the predicted stable rank and \(a\)-number. There are 54 squarefree tuples in this finite test, covering all six strata. Exhaustive finite-field testing is a regression check, not the proof of the characteristic-three algebraically closed assertion, which is the symbolic coefficient/block argument above.

## Relationship to prior work
England–Eilbeck, *Abelian functions associated with a cyclic tetragonal curve of genus six*, arXiv:0806.2377 (2008), studies exactly the geometric \((4,5)\) family and provides the same six-dimensional differential space, but develops complex Abelian and sigma functions rather than positive-characteristic Cartier or \(3\)-rank strata. Bouw, *The \(p\)-Rank of Ramified Covers of Curves*, *Compositio Mathematica* 126 (2001), develops general tame cyclic-cover Hasse–Witt coefficients and generic-rank bounds; its large-characteristic hypothesis for generic maximality does not include the present \(p=3\), degree-four, six-branch-point case, and it does not give this complete stratification. Published computations on characteristic-seven or -eleven cyclic tetragonal curves involve different Frobenius congruence classes and often smaller parameter families, and do not imply the stated characteristic-three coefficient conditions. The present result is the explicit, complete small-characteristic Cartier-power stratification for the original full centered family.

## Limitations
The conclusions are restricted to the smooth separable-quintic locus over algebraically closed fields of characteristic \(3\); neither singular models nor other branch exponents of cyclic fourth-power covers are treated. The displayed coefficient strata are marked equations, not a classification of unmarked isomorphism classes. The formula determines Cartier iterates, geometric \(3\)-rank and \(a\)-number, not the complete Newton polygon or integral endomorphism ring. Although checked against identified literature, exhaustive historical novelty cannot be certified without independent expert review.

## References
1. M. England and J. C. Eilbeck, *Abelian functions associated with a cyclic tetragonal curve of genus six*, arXiv:0806.2377 (first submitted June 14, 2008), https://arxiv.org/abs/0806.2377.
2. I. I. Bouw, *The \(p\)-Rank of Ramified Covers of Curves*, *Compositio Mathematica* **126** (2001), 295–322, DOI: 10.1023/A:1017513122376; electronically available December 4, 2007, https://doi.org/10.1023/A:1017513122376.
