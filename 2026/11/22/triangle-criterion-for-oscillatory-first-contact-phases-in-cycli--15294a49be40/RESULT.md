# Triangle criterion for oscillatory first-contact phases in cyclic switching diffusion

## Finding

Consider a particle with three strictly positive diffusivities \(D_1,D_2,D_3\) and an independent, directed three-state mobility cycle at common rate \(\gamma>0\). The observable is the probability of each mobility state at the particle's **first contact** with an absorbing endpoint, as a function of initial distance \(x>0\). Each state-resolved first-contact probability approaches the mobility-size-biased law \(\rho_j=D_j/(D_1+D_2+D_3)\).

**Sharp geometric classification.** For every ordered pair of initial/arrival mobility states \(i,j\), the difference between the first-contact probability and \(\rho_j\) has infinitely many strictly alternating sign intervals as \(x\) increases **if and only if** the three positive numbers \(D_1^{-1/2},D_2^{-1/2},D_3^{-1/2}\) are side lengths of a nondegenerate Euclidean triangle. Exactly on or outside its degenerate-triangle boundary, each of the nine differences has at most one positive zero. Thus the criterion is independent of the overall switching rate, even though the oscillation spacing depends on that rate.

Let \(a_i=\gamma/D_i\), \(S=a_1+a_2+a_3\), \(P=a_1a_2+a_2a_3+a_3a_1\), and \(\Delta=S^2-4P\). In the oscillatory regime \(\Delta<0\), the consecutive zeros of every deviation are exactly separated by
\[
\Lambda=\frac{\pi}{v},\qquad v=\sqrt{\frac{\sqrt P-S/2}{2}}>0,
\]
with exponential envelope \(e^{-ux}\), where \(u=\sqrt{(\sqrt P+S/2)/2}\). All nine deviations are nonidentically zero.

A useful one-defect specialization is \(D_1=D_2=D\) and \(c=D/D_3>0\). Infinite alternating first-contact phase preferences occur precisely for \(0<c<4\), equivalently \(D_3>D/4\). At \(c\ge4\), every deviation has at most one positive zero. The inverse-distance oscillation frequency is
\[
v^2=\frac{\gamma}{2D}\left(\sqrt{1+2c}-1-\frac c2\right),
\]
which has a **unique maximum at \(c=3/2\)**, with \(v_{\max}=\sqrt{\gamma/(8D)}\). Approaching the finite threshold from below, the exact consecutive-zero spacing diverges as
\[
\Lambda\sim 2\pi\sqrt{\frac{3D}{\gamma}}\,(4-c)^{-1/2}.
\]
These are statements about the first-hit *internal-state mark*; ordinary unmarked Brownian first-passage probabilities do not express them.

## Assumptions and scope

Fix \(D_1,D_2,D_3>0\), \(\gamma>0\), and \(x>0\). Let \(J_t\) be a continuous-time Markov chain cycling \(1\to2\to3\to1\), every transition at rate \(\gamma\), and let \(W_t\) be a standard Brownian motion independent of \(J\). Starting from \((X_0,J_0)=(x,i)\), define
\[
dX_t=\sqrt{2D_{J_t}}\,dW_t,\qquad \tau=\inf\{t\ge0:X_t=0\},\qquad H_{ij}(x)=\Pr_{x,i}(J_\tau=j).
\]
The process is defined on the full half-line until absorption, with no position reset or drift. The strictly positive diffusivity and common-rate assumptions are essential to the stated triangle characterization. The time-changed-Brownian representation and \(\int_0^tD_{J_s}\,ds\ge t\min_i D_i\) establish \(\tau<\infty\) almost surely for every fixed starting state and distance.

## Proof

