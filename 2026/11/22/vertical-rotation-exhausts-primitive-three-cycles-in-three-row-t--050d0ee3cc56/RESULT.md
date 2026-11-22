# Vertical rotation exhausts primitive three-cycles in three-row Toom dynamics

## Finding

Consider the deterministic north-east-center majority cellular automaton on the indexed binary torus \((\mathbb Z/3\mathbb Z)\times(\mathbb Z/n\mathbb Z)\), for every integer \(n\ge3\). Every configuration having least temporal period three is a **vertical rotating wave**: at every site, its next value is the value at the northern neighbor. Moreover, every vertical column of such a configuration is nonconstant.

The number \(P_n\) of **labelled configurations** having least temporal period three and the number \(C_n=P_n/3\) of their temporal orbits are exactly
\[
\boxed{P_n=2^n+2\cos(n\pi/3)+2\,3^{n/2}\cos(5n\pi/6),\qquad C_n=P_n/3.}
\]
Both counts are integers; \(C_n>0\) for every \(n\ge3\), and
\[
 C_n=\frac{2^n}{3}+O(3^{n/2}).
\]
In particular, primitive three-cycles occur at **every** admissible horizontal circumference, and their orbit count has exponential growth base two. The exact values of \(C_n\) for \(n=3,4,5,6,7,8,9,10,11,12\) are respectively \(2,2,20,4,70,58,170,422,440,1852\).

## Assumptions and scope

Coordinates are \((r,i)\in(\mathbb Z/3\mathbb Z)\times(\mathbb Z/n\mathbb Z)\), with three *distinct* rows, indexed columns, and no quotient by spatial or vertical shifts. States \(x_{r,i}\) belong to \(\{0,1\}\). One simultaneous update is
\[
 (Fx)_{r,i}=\operatorname{maj}(x_{r,i},x_{r+1,i},x_{r,i+1}),
\]
where the majority is one iff at least two inputs are one. Define the row rotation \((Rx)_{r,i}=x_{r+1,i}\). Least temporal period three means \(F^3x=x\) and \(Fx\ne x\). Each temporal orbit is counted once in \(C_n\), whereas spatially translated configurations are distinct unless they coincide literally. No stochastic perturbation is present.

## Proof

**1. A complete finite temporal-history transfer.** For a given three-time column history write \(a=(a^{(0)},a^{(1)},a^{(2)})\), where each \(a^{(t)}\) is a three-bit vertical column. There are exactly \(8^3=512\) possible histories. Define a directed edge \(a\to b\) precisely when all nine equalities
\[
 a^{(t+1\bmod3)}_r=\operatorname{maj}\bigl(a^{(t)}_r,a^{(t)}_{r+1\bmod3},b^{(t)}_r\bigr)
 \qquad (r,t\in\{0,1,2\})
\]
hold. A cyclic length-\(n\) word of these histories is equivalent, without multiplicity or omitted cases, to an initial configuration satisfying \(F^3x=x\): the history at column \(i\) records all three successive configurations and the east input is the next column's history.

The complete directed graph is finite and explicit: the nine Boolean tests are performed on all \(512^2=262144\) ordered candidate pairs. It has 1120 edges. An exhaustive strong-component classification finds exactly three components containing a directed cycle. Under encoding \(a=a^{(0)}+8a^{(1)}+64a^{(2)}\), with row \(r\) stored as bit \(r\), their vertex sets are
\[
 \{0,511\},\quad \{73,146,219,292,365,438\},\quad
 \{84,161,245,266,350,427\}.
\]
The other 498 vertices are singleton strong components without self-loops, so none lies in any closed directed walk. This is a **finite exhaustive lemma**, not an inference from a sample of circumferences. Its full elementary enumeration, two-pass strong-component algorithm, a separate return-reachability check at every vertex, and asserted component lists appear in the self-contained `verify_transfer.py` supplied with this result. The graph construction and exact assertions are part of the proof and may be replayed without external libraries.

The first component represents three-time-constant uniform vertical columns \(000\) or \(111\). The second consists of six three-time-constant, nonuniform columns. Any cyclic history confined to either component is therefore a fixed configuration of \(F\). The third consists of the histories \((a,Ra,R^2a)\) with \(a\) any of the six nonuniform columns. A closed history using that third component satisfies \(Fx=Rx\) and, because \(R\) has order three on a nonuniform binary three-bit column, has least temporal period three. Conversely the exhaustive component classification shows that **every** least-period-three configuration is of this form. This proves the structural assertion, including the absence of mixed fixed/rotating-column three-cycles.

**2. The six-state rotating transfer and its spectrum.** In the vertical-bit order \(001,010,100,011,101,110\), the allowed eastward transitions are
\[
\begin{array}{c|l}
001&010,110\\
010&100,101\\
100&001,011\\
011&100,110\\
101&010,011\\
110&001,101
\end{array}
\]
Indeed, for a nonuniform column \(a\), the condition \(\operatorname{maj}(a_r,a_{r+1},b_r)=a_{r+1}\) forces the eastern bit wherever \(a_r\ne a_{r+1}\), and leaves the other bit free. Hence the adjacency matrix on this ordered alphabet is
\[
 B=\begin{pmatrix}
0&1&0&0&0&1\\
0&0&1&0&1&0\\
1&0&0&1&0&0\\
0&0&1&0&0&1\\
0&1&0&1&0&0\\
1&0&0&0&1&0
\end{pmatrix}.
\]
The number of labelled period-three configurations equals the number of length-\(n\) cyclic walks on this six-state graph, so \(P_n=\operatorname{tr}(B^n)\). The characteristic polynomial, computed by an exact six-factor determinant and also directly checkable from the displayed matrix, factors as
\[
 \det(zI-B)=z(z-2)(z^2-z+1)(z^2+3z+3).
\]
Its nonzero roots are \(2\), \(\exp(\pm i\pi/3)\), and \(\sqrt3\exp(\pm5i\pi/6)\). Summing their \(n\)th powers gives the claimed exact expression for \(P_n\). Every least-period-three orbit has precisely three configurations, so \(C_n=P_n/3\).

