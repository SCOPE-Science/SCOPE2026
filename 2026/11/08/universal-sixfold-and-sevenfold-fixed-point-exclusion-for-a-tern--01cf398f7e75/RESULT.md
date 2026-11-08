# Universal sixfold and sevenfold fixed-point exclusion for a ternary quadratic permutation

## Finding

For every integer \(k\ge2\), consider the bijection of \((\mathbb F_3)^k\)
\[
T_k(w_0,\ldots,w_{k-1})=(w_1,\ldots,w_{k-1},\,w_0+w_{k-1}^2).
\]
The only fixed point of either iterate \(T_k^{6k}\) or \(T_k^{7k}\) is the zero state:
\[
\boxed{\operatorname{Fix}(T_k^{6k})=\operatorname{Fix}(T_k^{7k})=\{0\}\quad(k\ge2).}
\]
Thus **no nonzero cycle has least period dividing \(6k\) or \(7k\)**, uniformly in the lag. The exclusion is sharply bracketed by the known structured behavior at the fourth multiple and the concrete eighth-multiple example: \(T_2\) has one fixed point and one eight-cycle, so \(|\operatorname{Fix}(T_2^8)|=|\operatorname{Fix}(T_2^{16})|=9\). The analogous exclusion at the fifth multiple is not part of the new claim.

## Assumptions and scope

Arithmetic is in \(\mathbb F_3\), and \(k\) ranges over all integers at least two. The indicator \(b(z)\) is \(1\) when \(z\ne0\), and \(0\) otherwise, so \(z^2=b(z)\) in \(\mathbb F_3\). Fixed by \(T_k^{mk}\) means period dividing \(mk\), not necessarily least period \(mk\). A binary support mask lists the positions of nonzero elements of a ternary column. Rotations of masks are treated as equivalent solely for the combinatorial obstruction, not as identifications of distinct states.

## Proof

**1. Column decomposition.** Because \(T_k\) is a permutation (its first coordinate is recovered by subtracting the square of the last input), every state fixed by \(T_k^{mk}\) extends to a two-sided period-\(mk\) sequence satisfying
\[
x_n=x_{n-k}+b(x_{n-1}).\]
Arrange one period as an \(m\)-row, \(k\)-column matrix \(y_{j,t}=x_{tk+j}\) for \(0\le j<k\), \(t\in\mathbb Z/m\mathbb Z\). Let \(B_j(t)=b(y_{j,t})\), and set \((Dy)_t=y_t-y_{t-1}\). For \(j\ge1\) the recurrence says \(Dy_j=B_{j-1}\). For \(j=0\), it says \(Dy_0(t)=B_{k-1}(t-1)\). Summing the difference in each column modulo three proves that *every* binary mask \(B_j\) has Hamming weight divisible by \(3\), including the wrap column.

**2. An exact finite mask graph.** For fixed \(m\), make a directed graph whose vertices are binary masks of length \(m\) and weight divisible by \(3\), taken modulo cyclic rotation. An edge from a mask \(B\) to \(C\) exists when a ternary word \(y\in\mathbb F_3^m\) satisfies \(Dy=B\), and its nonzero-support mask is \(C\), which must also have weight divisible by \(3\). The construction commutes with rotation. Every period-\(mk\) solution therefore gives a closed walk of length \(k\) in this quotient graph: successive columns give edges, and the last-to-first step is a rotation of the source mask. This implication is valid even when the solution's least period is a proper divisor of \(mk\).

The graph is computed without search heuristics. For a binary word \(B=(b_0,\ldots,b_{m-1})\) whose weight is divisible by three, the **only** solutions of \(Dy=B\) are the three words
\[
y_t=a+\sum_{i=1}^{t}b_i\pmod3,\qquad a\in\{0,1,2\},\quad0\le t<m.\]
The equation at \(t=0\) follows from \(\sum_t b_t=0\pmod3\). Compute each support, reject supports whose weight is not divisible by three, and choose the lexicographically least rotation. Exhaustively doing so for all \(22\) admissible length-six masks and all \(43\) admissible length-seven masks yields the following **complete** quotient adjacency tables. Strings are literal support masks; \(\varnothing\) means no permitted successor.

