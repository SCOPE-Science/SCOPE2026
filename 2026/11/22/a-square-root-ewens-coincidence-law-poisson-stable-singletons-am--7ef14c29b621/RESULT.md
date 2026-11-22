# A square-root Ewens coincidence law: Poisson-stable singletons amid extensive pair overlap

## Finding
For every integer \(n\ge2\), let \(P_n,Q_n\) be independent Ewens random set partitions of \([n]\), with a common positive concentration parameter \(\theta_n\). Assume \(\theta_n/\sqrt n\to c\in(0,\infty)\). A **common block** is a subset that is an entire block of both partitions, not merely a block of their meet. Let \(C_n\) be the number of common singleton blocks and put \(\Xi_n=\sum_{\{i\}\in P_n\cap Q_n}\delta_{i/n}\). Then
\[
\Xi_n\Longrightarrow\operatorname{PPP}(c^2\,dx)\quad\hbox{on }[0,1],
\qquad C_n\xrightarrow{\mathrm{TV}}\operatorname{Poisson}(c^2).
\]
With probability tending to one, **there are no common blocks of size at least two**; consequently, the probability that the partitions have no identical blocks at all tends to \(e^{-c^2}\). Yet the count \(R_n\) of unordered pairs of labels lying in a shared equivalence class of *each* partition satisfies the exact identity
\[
\mathbb E R_n=\frac{\binom n2}{(\theta_n+1)^2}\sim\frac{n}{2c^2}.
\]
Thus extensive shared pairwise co-membership coexists with only finitely many exact shared blocks. The exact finite-size factorial moments of the singleton coincidence count are
\[
\mathbb E(C_n)_{k}=(n)_{\underline k}\left(\frac{\theta_n^k}{\prod_{j=0}^{k-1}(\theta_n+n-k+j)}\right)^2,
\qquad 0\le k\le n.
\]
Here \((C)_k=C(C-1)\cdots(C-k+1)\), and \((n)_{\underline k}=n(n-1)\cdots(n-k+1)\). The Poisson point process convergence is weak convergence of finite counting measures, not total-variation convergence of discrete locations to continuous points.

## Assumptions and scope
The Ewens(\(\theta\)) probability of a specified partition \(\pi\) of \([n]\) into blocks \(B\) is \(\theta^{|\pi|}\prod_{B\in\pi}(|B|-1)!/(\theta)_n\), with the rising factorial \((\theta)_n=\theta(\theta+1)\cdots(\theta+n-1)\). The two partitions are independent with the same parameter for each \(n\), but the parameter varies with \(n\). A block in the meet is an intersection of two original blocks; it need not be an entire block in either original partition. This distinction is essential. No assertion is made for concentration outside the stated square-root window.

## Proof
**Exact marked-block identity.** For any specified pairwise-disjoint nonempty subsets \(B_1,\ldots,B_k\) with total size \(s\le n\), summing the Ewens weight over all partitions of their complement shows
\[
\Pr(B_1,\ldots,B_k\hbox{ are all blocks of }P_n)=
\frac{\theta_n^k\prod_{j=1}^k(|B_j|-1)!}{\prod_{h=0}^{s-1}(\theta_n+n-s+h)}.
\]
The same joint event in both independent partitions has the square of this probability. For singleton \(B_j\), summing over the \((n)_{\underline k}\) ordered choices of distinct labels gives the displayed exact factorial-moment formula.

**Poisson limit and labels.** For each fixed \(k\), since \(\theta_n/\sqrt n\to c\), the last factorial moment tends to \(c^{2k}\). The first moment is bounded, so the sequence is tight; the next factorial moments give uniform integrability of each polynomial moment. The method of moments, using the moment determinacy of the Poisson distribution, gives \(C_n\Rightarrow\operatorname{Poisson}(c^2)\). On the countable nonnegative integers, convergence in distribution plus tightness implies convergence in total variation. By exchangeability, conditional on \(C_n=k\), the coincident singleton labels form a uniformly distributed \(k\)-subset of \([n]\). Their scaled positions converge jointly to \(k\) independent uniforms on \([0,1]\). Combining this conditional convergence with the tight count law gives \(\Xi_n\Longrightarrow\operatorname{PPP}(c^2\,dx)\). Alternatively, disjoint-set mixed factorial moments follow directly from the marked identity.

