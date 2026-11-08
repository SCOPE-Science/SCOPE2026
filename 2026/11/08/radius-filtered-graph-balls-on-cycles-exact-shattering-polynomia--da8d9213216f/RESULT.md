# Radius-filtered graph balls on cycles: exact shattering polynomials and a two-phase density law

## Finding
Let \(C_n\) be the unweighted cycle on \(n\ge4\) vertices. For \(0\le R\le\lfloor n/2\rfloor\), let \(\mathcal B_{n,R}\) comprise all vertex balls of integer radius at most \(R\), with no empty ball adjoined. For \(k\ge0\), let \(s_k(n,R)\) count unordered \(k\)-vertex supports shattered by this family, and let \(\Phi_{n,R}(z)=\sum_k s_k(n,R)z^k\).

Put \(h=\lfloor n/2\rfloor\), and define, for integer \(u\ge0\),
\[
Q_n(u)=\sum_{j=0}^{3}(-1)^j\binom3j\left\langle\binom{n-ju-1}{2}\right\rangle,
\qquad
\left\langle\binom t2\right\rangle=\begin{cases}\binom t2,&t\ge2,\\0,&t<2.\end{cases}
\]
Then the complete support-count polynomial is
\[
\Phi_{n,R}(z)=1+nz+s_2(n,R)z^2+s_3(n,R)z^3,
\]
with all higher coefficients zero, where
\[
s_2(n,R)=\begin{cases}2nR,&2R<h,\\\binom n2,&2R\ge h,\end{cases}
\]
and
\[
s_3(n,R)=
\begin{cases}
0,&R<h,\ 4R<n,\\
\dfrac n3\bigl(Q_n(2R)-Q_n(n-2R-1)\bigr),&R<h,\ 4R\ge n,\\
\binom n3,&R=h,\ n\text{ even},\\
\binom n3-n,&R=h,\ n\text{ odd}.
\end{cases}
\]

For \(R<h\), write a triple \(a,b,c\) in clockwise cyclic order and let \(g_1,g_2,g_3\ge1\) be its successive edge-gap lengths, summing to \(n\). Then that triple is shattered if and only if
\[
n-2R\ \le\ \max\{g_1,g_2,g_3\}\ \le\ 2R.
\]
For \(R=h\), every triple is shattered when \(n\) is even; when \(n\ge5\) is odd, precisely the \(n\) consecutive-vertex triples are not shattered.

Consequently,
\[
\operatorname{VCdim}(\mathcal B_{n,R})=
\begin{cases}
1,&R=0,\\
2,&1\le R<\lceil n/4\rceil,\\
3,&R\ge\lceil n/4\rceil.
\end{cases}
\]
The middle range is empty when \(n=4\). For the triangular cycle \(C_3\), the separate polynomials are \(\Phi_{3,0}(z)=1+3z\) and \(\Phi_{3,1}(z)=1+3z+3z^2\).

There is an additional sharp asymptotic result. If \(n\to\infty\) and \(R_n/n\to\rho\in[0,1/2]\), then a uniformly chosen three-element vertex support is shattered with limiting probability
\[
\lim_{n\to\infty}\frac{s_3(n,R_n)}{\binom n3}=
\begin{cases}
0,&0\le\rho\le1/4,\\
-6+36\rho-48\rho^2,&1/4\le\rho\le1/3,\\
1-3(1-2\rho)^2,&1/3\le\rho\le1/2.
\end{cases}
\]
(The expressions agree at their shared endpoints.) Thus the positive-density onset is at one quarter of the circumference, and the nonzero regime has two distinct quadratic pieces.

## Assumptions and scope
The graph metric is shortest-path distance on the standard simple cycle. Balls have an actual vertex center, contain their center, and have integer radii in the inclusive range from zero to \(R\). Supports are vertex sets without repetitions; an empty trace on a support must be realized by one of the listed, nonempty graph balls. No radius beyond the cycle's diameter changes the family. Only \(n\ge4\) is used in the main formula; the \(n=3\) case is handled explicitly.

## Proof
**One- and two-point supports.** Every singleton can be labeled both ways using radius-zero balls, so \(s_1=n\). For two vertices \(x,y\), the traces selecting each separately and neither are realized by singleton balls, since \(n\ge4\). The trace selecting both exists exactly when \(d_{C_n}(x,y)\le2R\): necessity follows from the triangle inequality, and sufficiency by choosing a center on a shortest \(x\)-to-\(y\) path. There are \(n\) unordered pairs at each cyclic distance strictly below \(n/2\), and \(n/2\) antipodal pairs when \(n\) is even. This gives the stated formula for \(s_2\).

**Four-point obstruction.** Fix four vertices in cyclic order. No proper cycle ball (a connected circular arc) can contain the alternating first and third vertices while avoiding the alternating second and fourth vertices. A whole-cycle ball cannot realize that trace either. Therefore no four-point support is shattered, and no larger support is shattered by heredity.

**Three-point classification below the diameter.** Suppose \(R<h\). Every non-universal ball is a contiguous circular arc of exactly \(2r+1\le2R+1\le n-1\) vertices. The singleton traces are supplied by radius zero; because \(n\ge4\), some radius-zero ball is disjoint from any given triple, supplying the empty trace. If the clockwise gaps of the triple are \(g_1,g_2,g_3\), a ball containing the entire triple exists precisely when one gap can supply the excluded interior of an arc of length at most \(2R+1\), i.e. when \(\max_i g_i\ge n-2R\). Indeed, if a gap of length \(g\) is used for the outside, the complementary arc containing the triple has \(n-g+1\) vertices; any shorter arc can be extended to an arc of length \(2R+1\) while retaining the triple.

