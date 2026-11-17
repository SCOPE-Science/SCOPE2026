# Sharp indicator scale and positive-witness transition for the Kalton–Peck range gauge

## Finding

Let \(\Omega:L^1([0,1];\mathbb K)\to L^0([0,1];\mathbb K)\) be the logarithmic centralizer
\[
\Omega(f)(x)=f(x)\log\frac{|f(x)|}{\|f\|_1},\qquad \Omega(0)=0,
\]
with the value zero wherever \(f(x)=0\), and \(\mathbb K=\mathbb R\) or \(\mathbb C\). Equip its range with the specific quotient quasi-gauge
\[
\rho(g)=\inf_{f\in L^1}\left(\|g-\Omega(f)\|_1+\|f\|_1\right),
\]
allowing an infinite residual norm. For every measurable \(A\subseteq[0,1]\) of measure \(t\) with \(0<t\le\exp(-\varphi)\), where \(\varphi=(1+\sqrt5)/2\), the **unrestricted** range gauge satisfies
\[
\boxed{\frac{t}{\log(1/t)}\left(1-\frac{t}{e}\right)
\le\rho(\mathbf1_A)\le\frac{t}{\log(1/t)}.}
\]
Consequently, the exact leading coefficient exists:
\[
\boxed{\lim_{t\downarrow0}\frac{\rho(\mathbf1_A)\log(1/t)}{t}=1,}
\]
uniformly over measurable sets \(A\) of a given measure \(t\). The relative uncertainty in the displayed two-sided estimate is at most \(t/e\).

There is also an exact finite-measure classification for the **nonnegative-witness restriction**, which is distinct from the unrestricted gauge:
\[
\rho_+(\mathbf1_A)=\inf_{\substack{f\in L^1([0,1];\mathbb R)\\f\ge0}}
\left(\|\mathbf1_A-\Omega(f)\|_1+\|f\|_1\right).
\]
Writing \(t_*=e^{-\varphi}\), for every \(0<t<1\),
\[
\boxed{\rho_+(\mathbf1_A)=
\begin{cases}
\dfrac{t}{\log(1/t)},&0<t\le t_*,\\[4pt]
t-t_*\left(1-\dfrac{1}{\varphi}\right),&t_*\le t<1.
\end{cases}}
\]
A minimizing positive witness is \(f=\mathbf1_E/\log(1/\delta)\), where \(E\subseteq A\) has measure \(\delta=\min(t,t_*)\). Thus the positive-witness optimization has a sharp support-saturation transition at \(t_*\). **The second boxed formula is not an exact formula for the unrestricted gauge.**

## Assumptions and scope

Lebesgue measure is normalized so that \(|[0,1]|=1\), and sets are considered modulo null sets. Natural logarithms are used. All gauge statements apply to real and complex input fields; the restricted optimization uses real nonnegative witnesses. The atomlessness of \([0,1]\) is used to select \(E\subseteq A\) with any prescribed measure up to \(t\). The result concerns the exact quotient gauge above, not an arbitrarily equivalent Orlicz or rearrangement-invariant quasi-norm.

## Proof

**1. A pointwise Lambert envelope.** Fix \(f\in L^1\) with \(s=\|f\|_1>0\). Let \(W=W_0(1/s)>0\) be the unique solution of \(W e^W=1/s\). For a scalar magnitude \(u\ge s\), the identity \(u_0=1/W\) gives \(u_0\log(u_0/s)=1\). On \(s\le u\le u_0\), the function \(u\log(u/s)\) is at most \(1\), and \(\log(u/s)\le W\). On \(u\ge u_0\), \(1/u\le W\). Hence
\[
\min\{1,u\log(u/s)\}\le Wu\qquad(u\ge s).
\]
For \(0\le u<s\), the elementary maximum of \(v\log(1/v)\) on \([0,1]\) implies
\[
|u\log(u/s)|\le s/e.
\]
Combining the branches, for every complex or real \(f\),
\[
\int_A\min\{1,|\Omega(f)|\}\le sW+\frac{st}{e}.\tag{1}
\]
The weaker but convenient right-hand side uses \(\int_A|f|\le s\). The inequality holds even when \(\Omega(f)\) is not integrable.

**2. Lower bound for the unrestricted gauge.** For every scalar \(z\in\mathbb C\) or \(\mathbb R\), \(|1-z|\ge1-\min(1,|z|)\). Applying (1) gives
\[
\|\mathbf1_A-\Omega(f)\|_1+s
\ge t+s-sW_0(1/s)-\frac{st}{e}.\tag{2}
\]
Put \(L=\log(1/t)\) and \(s_0=t/L\). The Lambert identity \(W_0(1/s_0)=L\) follows from \(Le^L=L/t\). For \(s\ge s_0\), the objective is at least \(s\ge s_0\). For \(0<s\le s_0\), differentiate the right side of (2):
\[
\frac{d}{ds}\left[t+s-sW_0(1/s)-st/e\right]
=1-\frac{W_0(1/s)^2}{1+W_0(1/s)}-\frac{t}{e}.\tag{3}
\]
When \(t\le t_*=e^{-\varphi}\), one has \(W_0(1/s)\ge L\ge\varphi\), and \(\varphi^2/(1+\varphi)=1\). Therefore (3) is strictly negative, so (2) is smallest at \(s=s_0\), where it equals \(s_0(1-t/e)\). The case \(s=0\) has cost \(t\) and satisfies the same lower bound. This establishes the left inequality over **all** witnesses, including sign-changing and complex ones.

