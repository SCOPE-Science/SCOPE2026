# Exact linear and cyclic capacities of ternary adjacent-sum multispectra

## Finding

Let a word use the labeled integer alphabet \(\{0,1,2\}\), and suppose its receiver retains only the **multiset** of sums of consecutive two-symbol windows, with integer (not modular) addition. With exactly \(m\ge1\) observed windows, let \(L_m\) be the number of different receiver outputs from linear words of length \(m+1\), and let \(C_m\) be the number of different outputs from indexed cyclic words of length \(m\) (including the wraparound window). Then
\[
\boxed{L_m=\binom{m+4}{4}-m^2+1},
\qquad
\boxed{C_m=\frac{m^4+8m^3-28m^2+136m+27\mathbf1_{2\nmid m}}{48}}.
\]
The complete cyclic counting generating function is
\[
\boxed{\sum_{m\ge1}C_mz^m=\frac{z(3-7z+5z^2+3z^3-3z^4)}{(1-z)^5(1+z)}}.
\]
In particular,
\[
L_m\sim\frac{m^4}{24},\qquad C_m\sim\frac{m^4}{48},\qquad\lim_{m\to\infty}\frac{C_m}{L_m}=\frac12.
\]
The two counts are the sharp finite-block zero-error code sizes for their respective deterministic readout channels: choose exactly one source per distinct output. The comparison holds at the **same number of read windows**, not the same input length.

## Assumptions and scope

For any \(m\ge1\), a linear source is \(w=(w_0,\dots,w_m)\in\{0,1,2\}^{m+1}\); its \(m\) reads are \(w_i+w_{i+1}\) for \(0\le i<m\). A cyclic source is \(w=(w_0,\dots,w_{m-1})\in\{0,1,2\}^m\) with reads \(w_i+w_{(i+1)\bmod m}\) for \(0\le i<m\); for \(m=1\), this is twice its only symbol. An output is the labeled five-component histogram \(a=(a_0,a_1,a_2,a_3,a_4)\), where \(a_s\) records the number of reads of sum \(s\) and \(\sum_s a_s=m\). Read locations, orientations and ordering are entirely forgotten, but multiplicities are retained. Sources are not quotiented by reversal, rotation, or alphabet relabeling. No noise, missing reads, symbol weights other than \(0,1,2\), or additional constraints are assumed.

## Proof

**1. Exact graph representation.** Every read of sum zero is a loop at vertex \(0\); every sum-one read is an edge \(0\!\! -\!\!1\); every sum-three read is an edge \(1\!\! -\!\!2\); and every sum-four read is a loop at vertex \(2\). The sum-two bin conflates precisely edges \(0\!\! -\!\!2\) and loops at \(1\). Introduce an integer \(k\in\{0,\dots,a_2\}\), allocate \(k\) sum-two reads to edges \(0\!\! -\!\!2\), and the other \(a_2-k\) to loops at \(1\). The resulting looped undirected multigraph has \(a_0,a_4,a_2-k\) loops at vertices \(0,2,1\) respectively and cross-edge multiplicities \(a_1,k,a_3\).

A linear word realizing \(a\) is equivalent to an Euler trail in one of these graphs; a cyclic word is equivalent to an Euler circuit. The classical undirected Euler criterion says that a nonempty looped multigraph has such a trail if and only if its positive-degree support is connected and it has zero or two odd-degree vertices; for a circuit, all degrees are even. Each traversal yields the word by recording visited vertices, and therefore sufficiency is constructive. In a three-vertex graph, the number of odd-degree vertices is always even, so the parity condition is automatic for a linear trail.

**2. Linear feasibility and exact subtraction.** The only five-bin histograms with no connected split \(k\) are the following three *disjoint* classes:

- \(a_2=a_3=0\), with \(a_1>0\) and \(a_4>0\): the \(0\!\! -\!\!1\) component is separated from a loop at \(2\);
- \(a_2=a_1=0\), with \(a_3>0\) and \(a_0>0\): the \(1\!\! -\!\!2\) component is separated from a loop at \(0\);
- \(a_1=a_2=a_3=0\), with \(a_0>0\) and \(a_4>0\): two separate loop components remain.

