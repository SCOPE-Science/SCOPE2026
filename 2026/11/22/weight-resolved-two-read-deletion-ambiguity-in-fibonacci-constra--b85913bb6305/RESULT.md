# Weight-resolved two-read deletion ambiguity in Fibonacci-constrained binary words

## Finding

Fix integers \(n\ge2\) and \(k\ge1\). Let \(\mathcal F_n\) consist of all indexed binary words of length \(n\) with no adjacent ones. For \(x\in\mathcal F_n\), let \(D(x)\) be the set of *distinct* outputs of exactly one ordinary symbol deletion. Define the two-read confusability graph \(G_n\) by joining distinct vertices if their deletion-output sets have at least two common elements. Let \(A_{n,k}\) count unordered edges joining two words of weight \(k\), and \(B_{n,k}\) unordered edges joining weights \(k\) and \(k+1\). Then

\[
A_{n,k}=\begin{cases}(n-2k+1)\binom{n-k+1}{k-1},&2k\le n,\\0,&2k>n,\end{cases}
\qquad
B_{n,k}=\begin{cases}(n-2k)\binom{n-k}{k-1},&2k+1\le n,\\0,&2k+1>n.\end{cases}
\]

No other weight-layer edges exist. In particular, \(B_{n,k}=A_{n-1,k}\) for every \(n,k\) with zero-outside-range convention. Both exact bivariate generating functions are rational:

\[
\sum_{n\ge0,k\ge1}A_{n,k}z^nu^k=\frac{uz^2}{(1-uz^2)(1-z-uz^2)^2},\qquad
\sum_{n\ge0,k\ge1}B_{n,k}z^nu^k=\frac{uz^3}{(1-uz^2)(1-z-uz^2)^2}.
\]

Every nonempty fixed-weight layer is connected as an induced subgraph. For \(n\ge2\), precisely two connected components of \(G_n\) exist: the isolated all-zero word, and the connected collection of all words containing at least one one. Among all edges, the proportion preserving weight tends to \(\varphi^{-1}\), and the proportion changing weight tends to \(\varphi^{-2}\), where \(\varphi=(1+\sqrt5)/2\).

## Assumptions and scope

The binary alphabet is labeled `0,1`. Words are indexed linear words (not necklaces). The `11` constraint is on sources, not on their deletion outputs. Deleting equal letters at different positions can yield the same output; the output sets discard duplicate reads. The graph requires **at least two distinct common outputs**. Weight is the number of ones. Binomial coefficients with infeasible arguments and formula terms outside the stated ranges are interpreted as zero. No assertion is made about maximum independent sets or perfect codes.

## Proof

**Step 1: the edge normal form.** For two unequal binary words with at least two distinct common single-deletion outputs, their first through last differing positions form one contiguous interval of length \(L\ge2\); on that interval they are complementary alternating binary words, and they agree everywhere else. Conversely, such a pair has two distinct common outputs. This is the standard two-read alternating-interval characterization; it may also be checked by comparing the two different deletion alignments. The unique first/last differing interval prevents double counting. Rispoli and Cosares (2008, Proposition 1) proved the related single-interval adjacency characterization for the Fibonacci hypercube, which also includes single-bit changes; here those length-one changes are excluded because they have fewer than two common deletion outputs.

**Step 2: allowable contexts.** Both alternating phases contain a one at each internal alternating neighborhood. Thus, for *both* source words to avoid `11`, the immediately preceding and following symbols, when present, must be zero. Every allowed outside prefix is either empty or ends in zero and avoids `11`, while every allowed suffix is empty or starts in zero and avoids `11`. Such prefixes decompose uniquely into a sequence of blocks `0` and `10` and suffixes have the same weight enumerator by reversal. Denote this generating function by
\[
P(z,u)=\frac1{1-z-uz^2},
\]
where \(z\) marks length and \(u\) marks ones. The prefix and suffix are independent.

**Step 3: count the unique varying interval.** An interval of even length \(2t\), \(t\ge1\), has \(t\) ones in both opposite phases and contributes one unordered edge per pair of allowable contexts. An odd interval of length \(2t+1\), \(t\ge1\), has \(t\) ones in one phase and \(t+1\) in the other; mark the smaller endpoint weight by \(u\). In both cases there is exactly one unordered phase pair. Hence the respective generating functions are
\[
P(z,u)^2\sum_{t\ge1}(uz^2)^t
=\frac{uz^2}{(1-uz^2)(1-z-uz^2)^2},
\]
\[
P(z,u)^2\sum_{t\ge1}z(uz^2)^t
=\frac{uz^3}{(1-uz^2)(1-z-uz^2)^2}.
\]
No interval changes the endpoint weights by more than one. An interval of length at least two contains a one in both phases, so the zero word is isolated.

