# Sharp RK4 positivity on heterogeneous weighted stars and a strict spectral-stability gap

## Finding

Let a star have one hub labeled \(0\), \(m\ge 2\) leaves labeled \(1,\ldots,m\), and arbitrary strictly positive edge conductances \(w_1,\ldots,w_m\). The symmetric, unnormalized weighted graph Laplacian is \(L\), with \(L_{00}=\sum_iw_i\), \(L_{ii}=w_i\), \(L_{0i}=L_{i0}=-w_i\), and all other entries zero. For every \(h\ge 0\), consider the *completed classical four-stage fourth-order explicit Runge–Kutta* heat update
\[
T(h)=R_4(-hL),\qquad R_4(-z)=1-z+\frac{z^2}{2}-\frac{z^3}{6}+\frac{z^4}{24}.
\]

Put \(S=\sum_iw_i\), \(V=\sum_iw_i^2\), \(W=\sum_iw_i^3\), and \(a=\max_i w_i\). Define
\[
\begin{split}
 A&=S+a,\\
 B&=S^2+V+Sa+a^2,\\
 C&=S^3+2SV+W+S^2a+Va+Sa^2+a^3,\\
 Q_a(h)&=1-\frac{Ah}{2}+\frac{Bh^2}{6}-\frac{Ch^3}{24}.
\end{split}
\]

There is exactly one positive real root \(H\) of \(Q_a(H)=0\), and
\[
\boxed{\ T(h)\text{ is entrywise nonnegative}\ \Longleftrightarrow\ 0\le h\le H.\ }
\]
For \(0<h<H\), every entry is strictly positive. At \(h=H\), precisely the hub-to-leaf entries incident to edges of maximum conductance become zero (and their symmetric counterparts); every other entry remains strictly positive. Those entries are negative for every \(h>H\): the positivity window never reappears.

Write \(r>0\) for the unique positive root of \(r^3-4r^2+12r-24=0\), and \(\lambda_{\max}\) for the largest eigenvalue of \(L\). The usual Euclidean stability interval for this linear heat system is \(0\le h\le r/\lambda_{\max}\). The positivity horizon satisfies
\[
\boxed{\ H\le \frac{r}{\lambda_{\max}},\quad
H=\frac{r}{\lambda_{\max}}\ \Longleftrightarrow\ w_1=\cdots=w_m.\ }
\]
Thus unequal spoke conductances cause loss of nonnegativity *strictly before* the classical RK4 spectral-stability limit. If all weights equal \(w\), the equality case is \(H=r/((m+1)w)\).

For example, \((w_1,w_2)=(1,2)\) gives \(H\approx0.5680221063\), versus a spectral-stability limit of approximately \(0.5886017874\). These decimals illustrate the theorem and are not proof certificates.

## Assumptions and scope

Only finite symmetric weighted stars, positive conductances, exact completed RK4 end steps, and nonnegative step sizes are treated. The star may have any number of leaves \(m\ge2\). Entrywise nonnegativity is equivalent to mapping every coordinatewise nonnegative initial state to a nonnegative one after one completed step. Stage-by-stage positivity, nonlinear heat equations, and nonstar networks are not asserted. Spectral stability means the operator norm of the symmetric update is at most one in the Euclidean norm.

## Proof

**1. Exact entry formulas.** For each leaf \(i\), the arrowhead structure of the Laplacian gives the hub-to-leaf polynomial
\[
T_{0i}(h)=T_{i0}(h)=h w_i Q_{w_i}(h),
\]
where \(Q_x\) has the preceding definition with \(a\) replaced everywhere by \(x\). For distinct leaves \(i,j\), put \(x=w_i\), \(y=w_j\) and
\[
D_{xy}=S^2+V+S(x+y)+x^2+xy+y^2.
\]
Direct multiplication of powers of the arrowhead matrix gives
\[
T_{ij}(h)=\frac{h^2xy}{24}\bigl(12-4h(S+x+y)+h^2D_{xy}\bigr).
\]
These identities hold for arbitrary positive real weights, with no symmetry among the leaves. To see the coefficient structure directly, \((L^2)_{0i}=-w_i(S+w_i)\), \((L^3)_{0i}=-w_i(S^2+V+Sw_i+w_i^2)\), and \((L^4)_{0i}=-w_i(S^3+2SV+W+S^2w_i+Vw_i+Sw_i^2+w_i^3)\). The signs alternate in the RK4 expansion, yielding the stated \(Q\).

