# Exact cubic-jet risk and finite-radius optimum for orthogonal finite differences

## Finding

Consider the centered, symmetric, random-orthogonal-direction estimator of a gradient using \(2k\) black-box evaluations. The first nonlinear odd term in a Taylor expansion is cubic. For this term, the estimator has an exact rotationally invariant risk identity, a complete zero-variance classification, and a sharp criterion under which a **strictly positive** perturbation radius has smaller mean-squared gradient error than the zero-radius limit, despite noiseless function evaluations.

Here is the precise theorem. For all integers \(d\ge 2\) and \(1\le k\le d\), all real \(h>0\), every \(b\in\mathbb R^d\), every real symmetric third-order tensor \(T=(T_{ijk})\), and any differentiable even function \(q:\mathbb R^d\to\mathbb R\) for which all evaluations below exist, set

\[
f(x)=f(0)+b\cdot x+\frac16\sum_{i,j,l=1}^{d}T_{ijl}x_ix_jx_l+q(x)-q(0).
\]

Let \(u_1,\ldots,u_k\) be the first \(k\) columns of a Haar-uniform orthogonal matrix in dimension \(d\). Define

\[
G_{k,h}=\frac{d}{k}\sum_{a=1}^k u_a\frac{f(hu_a)-f(-hu_a)}{2h}.
\]

The true gradient at the origin is \(\nabla f(0)=b\). Define the cubic trace vector and harmonic trace-free tensor by

\[
t_i=\sum_j T_{ijj},\quad
H_{ijl}=T_{ijl}-\frac{t_i\delta_{jl}+t_j\delta_{il}+t_l\delta_{ij}}{d+2},
\qquad \sum_jH_{ijj}=0.
\]

With Euclidean vector norms and the componentwise tensor Frobenius norm, **the following hold exactly, without an asymptotic limit**:

\[
\mathbb E G_{k,h}=w_h:=b+\frac{h^2}{2(d+2)}t,
\]

\[
\boxed{\mathbb E\|G_{k,h}-\mathbb E G_{k,h}\|^2
=\frac{d-k}{k}\|w_h\|^2
+\frac{d h^4}{6k(d+2)(d+4)}\|H\|_F^2,}
\]

\[
\boxed{\mathcal R(h):=\mathbb E\|G_{k,h}-b\|^2
=\frac{d-k}{k}\|b\|^2
+\frac{(d-k)h^2}{k(d+2)}b\cdot t
+\frac{d h^4}{4k(d+2)^2}
\left(\|t\|^2+\frac{2(d+2)}{3(d+4)}\|H\|_F^2\right).}
\]

If \(T\ne0\), set

\[
W=\|t\|^2+\frac{2(d+2)}{3(d+4)}\|H\|_F^2>0.
\]

For \(k<d\), **a strictly positive radius improves the zero-radius risk if and only if \(b\cdot t<0\)**. In that case the unique risk-minimizing radius obeys

\[
\boxed{h_*^2=-\frac{2(d-k)(d+2)(b\cdot t)}{dW}>0,\qquad
\mathcal R(0^+)-\mathcal R(h_*)
=\frac{(d-k)^2(b\cdot t)^2}{kdW}>0.}
\]

Otherwise the zero-radius limit minimizes risk over \(h\ge0\) (with equality at every radius only when \(T=0\)); if \(k=d\) no positive-radius improvement is possible. For \(k=d\), the random estimator has zero variance for every \(h>0\) exactly when \(H=0\), equivalently when the cubic is of the form \((v\cdot x)\|x\|^2\) for some vector \(v\). When \(k<d\), its variance at a specified radius vanishes exactly when \(H=0\) and \(w_h=0\).

A strongly convex witness makes the finite-radius effect non-artificial. Fix \(\|v\|=1\), \(k<d\), \(\lambda>0\), and \(a>9/(4\lambda)\). The globally strongly convex polynomial

\[
f(x)=-v\cdot x+(v\cdot x)\|x\|^2+\frac a2\|x\|^2+\lambda\|x\|^4
\]

has \(\nabla f(0)=-v\) and exact error law

\[
\mathcal R(h)=\frac{d-k}{k}(1-h^2)^2+h^4.
\]

