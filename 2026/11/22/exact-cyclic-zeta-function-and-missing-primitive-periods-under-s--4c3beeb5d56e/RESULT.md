# Exact cyclic zeta function and missing primitive periods under simultaneous binary two- and three-step square avoidance

## Finding

Let \(X\) be the set of all two-sided binary sequences in which no contiguous factor of length four is of the form \(uvuv\) with \(u,v\in\{0,1\}\), and no contiguous factor of length six is of the form \(abcabc\) with \(a,b,c\in\{0,1\}\). Constant adjacent bits are allowed: squares of half-length one are **not** forbidden. For every integer \(n\ge1\), let \(F_n\) be the number of indexed binary circles \((w_0,\ldots,w_{n-1})\) whose bi-infinite periodic extensions belong to \(X\). Rotations, reversal and bit complementation are **not** identified in \(F_n\).

The exact periodic-point zeta function is

\[
\zeta_X(z):=\exp\!\left(\sum_{n\ge1}\frac{F_n}{n}z^n\right)
=\frac{1}{(1-z^2-z^3-z^4+z^6)(1+z^2+z^3-z^4-z^6)}.
\]

The initial counts \((F_1,\ldots,F_{18})\) are

\[
(0,0,0,12,10,6,0,12,36,50,22,18,78,196,190,124,170,546).
\]

The complete set of attainable **least** periods is exactly

\[
\{4,5,6,9,10,11\}\ \cup\ \{n\in\mathbb Z:n\ge13\}.
\]

Thus the six excluded positive least periods are \(1,2,3,7,8,12\), even though circles of circumferences \(8\) and \(12\) exist. In particular, if \(P_n\) denotes the number of primitive rotation classes of length \(n\), then

\[
P_n=\frac1n\sum_{d\mid n}\mu(n/d)F_d,
\]

and \(P_n>0\) precisely for the lengths in the displayed set.

The shift has entropy \(\log\lambda\), where \(\lambda=1.401268367939855\ldots\) is the Perron root of

\[
t^6-t^4-t^3-t^2+1=0.
\]

The recurrent state graph is primitive, so the shift has one measure of maximal entropy and \(F_n\sim\lambda^n\) as \(n\to\infty\).

## Assumptions and scope

The two forbidden families are *literal contiguous tandem squares*: \(uvuv\) and \(abcabc\) may have repeated letters inside their halves. Squares of other half-lengths are unrestricted. Every short circle is tested using its infinitely periodic extension, rather than treating fewer than six cyclic indices as an exemption. The alphabet labels \(0\) and \(1\) are fixed. A marked/indexed circle means all \(n\) coordinates are distinguished; a primitive rotation class quotients by the \(n\) shifts of a least-period-\(n\) circle.

## Proof

**1. Finite-type presentation.** Use all \(32\) five-bit states. There is an edge from \(s=s_0\cdots s_4\) to \(s_1\cdots s_4a\) exactly if the six-bit concatenation \(s_0\cdots s_4a\) has neither a square in positions \(0\)–\(3\) or \(1\)–\(4\), nor a three-bit-half square in positions \(0\)–\(5\). Thus an edge tests every newly completed forbidden window. In particular, closed length-\(n\) paths correspond bijectively to indexed admissible periodic binary sequences of length \(n\), including \(n<6\).

A direct edge inspection shows that there is a single cyclic strongly connected component, with the following \(16\) states (lexicographic order):

`00010 00011 00100 00110 00111 01000 01100 01110 10001 10011 10111 11000 11001 11011 11100 11101`

The other \(16\) states are singleton components without loops. This can also be checked without trusting a precomputed graph: construct the \(32\) transitions by the stated local predicate, compute mutual reachability and compare the sixteen listed states. Any closed path must lie entirely within the listed component. Let \(M\) be its \(16\)-by-\(16\) adjacency matrix, in the stated order. Then \(F_n=\operatorname{tr}(M^n)\), and the determinant identity gives \(\zeta_X(z)=\det(I-zM)^{-1}\).

**2. Eight-state signed quotient.** Bit complementation commutes with every edge. Choose the eight representatives beginning with zero, in order:

`00010 00011 00100 00110 00111 01000 01100 01110`

Give them indices \(0,1,\ldots,7\). Their quotient edges, with the sign \(+\) when the destination has the chosen representative orientation and \(-\) when the destination is its bit complement, are:

`0>2:+; 1>3:+; 1>4:+; 2>5:+; 3>6:+; 4>7:+; 5>7:-; 6>3:-; 6>4:-; 7>0:-; 7>1:-`.

Let \(B_+\) be the unsigned adjacency matrix of this list and let \(B_-\) be the signed adjacency matrix (entries \(+1\) or \(-1\)). In the paired basis \((r_0,\ldots,r_7,\bar r_0,\ldots,\bar r_7)\), the complement action block-diagonalizes \(M\) as \(B_+\oplus B_-\). Exact row elimination in the two displayed, completely specified eight-state matrices yields

\[
\begin{aligned}
\det(I-zB_+)&=1-z^2-z^3-z^4+z^6,\\
\det(I-zB_-)&=1+z^2+z^3-z^4-z^6.
\end{aligned}
\]

The product proves the zeta identity and, by expansion of its logarithm, every marked-period count. These determinant identities are also independently replayed with exact arithmetic in `verify_transfer.py`.

