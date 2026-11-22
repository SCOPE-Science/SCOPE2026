# Exact von Neumann–Jordan profile of a square-to-hexagon deformation

## Finding
For every \(t>0\), equip the real plane with
\[
\|(u,v)\|_t=\max\{|u|,|v|,t|u-v|\},\qquad X_t=(\mathbb R^2,\|\cdot\|_t).
\]
Define the *unrestricted* von Neumann–Jordan constant by
\[
C_{\mathrm{NJ}}(X_t)=\sup_{(x,y)\ne(0,0)}
\frac{\|x+y\|_t^2+\|x-y\|_t^2}
{2(\|x\|_t^2+\|y\|_t^2)}.
\]
The exact profile for **every positive parameter** is
\[
\boxed{
C_{\mathrm{NJ}}(X_t)=
\begin{cases}
2,&0<t\le\tfrac12,\\[3pt]
\displaystyle\frac{3+r^2+\sqrt{r^4+2r^2+8r+5}}{4},
&t>\tfrac12,\quad r=|1-t^{-1}|.
\end{cases}}
\]
It decreases strictly on \((1/2,1)\), increases strictly on \((1,\infty)\), and has its unique minimum at \(t=1\), the affine-regular hexagon:
\[
\min_{t>0}C_{\mathrm{NJ}}(X_t)=\frac{3+\sqrt5}{4}.
\]
The transitions and endpoint expansions are
\[
\begin{aligned}
2-C_{\mathrm{NJ}}(X_t)&=4(t-\tfrac12)+O((t-\tfrac12)^2)&&\text{as }t\downarrow\tfrac12\text{ from above},\\
C_{\mathrm{NJ}}(X_t)&=\frac{3+\sqrt5}{4}+\frac{|t-1|}{\sqrt5}+O((t-1)^2)&&\text{as }t\to1,\\
2-C_{\mathrm{NJ}}(X_t)&=t^{-1}+O(t^{-2})&&\text{as }t\to\infty.
\end{aligned}
\]
Thus the non-squareness threshold is *exactly* \(t=1/2\); for \(t>1/2\) every \(X_t\) is uniformly non-square, while the square regime is not. The fixed \(t=1\) endpoint value was known; the result here is the **entire parameter profile**, exact threshold, and unique optimal deformation.

## Assumptions and scope
The scalar field is **real** and the dimension exactly two. All parameters are finite and strictly positive. The norm is the three-facet intersection norm above, not a weighted \(\ell_p\) or complex norm. The supremum ranges over all pairs not both zero and does **not** restrict the vectors to have equal norm or be isosceles-orthogonal. All claimed error terms are one-sided as specified and the constants implicit in \(O(\cdot)\) are local.

## Proof
**Step 1: the square regime.** If \(0<t\le1/2\), then \(t|u-v|\le\max(|u|,|v|)\), so \(X_t\) is exactly real \(\ell_\infty^2\). The pair \(x=(1,1)\), \(y=(1,-1)\) attains the universal von Neumann–Jordan upper bound \(2\).

**Step 2: dual finite-facet reduction.** Fix \(t>1/2\), put \(a=t^{-1}-1\in(-1,1)\) and \(r=|a|\). The unit ball is precisely the convex hexagon with vertices
\[
V=\{\pm(1,1),\ \pm(1,-a),\ \pm(-a,1)\}.
\]
Let \(f_1(u,v)=u\), \(f_2(u,v)=v\), \(f_3(u,v)=t(u-v)\). Then \(\|z\|_t=\max_{1\le i\le3}|f_i(z)|\). For \(i,j\in\{1,2,3\}\), define
\[
L_{ij}:X_t\oplus_2X_t\longrightarrow\mathbb R^2,
\quad L_{ij}(x,y)=(f_i(x+y),f_j(x-y)).
\]
As a maximum of finitely many nonnegative summands,
\[
2C_{\mathrm{NJ}}(X_t)=\max_{i,j}\|L_{ij}\|^2.
\]
Taking the operator adjoint and using the Hilbertian direct-sum duality gives
\[
\|L_{ij}\|^2=\max_{p^2+q^2=1}
\bigl(\|pf_i+qf_j\|_{X_t^*}^{2}+
\|pf_i-qf_j\|_{X_t^*}^{2}\bigr).
\]
The displayed sum is unchanged by changing the sign of either \(p\) or \(q\), so we may take \(p,q\ge0\). The dual norm of a linear functional is exactly the largest absolute value of that functional at one of the six listed vertices.

