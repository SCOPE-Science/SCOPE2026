# Classifying and counting shortest common reset words for a Černý product with three states

## Finding
Let \(C_k\) have states \(0,\ldots,k-1\) and shared letters \(a(i)=i+1\pmod k\), \(b(0)=1\), and \(b(i)=i\) for \(i\ne0\). Words act left to right. A common reset word maps each factor's full set to a singleton; the two targets need not agree. For \(C_n\times C_3\) with \(n\ge3\) the number of distinct literal words at the minimum common reset length is
\[
N_n=\begin{cases}
1,&n\equiv0\pmod3,\\
2(n-1)(n-3)/3,&n\equiv1\pmod3,\\
(n-2)(n-3)/3,&n\equiv2\pmod3.
\end{cases}
\]
For the divisible case the list consists only of \(W_n=b(a^{n-1}b)^{n-2}\). In the other cases it consists of
\[
V_{n,j,t}=b(a^{n-1}b)^{j-1}a^tba^{n-1-t}b(a^{n-1}b)^{n-2-j},
\qquad 1\le j\le n-2,\quad 0\le t\le n-2,\quad t\ne j,
\]
retaining \(t\not\equiv0\pmod3\) if \(n\equiv1\pmod3\) and \(t\equiv2\pmod3\) if \(n\equiv2\pmod3\).

The threshold \((n-1)^2+\mathbf1_{3\nmid n}\) and the witnesses \(W_n\) and \(V_{n,n-2,n-3}\) for \(n\ge4\) are already stated in [1], under the conjugate convention \(b(k-1)=0\) (cyclically relabel each factor by adding one). They are used here as context; the contribution is classification and counting at that threshold.

## Proof
**Single-factor candidates.** In reverse preimages, \(a\) rotates the current set one step backwards. The inverse of \(b\) adds \(0\) if the set contains \(1\) but not \(0\), and otherwise fixes it or removes \(0\). Starting from a target singleton, discard any inverse \(b\) that does not enlarge the maintained set; monotonicity ensures that ending at the full set is still possible with those deletions. Every productive step in the shortened sequence grows a circular interval, leaving it starting at \(0\). Before the next growth the interval must start at \(1\), requiring at least \(n-1\) inverse rotations. Thus exactly \(n-1\) growths and at least \((n-2)(n-1)\) rotations are needed. At equality every run is forced and there are no boundary letters, giving the unique \(W_n\), which resets by the same interval argument. In particular this gives \(W_3=baab\) for the identical-factor case \(n=3\).

One letter above the minimum, the established single-factor classification [2] consists of \(aW_n,W_na,W_nb\) and the \(V_{n,j,t}\) in the displayed range before the residue filter. To see the split indexing, the one extra letter is either a boundary rotation (interior rotation gaps are fixed modulo \(n\)) or a \(b\) inserted into \(W_n\). In reverse, just before the inserted \(b\), the interval has length \(n-j\) and cyclic start \(t+1\) modulo \(n\). It shrinks exactly when its endpoint is \(0\), which in the displayed range is \(t=j\); shrinkage makes full coverage impossible with only \(n\) inverse \(b\)'s. For \(0<t\le n-2\) with \(t\ne j\) the inserted \(b\) fixes the interval. At \(t=0\) the doubled \(b\) is equivalent to the original \(b\) by idempotence. The omitted offset \(t=n-1\) doubles the next \(b\), represented at \(t=0\) in the next run or by \(W_nb\) if final. Doubling the initial \(b\) is already represented by \(j=1,t=0\). Literal splits are distinct because the altered gap or doubled interior boundary identifies the inserted-letter location in this indexing.

**Three-state filter.** The first \(b\) sends the full three-state set to \(\{1,2\}\). When \(3\mid n\), the next block \(a^{n-1}b\) collapses it, so the single-factor unique optimum is common. Otherwise a full block fixes \(\{1,2\}\) as a set: the rotation exponent is \(0\) or \(1\) modulo three. Thus \(W_n\) and the three boundary extensions do not reset the three-state factor. For a split with \(t\equiv0\), the first split portion leaves \(\{1,2\}\) and the remainder does not collapse it. With \(t\equiv2\), the first split portion collapses \(\{1,2\}\) to a singleton. For \(t\equiv1\), the first split portion returns \(\{1,2\}\); the remaining rotation exponent is \(2\) if \(n\equiv1\) and \(0\) if \(n\equiv2\). Only exponent \(2\) gives a collapse. This proves exactly the stated filters. At least one split survives in each nondivisible case, including \(n=4,5\), since \((j,t)=(n-2,n-3)\) is eligible.

**Counting.** If \(n=3k+1\), there are \(3k-1\) choices of \(j\), \(2k\) eligible offsets and \(2k\) excluded diagonals \(t=j\), giving \(2k(3k-2)\). If \(n=3k+2\), there are \(3k\) choices of \(j\), \(k\) offsets and \(k\) excluded diagonals, giving \(k(3k-1)\). These yield the two formulas. \(\square\)

## Verification and scope
`python3 verify.py` performs breadth-first shortest-path counting on reachable subset pairs for \(3\le n\le16\), tests split candidates in the nondivisible cases through \(n=13\), and replays explicit witnesses through \(n=200\). The accompanying `verify_output.txt` records the run. Only the proof gives the statement for all \(n\). The count is for the specified shared-input pair, not independently chosen coordinate inputs, arbitrary second factors, or arbitrary synchronizing automata.

## Relationship to prior work
[1] establishes the threshold and witnesses but explicitly does not count all shortest words. [2] supplies the single-factor candidate family, not its intersection with the language of \(C_3\). [3] tabulates thresholds through \(n=11\), including the \(m=3\) slice. Fernau and Rystsov [4] establish general direct-product threshold bounds, not the count asserted here. These comparisons do not rule out an equivalent classification elsewhere.

## References
1. *A sharp modulo-three synchronization law for products of Černý automata*, [result](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-a-sharp-modulo-three-synchronization-law-for-products-of-ern-aut--eddab2697de1/RESULT.md).
2. *One-letter slack rigidity in the Černý reset language*, [result](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-one-letter-slack-rigidity-in-the-ern-reset-language--61d8f6568fe8/RESULT.md).
3. *Exact simultaneous reset thresholds for pairs of Černý automata through eleven states*, [result](https://github.com/Resultary/2026/tree/main/2026/10/13/SCOPE-exact-simultaneous-reset-thresholds-for-pairs-of-ern-automata-th--46765b03d598).
4. H. Fernau and I. Rystsov, *Shortest Synchronizing Words on Product Automata*, [arXiv:2611.09136v1](https://arxiv.org/abs/2611.09136).
