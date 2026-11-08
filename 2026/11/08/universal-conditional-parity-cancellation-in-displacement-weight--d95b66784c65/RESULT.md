# Universal conditional parity cancellation in displacement-weighted parking outcomes

## Finding
Let \(n\geq1\) cars park sequentially in \(n\) ordered spaces by the usual forward-search parking rule. Under any nonnegative per-car displacement weight \(h\) with \(h(0)>0\), weight a successful preference vector by the product of its displacement weights. Write \(\sigma\) for the final left-to-right order of car labels, \(K\) for the occupied position of the last-arriving car, and \(\varepsilon(\sigma)=(-1)^{\operatorname{inv}(\sigma)}\).

For \(r\geq1\), put \(F(r)=\sum_{d=0}^{r-1}h(d)\), and define the positive numbers
\[
T_m=\sum_{\tau\in\mathfrak S_m}\prod_{i=1}^mF(\ell_i(\tau)),\qquad
A_m=\sum_{\tau\in\mathfrak S_m}(-1)^{\operatorname{inv}(\tau)}\prod_{i=1}^mF(\ell_i(\tau)),
\]
with \(T_0=A_0=1\); \(\ell_i(\tau)\) is the largest length of a contiguous interval ending at position \(i\) for which \(\tau_i\) is its maximum. Define \(G(N,a)\), for \(0\leq a\leq N\), by
\[
G(N,a)=\begin{cases}
0,&N\text{ even and }a\text{ odd},\\
\displaystyle\binom{\lfloor N/2\rfloor}{\lfloor a/2\rfloor},&\text{otherwise}.
\end{cases}
\]
Then the conditional parity imbalance is exactly
\[
\boxed{\mathbb E[\varepsilon(\sigma)\mid K=k]
=(-1)^{n-k}\frac{G(n-1,k-1)}{\binom{n-1}{k-1}}
\frac{A_{k-1}A_{n-k}}{T_{k-1}T_{n-k}}},\qquad 1\leq k\leq n.
\]
In particular, **for every odd \(n\geq3\) and every even \(k\in\{2,4,\ldots,n-1\}\), the conditional outcome permutation is exactly parity-balanced:**
\[
\boxed{\mathbb P(\varepsilon(\sigma)=1\mid K=k)
=\mathbb P(\varepsilon(\sigma)=-1\mid K=k)=\tfrac12.}
\]
This holds simultaneously for uniform parking functions, every positive geometric displacement penalty, bounded-displacement variants, and arbitrary nonnegative displacement weights with \(h(0)>0\). The formula also gives all other parity imbalances by finite exact recurrences.

## Assumptions and scope
Preferences \(\alpha_1,\ldots,\alpha_n\) lie in \(\{1,\ldots,n\}\). Car \(j\) parks in the first currently unoccupied spot \(s_j\geq\alpha_j\); only preference vectors for which all cars park are retained. Each such vector has weight \(\prod_{j=1}^nh(s_j-\alpha_j)\), normalized by the sum over all successful vectors. Assume \(h:\mathbb Z_{\geq0}\to[0,\infty)\) takes finite values and \(h(0)>0\). The preference coordinates need not be identically distributed after normalization; this is a Gibbs-weighted measure on successful vectors. Every outcome permutation and every value \(K=k\) has positive total weight because the zero-displacement preference vector realizing that permutation has positive weight.

The sign concerns inversions in the **final order of the car labels** \(\sigma\), not inversions of the original preference word. No independence of the parked positions is assumed.

## Proof
**1. Factorization of a fixed outcome.** Fix a final permutation \(\sigma=(\sigma_1,\ldots,\sigma_n)\). Let \(j_i\) be the largest index \(j<i\) with \(\sigma_j>\sigma_i\), or \(0\) if there is no such index; thus \(\ell_i=i-j_i\). When car \(\sigma_i\) arrives, positions \(j_i+1,\ldots,i-1\) have already been occupied and position \(j_i\), if it exists, is still vacant. Therefore the car ends at position \(i\) precisely when its preference lies among the \(\ell_i\) positions \(j_i+1,\ldots,i\). These choices are independent **conditional on the specified outcome**, and their possible displacements are exactly \(0,\ldots,\ell_i-1\). The complete unnormalized outcome weight is consequently
\[
W_h(\sigma)=\prod_{i=1}^n F(\ell_i(\sigma)).
\]
This extends the uniform-preference fiber count, where \(F(r)=r\).

