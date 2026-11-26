# Exact inverse-extension lengths and their distribution in the Černý automata

## Finding

Let \(n\geq 3\) and let \(C_n\) be the deterministic automaton with states \(Q=\{0,1,\ldots,n-1\}\) and alphabet \(\{a,b\}\), where
\[
\delta(i,a)=i+1\pmod n,\qquad
\delta(i,b)=\begin{cases}0,&i=n-1,\\ i,&0\leq i<n-1.\end{cases}
\]
For a nonempty proper subset \(S\subset Q\), write \(S w^{-1}=\{q\in Q:\delta(q,w)\in S\}\), and define the *minimum inverse-extension length*
\[
E_n(S)=\min\bigl\{|w|:\lvert S w^{-1}\rvert>\lvert S\rvert\bigr\}.
\]
A *cyclic run start* of \(S\) is an \(i\in S\) with \(i-1\pmod n\notin S\). Every nonempty proper subset has at least one. Set
\[
r_n(S)=\min\{i\in S:i-1\pmod n\notin S\},
\]
where the minimum uses the standard integer ordering \(0<1<\cdots<n-1\).

**Theorem (exact length, unique witness, and complete spectrum).** For every \(n\geq3\) and every nonempty proper \(S\subset Q\),
\[
\boxed{E_n(S)=r_n(S)+1.}
\]
The **unique word of minimum length** extending \(S\) is \(b a^{r_n(S)}\). Moreover, for every integer \(t\), the exact number \(N_n(t)\) of nonempty proper subsets with \(E_n(S)=t\) is
\[
\boxed{N_n(t)=
\begin{cases}
 t\,2^{n-t-1},&1\leq t\leq n-1,\\
 n-1,&t=n,\\
 0,&\text{otherwise}.
\end{cases}}
\]
In particular, exactly \(n-1\) subsets cannot be extended by any word of length at most \(n-1\). They are exactly
\[
\boxed{\{n-1\}\cup\{0,1,\ldots,j-1\},\qquad 0\leq j\leq n-2,}
\]
with the second set empty when \(j=0\).

## Assumptions and scope

Words act on states from left to right. Their preimages act on subsets from right to left. Letter \(a\) is the cyclic permutation, and \(b\) collapses state \(n-1\) onto state \(0\) and fixes every other state. The result applies to every nonempty proper subset of every such labeled automaton, including singletons and subsets of cardinality \(n-1\). A nonempty proper subset cannot have zero inverse-extension length because the empty word leaves it unchanged.

The term *stuck* here means a subset with extension length strictly greater than \(n-1\); it does not mean one admitting no extending word at all. The result is about cardinality-increasing inverse images, not forward-set synchronization or avoidance.

## Proof

**1. Inverse letter actions and run starts.** For every subset \(T\subseteq Q\),
\[
T a^{-1}=T-1=\{i-1\pmod n:i\in T\},
\]
and \(T b^{-1}\) agrees with \(T\) at every state except possibly \(n-1\), whose membership becomes the membership of \(0\) in \(T\). Thus
\[
T b^{-1}=\begin{cases}
T\cup\{n-1\},&0\in T,\ n-1\notin T,\\
T\setminus\{n-1\},&0\notin T,\ n-1\in T,\\
T,&\text{otherwise}.
\end{cases}
\]

The first case is the only one increasing cardinality. It occurs **if and only if** \(r_n(T)=0\): a cyclic run starts at state \(0\) exactly when \(0\in T\) and \(n-1\notin T\).

Assume \(T\) is nonempty and proper and \(r_n(T)>0\). A reverse application of \(a\) shifts every cyclic run start down one state, so its least run start becomes precisely \(r_n(T)-1\). No wraparound can supply a smaller run start: all original starts lie between \(r_n(T)\) and \(n-1\), hence their predecessors lie between \(r_n(T)-1\) and \(n-2\).

Under a reverse \(b\) step when \(r_n(T)>0\), cardinality cannot grow. If the step is neutral, nothing changes. Otherwise it deletes \(n-1\), necessarily with \(0\notin T\). Such a deletion can remove an existing run start at \(n-1\), but cannot create a new start at \(0\) (because \(0\notin T\)) or at any other index. Consequently, if the resulting set is still nonempty and proper, its least run start does not decrease. If deletion makes it empty, every subsequent inverse image is also empty, so the word cannot eventually extend the initial nonempty set.

**2. Lower bound.** Begin with \(S\) and process the letters of any candidate word in reverse, applying preimages. Before the first cardinality-increasing step, reverse \(b\) applications cannot decrease the least run-start index when that index is positive. Reverse \(a\) can reduce a positive least run-start index by exactly one. If a reverse \(a\) is applied at run-start index zero, the least run-start index wraps to a nonnegative value rather than supplying a cardinality increase. Hence at least \(r_n(S)\) reverse \(a\) steps must occur before any cardinality-increasing reverse \(b\) step. At least one such \(b\) step is necessary for the final preimage to exceed \(\lvert S\rvert\), since \(a\) preserves cardinality and \(b\) is the only letter that can increase it. Therefore every extending word has length at least \(r_n(S)+1\).

