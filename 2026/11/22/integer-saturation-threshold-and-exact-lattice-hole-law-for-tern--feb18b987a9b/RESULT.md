# Integer saturation threshold and exact lattice-hole law for ternary two-decks

## Finding
Let \(a,b,c\ge1\), and let \(\mathcal D_{a,b,c}\subset\mathbb Z^3\) comprise all triples \((x,y,z)\) of scattered-pair counts
\[
x=\binom{w}{01},\qquad y=\binom{w}{02},\qquad z=\binom{w}{12}
\]
for ternary words \(w\) with exactly \(a\) zeros, \(b\) ones and \(c\) twos. Their exact convex hull is
\[
P_{a,b,c}=\left\{(x,y,z):0\le x\le ab,\quad0\le y\le ac,\quad0\le z\le bc,\quad0\le cx+az-by\le abc\right\}.
\]
**Saturation theorem.** Every integer point of this convex hull is a realizable two-deck coordinate, i.e. \(P_{a,b,c}\cap\mathbb Z^3=\mathcal D_{a,b,c}\), if and only if **at most one** of \(a,b,c\) is greater than one.

**Exact singleton-content hole law.** With \(a=1\), \(b,c\ge1\), and \(g=\gcd(b,c)\), the number of *unattainable* integer points in this hull is
\[
\boxed{H(1,b,c)=\frac{(b^2-1)(c^2-1)+(g^2-1)}6.}
\]
The numbers of attainable triples and all hull lattice points, respectively, are
\[
D(1,b,c)=\frac{(b+1)(c+1)(bc+2)}2,\qquad L(1,b,c)=D(1,b,c)+H(1,b,c).
\]
In particular, as both \(b,c\to\infty\), exactly one-quarter of the lattice points are unattainable in the limit: \(H/L\to1/4\). These assertions use **the entire multiplicity-preserving length-two scattered deck**; the three coordinates determine all the other two-letter counts once the content is fixed.

## Assumptions and scope
Letters are the labeled alphabet \(\{0,1,2\}\), counts \(a,b,c\) are strictly positive integers, and subsequence occurrences use distinct increasing positions, not necessarily adjacent positions. For a pattern \(uv\), \(\binom{w}{uv}\) is its number of scattered occurrences. Because \(\binom{w}{ij}+\binom{w}{ji}\) equals the product of the counts of the two distinct letters, the displayed \((x,y,z)\) precisely records all independent scattered two-deck entries at fixed content. A *hole* is a point of the standard integer lattice inside the convex hull which is not achieved by a word. The statement concerns lattice saturation of an image, **not** the integer decomposition property of its convex hull or saturation of a semigroup under dilation.

## Proof
**1. Exact convex hull.** Choose one position of each of the three distinct symbols. For any ordering of these three positions, the indicator triple \((I_{01},I_{02},I_{12})\) has entries zero or one and satisfies
\[
0\le I_{01}+I_{12}-I_{02}\le1.
\]
There are precisely \(abc\) choices of one position of each symbol. Summing this inequality shows that every word gives \(0\le cx+az-by\le abc\), while the individual bounds are immediate. Normalize the three coordinates to \(u=x/(ab)\), \(v=y/(ac)\), \(t=z/(bc)\). The resulting polytope is the unit cube intersected with \(0\le u+t-v\le1\). It has precisely six vertices: the six binary triples other than \((0,1,0)\) and \((1,0,1)\). Indeed, the two removed cube corners have only neighbors on their respective cutting planes, so truncation creates no additional vertices. Each of the six allowed corners occurs for a block-ordered word (the six permutations of \(0^a\), \(1^b\), \(2^c\)). Thus the displayed inequalities describe exactly the convex hull, not merely a relaxation.

**2. Complete saturation criterion.** First suppose \(a=b=1\). Then \(x\) equals zero or one. If \(x=0\), the unique \(1\) precedes the unique \(0\); the hull inequalities reduce to \(0\le y\le z\le c\). Each integer pair is realized by placing \(c-z\) copies of \(2\) before the \(1\), \(z-y\) between the \(1\) and the \(0\), and \(y\) after the \(0\). If \(x=1\), the \(0\) precedes the \(1\), the inequalities reduce to \(0\le z\le y\le c\), and the analogous three-gap construction realizes every pair. Permuting letters induces affine integer-lattice automorphisms of the three pair counts: a reversed ordered pair replaces its count by the relevant fixed product minus that count. Therefore every content with at most one multiplicity greater than one is saturated.

Conversely, suppose two multiplicities exceed one. Relabel so that \(a,b\ge2\) and \(c\ge1\). The integer point
\[
(x,y,z)=\left(0,1,\left\lceil\frac ba\right\rceil\right)
\]
belongs to the displayed hull: \(0\le a\lceil b/a\rceil-b\le a-1\le abc\), \(1\le ac\), and \(1\le\lceil b/a\rceil\le b-1\le bc\). The last upper bound holds for every \(a,b\ge2\). But \(x=0\) requires every \(1\) to precede every \(0\). Having \(y=1\) requires at least one \(2\) strictly after a \(0\), hence after all \(b\) ones. That single \(2\) already creates at least \(b\) occurrences of \(12\), contrary to \(z=\lceil b/a\rceil\le b-1\). Therefore a hole exists whenever two multiplicities are at least two, proving both implications.

