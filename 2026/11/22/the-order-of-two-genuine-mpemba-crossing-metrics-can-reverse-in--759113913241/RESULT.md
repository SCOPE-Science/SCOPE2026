# The order of two genuine Mpemba crossing metrics can reverse in a reversible three-level gate

## Finding

A reversible three-level thermalization process can have unique crossings in **both** total variation and its stationary-weighted Hilbert-space distance, yet **either** metric can report the hot-versus-warm reversal first. The ordering switches between two rationally specified sets of canonical initial and bath temperatures, even though the energies and transition-rate prefactors are identical.

For the model and notation below, define \(z_2=e^{-\delta t_2}\) and \(z_{TV}=e^{-\delta t_{TV}}\), where \(\delta=(c-a)(1-r)\). At energies \((0,1,3)\), \(a=1\), \(c=5\), and \(u=e^{-\beta}\), the following **exact** values hold:

| \((u_h,u_w,u_b)\) | \(z_2^2\) | \(z_{TV}\) | Crossover order |
|---|---|---|---|
| \((1,2/3,2/5)\) | \(8180/3657833\) | \(4259/126087\) | \(t_2<t_{TV}\) |
| \((1,4/5,1/8)\) | \(228877/138852250\) | \(2816/24875\) | \(t_{TV}<t_2\) |

The corresponding approximate times are \((t_2,t_{TV})=(1.049658765,1.165399641)\) and \((0.900927147,0.612583310)\). The strict ordering is proved by rational comparisons of \(z_{TV}^2\) with \(z_2^2\), not by floating-point approximation.

## Assumptions and scope

Let three distinct energies be \((0,\Delta,E)\) with \(0<\Delta<E\), and fix inverse bath temperature \(\beta_b>0\). Set \(Z(\beta)=1+e^{-\beta\Delta}+e^{-\beta E}\) and \(q(\beta)=Z(\beta)^{-1}(1,e^{-\beta\Delta},e^{-\beta E})\). Let \(\pi=q(\beta_b)=(p,r,s)\) and \(o=p+s=1-r\). At each state \(i\), the rate \(k_{ij}\) from \(i\) to \(j\) is: \(k_{1j}=a\pi_j\) and \(k_{j1}=a r\) for \(j=0,2\); also \(k_{02}=cs\) and \(k_{20}=cp\). Here \(0<a<c\). These rates are strictly positive and satisfy \(\pi_i k_{ij}=\pi_j k_{ji}\).

Both systems are prepared at canonical inverse temperatures \(0\le\beta_h<\beta_w<\beta_b\), then evolve with the same bath generator. Define the genuine metrics \(d_2(v,\pi)=[\sum_i(v_i-\pi_i)^2/\pi_i]^{1/2}\) and \(d_{TV}(v,\pi)=\frac12\sum_i|v_i-\pi_i|\). Their positive crossover times are the positive solutions of \(d(q_h(t),\pi)=d(q_w(t),\pi)\). A larger initial distance at \(t=0\) is required, so a crossover denotes an actual reversal.

For any starting inverse temperature \(\beta<\beta_b\), define \(m_\beta=q_1(\beta)-r\) and \(n_\beta=pq_2(\beta)-sq_0(\beta)>0\), and let \(\theta_\beta=sm_\beta\) if \(m_\beta\ge0\) and \(\theta_\beta=-pm_\beta\) otherwise. Write \(\lambda=a r+c o\), \(\delta=\lambda-a=(c-a)o>0\), and \(z=e^{-\delta t}\).

## Proof

**1. Exact two-mode dynamics.** Direct application of the forward generator gives \(\dot m=-am\) and \(\dot n=-\lambda n\). Because these variables and normalization determine all three coordinates, the exact deviations are

\[
q(t;\beta)-\pi=\frac{e^{-at}}{o}\bigl(-pm_\beta-n_\beta z,\;om_\beta,\;-sm_\beta+n_\beta z\bigr).
\]

In the weighted inner product \(\langle v,w\rangle_\pi=\sum_i v_iw_i/\pi_i\), the two modes are orthogonal, hence

\[
d_2(q(t;\beta),\pi)^2=e^{-2at}\left(A_\beta+B_\beta z^2\right),\quad
A_\beta=\frac{m_\beta^2}{ro},\quad B_\beta=\frac{n_\beta^2}{pso}.
\]

Inspection of the signs of the three components, using \(n_\beta>0\), gives independently

\[
d_{TV}(q(t;\beta),\pi)=e^{-at}\left(|m_\beta|+\frac{(n_\beta z-\theta_\beta)_+}{o}\right),\qquad(x)_+=\max\{x,0\}.
\]

**2. Initial ordering and Hilbert crossover.** For \(\beta<\beta_b\), \(d_2(q(\beta),\pi)^2+1=Z(\beta_b)Z(2\beta-\beta_b)/Z(\beta)^2\), which strictly decreases as \(\beta\) approaches \(\beta_b\), since the Gibbs mean energy strictly decreases with inverse temperature. The total-variation distance decreases strictly as well: initially \(q_0(\beta)<p\), \(q_2(\beta)>s\), and \(d_{TV}=\max\{p-q_0(\beta),q_2(\beta)-s\}\), with both entries decreasing in \(\beta\). Thus hot is initially farther for **both** metrics.

The canonical ordering implies \(n_h>n_w>0\), so \(B_h>B_w\). If \(|m_h|<|m_w|\), then \(A_h<A_w\), and strict initial ordering implies \(0<(A_w-A_h)/(B_h-B_w)<1\). The squared Hilbert distances therefore cross exactly once, at

