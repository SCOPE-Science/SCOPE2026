# Sharp principal-angle and stepsize stability for inexact high-index saddle reflections

## Finding

Let \(H\) be any real symmetric nonsingular Hessian of Morse index \(k\), where \(1\le k<n\), and let \(M\) be any symmetric positive-definite metric. Set
\[
B=M^{-1/2}HM^{-1/2},\qquad D=|B|=(B^2)^{1/2},
\qquad \mu=\lambda_{\min}(D),\quad L=\lambda_{\max}(D).
\]
Let \(P\) project orthogonally onto the negative eigenspace of \(B\). At each step choose *any* rank-\(k\) orthogonal projector \(Q_m\) with
\[
\|P-Q_m\|_2\le \sin\vartheta,
\qquad 0\le\vartheta\le\pi/2.
\]
No continuity, convergence, or consistency between successive choices is imposed. The inexact reflected-gradient Euler step on the quadratic energy \(E(x)=\frac12 x^\top Hx\) is
\[
x_{m+1}=x_m-\eta M^{-1/2}(I-2Q_m)M^{-1/2}Hx_m.
\]
The exact (strict) uniform contraction phase diagram in the absolute-Hessian energy norm
\[
\|x\|_{M,D}=\left((M^{1/2}x)^\top D(M^{1/2}x)\right)^{1/2}
\]
for **all dimensions, indices, admissible Hessians, metrics, starting points, and arbitrarily changing projectors** is
\[
\boxed{\quad \vartheta<\pi/4\quad\text{and}\quad
0<\eta<\frac{2\cos(2\vartheta)}{L}.\quad}
\]
Within this region, every step satisfies the quantitative estimate
\[
\boxed{\quad
\|x_{m+1}\|_{M,D}^{2}
\le\left[1-\eta\mu\bigl(2\cos(2\vartheta)-\eta L\bigr)\right]
\|x_m\|_{M,D}^{2}.\quad}
\]
The bracket lies in \([0,1)\). Both boundaries are sharp for the uniform guarantee: when a condition is violated, a two-dimensional index-one quadratic admits a constant admissible projector giving no contraction, and beyond the boundary gives strict expansion. In particular, at the \(45^\circ\) angular boundary *every positive step* can expand the error.

## Assumptions and scope

The theorem concerns exact quadratic objectives with an SPD preconditioner fixed across iterations, but permits the approximate negative eigenspace to vary arbitrarily at each iteration. The Hessian is nonsingular, not necessarily spectrally simple, and its negative spectral subspace has dimension \(k\). The numerical step uses the orthogonal reflection in the metric determined by \(M\), not a nonorthogonal approximate projector. All matrix norms on projectors are spectral norms; the projector discrepancy is the sine of the largest principal angle. The statement is a *universal* contraction characterization, not an assertion that every individual instance outside the region diverges.

Equivalently, if \(\widehat V_m^\top M\widehat V_m=I_k\), then \(Q_m=M^{1/2}\widehat V_m\widehat V_m^\top M^{1/2}\), and the step is
\[
x_{m+1}=x_m-\eta(I-2\widehat V_m\widehat V_m^\top M)M^{-1}Hx_m.
\]
The relevant preconditioned spectral bounds are \(0<\mu\le L\), independent of whether the eigenvalues of \(H\) are positive or negative.

## Proof

1. **Polar reflection identity.** Write \(S=\operatorname{sgn}(B)=I-2P\). Since \(B=SD=DS\), the exact reflector reverses exactly the negative eigenspace. Set \(R_m=I-2Q_m\) and \(U_m=R_mS\). Both \(R_m\) and \(S\) are orthogonal and symmetric; therefore \(U_m\) is orthogonal. Expanding the product of the two Householder-type reflections and using \(P^2=P\), \(Q_m^2=Q_m\) gives the *exact identity*
   \[
   \frac{U_m+U_m^\top}{2}=I-2(P-Q_m)^2.
   \]
   The projector-error hypothesis implies \(0\preceq(P-Q_m)^2\preceq\sin^2\vartheta\,I\). Thus
   \[
   \frac{U_m+U_m^\top}{2}\succeq\cos(2\vartheta)I.
   \]

2. **Natural energy-coordinate step.** Put \(z=M^{1/2}x\), \(y=D^{1/2}z\). Conjugation of the reflected update yields
   \[
   y_{m+1}=(I-\eta C_m)y_m,
   \qquad C_m=D^{1/2}U_mD^{1/2}.
   \]
   This transformation is valid because \(D\) is SPD. Its Euclidean squared norm equals the original absolute-Hessian energy norm squared.

3. **One-step energy inequality.** For \(c=\cos(2\vartheta)\), the symmetric-part estimate gives
   \[
   C_m+C_m^\top\succeq 2cD.
   \]
   Orthogonality of \(U_m\) and \(D\preceq LI\) give the other needed inequality:
   \[
   C_m^\top C_m
   =D^{1/2}U_m^\top D U_mD^{1/2}\preceq LD.
   \]
   Consequently, for every \(y\),
   \[
   \begin{aligned}
   \|(I-\eta C_m)y\|_2^2
   &=\|y\|_2^2-\eta y^\top(C_m+C_m^\top)y+\eta^2y^\top C_m^\top C_my\\
   &\le\|y\|_2^2-\eta(2c-\eta L)y^\top Dy.
   \end{aligned}
   \]
   When \(\vartheta<\pi/4\) and \(0<\eta<2c/L\), using \(D\succeq\mu I\) proves the claimed uniform strict contraction and hence geometric convergence for every sequence of inexact frames. The bracket is nonnegative because \(\eta\mu(2c-\eta L)\le\mu c^2/L\le1\).