**Excluding nontrivial identical blocks.** For a specified pair \(\{i,j\}\), its exact probability of being an entire block in one partition is \(\theta_n/[(\theta_n+n-2)(\theta_n+n-1)]\). Hence the expected number of common two-element blocks is
\[
\binom n2\left(\frac{\theta_n}{(\theta_n+n-2)(\theta_n+n-1)}\right)^2=O_c(n^{-1}).
\]
For each block of size at least three in \(P_n\), choose any deterministic three of its labels. Their probability of belonging to one block of the *independent* partition \(Q_n\) is exactly \(2/[(\theta_n+1)(\theta_n+2)]\), by sampling consistency. The expected number of all blocks in \(P_n\) is \(\sum_{j=0}^{n-1}\theta_n/(\theta_n+j)=O_c(\sqrt n\log n)\). A conditional union bound therefore gives probability \(O_c(\log n/\sqrt n)\) that any common block has size three or more. Combined with the two-block estimate, every non-singleton identical block disappears in probability.

**Shared pairwise co-membership.** Two fixed labels lie in the same Ewens block with probability \(1/(\theta_n+1)\). Independence of \(P_n,Q_n\) and linearity of expectation yield the exact displayed formula for \(\mathbb E R_n\). This count concerns pairs in the meet, not identical complete blocks, and the asymptotic follows from \(\theta_n/\sqrt n\to c\).

## Verification
The standalone standard-library script `verify.py` exhaustively lists all set partitions for \(2\le n\le6\), evaluates two independent Ewens partition laws at three positive rational concentrations, and checks the exact first and second factorial moments and shared-pair expectation using rational arithmetic. It reports 45 passing exact assertions over 15 complete paired-partition enumerations. The analytic arguments, not these finite checks, prove the asymptotic conclusions. Run `python3 verify.py` in the same directory.

## Relationship to prior work
Pittel's 2000 theorem on *uniform* set partitions describes the meet of independently sampled partitions and its nontrivial intersection classes. The present law concerns *Ewens* partitions in a growing square-root concentration regime and compares full-block agreement with shared pairwise co-membership; these are different events and probability measures. Gnedin and Pitman's 2006 public preprint states the Ewens partition formula and sampling consistency used here and constructs a single fragmentation process; it does not state the joint full-block agreement law of two independent draws. General Ewens Poisson approximation theory supplies related methods but does not automatically identify the full-block/meet contrast without the exact block-event computation and uniform bound.

## Limitations
The Poisson threshold is established only when \(\theta_n/\sqrt n\to c\in(0,\infty)\). It does not describe the full distribution of non-singleton blocks of the meet or fluctuations of \(R_n\). The bound excluding larger common complete blocks is not asserted to be sharp. Historical priority is qualified: general results about two Ewens partitions, their block agreements, and abstract Poisson approximation may imply related assertions not found in the inspected sources. No external independent mathematical audit has been carried out.

## References
1. A. Gnedin and J. Pitman, *Poisson representation of a Ewens fragmentation process*, first public arXiv version 2006-08-12, arXiv:math/0608307v1, especially the Ewens partition formula (1) and sampling consistency. https://arxiv.org/abs/math/0608307
2. B. Pittel, *Where the Typical Set Partitions Meet and Join*, Electronic Journal of Combinatorics 7 (2000), R5, published 2000-01-15, especially Theorem 4. https://doi.org/10.37236/1483
3. A. Gnedin, C. Haulk, and J. Pitman, *Characterizations of exchangeable partitions and random discrete distributions by deletion properties*, first public arXiv version 2009-09-20, arXiv:0909.3642, on the related Ewens partition deletion framework. https://arxiv.org/abs/0909.3642
