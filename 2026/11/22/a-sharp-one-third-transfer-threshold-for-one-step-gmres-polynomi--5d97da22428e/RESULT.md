# A sharp one-third transfer threshold for one-step GMRES polynomials on triangular paths

## Finding

Let \(n\ge2\) be an arbitrary integer, let \(S_n\) be the real lower shift with \((S_n)_{i+1,i}=1\), and put \(T_n(t)=I_n-tS_n\) for \(t\ge0\). Train one exact Euclidean GMRES step from zero on \(T_n(t)x=b\), using any \(b\ne0\), to obtain the degree-zero approximate-inverse polynomial
\[
q_b(z)=\alpha_t(b),\qquad
\alpha_t(b)=\frac{b^{\mathsf T}T_n(t)b}{\|T_n(t)b\|_2^2}.
\]
Freeze this polynomial and apply it to a possibly different right-hand side \(c\ne0\). Then **the following is an exact all-dimension, all-training, all-deployment equivalence**:
\[
\boxed{\ \forall n\ge2\ \forall b,c\ne0:\quad
\|(I_n-\alpha_t(b)T_n(t))c\|_2\le\|c\|_2
\quad\Longleftrightarrow\quad 0\le t\le\frac13.\ }
\]
The quantifier on \(n\) is essential: at each *fixed* dimension the threshold can be larger. In dimension two the precise safe interval is \(0\le t\le2/3\), while in dimension three it is
\[
\boxed{\ 0\le t\le \sqrt{3\sqrt2-4}=0.4925857155\ldots\ .\ }
\]
For any \(1/3<t<1\), a sufficiently long triangular path admits a training vector and a different deployment vector producing **strict residual amplification**, even though *every* one-step GMRES fit to its own training vector strictly reduces that training residual. Thus individually successful least-squares training does not, by itself, imply residual nonexpansion when the fitted polynomial is reused.

The two-site threshold has an entirely rational witness. At \(t=3/4\) take \(b=(1,7/4)^{\mathsf T}\), \(c=(1,-1/4)^{\mathsf T}\). Then \(\alpha_t(b)=11/8\) and
\[
\frac{\|(I-\alpha_t(b)T_2(t))c\|_2^2}{\|c\|_2^2}=\frac{45}{34}>1.
\]
These are exact-arithmetic, once-applied residual statements, not claims of divergence of a repeatedly applied stationary iteration.

## Assumptions and scope

The matrix is real and strictly unit lower bidiagonal with *constant* nonnegative subdiagonal magnitude \(t\), and Euclidean norms and dot products are used. We always start the training solve from zero and perform *exactly one* unconstrained minimization in \(\operatorname{span}\{b\}\). The trained scalar polynomial is held fixed for one subsequent approximate triangular solve, again from zero. The training and subsequent right-hand sides are arbitrary nonzero real vectors, independently chosen; no distributional assumption is made. Matrix order \(n\) is finite but is not bounded in the universal claim. Neither the fitted polynomial nor its residual is optimized on the deployment right-hand side.

The one-step fit is uniquely defined for every \(b\ne0\), since \(T_n(t)\) is invertible. For \(t=0\), \(T_n=I_n\), the fitted polynomial is the exact inverse, and the residual vanishes. All mathematical statements are in exact arithmetic.

## Proof

**1. Exact transfer reduction.** Write \(T=T_n(t)\), and set
\[
H=\tfrac12(T^{-1}+T^{-\mathsf T}),\quad
m=\lambda_{\min}(H),\quad M=\lambda_{\max}(H).
\]
For a nonzero vector \(b\), set \(y=Tb\). Direct substitution gives
\[
\alpha_t(b)=\frac{y^{\mathsf T}Hy}{\|y\|_2^2}.
\]
As \(T\) is invertible and \(b\) is unrestricted, the attainable fit coefficients range over the entire closed interval \([m,M]\), including both ends. Define likewise \(\beta(c)=c^{\mathsf T}Tc/\|Tc\|_2^2\); its attainable values are also \([m,M]\), independently of the training coefficient. Elementary expansion yields the **exact cross-residual identity**
\[
\|(I-\alpha T)c\|_2^2-\|c\|_2^2
=\alpha(\alpha-2\beta(c))\|Tc\|_2^2.
\tag{1}
\]
Because \(\operatorname{tr}H=n\), \(M\ge1>0\). Choosing training \(b=T^{-1}y_{\max}\) and deployment \(c=T^{-1}y_{\min}\), where the \(y\)'s are unit extremal eigenvectors of \(H\), makes the right side of (1) equal to \(M(M-2m)\|Tc\|_2^2\). Thus universal nonexpansion for all \(b,c\) **requires** \(M\le2m\). Conversely \(M\le2m\) forces \(m\ge M/2>0\), and every \(\alpha,\beta(c)\in[m,M]\) satisfies \(0<\alpha\le M\le2m\le2\beta(c)\); (1) is nonpositive. We have established the exact finite-dimensional criterion
\[
\boxed{\ \forall b,c\ne0:\ \|(I-\alpha_t(b)T)c\|_2\le\|c\|_2
\quad\Longleftrightarrow\quad M\le2m.\ }
\tag{2}
\]
This reasoning includes the equality boundary and shows how to construct the violating vectors when the inequality fails.