**2. No leaf-to-leaf or diagonal obstruction.** For any positive \(x,y\),
\[
3D_{xy}-(S+x+y)^2=2S^2+3V+S(x+y)+2x^2+xy+2y^2>0.
\]
Thus the quadratic factor of \(T_{ij}\) has negative discriminant and positive leading coefficient, and all distinct-leaf transitions are strictly positive for every \(h>0\). For \(z\ge0\),
\[
24R_4(-z)=z^2(z-2)^2+8(z^2-3z+3)>0.
\]
By the spectral theorem each diagonal \(T_{ii}(h)=\langle e_i,R_4(-hL)e_i\rangle\) is strictly positive for every \(h\ge0\), including at the positivity horizon.

**3. Unique hub-edge crossing for every leaf.** Fix a spoke weight \(x=w_i\) and put \(b=S-x>0\), \(v=V-x^2\), and \(u=W-x^3\). Let \(A_x,B_x,C_x\) be the three coefficients of \(Q_x\). An exact algebraic identity is
\[
\begin{split}
9A_xC_x-4B_x^2={}&80x^4+120x^3b+76x^2b^2+30xb^3+5b^4\\
&+v(22x^2+39xb+10b^2)+u(18x+9b)-4v^2.
\end{split}
\]
Because \(v\le b^2\), the last potentially negative term can be combined with \(10b^2v\) to obtain \(10b^2v-4v^2\ge6b^2v\ge0\). All other terms are positive or nonnegative and \(x>0\), so \(9A_xC_x>4B_x^2\). Therefore
\[
Q_x'(h)=-\frac{A_x}{2}+\frac{B_xh}{3}-\frac{C_xh^2}{8}<0
\]
for every real \(h\): its quadratic has strictly negative discriminant and a negative leading coefficient. Since \(Q_x(0)=1\) and \(Q_x(h)\to-\infty\) as \(h\to+\infty\), every hub-to-leaf entry crosses zero exactly once, permanently.

**4. The largest spoke is the first to cross.** For any two weights \(x>y>0\), expansion gives
\[
Q_x(h)-Q_y(h)= -\frac{(x-y)h}{24}\bigl(12-4h(S+x+y)+h^2D_{xy}\bigr)<0
\qquad(h>0),
\]
where strict negativity follows from Step 2. Hence the maximum-weight leaf has the smallest individual hub-edge zero. At the first such zero all other edges, nonedges, and diagonal entries have the signs claimed in the theorem. This proves the global if-and-only-if positivity classification.

**5. Sharp comparison with spectral stability.** Since \(L\) is real symmetric and positive semidefinite, the spectral norm of \(T(h)\) is \(\max_{\lambda\in\sigma(L)}|R_4(-h\lambda)|\). Step 2 shows \(R_4(-z)>0\), and
\[
R_4(-z)-1=\frac{z}{24}(z^3-4z^2+12z-24).
\]
The cubic in parentheses is strictly increasing on the real line, because its derivative \(3z^2-8z+12\) has negative discriminant and positive leading coefficient. Therefore the Euclidean stability interval is exactly \(0\le h\le r/\lambda_{\max}\). If \(T(H)\) is entrywise nonnegative, it is stochastic since \(L\mathbf1=0\), so its spectral norm is at most one (it is also symmetric). This yields \(H\le r/\lambda_{\max}\).

