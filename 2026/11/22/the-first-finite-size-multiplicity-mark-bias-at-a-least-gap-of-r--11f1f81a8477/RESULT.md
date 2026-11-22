# The first finite-size multiplicity-mark bias at a least gap of regular partitions

## Finding
Fix integers \(\ell\ge2\) and \(s\ge2\). Let \(\mathcal P_\ell(n)\) be the partitions of \(n\) into positive parts not divisible by \(\ell\), sampled uniformly. For a partition \(\lambda\), let \(m_\lambda(j)\) be the multiplicity of part \(j\), and define the first part deficient in \(s\) copies and its *deficiency mark* by
\[
M_s(\lambda)=\min\{j\ge1:\ell\nmid j,\ m_\lambda(j)<s\},\qquad J_s(\lambda)=m_\lambda(M_s(\lambda))\in\{0,\ldots,s-1\}.
\]
Put \(\rho_\ell=1-1/\ell\) and
\[
C_{\ell,s}=\frac{\pi}{24^{1/4}s^{3/2}\rho_\ell^{1/4}}>0.
\]
For every fixed mark \(a\in\{0,\ldots,s-1\}\), as \(n\to\infty\),
\[
\boxed{\Pr\{J_s=a\}=\frac1s+\left(\frac{s-1}{2}-a\right)C_{\ell,s}n^{-1/4}+o_{\ell,s}(n^{-1/4}).}
\]
Thus the asymptotic uniform marks exhibit a sharp *linear* positive finite-size bias toward smaller multiplicities. If \(1\le r<s\), then the exact equality of first-deficiency locations obeys
\[
\boxed{\Pr\{M_r=M_s\}=\frac rs+\frac{r(s-r)}2 C_{\ell,s}n^{-1/4}+o_{\ell,r,s}(n^{-1/4}).}
\]
In particular, the difference from \(r/s\) is eventually strictly positive, and the power \(n^{-1/4}\) and its coefficient are sharp.

## Assumptions and scope
All parameters \(\ell,s,r,a\) are fixed while \(n\) tends to infinity. Every permitted part has unrestricted nonnegative multiplicity. The probability is uniform over all \(\ell\)-regular partitions of \(n\); no growing-parameter uniformity is claimed. Write \(p_\ell(n)=|\mathcal P_\ell(n)|\) for \(n\ge0\) and \(p_\ell(n)=0\) for \(n<0\). The finite-size formulas below hold even at \(n=0\).

## Proof
**1. Exact marked count.** List the permitted parts as \(u_1<u_2<\cdots\) and put \(S_0=0\), \(S_{j-1}=\sum_{i<j}u_i\). To have \(M_s=u_j\) and \(J_s=a\), every smaller permitted part must occur at least \(s\) times, and \(u_j\) must occur exactly \(a\) times. Removing mandatory smaller copies and exactly \(a\) copies of \(u_j\), then forbidding further copies of \(u_j\), gives the **exact** formula
\[
N_a(n)=\sum_{j\ge1}\big[p_\ell(n-sS_{j-1}-a u_j)-p_\ell(n-sS_{j-1}-(a+1)u_j)\big]. \tag{1}
\]
Equivalently, with
\[
P_\ell(q)=\prod_{\substack{m\ge1\\\ell\nmid m}}(1-q^m)^{-1},\quad
B_a(q)=\sum_{j\ge1}q^{sS_{j-1}+a u_j}(1-q^{u_j}),
\]
we have \(N_a(n)=[q^n]P_\ell(q)B_a(q)\). Since \(\sum_{a=0}^{s-1}B_a(q)=\sum_{j\ge1}q^{sS_{j-1}}(1-q^{su_j})=1\) by telescoping, \(\sum_aN_a(n)=p_\ell(n)\) exactly.

