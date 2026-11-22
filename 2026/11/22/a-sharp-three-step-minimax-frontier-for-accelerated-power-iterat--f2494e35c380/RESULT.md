# A sharp three-step minimax frontier for accelerated power iteration

## Finding
Fix \(0<q<1\). For any real symmetric positive-semidefinite matrix \(A\) with a simple eigenvalue \(1\) and remaining spectrum in \([0,q]\), use the warm-started accelerated power iteration
\[
v_{-1}=v_0,\qquad v_{j+1}=A\big((1+\beta)v_j-\beta v_{j-1}\big),\qquad 0\le\beta\le q,
\]
with a nonzero leading-eigenvector component in \(v_0\). After three matrix multiplications the sharp worst-case tangent-of-angle amplification, over the permissible spectra and starts, is
\[
E_q(\beta)=\max_{0\le t\le q}\left|t^2\big[t-\beta(2+\beta)(1-t)\big]\right|.
\]
Write \(c=\beta(2+\beta)\) and define \(c_{\rm eq}(q)\) as the unique positive solution inside \(\big(0,q/(1-q)\big)\) of
\[
q^2\big[q-(1-q)c\big]=\frac{4c^3}{27(1+c)^2}.
\]
Let \(q_*\in(0,1)\) be the unique root of
\[
q^2+q-1=\frac{4(q+2)^3}{27(1+q)^4},\qquad q_*=0.755526784205864\ldots.
\]
**The unique optimal admissible constant momentum for the third iterate** is
\[
\boxed{\quad
\beta_{\rm min}(q)=\begin{cases}
\sqrt{1+c_{\rm eq}(q)}-1,&0<q\le q_*,\\
q,&q_*\le q<1.
\end{cases}\quad}
\]
The two branches agree at \(q=q_*\), and the sharp minimax value is
\[
\boxed{\quad E_q^{\rm min}=\begin{cases}
\dfrac{4c_{\rm eq}(q)^3}{27(1+c_{\rm eq}(q))^2},&0<q\le q_*,\\
q^3(q^2+q-1),&q_*\le q<1.
\end{cases}\quad}
\]
It is strictly below the three-step ordinary power-method factor \(q^3\) for every \(0<q<1\).

A distinct *endpoint-notch* criterion holds: there is a permissible constant \(\beta\) that completely eliminates an eigenspace at eigenvalue \(q\) after exactly three multiplications if and only if
\[
\boxed{\quad q\le\frac{\sqrt5-1}{2}.\quad}
\]
It is unique and equals \(\beta_{\rm notch}=(1-q)^{-1/2}-1\). At this parameter the three-step polynomial is \(t^2(t-q)/(1-q)\); for a two-level spectrum \(\{1,q\}\), the third iterate is exactly a leading eigenvector, provided its initial coefficient is nonzero. The endpoint-notch choice is **not** the interval-minimax choice: whenever admissible, its sharp interval error is \(4q^3/[27(1-q)]>E_q^{\rm min}\).

## Assumptions and scope
The matrix is real symmetric positive semidefinite, has largest eigenvalue \(1\) of multiplicity one, and its other eigenvalues lie between \(0\) and a specified bound \(q\in(0,1)\). The starting vector has a nonzero leading-eigenvector component. The coefficient \(\beta\) is held fixed throughout all three iterations and belongs to the explicitly chosen closed cap \([0,q]\). The originating paper analyzes the related range \([0,\lambda_2]\) (and its implementation specifies a strict endpoint); an upper bound \(q\) need not equal the actual second eigenvalue. This finite-step theorem does not assume that the original asymptotic parameter guarantees apply when the inequality is strict. The recurrence is considered in exact arithmetic; common rescaling of the two consecutive history vectors leaves the direction of the next iterate unchanged. The minimax criterion is worst-case *projective angle* for all admissible spectra, not asymptotic spectral radius and not the Rayleigh quotient at arbitrary later steps. An actual matrix can have a smaller maximum if its eigenvalues do not include the worst-case subdominant level.

