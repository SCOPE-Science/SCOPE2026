# Nonanalytic reset-onset and log-periodic mobility in a disordered random comb

## Finding

Consider the continuous-time biased random walk on a periodic comb, with independent geometric branch lengths. The positive stationary backbone drift induced by a weak Poisson return-to-junction mechanism does **not** generally have a linear onset in the return rate. On the trapping side of the unreset transition, the onset is a fractional power multiplied by an explicit, strictly nonconstant periodic function of the logarithm of the return rate. At the trapping boundary, the drift instead has a universal inverse-logarithmic onset.

Precisely, let \(\alpha>\beta>0\), \(f=\alpha/\beta>1\), \(c=(\alpha-\beta)^2/\alpha\), and let each branch length have law \(\Pr(L=\ell)=(1-\rho)\rho^\ell\) for every integer \(\ell\ge0\), with \(0<\rho<1\). Write \(v(r)\) for the almost-sure thermodynamic limit of the stationary unwrapped backbone drift at return rate \(r>0\). In the trapping regime \(1/f<\rho<1\), put \(s=-\log\rho/\log f\), so that \(0<s<1\), and define

\[
\Theta_s(y)=\sum_{j\in\mathbb Z}\frac{f^{s(y-j)}}{1+f^{y-j}}.
\]

The series converges absolutely and locally uniformly, is strictly positive and one-periodic, and is **not constant**. The exact weak-return asymptotic is

\[
\boxed{v(r)=\frac{c^s}{1-\rho}\,\frac{r^{1-s}}{\Theta_s(\log_f(c/r))}\,[1+o(1)]\qquad(r\downarrow0).}
\]

The phase argument can be taken modulo one. In particular, along the rates \(r_{n,y}=c f^{-(n+y)}\), with fixed \(y\in[0,1)\),

\[
\lim_{n\to\infty}\frac{v(r_{n,y})}{r_{n,y}^{1-s}}=\frac{c^s}{(1-\rho)\Theta_s(y)}.
\]

Since \(\Theta_s\) is nonconstant, there is no single phase-independent limiting prefactor for the normalized fractional power. At the exact trapping boundary \(\rho=1/f\),

\[
\boxed{v(r)=\frac{(\alpha-\beta)\log f}{\log(c/r)}\left[1+O\!\left(\frac1{\log(c/r)}\right)\right]\qquad(r\downarrow0).}
\]

At \(r=0\), the thermodynamic backbone speed is zero for every \(\rho\ge1/f\). At each strictly positive \(r\), the thermodynamic speed is strictly positive.

## Assumptions and scope

The backbone is a ring of \(N\ge3\) sites, with one outward branch of integer length \(L_i\ge0\) attached to each backbone site. Backbone jumps one site to the right and left occur at respective rates \(\alpha\) and \(\beta\); on every branch, jumps away from and toward the backbone have the same respective rates. The last branch site reflects, and there is no exclusion or interaction between particles. Every branch site independently undergoes a Poisson jump at rate \(r\) directly to its own junction. A reset attempted at a backbone site changes nothing. The displacement counts only unwrapped backbone jumps, not branch excursions or direct returns. The independent quenched lengths have the geometric law stated above. For each \(r\), first take the stationary state of each finite ring, then \(N\to\infty\) for a typical length realization, and only then let \(r\downarrow0\). No simultaneous volume/rate scaling is asserted.

## Proof

**1. Stationary one-branch equation.** Normalize the stationary probability at the junction to \(p_0=1\), and write \(p_m\) for the relative probability at depth \(m\) of a branch of length \(L\). At interior depths,

\[
\alpha p_{m-1}+\beta p_{m+1}-(\alpha+\beta+r)p_m=0,\qquad 1\le m<L,
\]

while the reflecting end obeys \(\alpha p_{L-1}=(\beta+r)p_L\). Set

\[
 u(r)=\frac{\alpha+\beta+r-\sqrt{(\alpha+\beta+r)^2-4\alpha\beta}}{2\beta},\quad
 w(r)=\frac{\alpha+\beta+r+\sqrt{(\alpha+\beta+r)^2-4\alpha\beta}}{2\beta}.
\]

Then \(0<u<1<f<w\) and \(p_m=A u^m+B w^m\). Extending the terminal recurrence by \(p_{L+1}=f p_L\) imposes zero current beyond the reflecting end. With

\[
q=\frac wu>1,\qquad T=\frac{\alpha-\beta u}{\beta w-\alpha}>0,\qquad b=\frac{\alpha-\beta u}{r},
\]

this boundary condition gives \(B/A=Tq^{-L}\). Summing the stationary flux balances over the branch yields \(r\sum_{m=1}^Lp_m=\alpha-\beta p_1\). Therefore the **exact finite-branch occupation ratio** is

