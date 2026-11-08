# Sharp exact-two palindromic-duplication spheres for odd block lengths over large alphabets

## Finding
For every odd integer \(k\ge3\), every \(n\ge k\), and every alphabet \(\Sigma\) with \(q=|\Sigma|\ge n\), the maximum cardinality of an exact-two-step length-\(k\) palindromic-duplication sphere is
\[
\max_{x\in\Sigma^n}|D^2_{k,\mathrm{pal}}(x)|=(n-k+1)(n+1)-\binom{\max\{0,n-2k+2\}}{2}.
\]
Every source with pairwise distinct symbols attains the bound. Moreover, each of its two-step descendants has exactly one history except descendants obtained by duplicating two disjoint original blocks in either order; these have exactly two histories. The result also has a proof for even \(k\ge2\), for which the maximum itself was already established in the cited 2026 work; the new maximum statement is restricted to **odd** block lengths.

## Assumptions and scope
An alphabet has \(q\) symbols, and a word \(x\) has length \(n\). With zero-based indices, \(T_{i,k}(x)\) replaces \(x=uvw\), \(|u|=i\), \(|v|=k\), by \(uvv^Rw\). The second step acts on the resulting word of length \(n+k\), and its source block may contain copies inserted by the first. Define \(D^2_{k,\mathrm{pal}}(x)=\{T_{j,k}(T_{i,k}(x)):0\le i\le n-k,\ 0\le j\le n\}\). No complement operation is used. There are \(H=(n-k+1)(n+1)\) ordered histories. We allow all \(n\ge k\) and all \(q\ge n\) (hence arbitrarily long odd duplication blocks), with no probabilistic assumptions.

## Proof
**Universal bound.** Take two source blocks starting at \(a<b\) with \(b-a\ge k\). They are disjoint, and the two histories \((a,b+k)\) and \((b,a)\) give the same word, since the operations act on disjoint original factors. These two-history pairs are pairwise disjoint. Their number is
\[
P=\#\{(a,b):0\le a<b\le n-k,\ b-a\ge k\}=\binom{\max\{0,n-2k+2\}}{2}.
\]
Thus every source has at most \(H-P\) distinct descendants, independently of the alphabet and parity.

**Distinct-symbol source and recoverable gaps.** Choose \(x=x_0\cdots x_{n-1}\) with all \(n\) symbols different. Every copied occurrence of a symbol is inserted strictly **after** a pre-existing occurrence of that symbol, so induction over the operations shows that the first occurrence of \(x_i\) in any descendant is its original occurrence. Those first occurrences appear in the original order. Consequently, the received word unambiguously identifies the original positions and every copied-symbol run in the gaps after original symbols. A history of two duplications has either two different occupied gaps with \(k\) copies each or one occupied gap with \(2k\) copies, since each insertion is a contiguous \(k\)-symbol block and does not move an original symbol to another gap.

**Two different gaps.** Label their original right endpoints \(a<b\), necessarily \(a,b\ge k-1\), and write \(R_c=x_cx_{c-1}\cdots x_{c-k+1}\). If gap \(b\) is duplicated before gap \(a\), the copied strings at the two gaps are \(R_a,R_b\). If gap \(a\) is duplicated first, its string is \(R_a\). Put \(d=b-a\). For \(d\ge k\), its insertion does not affect the last \(k\) symbols before original \(x_b\), so the gap-\(b\) string is also \(R_b\): these are precisely the commuting histories counted above. For \(1\le d<k\), the last \(k\) symbols before \(x_b\) consist of the last \(k-d\) letters of \(R_a\) followed by \(x_{a+1}\cdots x_b\). Their reversal is
\[
B'=(x_b\cdots x_{a+1})(x_{a-k+1}\cdots x_{a-d}),
\]
which differs from \(R_b=(x_b\cdots x_{a+1})(x_a\cdots x_{b-k+1})\): the letters immediately after their common initial \(d\)-symbol segment are respectively \(x_{a-k+1}\) and \(x_a\). Distinct original symbols, together with \(k\ge2\), make these unequal. Thus the execution order is recoverable whenever the original blocks overlap.

