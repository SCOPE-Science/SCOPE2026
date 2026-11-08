# Exact two-hole reaching distances in the Černý automata

## Finding

For every integer \(n\ge 4\), let \(Q=\{0,1,\ldots,n-1\}\) and let the classical two-letter Černý automaton act on states by
\[
a(i)=i+1\pmod n,\qquad
b(i)=\begin{cases}0,&i=n-1,\\i,&0\le i\le n-2.\end{cases}
\]
Words act from left to right. For \(0\le p<q<n\), set \(T_{p,q}=Q\setminus\{p,q\}\). Define the **exact reaching distance**
\[
d_n(p,q)=\min\{|w|:\delta(Q,w)=T_{p,q}\}.
\]
The exact answer for every such target is
\[
\boxed{
d_n(p,q)=
\begin{cases}
 n+2,&q=n-1,\ p=0,\\
 p+3,&q=n-1,\ p\ge1,\\
 n+p+3,&q\le n-2,\ q=p+1,\\
 q+3,&q\le n-2,\ q\ge p+2.
\end{cases}}
\]

In particular, **every integer between \(4\) and \(2n\), inclusive**, is an exact reaching distance. If \(H_n(t)\) counts unordered missing pairs with shortest reaching distance \(t\), then
\[
\boxed{H_n(t)=
\begin{cases}
t-3,&4\le t\le n+1,\\
1,&n+2\le t\le2n,\\
0,&\text{otherwise}.
\end{cases}}
\]
The unique hardest pair is \(\{n-3,n-2\}\), with distance \(2n\). This last maximum alone was known; the contribution is the exact distance of **every** pair and the complete histogram.

## Assumptions and scope

A reaching word must have image **equal to** \(T_{p,q}\), not merely contained in it. The alphabet is exactly \(\{a,b\}\), without inverses or weighted letters; word length is the number of letters. The two missing indices are distinct and sorted. The initial set is the entire state set \(Q\). No assertion is made for other automata, higher deficiencies or for the length of words only avoiding the pair (which permits an image of smaller rank).

## Proof

**1. Constructive upper bound.** For \(2\le h\le n-1\), the word \(ba^hb\) sends \(Q\) to a set with exactly the two missing states \(h-1\) and \(n-1\). Indeed, the first \(b\) removes \(n-1\); the rotation shifts that hole to \(h-1\), which is neither \(0\) nor \(n-1\); the second \(b\) adds a new hole at \(n-1\). A following \(a^j\) rotates both holes by \(j\) modulo \(n\).

For each pair \(p<q\), select \((h,j)\) as follows:

- If \(q=n-1\) and \(p\ge1\), use \((h,j)=(p+1,0)\).
- If \((p,q)=(0,n-1)\), use \((h,j)=(n-1,1)\).
- If \(q\le n-2\) and \(q=p+1\), use \((h,j)=(n-1,p+2)\).
- If \(q\le n-2\) and \(q\ge p+2\), use \((h,j)=(q-p,p+1)\).

In each case \(ba^hba^j\) has exactly the desired two holes and length equal to the corresponding displayed formula. Thus the displayed values are upper bounds.

**2. Lower-bound potential.** On subsets of cardinality at least \(n-2\), define a real-valued function \(F\) as follows. Set \(F(Q)=0\). If \(Q\setminus S=\{h\}\), put
\[
F(S)=\begin{cases}1,&h=n-1,\\h+2,&0\le h\le n-2.\end{cases}
\]
For two missing states \(p<q\), set \(F(S)\) equal to the claimed value \(d_n(p,q)\) displayed in the finding. We prove that for either letter \(c\in\{a,b\}\), whenever both \(S\) and \(Sc\) have cardinality at least \(n-2\),
\[
F(Sc)\le F(S)+1.\tag{1}
\]

From \(Q\), the letter \(a\) fixes the set, whereas \(b\) produces the sole hole \(n-1\), satisfying (1). With one missing state \(h\), the letter \(a\) moves the hole to \(h+1\pmod n\), and the stated one-hole formula changes by at most one upward. Under \(b\): if \(h=0\), the hole moves to \(n-1\); if \(h=n-1\), nothing happens; if \(1\le h\le n-2\), a second hole \(n-1\) is created and its potential is \(h+3=F(S)+1\).

With two holes \(p<q\), the letter \(a\) rotates the pair forward. All possibilities reduce to the following exhaustive cases:

- If \(q\le n-3\), a nonadjacent pair remains nonadjacent and increases the claimed potential by exactly one; an adjacent pair also remains adjacent and increases it by exactly one.
- If \(q=n-2\), the rotated pair has one hole at \(n-1\): for \(p\le n-4\), its new potential is \(p+4\le(q+3)+1\); for \(p=n-3\), its new potential is \(n+1\le(n+p+3)+1\).
- If \(q=n-1,p=0\), rotation produces \(\{0,1\}\), increasing the potential from \(n+2\) to \(n+3\).
- If \(q=n-1,1\le p\le n-3\), rotation produces \(\{0,p+1\}\), increasing the potential from \(p+3\) to \(p+4\).
- If \(q=n-1,p=n-2\), rotation produces \(\{0,n-1\}\), increasing the potential from \(n+1\) to \(n+2\).

