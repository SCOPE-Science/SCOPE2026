# Stable birth-labelled ancestry in independent random recursive trees

## Finding

Take \(q\ge2\) independent uniform recursive trees on the same increasing birth labels \([n]=\{1,\ldots,n\}\). Every nonroot birth \(j\) chooses independently in each tree a parent uniformly from \(\{1,\ldots,j-1\}\). Let \(S_n\) count the vertices whose *entire* root-to-vertex paths agree edge-for-edge across all \(q\) trees. The common root is included.

The coincidence count obeys the exact finite-state birth law
\[
\mathbb P(S_{k+1}=s+1\mid S_k=s)=\frac{s}{k^q},
\qquad (k,s)=(1,1)\text{ or } k\ge2,\ 2\le s\le k.
\]
It therefore converges almost surely to a finite integer \(S_\infty\), and
\[
\mathbb E S_\infty=\mu_q:=\prod_{k=1}^{\infty}\left(1+\frac1{k^q}\right),\qquad
\mathbb P(S_\infty>S_n)=\frac{\mu_q}{(q-1)n^{q-1}}+O_q(n^{-q}).
\]
For the natural two-tree case, \(\mu_2=\sinh(\pi)/\pi\approx3.67608\), and, for every integer \(n\ge2\) and \(2\le s\le n\),
\[
\mathbb P(S_\infty=S_n\mid S_n=s)
=\frac{\Gamma(n)^2}{\Gamma(n-\sqrt{s})\Gamma(n+\sqrt{s})}.
\]
In particular,
\[
\mathbb P(S_\infty=2)=-\frac{\sin(\pi\sqrt2)}{\pi\sqrt2}\approx0.216954.
\]
Although the number of shared *individual parent edges* in two trees grows like \(\log n\), the connected common-ancestry root component remains finite almost surely. A uniform exponential upper-tail bound for \(S_\infty\) is also proved below.

## Assumptions and scope

A *uniform recursive tree* on \([n]\) means an increasing rooted labelled tree with root \(1\), equivalently the independent uniform choice of a parent \(P(j)\in[j-1]\) at each birth \(2\le j\le n\). Across the \(q\) trees, all parent choices are independent. A vertex is counted only when **all** its ancestral edges agree, rather than merely its immediate parent. There is no optimization or relabelling of the vertices. Statements are exact for every indicated finite \(n\), while asymptotic statements hold as \(n\to\infty\) with fixed integer \(q\ge2\). The conditional Gamma formula uses \(2\le s\le n\) for \(n\ge2\): birth two always joins, and every subsequent step permits both a join and no join, so precisely these conditioning events have positive probability.

## Proof

**1. Common-ancestry Markov law.** Write \(C_k\) for the vertices in \([k]\) having identical root paths in every tree. Necessarily \(C_1=\{1\}\); a new vertex \(k+1\) enters \(C_{k+1}\) exactly when every one of its \(q\) parents is the same vertex in \(C_k\). Conditional on the complete history and \(|C_k|=s\), there are \(s\) favourable parent tuples out of \(k^q\), proving the displayed transition law. The finite distribution is thus specified completely by \(p_1(1)=1\) and
\[
 p_{k+1}(s)=\left(1-\frac{s}{k^q}\right)p_k(s)
                  +\frac{s-1}{k^q}p_k(s-1),
\]
with out-of-range probabilities zero.

**2. Almost-sure stabilization and mean.** Conditional expectation gives \(\mathbb E(S_{k+1}\mid S_k)=S_k(1+k^{-q})\). Thus
\[
\mu_{n}:=\mathbb ES_n=\prod_{k=1}^{n-1}(1+k^{-q})\uparrow\mu_q<\infty.
\]
Since the nondecreasing integer-valued sequence \(S_n\) has bounded expectations, it has an almost surely finite limit and monotone convergence yields its mean. For \(q=2\), the classical Euler hyperbolic-sine product gives \(\mu_2=\sinh\pi/\pi\).

**3. Exact eventual-stabilization probability.** If \(S_n=s\), and no new vertex ever joins, the conditional probability of no join at birth \(k+1\) equals \(1-s/k^q\). Hence
\[
 \mathbb P(S_\infty=S_n\mid S_n=s)
 =\prod_{k=n}^{\infty}\left(1-\frac{s}{k^q}\right).
\]
For \(q=2\), applying \(\Gamma(z+1)=z\Gamma(z)\) to partial products and taking their limit gives
\[
 \prod_{k=n}^{\infty}(1-s/k^2)
 =\frac{\Gamma(n)^2}{\Gamma(n-\sqrt s)\Gamma(n+\sqrt s)}.
\]
Every two-tree realization has \(S_2=2\). With \(n=s=2\), Euler's sine product reduces this expression to \(-\sin(\pi\sqrt2)/(\pi\sqrt2)\).

