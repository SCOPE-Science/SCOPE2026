# Exact binary length-five power-superstring optimum for every exponent at least three

## Finding

For every integer \(p\ge 3\), let \(\mathcal P_p=\{u^p:u\in\{0,1\}^5\}\), with \(u^p\) the concatenation of \(p\) copies of the binary root \(u\). Among **linear** binary strings containing every member of \(\mathcal P_p\) as a contiguous factor, the smallest possible length is
\[
\boxed{\operatorname{SCS}(\mathcal P_p)=40p+2.}
\]
There are \(32\) distinct mandatory factors, all of length \(5p\). In addition, in every minimum-length Hamiltonian-overlap ordering of these factors, the five-bit roots belonging to each cyclic-rotation (necklace) class occur in one consecutive block. Thus the ordering has exactly seven transitions between the eight necklace classes; an ordering that revisits a previously departed class cannot be optimal.

At \(p=3\), the optimum is \(122\). One optimal linear word is

`00000000000000010000100001000011000110001100010100101001010010110101101011010111001110011100111101111011110111111111111111`

Its length is \(122\); it contains all \(32\) requisite length-fifteen cubes. For every larger integer exponent, the same root ordering, maximally overlapped, gives a word of length \(40p+2\).

## Assumptions and scope

The alphabet is the labeled binary alphabet \(\{0,1\}\). Root length is exactly five; the exponent \(p\) is an **integer** with \(p\ge3\). The host is an ordinary finite **linear** word. The host is unrestricted except for containing every required factor, and repeated occurrences of compulsory factors are permitted. Circular hosts, fractional powers, other alphabet sizes, and other root lengths are not covered by this theorem.

For distinct equal-length words \(x,y\), define the overlap cost \(c(x,y)=|y|-\operatorname{ov}(x,y)\), where \(\operatorname{ov}(x,y)\) is the length of their longest matching proper suffix and prefix (or zero if none). For distinct roots \(u,v\), write \(c_p(u,v)=c(u^p,v^p)\). A necklace is an equivalence class of length-five roots under cyclic rotation. There are exactly eight: two singleton constant classes and six classes of size five, because five is prime.

## Proof

**1. Exact shortest-superstring reduction.** Given any permutation \(\pi\) of the \(32\) roots, maximal successive suffix-prefix overlap yields a host of length
\[
5p+\sum_{i=1}^{31}c_p(\pi_i,\pi_{i+1}).
\]
Conversely, occurrences of all the distinct equal-length mandatory factors in any host have distinct starting positions. Ordering one occurrence of each by position shows the host is at least as long as the maximally overlapped concatenation in that order. Hence minimizing the displayed cost over all permutations gives the shortest linear host exactly.

**2. Two types of transitions.** If \(u\) and \(v\) are distinct cyclic rotations of one another, let \(d\in\{1,2,3,4\}\) be the smallest left-shift converting \(u\) into \(v\). For every \(p\ge2\), the maximal overlap of \(u^p\) with \(v^p\) has length \(5p-d\), so \(c_p(u,v)=d\), independent of \(p\). An overlap of greater length would give a shorter shift contradicting the minimality of \(d\).

If \(u\) and \(v\) lie in different necklaces, their power words cannot overlap in five or more positions: a five-symbol factor of the periodic word \(u^p\) is a rotation of \(u\), so such an overlap would make \(v\) a rotation of \(u\). Therefore the maximal overlap is at most four, and for some \(t(u,v)\in\{0,1,2,3,4\}\), independent of \(p\ge2\),
\[
c_p(u,v)=5p-t(u,v)\ge5p-4.
\]

**3. All optimal orders respect necklaces.** Let \(B\) be the number of transitions between different necklaces in a Hamiltonian ordering. Every ordering has \(B\ge7\) because it visits eight necklace classes. The other \(31-B\) transitions join distinct words and each costs at least one. Consequently its host length is at least
\[
5p+(31-B)+B(5p-4)=5p+31+5(p-1)B.
\]
For \(B\ge8\) this is at least \(45p-9\), which exceeds \(40p+2\) whenever \(p\ge3\). A length-\(40p+2\) construction is given in Step 5 below. Hence every optimal ordering has \(B=7\), so each of the eight necklaces is visited in one uninterrupted block.

**4. An exhaustive, small, integer dynamic program at exponent three.** Partition the roots into their eight necklaces. For each necklace \(C\) and endpoints \(a,b\in C\), set
\[
h_C(a,b)=\min_{\substack{(v_1,\ldots,v_{|C|})\text{ permutation of }C\\v_1=a,\ v_{|C|}=b}}\sum_{i=1}^{|C|-1}c_3(v_i,v_{i+1}).
\]
For a singleton, the sole internal cost is zero. Each nonsingleton has five words, so these quantities are computed by exhaustively inspecting only \(5!=120\) local orders.

