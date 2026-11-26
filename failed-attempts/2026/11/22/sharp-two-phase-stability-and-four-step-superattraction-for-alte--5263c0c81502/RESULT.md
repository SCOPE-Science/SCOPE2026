# Sharp two-phase stability and four-step superattraction for alternating rank-one gradients

## Finding
Fix two distinct, nonparallel unit directions \(u,v\in\mathbb R^2\), and write \(s=1-(u^\top v)^2\in(0,1]\). A modified-gradient map that alternately acts only along these directions has a sharp two-phase Schur stability region. If the second gain is one, there is a unique first gain at which the two-update Jacobian is nonzero nilpotent, and hence the four-update nonlinear return has zero derivative. At sufficiently small angular separation, this superattracting gain exceeds the standard per-update gradient stability ceiling by an arbitrarily large factor.

**Theorem.** Let \(f\) be \(C^3\) on a neighborhood of \(0\in\mathbb R^2\), with \(\nabla f(0)=0\) and \(D^2f(0)=-I_2\). For \(a,b>0\), set
\[
 F_u(x)=x+a uu^\top\nabla f(x),\qquad
 F_v(x)=x+b vv^\top\nabla f(x),\qquad G=F_v\circ F_u.
\]
The fixed point \(0\) has a strictly Schur-stable return derivative \(DG(0)\) if and only if
\[
 a+b-ab>0,\qquad 4-2(a+b)+ab(2-s)>0. \tag{1}
\]
Consequently, (1) guarantees local asymptotic stability for every such \(f\). If either expression in (1) is strictly negative, \(DG(0)\) has an eigenvalue outside the closed unit disk and \(0\) is unstable. For the quadratic \(f(x)=-\|x\|^2/2\), (1) is precisely the necessary and sufficient condition for convergence of every initial state under the alternating updates (in every even/odd subsequence); no assertion is made at equality for general nonlinear objectives.

In the slice \(b=1\), the quadratic is globally attracting precisely for \(0<a<2/s\). At \(a=1/s\), if \(0<s<1\), the matrix \(DG(0)\) is **nonzero** and \(DG(0)^2=0\). For the quadratic, the four-update composition \(G^2\) sends all of \(\mathbb R^2\) exactly to zero, whereas the composition of three individual updates is not identically zero. For every nonlinear \(f\) as above, the same parameter choice makes \(0\) a locally quadratically attracting fixed point of \(G^2\): there are \(r,C>0\) with
\[
 \|G^2(x)\|\le C\|x\|^2\quad(\|x\|\le r).
\]
For \(s<1/2\), \(a=1/s>2\), and \(a\to\infty\) as \(s\downarrow0\), even though every preconditioning matrix has rank one.

## Assumptions and scope
The rank-one matrices are \(uu^\top\) and \(vv^\top\), with Euclidean unit vectors and constant positive scalar gains. The ordering is first \(F_u\), then \(F_v\), repeated. All claims about global convergence or exact finite annihilation concern the negative quadratic only. The nonlinear result is local, requiring \(C^3\) regularity and the stated stationary-point Hessian. A repeated or antiparallel pair has \(s=0\) and is excluded; the orthogonal case \(s=1\) is included in the Schur law, but its two-step map is already zero at \(a=b=1\). These maps are discrete-time updates, not continuous flows.

## Proof
Write \(P=uu^\top\), \(Q=vv^\top\) and \(c=u^\top v\), so \(c^2=1-s\). The chain rule gives
\[
 T=DG(0)=(I_2-bQ)(I_2-aP).
\]
Since \(\mathrm{tr}(P)=\mathrm{tr}(Q)=1\) and \(\mathrm{tr}(QP)=c^2\), and since each rank-one update has eigenvalues \(1\) and \(1-a\) (respectively \(1-b\)),
\[
 t=\mathrm{tr}(T)=2-a-b+ab(1-s),\qquad d=\det T=(1-a)(1-b).
\]
The characteristic polynomial is \(z^2-tz+d\). The real quadratic Schur (Jury) criterion is \(1-d>0\), \(1+t+d>0\), and \(1-t+d>0\). In the present setting these reduce respectively to
\[
 a+b-ab>0,\qquad 4-2(a+b)+ab(2-s)>0,\qquad abs>0.
\]
The last is automatic. This proves the exact strict Schur region. Standard local linearization proves asymptotic stability inside it and instability whenever an eigenvalue has modulus greater than one. For the quadratic, \(G(x)=Tx\) globally, so the same strict Schur region is necessary and sufficient for convergence of every state: \(T^k\to0\) exactly when its spectral radius is below one. Outside the strict region, a boundary matrix can have an eigenvalue on the unit circle, so global convergence fails as well. Each odd iterate is obtained by the bounded linear operator \(I-aP\) acting on the preceding even iterate.

