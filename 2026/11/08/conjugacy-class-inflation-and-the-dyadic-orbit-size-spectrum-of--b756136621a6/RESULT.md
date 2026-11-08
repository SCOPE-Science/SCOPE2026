# Conjugacy-class inflation and the dyadic orbit-size spectrum of the Thue–Morse word

## Finding

Let \(t=0110100110010110\cdots\) be the binary Thue–Morse word, the fixed point of \(\mu(0)=01\), \(\mu(1)=10\). For \(n\ge1\), let \(F_n\) denote its set of distinct length-\(n\) factors, and let \(\mathcal C_n\) denote the partition of \(F_n\) by circular rotation. For a class \(C\in\mathcal C_n\), put \(e(C)=|\{u\in C:u u_0\in F_{n+1}\}|\), with \(u_0\) the first letter. Write \(p(n)=|F_n|\) and \(E(n)=|\{u\in F_n:u u_0\in F_{n+1}\}|\).

**Conjugacy-class inflation theorem.** For every integer \(n\ge4\), the multiset of numbers of distinct occurring factors in each length-\(2n\) circular-conjugacy class is exactly

\[
\bigl\{|C|+e(C):C\in\mathcal C_n\bigr\}\ \uplus\ \bigl\{1\bigr\}^{p(n+1)-E(n)}.
\]

More explicitly, the class containing \(\mu(u)\) has size \(|C|+e(C)\) when \(u\in C\), and every remaining length-\(2n\) factor forms a singleton class. Consequently,

\[
c(2n)=c(n)+p(n+1)-E(n),\qquad n\ge4,
\]

where \(c(n)=|\mathcal C_n|\). This statement is about **sizes of intersections of full rotation orbits with the factor language**, not merely counts of rotation classes.

**Exact dyadic spectrum.** For every integer \(k\ge2\), put \(n=2^k\). There is exactly one class with \(n\) members, namely all \(n\) rotations of \(\mu^k(0)\), exactly three classes with two members each, and exactly \(2n-8\) singleton classes. Equivalently the size multiset is

\[
\{n\}\uplus\{2,2,2\}\uplus\{1\}^{2n-8}.
\]

The known numerical equalities \(p(n)=3n-2\) and \(c(n)=2n-4\) follow, but **are not claimed to be new**. The size-spectrum classification and the all-length class inflation formula are the claims of this note.

## Assumptions and scope

All factors are contiguous subwords of the one-sided infinite Thue–Morse word, indexed by their binary contents rather than their occurrence positions. The circular conjugacy class of a word \(w\) is the intersection of all cyclic rotations of \(w\) with \(F_{|w|}\). In particular, an absent rotation is not counted, and identical rotations of periodic words are counted only once. The inflation result requires \(n\ge4\); the dyadic formula requires \(k\ge2\). All statements hold for the infinite factor language, not just finite prefixes.

## Proof

**1. Synchronizing parity.** Every length-four factor of \(t\) occurs in one parity of positions only: at even positions one finds \(0101,0110,1001,1010\); at odd positions one finds \(0010,0011,0100,1011,1100,1101\). Longer factors inherit their unique parity from their four-letter prefix. The forbidden words \(000\) and \(111\) do not occur because each \(\mu\)-block has opposite bits. The forbidden words \(01010\) and \(10101\) do not occur because \(t\) is overlap-free [1, §5.3].

For any \(n\ge4\), the length-\(2n\) factors split disjointly into the even-start set \(A_n=\{\mu(u):u\in F_n\}\) and the odd-start set

\[
B_n=\{b(v):v=v_0\cdots v_n\in F_{n+1}\},\qquad
b(v)=(1-v_0)v_1(1-v_1)v_2\cdots(1-v_{n-1})v_n.
\]

Both maps are injective. Parity synchronization ensures \(A_n\cap B_n=\varnothing\).

**2. The inherited classes.** Any circular shift by an even number of positions of \(\mu(u)\) is \(\mu\) applied to the corresponding rotation of \(u\). Conversely, an odd shift of a word \(\mu(u)\) cannot be another member of \(A_n\): such a word would have opposite-bit adjacent pairs in both circular parity matchings, forcing the entire cyclic word to alternate, hence to contain a forbidden alternating factor of length five. Thus \(\mu\) induces a bijection of the classes \(\mathcal C_n\) with the classes represented in \(A_n\), preserving their initial cardinalities.

**3. Closing extensions.** If \(v_0=v_n\), then \(b(v)\) is the left circular shift by one bit of \(\mu(v_0\cdots v_{n-1})\). Accordingly, the closed-end extensions in \(B_n\) attach precisely one new, distinct factor to the inherited class of each \(u\in F_n\) satisfying \(u u_0\in F_{n+1}\). Since each such factor has the unique odd starting parity, different closing extensions cannot collide.

**4. All other odd-start factors are isolated.** Now take \(v=v_0\cdots v_n\in F_{n+1}\) with \(v_0\ne v_n\), and let \(w=b(v)\). In the circular matching consisting of the index pairs \((1,2),(3,4),\ldots,(2n-1,0)\), all pairs have opposite letters except the closing pair \((2n-1,0)\), whose letters agree. In the other matching \((0,1),(2,3),\ldots,(2n-2,2n-1)\), the number of agreeing pairs is the number of changes between successive letters of \(v\). This is at least two: if a binary length-\(n+1\ge5\) word had at most one change and contained neither \(000\) nor \(111\), each constant run would have length at most two, contradicting length at least five.