For a nonempty set \(S\) of necklaces and a root \(b\) in the last visited necklace, let \(D(S,b)\) be the smallest overlap length of an ordering that traverses exactly the necklaces in \(S\), each in one uninterrupted block, and ends at \(b^3\). Its initialization is
\[
D(\{C\},b)=15+\min_{a\in C}h_C(a,b),
\]
and appending a fresh necklace \(C\notin S\) gives the exhaustive recurrence
\[
D(S\cup\{C\},b)=\min_{\substack{a\in C\\e\in\bigcup S}}
\bigl(D(S,e)+c_3(e,a)+h_C(a,b)\bigr),\quad b\in C.
\]
All arithmetic is integer and every permitted ordering is represented. Exactly \(4096\) subset-endpoint states arise. Direct enumeration of these recurrences gives
\[
\min_bD(\{\text{all eight necklaces}\},b)=122.
\]
The standalone `verify.py` recomputes every local permutation and each global subset state from the displayed definitions. It also independently compares the class-block dynamic program with an unrestricted \(2^{2^n}\)-mask Hamiltonian path dynamic program for the smaller base lengths \(n=2,3,4\) and exponents \(p=2,3,4\); no optimizer, precomputed table, or floating-point tolerance is needed. The explicit machine-readable route, host and state counts appear in `CERTIFICATE.json`.

At \(p=3\), Step 3 excludes every ordering with at least eight class switches (length at least \(126\)), while the exhaustive dynamic program proves a minimum of \(122\) among the remaining orders. Therefore the unrestricted optimum is precisely \(122\).

**5. All exponents.** For any fixed permutation with exactly seven inter-necklace transitions, all internal costs remain constant when \(p\) increases, while each of its seven cross-necklace costs and the initial-word length increase by five per unit of \(p\). Thus its total length equals its length at \(p=3\) plus \(40(p-3)\). The exponent-three optimal route from Step 4 therefore produces a host of length \(122+40(p-3)=40p+2\) for every integer \(p\ge3\). Conversely, every possible order either has seven transitions and costs at least \(40p+2\) by Step 4 and the same cost identity, or has at least eight transitions and costs at least \(45p-9>40p+2\) by Step 3. This proves both the length formula and the forced necklace-block property. \(\square\)

## Verification

With Python 3 and its standard library, in a directory containing `verify.py` and `CERTIFICATE.json`, run `python3 verify.py`. Expected final line:

`VERIFY_OK power_exponent_formula_n5_p_ge3_exact_necklace_DP_and_switch_bound`

The script reconstructs all binary roots and overlaps from their definitions, checks every local necklace permutation, runs the \(4096\)-state global recurrence, reconstructs the explicit cubic host and independently searches the unrestricted Hamiltonian paths for smaller base lengths. It checks grouped constructions at exponents \(3,4,5,8\), including all required factors. The all-exponent claim is proved by the transition-cost identity, not inferred from the finite tests.

## Relationship to prior work

Yu Hin Au, *Generalized de Bruijn words for Primitive words and Powers* (first public arXiv version April 25, 2009; revised full text June 29, 2015), proves general bounds and a construction for all word powers. For the present parameters, his Proposition 14 gives the valid lower bound \(40p-8\), while his Theorem 15 yields a class-cover-dependent upper bound. An explicit ten-symbol conjugate cover already yields \(40p+2\) as an upper bound through that construction, but this does **not** prove optimality; the exact matching lower bound, sharp exponent-three class-switch obstruction, and all-optima necklace-block rigidity are established here by the finite recurrence and lifting argument. The exact result is therefore not a renaming of that prior upper bound.

OEIS A372435 records shortest-superstring values for **squares** of binary roots, not the present \(p\ge3\) power spectrum. The standard shortest-superstring overlap reduction itself is established methodology and is not claimed as novel.

## Limitations

The finite exact optimization treats only binary roots of length five. No formula is claimed for different base lengths, larger alphabets or circular hosts. The classification concerns necklace contiguity of required factors within optimal Hamiltonian orderings; it does not enumerate all optimal hosts or claim that required factors cannot occur incidentally more than once. The \(122\) base value is a finite computer-assisted proof with a fully enumerative standalone verification program; it has not been independently formally certified. Previously unindexed equivalent computations remain possible.

## References

1. Yu Hin Au, *Generalized de Bruijn words for Primitive words and Powers*, arXiv:0904.3997 (v1 April 25, 2009; v5 June 29, 2015), Section 3, Proposition 14, Theorem 15; https://arxiv.org/abs/0904.3997 and https://arxiv.org/html/0904.3997v5.
2. The On-Line Encyclopedia of Integer Sequences, A372435, *Length of the shortest binary string that contains all blocks of the form xx*, https://oeis.org/A372435 (accessed October 15, 2026 UTC).
