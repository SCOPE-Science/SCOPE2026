# Block-image condensation and a sharp entropy hierarchy for partition-preserving retractions

## Finding
Fix an integer \(m\ge2\). Let \(X\) be partitioned into \(m\) labeled blocks \(B_1,\ldots,B_m\), each of size \(n\). Choose uniformly from all **full** maps \(f:X\to X\) preserving the partition and satisfying \(f^2=f\). Every such map induces a block map \(\phi_f:[m]\to[m]\), which is itself idempotent. Write \(K_n=|\operatorname{im}\phi_f|\), and let \(R_n=|\operatorname{im} f|\).

For every fixed idempotent block map \(\phi\), let \(s_1,\ldots,s_k\) be the cardinalities of the fibers of \(\phi\) over its \(k\) fixed blocks (so \(s_i\ge1\), \(\sum_i s_i=m\)). Then the following sharp logarithmic probability limit holds:
\[
\boxed{\lim_{n\to\infty}\frac{1}{n}\log\Pr(\phi_f=\phi)
=\sum_{i=1}^k s_i\log s_i-m\log m.}\tag{1}
\]
Consequently, for every \(1\le k\le m\),
\[
\boxed{\lim_{n\to\infty}\frac{1}{n}\log\Pr(K_n=k)
=(m-k+1)\log(m-k+1)-m\log m.}\tag{2}
\]
Here \(1\log1=0\). Thus with probability tending to one **all \(m\) source blocks map into a single image-bearing block**, selected uniformly among the \(m\) blocks. The probability of at least two image-bearing blocks decays with exact exponential rate
\[
\boxed{\lim_{n\to\infty}\frac{1}{n}\log\Pr(K_n\ge2)
=(m-1)\log(m-1)-m\log m<0.}\tag{3}
\]
For example, with two blocks the failure of this collapse has probability \(4^{-n+o(n)}\). Conditional on \(K_n=k\), the limiting dominant block-fiber profile is the multiset \((m-k+1,1,\ldots,1)\). Finally, for every fixed admissible block map \(\phi\), the number of image points in its rooted block of fiber size \(s\), multiplied by \(\log n/n\), converges in probability to \(s\); in particular
\[
\boxed{\frac{R_n\log n}{n}\xrightarrow{\Pr}m.}\tag{4}
\]
The result is the joint entropy law of block-image condensation and image-rank scaling, **not** a claim of new finite idempotent counts.

## Assumptions and scope
A full transformation \(f:X\to X\) *preserves the partition* if the image of each entire block lies inside some block, which can be the same or a different one. All original blocks are labeled, and all points within them are labeled. Fix \(m\ge2\) while \(n\to\infty\) through integers \(n\ge2\). Probabilities refer to the uniform distribution on idempotents of this finite transformation monoid. Natural logarithms are used. The block map \(\phi_f\) is well-defined because blocks are nonempty and images are nonempty. Its image is the set of blocks containing image points of \(f\). The rank \(R_n\) counts actual points of \(X\), not blocks. The theorem does not assert an asymptotic uniformity in growing \(m\).

## Proof
**Exact conditional weight (previously enumerated).** For an idempotent \(\phi:[m]\to[m]\) with \(k\) fixed points and fiber sizes \(s_1,\ldots,s_k\), let
\[
J_s(n)=\sum_{r=1}^{n}\binom nr r^{sn-r}\qquad(s\in\{1,\ldots,m\}).
\]
An idempotent transformation has each image point fixed. For every fixed block of \(\phi\), choose \(r\) image points in that block; these are fixed. Each of the remaining \(n-r\) points of that block, and all \(n(s-1)\) points in source blocks assigned to it, can independently map to any of the \(r\) chosen image points. Thus the number of idempotents inducing exactly \(\phi\) is
\[
W_n(\phi)=\prod_{i=1}^k J_{s_i}(n),\qquad
Z_{m,n}=\sum_{\phi^2=\phi}W_n(\phi).
\tag{5}
\]
This is a grouping of the established finite enumeration in Dolinka and East [1, Proposition 3.1], and is used only as the starting point for the asymptotic theorem.