## Proof
**Spectral polynomial.** For an eigenvalue \(t\), let \(p_{-1}(t)=p_0(t)=1\) and \(p_{j+1}(t)=t[(1+\beta)p_j(t)-\beta p_{j-1}(t)]\). Then
\[
p_1(t)=t,\quad p_2(t)=t[t-\beta(1-t)],\quad
p_3(t)=t^2\big[t-(1-t)\beta(2+\beta)\big].
\]
In particular, \(p_3(1)=1\). Orthogonal spectral decomposition gives the stated tangent-of-angle upper bound; equality is attained by a two-eigenvalue diagonal matrix with a nonzero initial vector in both eigenspaces, choosing a maximizing \(t\in[0,q]\). This proves that the scalar interval supremum is the precise universal amplification factor.

**Exact equioscillation.** Put \(c=\beta(2+\beta)\), which increases strictly from \(0\) to \(c_{\max}=q(2+q)\). On \(0\le c\le c_0=q/(1-q)\), the cubic \(p_3(t)=t^2[(1+c)t-c]\) has its negative minimum at \(t_-(c)=2c/[3(1+c)]\), and its positive maximum on \([0,q]\) at \(t=q\). Since \(t_-(c)<q\) in this range, the two positive magnitudes are
\[
N(c)=\frac{4c^3}{27(1+c)^2},\qquad
P(c)=q^2[q-(1-q)c].
\]
Here \(N\) increases strictly and \(P\) decreases strictly; \(P(0)=q^3>N(0)=0\) and \(P(c_0)=0<N(c_0)\). Consequently, there is exactly one \(c_{\rm eq}\in(0,c_0)\) where \(P=N\). For \(c<c_{\rm eq}\), the endpoint \(q\) yields error \(P(c)>P(c_{\rm eq})\). For \(c>c_{\rm eq}\), evaluate the polynomial at the *fixed* interior point \(t_-(c_{\rm eq})\): because \(\partial p_3(t;c)/\partial c=t^2(t-1)<0\), its negative error strictly exceeds \(N(c_{\rm eq})\), even if \(c>c_0\). Hence \(c_{\rm eq}\) is the unique unrestricted nonnegative minimizer and restricting to \([0,c_{\max}]\) gives \(c_{\rm opt}=\min\{c_{\rm eq},c_{\max}\}\).

**The unique cap transition.** If \(q\le(\sqrt5-1)/2\), then \(c_{\max}\ge c_0>c_{\rm eq}\), so the equioscillation point is feasible. Above this golden-ratio bound, \(c_{\max}<c_0\), and the sign of \(P(c_{\max})-N(c_{\max})\) is the sign of
\[
F(q)=q^2+q-1-\frac{4(q+2)^3}{27(1+q)^4}.
\]
The first part of \(F\) strictly increases in \(q\), while the second part strictly decreases (its logarithmic derivative is \(-(q+5)/[(q+2)(q+1)]\)). Hence \(F\) is strictly increasing; it is negative at the golden-ratio bound and positive at \(q=1\), establishing the unique \(q_*\). The explicit minimax branches follow from \(P(c_{\rm eq})=N(c_{\rm eq})\) and \(P(c_{\max})=q^3(q^2+q-1)\). Strict improvement over ordinary power iteration follows because the unique minimizer is positive and the worst-case value initially decreases from \(q^3\); in the cap branch, \(q^2+q-1<1\) for \(q<1\).

**Exact endpoint annihilation.** The only possible positive nonzero zero of \(p_3(t)\) is \(t=c/(1+c)\); placing it at \(t=q\) requires \(c=c_0\) and thus \(\beta=\sqrt{1+c_0}-1=(1-q)^{-1/2}-1\). It satisfies \(\beta\le q\) exactly when \(1\le(1-q)(1+q)^2\), or \(q^2+q\le1\), giving the sharp golden-ratio cutoff. The corresponding polynomial simplifies to \(t^2(t-q)/(1-q)\). Its greatest absolute value on \([0,q]\) occurs at \(t=2q/3\) and equals \(4q^3/[27(1-q)]\). As \(c_0>c_{\rm eq}\), this value is strictly worse than the interval minimax value. There is no admissible exact cancellation at step two: \(p_2(q)=q[q-\beta(1-q)]\ge q^3>0\). Thus three is the earliest possible positive-spectrum cancellation under the stated cap.