**1. Backward system and limiting arrival law.** The first-contact matrix has boundary value \(H(0)=I_3\), is bounded between zero and one entrywise, and satisfies on \(x>0\)
\[
\mathcal D H''(x)+QH(x)=0,\qquad
\mathcal D=\operatorname{diag}(D_1,D_2,D_3),\qquad
Q=\gamma\begin{pmatrix}-1&1&0\\0&-1&1\\1&0&-1\end{pmatrix}.
\]
Set \(L=-\mathcal D^{-1}Q\). The constant right eigenvector is \(\mathbf1=(1,1,1)^T\); a normalized left eigenvector is \(\rho^T=(D_1,D_2,D_3)/(D_1+D_2+D_3)\). Thus \(\Pi=\mathbf1\rho^T\) is the rank-one zero-eigenspace projector, and \(R=I_3-\Pi\) is the transient projector. By the martingale stopping argument or the bounded uniqueness principle for the absorbing Markov diffusion, the solution is the bounded decaying branch of the matrix square-root equation, \(H(x)=\exp(-x\sqrt L)\). This matrix representation is a **known general first-passage method**, not claimed here as novel; the new content is the complete spatial sign and threshold classification derived from its cyclic specialization.

**2. Three-state spectral structure.** A direct determinant expansion gives
\[
\det(zI_3-L)=z(z^2-Sz+P),\qquad
\Delta=S^2-4P.
\]
The zero eigenvalue is simple; \(P,S>0\) imply that the two nonzero eigenvalues have strictly positive real parts. On the transient subspace, \(L\) satisfies \(L^2-SL+P I=0\), where \(I\) denotes identity restricted to that subspace. Put \(m=S/2\) and \(u=\sqrt{(\sqrt P+m)/2}>0\). The polynomial identity on this subspace gives the explicit principal root
\[
\sqrt L=uR+\frac{L-mR}{2u}.
\]
Indeed, squaring yields \(L\), since \((L-mR)^2=(m^2-P)R\). The nonzero root eigenvalues have strictly positive real parts, fixing the decaying branch.

**3. Sign-crossover theorem.** For \(\Delta<0\), write \(v=\sqrt{(\sqrt P-m)/2}>0\) and \(K=(L-mR)/(2uv)\). Then \(K^2=-R\), \(\Pi K=K\Pi=0\), and
\[
H(x)-\Pi=e^{-ux}\{R\cos(vx)-K\sin(vx)\}.
\]
Each \(R_{ij}=\delta_{ij}-\rho_j\) is nonzero, since every \(\rho_j\) lies strictly between zero and one. Hence each matrix entry is a nontrivial damped sinusoid with exactly one simple root per interval of length \(\pi/v\) and with alternating signs between roots. Its positive zero set is an arithmetic progression with step \(\pi/v\), after discarding nonpositive roots.

For \(\Delta>0\), the nonzero eigenvalues \(\mu_\pm=(S\pm\sqrt\Delta)/2\) are real and positive, and each entry of \(H-\Pi\) is a linear combination of \(e^{-\sqrt{\mu_+}x}\) and \(e^{-\sqrt{\mu_-}x}\). Dividing by either positive exponential reduces its zeros to a single monotonic exponential equation, so at most one positive zero exists. At \(\Delta=0\), the repeated transient eigenvalue has at most a size-two Jordan block, and every entry is \((A+Bx)e^{-\sqrt{S/2}x}\), again with at most one positive zero. This exhausts all strictly positive diffusivity triples.

**4. Triangle equivalence.** Write \(s_i=\sqrt{a_i}=\sqrt\gamma/\sqrt{D_i}\). Then
\[
\Delta=s_1^4+s_2^4+s_3^4-2s_1^2s_2^2-2s_2^2s_3^2-2s_3^2s_1^2
=[s_3^2-(s_1+s_2)^2][s_3^2-(s_1-s_2)^2].
\]
Thus \(\Delta<0\) if and only if \(|s_1-s_2|<s_3<s_1+s_2\), exactly the strict triangle inequalities, and \(\Delta=0\) exactly on the degenerate-triangle boundary. Multiplication by \(\sqrt\gamma\) cancels in these inequalities.