**2. The differentiating kernel.** For any fixed integers \(0\le a<b<s\), set \(B_{a,b}=B_a-B_b\). Let \(\rho=\rho_\ell\). Elementary counting of integers not divisible by \(\ell\) gives, uniformly in \(j\ge1\),
\[
u_j=j/\rho+O_\ell(1),\qquad S_{j-1}=j^2/(2\rho)+O_\ell(j).
\]
For real \(t\downarrow0\), the bracket in
\[
B_{a,b}(e^{-t})=\sum_{j\ge1}e^{-stS_{j-1}}
\left[e^{-atu_j}-e^{-(a+1)tu_j}-e^{-btu_j}+e^{-(b+1)tu_j}\right]
\]
is \((b-a)t^2u_j^2+O_s(t^3u_j^3)\). Gaussian summation, splitting at \(j\asymp t^{-1/2}\) and bounding the exponentially small tail, therefore yields
\[
\begin{aligned}
B_{a,b}(e^{-t})
&=(b-a)\frac{t^2}{\rho^2}\sum_{j\ge1}j^2e^{-stj^2/(2\rho)}+O_{\ell,s}(t)\\
&=(b-a)\frac{\sqrt{\pi/2}}{s^{3/2}\sqrt\rho}\,t^{1/2}+O_{\ell,s}(t). \tag{2}
\end{aligned}
\]
The same estimate with \(O(t)\) error is uniform for complex \(t\) in a shrinking sector \(|\operatorname{Im}t|\le(\operatorname{Re}t)^{3/2-\delta}\) for fixed \(0<\delta<1/6\). Indeed \(\operatorname{Im}t/\operatorname{Re}t\to0\), and the Taylor, Gaussian-sum, and exponential-tail estimates are uniform there.

**3. Coefficient localization, including cancellation.** Set \(\mu=\pi^2\rho/6\) and \(t_n=(\mu/n)^{1/2}\). The Euler product, or the modular transformation of the two Euler products, gives for \(t\) in the central complex sector
\[
P_\ell(e^{-t})=\ell^{-1/2}\exp\big(\mu/t+(\ell-1)t/24\big)
\big(1+O_\ell(e^{-c_\ell/\operatorname{Re}t})\big). \tag{3}
\]
For completeness, the required minor-arc localization follows directly from the nonnegative product factors. With \(q_0=e^{-t_n}\),
\[
\log\frac{P_\ell(q_0)}{|P_\ell(q_0e^{i\theta})|}
=\frac12\sum_{\ell\nmid m}\log\left(1+\frac{2q_0^m(1-\cos m\theta)}{(1-q_0^m)^2}\right).\tag{4}
\]
Restrict \(m\) to a fixed-width interval of order \(t_n^{-1}\), omitting multiples of \(\ell\). Its trigonometric sum is bounded below by \(c_\ell\min(\theta^2t_n^{-3},t_n^{-1})\) for \(0<|\theta|\le\pi\). For \(|\theta|\le t_n\), this follows from \(1-\cos(m\theta)\gg(m\theta)^2\) on a suitably shortened interval. For \(|\theta|\ge t_n\), here is a compactness proof of the uniform lower bound. If it failed for a sequence \(N\to\infty\), \(N\asymp t_n^{-1}\), the mean of \(1-\cos(m\theta_N)\) on permitted \(m\in[N,2N]\) would tend to zero. Taking a subsequence with \(\theta_N\to\theta_*\), the finite geometric-series identity, separately on each of the \(\ell-1\) permitted residue classes, forces \(\theta_*\) to be a multiple of \(2\pi/\ell\); otherwise the mean tends to one. Write \(\theta_N=2\pi h/\ell+\varepsilon_N\). If \(N\varepsilon_N\) has a finite subsequential limit \(v\), the mean tends to
\[
1-\operatorname{Re}\left(\frac{1}{\ell-1}\sum_{a=1}^{\ell-1}e^{2\pi i ha/\ell}\int_1^2e^{ivx}\,dx\right).
\]
For \(h\not\equiv0\pmod\ell\), the residue average is \(-1/(\ell-1)\), giving a strictly positive limit (also for \(\ell=2\), since the integral cannot identically equal \(-1\)). For \(h=0\), the condition \(|\theta_N|\ge1/N\) gives \(|v|\ge1\) if \(v\) is finite, and the displayed limit \(1-\int_1^2\cos(vx)\,dx\) is again strictly positive. If \(|N\varepsilon_N|\to\infty\), all residue-class geometric sums have vanishing normalized mean, giving limit one. Compactness gives the desired positive lower bound depending only on \(\ell\). The logarithm in (4) dominates a positive constant times \(1-\cos(m\theta)\) on the selected interval. Thus for \(|\theta|\ge t_n^{3/2-\delta}\),
\[
|P_\ell(q_0e^{i\theta})|\le P_\ell(q_0)e^{-c_{\ell,\delta}t_n^{-2\delta}}. \tag{5}
\]
The elementary bound \(|B_{a,b}(q_0e^{i\theta})|=O_{\ell,s}(t_n^{-1/2})\) then makes the entire minor-arc integral exponentially negligible relative to the main term. On the central arc, (2) implies
\[
B_{a,b}(e^{-t_n-i\theta})=B_{a,b}(q_0)(1+o(1))
\]
uniformly. Expanding \(\mu/(t_n+i\theta)+n(t_n+i\theta)\) at its stationary point gives a Gaussian of width \(t_n^{3/2}\). The same Gaussian integral occurs for \(P_\ell\) alone and for \(P_\ell B_{a,b}\), so their ratio is
\[
\frac{[q^n]P_\ell(q)B_{a,b}(q)}{p_\ell(n)}=B_{a,b}(q_0)(1+o(1)).\tag{6}
\]
This calculation is directly at the *difference of marked counts*: it does not attempt to subtract two uncontrolled \(o(1)\) marginal estimates. Equations (2) and (6) give
\[
\Pr\{J_s=a\}-\Pr\{J_s=b\}
=(b-a)\frac{\sqrt{\pi/2}\mu^{1/4}}{s^{3/2}\sqrt\rho}\,n^{-1/4}+o(n^{-1/4})
=(b-a)C_{\ell,s}n^{-1/4}+o(n^{-1/4}).\tag{7}
\]