**Uniform one-dimensional saddle lemma.** For each fixed positive integer \(s\), put \(L=\log n\) and \(t=rL/n\), where \(1\le r\le n\). The summand \(T_{s,n}(r)=\binom nr r^{sn-r}\) obeys the exact equality
\[
\frac1n\log T_{s,n}(r)-s\log(n/L)
=s\log t-t+\delta_n(t),\quad
\delta_n(t)=\frac{t}{L}\log\frac{L}{t}+\frac1n\log\binom nr.
\tag{6}
\]
The variable \(t\) belongs to \((0,L]\). The correction is nonnegative and is bounded globally by \(1/e+\log2\), since \(u\log(1/u)\le1/e\) for \(0<u\le1\) and \(\binom nr\le2^n\). On every fixed compact interval \([a,b]\subset(0,\infty)\), it tends uniformly to zero: the first term is at most \(O((\log L)/L)\), and the second is bounded by the binary entropy \(h(t/L)\to0\) uniformly. The limiting function \(s\log t-t\) tends to minus infinity as \(t\downarrow0\) or \(t\to\infty\), and has a unique maximum at \(t=s\) of value \(s\log s-s\). The global bound on the correction therefore excludes both tails from maximizing the sum. Evaluating at the integer nearest \(sn/L\) and using the uniform compact estimate prove
\[
\boxed{\log J_s(n)=sn\log\frac{n}{\log n}
+n(s\log s-s)+o(n).}\tag{7}
\]
The factor of at most \(n\) summands changes its logarithm by at most \(\log n=o(n)\). The strict unique maximizer and the same tail bounds show that, for a random \(r\) drawn with probability proportional to \(T_{s,n}(r)\),
\[
\frac{r\log n}{n}\xrightarrow{\Pr}s.
\tag{8}
\]
Indeed, outside any neighborhood of \(s\), the maximized exponent has a strictly positive \(n\)-scale gap.

**Block-map entropy.** Substituting (7) in (5), for any fixed \(\phi\) we have
\[
\log W_n(\phi)=mn\log\frac n{\log n}
+n\left(\sum_{i=1}^k s_i\log s_i-m\right)+o(n).
\tag{9}
\]
The set of block-idempotent maps is finite and independent of \(n\). For every composition \(m=s_1+\cdots+s_k\), the inequality
\(\sum_i s_i\log s_i\le m\log m\)
holds, with equality only if \(k=1\), because the function \(x\log x\) is strictly superadditive for positive arguments. There are exactly \(m\) constant block maps, each attaining equality. Therefore the finite sum in (5) has logarithmic asymptotic
\[
\log Z_{m,n}=mn\log\frac n{\log n}
+n(m\log m-m)+o(n).
\tag{10}
\]
Dividing (9) by (10) proves (1), including its normalization and exact domain of quantification.

**The hierarchy by image-bearing blocks.** For a prescribed \(k\), maximize \(\sum_i s_i\log s_i\) over positive integers \(s_i\) summing to \(m\). A transfer of one unit from any part \(b\ge2\) to a part \(a\ge b\) strictly increases this sum, by strict convexity of \(x\log x\). Hence the unique maximizing multiset is \((m-k+1,1,\ldots,1)\). Since only finitely many \(\phi\) exist, taking the logarithm of their sum yields (2). The right side decreases strictly with \(k\), so among \(k\ge2\), \(k=2\) determines the decay of the union, proving (3). Symmetry of the labels makes the dominant root block exactly uniform given \(k=1\), and (3) implies unconditional condensation.

**Image rank.** Given \(\phi\), the rooted blocks' image ranks are independent under the conditional uniform measure, each distributed as the saddle weight \(T_{s_i,n}(r)/J_{s_i}(n)\). By (8), their sum, multiplied by \(L/n\), tends to \(\sum_i s_i=m\), for each fixed \(\phi\). A finite mixture over possible \(\phi\) proves (4), completing the theorem.

