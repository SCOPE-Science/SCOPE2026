# Algebraic edge laws and a two-to-one height-layer split in ballot-prefix deletion reconstruction

## Finding
For every integer \(n\geq0\), let \(\mathcal B_n\) be the binary ballot prefixes of length \(n\): words over \(\{U,D\}\), with \(U\) interpreted as a rise of one and \(D\) as a fall of one, whose heights at every prefix are nonnegative. Form a simple undirected graph \(G_n\) on \(\mathcal B_n\) by joining distinct words precisely when their sets of distinct single-deletion outputs have at least two elements in common.

Let \(e_n^{=}\) count edges joining words with equal numbers of rises, and \(e_n^{\ne}\) count edges joining words with different numbers of rises. Write
\[
C(u)=\sum_{j\geq0}\frac{1}{j+1}\binom{2j}{j}u^j=\frac{1-\sqrt{1-4u}}{2u},\quad T(z)=zC(z^2).
\]
The following exact algebraic generating functions hold as formal power series:
\[
E_{=}(z)=\sum_{n\geq0}e_n^{=}z^n=
\frac{z^2C(z^2)T(z)(1+T(z)-T(z)^2)}{(1-z^2)(1-2z)(1-T(z)^2)},
\]
\[
E_{\ne}(z)=\sum_{n\geq0}e_n^{\ne}z^n=
\frac{z^3C(z^2)T(z)}{(1-z^2)(1-2z)(1-T(z)^2)}.
\]
Every edge in the second class joins adjacent rise-count layers (equivalently the final altitudes differ by exactly two). Moreover, as \(n\to\infty\),
\[
e_n^{=}\sim \frac{2}{3}\,2^n\sqrt{\frac{n}{2\pi}},\qquad
 e_n^{\ne}\sim \frac{1}{3}\,2^n\sqrt{\frac{n}{2\pi}},
\qquad |E(G_n)|=2^n\sqrt{\frac{n}{2\pi}}+O(2^n).
\]
Since \(|\mathcal B_n|=\binom{n}{\lfloor n/2\rfloor}\), the average degree satisfies \(2|E(G_n)|/|\mathcal B_n|\sim n\). Asymptotically two thirds of confusable pairs preserve the final height, while one third bridge consecutive height layers.

## Assumptions and scope
Deletion outputs are **distinct words**, not deletion indices counted with multiplicity. There is no condition on the final altitude, apart from nonnegativity of all prefix heights. The empty ballot word is included at \(n=0\), but there are no graph edges until \(n=3\). Adjacent graph vertices are different original words and need not have the same number of rises. All formulas use ordinary, not exponential, generating functions.

## Proof
**1. Unique alternating-interval model.** The standard two-read single-deletion intersection characterization shows that two different binary words have at least two distinct common single-deletion outputs exactly when they coincide before and after one *nonempty alternating mismatch interval* of length at least two, on which they are opposite binary phases. The interval is the unique span from their first differing coordinate to their last differing coordinate. For completeness, write the two words on that interval as \(a_1\cdots a_\ell\) and \(b_1\cdots b_\ell\). The two different common deletion strings arise from deleting, respectively, the left endpoint in the first word and the right endpoint in the second, and vice versa. These two equalities force \(b_i=a_{i+1}=a_{i-1}\) where indices exist, while distinctness forces \(a_1\ne a_2\); thus the first word alternates, and the second has opposite letters throughout. Conversely, deleting the respective opposite interval endpoints yields two distinct common words whenever the interval is alternating. The same first/last-difference argument proves uniqueness of this interval. The general intersection bound of two is known, but only the preceding explicit binary characterization is needed here.

For a pair of ballot words, orient the interval so that the marked word begins it with \(D\). The other word then begins it with \(U\), and flipping the marked factor from \(DUDU\cdots\) to \(UDUD\cdots\) raises every odd intermediate height by two. At even intermediate positions the heights agree; after an odd-length factor, the other word's final height and all subsequent heights are raised by two. Thus the other word is ballot automatically. The marked word must enter the factor at height \(h\geq1\). Conversely each occurrence of a length-at-least-two alternating factor beginning with \(D\) in a ballot word yields exactly one edge; the unique first-to-last mismatch span makes this a bijection, with no multiple counting. An even factor has length \(2m\) and returns to height \(h\); an odd factor has length \(2m+1\) and ends at \(h-1\), for \(m\geq1\). These are exactly the equal-rise and unequal-rise classes, respectively.

**2. Prefix and suffix languages.** Let \(P_h(z)\) enumerate ballot prefixes ending at height \(h\geq0\), by their number of steps. The unique decomposition into \(h+1\) Dyck excursions separated by \(h\) unmatched up-steps gives
\[
P_h(z)=z^h C(z^2)^{h+1}=C(z^2)T(z)^h.
\]
Let \(F_h(z)\) enumerate all suffixes starting at height \(h\) that never fall below zero. Among all binary continuations, whose generating function is \((1-2z)^{-1}\), those first reaching altitude \(-1\) have a unique initial first-passage prefix consisting of \(h+1\) record down-steps each preceded by a Dyck excursion. Its generating function is \(T(z)^{h+1}\). The remainder is unconstrained. Therefore
\[
F_h(z)=\frac{1-T(z)^{h+1}}{1-2z}.
\]
This identity is also valid for \(h=0\), and it is an identity of formal power series.

