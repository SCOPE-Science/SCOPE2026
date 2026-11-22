# A three-regime information-loss law for iterated binary tortoise sorting

## Finding

Let \(\tau\) denote Defant--Kravitz tortoise sorting on binary words, let \(W_n\) be a uniformly sampled binary word of length \(n\), and let
\[
F_{n,k}(w)=|\{u\in\{0,1\}^n:\tau^k(u)=\tau^k(w)\}|,\qquad Y_{n,k}=\tau^k(W_n).
\]
All logarithms and entropies below have base two. For integers \(n\ge1\) and \(1\le k\le n\), the exact number of nonempty inverse classes is
\[
|\tau^k(\{0,1\}^n)|=k+2^{n-k}.
\]
The entire multiset of their cardinalities is
\[
\left\{\binom nr:0\le r<k\right\}\ \uplus\ \left\{\binom nk\right\}\ \uplus\
\biguplus_{h=0}^{n-k-1}\left\{\binom{h+k}{k}\right\}^{\!\times 2^{n-k-h-1}}.
\]
Here \(\uplus\) is multiset union and the last multiset is empty when \(k=n\). The largest class has size \(\binom n{\min(k,\lfloor n/2\rfloor)}\).

For any integer sequence \(0\le k_n\le n\) with \(k_n/n\to\alpha\in[0,1]\),
\[
\frac{\log_2 F_{n,k_n}(W_n)}n\ \xrightarrow{\mathsf P}\ \min(2\alpha,1).
\]
Writing \(H\) for Shannon entropy of a discrete random variable,
\[
\lim_{n\to\infty}\frac{H(Y_{n,k_n})}{n}=(1-2\alpha)_+,
\qquad
\lim_{n\to\infty}\frac{\log_2|\operatorname{supp}(Y_{n,k_n})|}{n}=1-\alpha.
\]
Thus the asymptotic difference between the Hartley and Shannon entropy rates is \(\min(\alpha,1-\alpha)\), largest at \(\alpha=1/2\).

The phase transition also has three different fluctuation laws. Let \(Z\) be standard normal. If \(k_n/n\to\alpha\in(0,1/2)\), then
\[
\frac{\log_2 F_{n,k_n}(W_n)-2k_n}{\sqrt{2k_n}}\ \Longrightarrow\ Z.
\]
For the critical sequence \(k_n=\lfloor n/2\rfloor\),
\[
\frac{n-\log_2 F_{n,k_n}(W_n)}{\sqrt n}\ \Longrightarrow\ \max(0,Z),
\]
whose law has an atom of mass \(1/2\) at zero. If \(k_n/n\to\alpha\in(1/2,1]\), then
\[
\log_2 F_{n,k_n}(W_n)-n+\frac12\log_2(\pi n/2)
\ \Longrightarrow\ -\frac{Z^2}{2\ln2}.
\]

## Assumptions and scope

Words are finite strings over the ordered alphabet \(0<1\), and \(\tau\) is the recursive operator from Defant and Kravitz (not the faster hare operator). The input measure is the uniform measure on all \(2^n\) words, not a fixed-composition or a prescribed infinite factor language. For \(k=0\), the operator is the identity and has \(2^n\) singleton fibers; for \(k\ge n\), all words are sorted and \(n+1\) nonempty fibers have binomial sizes \(\binom nr\). The stated exact spectrum treats \(1\le k\le n\); the rate statements include both endpoint proportions.

A word with \(r\) ones has unique gap representation
\[
w=0^{g_0}1\,0^{g_1}1\cdots1\,0^{g_r},\qquad g_j\ge0.
\]
A zero-length gap is allowed. An inverse class always consists of words with the same number of ones.

## Proof

