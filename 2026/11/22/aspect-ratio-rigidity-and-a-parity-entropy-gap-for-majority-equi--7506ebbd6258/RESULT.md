# Aspect-ratio rigidity and a parity entropy gap for majority equilibria on rectangular rook graphs

## Finding

Let \(1\le m\le n\) and let \(R_{m,n}=K_m\square K_n\), whose vertices are the \(m n\) squares of an \(m\)-by-\(n\) board; two distinct squares are adjacent when they share a row or a column. In synchronous binary open-neighbor majority updating, each square adopts its neighbors' strict majority and retains its current value on a tie. Let \(U(m,n)\) count fixed binary configurations up to **independent permutations of rows and columns**, without identifying transposes even on a square board.

Every fixed configuration has nested one-supports, hence is equivalent to a unique Ferrers matrix. Moreover, with \(t=\min(m,n)\),

\[
U(m,n)=\begin{cases}2^t,&m\equiv n\pmod 2,\\
[z^t]\big((1-z)^2-z^3\big)^{-1},&m\not\equiv n\pmod 2.
\end{cases}
\]

In particular, changing the longer side length by two does not change the symmetry-reduced equilibrium count. For opposite parities, if \(a_t=[z^t]((1-z)^2-z^3)^{-1}\), then \(a_0=1\), \(a_1=2\), \(a_2=3\) and \(a_t=2a_{t-1}-a_{t-2}+a_{t-3}\) for \(t\ge3\). The first values for \(t=1,\ldots,10\) are \(2,3,5,9,16,28,49,86,151,265\). The dominant root \(\rho\approx1.7548776662\) of \(\lambda^3-2\lambda^2+\lambda-1\) gives \(a_t=\Theta(\rho^t)\); consequently opposite-parity classes form an exponentially smaller fraction of the same-parity class count as \(t\) grows.

## Assumptions and scope

All boards are finite and labelled before quotienting, with \(m,n\ge1\). The graph is simple, without self-neighbors. Ties mean equality of counts among open neighbors and retain the incumbent bit. The quotient group is \(S_m\times S_n\), acting separately on rows and columns. This theorem classifies **one-step fixed configurations**, not basins or primitive two-cycles. Only the smaller dimension \(t\) and the parity of the dimension difference remain after quotienting. The result does not assert the same number of labelled fixed configurations for different longer dimensions.

## Proof

**1. From the voting rule to nested supports.** Write the binary board as \(X=(x_{ij})\), with row sums \(r_i\) and column sums \(c_j\), and put \(H=(m+n)/2\). A square \((i,j)\) has \(r_i+c_j-2x_{ij}\) occupied neighbors among \(m+n-2\) neighbors. It remains fixed exactly when

\[
 x_{ij}=1\Longrightarrow r_i+c_j\ge H+1,
 \qquad x_{ij}=0\Longrightarrow r_i+c_j\le H-1.
\]

Suppose two rows contained an alternating \(2\)-by-\(2\) pattern \(\begin{psmallmatrix}1&0\\0&1\end{psmallmatrix}\), on columns \(j,k\). Applying the first inequality to \((i,j)\) and the second to \((i,k)\) forces \(c_j-c_k\ge2\); the other two entries force \(c_k-c_j\ge2\), impossible. Therefore all row one-supports are comparable by inclusion. Permute rows by decreasing size and then columns by decreasing height. This gives the unique Ferrers representative \(x_{ij}=\mathbf1_{\{j\le\lambda_i\}}\), with \(n\ge\lambda_1\ge\cdots\ge\lambda_m\ge0\). Conversely any Ferrers matrix satisfying the two displayed inequalities is stable, by the original neighbor count.

**2. A two-barrier lattice-path characterization.** Draw the southeast boundary of the Ferrers diagram starting at \((0,n)\) and ending at \((m,0)\). Let \(U\) increase the processed row coordinate by one and let \(D\) decrease the current column coordinate by one. Thus there are \(m\) steps \(U\), \(n\) steps \(D\). At a boundary vertex \((i,j)\), put \(h=i+j-H\). Its initial and terminal values are \((n-m)/2\) and \((m-n)/2\); \(U\) increases \(h\) by one, and \(D\) decreases it by one.

