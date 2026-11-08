# Two-shore primitive-three mass spectra in complete-bipartite parallel chip-firing

## Finding

On every labelled simple complete bipartite graph \(K_{m,n}\), the mass generating polynomial of *initially primitive-three* parallel chip-firing configurations is explicit. If \(\min(m,n)<3\), it vanishes. For \(m,n\ge3\), define \([r]_z=\sum_{j=0}^{r-1}z^j\), and, for positive triples \(\mathbf a=(a_0,a_1,a_2)\), \(\mathbf b=(b_0,b_1,b_2)\) of totals \(m,n\), respectively, put

\[
P_{m,n}(z)=\sum_{\mathbf a,\mathbf b}
\frac{m!n!}{\prod_{i=0}^{2}a_i!b_i!}
 z^{mn+\sum_{i=0}^{2}a_i b_i}
\prod_{i=0}^{2}[b_{i-1}]_z^{a_i}[a_{i-1}]_z^{b_i}.
\]

All phase indices are taken modulo three. The complete polynomial and its reflection law are

\[
H_{m,n}(z)=P_{m,n}(z)+z^{4mn-m-n}P_{m,n}(z^{-1}),\qquad
H_{m,n}(z)=z^{4mn-m-n}H_{m,n}(z^{-1}).
\]

The exact chip-mass support is the union of two *full* integer intervals

\[
[mn+m+n-3,\ 2mn-m-n]\ \cup\ [2mn,\ 3mn-2m-2n+3].
\]

No chip total between these intervals occurs; the strict gap consists of \(m+n-1\) integers. Write \(S_3(s)=3^s-3\cdot2^s+3\), the number of onto three-colorings of an \(s\)-element labelled set. The coefficient at either inner endpoint is exactly \(S_3(m)S_3(n)\). At either outer endpoint it is \(E_{m,n}\), where

\[
E_{m,n}=\begin{cases}
6S_3(\max(m,n)),&\min(m,n)=3,\\[2pt]
3mn\bigl((m-1)2^{n-1}+(n-1)2^{m-1}-2mn+2\bigr),&m,n\ge4.
\end{cases}
\]

Every primitive-three temporal orbit consists of exactly three configurations, so the orbit count is \(H_{m,n}(1)/3\). For illustration, the numbers of initial primitive-three configurations are \(72\) on \(K_{3,3}\), \(864\) on \(K_{3,4}\), and \(17{,}280\) on \(K_{4,4}\).

## Assumptions and scope

Vertices are labelled. Each vertex holds a nonnegative integer number of chips, and at each synchronous update every vertex holding at least its degree sends exactly one chip to each neighbor. The graph has \(m\) vertices on the left (degree \(n\)) and \(n\) on the right (degree \(m\)); \(m,n\) are arbitrary positive integers. Chip mass is the conserved sum of all chip counts. A configuration is initially primitive-three if its third update equals itself but neither of the first two updates equals itself. No claim about the size or temporal distribution of its attracting basin is made.

## Proof

**1. Equal firing counts and phase classes.** Let \(F_t(v)\) be the indicator that vertex \(v\) fires in update \(t\). For any configuration that returns after three updates, summing the update equation gives

\[
0=\sum_{w\sim v}\sum_{t=0}^{2}F_t(w)-\deg(v)\sum_{t=0}^{2}F_t(v).
\]

On a connected graph an integer-valued harmonic function is constant, by the maximum principle. Thus all vertices fire the same number \(q\) of times in the three updates. Values \(q=0\) and \(q=3\) yield fixed configurations, because then all vertices have the same firing bit at every update. A primitive-three configuration therefore has \(q=1\) or \(q=2\). In the first case, assign each vertex a phase \(c\in\{0,1,2\}\), the unique update at which it fires.

**2. Exact local intervals.** For one vertex of degree \(d\), let \(t_i\) count neighbors firing in update \(i\), so \(t_0+t_1+t_2=d\). The successive local chip counts are \(x_0\), \(x_1=x_0+t_0-d\mathbf1_{\{c=0\}}\), and \(x_2=x_1+t_1-d\mathbf1_{\{c=1\}}\). The conditions that the vertex fires exactly at phase \(c\) are *necessary and sufficient* for its initial count to lie in the following integer interval:

\[
\begin{array}{c|c|c}
\text{phase }c&\text{allowed initial count}&\text{number of choices}\\\hline
0 &[d,\ d+t_2-1]&t_2\\
1 &[t_1+t_2,\ d-1]&t_0\\
2 &[t_2,\ t_1+t_2-1]&t_1
\end{array}
\]

The third update returns the original local value because every vertex and all its neighbors fire once. Each displayed interval is nonnegative whenever it is nonempty, and the intermediate counts are nonnegative because the update never fires an under-threshold vertex. The number of choices is the number of neighbors of predecessor phase \(c-1\) modulo three. Hence the presence of any vertex of phase \(c\) forces a vertex of phase \(c-1\) on the opposite shore. Iterating this implication around a bipartite graph forces *all three phases on both shores*. Thus no period-three state exists if a shore has fewer than three vertices.

**3. Product formula and baseline.** Now let \(a_i\) be the count of left-shore vertices of phase \(i\), and \(b_i\) the corresponding right-shore count; all six are positive. Every left vertex of phase \(i\) has \(b_{i-1}\) possible chip counts and every right vertex has \(a_{i-1}\). By the interval table, the sum of all lower endpoints is

\[
B(\mathbf a,\mathbf b)=mn+\sum_{i=0}^{2}a_i b_i.
\]

The product of interval enumerators is therefore \(z^B\prod_i[b_{i-1}]_z^{a_i}[a_{i-1}]_z^{b_i}\). The multinomial factor counts labelled phase assignments of the prescribed sizes, giving exactly \(P_{m,n}(z)\).