**2. Toeplitz structure and dimension-uniform safety.** Since \(S_n^n=0\),
\[
T^{-1}=I+tS_n+\cdots+t^{n-1}S_n^{n-1}.
\]
It follows entry-by-entry that
\[
H=\tfrac12(I_n+C_n(t)),\qquad (C_n(t))_{ij}=t^{|i-j|}.
\tag{3}
\]
Here \(C_n(t)\) is the classical Kac–Murdock–Szegő Toeplitz correlation matrix; its established structure is background, not claimed as new. For \(0<t<1\) its symbol is the Poisson kernel
\[
f_t(\theta)=\frac{1-t^2}{1-2t\cos\theta+t^2},\quad
\min_\theta f_t(\theta)=\frac{1-t}{1+t},\quad
\max_\theta f_t(\theta)=\frac{1+t}{1-t}.
\]
For each nonzero real \(y\), the quotient \(y^{\mathsf T}C_n(t)y/\|y\|_2^2\) is the weighted average of this symbol against \(|\sum_{j=1}^ny_je^{ij\theta}|^2\), normalized by Parseval. A nonzero trigonometric polynomial cannot be supported only on the two isolated extremal frequencies, so both Toeplitz spectral inequalities are strict at every finite dimension. Combining with (3) gives
\[
\frac1{1+t}<m\le M<\frac1{1-t}.
\tag{4}
\]
For \(0<t\le1/3\), \(1/(1-t)\le2/(1+t)\). Hence (4) implies \(M<2m\) for every finite \(n\), proving safety (in fact strict reduction for nonzero \(c\)) at and below the proposed universal threshold. The case \(t=0\) is immediate.

**3. Sharpness above one third.** For \(0<t<1\), normalized all-ones vectors and normalized alternating-sign vectors provide Rayleigh quotients of \(C_n(t)\) given respectively by
\[
r_n^{\pm}(t)=1+2\sum_{k=1}^{n-1}\left(1-\frac{k}{n}\right)(\pm t)^k.
\]
As \(n\to\infty\), the limits are \((1+t)/(1-t)\) and \((1-t)/(1+t)\). Thus (3) and extremal Rayleigh bounds imply
\[
\lim_{n\to\infty}M_n(t)=\frac1{1-t},\qquad
\lim_{n\to\infty}m_n(t)=\frac1{1+t}.
\tag{5}
\]
For any \(1/3<t<1\), the first limit exceeds twice the second, so a **finite** dimension eventually satisfies \(M_n>2m_n\). The eigenvector construction from Step 1 then gives a strictly amplifying pair. For \(t\ge1\), dimension two already fails by Step 4 below. These exhaust the complement of \([0,1/3]\) and prove the sharp all-dimension statement.

For comparison with the training residual, when \(0<t<1\) the symmetric part of \(T\) has smallest eigenvalue \(1-t\cos(\pi/(n+1))>0\). Thus \(b^{\mathsf T}Tb>0\) for all \(b\ne0\); minimizing the strictly convex quadratic \(\|b-\alpha Tb\|_2^2\) gives a strictly positive reduction from its zero-coefficient value. Hence the cross-RHS failure in \(1/3<t<1\) is not a failed training solve.

**4. Exact small-dimensional boundaries.** For \(n=2\), the two eigenvalues of (3) are \(1\pm t/2\); (2) becomes \(1+t/2\le2(1-t/2)\), exactly \(t\le2/3\). The rational witness in the finding follows by direct multiplication.

