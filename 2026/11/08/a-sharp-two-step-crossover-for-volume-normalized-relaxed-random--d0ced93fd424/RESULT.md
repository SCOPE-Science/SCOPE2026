# A sharp two-step crossover for volume-normalized relaxed random projections

## Finding

Consider a two-row consistent linear system in \(\mathbb R^2\). At each step independently choose either row with probability \(1/2\). Compare ordinary Kaczmarz (unit relaxation on both rows) with the volume-normalized relaxed-uniform rule
\[
\omega_i=1+\sqrt{1-\|a_i\|_2^2/v_{\max}},\qquad v_{\max}=\max_j\|a_j\|_2^2,
\]
introduced for single-row sampling by Entezari, Banerjee and Kalantari (2026). For arbitrary \(0<\tau<1\) and \(0<\rho<1\), take the two rows
\[
a_1=(1,0),\quad a_2=\sqrt{1-\tau^2}\bigl(\rho,\sqrt{1-\rho^2}\bigr),
\]
and right-hand side zero. The relaxed weights are then exactly \(\omega_1=1\) and \(\omega_2=1+\tau\). Set \(s^2=1-\rho^2\), and let \(E_{\rm rel}(e)\), \(E_{\rm unit}(e)\) denote the expected squared errors after **exactly two** independent, uniformly selected row updates from the same initial error \(e\in\mathbb R^2\).

**Theorem (complete strict-benefit phase diagram).** There exists a nonzero initial error \(e\) with \(E_{\rm rel}(e)<E_{\rm unit}(e)\) if and only if
\[
\boxed{\tau^4+\tau(\tau+2)s^2<1.}
\]
When the inequality is reversed or equality holds, \(E_{\rm rel}(e)\ge E_{\rm unit}(e)\) for **every** initial error \(e\). In the strict-benefit phase there are also initial errors for which the relaxed method performs strictly worse. This is a sharp, initial-error-dependent two-step crossover, not a statement about asymptotic convergence rates.

Let \(\tau_0\) be the unique root in \((0,1)\) of \(\tau^4+\tau^2+2\tau-1=0\) (approximately \(0.4046978328\)). For \(0<\tau\le\tau_0\), every nonorthogonal two-row direction with \(0<\rho<1\) admits a strict two-step benefit for some initial error; for \(\tau>\tau_0\), such a benefit is possible precisely when
\[
\rho^2>\frac{\tau^4+\tau^2+2\tau-1}{\tau(\tau+2)}.
\]
The method is nevertheless never better in conditional **one-step** squared error: for every current error \(e\), its one-step expected squared error exceeds the unit-relaxation counterpart by \(\tau^2\|Qe\|_2^2/2\), where \(Q\) projects onto the second row direction.

## Assumptions and scope

All statements are in exact real arithmetic. The two rows are nonzero and linearly independent, since \(0<\rho<1\). Their norm squares are \(1\) and \(1-\tau^2\), hence the displayed weights are those prescribed by the fixed-global-maximum variant of the 2026 volume-normalized rule. The row choices are independent across steps, with replacement and equal probabilities. The system is the homogeneous, consistent system \(Ax=0\); its unique solution is zero. The error \(e\) is deterministic before the two draws. This is the singleton-block case, not a statement about arbitrary block sizes, row distributions, or the online-running-maximum implementation.

## Proof

Write \(u=(1,0)^\mathsf T\), \(v=(\rho,s)^\mathsf T\), where \(s=\sqrt{1-\rho^2}>0\). Let \(P=uu^\mathsf T\), \(Q=vv^\mathsf T\), \(U=I-P\), \(V=I-Q\), and \(W=I-(1+\tau)Q=V-\tau Q\). An unrelaxed step applies either \(U\) or \(V\), whereas a relaxed step applies either \(U\) or \(W\). These operators are symmetric, \(U^2=U\), \(V^2=V\), \(VQ=QV=0\), and \(W^2=V+\tau^2Q\).

For any symmetric pair of step matrices \(U,Z\), averaging the four equally likely length-two words gives
\[
\mathbb E\|e_2\|_2^2=e^\mathsf T B_Ze,\qquad
B_Z=\tfrac14\bigl[U(U^2+Z^2)U+Z(U^2+Z^2)Z\bigr].
\]
Thus \(E_{\rm rel}(e)-E_{\rm unit}(e)=e^\mathsf TDe\) where \(D=B_W-B_V\). Direct substitution, also using \(W^4=V+\tau^4Q\), gives the exact identity
\[
4D=\tau^2(UQU+QUQ)+\tau^4Q-\tau(VUQ+QUV).
\]
This identity can be independently reconstructed without stochastic approximations by enumerating the four row-index words.

