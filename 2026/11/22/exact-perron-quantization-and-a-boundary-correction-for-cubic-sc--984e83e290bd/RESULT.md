# Exact Perron quantization and a boundary correction for cubic Schoenberg averaging

## Finding

Let \(S_n:C([0,1])\to C([0,1])\) be the classical uniform *clamped cubic* Schoenberg–Greville operator on \(n\ge6\) equal subintervals. Let \(Lf(x)=(1-x)f(0)+xf(1)\). Its precise asymptotic convergence rate is
\[
\gamma_n=\lim_{m\to\infty}\|S_n^m-L\|_{C\to C}^{1/m}
=\frac{2+\cos\theta_n}{3},
\]
where \(\theta_n\) is the **unique** root in \((0,\pi/(n-2))\) of
\[
\tan\!\left(\frac{n-2}{2}\theta\right)
=\frac{9\cos^2\theta+7\cos\theta-4}
{3(3\cos\theta+1)\sin\theta}.
\]
For increasingly fine uniform meshes, its sharp spectral-gap expansion is
\[
1-\gamma_n=\frac{\pi^2}{6n^2}
-\frac{\pi^4}{72n^4}
-\frac{\pi^4}{9n^5}+O(n^{-6}).
\]
The nonzero \(n^{-5}\) term is a boundary contribution beyond the leading discrete-diffusion and dispersion terms. These statements determine the top nontrivial eigenvalue, not the entire spectrum.

## Assumptions and scope

Fix an integer \(n\ge6\). Work first in the coordinate \(z=nx\in[0,n]\). The knot vector is \((0,0,0,0,1,2,\ldots,n-1,n,n,n,n)\). Let \(B_j\), \(0\le j\le n+2\), denote its degree-three normalized B-splines, and let \(\xi_j=(t_{j+1}+t_{j+2}+t_{j+3})/3\) be the Greville nodes. Then \(S_nf(z)=\sum_j f(\xi_j)B_j(z)\), with the equivalent rescaling \(z=nx\). The endpoint interpolation \(L\) always uses the values at \(0\) and \(1\) in the original coordinate. No weights, nonuniform knots, or other spline degrees are included. The operator norm is the uniform \(C([0,1])\) norm, and the limit holds with \(n\) fixed as \(m\to\infty\).

## Proof

**1. Interior matrix.** Let \(P=(B_j(\xi_i))_{0\le i,j\le n+2}\). Since \(B_0(0)=B_{n+2}(n)=1\) and the other endpoint basis values vanish, \(P\) has diagonal endpoint blocks \(1\) and central block \(Q\) indexed \(1\le i,j\le n+1\). Recursive cubic B-spline evaluation gives the first two rows of \(Q\):
\[
Q_{1,1:3}=(61/108,43/324,1/162),\qquad
Q_{2,1:3}=(1/4,7/12,1/6),
\]
with all other entries in those rows zero. For \(3\le i\le n-1\), the only nonzero entries are \(Q_{i,i-1}=Q_{i,i+1}=1/6\) and \(Q_{i,i}=2/3\). The last two rows are the reversals of the first two. These identities follow from the de Boor recursion, and are independently evaluated with exact fractions in the accompanying checker. The central matrix is irreducible, nonnegative, substochastic, has positive diagonal, and its two outer rows have row sum strictly below one. Therefore its Perron eigenvalue \(\rho(Q)\) is simple and lies strictly between zero and one, and dominates every other eigenvalue in modulus.

**2. Boundary elimination.** Write \(\lambda v=Qv\), with indices \(v_1,\ldots,v_{n+1}\). At the left boundary the two equations are
\[
(\lambda-61/108)v_1=(43/324)v_2+(1/162)v_3,\quad
(\lambda-7/12)v_2=(1/4)v_1+(1/6)v_3.
\]
For \(\lambda>5/9\), elimination gives
\[
v_1=\frac{\lambda+3}{3(9\lambda-5)}v_2,\qquad
v_3=\frac{2(27\lambda^2-31\lambda+8)}{9\lambda-5}v_2.
\]
Put \(\lambda=(2+\cos\theta)/3\) and \(c=\cos\theta\). All central rows now reduce to \(v_{i+1}-2c v_i+v_{i-1}=0\). A reflection-symmetric solution on \(2\le i\le n\) is
\[
v_i=\cos\left(\left(i-\frac{n+2}{2}\right)\theta\right).
\]
The ratio of its third and second coordinates is \(c+\sin\theta\tan((n-2)\theta/2)\). Matching the eliminated boundary ratio gives the displayed tangent equation. The reflected last two boundary equations are then satisfied by \(v_{n+1}=v_1\).

