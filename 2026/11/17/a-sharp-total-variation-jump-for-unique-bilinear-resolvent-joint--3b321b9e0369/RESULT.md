# A sharp total-variation jump for unique bilinear-resolvent joint measures

## Finding

Unique positive matrix-valued joint Hausdorff measures of noncommuting planar bilinear resolvents need not depend continuously in total variation on their defining matrices, even when they depend weakly continuously. In the natural rank-drop family below, the limit of the variation distance is **exactly** twice the mass of a newly emerging rank-one singular component. More precisely, write \(E_c\) for the unique normalized positive \(2\times2\) matrix-valued measure defined in the assumptions. As \(c\downarrow0\),

\[
\int f\,dE_c\longrightarrow\int f\,dE_0\quad\text{in matrix norm for every }f\in C([0,1]^2),
\]

while

\[
\boxed{\displaystyle\lim_{c\downarrow0}\|E_c-E_0\|_{\mathrm{var}}=2\left(\frac da+\frac eb\right)>0.}
\]

Indeed, the difference from this exact limit is \(O_{a,b,d,e}(\sqrt c)\). For every \(c>0\), \(E_c\) is absolutely continuous with respect to planar Lebesgue measure; at \(c=0\), its nonzero singular component is rank one, concentrated on the exponential curve \(\Gamma=\{(e^{-dt},e^{-et}):t\ge0\}\). All jump sizes in \((0,2)\) occur for valid parameters.

## Assumptions and scope

Fix real parameters \(a>d>0\), \(b>e>0\) satisfying

\[
\frac da+\frac eb<1\qquad\Longleftrightarrow\qquad de<(a-d)(b-e).
\]

Let \(0\le c<de\) and define

\[
s_c=\frac{de-c}{(a-d)(b-e)},\qquad
p_c=(\sqrt{s_c},\sqrt{1-s_c})^{\mathsf T},
\]

\[
A=\begin{pmatrix}d&0\\0&a\end{pmatrix},\qquad
B_c=bI-(b-e)p_cp_c^{\mathsf T},\qquad
C_c=bA+aB_c-abI.
\]

Thus \(0<s_c<1\), and \(A,B_c\) are strictly positive, noncommuting real symmetric matrices, with spectra \(\{d,a\}\) and \(\{e,b\}\). Their unique positive completion is \(C_c\), as follows either from the explicit construction below or from the planar completion criterion in Tian (2026). The joint Hausdorff measure \(E_c\) is the unique positive matrix-valued Borel measure on \([0,1]^2\) such that for every \(m,n\in\mathbb N_0\),

\[
\int_{[0,1]^2}u^mv^n\,dE_c(u,v)
=(I+mA+nB_c+mnC_c)^{-1}.
\]

Uniqueness follows from density of bivariate polynomials in continuous functions on the compact square, entry by entry. We use the **operator-norm variation** of a finite matrix-valued measure \(M\):

\[
\|M\|_{\mathrm{var}}=
\sup_{\mathcal P}\sum_{D\in\mathcal P}\|M(D)\|_{\mathrm{op}},
\]

where the supremum is over finite Borel partitions. For scalar signed measures we use full total-variation norm (maximum \(2\) for the difference of two probabilities), not the convention dividing this norm by two.

## Proof

**1. Positivity, rank drop, and the three-measure decomposition.** Because \(aI-A=(a-d)e_1e_1^{\mathsf T}\) and \(bI-B_c=(b-e)p_cp_c^{\mathsf T}\),

\[
\operatorname{tr}[(aI-A)(bI-B_c)]
=(a-d)(b-e)s_c=de-c.
\]

The \(2\times2\) determinant identity for a sum of rank-one matrices gives

\[
\det C_c=ab\,c,\qquad \operatorname{tr}C_c=bd+ae>0.
\]

Consequently \(C_c\succeq0\) for the entire stated range; it has rank one exactly at \(c=0\). Set

\[
K_{0,c}=\frac{(bd+ae)I-C_c}{ab},\qquad
K_1=\frac{A-dI}{a},\qquad
K_{2,c}=\frac{B_c-eI}{b}.
\]

All are positive semidefinite, their sum is \(I\), and the inverse identity, obtained by the adjugate formula (equation (4.8) of Tian), is

\[
(I+xA+yB_c+xyC_c)^{-1}
=\frac{K_{0,c}+K_1/(1+ax)+K_{2,c}/(1+by)}{1+dx+ey+cxy}.
\tag{1}
\]

