# A sharp all-length greedy reverse-complement superstring ratio for three binary reads

## Finding

Let \(k\ge3\). For a binary word \(u\), write \(\operatorname{rc}(u)\) for the reversal of its bitwise complement, and \([u]=\{u,\operatorname{rc}(u)\}\). For each set \(S\) of exactly three distinct such classes of \(k\)-letter words, let \(\operatorname{OPT}_{\rm rc}(S)\) be the shortest length of a binary word having, for every class of \(S\), at least one representative as a contiguous factor. Let \(G_{\rm rc}(S)\) be the **maximum** final length among all legal executions of maximum-overlap greedy reverse-complement merging, with ties resolved adversarially. Each merge may first reverse-complement either input and choose their order; the largest proper suffix-prefix overlap among the current oriented inputs is used, and already contained words may be discarded.

Then

\[
\max_{|S|=3}\frac{G_{\rm rc}(S)}{\operatorname{OPT}_{\rm rc}(S)}=\frac{2k}{k+2}.
\]

The lower bound is attained by \(S=\{[0^k],[0^{k-1}1],[10^{k-1}]\}\). Thus the worst ratio already tends to \(2\) with three reads, although no equality-case uniqueness claim for general \(k\) is made.

## Assumptions and scope

Words and complements are over the binary alphabet \(\{0,1\}\), with complement interchanging its two symbols. The three input reverse-complement orbits are pairwise distinct, and each initial representative has length exactly \(k\). An overlap of length zero is allowed only when no positive overlap exists; any occurrence of a shorter input in another current string can be removed without increasing the output. All claims are about the **worst possible** greedy tie-break, not average or best-case tie resolution.

## Proof

### 1. The generic length bound

Put \(L=\operatorname{OPT}_{\rm rc}(S)=k+d\). Three distinct classes cannot occur as the at most two length-\(k\) factors of a length-\(k+1\) word, so \(d\ge2\). Conversely, concatenating three reads gives \(L\le3k\), whence \(d\le2k\).

Choose one optimal host and three selected occurrences, one per class, in nondecreasing order of their start positions. Such starts are distinct. The overlaps between consecutive chosen length-\(k\) occurrences, measured as nonnegative suffix-prefix overlaps, sum to at least \(3k-L=2k-d\): if some chosen occurrences are disjoint, the intervening positive gaps reduce this sum, but an optimal host cannot have gaps between the three selected occurrences unless a shorter host is obtained by closing them. More formally, after discarding unused symbols at the ends, the union of the three intervals has length at most \(L\), while covering them in start order uses exactly \(3k\) symbols minus the two adjacent interval-overlap lengths, provided there is no uncovered gap; any gap would contradict optimality by deleting that gap. Because the three intervals have equal length and increasing starts, an overlap of the first and third intervals can only make the second adjacent overlap at least as large. Hence at least one consecutively ordered pair has overlap \(\ge k-\lfloor d/2\rfloor\). The first greedy overlap \(a\) is at least this large.

If \(b\ge0\) denotes the overlap in the second merge (or its effective reduction when a contained class is removed), the greedy final length satisfies

\[
G_{\rm rc}(S)\le3k-a-b\le 2k+\lfloor d/2\rfloor.
\]

For integers \(3\le d\le2k\) and \(k\ge3\), the function \((2k+\lfloor d/2\rfloor)/(k+d)\) is nonincreasing in \(d\). Its odd steps are strict; for the even step from \(2j-1\) to \(2j\), cross-multiplication reduces to \(j\le k\). Therefore

\[
\frac{G_{\rm rc}(S)}L\le\frac{2k+1}{k+3}\le\frac{2k}{k+2}
\qquad(d\ge3),
\]

where the last inequality is equivalent to \(k\ge2\). It remains to prove \(G_{\rm rc}(S)\le2k\) when \(d=2\).

### 2. The three-window endpoint lemma

Assume \(L=k+2\). The optimal host necessarily supplies exactly three length-\(k\) windows, each from a different reverse-complement class. Write

