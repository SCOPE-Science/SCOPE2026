# A nonempty three-peak coexistence window in the reset Gillis walk

## Finding
Consider a centrally biased nearest-neighbor walk on the integer lattice. Each discrete step is replaced, independently, with probability \(r\) by an instantaneous return to the origin. Even though all resets use **one** spatial location, a weak outward bias creates a nonempty open interval of reset probabilities in which the stationary distribution has a strict **central local peak**, a dip at both nearest neighbors, and at least one **additional peak on each side**.

Precisely, for every \(-1/2<\varepsilon<0\), there are two distinct, uniquely defined transition rates \(0<r_1(\varepsilon)<r_2(\varepsilon)<1\). If \(\pi_r(n)\) denotes the stationary mass at site \(n\), then
\[
\begin{aligned}
\pi_r(1)>\pi_r(0)&\quad\Longleftrightarrow\quad r<r_1(\varepsilon),\\
\pi_r(2)>\pi_r(1)&\quad\Longleftrightarrow\quad r<r_2(\varepsilon).
\end{aligned}
\]
Consequently, throughout \(r_1<r<r_2\),
\[
\pi_r(0)>\pi_r(\pm1)<\pi_r(\pm2),
\]
with at least one finite local maximum farther out on each half-line. The two outer local maxima may form short plateaus at isolated reset probabilities; they are strict outside at most a countable set. Moreover, \(\pi_r(2)>\pi_r(0)\) on an open interval immediately above \(r_1\), so that the reset-site peak initially coexists with higher outer mass.

The thresholds are exact, not fit parameters. Put \(s=1-r\), let \(T_{j-1}\) be the first hitting time of site \(j-1\) for the **unreset** walk started from \(j\), and set
\[
w_j(s)=\mathbb E_j[s^{T_{j-1}}],\qquad j\ge1.
\]
Then \(r_1\) and \(r_2\) are the unique solutions of
\[
w_1(1-r_1)=1+\varepsilon,\qquad
w_2(1-r_2)=\frac{2+\varepsilon}{2(1-\varepsilon)}.
\]
For illustration, at \(\varepsilon=-1/4\), numerical evaluation of these exact equations gives \(r_1\approx0.007403435880\) and \(r_2\approx0.030997297563\). These decimals are diagnostic, not part of the existence proof.

## Assumptions and scope
For each nonzero integer \(n\), the unreset transition probabilities are
\[
P(n,n+1)=\frac{1-\varepsilon/n}{2},\qquad
P(n,n-1)=\frac{1+\varepsilon/n}{2};
\]
at the origin \(P(0,1)=P(0,-1)=1/2\). The bias obeys \(-1/2<\varepsilon<0\), so all probabilities are strictly between zero and one. The step kernel with complete geometric resetting is \(Q_r=sP+rR_0\), where \(R_0(x,\{0\})=1\) and \(s=1-r\). In this definition a reset **replaces** the proposed hop, rather than following it; the two conventions are not interchangeable.

The walk is on all integers. Peaks and valleys are defined with respect to the adjacent lattice sites. Every stated strict inequality holds for all rates in its specified open interval. The result gives exact sign thresholds for two adjacent comparisons, not a claim that all possible other extrema have been classified.

## Proof
**1. Unique invariant law and discounted visits.** A reset occurs with probability \(r\) independently of the current site, and therefore \(Q_r\) is uniformly regenerating. The unique invariant distribution is
\[
\pi_r(n)=r\sum_{k=0}^{\infty}s^kP^k(0,n).
\]
The series is normalized by \(r\sum_{k\ge0}s^k=1\), and total-variation contraction of initial distributions is bounded by \(s^k\). Reflection symmetry gives \(\pi_r(n)=\pi_r(-n)\), with \(\pi_r(n)>0\) at every site.

