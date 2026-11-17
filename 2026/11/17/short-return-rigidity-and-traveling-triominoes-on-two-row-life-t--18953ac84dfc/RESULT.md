# Short-return rigidity and traveling triominoes on two-row Life tori

## Finding

Let \(F_n\) denote synchronous Conway B3/S23 evolution on the labelled \(2\times n\) periodic square lattice, \(n\ge3\), using **eight offset occurrences** in the Moore neighborhood. In particular, on a two-row torus the offsets immediately above and below a site coincide as positions but are each counted once; the same convention applies to both diagonal offset pairs. Let \(L_n\) be the Lucas sequence, \(L_0=2\), \(L_1=1\), \(L_{n+2}=L_{n+1}+L_n\).

For every integer \(n\ge3\),

\[
\#\operatorname{Fix}(F_n)=L_n+2+(-1)^n+2\cos(\pi n/3),
\]

\[
\#\operatorname{Fix}(F_n^2)=L_n+2+(-1)^n+2\cos(\pi n/3)+12\mathbf1_{4\mid n}.
\]

Consequently exactly six *primitive temporal two-cycle orbits* occur when \(4\mid n\), and no primitive temporal two-cycle occurs for any other circumference. The twelve distinct temporal-two configurations, when they exist, are precisely the four cyclic spatial translates of each repeating four-column word `0033`, `0132`, and `0231`, where digit \(c=a+2b\) represents a column with top entry \(a\) and bottom entry \(b\).

Nevertheless, for every \(n\ge5\) there is an explicit traveling three-cell configuration of least temporal period \(2n/\gcd(n,2)\). Thus genuine two-cycles are uniformly bounded in number, while other temporal periods become arbitrarily large.

## Assumptions and scope

The state is a pair of binary rows \(a_i,b_i\in\{0,1\}\), indexed by \(i\in\mathbb Z/n\mathbb Z\), and every site updates simultaneously. The upper site's live-neighbor count is

\[
N_i^a=a_{i-1}+a_{i+1}+2(b_{i-1}+b_i+b_{i+1});
\]

the lower site's count is obtained by interchanging \(a,b\). A dead site becomes live if its count is three; a live site survives if its count is two or three. These counts deliberately use eight distinct **offsets**, not the number of distinct vertices of the quotient graph. The case \(n=2\), in which horizontal offsets also coincide, is not claimed. States are labelled by their column indices and are not quotiented by translation, reflection, or row exchange. The first two formulas count configurations fixed under exactly one and exactly two updates respectively, not all eventual attractors.

## Proof

**Local recoding.** Encode a column as \(c_i=a_i+2b_i\in\{0,1,2,3\}\). Let \(\ell(u,v,w)\) be the updated middle column computed from the two neighbor-count formulas above. This is an explicit map from \(\{0,1,2,3\}^3\) into \(\{0,1,2,3\}\), obtained by testing the two birth/survival conditions independently.

**Fixed-state transfer.** Form the directed graph \(G_1\) on all 16 two-column words \((u,v)\), with edge \((u,v)\to(v,w)\) exactly when \(\ell(u,v,w)=v\). Every cyclic \(n\)-column fixed configuration corresponds bijectively to a length-\(n\) closed walk with a marked starting vertex. Explicit enumeration of all \(4^3=64\) triples gives 23 edges. The graph has exactly three strongly connected components containing a directed cycle: the singleton `00`, the two-cycle of pairs `03`,`30`, and the four-vertex component of pairs `11`,`12`,`21`,`22`. All other components are acyclic and cannot appear in closed walks. In the displayed four-vertex order the adjacency matrix is

\[
B=\begin{pmatrix}1&1&0&0\\0&0&0&1\\1&0&0&0\\0&0&1&1\end{pmatrix},
\qquad
\det(zI-B)=(z^2-z-1)(z^2-z+1).
\]

The eigenvalues of \(B\) are the two roots of each quadratic. Its trace power is \(L_n+2\cos(n\pi/3)\). The other two components contribute respectively \(1\) and \(1+(-1)^n\), proving the first formula.

**Two-step transfer and complete short-return rigidity.** Define \(G_2\) on the 256 four-column words \((u,v,w,t)\). Add \((u,v,w,t)\to(v,w,t,s)\) exactly when

\[
\ell\bigl(\ell(u,v,w),\ell(v,w,t),\ell(w,t,s)\bigr)=w.
\]

This is necessary and sufficient for the central column to return after two updates; again a marked length-\(n\) closed walk corresponds bijectively to an indexed length-\(n\) configuration fixed by \(F_n^2\), even when \(n<5\), since the column string is read cyclically. Exhaustive evaluation of the \(4^5=1024\) possible local words yields 223 directed edges. The *only* cyclic strongly connected components are the following (all words displayed at length four):

- the singleton `0000`;
- the two-cycle `0303`, `3030`;
- the ten-word component `1111`, `1112`, `1122`, `1221`, `1222`, `2111`, `2112`, `2211`, `2221`, `2222`;
- the four cyclic rotations of `0033`;
- the four cyclic rotations of `0132`;
- the four cyclic rotations of `0231`.

