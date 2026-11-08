# Mesoscopic mass and extremal occupancy at a growing collection of critical zero-range defects

## Finding
Let \(\rho>0\) be fixed and let \(M\to\infty\). On a directed ring, consider \(M\) ordinary sites with constant departure rate one and \(r_M\) distinguished sites with identical constant departure rate \(q=\rho/(1+\rho)\), where \(r_M\to\infty\) and \(r_M/M\to0\). Each occupied site sends one particle clockwise at its departure rate, independently of its positive occupation, and the conserved particle total is \(N_M=\lfloor\rho M\rfloor\). Write \(T_M\) for the total occupation of the distinguished sites, and \(Y_{1,M},\ldots,Y_{r_M,M}\) for their individual occupations, in the unique stationary state. Put \(\sigma^2=\rho(1+\rho)\).

The following joint mesoscopic scaling law holds:

\[
\frac{T_M}{\sigma\sqrt{Mr_M}}\xrightarrow{\mathbb P}1,
\qquad
\frac{T_M-m_M}{\sqrt M}\xrightarrow{\mathrm d}
\mathcal N(0,\sigma^2/2),
\]

where \(m_M\) is the mode explicitly specified below. For each fixed \(k\ge1\),

\[
\left(\frac{Y_{1,M}}{\sigma\sqrt{M/r_M}},\ldots,
\frac{Y_{k,M}}{\sigma\sqrt{M/r_M}}\right)
\xrightarrow{\mathrm d} (E_1,\ldots,E_k),
\]

where the \(E_i\) are independent unit-mean exponential random variables. If additionally \(r_M(\log r_M)^2/M\to0\), then for every real \(x\),

\[
\mathbb P\!\left(
\frac{\max_{1\le i\le r_M}Y_{i,M}}{\sigma\sqrt{M/r_M}}
-\log r_M\le x\right)\longrightarrow \exp(-e^{-x}).
\]

Thus a subextensive, growing population of equally slow sites stores an aggregate mass of order \(\sqrt{Mr_M}\), has Gaussian aggregate fluctuations of order \(\sqrt M\), exponential typical-site occupations of order \(\sqrt{M/r_M}\), and (under the stated additional growth condition) a Gumbel largest occupation.

## Assumptions and scope
The sites can be arranged arbitrarily on the directed ring; their order is irrelevant to the stationary law. Both \(M\) and \(r_M\) are positive integers, with \(M\ge2\) and ultimately \(r_M\ge2\). Rates and densities are fixed exactly as defined above; in particular the distinguished-site rate is tuned to the ordinary-site critical fugacity. This is a stationary distribution theorem, not a mixing-time, dynamical coarsening, or uniform-in-density result. Statements about the first \(k\) sites hold for fixed \(k\), not for \(k\) growing with \(M\).

For finite \(M\), abbreviate \(r=r_M\), \(N=N_M\). The precise mode is

\[
 m_M=\left\lceil\frac{b+\sqrt{b^2+4(1-q)c}}{2(1-q)}\right\rceil,
 \quad b=N-r-q(N+M-2),\quad c=rN-q(N+M-1).
\]

If the ratio of consecutive probabilities is exactly one at an integer, there are two adjacent modes and this formula chooses the larger one.

## Proof
**1. Exact stationary weights.** A configuration \(\eta\), with nonnegative integer site occupations summing to \(N\), has stationary probability proportional to \(\prod_j a_j^{-\eta_j}\), where \(a_j\) is its positive departure rate. Indeed, for every clockwise edge \(j\to j+1\), the stationary incoming flux into \(\eta\) from that edge is \(a_{j+1}\pi(\eta)\) when the destination site in \(\eta\) is occupied; this cancels the corresponding outgoing flux from the next edge. The finite conserved-state chain is irreducible, so its stationary law is unique. Counting weak compositions of the distinguished mass and the remaining mass gives the **exact**, normalized marginal

\[
\mathbb P(T_M=t)=\frac{W_M(t)}{\sum_{u=0}^{N}W_M(u)},\qquad
W_M(t)=\binom{t+r-1}{r-1}q^{-t}\binom{N-t+M-1}{M-1},\quad 0\le t\le N.
\]

Conditional on \(T_M=t\), all weak compositions of \(t\) into \(r\) distinguished occupations are equiprobable.

