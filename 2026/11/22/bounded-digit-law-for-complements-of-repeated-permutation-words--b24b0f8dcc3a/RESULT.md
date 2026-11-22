# Bounded-digit law for complements of repeated permutation words

## Finding

Let \(q\ge 3\), let \(P=a_0a_1\cdots a_{q-1}\) be a word containing \(q\) distinct letters, and let \(m,k\ge0\) be integers. For words \(W,U\), define \(C(W,U)\) to be the set of distinct words remaining when the positions of any scattered-subsequence embedding of \(U\) in \(W\) are removed. Write \(R_s=a_s a_{s+1}\cdots a_{q-1}a_0\cdots a_{s-1}\) for the rotation of \(P\) starting at phase \(s\), where \(0\le s<q\).

**Complete multi-period complement theorem.** For each phase sequence \(\mathbf s=(s_1,\ldots,s_m)\in\{0,\ldots,q-1\}^m\), define its minimal deletion expenditure by
\[
E_q(\mathbf s)=s_1+\sum_{j=1}^{m-1}(s_{j+1}-s_j\bmod q),
\]
where every residue is chosen in \(\{0,\ldots,q-1\}\), and set \(E_q(())=0\). Then
\[
\boxed{C(P^{m+k},P^k)=\{R_{s_1}\cdots R_{s_m}:E_q(\mathbf s)\le qk\}.}
\]
Writing \([z^{\le t}]f(z)=\sum_{i=0}^{t}[z^i]f(z)\), its cardinality is
\[
\boxed{|C(P^{m+k},P^k)|=[z^{\le qk}](1+z+\cdots+z^{q-1})^m.}
\]
The smallest deletion-period budget realizing **every** one of the \(q^m\) concatenations of \(m\) cyclic rotations is exactly
\[
\boxed{k_{\mathrm{sat}}(q,m)=\left\lceil\frac{(q-1)m}{q}\right\rceil.}
\]
For \(q\ge3\), the two-variable range \(k\ge2\), \(m\ge2\) is the new part of the theorem; the binary case and the single-deleted-period slice have prior results explicitly credited below.

The count also has a sharp probabilistic interpretation: it equals \(q^m\) times the probability that the sum of \(m\) independent uniform digits from \(\{0,\ldots,q-1\}\) is at most \(qk\). For fixed \(q\) and \(m\to\infty\), if \((qk-(q-1)m/2)/\sqrt{m(q^2-1)/12}\to x\in\mathbb R\), the fraction of available rotation words tends to \(\Phi(x)\), the standard normal cumulative distribution function.

## Assumptions and scope

Words are linear; embeddings are strictly increasing source-position selections. Different embeddings producing the same remainder contribute one element to \(C(W,U)\). All symbols \(a_i\) are pairwise distinct, the source has exactly \(m+k\) full periods and the deleted pattern exactly \(k\) full periods in the same orientation. Powers with exponent zero are empty, including \(m=k=0\). Residues \((b-a\bmod q)\) always mean the least nonnegative residue, never a negative remainder. All alphabet relabelings of \(P\) have the same count. No assertion is made for periods with repeated symbols or for truncated hosts.

## Proof

**1. Forced rotation blocks in every valid deletion.** Read the source \(W=P^{m+k}\) from left to right and label each position kept or deleted, with the deleted positions reading \(U=P^k\). Use a reference pointer into the infinite periodic word \(P^\omega\) to record the number of deleted symbols (even after the finite deleted pattern is exhausted). Initially this reference and the source both have phase \(a_0\). Whenever a position is deleted, both pointers advance and retain the same phase; whenever a position is kept, only the source pointer advances. A deletion is forbidden once all \(qk\) target symbols have been consumed.

Suppose at least one retained position remains and its first letter is \(a_s\). Let \(h\) be the number of positions deleted before this first retained position. All earlier positions were deleted, hence their letters form a prefix of \(P^k\), so \(h\equiv s\pmod q\). If deletions remain, their next required symbol is \(a_s\); otherwise deletion is impossible. The next \(q-1\) source letters are \(a_{s+1},\ldots,a_{q-1},a_0,\ldots,a_{s-1}\); none can be deleted, because the deleted track still expects \(a_s\), which is absent from this segment. Thus the first \(q\) retained letters are exactly \(R_s\). Existence of the full block follows because the total number of retained positions is a multiple of \(q\): if fewer than \(q\) source positions remained, the nonempty retained output could not have length divisible by \(q\).

After this complete retained block the source pointer again expects \(a_s\), as does the deleted-pattern pointer. Repeating the argument inductively, all retained letters form \(m\) full rotation blocks. Between successive blocks, deleted positions constitute a possibly empty contiguous source segment that exactly matches the next segment of the deleted pattern. Let \(d_0\) count deletions before the first retained block, \(d_j\) those between block \(j\) and block \(j+1\) for \(1\le j<m\), and \(d_m\) those after the last block. The nonnegative integers \(d_0,\ldots,d_m\) sum to \(qk\), and
\[
 s_1\equiv d_0\pmod q,\qquad s_{j+1}\equiv s_j+d_j\pmod q.
\]
Therefore \(d_0\ge s_1\), each \(d_j\ge(s_{j+1}-s_j\bmod q)\), and \(E_q(\mathbf s)\le qk\).

