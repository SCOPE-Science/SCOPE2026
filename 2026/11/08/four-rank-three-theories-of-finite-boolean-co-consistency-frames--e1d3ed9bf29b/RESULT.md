# Four rank-three theories of finite Boolean co-consistency frames

## Finding

For every integer \(n\geq1\), let \(C_n\) be the first-order structure with domain \(\mathcal P([n])\setminus\{\varnothing\}\), equality, and **only** the binary relation
\[
R(X,Y)\quad\Longleftrightarrow\quad X\cap Y\ne\varnothing.
\]
In particular, \(R(X,X)\) holds for every element, and no constants, order, meet, Boolean operations, colours, or counting quantifiers are present.

**Theorem.** For all positive integers \(n,m\),
\[
C_n\equiv_3 C_m\quad\Longleftrightarrow\quad
\bigl(n=m<4\bigr)\ \lor\ \bigl(n\geq4\ \land\ m\geq4\bigr).
\]
Here \(\equiv_3\) means agreement on *all* first-order sentences of quantifier rank at most three, with unrestricted numbers of variables and formula length. Thus exactly four theories occur. The stable class starts sharply at four atoms and has the fifteen-world representative \(C_4\).

## Assumptions and scope

The domain is exactly the **full nonzero** powerset; it is not an arbitrarily chosen induced subframe. Loops are present. The result concerns pure first-order logic in the signature \(\{R\}\), not modal formulas with varying propositional valuations, not the Boolean-algebra signature, and not the order signature. The ambient atom count \(n\) ranges over every positive integer.

## Proof

### 1. Exact rank-one pair profiles

Fix \(n\), and two nonempty vertices \(A,B\). Write
\[
a=|A\setminus B|,\qquad b=|B\setminus A|,\qquad
c=|A\cap B|,\qquad d=|[n]\setminus(A\cup B)|.
\]
For a third vertex \(Z\notin\{A,B\}\), encode its two adjacency bits by \(j=2\mathbf1_{R(A,Z)}+\mathbf1_{R(B,Z)}\in\{0,1,2,3\}\). Let \(s(A,B)=\sum 2^j\), summed over the *distinct* bit patterns achieved by such \(Z\). Define the signature
\[
\tau(A,B)=\bigl(\mathbf1_{A=B},\mathbf1_{R(A,B)},s(A,B)\bigr).
\]
This is precisely the quantifier-rank-one type of the ordered pair: its quantifier-free atomic diagram fixes equality and \(R(A,B)\), while every extension by one quantified variable has one of the four displayed adjacency patterns, or equals \(A\) or \(B\) (those latter cases are already determined by the pair diagram).

If \(A\ne B\), the four contributions to the bit mask are given by the following **if and only if** conditions:
\[
\begin{array}{c|l}
\text{bit }2^j&\text{witness exists}\\ \hline
1\ (j=0)&d>0\\
2\ (j=1)&b>0\ \land\ (c>0\ \lor\ b\ge2\ \lor\ d>0)\\
4\ (j=2)&a>0\ \land\ (c>0\ \lor\ a\ge2\ \lor\ d>0)\\
8\ (j=3)&c=0\ \lor\ c\ge2\ \lor\ a+b+d\ge2.
\end{array}
\]
For example, the numbers of candidate \(Z\) giving the first three patterns, *before excluding* \(A,B\), are respectively \(2^d-1\), \((2^b-1)2^d\), and \((2^a-1)2^d\). In the second or third count the only possible excluded candidate is respectively \(B\) or \(A\), and it occurs exactly when \(c=0\). For the fourth pattern the candidate count is
\[
(2^c-1)2^{a+b+d}+(2^a-1)(2^b-1)2^d.
\]
If \(c>0\), exactly two of these candidates are \(A,B\); otherwise neither is. The displayed criterion follows by comparing with these exclusions. For \(A=B\) (so \(a=b=0,c>0\)), the only possible distinct-third-vertex patterns are \(j=0\) when \(d>0\), and \(j=3\) when \(c+d\ge2\). Consequently \(s(A,A)=\mathbf1_{d>0}+8\mathbf1_{c+d\ge2}\).

These formulas are exact for all \(n\), including the one-atom case. In particular every pair type depends on the four cell counts only through their values truncated at two.

### 2. The complete table of rank-two pointed profiles

For a nonempty \(A\), let \(k=|A|\) and \(\ell=n-k\). Its rank-two pointed type is determined exactly by the set
\[
T(k,\ell)=\{\tau(A,B):\varnothing\ne B\subseteq[n]\}.
\]
All rank-one pair profiles appearing here are obtained by taking \(0\le c\le k\), \(a=k-c\), \(0\le b\le\ell\), \(d=\ell-b\), discarding \(b=c=0\), and applying the preceding formulas. The complete outcome is the following seven-row table. Each ordered triple is \((\mathbf1_{A=B},\mathbf1_{R(A,B)},s(A,B))\); braces describe the *entire* type, not a sample.

| \(k\) | \(\ell\) | Exactly the triples in \(T(k,\ell)\) |
|---|---|---|
| \(1\) | \(0\) | \((1,1,0)\) |
| \(1\) | \(1\) | \((0,0,8),(0,1,2),(1,1,9)\) |
| \(1\) | \(\ge2\) | \((0,0,10),(0,0,15),(0,1,10),(0,1,11),(1,1,9)\) |
| \(2\) | \(0\) | \((0,1,4),(1,1,8)\) |
| \(\ge3\) | \(0\) | \((0,1,12),(1,1,8)\) |
| \(\ge2\) | \(1\) | \((0,0,12),(0,1,10),(0,1,13),(0,1,14),(1,1,9)\) |
| \(\ge2\) | \(\ge2\) | \((0,0,14),(0,0,15),(0,1,10),(0,1,11),(0,1,13),(0,1,14),(0,1,15),(1,1,9)\) |

