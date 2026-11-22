# Exact distance-resolved collisions of one-deletion set-partition reads

## Finding
Let \(P\) be a partition of the ordered set \([n]\), where \(n\ge2\). Let \(\Delta_i(P)\) be the induced partition obtained by removing position \(i\) and renumbering the remaining positions in increasing order. For \(1\le i<j\le n\), put \(\ell=j-i+1\).

**Collision classification.** The outputs \(\Delta_i(P)\) and \(\Delta_j(P)\) coincide if and only if one of two disjoint possibilities holds:

1. All positions in the interval \([i,j]\) belong to one block of \(P\).
2. For some \(d\) with \(2\le d\le\ell\), the block-membership sequence on \([i,j]\) is the length-\(\ell\) prefix of the periodic sequence \((A_1A_2\cdots A_d)^\omega\), where \(A_1,\ldots,A_d\) are pairwise different blocks of \(P\), and none of those blocks meets the complement of \([i,j]\).

Let \(S(a,b)\) denote a Stirling number of the second kind with \(S(0,0)=1\) and \(S(a,b)=0\) when \(b<0\) or \(b>a\), and let \(B_a=\sum_bS(a,b)\) be a Bell number. For any fixed ordered deletion pair with interval length \(\ell\), the number of \(k\)-block partitions yielding identical outputs is exactly
\[
C_{n,k,\ell}=S(n-\ell+1,k)+\sum_{d=2}^{\ell} S(n-\ell,k-d).
\]
Without fixing the number of blocks, this becomes
\[
C_{n,\ell}=B_{n-\ell+1}+(\ell-1)B_{n-\ell}.
\]
Consequently the total number of unordered *pairs of deletion positions* with equal outputs, summed over all set partitions of \([n]\), is
\[
T_n=\sum_{\ell=2}^{n}(n-\ell+1)\bigl[B_{n-\ell+1}+(\ell-1)B_{n-\ell}\bigr].
\]
Pairs are counted with multiplicity: this is not the number of distinct output partitions.

For a uniform random set partition \(P_n\), let \(D_n=|\{\Delta_i(P_n):1\le i\le n\}|\), and let \(A_n\) count adjacent positions in the same source block. Define
\[
R_n=\sum_{\ell=2}^n(n-\ell+1)(\ell-1)B_{n-\ell}.
\]
Then the finite-length bounds
\[
\Pr(D_n=n-A_n)\ge1-\frac{R_n}{B_n},\qquad
0\le n-(n-1)\frac{B_{n-1}}{B_n}-\mathbb E[D_n]\le\frac{R_n}{B_n}
\]
hold. Standard Bell-number ratio estimates additionally give \(R_n/B_n=O((\log n)^2/n)\). Thus with probability tending to one, the *only* loss of distinct deletion reads comes from neighboring positions in the same block, despite the existence of nonlocal collisions in exceptional partitions.

## Assumptions and scope
The source partition has unlabeled blocks, and positions are ordered and distinguishable before deletion. The receiver sees the induced partition of the remaining positions, not labels assigned to the original blocks. Two outputs are equal if and only if every pair of remaining positions has the same block-equivalence relation. These definitions differ from a labeled-alphabet deletion channel. All formulas are exact for every integer \(n\ge2\), \(1\le k\le n\), and \(2\le\ell\le n\); nonexistent Stirling indices contribute zero. The asymptotic statement concerns the uniform distribution over all \(B_n\) set partitions, without fixing \(k\).

## Proof
Represent a partition by an arbitrary block-name word \(a_1\cdots a_n\), where equal names mean membership in the same block. Comparing the outputs from deleting \(i\) and \(j\), the positions corresponding to \(t=i,\ldots,j-1\) carry names \(a_t\) in the second deletion and \(a_{t+1}\) in the first. Both outputs induce the same partition exactly when
\[
(a_s=a_t)\iff(a_{s+1}=a_{t+1})\quad (i\le s,t<j)
\]
and, for every outside position \(h<i\) or \(h>j\),
\[
(a_t=a_h)\iff(a_{t+1}=a_h)\quad(i\le t<j).
\]
Outside-versus-outside equality is unchanged automatically.

The first displayed condition says the right-shift map on symbols occurring within the interval is single-valued and injective wherever defined. If there is no repetition in the interval, take \(d=\ell\). Otherwise let \(s<t\) be the earliest repeated pair (minimal second index), and put \(d=t-s\). The equivalence applies both forward and backward, so \(a_u=a_{u+d}\) throughout the interval whenever both positions exist. The first \(d\) names are different, since any repetition among them would contradict the minimality of \(t\). Therefore the interval is exactly a prefix of a periodic sequence on \(d\) different block names. Conversely every such sequence satisfies the first condition.

