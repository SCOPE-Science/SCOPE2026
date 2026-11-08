# The missing algebraic factor in the quasistatic viscoelastic-reset tail

## Finding
For the strongly viscoelastic, quasistatic stationary Gaussian-mixture approximation of Santra and Das [1,2], the apparent Gaussian far tail has a necessary, reset-rate-dependent algebraic factor. For each fixed \(r>0\), put
\[S=(2r+1)/r,\qquad C=\frac{\Gamma(r+1)}{\sqrt{2\pi S}}\left(\frac{(2r+1)^2}{r(r+1)}\right)^r.\]
Then
\[p_r(x)=C|x|^{-2r}e^{-x^2/(2S)}\left(1-\frac{(2r+1)^3}{2(r+1)x^2}+O_r(|x|^{-4})\right).\]
The first factor shows that the source's Gaussian-only expression does not give an asymptotic equivalent; its ratio to the actual tail diverges as a power. The exact rare-excursion rate is therefore different even though the leading quadratic logarithmic rate is the same. For independent stationary samples, the correction shifts the maximum's squared centering by \(-(r+1/2)\log\log N\), rather than the usual Gaussian \(-\tfrac12\log\log N\).

## Assumptions and scope
Take the normalized strong-memory quasistatic density defined by the **specific exact integral within the approximation** of [1,2], not the stationary density at any fixed finite bath friction:
\[p_r(x)=r\int_0^\infty e^{-rt}\frac{e^{-x^2/[2V(t)]}}{\sqrt{2\pi V(t)}}\,dt,\quad V(t)=1-e^{-2t}+\frac{r+1}{r}(1-e^{-t})^2,\quad r>0.\]
All asymptotics are at a fixed positive \(r\) and \(|x|\to\infty\). For the final extreme-value conclusion, samples are independent draws from this density. The proposition does not assert the same far-tail equivalent for a finite-memory Langevin system or for temporally dependent sampled trajectories.

## Proof
Put \(u=e^{-t}\), \(S=(2r+1)/r\), \(A=2(r+1)/r\), \(B_0=1/r\), and \(v(u)=S-Au+B_0u^2\). The density becomes
\[p_r(x)=\frac{r}{\sqrt{2\pi}}\int_0^1u^{r-1}v(u)^{-1/2}\exp\left(-\frac{x^2}{2v(u)}\right)du.\]
Here \(v'(u)=-A+2B_0u\le -2\) on \([0,1]\), \(v(0)=S\), and \(v(1)=0\). The unique maximal variance is thus approached at the endpoint \(u=0\), with a nonzero linear deficit. For small \(u\),
\[v(u)^{-1/2}=S^{-1/2}\left(1+\frac{A}{2S}u+O(u^2)\right),\]
\[\frac1{2v(u)}-\frac1{2S}=c u+d u^2+O(u^3),\quad c=\frac{A}{2S^2},\quad d=\frac{A^2}{2S^3}-\frac{B_0}{2S^2}.\]
Set \(y=x^2u\). The endpoint integral, divided by \(e^{-x^2/(2S)}x^{-2r}\), is bounded and dominated near zero by a constant times \(y^{r-1}e^{-cy/2}\); on every region \(u\ge\delta>0\), monotonicity of \(v\) supplies an exponentially small remainder even after accounting for \(v(1)=0\). Splitting at a fixed sufficiently small \(\delta\) and applying Watson's lemma with these bounds justifies termwise integration, with a remainder \(O_r(x^{-4})\) relative to the leading term. This yields
\[C=\frac{r\Gamma(r)}{\sqrt{2\pi S}}c^{-r}=\frac{\Gamma(r+1)}{\sqrt{2\pi S}}\left(\frac{2S^2}{A}\right)^r.\]
The relative \(x^{-2}\) coefficient, from the first amplitude and quadratic exponent corrections, is
\[\delta=\frac{A}{2S}\frac{r}{c}-d\frac{r(r+1)}{c^2}=-\frac{(2r+1)^3}{2(r+1)}.\]
Since \(r>0\), the algebraic prefactor tends to zero relative to the pure Gaussian. Standard one-sided integration by parts or l'Hôpital's rule, with the obtained smooth asymptotic density, yields
\[\Pr(|X|>x)\sim2CSx^{-(2r+1)}e^{-x^2/(2S)}.\]
For \(N\) iid samples, set \(a=r+1/2\) and \(B=2CS(2S)^{-a}\). Their two-sided survival at \(x=\sqrt{2Sw}\) is \(Bw^{-a}e^{-w}(1+o(1))\). Consequently \(w_N=\log N-a\log\log N+\log B\) gives \(N\Pr(|X|>\sqrt{2Sw_N})\to1\). With \(b_N=\sqrt{2Sw_N}\) and \(d_N=S/b_N\), one has \((b_N+d_Nz)^2/(2S)=w_N+z+o(1)\). Hence \(N\Pr(|X|>b_N+d_Nz)\to e^{-z}\), and independence proves the standard Gumbel law.

## Verification
The included `verify_tail.py` numerically evaluates the mixture after removal of the dominant Gaussian factor, tests the explicit leading constant and first relative correction for several reset rates and magnitudes, and tests normalization of the mixture by Tonelli's theorem. These finite checks are corroboration, not the proof of the infinite-distance limit.

## Relationship to prior work
Santra and Das [1,2] derive the strong-memory quasistatic mixture (arXiv version Eq. 28, journal Eq. 26) and state a Gaussian-only far-tail expression (arXiv Eq. 29, journal Eq. 27). Those expressions and the physical model are not claimed as new. The exact endpoint analysis here changes the asserted **multiplicative** asymptotic equivalence: the missing power \(|x|^{-2r}\) and its constant are needed for rare-event probabilities. General endpoint Laplace asymptotics and classical Gumbel extreme-value arguments are established methods, not independent new theorems. At finite bath friction, the stationary tail belongs to a different order-of-limits problem and need not share the quasistatic polynomial factor.

## Limitations
The source integral is a quasistatic model approximation valid in a strong bath-memory regime. No uniformity in the bath-friction parameter, \(r\), or the sample size is established; taking extreme \(|x|\to\infty\) before the strict strong-memory limit need not give this Gaussian-type law. The iid maximum theorem does not concern consecutive-time samples from a correlated process. The asymptotic method is classical, and an earlier unindexed study could already derive the same specific prefactor.

## References
[1] I. Santra and D. Das, *Resetting in a viscoelastic bath: the bath remembers*, arXiv:2603.17027v1 (first public 2026-03-17), https://arxiv.org/html/2603.17027v1.

[2] I. Santra and D. Das, *Resetting in a viscoelastic bath: the bath remembers*, New Journal of Physics (2026), https://doi.org/10.1088/1367-2630/ae868c.

General endpoint Laplace asymptotics is a standard analytical method.