For completeness, if \(a_2>0\), choose \(k=a_2\) so that no sum-two reads become vertex-one loops; the \(0\!\! -\!\!2\) edge joins the end vertices and any positive \(a_1\) or \(a_3\) joins the middle vertex. When \(a_2=0\), two positive adjacent cross-edge types connect all active vertices; a single positive cross-edge type is obstructed only by a loop at the remaining isolated vertex; with no cross edges, a single nonzero loop vertex is feasible. Thus the list is exhaustive.

There are \(\binom m2\) histograms in each of the first two classes, and \(m-1\) in the last, among the \(\binom{m+4}4\) weak compositions of \(m\) into five bins. Hence
\[
L_m=\binom{m+4}4-2\binom m2-(m-1)=\binom{m+4}4-m^2+1.
\]

**3. Complete cyclic feasibility classification.** Since loops contribute even degree, degree parity requires
\[
a_1\equiv a_3\equiv k\pmod2.
\]
We now enumerate feasible nonnegative histograms by disjoint cases.

(i) If \(a_1,a_3>0\), both must have the same parity. For even-even, any \(a_2\ge0\) works by \(k=0\), and for odd-odd, \(a_2\ge1\) is necessary and sufficient by \(k=1\). Both cross-edge types already ensure connectivity. The sum of their length-generating contributions is
\[
\frac{z^4+z^3}{(1-z^2)^2(1-z)^3}=\frac{z^3}{(1-z)^4(1-z^2)}.
\]
Here the two loops at the outer vertices vary freely, explaining two factors \((1-z)^{-1}\); the third comes from the unrestricted sum-two bin after its minimum is taken.

(ii) If \(a_1>0\) and \(a_3=0\), then \(a_1\) must be positive even. If \(a_4=0\), take \(k=0\) and any \(a_2\ge0\). If \(a_4>0\), the loop at vertex \(2\) can only join the main component through a positive \(0\!\! -\!\!2\) edge; since \(k\) must be even, this is possible if and only if \(a_2\ge2\). The contribution is
\[
\frac{z^2}{1-z^2}\left(\frac1{(1-z)^2}+\frac{z^3}{(1-z)^3}\right).
\]
The symmetric case \(a_3>0,a_1=0\) has the same contribution with \(a_0\) and \(a_4\) interchanged.

(iii) If \(a_1=a_3=0\), the admissible alternatives are: positive even \(a_2\) with any outer loops (choose \(k=a_2\)); positive odd \(a_2\) with no outer loops (necessarily \(k=0\), all edges are vertex-one loops); or \(a_2=0\) with exactly one positive outer-loop bin. These contribute
\[
\frac{z^2}{(1-z^2)(1-z)^2}+\frac z{1-z^2}+\frac{2z}{1-z}.
\]
The nonempty assumption rules out the all-zero histogram. These alternatives are exhaustive by parity and connectivity, and each has a constructive Euler circuit.

**4. Generating function and coefficients.** Add case (i), twice case (ii), and case (iii). Direct common-denominator simplification gives
\[
\sum_{m\ge1}C_mz^m=\frac{z(3-7z+5z^2+3z^3-3z^4)}{(1-z)^5(1+z)}.
\]
Expanding the only possible poles, at \(1\) and \(-1\), yields the closed coefficient formula in the finding. Its degree-four leading term is \(m^4/48\), whereas the linear formula has leading term \(m^4/24\). This proves the sharp twofold asymptotic difference; the extra cyclic obstruction is fundamentally the requirement that the two cross-edge multiplicities \(a_1,a_3\) have equal parity.

**5. Zero-error capacity.** In either deterministic readout, different source words are confusable if and only if they produce the same five-bin histogram. At most one codeword may lie in any inverse fiber, while selecting one arbitrary representative from each nonempty fiber achieves this bound. This establishes the claimed exact maximum code sizes for every \(m\ge1\).

## Verification

