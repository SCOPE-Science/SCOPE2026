# Critical Gaussian positive-part law for growing-cut two-sample overlap distances

## Finding

Let \(n\ge 2\), and let \(X_1,\ldots,X_n\) and \(Y_1,\ldots,Y_n\) be independent samples from the same continuous distribution. For each integer \(q\ge1\), write \(\rho_{q,n,n}\) for the OVL-\(q\) empirical overlap statistic defined below. Let \(R_n\) be the number of consecutive same-sample-label runs in the ordered pooled sample. Then
\[
\rho_{q,n,n}=0\quad\Longleftrightarrow\quad R_n\le q+1.
\]
For every \(n\) and \(q\), the exact null probability of this event is the explicitly computable runs sum given under Verification.

The more substantive statement is the **critical near-saturation law**. For any fixed \(t\in\mathbb R\), put \(q_n=\lfloor n+t\sqrt{n/2}\rfloor\) for sufficiently large \(n\). If \(Z\sim N(0,1)\), then
\[
\boxed{\sqrt n\,\rho_{q_n,n,n}\ \xrightarrow{d}\ \frac{(Z-t)_+}{2\sqrt2},\qquad
\Pr\{\rho_{q_n,n,n}=0\}\longrightarrow\Phi(t).}
\]
Here \((x)_+=\max(x,0)\), and \(\Phi\) is the standard-normal cumulative distribution function. Thus the limiting law has an atom of mass \(\Phi(t)\) at zero and a positive continuous component; at \(t=0\), the atom has mass \(1/2\). More generally, \(\Pr\{\rho_{q_n,n,n}=0\}\to0\) when \(q_n/n\to a<1\), and tends to one when \(q_n/n\to a>1\).

The mechanism is an exact local combinatorial equality, not merely a concentration approximation: if the pooled label word has \(R\) runs and \(L\) disjoint seven-letter blocks of the form \(1001001\) at prescribed disjoint locations, then for \(d=(R-1-q)_+\le 2L\),
\[
\boxed{n\rho_{q,n,n}=\left\lceil\frac d2\right\rceil.}
\]
The pattern-count condition holds with ample margin at the critical scale with probability tending to one.

## Assumptions and scope

Take \(n\) observations in each of two independent samples, with a common *continuous* cumulative distribution function (so the pooled sample has no ties almost surely). After ordering all \(2n\) observations, record a binary label word \(\gamma=(\gamma_1,\ldots,\gamma_{2n})\), where exactly \(n\) labels are zero and \(n\) are one. Its law under the null is uniform over all \(\binom{2n}{n}\) words. No finite moments or density smoothness are required.

For \(q\ge1\), the original OVL statistic is the minimum, over \(q\) nondecreasing real cutpoints (allowing empty cells), of the sum of the smaller of the two *empirical probability masses* in each of the \(q+1\) consecutive intervals. Equivalently, for cuts at pooled rank indices \(0=j_0\le j_1\le\cdots\le j_q\le j_{q+1}=2n\),
\[
\rho_{q,n,n}=\frac1n\min_{j_1,\ldots,j_q}\sum_{i=0}^{q}\min\{N_0(j_i,j_{i+1}),N_1(j_i,j_{i+1})\},
\]
where \(N_a(i,j)\) counts label \(a\) in positions \(i+1,\ldots,j\). This is the statistic of Komaba, Johno and Nakamoto, not a modified statistic. The main distributional limit concerns \(q\) growing at order \(n\), unlike fixed-\(q\) asymptotics.

## Proof

