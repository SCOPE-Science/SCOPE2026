# Optimal subsequence-universal pseudopalindromes for mixed alphabet involutions

## Finding
Let \(\Sigma\) be a labeled alphabet, and let \(\theta:\Sigma\to\Sigma\) be an involution with exactly \(p\ge1\) transposed pairs and \(f\ge1\) fixed letters. Put \(q=2p+f\). Call a word \(w\) \(\theta\)-palindromic if \(w=\theta(w^R)\), and \(k\)-universal if every \(k\)-letter word over \(\Sigma\) is a scattered subsequence of \(w\). For every integer \(k\ge1\), the minimum possible length is
\[
L_\theta(k)=\begin{cases}qk,&k\text{ even},\\qk+f-1,&k\text{ odd}.\end{cases}
\]
The number \(M_\theta(k)\) of \(\theta\)-palindromic \(k\)-universal words of that minimum length is exactly
\[
M_\theta(k)=\begin{cases}(q!)^{k/2},&k\text{ even},\\(q!)^{(k-1)/2}\,f\,2^p(p+f-1)!,&k\text{ odd}.\end{cases}
\]
All minimizers are characterized explicitly below. These formulas concern the **mixed** case \(p,f\ge1\); the pure ordinary-palindrome and fixed-point-free reverse-complement cases are existing boundary cases and are not claimed as new.

## Assumptions and scope
The alphabet symbols are distinct and labeled. The symbol map \(\theta\) satisfies \(\theta^2=\mathrm{id}\) and consists of \(p\ge1\) disjoint transpositions and \(f\ge1\) fixed points. For a word \(u=u_1\cdots u_n\), write \(u^R=u_n\cdots u_1\) and \(\theta(u)=\theta(u_1)\cdots\theta(u_n)\). A scattered subsequence preserves relative order but need not occupy consecutive positions. All quantifiers range over finite words and integers \(k\ge1\).

A *permutation block* is a word of length \(q\) containing every alphabet symbol exactly once. Write \(k=2r\) or \(k=2r+1\) as appropriate. The precise set of shortest witnesses is:

**Even \(k=2r\).** Choose any ordered concatenation \(u=P_1\cdots P_r\) of \(r\) permutation blocks, and set
\[w=u\,\theta(u^R).\]
These, and only these, are optimal.

**Odd \(k=2r+1\).** Choose any fixed letter \(c\), any \(r\) permutation blocks \(P_1,\ldots,P_r\), and any word \(R\) that is a permutation of the \(p+f-1\) letters consisting of one representative of each transposed pair and every fixed letter other than \(c\). With \(u=P_1\cdots P_r R\), set
\[w=u\,c\,\theta(u^R).\]
These, and only these, are optimal. In particular, the shortest odd-index witness is necessarily odd-length and has a central fixed letter.

## Proof
**1. Universality and complete-alphabet blocks.** A word is \(k\)-universal if and only if it admits a factorization into \(k\) consecutive nonempty factors each containing every letter. The forward implication follows by greedy *arch* factorization: repeatedly end each factor at the first position where all \(q\) letters have appeared; if fewer than \(k\) arches exist, the sequence of last-new letters of the arches followed by a letter absent from the remaining suffix is not a subsequence. Conversely, one can select one target letter from each complete factor. Consequently every \(k\)-universal word has length at least \(qk\), and any \(k\)-universal word of length exactly \(qk\) is a concatenation of \(k\) permutation blocks.

**2. Parity lower bounds.** In a \(\theta\)-palindromic word, transposed letters occur with equal multiplicities. A fixed letter occurs an even number of times unless it is the unique middle letter of an odd-length word, in which case its multiplicity is odd. Every letter must occur at least \(k\) times in a \(k\)-universal word, because its \(k\)-fold constant word must embed. If \(k\) is even, the general lower bound \(qk\) applies. If \(k\) is odd, an even-length \(\theta\)-palindrome needs at least \(k+1\) copies of each of its \(f\) fixed letters, hence length at least \(qk+f\). An odd-length one has one central fixed letter \(c\), and the other \(f-1\) fixed letters must appear at least \(k+1\) times; hence length at least \(qk+f-1\). Equality in the odd bound forces exactly \(k\) occurrences of \(c\) and every nonfixed letter, and exactly \(k+1\) occurrences of every other fixed letter.

**3. Even minimizers.** At length \(2rq\), every complete-alphabet block in a universal \(\theta\)-palindrome has length \(q\) and is a permutation block by Step 1. Its first half \(u\), of length \(rq\), consists of \(r\) such blocks. The symmetry determines the second half as \(\theta(u^R)\), and every choice works: the second half is again a concatenation of \(r\) permutation blocks. There are precisely \((q!)^r\) distinct choices.

