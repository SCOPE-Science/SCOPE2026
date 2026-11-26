# Exact shortest-common-supersequence counts and all extremizers for opposing two-run binary inputs

## Finding

For all integers \(a,b,c,d\ge1\), let
\[
U=0^a1^b,\qquad V=1^c0^d,\qquad N=a+b+c+d.
\]
Let \(S(a,b,c,d)\) denote the number of **distinct output words** of minimum length containing both \(U\) and \(V\) as scattered subsequences. Set \(r_0=\min(a,d)\), \(r_1=\min(b,c)\), and
\[
F_0=\begin{cases}
\binom{b+d-a}{b},&a\le d,\\
\binom{c+a-d}{c},&a>d,
\end{cases}\qquad
F_1=\begin{cases}
\binom{a+c-b}{a},&b\le c,\\
\binom{d+b-c}{d},&b>c.
\end{cases}
\]
Then the shortest common-supersequence length is \(N-\max(r_0,r_1)\), and its **exact distinct-output multiplicity** is
\[
\boxed{S(a,b,c,d)=\mathbf1_{r_0\ge r_1}F_0+\mathbf1_{r_1\ge r_0}F_1.}
\]
Both summands contribute when \(r_0=r_1\); their output sets are disjoint.

At every fixed total input length \(N\ge4\), the sharp maximum over positive integer quadruples is
\[
\boxed{\max_{a+b+c+d=N}S(a,b,c,d)
=\binom{N-2}{\lfloor(N-2)/2\rfloor}.}
\]
**Every maximizing quadruple** belongs to one of precisely two families:
\[
(a,c)=(1,1),\quad |b-d|\le1;
\qquad\text{or}\qquad
(b,d)=(1,1),\quad |a-c|\le1.
\]
For \(N=4\) the two families coincide, and for greater \(N\) they are disjoint. The maximum behaves as \(2^{N-2}\sqrt{2/(\pi(N-2))}\) asymptotically.

The pre-existing general SCS-multiplicity bound of Alon–Bourla–Graham–He–Kravitz implies the displayed universal upper bound at fixed \(N\). **The contribution claimed here is the full independent-four-parameter exact count and the exhaustive equality classification *within this opposite two-run family*, not a new unrestricted upper bound.**

## Assumptions and scope

Words are finite, linear, and binary, with all four run lengths strictly positive. A word \(U\) is a scattered subsequence of \(W\) when \(U\) is obtained from \(W\) by deleting zero or more positions without reordering the survivors. A shortest common supersequence (SCS) contains both input words as subsequences and has least possible output length. Different embeddings or alignment paths producing the same output word count **once**. A minimal common supersequence means deletion-minimal and may be longer than an SCS; **only shortest** common supersequences are counted here.

For any positive integers \(h,k\), \(\binom{h+k}{h}\) counts words with \(h\) copies of one specified letter and \(k\) of another. The inequalities and integer-valued indicators in the displayed formula use the original input parameters, not an implicit assumption of balanced runs.

## Proof

**1. Longest common subsequences and shortest length.** Every nonempty scattered subsequence shared by \(0^a1^b\) and \(1^c0^d\) is monochromatic: a shared mixed pattern would have to contain a zero before a one in the first input and a one before a zero in the second. Thus the only possible longest common subsequences are \(0^{r_0}\) and/or \(1^{r_1}\), and their maximum length is \(s=\max(r_0,r_1)\). Standard merging of embeddings yields SCS length \(N-s\): the concatenation of both inputs with \(s\) matched positions is an upper bound, and any pair of embeddings into a common output has at most \(s\) shared positions, giving the lower bound.

For each shortest output \(W\), choose embeddings of both inputs. Every output position must be used by at least one of these embeddings: an unused position could be removed, contradicting shortestness. Hence their intersection has exactly \(s\) positions, and spells a longest common subsequence. It is therefore entirely zeros or entirely ones. This yields two *possible* classes, with zeros shared only if \(r_0\ge r_1\), and ones shared only if \(r_1\ge r_0\).