**4. Complementary two-fire phases.** Define the chip complement formally by \(C(x)_v=2\deg(v)-1-x_v\). For any integer-valued configuration the firing indicator of \(C(x)\) is exactly the complementary indicator of \(x\), and the update satisfies \(F(C(x))=C(F(x))\) algebraically (even if signed values are allowed provisionally). If \(x\) is a two-fire primitive-three state, its complement has the one-fire phase pattern; the necessity in Step 2 forces every complementary initial count into one of the nonnegative intervals displayed there. Hence \(C(x)\) is nonnegative. Conversely every one-fire state in those intervals has nonnegative complement, because its counts are at most \(2\deg(v)-1\), and the complement fires twice per period. Thus complement gives a bijection between the two classes, reversing chip mass about

\[
\sum_v(2\deg(v)-1)=4mn-m-n.
\]

This proves the formula for \(H_{m,n}(z)\) without assuming a priori that a candidate two-fire state has small chip counts.

**5. Full support and the gap.** For a fixed positive phase profile, the maximum total exponent in its summand is the baseline plus the sum of interval widths. Each cross-shore edge whose endpoints have distinct phases contributes exactly one to the total number of interval choices before subtracting one per vertex. Consequently this width is

\[
\sum_i a_i b_{i-1}+\sum_i b_i a_{i-1}-(m+n)
=mn-\sum_i a_i b_i-(m+n).
\]

Thus every summand has top exponent \(2mn-m-n\), independently of the phase counts, and has every integer exponent from its baseline to that top exponent with a positive coefficient. Write \(a_i=1+u_i\), \(b_i=1+v_i\) with all excesses nonnegative and sums \(\sum_i u_i=m-3\), \(\sum_i v_i=n-3\). Then

\[
\sum_i a_i b_i=m+n-3+\sum_i u_i v_i\ge m+n-3.
\]

Equality is attained by disjointly supported excesses, for example \(\mathbf a=(m-2,1,1)\), \(\mathbf b=(1,n-2,1)\). Its summand alone fills *every* integer from \(mn+m+n-3\) to \(2mn-m-n\). All other summands lie in this same band. The complement fills the reflected band from \(2mn\) to \(3mn-2m-2n+3\), proving the exact support and the central gap.

**6. Sharp endpoint populations.** In any product of positive integer interval polynomials \([r]_z\), both the smallest and largest coefficients are one. Since every phase profile has the same top exponent, the coefficient of \(z^{2mn-m-n}\) in \(P\) counts all pairs of surjective three-phase assignments, which is \(S_3(m)S_3(n)\). At the bottom of \(P\), only profiles with \(u_iv_i=0\) for all three \(i\) contribute. If \(\min(m,n)=3\), that shore has exactly one vertex of each phase and the count is \(6S_3(\max(m,n))\). For \(m,n\ge4\), the supports of the nonzero excess vectors must be disjoint and have respective sizes \((1,1)\), \((1,2)\), or \((2,1)\). These cases contribute, respectively,

\[
6m(m-1)n(n-1),\quad
3m(m-1)n(2^{n-1}-2n),\quad
3mn(n-1)(2^{m-1}-2m).
\]

Their sum simplifies to the stated expression for \(E_{m,n}\). Reflecting gives the outer endpoint at the high band and the inner endpoint at the low high-band boundary. This finishes the proof.

## Verification

The standalone programs `verify_kmn3.py` and `verify_phase_kmn3.py` are supplied with captured output files. The first directly enumerates all confined configurations at \((m,n)=(2,3),(3,2),(3,3),(3,4),(4,3)\), explicitly iterates the synchronous rule for three updates and compares every mass coefficient to the formula. It also tests all profile polynomials for \(3\le m,n\le7\), their full support, endpoint populations, mass reflection, and divisibility by three. The second independently constructs chip choices for each labelled three-phase assignment and checks exact coefficients on seven two-shore sizes up through \(K_{5,5}\), including the outer endpoint formula. These are finite reproducibility checks, not the basis for the all-size proof.

## Relationship to prior work

Jiang's complete-bipartite period theorem establishes which least periods can occur and the equal-firing-count and complement principles; it does not enumerate all initially primitive-three states by chip mass. Jiang, Scully, and Zhang prove qualitative restrictions on periodic firing words, not this two-shore graded distribution. Ji, Li, and Wang exclude three- and four-cycles from the middle energy interval for general graphs, consistent with the exact empty band found here; that theorem does not assert occupancy of every mass in the outer intervals, or count boundary states. A previously known thin-side formula for \(K_{3,b}\) is recovered when one shore has size three, and **that special case is not claimed as new**. The two-variable complete generating polynomial and the nonlinear excess-phase interaction for two shores of size at least four supply the extension.

## Limitations

The theorem concerns configurations already on least-period-three orbits, not eventual three-cycle attraction basins or higher periods. The finite programs cannot establish novelty, global completeness, or an infinite-family theorem by themselves; those require the proof above. Historical priority may be affected by unindexed mass-resolved parallel-chip-firing literature. The mathematical evidence presented is same-authority analytical and computational review only; no independent audit has been performed.

## References

1. Tian-Yi Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943 (first public version 2010-03-04), §§2–3, especially Proposition 2.5 and Theorem 3.10. https://arxiv.org/abs/1003.0943
2. Tian-Yi Jiang, Ziv Scully, Yan X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, arXiv:1211.6786 (first public version 2012-11-29), Theorem 6.2 and §7. https://arxiv.org/abs/1211.6786
3. David Ji, Michael Li, Daniel Wang, *Non-Stabilizing Parallel Chip-Firing Games*, arXiv:2408.10508 (first public version 2024-08-20), Theorem 1. https://arxiv.org/abs/2408.10508
