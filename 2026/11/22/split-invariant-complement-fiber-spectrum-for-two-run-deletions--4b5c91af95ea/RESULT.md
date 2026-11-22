# Split-invariant complement-fiber spectrum for two-run deletions from alternating words

## Finding
Let \(n\ge1\), \(a,b\ge1\), and \(k=a+b\ge3\). From the binary word \(W_n=(01)^n\), delete any order-preserving occurrence of \(U_{a,b}=0^a1^b\). Let \(C(W_n,U_{a,b})\) be the **set of distinct residual words**. For each residual \(v\), let \(e_{a,b}(v)\) be the number of embeddings of \(U_{a,b}\) in \(W_n\) whose deletion leaves \(v\). Use \(\binom rs=0\) when \(s<0\) or \(r<s\).

**Complete multiplicity law.** For every \(t\ge1\), the number of residual words with exactly \(t\) preimages is
\[
N_t(n;a,b)=\mathbf1_{\{t=1\}}\binom nk+
\begin{cases}
\displaystyle\binom{n-t-1}{k-3},&1\le t\le n-k+2,\\[3pt]
0,&\text{otherwise}.
\end{cases}
\]
Consequently, for every \(n\ge k-1\),
\[
\boxed{\lvert C(W_n,U_{a,b})\rvert=\binom nk+\binom{n-1}{k-2}},\qquad
\boxed{\sum_v e_{a,b}(v)=\binom{n+1}k}.
\]
When \(n<k-1\), there is no embedding and the complement set is empty. In particular **the complete fiber-size histogram, not just the output count, is independent of the run split** \((a,b)\) at fixed \(k\). The number of non-singleton fibers is \(\binom{n-1}{k-2}-\binom{n-2}{k-3}\) whenever \(n\ge k-1\), and the largest fiber has size \(n-k+2\). This maximum is attained exactly once if \(n\ge k-1\).

## Assumptions and scope
Words are finite, linear, and indexed from the left. An embedding of a length-\(k\) pattern is a strictly increasing sequence of \(k\) host positions carrying that pattern. A residual is formed by deleting precisely those chosen positions and retaining the other positions in order. Different embeddings may produce the same residual. There is no restriction that deleted positions be contiguous. We require \(a,b\ge1\) and \(k\ge3\); the two-letter case is treated in earlier work. All formulas are exact for all stated integer parameters, not asymptotic statements. For \(n=k-1\), the unique residual has multiplicity one.

## Proof
**1. Encode original blocks.** Regard \(W_n\) as \(n\) ordered copies of \(01\). Label the contribution of an original block to a residual by one of four tokens: \(F=01\) if both characters are retained; \(A=1\) if its zero is deleted; \(B=0\) if its one is deleted; and \(E=\varepsilon\) if both are deleted. Because every deleted zero precedes every deleted one, all \(A\) tokens precede all \(B\) tokens. There is at most one \(E\) token: it would consume the last deleted zero and first deleted one, since neither symbol occurs twice in an original block. If it occurs, all \(A\) tokens precede \(E\) and all \(B\) tokens follow \(E\). Conversely, every token sequence with these properties and the prescribed numbers of deletions is realized by one embedding, because each token uniquely specifies which original block positions are removed.

**2. The output determines the nonempty tokens uniquely.** For any ordered token sequence consisting of \(F,A,B\) with all \(A\)'s before all \(B\)'s, every occurrence of the adjacent factor \(01\) in its concatenated binary output is *exactly* one \(F\) token. Indeed, the boundary of two nonempty tokens cannot create a new \(01\): an \(A\) is \(1\), a \(B\) is \(0\), and no \(B\) precedes an \(A\). These \(01\) occurrences are nonoverlapping. Pairing each such occurrence and reading the remaining lone characters as \(A=1\) or \(B=0\) therefore recovers the unique nonempty token sequence. Inserting or removing an empty token does not alter the output.

**3. Embeddings without \(E\).** If no whole block is deleted, the tokens consist of exactly \(a\) copies of \(A\), \(b\) of \(B\), and \(n-k\) of \(F\), with all \(A\)'s before all \(B\)'s. Choose the \(k\) non-\(F\) block positions among \(n\); their first \(a\) labels are forced to be \(A\), and their last \(b\) are forced to be \(B\). Thus there are \(\binom nk\) embeddings. By step 2 they give pairwise distinct residuals, each with one embedding. Their outputs contain exactly \(n-k\) occurrences of \(01\).

**4. Embeddings with \(E\).** Delete the unique empty block from the token sequence temporarily. What remains is a sequence of \(n-1\) nonempty tokens, with \(a-1\) copies of \(A\), \(b-1\) of \(B\), and \(n-k+1\) of \(F\), with all \(A\)'s before all \(B\)'s. There are exactly \(\binom{n-1}{k-2}\) such nonempty token sequences. Each determines a unique output by step 2, containing \(n-k+1\) occurrences of \(01\); hence none coincides with a step-3 output.

