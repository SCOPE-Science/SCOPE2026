# An invariant one-deletion trace spectrum for every de Bruijn cycle

## Finding
Fix an integer alphabet size \(q\ge2\), an integer order \(n\ge2\), and any oriented \(q\)-ary de Bruijn circle \(W\) of order \(n\). Thus \(W\) has \(q^n\) indexed positions, and every length-\(n\) word over its labeled alphabet occurs exactly once as a cyclic factor. Delete one position and regard the remaining \(q^n-1\) letters as a necklace, identifying rotation but **not** reflection or relabeling. Let \(\mathcal D_1(W)\) denote the set of distinct resulting necklaces.

Under deletion of a uniformly selected position, write \(R_\ell\) for the number of distinct output necklaces having probability exactly \(\ell/q^n\). Then the **complete probability spectrum** is independent of the chosen de Bruijn circle:

\[
R_\ell=\begin{cases}
(q-1)^2q^{n-\ell-1},&1\le\ell\le n-2,\\
q(q-2),&\ell=n-1,\\
q,&\ell=n,\\
0,&\text{otherwise}.
\end{cases}
\]

The first range is empty for \(n=2\), and a displayed zero count denotes no outputs at that probability. In particular,
\[
\boxed{|\mathcal D_1(W)|=(q-1)q^{n-1}.}
\]
Every cyclic constant-symbol run yields one different output necklace. Consequently, quotienting deletion outputs by rotation creates **no additional collisions** beyond different deletion sites in the same run.

## Assumptions and scope
The alphabet is a fixed set of \(q\) distinguishable symbols, not a group of interchangeable colors. The source is a de Bruijn circle, not an arbitrary circular word or a linearized representation with fixed endpoints. The receiver is told the remaining cyclic string up to rotation only. A *cyclic run* of symbol \(a\) is a maximal contiguous cyclic interval consisting of \(a\). A deletion anywhere in the same run produces the same necklace, whereas positions from different runs are not automatically distinguishable for arbitrary necklaces. Probabilities here arise solely from uniformly selecting one of the original \(q^n\) positions, with no insertion or substitution noise.

## Proof
**1. A unique anchor for each deleted symbol.** Fix an alphabet symbol \(a\). In a de Bruijn circle of order \(n\), the factor \(a^n\) appears exactly once, so its maximal \(a\)-run has length **exactly \(n\)**. An \(a\)-run longer than \(n\) would give two cyclic occurrences of \(a^n\), and no other \(a\)-run can have length \(n\).

Deleting an \(a\) inside this distinguished run destroys the only occurrence of \(a^n\) and cannot create another: removing \(a\) cannot join two separated runs of \(a\). Deleting \(a\) in any other run leaves the **unique** occurrence of \(a^n\) intact. Therefore the first type of output cannot be rotation-equivalent to any output of the second type.

Now consider two deletions of \(a\) outside the distinguished run. Their output circles each have the same unique \(a^n\) factor. Rotate each output so that this factor begins at its uniquely determined position. Do the same to the input before either deletion. The two resulting linearly rooted deletion outputs agree only if the two deleted indices lie in the same constant run of the rooted input. To see this, for indices \(i<j\) in an ordinary linear word, equality of the two single-deletion results is equivalent, by comparing positions \(i\) through \(j-1\), to equality of all symbols at positions \(i,i+1,\ldots,j\). The distinguished \(a^n\) run is not cut by the deletion and so it supplies the same root in both outputs. Hence distinct \(a\)-runs always yield distinct cyclic deletion outputs.

Finally, deleting two different alphabet symbols gives different Parikh (letter-count) vectors, so their output necklaces cannot coincide. Thus distinct source runs yield distinct necklaces, for **every** source \(W\) satisfying the de Bruijn hypothesis.

**2. Exact distribution of run lengths.** Fix \(a\), and let \(r_{a,\ell}\) count its cyclic runs of length \(\ell\). For \(1\le\ell\le n-2\), every \(a\)-run of length \(\ell\) gives exactly one occurrence of a length-\(\ell+2\) factor \(b a^\ell c\), with \(b,c\neq a\), and conversely. Each such factor occurs \(q^{n-\ell-2}\) times, since there are that many distinct length-\(n\) extensions and each extension occurs once. There are \((q-1)^2\) choices of \((b,c)\). Consequently,
\[
r_{a,\ell}=(q-1)^2q^{n-\ell-2}\quad(1\le\ell\le n-2).
\]
The length-\(n-1\) factor \(a^{n-1}\) appears exactly \(q\) times, as each of its \(q\) distinct one-symbol right extensions occurs once. Exactly two such occurrences lie inside the unique length-\(n\) run. Every other occurrence must constitute a separate length-\(n-1\) run, since no other run is longer. Therefore \(r_{a,n-1}=q-2\), and \(r_{a,n}=1\). No runs longer than \(n\) exist.

