# Sharp subunit-\(q\) obstruction to segment realization by joint numerical ranges

## Finding
Let \(\Omega\) be a nonempty compact Hausdorff space, and let \(f_0,f_1\in C(\Omega)\) be distinct. Write \(L=\|f_1-f_0\|_\infty>0\), and let \(0<|q|<1\). If \(\mathcal H\) is any complex Hilbert space of dimension at least two and \(F\in C(\Omega,\mathcal B(\mathcal H))\), define
\[
\mathcal W_q(F)=\bigl\{\omega\mapsto\langle F(\omega)x,y\rangle:\ \|x\|=\|y\|=1,\ \langle x,y\rangle=q\bigr\}.
\]
Here the inner product is linear in the first variable. For nonempty bounded subsets of \(C(\Omega)\), write \(d_H\) for the symmetric Hausdorff distance in the supremum norm, whether or not either subset is closed. Then, with \(K=\{(1-t)f_0+tf_1:0\le t\le1\}\),
\[
\boxed{\ \inf_{\dim\mathcal H\ge2}\ \inf_{F\in C(\Omega,\mathcal B(\mathcal H))}
 d_H\bigl(\mathcal W_q(F),K\bigr)=
 \frac{L\sqrt{1-|q|^2}}{2\bigl(1+\sqrt{1-|q|^2}\bigr)}.\ }
\]
The infimum is attained by a continuous field of \(2\times2\) normal matrices, with no restriction on \(\Omega\) or on the direction of the complex-valued segment. In particular, no nondegenerate segment in \(C(\Omega)\) is even arbitrarily approximable by a joint \(q\)-numerical range for fixed \(0<|q|<1\), in contrast with exact realization at \(|q|=1\).

A universal geometric inequality underlies the result. For every bounded operator \(T\) on a complex Hilbert space of dimension at least two, every \(0\le |q|<1\), and every real direction \(\theta\),
\[
\boxed{\ \operatorname{width}_{\theta}W_q(T)\ \ge\
\sqrt{1-|q|^2}\,\operatorname{diam}W_q(T).\ }
\]
Here \(W_q(T)=\{\langle Tx,y\rangle:\|x\|=\|y\|=1,\langle x,y\rangle=q\}\), \(\operatorname{width}_{\theta}S=\sup_{z\in S}\operatorname{Re}(e^{-i\theta}z)-\inf_{z\in S}\operatorname{Re}(e^{-i\theta}z)\), and diameter is the supremum of pairwise complex-plane distances. The coefficient is sharp, already for \(T=\operatorname{diag}(-1,1)\).

## Assumptions and scope
All assertions concern bounded complex-linear Hilbert-space operators and norm-continuous operator fields. The parameter \(q\) may be complex, but the segment approximation formula assumes \(q\ne0\) because the scalar-centering construction requires division by \(q\). The universal directional-width inequality also covers \(q=0\). The Hilbert dimension is always at least two, so the constrained unit-vector pair set is nonempty. No compactness of \(F(\omega)\), separability of \(\mathcal H\), finite-dimensionality of \(\Omega\), or selfadjointness of candidate fields is assumed. The optimizing field happens to be two-dimensional and normal. First-public motivating source: arXiv:2610.32504v1 (2026-10-23), primary MSC2020 47A12.

## Proof
**1. A distance-to-scalars identity.** For a bounded operator \(T\), put
\[
\beta(T)=\sup_{\|x\|=1}
\bigl(\|Tx\|^2-|\langle Tx,x\rangle|^2\bigr)^{1/2}.
\]
The identity used below is \(\beta(T)=\inf_{\lambda\in\mathbb C}\|T-\lambda I\|\). One inequality follows immediately from \(\|(I-P_x)Tx\|\le\|(T-\lambda I)x\|\), where \(P_x\) projects onto \(\mathbb Cx\).