**1. Exact action.** The Defant--Kravitz recursive definition implies
\[
\tau(w)=0^{g_0+g_1}1\,0^{g_2}1\cdots1\,0^{g_r}1
\]
when \(r\ge1\) (the evident interpretation also applies at \(r=1\)); zero-only words are fixed. Iterating gives, for \(s=\min(k,r)\),
\[
\tau^k(w)=0^{g_0+\cdots+g_s}1\,0^{g_{s+1}}1\cdots1\,0^{g_r}1^s
\]
when \(r>s\), and the sorted word \(0^{g_0+\cdots+g_r}1^r\) when \(r=s\). In words, each pass moves the first remaining one to the final run of ones. This deterministic identity is established background; the new conclusions concern inverse-class enumeration and limiting laws.

**2. Inverse fibers and support.** If a target \(y\) has \(r<k\) ones, it is in the image exactly when sorted, and then every word of that composition maps to it: the fiber contains \(\binom nr\) words. If \(r\ge k\), the output ends in \(1^k\), and conversely every length-\(n\) word with that suffix is attained: recover it by splitting the leading zero gap of size \(h\) into \(k+1\) nonnegative gaps. The number of splittings is \(\binom{h+k}{k}\), independent of subsequent bits. For \(r=k\), the target is the sorted word and this is \(\binom nk\). For each \(h\) with \(0\le h<n-k\), the number of other suffix-\(1^k\) outputs beginning with exactly \(h\) zeros is \(2^{n-k-h-1}\), because the next bit is one and the following bits are free. This proves the full spectrum, whose support comprises \(2^{n-k}\) suffix-\(1^k\) words and \(k\) additional sorted words. The largest inverse class is the largest of \(\binom nr\) over \(0\le r\le k\), by monotonicity of the gap splitting count and binomial unimodality.

**3. Source-weighted representation.** Extend the fair binary input to an infinite independent fair sequence. Let \(B_n\) be the number of ones among its first \(n\) letters. Let \(G_k\) be the number of zeros strictly preceding the \((k+1)\)-st one in the infinite sequence. Then \(G_k\) is a sum of \(k+1\) independent geometric-zero-count random variables of mean one and variance two. Define \(E_{n,k}=\{B_n\ge k+1\}=\{G_k\le n-k-1\}\). The exact fiber result proves the distributional identity
\[
F_{n,k}(W_n)=
\begin{cases}
\binom{G_k+k}{k},&E_{n,k},\\
\binom n{B_n},&E_{n,k}^{\mathrm c}.
\end{cases}
\]
This identity couples all finite-source classes to a binomial count and a negative-binomial stopping time.

**4. Subcritical regime.** If \(k_n/n\to\alpha\in(0,1/2)\), binomial concentration makes \(\Pr(E_{n,k_n})\to1\). The law of large numbers and central limit theorem give
\[
G_k/k\xrightarrow{\mathsf P}1,\qquad
(G_k-k)/\sqrt{2k}\Longrightarrow Z.
\]
For \(|h-k|=O(\sqrt k)\), the binomial-ratio product and Stirling's formula yield the uniform local expansion
\[
\log_2\binom{h+k}{k}
=2k+(h-k)+O\left(\log k+\frac{(h-k)^2}{k}\right).
\]
Consequently the normalized log class size tends to \(2\alpha\), and its centered and scaled form tends to the standard normal. If \(\alpha=0\), the bound \(G_k=O_{\mathsf P}(k+1)\), with \(k=o(n)\), implies \(\log_2 F=o_{\mathsf P}(n)\), while \(k=0\) is immediate.

**5. Critical regime.** Take \(k=\lfloor n/2\rfloor\). Then \((G_k-k)/\sqrt n\Longrightarrow Z\), and the event \(E_{n,k}\) is precisely \(G_k-k\le n-2k-1\). On that event the preceding local expansion gives
\[
(n-\log_2F_{n,k})/\sqrt n=-(G_k-k)/\sqrt n+o_{\mathsf P}(1).
\]
On the complementary event, \(B_n=n/2+O_{\mathsf P}(\sqrt n)\) and the central binomial estimate gives \(n-\log_2\binom n{B_n}=O_{\mathsf P}(\log n+1)\), negligible after division by \(\sqrt n\). The threshold \((n-2k-1)/\sqrt n\to0\) therefore yields the positive-part Gaussian limit. The first-order class-size rate is one.

