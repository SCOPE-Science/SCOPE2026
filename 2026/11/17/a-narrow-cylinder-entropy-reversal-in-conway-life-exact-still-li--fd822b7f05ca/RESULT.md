# A narrow-cylinder entropy reversal in Conway Life: exact still-life and temporal-two spectra

## Finding

Let \(F_n\) be Conway's B3/S23 rule on a height-three array whose \(n\ge3\) columns are cyclic and whose rows outside the array are fixed dead and not updated. Denote by \(s_n\) the number of configurations fixed by one update, and by \(t_n\) the number returning to their initial configuration after two updates. These are **labelled** configurations, not orbits modulo translation or reflection.

There are explicit integer-polynomial power-sum formulas for every \(n\ge3\):
\[
s_n=\mathcal L_n(P_{14})+\mathcal L_n(P_{19}),\qquad
t_n=\mathcal L_n(P_{14})+\mathcal L_n(P_{20})+12\mathbf 1_{6\mid n},
\]
where \(\mathcal L_n(P)\) is the sum of the \(n\)th powers of all complex roots of the monic polynomial \(P\), with multiplicity. The polynomials are defined exactly in `verify_life_cylinder.py` as coefficient arrays, in descending degree. For clarity, they are also:
\[
P_{14}(u)=u^{14}-u^{11}+2u^{10}+5u^8-3u^7+2u^6-u^5+2u^3+u+1,
\]
\[
\begin{aligned}
P_{19}(u)={}&u^{19}-2u^{18}+u^{17}-7u^{16}+9u^{15}-17u^{14}+3u^{13}\\
&+12u^{12}+47u^{11}+22u^{10}+15u^9+4u^8+26u^7-8u^6\\
&-u^5+9u^4-3u^3-9u^2+5u-2,
\end{aligned}
\]
\[
\begin{aligned}
P_{20}(u)={}&u^{20}-2u^{19}+u^{18}-7u^{17}+7u^{16}-15u^{15}+3u^{14}\\
&+26u^{13}+41u^{12}+38u^{11}+25u^{10}-24u^9-20u^8\\
&-62u^7+9u^6+17u^5-27u^4-23u^3+33u^2-16u+4.
\end{aligned}
\]
The number of primitive temporal two-cycle orbits is \((t_n-s_n)/2\). In particular, for circumference \(n=3,4,5,6,7,8\), these orbit counts are respectively \(0,4,5,12,7,24\).

The positive Perron roots \(\rho_1\) and \(\rho_2\) of the fixed-state and temporal-two transfer matrices satisfy the **exact separation**
\[
\rho_1<\frac{243}{100}<\rho_2,
\]
and \(s_n\sim \rho_1^n\), \(t_n\sim\rho_2^n\). Numerically \(\rho_1\approx2.42331694\) and \(\rho_2\approx2.43740860\). Consequently, a uniformly chosen configuration from those satisfying \(F_n^2(x)=x\) is nonfixed with probability tending to one exponentially quickly as \(n\to\infty\).

## Assumptions and scope

A configuration is a function on \(\{0,1,2\}\times\mathbb Z/n\mathbb Z\) with values in \(\{0,1\}\). The first coordinate is the row. For each cell, its Moore neighbors are those at row displacement and column displacement in \(\{-1,0,1\}\), excluding displacement \((0,0)\), provided the row stays in \(\{0,1,2\}\). Column coordinates are taken modulo \(n\). A dead cell becomes live exactly for three live neighbors; a live cell survives for two or three live neighbors. For \(n\ge3\), different column displacements refer to distinct columns. There is **no vertical wraparound** and births outside the three rows are not part of the dynamical system. We do not assert these configurations remain supported within three rows under infinite-plane Life dynamics.

## Proof

Encode each column by an element of \(\{0,\ldots,7\}\), whose three bits are the row states. Define \(L(a,b,c)\) to be the 3-bit column produced at the center by the local Life rule with left/center/right column values \(a,b,c\). For any row \(r\), the live-neighbor count equals the sum of the bits in rows \(r-1,r,r+1\) of the left and right columns, plus the bits in rows \(r-1,r+1\) of the central column, omitting nonexistent rows. This defines \(L\) without any approximation.

Construct a directed graph \(A\) with vertices \((a,b)\in\{0,\ldots,7\}^2\), having an edge \((a,b)\to(b,c)\) exactly if \(L(a,b,c)=b\). A closed walk of length \(n\) uniquely records one labelled width-\(n\) fixed configuration, and conversely, so \(s_n=\operatorname{tr}(A^n)\).