The matrix coefficients are continuous in \(c\) near zero. From rank one of \(C_0\), \(K_{0,0}\) has eigenvalues \(0\) and

\[
r=\frac{bd+ae}{ab}=\frac da+\frac eb\in(0,1).
\tag{2}
\]

**2. The scalar measures and their regularity.** Let \(\mu_c\) be the unique probability measure on \([0,1]^2\) with moments \(1/(1+dm+en+cmn)\). For \(c=0\), take \(T\sim\mathrm{Exp}(\text{mean }1)\) and

\[
\mu_0=\mathcal L(e^{-dT},e^{-eT}),
\]

which is singular and supported on \(\Gamma\). For \(0<c<de\), put \(q=1-c/(de)\), take \(N\ge0\) with \(\Pr(N=k)=(1-q)q^k\), and conditional on \(N=k\) take independent gamma variables \(X_c,Y_c\) of shape \(k+1\) and scales \(c/e,c/d\), respectively. Then

\[
\mathbb E\exp(-xX_c-yY_c)
=\frac{1}{1+dx+ey+cxy},
\]

by summing the geometric series of conditional gamma Laplace transforms. Define \(\mu_c=\mathcal L(e^{-X_c},e^{-Y_c})\). Conditional on \(N\), it has a planar density, so \(\mu_c\ll\mathcal L^2\) for every \(c>0\). Uniqueness of moments identifies these scalar measures with those in (1).

Let independent \(Z_a,Z_b\) have exponential laws of means \(a,b\). Define

\[
\nu_{1,c}=\mathcal L(e^{-(X_c+Z_a)},e^{-Y_c}),\qquad
\nu_{2,c}=\mathcal L(e^{-X_c},e^{-(Y_c+Z_b)}).
\]

At \(c=0\), use \((X_0,Y_0)=(dT,eT)\). Their moments multiply those of \(\mu_c\) by \((1+am)^{-1}\) and \((1+bn)^{-1}\), respectively. Equation (1) therefore identifies the **entire unique** positive matrix-valued moment measure as

\[
E_c=K_{0,c}\mu_c+K_1\nu_{1,c}+K_{2,c}\nu_{2,c}.
\tag{3}
\]

At \(c>0\), all three scalar laws are planar absolutely continuous. At \(c=0\), the first is singular, but \(\nu_{1,0}\) and \(\nu_{2,0}\) are absolutely continuous: the maps \((T,Z_a)\mapsto(dT+Z_a,eT)\) and \((T,Z_b)\mapsto(dT,eT+Z_b)\) have nonzero Jacobian, and coordinatewise exponentiation preserves absolute continuity in the positive quadrant. Hence the Lebesgue-singular component of \(E_0\) is **exactly** \(K_{0,0}\mu_0\), with positive rank-one matrix mass of norm \(r\).

**3. Quantitative variation continuity of the smoothed parts.** The gamma representation yields exact exponential marginals \(X_c\sim\mathrm{Exp}(\text{mean }d)\) and \(Y_c\sim\mathrm{Exp}(\text{mean }e)\), and joint covariance \(de-c\), by differentiating the Laplace transform. Thus

\[
\mathbb E\bigl(X_c-(d/e)Y_c\bigr)^2=\frac{2dc}{e},\qquad
\mathbb E\bigl(Y_c-(e/d)X_c\bigr)^2=\frac{2ec}{d}.
\tag{4}
\]

Condition on \(Y_c=y\) and compare \(X_c+Z_a\) with \((d/e)y+Z_a\); the latter coupled pair has the exact \(\nu_{1,0}\) distribution because \(Y_c\) has the same exponential marginal as \(eT\). A shifted exponential density of mean \(a\) has full variation distance \(2(1-e^{-|h|/a})\le2|h|/a\) from its unshifted density. Coupling and Cauchy--Schwarz therefore give

\[
\|\nu_{1,c}-\nu_{1,0}\|_{\mathrm{TV}}
\le\frac{2}{a}\sqrt{\frac{2dc}{e}}.
\tag{5}
\]

The symmetric conditioning on \(X_c\) gives

\[
\|\nu_{2,c}-\nu_{2,0}\|_{\mathrm{TV}}
\le\frac{2}{b}\sqrt{\frac{2ec}{d}}.
\tag{6}
\]

