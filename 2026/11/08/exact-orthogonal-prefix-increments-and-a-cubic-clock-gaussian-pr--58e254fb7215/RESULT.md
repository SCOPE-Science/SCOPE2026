# Exact orthogonal prefix increments and a cubic-clock Gaussian process for asymmetric shelf shuffles

## Finding
Fix an integer \(m\ge2\) and \(p\in(0,1)\). A sequential asymmetric shelf shuffle creates a family of coupled deck-prefix permutations by assigning each new card a uniform shelf and independently inserting it on that shelf's top with probability \(p\), otherwise on its bottom. Shelves are concatenated in increasing index order. Count inversions relative to the cards' increasing arrival labels. Let \(I_k\) be the count for the first \(k\) cards.

With
\[
\theta=\frac{m-1+2p}{2m},\quad u=\frac{m^2-1}{12m^2},\quad v=\frac{p(1-p)}{m^2},
\]
for all integers \(1\le k\le\ell\),
\[
\mathbb E I_k=\theta\binom{k}{2},\qquad
\operatorname{Cov}(I_k,I_\ell)=\operatorname{Var}(I_k)
=\frac{u k(k-1)(2k+5)+v k(k-1)(2k-1)}{6}.
\]
Thus every pair of disjoint increments of the centered prefix inversion count is uncorrelated *exactly*, despite non-independence.

Define the process
\[
Z_n(t)=\frac{I_{\lfloor nt\rfloor}-\theta\binom{\lfloor nt\rfloor}{2}}{n^{3/2}},\qquad 0\le t\le1.
\]
Then, in \(D([0,1])\) with the Skorohod topology,
\[
Z_n\Longrightarrow \sigma W(t^3),\qquad
\sigma^2=\frac{u+v}{3}=\frac{m^2-1+12p(1-p)}{36m^2},
\]
where \(W\) is a standard Brownian motion. In particular the limiting covariance equals \(\sigma^2\min(s,t)^3\), and the limiting increments are independent even though the finite-prefix increments need not be.

## Assumptions and scope
The shelf number \(m\) and top-insertion probability \(p\) are fixed as the card count tends to infinity. For each integer \(j\ge1\), independently sample \(S_j\) uniform on \(\{1,\ldots,m\}\) and \(B_j\) Bernoulli with success probability \(p\); all coordinates are independent. Process the cards in increasing label order. For each \(k\), put the cards of each shelf into their actual physical insertion order (top insertions precede previous shelf contents, bottom insertions follow them), concatenate shelf lists in order, and count pairs of labels \(i<j\le k\) for which \(j\) precedes \(i\). This coupling is by common independent card assignments, not by independent re-shuffling at each \(k\).

## Proof
**Step 1: exact pair representation.** For \(i<j\), later card \(j\) precedes earlier card \(i\) exactly when its shelf is smaller, or when both use the same shelf and \(j\) enters on top. Thus, with \(X_j=(S_j,B_j)\),
\[
h(X_i,X_j)={\bf1}\{S_i>S_j\}+{\bf1}\{S_i=S_j\}B_j,\qquad I_k=\sum_{i<j\le k}h(X_i,X_j).
\]
The mean of a pair is \(\theta=(m-1+2p)/(2m)\).

**Step 2: nonsymmetric Hoeffding decomposition.** Define
\[
A_j=\frac{S_j-(m+1)/2}{m},\qquad C_j=\frac{B_j-p}{m},
\]
so that \(\mathbb E A_j=\mathbb E C_j=0\), \(\operatorname{Var}A_j=u\), \(\operatorname{Var}C_j=v\), and \(A_j,C_j\) are independent. The first-coordinate conditional projection of \(h-\theta\) is \(A_i\), and the second-coordinate projection is \(-A_j+C_j\). Set
\[
\psi(X_i,X_j)=h(X_i,X_j)-\theta-A_i+A_j-C_j.
\]
Both one-coordinate conditional expectations of \(\psi\) vanish. As \(h\) is Bernoulli with variance \(3u+v\), projection orthogonality gives \(\mathbb E\psi^2=u\). Sum over pairs to obtain the identity
\[
I_k-\theta\binom{k}{2}=\sum_{j=1}^k\big[(k-2j+1)A_j+(j-1)C_j\big]+R_k,\quad
R_k=\sum_{1\le i<j\le k}\psi(X_i,X_j).
\]
The \(R_k\) form a square-integrable martingale in the natural filtration, since conditional on all earlier assignments the expected increment is zero. Distinct unordered pairs of \(\psi\)-terms are orthogonal (including pairs sharing one coordinate), and each \(\psi\)-term is orthogonal to every linear term \(A_j,C_j\). Consequently \(\operatorname{Var}R_k=\binom{k}{2}u\) and \(\operatorname{Cov}(R_k,R_\ell)=\binom{k}{2}u\) for \(k\le\ell\).