Now set \(b=1\). Since \(d=0\), the two eigenvalues of \(T\) are \(0\) and \(t=1-as\). Hence strict Schur stability is exactly \(0<a<2/s\). The unique zero-trace gain is \(a=1/s\). By the Cayley–Hamilton equation \(T^2-tT+dI_2=0\), at this gain \(T^2=0\). If \(0<s<1\), then \(c\ne0\) and \(a>1\). In an orthonormal basis with \(u=e_1\) and \(v=(c,\sqrt{s})\), the second column of \(T\) is \((-c\sqrt{s},c^2)^\top\), which is nonzero. Thus \(T\ne0\), so \(G\ne0\) on the quadratic but \(G^2=0\). Moreover \(F_u\) is invertible for \(a=1/s\ne1\); hence a three-update product \((I-aP)T\) is nonzero. (Starting the alternating schedule with \(u\), the first three steps are \(F_u,F_v,F_u\).) The first uniform annihilation occurs after the fourth update.

For a general \(C^3\) function, \(F_u,F_v,G\) are \(C^2\), so \(H=G^2\) is \(C^2\), \(H(0)=0\), and \(DH(0)=T^2=0\). Taylor's theorem with a local second-derivative bound gives \(\|H(x)\|\le C\|x\|^2\). Choosing \(r\) such that \(Cr<1\) ensures iterates of \(H\) remain inside the ball and converge quadratically; the intermediate three updates converge as well by continuity. Finally \(a=1/s>2\) precisely for \(s<1/2\), and the gain diverges as \(s\downarrow0\).

## Verification
A standalone standard-library Python program `check.py` reproduces all trace/determinant identities in exact rational arithmetic, the Schur identities for multiple parameter choices, and the exact nilpotence example
\[
 u=(1,0),\quad v=(4/5,3/5),\quad s=9/25,\quad a=25/9,\quad b=1,
\]
\[
 T=\begin{pmatrix}-16/25&-12/25\\64/75&16/25\end{pmatrix},\qquad T^2=0\ne T.
\]
It also evaluates a smooth quartic perturbation at decreasing radii to check the predicted higher-order cancellation. Run `python3 check.py` from the extracted package. The finite tests corroborate but do not replace the all-parameter argument above.

## Relationship to prior work
Ridenhour (arXiv:2611.14756v1, November 10, 2026) proves general convergence for discrete modified-gradient systems using individual positive-semidefinite preconditioners, and explicitly discusses how anisotropic stability bounds can be conservative and require analysis of matrix products. Here the exact product criterion is solved for two alternating rank-one phases, with a nilpotent four-step nonlinear phenomenon even when one phase's gain exceeds the single-step ceiling. This does **not** make all gains beyond two safe or challenge the source's sufficient bound.

Classical Kaczmarz and relaxed alternating-projection analyses study related products of rank-one updates; accelerated/distributed and oblique Kaczmarz variants also have strong convergence properties. The specific distinction here is the joint sharp two-parameter **Schur region for this model** together with the unique gain producing a nonzero nilpotent return and an induced higher-order local attractor for every \(C^3\) nonlinear objective with the given Hessian. No claim of a new general matrix-product theorem or of an exhaustive historical priority search is made.

## Limitations
The clean result relies on a two-dimensional isotropic negative Hessian, two fixed unit directions, and a period-two update schedule. At the Schur boundary nonlinear stability can depend on higher derivatives. The nonlinear attraction is local rather than global; the finite-time four-step cancellation occurs only for the quadratic. The study does not give robustness bounds under miscalibrated gains or arbitrary time-varying directions. Closely related Kaczmarz literature may contain alternative formulations; the priority comparison is limited to accessible literature and indexed records.

## References
1. B. J. Ridenhour, *Stability of equilibria in discrete-time modified-gradient systems and the multivariate breeder’s equation*, arXiv:2611.14756v1 (posted 2026-11-10), https://arxiv.org/html/2611.14756v1 .
2. J. Borgard et al., *Accelerating the Distributed Kaczmarz Algorithm by Strong Over-relaxation*, arXiv:2006.01739, https://arxiv.org/pdf/2006.01739 .
3. A. Cegielski and A. Suchocka, *Relaxed Alternating Projection Methods*, SIAM Journal on Optimization, https://doi.org/10.1137/070698750 .
4. *Kaczmarz method with oblique projection*, Results in Applied Mathematics (2022), https://doi.org/10.1016/j.rinam.2022.100342 .
