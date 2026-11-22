# A universal sharp skewness boundary for separable saturated forward iterations

## Finding

**Theorem (three nested stability properties).** Let \(f:\mathbb R\to\mathbb R\) be an odd, continuously differentiable, nondecreasing, globally \(1\)-Lipschitz function satisfying
\[
f(0)=0,\quad f'(0)=1,\quad f(t)>0\ (t>0),\quad
\lim_{t\to+\infty}f(t)=L\in(0,\infty),\quad
\lim_{t\to+\infty}f'(t)=0.
\]
Put
\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
F_s=I+sJ,\quad g(y_1,y_2)=(f(y_1),f(y_2)),\quad
T_{s,\gamma}(x)=x-\gamma g(F_sx),
\]
where \(s\in\mathbb R\) and \(\gamma>0\). Then all of the following statements hold.

1. For every \(s\), **every** orbit \(x_{k+1}=T_{s,\gamma}(x_k)\) tends to the unique zero \(0\) whenever \(0<\gamma<2/(1+s^2)\).
2. The **universal one-step Fejér inequality** \(\|T_{s,\gamma}(x)\|_2\le\|x\|_2\) for **every** \(x\in\mathbb R^2\) holds **if and only if**
   \[
   |s|\le1\quad\text{and}\quad0<\gamma\le\frac{2}{1+s^2}.
   \]
   If \(|s|>1\), then **every** positive stepsize has some state whose Euclidean distance from the zero strictly increases, even when the stepsize lies inside the global-convergence range.
3. The stronger **pairwise nonexpansiveness** \(\|T_{s,\gamma}(x)-T_{s,\gamma}(z)\|_2\le\|x-z\|_2\) for **every** pair \(x,z\) holds **if and only if** \(s=0\) and \(0<\gamma\le2\).

Thus the maximal universal Fejér skewness is exactly \(|s|=1\), a \(45^\circ\) angle for \(F_s\); global convergence, Fejér monotonicity and pairwise nonexpansiveness are genuinely distinct properties within this family.

## Assumptions and scope

All norms are Euclidean. The nonlinearity is the *same scalar response in both coordinates*, not an arbitrary anisotropic map. The hypotheses include the gradient of the separable dual reference function in Example 2.6 of Quan--Oikonomidis--Bodard--Patrinos (2026):
\[
f(t)=\frac{t}{1+|t|},\qquad
\phi^*(y)=\sum_{i=1}^2\bigl(|y_i|-\log(1+|y_i|)\bigr),\quad g=\nabla\phi^*.
\]
The prescribed matrix is the normal, strongly monotone rotation-dilation \(F_s=I+sJ\); no claim is made about general nonnormal, nonlinear or higher-dimensional operators. The root set is \(\{0\}\), since \(F_s\) is invertible and \(f(t)>0\) for positive \(t\). At the largest Fejér stepsize, only one-step Fejér monotonicity is asserted, not convergence for arbitrary admissible \(f\).

## Proof

**1. A two-dimensional angular inequality.** Fix \(y\in\mathbb R^2\), write \(v=g(y)\) and \(r=y-v\). Oddness and monotonicity of \(f\), together with the fact that \(0\le f(a)\le a\) and \(a\mapsto a-f(a)\) is nondecreasing for \(a\ge0\), imply that \(r\) and \(v\) have coordinatewise matching signs. After sign changes and (if necessary) swapping coordinates, both belong to the cone
\[
\mathcal K=\{(a,b):a\ge b\ge0\}.
\]
The aperture of this cone is \(\pi/4\). Any two vectors \(r,v\in\mathcal K\) therefore obey
\[
\langle r,v\rangle\ge|\det(r,v)|
=|\langle Jr,v\rangle|.
\]
The same inequality is preserved by simultaneous coordinate sign changes and permutations, hence is valid for the original \(r,v\). Because \(Jv\perp v\), this implies for \(|s|\le1\)
\[
\langle y-sJy,v\rangle
=\|v\|_2^2+\langle r,v\rangle-s\langle Jr,v\rangle
\ge\|v\|_2^2.
\]
Since \(F_s^{-1}=(I-sJ)/(1+s^2)\), setting \(y=F_sx\) yields the key estimate
\[
\boxed{\langle x,g(F_sx)\rangle\ge\frac{\|g(F_sx)\|_2^2}{1+s^2}\qquad(|s|\le1).}
\]

**2. Sharp Fejér classification.** Expanding the squared norm gives
\[
\|T_{s,\gamma}(x)\|_2^2-\|x\|_2^2
=-2\gamma\langle x,g(F_sx)\rangle
+\gamma^2\|g(F_sx)\|_2^2.
\]
The key estimate makes this nonpositive for \(|s|\le1\) and \(0<\gamma\le2/(1+s^2)\), including the endpoint. For any \(s\), differentiability at zero gives \(g(F_sx)=F_sx+o(\|x\|_2)\). Hence
\[
\|T_{s,\gamma}(x)\|_2^2-\|x\|_2^2
=\gamma\bigl(\gamma(1+s^2)-2\bigr)\|x\|_2^2+o(\|x\|_2^2),
\]
which is strictly positive for sufficiently small nonzero \(x\) whenever \(\gamma>2/(1+s^2)\).