**5. One-defect cutoff and optimal frequency.** When \(D_1=D_2=D\) and \(c=D/D_3\), write \(a=\gamma/D\). Then \(S=a(2+c)\), \(P=a^2(1+2c)\), and \(\Delta=a^2c(c-4)\). In the open oscillatory interval, \(v^2=(a/2)(\sqrt{1+2c}-1-c/2)\). Its derivative is \((a/2)[(1+2c)^{-1/2}-1/2]\); its sign changes uniquely from positive to negative at \(c=3/2\). There \(v^2=a/8\). For \(c\uparrow4\), a Taylor expansion yields \(v^2\sim a(4-c)/12\), hence the stated spacing asymptotic.

## Verification

The accompanying standalone `verify.py` constructs the same hitting matrix by two independent calculations: an eigendecomposed matrix square root and a finite-difference solution of the absorbing three-phase backward boundary-value problem. It also verifies boundary normalization, the limiting arrival proportions, every phase-entry zero progression on selected oscillatory triples, the characteristic polynomial, the exact symmetric-diffusivity diagonal formula, and the one-defect frequency maximum. It reports the exact number of successfully evaluated deterministic comparisons. These checks are finite arithmetic corroboration only; global thresholds, positivity, and infinitely many zeros are established by the analytic proof above.

For the equal-diffusivity example \(D_1=D_2=D_3=D\), the position process itself is ordinary Brownian motion. Yet a particle initially in state one has
\[
H_{11}(x)=\frac13+\frac23 e^{-ux}\cos(vx),\quad
v=\sqrt{\frac\gamma{2D}\left(\sqrt3-\frac32\right)}>0,\quad
u=\sqrt{\frac\gamma{2D}\left(\sqrt3+\frac32\right)}.
\]
Thus the hidden contact-state preference reverses forever as distance grows even though unmarked position dynamics remain Gaussian. The formula is also reproduced independently by Fourier decomposition of the autonomous three-cycle at the Brownian hitting-time Laplace transform.

## Relationship to prior work

Grebenkov (2018/2019), *A unifying approach to first-passage time distributions in diffusing diffusivity and switching diffusion models*, gives general switching-diffusivity first-passage *time* distributions using integrated diffusivity. Breuer (2012), *Occupation times for Markov-modulated Brownian motion*, derives the general matrix-valued first-passage phase transform \(e^{U x}\) for Markov-modulated Brownian motion; that foundational exact matrix formula **already contains the present observable**. Accordingly, the generic first-arrival phase transform and the matrix-exponential solution are credited to prior work and not presented as new. The narrower independently derived contribution here is a complete **sign-change regime theorem** for cyclic three-state first-contact phase deviations, an equivalent inverse-square-root-diffusivity triangle criterion, the exact spacing law and the sharp one-defect boundary/maximum frequency. Guéneau and Touzo (2024) consider exit probabilities in switching/diffusing-diffusivity systems, providing further context. The exact triangle/nontriangle spatial sign classification was not located in the inspected sources; availability of the general matrix formula makes independent priority review important.

## Limitations

The result is for drift-free half-line first passage, strictly positive diffusivities and a directed cycle with equal transition rates. It does not classify arbitrary three-state Markov generators, finite intervals, position-dependent switching, different transition rates, or general reaction kernels. Its \(\rho\) is the **first-hit phase** law at large initial distance, not the stationary time-occupation law of \(J\), which is uniform. Infinite sign reversals have exponentially decaying magnitudes and can be experimentally difficult to detect. Exact matrix-valued first-passage methods are established prior art, so the sign-classification priority is not independently certified. No computational experiment is offered as proof of an infinite family.

## References

1. D. S. Grebenkov, *A unifying approach to first-passage time distributions in diffusing diffusivity and switching diffusion models*, arXiv:1812.07249 (first public 2018-12-18), https://arxiv.org/abs/1812.07249.
2. L. Breuer, *Occupation times for Markov-modulated Brownian motion*, J. Appl. Prob. 49 (2012), 549–565, doi:10.1239/jap/1339878804, https://doi.org/10.1239/jap/1339878804.
3. M. Guéneau and L. Touzo, *Siegmund duality for physicists*, arXiv:2404.10537 (first public 2024-04-16), https://arxiv.org/abs/2404.10537.
