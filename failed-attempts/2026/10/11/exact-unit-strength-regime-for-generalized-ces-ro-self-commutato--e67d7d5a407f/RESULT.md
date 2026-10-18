# Exact unit-strength regime for generalized Cesàro self-commutator bounds

## Finding
For a positive integer \(m\) and \(\alpha\ge 0\), let \(M_{\alpha,m}\) be the generalized Cesàro operator on \(\ell^2(\mathbb N_0)\) with entries
\[
(M_{\alpha,m})_{nj}=\frac{m(n-j+1)_{m-1}}{(n+\alpha+1)_m}\qquad(0\le j\le n),
\]
and let
\[
R_{\alpha,m}=\operatorname{diag}(r_n(\alpha)),\qquad
r_n(\alpha)=1-\frac{(n+\alpha+1)_m}{(n+\alpha+m+1)_m}.
\]
Define the optimal weighted self-commutator coefficient
\[
c_m(\alpha)=\sup\Bigl\{c\in\mathbb R:\ M_{\alpha,m}^*M_{\alpha,m}-M_{\alpha,m}M_{\alpha,m}^*\ge c\,M_{\alpha,m}^*R_{\alpha,m}M_{\alpha,m}\Bigr\}.
\]
Then
\[
c_m(\alpha)\le 1
\]
for every \(\alpha\ge0\), and
\[
c_m(\alpha)=1
\quad\Longleftrightarrow\quad
\alpha\in\{0,1,\ldots,m-2\}\cup[m-1,\infty).
\]
For \(m=1\), the finite set is empty, so equality holds for every \(\alpha\ge0\). Consequently every noninteger \(\alpha\) with \(0<\alpha<m-1\) satisfies \(c_m(\alpha)<1\).

The focal source proves the uniform estimate \(c_m(\alpha)\ge1/36\) for all \(\alpha\ge0\) but explicitly does not claim its constant is optimal. The statement above identifies exactly where the strongest possible coefficient \(1\) is attained.

## Assumptions and scope
The argument uses the boundedness, finite-support right inverse, and exact defect decomposition proved in arXiv:2610.00193v1. In particular, the source gives \(M_{\alpha,m}L_{\alpha,m}x=x\) for every \(x\in c_{00}\), hence \(M_{\alpha,m}\) has dense range. It also gives a bounded operator \(B_{\alpha,m}\) such that
\[
M_{\alpha,m}^*M_{\alpha,m}-M_{\alpha,m}M_{\alpha,m}^*
=M_{\alpha,m}^*(I-B_{\alpha,m}^*B_{\alpha,m})M_{\alpha,m},
\]
with
\[
I-B_{\alpha,m}^*B_{\alpha,m}
=R_{\alpha,m}+F_{\alpha,m},
\qquad
F_{\alpha,m}=\sum_{r=0}^{m-1}\lambda_{m,r}(\alpha)v_{m,r}v_{m,r}^*,
\]
and
\[
\lambda_{m,r}(\alpha)
=(2r+1)\binom{m+r}{2r+1}^2\alpha
\prod_{j=1}^r(\alpha^2-j^2).
\]
Each \(v_{m,r}\) has coordinates \(p_{m,r}(n;\alpha)/D_m(n+\alpha)\), where the numerator is monic of degree \(m-r-1\). The diagonal entries of \(R_{\alpha,m}\) are strictly positive.

The finding classifies only the parameters at which the optimal coefficient equals \(1\). It does not compute the exact value of \(c_m(\alpha)\) inside the noninteger bands \(0<\alpha<m-1\).

## Proof
Write \(M=M_{\alpha,m}\), \(R=R_{\alpha,m}\), and \(F=F_{\alpha,m}\). The source identity gives
\[
M^*M-MM^*=M^*(R+F)M.
\]
Because \(MLx=x\) on \(c_{00}\), the range of \(M\) contains \(c_{00}\) and is therefore dense. Hence, for any bounded self-adjoint operator \(X\),
\[
M^*XM\ge0\quad\Longleftrightarrow\quad X\ge0.
\]
Indeed, the forward implication gives nonnegativity of the quadratic form of \(X\) on the dense range of \(M\), and continuity extends it to all of \(\ell^2\).

Therefore
\[
M^*M-MM^*\ge cM^*RM
\quad\Longleftrightarrow\quad
F+(1-c)R\ge0.
\]
The range of \(F\) lies in the finite-dimensional span of \(v_{m,0},\ldots,v_{m,m-1}\). Choose a nonzero vector \(x\) orthogonal to this span. Then \(Fx=0\), while \(\langle Rx,x\rangle>0\) because every diagonal entry of \(R\) is positive. If \(c>1\), the preceding operator inequality would give
\[
0\le\langle(F-(c-1)R)x,x\rangle=-(c-1)\langle Rx,x\rangle<0,
\]
a contradiction. Thus \(c_m(\alpha)\le1\).

