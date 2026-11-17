# A three-symbol past repeller and a three-term dimension law for an implicit cubic step

## Finding

Let \(H_h(t)=(1-h)t+ht^3\), \(I=[-1,1]\), and let the forward implicit Euler relation for the scalar double-well reaction equation \(\dot x=x-x^3\) be \(x_n=H_h(x_{n+1})\), for step \(h>0\). Define the bounded-*past* set
\[
K_h=\{x\in I:H_h^j(x)\in I\text{ for every integer }j\ge0\}.
\]
The backward-in-time state preceding \(x\) is uniquely determined as \(H_h(x)\), even though a forward step may have multiple admissible solutions.

**Theorem.** For all \(0<h\le4\), \(K_h=I\). For every \(h>4\), the interval \(I\) is no longer forward invariant under \(H_h\). For every \(h\ge64\), \(K_h\) is a strongly separated Cantor repeller, and \(H_h|_{K_h}\) is topologically conjugate to the one-sided full shift on three symbols. Hence its topological entropy is \(\log3\).

Writing \(s_h=\dim_{\mathrm H}K_h\) and \(L=\log h\),
\[
\boxed{\displaystyle s_h=\frac{\log3}{L}-\frac{2\log2\,\log3}{3L^2}+\frac{(\log2)^2\log3(4+\log3)}{9L^3}+O(L^{-4})}\qquad(h\to\infty).
\]
Moreover, let \(\widehat s_h\) be the unique positive root of \(h^{-s}(1+2^{1-s})=1\). Then
\[
|s_h-\widehat s_h|=O\left(\frac1{h(\log h)^2}\right).
\]
Thus the central inverse branch and the two outer branches contribute unequal effective contractions \(h^{-1}\) and \((2h)^{-1}\) to the dimension, despite sharing the same symbolic entropy.

## Assumptions and scope

All variables are real. The parameter ranges are exact: interval invariance for \(0<h\le4\), loss of invariance for \(h>4\), and the Cantor/dimension assertions for \(h\ge64\). The dimension expansion holds as \(h\to\infty\). "Past" means time indices \(n=0,-1,-2,\ldots\), with each bounded prior state forced by \(x_{-j}=H_h^j(x_0)\). This is not a claim about a particular forward root selection or numerical stability of a chosen solver.

## Proof

**1. Sharp interval-invariance threshold.** Denote the degree-three Chebyshev polynomial by \(T_3(t)=4t^3-3t\). Then the identity
\[
H_h(t)=(1-h/4)t+(h/4)T_3(t)
\]
shows \(H_h(I)\subseteq I\) for \(0<h\le4\), since both \(t\) and \(T_3(t)\) lie in \(I\) on this interval. Therefore \(K_h=I\). If \(h>4\), \(H_h\) has turning points \(\pm c_h\), \(c_h=\sqrt{(h-1)/(3h)}\), of absolute critical value \(m_h=(2/3)(h-1)\sqrt{(h-1)/(3h)}\). One has \(m_h>1\) if and only if \(4(h-1)^3>27h\); the difference factors as \((h-4)(2h+1)^2\). Hence some points in \(I\) escape in one step for every \(h>4\).

**2. Three exact inverse branches.** Fix \(h\ge64\) and write \(a_h=\sqrt{1-h^{-1}}\). The three simple zeros of \(H_h\) are \(-a_h,0,a_h\). The central monotonic branch maps \([-2/h,2/h]\) across \(I\), because \(H_h(2/h)=8/h^2-2+2/h<-1\) and oddness gives the opposite sign. The outer monotonic branches map intervals inside \([-1,1]\) across \(I\): the right one lies within \([a_h-2/h,1]\) (indeed \(H_h(a_h-2/h)<-1\) and \(H_h(1)=1\)), with the left one obtained by symmetry. To verify the displayed inequality, put \(r=2/h\); then
\[
H_h(a_h-r)=-(2h-2)r+3ha_hr^2-hr^3=-4+4/h+12a_h/h-8/h^2<-1
\]
for \(h\ge64\). Since the critical values have absolute value greater than \(1\), each target \(y\in I\) has exactly three inverse images in \(I\), one on each branch. Denote the three smooth inverse maps by \(b_-,b_0,b_+\). Their images are pairwise disjoint closed subintervals of \(I\).

