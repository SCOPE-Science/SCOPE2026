# Centralizer rank spectra and a stable commuting law for finite Schrödinger Lie algebras

## Finding

**Theorem.** Let \(q\) be an odd prime power and \(n\ge1\). The \((2n+4)\)-dimensional Schrödinger Lie algebra \(L=\mathfrak{sch}_n(\mathbb F_q)\) has the complete element-centralizer distribution in the following table. Write an element as \(a=(X,v,c)\), where \(X\in\mathfrak{sl}_2(\mathbb F_q)\), \(v\in V=(\mathbb F_q^2)^{\oplus n}\), and \(c\in\mathbb F_q\). For \(X=0\), the rank of \(v\) means the dimension of the span of its \(n\) columns in \(\mathbb F_q^2\).

| Disjoint type | \(\dim_{\mathbb F_q}C_L(a)\) | Number of elements of this type |
| --- | ---: | ---: |
| \(X=0,\ v=0\) | \(2n+4\) | \(q\) |
| \(X=0,\ \operatorname{rank}(v)=1\) | \(2n+1\) | \(q(q+1)(q^n-1)\) |
| \(X=0,\ \operatorname{rank}(v)=2\) | \(2n\) | \(q(q^n-1)(q^n-q)\) |
| \(X\ne0\) nilpotent, \(v\in\ker X_V\) | \(n+2\) | \(q(q^2-1)q^n\) |
| \(X\ne0\) nilpotent, \(v\notin\ker X_V\) | \(n+1\) | \(q(q^2-1)(q^{2n}-q^n)\) |
| \(X\) invertible | \(2\) | \(q(q^3-q^2)q^{2n}\) |

Here \(X_V\) is the diagonal action of \(X\) on \(V\). The six types partition the algebra; a type can be empty, and equal centralizer dimensions are combined by adding the table counts.

If \(A,B\) are independent uniformly distributed elements of \(L\), then the **exact finite-field commuting probability** is

\[
\Pr([A,B]=0)=q^{-7}+(q^{-4}+q^{-5}-q^{-6}-q^{-7})q^{-n}+(q^{-2}+q^{-3}-q^{-4}-2q^{-5}+q^{-6})q^{-2n}.
\]

For every fixed odd \(q\), this tends to \(q^{-7}>0\) as \(n\to\infty\), with an explicit first-order correction of order \(q^{-n}\). The corresponding adjoint ranks are obtained by subtracting the listed centralizer dimensions from \(2n+4\).

## Assumptions and scope

Let \(V=\bigoplus_{i=1}^n\mathbb F_q^2\) with its nondegenerate alternating form \(\omega(v,w)=\sum_{i=1}^n(v_{x_i}w_{y_i}-v_{y_i}w_{x_i})\). Let \(\mathfrak{sl}_2(\mathbb F_q)\) act on \(V\) by the standard representation on each summand. The bracket on \(L=\mathfrak{sl}_2\oplus V\oplus\mathbb F_qz\) is

\[
[(X,v,c),(Y,w,d)]=([X,Y],X_Vw-Y_Vv,\omega(v,w)z).
\]

This normalization agrees with the standard Heisenberg generators having \([x_i,y_j]=\delta_{ij}z\). All elements, including the zero element and all scalar multiples of \(z\), are counted, and ordered commuting pairs are counted with repetition. Only odd characteristic is asserted; no statement in characteristic two is claimed.

## Proof

**Centralizer equations.** An element \((Y,w,d)\) centralizes \((X,v,c)\) exactly when \([X,Y]=0\), \(X_Vw=Y_Vv\), and \(\omega(v,w)=0\). The coordinate \(d\) is always free.

**Case \(X=0\).** If \(v=0\), everything commutes, giving dimension \(2n+4\). If \(v\ne0\), the equation \(Y_Vv=0\) constrains the three-dimensional \(\mathfrak{sl}_2\)-coordinate, while \(\omega(v,w)=0\) is a nonzero linear functional on \(V\). If the component vectors of \(v\) span a line in \(\mathbb F_q^2\), their common annihilator in \(\mathfrak{sl}_2\) is one-dimensional; if they span the whole two-space, it is zero. The resulting centralizer dimensions are \(2n+1\) and \(2n\). Nonzero rank-one \(2\times n\) matrices number \((q+1)(q^n-1)\); rank-two matrices number \((q^n-1)(q^n-q)\). Multiplication by the \(q\) free central coordinates gives the first three table entries.