A nonzero even circular shift moves the unique equal pair in the first matching away from the closing boundary and so cannot belong to \(B_n\); it also has at least one equal pair in that matching, so cannot belong to \(A_n\). An odd circular shift interchanges the two matchings. It has at least one equal pair in the even matching, excluding \(A_n\), and at least two equal pairs in the odd matching, one necessarily internal, excluding \(B_n\). Hence no nonidentity circular shift of \(w\) is an occurring factor. The word \(w\) is a singleton class. There are exactly \(p(n+1)-E(n)\) such words, completing the inflation formula.

**5. Dyadic closed-end set.** Let \(H_n=\{u\in F_n:u u_0\in F_{n+1}\}\). At length four, direct inspection gives

\[
F_4=\{0010,0011,0100,0101,0110,1001,1010,1011,1100,1101\},
\]

and \(H_4=\{0011,0110,1001,1100\}\), exactly the four rotations of \(\mu^2(0)=0110\). The four classes at this length have sizes \(4,2,2,2\).

For every \(n\ge4\), a closed-end factor of length \(2n+1\) has a unique even or odd start. In either alignment its desubstitution is a closed-end factor of length \(n+1\). For each \(u\in H_n\), these two alignments give respectively \(\mu(u)\) and its left circular one-bit shift as the first \(2n\) letters; all such factors are distinct by parity and injectivity. Thus \(|H_{2n}|=2|H_n|\), and if \(H_n\) consists of all rotations of \(\mu^k(0)\), then \(H_{2n}\) consists of all rotations of \(\mu^{k+1}(0)\). Induction yields \(|H_{2^k}|=2^k\) and the claimed description of this entire set.

**6. Dyadic class sizes.** The standard Thue–Morse factor-complexity recurrence \(p(2m+1)=2p(m+1)\) [1, §5.3] and direct value \(p(5)=12\) give \(p(2^k+1)=3\cdot2^k\) for every \(k\ge2\). Therefore, at \(n=2^k\), the inflation theorem adds \(n\) members (all in the unique full rotation class) and introduces \(p(n+1)-|H_n|=2n\) singleton classes. The three two-member classes remain two-member classes, and the previous singleton classes remain singleton. Starting from the size distribution \(4,2,2,2\), induction proves the stated multiset \(\{n\}\uplus\{2,2,2\}\uplus\{1\}^{2n-8}\) for every dyadic \(n\ge4\). ∎

## Verification

The accompanying standard-library Python script `VERIFY.py` enumerates distinct factors, constructs actual circular-conjugacy classes, and checks the all-length inflation multiset for every \(4\le n\le64\). It separately checks the dyadic class-size spectrum and identification of the full rotation class at \(n=4,8,16,32,64,128\). Factor sets are compared across two successive long substitution prefixes, and the four forbidden local patterns are tested. The script prints `VERIFY_OK` when every test succeeds. These are finite cross-checks, not a substitute for the preceding infinite proof.

## Relationship to prior work

Cassaigne, Fici, Sciortino and Zamboni [1] introduced cyclic complexity and established unique alignment of length-four Thue–Morse factors, recurrences for factor complexity and same-end factor counts, and a proof yielding many singleton conjugacy classes. Their Proposition 15 contains a closely related isolation argument; the present result refines it to a complete **class-size multiset recurrence**, not merely a lower bound on class count. Krawchuk and Rampersad [2, Proposition 1] already proved the numerical formula \(c(2^k)=2^{k+1}-4\) for \(k\ge3\), using Walnut. Bell and Shallit [3] study the **Lie complexity** that counts classes all of whose circular rotations occur, and give its value for Thue–Morse. Those count-level and full-rotation results overlap substantially with, but do not state, the entire partial-class size spectrum or the all-length inflation rule. Combining some published count-level results does not by itself specify the sizes of the remaining partially represented classes.

## Limitations

The result applies to the exact one-sided Thue–Morse factor language, and the general inflation lemma is established only for \(n\ge4\). The dyadic classification does not give a closed classification for all nondyadic lengths. It does not address factor occurrence frequencies. Earlier unindexed equivalence results or unpublished calculations could affect historical priority; the literature comparison is bounded and has not been independently audited.

## References

[1] J. Cassaigne, G. Fici, M. Sciortino and L. Q. Zamboni, *Cyclic Complexity of Words*, arXiv:1402.5843, first posted 24 February 2014, §5.3, Lemma 13 and Proposition 15. https://arxiv.org/abs/1402.5843

[2] C. Krawchuk and N. Rampersad, *Cyclic Complexity of Some Infinite Words and Generalizations*, Integers **18A** (2018), #A12, Proposition 1. https://math.colgate.edu/~integers/sjs12/sjs12.pdf

[3] J. P. Bell and J. Shallit, *Lie complexity of words*, arXiv:2102.03821, first posted 7 February 2021, §§6–7. https://arxiv.org/abs/2102.03821