For \(m=6\):

| Source | Successors |
|---|---|
| `000000` | `000000`, `111111` |
| `000111` | \(\varnothing\) |
| `001011` | `000111` |
| `001101` | `000111` |
| `010101` | \(\varnothing\) |
| `111111` | \(\varnothing\) |

For \(m=7\):

| Source | Successors |
|---|---|
| `0000000` | `0000000` |
| `0000111` | `0111111` |
| `0001011` | `0000111`, `0111111` |
| `0001101` | `0000111`, `0111111` |
| `0010011` | `0111111` |
| `0010101` | \(\varnothing\) |
| `0111111` | \(\varnothing\) |

Both graphs have **only one directed cycle**, the all-zero self-loop. Indeed, in the six-row graph every nonzero vertex is a sink or points directly to a sink. In the seven-row graph every nonzero vertex reaches a sink in at most two steps. Neither graph has any arrow from a nonzero vertex to the zero vertex. Thus every closed walk is the all-zero walk. All the \(B_j\) are zero and therefore all \(y_{j,t}\) are zero. Conversely the zero state is fixed, proving the theorem for every \(k\ge2\).

**3. Endpoint check.** For \(k=2\), the permutation on nine states has one fixed point and an eight-cycle (or directly iterate its nine states). Thus nonzero fixed points exist at iterates \(4k=8\) and \(8k=16\); the two exclusions are nontrivial and fall strictly between these multiples.

## Verification

The standalone `verify.py` computes each quotient adjacency table twice, once by all admissible binary masks and their three additive lifts, and independently by scanning all \(3^m\) ternary column words and forming their cyclic differences. It checks equality with both printed adjacency tables and proves by graph pruning that there is no nonzero directed cycle. A separate direct iterate check enumerates all \(3^k\) states for \(2\le k\le9\), verifying that each of the two iterates fixes exactly one state. The code verifies the eight-cycle endpoint for \(k=2\). All arithmetic is exact integers modulo three. The infinite-\(k\) conclusion comes from the finite-mask-graph proof, not the bounded direct state tests.

Run: `python3 verify.py`.

## Relationship to prior work

Finch (2026), *Three Quadratic Recurrences Modulo 3*, Section 3, establishes invertibility and gives an exact count at iterate \(4k\), not at the sixth and seventh multiples. The nearby fifth-multiple exclusion is not claimed here. The 1995 Cassaigne–Finch paper studies a different ternary quadratic recurrence arising from 1-additive sequences, so its stated results do not imply this two-multiplier exclusion. OEIS A112684 tabulates eventual periods for a prescribed initial word, not all \(3^k\) starting states or these universal iterate fixed sets. Neither the known fourth-multiple count nor one special-seed period table implies the stated sixth- and seventh-multiple vanishing.

## Limitations

No claim is made about the complete period spectrum or the length of the cycle through the distinguished initial state. This statement excludes **periods dividing** \(6k\) or \(7k\); it does not exclude all numerical period lengths lying between \(4k\) and \(8k\). The finite automaton is exhaustive for the two stated multipliers only, not for every multiplier. An unindexed earlier equivalent argument may exist. Independent mathematical audit has not been performed.

## References

- Steven Finch, *Three Quadratic Recurrences Modulo 3: What We Can Prove and What We Can Guess*, arXiv:2610.34300v1 (first public 2026-10-25), https://arxiv.org/abs/2610.34300 . Section 3, Proposition 7 and Theorem 8.
- Julien Cassaigne and Steven R. Finch, *A Class of 1-Additive Sequences and Quadratic Recurrences*, Experimental Mathematics 4 (1995), 49–60, DOI 10.1080/10586458.1995.10504307, https://projecteuclid.org/journals/experimental-mathematics/volume-4/issue-1/A-class-of-1-additive-sequences-and-quadratic-recurrences/em/1062621142.pdf .
- OEIS A112684, https://oeis.org/A112684 .
