# Complete all-on press-weight distribution on three-row Lights Out strips

## Finding
For each integer \(n\ge1\), let \(G_n=P_3\square P_n\) be the ordinary three-row rectangular grid. A *press set* \(S\subseteq V(G_n)\) solves the all-on binary Lights Out instance if toggling the closed neighborhood of each selected vertex once changes every initially lit cell to unlit. Equivalently, every closed vertex neighborhood has odd intersection with \(S\). Define its **complete solution-weight polynomial**
\[
W_n(z)=\sum_{\substack{S\subseteq V(G_n)\\|S\cap N[v]|\equiv1\pmod2\ \forall v}}z^{|S|}.
\]
Write \(n=6q+r\), with \(q\ge0\), \(0\le r\le5\), and \(n\ge1\). Then the following six formulas hold exactly:
\[
\boxed{W_n(z)=\begin{cases}
z^{10q},&r=0,\\
z^{6q+1},&r=1,\\
2z^{6q+2}+2z^{6q+4},&r=2,\\
z^{6q+5},&r=3,\\
z^{10q+10},&r=4,\\
6z^{6q+6}+2z^{10q+10},&r=5.
\end{cases}}
\]
In particular, **exactly two optimal solutions** occur when \(n\equiv2\pmod6\), **exactly six optimal solutions** occur when \(n\equiv5\pmod6\), and **exactly one** occurs in every other residue class. For \(n\equiv5\pmod6\), two further solutions have strictly greater weight, while all six optima have the same minimum cardinality. The minimum cardinalities themselves were already determined in earlier work; this theorem claims the complete weight distribution, optimizing multiplicities, and explicit periodic classification rather than rediscovering those minima.

## Assumptions and scope
The rows are \(1,2,3\), and the columns are \(1,\ldots,n\). Grid edges join cells sharing a side, not a diagonal, and there is no boundary wraparound. A press toggles its own light and each existing horizontally or vertically adjacent light; each cell is pressed at most once since two presses cancel. Press sets are distinguished as labeled cell subsets, without identifying rotations or reflections. The variable \(z\) is formal; a coefficient counts exact solutions having its exponent as number of pressed cells. In particular this is not an enumeration of all possible initial on/off patterns, nor a theorem for grids of another width.

## Proof
Work over \(\mathbb F_2\). Encode the pressed cells of column \(i\) by \(x_i\in\mathbb F_2^3\), with the top row in binary place \(2^0\), middle in \(2^1\), and bottom in \(2^2\); we identify each vector with an integer \(0,\ldots,7\). Put \(x_0=x_{n+1}=0\). Let \(B=I_3+A(P_3)\) over \(\mathbb F_2\), so in the integer encoding
\[
B(s)=s\mathbin{\mathrm{xor}}((2s)\mathbin{\mathrm{and}}7)\mathbin{\mathrm{xor}}\lfloor s/2\rfloor.
\]
Here `xor` and `and` have their ordinary binary-bit meanings. At column \(i\), each closed-neighborhood parity requirement is exactly
\[
x_{i-1}+Bx_i+x_{i+1}=(1,1,1)^T\quad\text{in }\mathbb F_2^3.
\]
Consequently each solution is determined uniquely by the first-column seed \(s=x_1\), because its subsequent columns are forced by
\[
x_{i+1}=(1,1,1)^T+Bx_i+x_{i-1},\qquad x_0=0.
\]
The seed is admissible for the width \(n\) **if and only if** the forced value \(x_{n+1}\) is zero. Thus enumerating the eight seeds is exhaustive, not probabilistic or a truncation of a larger search.

The following table lists the exact first twelve columns for all eight seeds. Each character is the binary encoding \(0,\ldots,7\) of one three-bit column. The last column gives the weight sum in each of positions \(1\) through \(6\) and \(7\) through \(12\). The table can be checked directly by the displayed recurrence, and the recurrence also gives \(x_{13}=x_1\) and \(x_{14}=x_2\) for every row. Therefore these twelve-column strings repeat indefinitely, for every seed.

| Seed \(s\) | Repeating twelve-column word | Weight of each six-column block |
|---:|:---:|---:|
| 0 | `075570075570` | 10 |
| 1 | `140330410660` | 6 |
| 2 | `205250205250` | 6 |
| 3 | `330410660140` | 6 |
| 4 | `410660140330` | 6 |
| 5 | `525020525020` | 6 |
| 6 | `660140330410` | 6 |
| 7 | `755700755700` | 10 |

