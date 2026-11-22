# Three reentrant reset-clock preference switches in a two-rate Gaussian harmonic system

## Finding
Consider two independent Gaussian Ornstein–Uhlenbeck coordinates that are jointly redrawn at every reset from the centered Gaussian covariance \(qI_2\), where \(0<q<1\), and relax between resets to covariance \(I_2\) with variance-relaxation rates \(1\) and \(K>1\). Assess each completed reset cycle with the *conditional endpoint Jeffreys divergence* between its initial and final centered Gaussian distributions. At equal mean reset frequency \(r>0\), compare a periodic interval \(1/r\) with independent exponential intervals of rate \(r\), using expected endpoint divergence per unit physical time.

**Theorem.** For every fixed \(0<q<1\) there exists a finite \(K_0(q)>1\) such that, for every \(K>K_0(q)\), the Poisson-minus-periodic conditional endpoint-divergence rate has **at least three distinct positive zeros**, with strictly alternating negative, positive, negative, positive signs at four increasing frequencies. Therefore no one-crossover principle valid for a single harmonic relaxation mode extends to the sum of two arbitrarily separated modes.

**Explicit certified example.** For \(q=1/2\) and \(K=10000\), the signed difference *divided by the common reset rate* is negative at \(r=1\), positive at \(r=5\), negative at \(r=300\), and positive at \(r=30000\). Each of these four inequalities is certified by exact rational arithmetic in `sign_certificate.py`, with rigorously bounded geometric-series and exponential remainders. Consequently distinct crossings occur in \((1,5)\), \((5,300)\), and \((300,30000)\).

## Assumptions and scope
The coordinates evolve independently between common reset times according to
\[
 dX_i(t)=-\frac{\lambda_i}{2}X_i(t)\,dt+\sqrt{\lambda_i}\,dW_i(t),\qquad
 (\lambda_1,\lambda_2)=(1,K),
\]
with independent standard Wiener noises. Each reset independently redraws both coordinates according to \(N(0,qI_2)\), and resets are instantaneous. Conditional on time \(t\) since the preceding reset, the particle has covariance
\[
 \Sigma(t)=\operatorname{diag}\!\left(1-(1-q)e^{-t},\,1-(1-q)e^{-Kt}\right).
\]
The dimensionless cycle reward is the sum of the two directions of Gaussian KL divergence,
\[
 S_{q,K}(t)=D_{\mathrm{KL}}(N(0,qI_2)\Vert N(0,\Sigma(t)))+
 D_{\mathrm{KL}}(N(0,\Sigma(t))\Vert N(0,qI_2)).
\]
Only the **conditional per-cycle endpoint information** and its renewal-reward rate are compared. This is not, without a specified reverse implementation, the total actuator-inclusive entropy production. The Poisson cycle is evaluated *before* averaging Gaussian endpoint distributions; the mixture of conditional distributions is not substituted into the KL divergence.

## Proof
Define the scalar reward and its Poisson-minus-periodic difference by
\[
 J_q(t)=\frac12\left[\frac{1-(1-q)e^{-t}}q+
 \frac{q}{1-(1-q)e^{-t}}-2\right],\qquad
 h_q(z)=\int_0^\infty ze^{-zt}J_q(t)\,dt-J_q(1/z).
\]
Gaussian KL additivity and time scaling give
\[
 \mathcal R_{\mathrm{Pois}}(r)-\mathcal R_{\mathrm{per}}(r)
 =r\{h_q(r)+h_q(r/K)\}.
\]
Here both renewal laws have mean interval \(1/r\); the renewal-reward theorem identifies their long-run mean rate as expected reward divided by this mean. The bounded continuous reward and positive finite mean justify the formula.

Write \(A_q=(1-q)^2/(2q^2)>0\) and \(B_q=(1-q)/(2q)+(q/2)\log q>0\). The scalar reward has \(J_q(t)=A_qt^2+O(t^3)\) as \(t\downarrow0\), and it approaches \(J_q(\infty)=(q+q^{-1}-2)/2\) exponentially quickly. Furthermore,
\[
 B_q=\int_0^\infty\{J_q(\infty)-J_q(t)\}\,dt>0.
\]
An exponential holding time of rate \(z\) has second moment \(2/z^2\); a Taylor expansion at zero with an exponentially negligible long-time remainder yields
\[
 h_q(z)=A_qz^{-2}+O(z^{-3})\quad(z\to\infty).
\]
Conversely, subtracting the finite limiting reward inside the Laplace integral and using dominated convergence yields
\[
 h_q(z)=-B_qz+o(z)\quad(z\downarrow0),
\]
since the deterministic difference from \(J_q(\infty)\) is \(O(e^{-1/z})\). Continuity of \(h_q\) follows from dominated convergence on every compact subinterval of positive \(z\).