Multiply each per-symbol count by \(q\) to obtain the asserted \(R_\ell\). A source run of length \(\ell\) has exactly \(\ell\) deletion positions, and by Part 1 its descendant is unique to that run; hence its probability is \(\ell/q^n\). Summing the distribution gives
\[
\begin{aligned}
|\mathcal D_1(W)|
&=q(q-1)^2\sum_{\ell=1}^{n-2}q^{n-\ell-2}+q(q-2)+q\\
&=q(q-1)(q^{n-2}-1)+q(q-1)\\
&=(q-1)q^{n-1}.
\end{aligned}
\]
The empty sum convention covers \(n=2\). The run-length check \(\sum_{\ell}\ell R_\ell=q^n\) follows independently because all original positions belong to precisely one run. This proves the complete statement. \(\square\)

## Verification
The self-contained Python 3 program `verify.py` independently generates de Bruijn circles using the FKM necklace-concatenation algorithm, literally deletes every indexed position, takes the lexicographically least rotation of each output, and compares its empirical probability multiplicity spectrum with the theorem. It tests all \(q\in\{2,3,4,5\}\) across the finite parameter range recorded in `verification.log` (16 parameter pairs). A separate exhaustive family generator varies the outgoing-arc orders of **every** binary de Bruijn overlap state and checks all \(1,2,16,2048\) distinct cycles at orders \(2,3,4,5\). Reproduce with `python3 verify.py`; expected terminal marker: `VERIFY_OK FKM_parameter_pairs 16 binary_all_orders_2_to_5`. Finite tests corroborate the proof; they are not the reason for the all-order assertion.

## Relationship to prior work
Sloane (2002), Section 5, treats ordinary linear one-deletion descendants, whose number is the number of linear runs. Liron and Langberg (2012) study the linear run-sensitive subsequence problem in considerably more generality. Sawada, Williams and Wong (2015 preprint, 2016 journal) construct de Bruijn sequences through a necklace-based successor rule; this supplies a natural source family but not the effect of deleting one source position. A publicly available sharp one-deletion-outdegree theorem for **arbitrary binary necklaces** (2026) determines the maximum over length classes; it does not give the exact output support or likelihood distribution for *every* de Bruijn cycle, nor does it cover the arbitrary-\(q\) probability spectrum. This theorem explicitly separates the new cyclic trace assertion from the elementary existing linear-run counting fact. The numerical formula alone should not be interpreted as a uniqueness or priority certificate.

## Limitations
This is an exact one-deletion **output distribution for a fixed source**, not a reconstruction probability for an unknown de Bruijn cycle, nor a deletion-correcting code capacity. It does not cover two deletions, reflections, letter relabeling, near-de Bruijn sources, or nonuniform site deletion. The result has an elementary proof, and a previously unindexed formulation or a broader result about cyclic insertion/deletion could subsume it. Independent validation of the novelty assessment and mathematical proof has not been performed.

## References
1. N. J. A. Sloane, *On Single-Deletion-Correcting Codes*, arXiv:math/0207197v1, publicly posted 2002-07-22, https://arxiv.org/html/math/0207197v1, especially Sections 1, 2 and 5.
2. Y. Liron and M. Langberg, *A characterization of the number of subsequences obtained via the deletion channel*, arXiv:1202.1644v1, posted 2012-02-08, https://arxiv.org/html/1202.1644v1, especially Sections I–II and VII.
3. J. Sawada, A. Williams and D. Wong, *A surprisingly simple de Bruijn sequence construction*, dated 2015-08-12, https://www.cis.uoguelph.ca/~sawada/papers/new_construction_binary.pdf, Sections 1–4; *Discrete Mathematics* **339** (2016), 127–131.
4. *Sharp one-deletion outdegree of binary necklaces*, publicly indexed mathematical finding (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-one-deletion-outdegree-of-binary-necklaces--2341722fce11/RESULT.md, especially Finding and Proof.