For \(n=3\), (3) becomes
\[
H_3=\begin{pmatrix}1&t/2&t^2/2\\t/2&1&t/2\\t^2/2&t/2&1\end{pmatrix}
\]
with eigenvalues
\[
1-\frac{t^2}{2},\qquad
1+\frac{t^2}{4}\pm\frac{t\sqrt{t^2+8}}4.
\]
When \(0\le t\le1\), the minus-sign root is the least and the plus-sign root is the greatest. Criterion (2) is therefore equivalent to
\[
3t\sqrt{t^2+8}\le4+t^2
\quad\Longleftrightarrow\quad
t^4+8t^2-2\le0,
\]
whose nonnegative solution is \(t\le\sqrt{3\sqrt2-4}\). For \(t>1\), the leading \(2\times2\) principal submatrix already has largest eigenvalue greater than twice its least eigenvalue (by the dimension-two formula), so eigenvalue interlacing forces \(M_3>2m_3\). This also proves sharpness beyond the displayed three-site boundary. No finite computation is used as an infinite-dimensional proof.

## Verification

Run `python verify_transfer.py` from the extracted package with Python 3.10+, NumPy and SymPy. The script independently constructs the exact symmetrized inverse for dimensions two through eight, verifies the dimension-three symbolic eigenvalues and threshold polynomial, and checks the rational two-site amplification \(45/34\). It additionally tests random transfer identities, extreme-eigendirection witnesses and a subunit-coupling finite-dimensional failure at \(n=25\), \(t=2/5\). These finite tests are supporting consistency checks; the universal quantifiers follow exclusively from the analytic argument above.

## Relationship to prior work

Dargaville and Pain (2026) compare approximate ILU triangular solves and explicitly construct a fixed GMRES polynomial from a single random right-hand side for reuse during subsequent solves (their Sections 4–5). Their experiments and descriptions motivate the transfer question, but do not supply the sharp all-dimension, all-training, all-deployment residual criterion for the one-step polynomial. Embree, Henningsen, Jackson and Morgan (2025) develop GMRES-derived approximate inverses for multiple right-hand sides; their Theorems 2.3 and 4.1 provide bounds based on eigenvector decompositions of **diagonalizable** matrices, whereas \(T_n(t)\) is defective whenever \(n\ge2\), \(t>0\). Their empirical transfer-instability examples do not supply the thresholds above. The Kac–Murdock–Szegő spectral structure and Toeplitz-symbol bounds are classical and are explicitly used as known ingredients; the new question is how its **extreme spectral quotient** governs reuse of a fitted scalar GMRES polynomial.

Prior work on weighted three-site Jordan GMRES stagnation concerns **two simultaneous residual-minimizing iterations on the same right-hand side**, not a frozen one-step scalar polynomial trained and then applied to another right-hand side. General polynomial-preconditioning convergence results, including Joubert's adaptive polynomial method, concern different algorithms or iteration-level convergence and do not by themselves establish (2) or its Toeplitz transfer threshold. Exact priority against unpublished or unindexed equivalent transfer analyses cannot be proved by literature search.

## Limitations

This theorem is for an ideal one-step, **degree-zero** approximate inverse trained by exact Euclidean GMRES. It is not a theorem for longer GMRES training, arbitrary ILU factors or unequal subdiagonal weights, distributions of random training vectors, roundoff, inverse-error norms, or repeated stationary convergence. The one-third threshold is uniform in dimension; it does not assert a dimension-independent contraction factor at equality, and the three-site and two-site bounds show why small computational tests can misidentify the uniform boundary. Strict own-right-hand-side improvement is claimed for \(0<t<1\), not all \(t\ge1\). The historical literature may contain uncatalogued equivalent observations; independent mathematical validation has not been performed.

## References

1. S. Dargaville and C. C. Pain, *A comparison of parallel iterative methods for ILU triangular solves*, arXiv:2611.00552v1, first posted 31 October 2026, especially Sections 4–5. https://arxiv.org/html/2611.00552v1
2. M. Embree, J. A. Henningsen, J. Jackson and R. B. Morgan, *Polynomial Approximation to the Inverse of a Large Matrix*, arXiv:2502.18317, first posted 25 February 2025; see especially Sections 2, 4 and Theorem 4.1. https://arxiv.org/abs/2502.18317
3. N. J. Higham, *What Is the Kac–Murdock–Szegö Matrix?*, 6 July 2021. https://nhigham.com/2021/07/06/what-is-the-kac-murdock-szego-matrix/
4. M. Kac, W. L. Murdock and G. Szegö, *On the Eigen-values of Certain Hermitian Forms*, Journal of Rational Mechanics and Analysis 2 (1953), 767–800 (classical Toeplitz background).
5. W. Joubert, *A Robust GMRES-Based Adaptive Polynomial Preconditioning Algorithm for Nonsymmetric Linear Systems*, SIAM Journal on Scientific Computing 15 (1994), 427–439, doi:10.1137/0915029 (algorithmic background; abstract consulted). https://epubs.siam.org/doi/abs/10.1137/0915029