**1. Reduction to whole runs and a universal lower bound.** For a fixed label word, regard an interval's cost as \(\min\{N_0,N_1\}\). If cuts split a homogeneous run, redistribute its observations among their adjacent cells while preserving the cell order. The sum of costs is a concave, piecewise-linear function of that allocation, so its minimum over the allocation simplex occurs at a vertex: the entire run can be assigned to one cell. Repeating for all split runs produces an optimal partition using only run boundaries, possibly with repeated cuts. A cell containing \(s\ge1\) complete alternating runs has at least \(\lfloor s/2\rfloor\) observations of each of its minority-run type, and hence cost at least \(\lfloor s/2\rfloor=\lceil(s-1)/2\rceil\). If the partition has at most \(q+1\) nonempty cells, the total number of merged run boundaries is at least \(d=(R-1-q)_+\). Summation gives
\[
n\rho_{q,n,n}\ge\left\lceil\frac d2\right\rceil.
\]
The cost is exactly zero if and only if every cell is pure, which requires at least one cut between every pair of consecutive opposite-label runs. This proves \(\rho_{q,n,n}=0\) if and only if \(q\ge R-1\).

**2. Exact attainment near the run boundary.** A contiguous occurrence of \(1001001\) contains three complete, internally isolated runs \(00,1,00\); its boundary ones prevent these internal runs from extending into other blocks. Removing both cuts around its singleton run merges these three runs, removes two run boundaries, and incurs exactly one minority observation. Removing only one of those cuts removes one boundary at the same cost. Across \(L\) pairwise disjoint occurrences in predetermined nonoverlapping seven-position blocks, choose \(\lfloor d/2\rfloor\) occurrences for two-cut removal and, if \(d\) is odd, a further occurrence for one-cut removal. These edits are disjoint and incur exactly \(\lceil d/2\rceil\) minority observations. Together with Step 1 this proves the displayed exact equality whenever \(d\le2L\).

**3. Linearly many usable patterns.** Split the \(2n\) positions into \(M=\lfloor2n/7\rfloor\) disjoint consecutive blocks of length seven, and let \(L_n\) count blocks equal to \(1001001\). For the uniform balanced word, using falling factorials,
\[
\mathbb E L_n=M\frac{(n)_{\underline3}(n)_{\underline4}}{(2n)_{\underline7}},
\quad
\mathbb E[L_n(L_n-1)]=M(M-1)\frac{(n)_{\underline6}(n)_{\underline8}}{(2n)_{\underline{14}}}.
\]
For sufficiently large \(n\) these expressions are defined and the corresponding probabilities equal \(2^{-7}+O(n^{-1})\) and \(2^{-14}+O(n^{-1})\). Hence \(\operatorname{Var}(L_n)=O(n)\) and
\[
\frac{L_n}{n}\xrightarrow{P}\frac1{448}>0.
\]
No independence of blocks is assumed; the second factorial moment explicitly handles the fixed-composition dependence.

**4. Exact run counts and Gaussian fluctuations.** For \(r\ge2\), the number \(A_{n,r}\) of balanced words with exactly \(r\) runs is
\[
A_{n,2k}=2\binom{n-1}{k-1}^{\!2},\qquad
A_{n,2k+1}=2\binom{n-1}{k-1}\binom{n-1}{k},
\]
with out-of-range binomials zero. These follow by positive compositions of the zero- and one-run lengths and by choosing the starting label. They yield
\[
\mathbb ER_n=n+1,\qquad \operatorname{Var}(R_n)=\frac{n(n-1)}{2n-1},\qquad
\frac{R_n-n-1}{\sqrt{n/2}}\xrightarrow{d}N(0,1).
\]
For completeness, the last limit follows directly by applying Stirling's formula to the displayed two parity-specific binomial products uniformly for \(|r-(n+1)|=O(\sqrt n)\); both parities have the same normal local limit. The exact variance controls the tails outside growing fixed multiples of \(\sqrt n\), completing weak convergence. This is also the classical fixed-composition Wald–Wolfowitz runs limit.