An \(E\) can be reinserted only in the *central gap* after the last \(A\) and before the first \(B\), interpreting that gap as the initial gap if \(a=1\) and the final gap if \(b=1\). If the gap contains \(s\ge0\) copies of \(F\), there are precisely \(s+1\) different insertion places, giving \(s+1\) embeddings with the same residual. All these insertions have deleted pattern \(0^a1^b\), and there are no other embeddings giving that output by step 2.

**5. Count the central-gap sizes.** Place the \(k-2\) labeled non-\(F\) tokens in their fixed order. There are \(k-1\) gaps around and between them, filled by the \(n-k+1\) copies of \(F\). Such placements correspond bijectively to weak compositions of \(n-k+1\) into \(k-1\) nonnegative parts. The designated central gap is one of these parts, regardless of the values of \(a,b\). If its size is \(s=t-1\), the other \(k-2\) parts sum to \(n-k+2-t\). The number of choices is
\[
\binom{(n-k+2-t)+(k-2)-1}{(k-2)-1}
=\binom{n-t-1}{k-3},
\]
for \(1\le t\le n-k+2\). The remaining singleton fibers from step 3 give the displayed multiplicity formula. Summing over \(t\) via the hockey-stick identity gives \(\binom{n-1}{k-2}\) outputs in step 4 and the asserted total. Counting token embeddings yields
\[
\binom nk+\binom n{k-1}=\binom{n+1}k.
\]
Finally, the central gap can contain all \(n-k+1\) full blocks only when all other gaps are empty. That choice is unique and yields the unique maximal fiber, of size \(n-k+2\). For \(n<k-1\), neither token type is possible, completing the proof.

## Verification
The standalone program `verify_exhaustive.py` independently enumerates every position-subset embedding of the two-run pattern in each alternating host for \(1\le n\le9\), and compares the exact observed multiplicity histograms, embedding totals, and output counts with the theorem: 447 parameter triples and 7,181 embeddings passed. The second standalone program `verify_token_model.py` implements the predicted nonempty-token normal form and its central-gap multiplicities, independently comparing the *entire word-to-multiplicity map* with direct positional deletion for 286 parameter triples through host size \(11\). Both test programs use only the Python standard library and can be run from the directory containing them. These finite tests are independent checks, not a substitute for the unrestricted proof in steps 1–5.

For example, with \(n=6\) and \(k=4\), each of the patterns \(0111\), \(0011\), and \(0001\) has exactly \(25\) distinct residuals. The fiber histogram is \(N_1=19\), \(N_2=3\), \(N_3=2\), \(N_4=1\), totaling \(35\) embeddings; all other fiber counts vanish.

## Relationship to prior work
Adamson, Fleischmann and Huch introduced complement scattered-factor sets and algorithms in their March 2026 preprint. Its Sections 3–4 and conclusion study general computation, singleton conditions, and shuffle connections; Section 5 notes closed counts for specific cases as an open direction. None of the inspected statements yields the present split-invariant full fiber-size law.

An existing binomial-tail theorem for deleting an *alternating* pattern from an alternating host determines a different residual language: here the prescribed deleted pattern has exactly two runs, and the token normal form gives a length-only fiber law for every positive split. A separate published run-pair identity covers deletion of a two-letter pattern from an arbitrary host; the present result deliberately assumes \(k\ge3\), where that identity does not apply. An existing fixed-composition enumerator for arbitrary deletion subsequences of an alternating host counts the union of outputs for all deleted patterns of a given symbol composition, without tracking individual two-run patterns or their embedding fibers. The 2004 distinct-subsequence enumeration of Flaxman, Harrow and Sorkin studies residuals across all deletion patterns and does not imply this prescribed-pattern fiber spectrum.

## Limitations
The theorem is limited to the binary alternating source and deleted patterns with one zero-run followed by one one-run. It does not classify arbitrary deletion patterns or general source words. The previously studied two-letter case is excluded from the new claim. No computational complexity improvement for arbitrary source-pattern pairs is claimed. Although the inspected indexed results do not imply the formula, a differently stated or unindexed identity in earlier shuffle or deletion literature remains a priority risk. No independent external mathematical validation is asserted.

## References
1. D. Adamson, P. Fleischmann and A. Huch, *(Sets of) Complement Scattered Factors*, arXiv:2603.20790v1, first public 21 March 2026. https://arxiv.org/html/2603.20790v1
2. *Binomial-tail law for complements of alternating words*, publicly indexed research note, 2026; concerns deleting an alternating pattern from an alternating host.
3. *A run-pair formula for two-letter complement scattered factors*, publicly indexed research note, 2026; concerns deletion patterns of length two.
4. *Fixed-composition deletion spectra and parity bias for alternating binary words*, publicly indexed research note, 2026; concerns the union over all deleted patterns with prescribed composition.
5. A. Flaxman, A. W. Harrow, and G. B. Sorkin, *Strings with Maximally Many Distinct Subsequences and Substrings*, Electron. J. Combin. 11 (2004), R8. https://doi.org/10.37236/1761