**2. Detailed balance and two exact stationary ratios.** Introduce the unnormalized reversible weights \(m_0=1\), \(m_n=m_{-n}\), and \(m_nP(n,n+1)=m_{n+1}P(n+1,n)\). The first ratios are
\[
\frac{m_1}{m_0}=\frac{1}{1+\varepsilon},\qquad
\frac{m_2}{m_1}=\frac{2(1-\varepsilon)}{2+\varepsilon}.
\]
Write \(G_s(i,j)=\sum_{k\ge0}s^kP^k(i,j)\). Reversibility gives \(G_s(0,n)=m_nG_s(n,0)\). By the strong Markov property, reaching the origin from site \(n\ge1\) requires successive first hits of \(n-1,n-2,\ldots,0\), so
\[
G_s(n,0)=\left(\prod_{j=1}^n w_j(s)\right)G_s(0,0).
\]
It follows exactly that
\[
\frac{\pi_r(1)}{\pi_r(0)}=\frac{w_1(s)}{1+\varepsilon},\qquad
\frac{\pi_r(2)}{\pi_r(1)}=\frac{2(1-\varepsilon)}{2+\varepsilon}w_2(s).
\]
This argument does not require normalizability of the unreset reversible measure.

**3. Strict, unique thresholds.** For \(-1/2<\varepsilon<0\), the unreset Gillis walk is recurrent. One direct verification uses
\[
m_n=\frac{\Gamma(1+\varepsilon)}{\Gamma(1-\varepsilon)}
\frac{n\Gamma(n-\varepsilon)}{\Gamma(n+1+\varepsilon)}
\sim \frac{\Gamma(1+\varepsilon)}{\Gamma(1-\varepsilon)}n^{-2\varepsilon}.
\]
The positive-half-line electrical resistance \(\sum_{n\ge0}[m_nP(n,n+1)]^{-1}\) diverges, proving almost-sure hitting of lower sites. Thus \(T_{j-1}<\infty\) almost surely for each fixed \(j\). Each transform \(w_j(s)=\mathbb E_j[s^{T_{j-1}}]\) is continuous and strictly increasing on \(0<s<1\), with limits zero and one at its endpoints. Since
\[
0<1+\varepsilon<1,\qquad
0<\frac{2+\varepsilon}{2(1-\varepsilon)}<1,
\]
there is exactly one solution to each threshold equation. The two ratio comparisons consequently change sign exactly once as \(r\) increases.

**4. The threshold order is strict.** At \(r=r_1\) we have \(\pi_{r_1}(0)=\pi_{r_1}(1)\). The stationary master equation at site one (which cannot receive a direct reset) is
\[
\pi_r(1)=s\left[\frac{\pi_r(0)}2+\frac{2+\varepsilon}{4}\pi_r(2)\right].
\]
Substitute equality of the first two masses to obtain
\[
\left.\frac{\pi_r(2)}{\pi_r(1)}\right|_{r=r_1}
=\frac{2(2-s)}{s(2+\varepsilon)}>1,
\]
since \(4>s(4+\varepsilon)\) for \(0<s<1\) and \(\varepsilon<0\). The second ratio is strictly decreasing as \(r\) increases and equals one precisely at \(r_2\); hence \(r_1<r_2\). At the first threshold, the last display also proves \(\pi_{r_1}(2)>\pi_{r_1}(0)\).

**5. Three spatial peaks, including a higher outer component.** For every \(r_1<r<r_2\), the ratio tests give \(\pi_r(0)>\pi_r(1)\) and \(\pi_r(2)>\pi_r(1)\); symmetry gives the analogous negative-site comparisons. Since \(\pi_r\) is a summable probability law, \(\pi_r(n)\to0\) as \(n\to\infty\). Therefore the positive half-line \(n\ge2\) has a finite attained maximum, which is a local maximum, and so does its negative reflection. Together with the strict local maximum at zero these give three spatial peaks, allowing possible plateaus at the outer modes.

