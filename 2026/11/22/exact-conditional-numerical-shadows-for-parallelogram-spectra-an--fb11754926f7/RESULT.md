# Exact conditional numerical shadows for parallelogram spectra and a universal factor-two regression gain

## Finding
Let \(A\) be a normal matrix on \(\mathbb C^4\) with four eigenvalues \(z_0+s u+t v\), indexed by \(s,t\in\{-1,1\}\), where \(u,v\in\mathbb C\) are linearly independent over \(\mathbb R\). Let \(h\) be uniform on the complex unit sphere. For any \(B\) commuting with \(A\), write in this eigenbasis
\[
B=c_0 I+c_1 S+c_2 T+c_3 ST,
\]
where \(S=\operatorname{diag}(1,1,-1,-1)\) and \(T=\operatorname{diag}(1,-1,1,-1)\) (ordered \((++),(+-),(-+),(--)\)). Observe \(Z_A=\langle Ah,h\rangle\) and seek to predict \(Z_B=\langle Bh,h\rangle\) in squared absolute loss.

Since \(Z_A=z_0+uX+vY\) with uniquely determined real \(X,Y\in[-1,1]\), define
\[
L(x,y)=-1+|x+y|,\quad U(x,y)=1-|x-y|,
\quad m(x,y)=\tfrac12\bigl(|x+y|-|x-y|\bigr).
\]
The conditional law of \(Z_B\) given \(Z_A=z_0+ux+vy\) is uniform along the line segment from \(c_0+c_1x+c_2y+c_3L(x,y)\) to \(c_0+c_1x+c_2y+c_3U(x,y)\), interpreted as a point mass when \(c_3=0\). Consequently the unique optimal square-integrable predictor (almost everywhere) is
\[
F_*(z_0+ux+vy)=c_0+c_1x+c_2y+c_3m(x,y).
\]
Its exact squared-error risk and the best real-affine predictor's squared-error risk are respectively
\[
\boxed{\ \mathcal E_{\rm nonlinear}(B\mid A)=|c_3|^2/10,\qquad
\mathcal E_{\rm affine}(B\mid A)=|c_3|^2/5.\ }
\]
In particular **every genuinely hidden commuting direction gains exactly one half of its optimal affine mean-square error through nonlinear recovery**, independently of the parallelogram geometry and the target coefficients. Exact recovery occurs if and only if \(c_3=0\).

## Assumptions and scope
All four eigenvalues are distinct because \(u,v\) are real-linearly independent. Thus every matrix commuting with \(A\) is diagonal in its eigenbasis, and the above four Walsh coefficients \(c_j\in\mathbb C\) are uniquely defined. The sphere measure is normalized complex Haar measure (not the uniform real sphere measure). Conditional statements hold for almost every measured \(z\) in the interior of the parallelogram; boundary laws can be chosen by continuous interval collapse. Predictors are measurable complex-valued functions; a real-affine predictor is an affine function of the real and imaginary parts of \(Z_A\).

## Proof
**1. Uniform simplex and exact fiber.** Set \(p_{st}=|h_{st}|^2\) and \(X=\sum_{s,t}sp_{st}\), \(Y=\sum_{s,t}tp_{st}\), \(Q=\sum_{s,t}stp_{st}\). The established complex Haar-coordinate law is \((p_{++},p_{+-},p_{-+},p_{--})\sim\operatorname{Dirichlet}(1,1,1,1)\), of density \(6\) in the three independent simplex coordinates. The inverse Walsh transform is
\[
p_{st}=\frac{1+sX+tY+stQ}{4}.
\]
The Jacobian for the map from \((X,Y,Q)\) to three independent \(p\)-coordinates is \(1/16\); hence the joint density of \((X,Y,Q)\) is the constant \(3/8\) on its feasible region. Positivity of the four \(p_{st}\) is equivalent to \(|X|,|Y|\le1\) and
\[
-1+|X+Y|\le Q\le1-|X-Y|.
\]
The interval length equals \(2(1-\max(|X|,|Y|))\). Therefore \(Q\), conditional on \((X,Y)=(x,y)\), is uniform on precisely this interval, while the planar observation density is
\[
f_{X,Y}(x,y)=\frac34(1-\max(|x|,|y|))\mathbf 1_{[-1,1]^2}(x,y).
\]
The real-linear independence of \(u,v\) makes \(Z_A\) equivalent as a measurable observation to \((X,Y)\).

