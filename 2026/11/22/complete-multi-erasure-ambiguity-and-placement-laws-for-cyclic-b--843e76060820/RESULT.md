# Complete multi-erasure ambiguity and placement laws for cyclic binary pair-sum reads

## Finding

Fix integers \(n\ge3\) and \(2\le e\le n\). An indexed binary circular source \(x=(x_0,\ldots,x_{n-1})\in\{0,1\}^n\) has integer pair-sum reads \(s_i=x_i+x_{i+1\bmod n}\). A known set \(E\subseteq\{0,\ldots,n-1\}\) of \(e\) read coordinates is erased, and the remaining reads retain their labels and numerical values. Removing the corresponding \(e\) edges of the cycle leaves \(e\) vertex-disjoint paths; write their positive vertex counts as \(v_1,\ldots,v_e\), so \(\sum_jv_j=n\). Isolated vertices are paths of size one.

**Complete inverse-list spectrum.** Let \(N_k(E)\) be the number of *distinct attainable read vectors* with exactly \(2^k\) source preimages. There are no other positive fiber sizes, and
\[
\boxed{\sum_{k=0}^{e}N_k(E)t^k=\prod_{j=1}^{e}(2^{v_j}-2+t).}
\]
In particular, the maximum zero-error distinguishable codebook under this fixed erasure pattern has cardinality
\[
\boxed{A(E)=\prod_{j=1}^{e}(2^{v_j}-1).}
\]
The largest inverse list has exactly \(2^e\) sources and occurs for precisely one attainable read vector, namely the vector whose every surviving pair sum is one. If any path is a singleton, then no attainable vector has a unique source.

**Best and worst placement for a fixed erasure count.** Write \(n=ae+r\) with \(0\le r<e\). Among all \(\binom ne\) patterns of \(e\) erased positions,
\[
\boxed{\min_{|E|=e}A(E)=2^{n-e+1}-1,\qquad
\max_{|E|=e}A(E)=(2^a-1)^{e-r}(2^{a+1}-1)^r.}
\]
Minimum-capacity masks have \(e-1\) singleton paths and one path of size \(n-e+1\). Maximum-capacity masks have component sizes differing by at most one. These conditions include coincident extrema in degenerate cases.

**All-mask census.** For \(0\le k\le e\), let \(T_{n,e,k}=\sum_{|E|=e}N_k(E)\). Then
\[
\boxed{\sum_{k=0}^e T_{n,e,k}t^k=\frac ne[z^{n-e}]\left(\frac{t+2(1-t)z}{(1-z)(1-2z)}\right)^e.}
\]
This counts all inverse lists across all erasure patterns with at least two erased readings, including the exactly averaged optimal codebook size \(\binom ne^{-1}\sum_k T_{n,e,k}\).

**Sharp random-erasure reconstructibility transition.** For uniformly selected \(e\)-element erasure masks, at least one uniquely reconstructed source exists if and only if no two erased read positions are cyclically adjacent. Its probability is exactly
\[
\boxed{p_{n,e}=\begin{cases}\displaystyle\frac{n}{n-e}\frac{\binom{n-e}{e}}{\binom ne},&2e\le n,\\[4pt]0,&2e>n.\end{cases}}
\]
Consequently, if \(e/\sqrt n\to c\in[0,\infty)\), then \(p_{n,e}\to e^{-c^2}\); it tends to zero whenever \(e/\sqrt n\to\infty\), and tends to one when \(e=o(\sqrt n)\). The exponent here is Euler's exponential function, not the erasure count.

## Assumptions and scope

The binary source is indexed (rotations are different). Both source and read positions are cyclic; window size is exactly two. Pair weights are ordinary integer sums, not parity or ordered pairs. Erasures are known *positions in the read vector*, not unknown source-bit deletions. All un-erased pair weights are noiseless, and the codebook capacity is the size of the observation image, since one codeword can be selected from each inverse fiber. The theorem is stated for at least two known erased reads (the case of one erased read is a previously studied boundary case); it includes the all-erased pattern.

## Proof

**1. One path has a single ambiguous reading.** On a path with \(v\ge1\) vertices \(b_1,\ldots,b_v\), the observed sums are \(b_i+b_{i+1}\) for \(1\le i<v\). Fixing the first bit determines every subsequent bit inductively. Thus an attainable reading has at most two sources. If both choices for the first bit produce binary sources, then at every vertex the two solutions have complementary values (their differences alternate \(+1,-1,+1,\ldots\)). Every observed sum must therefore equal one. Conversely, the all-one reading is realized by the two alternating binary paths. Hence the \(2^v\) sources form exactly one two-source fiber and \(2^v-2\) singleton fibers. For \(v=1\), the single empty reading has two sources, so the same statement holds.

**2. Independent path products.** Every surviving read lies on exactly one component of the cycle after edge erasures. Conversely, the bit assignments on distinct components can be combined freely. Thus image fibers are Cartesian products of component fibers. Choosing for each component a singleton reading contributes the factor \(2^{v_j}-2\), while choosing its one doubleton reading contributes one factor \(t\) and doubles the resulting list size. Multiplication proves the full \(N_k\) polynomial, its sum at \(t=1\), and the unique \(2^e\)-element fiber. Evaluating at \(t=2\) recovers \(\sum_k2^kN_k(E)=\prod_j2^{v_j}=2^n\), also checking conservation of source mass.