**4. Sharp probability of late new ancestral agreements.** Let \(H_{n,q}=\sum_{k=n}^{\infty} k^{-q}\). Given \(C_n\), consider for each \(k\ge n\) the event that all parents of vertex \(k+1\) equal one vertex in the fixed set \(C_n\). These events are independent given \(C_n\), with probabilities \(s/k^q\) for \(|C_n|=s\). The first such event, if any, is exactly the first new agreement after time \(n\), since until that event the agreement set stays \(C_n\). Bonferroni's inequalities thus imply
\[
0\le sH_{n,q}-\left[1-\prod_{k=n}^{\infty}(1-s/k^q)\right]
 \le \frac12 s^2H_{n,q}^2.
\]
Second moments are uniformly bounded: expanding the square after the single Bernoulli increment gives
\[
\mathbb ES_{k+1}^2=(1+2/k^q)\mathbb ES_k^2+k^{-q}\mathbb ES_k.
\]
Both the multiplicative products and the forcing sum converge because \(q\ge2\), and \(\mathbb ES_k\le\mu_q\). Taking expectations in the Bonferroni estimate therefore yields
\[
 \mathbb P(S_\infty>S_n)=\mu_n H_{n,q}+O_q(H_{n,q}^2).
\]
The estimates \(\mu_q-\mu_n=O_q(n^{1-q})\) and \(H_{n,q}=n^{1-q}/(q-1)+O_q(n^{-q})\) give the stated sharp asymptotic, since \(n^{2-2q}=O(n^{-q})\) for integers \(q\ge2\).

**5. Exponential tail.** Set
\[
\tau=\sum_{k=2}^\infty \frac1k\log\frac{k}{k-1}<\infty,
\qquad p=e^{-\tau},\quad a=1-p.
\]
Starting at \(S_2=2\), compare each birth step at state \(s\le k\) with a standard rate-one-per-individual Yule birth process run for time \(\delta_k=k^{-1}\log(k/(k-1))\). Its probability of at least one birth from \(s\) particles is \(1-(1-1/k)^{s/k}\), at least \(s/k^2\) by concavity, and therefore at least \(s/k^q\). If the Yule population is already larger, its birth probability increases. Stepwise monotone coupling embeds the common-ancestry process below a Yule process with two initial ancestors run for total time \(\tau\). Its final size has the negative-binomial law, so for every integer \(m\ge2\),
\[
 \mathbb P(S_\infty\ge m)
 \le a^{m-2}\bigl((m-1)p+a\bigr).
\]
This supplies a uniform exponential tail, not merely finite expectation.

**6. The difference from edge-by-edge agreement.** In the two-tree case, the indicator that the immediate parents of vertex \(k+1\) agree has probability \(1/k\). These indicators are independent over birth indices, so their sum \(W_n\) has mean \(\sum_{k=1}^{n-1}1/k\) and variance at most that mean. Chebyshev's inequality gives \(W_n/\log n\to1\) in probability, whereas the root-connected ancestry count converges almost surely to a finite limit.

## Verification

The standalone `check.py` implements the rational finite-state recurrence and separately enumerates all parent-vector tuples for two trees through seven vertices and three trees through five vertices. It also checks first and second finite moments, the exact finite probability of \(S_n=2\), and numerical consistency of the Gamma and Euler products. Run with `python check.py` using Python's standard library. The exact enumeration comprises 547,466 tuples; 375 assertions use rational arithmetic and the remaining 80 check numerical analytic identities. Exhaustive finite checks do not replace the infinite-product, coupling or asymptotic proofs above.

## Relationship to prior work

Baur's 2014 public preprint studies *homogeneous* Bernoulli percolation on random recursive trees, mainly with retention \(p(n)\to1\) and macroscopic root clusters. The present common-parent forest is an **age-dependent** edge-retention process with retention \(k^{1-q}\) at birth \(k+1\), with a finite root component; homogeneous percolation results do not imply the exact transition, Gamma stabilization law or late-agreement constant. Note that conditional on a match at birth \(k+1\), its parent is uniform on \([k]\), which is exactly the recursive-tree thinning representation.

Bäumler and collaborators' 2026 preprint concerns much larger **unlabelled, optimally matched** common subtrees of independent uniform-attachment trees. Its reported \(n^{0.83}\) lower-bound behavior concerns a different matching notion, so it does not imply a result for the birth-label-preserving root component. The full text of that recent preprint could not be inspected here; only its abstract and publicly available description were accessible.

## Limitations

The claimed ancestral overlap requires **identical birth labels and every parent edge**, not merely isomorphic or optimally re-embedded subtrees. The theorem does not describe the largest unlabelled common subtree or the largest nonroot common-edge component. The Yule bound gives exponential tails but is not asserted to be optimal. Unindexed historical formulas for inhomogeneous recursive forests and details of the inaccessible recent common-subtree paper remain originality risks; no independent mathematical validation has been performed.

## References

- Erich Baur, *Percolation on random recursive trees*, arXiv:1407.2508v1, first public version 9 July 2014. https://arxiv.org/abs/1407.2508
- Johannes Bäumler, Céline Kerriou, Bas Lodewijks, James Martin, Emil Powierski, Miklós Z. Rácz, Anirudh Sridhar, *On the largest common subtree of uniform attachment trees*, arXiv:2609.30098v1, 24 September 2026. https://arxiv.org/abs/2609.30098