**2. Exact nonlinear predictor and risk.** Since \(Z_B=c_0+c_1X+c_2Y+c_3Q\), the conditional mean of \(Q\) is \(m(X,Y)=(L+U)/2\), and its conditional variance is
\[
\operatorname{Var}(Q\mid X,Y)=\frac13(1-\max(|X|,|Y|))^2.
\]
Conditional expectation is the unique \(L^2\)-minimizing predictor. Integrate against \(f_{X,Y}\) by using the area differential \(8r\,dr\) of squares with maximum-coordinate radius \(r\):
\[
\begin{aligned}
\mathbb E\operatorname{Var}(Q\mid X,Y)
&=\frac13\cdot\frac34\cdot 8\int_0^1r(1-r)^3\,dr\\
&=2\operatorname{B}(2,4)=\frac1{10}.
\end{aligned}
\]
This proves the optimal nonlinear formula including its exact residual loss.

**3. Optimal affine loss.** The random variables \(X,Y,Q\) are centered and pairwise uncorrelated: independent sign changes of the four Walsh labels preserve the uniform simplex law and reverse the corresponding cross terms. Moreover, the complex Haar fourth-moment formula gives \(\mathbb E Q^2=\operatorname{Tr}((ST)^2)/(4\cdot5)=1/5\). Hence the orthogonal \(L^2\) projection of \(Z_B\) onto \(\operatorname{span}_{\mathbb C}\{1,X,Y\}\) is \(c_0+c_1X+c_2Y\) and the smallest affine mean-square error is \(|c_3|^2/5\). Division yields the universal factor \(1/2\) for every \(c_3\ne0\); if \(c_3=0\), both errors vanish. All assertions follow.

## Verification
The independent, self-contained Python 3 script `verify.py` uses exact fractions and tests the Walsh inversion, every rational simplex grid point of denominator seven, positivity and conditional endpoints on a second rational grid, the Beta-integral identities, and the ratio of the two theoretical risks. It reports `PARALLELOGRAM_NUMERICAL_SHADOW_EXACT_CHECK_OK 3853`. Finite checks corroborate algebra; the continuous distribution and all-parameter claims follow from the proof, not from grid enumeration.

## Relationship to prior work
D. M. Johnson (2026) characterizes exact numerical-information dependence via affine combinations of the real and imaginary parts of an operator; that is a qualitative zero-loss theorem, not the conditional distribution or nonzero-loss optimum computed here. Dunkl, Gawron, Holbrook, Puchała and Życzkowski (2010), Section IV, identify normal numerical shadows as uniform-simplex projections and illustrate square spectra; their simplex law is explicitly used above and the marginal shadow density is **not** claimed as new. A published 2026 exact Haar-regression criterion for general normal matrices gives the best affine loss and identifies when nonlinearity can help; it does not give the stated complete parallelogram posterior or its exact universal factor-one-half risk. The separate published three-level classification treats collinear and triangular spectra and does not imply a four-corner hidden-mode conditional law.

## Limitations
The claim concerns four simple spectral values that form a nondegenerate parallelogram, and targets commuting with the observed normal matrix. It does not classify general quadrilateral spectra, repeated eigenvalues, noncommuting targets, or non-Haar probe ensembles. The inherited simplex law and best-affine projection are established ingredients rather than independent new results. Earlier equivalent formulas in the probability theory of conditional Dirichlet projections could supersede the quantitative conclusion; exhaustive publication-priority certification and independent validation have not been performed.

## References
- D. M. Johnson, *Numerical Information of Hilbert Space Operators*, arXiv:2610.29826v1, first public 21 October 2026. https://arxiv.org/abs/2610.29826
- C. F. Dunkl, P. Gawron, J. A. Holbrook, Z. Puchała and K. Życzkowski, *Numerical shadows: measures and densities on the numerical range*, arXiv:1010.4189v1 (2010), Section IV, Lemma 4.1 and Fig. 3. https://arxiv.org/abs/1010.4189
- *An exact Haar-regression criterion for numerical information of normal matrices* (2026), published mathematical record: https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-an-exact-haar-regression-criterion-for-numerical-information-of--56cf8c2fea12
- *Exact conditional numerical-shadow loss for normal three-level matrices* (2026), published mathematical record: https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-conditional-numerical-shadow-loss-for-normal-three-level-m--8f78f56cee13
