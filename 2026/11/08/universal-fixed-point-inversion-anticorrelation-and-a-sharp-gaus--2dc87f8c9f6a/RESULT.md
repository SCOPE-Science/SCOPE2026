# Universal fixed-point–inversion anticorrelation and a sharp Gaussian law for one-pass overhand shuffling

## Finding
For a one-pass, independently cut packet-reversal shuffle of a deck initially in increasing order, denote by \(F_n\) the number of original positions retained, and by \(I_n\) the Kendall inversion count. Independent gap probabilities, even if nonidentical, force
\[\operatorname{Cov}(F_n,I_n)<0\qquad(n\ge2).\]
When each gap is cut with the same fixed probability \(p\in(0,1)\), set \(q=1-p\). The centered vector has the nondegenerate Gaussian limit
\[\frac1{\sqrt n}\binom{F_n-np/(2-p)}{I_n-nq/p}\Longrightarrow\mathcal N_2(0,\Sigma(p)),\]
where
\[\Sigma(p)=\begin{pmatrix}\frac{4pq}{(2-p)^3}&-\frac{2q(1+q^2)}{p(2-p)^3}\\-\frac{2q(1+q^2)}{p(2-p)^3}&\frac{q(2-p)}{p^3}\end{pmatrix}.\]
Consequently
\[\lim_{n\to\infty}\operatorname{Corr}(F_n,I_n)=-\frac{1+q^2}{(1+q)^2}.\]
This expression strictly decreases as \(p\) increases, with endpoint limits \(-1/2\) and \(-1\). It is a precise dependence law between two intrinsic one-pass diagnostics: unchanged cards and pairwise inversions.

## Assumptions and scope
A deck has \(n\ge2\) ordered labeled cards. Independently for each of its \(n-1\) gaps, place a cut with probability \(p_j\in(0,1)\); reverse the card order inside each contiguous packet, but do not reorder packets. An inversion is an ordered pair of original labels appearing in reverse order; a fixed point is a card remaining at its original position. The strict finite-deck statement allows arbitrary nonidentical probabilities \(p_j\). All limit statements take \(p_j=p\) for one fixed \(p\in(0,1)\) independent of \(n\). Neither endpoint \(p=0\) nor \(p=1\) is included in the Gaussian assertion.

## Proof
**Packet reduction and strict finite-deck covariance.** If the consecutive packet lengths are \(\ell_1,\ldots,\ell_m\), packet reversal leaves exactly one fixed card in each *odd* packet and zero in each even packet; it creates exactly \(\binom{\ell_i}{2}\) inversions inside that packet and none between packets. Thus
\[F_n=\sum_{i=1}^m\mathbf1_{\{\ell_i\text{ odd}\}},\qquad I_n=\sum_{i=1}^m\binom{\ell_i}{2}.\]
Adding one new cut to split a packet of sizes \(a,b\) decreases inversions by \(ab>0\). It increases the number of fixed cards by two when both \(a,b\) are odd, and otherwise does not change it. Therefore, as functions of independent Bernoulli cut bits, \(F_n\) is coordinatewise nondecreasing and \(I_n\) is strictly decreasing in every coordinate. The elementary product-measure correlation inequality (provable by induction from conditional covariance in one coordinate) gives nonpositive covariance. It is *strictly* negative because, conditioning on all cuts except any chosen gap and taking those other gaps present, the two adjacent subpackets each have length one. On this event of strictly positive probability, varying the chosen gap changes \(F_n\) by \(+2\) and \(I_n\) by \(-1\). Conditional covariance in that bit is strictly negative; the second total-covariance term is nonpositive by the same monotonicity induction. This proves the all-\(n\) claim without identical cut probabilities.

**Regeneration and central limit theorem.** For fixed homogeneous \(p\), extend the independent gap bits to an infinite sequence and let \(T_1,T_2,\ldots\) be the i.i.d. lengths between successive cuts. Then \(\Pr(T=k)=p q^{k-1}\), \(k\ge1\). Define two packet rewards \(R=\mathbf1_{\{T\text{ odd}\}}\) and \(U=T(T-1)/2\), and let \(S_k=\sum_{i=1}^k T_i\). Their renewal-reward means per card are
\[\mu_F=\frac{\mathbb ER}{\mathbb ET}=\frac p{2-p},\qquad \mu_I=\frac{\mathbb EU}{\mathbb ET}=\frac qp.\]
Indeed \(\mathbb ET=1/p\), \(\mathbb ER=1/(1+q)\), and \(\mathbb EU=q/p^2\). For a centered reward pair \(W=(R-\mu_FT,U-\mu_IT)\), the i.i.d. multivariate central limit theorem, the renewal law \(\max\{k:S_k\le n\}/n\to1/\mathbb ET=p\), and random-time substitution yield a Gaussian limit for complete packets with covariance matrix \(\mathbb E(WW^{\mathsf T})/\mathbb ET\). The final truncated packet is the backward recurrence age; its length is stochastically dominated uniformly by a geometric variable, so its two rewards and centered length have bounded moments of every fixed order. It is therefore negligible on the \(\sqrt n\) scale. The renewal-reward CLT also yields the law of large numbers. For the covariance limits, stopped martingale second-moment identities applied at the first crossing of \(n\), plus uniform moment bounds for that crossing packet, give \(n^{-1}\operatorname{Cov}(F_n,I_n)\to\Sigma_{12}\), and similarly for the diagonal entries. This justifies convergence of correlations, not merely weak convergence.

