# Exact Euclidean Banach--Mazur distance of the Banaś--Frączek plane
## Finding
For every \(\lambda>1\), define the real Banaś--Frączek plane \(X_\lambda=(\mathbb R^2,N_\lambda)\) by
\[
N_\lambda(x_1,x_2)=\max\left\{\lambda|x_1|,\sqrt{x_1^2+x_2^2}\right\}.
\]
Then
\[
d_{\mathrm{BM}}(X_\lambda,\ell_2^2)^2=C_{\mathrm{NJ}}(X_\lambda)=2-\lambda^{-2}.
\]
One optimal Euclidean pullback norm is, up to multiplication by a positive scalar,
\[
|(x_1,x_2)|_*=\sqrt{x_1^2+\lambda^{-2}x_2^2}.
\]

## Assumptions and scope
The scalar field is real and \(\lambda>1\). The multiplicative Banach--Mazur distance is
\[
d_{\mathrm{BM}}(X,\ell_2^2)=\inf_T \|T\|\,\|T^{-1}\|,
\]
where the infimum runs over all invertible linear maps from \(X\) to the Euclidean plane. The von Neumann--Jordan constant is
\[
C_{\mathrm{NJ}}(X)=\sup_{x,y\neq(0,0)}
\frac{\|x+y\|^2+\|x-y\|^2}{2(\|x\|^2+\|y\|^2)}.
\]
No restriction to diagonal linear maps is assumed at the outset.

## Proof
Pulling the Euclidean norm back through an arbitrary invertible linear map gives a positive-definite quadratic form \(q\). For such a form set
\[
m(q)=\inf_{z\ne0}\frac{N_\lambda(z)^2}{q(z)},\qquad
M(q)=\sup_{z\ne0}\frac{N_\lambda(z)^2}{q(z)}.
\]
The squared distortion of this Euclidean pullback is \(M(q)/m(q)\).

The norm \(N_\lambda\) is invariant under both coordinate sign changes. If
\[
m(q)q(z)\le N_\lambda(z)^2\le M(q)q(z),
\]
then the same inequalities hold after either sign change. Averaging \(q\) over the four sign changes therefore preserves these two comparison constants and removes the cross term. Consequently some distortion-minimizing pullback may be taken diagonal. After positive rescaling write it as
\[
q_t(x_1,x_2)=x_1^2+t x_2^2,\qquad t>0.
\]

For \(x_1\ne0\), put \(u=x_2^2/x_1^2\). The ratio becomes
\[
R_t(u)=\frac{N_\lambda(x_1,x_2)^2}{q_t(x_1,x_2)}
=\frac{\max\{\lambda^2,1+u\}}{1+t u},\qquad u\ge0,
\]
with the direction \(x_1=0\) represented by \(u=\infty\). The two branches meet at \(u=\lambda^2-1\). Direct monotonicity on the two branches gives the exact distortion ratio
\[
D(t)=\frac{M(q_t)}{m(q_t)}=
\begin{cases}
\displaystyle \frac{1+t(\lambda^2-1)}{\lambda^2 t},&0<t\le\lambda^{-2},\\[6pt]
\displaystyle 1+t(\lambda^2-1),&\lambda^{-2}\le t\le1,\\[6pt]
\displaystyle \lambda^2 t,&t\ge1.
\end{cases}
\]
The first branch is strictly decreasing, while the second and third are increasing. Hence the global minimum occurs at \(t=\lambda^{-2}\), and
\[
\min_{t>0}D(t)=2-\lambda^{-2}.
\]
This proves
\[
d_{\mathrm{BM}}(X_\lambda,\ell_2^2)^2=2-\lambda^{-2}
\]
and gives the displayed optimal pullback norm.

For the von Neumann--Jordan constant, take
\[
x=\left(\lambda^{-1},\sqrt{1-\lambda^{-2}}\right),\qquad
y=\left(\lambda^{-1},-\sqrt{1-\lambda^{-2}}\right).
\]
Then \(N_\lambda(x)=N_\lambda(y)=1\), while
\[
N_\lambda(x+y)=2,\qquad
N_\lambda(x-y)=2\sqrt{1-\lambda^{-2}}.
\]
Thus \(C_{\mathrm{NJ}}(X_\lambda)\ge2-\lambda^{-2}\). Conversely, any Euclidean pullback with distortion squared \(D\) transfers the Euclidean parallelogram identity to give \(C_{\mathrm{NJ}}(X_\lambda)\le D\). Taking the optimal pullback just proved yields the reverse inequality, so equality follows.

## Verification
The proof is exact and covers every invertible linear map: sign-symmetry averaging is applied to an arbitrary positive-definite pullback before the one-variable optimization. At \(t=\lambda^{-2}\), the directional ratio has equal maxima \(\lambda^2\) at the coordinate-axis limits and minimum \(\lambda^2/(2-\lambda^{-2})\) at the branch-contact directions, giving squared distortion exactly \(2-\lambda^{-2}\). The explicit pair in the last paragraph independently attains the same von Neumann--Jordan ratio.

## Relationship to prior work
Banaś and Frączek introduced the named plane and its norm in Example 4.1 of *Deformation of Banach spaces*; the DML-CZ record classifies the paper under MSC 46B20 and records public availability on 2009-01-08. Their inspected example computes convexity and smoothness moduli, not the Euclidean Banach--Mazur distance.

Yang's 2014 paper reports the exact value \(C_{\mathrm{NJ}}(X_\lambda)=2-\lambda^{-2}\) for the same Banaś--Frączek space. That known constant is consistent with, but does not by itself state, the optimal Euclidean pullback or the exact Banach--Mazur distance. A later paper of Yang and Li studies generalized von Neumann--Jordan constants for the same family. Searches by the named space, the explicit norm, the candidate distance formula, the Euclidean target, and the ellipsoid formulation did not locate a prior exact-distance statement.

## Limitations
The result is restricted to this real two-dimensional Banaś--Frączek family. It gives one optimal Euclidean pullback but does not classify every optimal linear isomorphism. The 2014 same-object paper was available through abstract and bibliographic records rather than inspected full text, leaving a residual bibliographic risk that a passing remark there or in another unindexed specialist source records the same distance; no such statement was found in the searches performed.

## References
1. J. Banaś and K. Frączek, *Deformation of Banach spaces*, Comment. Math. Univ. Carol. 34 (1993), 47--53. Stable record: hdl:10338.dmlcz/118554.
2. C. Yang, *Jordan-Von Neumann constant for Banaś-Frączek space*, Banach J. Math. Anal. 8 (2014), 185--192. DOI: 10.15352/bjma/1396640062.
3. C. Yang and H. Li, *Generalized von Neumann--Jordan constant for the Banaś--Frączek space*, Colloq. Math. 154 (2018), 149--156. DOI: 10.4064/cm7422-1-2018.