**Step 4: extract exact coefficients.** For integers \(a,b\ge0\),
\[
[z^{a+2b}u^b]P(z,u)^2=(a+b+1)\binom{a+b}{b}.
\]
For fixed \(n,k\), put \(a=n-2k\) for equal-weight edges and \(a=n-2k-1\) for cross-weight edges. Sum over intervals with \(t=1,\ldots,k\), or equivalently over \(b=k-t=0,\ldots,k-1\). The hockey-stick identity
\[
\sum_{b=0}^{k-1}(a+b+1)\binom{a+b}{b}
=(a+1)\binom{a+k+1}{k-1}
\]
gives exactly the two displayed binomial formulas, including their feasibility boundaries. This is a coefficient identity in formal power series, not an extrapolation from finite data.

**Step 5: connectivity.** Within a fixed positive weight layer, any legal `01`-to-`10` interchange that preserves the no-`11` condition is a length-two alternating toggle and hence an edge. Move the leftmost one to coordinate one, then the next one to coordinate three, and so forth; at each step the move remains legal because all previously packed ones are separated by zeros. Thus every word of weight \(k\) reaches the canonical word \((10)^{k-1}1\,0^{n-2k+1}\), proving connectivity whenever the layer exists. For every adjacent pair of nonempty layers, \(1\le k<\lceil n/2\rceil\), the words with a local `010` versus `101` block after \(k-1\) appropriately separated ones yield an edge; equivalently \(B_{n,k}>0\). These links join all positive layers. The zero layer is isolated, proving the component claim for \(n\ge2\).

**Step 6: asymptotic split.** Specialize \(u=1\). The equal-weight edge-count series is
\[
A(z)=\frac{z^2}{(1-z^2)(1-z-z^2)^2},\qquad B(z)=zA(z).
\]
The unique dominant singularity of both is the positive double pole \(\rho=(\sqrt5-1)/2=\varphi^{-1}\). Consequently \([z^n]A(z)\sim c n\rho^{-n}\) for a positive constant \(c\), and \([z^n]B(z)/[z^n]A(z)\to\rho\). Their limiting edge fractions are \(1/(1+\rho)=\varphi^{-1}\) and \(\rho/(1+\rho)=\varphi^{-2}\).

## Verification

The included `verify_fibonacci_weight_edges.py` independently constructs all source words and deletion-output sets and tests every pair, without using the alternating-interval theorem in the enumeration. It compares all \(A_{n,k}\) and \(B_{n,k}\) to the closed formulas for every \(2\le n\le12\). It also checks the zero component and connectivity for that finite range. A second coefficient routine checks the two rational series through length 45 and the identity \(B_{n,k}=A_{n-1,k}\). These checks verify implementation and edge cases; the proof above establishes the infinite claims.

## Relationship to prior work

Levenshtein (2001) and Cai et al. (2020) developed single-deletion reconstruction and its exact overlapping-read criterion. Rispoli and Cosares (2008, Proposition 1) characterize the *larger* Fibonacci-hypercube graph whose edges include single-bit toggles; their Proposition 2 counts its unweighted edges. The graph here is obtained by deleting those single-bit edges. Thus the univariate total edge count, \(z^2/((1-z)(1-z-z^2)^2)\), is a direct consequence of earlier results **and is not claimed as new**. Earlier unrestricted-binary weight-layer formulas also concern a larger source language. The contribution assessed here is the complete bivariate weight-preserving and weight-changing edge spectrum and the resulting boundary/connectivity and limiting-split consequences for this constrained two-read channel. The polynomial and full weighted binomial formulas were not found in the inspected publications or targeted mathematical database searches. This is a best-knowledge comparison, not a proof that an equivalent treatment does not exist.

## Limitations

This is an exact graph-edge enumeration, not an exact independence-number theorem or a bound on optimal individual zero-error code size. The key alternating-interval structural lemma is established prior work. The known full adjacency characterization makes the new bivariate enumeration accessible by elementary generating-function arguments; its value lies in the constrained, fixed-composition spectrum rather than a new general graph theorem. Earlier papers on Fibonacci-hypercube weight layers may contain equivalent formulas; that remains a specific literature risk. No independent scientific validation has been performed.

## References

1. F. J. Rispoli and S. Cosares, *The Fibonacci hypercube*, Australasian Journal of Combinatorics **40** (2008), 187–196, especially Propositions 1–3. https://ajc.maths.uq.edu.au/pdf/40/ajc_v40_p187.pdf . Public date 2008-03-11 as cataloged by MaRDI: https://portal.mardi4nfdi.de/wiki/Publication%3A5449157 .
2. V. I. Levenshtein, *Efficient reconstruction of sequences*, IEEE Transactions on Information Theory **47** (2001), 2–22. https://doi.org/10.1109/18.904499 .
3. K. Cai, H. M. Kiah, T. T. Nguyen and E. Yaakobi, *Coding for Sequence Reconstruction for Single Edits*, arXiv:2001.01376 (2020), Sections II–III. https://arxiv.org/html/2001.01376v2 .
4. M. Mollard, *Edges in Fibonacci cubes, Lucas cubes and complements*, arXiv:2102.04086 (2021), for distinguishing the ordinary Hamming-edge Fibonacci cube. https://arxiv.org/abs/2102.04086 .