**2. Split at the last car.** Put \(a=k-1\) and \(b=n-k\). If \(\sigma_k=n\), the label \(n\) is larger than every earlier label, so \(\ell_k=k\). For each \(a\)-element subset \(S=\{s_1<\cdots<s_a\}\subseteq\{1,\ldots,n-1\}\), standardize the left and right subpermutations separately as \(\tau\in\mathfrak S_a\) and \(\upsilon\in\mathfrak S_b\). All contiguous-maximum lengths on the two sides are preserved under standardization, including those just to the right of position \(k\). Hence
\[
W_h(\sigma)=F(k)W_h(\tau)W_h(\upsilon).
\]
The inversions in \(\sigma\) are the inversions on each side, the \(b\) inversions from \(n\) to right-hand positions, and the left-right inversions. The latter have cardinality \(\sum_{j=1}^{a}(s_j-j)\). Thus
\[
(-1)^{\operatorname{inv}(\sigma)}=(-1)^b
(-1)^{\sum_j(s_j-j)}
(-1)^{\operatorname{inv}(\tau)}
(-1)^{\operatorname{inv}(\upsilon)}.
\]
The unnormalized signed and unsigned totals conditional on \(K=k\) are respectively
\[
U_{n,k}=F(k)(-1)^b A_aA_b
\sum_{\substack{S\subseteq[n-1]\\|S|=a}}(-1)^{\sum_j(s_j-j)},
\qquad
V_{n,k}=F(k)\binom{n-1}{a}T_aT_b.
\]
The positive factor \(F(k)\) cancels in the conditional ratio.

**3. Exact alternating subset sum.** For integers \(N\geq0\), \(0\leq a\leq N\), set
\[
Q(N,a)=\sum_{1\leq s_1<\cdots<s_a\leq N}(-1)^{\sum_j(s_j-j)}.
\]
The finite product identity
\[
Q(N,a)=(-1)^{a(a-1)/2}[z^a]\prod_{j=0}^{N-1}\bigl(1+(-1)^jz\bigr)
\]
follows by expanding and keeping track of the parity of \(\sum_j(s_j-j)\). For \(N=2m\) the product is \((1-z^2)^m\); for \(N=2m+1\) it is \((1+z)(1-z^2)^m\). Direct coefficient comparison yields \(Q(N,a)=G(N,a)\). Division of \(U_{n,k}\) by \(V_{n,k}\) proves the displayed conditional expectation. Since \(n\) odd means \(n-1\) even, the alternating factor is zero whenever \(k-1\) is odd. As \(\varepsilon\) takes only values \(\pm1\), zero conditional expectation is equivalent to exact equiparity.