For temporal-two recurrence, use a 64-letter alphabet of pairs \((a,a')\) of columns, representing time-zero and time-one columns. The directed graph \(B\) has as vertices pairs of such letters. An edge from \(((a,a'),(b,b'))\) to \(((b,b'),(c,c'))\) exists exactly when \(L(a,b,c)=b'\) and \(L(a',b',c')=b\). Thus a closed walk uniquely records a configuration \(x\) together with \(F_n(x)\), subject to \(F_n^2(x)=x\). Hence \(t_n=\operatorname{tr}(B^n)\). There are 64 vertices for \(A\), and 4096 for \(B\).

The exact finite graph certificates `verify_life_cylinder.py` compute the strongly connected components and their characteristic polynomials using only integer arithmetic and Newton identities. The only cycle-bearing component of \(A\) has 40 vertices, 94 edges and characteristic polynomial \(u^7P_{14}(u)P_{19}(u)\); the only cycle-bearing components of \(B\) have 48, 6, 6 vertices, with 112, 6, 6 edges and polynomials \(u^{14}P_{14}(u)P_{20}(u)\), \(u^6-1\), \(u^6-1\). Edges between different components cannot belong to closed walks. All non-cycle components therefore contribute zero to every positive power trace. Trace equals the sum of eigenvalue powers even for nondiagonalizable matrices; this gives both formulas.

Each large cycle-bearing component is strongly connected and contains a self-loop, hence is primitive. Let \(U\) and \(V\) be their nonnegative adjacency matrices of sizes 40 and 48, in the deterministic vertex order specified by the verifier. Starting from the all-ones integer vector, define \(v=U^{16}\mathbf1\) and \(w=V^{14}\mathbf1\). The included integer certificate checks that these vectors are strictly positive and satisfy coordinatewise
\[
100Uv<243v,\qquad 100Vw>243w.
\]
In fact, the largest entry of \(100Uv-243v\) is \(-37829\), and the smallest entry of \(100Vw-243w\) is \(16163\). The Collatz–Wielandt inequalities yield \(\rho(U)<243/100<\rho(V)\). Primitivity makes each Perron eigenvalue simple and strictly dominant in modulus, and the other two components of \(B\) have spectral radius one. The stated asymptotics follow, with leading coefficient one for the positive trace of the Perron eigenvalue. The oscillatory fraction tends to one because \(s_n/t_n\) decays exponentially.

## Verification

Run `python3 verify_life_cylinder.py` using Python 3 with no third-party dependencies. It constructs both transition graphs from the specified local rule; computes cycle-bearing strongly connected components; verifies the complete factorizations by exact integer Newton identities; verifies both strict positive-vector inequalities; and calculates the labelled counts for several ring lengths. The separate implementation `python3 crosscheck_life_cylinder.py` uses direct site-by-site Moore-neighborhood updates and checks all \(299520\) labelled configurations over circumferences \(n=3,4,5,6\). Its output appears in `direct_check.txt`; the transfer proof's output appears in `transfer_check.txt`. These finite tests supplement, but do not replace, the all-length closed-walk proof.

For \(n=3,4,5,6\), the exact pairs \((s_n,t_n)\) are \((26,26),(14,22),(102,112),(314,338)\). For \(n=7,8\), they are \((478,492),(1102,1150)\).

## Relationship to prior work

Conway's rule was publicly introduced by Gardner (1970). McIntosh's earlier work, republished as the chapters *Conway's Life* and *Life's Still Lifes* in 2010, explains de Bruijn approaches to periodic configurations and still lifes; those methods are credited. The present claim is narrower than general de Bruijn computability, but more specific: it determines the two explicit all-circumference spectra of **the vertically open, three-row cylinder** and proves their strict entropy separation. The bibliographic abstract of the chapters does not provide this precise conclusion. Because their complete text was not accessible for comparison, no claim of absolute historical priority is made.

General Life pattern databases count objects up to geometric symmetries or by live-cell population, rather than these labelled cylindrical recurrent-state counts. A related published mathematical-record result concerns three-row *cyclic-dominance* toroidal dynamics, not Life with dead vertical boundaries. Those results neither numerically determine the present three-row Life spectra nor entail this specific strict Perron-root inequality.

## Limitations

Only configurations satisfying the first or second temporal iterate are classified; no claim about initial transients, eventual periods greater than two, or all attractors is made. The vertical exterior is fixed dead and excluded from updates; this is not the same as an unbounded plane or a torus periodic in both directions. The labelled-cylinder counts use a fixed column coordinate origin. The algebraic constants are specified by exact matrices and polynomials, with decimal approximations supplied only for intuition. Prior-art priority is qualified by incomplete access to McIntosh's full 1988/2010 chapters and the possibility of older unpublished strip tables. The verification is computationally exact for the finite certificates but has not undergone independent external audit.

## References

1. M. Gardner, *Mathematical Games: The fantastic combinations of John Conway's new solitaire game Life*, Scientific American 223(4) (1970), 120–123; DOI: 10.1038/scientificamerican1070-120; publisher date 1970-10-01.
2. H. V. McIntosh, *Conway's Life*, in A. Adamatzky (ed.), *Game of Life Cellular Automata*, Springer (2010), pp. 17–33; DOI: 10.1007/978-1-84996-217-9_3. Publisher abstract notes a 1988 manuscript and de Bruijn method.
3. H. V. McIntosh, *Life's Still Lifes*, same volume, pp. 35–50; DOI: 10.1007/978-1-84996-217-9_4. Publisher abstract notes a 1988 manuscript and de Bruijn method.
4. E. W. Weisstein, *Game of Life*, MathWorld, https://mathworld.wolfram.com/GameofLife.html (definitions and object-count conventions).