**Step 3: an exhaustive sharp two-function envelope.** Define
\[
U_r(p,q)=(p+q)^2+\max\{p+rq,rp+q\}^2.
\]
For equal facet indices \(i=j\), the dual sum is \(2(p^2+q^2)\le U_r(p,q)\). For distinct indices, direct substitution of the three non-opposite vertices gives the following exhaustive alternatives (the reversed ordered pairs interchange \(p,q\)):

When \(a\ge0\), the \((1,2)\) dual-norm pair is
\[
(p+q,\ \max\{p+aq,ap+q\}),
\]
while the \((1,3)\) and \((2,3)\) pairs, in one order or the other, are
\[
(p+q,\ \max\{p,q-ap\}).
\]
Every displayed sum of squares is at most \(U_r(p,q)\), and **the pair \((1,2)\) attains \(U_r\) for every \(p,q\ge0\)**.

When \(a<0\), write \(r=-a\). For \((1,2)\) the first dual norm is \(p+q\) and the second is at most \(\max\{p,q\}\). For \((1,3)\), the two norms are
\[
(p+q,\ \max\{p,rp+q\}),
\]
while for \((2,3)\) their roles are reversed. These also yield upper bound \(U_r(p,q)\). **For \(q\ge p\)** the \((1,3)\) pair attains \(U_r\), since \(rp+q\ge p\) and \(rp+q\ge p+rq\). Thus in *both* parameter regimes
\[
2C_{\mathrm{NJ}}(X_t)=\max_{p,q\ge0,\ p^2+q^2=1}U_r(p,q).
\]

**Step 4: solve the continuous optimization.** By symmetry we may put \(p\ge q\). Because \(0\le r<1\), the larger linear term in \(U_r\) is then \(p+rq\). Therefore
\[
U_r(p,q)=(p+q)^2+(p+rq)^2
=\begin{pmatrix}p&q\end{pmatrix}
\begin{pmatrix}2&1+r\\1+r&1+r^2\end{pmatrix}
\begin{pmatrix}p\\q\end{pmatrix}.
\]
The symmetric matrix has a strictly positive off-diagonal entry and first diagonal at least the second; hence its top eigenvector can be chosen with \(p\ge q\ge0\). The cone restriction does not change its largest Rayleigh quotient. Its largest eigenvalue is
\[
\lambda_r=\frac{3+r^2+\sqrt{r^4+2r^2+8r+5}}2.
\]
Consequently \(C_{\mathrm{NJ}}(X_t)=\lambda_r/2\), as claimed.

**Step 5: explicit witnesses.** Put \(k=(\lambda_r-2)/(1+r)\in(0,1]\). If \(1/2<t\le1\), take \(p=(1+k^2)^{-1/2}\), \(q=kp\) and
\[
x=(p+q)(1,1),\qquad y=(p+rq)(1,-r).
\]
If \(t\ge1\), take \(q=(1+k^2)^{-1/2}\), \(p=kq\) and
\[
x=(p+q)(1,r),\qquad y=(rp+q)(r,1).
\]
In the first case the corresponding \((f_1,f_2)\) operator, and in the second the \((f_1,f_3)\) operator, sends the displayed pair to \(\lambda_r(p,q)\). Each input component is a nonnegative multiple of a unit-ball vertex and its sum-of-squared norms is \(\lambda_r\). The original von Neumann–Jordan quotient is therefore at least \(\lambda_r/2\), and the established upper bound makes it exactly equal. This proves actual attainment for every parameter.

**Step 6: sharp qualitative transitions.** The function
\[
F(r)=\frac{3+r^2+\sqrt{r^4+2r^2+8r+5}}4
\]
has strictly positive derivative on \([0,1]\); explicitly \(F'(0)=1/\sqrt5\) and \(F'(1)=1\). Since \(r=|1-t^{-1}|\) decreases strictly on \((1/2,1)\) and increases strictly on \((1,\infty)\), the unique minimum occurs at \(t=1\), with value \(F(0)\). The expansions follow by differentiating \(F\) and \(t^{-1}\). Uniform non-squareness is equivalent to \(C_{\mathrm{NJ}}<2\), and \(F(r)<2\) for \(0\le r<1\), finishing the threshold claim.

