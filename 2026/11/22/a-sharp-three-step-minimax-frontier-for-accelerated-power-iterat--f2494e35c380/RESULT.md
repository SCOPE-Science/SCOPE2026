# A sharp three-step minimax frontier for accelerated power iteration

## Finding

Let \(0<q<1\). Let \(A\) be a real symmetric positive-semidefinite matrix with a simple eigenvalue \(1\) and all other eigenvalues in \([0,q]\). Start with a vector \(v_0\) having a nonzero leading-eigenvector component and use
\[
v_{-1}=v_0,\qquad v_{j+1}=A\big((1+\beta)v_j-\beta v_{j-1}\big),\qquad 0\le\beta\le q,
\]
with the same \(\beta\) throughout. After three matrix multiplications the sharp worst-case tangent-of-angle amplification over these spectra and starts with nonzero initial angle is
\[
E_q(\beta)=\max_{0\le t\le q}\left|t^2\big[t-\beta(2+\beta)(1-t)\big]\right|.
\]
Let \(c_{\rm eq}(q)\) be the unique solution in \((0,q/(1-q))\) of
\[
q^2\big[q-(1-q)c\big]=\frac{4c^3}{27(1+c)^2}.
\]
Let \(q_*\in(0,1)\) be the unique solution of
\[
q^2+q-1=\frac{4(q+2)^3}{27(1+q)^4},\qquad q_*=0.755526784205864\ldots.
\]
The unique optimal admissible constant momentum and its sharp minimax error are
\[
\beta_{\min}(q)=\begin{cases}
\sqrt{1+c_{\rm eq}(q)}-1,&q\le q_*,\\
q,&q\ge q_*,
\end{cases}
\qquad
E_q^{\min}=\begin{cases}
\dfrac{4c_{\rm eq}(q)^3}{27(1+c_{\rm eq}(q))^2},&q\le q_*,\\
q^3(q^2+q-1),&q\ge q_*.
\end{cases}
\]
The branches agree at \(q_*\), and \(E_q^{\min}<q^3\) for every \(0<q<1\).

The endpoint eigenvalue **\(t=q\)** can be annulled after exactly three multiplications by an admissible momentum if and only if \(q\le(\sqrt5-1)/2\). The unique such momentum is \(\beta_{\rm notch}=(1-q)^{-1/2}-1\). At this parameter the polynomial is \(t^2(t-q)/(1-q)\), so for a two-level spectrum \(\{1,q\}\), the third iterate is exactly a leading eigenvector. The sharp worst-case interval error for the notch is \(4q^3/[27(1-q)]>E_q^{\min}\). Whenever the endpoint notch is admissible, step three is its earliest possible occurrence. This last statement concerns the endpoint, not an interior subdominant eigenvalue.

## Assumptions and scope

The angle is the acute angle with the leading eigenspace. The recurrence is in exact arithmetic; a common rescaling of the two history vectors preserves the direction of the next iterate. The cap is the specified closed interval \([0,q]\), where \(q\) may be a loose bound rather than the actual second eigenvalue. The objective is a worst-case finite-horizon projective angle, not asymptotic rate, an optimal schedule of varying momentum, or optimality among arbitrary cubic spectral filters.

## Proof

**Sharp spectral reduction.** The scalar coefficients satisfy \(p_{-1}=p_0=1\) and \(p_{j+1}(t)=t[(1+\beta)p_j(t)-\beta p_{j-1}(t)]\). Direct substitution gives
\[
p_1(t)=t,\qquad p_2(t)=t[t-\beta(1-t)],\qquad
p_3(t)=t^2[t-\beta(2+\beta)(1-t)].
\]
Since \(p_3(1)=1\), the leading component stays fixed and the orthogonal component contracts by at most \(\max_{[0,q]}|p_3|\). Equality in the tangent amplification is attained for \(A=\operatorname{diag}(1,t)\) at a maximizing \(t\), with both initial components nonzero. A start already in the leading eigenspace remains there.