**4. Normalization and tied gaps.** Since the \(s\) mark probabilities sum to one, (7) uniquely yields the displayed linear profile. For \(1\le r<s\), all permitted parts below \(M_s\) have multiplicity at least \(s\), hence at least \(r\). Therefore \(M_r=M_s\) if and only if \(J_s<r\). Summing the marked profile for \(a=0,\ldots,r-1\) gives the tie formula. The second-order coefficients are positive for every \(1\le r<s\), proving sharpness and eventual strict bias.

## Verification
Run `python verify_gap_marks.py` using only the Python standard library. The script uses independent direct enumeration of partitions for \(0\le n\le19\) and \(2\le\ell\le6\), comparing 300 mark vectors with the exact formula (1). It separately checks the mark-probability asymptotic trend at 27 tuples with \(\ell\in\{2,3,5\}\), \(s\in\{2,3,4\}\), and \(n\in\{800,1500,3000\}\); the latter are numerical diagnostics rather than a proof of the limit. The expected output is `REGULAR_GAP_MARK_EXACT_OK 300 27`. The analytic proof of (7) is the saddle localization and Gaussian asymptotic above.

## Relationship to prior work
Priya, Bhowmick and Meher (first public version November 5, 2026) obtain a two-variable generating function marking the *location* of the least deficient part and aggregate asymptotics at several moduli. Their formula does not resolve the actual multiplicity *at* the stopping part, let alone its first finite-size bias. Wagner's Theorem 3 (2011) proves a one-threshold Weibull local limit for much more general permitted-part sequences; its leading local limit does not supply the explicit cancellation-sensitive \(n^{-1/4}\) correction to marked probabilities. The public notes *Joint least-multiplicity-gap laws for regular partitions* (November 2026) establish an exact multi-rank survivor and weak vector limit, but expressly do not assert convergence of exact equality events or finite-size marked corrections. *Joint Rayleigh records and uniform multiplicity marks for least partition gaps* (October 2026) concerns unrestricted partitions and gives a uniform mark **limit**, not its signed first correction. Thus the present claim is a marked, quantitative order beyond those statements, not a new assertion about their already-known leading Rayleigh marginal.

## Limitations
This treats the uniform ensemble of regular partitions, fixed \(\ell,s\), and the first finite-size mark bias only; no full higher-order expansion or parameter-uniform bounds are asserted. The use of classical Euler-product modular transformation and saddle localization is standard analytic input; the new claim is the explicit signed coefficient and its tied-gap consequence. The prime-to-\(\ell\) density constant is not a prime-number density; it is the density of part sizes not divisible by \(\ell\). Unindexed equivalent marked refinements remain a priority risk. Independent mathematical audit has not been performed.

## References
- P. Tejash, S. Bhowmick and N. K. Meher, *The minimal excludant and the least r-gaps of ℓ-regular partitions*, arXiv:2611.07871, first posted 2026-11-05, https://arxiv.org/html/2611.07871v1.
- S. Wagner, *Limit distributions of smallest gap and largest repeated part in integer partitions*, Ramanujan Journal 25 (2011), 229–246, https://www.finanz.math.tugraz.at/~wagner/limitdist.pdf.
- *Joint least-multiplicity-gap laws for regular partitions*, published research note (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-joint-least-multiplicity-gap-laws-for-regular-partitions--a7d5664f9d36.
- *Joint Rayleigh records and uniform multiplicity marks for least partition gaps*, published research note (2026-10-25), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-joint-rayleigh-records-and-uniform-multiplicity-marks-for-least--1284bec11d63.
