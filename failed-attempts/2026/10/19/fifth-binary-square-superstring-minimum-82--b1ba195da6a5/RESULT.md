# Fifth binary square-superstring minimum: \(82\)

## Finding
Let \(\mathcal Q_5=\{uu:u\in\{0,1\}^5\}\), consisting of \(32\) distinct binary words of length \(10\). Among all finite **linear** binary words containing every element of \(\mathcal Q_5\) as a contiguous factor, the minimum possible length is exactly
\[
\boxed{82}.
\]
An attaining word, written without spaces, is

`1111111111001110011101111011110101101011010000100001001010010100011000110000000000`

This determines the previously unlisted fifth value of the length-minimization sequence OEIS A372435, whose first four values are \(4,12,24,48\). The theorem is an exact finite statement for half-length \(5\), not an assertion at larger half-lengths.

## Assumptions and scope
The alphabet is precisely \(\{0,1\}\). A square means a tandem repeat \(uu\) of **one fixed root length** \(5\), not an arbitrary square of any length. Occurrences are ordinary linear factors, with no wraparound. The host word is unrestricted: other length-\(10\) factors and repeated squares are allowed. Roots are indexed by \(i\in\{0,\ldots,31\}\) in five-bit binary order, and \(W_i\) denotes their ten-bit squares.

## Proof
**Exact overlap reduction.** For distinct roots \(i,j\), define the positive shift
\[
d(i,j)=\min\{h\in\{1,\ldots,10\}:W_i[h:10]=W_j[0:10-h]\}.
\]
The empty overlap at \(h=10\) makes this defined. For any permutation \(\pi\) of the \(32\) roots, concatenating the first square and subsequently appending the last \(d(\pi_t,\pi_{t+1})\) bits of the next square constructs a word of length
\[
10+\sum_{t=1}^{31}d(\pi_t,\pi_{t+1})
\]
containing every required square. Conversely, select one occurrence of each required square in any covering word and order these \(32\) occurrences by their starting indices. Two consecutive selected occurrences with starting-index separation \(h<10\) must overlap consistently, so \(h\ge d(i,j)\); if \(h\ge10\) the same inequality holds automatically. Summing separations and allowing the ten bits of the last selected square shows the covering word has at least the displayed expression. Thus the minimum superstring length equals the minimum of that expression over **all** permutations: no special ordering or grouping assumption is introduced.

**Finite integer optimization.** Introduce the dummy vertex \(32\). A directed Hamiltonian circuit through \(\{0,\ldots,32\}\) receives arc costs \(d(i,j)\) between distinct real vertices, cost \(10\) on any arc leaving dummy \(32\), and cost \(0\) on any arc entering it. Removing the dummy turns a circuit into the permutation above, with exactly the same cost. The problem is therefore a \(33\)-vertex directed Hamiltonian-cycle integer program with integer costs. For each ordered pair of distinct vertices introduce \(x_{ij}\in\{0,1\}\), enforce every vertex's in-degree and out-degree to equal one, and enforce for each nonempty proper vertex set \(S\)
\[
\sum_{i,j\in S,\ i\ne j} x_{ij}\le |S|-1.
\]
These subtour constraints are valid for every Hamiltonian circuit. The package supplies a compact list of \(20\) such valid cuts in `certificate.json`. Solving the **weaker** integer program consisting of the degree constraints and just those \(20\) cuts gives optimum \(82\). In `verify.py`, the solver is required to report an optimal integral solution and a matching dual lower bound within \(10^{-7}\) of \(82\); the program additionally checks the recovered integer circuit, its cost, and the stated witness using fresh independently generated squares. Consequently, even the weakened model has no solution of integer cost at most \(81\), so neither does the complete Hamiltonian-tour model. This establishes the lower bound without assuming that the cut list is exhaustive.

**Attaining upper bound.** The root ordering, in decimal five-bit notation, is

`31 28 25 19 7 14 27 23 15 30 29 21 11 22 13 26 8 16 1 2 4 9 18 5 10 20 17 3 6 12 24 0`.

Its exact successive-overlap cost plus the first ten symbols is \(82\). The concatenation is the displayed witness. Direct factor enumeration checks that all \(32\) roots' squares occur; in particular the result is constructive and the bounds match.

## Verification
Execute `python verify.py` beside `certificate.json` with Python, NumPy \(2.3.5\) and SciPy \(1.17.0\) (which supplies HiGHS MILP). The verifier reconstructs all \(32\) distinct squares, reassembles the explicit witness, checks every required factor, rebuilds the \(1056\)-variable binary arc model from the published cut sets, and solves the integer model to verified optimality. It directly inspects the returned \(33\)-arc Hamiltonian circuit and exact integer cost, rather than trusting a textual optimization log. As an additional check, a separate bitmask dynamic program derives the established smaller linear values \(4,12,24,48\) for half-lengths \(1,2,3,4\).

## Relationship to prior work
Au's *Generalized de Bruijn words for Primitive words and Powers* (first publicly posted \(2009\)-\(04\)-\(25\), revised/published subsequently) studies shortest words containing all prescribed powers and gives general bounds and constructions, but does not resolve this fifth binary-square minimum. For half-length \(5\), the published lower-bound mechanism gives \(32+5\cdot8=72\) because there are eight binary length-five necklace classes; the primitive-word conjugate-cover construction in the updated manuscript gives an upper bound of \(32+5\cdot8+12+5+2-2=89\). The exact value \(82\) lies strictly between those bounds. The exact-sequence entry OEIS A372435 currently lists only the four preceding values. Tan and Shallit analyze broader questions about the factor sets witnessed by finite words, with different exact-set and maximal-witness formulations, not this prescribed-subset minimum.

## Limitations
This is a finite exact minimization, with no theorem for half-lengths greater than \(5\), no count of all minimizing words, and no independent formal proof assistant certificate. The optimality bound is a reproducible finite integer-programming computation using a solver, with fully specified variables, constraints, cuts, integer witness, and source code; correctness of the numerical solver is not independently formally verified.

## References
1. Yu Hin Au, *Generalized de Bruijn words for Primitive words and Powers*, arXiv:0904.3997 (first submitted 2009-04-25); updated full manuscript https://au-gary.github.io/Au15a.pdf (2015), especially Proposition 14, Theorem 15 and Corollary 16.
2. OEIS A372435, *Length of the shortest binary string that contains all blocks of the form xx*, https://oeis.org/A372435 (accessed 2026-10-15 UTC).
3. Shuo Tan and Jeffrey Shallit, *Sets Represented as the Length-n Factors of a Word*, arXiv:1304.3666 (2013), especially sections 1 and 4.
