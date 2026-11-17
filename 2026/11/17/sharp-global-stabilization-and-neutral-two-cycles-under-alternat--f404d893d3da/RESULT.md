# Sharp global stabilization and neutral two-cycles under alternating-coordinate Lozi control

## Finding

For the classical Lozi map with alternating *one-coordinate-at-a-time* target feedback, the exact global exponential stabilization threshold coincides with the local Floquet boundary. At equality, the controlled system supports an explicitly parameterized nonconstant family of two-season periodic orbits; beyond it the target is a two-step saddle. No restriction to the positive half-plane is needed for convergence below threshold.

The sharp threshold is
\[
\boxed{r_*(a,b,t)=\frac{1-b}{a^2+b(1-b)t}.}
\]
For every admissible parameter triple the full-plane target is globally exponentially stable exactly when \(r<r_*\).

## Assumptions and scope

Fix real parameters \(a>1\), \(0<b<1\), \(0<r,t<1\). Define
\[
F(x,y)=(1-a|x|+y,\;bx),\qquad
\xi=\frac1{1+a-b},\qquad P=(\xi,b\xi).
\]
Then \(\xi>0\) and \(F(P)=P\). On even-to-odd steps apply only first-coordinate target control, retaining the second coordinate of \(F\); on odd-to-even steps apply only second-coordinate target control, retaining the first coordinate of \(F\):
\[
\begin{split}
X_{2k+1}&=A_r(X_{2k}),\\
A_r(X)&=P+\operatorname{diag}(r,1)(F(X)-P),\\
X_{2k+2}&=B_t(X_{2k+1}),\\
B_t(X)&=P+\operatorname{diag}(1,t)(F(X)-P).
\end{split}
\]
Here \(k\) ranges over all nonnegative integers, and initial states are arbitrary \(X_0\in\mathbb R^2\), including points crossing the fold. Feedback intensities on the active coordinates are \(1-r\) and \(1-t\), respectively. Each controlled step preserves \(P\), but no step controls both coordinates.

**Theorem.** Put
\[
r_*:=\frac{1-b}{a^2+b(1-b)t} \in(0,1).
\]
(1) If \(0<r<r_*\), there exist constants \(C>0\) and \(0<\gamma<1\), depending only on \(a,b,r,t\), such that for every \(X_0\in\mathbb R^2\) and every integer \(n\ge0\),
\[
\|X_n-P\|_\infty\le C\gamma^n\|X_0-P\|_\infty.
\]
(2) If \(r=r_*\), then every \(\varepsilon\ne0\) with
\[
|\varepsilon|<\frac{\xi}{\max\{a,1-b\}}
\]
generates an exact nonconstant two-season periodic trajectory
\[
\begin{split}
X_{2k}&=P+\varepsilon\bigl(a,-b(1-b)t\bigr),\\
X_{2k+1}&=P+\varepsilon\bigl(-(1-b),ab\bigr).
\end{split}
\]
Thus \(P\) is not asymptotically stable at equality. (3) If \(r>r_*\), the two-step return map has one real multiplier larger than one and another strictly between zero and one at \(P\), hence \(P\) is a hyperbolic saddle and not locally asymptotically stable. In particular, global exponential stability holds **if and only if** \(r<r_*\).

## Proof

**Step 1: a global positive comparison system.** For any real \(x\), since \(\xi>0\), the reverse triangle inequality gives
\[
\big|\,|x|-\xi\,\big|\le |x-\xi|.
\]
Let \(e(X)=(|x-\xi|,|y-b\xi|)^{\mathsf T}\). By the triangle inequality the controlled steps satisfy the componentwise inequalities
\[
e(A_r(X))\le L_A e(X),\qquad e(B_t(X))\le L_B e(X),
\]
where
\[
L_A=\begin{pmatrix}ar&r\\b&0\end{pmatrix},
\qquad
L_B=\begin{pmatrix}a&1\\bt&0\end{pmatrix}.
\]
In particular, the *complete two-season* comparison holds globally:
\[
e(X_{2k+2})\le L e(X_{2k}),\qquad
L=L_B L_A=
\begin{pmatrix}a^2r+b&ar\\abrt&brt\end{pmatrix}.
\]
No assumption is made about the signs of the state coordinates at intermediate times.

**Step 2: the sharp contraction inequality.** The matrix \(L\) is strictly positive; its trace and determinant are
\[
T=a^2r+b+brt>0,\qquad D=b^2rt\in(0,1).
\]
The eigenvalues are real, distinct and positive, because the off-diagonal entries are positive and the discriminant equals \((L_{11}-L_{22})^2+4L_{12}L_{21}>0\). Since their product is \(D<1\), both eigenvalues lie below one exactly when their characteristic polynomial at one is positive:
\[
\begin{split}
\det(I-L)&=1-T+D\\
&=(1-b)-r\bigl(a^2+b(1-b)t\bigr)>0\\
&\Longleftrightarrow r<r_*.
\end{split}
\]
At the strict inequality the spectral radius \(\rho(L)<1\), so for any \(\gamma_2\) with \(\rho(L)<\gamma_2<1\) there is a finite \(C_2\) such that \(\|L^k\|_\infty\le C_2\gamma_2^k\) for all integers \(k\ge0\). Combining the even-step bound with the odd-step inequality gives the theorem's uniform estimate with \(\gamma=\sqrt{\gamma_2}\), after enlarging \(C\). This proves full-plane global exponential stability.

