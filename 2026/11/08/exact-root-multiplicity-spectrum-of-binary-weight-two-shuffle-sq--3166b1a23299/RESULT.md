# Exact root-multiplicity spectrum of binary weight-two shuffle squares

## Finding
For every integer \(m\ge1\), let \(\mathcal W_m\) be the set of length-\(2m\) binary words containing exactly two ones. A *shuffle root* of \(w\in\mathcal W_m\) is a length-\(m\) word \(u\) such that the symbols of \(w\) can be assigned to two disjoint increasing subsequences, both spelling \(u\). Let \(R(w)\) be the number of **distinct words** \(u\) satisfying this condition; assignments producing the same root are not counted separately.

Every \(w\in\mathcal W_m\) has a unique gap representation \(w=0^a1\,0^b1\,0^c\), with \(a,b,c\ge0\) and \(a+b+c=2m-2\). The precise root count is
\[
R(w)=\max\{0,U-L+1\},\quad
L=\max\left\{\left\lceil\frac a2\right\rceil,a+b-m+1\right\},\quad
U=\min\left\{a,\left\lfloor\frac{a+b}{2}\right\rfloor,m-1\right\}.
\]
More strongly, for every integer \(r\ge1\), put \(h=m-3(r-1)\). The **exact root-multiplicity tail spectrum** is
\[
\#\{w\in\mathcal W_m:R(w)\ge r\}=
\begin{cases}
1+3\binom h2,&h\ge1,\\
0,&h\le0.
\end{cases}
\]
Consequently \(\max_{w\in\mathcal W_m}R(w)=\lfloor(m+2)/3\rfloor\), and the exact number with \(r\) roots is the difference between two successive displayed tail counts. In particular, when \(1\le r<\lfloor(m+2)/3\rfloor\), that number is \(9(m-3r+1)\); the highest-multiplicity class has respectively \(1,4,10\) members as \(m\) is respectively congruent to \(1,2,0\) modulo \(3\). The zero-root count is \(\binom{2m}{2}-1-3\binom m2\).

If \(W_m\) is uniformly sampled from \(\mathcal W_m\), then \(R(W_m)/m\) converges in distribution to a nonnegative law with atom \(1/4\) at zero and density \(\frac92(1-3t)\) on \(0<t<1/3\) (zero elsewhere). Its mean is \(1/12\). Here the \(r=1\) count \(1+3\binom m2\) is **previously known**; the root-number formula, all \(r\ge2\) tail counts, and limiting root-multiplicity law are the contributions claimed here.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\), with indexed words of length \(2m\), exactly two ones, and \(m\ge1\). Self-shuffling preserves the internal order of each copy and counts distinct roots, not colorings or interleavings. No statement is made for arbitrary Hamming weight or all binary shuffle squares.

## Proof
Every possible root contains exactly one one, so it is uniquely \(u_k=0^k1\,0^{m-1-k}\) for \(0\le k\le m-1\). To test \(u_k\), assign the first one of \(w\) to copy A and the second to copy B; exchanging the copy names does not change a root. Assign exactly \(k\) of the first \(a\) zeros to A. This requires \(k\le a\), and B's remaining \(a-k\) early zeros must not exceed its required \(k\), so \(2k\ge a\). Before the second one, B needs exactly \(2k-a\) zeros from the middle block, forcing \(2k\le a+b\). Then A has received \(a+b-2k\) zeros after its one; that must be at most its total allowance \(m-1-k\), equivalently \(k\ge a+b-m+1\). Conversely these inequalities, together with \(k\le m-1\), permit allocating the remaining middle and final zeros to complete both copies. This proves the integer interval \(L\le k\le U\) and the root-count formula, including boundary cases \(a=0\), \(b=0\), or \(c=0\).

Let \(t=r-1\ge0\). The condition \(R(w)\ge r\) is exactly \(L+t\le U\). Comparing each of the two lower bounds with each of the three upper bounds gives the following equivalent four conditions:
\[
a\ge2t,\qquad c\ge2t,\qquad b\ge2t+(a\bmod2),\qquad b\le m-1-t.
\]
For completeness, the nontrivial comparisons are \(\lceil a/2\rceil+t\le a\iff a\ge2t\), \(\lceil a/2\rceil+t\le\lfloor(a+b)/2\rfloor\iff b\ge2t+(a\bmod2)\), \(a+b-m+1+t\le a\iff b\le m-1-t\), and \(a+b-m+1+t\le\lfloor(a+b)/2\rfloor\iff c\ge2t\). The two remaining comparisons are implied by \(a\ge2t\) and \(c\ge2t\) together with \(a+b+c=2m-2\).