For \(s>1\), choose \(b>0\) such that \(sf(b)>L\), possible by the positive saturation limit, and let \(y=(a,b)\) with \(a\to\infty\). Writing \(x=F_s^{-1}y\), we obtain
\[
(1+s^2)\langle x,g(y)\rangle
=a\bigl(f(a)-sf(b)\bigr)
+b\bigl(sf(a)+f(b)\bigr)\longrightarrow-\infty.
\]
Thus the same squared-norm identity gives strict expansion for *every* \(\gamma>0\). Reflection of the second coordinate transfers the construction to \(s<-1\). This proves necessity and sufficiency.

**3. Pairwise nonexpansiveness.** If \(s=0\), each coordinate map is \(t\mapsto t-\gamma f(t)\). Its secant slopes are \(1-\gamma\theta\), with \(0\le\theta\le1\); they have absolute value at most one precisely throughout \(0<\gamma\le2\). For \(s\ne0\), choose \(x=F_s^{-1}(0,b)\). The derivative exists and
\[
DT_{s,\gamma}(x)e_2=
\begin{pmatrix}\gamma s\\1-\gamma f'(b)\end{pmatrix}
\longrightarrow
\begin{pmatrix}\gamma s\\1\end{pmatrix},
\qquad b\to+\infty.
\]
Its norm is eventually greater than one for every \(\gamma>0\). A globally nonexpansive differentiable map cannot have such a derivative, so pairwise nonexpansiveness is impossible when \(s\ne0\).

**4. Global convergence despite loss of Fejér monotonicity.** Define the convex dual potential
\[
\Phi(y)=\sum_{i=1}^2\int_0^{y_i}f(t)\,dt,
\quad \nabla\Phi(y)=g(y).
\]
Its gradient is globally \(1\)-Lipschitz. If \(y_k=F_sx_k\), then \(y_{k+1}=y_k-\gamma F_sg(y_k)\). The smooth-convex descent lemma and the exact identities
\[
\langle g,F_sg\rangle=\|g\|_2^2,\qquad
\|F_sg\|_2^2=(1+s^2)\|g\|_2^2
\]
give
\[
\Phi(y_{k+1})\le\Phi(y_k)-\gamma\left(1-\frac{\gamma(1+s^2)}2\right)\|g(y_k)\|_2^2.
\]
For \(0<\gamma<2/(1+s^2)\), the coefficient is positive. As \(\Phi\ge0\), summing implies \(g(y_k)\to0\). The assumed strict positivity of \(f\) on positive inputs implies \(y_k\to0\), and invertibility of \(F_s\) gives \(x_k\to0\). All conclusions follow.

## Verification

`CHECK.py` is standalone Python 3 code using only the standard library. From the directory containing this file, execute `python3 CHECK.py`. It verifies the exact inverse and angular inequalities and finite-grid Fejér tests using rational arithmetic; it checks supercritical and large-skew witnesses and the Jacobian obstruction, including a rational witness for the motivating \(s=2\) example. The script returns a reproducible `VERIFY_OK` count. Finite checks are cross-checks only: the quantified assertions above are established in the analytic proof.

For the motivating response \(f(t)=t/(1+|t|)\), a concrete counterexample uses \(s=2\), \(\gamma=1/5\), \(y=(30,2)\) and \(x=F_s^{-1}y\), for which the exact squared-distance increase is \(22328/43245>0\). In the same case, the dual potential decreases at every nonzero step for \(0<\gamma<2/5\), so this increase does not prevent convergence.

## Relationship to prior work

Quan, Oikonomidis, Bodard and Patrinos (2026, Section 2, Theorem 2.4, Theorem 2.7 and Example 2.6) establish convergence under a nonlinear cocoercivity condition, guarantee Fejér monotonicity for *isotropic* preconditioners, and exhibit a *non-isotropic* planar case where Fejér monotonicity can fail. The current result proves a sharp parameter boundary for a specified separable family (and a class of scalar saturations), together with an exact larger convergence range and the distinction from pairwise nonexpansiveness. It does not claim that nonlinear cocoercivity, potential descent or the qualitative non-Fejér example are themselves new.

Akram, Ishtiaq, Ahmad and Popa (2026) study general enriched nonexpansiveness and Jacobian-based operator certificates for plug-and-play methods. Such results concern pairwise operator behavior and do not state this sharp fixed-point Fejér boundary for coordinatewise saturation and planar skew coupling. General fixed-point literature already distinguishes Fejér monotonicity from nonexpansive maps; the contribution here is the exact simultaneous classification for the specified iterative family.

## Limitations

The boundary uses two identical scalar coordinate responses, an exactly normal \(2\times2\) operator, exact arithmetic and a fixed positive stepsize. No statement is made for arbitrary diagonal response functions, higher dimensions, noisy gradients, line searches, general variational inequalities or practical performance. Global convergence at the endpoint \(\gamma=2/(1+s^2)\) is not asserted. The new result does not replace independent peer review or settle exhaustive historical priority.

## References

1. J. Quan, K. Oikonomidis, A. Bodard and P. Patrinos, *Dual-Space Preconditioning for Variational Inequalities and Root-Finding Problems*, arXiv:2611.13916v1, publicly submitted 10 November 2026. https://arxiv.org/abs/2611.13916
2. M. Akram, U. Ishtiaq, K. Ahmad and I.-L. Popa, *Enriched-nonexpansive Plug-and-Play image restoration*, Frontiers in Applied Mathematics and Statistics 12 (9 October 2026), DOI: 10.3389/fams.2026.1945678. https://doi.org/10.3389/fams.2026.1945678