For completeness, in finite dimension choose a minimizer \(\lambda_*\) and set \(A=T-\lambda_*I\), \(R=\|A\|\). Let \(E\) be the top-eigenspace of \(A^*A\). If \(0\notin\{\langle Ax,x\rangle:\|x\|=1,x\in E\}\), convexity of this numerical range supplies a complex direction \(h\) with \(\operatorname{Re}(\overline h\langle Ax,x\rangle)>0\) uniformly over unit \(x\in E\). The right derivative of \(\|A-thI\|^2\) at \(t=0\) equals \(-2\min_{x\in E,\|x\|=1}\operatorname{Re}(\overline h\langle Ax,x\rangle)<0\), contradicting minimality. Thus some unit \(x\in E\) satisfies \(\langle Ax,x\rangle=0\), and \(\|(I-P_x)Tx\|=\|Ax\|=R\).

For arbitrary \(\mathcal H\), the distance to scalars is the supremum of the corresponding distances for finite-dimensional compressions \(P_ET|_E\): for a finite net of scalar \(\lambda\)'s in a sufficiently large bounded disk, select almost-norming unit vectors for \(T-\lambda I\) and let \(E\) contain those vectors and their images under \(T\). The compression then approximates all \(\|T-\lambda I\|\) uniformly on the disk; outside the disk the scalar norm lower bound is already larger than the required infimum. As \(\beta(P_ET|_E)\le\beta(T)\), the finite-dimensional identity proves the general one.

**2. Universal thickness.** Write \(s=\sqrt{1-|q|^2}\). Fix a unit vector \(x\). Every vector \(y\) of the form \(y=\overline q x+s z\), where \(z\perp x\) and \(\|z\|=1\), is admissible. As the phase of \(z\) varies, the values \(\langle Tx,y\rangle\) include a complete circle with center \(q\langle Tx,x\rangle\) and radius \(s\bigl(\|Tx\|^2-|\langle Tx,x\rangle|^2\bigr)^{1/2}\). Consequently every directional width is at least \(2s\beta(T)\). On the other hand, every scalar \(\lambda\) yields \(W_q(T)\subset q\lambda+\{z:|z|\le\|T-\lambda I\|\}\), hence \(\operatorname{diam}W_q(T)\le2\beta(T)\). Combining establishes the width inequality in every dimension.

**3. Hausdorff lower bound.** Suppose \(d_H(\mathcal W_q(F),K)=\varepsilon\). Choose \(\omega_0\in\Omega\) with \(|f_1(\omega_0)-f_0(\omega_0)|=L\). Evaluation at \(\omega_0\) is a norm-one map and takes the joint range onto \(W_q(F(\omega_0))\). Therefore that planar set lies within \(\varepsilon\) of the segment joining \(f_0(\omega_0)\) to \(f_1(\omega_0)\), and conversely. Its diameter is at least \(L-2\varepsilon\), whereas its width perpendicular to the segment is at most \(2\varepsilon\). Step 2 gives \(2\varepsilon\ge s(L-2\varepsilon)\), i.e.
\[
\varepsilon\ge\frac{Ls}{2(1+s)}.
\]
The estimate is meaningful for arbitrary Hilbert dimension, including infinite dimensions.

**4. Attaining field.** Write \(q=|q|e^{i\vartheta}\), \(c=(f_0+f_1)/2\), \(g=(f_1-f_0)/2\), \(a=(1+s)^{-1}\), and \(A=\operatorname{diag}(-1,1)\) on \(\mathbb C^2\). Define
\[
F(\omega)=\frac{c(\omega)}q I_2+ae^{-i\vartheta}g(\omega)A.
\]
For \(r=|q|\), a direct unit-vector parametrization yields
\[
W_r(A)=E_s:=\{u+iv\in\mathbb C:u^2+v^2/s^2\le1\}.
\]
Indeed, every value has the form \(rt+s\sqrt{1-t^2}\,e^{i\phi}\) for \(-1\le t\le1\). Its support function in angular direction \(\gamma\) is \(\sqrt{r^2\cos^2\gamma+s^2}\), the support function of \(E_s\). To prove that the ellipse is **filled**, not merely that its convex hull is the ellipse, take any \(u+iv\in E_s\). The equation \((u-rt)^2+v^2=s^2(1-t^2)\) has roots \(t=ru\pm\sqrt{s^2(1-u^2)-v^2}\). They are real and satisfy \(|t|\le |ru|+s\sqrt{1-u^2}\le1\). Choosing the phase of the perpendicular vector therefore realizes \(u+iv\) itself. Rotation of \(q\) gives \(W_q(A)=e^{i\vartheta}E_s\). It follows that \(\mathcal W_q(F)=c+agE_s\), while \(K=c+g[-1,1]\). Multiplication by \(g\) scales all scalar distances by \(\|g\|_\infty=L/2\). Since \(a\le1\), the two one-sided Hausdorff distances between \(aE_s\) and \([-1,1]\) are respectively \(as\) and \(1-a\); both equal \(s/(1+s)\). Thus this continuous two-dimensional field attains the lower bound. Choosing \(T=A\) also makes the universal width-to-diameter inequality sharp, since \(E_s\) has diameter two and minimal directional width \(2s\).

