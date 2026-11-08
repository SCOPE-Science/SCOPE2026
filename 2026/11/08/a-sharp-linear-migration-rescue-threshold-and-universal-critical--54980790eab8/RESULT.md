# A sharp linear-migration rescue threshold and universal critical decay in an Allee--logistic two-patch population

## Finding

For the linearly dispersing Allee--logistic two-patch population model of Xia, Chen, Srivastava and Parshad (equation (2.11) of [1]), the high-Allee regime \(m\geq 1/h\) has a complete and sharp migration classification. In particular, when the mortality rate of the first patch exceeds the logistic growth rate of the second, \(e>s\), the unique extinction/persistence threshold is
\[
\delta_c=\frac{es}{e-s}.
\]
For \(0<\delta<\delta_c\) there is exactly one strictly positive equilibrium, attracting every nonzero nonnegative solution; for \(\delta>\delta_c\), all nonnegative solutions converge exponentially to extinction. At \(\delta=\delta_c\), all nonzero nonnegative solutions still become extinct, but at an exact universal reciprocal-time rate:
\[
\lim_{t\to\infty}t\binom{u(t)}{v(t)}
 =\frac1{k}\binom{a}{1},\quad
 a=\frac{s}{e},\quad
 k=\frac{s+a^3(h-1/m)}{1+a^2}>0.
\]
As \(\delta\uparrow\delta_c\) from below, the unique positive equilibrium satisfies
\[
\binom{u_*(\delta)}{v_*(\delta)}
=\frac{(\delta_c-\delta)(1-a)^2}{s+a^3(h-1/m)}\binom{a}{1}
+O((\delta_c-\delta)^2).
\]
When \(e\leq s\), one positive equilibrium exists and attracts all nonzero nonnegative solutions for every finite \(\delta>0\). All limits refer to physical time of the displayed ODE.

## Assumptions and scope

Let \(m,h,e,s,\delta>0\) and \(m\geq1/h\). Consider the deterministic two-patch equations
\[
\begin{aligned}
\dot u&=u\left(\frac{u}{m+u}-e-hu\right)+\delta(v-u),\\
\dot v&=sv(1-v)+\delta(u-v),
\end{aligned}
\]
with any \((u(0),v(0))\in[0,\infty)^2\). The nonzero-initial-data assertions require \(u(0)+v(0)>0\); the zero trajectory stays zero. An equilibrium is strictly positive when both coordinates are positive. The threshold \(\delta_c\) is defined only when \(e>s\). The parameter restriction entails \(u/(m+u)-hu<0\) for every \(u>0\): without migration, patch one cannot sustain a positive population.

## Proof

**1. The cooperative bounded semiflow.** Set
\[
F(X)=L_\delta X+N(X),\quad X=(u,v)^T,\quad
L_\delta=\begin{pmatrix}-e-\delta&\delta\\\delta&s-\delta\end{pmatrix},\quad
N(X)=\binom{u^2((m+u)^{-1}-h)}{-sv^2}.
\]
For \(u\geq0\), \(N_1(u)\leq0\). Off-diagonal derivatives of \(F\) equal \(\delta>0\), and \(u=0<v\) implies \(\dot u>0\), while \(v=0<u\) implies \(\dot v>0\). Thus the nonnegative quadrant is forward invariant and every nonzero solution is strictly positive at every positive time. The total \(T=u+v\) satisfies
\[
\dot T\leq-eT+(e+s)v-sv^2\leq-eT+\frac{(e+s)^2}{4s}.
\]
Solutions therefore exist globally and remain bounded. The flow is order preserving, with strict positivity between interior states.

**2. Exact linear threshold.** The determinant and trace at zero are
\[
\det L_\delta=\delta(e-s)-es,\qquad
\operatorname{tr}L_\delta=s-e-2\delta.
\]
The real, simple principal eigenvalue \(\lambda_+(\delta)\) of this irreducible Metzler (indeed symmetric) matrix is positive for all \(\delta>0\) if \(e\leq s\), and otherwise has sign \(\operatorname{sgn}(\delta_c-\delta)\). For \(e>s\) and \(\delta>\delta_c\), its other eigenvalue is also negative. Let \(r,\ell\gg0\) be respectively positive right and left principal eigenvectors.

