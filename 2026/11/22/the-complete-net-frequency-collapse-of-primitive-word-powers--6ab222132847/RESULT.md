# The complete net-frequency collapse of primitive word powers

## Finding

**Theorem.** For every finite alphabet \(\Sigma\), every nonempty primitive word \(v\in\Sigma^+\), and every integer \(e\ge3\), let \(p=|v|\) and \(T=v^e\). The full net-frequency spectrum is

\[
\operatorname{NF}_T(x)=\begin{cases}2,&x=v^{e-1},\\0,&\text{every other nonempty factor }x\text{ of }T.\end{cases}
\]

The two net occurrences are at zero-based half-open intervals \([0,(e-1)p)\) and \([p,ep)\); there are no others. This is uniform in the period length, the alphabet size, and the symbols of the primitive root.

The exponent bound is sharp: the primitive word `00100` has a square `0010000100` whose four net occurrences occupy \([0,5)\) and \([5,10)\) (factor `00100`), and \([3,6)\) and \([4,7)\) (factor `000`). Thus a universal two-occurrence statement does not hold for exponent two.

## Assumptions and scope

The finite text \(T\) is indexed from zero. A **primitive** word is not an integer power of a strictly shorter word. A factor \(x\) is **repeated** when it has at least two occurrences, with overlaps allowed. For an occurrence \([i,j)\) of a repeated nonempty factor, the left extension is the factor \(T[i-1:j]\) if \(i>0\), and is defined to be unique if \(i=0\). The right extension is \(T[i:j+1]\) if \(j<|T|\), and is defined to be unique if \(j=|T|\). The occurrence is **net** if both extensions are unique (meaning that each available extension occurs exactly once in the entire text). Net frequency \(\operatorname{NF}_T(x)\) counts such occurrences of \(x\), not distinct strings. Absent/unique factors have frequency zero. This agrees with the boundary convention for net occurrences in Guo–Kishi (2025, Definition 1).

## Proof

**1. Phase rigidity.** All \(p\) cyclic rotations of a primitive word \(v\) are distinct. Indeed, equality of rotations at two different phases gives \(v\) a nontrivial cyclic period \(d<p\); the gcd of \(d\) and \(p\) is then a proper period dividing \(p\), contradicting primitivity. In the periodic text \(v^e\), length-\(p\) factors beginning at different phases have these different rotations. Consequently, if a factor has length \(\ell\ge p\), any two of its occurrences have the same starting phase modulo \(p\).

**2. Short factors have repeated extensions.** Every nonempty factor of length \(t\le p\) that occurs in \(T\) also occurs at some starting phase \(r\in\{0,\ldots,p-1\}\). The factors starting at \(r\) and \(r+p\) are identical and fit inside the first \(3p\) symbols, hence both fit inside \(T\) because \(e\ge3\). Thus every occurring factor of length at most \(p\) has frequency at least two. In particular, for an occurrence of length \(\ell<p\), any available left or right extension has length at most \(p\) and is repeated; it is impossible for both boundary extensions to be absent because \(\ell<|T|\). So such an occurrence is not net.

**3. Long factors not starting at phase zero.** Fix a repeated factor of length \(\ell\ge p\), and write its first occurrence start as \(r\in\{0,\ldots,p-1\}\). By step 1, all occurrences have starting positions \(r,r+p,\ldots,r+(m-1)p\) for some integer \(m\ge2\), since the start range in the finite periodic text is an interval and the phases repeat every \(p\). If \(r>0\), every occurrence has an available left extension. By periodicity these \(m\) left extensions coincide, hence are repeated. No such occurrence is net.

**4. Phase-zero factors.** Suppose \(r=0\). Again the occurrences begin at \(0,p,\ldots,(m-1)p\). If \(m\ge3\), at every start \(kp\) with \(1\le k\le m-1\), the available left extension is identical to that at every other positive start, so is repeated; at start zero the right extension is available and repeats at start \(p\) (since a third occurrence exists). Therefore none is net.

If \(m=2\), the two occurrences begin at \(0\) and \(p\). Their left extensions are unique: the former is missing, and the latter exists only at the second occurrence because there are only two occurrences of the underlying factor. The right extension of the first occurrence is unique if and only if the second occurrence reaches the right boundary of \(T\). If the second does not, their available right extensions are identical, and both are repeated. If it reaches the boundary, the second's right extension is missing, and only the first has the one-letter right extension (all possible occurrences of this extension must begin at a position where the base factor occurs, so it is unique). Thus the two occurrences are net exactly when \(p+\ell=ep\), i.e. \(\ell=(e-1)p\). This factor is precisely \(v^{e-1}\); its starts are zero and \(p\). The proof also covers \(p=1\).

## Verification

Two independent standard-library Python programs are included. `verify_bruteforce.py` constructs a complete substring-frequency dictionary and checks the precise intervals and factors for all primitive roots of lengths at most 7 (binary), 5 (ternary), and 4 (four-symbol), at exponents 3, 4, and 5; it checked 2679 cases including the exponent-two counterexample. `verify_phases.py` instead tests equality of substrings by pairwise comparison and enumerates all net intervals, independently confirming 1154 cases at exponents 3 and 4 and the cyclic-rotation property. Reproduce with `python3 verify_bruteforce.py` and `python3 verify_phases.py`. Both output logs are included. Finite checks do not replace the infinite proof.

## Relationship to prior work

Guo and Kishi (CPM 2025) prove exact net-occurrence counts for Fibonacci and Thue–Morse finite words; these are nonperiodic morphic families and do not imply the present all-primitive-root classification. Faro and Pavone (2026, first public October 3, 2026) establish a two-versus-three dichotomy for period-aligned finite regular epistandard iterates; those iterates and the present power family are distinct, with no cited theorem identifying their net-occurrence sets. Kimura and I (CPM 2026) give generic near-supermaximal-repeat/net-frequency enumeration algorithms and a \(2r\) bound in terms of BWT runs, not this two-occurrence value, unique factor, and positions. The connection to near-supermaximal repeats, largest maximal repeats, and maximum repeats was included in equivalence searches. Exact published priority cannot be guaranteed merely by search absence.

## Limitations

The result applies to exact powers with exponent at least three, not arbitrary almost-periodic texts, conjugate products, or all exponent-two squares. The primitive-root requirement is a normalization: a nonprimitive base may be replaced by its primitive root to obtain the same claim at the actual exponent. Earlier literature may contain an equivalent observation under older maximal-repeat terminology. The highly relevant Faro–Pavone full preprint could not be inspected through the available lawful public channels; the accessible abstract supports a comparison but does not establish noncoverage of the complete paper. No independent audit has been performed.

## References

1. S. Faro and A. Pavone, *Exact Net-Occurrence Counts in Purely Morphic Regular Epistandard Words*, arXiv:2610.04298 (first submitted 2026-10-03), https://arxiv.org/abs/2610.04298 .
2. P. Guo and K. Kishi, *Net Occurrences in Fibonacci and Thue-Morse Words*, CPM 2025, https://doi.org/10.4230/LIPIcs.CPM.2025.16 .
3. K. Kimura and T. I, *R-Enum Revisited: Speedup and Extension for Context-Sensitive Repeats and Net Frequencies*, CPM 2026, https://doi.org/10.4230/LIPIcs.CPM.2026.10 .
