# Exact Nash-product law and exponential limit in master-priority random stable marriage

## Finding
Consider a balanced, complete, strict marriage market with \(n\ge1\) men and \(n\) women. Every woman ranks the men in one common priority order; the men's rankings are independent and uniformly distributed over all \(n!\) permutations. Let \(r_a\in\{1,\ldots,n\}\) be agent \(a\)'s partner rank in the unique stable matching and give that agent positive Borda utility \(u_a=n+1-r_a\). Let \(Z_n=\prod_a u_a\), the \(2n\)-agent Nash product (its \(2n\)-th root is Nash social welfare).

For \(k=1,\ldots,n\), take independent random variables \(U_{k,n}\) with
\[
\Pr(U_{k,n}=u)=\frac{\binom{u-1}{k-1}}{\binom nk},\qquad k\le u\le n.
\]
Then the entire Nash-product distribution has the exact factorization
\[
Z_n\ \stackrel{d}{=}\ n!\prod_{k=1}^{n}U_{k,n}.
\]
In particular, for every real \(s\ge0\),
\[
\mathbb E[Z_n^s]=(n!)^s\prod_{k=1}^{n}\frac{\sum_{u=k}^{n}u^s\binom{u-1}{k-1}}{\binom nk},
\qquad
\mathbb E[Z_n]=n!(n+1)^{n-1}.
\]
Furthermore, the normalized Nash product has a **nondegenerate** exponential limit,
\[
\frac{nZ_n}{n!(n+1)^n}\ \xrightarrow[n\to\infty]{d}\ \operatorname{Exp}(1),
\]
with convergence of every fixed nonnegative integer moment. Thus its normalized variance tends to one rather than zero.

## Assumptions and scope
All lists are strict and complete, each side has exactly \(n\) agents, women share one fixed strict order, and men draw their entire rankings independently uniformly. The Nash product includes **both sides** and uses \(n+1-r\), not zero-based rank, not sum of utilities, and not the expectation of the geometric mean. All probabilities are over the men's rankings only. The law is for the unique stable matching, not an arbitrary matching or a mixture over multiple stable matchings.

## Proof
**Step 1: stable matching and independence.** Order men by their common rank at all women. The first man must take his most preferred woman; otherwise that man and his preferred woman block any matching. After deleting the matched pair, repeat by induction. Hence the unique stable matching is serial dictatorship in this fixed order. This property is also given by Irving--Manlove--Scott, Theorem 2.1, for one strict master list. When the \(k\)-th number of women remain (with \(k=n,n-1,\ldots,1\)), the current man's independent uniform preference list puts these \(k\) women at a uniformly random \(k\)-subset of the \(n\) positions. The best available woman has the smallest position, so her positive Borda utility is the **maximum** of a uniformly sampled \(k\)-subset of \(\{1,\ldots,n\}\). For a particular maximum \(u\), exactly \(\binom{u-1}{k-1}\) of the \(\binom nk\) subsets qualify. This conditional distribution does not depend on the earlier choices, proving mutual independence of the \(U_{k,n}\). Each man is matched once; women receive each man exactly once, giving a deterministic product of women's utilities \(n!\). The distributional factorization follows.

**Step 2: finite moments.** The displayed Mellin/moment product follows by independence. For a uniform size-\(k\) sample without replacement, its maximum satisfies
\[
\mathbb E[U_{k,n}]=\frac{k(n+1)}{k+1},\quad
\operatorname{Var}(U_{k,n})=\frac{k(n+1)(n-k)}{(k+1)^2(k+2)}.
\]
These are the standard finite-population order-statistic formulas; they also follow by summing the above exact point masses. Multiplying the first formula and telescoping yields
\[
\mathbb E[Z_n]=n!\,(n+1)^n\prod_{k=1}^{n}\frac{k}{k+1}=n!(n+1)^{n-1}.
\]
For additional finite-moment control, write \(V_{k,n}=U_{k,n}/(n+1)\). The same mean and variance formulas give
\[
\mathbb E[V_{k,n}^2]=\frac{k}{k+2}\left(1-\frac1{(n+1)(k+1)}\right),
\]
so
\[
\mathbb E\!\left[\left(\frac{nZ_n}{n!(n+1)^n}\right)^2\right]
=\frac{2n^2}{(n+1)(n+2)}\prod_{k=1}^{n}\left(1-\frac1{(n+1)(k+1)}\right)\longrightarrow2.
\]
The normalized first moment is \(n/(n+1)\), hence its variance tends to \(2-1=1\).