**2. The exact mode and mass scale.** Direct cancellation yields

\[
R_M(t):=\frac{W_M(t+1)}{W_M(t)}
=\frac{t+r}{t+1}\frac{N-t}{q(N-t+M-1)},\qquad0\le t<N.
\]

Both factors are decreasing in \(t\) when \(r>1\), hence the weights are strictly log-concave except possibly for two tied adjacent modes. The equation \(R_M(t)=1\) is precisely \((1-q)t^2-bt-c=0\); its positive root gives the stated mode. In the regime \(r\to\infty\), \(r/M\to0\), set \(s_M=\sigma\sqrt{Mr}\). For each fixed \(u>0\), uniformly at \(t=us_M+O(1)\), elementary logarithmic expansions with \(N=\rho M+O(1)\) yield

\[
\log R_M(t)=\frac{r}{t}-\frac{t}{\sigma^2M}
+o(\sqrt{r/M})
=\frac{\sqrt{r/M}}\sigma\bigl(u^{-1}-u+o(1)\bigr).
\]

Thus \(m_M/s_M\to1\). To transfer localization of the mode to probability concentration, note that \(\log R_M(t)\) is decreasing and

\[
\frac{d}{dt}\log R_M(t)
=-\frac{r-1}{(t+r)(t+1)}
-\frac{M-1}{(N-t)(N+M-1-t)}
\le-\frac{c_\rho}{M}
\]

for \(0\le t<N\) and a constant \(c_\rho>0\), for all sufficiently large \(M\). The derivative is interpreted for real \(t\) inside this interval. Consequently the weights have a uniform discrete-Gaussian tail bound about their mode; their mass concentrates in a window of order \(\sqrt M\). Since \(m_M/\sqrt M\sim\sigma\sqrt r\to\infty\), this proves the first convergence.

**3. Gaussian total-mass fluctuations.** In a window \(t=m_M+O(\sqrt M)\), both terms in the preceding derivative have the same asymptotic value \(-1/(\sigma^2M)\), because \(m_M\sim\sigma\sqrt{Mr}\), \(m_M/r\to\infty\) and \(m_M/M\to0\). Therefore, uniformly for \(z\) in each fixed compact interval,

\[
\log\frac{W_M(m_M+\lfloor z\sqrt M\rfloor)}{W_M(m_M)}
\longrightarrow-\frac{z^2}{\sigma^2}.
\]

The global discrete-Gaussian envelope from Step 2 dominates the corresponding Riemann sums and supplies uniform integrability. Normalizing gives the centered Gaussian density proportional to \(e^{-z^2/\sigma^2}\), whose variance is \(\sigma^2/2\). This also establishes the required \(O_{\mathbb P}(\sqrt M)\) precision for \(T_M\).

**4. Finite collections of sites.** For fixed nonnegative integers \(k_1,\ldots,k_\ell\) with \(K=\sum_i k_i\le t\), uniform weak compositions give the exact joint survival probability

\[
\mathbb P(Y_{1,M}\ge k_1,\ldots,Y_{\ell,M}\ge k_\ell\mid T_M=t)
=\frac{\binom{t-K+r-1}{r-1}}{\binom{t+r-1}{r-1}}.
\]

If \(t\sim\sigma\sqrt{Mr}\), then \(r/t\to0\). Taking \(k_i=\lceil a_i\sigma\sqrt{M/r}\rceil\), with fixed \(a_i\ge0\), the logarithm of the displayed ratio tends to \(-\sum_i a_i\). Step 2 ensures this holds after averaging over the random \(T_M\). Joint survival functions consequently converge to those of independent unit exponentials.

**5. Largest occupation.** Assume additionally \(r(\log r)^2/M\to0\). Conditional on \(T_M=t\sim\sigma\sqrt{Mr}\), let \(C_M\) count the distinguished sites with occupation strictly greater than \(k=\lfloor (t/r)(\log r+x)\rfloor\). For every fixed positive integer \(j\), the exact conditional factorial moment is

\[
\mathbb E[(C_M)_j\mid T_M=t]
=(r)_j\frac{\binom{t-j(k+1)+r-1}{r-1}}{\binom{t+r-1}{r-1}}.
\]