**2. All shortest words whose alignment shares zeros.** In this class, the output has \(\max(a,d)\) zeros and exactly \(b+c\) ones. Suppose \(a\le d\). Since every one of the \(d\) output zeros is needed by \(V=1^c0^d\), the \(c\) ones needed by \(V\) must precede the first zero. The \(b\) ones needed by \(U=0^a1^b\) must follow the \(a\)-th zero. There are exactly \(b+c\) output ones, so none can occur in the first \(a\) zeros except the initial \(c\) ones. Each output consequently has the **unique** form
\[
1^c0^aX,\qquad X\in\operatorname{Shuffle}(0^{d-a},1^b),
\]
where \(\operatorname{Shuffle}\) here is the set of distinct binary words of the displayed letter multiplicities. Conversely each such word contains both inputs and has optimum length when \(r_0=s\). The number is \(\binom{b+d-a}{b}\).

If \(a>d\), all \(a\) output zeros serve \(U\), and the \(b\) output ones of \(U\) occur after the last zero. The \(c\) ones serving \(V\) must precede its last \(d\) zeros. Therefore the shortest outputs are exactly
\[
Y0^d1^b,\qquad Y\in\operatorname{Shuffle}(0^{a-d},1^c),
\]
numbering \(\binom{c+a-d}{c}\). The two cases establish \(F_0\).

**3. All shortest words whose alignment shares ones.** Applying the same argument with zeros and ones exchanged, and with the input order appropriately reversed, gives the explicit disjoint alternatives
\[
\begin{array}{ll}
Z1^b0^d,&Z\in\operatorname{Shuffle}(0^a,1^{c-b}),\quad b\le c,\\
0^a1^cT,&T\in\operatorname{Shuffle}(1^{b-c},0^d),\quad b>c.
\end{array}
\]
Their counts are respectively \(\binom{a+c-b}{a}\) and \(\binom{d+b-c}{d}\), giving \(F_1\). The zero-sharing class has \(b+c\) ones whereas the one-sharing class has \(\max(b,c)=b+c-r_1\) ones. Since \(r_1\ge1\), the classes cannot overlap. This proves the four-parameter exact formula, including ties and equality cases such as \(a=d\) or \(b=c\).