## Verification
The standalone, standard-library-only script `verify_fixed_block_retractions.py` independently enumerates actual labeled full transformations, tests partition preservation and \(f^2=f\) through direct composition, and groups them by exact block map. It compares those counts with the product (5). Its direct checks passed for \((m,n)=(2,2),(2,3),(3,2),(3,3),(4,2)\), yielding totals \(21,256,189,9028,2073\), respectively. The first four published examples for these parameters agree with [1, Table 3]. Numerical log-sum-exp calculations test the convergence of the logarithmic expressions for \(m=2,3,4\) and \(n=2000\); their finite values are not claimed to equal their limiting constants. Execute `python3 verify_fixed_block_retractions.py` from this package; a successful run prints `VERIFY_OK_FIXED_BLOCK_RETRACTIONS`.

## Relationship to prior work
Dolinka and East [1, Proposition 3.1, Proposition 3.2, Table 3] explicitly classify and enumerate all finite idempotents of exactly this uniform-partition endomorphism monoid. Those formulas are stronger **for finite enumeration** and are not claimed as new; the proof uses their finite count as an input. The contribution is the fixed-block-count asymptotic **law for the random image-block pattern**, its nontrivial ordered entropy rates for all exact block-map fibers, the sharp \(k\)-root hierarchy, and universal leading image-rank scaling. These statements are not given by merely substituting a finite parameter into the prior enumeration: they require the uniform saddle lemma (6)–(8) and entropy optimization across competing block-root structures.

Dolinka, East and Mitchell [2] extend structural classification and finite enumeration to nonuniform partitions; this does not state the present fixed-\(m\), growing-\(n\) logarithmic law. Cicalò, Fernandes and Schneider [3] treat partial transformations, a different semigroup that allows undefined points; their finite trivariate partial-idempotent enumeration is also recorded in a subsequent accessible research result [4]. Krattenthaler and Müller [5] develop semigroup-equation asymptotics for \(H\wr\mathcal T_n\) with a **fixed finite group** \(H\) and a growing number of top-level letters, not for \(\mathcal T_n\wr\mathcal T_m\) with fixed \(m\) and expanding blocks.

## Limitations
The exact finite counts and their block-map decomposition were known before this result. The theorem addresses a different asymptotic regime, but prior explicit formulas logically determine its finite sequence; an unpublished saddle analysis or a broad wreath-product limit theorem may already imply the same entropy limits. The proof holds only for fixed \(m\), not \(m\) growing with \(n\), and gives logarithmic \(n\)-speed rates, not asymptotically exact constants or moderate-deviation corrections. The rank convergence has no claimed central limit theorem. The numerical checks are finite corroboration only; the general conclusions rest on the proof above. Independent mathematical audit has not been performed.

## References
[1] I. Dolinka and J. East, *Idempotent generation in the endomorphism monoid of a uniform partition*, arXiv:1407.3312v1, publicly posted 11 July 2014, especially Proposition 3.1, Proposition 3.2 and Table 3; *Communications in Algebra* 44 (2016), 5179–5198. https://arxiv.org/abs/1407.3312

[2] I. Dolinka, J. East and J. D. Mitchell, *Idempotent rank in the endomorphism monoid of a nonuniform partition*, arXiv:1504.02520v1, publicly posted 9 April 2015; *Bulletin of the Australian Mathematical Society* 93 (2016), 73–91. https://arxiv.org/abs/1504.02520

[3] S. Cicalò, V. H. Fernandes and C. Schneider, *Partial transformation monoids preserving a uniform partition*, arXiv:1210.4775v1, publicly posted 17 October 2012. https://arxiv.org/abs/1210.4775

[4] *Joint rank, domain, and image-block spectrum of uniform-partition partial idempotents*, publicly accessible results and proof, 26 October 2026. https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-joint-rank-domain-and-image-block-spectrum-of-uniform-partition--70fcbccf178c/RESULT.md

[5] C. Krattenthaler and T. Müller, *Equations in finite semigroups: Explicit enumeration and asymptotics of solution numbers*, arXiv:math/0303028, publicly posted 3 March 2003. https://arxiv.org/abs/math/0303028