For completeness, the table is a **finite** consequence of the preceding universal formulas, not an extrapolation from finite graph sizes: each truncated pair \((a,c)\) with \(a+c=k\) and \((b,d)\) with \(b+d=\ell\) is already realized whenever the corresponding total equals four; for larger totals the same truncated pairs, and no new ones, occur. Hence it suffices to substitute \(k\in\{1,2,3,4\}\) and \(\ell\in\{0,1,2,3,4\}\); the listed seven distinct outcomes follow by direct case enumeration. The cases \(k=2\) versus \(k\ge3\) at \(\ell=0\) are intentionally distinguished.

The type equivalences used above are exact back-and-forth facts: for an assigned \(A\), two rounds remain, and each possible response \(B\) carries exactly its rank-one pair type \(\tau(A,B)\). Hence the collection \(T(k,\ell)\) completely determines, and is determined by, the two-round Ehrenfeucht–Fraïssé winning possibilities for the pointed structure.

### 3. Stabilization and sharpness

At sentence rank three, the complete theory is determined by the collection of rank-two pointed types of possible first moves. In \(C_n\) this is exactly \(\{T(k,n-k):1\le k\le n\}\). The seven-row table shows that the collections for \(n=1,2,3\) are distinct, and for every \(n\ge4\) consist of the same four pointed types: singleton, interior, coatom and top. Therefore all \(C_n\) for \(n\ge4\) are three-round equivalent, with no upper bound on \(n\). This proves stabilization for *all* first-order rank-three sentences, not only the examples below.

Sharpness is also explicit. Write \(D(X,Y)=\neg R(X,Y)\) for disjointness. The rank-two sentence \(\exists X\exists Y\,D(X,Y)\) holds precisely when \(n\ge2\). The rank-three sentence asserting three pairwise \(D\)-related vertices holds precisely when \(n\ge3\). Finally the rank-three sentence
\[
\exists X\Bigl[
\bigl(\exists Y\exists Z\,[R(X,Y)\land R(X,Z)\land D(Y,Z)]\bigr)
\land
\bigl(\exists Y\exists Z\,[D(X,Y)\land D(X,Z)\land D(Y,Z)]\bigr)
\Bigr]
\]
holds precisely when \(|X|\ge2\) and \(|[n]\setminus X|\ge2\) for some \(X\), equivalently \(n\ge4\). These three sentences distinguish all four classes. The formula has rank three because the two nested existential quantifiers in each conjunct occur below only the outer \(\exists X\).

## Verification

The accompanying standalone `checker.py` implements the exact four-cell mask formulas, computes each unary and sentence type by explicit back-and-forth signatures, and independently recomputes every ordered-pair mask by enumerating all distinct third vertices for all frames with one through seven atoms. It verifies \(21{,}343\) pair profiles, all unary orbits in these examples, the symbolic count-truncation identity on \(1\le k\le30,0\le\ell\le30\), the four rank-three classes through 30 atoms without constructing their enormous frames, and the three explicit separating conditions through eight atoms. Run from an ordinary Python 3 interpreter using `python3 checker.py`; no nonstandard packages or external data are needed.

The finite tests independently corroborate the pair formulas and small cases; the unrestricted theorem follows from the proof's count formulas, truncation argument and the complete finite type table, **not** from extrapolating the checker’s finite range.

## Relationship to prior work

Jockwich, Tarafder and Venturi (2026), Sections 3.2 and 6.7, introduce precisely the co-consistency relation and analyze the finite powerset modal frames and their induced-subframe modal logics. The present result asks a distinct question: first-order rank-three *sentence equivalence of the full nonzero frame in the bare binary relation*. Their finite-algebra corollaries and modal hierarchy comparisons do not state this rank-three cutoff.

A published result titled *Every finite stage of the internal forcing logic hierarchy is strict* proves strict descent for the associated modal logics. Modal validity over varying valuations and induced subframes does not imply that pure first-order theories of the **full** frames remain distinguishable at any fixed quantifier rank. The theorem here gives a precise complementary boundary: the pure first-order rank-three theories stabilize after four atoms even though the modal hierarchy distinguishes larger sizes. A separate published sharp \(2^q\)-atom visibility result concerns the **full Boolean-algebra operations signature**, in which quantifier rank three does not stabilize until eight atoms; its stronger signature does not supply the sharp rank-three threshold for the relation-only reduct.

## Limitations

The result is confined to three-quantifier-rank first-order theories in a specific reduct. It does not classify rank-four theories or modal validity, arbitrary induced subframes, infinite atomic algebras, or power-set structures including the empty set. Its classification is mathematical, not an independent historical-priority certificate. The two closely related published comparison records were accessible as indexed summaries but their full repository bodies were unavailable; their exact implications were compared using their published statements and signature distinctions. No independent mathematical audit has been performed.

## References

1. S. Jockwich, S. Tarafder and G. Venturi, *The Internal Modal Logic of Forcing*, arXiv:2607.25977v1 (first posted 28 July 2026), Sections 3.2, 5, 6.7. https://arxiv.org/abs/2607.25977
2. *Every finite stage of the internal forcing logic hierarchy is strict*, publicly indexed mathematical research record (2026), identifier `069a2c03aeb3` (indexed title and abstract available; full record was inaccessible for direct inspection).
3. *Sharp \(2^q\) atom-visibility threshold for finite Boolean algebras*, publicly indexed mathematical research record (2026), identifier `938cb5f89dc7` (distinct richer signature; indexed statement available).
4. Ehrenfeucht–Fraïssé back-and-forth characterization of bounded first-order quantifier rank; standard finite model theory background.