\[
\boxed{\Delta_L(r):=\sum_{m=1}^Lp_m=b\,\frac{1-q^{-L}}{1+Tq^{-L}}.}\tag{1}
\]

The right side also vanishes at \(L=0\), so the formula covers empty branches. Direct expansion of the roots at \(r=0\) gives

\[
q=f+O(r),\qquad T=\frac cr[1+O(r)],\qquad b=\frac{\alpha-\beta}{r}+O(1),\tag{2}
\]

with dimensionless relative errors understood at fixed positive \(\alpha,\beta\). At fixed \(L\), equation (1) converges to \(\frac{f}{f-1}(f^L-1)\).

**2. Exact finite-volume transport and infinite volume.** Summing the stationary master equations over the depths of each branch cancels the internal branch flux and returns, leaving the biased nearest-neighbor stationarity equation on the backbone ring. Its unique positive solution has equal junction probabilities. Normalization therefore gives

\[
v_N(r)=\frac{\alpha-\beta}{1+N^{-1}\sum_{i=1}^N\Delta_{L_i}(r)}.\tag{3}
\]

Equation (1) gives \(0\le\Delta_L(r)\le b\) for every \(L\), so the strong law applies for each \(r>0\). Consequently,

\[
v(r)=\frac{\alpha-\beta}{1+E_r},\qquad
E_r=(1-\rho)b\sum_{L=0}^{\infty}\rho^L\frac{1-q^{-L}}{1+Tq^{-L}}.\tag{4}
\]

For \(r=0\), stationary branch occupation equals \(\frac{f}{f-1}(f^L-1)\). Its expectation diverges precisely when \(\rho f\ge1\). The truncated strong law then forces the finite-volume drift in (3) to tend to zero almost surely. This establishes the trapping boundary and the order of limits.

**3. Fractional-power, oscillatory onset.** Suppose \(\rho f>1\), and write \(s=-\log\rho/\log f\in(0,1)\). Define \(k=\lfloor\log_q T\rfloor\) and \(y=\log_qT-k\in[0,1)\). Substituting \(L=k+j\) in (4), and using \(\rho^k=T^{-s_r}\rho^{-y}\), where \(s_r=-\log\rho/\log q\), gives the exact identity

\[
\frac{E_r}{(1-\rho)bT^{-s_r}}
=\rho^{-y}\sum_{j=-k}^{\infty}
\rho^j\frac{1-q^{y-j}/T}{1+q^{y-j}}.\tag{5}
\]

As \(r\downarrow0\), one has \(k\to\infty\), \(q\to f\) and \(s_r\to s\). Terms with \(j\) large and positive are dominated by a geometric multiple of \(\rho^j\); terms with \(j\) large and negative are dominated by a geometric multiple of \((\rho q)^j\). Because \(\rho q>1\) uniformly near zero return rate, the two tails vanish uniformly in \(y\). On every fixed finite band of indices, the summands converge uniformly. Thus the right side of (5) equals \(\Theta_s(y)+o(1)\) uniformly in \(y\). From (2),

\[
T^{-s_r}=(r/c)^s[1+o(1)],\qquad
\log_qT-\log_f(c/r)=o(1).
\]

Periodicity and uniform continuity of \(\Theta_s\) now give

\[
E_r=(1-\rho)(\alpha-\beta)c^{-s}r^{s-1}\Theta_s(\log_f(c/r))[1+o(1)].
\]

Since \(s<1\), \(E_r\to\infty\), and substitution in (4) proves the asserted fractional-power formula.

To show that the modulation is genuinely nonconstant, periodize \(h(x)=f^{sx}/(1+f^x)\). The \(n\)-th Fourier coefficient of \(\Theta_s\), for every integer \(n\), is the convergent Euler beta integral

\[
\widehat\Theta_s(n)
=\int_{-\infty}^{\infty}\frac{f^{sx}e^{-2\pi i n x}}{1+f^x}\,dx
=\frac{\pi}{(\log f)\sin\!\left(\pi s-\frac{2\pi^2 i n}{\log f}\right)}.\tag{6}
\]

For \(n=1\), this coefficient is nonzero, because \(0<s<1\). Hence \(\Theta_s\) cannot be constant.

**4. Critical inverse logarithm.** Let \(\rho=1/f\). Equation (4) together with (2) implies

\[
E_r=(1-f^{-1})b\sum_{L\ge0}\frac{1}{f^L+T}+O(1).\tag{7}
\]

