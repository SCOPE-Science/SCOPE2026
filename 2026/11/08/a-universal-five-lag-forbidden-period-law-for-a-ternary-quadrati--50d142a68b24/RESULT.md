# A universal five-lag forbidden-period law for a ternary quadratic permutation

## Finding

For each integer \(k\ge 2\), let \(T_k:(\mathbb F_3)^k\to(\mathbb F_3)^k\) be the polynomial permutation
\[
T_k(w_0,\ldots,w_{k-1})=(w_1,\ldots,w_{k-1},\,w_0+w_{k-1}^{2}).
\]
The exact fixed-point count at five times the memory length is
\[
\boxed{\#\operatorname{Fix}(T_k^{5k})=1\qquad\text{for every integer }k\ge2.}
\]
The fixed state is \((0,\ldots,0)\). Equivalently, there is **no nonzero orbit whose least period divides \(5k\)**. This is a uniform period exclusion, in contrast to the numerous nonzero states of period dividing \(4k\) counted in the motivating article.

## Assumptions and scope

All operations are in the field \(\mathbb F_3=\{0,1,2\}\). The exponent \(5k\) means exactly \(5k\) iterations of the indicated state map, with no assumption on the initial state. A state fixed by \(T_k^{5k}\) may have any least period dividing \(5k\); the assertion rules out all such nonzero states. The condition \(k\ge2\) follows the parameter range of the motivating recurrence. No probabilistic or genericity assumptions are made.

## Proof

**Step 1: Convert a fixed state into a cyclic word.** The map is invertible: from \((v_0,\ldots,v_{k-1})=T_k(w)\), recover \(w_i=v_{i-1}\) for \(1\le i<k\) and \(w_0=v_{k-1}-v_{k-2}^2\). A state fixed by \(T_k^{5k}\) is therefore equivalent to a two-sided \(5k\)-periodic word \((x_n)_{n\in\mathbb Z}\) with
\[
x_n=x_{n-k}+b_{n-1},\qquad b_n=\mathbf1_{\{x_n\ne0\}}=x_n^2\in\{0,1\}.
\]

**Step 2: Each five-row column is either zero or has exactly two zeros.** Arrange a period in a cyclic array with five rows and \(k\) columns: \(c_{j,t}=x_{j+tk}\), where \(0\le j<k\) and \(t\in\mathbb Z/5\mathbb Z\). For \(j\ge1\), the recurrence gives
\[
c_{j,t}-c_{j,t-1}=\mathbf1_{\{c_{j-1,t}\ne0\}}.
\]
For \(j=0\), the right side is \(\mathbf1_{\{c_{k-1,t-1}\ne0\}}\). Thus the passage from one column to the next uses the nonzero mask of the preceding column, with a cyclic row rotation only at the wraparound. Summing the five increments in any column gives zero in \(\mathbb F_3\). Hence the preceding column has a multiple of three nonzero entries. As it contains five entries, that number is either \(0\) or \(3\). Every column consequently is all zero or has exactly three nonzero entries and two zeros.

If one column is all zero, the next column has all increments zero and is constant. A constant nonzero column would have five nonzero entries, which is impossible. Thus the next is zero, and repeated propagation around all \(k\) columns makes the entire word zero. We henceforth assume there is no all-zero column; every column then has exactly two zeros.

**Step 3: The five-step zero-pattern lemma.** Suppose \(b=(b_0,\ldots,b_4)\in\{0,1\}^5\) has exactly three ones, and \(y=(y_0,\ldots,y_4)\in(\mathbb F_3)^5\) obeys the cyclic difference equations
\[
y_{t+1}-y_t=b_t\qquad(t\bmod5).
\]
The two zero positions of \(b\) are either adjacent or nonadjacent on the five-cycle. Set \(s_0=0\) and \(s_t=\sum_{i=0}^{t-1}b_i\pmod3\) for \(1\le t\le4\). Every possible solution has \(y_t=s_t+c\) for a constant \(c\in\mathbb F_3\). Since \(\sum b_t=3\), this construction satisfies the cyclic closing equation.

If the two zero positions of \(b\) are adjacent, the five values \(s_t\) have multiplicities \((3,1,1)\) among the three residues; if they are nonadjacent, the multiplicities are \((2,2,1)\). These two cases follow simply by traversing the three successive unit increments and inserting the two zero increments either together or in separate gaps; cyclic rotation of the five steps does not change the multiplicities. Thus \(y\) can have **exactly two zeros only when the two zeros of \(b\) are nonadjacent**. In that case every residue attained twice occurs at consecutive positions, because the equal adjacent values are precisely those separated by one of the zero steps of \(b\). Therefore **the two zeros of \(y\) are adjacent**.

The same conclusion holds if the input mask \(b\) is cyclically rotated, since adjacency of its zero positions is preserved.

**Step 4: Contradiction around the cyclic array.** Every column has exactly two zeros. Applying Step 3 to the transition from each column to the next forces each source column to have *nonadjacent* zeros and each target column to have *adjacent* zeros. Every column is both a source and a target, even across the row-rotated wraparound, so this is impossible. Hence only the all-zero cyclic word exists. The all-zero state is indeed fixed, proving the assertion for every \(k\ge2\).

## Verification

The standalone `verify.py` checks the decisive finite five-row lemma exhaustively: it enumerates all ten two-zero masks and the three additive offsets for their possible successors, finding ten admissible transitions. Every such transition starts with two nonadjacent zeros and ends with two adjacent zeros; the corresponding ten-state transition matrix has square zero. This is a complete certificate for the local lemma, not an enumeration of infinitely many memory lengths.

As an independent finite check of the global conclusion, the same script enumerates every one of the \(3^k\) initial states for each \(2\le k\le10\) and confirms that exactly one is fixed after \(5k\) iterations. The unrestricted theorem is proved by the preceding structural argument, not by those finite tests. Run `python3 verify.py` from a directory containing the supplied script.

## Relationship to prior work

Steven Finch, *Three Quadratic Recurrences Modulo 3: What We Can Prove and What We Can Guess*, arXiv:2610.34300v1 (first public posting 25 October 2026), introduces this same polynomial permutation in Proposition 7. Its Theorem 8 computes the number of fixed states of \(T_k^{4k}\), and its Section 5 summarizes that coverage. The exact \(5k\)-period exclusion proved above is not stated there. It is not a corollary of the \(4k\)-fixed-point census alone: a period dividing \(5k\) need not divide \(4k\), and the numerical count at one exponent supplies no upper bound at the other without an additional argument. The present argument uses a five-row adjacency obstruction in place of the four-row zero-position walk.

## Limitations

The theorem is specific to the characteristic-three square map and to periods dividing five times the memory length. It does not classify other period multipliers or the full cycle structure of \(T_k\), and it does not assert anything about periods of a separately specified initial seed beyond the stated exclusion. Although searches found no equivalent exact result, an implicit older classification of this local symbolic-dynamics condition remains a historical-priority risk. In particular, the abstract of Cassaigne and Finch (1995) describes a ternary quadratic recurrence in a different application, but its accessible mathematical text was insufficient for a complete comparison. The supplied finite tests are not independent validation of the unrestricted proof.

## References

1. S. Finch, *Three Quadratic Recurrences Modulo 3: What We Can Prove and What We Can Guess*, arXiv:2610.34300v1, https://arxiv.org/html/2610.34300v1, first public posting 2026-10-25, especially Proposition 7 and Theorem 8.
2. J. Cassaigne and S. R. Finch, *A Class of 1-Additive Sequences and Quadratic Recurrences*, Experimental Mathematics 4 (1995), 49–60, doi:10.1080/10586458.1995.10504307 (partial-access historical context; priority not resolved).