For the trace selecting two vertices while excluding the third, the selected pair must be joined in the cycle path avoiding the excluded vertex. Its edge length is exactly the corresponding cyclic gap \(g\). Necessity is \(g\le2R\). For sufficiency, remove the excluded vertex, leaving a path of \(n-1\) vertices. The selected pair's connecting subpath has \(g+1\le2R+1\) vertices; since \(2R+1\le n-1\), it extends inside that path to a subpath of exactly \(2R+1\) vertices. This is a radius-\(R\) cycle ball avoiding the excluded vertex. Applying this to all three excluded vertices gives \(\max_i g_i\le2R\). Together with the full-trace condition, this proves the claimed equivalence.

**Counting triples.** The number of ordered triples of positive integers with sum \(n\) and all parts at most \(u\) is \(Q_n(u)\), by inclusion–exclusion after subtracting one from each part. For \(R<h\), successful gap triples have maximum between \(n-2R\) and \(2R\). When \(4R\ge n\), their number is \(Q_n(2R)-Q_n(n-2R-1)\); if \(4R<n\), there are none. Each unordered vertex triple has precisely three choices of marked starting vertex in the fixed cyclic orientation, whereas an ordered gap triple has \(n\) choices of starting vertex. Hence the factor \(n/3\).

**Diameter radii.** If \(n=2h\), the radius-\((h-1)\) balls are complements of single vertices, the radius-zero balls are singletons, and a radius-\(h\) ball is the full cycle. These realize all eight traces on any three-point support. If \(n=2h+1\ge5\), the largest proper balls are length \(n-2\) arcs, i.e. complements of adjacent vertex pairs. The path joining a selected pair while avoiding the third can fit inside such a ball exactly when its cyclic gap is at most \(n-3\); all three pairs are feasible exactly when the triple is not three consecutive vertices. Singleton, empty, and full traces remain available. There are exactly \(n\) consecutive triples. The exceptional \(C_3\) is checked directly.

**Dimension threshold.** The three-point criterion requires \(4R\ge n\) below the diameter. When \(R=\lceil n/4\rceil<h\), positive gap triples with maximum in the stated interval exist: take one gap \(n-2R\), and split the remaining \(2R\) into two positive gaps no larger than \(2R\), except if the chosen maximum is smaller than another gap; the sum still admits a maximum in the interval since \(n\le4R\) and \(n\ge3\). More directly, for every \(R\) with \(4R\ge n\), take a gap of \(2R\) and split \(n-2R\) into two positive gaps each at most \(2R\) (here \(n-2R\ge2\) because \(R<h\)). For \(R=h\), the explicit diameter case supplies shattered triples. Two-point supports exist for every \(R\ge1\); radius zero alone has VC dimension one. This proves the threshold.

**Limiting three-point density.** For uniformly random unordered triples, their three cyclic gaps, with a uniformly marked starting point, are uniform over positive integer compositions of \(n\) into three parts. Their normalized values converge to uniform area measure on the simplex of three positive reals summing to one. For \(\rho<1/2\), the shattering event becomes \(1-2\rho\le\max_i G_i\le2\rho\). Inclusion–exclusion gives the maximum-gap distribution: for \(1/3\le t\le1\), its distribution function is \(1-3(1-t)^2+3(1-2t)_+^2\) (and is zero below \(1/3\)). Subtraction at \(t=2\rho\) and \(t=1-2\rho\) yields the displayed two-piece limit. The endpoints follow by continuity, including \(\rho=1/2\), where the fraction of the exceptional consecutive triples is asymptotically zero.

## Verification
A separate finite verifier enumerates actual radius-filtered ball masks, then enumerates all supports of sizes one through four and directly computes their Boolean traces. It compares the complete counts and the individual three-support gap classification against the formulas for every \(3\le n\le20\) and every permitted radius cutoff. Run `python3 verify_radius_filtered_cycle_balls.py`. The observed result is `ALL_CYCLE_BALL_SHATTERING_CHECKS_PASS 117 families 259527 supports 54318 triples`. This computational range corroborates, but is not used in place of, the all-\(n\) proof.

For example, the polynomials at \((n,R)=(8,2)\), \((12,3)\), and \((12,4)\) have coefficient vectors \((1,8,28,24)\), \((1,12,66,60)\), and \((1,12,66,184)\), respectively.

## Relationship to prior work
Chalopin, Chepoi, Mc Inerney, Ratel and Vaxès, *Sample compression schemes for balls in graphs* (arXiv:2206.13254, first public 2022-06-27), study graph-ball VC complexity and prove in Section 4, Proposition 10, a proper size-three sample compression scheme for cycle balls of arbitrary radius. Their cycle-ball proof does not enumerate shattered supports by radius cutoff or give the present finite coefficient formulas and limiting density transition. Standard finite cyclic-interval classes give broader VC-dimension bounds; these do not determine the parity and radius-dependent count of all supports realized by centered integer-radius balls. This result concerns exact support counts and their density, not new compression bounds.

## Limitations
The formula is for unweighted simple cycles, vertex centers, and every integer radius up to a fixed cutoff; it does not address weighted cycles, directed distances, nonuniform center restrictions, or arbitrary connected arcs. The asymptotic law concerns uniformly chosen three-point subsets, not general random samples or arbitrary graph classes. Historical priority under alternate names such as circular-arc hypergraphs and exact range-shattering profiles may remain incomplete. Computational finite checks do not establish independent mathematical validation.

## References
1. J. Chalopin, V. Chepoi, F. Mc Inerney, S. Ratel, Y. Vaxès, *Sample compression schemes for balls in graphs*, arXiv:2206.13254 (first submitted 2022-06-27), especially Section 4 and Proposition 10. https://arxiv.org/abs/2206.13254
