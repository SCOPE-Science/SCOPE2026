# Exact first post-half rank compression in the even Černý automata

## Finding
For each integer \(m\ge3\), consider the \(2m\)-state Černý automaton with letters \(r:i\mapsto i+1\pmod{2m}\) and \(d:0\mapsto1\), with \(d\) fixing all other states. The minimum length of a word whose image has at most \(m-1\) states is exactly
\[
\boxed{\lambda_{2m}(m+1)=3m+3.}
\]
A shortest word is \(d r^3d(r^2d)^{m-2}r^3d\). This is the first deficiency beyond the known linear regime \(\lambda_{2m}(s)=3s-2\) for \(s\le m\).

## Assumptions and scope
Words act on the full state set \(Q=\mathbb Z/(2m)\mathbb Z\), from left to right. The rank of a word \(w\) is \(|Qw|\), and its deficiency is \(2m-|Qw|\). We assume \(m\ge3\). The claim is exactly about the first target deficiency \(m+1\) beyond the half-rank threshold, not about all later targets or uniqueness of the minimizing word. The convention \(d:0\mapsto1\) is cyclically conjugate to the standard \(b:(2m-1)\mapsto0\), so rank-length thresholds coincide.

## Proof
Write \(n=2m\) and \(s=m+1\). A letter \(d\) is *effective* if it reduces the cardinality of the current image. It is effective precisely when both \(0\) and \(1\) are present, and then it removes \(0\) from the image. The rotation \(r\) never changes the cardinality. Consequently at least \(s\) effective \(d\)'s are needed.

**Spacing lemma.** There must be at least two occurrences of \(r\) between successive effective \(d\)'s. Immediately after an effective \(d\), state \(0\) is absent. With no rotations, further \(d\)'s cannot be effective. After exactly one rotation, state \(1\) is absent. Any subsequent \(d\) with no additional rotation either acts as the identity (if \(0\) is absent) or replaces \(0\) by \(1\), making \(0\) absent. Thus no effective \(d\) can occur before the second rotation. This proves the elementary bound \(|w|\ge s+2(s-1)=3m+1\).

**The extra two letters are necessary.** Suppose a word reaches deficiency \(s\) in at most \(3m+2\) letters. Delete any prefix preceding its first effective \(d\) (the full state set is invariant under rotations), and truncate after its \(s\)-th effective \(d\). A shortest such word begins and ends with effective \(d\); its number \(R\) of rotations is at least \(2(s-1)=n\), and the number \(D\) of defect letters is at least \(s\). Since its length is at most \(3m+2=n+s+1\), either (i) \(D=s\) and \(R\in\{n,n+1\}\), or (ii) \(D=s+1\) and \(R=n\).

In (i), every \(d\) is effective. Let \(0=S_1<S_2<\cdots<S_s=R\) be the cumulative numbers of rotations immediately before the effective defect letters. As each effective \(d\) removes state \(0\), the holes just before the \(j\)-th effective \(d\) are exactly the residues \(S_j-S_i\pmod n\) for \(i<j\); no previously missing state is filled during an effective step. Effectiveness therefore requires \(S_j-S_i\not\equiv0,1\pmod n\) for all \(i<j\). At the last step, \(S_s-S_1=R\) equals \(n\) or \(n+1\), violating this condition.

In (ii), exactly \(n\) rotations occur. By the spacing lemma, the \(s-1\) intervals between successive effective \(d\)'s each contain exactly two rotations. The one non-effective \(d\) must lie inside one such interval; any defect letter before the first or after the last effective step would be removable. If it lies before the first rotation, it is the identity because \(0\) is absent. If it lies between the rotations, the first rotation leaves \(1\) absent; the non-effective \(d\) then either does nothing or changes the image by replacing \(0\) with \(1\), making \(0\) absent. In the first case, the extra letter is removable; in the second case, the second rotation leaves \(1\) absent, so the following \(d\) cannot be effective. If the extra \(d\) lies after the second rotation, an effective next \(d\) cannot follow it without another rotation unless the extra letter is the identity. Thus case (ii) is also impossible for a shortest word. We conclude \(\lambda_n(s)\ge n+s+2=3m+3\).

**Attainment.** Consider
\[
W_m=d r^3d(r^2d)^{m-2}r^3d.
\]
Its successive \(m+1\) defect letters occur after cumulative rotation counts
\[
0,3,5,7,\ldots,n-1,n+2.
\]
For any two of these counts in increasing order, their difference is neither \(0\) nor \(1\) modulo \(n\): internal differences are between \(2\) and \(n-1\), while differences from \(n+2\) are between \(3\) and \(n+2\), and the sole difference exceeding \(n\) is \(n+2\equiv2\pmod n\). By the hole criterion above, every \(d\) is effective. Thus \(W_m\) has deficiency \(m+1\) and length \((m+1)+(3+2(m-2)+3)=3m+3\), completing the proof.

## Verification
The standalone standard-library program `artifacts/verify.py` independently computes breadth-first search on image subsets for every even \(n\) from \(6\) to \(18\). It confirms thresholds \(12,15,18,21,24,27,30\) respectively. It also checks the displayed witness for every \(3\le m\le500\). These finite experiments are verification checks, not the proof of the unbounded theorem.

## Relationship to prior work
Pin's 1977 paper developed bounds for words of prescribed rank in finite automata. A published exact result on the Černý family establishes \(\lambda_n(s)=3s-2\) up to \(s\le\lceil n/2\rceil\), but explicitly leaves later deficiencies unclassified; the present theorem identifies the first boundary value outside that interval for every even state count. Rystsov's later work concerns rank properties and minimal-rank thresholds of Černý-type transformation monoids, rather than the first post-half intermediate rank. Related avoidance results maximize over prescribed forbidden subsets and do not directly give this minimum over all images. The novelty assessment is limited to the inspected sources and searches and does not claim that exhaustive historical priority has been established.

## Limitations
Only even state counts \(n\ge6\) and target deficiency \(n/2+1\) are covered. The formula does not classify all later rank thresholds, the number of minimizing words, or variants of the automaton. The source-inspection and index searches cannot rule out an unindexed older equivalent statement. Independent validation has not been conducted.

## References
1. J.-É. Pin, “Sur la longueur des mots de rang donné d'un automate fini,” *Comptes Rendus de l'Académie des Sciences, Paris*, 284 (16 May 1977), 1233–1235; HAL identifier `hal-00017720`.
2. “Exact early deficiency profile of the Černý automata,” published research record (2026): https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-early-deficiency-profile-of-the-ern-automata--766d362d36d3
3. A. Cherubini, A. Frigeri and L. Liu, “The effect of alphabet size on the synchronizing property of automata,” arXiv:1406.1413 (2014): https://arxiv.org/abs/1406.1413
4. I. Rystsov, “Cerny type automata and rank conjecture,” arXiv:2501.19166 (2025): https://arxiv.org/abs/2501.19166