4. **Sharpness of both frontiers.** Let \(n=2\), \(k=1\), \(M=I\), and \(H=L\operatorname{diag}(-1,1)\). Take \(P\) onto the first coordinate and \(Q\) onto \((\cos\vartheta,\sin\vartheta)^\top\). Then \(D=LI\), \(\|P-Q\|_2=\sin\vartheta\), and \(U=(I-2Q)(I-2P)\) is a planar rotation through an angle of magnitude \(2\vartheta\). Direct multiplication gives
   \[
   (I-\eta LU)^\top(I-\eta LU)
   =\left(1-2\eta L\cos(2\vartheta)+\eta^2L^2\right)I.
   \]
   For \(0\le\vartheta<\pi/4\), strict contraction holds here **exactly** for \(0<\eta<2\cos(2\vartheta)/L\), becomes an isometry at the upper endpoint, and expands above it. For \(\vartheta\ge\pi/4\), every \(\eta>0\) expands. This single admissible index-one family disproves any universally larger angle or step region. Thus the characterization is necessary and sufficient for the stated uniform guarantee.

## Verification

The standalone `verify.py` uses standard-library exact rational arithmetic. It tests the reflection identity, the positive-semidefinite contraction gap on orthogonally mixed two-, four-, and six-dimensional quadratics, the exact sharp equality at a rational-angle two-dimensional boundary, strict expansion past that boundary, and expansion at \(45^\circ\). The runs pass. The optional standalone `numerical_stress.py` (requires NumPy) performs a deterministic 1,000-instance stress test, spanning dimensions two through twelve and many Morse indices, independently checking the bound and projector identity. The finite tests are illustrations and defect screens; the proof for arbitrary dimension and indefinite Hessian is the algebraic argument above.

## Relationship to prior work

Huang, Su, Zhang, and Zhao introduced preconditioned high-index saddle dynamics and proved a local nonlinear convergence estimate with a sufficient projector-error restriction \(\theta<1/(2\kappa_M)\) at the fixed step \(\eta=2/(\mu+L)\). That bound is in the \(M\)-norm and addresses nonlinear perturbations; it does not state the present exact quadratic energy-norm angular/stepsize characterization, nor its universal sharpness under freely switching approximate frames. The new theorem trades a tunable smaller step and an absolute-Hessian norm for the sharp \(45^\circ\) maximum frame angle in this narrower quadratic setting.

Chu and Lin study generalized gentlest ascent reflectors and evolving subspace flows; their reflector/gradient alignment discussion is different from a uniform principal-angle error of the estimated negative Hessian subspace. Zhao's regional-reflector Euler analysis proves local convergence for sufficiently small steps without optimizing the step-size law. The related curvature-scaled and perturbed high-index saddle literature concerns different or broader dynamics, but remains a priority comparison risk where entire texts were not accessible. The two-reflection identity is elementary; the claim here is the sharp universal phase diagram for the specified numerical iteration, not discovery of that matrix identity.

## Limitations

This statement does not prove nonlinear local convergence with a \(45^\circ\) inexact projector, guarantee convergence in the unweighted \(M\)-norm, incorporate inaccurate nonorthogonal frames, establish an adaptive stepsize rule, or certify the efficiency of an inner eigensolver. It is a uniform error-contraction theorem in the stated absolute-Hessian energy norm and allows arbitrarily changing frame errors only within the asserted bound. Its historical originality is qualified by incomplete access to some contemporary full texts and potential alternate formulations in older reflector literature; independent validation has not been performed.

## References

1. Bingzhang Huang, Hua Su, Lei Zhang, and Jin Zhao, *Computing Saddle Points in Stiff Problems via a Preconditioned High-index Saddle Dynamics Method*, arXiv:2603.25390, first posted 26 March 2026; version 2, 22 May 2026. https://arxiv.org/abs/2603.25390. In particular, §§3–5 and Theorem 5.2.
2. Moody T. Chu and Matthew M. Lin, *Generalized Gentlest Ascent Dynamics Methods for High-Index Saddle Points*, SIAM Journal on Numerical Analysis 63 (2025), DOI 10.1137/24M1710905. https://epubs.siam.org/doi/full/10.1137/24M1710905.
3. Jin Zhao, *Regional Reflector Dynamics for Saddle Search: Stability and Sampling Design*, publicly available May 2026. https://www.researchgate.net/publication/404708493_Regional_Reflector_Dynamics_for_Saddle_Search_Stability_and_Sampling_Design, §§3–4.
4. Jianyuan Yin, Lei Zhang, and Zhiyi Zhang, *Subspace curvature-scaling high-index saddle dynamics for accelerating ill-conditioned saddle point searches*, arXiv:2607.03030 (2026). https://arxiv.org/abs/2607.03030. Abstract-level comparison only.
5. Baoming Shi, Lei Zhang, Xiangcheng Zheng, and Shangqin Zhu, *Asymptotic stability of high-index saddle dynamics*, arXiv:2611.09049 (6 November 2026). https://arxiv.org/abs/2611.09049. Abstract-level comparison only; full-text priority comparison remains unresolved.