**4. Finite recurrences and a representative specialization.** Summing the two split identities over \(k\) gives, for every \(n\geq1\),
\[
T_n=\sum_{k=1}^n F(k)\binom{n-1}{k-1}T_{k-1}T_{n-k},
\quad
A_n=\sum_{k=1}^n F(k)(-1)^{n-k}G(n-1,k-1)A_{k-1}A_{n-k}.
\]
These determine the general conditional law using only finite calculations. For unit-interval parking, take \(h(0)=h(1)=1\) and \(h(d)=0\) for \(d\geq2\); then \(F(1)=1\) and \(F(k)=2\) for \(k\geq2\). The classical ordered Bell numbers \(B_m\), with exponential generating function \(\sum_{m\geq0} B_mz^m/m!=1/(2-e^z)\), satisfy \(T_n=B_n\) and \(A_n=B_{\lceil n/2\rceil}\) (and \(A_0=B_0=1\)). Indeed, with \(E(z)=\sum_{m\geq0}A_{2m}z^m/m!\) and \(O(z)=\sum_{m\geq0}A_{2m+1}z^m/m!\), the preceding recurrence yields \(E'=O=2E^2-E\), \(E(0)=1\), hence \(E=1/(2-e^z)\). This specialization serves as a consistency check, not as a claim of new signed-Eulerian enumeration.

## Verification
The independent finite implementations in `CHECK.py` (i) enumerate full preference vectors by the parking procedure, (ii) enumerate final permutations and reconstruct their weighted preference fibers, and (iii) evaluate the signed/unsigned split recurrences. Five kernels are checked: uniform, unit-interval, linear, geometric, and a nonmonotone finite-support kernel. There are \(855\) exact assertions, including permutation orders through \(8\), direct preference orders through \(5\), and recurrence orders through \(16\). Run `python3 CHECK.py` using Python 3's standard library. The finite checks corroborate the proof and do not replace the all-\(n\) argument.

## Relationship to prior work
Pinsky (2024) explicitly derives the full permutation-outcome distribution for **uniform** parking functions, including the fixed-outcome weight \(\prod_i\ell_i\) and the distribution of the last-arriving car's parked position. These are prior results, not the present finding. The new statement is the conditional **permutation-sign decomposition for every displacement-weighting kernel**, with exact parity cancellation at half of the final-car positions for odd size. Meyles et al. (2023) characterize and enumerate unit-interval parking functions, represented here by a bounded-displacement kernel. Celano et al. (2025, revised 2026) prove a full fixed-outcome generating-function formula for interval parking functions with geometric displacement weights and arbitrary outcome statistics (their Theorem 4.3); their Theorem 4.4 and Corollary 4.8 also provide global signed inversion enumerators for unit-interval parking functions. Those are **strong prior coverage** of the underlying fiber enumeration, the geometric/bounded-weight subfamilies and the unit-interval global sign count. The remaining claim is the **explicit last-car-position conditional sign formula**, its alternating subset factor, and exact positional equiparity for arbitrary nonnegative per-displacement kernels. Neither the fixed-outcome generating function nor the unconditional signed counts as stated supplies that positional cancellation without an additional split-and-alternating-subset argument. Chebikin and Postnikov (2008) study a different inversion-like statistic on parking preferences, not this conditional final-order sign. The alternating-subset cancellation uses the classical Gaussian-binomial evaluation at \(-1\).

## Limitations
This is an exact finite-\(n\) statement for the standard forward-search rule with a product weight depending **only** on each car's final displacement. It does not cover interactions between cars, time-dependent preferences, or parking rules permitting backward motion. It does not assert that outcome parity is unconditional fair, nor that all final positions are balanced. The even/odd cancellation is robust; for other parameters, the conditional imbalance depends on \(h\) through \(A_m/T_m\). The very general fixed-outcome enumeration by Celano et al. (2025/2026) makes the present conditional result a derived structural refinement, rather than an independent enumeration of all outcome statistics. An earlier equivalent conditional-sign treatment, possibly implicit in a generating-function identity, remains a historical-priority risk. The uniform-only fiber identity, unit-interval ordered-Bell counts, and global geometric-weight signed-inversion enumerators are established prior mathematics. No independent audit is claimed.

## References
- R. G. Pinsky, *The distribution on permutations induced by a random parking function* (first posted April 17, 2024), arXiv:2404.11529, https://arxiv.org/abs/2404.11529.
- L. C. Meyles et al., *Unit-Interval Parking Functions and the Permutohedron* (first posted May 24, 2023), arXiv:2305.15554, https://arxiv.org/abs/2305.15554.
- K. Celano et al., *Statistics on ℓ-interval parking functions* (first posted July 9, 2025; revised September 19, 2026 under title *ℓ-Interval Parking Functions: Foata invariance, statistic generating functions, and ciphers*), arXiv:2507.07243, https://arxiv.org/abs/2507.07243; especially Theorems 4.3–4.4 and Corollary 4.8.
- P. E. Harris and L. Martinez, *Parking functions with a fixed set of lucky cars* (first posted October 10, 2024), arXiv:2410.08057, https://arxiv.org/abs/2410.08057.
- D. Chebikin and A. Postnikov, *Generalized parking functions, descent numbers, and chain polytopes of ribbon posets* (2008), arXiv:0806.0440, https://arxiv.org/abs/0806.0440.
- Classical Gaussian-binomial subset evaluation at \(-1\), also proved directly above.
