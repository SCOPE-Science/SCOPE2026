# Degree three and dimension three are jointly minimal for Chebyshev positivity loss
## Finding
Consider classical Chebyshev semi-iteration for \(Ax=b\), starting from \(x_0=0\), where \(A\) is a real symmetric positive definite Stieltjes matrix and \(b\ge 0\). Assume that the Chebyshev interval is the exact spectral interval \([\lambda_{\min}(A),\lambda_{\max}(A)]\). Positive rescaling reduces the analysis to \(\lambda_{\min}(A)=1\) and \(\kappa=\lambda_{\max}(A)>1\).

Let \(p_m\) be the degree-\(m\) residual polynomial and \(q_m(\lambda)=(1-p_m(\lambda))/\lambda\), so that \(x_m=q_m(A)b\). Then the first two iterates are entrywise nonnegative in every dimension. The third iterate is entrywise nonnegative for every such problem in dimensions one and two, but not in dimension three. Hence iteration degree three and matrix dimension three are jointly minimal for coordinatewise positivity loss under exact extremal spectral bounds.

A rational witness is
\[
A=\operatorname{diag}\!\left(1,\begin{pmatrix}79/20&-1/20\\-1/20&79/20\end{pmatrix}\right),
\qquad
b=\begin{pmatrix}1\\1\\1/1000\end{pmatrix}.
\]
The spectrum is exactly \(\{1,39/10,4\}\), so \(\kappa=4\). The third iterate is
\[
x_3=\begin{pmatrix}
338/365\\[2pt]
304248/1140625\\[2pt]
-6783/4562500
\end{pmatrix},
\]
whereas
\[
A^{-1}b=\begin{pmatrix}1\\6077/24000\\83/24000\end{pmatrix}>0.
\]

## Assumptions and scope
A Stieltjes matrix here means a real symmetric positive definite matrix with nonpositive off-diagonal entries. The result concerns exact arithmetic, zero initial guess, and the classical Chebyshev residual polynomial constructed from the exact extremal eigenvalues. It does not assert positivity for loose spectral bounds, nonsymmetric \(M\)-matrices, preconditioned systems whose transformed operator is not Stieltjes, finite-precision recurrences, or iterates of degree four and above.

## Proof
After scaling, the exact interval is \([1,\kappa]\). Write
\[
p_m(\lambda)=
\frac{T_m\!\left((\kappa+1-2\lambda)/(\kappa-1)\right)}
{T_m\!\left((\kappa+1)/(\kappa-1)\right)}
\]
and \(q_m(\lambda)=(1-p_m(\lambda))/\lambda\). Since \(b-Ax_m=p_m(A)b\) and \(A\) is nonsingular, \(x_m=q_m(A)b\).

For degree one,
\[
q_1(\lambda)=\frac{2}{\kappa+1},
\]
so \(q_1(A)\) is a positive scalar multiple of the identity.

For degree two, direct reduction of \(T_2\) gives
\[
q_2(\lambda)=\frac{8(\kappa+1-\lambda)}{\kappa^2+6\kappa+1}.
\]
Therefore
\[
q_2(A)=\frac{8}{\kappa^2+6\kappa+1}\bigl((\kappa+1)I-A\bigr).
\]
Every off-diagonal entry is nonnegative because \(A\) is a Stieltjes matrix. Moreover \(A_{ii}\le\lambda_{\max}(A)=\kappa\), so every diagonal entry of \((\kappa+1)I-A\) is at least one. Thus \(q_2(A)\) is entrywise nonnegative in every dimension.

