# Critical-loss exponential rate for the careless coupon collector

## Finding

In the post-loss careless coupon collector, one of \(n\) types is sampled uniformly and made present each round; every currently present type, including the sampled one, is then independently erased with probability \(p\). Starting with no types present, let \(T_{n,p}\) be the first round whose **post-erasure** collection contains every type. For every fixed \(c>0\), with \(p=c/n\) and integer \(n>c\),

\[
\lim_{n\to\infty}\frac1n\log\mathbb E T_{n,c/n}
= I(c):=\int_0^1\log\left(1+\frac{e^{cx}-1}{x}\right)\,dx,
\]

where the continuous value of the integrand at \(x=0\) is \(\log(1+c)\). This rate is **strictly greater** than \(\log(1+c)\) for every \(c>0\): the asymptotic completion time is exponentially larger than the prediction obtained by treating stationary one-type presences as independent.

The argument also gives the **exact finite stationary all-present mass** for all \(n\ge1\) and \(0<p<1\): with \(q=1-p\),

\[
\pi_{n,p}=\prod_{k=1}^{n}
\frac{kq^{k}}{n-(n-k)q^{k}}.
\]

More generally, for each fixed set \(A\subseteq[n]\) of size \(k\), its stationary inclusion probability is \(a_{n,k}=\prod_{j=1}^{k} jq^j/[n-(n-j)q^j]\), with \(a_{n,0}=1\). Thus, writing \(K\) for the number present at stationarity, its full distribution can be recovered exactly by

\[
\Pr(K=j)=\sum_{k=j}^{n}(-1)^{k-j}\binom{k}{j}\binom{n}{k}a_{n,k}
\qquad(0\le j\le n).
\]

For any \(n\) and \(p\) with \(\pi_{n,p}\le1/4\), a quantitative connection to the first completion time is

\[
\frac1{4\pi_{n,p}}\le \mathbb E T_{n,p}\le
\frac2{\pi_{n,p}}
\left\lceil\frac{\log(2n/\pi_{n,p})}{-\log(1-p)}\right\rceil.
\]

## Assumptions and scope

The chain evolves on subsets of \([n]=\{1,\ldots,n\}\). Precisely, \(S_0=\varnothing\), \(C_t\) is independently uniform on \([n]\), \(L_{i,t}\) are mutually independent Bernoulli\((p)\) erasure indicators independent of all draws, and

\[
S_{t+1}=(S_t\cup\{C_t\})\setminus\{i:L_{i,t}=1\}.
\]

Completion is checked **after** erasure; checking before erasure changes the law. The finite stationary formulas hold for each \(n\ge1\), \(0<p<1\). The limiting theorem holds for each fixed real \(c>0\) along all integers \(n>c\); no limit uniform in \(c\), prefactor asymptotic, or distributional limit for \(T_{n,c/n}\) is asserted. The primary subject is finite Markov chains and their rare hitting times (MSC2020 60J10).

## Proof

**1. Unique invariant measure and inclusion recurrence.** For \(0<p<1\), every set can reach the empty set by erasing all currently held types, and the empty set can reach every prescribed set through a positive-probability sequence of distinct draws without erasures. The empty set has a self-loop; the finite set-valued chain is irreducible and aperiodic, hence has a unique stationary law. Permutation symmetry makes the probability that a fixed \(k\)-set \(A\) is contained in the stationary collection depend only on \(k\); denote it by \(a_{n,k}\), with \(a_{n,0}=1\).

If the next sampled type is outside \(A\), an event of probability \(1-k/n\), all \(k\) types of \(A\) must already be present and survive, with conditional probability \(q^ka_{n,k}\). If the sample is in \(A\), with probability \(k/n\), that sampled type is restored regardless of its previous state; the remaining \(k-1\) must already be present, and all \(k\) must survive. Thus stationarity gives the *exact* identity

\[
a_{n,k}=q^k\left[(1-k/n)a_{n,k}+(k/n)a_{n,k-1}\right].
\]

The denominator \(1-(1-k/n)q^k\) is strictly positive. Solving recursively proves the stated product. In particular, the event that **all** types are present has stationary probability \(a_{n,n}=\pi_{n,p}\). Since \(\mathbb E\binom Kk=\binom nk a_{n,k}\), expansion of \(\mathbb E z^K\) in powers of \(z-1\) gives the distributional inversion displayed in the finding.

**2. Two-sided hitting-time comparison.** Couple a chain from the empty set and another from its stationary law using the same draws and erasure indicators. Because the update preserves subset inclusion, the empty-start chain remains a subset of the stationary chain. Hence for every integer \(t\ge0\),

\[
\Pr_{\varnothing}(S_t=[n])\le\pi_{n,p}.
\]

By a union bound \(\Pr_{\varnothing}(T_{n,p}\le t)\le t\pi_{n,p}\) for positive integer \(t\) (the time-zero state is empty when \(n\ge1\)). If \(\pi_{n,p}\le1/4\), summing \(\Pr(T_{n,p}>t)\ge1-t\pi_{n,p}\ge1/2\) through \(\lfloor(2\pi_{n,p})^{-1}\rfloor\) gives \(\mathbb E T_{n,p}\ge1/(4\pi_{n,p})\).

For an arbitrary initial set \(B\), couple its trajectory with a stationary-start chain using common draws and erasures. A discrepancy at a given type cannot persist if that type is either drawn or erased; in particular, it survives through \(t\) steps with probability at most \(q^t\). Union bounding over the \(n\) types yields the **uniform total-variation estimate**

\[
\sup_B\lVert\mathcal L_B(S_t)-\pi\rVert_{\rm TV}\le nq^t.
\]