**3. Achievability and uniqueness.** Let \(r=r_n(S)\). Apply \(a^{-1}\) exactly \(r\) times to \(S\). The set \(T=S-r\) has a cyclic run beginning at \(0\), hence \(0\in T\) and \(n-1\notin T\). The subsequent \(b^{-1}\) adds \(n-1\), giving \(\lvert T b^{-1}\rvert=\lvert S\rvert+1\). This is the inverse action of the word \(b a^r\), of length \(r+1\).

Any word attaining the lower bound must use exactly \(r\) copies of \(a\) before its first increasing preimage step, and exactly one copy of \(b\), used at that step. Since no other letters are available, the inverse-action sequence is forced to be \(r\) copies of \(a^{-1}\) followed by one \(b^{-1}\). Thus \(b a^r\) is the **unique** shortest extending word.

**4. Counting the distribution.** Fix \(r=r_n(S)\). For \(r=0\), the conditions are precisely \(0\in S\) and \(n-1\notin S\), with the remaining \(n-2\) membership bits arbitrary. Hence \(2^{n-2}\) subsets have \(r=0\), the stated formula for \(t=1\).

For \(1\leq r\leq n-2\), the membership bits \(0,\ldots,r-1\) may not contain any new run start, and the bit at \(r-1\) must be zero. Thus the prefix has the unique shape \(1^j0^{r-j}\) for some \(0\leq j\leq r-1\). The bit at \(r\) must be one. If \(j=0\), state \(0\) is absent, so the \(n-r-1\) remaining bits are unrestricted, giving \(2^{n-r-1}\) choices. If \(j\geq1\), state \(0\) is present, and to exclude a run start at zero the bit at \(n-1\) must be one. There are \(r-1\) choices of \(j\), each with \(2^{n-r-2}\) unconstrained internal bits. The total is
\[
2^{n-r-1}+(r-1)2^{n-r-2}=(r+1)2^{n-r-2}.
\]
With \(t=r+1\), this is \(t2^{n-t-1}\).

Finally \(r=n-1\) forces state \(n-1\) present and state \(n-2\) absent. Since no smaller run start may occur, the membership bits at \(0,\ldots,n-2\) must be \(1^j0^{n-1-j}\) for exactly one \(j\) in \(\{0,\ldots,n-2\}\). This yields exactly \(n-1\) subsets and the explicit stuck-set list. The cases partition all nonempty proper subsets (as also checked by summing to \(2^n-2\)), completing the proof.

## Verification

The included standalone program `checker.py` computes reverse-image shortest distances by breadth-first search over all subsets; separately, for small instances, it evaluates the actual forward action of each candidate word and checks that the claimed shortest word is the only shortest one. It also compares the full histogram with the displayed formula for every state count from three through eleven.

Run `python3 checker.py` from a directory containing that file. Expected output:

```
VERIFY_OK
bfs_exact_cases=4070
unique_shortest_word_cases=492
histogram_coefficients=63
```

These finite checks support, but do not replace, the proof for arbitrary \(n\).

## Relationship to prior work

Miccinesi [1] studies certificates for whether arbitrary subsets have an inverse-extension word of length at most \(n-1\). In Section 8.1, the Černý family supplies a necessary obstruction, but the work does not give the complete exact subset-by-subset extension lengths, unique optimal words, or histogram established here. The present result is a specialization to that family, **not** a general improvement to the certificate theorem.

Berlinkov, Ferens and Szykuła [2] formulate inverse-preimage extension and bounded-length decision problems and give general complexity results, with an illustrative small Černý example. A decision procedure or the existence of some extending word does not yield the explicit formula and exact counts for all subsets of the entire family. Szykuła [3] surveys related synchronization, avoidance, and subset problems but does not present this exact classification.

Related published results on forward *avoiding* thresholds and forward *rank-deficiency* profiles of the Černý family use the same automaton but different targets. They do not imply the new exact inverse-extension distribution. Conversely, this result by itself gives no improved universal reset threshold or forward-target reachability bounds.

## Limitations

The theorem treats the labeled two-letter Černý family only; it says nothing about general cyclic rank-deficient automata. It classifies the shortest word that enlarges a given inverse image, not the shortest word that takes the given subset all the way to \(Q\), and it does not improve the known quadratic reset threshold. The literature comparisons do not establish definitive historical priority: independently unindexed notes or an implicit stronger lemma could cover the specialization. An independent mathematical audit has not been performed.

## References

1. Michele Miccinesi, *Certificates for short extending words in a finite automaton*, 2026, arXiv:2609.21603, first posted September 18, 2026. https://arxiv.org/abs/2609.21603
2. Mikhail V. Berlinkov, Robert Ferens, Marek Szykuła, *Preimage problems for deterministic finite automata*, 2017, arXiv:1704.08233. https://arxiv.org/abs/1704.08233
3. Marek Szykuła, *Synchronizing Automata: Open Problems*, 2026, arXiv:2608.24245. https://arxiv.org/abs/2608.24245