It remains to decide when \(c=1\) is valid. This is equivalent to \(F\ge0\). Let \(V:\mathbb C^m\to\ell^2(\mathbb N_0)\) have columns \(v_{m,r}\). The vectors are linearly independent: after multiplication by the common nonzero denominator \(D_m(n+\alpha)\), a linear relation becomes a polynomial identity among monic polynomials of the distinct degrees \(m-1,m-2,\ldots,0\). Hence \(V\) is injective and \(V^*\) is surjective. With
\[
\Lambda=\operatorname{diag}(\lambda_{m,0}(\alpha),\ldots,\lambda_{m,m-1}(\alpha)),
\]
one has \(F=V\Lambda V^*\). Surjectivity of \(V^*\) therefore yields
\[
F\ge0\quad\Longleftrightarrow\quad
\lambda_{m,r}(\alpha)\ge0\text{ for every }0\le r<m.
\]

The signs are now exact. If \(\alpha=0\), every coefficient vanishes. If \(\alpha=k\) is a positive integer, then for \(r<k\) every factor \(k^2-j^2\) is positive, while for \(r\ge k\) the factor with \(j=k\) vanishes. Thus all coefficients are nonnegative at every nonnegative integer parameter.

Now suppose \(\alpha\in(k,k+1)\) is noninteger. For \(r\le k\), all factors \(\alpha^2-j^2\) are positive. If \(\alpha<m-1\), then \(k+1\le m-1\), and the coefficient with \(r=k+1\) contains one negative factor \(\alpha^2-(k+1)^2\) and only positive earlier factors, so
\[
\lambda_{m,k+1}(\alpha)<0.
\]
Thus \(F\not\ge0\) and \(c_m(\alpha)<1\). Conversely, if \(\alpha>m-1\), then \(j<\alpha\) for every \(1\le j\le r\le m-1\), so every coefficient is positive. The endpoint \(\alpha=m-1\) is already covered by the integer case. This proves the stated classification.

## Verification
The critical source identities were checked in the full text of arXiv:2610.00193v1: the finite-support right inverse is equation (2.2), the defect factorization and rank-one coefficients are Theorem 2.3, and positivity of every diagonal entry of \(R_{\alpha,m}\) is stated immediately after its definition. The source also states the uniform \(1/36\) bound and explicitly notes that this constant is not asserted optimal.

The new argument itself is symbolic. The only structural steps beyond the source are dense-range transfer of a quadratic-form inequality, finite-rank orthogonal-complement obstruction to any coefficient above \(1\), linear independence of the rank-one vectors from distinct polynomial degrees, and the sign pattern of the explicit coefficients. No finite sampling, asymptotic extrapolation, or numerical experiment is used.

## Relationship to prior work
Ma's 2026 theorem proves that \(M_{\alpha,m}\) is hyponormal exactly for \(\alpha\ge0\) and obtains the uniform weighted lower bound with coefficient \(1/36\). The paper states that the constant is not claimed optimal. Its defect decomposition contains the coefficient formula used here, but it does not state the optimal-coefficient ceiling or the exact unit-strength parameter classification.

For order \(m=2\), Rhaly's 2018 theorem proved hyponormality on \(\{0\}\cup[1,\infty)\), leaving \(0<\alpha<1\) open at that time. The present unit-strength classification recovers exactly that old parameter set as the region where \(c_2(\alpha)=1\), while Ma's later theorem fills the omitted interval with hyponormal operators having \(c_2(\alpha)<1\). Ma's introduction records the analogous earlier order-three region \(\{0,1\}\cup[2,\infty)\); the same phenomenon holds for every positive integer order.

## Limitations
The theorem does not determine \(c_m(\alpha)\) exactly when \(\alpha\) is noninteger and \(0<\alpha<m-1\); it only proves the strict upper bound \(c_m(\alpha)<1\), together with the focal source's universal lower bound \(c_m(\alpha)\ge1/36\). The proof depends on the specific finite-rank defect decomposition for generalized Cesàro matrices and does not extend automatically to arbitrary hyponormal weighted mean matrices.

A residual originality risk is that the same optimal-coefficient criterion could have appeared under older interrupter or supraposinormal terminology without using the present notation. The inspected order-two paper and targeted semantic searches did not reveal such a statement.

## References
1. Yicen Ma, *Hyponormality of Generalized Cesàro Matrices of Every Positive Integer Order*, arXiv:2610.00193v1, 18 September 2026.
2. H. C. Rhaly Jr., *Supraposinormality and hyponormality for the generalized Cesàro matrices of order two*, Operators and Matrices 12 (2018), DOI:10.7153/oam-2018-12-08.