**3. Positive equilibrium, uniqueness and global attraction in the supercritical spectral regime.** Suppose \(\lambda_+>0\). For sufficiently small \(\varepsilon>0\),
\(F(\varepsilon r)=\varepsilon\lambda_+r+O(\varepsilon^2)\gg0\).
For sufficiently large \(M\), \(F(M,M)^T\ll0\), since its components contain \(-hM^2+O(M)\) and \(-sM^2+O(M)\). The monotone positive flow from the lower constant vector rises, and the flow from the upper constant vector falls, producing at least one interior equilibrium between them.

For any \(X\gg0\) and \(c>1\), strict sublinearity holds:
\[
F(cX)\ll cF(X),
\]
because the per-capita expressions \(u/(m+u)-e-hu\) and \(s(1-v)\) are strictly decreasing on positive arguments. If two distinct interior equilibria \(P,Q\) existed, choose \(c=\max_j P_j/Q_j>1\) (interchange the equilibria if necessary). Then \(P\leq cQ\) with equality in at least one coordinate \(i\). Cooperativity yields \(0=F_i(P)\leq F_i(cQ)<cF_i(Q)=0\), impossible. Thus the positive equilibrium \(E\) is unique. Any interior state lies between a sufficiently small and a sufficiently large positive scalar multiple of \(E\). Such multiples are strict sub- and supersolutions by sublinearity and its \(0<c<1\) counterpart; their solutions converge monotonically to equilibria, necessarily \(E\). Comparison shows every nonzero nonnegative solution converges to \(E\).

**4. Exponential extinction when \(\lambda_+<0\).** With \(\ell\gg0\) a positive left eigenvector, define \(W=\ell\cdot X\). As \(N(X)\leq0\) componentwise,
\[
\dot W=\lambda_+W+\ell\cdot N(X)\leq\lambda_+W.
\]
Thus \(W(t)\leq W(0)e^{\lambda_+t}\); since \(\ell\gg0\), both populations decay exponentially.

**5. Global critical decay.** Suppose \(e>s\), \(\delta=\delta_c\), and put
\[
a=s/e\in(0,1),\quad r=(a,1)^T,\quad q=(1,-a)^T,\quad
\kappa=e-s+2\delta_c>0.
\]
Here \(L_{\delta_c}r=0\), \(L_{\delta_c}q=-\kappa q\), with \(r\cdot q=0\). The weighted mass \(W=au+v\) obeys
\[
\dot W=a u^2((m+u)^{-1}-h)-sv^2\leq-sv^2.
\]
Hence \(\int_0^\infty v(t)^2\,dt<\infty\). Since the trajectories and their derivatives are bounded, uniform continuity gives \(v(t)\to0\). The first equation gives \(\dot u\leq-(e+\delta_c)u+\delta_cv\), hence \(u(t)\to0\) by stable linear comparison. The extinction is therefore global even at the neutral linear threshold.