Choose fixed \(0<a<b\) for which \(h_q(a)<0<h_q(b)\), possible by the two limits. For sufficiently large \(K\), the frequencies \(a<b<\sqrt K<Kb\) are ordered. At them, respectively,
\[
\begin{array}{c|c}
 r&\lim_{K\to\infty}\operatorname{sgn}(h_q(r)+h_q(r/K))\\
 a&-\\ b&+\\ \sqrt K&-\\ Kb&+
\end{array}
\]
where the third sign follows more quantitatively from
\[
 h_q(\sqrt K)+h_q(K^{-1/2})=-B_qK^{-1/2}+O(K^{-1})+o(K^{-1/2})<0.
\]
The other three inequalities follow by continuity and the scalar asymptotics. Multiplication by \(r>0\) preserves signs. Three applications of the intermediate value theorem on the disjoint adjacent intervals prove the theorem.

For the explicit \(q=1/2\) example, let \(v=e^{-t}\). One mode's reward becomes
\[
 f(v)=\frac12\left(-v+\frac1{2-v}\right)
 =-\frac v2+\frac14\sum_{n=0}^\infty 2^{-n}v^n.
\]
If the cycle length is exponential with rate \(r\) and a mode relaxes at rate \(\lambda\), set \(z=r/\lambda\). Its expected reward is exactly
\[
 E_z=-\frac{z}{2(z+1)}+\frac14\sum_{n=0}^\infty 2^{-n}\frac{z}{z+n},
\]
with the \(n=0\) summand interpreted as \(1/4\). Truncation through \(n=70\) has nonnegative error at most \(2^{-72}\). Deterministic reward is \(f(e^{-\lambda/r})\). The decreasing function \(f\) and rigorous rational upper/lower bounds on the exponentials give exact rational enclosures for the difference; `sign_certificate.py` verifies the strict signs at the four stated reset rates.

## Verification
Run `python3 sign_certificate.py` using Python 3 and its standard library only. The script computes exact `fractions.Fraction` lower and upper intervals for each of the four witnesses, asserts the alternating signs, and prints approximate intervals solely for readability. For \(0<p\le1\) it bounds \(e^{-p}\) between Taylor polynomials of odd degree \(21\) and even degree \(20\); for \(p>1\) it uses \(0<e^{-p}\le(1+p/20)^{-20}\), valid since \(\log(1+x)\le x\). Thus every sign is an exact finite rational inequality, not a floating-point observation. Independently, direct numerical quadrature agrees with the four displayed signs, but is not needed for the proof.

| Reset rate \(r\) | Certified Poisson-minus-periodic difference divided by \(r\) |
|---|---:|
| \(1\) | between \(-0.025870\) and \(-0.025868\) |
| \(5\) | between \(+0.003482\) and \(+0.003483\) |
| \(300\) | between \(-0.009487\) and \(-0.009486\) |
| \(30000\) | between \(+0.002579\) and \(+0.002580\) |

## Relationship to prior work
Farago's 2026 analysis of a harmonic resetting heat engine establishes the endpoint symmetric-KL formulation and compares periodic with Poissonian reset clocks in one spatial relaxation mode. It also distinguishes endpoint information from implementation-dependent entropy production. Previously published single-mode finite-width results prove that periodic and Poisson reward rates cross at a unique reset cadence; they therefore cannot imply this two-mode **three-crossing counterexample**, because independent Gaussian directions share a single reset clock but contribute at distinct time scales. The present result extends the comparison to the smallest number of distinct relaxation scales that can defeat one-mode uniqueness. Existing renewal-clock optimization bounds address optimization over all clocks rather than this exact multiscale sign-alternation statement. These comparisons establish distinct mathematical claims, not an exhaustive originality guarantee.

## Limitations
At least three crossings are proved; no assertion is made that exactly three exist or that the large-separation threshold \(K_0(q)\) is optimal. The explicit certified witness has \(q=1/2\) and \(K=10000\). For general \(q\), existence of finite \(K_0(q)\) follows from asymptotics without a numerical formula. The theorem concerns conditional Gaussian endpoint Jeffreys divergence, not physical work, actuator-inclusive entropy production, path-wise entropy fluctuations, or KL divergence after mixing over reset ages. No independent audit or publication-priority certification is claimed.

## References
1. O. Farago, *The Resetting Heat Engine: A Thermodynamic Cycle of Thermal Expansion and Compression*, arXiv:2605.28445, first submitted 2026-05-27, https://arxiv.org/abs/2605.28445.
2. *A unique reset-clock preference reversal in Gaussian endpoint divergence*, published mathematical finding, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-unique-reset-clock-preference-reversal-in-gaussian-endpoint-di--85d09840dcfa (index abstract inspected; full text not accessible).
3. *A unique reset-cadence reversal and a logarithmic temperature frontier for Gaussian reset cycles*, published mathematical finding, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-unique-reset-cadence-reversal-and-a-logarithmic-temperature-fr--31e22fdf4f67 (index abstract inspected; full text not accessible).
4. *Sharp renewal-clock envelope for Gaussian endpoint divergence*, published mathematical finding, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-renewal-clock-envelope-for-gaussian-endpoint-divergence--3fdf1f9dc897 (index abstract inspected; full text not accessible).