**3. Unique positive root and identification.** Let \(g(c)=(9c^2+7c-4)/(3(3c+1))\). For \(n\ge6\) and \(0<\theta<\pi/(n-2)\), we have \(c\ge\cos(\pi/4)>0\), \(g(c)>0\), and \(g'(c)>0\). The left side of \(\tan((n-2)\theta/2)=g(\cos\theta)/\sin\theta\) increases continuously from zero to infinity; the right side decreases continuously from infinity to a finite positive value. There is exactly one root. Its cosine profile is strictly positive on indices \(2,\ldots,n\), and the boundary factor \((\lambda+3)/(3(9\lambda-5))\) is positive, so the entire eigenvector is strictly positive. By Perron–Frobenius, \(\lambda=\rho(Q)=\gamma_n\). Since \(S_n\) reproduces affine functions and preserves endpoint values, \(S_nL=LS_n=L\). The nontrivial spectrum of \(S_n-L\) is the spectrum of \(Q\); the spectral-radius formula then gives the claimed norm-root limit.

**4. Fine-mesh expansion.** Define \(\delta(\theta)=\arctan(\sin\theta/g(\cos\theta))\). The positive-root equation is equivalently
\[
(n-2)\theta_n+2\delta(\theta_n)=\pi.
\]
Taylor expansion at zero yields \(g(\cos\theta)=1-2\theta^2/3+O(\theta^4)\) and \(\delta(\theta)=\theta+\theta^3/6+O(\theta^5)\). Consequently \(\theta_n=\pi/n-\pi^3/(3n^4)+O(n^{-6})\). Substituting into \((1-\cos\theta_n)/3\) gives all three displayed terms and an \(O(n^{-6})\) remainder.

## Verification

The standalone `check.py` evaluates the complete cubic Greville collocation block using exact rational Cox–de Boor recursion, compares all asserted row patterns and their reflection, constructs the positive root numerically by bisection, and checks an independently constructed positive eigenvector against that exact collocation block. It passed for every \(n=6,\ldots,28\), with maximum displayed residual near machine precision. It also checked the asymptotic expansion at \(n=40,60,100,200\). The symbolic proof, not the finite diagnostics, establishes the result for every integer \(n\ge6\).

## Relationship to prior work

Nagler and Kähler (arXiv:1312.5546v1, 2013) proved iteration and approximation estimates for uniform Schoenberg operators without an explicit cubic Perron root. Nagler, Cerejeiras, and Forster (arXiv:1402.2403v1, 2014) established abstract spectral convergence bounds and expressly asked about the second largest eigenvalue, stating that its explicit form was unknown. Nagler (arXiv:1403.4522v1, 2014) gives a more general peripheral-spectrum theorem, which does not determine interior eigenvalues. Nagler's 2015 thesis establishes reality and simplicity but does not give this cubic quantization or three-term gap law. The contribution here is the exact cubic boundary quantization and the sharp high-order rate, rather than general convergence or the lower spectral edge.

## Limitations

The theorem covers only the uniform clamped cubic Greville rule and meshes with \(n\ge6\). It does not claim explicit formulas for the other positive eigenvalues, eigenvector normalization, arbitrary knot vectors, degree-uniform estimates, or finite-iterate norm constants. Undiscovered equivalent computations in older spline-collocation literature remain a novelty risk.

## References

- J. Nagler and U. Kähler, *A lower bound for the uniform Schoenberg operator*, arXiv:1312.5546v1 (2013), https://arxiv.org/abs/1312.5546.
- J. Nagler, P. Cerejeiras and B. Forster, *Lower bounds for the approximation with variation-diminishing splines*, arXiv:1402.2403v1 (2014), https://arxiv.org/abs/1402.2403.
- J. Nagler, *On the spectrum of positive finite-rank operators with a partition of unity property*, arXiv:1403.4522v1 (2014), https://arxiv.org/abs/1403.4522.
- J. Nagler, *Digital Curvature Estimation: An Operator Theoretic Approach*, doctoral thesis (2015), Section 3.2.3, https://d-nb.info/1078405816/34.