Its uniquely optimal radius is \(h_*^2=(d-k)/d\), with risk \((d-k)/d\), compared with the zero-radius risk \((d-k)/k\): the improvement factor is exactly \(d/k\). For instance, \(d=3,k=1\) gives an optimum \(h_*^2=2/3\) and risk \(2/3\) instead of \(2\).

## Assumptions and scope

The frame has Haar-uniform orthonormal columns, not \(k\) independent uniform sphere directions. Evaluations are noiseless and use one symmetric pair \(\pm hu_a\) per direction; the estimator is scaled by \(d/k\), not \(1/k\). The even contribution \(q\) cancels exactly in every central difference; differentiability and evenness ensure its gradient at the origin vanishes. There is no assumption of convexity in the general identity. The strongly convex witness is an additional specialization. The identities concern one gradient estimate at the origin, not an optimization trajectory.

## Proof

**Odd central difference and harmonic decomposition.** Since the even part cancels, for every unit vector \(u\),

\[
\frac{f(hu)-f(-hu)}{2h}
=b\cdot u+\frac{h^2}{6}T[u,u,u]
=w_h\cdot u+\frac{h^2}{6}H[u,u,u].
\]

The last identity follows by inserting the displayed tensor decomposition and using \(\|u\|=1\). Direct contraction gives \(\sum_j H_{ijj}=0\); the decomposition is orthogonal because \(\langle H,t\otimes I+\text{permutations}\rangle=3\sum_i t_i\sum_jH_{ijj}=0\). Also \(\|T\|_F^2=\|H\|_F^2+3\|t\|^2/(d+2)\).

**Exact spherical moments.** If \(U\) is uniform on the sphere in dimension \(d\), its second, fourth, and sixth coordinate moments are the sums over pairings of indices divided respectively by \(d\), \(d(d+2)\), and \(d(d+2)(d+4)\). The trace-free condition therefore gives

\[
\mathbb E[U H[U,U,U]]=0,\qquad
\mathbb E[(w_h\cdot U)H[U,U,U]]=0,
\]

\[
\mathbb E[(H[U,U,U])^2]
=\frac{6\|H\|_F^2}{d(d+2)(d+4)}.
\]

In the last equality precisely the six pairings joining every index of one tensor to an index of the other survive; the nine other pairings contain an internal trace and vanish. Also \(\mathbb E(UU^{\mathsf T})=I/d\).

**Orthonormality eliminates all pair cross terms.** Write \(\psi_h(u)=w_h\cdot u+(h^2/6)H[u,u,u]\). Pointwise, orthogonality gives

\[
\left\|\sum_{a=1}^ku_a\psi_h(u_a)\right\|^2
=\sum_{a=1}^k\psi_h(u_a)^2.
\]

Each column has the uniform spherical marginal, even though different columns are dependent. Consequently

\[
\mathbb E\|G_{k,h}\|^2
=\frac{d^2}{k}\mathbb E[\psi_h(U)^2]
=\frac dk\|w_h\|^2+
\frac{d h^4}{6k(d+2)(d+4)}\|H\|_F^2,
\]

and \(\mathbb E G_{k,h}=w_h\). Subtracting the squared mean proves the variance formula. Adding the squared bias \(\|w_h-b\|^2\) and expanding yields the risk formula.

**Sharp radius and zero-variance classification.** The risk is a quadratic polynomial in \(s=h^2\ge0\). If \(T\ne0\) its quadratic coefficient is strictly positive because \(W>0\). The coefficient of \(s\) is \((d-k)(b\cdot t)/(k(d+2))\), giving the stated if-and-only-if, optimum and exact gap by completing the square. The variance formula is a sum of two nonnegative terms; its zero set gives the stated classifications. If \(H=0\), then \(T_{ijl}=(t_i\delta_{jl}+t_j\delta_{il}+t_l\delta_{ij})/(d+2)\); its associated homogeneous cubic equals \((t\cdot x)\|x\|^2/[2(d+2)]\), establishing the radial form and converse.