**3. Matching upper bound.** Set \(f=\mathbf1_A/L\). Then \(\|f\|_1=t/L=s_0\) and
\[
\Omega(f)=\frac{\mathbf1_A}{L}\log\frac{1/L}{t/L}=\mathbf1_A.
\]
Thus the residual is zero and \(\rho(\mathbf1_A)\le t/L\). The two-sided estimate immediately gives the claimed uniform limit and relative error.

**4. Exact positive-witness optimization.** Suppose \(f\ge0\), still with \(s=\|f\|_1\). Where \(f\le s\), \(\Omega(f)\le0\), which cannot lower the residual of the positive indicator. The positive part of the elementary envelope satisfies
\[
0\le\min\{1,(u\log(u/s))_+\}\le\min\{1,W_0(1/s)u\}.
\]
Consequently,
\[
\|\mathbf1_A-\Omega(f)\|_1+s\ge s+\max\{0,t-sW_0(1/s)\}.\tag{4}
\]
For \(s\ge s_0\) this is at least \(s_0\), achieved by the full-support witness from step 3. For \(s<s_0\) set \(\delta=sW_0(1/s)<t\). Since \(sW_0(1/s)=e^{-W_0(1/s)}\), we have
\[
s=\frac{\delta}{\log(1/\delta)}.
\]
The lower bound (4) becomes \(t-\delta+\delta/\log(1/\delta)\). Conversely, by atomlessness choose \(E\subseteq A\) of measure \(\delta\) and set \(f=\mathbf1_E/\log(1/\delta)\). Then \(\Omega(f)=\mathbf1_E\), and this expression is attained. Including \(\delta=t\) and the zero witness therefore yields
\[
\rho_+(\mathbf1_A)=\min_{0<\delta\le t}
\left[t-\delta+\frac{\delta}{\log(1/\delta)}\right].\tag{5}
\]
Its derivative with respect to \(\delta\) is \(-1+1/H+1/H^2\), with \(H=\log(1/\delta)\). This changes sign once, from negative to positive, at \(H=\varphi\), or \(\delta=e^{-\varphi}\). Formula (5) and its minimizing witness give the piecewise expression.

## Verification

The analytic proof is self-contained after the explicitly stated centralizer and quotient-gauge definitions. `CHECK.py` independently evaluates the finite-cell objective and the positive-witness candidates, tests random real signed witnesses against the unrestricted lower estimate, and verifies the Lambert envelope on scalar grids. Run with `python CHECK.py` using Python's standard library. These finite tests illustrate, but do not establish, the all-witness inequalities; the infinite-dimensional conclusion follows from steps 1–4.

## Relationship to prior work

Cabello Sánchez, Castillo, Martínez-Bohórquez and Navarro Garmendia (2026), Example 6.1, define exactly this range quotient quasi-gauge and prove the **upper** estimate \(\rho(\mathbf1_A)\le t/\log(1/t)\), and note setwise agreement with \(L\log^{-1}L\). No matching lower constant or positive-witness support transition appears in that inspected example. Equality of underlying function spaces or equivalence of quasi-norms does not imply a leading constant for the particular quotient gauge. Earlier centralizer literature establishes construction and interpolation facts but does not provide this quantitative claim in the material inspected; possible unindexed equivalent calculations remain a bibliographic risk.

## Limitations

The unrestricted gauge is **not** determined exactly at every finite \(t\); its two-sided bound is asserted only for \(t\le t_*\), and its sharp asymptotic is as \(t\downarrow0\). The finite-\(t\) exact classification concerns only **nonnegative real witnesses**, not the full infimum over all real or complex witnesses. Neither uniqueness of witnesses nor any general theorem about other centralizers is claimed. The result uses Lebesgue atomlessness and the normalization of the centralizer; changing the centralizer by a constant factor changes the constants. Potential earlier formulations in the extensive centralizer/Orlicz literature have not been exhaustively excluded.

## References

1. F. Cabello Sánchez, J. M. F. Castillo, R. Martínez-Bohórquez and J. Navarro Garmendia, *The Serre closure of Banach spaces*, arXiv:2610.35259v1 (2026-10-26), especially Example 6.1 and its proof. https://arxiv.org/html/2610.35259v1
2. F. Cabello Sánchez, *Factorization in Lorentz spaces, with an application to centralizers*, Journal of Mathematical Analysis and Applications (2016), DOI: 10.1016/j.jmaa.2016.09.038. The accessible excerpt identifies the logarithmic centralizer; complete article text was not available for comparison.
3. *Group Actions on Twisted Sums of Banach Spaces*, Bulletin of the Malaysian Mathematical Sciences Society (2023), DOI: 10.1007/s40840-023-01531-0, especially Sections 1, 6–7. https://link.springer.com/article/10.1007/s40840-023-01531-0
4. *Nonlinear centralizers with values in \(L_0\)*, Nonlinear Analysis 88 (2013), DOI: 10.1016/j.na.2013.04.006. Only the accessible abstract and introduction were inspected.