## Verification
Run `python verify.py` using only Python's standard library. It verifies the cubic recurrence by exact rational fractions across hundreds of parameter cases; independently computes the interior extrema for rational parameters, checks the equioscillation and cap regime over a broad deterministic grid, evaluates root uniqueness and numerical critical bounds, and checks the endpoint-notch formula, its gold-ratio admissibility cutoff, and the sharp worst-case spectral point. The exact polynomial factorization and calculus/monotonicity argument, rather than finite enumeration, establish the universal statements.

Representative spectra with \(q=1/2\) have \(\beta_{\rm min}\approx0.3448025781\), whereas the exactly notching parameter is \(\beta_{\rm notch}=\sqrt2-1\approx0.4142135624\). The minimum worst-case third-step amplification is approximately \(0.02393825324\), compared with \(0.125\) for three ordinary power steps. At \(q=4/5\), the cap is active, \(\beta_{\rm min}=4/5\), and the exact amplification is \(0.22528\), compared with \(0.512\) for ordinary power iteration.

## Relationship to prior work
R. Tappenden's *An Accelerated Power Method* (2026) provides exactly the stated warm-started recurrence, common normalization rule, admissible momentum interval, and an optimal *asymptotic* spectral rate. Its Section 3 and finite experiments analyze the augmented-matrix eigenvalues, not the sharp three-step interval minimax choice or the distinct finite-time spectral notch. The optimal asymptotic tuning and the finite-time minimax tuning solve different objectives. The latter is not a re-expression of the spectral-radius formula because eigenmode cancellation depends on the initialized recurrence polynomial.

Xu, He, De Sa, Mitliagkas and Ré (2018) analyze a different momentum power recurrence with a momentum term outside the matrix multiplication, with Chebyshev-polynomial and stochastic-variance analysis. Their asymptotic rate guarantees do not supply the present minimax law for momentum *inside* the multiplication with identical two-step initialization.

Classical Chebyshev polynomial minimax approximation permits arbitrary degree-three coefficients and therefore addresses a larger filter-design class; its existence does not identify the optimal \(\beta\) inside this one-parameter, constant-momentum iteration with the explicitly imposed closed cap. Closely related published exact results address a differently normalized two-sweep parameterized power method, or coefficient-capped Anderson extrapolation of scalar fixed-point maps; neither gives the stated cubic spectral filter for this recurrence. The comparison does not rule out unindexed independent derivations of the same special-purpose minimax formula.

## Limitations
The result assumes known spectral upper bound \(q\) and the chosen closed cap \(\beta\in[0,q]\), which can extend beyond the actual second eigenvalue when the bound is loose; a positive-semidefinite matrix with a simple normalized top eigenvalue, one common fixed momentum parameter, and exactly three matrix multiplications. It does not provide an implementable estimator of \(q\), finite-precision or noisy-matrix guarantees, an optimal schedule of varying momentum coefficients, general indefinite-matrix conclusions, or an all-horizon acceleration theorem. Sharpness is universal over matrices with remaining eigenvalues *within* \([0,q]\), not a statement that every matrix in that class attains the bound. The presence of any additional eigenvalue between zero and \(q\) generally prevents exact endpoint-notch termination.

## References
- R. Tappenden, *An Accelerated Power Method*, arXiv:2611.13283v1 (first public 2026-11-09), https://arxiv.org/html/2611.13283v1.
- P. Xu, B. He, C. De Sa, I. Mitliagkas and C. Ré, *Accelerated Stochastic Power Iteration*, AISTATS/PMLR 84 (2018), arXiv:1707.02670, https://arxiv.org/abs/1707.02670.
- T. Sun, X. Peng, J. Zhang and S. Vong, *A Gaussian Process Regression-Enhanced Two-Sweep Parameterized Power Method for Computing Extreme Eigenpairs*, arXiv:2610.41627 (2026), https://arxiv.org/abs/2610.41627.