Every edge in each of the first three cyclic components has an unchanged central column under \(\ell\). Thus every corresponding two-step fixed configuration is already fixed after one step. Each of the remaining three components consists internally of one directed cycle of length four, and each corresponding spatial pattern changes under one step. Such a component contributes four cyclic words exactly when \(4\mid n\), and contributes none otherwise. This proves the second formula and the precise characterization of the twelve non-fixed configurations. Since each temporal two-cycle has exactly two distinct configurations, the count of primitive temporal two-cycle orbits is \(6\mathbf1_{4\mid n}\).

The finite component assertions are supported by the complete, standalone exhaustive `verify_transfer.py` certificate. It independently computes the strongly connected components by Tarjan's algorithm and by repeated directed reachability, verifies the component identities, checks the local first-step statuses and four-cycle edges, and directly checks the four-state characteristic polynomial. Its iteration ranges are explicitly all possible local words rather than a sample of circumferences.

**Unbounded-period traveling triomino.** For \(n\ge5\), let \(X_j\) have upper-row live sites \(\{j,j+1\}\) and lower-row live site \(\{j\}\), with all other sites dead. Direct substitution in the exact local rule gives

\[
F_n(X_j)=(\{j-1,j,j+1\},\{j-1\}),\qquad
F_n^2(X_j)=X_{j-2},
\]

where the displayed ordered pair lists upper and lower live-site sets. The same local check applies to \(n=5,6\) as well as \(n\ge7\). Spatial translation acts freely on this single triomino, so the smallest positive even return is at update \(2n/\gcd(n,2)\). Odd updates cannot return because they have four live sites, whereas \(X_j\) has three. The claimed least period follows.

## Verification

Run `python verify_transfer.py` and `python verify_direct.py` from their containing directory using Python 3. The first enumerates all 64 one-step and 1024 two-step local five-column possibilities; it checks 23 and 223 selected edges and computes all cyclic components with two distinct exact graph algorithms. It also evaluates an explicit four-by-four determinant. The second directly updates individual cells using all eight offsets and enumerates all \(4^n\) initial states for \(3\le n\le8\), independently comparing first- and second-return counts, then checks the proposed traveler and its least period through \(n=30\). Actual outputs are included as `transfer_output.txt` and `direct_output.txt`.

Finite direct simulations are independent checks, not an extrapolated proof. The all-circumference statements follow from the finite exhaustive local-component certificate and the symbolic return-shift argument.

## Relationship to prior work

Gardner's October 1, 1970 article introduced Conway's Game of Life. Jen (1988) established a *general* cylinder transfer-matrix framework for one-dimensional cellular automata and shifts; that method is credited here, not claimed as new. Jen's accessible abstract says that closed-form formulas are given for two-neighbor rules, not specifically this four-symbol, three-column local rule induced by a two-row Moore torus. Blok and Bergersen (1997) address how boundary conditions affect empirical scaling in Life. Buckingham and Callahan (1998) construct large-period oscillators in ordinary Life using glider-reflector mechanisms. These statements do not supply the present explicit two-row Lucas/six-phase fixed formula, the uniform twelve-state two-cycle rigidity, or the displayed short-period/long-period contrast.

Relevant nearby calculations for vertically *open* two-row cylinders and for periodic three- and four-row Life strips use different boundary multiplicities or different heights; none implies the two-row periodic formula. Database comparisons included descriptions and equivalent formulations using the terms `two-row`, `width two`, `2xN`, `toroidal`, `Moore`, `B3/S23`, `fixed`, `two-cycle`, `short-return`, and `glider`.

## Limitations

The classification concerns **immediate** temporal returns of length one or two, and exhibits an explicit family of longer-period orbits; it does not enumerate all longer-period orbits or their attraction basins. The eight-offset multiplicity convention on a two-row torus is essential. For example, replacing it by a simple quotient-neighbor graph changes the rule. Jen's full original paper and the full text of Blok and Bergersen (1997) could not be independently inspected; the former's abstract and bibliographic information, and the latter's abstract plus a full related author-authored account, were available. These are remaining historical-priority uncertainties, not gaps in the stated finite local proof. The result has not undergone independent mathematical validation.

## References

1. M. Gardner, "Mathematical Games: The fantastic combinations of John Conway's new solitaire game 'life'," *Scientific American* 223(4), 120–123 (October 1, 1970). https://doi.org/10.1038/scientificamerican1070-120.
2. E. Jen, "Cylindrical cellular automata," *Communications in Mathematical Physics* 118, 569–590 (1988). https://doi.org/10.1007/BF01221109.
3. H. J. Blok and B. Bergersen, "Effect of boundary conditions on scaling in the 'game of Life'," *Physical Review E* 55, 6249–6252 (May 1, 1997). https://doi.org/10.1103/PhysRevE.55.6249.
4. D. J. Buckingham and P. B. Callahan, "Tight bounds on periodic cell configurations in Life," *Experimental Mathematics* 7(3), 221–241 (1998). https://doi.org/10.1080/10586458.1998.10504370.
5. R. Blok, "Conway's Game of Life (2020)," author-authored explanatory model and bibliography. https://www.cs.ubc.ca/~rikblok/science/models/game_of_life/index.html.
