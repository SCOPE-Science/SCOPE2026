# Two coexisting fixed-state phases in the three-row Toom automaton

## Finding

Consider the deterministic north-east-center majority rule of Toom on a labelled three-row torus of horizontal circumference \(n\ge 3\). Its one-step fixed configurations divide into two disjoint classes: **every column is vertically uniform** or **every column is vertically nonuniform**. Mixed classes within a single fixed configuration are impossible.

The uniform-column class has \(2^n\) members. Every nonuniform-column fixed configuration is a cyclic walk on an oriented six-cycle with a loop at every vertex. Consequently its exact population is
\[
M_n=6\sum_{j=0}^{\lfloor n/6\rfloor}\binom{n}{6j},
\]
and the total number of fixed configurations is
\[
\boxed{S_n=2^n+6\sum_{j=0}^{\lfloor n/6\rfloor}\binom{n}{6j}.}
\]
Equivalently, for all \(n\ge3\),
\[
\boxed{S_n=2^{n+1}+2\,3^{n/2}\cos(n\pi/6)+2\cos(n\pi/3).}
\]
Both classes have the same exponential growth rate: \(M_n/2^n\longrightarrow1\) and \(S_n/2^n\longrightarrow2\). Under uniform sampling from the fixed configurations, the probability of the vertically nonuniform class approaches \(1/2\), despite the absolute prohibition on interfaces between the classes.

## Assumptions and scope

Vertices are \((r,c)\in(\mathbb Z/3\mathbb Z)\times(\mathbb Z/n\mathbb Z)\), with row and column coordinates indexed and not quotiented by translation. The binary state at vertex \((r,c)\) is \(x_{r,c}\in\{0,1\}\). One synchronous update is
\[
(Fx)_{r,c}=\operatorname{maj}(x_{r,c},x_{r+1,c},x_{r,c+1}),
\]
where \(\operatorname{maj}(a,b,e)=1\) exactly when at least two of \(a,b,e\) are one. The choice of increasing row as north and increasing column as east merely fixes orientation. The theorem counts configurations satisfying \(Fx=x\), not all stationary probability measures, general temporal cycles, or noisy dynamics. Ring lengths \(n\ge3\) and the three distinct cyclic rows are assumed throughout.

## Proof

Identify each vertical column with a three-bit integer \(a\in\{0,1,\ldots,7\}\), with row \(r\) in bit position \(r\). For a column \(a\) followed to its east by \(b\), the fixed-point condition at row \(r\) is
\[
\operatorname{maj}(a_r,a_{r+1},b_r)=a_r.
\]
If \(a_r=a_{r+1}\), this equation holds for either value of \(b_r\). If \(a_r\ne a_{r+1}\), it forces \(b_r=a_r\). Thus the allowed adjacent-column relation is exactly
\[
 a\longrightarrow b\quad\Longleftrightarrow\quad
 \forall r\in\mathbb Z/3\mathbb Z:\;
 (a_r=a_{r+1})\ \text{or}\ (b_r=a_r).
\]

If \(a\in\{0,7\}\), all three bits of \(a\) agree, so any following column is locally allowed. In particular \(0\) and \(7\) form a complete directed two-vertex graph, including loops. If \(a\) is nonuniform, the three-bit cyclic word has exactly two unequal adjacent-bit pairs, so the corresponding two bits of \(b\) are forced. The third bit may stay or flip. Checking the six possibilities gives precisely a self-loop at each nonuniform symbol and the directed cycle
\[
1\longrightarrow3\longrightarrow2\longrightarrow6\longrightarrow4\longrightarrow5\longrightarrow1.
\]
In particular, a nonuniform column can never be followed by a uniform one in a fixed configuration. On a finite cyclic column word, this implies that the presence of any nonuniform column forces every column to be nonuniform. Conversely, every cyclic word entirely in either indicated directed component satisfies all the local fixed-point equations. This proves the complete two-class decomposition, with no omitted configurations.

In the uniform component any of the two symbols can be chosen independently at each of the \(n\) indexed columns, giving \(2^n\) closed walks. In the nonuniform component, each step either stays at the current symbol or advances one position around the directed six-cycle. Exactly \(k\) advances close the walk if and only if \(6\mid k\). For each length-\(n\) choice of advance sites there are exactly six initial phase choices. The resulting count is the claimed \(M_n\), and summing the classes yields \(S_n\).

Let \(\zeta=\exp(2\pi i/6)\). The roots-of-unity filter gives
\[
6\sum_{6\mid k}\binom nk=\sum_{j=0}^{5}(1+\zeta^j)^n
=2^n+2\,3^{n/2}\cos(n\pi/6)+2\cos(n\pi/3)
\]
for all positive \(n\). Since \(\sqrt3<2\), the oscillating correction is exponentially smaller than \(2^n\). The two asymptotic statements and limiting class probability follow immediately.

## Verification

The exact local directed graph has eight symbols and 28 directed edges. Its recurrent parts consist of the two-symbol complete directed component and the six-symbol looped directed cycle. The standalone script `verify_structure.py` constructs all 64 possible ordered column pairs directly from the original majority rule, tests this decomposition, and compares trace counts with the binomial formula for lengths one through twenty. `verify_direct.cpp` independently evaluates the full synchronous update on all \(2^{3n}\) configurations for each \(3\le n\le7\), checks the class dichotomy, and matches both counts. Corresponding captured outputs are `structure_output.txt` and `direct_output.txt`. The proof above, not finite enumeration, establishes all circumferences.

Some exact values are: \(S_3=14\), \(S_4=22\), \(S_5=38\), \(S_6=76\), \(S_7=176\), \(S_8=430\), \(S_9=1022\), and \(S_{12}=9652\).

## Relationship to prior work

Toom's deterministic north-east-center majority update is classical. Makowiec's 1997 study examines ground-state patterns by simulations on periodic square lattices, and her openly available 1998 preprint examines stochastic Toom dynamics, critical exponents, interfaces, and stationary measures. Those inspected materials do not furnish this three-row all-circumference deterministic fixed-point count or the six-symbol phase decomposition. Exact fixed-point results for other local majority rules or other graphs do not imply this result, because their neighbor relations and admissible column transitions differ. The spatial two-class obstruction and the equal exponential growth of the classes constitute the asserted new result, not the general majority-rule definition or the transfer-matrix method.

## Limitations

No classification of transient configurations or periodic orbits of temporal period greater than one is claimed. The total count is on indexed tori; identifying spatial rotations would require a different Burnside count. The historical-priority comparison with the 1997 ground-state article is limited to its public abstract because full publisher text was inaccessible through the attempted sources; thus unindexed earlier finite-strip counts remain a priority risk. No independent mathematical audit has been performed.

## References

- D. Makowiec, *Ground-state configurations for Toom cellular automata: Experimental hints*, Physical Review E 56 (1997), 5195–5203, https://doi.org/10.1103/PhysRevE.56.5195 (public date 1997-11-01; abstract accessible).
- D. Makowiec, *Critical properties of Toom cellular automata*, arXiv:cond-mat/9808247, https://arxiv.org/abs/cond-mat/9808247 (first public preprint 1998-08-22; full text inspected).
- G. T. Barkema, P. L. Ferrari, J. L. Lebowitz and H. Spohn, *Kardar-Parisi-Zhang universality class and the anchored Toom interface*, Physical Review E 90 (2014), 042116, https://doi.org/10.1103/PhysRevE.90.042116 (interface literature; not the stated finite-strip census).
