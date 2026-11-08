# Distinct endpoint slopes for eventual and eternal leadership in recursive-tree percolation

## Finding
Consider a growing uniform random recursive tree with independent bond retention probability \(p\in(0,1]\). The root component wins ties against later components. Write \(\rho(p)\) for the probability that the root component is a largest component at **every** finite growth time, and write \(\theta(p)\) for the limit of the probability that it is a largest component at a single time \(n\), as \(n\to\infty\). Both functions and their qualitative continuity were studied by Zheng [1].

**Theorem (two distinct sharp endpoint slopes).** In the iterated regime where the graph-size limit in \(\theta\) is taken first and then \(p\uparrow1\),
\[
\lim_{p\uparrow1}\frac{1-\rho(p)}{1-p}=\frac32,
\qquad
\lim_{p\uparrow1}\frac{1-\theta(p)}{1-p}=1.
\]
Consequently,
\[
\theta(p)-\rho(p)=\frac12(1-p)+o(1-p),\qquad p\uparrow1.
\]
Thus a loss of leadership that is subsequently reversed contributes a strictly positive first-order fraction of the near-deterministic failure probability.

## Assumptions and scope
At time \(n=1\), there is one rooted vertex. At each time \(n+1\), a new vertex attaches to a uniformly chosen previous vertex, and the new edge is independently retained with probability \(p\). The resulting connected components are labeled by their creation times. A component wins a size tie against a later-born component. Equivalently, in the Simon-type restaurant representation [1], a new customer opens a new table with probability \(\varepsilon=1-p\), and otherwise joins existing table \(i\) with conditional probability equal to its occupancy divided by \(n\). The root component is table 1. All subsequent probabilities are with respect to this infinite, canonically coupled growth process. The result is for \(p\uparrow1\) from below, not for a simultaneous scaling \(p=p_n\) with \(n\).

## Proof
**1. Exact competition with a single new table.** Condition on a new table being born when table 1 has occupancy \(r\ge1\). Erasing times at which neither of these two tables gains a customer produces the classical two-color Pólya urn with initial occupancies \((r,1)\): whenever either table is chosen, the conditional probabilities are proportional to their current sizes. There are almost surely infinitely many such choices for every \(p>0\), since the conditional probability of choosing table 1 at step \(n+1\) is at least \(p/n\) and conditional Borel–Cantelli applies. The Pólya urn has a directing variable \(X\sim\operatorname{Beta}(1,r)\) for the limiting share of the new table in the pair.

The probability that the new table has a *larger eventual share* than table 1 is
\[
 h_r=\Pr(X>1/2)=2^{-r}.
\]
The probability that it is *strictly larger at least once* is computed conditional on \(X=x\). Initially the root leads by \(r-1\), so for \(x<1/2\) the chance that the biased nearest-neighbor difference walk ever reaches a lead of one for the new table is \((x/(1-x))^r\); for \(x\ge1/2\) that chance is one. Integrating against the Beta density gives
\[
 g_r=2^{-r}+r\int_0^{1/2}\frac{x^r}{1-x}\,dx
 =2^{-r}+r\sum_{k=r+1}^{\infty}\frac{2^{-k}}{k},
 \qquad h_r\le g_r<2^{1-r}.
\]
These exact conditional probabilities do not depend on \(p>0\). The last strict bound follows by using \(1/(1-x)\le2\) on \([0,1/2]\).