Reading the positions of zero columns in the displayed words gives the exact permitted seeds by \(r=n\bmod6\):
\[
\begin{array}{c|cccccc}
r&0&1&2&3&4&5\\\hline
s&\{0\}&\{2\}&\{1,3,4,6\}&\{5\}&\{7\}&\{0,1,2,3,4,5,6,7\}.
\end{array}
\]
The equality of six-block weights implies that adding six columns increases each seed's press weight by \(10\) for seeds \(0,7\) and by \(6\) for all other seeds. Finally, the initial \(r\)-column weights of precisely the permitted seeds are, respectively, \(0\) for \(r=0\); \(1\) for \(r=1\); \(2,4,2,4\) for \(r=2\) (seeds in the order displayed); \(5\) for \(r=3\); \(10\) for \(r=4\); and \(10,6,6,6,6,6,6,10\) for \(r=5\). Multiplying each by \(z\) to its corresponding power and collecting terms proves every coefficient in the stated polynomial. No other press sets exist because every press set determines exactly one of the eight seeds. \(\square\)

## Verification
The file `verify_chase.py` reconstructs the all-on parity recurrence from the definition of binary cells, verifies the twelve-column table for all eight seeds, and independently checks the six formulas for \(1\le n\le300\). The file `verify_gauss.cpp` instead builds the full \(3n\times3n\) closed-neighborhood binary matrix, performs complete Gaussian elimination over \(\mathbb F_2\) with all free-variable choices, independently checks that each resulting press set toggles every cell exactly once modulo two, and compares the whole weight spectrum for \(1\le n\le80\). `chase_output.txt` and `gauss_output.txt` contain their actual successful outputs. These computations corroborate the algebraic proof; the infinite statement follows from the exhaustive eight-seed and period-twelve arguments, not from extrapolation.

## Relationship to prior work
Caro and Klostermeyer, *The Odd Domination Number of a Graph* (2003), Section 3, give the **minimum cardinality** for three-row grids by residue class modulo six and explain a column recurrence using eight initial vectors (pp. 73–74); those minima and the recurrence are **not new**. Caro, Goldwasser and Klostermeyer (2001), Section 4.1, explicitly acknowledge those previously known width-one through width-four minima. Minevich (2012), Sections 2–3, proves general solvability of all-on binary closed-neighborhood instances through the diagonal-in-range theorem. Goldwasser, Klostermeyer and Ware (2002) study the general Fibonacci-polynomial nullspace/solvability framework for rectangular grids. These broader results do not display the exact coefficientwise weight distribution or counts of minimizing press patterns for every three-row length. The 2003 recurrence permits their *derivation after an additional complete weight census*; the contribution here is the explicit closed and proven six-residue solution polynomial and optimizing multiplicities, not the existence of an algorithm. Known small values, including four all-on solutions for the three-by-two grid, are special cases and are not separately claimed.

## Limitations
This result is specific to all-on Lights Out on \(P_3\square P_n\); it gives no complete solution-weight distribution for arbitrary starting configurations or other widths. Standard minimum-press formulas for this same family are prior work. Only the accessible sections of the 2002 *Fibonacci Polynomials and Parity Domination in Grid Graphs* article were available through bibliographic descriptions; an unindexed or inaccessible equivalent enumeration cannot be ruled out. General finite-field algorithms can calculate this polynomial at each fixed \(n\), but that does not constitute a published closed coefficient formula for all lengths. No independent scholarly certification is claimed.

## References
1. Y. Caro and W. F. Klostermeyer, *The Odd Domination Number of a Graph*, J. Combin. Math. Combin. Comput. 44 (2003), 65–83, Section 3 and Table, open full text: https://combinatorialpress.com/article/jcmcc/Volume%20044/vol-044-paper%206.pdf .
2. Y. Caro, W. F. Klostermeyer and J. L. Goldwasser, *Odd and Residue Domination Numbers of a Graph*, Discuss. Math. Graph Theory 21 (2001), 119–136, Section 4.1. DOI: https://doi.org/10.7151/dmgt.1137 .
3. I. Minevich, *Symmetric Matrices over F_2 and the Lights Out Problem*, arXiv:1206.2973v1, first submitted 14 June 2012, https://arxiv.org/html/1206.2973v1 .
4. J. Goldwasser, W. F. Klostermeyer and H. Ware, *Fibonacci Polynomials and Parity Domination in Grid Graphs*, Graphs Combin. 18 (2002), 271–283. DOI: https://doi.org/10.1007/s003730200020 .
5. E. W. Weisstein, *Lights Out Puzzle*, MathWorld, https://mathworld.wolfram.com/LightsOutPuzzle.html (background small-board examples).