**3. Uniform derivative control.** From the inverse-function formula \(|b_i'(y)|=|H_h'(b_i(y))|^{-1}\) and the central interval bound \(|b_0(y)|\le2/h\),
\[
1-1/h-12/h^2\le |H_h'(b_0(y))|/h\le1.
\]
For an outer branch, write \(b_+(y)=a_h+\varepsilon\) with \(|\varepsilon|\le2/h\) (and use odd symmetry for the other branch). Direct expansion yields
\[
\frac{H_h'(a_h+\varepsilon)}{2h}=1-\frac1h+3a_h\varepsilon+\frac32\varepsilon^2,
\qquad
\left|\frac{H_h'(a_h+\varepsilon)}{2h}-1\right|\le\frac7h+\frac6{h^2}.
\]
All these derivatives have absolute value greater than one for \(h\ge64\). Elementary bounds for \(\log(1+u)\) imply, uniformly in \(y\in I\),
\[
e^{-16/h}h^{-1}\le |b_0'(y)|\le e^{16/h}h^{-1},\qquad
\frac{e^{-16/h}}{2h}\le |b_\pm'(y)|\le\frac{e^{16/h}}{2h}.
\]
These imply strict contraction and a common separation gap. The standard nested-cylinder construction therefore gives a homeomorphism from the full three-symbol sequence space onto \(K_h=\bigcap_{n\ge0}H_h^{-n}(I)\), intertwining the shift and \(H_h\). The set is compact, perfect, and nowhere dense, and the entropy is \(\log3\).

**4. Hausdorff dimension comparison.** The disjoint \(C^1\) inverse iterated-function system satisfies the usual cylinder-cover and mass-distribution bounds. Put \(\epsilon_h=16/h\) and let \(s_-\) and \(s_+\) denote the positive solutions of
\[
e^{-\epsilon_hs_-}h^{-s_-}(1+2^{1-s_-})=1,\qquad
e^{\epsilon_hs_+}h^{-s_+}(1+2^{1-s_+})=1.
\]
Uniform lower and upper bounds on all branch derivatives, together with disjoint branch images, give
\[
s_-\le\dim_{\mathrm H}K_h\le s_+.
\]
Let \(F_h(s)=-s\log h+\log(1+2^{1-s})\). Since \(F_h'(s)\le-\log h\) and \(\widehat s_h\le(\log3)/(\log h)\), the mean-value theorem gives \(|s_\pm-\widehat s_h|\le C/(h(\log h)^2)\), with a numerical constant \(C\) independent of \(h\ge64\). This proves the stated sharper implicit-root approximation.

**5. The three coefficients.** With \(a=\log3\), \(c=\log2\), and \(L=\log h\), the defining equation becomes
\[
L\widehat s_h=\log(1+2e^{-c\widehat s_h})
=a-\frac{2c}{3}\widehat s_h+\frac{c^2}{9}\widehat s_h^2+O(\widehat s_h^3).
\]
Solving successively in powers of \(L^{-1}\) yields
\[
\widehat s_h=\frac aL-\frac{2ca}{3L^2}+\frac{c^2a(a+4)}{9L^3}+O(L^{-4}).
\]
The difference between \(s_h\) and \(\widehat s_h\) decays faster than any fixed power of \((\log h)^{-1}\), so the same three-term expansion holds for \(s_h\).

## Verification

Run `python3 verify_implicit_cubic.py` with Python 3.10 or later; no third-party dependencies are needed. The checker re-evaluates the critical-value polynomial factorization, root neighborhoods and derivative inequalities on sampled parameter values, the implicit comparison root, and a numerical residual of the three-term asymptotic law. These finite checks are corroboration, not the proof of the all-parameter theorem. All critical analytic inequalities are displayed explicitly above.

## Relationship to prior work

Oliveira's 2026 treatment of implicit discrete dynamics develops local periodic-orbit Lyapunov–Schmidt bifurcation reduction and notes multivalued numerical steps; it does not give the global bounded-past set or its Hausdorff dimension. Green, Patrick and Spiteri (2019) examine valid timestep bounds and possible solver selection among multiple implicit solutions; their ten-page study does not contain a Cantor-past dimension law. The symbolic coding and dimension comparisons use standard principles for strongly separated iterated-function systems; their general form is not claimed as new. The new content is the sharp interval-invariance boundary and, chiefly, the explicit unequal-branch three-term dimension asymptotics for this implicit polynomial relation.

## Limitations

The full Cantor conjugacy is established here for \(h\ge64\); the intermediate parameter interval \(4<h<64\) is not classified. The constant implicit in each error term is not optimized. The result describes the set of initial states admitting a complete bounded past, rather than the distribution of outcomes of any particular nonlinear root-selection algorithm. The dimension proof uses classical finite-branch IFS bounds and does not furnish a closed formula for the exact dimension at finite \(h\).

## References

1. H. M. Oliveira, *Lyapunov–Schmidt reduction for periodic orbits of implicit discrete dynamical systems*, arXiv:2611.03336v1 (first public posting 2 November 2026), https://arxiv.org/html/2611.03336v1.
2. K. R. Green, G. W. Patrick and R. J. Spiteri, *On theoretical upper limits for valid timesteps of implicit ODE methods*, arXiv:1912.08900v1 (18 December 2019), https://arxiv.org/pdf/1912.08900.
3. Standard contraction-IFS dimension bounds and symbolic coding are used as background; no claim of priority for those general theorems is made.