**3. Exact edge generating functions.** Mark an edge by its \(D\)-first alternating factor in its unique ballot representative. Even factors have total length-generating series \(z^2/(1-z^2)\); odd factors have \(z^3/(1-z^2)\). Free valid prefixes and suffixes therefore give
\[
E_{=}(z)=\frac{z^2}{1-z^2}\sum_{h\geq1}P_h(z)F_h(z),
\qquad E_{\ne}(z)=\frac{z^3}{1-z^2}\sum_{h\geq1}P_h(z)F_{h-1}(z).
\]
Substituting the prefix/suffix identities and summing the geometric series yields
\[
\sum_{h\geq1}P_hF_h=\frac{C(z^2)}{1-2z}\left(\frac{T}{1-T}-\frac{T^3}{1-T^2}\right)
=\frac{C(z^2)T(1+T-T^2)}{(1-2z)(1-T^2)},
\]
\[
\sum_{h\geq1}P_hF_{h-1}=\frac{C(z^2)}{1-2z}\left(\frac{T}{1-T}-\frac{T^2}{1-T^2}\right)
=\frac{C(z^2)T}{(1-2z)(1-T^2)}.
\]
This proves the two claimed algebraic generating functions for every \(n\).

**4. Asymptotics and layers.** Put \(\epsilon=1-2z\). Along the real radius at the dominant positive singularity, \(T(z)=1-\sqrt{2\epsilon}+O(\epsilon)\) and \(C(z^2)=2+O(\sqrt\epsilon)\). Consequently the local leading terms are
\[
E_{=}(z)\sim \frac{1}{3\sqrt2}\epsilon^{-3/2},\qquad
E_{\ne}(z)\sim \frac{1}{6\sqrt2}\epsilon^{-3/2}.
\]
These algebraic functions are analytic inside \(|z|<1/2\); the only other singularity on the circle is \(z=-1/2\), where the growth is at most \(O((1+2z)^{-1/2})\), contributing a lower-order coefficient. Standard algebraic singularity transfer therefore gives the asserted asymptotics, with remainder \(O(2^n)\) for the total. Summing \(P_h\) over final heights shows \(|\mathcal B_n|=\binom n{\lfloor n/2\rfloor}\). Stirling's formula then yields average degree asymptotic to \(n\). The ratio of edge types tends to \(2:1\).

## Verification
The standalone `verification.py` reproduces three genuinely distinct routes to finite coefficients: (i) direct enumeration of all ballot words and pairwise intersections of distinct one-deletion output sets for \(2\leq n\leq10\); (ii) a state-based recurrence that accumulates all \(D\)-starting alternating factors for lengths through \(60\); and (iii) exact integer arithmetic on the two algebraic formal power series through length \(60\). These agree in both edge classes. Coefficients at lengths \(n=3,4,5,6,7,8,9,10\) are, respectively,
\[
(1,0),\ (3,1),\ (9,2),\ (23,8),\ (54,16),\ (128,46),\ (278,92),\ (632,233),
\]
where each ordered pair gives \((e_n^{=},e_n^{\ne})\). Finite tests corroborate but do not replace the all-length proof or establish originality.

## Relationship to prior work
Cai, Kiah, Nguyen and Yaakobi develop the general single-deletion two-read confusability criterion, whose alternating-interval mechanism is used here. Niederhausen and Sullivan enumerate ballot paths **avoiding a fixed depth-zero pattern**, not the graph defined by simultaneous read collisions across all alternating factor lengths. Manes, Sapounakis, Tasoulas and Tsikouras study ballot-path equivalence by **positions of occurrences of a selected short pattern**; this is not an equality-of-deletion-output condition. Earlier work by Sapounakis, Tasoulas and Tsikouras and by Manes and collaborators counts fixed-pattern occurrences in Dyck paths. Such techniques are relevant but do not directly imply the unrestricted-final-height graph edge split or the two-thirds/one-third asymptotic law without the new boundary-respecting marked-interval enumeration. No priority claim is made for the basic deletion criterion, Catalan path decomposition, or general analytic transfer.

## Limitations
Only the total number of confusable pairs, split by whether the final height changes, is determined. The theorem does not enumerate individual degree distributions, largest independent sets or the exact maximum reconstruction codebook, and it does not refine counts by a prescribed final height. The first-passage derivation works for ballot prefixes at boundary zero and binary single deletions; other path constraints and error channels require separate proofs. An earlier unindexed edge-count interpretation or a stronger result hidden within historical pattern-count literature remains possible; no independent mathematical audit has been performed.

## References
- H. Niederhausen and S. Sullivan, *Ballot Paths Avoiding Depth Zero Patterns*, arXiv:1004.2710v1, first posted 15 April 2010. https://arxiv.org/abs/1004.2710
- K. Manes, A. Sapounakis, I. Tasoulas and P. Tsikouras, *Equivalence classes of ballot paths modulo strings of length 2 and 3*, arXiv:1510.01952v1, first posted 7 October 2015. https://arxiv.org/abs/1510.01952
- K. Cai, H. M. Kiah, T. T. Nguyen and E. Yaakobi, *Coding for Sequence Reconstruction for Single Edits*, arXiv:2001.01376, first posted 6 January 2020. https://arxiv.org/abs/2001.01376
- K. Manes, A. Sapounakis, I. Tasoulas and P. Tsikouras, *General Results on the Enumeration of Strings in Dyck Paths*, Electronic Journal of Combinatorics 18(1), P74 (2011). https://doi.org/10.37236/561
- A. Sapounakis, I. Tasoulas and P. Tsikouras, *Counting strings in Dyck paths*, Discrete Mathematics 307 (2007), 2909–2924. https://doi.org/10.1016/j.disc.2007.03.005