## Verification
A standalone standard-library Python program, `CHECK.py`, exhaustively enumerates the 324 ordered facet/vertex-pair singular-value candidates at 170 sample parameters, and checks the resulting exact-formula values and explicit witnesses. It additionally tests random original-vector pairs. The program printed `HEXAGON_DEFORMATION_NJ_DIAGNOSTIC_OK 5777`. This finite diagnostic corroborates the algebra only; the proof above covers the full uncountable range of \(t\) and all real input pairs.

## Relationship to prior work
Li, Zhang, Qi and Liu (2026), Section 4 and Remark 9, introduce an isosceles-orthogonality-restricted constant and give a *lower bound* \((3+\sqrt5)/4\) for the unrestricted constant of the affine-regular hexagonal endpoint. Yang and Wang (2006) had already computed that endpoint exactly. A published generalized exponent profile likewise contains the fixed endpoint. Neither endpoint result, nor the restricted isosceles computation \(5/4\), implies the exact profile as the third facet is varied through the full parameter range, especially the square saturation threshold, strict optimality of the regular hexagon, and asymptotic return to \(2\).

Ciesielski and Płuciennik (2020) give general theory and non-squareness criteria for von Neumann–Jordan constants, but not a formula for this planar three-facet deformation. Yang and Wang (2016) study a different \(\ell_p-\ell_1\) Day–James family; the available abstract gives no formula for varying the present facet parameter, while its full text was not obtained. The construction is a norm-specific finite-facet calculation; no claim of novelty for the adjoint identity, matrix eigenvalues, or existing fixed endpoint is made.

The potentially broader Komuro–Saito–Mitani (2010) classification of extreme absolute norms includes these norms after the linear reparametrization \(s=(u+v)/2\), \(d=2t(u-v)/2\). Its explicit constant formula, however, assumes \(\psi\le\psi_2\); here \(\psi(z)=\max\{1-(1-a)z,z\}\), \(a=1/(2t)>0\), violates that hypothesis near \(z=0\); it also lies strictly below the Euclidean norm near \(z=1\), so neither of the global-comparison hypotheses in Proposition 3.1 applies. The remaining 2000 complex absolute-norm study is a residual priority comparison because its complete theorem was not obtained.

## Limitations
The classification is for real two-dimensional norms with exactly the specified third-facet deformation, not for arbitrary hexagons, complex normed planes, modified/isosceles von Neumann–Jordan constants, or generalized exponent parameters. Prior work in unindexed sources or inaccessible full texts could affect priority. The proof does not claim new fixed-point theorems: it supplies the sharp geometric invariant and uniform-nonsquareness threshold.

## References
1. Y. Li, W. Zhang, J. Qi, Q. Liu, “Isosceles-Orthogonal Takahashi–von Neumann–Jordan-Type Constants in Banach Spaces,” *Axioms* **15** (2026), 684. Published 15 September 2026. DOI: https://doi.org/10.3390/axioms15090684.
2. C. Yang, F. Wang, “On a new geometric constant related to the von Neumann–Jordan constant,” *J. Math. Anal. Appl.* **324** (2006), 555–565. DOI: https://doi.org/10.1016/j.jmaa.2005.12.009.
3. C. Yang, F. Wang, “The von Neumann–Jordan Constant for a Class of Day–James Spaces,” *Mediterr. J. Math.* **13** (2016), 1127–1133. DOI: https://doi.org/10.1007/s00009-015-0539-x.
4. M. Ciesielski, R. Płuciennik, “On some modifications of n-th von Neumann–Jordan constant for Banach spaces,” *Banach J. Math. Anal.* **14** (2020), 650–673. https://doi.org/10.1007/s43037-019-00033-1.
5. “Exact generalized von Neumann–Jordan profile of the Day–James hexagon,” published mathematical record, 11 October 2026. https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-exact-generalized-von-neumann-jordan-profile-of-the-day-james-he--f84aa4a74a83/RESULT.md.

7. N. Komuro, K.-S. Saito and K.-I. Mitani, “Extremal structure of the set of absolute norms on R2 and the von Neumann–Jordan constant,” *J. Math. Anal. Appl.* **370** (2010), 101–106, DOI 10.1016/j.jmaa.2010.04.016.
8. K.-S. Saito, M. Kato and Y. Takahashi, “Von Neumann–Jordan constant of absolute normalized norms on C2,” *J. Math. Anal. Appl.* **244** (2000), 515–532, DOI 10.1006/jmaa.2000.6727 (abstract inspected; complete theorem unavailable).
