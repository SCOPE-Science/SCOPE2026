# Sharp alphabet threshold and repeat onset for full circular deletion shadows

## Finding

Let \(t\ge2\), \(n\ge t+1\), and let \(w\) be an indexed circular word of length \(n\) over a labeled alphabet of size \(q\). For each \(t\)-element subset of the indexed positions, delete exactly those positions, retain the cyclic order of the surviving symbols, and identify outputs only under rotation, **not** reversal or alphabet permutation. Write \(\mathcal D_t^\circ(w)\) for the distinct output necklaces.

**Theorem (full-shadow threshold and repeat onset).**

1. For every \(t+1\le n\le2t+1\), equality
   \[|\mathcal D_t^\circ(w)|=\binom nt\]
   holds **if and only if** all \(n\) symbols of \(w\) are pairwise distinct. In this range the minimum alphabet size for a full shadow is exactly \(n\).
2. For **every** \(n\ge t+1\) and every \(q\ge2t+1\), a full-shadow source exists. In particular,
   \[\max_{w\in\Sigma_q^n}|\mathcal D_t^\circ(w)|=\binom nt.\]
   A uniform explicit construction uses \(t\) distinct single-occurrence markers followed by a periodic data block of period \(t+1\) using further distinct symbols.
3. Consequently the least fixed alphabet size that guarantees this maximum at **every** admissible blocklength is exactly \(2t+1\). The first length at which a word with a repeated symbol can attain the full shadow is exactly \(2t+2\): the construction at that length uses only \(2t+1\) symbols.

These assertions concern *all indexed deletion masks* surviving the quotient by cyclic rotation. They do not claim that the minimum alphabet for any one length greater than \(2t+1\) is \(2t+1\).

## Assumptions and scope

The starting word has indexed positions \(0,1,\ldots,n-1\), even though its outputs are regarded as cyclic rotation classes. Each deletion mask is a subset of exactly \(t\) positions; the number of candidate masks is \(\binom nt\). The remaining length is \(n-t\ge1\). Equality of outputs means equality after cyclic rotation only. Distinct source symbols are labeled and distinguishable; no probability distribution, substitutions, complementary identification, or reversal is assumed. The theorem holds for all integers \(t\ge2\), all integers \(n\ge t+1\), and arbitrary alphabets satisfying the relevant sizes. The one-deletion case obeys the same elementary construction but is not included in the novelty claim.

## Proof

**Upper bound.** Each deletion mask yields precisely one necklace, so \(|\mathcal D_t^\circ(w)|\le\binom nt\).

**A short-arc collision lemma.** Suppose positions \(i\) and \(j\) have equal symbols, and one of the directed cyclic arcs from \(i\) to \(j\) has \(d\) edges with \(1\le d\le t\). Let \(B\) be its \(d-1\) interior positions. Choose \(t-d\) other positions from outside the arc, which is possible because there are \(n-d-1\ge t-d\) such positions by \(n\ge t+1\). The two size-\(t\) masks
\[B\cup\{i\}\cup E,\qquad B\cup\{j\}\cup E\]
are distinct and yield the same output necklace. Indeed, after all interior positions are deleted, the equal endpoint symbols are interchangeable at the sole remaining arc location in the cyclic survivor sequence; the other surviving symbols occur in exactly the same cyclic order. Hence a full-shadow source cannot have two equal symbols at circular distance at most \(t\).

If \(t+1\le n\le2t+1\), the smaller circular distance between any two distinct positions is at most \(\lfloor n/2\rfloor\le t\). Thus the lemma forces **every** pair of source symbols to differ. Conversely, if all symbols are different, the symbol *set* surviving a mask uniquely specifies that mask, so all \(\binom nt\) necklaces are distinct. This proves assertion 1.

**Long-word construction.** Choose \(2t+1\) distinct symbols
\[b_1,\ldots,b_t,a_0,\ldots,a_t\]
and, for every \(m=n-t\ge1\), let \(u_m\) be the prefix of length \(m\) of the infinite periodic word \(a_0a_1\cdots a_ta_0a_1\cdots\). Set \(w=b_1\cdots b_tu_m\). Every marker occurs exactly once; no marker appears in the data block.

Consider any deletion mask of size \(t\). The surviving set of marker symbols determines exactly which of the \(t\) marker positions were deleted, since markers are unique and disjoint from the data alphabet. If no marker survives, the mask necessarily deletes every marker and no data position, and is unique. Otherwise, the surviving marker sequence forms a nonempty consecutive block in the cyclic output, and a fixed surviving marker provides an unambiguous cyclic root. Thus the cyclic output determines the **linear** data subsequence \(v\) obtained by deleting precisely \(r\) data positions from \(u_m\), where \(0\le r\le t\) is fixed by the surviving marker subset.

