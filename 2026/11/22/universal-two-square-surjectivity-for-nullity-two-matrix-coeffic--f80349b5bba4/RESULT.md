# Universal two-square surjectivity for nullity-two matrix coefficients

## Finding

**Theorem.** Let \(F\) be an algebraically closed field of characteristic zero, let \(n\ge7\), and let \(A_1,A_2\in M_n(F)\) satisfy \(A_1\in\mathrm{GL}_n(F)\) and \(\operatorname{nullity}(A_2)=2\). Then the matrix polynomial map

\[
\omega:M_n(F)^2\longrightarrow M_n(F),\qquad
\omega(X,Y)=A_1X^2+A_2Y^2
\]

is surjective. Equivalently, **every** target matrix \(C\) has a decomposition \(C=A_1X^2+A_2Y^2\), without restrictions on the Jordan form of \(A_2\). This settles the \(k=2\) case of Question 6.1 in [1] for every order \(n\ge7\). In fact the proof establishes the same statement for \(n\ge3\); those smaller orders were already covered by [1,2].

## Assumptions and scope

All matrices and ranks are over an algebraically closed field \(F\) of characteristic zero. A square root of a matrix \(N\) means an \(X\) with \(X^2=N\); a *right full-row-rank* matrix of shape \(s\times n\) has row rank \(s\). Throughout, put \(s=n-2\), and write \(e_i\) for the \(i\)-th coordinate column vector; \(E_{ij}=e_ie_j^{\mathsf T}\). The only newly asserted range is \(n\ge7\). No assertion is made for exponents \(k>2\), positive characteristic, or general non-algebraically-closed fields.

## Proof

**Step 1 (coefficient and row reduction).** Multiplying the target on the left by \(A_1^{-1}\), reduce to \(X^2+BY^2=C\), where \(B=A_1^{-1}A_2\) has rank \(s\). Choose a basis with \(\operatorname{im}B=\langle e_1,\ldots,e_s\rangle\). Conjugation by the same invertible matrix on \(B,C,X,Y\) preserves the desired equation. In this basis

\[
B=\begin{pmatrix}D\\0_{2\times n}\end{pmatrix},\qquad
C=\begin{pmatrix}C_0\\L\end{pmatrix},\qquad
D\in F^{s\times n},\quad\operatorname{rank}D=s.
\]

**Step 2 (full-row-rank lifting).** For any \(H\in F^{s\times n}\) with \(\operatorname{rank}H=s\), there is \(Y\in M_n(F)\) with \(DY^2=H\). Indeed, \(D\) and \(H\) are surjective linear maps \(F^n\to F^s\); extend respective row frames to invertible matrices to obtain \(T\in\mathrm{GL}_n(F)\) satisfying \(DT=H\). Every invertible matrix over an algebraically closed field of characteristic zero has a square root: on a Jordan block \(\lambda I+J\), \(\lambda\ne0\), take the finite truncation of \(\sqrt\lambda(1+J/\lambda)^{1/2}\). Choose \(Y\) with \(Y^2=T\). Hence we need only a square \(N=X^2\) whose last two rows are \(L\), such that the top \(s\) rows of \(C-N\) have rank \(s\).

**Step 3 (two independent prescribed rows).** Suppose \(\operatorname{rank}L=2\). Let \(Z\) vary freely in \(F^{s\times n}\), and set \(N(Z)=\binom ZL\). The polynomial \(\det N(Z)\) is not identically zero, because \(L\) can be completed to an invertible matrix. The polynomial equal to the determinant of *some fixed* \(s\times s\) minor of \(C_0-Z\) is not identically zero, because \(Z\) is arbitrary and one can choose such a minor to equal the identity. Their product is a nonzero polynomial, so over the infinite field \(F\) it is nonzero for some \(Z\). Thus \(N(Z)\) is invertible and hence a square, while \(H=C_0-Z\) has rank \(s\). Apply Step 2.

**Step 4 (zero prescribed rows).** If \(L=0\), take

\[
N(t)=t\sum_{j=1}^{s}E_{jj}\qquad(t\ne0).
\]

It is the square of \(\sqrt t\sum_{j=1}^{s}E_{jj}\), and its bottom two rows vanish. The determinant of the first \(s\) columns of \(C_0-N(t)\) has leading term \((-t)^s\); hence for generic nonzero \(t\) the top residual has full row rank.

**Step 5 (rank-one row normal forms).** Suppose \(\operatorname{rank}L=1\). Conjugations by invertible matrices stabilizing \(\langle e_1,\ldots,e_s\rangle\) preserve the block form of \(B\) and transform \(L\) by \(L\mapsto R^{-1}LS\), with \(S=\begin{pmatrix}P&Q\\0&R\end{pmatrix}\). Write \(L=u\ell\), a nonzero column \(u\in F^2\) times a nonzero row \(\ell\in (F^n)^*\). If \(\ell\) is nonzero on the first \(s\) coordinates, choosing \(P,R,Q\) puts \(L\) into the form \(\binom{e_1^{\mathsf T}}0\). If \(\ell\) vanishes on those coordinates, the induced bottom-right \(2\times2\) block has rank one and is conjugate either to \(\operatorname{diag}(\lambda,0)\) for \(\lambda\ne0\), or to the nilpotent block \(E_{12}\). Hence three forms exhaust all possibilities:

\[
\text{(I)}\ \binom{e_1^{\mathsf T}}0,\qquad
\text{(II)}\ \binom{\lambda e_{s+1}^{\mathsf T}}0\ (\lambda\ne0),\qquad
\text{(III)}\ \binom{e_n^{\mathsf T}}0.
\]

In form (I), choose \(a\in F\) with \(a\ne(C_0)_{11}\), and set

\[
N(t)=aE_{11}+E_{1,s+1}+E_{s+1,1}
+t\sum_{j=2}^s E_{jj}.
\]

Its nonzero blocks are the invertible \(2\times2\) block \(\begin{psmallmatrix}a&1\\1&0\end{psmallmatrix}\) and scalar blocks \(t\) (take \(t\ne0\)); it therefore has a square root. Its last rows are exactly (I). The minor of \(C_0-N(t)\) in columns \(1,2,\ldots,s\) has leading coefficient \(((C_0)_{11}-a)(-1)^{s-1}\) at degree \(s-1\) in \(t\), so is nonzero for generic \(t\).

In form (II), take

\[
N(t)=t\sum_{j=1}^sE_{jj}+\lambda E_{s+1,s+1}.
\]

It is a diagonal square for any nonzero \(t\); its bottom rows are (II), and the same first-\(s\)-column determinant has leading term \((-t)^s\).

In form (III), choose \(a\in F\) with \(a\ne(C_0)_{1n}\), and set

\[
N(t)=aE_{1n}+E_{s+1,n}+t\sum_{j=2}^sE_{jj}.
\]

Its bottom rows are exactly (III). To prove it is a square, work on \(\langle e_1,e_{s+1},e_n\rangle\): define a linear map \(X\) by

\[
X(e_n)=e_1,\quad
X(e_1)=a e_1+e_{s+1},\quad
X(e_{s+1})=-a(ae_1+e_{s+1}),
\]

and on the remaining vectors set \(X(e_j)=\sqrt t\,e_j\) for \(2\le j\le s\). Then direct multiplication gives \(X^2=N(t)\): on the three-dimensional subspace the square sends \(e_n\) to \(ae_1+e_{s+1}\) and annihilates the other two vectors. For \(H=C_0-N(t)_{\mathrm{top}}\), the \(s\times s\) minor in columns \(n,2,3,\ldots,s\) has leading coefficient \(((C_0)_{1n}-a)(-1)^{s-1}\) at degree \(s-1\). Thus generic \(t\ne0\) makes \(H\) full row rank.

Every rank-one case therefore admits the square \(N\) required in Step 2. Together with Steps 3 and 4 this covers every possible rank of the bottom two rows, proving surjectivity. Undo the basis change and multiply by \(A_1\). \(\square\)

## Verification

The executable `check_square_coeff.py` constructs exact rational examples in all five strata (zero, rank-one top-supported, rank-one semisimple, rank-one nilpotent, and rank-two bottom rows) at matrix sizes \(7,8,9,12\). It tests six independently generated targets for each stratum and dimension, checks the bottom-row constraint and full residual row rank, and explicitly squares the three-coordinate nilpotent root in form (III). The expected successful output ends in `MATRIX_TWO_SQUARES_NULLITY_TWO_CERTIFICATES_OK`. The finite checks are corroborative, not an infinite proof. Steps 2–5 provide the all-parameter argument.

## Relationship to prior work

Saini [1, §6, Question 6.1] asks, for \(n\ge7\) and \(2\le k\le n-2\), exactly which nullity-two coefficients give surjective two-term power sums. Its Theorems 1.1–1.2 address large exponents and orders five and six. The present finding resolves the entire exponent-two slice for all \(n\ge7\), including every nullity-two Jordan type. Saini and Singh [2, Theorems 1.2–1.3] prove surjectivity in every dimension when the second coefficient has nullity at most one and classify dimensions three and four; these conclusions do not cover the claim's nullity-two, high-dimensional range. Panja–Saini–Singh [3] study order-two matrices. The proof's new organizing device is a square completion with a full-row-rank residual; the rank-one nilpotent bottom block is handled by an explicit square root containing a length-three Jordan chain.

## Limitations

This theorem treats only the square exponent and algebraically closed characteristic-zero fields. It does not determine whether the analogous statement holds for larger powers in Question 6.1, nor does it provide a count of decompositions or a uniform formula for arbitrary matrix roots. The exact-arithmetic checker is a finite consistency test. An exhaustive historical-priority determination and an independent specialist audit have not been performed.

## References

1. P. Saini, *Sum of Powers with Matrix Coefficients*, arXiv:2611.19228v1, publicly posted 2026-11-14, https://arxiv.org/html/2611.19228v1 .
2. P. Saini and A. Singh, *Polynomial Maps with Constants on Matrix Algebra*, arXiv:2604.27592v1, publicly posted 2026-04-30, https://arxiv.org/html/2604.27592v1 .
3. S. Panja, P. Saini, and A. Singh, *Images of polynomial maps with constants*, Mathematika 71 (2025), e70031, https://doi.org/10.1112/mtk.70031 .