\[
H=h_0h_1\cdots h_{k+1},\quad
W_0=h_0\cdots h_{k-1},\quad
W_1=h_1\cdots h_k,\quad
W_2=h_2\cdots h_{k+1}.
\]

The first greedy overlap is precisely \(k-1\): consecutive windows attain it, while an overlap of \(k\) would imply equal reverse-complement classes. The first merged word \(C\) thus has length \(k+1\). We show that \(C\) and the unused window \(Z\) have at least one positive suffix-prefix overlap in some orientation and order. This implies \(G_{\rm rc}(S)\le(k+1)+k-1=2k\), unless \(Z\) is contained in \(C\), in which case the output is shorter.

**Endpoint fact.** If two nonempty binary words \(A,B\) admit no one-letter suffix-prefix overlap in either order or any independent reverse-complement orientations, then their first symbols are equal, both last symbols are equal, and the last symbol is the complement of the first. Indeed the possible last symbols of an oriented \(A\) are \(\{A_{\rm last},1-A_{\rm first}\}\), whereas the possible first symbols of an oriented \(B\) are \(\{B_{\rm first},1-B_{\rm last}\}\). Disjoint nonempty subsets of the two-symbol alphabet must each be singletons. Applying the same argument in reverse order gives the asserted endpoint configuration. In particular a word with equal first and last symbols cannot form such a zero-overlap pair.

To prove the claim, suppose for contradiction \(C\) and \(Z\) have no positive overlap, and apply this endpoint fact. Write \(\bar v=1-v\). Reverse-complementing the entire host and/or the candidate merge allows the chosen first pair to be ordered either \((W_0,W_1)\) or \((W_0,W_2)\), with each input independently either ordinary or reverse-complemented. There are eight cases. A merge of maximum overlap \(k-1\) imposes the following constraints, each incompatible with the endpoint fact or with the stipulated distinct classes.

**First pair \((W_0,W_1)\)** (remaining \(Z=W_2\)):

1. Ordinary / ordinary: the merged word is \(h_0\cdots h_k\), which overlaps \(W_2\) in \(k-1\) letters.
2. Reverse-complemented / ordinary: the overlap forces \(W_0=\operatorname{rc}(W_0)\), reducing to case 1.
3. Ordinary / reverse-complemented: matching the overlap gives \(h_t=\bar h_{k+1-t}\) for \(1\le t\le k-1\). The endpoint fact applied to \(C,W_2\) gives \(h_0=h_1=h_2\) and \(h_{k+1}=\bar h_2\). These relations give \(W_0=\operatorname{rc}(W_2)\), contradicting distinct classes.
4. Reverse-complemented / reverse-complemented: matching the overlap gives \(h_t=h_{t+2}\) for \(0\le t\le k-2\). The endpoint fact gives \(h_1=h_2\) and \(h_{k-1}=\bar h_2\). Period two and \(h_1=h_2\) force all \(h_0,\ldots,h_k\) equal, a contradiction.

**First pair \((W_0,W_2)\)** (remaining \(Z=W_1\)):

5. Ordinary / ordinary: matching the overlap forces \(h_1=\cdots=h_k\), hence \(W_1\) has equal endpoint symbols, contradicting the endpoint fact.
6. Ordinary / reverse-complemented: matching the overlap gives \(h_t=\bar h_{k+2-t}\) for \(1\le t\le k-1\). The endpoint fact forces \(h_0=h_1=h_2\) and \(h_k=\bar h_1\); together these imply \(W_1=\operatorname{rc}(W_2)\), a contradiction.
7. Reverse-complemented / ordinary: matching the overlap identifies the last \(k-1\) symbols of \(\operatorname{rc}(W_0)\) with those of \(W_1\). The endpoint fact identifies their first symbols, forcing \(W_1=\operatorname{rc}(W_0)\), a contradiction.
8. Reverse-complemented / reverse-complemented: matching the overlap gives \(h_t=h_{t+3}\) for \(0\le t\le k-2\). The endpoint fact gives \(h_1=h_2\), \(h_{k-1}=\bar h_1\), and \(h_k=\bar h_1\). By periodicity modulo three, if \(k\equiv0,2\pmod3\) then \(h_{k-1}=h_1\), and if \(k\equiv1\pmod3\) then \(h_k=h_1\), again a contradiction.