**Step 3: necessity and the exact boundary continuum.** Because \(\xi>0\), both controlled maps are affine in a neighborhood of \(P\), with Jacobians
\[
J_A=\begin{pmatrix}-ar&r\\b&0\end{pmatrix},
\qquad J_B=\begin{pmatrix}-a&1\\bt&0\end{pmatrix}.
\]
Their two-step derivative is
\[
Q=J_BJ_A=\begin{pmatrix}a^2r+b&-ar\\-abrt&brt\end{pmatrix}.
\]
With \(S=\operatorname{diag}(1,-1)\), we have \(Q=SLS\), so the local Floquet eigenvalues equal those of the global comparison matrix, with precisely the same sharp threshold. At \(r>r_*\), the larger multiplier exceeds one while the smaller lies in \((0,1)\); hence \(P\) is a hyperbolic saddle. At \(r=r_*\), let
\[
v=\bigl(a,-b(1-b)t\bigr)^{\mathsf T},\quad
w=\bigl(-(1-b),ab\bigr)^{\mathsf T}.
\]
Direct multiplication gives \(J_Av=w\) and \(J_Bw=v\), using \(r_*(a^2+b(1-b)t)=1-b\). For every \(\varepsilon\) satisfying the stated strict bound, both x-coordinates of \(P+\varepsilon v\) and \(P+\varepsilon w\) remain strictly positive. The nonlinear controlled maps therefore agree exactly with their affine expansions at these two points. Consequently \(A_{r_*}(P+\varepsilon v)=P+\varepsilon w\), and \(B_t(P+\varepsilon w)=P+\varepsilon v\). Since \(v\ne w\), the controlled orbit is nonconstant. The full classification follows. \(\square\)

## Verification

For a concrete nondegenerate parameter choice,
\[
(a,b,t)=\left(\frac75,\frac3{10},\frac12\right),
\quad r_*=\frac{140}{413}.
\]
The standalone `checker.py` uses exact rational arithmetic. It checks the two-step matrices, the characteristic polynomial and threshold for \(r\in\{1/4,140/413,1/2\}\); verifies 108 representative full-plane finite trajectories against the exact two-step positive majorant over eight periods; and checks three distinct critical cycles, including positive coordinates at both phases. Its success message is `PERIODIC_LOZI_COORDINATE_SHARP_OK exact_matrix_cases=3 comparison_trajectories=108 critical_two_cycles=3`. The finite checks are **not** substituted for the analytic proof of any all-state or infinite-time assertion.

Reproduce with `python3 checker.py` using only the Python standard library. The checker applies to the displayed rational instance; the symbolic proof above applies to the entire stated real parameter domain.

## Relationship to prior work

Braverman and Rodkina [1] introduce modified vector target-oriented control for Lozi maps with deterministic, step-dependent diagonal control matrices. Their Theorem 2.1 and Proposition 2.5 give sufficient *per-step* contraction conditions and local stabilization estimates; their Remark 2 addresses full-plane control with a coarser one-step bound. In the present two-season schedule the second step has no first-coordinate intervention, and its local Jacobian is already expanding for \(a>1\); the pointwise contraction hypothesis from [1] cannot certify it. The distinct contribution here is the exact two-step global threshold, its coincidence with the local saddle frontier, and the continuum of exact neutral periodic responses at equality.

Braverman and Chan [2] study regular and pulse stabilization for scalar maps; their accessible abstract does not state a two-coordinate Lozi Floquet boundary. A separate published study of delayed Lozi recurrences [3] addresses autonomous delayed orbit parity, not alternating target controllers. Those works are not claimed as new here. The Floquet and Perron matrix steps use standard linear algebra; novelty rests on the particular nonlinear all-plane classification and boundary construction, not the general matrix criteria.

## Limitations

The theorem covers the stated alternating schedule, fair deterministic temporal allocation, the positive fixed point and the real parameter domain \(a>1\), \(0<b<1\), \(0<r,t<1\). It does not classify arbitrary switching words, random feedback, other targets, global attractor structure beyond the stable regime, or physical actuator saturation. The strict inequality ensures exponential convergence but no uniform decay rate as \(r\uparrow r_*\). At criticality the exhibited periodic family establishes failure of target attraction, not completeness of all possible invariant sets. Although full relevant sections of [1] were inspected, publication priority beyond indexed and accessible literature remains a risk.

## References

1. E. Braverman and A. Rodkina, *On Target-Oriented Control of Hénon and Lozi maps*, Journal of Difference Equations and Applications (first publicly available 18 June 2022), DOI: https://doi.org/10.1080/10236198.2022.2088286; open manuscript https://arxiv.org/html/2208.09092v1 (arXiv posting 18 August 2022).
2. E. Braverman and B. Chan, *Stabilization of prescribed values and periodic orbits with regular and pulse target oriented control*, Chaos 24 (2014), 013119, https://pubmed.ncbi.nlm.nih.gov/24697381/.
3. *Delay-parity bifurcations of prime-two cycles in the generalized Lozi recurrence*, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-delay-parity-bifurcations-of-prime-two-cycles-in-the-generalized--61b734b81bc7.