**2. The first-order effect of finitely many possible births.** Index potential new-table births by their *arrival time* \(j\ge2\), rather than by their table number. Let \(R_n\) be the occupancy of table 1 after \(n\) customers. Let \(F_j^{\mathrm{ever}}\) mean that a new table is born at time \(j\) and subsequently strictly exceeds table 1 at least once. Let \(F_j^{\mathrm{lim}}\) mean the same birth but with eventual relative share exceeding one-half. The exact conditioning in Step 1 yields
\[
 \Pr(F_j^{\mathrm{ever}})=\varepsilon\,\mathbb E[g_{R_{j-1}}],
 \qquad
 \Pr(F_j^{\mathrm{lim}})=\varepsilon\,\mathbb E[h_{R_{j-1}}].
\]
For each fixed \(j\), \(R_{j-1}\to j-1\) in probability as \(p\uparrow1\). Moreover, for distinct fixed \(j,k\), either type of intersection \(F_j\cap F_k\) requires two independent new-table births and hence has probability at most \(\varepsilon^2\). Therefore, for every fixed \(J\),
\[
 \frac{\Pr(\bigcup_{j=2}^J F_j^{\mathrm{ever}})}{\varepsilon}\longrightarrow \sum_{r=1}^{J-1}g_r,
 \qquad
 \frac{\Pr(\bigcup_{j=2}^J F_j^{\mathrm{lim}})}{\varepsilon}\longrightarrow \sum_{r=1}^{J-1}h_r.
\]

**3. Uniform control of all later births.** The following estimate works for either event type, since both conditional probabilities are bounded by \(2^{1-r}\). Fix \(p\ge1/2\) and an integer \(J\ge8\). Let \(A_J\) be the event that no new table is born at times \(2,\ldots,J\); on \(A_J\), \(R_J=J\). The root-selection probability at step \(n+1\) is \(pR_n/n\ge J/(2n)\) for all \(n\ge J\). Coupling its selections from below by independent Bernoulli variables of parameters \(J/(2n)\) gives
\[
 \mathbb E[2^{-R_n}\mid A_J]
 \le2^{-J}\prod_{k=J}^{n-1}\left(1-\frac{J}{4k}\right)
 \le2^{-J}(J/n)^{J/4},\qquad n\ge J.
\]
A union bound over births at times greater than \(J\) then yields
\[
 \Pr\left(\bigcup_{j>J}F_j\,\middle|\,A_J\right)
 \le\varepsilon\,2^{1-J}\left(1+\frac{J}{J/4-1}\right).
 \tag{1}
\]

It remains essential to handle \(A_J^c\), rather than silently discarding early births. **Finite-history late-birth lemma:** for every fixed state of the restaurant after time \(J\), the probability that *some table newly born after \(J\)* ever exceeds table 1 tends to zero as \(p\uparrow1\). To prove this, fix \(\delta>0\) and \(K\ge8\). At \(p=1\), starting from that fixed state, the root-table occupancy tends to infinity almost surely by the ordinary finite-color Pólya-urn law (its limiting share is positive almost surely). Choose a finite \(m>J\) with \(\Pr_{p=1}(R_m<K)<\delta\). Because the law through a fixed time \(m\) is continuous in \(p\), this probability is below \(2\delta\) for \(p\) close to one. The chance of a new table in times \(J+1,\ldots,m\) is at most \((m-J)\varepsilon\). Conditional on \(R_m\ge K\), repeat the coupling preceding (1), with initial lower count \(K\) at time \(m\), to bound all later new-table takeovers by
\[
 \varepsilon\,2^{1-K}\left(1+\frac{m}{K/4-1}\right).
\]
Thus the late-birth probability has \(\limsup_{p\uparrow1}\) at most \(2\delta\), and \(\delta\downarrow0\) proves the lemma. There are only finitely many possible occupancy states at fixed time \(J\), so the conclusion is uniform over these states. Since \(\Pr(A_J^c)\le(J-1)\varepsilon\), the contribution of \(A_J^c\) to the probability of a late challenger is \(o(\varepsilon)\). Together with (1), for either event type,
\[
 \limsup_{p\uparrow1}\frac{\Pr(\bigcup_{j>J} F_j)}{\varepsilon}
 \le 2^{1-J}\left(1+\frac{J}{J/4-1}\right)\longrightarrow0
 \quad(J\to\infty).
\]
This justifies taking the infinite union *after* the first-order limit in Step 2.

