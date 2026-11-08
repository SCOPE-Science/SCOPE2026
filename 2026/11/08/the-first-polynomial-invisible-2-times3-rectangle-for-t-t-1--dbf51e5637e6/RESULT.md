# The first polynomial-invisible \(2\times3\) rectangle for \(t(t+1)\)

## Finding

Let \(P(t)=t(t+1)\). A positive integer lattice point \((x,y)\) is *\(P\)-invisible* when there is an integer \(t\) with \(1\le t<x\) and \(P(x)\mid yP(t)\). A \(2\times3\) invisible rectangle with lower-left corner \((x,y)\) consists of the six points \((x+i,y+j)\), \(i\in\{0,1\}\), \(j\in\{0,1,2\}\), all \(P\)-invisible.

**Theorem.** No such rectangle exists with \(x<230\). At \(x=230\), the set of all possible positive integer lower-left ordinates is exactly
\[
y\equiv 759044\quad\text{or}\quad781724\pmod{1540770}.
\]
Thus the first rectangle in lexicographic order of the lower-left corner is \((230,759044)\). In particular this is an unconditional existence example for a larger invisible rectangle than the \(2\times2\) ones tabulated in the motivating polynomial-visibility investigation.

## Assumptions and scope

All coordinates and polynomial evaluation parameters are positive integers. An intermediate point must have strictly smaller positive abscissa \(t<x\); the displayed divisibility is equivalent to \(yP(t)/P(x)\) being an integer. The result refers to the exact polynomial \(P(t)=t(t+1)\), to a rectangle with two *consecutive abscissae* and three *consecutive ordinates*, and to lexicographic rather than Euclidean radial minimization. It does not assert anything about the least \(3\times3\) square or rectangles for different polynomials.

## Proof

For \(x\ge2\), define the finite obstruction-modulus set
\[
D_x=\left\{\frac{x(x+1)}{\gcd(x(x+1),t(t+1))}:1\le t<x\right\}.
\]
Then \((x,y)\) is invisible exactly when at least one modulus in \(D_x\) divides \(y\). Replacing \(D_x\) by its divisibility-minimal antichain \(A_x\) does not change that disjunction: every discarded modulus is divisible by a retained one. The condition that *both* points \((x,y)\) and \((x+1,y)\) are invisible is therefore equivalent to \(L\mid y\) for some member of
\[
B_x=\{\operatorname{lcm}(d,e):d\in A_x,\ e\in A_{x+1}\}.
\]

It follows that the full rectangle exists above \(x\) exactly when there are \(L_0,L_1,L_2\in B_x\) such that the congruences
\[
y\equiv0\pmod{L_0},\qquad
 y\equiv-1\pmod{L_1},\qquad
 y\equiv-2\pmod{L_2}
\]
are simultaneously soluble. The generalized Chinese remainder theorem makes the necessary-and-sufficient conditions
\[
\gcd(L_0,L_1)=\gcd(L_1,L_2)=1,
\qquad \gcd(L_0,L_2)\mid2.
\]
This finite criterion is valid for every positive \(x\). For \(x=1\), invisibility is impossible by definition.

The exact exhaustive computation in `verify.py` loops over every \(x=2,\ldots,229\), forms all distinct \(D_x\), removes only elements divisible by smaller elements, constructs every member of \(B_x\), and tests *all* triples in \(B_x^3\) against the three gcd conditions. It finds none. In particular, the absence of a rectangle below the stated abscissa is certified independently of any bound on \(y\). The source code consists exclusively of finite integer loops and arithmetic; no randomized algorithm, floating-point threshold, or incomplete search is used.

For the next abscissa the exact minimal-modulus antichains are
\[
A_{230}=\{11,23,105\},\qquad
A_{231}=\{7,22,58,87,319\}.
\]
Enumerating their fifteen possible least-common-multiple values produces exactly two admissible ordered triples:
\[
(L_0,L_1,L_2)=(22,105,1334),\quad(1334,105,22).
\]
The Chinese remainder theorem gives respectively \(y\equiv759044\) and \(y\equiv781724\pmod{1540770}\). Every such ordinate makes all six points invisible. Since the two classes exhaust all possible triples, the classification of ordinates at \(x=230\) is complete.

For independent explicit existence checks at \(y=759044\), the intermediate abscissae \(t\) may be chosen as follows: for \(x=230\) and successive ordinate offsets \(j=0,1,2\), take \(t=69,22,209\); for \(x=231\), take \(t=174,87,132\). Each satisfies the required divisibility by direct integer arithmetic. Hence \(759044\) is the least positive ordinate at the least possible abscissa, finishing the proof.

## Verification

Execute `python3 verify.py`; optionally compile `verify_independent.cpp` with a C++17 compiler and run the executable. Both verify all abscissae below \(230\) and the exact two admissible modulus triples at \(230\); the Python code additionally computes both complete residue classes using a generalized CRT calculation and checks the defining divisibility for all six points in both classes. The C++ program independently reconstructs the obstruction moduli by integer gcd and performs direct six-point checks.

The finite enumeration is an exhaustive proof because the reduction to obstruction moduli and the CRT compatibility criterion are proved above; it does not make any claim based on sampling ordinates alone.

## Relationship to prior work

Chahat Ahuja, *Visibility of Lattice Points across Polynomials*, arXiv:2601.15877 (first posted January 22, 2026), develops the fixed-polynomial visibility definition and in Section 4 records \(2\times2\) invisible blocks, including \((13,195)\) for \(t(t+1)\). Its conclusion explicitly proposes investigation of larger blocks and their minimal locations. The present theorem classifies the first \(2\times3\) rectangle for that concrete polynomial; its result is not implied by an example of a smaller \(2\times2\) block.

Nolan Murphy, Lauren Schmiedeler and Ellen Stonner, *First Occurrence and Frequency of Invisible Lattice Point Patterns*, study the classical *linear* visibility condition \(\gcd(x,y)>1\), including rectangular patterns. Their results do not determine the present polynomial-visibility invariant. In fact, the corner rectangle proved here contains the classically visible point \((231,759046)\), whose coordinate gcd is \(1\). The arithmetic problem is genuinely distinct even though similar CRT mechanisms occur in both.

## Limitations

The numerical boundary is a finite exact classification, not a theorem on asymptotic densities or all rectangular sizes. The general CRT criterion is elementary; the nontrivial additional content is the exhaustive first-coordinate obstruction and complete two-class classification at the boundary. Searches of indexed mathematical records cannot exclude all historical unpublished or unindexed solutions, and a separate independent scholarly audit has not been performed.

## References

1. Chahat Ahuja, *Visibility of Lattice Points across Polynomials*, arXiv:2601.15877, version 1, January 22, 2026, especially Sections 3 and 4, https://arxiv.org/abs/2601.15877.
2. Nolan Murphy, Lauren Schmiedeler, Ellen Stonner, *First Occurrence and Frequency of Invisible Lattice Point Patterns*, https://www.siam.org/media/i1thfsyh/s136404pdf.pdf, especially the introduction, Tables 2.1 and 4.1, and Section 4.
3. Sneha Chaubey, Ashish Kumar Pandey, Shvo Regavim, *On the density of visible lattice points along polynomials*, arXiv:2109.08431, https://arxiv.org/abs/2109.08431.