Let \(w=(-s,\rho)^\mathsf T\), so \((v,w)\) is an orthonormal basis and \((0,1)^\mathsf T=sv+\rho w\). In this basis,
\[
4D=\begin{pmatrix}
\tau^2s^2(1+s^2)+\tau^4 & \rho s(\tau^2s^2-\tau)\\
\rho s(\tau^2s^2-\tau)&\tau^2s^2\rho^2
\end{pmatrix}.
\]
It follows, with no numerical approximation, that
\[
\operatorname{tr}D=\frac{\tau^2(\tau^2+2s^2)}4>0,
\quad
\det D=\frac{\rho^2s^2\tau^2}{16}\bigl[\tau^4+\tau(\tau+2)s^2-1\bigr].
\]
A real symmetric \(2\times2\) matrix of strictly positive trace has a negative eigenvalue exactly when its determinant is negative. If its determinant is nonnegative, both eigenvalues are nonnegative. In the negative-determinant case both signs occur, giving both strict improvement and strict degradation for suitable nonzero initial errors. This proves the sharp comparison and equality boundary. Moreover \(\tau^4+\tau^2+2\tau-1\) is strictly increasing for positive \(\tau\), negative at zero and positive at one; this proves uniqueness of \(\tau_0\) and the stated phase classification.

Finally, \(\|We\|_2^2=\|Ve\|_2^2+\tau^2\|Qe\|_2^2\), because \(VQ=0\). The first row has identical update in both algorithms. Averaging the two rows yields the one-step difference claimed above.

**Exact rational witness.** Take \(\tau=3/5\), \(\rho=4/5\), \(s=3/5\). The actual two rows are \((1,0)\) and \((16/25,12/25)\). From \(e=(0,1)^\mathsf T\), independently averaging all four length-two row sequences gives
\[
E_{\rm unit}(e)=\frac{1681}{2500},\qquad
E_{\rm rel}(e)=\frac{10297}{15625},\qquad
E_{\rm rel}(e)-E_{\rm unit}(e)=-\frac{837}{62500}<0.
\]
Thus even the same fixed initial error can benefit at horizon two despite the universally unfavorable one-step comparison.

## Verification

Run `python3 verify.py` using Python 3 with its standard library. The script independently constructs the symmetric two-step moment operators by exact rational matrix multiplication, enumerates all four row-update words, and checks the trace/determinant identities for 252 rational parameter triples and the rational witness. It completed successfully with 50,904 exact checks on the supplied version. The infinite-parameter assertions are proved algebraically above; finite test grids alone would not prove them.

## Relationship to prior work

Entezari, Banerjee and Kalantari (2026), arXiv:2610.12346v1, Theorem 2 and §3.3, specify the volume-normalized uniform-sampling relaxation and its one-step contraction bound, while §5 discusses performance over longer horizons. Their article does not give the two-row two-step all-initial-error comparison or the sharp angular threshold above. Marshall and Mickelin (2022/2023) examine optimized learning-rate schedules for noisy randomized Kaczmarz, with a different sampling/noise regime. Dong et al. (2025) study averaging-block extended Bregman-Kaczmarz with relaxation, not this row-norm-fixed, two-step projection comparison. Bai and Wu (2018) examine exact mean-square errors for unrelaxed randomized Kaczmarz; the present operator difference isolates the new relaxation policy.

The one-step identity uses familiar orthogonal-projection geometry. What is additional is the sharp two-step criterion for the precise, newly proposed norm-dependent policy, obtained by retaining noncommutativity of successive projections. No priority claim is made against unindexed equivalent computations or general higher-order moment methods that may subsume this two-dimensional specialization.

## Limitations

This is a two-row, two-dimensional, fixed-global-maximum, equal-probability and two-iteration result. It does not imply improved worst-case performance: indeed, whenever strict benefit is possible, some other initial errors are strictly worse. It does not imply benefits for all initializations, over arbitrary time horizons, or under a running estimate of the maximum row norm. It is not an optimal learning-rate theorem. The comparison is analytic and exact, but historical originality has the residual risk of earlier unindexed equivalent two-step random-projection calculations. Independent mathematical validation has not been performed.

## References

1. A. Entezari, A. Banerjee and L. Kalantari, *Volume Sampling and Spectral Equalization in Randomized Alternating Projections*, arXiv:2610.12346v1, first posted 8 October 2026. https://arxiv.org/html/2610.12346v1
2. N. F. Marshall and O. Mickelin, *An Optimal Scheduled Learning Rate for a Randomized Kaczmarz Algorithm*, arXiv:2202.12224v4 (2022); SIAM Journal on Matrix Analysis and Applications 44 (2023), 312–330. https://arxiv.org/pdf/2202.12224
3. Z. Dong, A. Xiao, G. Yin and J. Yin, *A Relaxed Randomized Averaging Block Extended Bregman-Kaczmarz Method for Combined Optimization Problems*, arXiv:2512.09825v1 (2025). https://arxiv.org/html/2512.09825v1
4. Z.-Z. Bai and W.-T. Wu, *On convergence rate of the randomized Kaczmarz method*, Linear Algebra and its Applications 553 (2018), 252–269. https://doi.org/10.1016/j.laa.2018.05.009