**4. Identify and squeeze both leadership failures.** The event \(1-\rho(p)\) is exactly \(\bigcup_{j\ge2}F_j^{\mathrm{ever}}\), because the oldest component wins every tie. For the one-time limit \(\theta(p)\), it is not necessary to assume an interchange of an infinite maximum with an infinite-time limit. Fix \(J\). At time \(n\ge J\), let \(B_{n,J}\) denote the event that some table *born at an arrival time* \(2\le j\le J\) strictly exceeds table 1. The individual relative Pólya ratios converge almost surely to continuous Beta limits, hence \(\mathbf1_{B_{n,J}}\to\mathbf1_{\cup_{j=2}^J F_j^{\mathrm{lim}}}\) almost surely as \(n\to\infty\). Since every other possible component must have been born at an arrival time greater than \(J\),
\[
 \Pr\left(\bigcup_{j=2}^J F_j^{\mathrm{lim}}\right)
 \le 1-\theta(p)
 \le \Pr\left(\bigcup_{j=2}^J F_j^{\mathrm{lim}}\right)
 +\Pr\left(\bigcup_{j>J}F_j^{\mathrm{ever}}\right).
\]
The existence of \(\theta(p)\) is an established fixed-parameter fact [1]; this finite-family squeeze and Step 3 suffice for its endpoint coefficient without invoking a full cluster-size limit theorem. The corresponding exact union for \(\rho(p)\) is treated identically by Step 3.

Finally, monotone interchange of the positive sums gives
\[
 \sum_{r=1}^{\infty}h_r=1,
 \qquad
 \sum_{r=1}^{\infty}(g_r-h_r)
 =\sum_{k=2}^{\infty}\frac{2^{-k}}{k}\sum_{r=1}^{k-1}r
 =\frac12\sum_{k=2}^{\infty}(k-1)2^{-k}=\frac12.
\]
Consequently \(\sum_{r\ge1}g_r=3/2\), proving the theorem.

## Verification
The independent finite-time verifier `verify_endpoint.py` exhaustively enumerates all uniform recursive-tree parent histories through eight vertices under one deleted edge, checks their exact first-order leadership-failure coefficients against a separate rational Pólya-urn dynamic program, and confirms that the finite-horizon coefficients increase toward the two claimed limits. It also checks the beta/gambler formula at small initial states and the exponential bounds used above. These finite checks are diagnostics only; the infinite union, endpoint limit and absence of omitted late competitors are proved analytically in Steps 1–4.

## Relationship to prior work
Zheng [1] establishes the restaurant representation, strict positivity, monotonicity and continuity of both leadership probabilities. The present statement adds explicit, unequal one-sided derivatives at perfect retention and a first-order transient-leadership gap. The two-color Beta mixture is classical; novelty is claimed only for the exact joint endpoint sensitivity of the *infinite* recursive-tree leadership events and its justified infinite-challenger tail. Baur [2] studies the distinct regime in which retention varies with growing tree size; that does not imply the iterated fixed-parameter endpoint slopes here. The full text of [1] was not accessible for a complete line-by-line priority comparison; its verified abstract and available detailed descriptions establish qualitative statements but not these numerical derivatives. Independent priority assessment is still appropriate.

## Limitations
No exact formula for \(\rho(p)\) or \(\theta(p)\) away from \(p=1\) is proved. No second-order remainder or uniform joint \(n,p\) scaling is claimed. The proof uses the established existence of the fixed-parameter one-time limit \(\theta(p)\) [1], but derives its endpoint coefficient from a finite-family squeeze without assuming a global limit-max interchange. Verification scripts check finite instances, not arbitrary time or all parameter values. The possibility of an equivalent endpoint derivative in inaccessible full-text literature remains a residual priority risk.

## References
[1] Y. Zheng, *Can the root cluster remain largest forever in random recursive tree percolation?*, arXiv:2606.01881 (first submitted 2026-06-01), https://arxiv.org/abs/2606.01881.

[2] E. Baur, *Percolation on random recursive trees*, arXiv:1407.2508 (2014), https://arxiv.org/abs/1407.2508; *Random Structures & Algorithms* **48** (2016), 655–680.
