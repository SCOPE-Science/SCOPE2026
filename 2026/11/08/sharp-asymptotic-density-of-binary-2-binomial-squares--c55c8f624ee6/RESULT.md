# Sharp asymptotic density of binary \(2\)-binomial squares

## Finding
A binary word of even length \(2n\) is a **\(2\)-binomial square** if its first and last length-\(n\) halves have equal counts of every scattered subword of length at most two. Let \(S_n\) be the number of such indexed binary words. Then, as \(n\to\infty\),
\[
S_n\sim \frac{2\sqrt{3}}{\pi}\frac{4^n}{n^2}.
\]
Equivalently, the proportion of binary words of length \(2n\) that are \(2\)-binomial squares is asymptotic to \(2\sqrt{3}/(\pi n^2)\). For each integer \(n\ge1\) there is also the exact finite expression
\[
S_n=\sum_{k=0}^{n}\sum_{j=0}^{k(n-k)}\left([t^j]\begin{bmatrix}n\\k\end{bmatrix}_t\right)^2,
\]
where the bracket is the usual Gaussian binomial polynomial. The asymptotic, rather than the standard coefficient expansion, is the principal finding.

## Assumptions and scope
Words are over \(\{0,1\}\). Halves and positions are indexed; no quotient by reversal, rotation or symbol complementation is taken. Both halves have exactly length \(n\); repetitions of a given half are permitted, and ordered choices of halves are counted. Scattered factors are subsequences, not necessarily contiguous factors. The counting statement applies to all positive integers \(n\), and the limit concerns \(n\to\infty\).

## Proof
**Reduction to one lattice statistic.** For a length-\(n\) word \(u\), put \(K(u)=|u|_1\) and let \(I(u)\) count its ordered \(01\) subsequences. Two such words are \(2\)-binomially equivalent if and only if their pairs \((K,I)\) agree: the length-one counts determine the equal-symbol pairs, and the other mixed pair count is \(K(n-K)-I\). Thus
\[
S_n=\sum_{k,j} N_n(k,j)^2,
\]
where \(N_n(k,j)\) is the number of length-\(n\) words having \(k\) ones and \(j\) occurrences of scattered \(01\). Standard inversion/partition duality gives \(\sum_jN_n(k,j)t^j=\begin{bmatrix}n\\k\end{bmatrix}_t\); replacing inversion number by its complement changes no coefficient multiset. This proves the exact expression.

**Uniform conditional collision estimate.** Let \(U\) be uniform on binary length-\(n\) words; conditional on \(K(U)=k\), let \(p_{n,k}(j)=\Pr(I(U)=j\mid K(U)=k)\). Its mean is \(\mu_{n,k}=k(n-k)/2\) and its variance is
\[
\sigma_{n,k}^2=\frac{k(n-k)(n+1)}{12}.
\]
For \(|k-n/2|\le n^{2/3}\), the two multiplicities \(k,n-k\) are each a fixed positive fraction of \(n\). The uniform local limit theorem for multiset inversions, Theorem 4.5 of Canfield–Janson–Zeilberger, therefore gives, uniformly for all integers \(j\) and for those \(k\),
\[
\sigma_{n,k}p_{n,k}(j)=\varphi\!\left(\frac{j-\mu_{n,k}}{\sigma_{n,k}}\right)+O(n^{-1}),
\quad \varphi(x)=\frac{e^{-x^2/2}}{\sqrt{2\pi}}.
\]
In particular \(\sup_j p_{n,k}(j)=O(\sigma_{n,k}^{-1})\) uniformly. Fix \(R>0\). Within \(|j-\mu_{n,k}|\le R\sigma_{n,k}\), square this estimate and use a Riemann sum: the contribution multiplied by \(\sigma_{n,k}\) tends uniformly to \(\int_{-R}^{R}\varphi(x)^2\,dx\). Outside that region, Chebyshev's inequality and the uniform point-mass bound give
\[
\sigma_{n,k}\sum_{|j-\mu_{n,k}|>R\sigma_{n,k}}p_{n,k}(j)^2=O(R^{-2}),
\]
uniformly in the central \(k\)-range. Letting first \(n\to\infty\) and then \(R\to\infty\) proves
\[
\sum_jp_{n,k}(j)^2=\frac{1+o(1)}{2\sqrt\pi\,\sigma_{n,k}},
\]
uniformly for \(|k-n/2|\le n^{2/3}\). Since \(\sigma_{n,k}\sim n^{3/2}/(4\sqrt3)\) in this range, the conditional collision probability is \((2\sqrt3/\sqrt\pi+o(1))n^{-3/2}\).

