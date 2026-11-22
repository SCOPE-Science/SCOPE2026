# A mixed uniform limit for single-bit perturbations of bilateral run-pair tokens

## Finding

Let \(W_n\) be a uniformly random binary word of length \(n\ge3\), and independently let \(P_n\) be uniform on its interior positions \(\{2,\ldots,n-1\}\). Form \(W'_n\) by complementing the bit at \(P_n\). Consider the reversible bilateral run-peeling decomposition of Konstantinovsky and Yaari, with its initial sentinel token removed. Write \(T_j(w)\) for the content token at depth \(j\), including its stored split position (the terminal token has split zero), and \(h(w)\) for the number of content tokens. Define the *common-depth token rewrite count*

\[
H_n=\sum_{j=1}^{\min(h(W_n),h(W'_n))}\mathbf1\{T_j(W_n)\ne T_j(W'_n)\}.
\]

Then, as \(n\to\infty\),

\[
\boxed{\frac{H_n}{n}\ \xrightarrow{\mathrm d}\ \tfrac12\delta_0+\tfrac12\operatorname{Unif}[0,\tfrac16].}
\]

In particular,

\[
\boxed{\lim_{n\to\infty}\frac{\mathbb E H_n}{n}=\frac1{24}.}
\]

The law has an atom of mass one-half at zero; conditional on the complementary event, it is uniform on the interval \([0,1/6]\). This is a statement about *depth-aligned token rewrites*, not the Levenshtein distance between token sequences.

## Assumptions and scope

The binary input bits are independent and fair, and the edit position is independently uniform over interior positions. A content token pairs the outermost remaining maximal runs, storing their concatenation and the left-run length, except for the last token, which has split zero and contains the central one or two runs. The initial token of two distinct sentinels is deterministic and ignored. The numerical values concern the specified binary source and exactly one bit complementation; no higher-alphabet or arbitrary-source assertion is made. A token present in only one sequence is not counted in \(H_n\).

## Proof

**1. Boundary representation and the two edit regimes.** Write \(B_i=W_n[i]\mathbin{\oplus}W_n[i+1]\) for \(1\le i<n\). The vector of \(n-1\) boundary indicators is independent with fair Bernoulli coordinates, and the number of maximal constant runs is \(R_n=1+\sum_{i=1}^{n-1}B_i\). Complementing the bit at interior position \(p\) toggles exactly \(B_{p-1}\) and \(B_p\). If these two indicators differ, the number and ordered symbol sequence of runs are unchanged and only two adjacent run lengths can change. Consequently, at most two paired content tokens change, and \(H_n\le2\). If the indicators agree, the number of runs changes by exactly two (a run is split into three, or three runs are merged). This second event, denoted \(E_n\), has probability exactly \(1/2\) and is independent of the choice of \(p\).

**2. Pairing shift.** By the run-pairing description, the \(j\)-th nonterminal content token consists of the \(j\)-th maximal run from each end, with its split length. Let \(K_n\) be the index of the original run containing the edited position. On \(E_n\), after at most a fixed number of exceptional depths surrounding the modified run and the middle terminal token, the only possibly different depth-aligned tokens are those from the edited run's distance from the nearest end up to the middle. The unedited side of each such pair is identical, while the other side is an original run compared to an original run two run-indices away. Their number is

\[
A_n=\frac{R_n}{2}-\min(K_n,R_n+1-K_n)+O(1),
\]

with the right-hand side truncated at zero if necessary. The additive error is bounded by an absolute constant. This statement follows by writing the two run lists side by side: inserting or removing two consecutive run boundaries shifts the run index by two on the affected side, but leaves the order from the opposite end fixed. Since binary run letters alternate, runs at index distance two have the same letter, so the corresponding nonterminal tokens differ if and only if the two compared run lengths differ.

**3. Renewal law for mismatches.** Couple the length-\(n\) word to an infinite fair-bit sequence. Its completed successive run lengths \(L_1,L_2,\ldots\) are independent with \(\mathbb P(L_i=\ell)=2^{-\ell}\), \(\ell\ge1\); only the final incomplete run is truncated. Therefore

\[
\mathbb P(L_i\ne L_{i+2})=1-\sum_{\ell\ge1}4^{-\ell}=\frac23.
\]

The indicators \(\mathbf1\{L_i\ne L_{i+2}\}\) form a stationary two-dependent sequence. By the strong law, sums over any (even randomly selected) index interval whose endpoints are \(O(n)\) differ from \(2/3\) times its length by \(o(n)\), uniformly over such intervals. The finitely many modified or terminal runs contribute \(O(1)\). Hence, on \(E_n\),

\[
H_n=\frac23 A_n+o_{\mathbb P}(n).
\]

The same conclusion applies to a shifted index interval counted from the other end.

**4. Location limit and distribution.** We have \(R_n/n\to1/2\) in probability. Also \(P_n/n\Rightarrow U\), where \(U\) is uniform on \([0,1]\), and the boundary-sum law gives \(K_n/n-P_n/(2n)\to0\) in probability. Consequently,

\[
\frac{A_n}{n}-\frac12\left|\frac{P_n}{n}-\frac12\right|\ \xrightarrow{\mathbb P}\ 0.
\]

The event \(E_n\) is independent of \(P_n\) and has probability \(1/2\); conditioning on its two adjacent boundary bits does not alter the limiting boundary density or renewal comparison frequency. Combining the four observations yields the limit \(Z=J|U-1/2|/3\), where \(J\) is an independent fair Bernoulli indicator. Since \(|U-1/2|\) is uniform on \([0,1/2]\), \(Z\) has the asserted mixture distribution.

Finally, \(0\le H_n/n\le (n+1)/(2n)\) for every word, so bounded convergence in distribution implies convergence of first moments. The mean of the nonzero uniform component is \(1/12\), and the mixture weight is \(1/2\), giving \(1/24\).

## Verification

Run `python3 verify_flashback_sensitivity.py` in the directory containing the two supplied files. The script independently constructs tokens by actual outside-in peeling and by paired maximal runs. It verifies agreement on every binary word through length 14 (32,766 words), evaluates 360,456 directed interior bit flips and verifies the at-most-two-token property when the run count is unchanged. Exact finite means are printed. A fixed-seed simulation with 3,000 trials at each of lengths 256, 1,024 and 4,096 checks the scale and conditional median; the simulation is diagnostic and does **not** prove the limit law. Its captured output is `verification_output.txt`.

## Relationship to prior work

Konstantinovsky and Yaari introduced the bilateral run-peeling transform and proved the exact run-pairing representation, together with one-token locality for *run-length changes that preserve the run-symbol skeleton*. Their character-edit discussion also notes that changing the skeleton can realign token contents at several depths, without giving the random single-bit rewrite law. The present theorem quantifies this distinction by a nondegenerate linear-scale limit. Generic algorithms for maximal runs or edit distances do not supply this particular depth-aligned token statistic. The proof relies on the published run-pairing representation, while the stochastic limit and its \(1/24\) constant are the new assertions.

## Limitations

The comparison is fixed-depth (no optimal token alignment), ignores any unmatched trailing token, and uses a uniform binary source. A token-edit-distance or a worst-case rewrite bound is not established. The argument is an ordinary analytic proof supported by finite checks, not independent validation. An unindexed equivalent stochastic formula cannot be excluded.

## References

1. T. Konstantinovsky and G. Yaari, *Flashback: A Reversible Bilateral Run-Peeling Decomposition of Strings*, first public arXiv submission 2026-04-29, https://arxiv.org/abs/2604.26190 (especially Section 6.1 and Section 6.4).
2. The original run-pairing and run-length locality arguments in Reference 1 are used only for deterministic token structure; the probabilistic calculation above is separate.