**3. All-length occurrence and growth.** In the rotating graph, both \(001\to110\to001\) and \(001\to010\to100\to001\) are closed walks based at \(001\). Concatenating them provides a closed walk of every length \(n\ge2\), since every such integer is a nonnegative sum of twos and threes. Thus \(P_n>0\) for every \(n\ge3\). The remaining characteristic roots have modulus at most \(\sqrt3<2\); their power sums give \(P_n=2^n+O(3^{n/2})\), proving the asymptotic and completing the theorem.

## Verification

Two stand-alone verification programs accompany this proof. `verify_transfer.py` reconstructs the complete 512-history transfer graph from the Boolean majority rule, checks all 262144 possible edges, verifies its 14 recurrent-history vertices by both strong components and direct return reachability, verifies the six-state matrix, evaluates its characteristic polynomial by an exact integer Leibniz determinant, and computes exact traces through circumference 20. Its output is included as `verify_transfer_output.txt`.

Independently, `verify_direct.py` iterates the original cellular automaton, without reading the transfer matrix, for **every** labelled binary configuration on the \(3\times n\) tori with \(n=3,4,5,6\). It tests the exact least-period-three counts and checks \(Fx=Rx\) for every such configuration. There are respectively 512, 4096, 32768 and 262144 initial configurations in these exhaustive finite tests. Its output is included as `verify_direct_output.txt`. The direct finite checks are independent corroboration; the graph decomposition and spectral calculation establish the infinite all-\(n\) theorem.

## Relationship to prior work

Toom's north-east-center majority rule, including its deterministic limit, is classical; the foundational source by Gács studies erosion and global behavior in planar and toroidal settings, while Makowiec studies noisy square-lattice stationary states. Neither establishes the temporal three-cycle structure or its count on an indexed three-row strip. Jen's general periodic-cylinder transfer method explains why finite automata admit matrix-counting algorithms but does not provide this specific 14-history recurrence decomposition, all-length three-cycle spectrum, or vertical-rotation rigidity.

A publicly available earlier exact **fixed-point** classification for the same three-row rule gives \(2^n+6\sum_{6\mid j}\binom nj\) one-step fixed configurations. That result is acknowledged and is separate from the present classification of configurations with **least temporal period three**: its stated scope excludes nonfixed temporal cycles. A separate two-row attraction-basin theorem has a different vertical circumference and no implication yielding the three-row three-cycle formula. Combining the previously known fixed-point count with the present result shows that period-three points constitute an asymptotic one-third of all configurations with period dividing three, though they constitute only an exponentially small proportion of all \(2^{3n}\) initial states.

## Limitations

The theorem classifies states of least temporal period exactly three; it does **not** assert that every trajectory converges to a fixed point or a three-cycle, nor classify other periods, attraction basins, noisy stationary distributions, or strips of larger height. Computer-assisted finite graph reduction is explicitly part of the exact proof, with its fully specified and replayable 512-vertex certificate, and is not an independent external certification. The 1997 full-text article on Toom ground states was not available for complete comparison; it concerns stationary-state simulations according to its inspected abstract. Historical equivalents not accessible in the searched sources remain a priority risk.

## References

1. E. Jen, *Cylindrical Cellular Automata*, Communications in Mathematical Physics 118 (1988), 569–590, DOI:10.1007/BF01221109. Full accessible text: https://www.academia.edu/72440176/Cylindrical_cellular_automata
2. D. Makowiec, *Gibbsian versus non-Gibbsian nature of stationary states for Toom probabilistic cellular automata via simulations*, Physical Review E 55 (1997), 6582–6588, DOI:10.1103/PhysRevE.55.6582 (public 1997-06-01).
3. D. Makowiec, *Ground-state configurations for Toom cellular automata: Experimental hints*, Physical Review E 56 (1997), 5195–5203, DOI:10.1103/PhysRevE.56.5195 (public abstract inspected; complete text not obtained).
4. D. Makowiec, *Critical properties of Toom cellular automata*, arXiv:cond-mat/9808247v1 (public 1998-08-22). https://arxiv.org/html/cond-mat/9808247v1
5. P. Gács, *A Toom rule that increases the thickness of sets*, arXiv:math-ph/0102009v1 (public 2001-02-08). https://arxiv.org/abs/math-ph/0102009
6. *Two coexisting fixed-state phases in the three-row Toom automaton* (2026), public manuscript: https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-two-coexisting-fixed-state-phases-in-the-three-row-toom-automato--ba0ec0595c40
7. *Exact attraction basins and an emergent Ising law for two-row Toom dynamics* (2026), public manuscript: https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-attraction-basins-and-an-emergent-ising-law-for-two-row-to--c044dc7d101f