Write \(X=zr+wq\), so
\[
z=\frac{au+v}{1+a^2}>0,\qquad
w=\frac{u-av}{1+a^2}.
\]
Positivity bounds \(w/z\) uniformly. Since \(N(X)=O(\|X\|^2)\), the equations are
\[
\dot z=O(z^2),\qquad \dot w=-\kappa w+O(z^2).
\]
For \(\eta=w/z\), one has \(\dot\eta=-\kappa\eta+O(z)\), because \(\eta\) remains bounded; as \(z(t)\to0\), stable variation of constants yields \(\eta(t)\to0\). Thus \(X=zr+o(z)\). A direct projection of the quadratic term then yields
\[
\dot z=-kz^2+o(z^2),\qquad
k=-\frac{r\cdot((1/m-h)a^2,-s)^T}{r\cdot r}
=\frac{s+a^3(h-1/m)}{1+a^2}>0.
\]
Integrating \((1/z)'=k+o(1)\) establishes \(tz(t)\to1/k\) and the claimed vector limit. This proof applies also at \(m=1/h\), where the first patch's leading self-suppression becomes cubic, because the second patch contributes \(-sv^2\) and keeps \(k>0\).

**6. Coexistence amplitude immediately below the threshold.** Set \(\varepsilon=\delta_c-\delta>0\) and \(B=\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\), so \(L_\delta=L_{\delta_c}+\varepsilon B\). The unique positive equilibria tend to zero as \(\varepsilon\downarrow0\): boundedness and continuity give limit equilibria at criticality, where only zero exists by the strict weighted-mass equation and the equilibrium equations. A smooth Lyapunov--Schmidt decomposition \(X=zr+wq\) gives \(w=O(\varepsilon z+z^2)\) and
\[
0=\alpha\varepsilon z-kz^2+O(\varepsilon^2z+\varepsilon z^2+z^3),\qquad
\alpha=\frac{r\cdot Br}{r\cdot r}=\frac{(1-a)^2}{1+a^2}>0.
\]
The nonzero branch therefore has \(z=(\alpha/k)\varepsilon+O(\varepsilon^2)\), and substituting \(X=zr+wq\) gives the stated first-order vector coefficient.

**Exact rational instance.** For \((e,s,h,m)=(3/4,1/2,1,2)\),
\[
\delta_c=3/2,\quad a=2/3,\quad k=35/78,\quad
\lim_{t\to\infty}t(u(t),v(t))=(52/35,78/35),
\]
and \((u_*,v_*)=(\delta_c-\delta)(4/35,6/35)+O((\delta_c-\delta)^2)\).

## Verification

The accompanying standalone executable `verify.py` uses exact symbolic arithmetic to verify the Jacobian, characteristic discriminant, critical eigenvectors, quadratic reduction, the amplitude coefficient and all rational constants. It also compares representative subcritical equilibria and critical/supercritical trajectories against the asymptotic formulas using finite precision integration. Run `python verify.py` with Python 3, SymPy, NumPy and SciPy. The printed final status is `VERIFY_OK`. The exhaustive-in-time conclusions do not depend on these finite numerical experiments; they follow from the comparison, positivity and asymptotic arguments above.

## Relationship to prior work

Xia et al. [1] introduce the exact linear migration ODE as their equation (2.11), remark that a complete positive-equilibrium classification is not then available, establish global extinction for \(m\geq1/h\), \(e>s\), \(\delta>es/(e-s)\) (Theorem 2.9), and establish a unique positive equilibrium for \(0<\delta\leq s\), with global attraction under the narrower \(\delta<(s-e)/2\) condition (Theorem 2.10). Consequently the known high-migration extinction theorem is **not** new here. The new part is the full sharp parameter partition in the strong-Allee class, the missing globally attracting coexistence regimes, exact critical reciprocal-time profile and explicit branch amplitude. A broader source--sink analysis by Wu et al. [4] reports a global dispersal-dependent persistence/extinction classification for asymmetric patch movement; its accessible abstract does not identify the specific rational Allee--logistic model, and its unavailable full text leaves a priority uncertainty for qualitative components, not affirmative proof of noncoverage. The nonlinear-dispersal equation (2.1) in [1] has multiplicative population-dependent movement and differs essentially from (2.11). Chen, Liu and Chen [2] investigate a distinct additive-Allee model with a different source-patch nonlinearity. General cooperative and sublinear-flow methods motivate the monotonicity proof but do not supply this particular critical asymptotic and branch coefficient without the model-specific calculation.

## Limitations

Only the two-dimensional deterministic ODE with symmetric linear migration and \(m\geq1/h\) is covered. The assertion does not treat weak Allee effects, asymmetric dispersal, stochastic extinction times, reaction-diffusion spatial patterns or the distinct nonlinear-migration model. The critical limit gives a leading term, not a uniform-in-parameters error bound or a second-order long-time expansion. Priority remains contingent on comparison with any unindexed equivalent results, the inaccessible full text of [4], and general-theorem specializations; there has been no independent external mathematical validation.

## References

[1] Y. Xia, L. Chen, V. Srivastava and R. D. Parshad, *Stability and bifurcation analysis of a two-patch model with the Allee effect and dispersal*, Mathematical Biosciences and Engineering 20 (2023), 19781--19807. First public preprint: 2023-10-16. https://arxiv.org/abs/2310.10558 ; https://doi.org/10.3934/mbe.2023876 .

[2] L. Chen, T. Liu and F. Chen, *Stability and bifurcation in a two-patch model with additive Allee effect*, AIMS Mathematics 7 (2022), 536--551. https://doi.org/10.3934/math.2022034 .

[3] Y. Kang and N. Lanchier, *Expansion or extinction: deterministic and stochastic two-patch models with Allee effects*, Journal of Mathematical Biology 62 (2011), 925--973. https://arxiv.org/abs/1003.0121 .

[4] H. Wu, Y. Wang, Y. Li and D. L. DeAngelis, *Dispersal asymmetry in a two-patch system with source--sink populations*, Theoretical Population Biology 131 (2020), 54--65. https://doi.org/10.1016/j.tpb.2019.11.004 .