**Global convexity of the example.** The Hessian of \((v\cdot x)\|x\|^2\) is \(2(vx^{\mathsf T}+xv^{\mathsf T})+2(v\cdot x)I\), whose smallest eigenvalue is bounded below by \(-6\|v\|\|x\|\). The Hessian of \(\lambda\|x\|^4\) is at least \(4\lambda\|x\|^2 I\). Thus the total Hessian is bounded below by \((a-9/(4\lambda))I\succ0\) when \(\|v\|=1\). Its even terms cancel in the central differences, yielding the exact displayed risk and sharp optimum.

## Verification

The standalone \(\texttt{verify.py}\) uses rational arithmetic and no nonstandard dependencies. It reconstructs sphere moments directly from even-monomial double-factorial formulas and compares the resulting exact estimator mean, variance and gradient risk against the tensor identities for dimensions \(2\le d\le5\), all admissible frame sizes, several nonzero and limiting radii, and random, radial and harmonic cubic tensors. It also compares actual symmetric function evaluations on rational orthogonal frames with the harmonic reduction, checks the sharp radial-risk quadratic identity for dimensions through \(11\), and validates tensor trace identities. The executed checker reported **1967 exact rational assertions passed**. These finite checks are evidence of faithful normalization and calculation, not a proof for arbitrary dimension; the universal proof is given above.

## Relationship to prior work

Feng and Wang (arXiv:2205.14737, first public 2022-05-29) introduce precisely the Haar-Stiefel centered gradient estimator and establish bounds for its variance and smoothing bias on smooth functions. Their spherical projection and Stiefel marginal facts, and the method itself, are prior art. The current finding evaluates the **exact cubic-order Euclidean risk**, separates radial and harmonic parts, identifies the complete zero-variance cases, and exhibits a sharp noise-free nonzero-radius risk optimum. The examined gradient-variance and bias theorems in that paper are upper bounds, not these tensor-resolved risk equalities or the signed radius criterion. Kozak et al. (arXiv:2107.03941) and Rando et al. (arXiv:2206.05124) develop structured random-direction descent and convergence theory, using forward differences, rather than the present exact central-difference cubic-jet risk law. Yu et al. (arXiv:2406.19617), Algorithm 1 and Theorem 4.1, prove sharp general bias and covariance bounds for independently sampled spherical or ellipsoidal directions with noisy feedback; their independent-direction estimator does not imply the exact mutually orthogonal cubic-jet risk or its signed radius threshold. No novelty is claimed for basic sphere moment formulas, Haar frames, the finite-difference estimator, or generic bias-variance decomposition.

## Limitations

This is an exact single-point noiseless calculation for a cubic odd part plus arbitrary even part. General smooth functions contain higher odd terms, so the formula does not remain exact without controlling remainders. It provides no convergence guarantee for iterative optimization and no optimality for nonlinear or adaptive estimators. The risk-minimizing radius uses the unknown gradient and third derivative and is therefore an oracle benchmark, not a directly executable tuning rule without additional estimation. The strongly convex example has quartic growth and does not satisfy a globally bounded-Hessian hypothesis. Numerical code and scientific novelty remain subject to independent review; no independent audit has been performed.

## References

1. Y. Feng and T. Wang, *Stochastic Zeroth Order Gradient and Hessian Estimators: Variance Reduction and Refined Bias Bounds*, arXiv:2205.14737 (first public 2022-05-29), https://arxiv.org/abs/2205.14737.
2. D. Kozak, C. Molinari, L. Rosasco, L. Tenorio and S. Villa, *Zeroth order optimization with orthogonal random directions*, arXiv:2107.03941 (first public 2021-07-08), https://arxiv.org/abs/2107.03941.
3. M. Rando, C. Molinari, S. Villa and L. Rosasco, *Stochastic Zeroth Order Descent with Structured Directions*, arXiv:2206.05124 (2022), https://arxiv.org/abs/2206.05124.
4. Y. Feng and T. Wang, journal version, *Information and Inference*, 12 (2023), 1514--1545, https://doi.org/10.1093/imaiai/iaad014 (a later version of reference 1, not a separate first-public source).
5. Q. Yu, Y. Wang, B. Huang, Q. Lei and J. D. Lee, *Stochastic Zeroth-Order Optimization under Strongly Convexity and Lipschitz Hessian: Minimax Sample Complexity*, arXiv:2406.19617 (first public 2024-06-28), https://arxiv.org/abs/2406.19617.
