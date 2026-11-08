# Fibonacci period-three counts and sharp chip-mass bands on wheel graphs

## Finding

Let \(n\ge4\) and let \(W_n=K_1\vee C_n\) have a labelled central hub and an ordered labelled rim cycle of length \(n\). In synchronous parallel chip-firing, a vertex with at least its degree in nonnegative integer chips sends one chip to each neighbor; other vertices wait. Write \(U\) for the update, and let \(|x|\) denote total chips. Define the *immediate primitive-three mass polynomial*
\[
H_n(z)=\sum_{\substack{x\in\mathbb Z_{\ge0}^{n+1}\\U^3x=x,\;Ux\ne x}}z^{|x|}.
\]
Write \(F_0=0,F_1=1,F_{k+2}=F_{k+1}+F_k\), and put \(\delta_n=3\) if \(n\equiv0\pmod3\), \(\delta_n=-2\) if \(n\equiv1\pmod3\), and \(\delta_n=-1\) if \(n\equiv2\pmod3\). Then
\[
\boxed{H_n(1)=3n\bigl(F_{2n+1}+\delta_n\bigr).}
\]
These are labelled periodic *configurations*, not three-orbits; the number of distinct orbits is \(n(F_{2n+1}+\delta_n)\).

Let \(\varepsilon_n=n\bmod2\), taking values zero or one. The exact set of supported chip masses is the disjoint union of two integer intervals:
\[
\boxed{\operatorname{supp}H_n=\bigl([2n+\varepsilon_n,3n-1]\cup[4n,5n-1-\varepsilon_n]\bigr)\cap\mathbb Z.}
\]
In particular, the gap strictly between the two bands has no immediate primitive-three configurations. Each *outer* endpoint (\(2n+\varepsilon_n\), \(5n-1-\varepsilon_n\)) has coefficient \(6\) for even \(n\), and coefficient \(12n\) for odd \(n\). For the two *inner* endpoints \(3n-1\) and \(4n\), define \(a_0=3,a_1=2,a_2=4\), and \(a_j=2a_{j-1}+a_{j-3}\) for \(j\ge3\). Both coefficients equal
\[
\boxed{3\bigl(a_n+1\bigr)\quad(3\mid n),\qquad 3\bigl(a_n-2\bigr)\quad(3\nmid n).}
\]

The *whole polynomial* is determined by a nine-state transfer formula, not merely its count or support. Index rows and columns by ordered pairs \((a,b)\in\{0,1,2\}^2\). For a triple \((a,b,c)\), define
\[
q(a,b,c)=\begin{cases}
\mathbf1_{a=2}+\mathbf1_{c=2},&b=0,\\
1+\mathbf1_{a=0}+\mathbf1_{c=0},&b=1,\\
\mathbf1_{a=1}+\mathbf1_{c=1},&b=2,
\end{cases}\qquad
 e(a,b,c)=\begin{cases}
3,&b=0,\\3-q(a,b,c),&b=1,\\
\mathbf1_{a=2}+\mathbf1_{c=2},&b=2.
\end{cases}
\]
Set \([q]_z=1+z+\cdots+z^{q-1}\) for positive \(q\), and \([0]_z=0\). The only nonzero-eligible matrix entries are
\[
\mathcal M(z,y)_{(a,b),(b,c)}=y^{\mathbf1_{b=2}}z^{e(a,b,c)}[q(a,b,c)]_z;
\]
all other entries vanish. Define
\[
H_n^+(z)=\frac{3z^n}{1-z}\left(\operatorname{tr}\mathcal M(z,1)^n-\operatorname{tr}\mathcal M(z,z)^n\right).
\]
This quotient is a polynomial over the integers. Then, exactly,
\[
\boxed{H_n(z)=H_n^+(z)+z^{7n-1}H_n^+(z^{-1}).}
\]
The superscript \(+\) denotes states in which every vertex fires once during the three-round period. It does not denote eventual periodicity after transients.

## Assumptions and scope

The rim is a labelled simple cycle and \(n\ge4\); the wheel contains \(n+1\) vertices and \(2n\) edges. Rim degrees are three and the hub degree is \(n\). Chip counts are nonnegative integers, not residues. All firing decisions are simultaneous. Only states periodic *at time zero* with least temporal period three are enumerated; there is no claim about eventual basins, other period lengths, or arbitrary initial chip counts. The transfer matrix is ordered lexicographically by pair and may be evaluated by exact integer arithmetic.

## Proof