\[z_2^2=\frac{A_w-A_h}{B_h-B_w},\qquad t_2=-\frac{\log z_2}{\delta}.\]

If \(|m_h|\ge|m_w|\), the two squared-distance coefficients are already ordered and no positive Hilbert crossing occurs (an equality in the slow coefficient is not a strict long-time reversal).

**3. Unique variation crossover.** Under \(|m_h|<|m_w|\), divide the hot-minus-warm variation distance difference by \(e^{-at}\). The resulting function is

\[F(z)=|m_h|-|m_w|+\frac{(n_hz-\theta_h)_+-(n_wz-\theta_w)_+}{o}.\]

Here \(F(0)<0\), \(F(1)>0\), and the hinge activation points are nonnegative. If the hot hinge activates first, \(F\) is constant and then has slopes \(n_h/o>0\) and \((n_h-n_w)/o>0\). If the warm hinge activates first, \(F\) is constant, then has slope \(-n_w/o<0\), and finally slope \((n_h-n_w)/o>0\). Thus either activation order yields exactly one positive root \(z_{TV}\in(0,1)\), hence exactly one positive time \(t_{TV}\).

**4. Exact reversal witnesses.** Set \((\Delta,E,a,c)=(1,3,1,5)\), so the stationary and starting Gibbs distributions for rational \(u=e^{-\beta}\) all have rational coordinates. For the first witness, the exact fraction computations give \(z_2^2=8180/3657833\) and \(z_{TV}=4259/126087\); only the hot positive-part term is active at the latter root, and \(z_{TV}^2<z_2^2\). Therefore \(t_{TV}>t_2\). For the second, the computations give \(z_2^2=228877/138852250\), \(z_{TV}=2816/24875\), and both positive-part terms are active at that root. Here \(z_{TV}^2>z_2^2\), so \(t_{TV}<t_2\). All assertions about hinge activation, roots and inequalities are exact rational checks, reproduced by `checker.py`.

**5. Temperature-domain boundary (supporting classification).** The intermediate Gibbs mass \(q_1(\beta)\) has derivative with the sign of \((E-\Delta)e^{-\beta E}-\Delta\). Consequently it has an interior strict maximum precisely if \(E>2\Delta\), located at \(\beta_*=(1/E)\log((E-\Delta)/\Delta)\). A hot/warm pair with \(|m_h|<|m_w|\) exists below bath inverse temperature \(\beta_b\) precisely when \(E>2\Delta\) and \(\beta_b>\beta_*\). This is a model-specific manifestation of established slow-eigenmode geometry, not an independently claimed general novelty.

## Verification

Run `python3 checker.py` using Python 3 and only the standard library. The program checks rational stationarity and detailed balance through the forward operator, both eigenmodes and their weighted orthogonality, the total-variation identity at multiple exact points, the exact root identities, the hinge conditions and rational strict sign comparisons for both witnesses. Its output includes the exact crossover fractions and approximate times. This finite checker verifies calculations and finite instances, while the general uniqueness arguments are analytic as proved above; the code alone is not a proof of universal statements.

## Relationship to prior work

The three-level Markovian Mpemba phenomenon and its slow-eigenmode mechanism are established in Lu–Raz (2017). Avitan–Factor–Gelbwaser-Klimovsky (2026) and Gelbwaser-Klimovsky (2026) give general necessary and/or sufficient geometric conditions for three-level Mpemba behavior; the existence boundary in Step 5 specializes those ideas, and is not presented as a novel general criterion. Pardhi–Abbas–Das (2026) develop a genuine weighted-Hilbert distance approach for continuous-space Markovian dynamics; their results do not provide the present three-state hinge formula or two-way crossing-time ordering. Taye (2026) bounds **relative-entropy** crossover times, reporting that energy can cross later; that is a different comparison. A known general reversible-chain spectral zero-count bound also yields the at-most-one weighted-Hilbert crossing in dimension three; the distinguishing result here is the **two-way reversal in the ordering of the two genuine metrics**, with exact finite certificates, for canonical preparations of one physical gate model.

## Limitations

The theorem assumes exactly three discrete energy levels, strictly positive detailed-balance rates of the specified gate form, independent canonical initial equilibria, \(0<a<c\), and exact distances. It does not assert metric-order reversal for every hot/warm pair, nor that all reasonable metrics share crossing times. Crossing-time order is not an invariant of a thermomajorization relation. The two examples change the bath and initial temperatures, but hold the energy spectrum and rate prefactors fixed. No experimental finite-sampling, uncertainty-propagation, or continuum limit is established. The source comparison does not establish publication priority; more general unpublished or less visible finite-state results might implicitly contain the metric-order comparison.

## References

- Z. Lu and O. Raz, *Nonequilibrium thermodynamics of the Markovian Mpemba effect and its inverse*, PNAS 114 (2017), 5083–5088, https://doi.org/10.1073/pnas.1701264114.
- I. Avitan, R. Factor and D. Gelbwaser-Klimovsky, *Necessary conditions for the Markovian Mpemba effect*, arXiv:2603.04567, https://arxiv.org/abs/2603.04567.
- D. Gelbwaser-Klimovsky, *Efficient protocol for the Markovian Mpemba effect in \(N\)-level systems*, arXiv:2609.09988, https://arxiv.org/abs/2609.09988.
- M. Taye, *Mpemba effect as an entropy-production race: Finite-amplitude bounds on crossing times in Markovian relaxation*, arXiv:2610.40704, https://arxiv.org/abs/2610.40704.
- U. Pardhi, S. Abbas and M. Das, *Mathematical analysis of the Markovian Mpemba effect*, arXiv:2611.09391, first released 2026-11-06, https://arxiv.org/abs/2611.09391.