**2. Sufficiency using a constructive allocation.** Conversely take any phase sequence with \(E_q(\mathbf s)\le qk\). Delete \(d_0=s_1\) source letters, retain the next \(q\); for \(1\le j<m\), delete \(d_j=(s_{j+1}-s_j\bmod q)\) source letters and retain the next \(q\). Finally delete the remaining \(d_m=qk-E_q(\mathbf s)\) source letters. Every retained segment begins at the designated phase and equals \(R_{s_j}\). During each deleted segment, the source and deleted-pattern pointers have identical cyclic phases: this is true initially, and retaining any multiple of \(q\) source symbols does not change their phase agreement. Consequently **all** deleted letters, concatenated in order, form precisely the first \(qk\) symbols of the infinite periodic word \(P^\omega\), namely \(P^k\). The total source length consumed is \(qm+qk\), so this is a valid embedding in \(P^{m+k}\). This proves the language equality for \(m\ge1\). For \(m=0\), deleting the entire source gives only the empty remainder, matching the formula.

**3. Count without overcounting.** Rotations \(R_0,\ldots,R_{q-1}\) have different first letters; hence concatenations of \(m\) rotations uniquely determine their phase sequence. The map
\[
(s_1,\ldots,s_m)\longleftrightarrow
(t_1,\ldots,t_m)=(s_1,(s_2-s_1\bmod q),\ldots,(s_m-s_{m-1}\bmod q))
\]
is a bijection between phase sequences and digit vectors in \(\{0,\ldots,q-1\}^m\), with \(E_q(\mathbf s)=\sum_i t_i\). Counting digit vectors of bounded sum proves the coefficient formula, including \(m=0\).

**4. Saturation and asymptotic boundary.** The maximum digit sum is \((q-1)m\), attained by the unique vector with every entry equal to \(q-1\). Thus all \(q^m\) rotations occur if and only if \(qk\ge(q-1)m\). The stated ceiling is the least feasible integer \(k\). The random-digit identity follows by dividing each of the \(q^m\) digit vectors by \(q^m\). Each digit has mean \((q-1)/2\) and variance \((q^2-1)/12\). For fixed \(q\), the classical iid central limit theorem gives the displayed scaled limit. \(\square\)

## Verification

Run `python3 verify_masks.py` and `python3 verify_dp.py` in the directory containing this document. The first uses direct enumeration of positional deletion masks and compares **complete literal residual sets** to the rotation-language construction in 56 parameter cases. The second uses an independently written delete-or-keep recursion with memoization, comparing distinct-output counts to an independently computed polynomial convolution over 112 cases. Both scripts reproduce the attached `.txt` logs. Examples: for \((q,m,k)=(3,4,2)\) the count is \(76\); for \((4,4,2)\), \(221\); and for \((5,3,2)\), \(121\). The scripts are finite corroboration; the unrestricted statement is proved above.

## Relationship to prior work

Adamson, Fleischmann and Huch (2026), *\((\mathrm{Sets\ of})\) Complement Scattered Factors*, introduce the complement operator, a dynamic programming enumeration algorithm, and general structural/singleton results. The inspected Sections 3–5 do not give the displayed all-alphabet, all-period phase language or digit-sum count. Their general algorithm handles individual finite inputs but does not state the bounded-digit law.

The published *Binomial-tail law for complements of alternating words* and *An exact run formula for complements of alternating binary subsequences* cover the complete \(q=2\) specialization for all \(m,k\). The prior *Phase rigidity and exact complementary-subsequence capacity of permutation powers* covers \(q\ge3\) **only** when \(k=1\), yielding \(\binom{m+q}{q}-m\). The coefficient formula above agrees with it on that slice but supplies the previously unaddressed joint family \(q\ge3\), \(k\ge2\). The published *Exact embedding-multiplicity spectrum of cyclic permutation powers* counts embeddings of arbitrary *survivor* subsequences rather than complements of a prescribed deleted word; its formulas do not determine the required shuffle-compatible residual language without additional reasoning. Ordinary bounded-composition identities are used for enumeration, not separately claimed as new.

## Limitations

The phase-block argument critically requires a period containing each symbol once. It does not apply directly to arbitrary repeated-symbol periods, reverse-phase deletions, or cyclic quotients. The Gaussian corollary is fixed-alphabet asymptotics and does not assert a uniform limit for growing \(q\). Earlier equivalent shuffle-quotient results not indexed by the checked sources remain possible. No independent external mathematical audit has been performed.

## References

1. D. Adamson, P. Fleischmann and A. Huch, *(Sets of) Complement Scattered Factors*, arXiv:2603.20790v1, first posted 2026-03-21, https://arxiv.org/html/2603.20790v1.
2. *Binomial-tail law for complements of alternating words*, published published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-binomial-tail-law-for-complements-of-alternating-words--d7ef6cdd9c92.
3. *An exact run formula for complements of alternating binary subsequences*, published published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-an-exact-run-formula-for-complements-of-alternating-binary-subse--53b12846b520.
4. *Exact embedding-multiplicity spectrum of cyclic permutation powers*, published published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-embedding-multiplicity-spectrum-of-cyclic-permutation-powe--bcaf0c227997.
5. *Phase rigidity and exact complementary-subsequence capacity of permutation powers*, existing mathematical manuscript, comparison from its complete theorem and proof.