**3. Missing primitive periods.** The zeta identity gives \(F_1=F_2=F_3=F_7=0\), \(F_4=12\), \(F_5=10\), \(F_6=6\), \(F_8=12\) and \(F_{12}=18\). Every period-four circle yields one of the twelve indexed period-eight circles, and no other period-eight circle exists. For period twelve, the twelve indexed period-four circles and six indexed period-six circles are disjoint, and exhaust all eighteen possibilities. Hence no least periods \(1,2,3,7,8,12\) occur.

Conversely the graph has three *simple return loops* based at `10001`, shown as lists of successive five-bit states, with only their initial and terminal states equal:

- Length \(4\): `10001 00010 00100 01000 10001`.
- Length \(5\): `10001 00011 00110 01100 11000 10001`.
- Length \(6\): `10001 00011 00111 01110 11100 11000 10001`.

Each step passes the literal six-bit transition predicate. Their labels therefore produce admissible circles of least periods \(4,5,6\). Concatenate these based loops in any **nonperiodic sequence of loop types**. The resulting binary circle is primitive: occurrences of the five-bit marker `10001` are exactly its loop boundaries, so a shorter period would induce a nontrivial period of the cyclic sequence of return lengths.

Every odd \(n\ge9\) equals \(5+4a+6b\) for integers \(a,b\ge0\) with \(a+b\ge1\); use one length-five loop and the specified numbers of length-four and length-six loops. Every \(n\equiv2\pmod4\) with \(n\ge10\) equals \(6+4a\) with \(a\ge1\); use one length-six loop followed by \(a\) length-four loops. Every \(n\equiv0\pmod4\) with \(n\ge16\) equals \(12+4a\) with \(a\ge1\); use two length-six loops followed by \(a\) length-four loops. Each return-length itinerary is a nonconstant cyclic word with one unique exceptional run of loop lengths, hence has least period equal to its number of excursions. These cases prove exactly the asserted least-period spectrum.

**4. Entropy.** The recurrent directed graph is strongly connected and has closed loops of lengths \(4\) and \(5\), so it is aperiodic. Perron–Frobenius theory yields a simple spectral radius \(\lambda>1\), strictly dominating all other eigenvalue moduli. The factor \(\det(I-zB_+)\) contains the Perron root, as \(B_+\) is the nonnegative irreducible eight-state quotient. Substituting \(z=1/t\) gives the displayed sextic equation. The primitive finite-type presentation and Perron–Frobenius theory give entropy \(\log\lambda\), the uniqueness of the maximal-entropy measure, and the asymptotic \(\operatorname{tr}(M^n)\sim\lambda^n\).

## Verification

Run `python verify_transfer.py` with Python 3 and SymPy to rebuild the complete graph from the literal forbidden-window predicate, verify its strongly connected decomposition, the exact signed quotient, determinant identities, thirty marked-count values, the corresponding Möbius primitive counts and the Perron root.

Independently run `python verify_direct.py` with only Python 3. It exhaustively tests every binary circle of lengths \(1\) through \(16\) directly against periodic length-four and length-six windows, checks the marked- and least-period counts, and generates explicit primitive circles for all lengths \(13\) through \(150\). The latter finite range is only an independent check; the unbounded construction is proved above.

## Relationship to prior work

Richard and Grimm (2003/2004) develop rational generating functions for finite truncations of square avoidance on a ternary alphabet; their truncation forbids *all* square half-lengths up to a bound, including half-length one. Grimm and Heuer (2008) review finite forbidden-pattern methods and binary cubefree/ternary squarefree entropy calculations. Mousavi and Shallit (2012) study a different, exponent-based requirement on the circular interpretations of **all factors** of a word. None of these statements directly supplies the simultaneous binary half-length-two/three periodic-point zeta identity or the isolated primitive-period gaps. The algebraic number \(\lambda\) also occurs as a growth ratio of an unrelated rational integer sequence in OEIS A225490; that numerical coincidence does not supply the periodic-word interpretation or the two-factor zeta function.

The general transfer-matrix, determinant, Möbius-inversion and Perron–Frobenius techniques are standard. The concrete signed quotient and exact joint restriction, including its complete primitive-period spectrum, are the contribution here. A separate known formula for forbidding only half-length-three squares does not determine the simultaneous avoidance system.

## Limitations

Only the specified **two** square half-lengths are excluded; no claim concerns full binary square-freeness, all bounded square lengths, deletion coding or ternary alphabets. No quotient by complementation or reversal is taken. First-publication priority may be affected by unindexed literature, software tables or equivalent automaton presentations not found in the searches described in the review. The two test programs are repeatability checks, not independent mathematical audit.

## References

- C. Richard and U. Grimm, *On the Entropy and Letter Frequencies of Ternary Square-Free Words*, arXiv:math/0302302 (first submitted 25 February 2003), *Electronic Journal of Combinatorics* **11** (2004), R14, https://doi.org/10.37236/1767.
- U. Grimm and M. Heuer, *On the Entropy and Letter Frequencies of Powerfree Words*, *Entropy* **10** (2008), 590–612, https://doi.org/10.3390/e10040590.
- H. Mousavi and J. Shallit, *Repetition Avoidance in Circular Factors*, arXiv:1212.0052 (1 December 2012), https://arxiv.org/abs/1212.0052.
- OEIS A225490, https://oeis.org/A225490 (a rational-series coefficient sequence sharing one growth constant; not an avoidance enumeration).
