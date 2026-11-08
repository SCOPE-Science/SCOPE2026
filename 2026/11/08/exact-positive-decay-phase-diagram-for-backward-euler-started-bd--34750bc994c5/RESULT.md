# Exact positive-decay phase diagram for backward-Euler-started BDF2 on alternating time grids

## Finding

For the scalar dissipative equation \(u'(t)=-\lambda u(t)\) with \(\lambda>0\), choose arbitrary \(u_0>0\) and positive time steps alternating forever between \(h_1\) and \(h_2\). Start with one backward-Euler step and subsequently use the **genuine variable-step BDF2** formula (quadratic interpolation on the most recent three nonuniform time levels). Write
\[
x=\lambda h_1>0,\qquad y=\lambda h_2>0,\qquad s=x+y,\qquad
\Delta=(x-y)^2-4(s-1).
\]
Then the following three statements are equivalent:

1. \(u_n>0\) for every integer \(n\geq0\).
2. \(u_0>u_1>u_2>\cdots>0\).
3. \(s<2\) and \(\Delta\geq0\).

Thus every positive step split is admissible when \(0<s\leq1\); for \(1<s<2\), precisely the splits satisfying \(\lvert x-y\rvert\geq2\sqrt{s-1}\) are admissible; and there are none for \(s\geq2\). At fixed \(s\in(1,2)\), setting \(r=\max\{x,y\}/\min\{x,y\}\), the criterion is equivalently
\[
r\geq r_*(s):=\frac{s+2\sqrt{s-1}}{s-2\sqrt{s-1}},\qquad
r_*(s)\sim\frac{16}{(2-s)^2}\quad(s\uparrow2).
\]
In the equal-step case \(x=y\), this yields the familiar sharp bound \(x=y\leq1/2\). With unequal steps, the admissible mean normalized step \(s/2\) has supremum \(1\), twice the equal-step maximum \(1/2\) (the supremum is not achieved by a finite positive pair). A rational boundary example is \((x,y)=(1/8,9/8)\), where \(\Delta=0\), whereas the equal split of the same total \(s=5/4\) does not preserve positivity indefinitely.

## Assumptions and scope

Fix \(\lambda,u_0,h_1,h_2>0\) and time levels \(t_0=0\), \(t_n-t_{n-1}=h_1\) for odd \(n\), and \(h_2\) for even \(n\). Initialize \(u_1=u_0/(1+x)\). For every \(n\geq2\), define \(u_n\) by
\[
\bigl[1+2r_n+(1+r_n)z_n\bigr]u_n
=(1+r_n)^2u_{n-1}-r_n^2u_{n-2},\qquad
r_n=\frac{h_n}{h_{n-1}},\quad z_n=\lambda h_n.
\]
All denominators are strictly positive, so the numerical trajectory exists uniquely at every index. The claim is about this specific positive scalar initial-value problem and its specified backward-Euler starter, not about positivity for arbitrary two-value histories, perturbations, nonlinear problems, general matrices, or aperiodic grids.

## Proof

**1. Exact two-step monodromy.** Set
\[
D_x=x^2+xy+2x+y,\qquad D_y=xy+x+y^2+2y,\qquad H=D_xD_y.
\]
The step of normalized size \(y\), following one of size \(x\), is \(u_{n}=A_yu_{n-1}-B_yu_{n-2}\), where
\[
A_y=\frac{s^2}{xD_y},\qquad B_y=\frac{y^2}{xD_y}.
\]
The reverse step has \(A_x=s^2/(yD_x)\), \(B_x=x^2/(yD_x)\). In particular, for \(w_k=(u_{2k+1},u_{2k})^{\mathsf T}\),
\[
w_{k+1}=Pw_k,\quad
P=\begin{pmatrix}
A_xA_y-B_x&-A_xB_y\\
A_y&-B_y
\end{pmatrix},\quad
w_0=u_0\begin{pmatrix}(1+x)^{-1}\\1\end{pmatrix}.
\]
Direct polynomial simplification gives
\[
\operatorname{tr}P=\frac{N}{H},\qquad
\det P=\frac{xy}{H}>0,\qquad
(\operatorname{tr}P)^2-4\det P=\frac{s^4\Delta}{H^2},
\]
where \(N=s^2(2-s)+2xy(s+1)\). Consequently the two multipliers, when real, are
\[
\mu_\pm=\frac{N\pm s^2\sqrt{\Delta}}{2H}.
\]
All displayed polynomial identities are also checked exactly by the companion program `verify.py`.

**2. Sufficiency with distinct multipliers.** Suppose \(s<2\) and \(\Delta>0\). Since \(N>0\) and \(\det P>0\), the multipliers satisfy \(\mu_+>\mu_->0\). An eigenvector for \(\mu\) with second component \(1\) is \(v(\mu)=(q(\mu),1)^{\mathsf T}\), where \(q(\mu)=(\mu+B_y)/A_y>0\). Denote \(q_\pm=q(\mu_\pm)\); then \(0<q_-<q_+\). Put \(q=(1+x)^{-1}\). The exact second iterate, normalized by \(u_0\), is
\[
z=\frac{u_2}{u_0}=A_yq-B_y
=\frac{x+2y-y^2}{(1+x)D_y}.
\]
One more exact identity gives
\[
2H(z-\mu_-)=s^2\left(
\frac{2x^2+(2-s)(1+x)}{1+x}+\sqrt{\Delta}
\right)>0.
\]
Hence \(q>q_-\), so the decomposition
\[
\frac{w_0}{u_0}=c_+v(\mu_+)+c_-v(\mu_-),\quad
c_+=\frac{q-q_-}{q_+-q_-}>0,\quad c_-=1-c_+
\]
has a strictly positive dominant coefficient. If \(c_-\geq0\), positivity of every \(P^kw_0\) is immediate. If \(c_-<0\), then for each vector component \(j\), because \(\mu_-/\mu_+\in(0,1)\) and \(v_j(\mu_-)>0\),
\[
(P^kw_0)_j=u_0\mu_+^k\left[c_+v_j(\mu_+)
+c_-\left(\frac{\mu_-}{\mu_+}\right)^kv_j(\mu_-)\right]
\geq u_0\mu_+^k\left[c_+v_j(\mu_+)+c_-v_j(\mu_-)\right]>0.
\]
Thus both even and odd-indexed iterates are positive for all \(k\geq0\).

**3. Sufficiency at the double root.** If \(s<2\) and \(\Delta=0\), then \(\mu=N/(2H)>0\), \((P-\mu I)^2=0\), and the preceding strict starter identity gives \(q>q_*=(\mu+B_y)/A_y\). Writing \(w_0/u_0=v(\mu)+(q-q_*)e_1\), we find
\[
(P-\mu I)w_0=u_0(q-q_*)
\begin{pmatrix}\mu+B_y\\ A_y\end{pmatrix}>0.
\]
The finite binomial expansion
\[
P^kw_0=\mu^kw_0+k\mu^{k-1}(P-\mu I)w_0
\]
is therefore componentwise positive for every nonnegative integer \(k\) (with the second summand zero for \(k=0\)).

**4. Necessity.** If \(\Delta<0\), the monodromy eigenvalues form a nonreal conjugate pair \(\rho e^{\pm i\theta}\), \(0<\theta<\pi\). Each component of \(P^kw_0\) is a real oscillatory sequence \(\rho^k(a\cos k\theta+b\sin k\theta)\); at least the second component has \(a=u_0>0\). Such a sequence takes negative values: if \(\theta/(2\pi)\) is rational, its full period averages to zero and cannot be everywhere nonnegative with a positive zeroth value; if irrational, the orbit is dense on the circle. Therefore some \(u_n<0\).

If \(s\geq2\), the case \(\Delta<0\) was just handled. When \(s>2\) and \(\Delta\geq0\), necessarily \(xy\leq(s-2)^2/4\); thus
\[
N\leq-s^2(s-2)+\frac{(s-2)^2(s+1)}2
=-\frac{(s-2)(s^2+s+2)}2<0.
\]
Both real multipliers are strictly negative. Any nonzero real scalar component of a two-dimensional recurrence with these negative characteristic roots eventually alternates sign (a double root gives the same conclusion via \((a+bk)\mu^k\)). In particular, the scalar sum of the two coordinates of \(P^kw_0\), initially positive and never identically zero because \(P\) is invertible, cannot stay positive. At \(s=2\), \(\Delta=-4xy<0\). This exhausts all excluded parameter pairs.

**5. Strict decay and the phase boundary.** Rearranging the defining recurrence gives
\[
[1+2r_n+(1+r_n)z_n](u_n-u_{n-1})
=r_n^2(u_{n-1}-u_{n-2})-(1+r_n)z_nu_{n-1}.
\]
The starter satisfies \(0<u_1<u_0\). If all iterates are positive, induction on the displayed identity proves \(u_n<u_{n-1}\) strictly at every index, so positivity and strict positive decay are equivalent. Finally, \(\Delta=(x-y)^2-4(s-1)\); algebra gives the stated ratio threshold \(r_*(s)\). Its quadratic divergence as \(s\uparrow2\) follows from expanding \(\sqrt{s-1}\) at \(s=2\). The equal-grid boundary and near-double admissible mean step follow directly.

## Verification

Run `python verify.py` with Python 3.10+ and SymPy 1.11+ (dependency in `requirements.txt`). The program verifies six symbolic rational-function identities in the proof, 234 distinct admissible rational parameter pairs for 60 subsequent updates each, four critical/contrast pairs for 120 updates each, and six explicit outside-domain pairs with recorded negative iterates. It checks strict decrease wherever the theorem predicts it. These are supplementary finite checks; the proof above, not sampling or bounded iteration, establishes the universal all-index statements. No computer-assisted interval numerics or external certificates are required.

## Relationship to prior work

Bonaventura and Della Rocca (2015) analyze positivity and absolute monotonicity for **one-step TR-BDF2** and hybrid methods, not genuine continuously restarted variable-step BDF2. Wang, Mao and Wang (2020), and Li and Liao (2022), analyze norm stability and errors for variable-grid BDF2, including backward-Euler starts, without the specific two-periodic all-index scalar sign characterization. Liao, Tang and Zhou (2020) derive sufficient ratio and stepsize criteria for a nonlinear Allen–Cahn maximum principle; their bounds are not the present necessary-and-sufficient alternating scalar criterion. Malygina (2014) gives general characteristic-root criteria for positivity of fundamental solutions of constant-coefficient difference equations: that mathematical mechanism is prior art, not claimed as new. The result here adds the genuine unequal-grid BDF2 two-period monodromy, its explicit step-pair phase boundary, and the backward-Euler-starter comparison, which are required to turn a spectral condition into the claimed all-index statement.

## Limitations

This is a **single scalar-decay mode** with strictly positive two-periodic steps and a fixed backward-Euler starter. It does not prove nonnegativity for every two-component initial history, matrix diffusion, nonlinear problems, arbitrary nonperiodic grids, stability under perturbations, accuracy improvement, or a universal strong-stability-preserving radius. Large ratios in the positive region may be undesirable for error control. The optimal mean normalized step is a supremum requiring unbounded step contrast and is never attained by a finite positive pair. Publication priority against uninspected specialist cyclic-difference results remains a genuine uncertainty; no independent audit has occurred.

## References

- L. Bonaventura and A. Della Rocca, *Monotonicity, positivity and strong stability of the TR-BDF2 method and of its SSP extensions*, first public arXiv version 14 October 2015, [arXiv:1510.04303v1](https://arxiv.org/abs/1510.04303).
- V. V. Malygina, *On Positiveness of the Fundamental Solution of a Difference Equation*, Russian Mathematics 58(3) (2014), 14–25, [doi:10.3103/S1066369X14030025](https://doi.org/10.3103/S1066369X14030025).
- W. Wang, M. Mao and Z. Wang, *Stability and error estimates for the variable step-size BDF2 method for linear and semilinear parabolic equations*, [arXiv:2003.03534v1](https://arxiv.org/abs/2003.03534).
- H.-L. Liao, T. Tang and T. Zhou, *On energy stable, maximum-principle preserving, second order BDF scheme with variable steps for the Allen–Cahn equation*, [arXiv:2003.00421v1](https://arxiv.org/abs/2003.00421).
- Z. Li and H.-L. Liao, *Stability of variable-step BDF2 and BDF3 methods*, [arXiv:2201.00527v1](https://arxiv.org/abs/2201.00527).