Subtracting \(2t\) from **each** of the three zero gaps maps these four conditions bijectively to the conditions for at least one root in \(\mathcal W_{m-3t}\): the transformed gaps are nonnegative, their sum is \(2(m-3t)-2\), and they satisfy \(b'\ge (a'\bmod2)\) and \(b'\le(m-3t)-1\). If \(m-3t\le0\) the set is empty. Thus the \(r\)-root tail is in bijection with the one-root existence set at shorter half-length \(h=m-3t\).

For \(h\ge1\), we independently count the latter set: at middle gap \(b'=0\), only even \(a'\) work, giving \(h\) words. For every integer \(1\le b'\le h-1\), there are \(2h-1-b'\) possible values of \(a'\), the final gap being forced. Summing gives \(h+\sum_{b'=1}^{h-1}(2h-1-b')=1+3\binom h2\). This also recovers (without claiming priority over) the published total number of weight-two shuffle squares. Substituting \(h=m-3(r-1)\) proves the tail formula. Taking differences yields the multiplicities, and the largest nonempty tail occurs at \(r=\lfloor(m+2)/3\rfloor\).

For the limit law, \(\#\mathcal W_m=\binom{2m}{2}\). For any fixed \(0<t<1/3\), the preceding tail formula at \(r=\lfloor mt\rfloor+1\) yields
\[
\Pr\{R(W_m)/m>t\}\longrightarrow\frac34(1-3t)^2.
\]
For \(t=0\) the same limit is \(3/4\), and for \(t\ge1/3\) it is zero. The limiting distribution therefore has atom \(1/4\) at zero and the asserted density on its continuous part; integrating the survival function gives \(\int_0^{1/3}\frac34(1-3t)^2\,dt=1/12\). The endpoint limits establish weak convergence.

## Verification
The included standalone `verify_shuffle_roots.py` independently tests root membership using memoized two-copy interleaving dynamic programming (not the gap inequalities). It enumerates all \(946\) two-one words for half-lengths \(1\) through \(11\), checks every root count and the exact root threshold conditions, and then independently checks the tail counts by direct gap enumeration for half-lengths \(12\) through \(64\). The actual execution returned `VERIFY_OK direct_words=946 direct_root_memberships=1001 max_roots_tested=4 lengths=1..64`. Finite tests are supporting checks, not substitutes for the all-length proof above.

## Relationship to prior work
Buss and Soltys (2012, arXiv:1211.7161) established computational hardness of recognizing shuffle squares in general. Grytczuk, Pawlik and Pleszczyński (2023, arXiv:2308.13882, §2.4, Theorem 3 and Corollary 1) gave the **existing** characterization and the formula \(1+3\binom m2\) for the total number of weight-two binary shuffle-square words; the present theorem does not claim that formula as novel. Datko and Pawlik (2025, DOI:10.3390/sym17020305, §§2–3) studied generation counts from specified roots, the existence of multiply rooted words and some uniquely rooted families, but did not state the all-length root-multiplicity tail law in the inspected material. Grytczuk, Pawlik and Ruciński (2025, arXiv:2503.22043, Propositions 1–3 and 6) investigated existence of shuffle decompositions using nest-free graph representations, including five-run recognition, not the number of distinct root words in this two-one class. This work refines the previously known \(r=1\) existence enumeration to the complete distribution of root multiplicities.

## Limitations
The theorem is restricted to words with exactly two ones. It counts different roots, not the potentially many distinct two-color interleavings realizing each root. The asymptotic distribution refers to the uniform measure on all indexed two-one words (including non-shuffle-squares); it does not assert a distribution for unrestricted random binary words. No independent external mathematical validation has been performed. Although directly relevant published statements and indexed research records were compared, unindexed equivalent prior results cannot be excluded.

## References
1. S. Buss and M. Soltys, *Unshuffling a Square is NP-Hard*, first public arXiv posting 2012-11-30, https://arxiv.org/abs/1211.7161.
2. J. Grytczuk, B. Pawlik and M. Pleszczyński, *Variations on shuffle squares*, arXiv:2308.13882 (first posted 2023-08-26), https://arxiv.org/abs/2308.13882, especially Theorem 3 and Corollary 1.
3. D. Datko and B. Pawlik, *Roots of Binary Shuffle Squares*, *Symmetry* 17(2), 305 (2025), https://doi.org/10.3390/sym17020305, especially Propositions 1–3 and Theorem 2.
4. J. Grytczuk, B. Pawlik and A. Ruciński, *Shuffle squares and nest-free graphs*, arXiv:2503.22043 (first posted 2025-03-27), https://arxiv.org/abs/2503.22043, especially Propositions 1, 2 and 6.