**One occupied gap.** Let its right endpoint be \(a\), and let \(R=R_a\), a list of \(k\) pairwise distinct symbols. The first insertion must occur directly after original \(x_a\), creating \(R\). The second insertion occurs after the first \(t\) copied symbols for one unique integer \(0\le t\le k\); the block inserted is the reversal of the preceding \(k\) letters. For \(t=0\), the final gap string is \(RR\), which has no equal adjacent symbols inside the gap when \(k\ge2\). For \(1\le t\le k\), the first \(t\) gap symbols are \(R_1\cdots R_t\), pairwise different, and the next symbol, the first newly inserted one, repeats \(R_t\). Therefore the *first* pair of equal adjacent symbols **inside the gap** occurs precisely at gap positions \(t\) and \(t+1\) (one-based). Hence the final gap string determines \(t\) uniquely. There are no distinct histories yielding the same one-gap output.

The occupied-gap pattern is recoverable, the two-gap comparison has only the indicated commuting collisions, and the one-gap comparison has none. Therefore there are exactly \(P\) two-element history fibers and all other fibers are singletons. The exact sphere size is \(H-P\), achieving the universal bound. \(\square\)

## Verification
Run `python3 checker.py` (Python 3 standard library). The checker enumerates all ordered histories for pairwise-distinct sources, for every \(2\le k\le8\) and \(k\le n\le19\), verifies the exact sphere count and tests that the only doubleton fibers are the two commuting orders. It also enumerates all binary and ternary sources through length \(7\) for the universal upper bound. The mathematical proof is uniform and independent of these finite experiments.

## Relationship to prior work
Zabokritskiy (arXiv:2609.00779, publicly submitted September 1, 2026), Theorem 5.1, proves the same numerical upper bound is sharp for **even** \(k\ge2\) over **every** alphabet with at least two symbols, using alternating binary sources and equality-edge signatures. Its disjoint-block commutation supplies the upper-bound idea. The odd-block regime treated here is outside that theorem, and the present proof establishes attainment for all odd \(k\ge3\) when \(q\ge n\), by tracking first occurrences. Lenz, Wachter-Zeh and Yaakobi (arXiv:1707.00052, Sections 3.3 and Appendix 0.A) address one palindromic duplication and collisions among *single* duplication positions, not exact-two sequential spheres. Sun and Ge (arXiv:2602.01151) study coding constructions for disjoint long duplications and other regimes, not the exact-two maximum in the present setting.

## Limitations
The **odd**-\(k\) maximum is proved only when \(q\ge n\); the unrestricted odd-block maximum for fixed small alphabets is not determined. The proof does not give an optimal error-correcting code, nor does it cover three or more duplications. The distinct-symbol collision assertion fails at \(k=1\) (e.g. a one-symbol source has two histories but only one exact-two descendant). The finite checker does not prove the infinite statement; it is a reproducibility aid. Independent validation and definitive historical-priority checks have not been performed.

## References
1. A. L. Zabokritskiy, *Coding for Multiple Reverse-Complement and Palindromic Duplications*, arXiv:2609.00779 (first public version September 1, 2026), especially Theorem 5.1 and its proof. https://arxiv.org/abs/2609.00779
2. A. Lenz, A. Wachter-Zeh, and E. Yaakobi, *Bounds on Codes Correcting Tandem and Palindromic Duplications*, arXiv:1707.00052 (June 30, 2017), Sections 3.3 and Appendix 0.A. https://arxiv.org/abs/1707.00052
3. Y. Sun and G. Ge, *On the Palindromic/Reverse-Complement Duplication Correcting Codes*, arXiv:2602.01151 (February 1, 2026). https://arxiv.org/abs/2602.01151