**Exact equioscillation.** Put \(c=\beta(2+\beta)\), an increasing function of \(\beta\) with admissible cap \(c_{\max}=q(q+2)\). Write \(c_0=q/(1-q)\). For \(0<c\le c_0\), \(p_3(t)=t^2[(1+c)t-c]\) has its negative minimum at \(t_-(c)=2c/[3(1+c)]<q\), and its maximum on \([0,q]\) at \(q\). The two magnitudes are
\[
N(c)=\frac{4c^3}{27(1+c)^2},\qquad P(c)=q^2[q-(1-q)c].
\]
The same formula \(\max(N,P)\) for the worst error includes \(c=0\). On \([0,c_0]\), \(N\) is strictly increasing, \(P\) strictly decreasing, and their difference changes sign between the endpoints. Their unique crossing is \(c_{\rm eq}\). The error strictly decreases up to the crossing, where it equals \(N(c_{\rm eq})\). For any \(c>c_{\rm eq}\), even beyond \(c_0\), evaluate the polynomial at the fixed interior point \(t_-(c_{\rm eq})\): the derivative with respect to \(c\) at that point is \(-t^2(1-t)<0\), so the error there is strictly larger than \(N(c_{\rm eq})\). Thus \(c_{\rm opt}=\min(c_{\rm eq},c_{\max})\) is the unique constrained optimizer. It is positive, and the initial strict decrease gives \(E_q^{\min}<E_q(0)=q^3\).

**Cap transition.** If \(q\le(\sqrt5-1)/2\), then \(c_{\max}\ge c_0>c_{\rm eq}\). Otherwise \(c_{\max}<c_0\) and \((P(c_{\max})-N(c_{\max}))/q^3\) equals
\[
F(q)=q^2+q-1-\frac{4(q+2)^3}{27(1+q)^4}.
\]
The polynomial part strictly increases on \((0,1)\); the positive term being subtracted strictly decreases, with logarithmic derivative \(-(q+5)/[(q+2)(q+1)]\). The sign is negative at \((\sqrt5-1)/2\) and positive at \(1\). Thus there is a unique crossing \(q_*\), and the optimizer and error have the stated branches.

**Endpoint annihilation.** The condition \(p_3(q)=0\) requires \(c=c_0\), or \(\beta=(1-q)^{-1/2}-1\). This momentum meets the cap if and only if \((1-q)(1+q)^2\ge1\), equivalent to \(q^2+q\le1\). At the notch, \(p_3(t)=t^2(t-q)/(1-q)\) and its largest absolute value on the interval occurs at \(2q/3\). That error exceeds the minimax value because \(c_0>c_{\rm eq}\). There is no endpoint cancellation at steps one or two: \(p_1(q)=q>0\) and \(p_2(q)=q[q-\beta(1-q)]\ge q^3>0\). By contrast, for every \(0<\beta\le q\) the positive root \(t=\beta/(1+\beta)\) of \(p_2\) lies strictly inside \((0,q)\). Step-two cancellation of such an interior eigenmode is possible; it is not endpoint notching.

## Verification

The companion `verify.py` in the source package (unchanged) checks the scalar and diagonal matrix recurrences using rational arithmetic, computes candidate extrema, and checks the transition and endpoint notch numerically. Run it with Python 3 from that package. The exact proof above supplies the continuous parameter statements. As an exact check of the endpoint/interior distinction, for \(q=\beta=1/2\), \(p_2(1/3)=0\) but \(p_2(1/2)=1/8\). At \(q=1/2\), \(\beta_{\min}\approx0.3448025781\) and \(E_q^{\min}\approx0.02393825324\); at \(q=4/5\) the cap is active and \(E_q^{\min}=0.22528\).

## Relationship to prior work and limitations

Tappenden, *An Accelerated Power Method*, [arXiv:2611.13283v1](https://arxiv.org/html/2611.13283v1), §2 Definition 1 and Eq. (14), supplies the warm-started recurrence, with the momentum range related to the actual second eigenvalue. Its implementation uses a strict endpoint, and §3.1.1 gives an optimal **asymptotic** rate. Neither the rate nor its parameter selection gives the finite three-step interval tuning. The theorem here studies its explicitly stated closed cap and does not extend the paper's asymptotic guarantees to a loose bound \(q\).

Xu, He, De Sa, Mitliagkas and Ré, *Accelerated Stochastic Power Iteration*, [arXiv:1707.02670](https://arxiv.org/abs/1707.02670), put momentum outside the matrix multiplication. Sun, Peng, Zhang and Vong, *A Gaussian Process Regression-Enhanced Two-Sweep Parameterized Power Method for Computing Extreme Eigenpairs*, [arXiv:2610.41627](https://arxiv.org/abs/2610.41627), study a differently normalized two-sweep iteration. Classical polynomial minimax theory gives general alternation principles, but the filter, its feasible cap and the notch must be analyzed for the particular recurrence.

The result does not assert optimality at other horizons, finite-precision behavior, performance for indefinite matrices, or worst-case attainment by every individual matrix. The endpoint notch generally does not annihilate other interior eigenvalues. The source comparison does not exclude an unindexed equivalent derivation.