At a turn \(U\to D\), the adjacent bottom-right occupied square has row sum \(j\) and column sum \(i\); this is the *least* occupied-neighbor sum for the corresponding constant-row-length block. At a turn \(D\to U\), the adjacent top-left unoccupied square has row sum \(j\) and column sum \(i\); this is the *greatest* unoccupied-neighbor sum for that block. Consequently the entire Ferrers board is fixed if and only if **every local peak** (turn \(U\to D\)) has \(h\ge1\) and **every local valley** (turn \(D\to U\)) has \(h\le-1\). This also covers full and empty rows and columns: they have no other potentially failing cell. No restrictions are imposed at the initial and terminal vertices.

**3. Adding two columns is an invertible stability-preserving operation.** Assume \(m\le n\). Given such an admissible word with \(m\) letters \(U\) and \(n\) letters \(D\), insert one \(D\) **before the first existing \(D\)** and one \(D\) **after the last existing \(D\)**. When \(n\) becomes \(n+2\), the initial altitude increases by one and the final altitude decreases by one. Between the two insertions all old altitudes are unchanged. A peak before the first \(D\), if present, rises one; a valley after the last \(D\), if present, falls one. Hence all barrier conditions survive. Conversely, for a valid word of dimensions \((m,n+2)\), remove the first and last \(D\). The first and last \(D\)-runs each have sufficient length that no turn disappears: their respective endpoint barriers are at least one step beyond the corresponding starting or finishing altitudes, because \((n+2-m)/2\ge1\) when the dimensions have equal parity and \(\ge3/2\) otherwise. A first peak drops by one but stays at least one, and a last valley rises by one but stays at most minus one. All other extrema remain unchanged. Thus these maps are mutually inverse and \(U(m,n+2)=U(m,n)\) for \(n\ge m\). It remains to count admissible paths at \(n=m\) and \(n=m+1\).

**4. Count the two balanced endpoint problems.** Assign a formal weight \(x\) to each \(U\) and \(y\) to each \(D\), and write \(z=xy\). All peak and valley heights are on the unit lattice if the endpoints are at height zero, or the half-integer lattice if the endpoints are \(1/2\) and \(-1/2\). An admissible path alternates between peaks at height at least \(1\) (respectively \(3/2\)) and valleys at height at most \(-1\) (respectively \(-3/2\)). For both endpoint problems, sum by the number of peaks, with no peaks counted separately.

