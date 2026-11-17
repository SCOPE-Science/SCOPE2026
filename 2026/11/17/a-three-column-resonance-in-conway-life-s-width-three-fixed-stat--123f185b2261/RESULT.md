# A three-column resonance in Conway Life's width-three fixed-state spectrum

## Finding

On the labelled periodic Moore lattice with three rows and \(n\ge3\) columns, let \(N_n\) denote the number of configurations fixed after one synchronous update of the standard binary Conway Life rule B3/S23. Define
\[
P(x)=x^{10}-x^9-x^8-14x^7+6x^6+63x^4-63x^3-81x+243.
\]
There is an explicitly specified nonnegative primitive integer matrix \(B\) of size ten (below) with characteristic polynomial \(P\), such that **for every** integer \(n\ge3\),
\[
\boxed{N_n=\operatorname{tr}(B^n)+3^{n+1}\mathbf{1}_{\{3\mid n\}}.} \tag{1}
\]
The Perron eigenvalue \(\lambda\) of \(B\) lies strictly between \(2.70\) and \(2.71\), numerically \(\lambda\simeq2.7036317883\). Consequently the two residue regimes have distinct precise leading scales:
\[
\boxed{N_n\sim\begin{cases}3^{n+1},&3\mid n,\\\lambda^n,&3\nmid n,\end{cases}\quad(n\longrightarrow\infty).} \tag{2}
\]
Thus finite-width fixed-point populations exhibit an exact length-three arithmetic resonance: along divisible circumferences the growth base is three, while along the other two residue classes it is about \(2.704\). The spatial periodic-point growth limsup is still \(\log 3\); (2) concerns the distinct subsequential rates, not nonexistence of spatial entropy. The initial counts for \(n=3,4,5,6,7,8,9,10\) are respectively \(127,39,121,2595,1177,2919,66151,22143\).

## Assumptions and scope

The sites are \((r,j)\in(\mathbb Z/3\mathbb Z)\times(\mathbb Z/n\mathbb Z)\), with \(n\ge3\); both axes are periodic, and the eight Moore neighbors of each site are the sites \((r+u,j+v)\) for \(u,v\in\{-1,0,1\}\) other than \((u,v)=(0,0)\). For \(n\ge3\) these are eight **distinct** vertices. A live site survives exactly when it has two or three live neighbors; a dead site becomes live exactly when it has three live neighbors. Vertices are individually labelled, and configurations are not identified modulo rotation, translation, or reflection. The word *fixed* means unchanged by a **single temporal update**, not just stationary modulo a spatial shift.

Let \(b_j\in\{0,1,2,3\}\) denote the number of live sites in column \(j\). At a fixed column count \(b\), the \(\binom{3}{b}\) possible placements of live sites have identical viability conditions: each live site sees \(a+b+c-1\) live neighbors and each dead site sees \(a+b+c\), where \(a\) and \(c\) are the neighboring column counts.

## Proof

**Local criterion.** For a triple \((a,b,c)\) of consecutive column counts, put \(u=a+c\). The Life survival/birth conditions are equivalent to the following exhaustive cases:
\[
\begin{array}{c|l}
b&\text{condition}\,\\\hline
0&u\ne3\\
1&u=3\\
2&u=2\\
3&u\in\{0,1\}.
\end{array}\tag{3}
\]
For \(b=0\), a dead cell must not see exactly three neighbors. For \(b=3\), a live cell sees \(u+2\) neighbors and must have two or three. For \(b=1\) or \(2\), the simultaneous survival of a live cell and nonbirth at a dead cell forces \(a+b+c=4\), giving the middle two cases. The orientation of individual live cells is irrelevant to (3).