## Verification
Run `python check.py` with Python's standard library only. The checker evaluates the balancing identity, sharp lower-bound equality, real and imaginary ellipse bounds, and exact rational parametrizations for eight Pythagorean parameter pairs and five segment lengths. Its output on execution was `SUBUNIT_Q_SEGMENT_CHECK_OK 12504 exact rational assertions`. These finite algebraic assertions do not establish the infinite-dimensional distance-to-scalars identity or the universal quantifiers; those follow from the preceding proof. The proof includes no numerical root searches or unproved spectral-limit steps.

## Relationship to prior work
Azadi, *Joint q-Numerical Ranges of Continuous Operator-Valued Functions*, arXiv:2610.32504v1 (2026-10-23), Theorem 2.16, realizes arbitrary compact convex sets for \(|q|=1\). The current result identifies the optimal positive approximation defect for every nondegenerate segment at fixed \(0<|q|<1\), even allowing nonnormal operators and arbitrarily large Hilbert spaces. Azadi's Proposition 2.4(4) concerns singleton ranges and is strictly weaker than the quantitative segment result.

Chien and Nakazato, *The q-numerical ranges of normal operators* (2005), and the earlier work of Li, Mehta, and Rodman provide general and normal-operator \(q\)-numerical-range background. The elliptical range of a selfadjoint two-level matrix and the distance-to-scalars identity are used as classical ingredients, not claimed independently novel. The new assessed statement is the exact universal Hausdorff infimum for function-valued line segments, together with the all-direction width-to-diameter bound underpinning its optimality.

## Limitations
The segment target is one-dimensional in the real affine sense; no comparable formula is asserted for arbitrary compact convex sets of higher affine dimension. The exact Hausdorff formula excludes \(q=0\), although the width bound includes it. For \(\dim\mathcal H=1\) the pair constraint is empty when \(|q|<1\), so that case is excluded. The result does not classify all minimizers. Older comprehensive numerical-range studies may contain equivalent width estimates under other names; the full texts of two potentially relevant older sources were unavailable during the literature review. The source-level priority comparison is therefore qualified, and no independent scientific audit has been performed.

## References
1. A. Azadi, *Joint q-Numerical Ranges of Continuous Operator-Valued Functions*, arXiv:2610.32504v1 (first posted 2026-10-23), especially Definition 2.1, Proposition 2.4, Theorem 2.16 and Corollaries 2.17–2.20. https://arxiv.org/abs/2610.32504
2. C.-K. Li, P. P. Mehta and L. Rodman, *A generalized numerical range: the range of a constrained sesquilinear form*, Linear and Multilinear Algebra 37 (1994), 25–49. https://doi.org/10.1080/03081089408818311
3. M.-T. Chien and H. Nakazato, *The q-numerical ranges of normal operators*, Linear and Multilinear Algebra 53 (2005), 393–416. https://doi.org/10.1080/03081080500156888
4. K. Feki, A. Patra, J. Rani and Z. Taki, *Joint q-Numerical Ranges of Operators in Hilbert and Semi-Hilbert Spaces*, arXiv:2410.03669 (first posted 2024-09-12), subsequently Linear and Multilinear Algebra 74 (2026), 294–316. https://arxiv.org/abs/2410.03669
5. P. Grover and S. Singla, *A distance formula for tuples of operators*, arXiv:2206.01503 (2022). The single-operator distance identity used above has been proved directly rather than inferred from the tuple results.