For clarity, dropping the factor \(1-q^{-L}\) changes (4) by at most \((1-\rho)b/T=O(1)\). Replacing \(q\) with \(f\) changes it by \(O(1)\), because the derivative of \(1/(1+Tq^{-L})\) with respect to \(\log q\) has absolute value at most \(L/4\), the geometric law has finite mean, and \(\log q-\log f=O(r)\) while \(b=O(r^{-1})\). Thus (7) has a uniform bounded error.

For \(T\to\infty\), splitting the sum at \(\lfloor\log_fT\rfloor\) gives

\[
\sum_{L\ge0}\frac{1}{f^L+T}
=\frac{\log_fT}{T}+O(T^{-1}).\tag{8}
\]

Indeed, each of the terms below the cutoff differs from \(T^{-1}\) by a summable geometric error of total order \(T^{-1}\), and the upper tail is also of that order. Finally \((1-f^{-1})b/T=1+O(r)\), so

\[
E_r=\frac{\log(c/r)}{\log f}+O(1).
\]

Inserting this in (4) proves the asserted critical inverse-logarithmic drift asymptotic.

## Verification

The standalone `check_comb.py` uses the Python standard library only. It separately solves finite branch stationary equations over exact rational numbers and compares their occupation masses with (1), then builds and solves the full stationary master equation on a heterogeneous four-junction comb and checks (3). It also evaluates the geometric disorder sum at high decimal precision for separated logarithmic phases and rates approaching zero, and tests the critical coefficient at several decades. On the packaged code the checker reports 36 passed assertions. For \(\alpha=100\), \(\beta=1\), and \(\rho=1/10\), the modulation is visibly nonconstant: \(\Theta_{1/2}(0)\approx0.7202400\) and \(\Theta_{1/2}(1/2)\approx0.6451692\). These finite checks are diagnostics, not a replacement for the uniform asymptotic proof or Fourier argument.

Reproduce using `python3 check_comb.py` from a directory containing this result and the script.

## Relationship to prior work

Sarkar and Gupta, arXiv:2205.15232 (first publicly posted 2022-05-30), establish the exact stationary backbone drift on random combs with arbitrary tooth-length laws and resetting, including the speed-zero trapping criterion and fixed-length weak-rate expansion. Their exact stationary representation is the starting point here; neither the stationary formula nor the trapping threshold is claimed as new. The result above identifies the **singular weak-reset scaling in the infinite-volume geometric disorder ensemble**, including its nonconstant log-periodic amplitude and the critical inverse-logarithmic law. A fixed-tooth expansion cannot be averaged termwise in this regime because its moments diverge.

Kotak and Barma, arXiv:2204.05357, study transit-time fluctuations and trapping thresholds for biased walks on random combs **without** Poisson returns. Masó-Puigdellosas, Sandev, and Méndez, *Entropy* 25 (2023), article 1529, analyze resetting on comb-like structures with continuous-time-random-walk fingers rather than a biased random-length geometric comb. These works supply related phenomena, not an identified proof of the displayed onset laws.

## Limitations

The theorem takes the stationary finite-volume limit first, the thermodynamic number-of-branches limit second, and the zero-return limit last. It assumes a geometric **integer** tooth-length law, a single constant bias shared by backbone and teeth, strictly positive rates \(\alpha>\beta\), independent branches, and instantaneous returns from each tooth to its own junction. It makes no claim about simultaneous finite-size/weak-return scaling, other disorder tails, interacting walkers, non-Poisson returns, or the size of finite-rate error constants uniform in \(f\). The log-periodic modulation can be exponentially small when \(f\) approaches one and is not asserted to be experimentally resolved in noisy data. Publication-priority novelty is assessed against available primary literature and remains subject to independent review.

## References

1. M. Sarkar and S. Gupta, “Biased random walk on random networks in presence of stochastic resetting: Exact results,” arXiv:2205.15232, first posted 2022-05-30, https://arxiv.org/abs/2205.15232 ; *Journal of Physics A* 55 (2022), 42LT01, https://doi.org/10.1088/1751-8121/ac9656.
2. J. D. Kotak and M. Barma, “Bias induced drift and trapping on random combs and the Bethe lattice: Fluctuation regime and first order phase transitions,” arXiv:2204.05357, first posted 2022-04-11, https://arxiv.org/abs/2204.05357 ; *Physica A* 597 (2022), 127311.
3. A. Masó-Puigdellosas, T. Sandev and V. Méndez, “Random Walks on Comb-like Structures under Stochastic Resetting,” *Entropy* 25 (2023), 1529, https://doi.org/10.3390/e25111529.
4. Euler's beta integral, \(\int_0^\infty t^{z-1}/(1+t)\,dt=\pi/\sin(\pi z)\) for \(0<\operatorname{Re}z<1\), a classical identity used in equation (6).