Set \(b=\lceil\log(2n/\pi_{n,p})/(-\log q)\rceil\). Uniformly in the starting state, \(\Pr(S_b=[n])\ge\pi_{n,p}/2\). By the Markov property, the probability of no completion by time \(mb\) is at most \((1-\pi_{n,p}/2)^m\). Summing the resulting block-tail bound gives \(\mathbb E T_{n,p}\le2b/\pi_{n,p}\). All these are finite-horizon inequalities with no independence assumption between successive occupancy states.

**3. The critical exponential rate.** Fix \(c>0\), let \(p_n=c/n\), \(q_n=1-c/n\) for \(n>c\), and put \(d_n=-n\log q_n\). Then \(d_n\to c\) and the exact stationary formula rewrites as

\[
-\frac1n\log\pi_{n,p_n}
=\frac1n\sum_{k=1}^{n} f_{d_n}(k/n),\qquad
f_d(x)=\log\left(1+\frac{e^{dx}-1}{x}\right),
\]

with \(f_d(0)=\log(1+d)\). On a compact interval containing \(c\), the family \(f_d\) is jointly continuous on \([0,1]\), including at \(x=0\), and thus uniformly continuous. Therefore the sums are Riemann sums converging to \(I(c)=\int_0^1f_c(x)\,dx\). Moreover, \(I(c)>0\), so \(\pi_{n,p_n}\to0\) exponentially. The hitting-time inequalities apply for large \(n\). Since \(-\log q_n\sim c/n\), the block length \(b\) above is \(O(n^2)\); its logarithm is \(o(n)\). Consequently both logarithmic bounds for \(\mathbb E T_{n,p_n}\), divided by \(n\), converge to \(I(c)\).

**4. Strict deviation from the marginal heuristic.** The exact one-type stationary inclusion probability is

\[
a_{n,1}=\frac{1-p}{1+(n-1)p}\longrightarrow\frac1{1+c}.
\]

For \(x>0\), \(e^{cx}-1>cx\), hence \(f_c(x)>\log(1+c)\). Integrating proves \(I(c)>\log(1+c)\) strictly. This compares the correct rare-completion exponent with the exponent of the independent-one-type-presence approximation, not with a proved matching lower bound in the prior literature. \(\square\)

## Verification

The accompanying standalone `checker.py` uses only the Python standard library. For \(n\le7\) and several rational erasure probabilities, it independently solves the invariant distribution of the **count** Markov chain using exact fractions and compares every binomial moment with the product recurrence. For \(n\le4\), it separately constructs and solves the original **set-valued** chain. Its numerical diagnostic computes the rate integral and its Riemann approximants for five fixed values of \(c\). All 491 programmed finite assertions passed. The code is not an asymptotic proof; the full argument is given above.

For example, at \(c=1\), numerical quadrature gives \(I(1)\approx0.836727862260\), whereas the product-marginal rate is \(\log2\approx0.693147180560\). A direct exact count-chain calculation at \(n=10\), \(p=1/10\), gives \(\pi_{n,p}\approx0.0001331794519\) and \(\mathbb E T_{n,p}\approx12031.50\), consistent with the stated exponential order but insufficient by itself to establish it.

Reproduction: execute `python3 checker.py` with a standard Python 3 installation. No downloaded data, nonstandard dependencies, or external computational certificates are required.

## Relationship to prior work

Cruciani and Dudeja (arXiv:2602.20705, Sections 3–4) introduce this exact post-loss process, prove metastability and general hitting-time bounds, and describe matching the product-marginal lower bound as a future challenge. Their bound \(q_*^{-n}\), where \(q_*=(1-p)/(1+(n-1)p)\), is not a sharp exponential-scale estimate for \(p=c/n\). Their finite algorithm computes the expected hitting time but does not state the integral rate above.

Long (arXiv:2605.14511, Sections 5.1–5.5 and Remark 5.16) proves sharp stationary-entry and hitting-time asymptotics for **fixed** \(p\in(0,1)\), showing that the product-marginal heuristic fails there. This is a close methodological precedent, but those fixed-parameter asymptotics cannot be specialized to \(p=c/n\) without a uniform theorem; that scaling changes the order of the rare-event exponent. The present stationary inclusion recursion gives an exact finite formula and a separate critical-loss proof. Long's deterministic-expiration collector (arXiv:2604.26298) has a different sliding-window update and different rare-event probability. Standard finite-state coupling and moment inversion are used as methods, not claimed as inventions.

## Limitations

The proved completion-time statement identifies the exponential rate of the **mean**, not its multiplicative prefactor or the weak limit of the normalized hitting time. In particular, the proof's polynomial-factor upper bound is not an asymptotic equivalence. The statement requires uniform sampling, independent losses with a common probability, the post-loss observation convention, and fixed \(c>0\). There is no extension asserted to heterogeneous losses, nonuniform sampling, pre-loss checking, or regimes in which \(np_n\) does not converge to a fixed positive constant. Independent historical priority verification remains outstanding, including the possibility that a broad cache-thinning or finite-chain occupation identity implicitly includes part of the stationary product formula.

## References

1. E. Cruciani and A. Dudeja, *The Careless Coupon Collector's Problem*, arXiv:2602.20705v1 (first posted 2026-02-24), https://arxiv.org/abs/2602.20705 ; also FUN 2026, DOI:10.4230/LIPIcs.FUN.2026.14.
2. C. D. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors*, arXiv:2605.14511 (first posted 2026-05-14), https://arxiv.org/abs/2605.14511 .
3. C. D. Long, *The Expiring Coupon Collector: Sliding-Window Surjection Flux and Rare-Entry Laws*, arXiv:2604.26298 (first posted 2026-04-29), https://arxiv.org/abs/2604.26298 .
