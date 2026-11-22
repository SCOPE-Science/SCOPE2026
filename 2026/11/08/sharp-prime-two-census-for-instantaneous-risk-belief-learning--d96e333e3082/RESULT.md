# Transverse stability and a global Floquet obstruction for instantaneous risk-belief two-cycles

## Finding

Consider the instantaneous-belief, two-dimensional risk-sensitive multiplicative-weights map
\[
F(x,q)=\left(\frac{x}{x+(1-x)\exp(a(x-b+cq))},\;p_0+p_1x\right),
\]
where \(a,c>0\), \(0<b<1\), \(p_0,p_1\geq0\), and \(p_0+p_1\leq1\). Let
\[
r=cp_1,\qquad m=\frac{b-cp_0}{1+r},\qquad
 a_*=\frac{2}{m(1-m)(1-r)}.
\]
Assume \(0<m<1\), \(0\leq r<1\), and \(a>a_*\). The map has one primitive interior period-two orbit, as follows from a known scalar multiplicative-weights two-cycle theorem after an exact effective-parameter reduction described below. Its two population values are \(m\pm d\), where \(0<d<\min(m,1-m)\) is the unique solution of
\[
\frac{\operatorname{logit}(m+d)-\operatorname{logit}(m-d)}{d}=a(1-r).
\]
The associated beliefs are \(p_0+p_1(m\mp d)\).

**New two-dimensional Floquet conclusions.** Write
\[
s_+=(m+d)(1-m-d),\qquad s_-=(m-d)(1-m+d).
\]
The trace \(T\) and determinant \(D\) of the derivative of the second iterate at either point of this orbit satisfy
\[
T=1-a(1+r)(s_++s_-)+a^2s_+s_-,\qquad D=a^2r^2s_+s_-.
\]
For *every* such primitive two-cycle, at every permitted \(a>a_*\),
\[
\boxed{\;1-T+D>0.\;}
\]
In particular, the period-two Floquet matrix never has eigenvalue \(+1\) along this branch. Furthermore, as \(a\downarrow a_*\) from above, the two Floquet multipliers converge, with multiplicities, to
\[
1\quad\text{and}\quad\left(\frac{2r}{1-r}\right)^2.
\]
For \(0\leq r<1/3\), the period-two orbit is linearly attracting for **all sufficiently small** \(a-a_*>0\). For \(1/3<r<1\), it is **not** linearly attracting for all sufficiently small positive excess. The borderline \(r=1/3\) is expressly not classified.

This result is a stability classification of a *two-dimensional* periodic orbit, not a claim of novelty for existence, uniqueness or its scalar amplitude. The latter is inherited from established one-dimensional results after exact reduction. The asserted distinction is the transverse Floquet boundary and the strict global \(+1\)-exclusion inequality.

## Scope and conventions