**Uniform firing frequency and complementation.** If \(U^3x=x\), the vector of three-round firing counts is harmonic for the graph Laplacian, hence constant on connected \(W_n\). The common number is \(k\in\{0,1,2,3\}\). If \(k=0\) or \(3\), every vertex always waits or always fires, so the state is fixed. Thus a primitive-three state has \(k=1\) or \(2\). For \(k=1\), give vertex \(v\) color \(c_v\in\mathbb Z/3\mathbb Z\), its unique firing time. Define \(q_v\) to be the number of neighbors whose firing time is \(c_v-1\pmod3\). At its firing moment the chip count must be exactly \(d_v+s_v\) with \(0\le s_v<q_v\); conversely these inequalities at every vertex construct the prescribed three-round orbit, as verified below. In particular, admissibility is precisely \(q_v\ge1\) for all vertices. All its chip counts lie in \([0,2d_v-1]\). Consequently the coordinatewise involution \(x_v\mapsto2d_v-1-x_v\) commutes with \(U\), interchanges one-firing and two-firing patterns, and maps total chip mass \(m\) to \(4|E|-|V|-m=7n-1-m\).

**Local inequalities and mass.** For any vertex of phase zero, the initial chip count is \(d_v+s_v\); for phase one it is \(d_v-q_v+s_v\); and for phase two it is \(r_v+s_v\), where \(r_v\) is the number of neighbors of phase two. In each case the three successive chip amounts satisfy exactly the required fire/wait inequalities if and only if \(0\le s_v<q_v\). These choices are independent across vertices. Summing the lower endpoints of the local chip intervals edge-by-edge gives two chips from each monochromatic edge and one chip from each bichromatic edge. Hence, if \(m(c)\) is the number of edges with equal endpoint phases,
\[
|x|=|E|+m(c)+\sum_v s_v=2n+m(c)+\sum_v s_v.
\]
Every heterochromatic edge contributes to exactly one \(q_v\); thus \(\sum_vq_v=|E|-m(c)\). Therefore the largest mass for *every* admissible phase coloring, obtained by taking all \(s_v=q_v-1\), is
\[
2n+m(c)+\sum_v(q_v-1)=2|E|-|V|=3n-1.
\]
All integer masses between \(2n+m(c)\) and \(3n-1\) occur for that coloring, since the Minkowski sum of the finite integer intervals \([0,q_v-1]\) is an integer interval.

**Extremal phase colorings.** Fix the hub phase to zero. A rim vertex of phase zero must have a rim neighbor in phase two; a rim vertex of phase two must have a rim neighbor in phase one; a rim vertex of phase one already has its predecessor on the hub. The hub must have at least one phase-two rim neighbor. If \(n\) is even, zero monochromatic edges is possible precisely for the two alternating rim words \(1,2,1,2,\ldots\) and \(2,1,2,1,\ldots\); each is admissible. If \(n\) is odd, a proper three-coloring of the wheel is impossible, so at least one monochromatic edge occurs. Exactly one monochromatic edge is possible in precisely two types: (i) no rim zero and exactly one repeated edge in the alternating \(1,2\) rim word (\(2n\) words), or (ii) one rim zero and an alternating \(1,2\) path on the remaining \(n-1\) rim vertices (\(2n\) words). All these words satisfy the predecessor condition. There are three possible hub phases, so the minimal-mass coefficients are \(6\) and \(12n\). Since any one minimum coloring supports every mass up to \(3n-1\), the claimed first interval has no gaps; complementation gives the second interval and the reflected endpoint coefficients.