**Weighted transfer and exact spectrum.** Index a sixteen-state integer matrix \(T\) by ordered pairs \((a,b)\in\{0,1,2,3\}^2\). Set
\[
T_{(a,b),(b',c)}=\begin{cases}\binom{3}{b},&b=b'\text{ and }(a,b,c)\text{ satisfies (3)},\\0,&\text{otherwise}.\end{cases}\tag{4}
\]
A cyclic closed walk in \(T\) of length \(n\) specifies exactly a cyclic column-count sequence. The product of edge weights is \(\prod_j\binom3{b_j}\), precisely the number of ordered column arrangements realizing that sequence. Thus for all \(n\ge3\),
\[
N_n=\operatorname{tr}(T^n).\tag{5}
\]
Write the index of \((a,b)\) as \(4a+b\) and take \(B\) to be the principal submatrix of \(T\) on indices \(\{0,1,2,3,4,7,8,10,12,13\}\), in that order. The other recurrent component consists of indices \(\{5,6,9\}\). It is a directed three-cycle, each edge having weight three. All three remaining singleton components are acyclic. Therefore an exact block-triangular decomposition (or direct determinant calculation) gives
\[
\boxed{\det(xI_{16}-T)=x^3(x^3-27)P(x).}\tag{6}
\]
Equivalently the ten-state block has \(\det(xI_{10}-B)=P(x)\). Because the nonzero eigenvalues of the weighted three-cycle are three times the cube roots of unity, its contribution to the trace is \(3^{n+1}\) precisely when \(3\mid n\), and zero otherwise. The three acyclic singleton components contribute zero to positive powers. Combining (5) and (6) proves (1).

**Two spectral scales.** The support digraph of \(B\) is strongly connected; it contains a self-loop at the state \((0,0)\), so it is primitive. The positive vector, indexed in the displayed order of the ten states,
\[
v=(740,261,1000,456,539,235,812,901,635,598)^\mathsf{T}
\]
satisfies, coordinatewise,
\[
(27/10)v<Bv<(271/100)v.\tag{7}
\]
The Perron-Frobenius theorem and its Collatz–Wielandt bounds therefore give \(2.70<\lambda<2.71<3\). The eigenvalue \(\lambda\) is algebraically simple and all other eigenvalues of \(B\) have strictly smaller modulus. Taking traces of positive powers yields \(\operatorname{tr}(B^n)=\lambda^n(1+o(1))\). In residue classes divisible by three, the term \(3^{n+1}\) dominates; in the others, it vanishes. This proves (2). The root location is also verified by an exact Sturm count for \(P\) in \((2.70,2.71)\).

## Verification

The self-contained program `verify_transfer.py` (Python 3 with SymPy) constructs all sixteen states from (3)-(4), checks the strongly connected components, computes the **entire characteristic polynomial** with exact integer arithmetic, verifies the ten-state factor and inequality (7), isolates the indicated real root, and checks trace populations through width sixteen. `transfer_output.txt` records its executed output.

A separately implemented `verify_direct.cpp` (C++17) constructs all eight Moore-neighbor masks directly from vertex coordinates, checks that each mask has exactly eight sites, and enumerates **every** binary configuration for widths three through seven. `direct_output.txt` records its output. This independent calculation matches the predicted populations \(127,39,121,2595,1177\). Both verification programs were executed from the delivered standalone source files. The finite checks corroborate the general proof; the proof's unlimited-width assertion rests on the explicit local criterion and matrix identity, not finite simulation alone.

## Relationship to prior work

Conway's Life B3/S23 still-life condition is classical. Jen (1988) supplied a general transfer-matrix trace framework for cellular automata on periodic cylinders; the transfer principle in (4)-(5) is not claimed as new. Eppstein (2009) surveys Life-like semi-totalistic rules and their qualitative growth and decay, rather than the fixed-state count for a three-row periodic Moore strip. The maximum-density still-life optimization studied by Chu, Stuckey, and García de la Banda (2009) uses finite square domains and dead exterior cells, not exact all-width toroidal fixed-state populations.

Related published analyses of three-row periodic lattices cover either three-color cyclic threshold dynamics on the eight-neighbor Moore torus or binary neighbor-majority on the four-regular Cartesian cylinder. Their objects have different local rules; neither implies the B3/S23 transition criterion (3) or the factor \(x^3-27\) here. The substantive object-specific contribution is the compression to sixteen weighted states and **the explicit competing primitive and resonant spectral components**, with exact polynomial and two subsequential exponential scales. Ordinary still-life object counts by live-cell population on the infinite plane are not this labelled toroidal count.

## Limitations

The result counts immediate one-step fixed configurations only. It does not assert global convergence, enumerate temporal oscillators, specify attraction basins, count finite-plane strict still lifes, or extend to other strip heights. The transfer identity assumes \(n\ge3\); shorter repeated-neighbor conventions are excluded. The explicit characteristic polynomial is exactly reproducible with SymPy but has not been independently human-certified. Prior literature employing generic transfer methods may contain overlooked equivalent specializations, so historical priority is qualified.

## References

1. D. Eppstein, *Growth and Decay in Life-Like Cellular Automata*, arXiv:0911.2890v1, first posted 15 November 2009, https://arxiv.org/html/0911.2890 and https://arxiv.org/abs/0911.2890.
2. E. Jen, *Cylindrical Cellular Automata*, Communications in Mathematical Physics **118** (1988), 569–590, DOI:10.1007/BF01221109, https://doi.org/10.1007/BF01221109.
3. G. Chu, P. J. Stuckey, and M. García de la Banda, *Using Relaxations in Maximum Density Still Life*, 2009, https://users.monash.edu/~mbanda/papers/cp09-sl.pdf.
4. S. P. Banks and S. Djirar, *Fixed Points and Shift Cycles in Cellular Automata*, research report, 1992, https://eprints.whiterose.ac.uk/id/eprint/79286/.