For a fixed \(n\ge1\), the adjacent mass ratio \(\pi_r(n)/\pi_r(n-1)=(m_n/m_{n-1})w_n(s)\) is strictly decreasing in \(r\). Thus any adjacent equality can happen at at most one reset probability. The union over integers is countable, so the outer maxima are strict away from at most countably many rates. Finally, continuity of the invariant resolvent and \(\pi_{r_1}(2)>\pi_{r_1}(0)\) gives a nonempty right-neighborhood of \(r_1\) in which \(\pi_r(2)>\pi_r(0)>\pi_r(1)\).

**6. Evaluation without random simulation.** The transforms satisfy the backward continued-fraction equation
\[
w_j(s)=\frac{s(1+\varepsilon/j)/2}
{1-s(1-\varepsilon/j)w_{j+1}(s)/2},\qquad j\ge1.
\]
For fixed \(s<1\), backward truncation with a sufficiently far boundary approximates the bounded solution; the root equations may then be solved by bisection. This is solely a numerical aid to the exact existence-and-ordering proof.

## Verification
The standalone `verify_gillis.py` evaluates the discounted nearest-neighbor hitting transforms, checks the two threshold equations and strict ordering for five outward biases, confirms the local-peak inequalities throughout sampled coexistence windows, checks the stationary master equation, and independently iterates the reset transition kernel on a large finite window. It also checks the exactly solvable unbiased limit. The run printed `PASS: 162 deterministic tests; exact identities and finite-kernel dynamics agree.` These tests are finite diagnostics; the infinite-chain statements are proved in the preceding steps.

## Relationship to prior work
Radice, *Non-homogeneous random walks with stochastic resetting: an application to the Gillis model* (first publicly posted 2022-08-22), established resetting first-passage formulas for this same discrete walk, including exact hypergeometric hitting transforms. Those formulas supply mathematical background for the present hitting quantities but do not state or prove the two stationary **mode-comparison** thresholds or the nonempty three-peak coexistence window. Artuso, Onofri, Pozzoli and Radice (2022) derive the reset-free invariant measure in the positive-recurrent regime; here the admissible outward-biased range is reset-free null recurrent. Ray and Reuveni (2020) analyze reset diffusion in a continuous logarithmic potential, including a spatial-mode shift in a strongly repulsive half-line model. That is a distinct continuum boundary protocol, not the lattice walk that resets directly to a recurrent origin. The existence of mode shifts in related models is prior background and is not claimed here as a new general concept. The contribution is the sharp **two-threshold, three-peak coexistence statement for the specified lattice chain**, supported by a structural ratio argument.

## Limitations
The proof assumes independent complete resets that replace hops, a symmetric integer lattice, weak outward parameter \(-1/2<\varepsilon<0\), and nearest-neighbor transitions. For every rate inside the window there are at least three local maxima (counting possible equal-height outer plateaus); the proof does not enumerate all side maxima or classify the entire stationary profile. The thresholds are implicit exact values, not closed-form elementary constants. The finite computational diagnostics are not exhaustive certification, and equivalent or stronger unindexed literature could alter publication priority.

## References
1. M. Radice, *Non-homogeneous random walks with stochastic resetting: an application to the Gillis model*, arXiv:2208.10220 (first public version 2022-08-22), https://arxiv.org/abs/2208.10220. See the model in Section 1, first-passage analysis in Sections 3 and 7, and generating functions in Appendix A.
2. R. Artuso, M. Onofri, G. Pozzoli and M. Radice, *Extreme value statistics of positive recurrent centrally biased random walks*, arXiv:2207.07367 (2022), https://arxiv.org/abs/2207.07367. See Section 3.1 and its stationary measure.
3. S. Ray and S. Reuveni, *Diffusion with resetting in a logarithmic potential*, arXiv:2004.01898 (2020), https://arxiv.org/abs/2004.01898. See Section III and the continuous stationary mode analysis.
