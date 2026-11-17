# A sharp two-parameter amplitude cap at the tangential flip of the reduced Chialvo neuron map

## Finding
For the reduced Chialvo map
\[
f_{r,k}(x)=x^2 e^{r-x}+k,\qquad x\ge0,\quad r\in\mathbb R,\ k\ge0,
\]
put
\[
q=2+\sqrt2,\qquad r_c=q-\log\bigl(2+2\sqrt2\bigr).
\]
There is a neighborhood of \((r_c,1,q)\) in parameter-state space in which a distinguished fixed point \(p(r,k)\) and an analytic squared half-gap \(U(r,k)\) are uniquely defined. A **distinct real prime-two orbit sufficiently close to \(q\)** exists exactly when \(U(r,k)>0\), in which case it is unique locally, positive and attracting, with states \(m(r,k)\pm\sqrt{U(r,k)}\). The fixed point is attracting when \(U<0\), repelling when \(U>0\), and neutral at \(U=0\). At the tangency,
\[
U(r,k)=3q(r-r_c)-\frac34(k-1)^2
 +O\left((r-r_c)^2+|r-r_c|\,|k-1|+|k-1|^3\right).
\]
In particular, for sufficiently small \(\delta>0\), the bias sweep \(r=r_c+\delta\) has precisely two local flip boundaries
\[
k_\pm(\delta)=1\pm2\sqrt{q\delta}+O(\delta),
\]
and the nearby attracting two-cycle exists exactly between them. For every fixed \(t\) with \(|t|<2\sqrt q\), along \(k=1+t\sqrt\delta\), its half-amplitude \(A\) and mean \(m\) obey
\[
\frac{A^2}{\delta}\longrightarrow 3q-\frac34 t^2,\qquad
\frac{m-p(r,k)}{\delta^{3/2}}\longrightarrow
\frac{t}{4q}\left(3q-\frac34t^2\right).
\]
The limits are uniform for \(t\) in compact subintervals of \((-2\sqrt q,2\sqrt q)\). For fixed \(t\) strictly outside this closed interval, the nearby fixed point is attracting and no nearby distinct prime-two cycle exists at sufficiently small \(\delta\). At \((r,k)=(r_c,1)\), every sufficiently close nonfixed real orbit satisfies the **sharp critical slowing law**
\[
\lim_{n\to\infty}n\bigl(x_n-q\bigr)^2=\frac{3q}{2}.
\]
All statements are local in state space; they do not classify distant periodic orbits or basins.

## Assumptions and scope
Time is discrete, \(x_{n+1}=f_{r,k}(x_n)\). The parameter \(r\) is real and the constant additive input \(k\) is nonnegative. Conclusions concern a sufficiently small but fixed neighborhood of the distinguished point \((r_c,1,q)\); the critical slowing law assumes a sufficiently small nonzero initial displacement. A prime-two orbit consists of two distinct real points interchanged by \(f_{r,k}\). Its mean is \(m=(x_++x_-)/2\), half-gap \(A=(x_+-x_-)/2>0\), and squared half-gap \(U=A^2\). The fixed point \(p(r,k)\) is the unique fixed point in that local neighborhood. No global attraction, physiological parameter calibration, or inference for the full two-variable neuron system is claimed.

## Proof
**1. A distinguished tangential flip.** On a fixed point \(p\), use \(p-k=p^2e^{r-p}\). The multiplier is \(\mu=(p-k)(2-p)/p\). Setting \(\mu=-1\) gives the exact flip curve parameterized by \(z>3\):
\[
k(z)=\frac{z(z-3)}{z-2},\qquad r(z)=z-\log[z(z-2)].
\]
Its derivatives are
\[
k'(z)=\frac{z^2-4z+6}{(z-2)^2}>0,\qquad
r'(z)=\frac{z^2-4z+2}{z(z-2)}.
\]
The unique minimum of \(r(z)\) on \(z>3\) is attained at \(z=q=2+\sqrt2\), where \(k(q)=1\). Thus \(r_c=r(q)\); furthermore \(d^2r/dk^2=1/(2q)\) at \(k=1\). For every sufficiently small positive \(\delta\), the horizontal line \(r=r_c+\delta\) intersects the flip curve twice at the stated \(k_\pm\), by Taylor expansion and strict monotonicity on either side.