**6. Supercritical regime.** For \(k_n/n\to\alpha\in(1/2,1]\), binomial concentration gives \(\Pr(B_n\le k_n)\to1\). Thus with high probability \(F=\binom n{B_n}\). Since \((B_n-n/2)/(\sqrt n/2)\Longrightarrow Z\), Stirling's formula uniformly in the central \(O(\sqrt n)\) window gives
\[
\log_2\binom n{B_n}
=n-\frac12\log_2(\pi n/2)
-\frac{2(B_n-n/2)^2}{n\ln2}+o_{\mathsf P}(1),
\]
proving the quadratic-normal limit. At \(\alpha=1/2\) with other sequences \(k_n/n\to1/2\), the first-order rate follows by the same laws of large numbers and the exact coupling, without asserting a universal second-order limit.

**7. Entropies.** As a deterministic function of a uniform \(n\)-bit input, \(Y_{n,k}\) has conditional uniform input on each of its fibers. The chain rule therefore gives exactly
\[
H(Y_{n,k})=n-\mathbb E[\log_2F_{n,k}(W_n)].
\]
Since \(0\le\log_2F\le n\), convergence in probability of the normalized log fiber implies convergence of its expectations. The support size in Step 2 gives \(\log_2(k_n+2^{n-k_n})/n\to1-\alpha\). Subtraction yields the stated entropy-rate gap.

## Verification

Run `python3 verify_exact.py` for an independent recursive evaluation on all binary words of lengths zero through twelve and every iteration count. It checks exact pointwise inverse sizes and image histograms (98,305 word/iteration instances). Run `python3 verify_probabilities.py` for a separate composition-based census covering all 5,050 parameter pairs with lengths one through 100, including full mass conservation, image counts and sharp maximum size, plus Shannon-entropy values for length 100, 200, 400 and 800 at three iteration proportions. Both programs use Python's standard library. Their output records are supplied as `verify_exact.out` and `verify_probabilities.out`.

The finite checks corroborate the exact formulas only within their stated ranges. The infinite fluctuation laws follow from the analytic proof and are not inferred from those finite computations.

## Relationship to prior work

Defant and Kravitz introduced the tortoise operator, its iterates and fertility questions in *Stack-sorting for words* (first available arXiv September 24, 2018; *Australasian Journal of Combinatorics* 77 (2020), 51--68). Campbell and Rampersad's *Subword enumeration up to stack-sorting equivalence* (first submitted April 28, 2026, arXiv:2604.25811) defines iterative binary tortoise equivalence and studies the complexity of restricted automatic-word factor languages. Its Section 3 already observes the underlying relocation of the first \(k\) ones, which is **not** claimed as new. The present theorem addresses a different, full-cube probability space and determines the inverse-fiber spectrum and the three distinct limiting fluctuation laws, as well as the Hartley/Shannon separation. Related exact tortoise computations for restricted morphic or Christoffel factor languages are distinct from this uniform-all-words problem.

## Limitations

The theorem assumes a fair independent binary source and the Defant--Kravitz tortoise convention. It does not assert the analogous asymptotics for biased sources, larger alphabets, specific automatic or morphic factor languages, or the hare map. The critical fluctuation statement is for the particular sequence \(k=\lfloor n/2\rfloor\); sequences differing from \(n/2\) at order \(\sqrt n\) can have other critical crossover laws. Originality is assessed against accessible literature and is not a claim of an exhaustive global publication search. Independent mathematical audit has not been performed.

## References

1. J. M. Campbell and N. Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811, first submitted 2026-04-28; version 2 dated 2026-10-05. https://arxiv.org/pdf/2604.25811v2
2. C. Defant and N. Kravitz, *Stack-sorting for words*, arXiv:1809.09158, first submitted 2018-09-24; *Australasian Journal of Combinatorics* 77 (2020), 51--68. https://ajc.maths.uq.edu.au/pdf/77/ajc_v77_p051.pdf