The coordinatewise exponential map cannot increase total variation, so these estimates also hold for the measures on \([0,1]^2\).

**4. Exact variation jump.** The measures \(\mu_c\) and \(\mu_0\) are mutually singular for every \(c>0\). Both \(K_{0,c}\) and \(K_{0,0}\) are positive, so by partitioning the two disjoint supports,

\[
\|K_{0,c}\mu_c-K_{0,0}\mu_0\|_{\mathrm{var}}
=\|K_{0,c}\|_{\mathrm{op}}+\|K_{0,0}\|_{\mathrm{op}}.
\tag{7}
\]

Subtracting the two instances of (3), applying the reverse triangle inequality for measure variation, and then (5)--(7) shows

\[
\begin{aligned}
\left|\|E_c-E_0\|_{\mathrm{var}}-2r\right|
&\le\|K_{0,c}-K_{0,0}\|_{\mathrm{op}}
+\frac{2\|K_1\|_{\mathrm{op}}}{a}\sqrt{\frac{2dc}{e}}\\
&\quad+\frac{2\|K_{2,c}\|_{\mathrm{op}}}{b}\sqrt{\frac{2ec}{d}}
+\|K_{2,c}-K_{2,0}\|_{\mathrm{op}}.
\end{aligned}
\tag{8}
\]

Because \(s_c\) remains strictly inside \((0,1)\) as \(c\downarrow0\), the coefficients in (8) are Lipschitz in \(c\) near zero. Hence (8) proves the asserted \(O(\sqrt c)\) error and exact limit.

**5. Weak continuity and realizability.** For each fixed pair \(m,n\in\mathbb N_0\), the defining matrix inverse varies continuously with \(c\), so all mixed monomial moments of \(E_c\) converge to those of \(E_0\). Polynomial density and the uniform finite variation bounds for the positive normalized \(2\times2\) measures extend convergence to every continuous scalar test function. Finally, for any prescribed \(r\in(0,1)\) choose \(a=b=1\) and \(d=e=r/2\); then the assumptions hold and the jump equals \(2r\). This realizes all sizes in \((0,2)\).

## Verification

A standalone exact-rational \(2\times2\) script, `CHECK.py`, checks the determinant relation, coefficient normalization, and all 81 matrix moment identities with \(0\le m,n\le8\) in each of four rational parameter cases (including the rank-one boundary). Its success does not prove the infinite-dimensional or limiting statements; the derivations in the Proof do that. For reproduction, execute `python CHECK.py` with a standard Python 3 interpreter. Equations (4)--(8) provide a separate analytic certificate for the limiting claim. The defining matrices and measures have no dependence on any data external to this document and Tian's published inverse identity, which is also reconstructed from the adjugate in (1).

## Relationship to prior work

Tian, *Joint Moments of Bilinear Resolvents* (2026), Theorem 4.1 and equation (4.8), establishes uniqueness and positivity of the planar completion and explicitly decomposes its representing POVM into three scalar measures; the source also treats the scalar \(c=0\) diagonal law. These constructions are **prior results**, not newly claimed. The scalar bivariate exponential family is likewise classical (e.g. Downton 1970). The claim here is solely the exact **matrix-valued variation discontinuity and its coefficient**, its quantitative \(O(\sqrt c)\) control, and the weak/variation contrast across the positive-completion rank boundary. These statements do not follow merely from existence of scalar moment representations or identification of the completion matrix without analyzing absolute-continuity types and the two smoothed terms.

## Limitations

The theorem is restricted to the explicitly parameterized real-symmetric \(2\times2\) family and the one-sided limit \(c\downarrow0\); it does not assert a variation classification of all feasible noncommuting pairs or an optimal exponent for the \(O(\sqrt c)\) remainder. The numerical script is finite verification only. Possible equivalent formulations in older bivariate-exponential or operator-valued measure literature remain a bibliographic risk; no independent audit has been performed.

## References

- J. Tian, *Joint Moments of Bilinear Resolvents* (2026), arXiv:2611.03081v1, especially Lemma 2.1 and Theorem 4.1, https://arxiv.org/html/2611.03081v1 (first public 2026-11-02).
- F. Downton, *Bivariate Exponential Distributions in Reliability Theory*, Journal of the Royal Statistical Society Series B **32** (1970), 408–417, https://doi.org/10.1111/j.2517-6161.1970.tb00852.x (historical background, summary consulted).