**4. Sharp maximum and all equality cases.** Write \(B(m)=\binom{m}{\lfloor m/2\rfloor}\), increasing strictly with \(m\). If \(r_0>r_1\), then \(r_0\ge2\), and only \(F_0\) contributes. Its binomial top index is \(N-(2r_0+\eta)\), where \(\eta=c\) for \(a\le d\) and \(\eta=b\) otherwise. Thus \(S\le B(N-5)<B(N-2)\). The case \(r_1>r_0\) is symmetric. If \(r_0=r_1\ge2\), both binomial tops are at most \(N-5\), so \(S\le2B(N-5)<B(N-2)\), since \(B(m+3)>2B(m)\) for all nonnegative \(m\) for which these cases occur (by Pascal's identity).

It remains that \(r_0=r_1=1\). The two conditions force one of the four boundary pairs \((a,c)=(1,1)\), \((b,d)=(1,1)\), \((a,b)=(1,1)\), or \((c,d)=(1,1)\). If \(a=c=1\), Pascal's identity in the formula gives
\[
S=\binom{b+d-1}{b}+\binom{b+d-1}{d}=\binom{b+d}{b}=\binom{N-2}{b}.
\]
Likewise if \(b=d=1\), \(S=\binom{a+c}{a}=\binom{N-2}{a}\). These equal \(B(N-2)\) precisely when the two free run lengths differ by at most one. In the remaining cases \((a,b)=(1,1)\) with \(c,d>1\), or \((c,d)=(1,1)\) with \(a,b>1\), the formula reduces to \(S=N-2<B(N-2)\) (here \(N\ge6\)). For \(N=4,5\), direct substitution in the now-proved formula shows that every optimizer still lies in the two stated families. This completes the equality classification.

**5. Asymptotic.** Stirling's formula gives \(B(N-2)\sim2^{N-2}\sqrt{2/(\pi(N-2))}\). This is a consequence, not a separate novelty assertion.

## Verification

The standalone Python 3 scripts in `verification/` use only the standard library. `check_literal.py` enumerates every binary candidate of the independently established shortest length, and tests both subsequence inclusions directly for all \(715\) positive quadruples of total input length \(4\) through \(13\), assessing \(655{,}464\) literal candidates. `check_dp.py` independently generates **distinct** shortest words from the classical two-string recursion, checks the claimed formula for all \(6^4=1{,}296\) parameter quadruples with each component at most six, then checks the sharp maximum and **complete equality-class membership** at every total input length \(4\) through \(54\). Both were executed successfully from the packaged source paths; their exact stdout is recorded as plain text. These finite checks corroborate the classification, while the all-length result is proved by the preceding reasoning.

## Relationship to prior work

Alon, Bourla, Graham, He and Kravitz (arXiv:2209.11882, 2026 revised version, Theorem 3) already establish a **general** binomial upper bound on SCS multiplicity for arbitrary words at specified lengths and LCS size. In our notation, with shared length \(s\), their theorem gives \(m_{\rm SCS}(U,V)\le\binom{N-2s}{a+b-s}\). As \(s\ge1\), this implies the bound \(B(N-2)\). Accordingly **neither that upper bound nor its binomial asymptotic alone is new here**. Their article does not state the complete four-run formula or characterize equality among these four-parameter input pairs.

Sopp, Liyanage, Gong and Zhu (arXiv:2603.22591, first posted 2026-03-23) supply general algorithms and a structural graph for *minimal* common supersequences. Shortest outputs are among the minimal ones, but their inspected full text does not enumerate distinct shortest outputs for four independent run lengths or classify the above equality cases.

Previously published exact spectra for \(0^m1^m\) versus \(1^m0^m\), and for \(0^a1^b\) versus \(1^b0^a\), imply the old special cases in which the mirrored blocks have matching run parameters: one shortest word when \(a\ne b\), and two when \(a=b\). These are expressly not claimed as new. Another exact binomial SCS count for repeated *permutation powers* concerns alternating runs and does not imply this statement for all independent block lengths. The present contribution resolves the unrestricted four-parameter opposing two-run family and the equality classification within it. An unindexed earlier closed formula remains a residual priority risk.

## Limitations

This is an exact classification for two **oppositely oriented single-transition binary** inputs with positive run lengths; it does not count minimal-but-longer common supersequences, SCS alignments/embeddings as separate objects, or pairs with three or more runs. The general upper bound and its asymptotic were previously known, and the result makes no claim to reprove them as novel unrestricted bounds. An older Fraser–Irving–Middendorf treatment of minimal supersequences was located bibliographically, but not verified by full-text inspection; this leaves residual historical priority uncertainty. Verification programs check finite instances and do not constitute independent review or replace the mathematical proof.

## References

1. B. Sopp, A. Liyanage, M. Gong and B. Zhu, *Computing and Enumerating Minimal Common Supersequences Between Two Strings*, arXiv:2603.22591v1, https://arxiv.org/html/2603.22591v1 (first publicly posted 2026-03-23).
2. N. Alon, G. Bourla, B. Graham, X. He and N. Kravitz, *Logarithmically larger deletion codes of all distances*, arXiv:2209.11882v3, https://arxiv.org/html/2209.11882v3 (first publicly posted 2022-09-23; cited revised version 2026-09-11).
3. *Exact minimal-supersequence spectra for unequal opposite binary runs*, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-minimal-supersequence-spectra-for-unequal-opposite-binary--d41f14eae316/RESULT.md (public result for a mirrored two-parameter specialization).
4. *Exact length spectrum of minimal common supersequences of opposite binary blocks*, https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-exact-length-spectrum-of-minimal-common-supersequences-of-opposi--10a0d52c68a3/RESULT.md (equal-block case).
5. *A binomial law for shortest common supersequences of opposite permutation powers*, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-a-binomial-law-for-shortest-common-supersequences-of-opposite-pe--980cf845dba3/RESULT.md (different alternating-pattern input family).
6. C. B. Fraser, R. W. Irving and M. Middendorf, *Maximal Common Subsequences and Minimal Common Supersequences*, *Information and Computation* 124(2) (1996), 145–153, DOI 10.1006/inco.1996.0011 (bibliographic record; complete text not inspected).
