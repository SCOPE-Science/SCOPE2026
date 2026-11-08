# Complete minimal absent-word language of the Narayana morphic fixed point

## Finding
Let \(\Sigma=\{0,1,2\}\), let \(\nu(0)=01\), \(\nu(1)=2\), \(\nu(2)=0\), and let \(\mathbf n=\nu^\omega(0)\). A *minimal absent word* (MAW) is a word over \(\Sigma\) absent from \(\mathbf n\) although every proper contiguous factor occurs.

Here is a complete recursive description of the MAW language. Put \(u_1=0\), and, for each \(j\ge1\), put
\[
u_{j+1}=\begin{cases}\nu(u_j)&j\text{ odd},\\\nu(u_j)0&j\text{ even}.\end{cases}
\]
Define \(R_j=\{0,1\}\) when \(j\) is odd and \(R_j=\{0,2\}\) when \(j\) is even. Define a sequence of sets of ordered letter pairs by
\[
E_1=\{(0,1),(1,1),(2,0),(2,1)\}.
\]
Let \(\pi(0)=1,\ \pi(1)=2,\ \pi(2)=0\). For odd \(j\), set
\[
E_{j+1}=\{(\pi(a),f(b)):(a,b)\in E_j\},\qquad f(0)=0,\ f(1)=2.
\]
For even \(j\), set
\[
E_{j+1}=\{(\pi(a),g(b)):(a,b)\in E_j\},\qquad g(0)=1,\ g(2)=0.
\]
Then **all** the minimal absent words are precisely
\[
\boxed{\{02,11,21,22\}\ \cup\ \bigcup_{j\ge1}\{a u_j b:a\in\Sigma,\ b\in R_j,\ (a,b)\notin E_j\}.}
\]
There are exactly four MAWs of length two, exactly two of length \(|u_j|+2\) for each \(j\ge1\), and none of any other length. The first lengths with two MAWs are \(3,4,6,8,12,17,25,36,53,77,113,\ldots\). The recurrence is an effective complete antidictionary, not just a count formula.

## Assumptions and scope
The fixed point is a one-sided infinite word; occurrence means a contiguous finite factor at any nonnegative position. Its factor language is recurrent (the substitution is primitive); in particular, whenever a factor occurs, it also occurs with a preceding and a following letter. Every assertion ranges over all finite words on the explicitly stated three-letter alphabet, not just words of bounded length. Distinct MAWs are counted as words, not occurrences. No assumption on a finite substitution-iterate boundary is made.

## Proof
**1. Short contexts and synchronization.** Direct substitution gives the exact length-two and length-three factor sets
\[
\mathcal F_2=\{00,01,10,12,20\},\qquad
T=\mathcal F_3=\{001,010,012,101,120,200,201\}.
\]
For completeness, all seven members of \(T\) occur in \(\nu^6(0)\). For every \(t\in T\), every length-three factor of \(\nu(t)\) again belongs to \(T\), as verified directly from the seven displayed triples. Since every image of a letter is nonempty, each length-three factor of an image of a sufficiently long word is contained in the image of three consecutive original letters. Induction from finite iterates proves \(\mathcal F_3\subseteq T\); the exhibited occurrences give equality. Its length-two projections give \(\mathcal F_2\).

In particular every \(2\) is followed by \(0\), and the factor \(01\) only occurs as the entire image \(\nu(0)\): it cannot cross an image boundary, since the first letter of every letter image is \(0\) or \(2\), never \(1\). Consequently, every occurrence of a factor beginning with \(01\) starts at a letter-image boundary. The last letters of images of \(0,1,2\) are respectively \(1,2,0\), namely the permutation \(\pi\).

**2. All right-special prefixes.** Write \(R(v)=\{b\in\Sigma:vb\in\mathcal F(\mathbf n)\}\). The prefix \(0\) has \(R(0)=\{0,1\}\). Every prefix \(p\) of length at least two begins with \(01\), so the synchronization just proved allows a unique desubstitution at the left end.

If \(p\) ends in \(1\) or \(2\), it is exactly \(\nu(q)\) for a nonempty shorter prefix \(q\), and
\[
R(p)=\{h(b):b\in R(q)\},\qquad h(0)=h(2)=0,\ h(1)=2.
\]
If \(p\) ends in \(0\), it is exactly \(\nu(q)0\) for a shorter prefix \(q\), possibly empty. The next letter is \(1\) when the final \(0\) is the first letter of \(\nu(0)=01\), and is \(0\) when the final \(0\) is \(\nu(2)\): in the latter case the following parent letter is necessarily \(0\), because \(20\) is the only digram beginning with \(2\). Thus
\[
R(p)=\{1:0\in R(q)\}\cup\{0:2\in R(q)\}.
\]
The formula also holds for the initial prefix \(p=0\) with \(q\) empty, whose right-extension set is the entire alphabet.

Induction on prefix length now proves that its nonempty right-special prefixes are *exactly* \(u_j\). They have \(R(u_j)=R_j\), and the final letter of \(u_j\) alternates between \(0\) (odd \(j\)) and \(1\) (even \(j\)). Indeed, a right-special prefix ending in \(1\) is the image of a shorter right-special prefix ending in \(0\), with right extensions \(\{0,1\}\); its new right extensions are \(\{0,2\}\). A right-special prefix ending in \(0\), other than \(0\) itself, must be \(\nu(q)0\) for a shorter right-special prefix with extensions \(\{0,2\}\); its new extensions are \(\{0,1\}\). No prefix ending in \(2\) is right-special because a parent prefix ending in \(1\) can only be followed by \(0\) or \(2\), both mapped to initial symbol \(0\). The recursion is exhaustive and each successive prefix is longer.