These exhaustive cases prove that a legal second merge overlaps positively, establishing the upper bound in the remaining case.

### 3. Sharpness for every length

Take the three distinct classes

\[
S_k=\{[0^k],[0^{k-1}1],[10^{k-1}]\}.
\]

The host \(10^k1\) contains representatives of all three classes in its three consecutive length-\(k\) windows, so \(\operatorname{OPT}_{\rm rc}(S_k)=k+2\). A first greedy merge may select \(\operatorname{rc}(0^{k-1}1)=01^{k-1}\) and \(\operatorname{rc}(10^{k-1})=1^{k-1}0\), overlapping their \(k-1\) consecutive ones. The resulting \(C=01^{k-1}0\) has length \(k+1\), and with the remaining \(0^k\) the largest overlap across both orders and all reverse-complement orientations is exactly one for every \(k\ge3\). Thus this legal greedy execution produces \(2k\) symbols, meeting the bound.

## Verification

The standalone `verification/three_rc_verifier.py` checks the all-three-input instance space for every \(k\) from \(3\) through \(7\), independently computing the exact optimum by oriented permutation search and the maximum greedy length by exhaustive tie recursion. It also enumerates all distinct-class length-\(k+2\) hosts and all legal first maximum-overlap merges for \(3\le k\le12\), testing that a one-symbol second overlap always exists; it checks the explicit sharpness witness through \(k=20\). The exact output is in `verification/three_rc_verifier.out`. No finite computation is used to justify the unbounded quantifiers; they are supplied by the proof above.

## Relationship to prior work

Yamano and Shibuya, *Approximation Ratios for the Shortest Common Superstring Problem with Reverse Complements*, arXiv:2601.15814 (first public January 22, 2026), analyze related orientation-aware greedy variants and motivate the special three-read comparison. Fici and coauthors, *On the Greedy Algorithm for the Shortest Common Superstring Problem with Reversals*, arXiv:1511.08431, establish a broad one-half compression guarantee for reversals, but do not state the sharp binary reverse-complement, exactly-three-read, equal-length ratio and exceptional length-\(k+2\) obstruction. A later 2026 update (arXiv:2611.16573) concerns different modified greedy algorithms and was only accessible in abstract. An existing exact binary four-mer ordinary input-set result gives the worst ratio at \(k=4\) but does not imply the all-length statement.

## Limitations

The theorem depends on the binary complement being fixed-point-free, exactly three classes, and the stated all-legal-tie greedy model. It does not establish the best-case greedy ratio, classify all extremal triples for arbitrary \(k\), or extend to larger collections or alphabets. The priority assessment is based on accessible full primary texts and published summaries; inaccessible or unindexed equivalent statements are not excluded.

## References

1. S. Yamano and T. Shibuya, *Approximation Ratios for the Shortest Common Superstring Problem with Reverse Complements*, arXiv:2601.15814 (2026), https://arxiv.org/abs/2601.15814 ; open proceedings https://drops.dagstuhl.de/storage/00lipics/lipics-vol369-cpm2026/html/LIPIcs.CPM.2026.15/LIPIcs.CPM.2026.15.html.
2. G. Fici, T. Kociumaka, J. Radoszewski, W. Rytter, T. Waleń, *On the Greedy Algorithm for the Shortest Common Superstring Problem with Reversals*, arXiv:1511.08431 (2015), https://arxiv.org/pdf/1511.08431.
3. S. Yamano and T. Shibuya, updated related algorithms manuscript, arXiv:2611.16573 (2026), https://arxiv.org/abs/2611.16573 (abstract inspected; full text unavailable).