The logarithm of the binomial ratio is
\(-j(\log r+x)+o(1)\): its remainder is bounded, for fixed \(j\) and bounded \(x\), by a constant multiple of \((\log r)^2/r+(r/t)\log r\), both tending to zero. Hence the factorial moments converge to \(e^{-jx}\), giving \(C_M\Rightarrow\mathrm{Poisson}(e^{-x})\) and \(\mathbb P(C_M=0)\to e^{-e^{-x}}\). Finally \(T_M=m_M+O_{\mathbb P}(\sqrt M)\), \(m_M/(\sigma\sqrt{Mr})=1+O(1/r+\sqrt{r/M})\), and the growth assumption imply

\[
\left(\frac{T_M}{r}-\sigma\sqrt{M/r}\right)
\frac{\log r}{\sigma\sqrt{M/r}}\xrightarrow{\mathbb P}0.
\]

Thus the random conditional threshold can be replaced by the deterministic scale in the stated Gumbel convergence. All limits are along arbitrary integer sequences satisfying the listed hypotheses.

## Verification
The accompanying `check.py` uses only Python's standard library. It reconstructs exact finite conserved-state Markov-generator balance, counts defect masses by the two weak-composition factors, checks the exact consecutive-weight ratio and quadratic mode, and evaluates finite-size scale and conditional-extremal diagnostics. Run it by `python check.py`; its expected result is `PASS 130 finite and asymptotic diagnostic checks`. The integer-conservation and generator checks are exact up to floating arithmetic; the asymptotic checks are finite diagnostics, not replacements for Steps 2–5 of the proof.

## Relationship to prior work
The zero-range product measure and the importance of defect-induced condensation are established starting points. Angel, Evans and Mukamel (2004), especially Sections II, III and V, examine a **single** inhomogeneous slow site with occupation-dependent corrections and canonical finite-size effects, including a square-root density window. Chleboun and Grosskinsky (2010) analyze finite-size metastability and related condensation for homogeneous occupation-dependent jump rates. Angel, Evans, Levine and Mukamel (2007) study subextensive mesocondensates in a **non-conserving**, creation-and-annihilation model. These mechanisms and their studied limits do not, as stated, supply the growing-number-of-equal-defects stationary theorem above. The established product-measure formula alone does not specify the simultaneous aggregate Gaussian, site exponential and extreme-value scales for \(r_M\to\infty\).

Rafferty's 2016 thesis includes a multiple-defect constant-rate model and studies relaxation-time questions; the complete thesis was not reliably accessible for full comparison in this assessment. A 2014 publication by Zeng also considers many defect sites and critical density; its complete text could not be assessed. These remain specific priority risks: their statements may overlap the present stationary asymptotics. No claim of exhaustive historical priority is made.

## Limitations
The theorem is restricted to identical slow-site rates exactly at the critical value, an asymmetric directed ring, subextensive growing defect count, and stationarity. No convergence rate, mixing-time result or uniqueness of a possible physical universality class is asserted. The Gumbel conclusion requires the stronger logarithmic growth condition; it is not claimed for every \(r_M=o(M)\). Results with finite \(r_M\), extensive defect density, heterogeneous defect rates, or density shifted away from \(\rho\) are not included. The literature comparison establishes a bounded positive novelty assessment, not independent certification.

## References
1. A. G. Angel, M. R. Evans and D. Mukamel, *Condensation Transitions in a One-Dimensional Zero-Range Process with a Single Defect Site*, first posted 2004-01-15, https://arxiv.org/abs/cond-mat/0401262 .
2. P. Chleboun and S. Grosskinsky, *Finite size effects and metastability in zero-range condensation*, first posted 2010-04-03, https://arxiv.org/abs/1004.0408 .
3. A. G. Angel, M. R. Evans, E. Levine and D. Mukamel, *Criticality and Condensation in a Non-conserving Zero Range Process*, first posted 2007-05-28, https://arxiv.org/abs/0705.4042 .
4. T. Rafferty, *Dynamic properties of condensing particle systems*, doctoral thesis, University of Warwick, 2016, https://wrap.warwick.ac.uk/91746/ .
5. R. F. Zeng, *Research on Thermal Balance with Critical Density in the Zero-Range Process with many Defect Sites*, 2014, https://doi.org/10.4028/www.scientific.net/AMR.977.191 .