**3. Extremal erasure placement.** Put \(a_v=2^v-1\). For each positive integer \(v\),
\[
(2^{v+1}-1)^2-(2^v-1)(2^{v+2}-1)=2^v>0.
\]
Therefore the discrete increments of \(\log a_v\) strictly decrease with \(v\). Replacing a component-size pair \((u,v)\) with \((u-1,v+1)\) for \(u\ge v+2\) strictly increases \(a_ua_v\). Repeating this operation makes the sizes differ by at most one and maximizes their product. Reversing the operation toward \((u+1,v-1)\) while \(v\ge2\) strictly decreases the product; this terminates at \((n-e+1,1,\ldots,1)\) and gives the minimum. Every positive ordered composition of \(n\) into \(e\) parts occurs as consecutive gaps between erased cycle edges, so these extremizers are realizable. Substituting their sizes gives both formulas.

**4. Averaging over all masks.** Mark one of the \(e\) erased edges and, proceeding cyclically from this edge, record the numbers of vertices in the successive \(e\) paths. These are positive integers summing to \(n\). The marked edge can be in any of \(n\) positions, and each unmarked mask is represented exactly \(e\) times. Since
\[
\sum_{v\ge1}(2^v-2+t)z^v=\frac{z\bigl(t+2(1-t)z\bigr)}{(1-z)(1-2z)},
\]
coefficient extraction from the \(e\)-fold product, followed by multiplication by \(n/e\), gives the stated polynomial for \(T_{n,e,k}\).

**5. The erasure-mask threshold.** The number of singleton readings is \(N_0(E)=\prod_j(2^{v_j}-2)\). It is positive exactly when all \(v_j\ge2\), equivalently when no erased edges are adjacent. The marked-edge argument now counts all such masks as \((n/e)\binom{n-e-1}{e-1}\) if \(2e\le n\), and zero otherwise. Dividing by \(\binom ne\) gives the exact probability. For \(e=O(\sqrt n)\), taking logarithms of
\[
\frac{n}{n-e}\prod_{j=0}^{e-1}\frac{n-e-j}{n-j}
\]
yields \(\log p_{n,e}=-e^2/n+o(1)\) whenever \(e/\sqrt n\) has a finite limit. For \(\sqrt n\ll e\le n/2\), the same product is at most \(2\exp(-e^2/n)\); beyond \(n/2\), it vanishes identically. This proves all asserted limiting regimes.

## Verification

The supplied standalone `verify.py` enumerates every binary word and every nonempty erasure pattern at lengths \(3\le n\le10\). It directly groups outputs into source fibers and compares the complete observed list-size polynomial to the predicted path product. It also checks total source mass, the product-series all-mask polynomial, the sharp minimum and maximum over masks, and the exact criterion and count for masks admitting singleton fibers. It completed 2,032 mask cases and 1,396,040 direct source evaluations without a mismatch. Additional arithmetic checks for \(e\approx\sqrt n\) at lengths \(100,400,1600,6400\) converge toward \(e^{-1}\); those numerical checks are illustrative, not proof of the limit.

Run reproducibly with `python3 verify.py` in a standard Python 3 environment, with no external dependencies. These experiments are finite corroboration only; the proof above establishes all universal quantifiers.

## Relationship to prior work

Sporring and Darkner [1], Section 4.3, prove that a noncyclic binary length-two local-histogram readout has exactly one non-singleton metameric class. This is precisely the single-path building block in Step 1; that building block is *not claimed as new*. Their paper does not analyze arbitrary known deletions of indexed cyclic readings, the interaction of resulting component sizes with fixed-erasure-rate optimal placement, the exact all-mask inverse-list census, or the square-root erasure threshold.

A published complete cyclic weighted-read classification [3] treats the case of **no read erasures** and arbitrary widths. A subsequent known-position one-erasure calculation [4] handles exactly **one missing read coordinate** and arbitrary widths. The present result changes the parameter from one erasure to every possible nonempty mask and fixes width two, yielding independent path components, their full inverse-list spectrum, sharp placement optima, and a probabilistic threshold. Neither the full-read fiber classification nor the one-erasure theorem alone asserts this multi-erasure result. Yerushalmi, Etzion and Yaakobi [2] analyze a sliding weighted-read capacity model with noncyclic output and generally different observation boundaries; its abstract does not imply the formulas here. Symbol-pair channels that reveal the *ordered pair of symbols* (rather than the pair's integer sum) retain strictly more information and have different reconstruction problems.

## Limitations

This is an exact noiseless, position-known-erasure result only for binary circular integer pair sums. It does not address unknown erasure locations, higher window widths, source deletions, read substitutions, unordered read multisets, or adversarial coding without knowledge of the erasure pattern at the decoder. The path-level two-source ambiguity was already established in [1]; novelty is claimed only for its complete arbitrary-mask consequences and placement/threshold classifications. An equivalent earlier treatment under graph edge-sum or binary tomography terminology may remain unindexed. No independent mathematical audit has yet been conducted.

## References

[1] J. Sporring and S. Darkner, *Reconstructing Binary Signals from Local Histograms*, Entropy **24**(3), 433 (21 March 2022), DOI: 10.3390/e24030433. https://doi.org/10.3390/e24030433.

[2] O. Yerushalmi, T. Etzion and E. Yaakobi, *The Capacity of the Weighted Read Channel*, arXiv:2401.15368v1, first public 27 January 2024. https://arxiv.org/abs/2401.15368.

[3] *Exact fiber and constant-weight capacity laws for cyclic binary weighted reads*, public mathematical research record (2026), identifier 21136e4ec91c.

[4] *Exact capacity and ambiguity of one-erased cyclic weighted reads*, public mathematical research record (2026), identifier 9ee0bce770fc.