**5. Transfer to the overlap statistic.** With \(q_n=\lfloor n+t\sqrt{n/2}\rfloor\), the run-count limit makes \(d_n=(R_n-1-q_n)_+=O_P(\sqrt n)\), whereas Step 3 makes \(L_n\) of order \(n\). Thus \(\Pr(d_n\le2L_n)\to1\). Step 2 gives
\[
\sqrt n\,\rho_{q_n,n,n}=\frac1{\sqrt n}\left\lceil\frac{d_n}{2}\right\rceil
=\frac{(R_n-1-q_n)_+}{2\sqrt n}+o_P(1).
\]
The continuous mapping theorem and Slutsky's lemma establish the stated positive-part Gaussian law. The exact zero-event identity in Step 1 and the continuous normal CDF separately establish its atom probability. The cases \(q_n/n\to a\ne1\) follow from \(R_n/n\to1\) in probability.

## Verification

The finite-sample zero-atom probability is exactly
\[
\Pr\{\rho_{q,n,n}=0\}=\frac1{\binom{2n}{n}}\sum_{r=2}^{\min(2n,q+1)}A_{n,r},
\]
where \(A_{n,r}\) is given in Proof, Step 4. At \(q=n\), the values for \(n=3,6,10,25,50\), respectively, are approximately \(0.7\), \(0.608225\), \(0.58593\), \(0.557847\), and \(0.539596\), trending to the proved limit \(1/2\).

Run `python3 check.py` from the package directory (Python 3 standard library only). The script independently computes the original OVL partition objective by dynamic programming for every balanced binary word through \(n=6\), checks the zero-event equivalence, universal lower bound, exact classical run counts, and the constructive isolated-pattern equality on further randomly sampled words up to \(n=40\). It also checks the mean and variance against the exact runs formulas. These finite checks supplement, but do not replace, the infinite proofs in the preceding section.

## Relationship to prior work

Komaba, Johno and Nakamoto (2022; revised 2023) define and study the OVL-\(q\) statistic, give general permutation enumeration, and develop an efficient finite method for \(q=2\) with balanced samples. Their 2024 one-sample paper proves the fixed-\(q=2\) range representation. An independent 2026 study supplies a general finite dynamic program and selected small finite null tables for \(q\ge3\). The exact Wald–Wolfowitz run-count distribution predates these overlap statistics. None of these inspected results states the near-saturation joint scaling regime \(q=n+O(\sqrt n)\), its non-Gaussian positive-part limit, or the isolated-pattern exact-attainment lemma. The present claim concerns **growing cut complexity**, not a new identity for \(q=2\), a new runs distribution, or general finite null enumerability.

## Limitations

The distributional transition is proved for equal sample sizes, two independent continuous samples under the exact common-distribution null, and deterministic cut counts \(q_n\) as stated. It does not establish power under alternatives, an optimal tuning rule, or the analogous constant for unequal sample sizes. The exact pattern equality is a high-probability condition in the critical regime, not an identity for every binary word at every \(q\). The cited finite tables and classical runs law constrain novelty; possible earlier results on high-complexity binary segmentation remain a historical-priority risk. There has been no independent mathematical audit.

## References

1. Atsushi Komaba, Hisashi Johno and Kazunori Nakamoto, *A novel statistical approach for two-sample testing based on the overlap coefficient*, arXiv:2206.03166 (first public version 2022-06-07), Journal of Mathematical Sciences, University of Tokyo **30** (2023), 205–240. https://arxiv.org/html/2206.03166v2
2. Atsushi Komaba, Hisashi Johno and Kazunori Nakamoto, *Extension of the one-sample Kolmogorov-Smirnov test*, arXiv:2408.10612 (2024-08-20). https://arxiv.org/abs/2408.10612
3. F. S. Swed and C. Eisenhart, *Tables for Testing Randomness of Grouping in a Sequence of Alternatives*, Annals of Mathematical Statistics **14** (1943), 66–87. Run-count formula reproduced at https://search.r-project.org/CRAN/refmans/randtests/html/runs.html
4. *Exact null distributions of the OVL-q goodness-of-fit tests: a linear-time algorithm for D_q, and the cells with q ≥ 3*, 2026-09-07 public snapshot, https://ideosphere.ai/papers/ovl2-pvalues (finite-algorithm and small-table comparison only).