**4. Odd minimizers: forced central orbit transversal.** Let \(w=u\,c\,\theta(u^R)\) be a shortest odd-index witness, with \(k=2r+1\). Then \(c\) is fixed and
\[|u|=rq+p+f-1.\]
By equality in Step 2, \(c\) occurs exactly \(2r+1\) times throughout \(w\). In any factorization into \(2r+1\) complete-alphabet factors, each factor must therefore contain exactly one \(c\). The central occurrence of \(c\) is the \((r+1)\)-st occurrence of \(c\), so the first \(r\) factors are entirely in \(u\), and the last \(r\) are entirely in \(\theta(u^R)\).

Let \(L\) be the shortest prefix length of \(u\) containing \(r\) successive complete-alphabet factors, with \(L=0\) when \(r=0\). Necessarily \(L\ge rq\). Reversal followed by \(\theta\) transforms a factorization of a prefix of \(u\) into a factorization of a suffix of \(\theta(u^R)\), and conversely; hence the last \(r\) factors of \(w\) require at least \(L\) positions of its right half. The middle factor containing the central \(c\) must be contained in
\[R\,c\,\theta(R^R),\qquad R=u[L+1\ldots |u|].\]
For this middle region to contain all alphabet letters, \(R\) must contain at least one representative from each of the \(p\) transposed pairs and all \(f-1\) fixed letters other than \(c\). Consequently
\[|R|\ge p+f-1,\qquad |R|=rq+p+f-1-L\le p+f-1.\]
Both inequalities are equalities, giving \(L=rq\). Therefore the first \(rq\) letters of \(u\) form \(r\) permutation blocks, while its remaining \(p+f-1\) letters form exactly the stated orbit transversal and the other fixed letters, with no repetitions. This proves necessity.

Conversely, any such \(u\) yields \(r\) full permutation blocks on the left, the middle factor \(R c\theta(R^R)\) containing all \(q\) letters, and \(r\) full permutation blocks on the right. Hence \(w\) is \((2r+1)\)-universal and attains the lower bound. There are \((q!)^r\) choices for the outer blocks, \(f\) choices of central fixed letter, \(2^p\) choices of representatives of transposed pairs, and \((p+f-1)!\) orders for \(R\). All give different words, establishing the odd count.

## Verification
The standalone Python 3 program `verify.py` enumerates all words fixed by the specified antimorphism at the asserted optimum length for small involution types. It independently tests the explicit block-orbit characterization against a greedy universality index, and checks the factorial enumerator. A second oracle explicitly checks all \(q^k\) length-\(k\) patterns as scattered subsequences for selected small cases. The included output records 1,385,969 tested symmetric words, 7,632 classified extremizers and 79,828 full-pattern oracle comparisons across 34 test configurations. These are finite diagnostics, not substitutes for the proof.

To reproduce, run `python3 verify.py` alongside this report. Only the Python standard library is needed; no external input is required.

## Relationship to prior work
Barker, Fleischmann, Harwardt, Manea, and Nowotka (2020), especially Proposition 15 and its discussion of palindromes, supply the known arch-based index framework. Their Proposition 18 addresses permutations applied to concatenated words, but the inspected text does not state the mixed fixed-point/transposition optimal-length and exact enumeration formulas. Adamson (2023) provides enumeration algorithms for unrestricted subsequence-universal words, but does not impose the present mixed antimorphic symmetry. Related research on reverse-complement sequences in DNA storage motivates such symmetries, without proving a universal-subsequence classification.

The two endpoint cases, when every symbol is fixed or no symbol is fixed, have existing separate classifications; in particular the all-fixed case follows from the known palindrome midpoint relation. The statement here is expressly confined to the mixed case, where the exact penalty \(f-1\) and the orbit-transversal multiplicity \(f2^p(p+f-1)!\) are the new content. The fact that the sources and consulted research indexes did not expose the same assertion is evidence for, not a proof of, originality.

## Limitations
The theorem concerns exact symmetry under a single involution and exact subsequence coverage at *minimum possible length*. It does not classify near-minimal words, approximate subsequence coverage, or simultaneous invariance under multiple antimorphisms. The all-fixed and fixed-point-free boundary cases are not originality claims. Independent mathematical audit is not performed, and unindexed equivalent results remain possible.

## References
1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, and D. Nowotka, *Scattered Factor-Universality of Words*, first public posting 2020-03-10, arXiv:2003.04629v1, particularly Section 4 and Propositions 15 and 18, https://arxiv.org/abs/2003.04629 .
2. D. Adamson, *Ranking and Unranking k-subsequence universal words*, first public posting 2023-04-10, arXiv:2304.04583v1, especially Section 3, https://arxiv.org/abs/2304.04583 .
3. R. Zhang and H. Wu, *On secondary structure avoidance of codes for DNA storage*, published 2023-11-29, https://doi.org/10.1016/j.csbj.2023.11.035 .