**3. Exact hole count with one singleton.** Let \(a=1\). The polytope inequalities give, for fixed integers \(0\le x\le b\) and \(0\le y\le c\), exactly
\[
\#\{z\in\mathbb Z:(x,y,z)\in P_{1,b,c}\}=bc+1-|cx-by|.
\]
This follows by intersecting the two integer intervals \([0,bc]\) and \([by-cx,by-cx+bc]\). Consequently
\[
L=(b+1)(c+1)(bc+1)-\sum_{x=0}^b\sum_{y=0}^c|cx-by|.
\]
To count *achievable* triples independently, fix \((x,y)\). The unique \(0\) has \(b-x\) ones and \(c-y\) twos before it, and \(x\) ones and \(y\) twos after it. The number \(z\) of \(12\) pairs is a fixed cross-gap contribution \((b-x)y\) plus independent within-gap contributions varying over **every** integer in \([0,(b-x)(c-y)]\) and \([0,xy]\), respectively. The interval assertion is proved by adjacent swaps \(21\mapsto12\), each increasing the pair count by one. Hence there are exactly \(1+(b-x)(c-y)+xy\) realizable values of \(z\) for each \((x,y)\), and summation yields
\[
D=\sum_{x=0}^b\sum_{y=0}^c[1+(b-x)(c-y)+xy]=\frac{(b+1)(c+1)(bc+2)}2.
\]
This attainable-deck enumeration is also a special case of the previously published distinct-singleton-marker two-deck enumeration; it is supplied here to make the lattice-hole subtraction self-contained.

For the absolute-value sum, put \(t=cx/b\) and \(f=\{t\}\), its fractional part. A direct split at \(\lfloor t\rfloor\) gives
\[
\sum_{y=0}^{c}|t-y|=t^2-ct+\frac{c(c+1)}2+f(1-f).
\]
As \(x\) runs from zero through \(b-1\), the fractional parts of \(cx/b\) comprise each fraction \(j/(b/g)\) exactly \(g\) times, where \(g=\gcd(b,c)\); \(x=b\) adds a zero fraction. Using elementary sums of integers and their squares therefore gives
\[
\sum_{x=0}^b\sum_{y=0}^c|cx-by|=\frac{b(b+1)c(c+1)}2-\frac{c^2(b^2-1)}6+\frac{b^2-g^2}6.
\]
Substitution into \(L-D\) simplifies to the claimed formula. As both \(b,c\to\infty\), \(D\sim b^2c^2/2\) and \(H\sim b^2c^2/6\); consequently \(H/L\to1/4\). Every step is valid for all positive integers, including \(b=1\) or \(c=1\), when the formula correctly gives zero.

## Verification
Run `python3 verify_deck_polytope.py` to enumerate all multiset words for 60 positive Parikh triples of total length at most ten, independently build the integer hull inequalities and test saturation and exact holes, then verify the lattice and hole formula via 625 independent integer double sums. Run `python3 verify_deck_gap_slices.py` to construct 1,301 singleton slices from independent binary interleavings and test their complete attainable intervals and hole counts. Their captured outputs are included as `.txt` files. Finite tests check the formulas and boundary cases; they do not substitute for the infinite-parameter proof above.

## Relationship to prior work
Nilforoushan and Parvaresh (2026) identify independent degrees of freedom and asymptotic counts for general scattered-subsequence decks; the current result asks the different question whether **every integer point of the exact fixed-content convex hull** is realized. Lejeune, Rigo, and Rosenfeld (2020) provide a general algorithm for two-binomial equivalence classes and a group-theoretic description, but no equivalent saturation criterion or gcd hole-count statement was located in their inspected Sections 2–4. Chrisnata and coauthors study binary deck enumeration and bounds. The published *Exact two-deck spectra and fiber multiplicities with distinct marker letters* supplies the singleton-content achievable-deck count already used here and credited above; that count alone neither fixes the full three-dimensional convex hull nor the number of missing integer points, and does not settle all repeated-letter triples. The published *Exact fixed-content Parikh-matrix image and its parity boundary* instead fixes counts of \(01\), \(12\), and the length-three subsequence \(012\), not the full two-deck independent triple \(01\), \(02\), \(12\). No equivalence is claimed on the basis of title search alone.

## Limitations
This is specifically the three-letter full length-two scattered deck at fixed *positive* content; larger alphabets and zero multiplicities are outside the theorem. The integer-hole property is not a normality or semigroup-saturation assertion. The asymptotic hole fraction concerns singleton compositions with both other multiplicities growing and is not claimed universally. The full text of the recent 2026 motivating preprint could not be inspected; an unindexed or inaccessible equivalent argument remains a historical-priority risk. Finite computation provides cross-checks but not external independent certification.

## References
1. A. Nilforoushan and F. Parvaresh, *Improved upper bound on the number of distinct k-decks for any k and alphabet size by counting the independent parameters*, arXiv:2609.23106v1, first posted 2026-09-19, https://arxiv.org/abs/2609.23106.
2. M. Lejeune, M. Rigo and M. Rosenfeld, *On the binomial equivalence classes of finite words*, arXiv:2001.11732, https://www.lirmm.fr/~mrosenfeld/LejeuneRigoRosenfeld.pdf.
3. J. Chrisnata et al., *On the number of distinct k-decks: Enumeration and bounds*, Advances in Mathematics of Communications 17 (2023), 960–978, https://doi.org/10.3934/amc.2021032, author full text https://yaakobi.net.technion.ac.il/files/2022/08/60_k_Decks_Disc_Math21.pdf.
4. *Exact two-deck spectra and fiber multiplicities with distinct marker letters*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-two-deck-spectra-and-fiber-multiplicities-with-distinct-ma--26e221758afc.
5. *Exact fixed-content Parikh-matrix image and its parity boundary*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-fixed-content-parikh-matrix-image-and-its-parity-boundary--097158f6d402.