If the weights are not all equal, there is a leaf of smaller-than-maximum conductance, so at \(h=H\) at least one hub-to-leaf transition remains strictly positive. Every distinct-leaf transition is positive, hence the stochastic matrix \(T(H)\) is irreducible. Perron–Frobenius makes eigenvalue \(1\) simple. If \(H=r/\lambda_{\max}\), a nonconstant Laplacian eigenvector for \(\lambda_{\max}>0\) would furnish a second eigenvector with eigenvalue \(R_4(-r)=1\), a contradiction. Thus inequality is strict for unequal weights. When all weights equal \(w\), the weighted star has Laplacian eigenvalues \(0,w\) (multiplicity \(m-1\)) and \((m+1)w\), and its hub-to-leaf update is \((1-R_4(-(m+1)wh))/(m+1)\). Consequently \(H=r/((m+1)w)\), proving the equality statement.

## Verification

Run `python3 verify.py` (standard library only). It uses exact rational matrix multiplication, not floating-point tolerances, to test arrowhead identities, negative-discriminant certificates, uniqueness certificates and endpoint sign predictions for \(90\) specified and seeded-random weight configurations with \(2\) through \(7\) leaves. At review, it printed `VERIFY_OK 42875 rational matrix identities and signs; 90 weight configurations`. The all-positive-weight, all-size and exact uniqueness claims are justified by the proof above; a finite program is not an infinite proof. The two illustrative decimal values in the Finding section were computed separately from characteristic eigenvalues and cubic roots.

## Relationship to prior work

The SSP and monotonicity literature, including Ketcheson–Gottlieb–Macdonald (2011), develops method-level positivity/stability guarantees and order barriers; it does not in its inspected treatment evaluate this exact arbitrary-weight star RK4 positivity horizon. Horváth (1998) provides a broader Runge–Kutta positivity framework, but full-text assessment of that potentially relevant source was unavailable. Earlier graph-specific studies already provide a fourth-order RK4 obstruction formula for **unweighted bipartite graphs**, including unit-weight stars, and a family-wide result for unweighted complete multipartite graphs. Those are covered, not new. Separate prior work determines the strongest-spoke obstruction for the **two-stage implicit Gauss–Legendre rational** fourth-order heat update on weighted stars; its stability function and positivity horizon are different from the classical explicit RK4 polynomial here. This theorem's distinct claim concerns the unrestricted positive conductance vector for explicit RK4, the unique scalar cubic threshold and the iff spectral-gap/equality criterion.

## Limitations

No claim of exhaustive publication priority is made. The inaccessible full text of Horváth (1998) and possible unindexed general matrix-polynomial positivity formulas are residual risks. Nonstar graphs can have other obstructions. No stagewise SSP or nonlinear positivity claim follows. Numerically printed decimal approximations are not substituted for the rigorous proof. Independent external mathematical validation is not performed.

## References

- D. I. Ketcheson, S. Gottlieb and C. B. Macdonald, *Strong Stability Preserving Two-step Runge–Kutta Methods*, arXiv:1106.3626v1 (first publicly posted June 18, 2011), https://arxiv.org/html/1106.3626v1.
- Z. Horváth, *Positivity of Runge-Kutta and diagonally split Runge-Kutta methods*, Applied Numerical Mathematics 28 (1998), 309–326, DOI:10.1016/S0168-9274(98)00050-6. Only abstract/metadata were accessible for this comparison.
- I. Higueras, D. I. Ketcheson and T. A. Kocsis, *Optimal monotonicity-preserving perturbations of a given Runge-Kutta method*, arXiv:1505.04024 (2015); full text was not accessible for this comparison.
- Earlier mathematical results on unweighted bipartite RK4 positivity and fourth-order Gauss–Legendre positivity on weighted stars, compared at statement/assumption level; the unweighted and different-method special cases are expressly credited.