For degree three,
\[
q_3(\lambda)=
\frac{2\bigl(9\kappa^2-24\kappa\lambda+30\kappa+16\lambda^2-24\lambda+9\bigr)}
{(\kappa+1)(\kappa^2+14\kappa+1)}.
\]
At the two endpoints,
\[
q_3(1)=\frac{2(3\kappa+1)^2}{(\kappa+1)(\kappa^2+14\kappa+1)},
\qquad
q_3(\kappa)=\frac{2(\kappa+3)^2}{(\kappa+1)(\kappa^2+14\kappa+1)},
\]
and
\[
\frac{q_3(\kappa)-q_3(1)}{\kappa-1}
=-\frac{16}{\kappa^2+14\kappa+1}<0.
\]
If \(A\) is two-dimensional and its exact spectral endpoints are \(1\) and \(\kappa\), functional calculus reduces \(q_3(A)\) to
\[
q_3(A)=c_0I+c_1A,
\qquad
c_1=-\frac{16}{\kappa^2+14\kappa+1}<0.
\]
Its off-diagonal entries are nonnegative because those of \(A\) are nonpositive. Its two eigenvalues are \(q_3(1)>0\) and \(q_3(\kappa)>0\), so its diagonal entries are positive. Hence \(q_3(A)\) is entrywise nonnegative. Dimension one is immediate.

For the displayed three-dimensional witness, the trailing block has eigenvalues \(39/10\) and \(4\). At \(\kappa=4\),
\[
q_3(\lambda)=\frac{2(16\lambda^2-120\lambda+273)}{365}.
\]
Consequently the trailing \(2\times2\) block of \(q_3(A)\) has diagonal entry \(2434/9125\) and off-diagonal entry \(-16/9125\). Multiplication by \((1,1/1000)^{\mathsf T}\) gives third coordinate \(-6783/4562500\), proving sign loss. Direct inversion gives the strictly positive exact solution displayed above.

## Verification
The bundled checker uses exact rational arithmetic. It verifies the witness spectrum, reconstructs the degree-three matrix polynomial, checks the stated iterate exactly, verifies the negative coordinate, and verifies \(A(A^{-1}b)=b\). The universal degree-one, degree-two, and two-dimensional degree-three statements are proved symbolically above rather than inferred from finite tests.

## Relationship to prior work
Classical Chebyshev semi-iteration, its residual-polynomial characterization, spectral-interval assumptions, and minimax residual property are prior work. Gutknecht and Röllin's research report *The Chebyshev iteration revisited* gives the scaled Chebyshev residual polynomial, treats the symmetric positive definite interval case, and classifies the subject primarily as MSC 65F10. Meng, Saunders, and Mahoney use Chebyshev semi-iteration as a communication-efficient iterative component in LSRN; the first public arXiv version is dated 2011-09-27.

The new statement concerns coordinatewise order structure rather than residual minimaxity, roundoff stability, communication cost, or Euclidean nonexpansion. Searches for Chebyshev semi-iteration together with Stieltjes, \(M\)-matrix, nonnegative-iterate, positivity, monotonicity, and overshoot terminology did not locate a theorem implying the joint degree/dimension boundary above. Published results on stagewise-safe Richardson and weighted-Jacobi damping compare norm behavior, not entrywise positivity of \(q_m(A)\).

## Limitations
The counterexample is reducible; no irreducible minimal witness is claimed. Exact extremal spectral bounds are essential to the two-dimensional proof and are part of the theorem. No claim is made about coordinatewise positivity at later degrees, about arbitrary spectral enclosures, or about floating-point implementations. The literature search leaves residual risk that an older monotone-iteration or matrix-polynomial source states an equivalent sign result under different terminology.

## References
1. M. H. Gutknecht and S. Röllin, *The Chebyshev iteration revisited*, ETH Zürich Research Report 2000-16, December 2000; later published in *Parallel Computing* 28 (2002), 263–283. DOI: 10.1016/S0167-8191(01)00139-9.
2. X. Meng, M. A. Saunders, and M. W. Mahoney, *LSRN: A Parallel Iterative Solver for Strongly Over- or Under-Determined Systems*, arXiv:1109.5981v1, first submitted 2011-09-27; later published in *SIAM Journal on Scientific Computing*. DOI: 10.1137/120866580.