**Step 3: exact covariance.** The linear part has covariance for \(k\le\ell\)
\[
u\sum_{j=1}^k(k-2j+1)(\ell-2j+1)+v\sum_{j=1}^k(j-1)^2.
\]
Because \(\sum_{j=1}^k(k-2j+1)=0\), the first sum is unchanged when \(\ell\) is replaced by \(k\). The power sums are
\[
\sum_{j=1}^k(k-2j+1)^2=\frac{k(k^2-1)}{3},\quad
\sum_{j=1}^k(j-1)^2=\frac{k(k-1)(2k-1)}{6}.
\]
Adding the martingale residual contribution \(u\binom{k}{2}\) gives exactly the displayed covariance and variance, including \(k=1\).

**Step 4: functional limit, including the error bound.** For \(0\le t\le1\), multiply the linear part by \(n^{-3/2}\), set \(k=\lfloor nt\rfloor\), and rewrite it through the independent bivariate partial-sum processes of \(A_j,C_j\). The vector Donsker theorem and continuity of the integral map at continuous limits yield
\[
G(t)=\sqrt u\int_0^t(t-2r)\,dW_A(r)+\sqrt v\int_0^t r\,dW_C(r),
\]
with independent standard Brownian motions \(W_A,W_C\). In this display the integrals are equivalently defined by integration by parts, avoiding any ambiguity about convergence of stochastic integrals. Doob's maximal inequality gives
\[
\mathbb E\max_{k\le n}|R_k|^2\le4\binom n2 u=O(n^2),
\]
therefore \(\max_{k\le n}|R_k|/n^{3/2}\to0\) in \(L^2\). For \(s\le t\), direct integration yields
\[
\operatorname{Cov}(G(s),G(t))
=u\int_0^s(s-2r)(t-2r)\,dr+v\int_0^s r^2\,dr
=\frac{u+v}{3}s^3.
\]
This centered continuous Gaussian process has the same law as \(\sigma W(t^3)\). Slutsky's theorem for \(D([0,1])\) completes the proof.

## Verification
Run `python3 check.py` using Python's standard library. The program exhaustively constructs *physical shelf lists* for finite examples with rational probabilities, compares inversion-count means and every nested-prefix covariance against the formulas, and checks the linear algebra identities independently. These finite checks are reproducibility tests, not an infinite proof. The general result follows from the displayed decomposition, Doob inequality, and functional central limit theorem.

## Relationship to prior work
Tripathi, *Analysis of the asymmetric shelf shuffle* (first publicly posted June 16, 2026), develops the asymmetric model and studies several single-deck statistics including inversions. Clay, *Limit theorems for descents and inversions of shelf-shuffles* (first publicly posted September 30, 2025), already gives inversion means/variances and a one-time CLT for the unbiased shelf shuffle; that existing marginal result is not claimed as new here. Clay's arXiv full text, Section 3, describes the relevant pairwise inversion-statistic representation. Standard Hoeffding decomposition and Donsker theory already provide general analytic tools. The additional assertion here is the exact *cross-prefix covariance cancellation* in the common-assignment coupling and its specifically identified cubic-clock process limit for fixed shelves and arbitrary top-insertion bias. Related general sequential U-statistic invariance principles can imply parts of the limit theory but do not by themselves state this model-specific finite-prefix cancellation.

## Limitations
The theorem concerns a single coupled sequential insertion experiment, fixed \(m\), fixed \(p\), and inversion count only. No assertion is made for a growing shelf count, independently repeated shuffles, mixing times, other permutation statistics, or finite-prefix independence. One-time unbiased normal approximation and one-deck moments are previously studied. The complete text of Tripathi's closely related 2026 article could not be accessed for definitive priority assessment: the accessible journal page is an abstract/subscription preview. Thus independent historical-priority verification remains important. The package contains no independent audit.

## References
1. Raghavendra Tripathi, *Analysis of the Asymmetric Shelf Shuffle*, arXiv:2606.18047 (first public posting 2026-06-16); *Journal of Theoretical Probability* (2026), doi:10.1007/s10959-026-01547-9. https://arxiv.org/abs/2606.18047
2. Alexander Clay, *Limit theorems for descents and inversions of shelf-shuffles*, arXiv:2510.00343 (first public posting 2025-09-30). https://arxiv.org/html/2510.00343v2
3. Persi Diaconis, Jason Fulman and Susan Holmes, *Analysis of casino shelf shuffling machines*, *Annals of Applied Probability* **23** (2013), 1692–1720.
4. Standard probabilistic tools: Hoeffding decomposition for order-two statistics, vector Donsker theorem and Doob maximal inequality.