We claim the original data deletion mask is determined by \(v\). Let the retained index lists be \(i_1<\cdots<i_{m-r}\) and \(j_1<\cdots<j_{m-r}\). At every position \(k\),
\[k\le i_k,j_k\le k+r,\qquad |i_k-j_k|\le r\le t.\]
If the two index lists differ, they contain a different index at some \(k\), and equality of the corresponding output letters would force two equal letters of \(u_m\) at different positions separated by at most \(t\). Yet equal letters in \(u_m\) are separated by a positive multiple of \(t+1\), a contradiction. Therefore every deletion mask yields a distinct necklace. This proves assertion 2.

For assertion 3, assertion 1 at \(n=2t+1\) forces at least \(2t+1\) alphabet symbols in **any** construction that works for all lengths. Assertion 2 attains this bound at all lengths. At \(n\le2t+1\) no full-shadow source can repeat a symbol, while at \(n=2t+2\) our construction has \(m=t+2\) and repeats \(a_0\) once, attaining full shadow. This proves the sharp onset. \(\square\)

## Verification

The standalone Python 3 standard-library script `verify.py` implements deletion by indexed masks and independently identifies outputs via lexicographically minimal cyclic rotation. It tests the full marker construction for all \(t\in\{1,2,3,4,5\}\) and \(n=t+1,\ldots,t+12\): \(60\) parameter pairs and \(27113\) distinct masks. It exhaustively checks the short-length iff condition for \(t=1,2\) over all alphabets of size up to \(2t+1\), testing \(4461\) source words and \(44358\) mask occurrences. As a separate nonclaimed finite diagnostic, it checks all quaternary words of lengths \(5,6,7\) at \(t=2\), obtaining maximum sphere sizes \(9,15,20\) against mask counts \(10,15,21\), respectively. All tests pass; `verification_output.txt` contains the actual recorded output. These finite tests support, but do not replace, the all-parameter proof.

## Relationship to prior work

Luchinin, Puzynina and Rao [1] investigate when binary cyclic words are recoverable from collections of their scattered cyclic subwords. Their quantified reconstruction threshold concerns distinguishing *different source necklaces*, rather than whether a **single** source has distinct outputs for **every indexed deletion mask**. Their framework motivates studying cyclic subsequences with no designated origin.

Burudgunte, Valiant and Wang [2] analyze a stochastic circular trace channel in which deletion is followed by a random rotation, focusing on sample complexity and sparse-source statistics. It does not state this exact finite-support saturation or the universal minimum alphabet size.

Li, Wang and Fu [3] establish deletion-ball cardinalities and extremal classes for **linear** nonbinary sequences. Their periodic alphabet construction prevents local linear deletion collisions but does not distinguish all output rotations. The marker argument supplies the missing cyclic anchoring.

Published special-source necklace calculations [4] count deletion-mask *orbits* for powers of a permutation, rather than all indexed masks, and record collisions induced by source periodicity. The present construction deliberately removes these orbit identifications, and its necessity argument treats **arbitrary** circular sources at the sharp length. The other nearby results [5] give exact one-deletion degrees in the binary case; they do not imply higher-deletion full shadows on larger alphabets.

## Limitations

The theorem is an existence-and-sharp-alphabet statement, not a classification of every maximizing word at lengths above \(2t+1\). The least alphabet size for a **particular** longer length may be smaller than \(2t+1\). The case of no surviving symbols is excluded. A full shadow does not by itself imply error correction or efficient recovery of the unknown original source from its traces. The originality comparison uses inspected literature and accessible published results; an unindexed equivalent argument remains possible. Independent validation has not been performed.

## References

1. S. Luchinin, S. Puzynina, M. Rao, *Recovery of cyclic words by their subwords*, arXiv:2412.03289, first public 2024-12-04, https://arxiv.org/abs/2412.03289 (especially Sections 1–2).
2. A. Burudgunte, P. Valiant, H. Wang, *New Bounds for Circular Trace Reconstruction*, arXiv:2512.02412, first public 2025-12-02, https://arxiv.org/abs/2512.02412 (especially Definitions 5–6 and Sections 1–2).
3. H. Li, X. Wang, F.-W. Fu, *On the Number of Subsequences in the Nonbinary Deletion Channel*, arXiv:2601.06493, first public 2026-01-10, https://arxiv.org/abs/2601.06493 (especially Sections I, IV–V).
4. *Short-deletion necklaces of permutation powers: exact orbit counts and the first phase-wrap collision*, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-short-deletion-necklaces-of-permutation-powers-exact-orbit-count--16ccfbf22eda (Finding, Proof).
5. *Sharp one-deletion outdegree of binary necklaces*, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-one-deletion-outdegree-of-binary-necklaces--2341722fce11 (Finding, Proof).