For \(b\) acting on a two-hole set, a genuine rank reduction to \(n-3\) lies outside the condition in (1). Otherwise \(b\) either fixes the set or, for the pair \(\{0,j\}\) with \(1\le j\le n-2\), replaces it by \(\{j,n-1\}\). The potential of the latter is \(j+3\). The potential of the former is \(n+3\) for \(j=1\), and \(j+3\) for \(j\ge2\), so it never increases. This proves (1) in all cases.

**3. Why lower ranks cannot shorten the path.** All state-set images are monotonically nonincreasing in cardinality under letter actions. A word ending with exactly \(n-2\) states cannot pass through a set of rank \(n-3\) or lower. Therefore every intermediate image along any reaching word lies in the domain of \(F\), and repeatedly applying (1) from \(F(Q)=0\) gives \(F(T_{p,q})\le |w|\). Together with the constructive upper bound, this establishes the distance formula for all \(n\ge4\) and all pairs.

**4. Histogram and extremal pairs.** For each \(t\in\{4,\ldots,n+1\}\), exactly one pair of the form \(\{p,n-1\}\), with \(p=t-3\), has length \(t\), and exactly \(t-4\) nonadjacent pairs with \(q=t-3\) have the same length; hence \(H_n(t)=t-3\). The pair \(\{0,n-1\}\) alone has length \(n+2\). Every adjacent pair \(\{p,p+1\}\) with \(0\le p\le n-3\) has length \(n+p+3\), yielding one instance of each \(t=n+3,\ldots,2n\). The largest is uniquely \(\{n-3,n-2\}\). The total count is \(\binom n2\), confirming completeness.

## Verification

`checker.py` is a standalone Python 3 program using only the standard library. It computes the shortest reaching distances independently by breadth-first search on the image-subset automaton, rather than by the formula or proof potential. It compares all pairs for \(4\le n\le14\), directly executes each constructed shortest witness, and checks every histogram entry in the stated range. Separately, it checks every possible transition satisfying (1) on every high-rank subset for \(4\le n\le40\), including the rank \(n-1\) boundary cases. Its actual execution reported:

```
VERIFY_OK
exact_BFS_pairs 451
witness_pairs 451
histogram_entries 220
potential_transitions 23014
```

These are finite checks; the proof using (1) and the witnesses establishes the universal theorem. The checker does not establish novelty or independent review.

## Relationship to prior work

The 2026 survey by Szykuła explicitly highlights avoiding and synchronization questions, including the one-state avoidance threshold of the Černý automaton, but does not state the exact two-hole reaching distances. Ferens, Szykuła and Vorel (2021) give the \(n=4\) *maximum* two-avoiding threshold of \(8\), not the all-pair distance formula or histogram. Ferens and Szykuła (first public 2022; 2026 journal version) develop general reaching bounds and record sharp Černý examples, not the pairwise expression.

Two public research records provide closer coverage: *Exact k-avoiding thresholds of the Černý automata* proves the \(k=2\) worst-case \(2n\) and unique maximizing target; *Two-defect reachability in cyclic defect-one automata* supplies two-merge witnesses of length at most \(2n\) for every Černý two-hole target. Both results **cover parts of the present statement** (the maximum, the exceptional pair, and existence of bounded witnesses). Neither read result states all the shortest distances or their histogram. The separate initial-rank-compression result supplies the minimum distance \(4\), but not the intermediate distances or multiplicities. A recorded one-step inverse-extension formula determines the cost of expanding a given subset; it does not, by itself, determine the shortest exact reaching words from \(Q\) to every two-hole target. The specific contribution here is the full pairwise geodesic metric and its exact count distribution.

## Limitations

No claim is made that \(2n\), its unique worst target, the two-merge existence theorem, or the rank-\((n-2)\) minimum are new separately; these have existing coverage. The scope is the standard labeled Černý family and exactly two missing states. An older equivalent pairwise classification might be present under avoidance, total extension or transformation-semigroup terminology; historical priority is provisional. The work is mathematically proved and self-review, not independently audited. No bound for arbitrary synchronizing automata or all deficiencies follows from the theorem.

## References

1. M. Szykuła, *Synchronizing Automata: Open Problems*, arXiv:2608.24245, first public 2026-08-25. https://arxiv.org/abs/2608.24245
2. R. Ferens, M. Szykuła, V. Vorel, *Lower Bounds on Avoiding Thresholds*, MFCS 2021, pp. 46:1–46:14. https://doi.org/10.4230/LIPIcs.MFCS.2021.46
3. R. Ferens, M. Szykuła, *Completely reachable automata: a quadratic decision algorithm and a quadratic upper bound on the reaching threshold*, arXiv:2208.05956, first public 2022-08-11; journal version *Recognizing Completely Reachable Automata in Quadratic Time*, 2026. https://arxiv.org/abs/2208.05956
4. *Exact k-avoiding thresholds of the Černý automata*, public mathematical research record, 2026-09-17, published-finding corpus 2026 research collection. https://github.com/published-finding corpus/2026
5. *Two-defect reachability in cyclic defect-one automata*, public mathematical research record, 2026-10-04, published-finding corpus 2026 research collection. https://github.com/published-finding corpus/2026
6. *Exact early deficiency profile of the Černý automata*, public mathematical research record, 2026-10-04, published-finding corpus 2026 research collection. https://github.com/published-finding corpus/2026