**Explicit covariance computation.** The probability-generating functions \(\mathbb Ez^T=pz/(1-qz)\) and \(\mathbb E[z^T\mathbf1_{\{T\text{ odd}\}}]=pz/(1-q^2z^2)\) give
\[\begin{aligned}
\mathbb ET^2&=(1+q)/p^2,\\
\mathbb ET^3&=(1+4q+q^2)/p^3,\\
\mathbb ET^4&=(1+11q+11q^2+q^3)/p^4,\\
\mathbb E(TR)&=(1+q^2)/(p(1+q)^2),\\
\mathbb E(T^2R)&=(1+6q^2+q^4)/(p^2(1+q)^3).
\end{aligned}\]
Also \(\mathbb E(TU)=(\mathbb ET^3-\mathbb ET^2)/2\), and \(\mathbb EU^2=(\mathbb ET^4-2\mathbb ET^3+\mathbb ET^2)/4\). Substitute these into \(p\,\mathbb E(WW^{\mathsf T})\) to obtain the displayed matrix, including its negative cross-entry. Its determinant is strictly positive because
\[(1+q)^4-(1+q^2)^2=4q(1+q+q^2)>0.\]
After dividing the cross-entry by the two standard deviations, the limiting correlation simplifies to \(-(1+q^2)/(1+q)^2\). Its derivative with respect to \(q\) is \(2(1-q)/(1+q)^3>0\), so it decreases strictly with \(p=1-q\), and its endpoint limits follow.

## Verification
The accompanying executable \(check.py\) uses only the Python standard library. It exhausts all cut patterns through ten cards at three homogeneous rational cut probabilities, tests inhomogeneous cut probabilities through eight cards, checks the exact finite-deck inversion expectation, and independently reconstructs the rational renewal moment matrix at nine rational probabilities. It verifies 43 test suites with no failures. The finite tests do not establish the CLT; that step follows from the regenerative proof.

## Relationship to prior work
Jiang's *Cutoff for the Overhand Shuffle* (2026) introduces precisely the independent-gap packet-reversal kernel and proves the many-pass mixing cutoff, but its relevant Sections 1, 3 and appendix do not supply this one-pass fixed-point/inversion covariance or its sharp correlation formula. The classical generic central limit theory of renewal rewards and random compositions explains the Gaussian mechanism; it does not by itself supply the explicit two-statistic rational matrix or the all-finite-size strict sign for nonuniform cuts. The 2005 Bender–Canfield paper states a general multivariate CLT for composition statistics; no claim of complete novelty of the CLT method is made here. The individual combinatorial inversion and fixed-point quantities are standard; the asserted finding is their full quantitative joint dependence in this shuffle model.

## Limitations
The model is a single pass of independently cut packet reversal, not an iterated deck or an arbitrary physical overhand shuffle. The Gaussian limit assumes a *fixed* homogeneous cut probability strictly between zero and one; neither a varying-probability crossover nor a local limit theorem is claimed. The negative-covariance sign alone extends to nonuniform independent cuts; the rational matrix need not. Historical priority of the explicit covariance formula beyond the primary papers inspected remains subject to further literature checks, especially broad random-composition texts. No independent mathematical validation has been performed.

## References
1. Yunjiang Jiang, *Cutoff for the Overhand Shuffle* (2026), arXiv:2610.00137, https://arxiv.org/abs/2610.00137 (source date recorded as 2026-09-10).
2. R. Pemantle, *Randomization time for the overhand shuffle* (1989), cited in Jiang's historical discussion, https://arxiv.org/abs/2610.00137.
3. Edward A. Bender and E. Rodney Canfield, *Locally Restricted Compositions I. Restricted Adjacent Differences*, Electronic Journal of Combinatorics 12 (2005), #R57, https://doi.org/10.37236/1954.