**3. Left special factors.** The Narayana word is the simple-Parry fixed point with expansion parameter \((t_1,t_2,t_3)=(1,0,1)\). The cited results of Frougny, Masáková and Pelantová (2004, Theorem 3.9 and Corollary 4.11), also summarized by Bernat, Masáková and Pelantová (2007, section 3), establish that every prefix has precisely three left extensions, that there is only one infinite left-special branch, and that there are no maximal left-special factors in the final-digit-one case. Therefore **the left-special factors are exactly the prefixes**: otherwise a nonprefix left-special factor, having no maximal right extension among left-special factors, would extend along an infinite left-special branch different from the unique one. This also follows from the affine complexity \(2n+1\) and the fact that the prefix alone contributes the full complexity increment two.

It follows that the nonempty bispecial factors are precisely the \(u_j\), each with left-extension set \(\Sigma\) and right-extension set \(R_j\).

**4. Exact joint extension graphs.** Define
\[
\widetilde E_j=\{(a,b)\in\Sigma\times R_j:a u_j b\text{ is a factor of }\mathbf n\}.
\]
From \(\mathcal F_3=T\), \(\widetilde E_1=E_1\), with four members. If \(j\) is odd, \(u_{j+1}=\nu(u_j)\), which starts with synchronized \(01\). For any occurrence of \(a u_j b\), its image provides the left letter \(\pi(a)\), the core \(\nu(u_j)\) and right letter \(h(b)\), which on \(R_j=\{0,1\}\) is exactly \(f(b)\). Conversely, every occurrence of the synchronized longer core desubstitutes to a parent context, so no other edges exist.

If \(j\) is even, \(u_{j+1}=\nu(u_j)0\). If the old next letter is \(0\), the added \(0\) is followed by \(1\). If it is \(2\), the added \(0\) is a complete image \(\nu(2)\), followed by \(0\) since \(2\) is always followed by \(0\) in the parent word. Hence its right letter is \(g(b)\). The left letter is again \(\pi(a)\); synchronized desubstitution gives the converse. This proves \(\widetilde E_j=E_j\) for every \(j\), by induction. Each update acts bijectively on \(\Sigma\times R_j\), so every \(E_j\) has precisely four edges among six possible ones.

**5. Minimal absence and exhaustion.** For length two, the missing digrams are precisely \(02,11,21,22\), all minimal since the three letters occur. For any absent word \(a v b\) of length at least three whose prefix \(av\) and suffix \(vb\) occur, recurrence supplies interior occurrences of these shorter factors. Since \(avb\) is absent, some other letter precedes \(vb\) and some other letter follows \(av\); therefore \(v\) is both left-special and right-special. By steps 2–3, \(v=u_j\) for some \(j\). The corresponding possible left and right letters are exactly \(\Sigma\) and \(R_j\), while the occurring joint contexts are exactly \(E_j\). Each of the two missing edges therefore defines a MAW, and every MAW has been listed. The length-two and nonempty-core cases are disjoint, completing the proof.

## Verification
The standalone Python file `verify_narayana_maw.py` constructs substitution iterates 25 and 26, checks that their observed factor sets agree for lengths 1 through 40, and independently enumerates every absent word with occurring proper prefix and suffix for lengths 2 through 40. It compares these literal sets with the recursive formula, including the base trigram set and the two missing edges per special length. The actual replay passed, finding twenty MAWs in this finite test range; an additional direct scan checked thirteen successive joint-extension graphs up to core length 240. Such finite-prefix stabilization does **not** establish stabilization for every length or prove the infinite statement; the full proof above provides the infinite argument.

## Relationship to prior work
Shallit's *The Narayana Morphism and Related Words* (first public March 2, 2025), sections 5.3–5.5, gives the affine factor complexity, the palindrome spectrum, and the number of right-special factors at each length. Frougny, Masáková and Pelantová (2004) establish strong structural properties of left-special factors for the corresponding Parry substitution. Bernat, Masáková and Pelantová (2007) give an affine-complexity characterization. None of those inspected statements enumerates the language's minimal absent words or its two missing bidirectional contexts at each exceptional length. Their results are important premises, not an assertion that this antidictionary follows verbatim from a published table. No exhaustive historical-priority claim is made.

## Limitations
The theorem applies to the infinite three-letter Narayana fixed point with the stated morphism, not arbitrary ternary morphic words, other beta substitutions, or the minimal absent words of a fixed finite iterate. The checker is finite corroboration only. Historical priority remains subject to unindexed and not fully accessible sources; no independent mathematical audit has been performed.

## References
- J. Shallit, *The Narayana Morphism and Related Words*, arXiv:2503.01026 (first version March 2, 2025), https://arxiv.org/abs/2503.01026 .
- C. Frougny, Z. Masáková and E. Pelantová, *Complexity of infinite words associated with beta-expansions*, RAIRO Theoretical Informatics and Applications 38 (2004), 163–185, https://doi.org/10.1051/ita:2004009 ; OA https://www.numdam.org/article/ITA_2004__38_2_163_0.pdf .
- J. Bernat, Z. Masáková and E. Pelantová, *On a class of infinite words with affine factor complexity*, Theoretical Computer Science 389 (2007), 12–25, arXiv:math/0612466, https://arxiv.org/abs/math/0612466 .