**Step 3: all-moment exponential limit.** Fix a positive integer \(s\). Let \(B_k\) be independent with the \(\operatorname{Beta}(k,1)\) distribution. Then
\[\mathbb E[B_k^s]=\frac{k}{k+s},\quad \mathbb E B_k=\frac{k}{k+1},\quad \operatorname{Var}(B_k)=\frac{k}{(k+1)^2(k+2)}.\]
For each fixed \(k\), the maximum-rank CDF implies \(V_{k,n}\Rightarrow B_k\) as \(n\to\infty\), since \(\binom{\lfloor(n+1)t\rfloor}{k}/\binom nk\to t^k\) for \(0<t<1\). Also \(V_{k,n}\) and \(B_k\) have the same mean and variances at most \(k/((k+1)^2(k+2))\). Taylor's formula with \(f(t)=t^s\) and \(\sup_{[0,1]}|f''|=s(s-1)\) gives, uniformly in \(n\ge k\),
\[
\left|\mathbb E[V_{k,n}^s]-\mathbb E[B_k^s]\right|
\le s(s-1)\frac{k}{(k+1)^2(k+2)}=O_s(k^{-2}).
\]
For \(s=1\) the difference is identically zero. Since \(\mathbb E B_k^s=k/(k+s)\) is bounded away from zero for fixed \(s\), the relative error is \(O_s(k^{-2})\). Split the product of moment ratios at any fixed \(K\): its finite initial factors tend to one, and the logarithmic tail is uniformly \(O_s(\sum_{k>K}k^{-2})\). Therefore
\[
\prod_{k=1}^n\frac{\mathbb E V_{k,n}^s}{\mathbb E B_k^s}\longrightarrow1.
\]
Consequently,
\[
\mathbb E\!\left[\left(\frac{nZ_n}{n!(n+1)^n}\right)^s\right]
\sim n^s\prod_{k=1}^n\frac{k}{k+s}
=n^s\frac{s!\,n!}{(n+s)!}\longrightarrow s!.
\]
These are precisely the moments of a unit-mean exponential law. That law is moment-determinate (its moment generating function is finite near zero), so the method of moments proves the asserted weak convergence and all fixed integer-moment limits.

## Verification
The standalone `check.py` independently exhausts all men's complete strict ranking profiles for \(n=1,2,3,4\), constructing the serial stable matching directly and checking the **full joint law** of all men's Borda utilities against the independent order-statistic point masses, as well as the first and second Nash-product moments using exact rational arithmetic. Numbers of profiles checked are \(1,4,216,331776\); first moments of the full Nash product are \(1,6,96,3000\), respectively. To reproduce, run `python3 check.py` with a standard Python 3 installation. See `CHECK_RESULTS.txt` for the recorded execution. The proof, not finite enumeration, establishes all \(n\) and the limit.

## Relationship to prior work
Irving, Manlove and Scott (2008), Section 2 and Theorem 2.1, establish uniqueness and the fixed-priority greedy construction for a strict master list; they do not analyze random Borda-product laws. Desai, Rasheed M, Ghalme and Gujar (arXiv:2609.02354, September 2, 2026) introduce/study rank-induced Nash social welfare for stable matching and an algorithm for its maximization over stable matchings. The available abstract concerns algorithmic optimization, not the distribution or exponential limit in the one-master-list random model; its full text was not accessible for comparison, so priority qualification remains. Caragiannis and Homrighausen (arXiv:2405.14316, 2024) study **additive expected** social welfare of random serial dictatorship over random agent orderings for fixed input profiles, a different expectation/objective from this multiplicative Nash law over independent random preference lists with fixed priority. The present exact product factorization uses the classic master-list structure and elementary sampling-without-replacement probabilities; these ingredients are prior mathematics, not claimed new. The contribution is the integrated exact welfare law and its non-concentrating exponential limit in the stated matching market.

## Limitations
This theorem assumes uniform independent male rankings and an identical strict female priority list. It does not cover correlated preferences, varying priorities, incomplete lists, ties, positive cardinal utilities other than positive Borda, or the distribution of welfare-optimal stable matchings in markets with multiple stable matchings. The limit concerns the Nash product after the explicit normalization, not the geometric mean on its original scale. Exact law statements are mathematical deductions from classical random-sample facts; unpublished or unindexed prior derivations cannot be ruled out. The 2026 Nash-welfare paper could not be inspected in full, so novelty requires further human literature review. The supplied computational verification is finite exact checking, not an independent scientific audit.

## References
1. R. W. Irving, D. F. Manlove and S. Scott, *The stable marriage problem with master preference lists*, Discrete Applied Mathematics 156 (2008), 2959--2977. Open full text: https://eprints.gla.ac.uk/25737/1/25737.pdf . See Section 2, Theorem 2.1.
2. P. Desai, Rasheed M, G. Ghalme and S. Gujar, *Fair Stable Matching: A Nash Social Welfare Approach*, arXiv:2609.02354, first posted September 2, 2026. https://arxiv.org/abs/2609.02354 .
3. I. Caragiannis and S. Homrighausen, *Estimating the Expected Social Welfare and Cost of Random Serial Dictatorship*, arXiv:2405.14316, 2024. https://arxiv.org/abs/2405.14316 .