**Nine-state determinant for the total count.** With hub phase zero, each rim word \((c_1,\ldots,c_n)\) has predecessor counts \(q(c_{i-1},c_i,c_{i+1})\) on the rim, and the hub has \(r=\#\{i:c_i=2\}\) possible local offsets. Summing the number of one-firing states over the three possible hub phases gives
\[
H_n^+(1)=3\sum_{c_1,\ldots,c_n\in\mathbb Z_3}r\prod_{i=1}^nq(c_{i-1},c_i,c_{i+1}).
\]
Define the nine-by-nine matrix \(M(y)\) by \(M(y)_{(a,b),(b,c)}=q(a,b,c)y^{\mathbf1_{b=2}}\), with all other entries zero. The preceding formula is \(3\partial_y\operatorname{tr}M(y)^n|_{y=1}\). A direct finite determinant expansion yields
\[
D(t,y)=\det(I-tM(y))=1-t-2yt^2-(y^2+4y)t^3-2y^2t^4-y^2t^5+y^2t^6.
\]
The exact identities \(D(t,1)=(1-3t+t^2)(1+t+t^2)^2\) and
\[
-\frac{\partial_yD(t,y)|_{y=1}}{D(t,1)}=
-2+\frac{1-t}{2(1-3t+t^2)}+\frac{t+3}{2(1+t+t^2)}
\]
follow by polynomial algebra. By \(-\log\det(I-tM)=\sum_{j\ge1}\operatorname{tr}(M^j)t^j/j\), the coefficient at \(t^n\) of the last rational function, multiplied by \(3n\), is \(H_n^+(1)\). The first nonconstant summand has coefficient \(F_{2n+1}/2\); the second has coefficient \(\delta_n/2\). Therefore \(H_n^+(1)=3n(F_{2n+1}+\delta_n)/2\), and complementation doubles it to the boxed total.

**Whole polynomial and inner endpoints.** The local chip intervals with hub phase zero are \(n+[0,r-1]\) at the hub, and on a rim triple \((a,b,c)\) are exactly \(e(a,b,c)+[0,q(a,b,c)-1]\). Multiplying these polynomials around the rim as a nine-state transfer gives \(\operatorname{tr}\mathcal M(z,y)^n\). The hub factor is \(z^n[r]_z=z^n(1-z^r)/(1-z)\). This proves the whole-polynomial formula and its integrality. At mass \(3n-1\), each admissible phase word contributes one state, with every offset maximal. The zero-one support matrix \(B\), obtained by replacing each nonzero \(q(a,b,c)\) in \(M(1)\) by one, has
\[
\det(\lambda I-B)=\lambda^4(\lambda^2+\lambda+1)(\lambda^3-2\lambda^2-1).
\]
Its trace \(\operatorname{tr}B^n\) counts all rim phase words with positive rim predecessor counts. Exactly one of these words, the all-one rim word, lacks a phase-two rim neighbor and must be removed. The sum of \(n\)-th powers of the cubic factor's three roots is \(a_n\), satisfying \(a_0=3,a_1=2,a_2=4\), \(a_n=2a_{n-1}+a_{n-3}\); the quadratic factor contributes \(2\) when \(3\mid n\), and \(-1\) otherwise. Hence the number of admissible rim words is \(a_n+1\) or \(a_n-2\), respectively, and multiplication by three hub phases gives the stated inner-endpoint coefficients.

## Verification

The exact symbolic determinant identities and binary-support matrix characteristic polynomial were checked by `checks/verify_transfer.py`, using exact integer/symbolic operations. The same script independently enumerates phase words and all allowed chip offsets for \(3\le n\le12\), checking the entire mass support, total Fibonacci formula, sharp endpoint coefficients, and reflected bands. `checks/verify_direct.py` independently evolves every bounded integer state for \(3\le n\le6\), including 649,296 states altogether, testing \(U^3x=x\ne Ux\) with no phase assumptions. A separate `checks/verify_crosscheck.py` imports the two implementations and directly reconciles every mass coefficient for these four sizes. The deterministic outputs are recorded in adjacent `.out` files. The checks on \(n=3\) are a boundary control; the claim concerns \(n\ge4\). The finite checks supplement rather than replace the determinant and structural proofs.

## Relationship to prior work

Bitar and Goles (1992) introduced and studied the period structure of parallel chip-firing on finite graphs, including period restrictions on trees. Jiang (arXiv:1003.0943, first posted 2010) established a periodicity classification for complete bipartite graphs and general firing/complement lemmas. Jiang, Scully, and Zhang (arXiv:1211.6786, first posted 2012) characterized realizable periodic firing patterns; their general results do not state the wheel's exact mass polynomial or Fibonacci census. Ji, Li, and Wang (arXiv:2408.10508, first posted 2024), Theorem 1, exclude periods three and four strictly between \(2|E|-|V|\) and \(2|E|\), without giving the exact counts at the boundary. Here the two inner wheel bands attain these boundaries with explicit positive coefficients.

For comparison, a maximum-cut energy formula for period-two states on arbitrary connected graphs and explicit period-three results for graphs with exactly one cycle of length divisible by three and for friendship graphs are known related findings; they do not imply the wheel's two-band mass formula or the Fibonacci count for all \(n\ge4\). Wheels have many resonant cycles sharing a hub and a rim cycle, and are neither the single-resonant-cycle family nor the friendship family. The general local phase-counting principle is acknowledged as an antecedent rather than claimed as new.

## Limitations

No novelty assertion is made for the general firing-pattern or complementation lemmas. The new claim concerns only the wheel-specific exact period-three mass polynomial, sharp support and coefficients, and Fibonacci count. Exhaustive computation covers finite sizes only. The original Bitar–Goles full text was not available through the accessible sources; its bibliographic record and abstract were inspected, so an equivalent unindexed formulation in that work remains a priority risk. Other unindexed accounts of the wheel case may exist. No independent external mathematical audit has been performed.

## References

1. J. Bitar and E. Goles, “Parallel chip firing games on graphs,” *Theoretical Computer Science* 92 (1992), 291–300. DOI: 10.1016/0304-3975(92)90316-8. Public record dates the article January 20, 1992.
2. T.-Y. Jiang, “On the Period Lengths of the Parallel Chip-Firing Game,” arXiv:1003.0943, first posted March 4, 2010; full preprint inspected (particularly Section 2).
3. T.-Y. Jiang, Z. Scully and Y. X. Zhang, “Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game,” arXiv:1211.6786, first posted November 29, 2012; full preprint inspected (particularly Sections 2 and 6–7).
4. D. Ji, M. Li and D. Wang, “Non-Stabilizing Parallel Chip-Firing Games,” arXiv:2408.10508, first posted August 20, 2024; full preprint inspected (particularly Theorem 1).