Run `python3 verify.py` using Python 3's standard library. The executable independently enumerates all \(3^m\) cyclic inputs and \(3^{m+1}\) linear inputs for each \(1\le m\le9\), checks both exact formulae against the actual output sets, and compares every five-bin vector against both feasibility tests. It separately enumerates all 3,478,760 five-bin vectors of total size \(1\) through \(50\) and checks the all-length formulas at those lengths. A third routine constructs explicit Euler-trail and Euler-circuit witnesses for every feasible profile through length \(13\) and for 1,000 sampled profiles at lengths through \(500\), checking observed histograms from the constructed words. The executed program returned `SPECTRUM_VERIFY_OK word_instances=118092 histogram_vectors=3478760 Euler_witnesses=12286 lengths=1..50`.

The initial cyclic values at \(m=1,\dots,12\) are \(3,5,10,18,34,59,99,156,237,345,488,670\); the initial linear values are \(5,12,27,55,102,175,282,432,635,902,1245,1677\). A separate exact symbolic simplification of the case generating functions also recovers the stated rational function and low-order coefficients. These finite computations are corroboration, **not** a substitute for the exhaustive parameter-case proof valid for all lengths.

## Relationship to prior work

Ye and Elishco [1] motivate reconstruction from substring compositions and treat linear string reconstruction using richer, generally longer composition observations. Their length-limited problems do not state the five-bin adjacent-integer-sum image counts here, nor do they compare linear and cyclic closure at the same number of reads. Yehezkeally, Marcovich and Yaakobi [2] treat multi-strand reconstruction from unaggregated substring content. Kiah, Puleo and Milenkovic [3] develop constrained DNA sequence profiles and Eulerian-flow counting for **oriented** factor frequencies. Sporring and Darkner [4] study **indexed** local histograms. These models differ from the position-agnostic, additive coarsening of two-letter windows in this theorem.

Exact earlier ternary profile results [5–8] keep six unordered pair categories, nine oriented pair categories (including a separate full linear enumerator), or impose a no-triple repetition constraint before counting. The present receiver combines the distinct unordered pairs \(\{0,2\}\) and \(\{1,1\}\) into the same sum-two output. The image of the resulting non-injective projection must be counted without multiplicity, and neither earlier enumerator directly supplies its cardinality. We use the classical Euler-trail criterion as a tool and do not claim to originate it, nor to originate general string-profile coding. The contribution is the exact **projected** five-bin feasibility and two-channel all-length enumeration with the closure gap.

## Limitations

This is a noiseless, complete-coverage, aggregate two-window readout with labeled values \(0,1,2\). Its integer sums are mathematical weights and should not automatically be interpreted as experimentally distinct molecular masses. Neither error correction with corrupted read bins nor the number of representatives in each fiber is calculated. No larger alphabets or longer read windows are covered. As for any literature search, a previously unindexed equivalent additive-histogram result remains a historical-priority risk; an independent mathematical audit has not been performed.

## References

1. Z. Ye and O. Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, arXiv:2208.14963, first public 2022-08-31. https://arxiv.org/abs/2208.14963
2. Y. Yehezkeally, S. Marcovich and E. Yaakobi, *Multi-strand Reconstruction from Substrings*, arXiv:2108.11725, first public 2021-08-26. https://arxiv.org/abs/2108.11725
3. H. M. Kiah, G. J. Puleo and O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1502.00517, first public 2015-02-02. https://arxiv.org/abs/1502.00517
4. J. Sporring and S. Darkner, *Reconstructing Binary Signals from Local Histograms*, Entropy 24 (2022), 433. https://doi.org/10.3390/e24030433
5. *Exact capacities of ternary cyclic unordered-pair profiles at prescribed composition*, published mathematical result identifier `3e67d435e70c` (2026).
6. *Exact ternary cyclic adjacent-pair profiles and the disconnected correction*, published mathematical result identifier `fec58989960d` (2026).
7. *Exact cyclic pair-composition capacity for ternary words with runs of length at most two*, published mathematical result identifier `4aee40122a4b` (2026).
8. *Exact ternary adjacent-pair spectrum enumerator for linear words*, published mathematical result identifier `87bc1f36ef2d` (2026).