For endpoints \(0\to0\), a peak has height \(1+a\), a valley has height \(-1-b\), where \(a,b\ge0\). The weight for an initial segment ending at peak \(a\), allowing an initial valley, is \(s_a=x^{1+a}/(1-z)\). The weight for a terminal segment starting at peak \(a\), allowing a terminal valley, is \(e_a=y^{1+a}/(1-z)\). The two-run transition from peak \(a\) to peak \(a'\) has weight

\[
 K_{a,a'}=\frac{z^2}{1-z}\,y^a x^{a'}.
\]

This is a rank-one matrix with nonzero eigenvalue \(z^2/(1-z)^2\). The no-peak paths have generating function \(1/(1-z)\); summing all one-or-more-peak paths gives \(z/((1-z)(1-2z))\). Thus the total path generating series is

\[
 F_{\rm even}(x,y)=\frac1{1-z}+\frac{z}{(1-z)(1-2z)}=\frac1{1-2z}.
\]

The coefficient of \(x^m y^m\) is \(2^m\).

For endpoints \(1/2\to-1/2\), peaks have heights \(3/2+a\) and valleys \(-3/2-b\). Now

\[
 s_a=x^{1+a}\frac{1-z+z^2}{1-z},\qquad
 e_a=\frac{y^{2+a}}{1-z},\qquad
 K_{a,a'}=\frac{z^3}{1-z}\,y^a x^{a'}.
\]

The no-peak paths contribute \(y+xy^2/(1-z)\), and the positive-peak paths contribute \(xy^2(1-z+z^2)/((1-z)((1-z)^2-z^3))\). By the same rank-one geometric series,

\[
 F_{\rm odd}(x,y)=\frac{y}{(1-z)^2-z^3}.
\]

Its \(x^m y^{m+1}\) coefficient is the stated \(a_m\). For \(n=m+1\) the endpoints have exactly these heights; step 3 extends the count to all higher widths of the same parity. Symmetry swaps \(m,n\) if necessary. This proves the theorem.

**5. Recurrence and growth.** Multiplying \(\sum_{t\ge0}a_tz^t\) by \(1-2z+z^2-z^3\) gives the stated initial values and recurrence. Its pole of smallest modulus is the simple positive zero \(\rho^{-1}\) with \(\rho\approx1.7548776662\), while the other two reciprocal roots have modulus \(<1\). Thus \(a_t=\Theta(\rho^t)\), whereas the other parity gives exactly \(2^t\).

## Verification

The standalone `verify.py` reconstructs all \(m\)-by-\(n\) Ferrers partitions for \(1\le m\le8\), \(m\le n\le14\), checks the original neighbor-majority inequality, and compares the counts to the coefficient formula. It independently enumerates all binary boundary words for \(1\le m\le6\), \(m\le n\le9\), verifies the peak/valley criterion on every word, and checks the explicit width-two bijection. Finally, it exhaustively checks the original labelled Boolean configurations for eight small boards with up to 20 squares, including \(4\)-by-\(5\), which has 116 labelled fixed states. All assertions passed. These are finite checks; the infinite-family result rests on the proof above, not on extrapolation.

## Relationship to prior work

The finite-graph two-period eventuality theorem of Goles and Olivos and the majority-dynamics framework of Benjamini et al. (arXiv:1405.2486, submitted 2014-05-11) address eventual period bounds and random-network behavior rather than enumerating fixed states on rook graphs. The existing square-rook enumeration \(2^n\) and Ferrers rigidity are prior results and are recovered at \(m=n\); the new part is an explicit **anisotropic parity-stabilization law**, a second algebraic count \(a_t\), and their proof uniformly for all rectangles. Bujtás et al. (arXiv:2608.27669, 2026) study maximum color counts of majority C-colorings on the same Cartesian products; this is a different invariant, not a count of binary fixed configurations. The opposite-parity numerical sequence is the previously indexed sequence OEIS A005314 with a shift in indexing; the integer sequence itself is not claimed new, only its natural majority-dynamical interpretation and its parity connection. Related work on three-row rook-graph transients studies maximal entrance time rather than a complete fixed-class count.

## Limitations

The quotient identifies configurations only under independent row and column permutations; additional board transposition symmetry is deliberately not imposed. The labelled fixed-state count, attraction basins, and primitive two-cycle populations are not evaluated by this theorem. The fixed-point sequence is known in unrelated combinatorial settings; an unindexed equivalence or older unpublished rook-specific enumeration cannot be excluded by literature search alone. A related published three-row rook-transient result was found only as a publicly indexed statement, not inspected in full, and should not be treated as proof of noncoverage. The present result has not undergone independent external mathematical review.

## References

- I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486 (first submitted 2014-05-11), https://arxiv.org/html/1405.2486v1 .
- C. Bujtás, M. Dettlaff, H. Furmańczyk, A. Laskowska, *Majority C-coloring in Cartesian products*, arXiv:2608.27669 (first submitted 2026-08-27), https://arxiv.org/abs/2608.27669 .
- OEIS Foundation, sequence A005314, *For n = 0, 1, 2, a(n) = n; thereafter a(n) = 2a(n-1)-a(n-2)+a(n-3)*, https://oeis.org/A005314 .