If \(d=1\), the interval is constant and the comparison with outside positions holds automatically. If \(d\ge2\), the second displayed condition implies that no interval block can occur outside: an outside name equal to one internal name would have to remain equal to every successive internal name, which contradicts their distinctness. Conversely isolation of all \(d\) interval blocks makes the comparisons with outside positions automatically true. This proves the classification, including the case \(\ell=2\) and intervals reaching the endpoints.

For the constant case, contract the \(\ell\) consecutive positions to one element. This is a bijection to partitions of \(n-\ell+1\) points with \(k\) blocks, counted by \(S(n-\ell+1,k)\). For each fixed \(d\ge2\), the residue classes of positions modulo \(d\) determine the \(d\) distinct wholly internal blocks uniquely. Independently partition the remaining \(n-\ell\) positions into \(k-d\) blocks, counted by \(S(n-\ell,k-d)\). The different minimal periods are disjoint. Summing over \(d\) proves the block-refined formula. Summing over \(k\) and noting that \(\sum_k S(n-\ell,k-d)=B_{n-\ell}\) proves the Bell formula; exactly \(n-\ell+1\) pairs of deletion sites have the same interval length \(\ell\), yielding \(T_n\).

Let \(E(P)\) count pairs of deletion sites of the second, isolated-periodic type. All positions belonging to a maximal consecutive run of one block give the same deletion output, by the constant case; the number of such runs is \(n-A(P)\). Any further identification between different runs is a pair of the second type. Hence
\[
0\le n-A(P)-D(P)\le E(P).
\]
The mean of \(A(P)\) over the uniform partition model is \((n-1)B_{n-1}/B_n\), because requiring any specified adjacent pair to share a block is equivalent to contracting that pair. The sum of \(E(P)\) over all partitions is exactly \(R_n\). The probability and expectation inequalities follow from the union bound and linearity of expectation.

For completeness, the classical Bell-number consecutive-ratio estimate \(B_{m-1}/B_m=O(\log m/m)\) implies that uniformly for \(2\le\ell\le n/2\), \(B_{n-\ell}/B_n\le(C\log n/n)^\ell\), for some constant \(C\) and sufficiently large \(n\). For \(\ell>n/2\), monotonicity gives \(B_{n-\ell}/B_n\le B_{\lfloor n/2\rfloor}/B_n\), which is superpolynomially small by the same ratio bound. Substitution into the definition of \(R_n\) proves the stated \(O((\log n)^2/n)\) estimate.

## Verification
The standalone Python 3 program `check.py` constructs all unlabeled set partitions by canonical first-occurrence block names, forms actual induced deletion partitions, and checks the structural criterion for every ordered pair of deletion positions through \(n=9\). It independently evaluates the block-refined Stirling formula at every such length and checks the total Bell formula. It also checks 11,800 pseudorandom larger cases (lengths 2 through 60) under arbitrary block labels. Run `python3 check.py`; expected final line begins `VERIFY_OK` and reports 899301 exhaustive comparisons. Exact exhaustive checks are finite confirmation and are not substituted for the all-length proof.

## Relationship to prior work
The notion of restricting and standardizing a set partition occurs in Sagan's *Pattern Avoidance in Set Partitions* (2006) and Bloom–Saracino's *Pattern avoidance for set partitions à la Klazar* (2015). Both study which smaller partitions occur and enumerate avoidance classes; the inspected full texts do not provide equality conditions for two specified one-position deletions, an exact distance-and-block-count collision formula, or the exceptional-periodic collision bound. The classical labeled-word deletion rule identifies equal outputs only when the deleted positions lie in the same constant run; unlabeled block identities create the additional isolated-periodic mechanism.

## Limitations
These results count collisions among deletion *positions within one source*, not confusability between two different source partitions, and do not give an exact generating function for the entire distinct-output-size distribution or optimal deletion-correcting code sizes. The asymptotic probability bound uses a standard established Bell-ratio estimate; the combinatorial equalities and all finite-length formulas are independent of that estimate. A yet-unlocated earlier equivalent set-partition deletion theorem remains a priority risk; novelty is not certified by negative search results.

## References
- B. E. Sagan, *Pattern Avoidance in Set Partitions*, first arXiv version 12 April 2006, https://arxiv.org/abs/math/0604292 .
- J. Bloom and D. Saracino, *Pattern avoidance for set partitions à la Klazar*, first arXiv version 1 November 2015, https://arxiv.org/abs/1511.00192 .
- N. G. de Bruijn, *Asymptotic Methods in Analysis*, classical Bell-number asymptotics; the weaker ratio estimate cited in the proof is standard.