**Case \(X\ne0\).** Every nonzero trace-zero \(2\times2\) matrix over a field of odd characteristic has a one-dimensional Lie centralizer within \(\mathfrak{sl}_2\), so \(Y=tX\). The vector equation becomes \(X_V(w-tv)=0\); hence \(w=tv+u\) with \(u\in\ker X_V\). The remaining equation is \(\omega(v,u)=0\). If \(\det X\ne0\), then \(\ker X_V=0\), leaving exactly two free scalar coordinates \(t,d\).

If \(X\ne0\) is nilpotent, then \(\ker X_V\) is an \(n\)-dimensional Lagrangian subspace of \(V\). Its symplectic annihilator is itself. Accordingly, the linear functional \(u\mapsto\omega(v,u)\) on \(\ker X_V\) vanishes identically if and only if \(v\in\ker X_V\); otherwise it has a one-dimensional image. The centralizer dimensions are respectively \(n+2\) and \(n+1\), including the two free scalars \(t,d\). There are \(q^2-1\) nonzero nilpotent matrices in \(\mathfrak{sl}_2(\mathbb F_q)\) and \(q^3-q^2\) invertible ones. For each nilpotent matrix, the two kinds of vector coordinates number \(q^n\) and \(q^{2n}-q^n\), respectively. Including the arbitrary central coordinate gives the remaining three table entries.

**Probability.** Summing \(q^{\dim C_L(a)}\) over all the table entries gives the number of ordered commuting pairs; division by \(|L|^2=q^{4n+8}\) and expansion yields the displayed expression. The coefficient of \(q^{-n}\) is positive for every odd \(q\), and the coefficient of \(q^{-2n}\) is also positive for such \(q\). This proves convergence from above to \(q^{-7}\) and its first-order correction.

## Verification

The standalone file `check.py` constructs the Lie bracket directly in the basis \((h,e,f,x_1,y_1,\ldots,x_n,y_n,z)\), builds each adjoint matrix, and computes its rank by modular Gaussian elimination. Running `python3 check.py` exhaustively checks all algebra elements for the parameters \((q,n)=(3,1),(5,1),(3,2)\). It compares the complete centralizer-size multiset and total commuting-pair count independently with the six-type formula. Successful output ends in `VERIFY_OK`. These finite checks corroborate, but do not replace, the general proof.

## Relationship to prior work

Sosnov [1] defines precisely this Schrödinger Lie algebra and proves a criterion for Lie bracket width one and uniqueness of addition. Its Section 2 supplies the relations used here, but its main theorems do not give an elementwise centralizer census or a commuting probability. Fulman and Guralnick [2] develop finite-field commuting-pair enumerations for classical matrix Lie algebras; they do not state this semidirect Heisenberg-extension formula. The result here is an exact distribution for a different, nonreductive perfect Lie algebra with nonzero center; the width-one result is credited, not claimed as new.

## Limitations

Odd finite field characteristic is essential to the centralizer argument as stated; the behavior in characteristic two is not addressed. The six structural rows need not represent six distinct numerical centralizer dimensions for small \(n\). Computational checks cover prime fields \(q=3,5\), not every extension field, and the unrestricted theorem follows from the algebraic proof. Literature priority is provisional: unindexed equivalent formulas for semidirect products or other treatments of Schrödinger centralizers may exist. No independent mathematical audit has been performed.

## References

1. G. Sosnov, *Uniqueness of addition in Schrödinger algebras*, arXiv:2611.16812v1 (12 November 2026), https://arxiv.org/html/2611.16812v1.
2. J. Fulman and R. Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields*, arXiv:1611.05499 (16 November 2016), https://arxiv.org/abs/1611.05499.