**Average over symbol count.** For independent uniform \(U,V\), the probability of \(2\)-binomial equivalence is
\[
4^{-n}S_n=\sum_{k=0}^{n}\left(\frac{\binom nk}{2^n}\right)^2\sum_jp_{n,k}(j)^2.
\]
The mass for \(|k-n/2|>n^{2/3}\) is exponentially small by the binomial tail bound, because each inner collision probability is at most one. The elementary Vandermonde identity and Stirling's formula give
\[
\sum_{k=0}^{n}\left(\frac{\binom nk}{2^n}\right)^2=\frac{\binom{2n}{n}}{4^n}\sim\frac1{\sqrt{\pi n}}.
\]
Multiplication by the uniform central conditional collision estimate therefore yields
\[
\frac{S_n}{4^n}\sim\frac{2\sqrt3}{\sqrt\pi\,n^{3/2}}\frac1{\sqrt{\pi n}}=\frac{2\sqrt3}{\pi n^2}.
\]
All tail estimates and asymptotics refer to explicitly specified finite probability distributions. No computation is used to establish the infinite limit.

## Verification
Run `python3 verify.py` from the directory containing this file. It builds all Gaussian-binomial coefficient polynomials for \(1\le n\le100\) via the standard \(q\)-Pascal recurrence, independently enumerates every binary half of lengths \(1\le n\le12\) by its scattered-deck signature, and checks agreement of the two exact formulas. It also reproduces selected large integer counts and scaled ratios. For example \(S_4=18\), \(S_8=1064\), \(S_{12}=122570\), and \(n^2S_n/4^n\) is approximately \(1.096100119\) at \(n=100\), versus the proved limit \(2\sqrt3/\pi\approx1.102657791\). These calculations are finite consistency checks only.

## Relationship to prior work
Rao, Rigo and Salimov (first public preprint 17 October 2013) introduced and investigated avoidance of \(2\)-binomial squares, with explicit morphic constructions and a binary cube-avoidance result; the full accessible preprint does not enumerate the density of all binary \(2\)-binomial squares. Canfield, Janson and Zeilberger (14 August 2009), Theorem 4.5, prove a uniform local central limit theorem for inversion counts in multiset permutations. That powerful preexisting local theorem is an essential ingredient, and the exact Gaussian-binomial coefficient expansion follows from their standard partition interpretation. The present result concerns a different aggregated collision probability, simultaneously across all symbol multiplicities, whose constant requires a second Gaussian summation. Richomme's later work on binary \(2\)-binomial class structure supplies relevant partition context but does not state this density constant in inspected material. This analysis does not claim independent discovery of the prerequisite local theorem or of Gaussian-binomial coefficient identities.

## Limitations
No error term beyond the displayed asymptotic equivalence is asserted. No claims are made about alphabets of more than two symbols, higher-binomial equivalence, or squares in a particular infinite word. An unindexed earlier counting result or a previously unstated consequence of stronger general collision estimates could affect historical priority. An independent mathematical audit has not been performed.

## References
1. E. R. Canfield, S. Janson and D. Zeilberger, *The Mahonian probability distribution on words is asymptotically normal*, arXiv:0908.2089v1 (first public 2009-08-14), especially Theorem 4.5. https://arxiv.org/pdf/0908.2089
2. M. Rao, M. Rigo and P. Salimov, *Avoiding 2-binomial squares and cubes*, arXiv:1310.4743v1 (first public 2013-10-17). https://arxiv.org/pdf/1310.4743
3. G. Richomme, *On some 2-binomial coefficients of binary words: geometrical interpretation, partitions of integers, and fair words*, arXiv:2510.07159 (first public 2025-10-08). https://arxiv.org/abs/2510.07159