**2. Symmetric two-cycle equations and local uniqueness.** Introduce \(m=(x_++x_-)/2\) and \(u=A^2\). Analytically extend to signed small \(u\) the even Taylor series
\[
H_1(m,u;r,k)=f(m)+\frac{u}{2!}f''(m)+\frac{u^2}{4!}f^{(4)}(m)+\cdots-m,
\]
\[
H_2(m,u;r,k)=f'(m)+\frac{u}{3!}f^{(3)}(m)+\frac{u^2}{5!}f^{(5)}(m)+\cdots+1.
\]
For \(u>0\), the equations \(H_1=H_2=0\) are equivalent to \(f(m+A)=m-A\) and \(f(m-A)=m+A\), using their sum and difference divided by \(2A\). At \((m,u,r,k)=(q,0,r_c,1)\), direct differentiation gives
\[
f(q)=q,\quad f'(q)=-1,\quad f''(q)=0,\quad f'''(q)=\frac2q.
\]
Hence the Jacobian \(D_{(m,u)}(H_1,H_2)\) is diagonal with entries \(-2\) and \(1/(3q)\), both nonzero. The analytic implicit-function theorem produces unique analytic \(m(r,k),U(r,k)\) in a neighborhood. The fixed point \(p(r,k)\) is separately analytic because \(f'(q)-1=-2\). The surface \(U=0\) is precisely the local flip curve.

**3. Exact coefficients and profile.** Implicit differentiation at the distinguished point gives
\[
m_k=\tfrac12,\quad U_k=0,\quad U_r=3q,\quad U_{kk}=-\tfrac32.
\]
For the second derivative, \(f''(q)=0\) and \(m_k=1/2\) leave \(f'''(q)m_k^2+(f'''(q)/6)U_{kk}=0\), yielding \(U_{kk}=-3/2\). Taylor's theorem gives the expansion of \(U\). Under \(r=r_c+\delta\), \(k=1+t\sqrt\delta\), this becomes \(U/\delta\to3q-3t^2/4\), uniformly away from the edge values. Moreover, subtracting the fixed point equation from \(H_1=0\) gives, when \(U=O(\delta)\),
\[
m-p=\frac14 f''(p)U+O(\delta^2),
\]
while \(f''(p)=(k-1)/q+O(\delta)\); this proves the asserted suppressed mean-shift coefficient. At \(t=0\), the mean shift is \(O(\delta^2)\), rather than the generic \(O(\delta)\).

**4. Stability and exhaustion.** The implicit-function uniqueness shows no other sufficiently nearby prime-two orbit exists. Along \(U=0\), \(\mu=-1\). Near the distinguished point the flip's cubic saturation is \(f'''/6+(f''/2)^2>0\), since its limiting value is \(1/(3q)\). Standard composition of the two Taylor series (or direct differentiation of the two-cycle multiplier) gives that the nontrivial orbit has return multiplier less than one and greater than minus one for all small \(U>0\); the fixed-point multiplier is in \((-1,1)\) for \(U<0\), and is below \(-1\) for \(U>0\). Thus the cycle is locally attracting exactly inside the bubble and the fixed point is attracting on the other side. In the neighboring parameter domain \(k>0\), both cycle points remain positive.

**5. Critical relaxation.** At \((r_c,1)\), writing \(z=x-q\),
\[
f(q+z)-q=-z+\frac{z^3}{3q}+O(z^4),\qquad
f^2(q+z)-q=z-\frac{2z^3}{3q}+O(z^4).
\]
For sufficiently small nonzero \(z\), the even iterates preserve sign and their absolute values decrease toward zero. Their reciprocal-square increments tend to \(4/(3q)\), so \(n(x_n-q)^2\to3q/2\) for the full iteration index \(n\); the interlaced odd subsequence has the same limit.

## Verification
The accompanying standalone Python checker uses exact symbolic algebra to verify 12 derivative/identity statements, numerically solves nine nearby two-cycle systems at three different detunings and three scaled bias values, checks residuals and return multipliers, verifies the leading amplitude and mean-center profiles, and tests the critical relaxation over 80,000 iterations. Its observed completion message is `CHIALVO_TANGENTIAL_FLIP_CHECK_OK exact_identities=12 cycle_cases=9 relaxation_steps=80000`. Numerics corroborate but do not replace the analytic implicit-function and asymptotic proofs. Reproduce with `python check_chialvo.py` in an environment with SymPy, NumPy, and SciPy.

## Relationship to prior work
Llovera Trujillo, Signerska-Rynkowska, and Bartłomiejczyk (arXiv:2111.14499, version 3, Sections 2.1 and 4) establish the map's exact flip locus, supercriticality for a recovery-parameter sweep, and the general S-unimodal structure. **The flip locus and generic local existence on its supercritical side are prior results and are not claimed as new.** The quantitative addition here is the two-parameter **squared-amplitude cap with its exact coefficients**, the leading suppression and scaled profile of the cycle's mean, and the explicit critical relaxation constant at the minimum of the flip locus. Martin, Tang, and Chialvo (arXiv:2505.24673, Sections II–III and Appendix) give generic finite-time scaling and analyze the zero-bias reduced model; their Chialvo calculation is at a different flip point and does not provide the nonzero-bias two-parameter amplitude cap.

## Limitations
This is a local asymptotic theorem, not a global parameter diagram, a physical calibration, a description of the full slow–fast model, or a statement about stochastic forcing. The qualitative two-boundary tongue follows from the previously published parametric flip locus; novelty concerns the additional concrete two-parameter amplitudes, mean-centering and critical coefficient. Classical flip-normal-form theory supplies the general mechanism, and the possibility of equivalent specialized asymptotics in unindexed literature cannot be excluded. No independent mathematical audit has been performed.

## References
1. F. Llovera Trujillo, J. Signerska-Rynkowska, P. Bartłomiejczyk, *Periodic and chaotic dynamics in a map-based neuron model*, first public 2021-11-29, arXiv:2111.14499, https://arxiv.org/abs/2111.14499 (full HTML version 3: https://arxiv.org/html/2111.14499v3).
2. D. A. Martin, Q.-Y. Tang, D. R. Chialvo, *Finite-time scaling on low-dimensional map bifurcations*, arXiv:2505.24673, https://arxiv.org/abs/2505.24673 (relevant later supporting literature).
3. D. R. Chialvo, *Generic excitable dynamics on a two-dimensional map*, Chaos, Solitons & Fractals 5 (1995), 461–479, https://doi.org/10.1016/0960-0779(93)E0056-H (original model background).