The physical domain has \(0<x<1\) and \(0\leq q\leq1\), with instant belief replacement \(q'=p_0+p_1x\), the \(k=1\) endpoint of the adaptive-expectations model. An orbit of least period two must have two distinct population values; if they were equal, both belief values would be equal after one update and the state would be fixed. The stated results require the strict inequalities on \(m,r,a\). When \(m\notin(0,1)\), or \(r\geq1\), or the scalar effective learning intensity is at or below the scalar flip threshold, the same reduction shows that no interior primitive two-cycle exists; these elementary excluded regimes are not the novel part of the theorem. The boundary population states \(x=0,1\), if adjoined, are fixed in the first coordinate and cannot form a primitive period-two state.

## Proof

**1. Exact reduction to the established scalar two-cycle equation.** Put \(L(x)=\log(x/(1-x))\). Along the map,
\[
L(x')-L(x)=-a(x-b+cq).
\]
For a primitive period-two orbit \((x_0,q_0)\mapsto(x_1,q_1)\mapsto(x_0,q_0)\), the belief updates give \(q_0=p_0+p_1x_1\) and \(q_1=p_0+p_1x_0\). Adding log-odds increments yields
\[
x_0+x_1=2m.
\]
Writing \(x_0=m+d\), \(x_1=m-d\), the first logit equation becomes exactly
\[
L(m+d)-L(m-d)=a(1-r)d.
\]
Conversely this equation and those two belief values reconstruct both updates of the original two-dimensional map. Thus for period-two states, and only for this claim, the scalar population dynamics is equivalent to the ordinary one-dimensional replicator map of target \(m\) and effective gain \(a(1-r)\). Existence and uniqueness for the latter are known; see Kryzhevich, Zhang and Chmara (2024), Lemma 3.1, and earlier work cited there. Alternatively, the strict increase of
\[
H_m(d)=\int_{-1}^{1}L'(m+td)\,dt
\]
with \(d\), its limit \(2/[m(1-m)]\) at zero and its divergence at the endpoint give the same scalar statement. The derivative is strictly positive because
\[
H_m'(d)=\int_0^1 t\bigl[L''(m+td)-L''(m-td)\bigr]dt>0,
\]
as \(L'''(x)=2/x^3+2/(1-x)^3>0\). This step fixes our normalization; it is *not* counted as a new mathematical census. It also shows \(d\to0\) as \(a\downarrow a_*\), with \(d^2=3(1-r)(a-a_*)/L'''(m)+O((a-a_*)^2)\).

**2. Two-step derivative and exact Floquet data.** Write \(f(x,q)=F_1(x,q)\) and \(s(x)=x(1-x)\). The derivative at any point is
\[
DF(x,q)=\begin{pmatrix}
 s(f(x,q))\bigl(s(x)^{-1}-a\bigr)&-ac\,s(f(x,q))\\
 p_1&0
\end{pmatrix}.
\]
Evaluating this matrix at the two cycle points, multiplying the two matrices in temporal order and simplifying gives
\[
T=1-a(1+r)(s_++s_-)+a^2s_+s_-,\qquad
D=a^2r^2s_+s_-.
\]
The second determinant can also be read off immediately as the product of the two one-step determinants \(acp_1s_\pm=ar s_\pm\). No sign convention or continuum-time approximation is involved.

**3. A strict global exclusion of Floquet multiplier \(+1\).** Direct algebra factors the characteristic polynomial at \(1\):
\[
1-T+D=a(1+r)s_+s_-\left(\frac1{s_+}+\frac1{s_-}-a(1-r)\right).
\]
Since \(L'(x)=1/s(x)\) is *strictly convex* on \((0,1)\), the trapezoid inequality is strict for \(d>0\):
\[
\begin{split}
a(1-r)&=\frac1d\bigl[L(m+d)-L(m-d)\bigr]\\
&=\frac1d\int_{m-d}^{m+d}L'(x)\,dx
<L'(m+d)+L'(m-d)
=\frac1{s_+}+\frac1{s_-}.
\end{split}
\]
All remaining factors are positive. Therefore \(1-T+D>0\) for every allowed nontrivial two-cycle, hence \(+1\) is not a Floquet multiplier anywhere along its parameterized branch.

**4. Near-onset transverse stability and sharp feedback boundary.** At \(d=0\), the equilibrium Jacobian is
\[
J_* = \begin{pmatrix}1-a s&-ac s\\p_1&0\end{pmatrix},
\quad s=m(1-m),\quad
\chi_*(\lambda)=\lambda^2-(1-as)\lambda+ars.
\]
At \(a=a_*\) its two eigenvalues are \(-1\) and \(-2r/(1-r)\); therefore the limiting eigenvalues of the orbit's two-step matrix are \(1\) and \((2r/(1-r))^2\). For \(r<1/3\), this gives \(D<1\) and \(1+T+D>0\) for every sufficiently small \(d>0\). Together with the strict identity \(1-T+D>0\), the three planar Schur inequalities
\[
1-T+D>0,\qquad 1+T+D>0,\qquad 1-D>0
\]
show both Floquet multipliers have modulus strictly smaller than one. For \(r>1/3\), \(D>1\) for all sufficiently small positive \(d\), so linear attraction is impossible. At \(r=1/3\) both limiting equilibrium multipliers equal \(-1\), and this proof asserts no classification of the double-critical case. This completes the two-dimensional result.

## Exact arithmetic example and verification limits

At \(b=3/5\), \(c=2\), \(p_0=1/20\), \(p_1=1/10\), \(a=15\log 2\), we have \(m=5/12\), \(r=1/5\), \(a_*=72/7\), and the exact cycle
\[
(1/2,1/12)\longleftrightarrow(1/3,1/10).
\]
Here \(s_+=1/4\), \(s_-=2/9\), so \(T=1-17a/30+a^2/18\) and \(D=a^2/450\); the strict Schur inequalities can be verified by rational enclosures of \(\log2\). The existing `verification/check.py` script symbolically checks the two-step trace and determinant, the Schur-factor identity, and this exact witness, and adds parameter samples. These checks do not establish the universal result; Steps 1–4 supply its proof. No formal-machine or external expert certification is asserted.

## Relation to earlier mathematics and motivation

Kryzhevich, Zhang and Chmara (2024), Lemma 3.1 and its sources, establish the unique scalar primitive two-cycle for the one-dimensional replicator map above its exact flip threshold, for general interior target. Chotibut, Falniowski, Misiurewicz and Piliouras (2018) analyze the symmetric one-dimensional case. The population-coordinate census, critical gain and leading scalar amplitude in this note are *algebraically inherited* after substituting effective target \(m\) and effective gain \(a(1-r)\); none of these are claimed as independent novelty.

Metaxas and Sapsis (2026), equations (5) and (9), supply the present two-variable risk-belief model and its numerical period-doubling/Neimark–Sacker phenomenology, and already establish the stationary mean identity. Published same-model studies of inverse-fold multiplicity concern one-step inverse branches for \(k<1\), not two-step orbit Floquet multipliers. The distinction made here is the exact feedback value \(r=1/3\) separating locally attracting from nonattracting newly appearing cycles, together with the global exclusion of a \(+1\) Floquet multiplier, which are not consequences of the scalar cycle count. These give a practical structural benchmark when a second, lagged belief state changes the local stability of an otherwise familiar one-dimensional flip branch.

## Limitations and sources

Only the instantaneous-belief case \(k=1\) is analyzed. The attraction statement concerns sufficiently near-birth cycles, not their full lifetime or basins. No nonlinear stability assertion is made at \(r=1/3\); higher periods and global attractors are outside scope. Historical priority of the surviving two-dimensional Floquet conclusions is best-of-knowledge, not certified against all unpublished or unindexed literature.

1. S. Kryzhevich, Y. Zhang and M. Chmara, *Bifurcations and invariant sets for a family of replicator maps from evolutionary games*, arXiv:2412.16379 (2024), Lemma 3.1, https://arxiv.org/abs/2412.16379.
2. T. Chotibut, F. Falniowski, M. Misiurewicz and G. Piliouras, *Family of chaotic maps from game theory*, arXiv:1807.06831 (2018), Theorems 3.8–3.9, https://arxiv.org/abs/1807.06831.
3. K. Metaxas and T. P. Sapsis, *Risk-Sensitive Learning in Population Games under Extreme Events: Bifurcations and Chaotic Dynamics*, arXiv:2606.29967 (2026), model (5),(9), Proposition 1 and period-two bifurcations, https://arxiv.org/abs/2606.29967.
