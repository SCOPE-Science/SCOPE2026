# Vacancy-corridor face spectrum and a unique cluster-density peak in three-row site percolation

## Finding

Let \(G_n=P_3\square P_n\), with open (nonperiodic) boundaries, and retain its vertices independently with probability \(p\in[0,1]\). Write \(C_n\) for the number of nonempty connected components of the graph induced by retained sites, and \(N_n\) for the retained-site count. For every integer \(n\ge1\),

\[
\mathbb E C_n=3np-(5n-3)p^2+2(n-1)p^4+\sum_{d=2}^{n-1}(n-d)p^{2d+4}(1-p)^{d-1}.
\]

The sum is zero when \(n\le2\). It decomposes the expected count of *nonunit bounded faces* by exact horizontal span \(d\); their expected number at span \(d\) is \((n-d)p^{2d+4}(1-p)^{d-1}\) for \(2\le d<n\). These faces are vacancy corridors in the middle row.

For every fixed \(p\in[0,1]\), \(C_n/n\) converges in \(L^2\) to

\[
 c(p)=3p-5p^2+2p^4+\frac{p^8(1-p)}{1-p^2(1-p)}
 =\frac{p(1-p)^3(p^5+2p^4+p^3+4p+3)}{1-p^2+p^3}.
\]

The limit has a unique maximum on \([0,1]\), attained at \(p_*=0.328618598090884\ldots\), which is the unique root on \((0,1)\) of

\[
 P(p)=6p^9-8p^7+9p^6+20p^5-8p^4-4p^3+17p^2+4p-3.
\]

The vacancy-side expansion is \(c(p)\sim 11(1-p)^3\) as \(p\uparrow1\). The exact occupancy–cluster covariance identity

\[
 \operatorname{Cov}(C_n,N_n)=p(1-p)\frac{d}{dp}\mathbb E C_n
\]

implies \(\operatorname{Cov}(C_n,N_n)/n\to p(1-p)c'(p)\). Therefore, for fixed \(p\in(0,1)\) below the maximizer the limiting covariance is positive, and above it negative.

## Assumptions and scope

The graph has precisely three rows and \(n\) columns; edges connect vertically or horizontally adjacent sites, not diagonal sites. Retention events are mutually independent with the *same* fixed probability \(p\). A connected component with one occupied vertex is counted, while an empty configuration has zero components. All faces refer to the conventional planar embedding of this finite induced subgraph. An edge is present exactly when both its original endpoints survive. There are no wraparound edges.

The probability \(p_*\) maximizes the **expected number of occupied clusters per column**, not a spanning probability or a two-dimensional percolation threshold.

## Proof

**1. A complete face classification.** Place the three rows at heights \(0,1,2\). In the rectangular grid, a bounded face must have its upper and lower horizontal boundary edges on two occupied horizontal row segments and its vertical boundary at two columns. If its upper and lower levels are adjacent, any intermediate vertical grid edge splits the rectangle, so the face is one unit square. A face spanning both rows of vertical edges must have all top and bottom boundary sites occupied from column \(i\) to \(j\), both middle-row endpoints occupied, and every middle-row site at columns \(i+1,\ldots,j-1\) absent: an occupied internal middle-row site connects vertically to both occupied boundary rows and splits the interior. Conversely these exact conditions produce one bounded face and no intervening internal edge. Here \(d=j-i\ge2\), since at \(d=1\) the fully occupied middle edge instead creates two unit faces. The two types are disjoint and exhaustive.

For any specified unit square, all four sites must survive, giving probability \(p^4\). There are \(2(n-1)\) squares. For fixed corridor span \(d\ge2\), each of its \(n-d\) possible positions requires \(2(d+1)+2=2d+4\) retained sites and \(d-1\) missing middle-row interior sites. Its probability is \(p^{2d+4}(1-p)^{d-1}\), with no restriction on sites outside the corridor. Linearity of expectation proves the face spectrum.

**2. The finite identity.** The occupied subgraph has expected vertex count \(3np\) and expected edge count \((5n-3)p^2\), since the host contains \(3(n-1)\) horizontal and \(2n\) vertical edges. For every finite planar graph, the number of nonempty components is the vertex count minus the edge count plus the number of bounded faces, by Euler's formula. Applying expectation and the exhaustive face classification gives the asserted expression.

**3. The limit and concentration.** Put \(r=p^2(1-p)\). Since \(0\le r\le4/27<1\), dividing the finite formula by \(n\) and applying dominated convergence to the corridor series yields

\[
 \lim_{n\to\infty}\frac{\mathbb E C_n}{n}
 =3p-5p^2+2p^4+\sum_{d=2}^{\infty}p^{2d+4}(1-p)^{d-1}
 =3p-5p^2+2p^4+\frac{p^8(1-p)}{1-r}.
\]

Changing the status of one vertex changes the number of components by at most three: adding a vertex creates one component and merges at most four preexisting neighboring components. The bounded-differences/Efron–Stein inequality therefore gives \(\operatorname{Var}(C_n)\le (3n)\,3^2/2=27n/2\). Convergence of the means and this variance bound prove \(L^2\) convergence of \(C_n/n\).

**4. Unique density maximizer.** Algebraic rearrangement gives the factored expression for \(c(p)\) above and

\[
 c'(p)=-\frac{(1-p)^2 P(p)}{(1-p^2+p^3)^2}.
\]

The denominator is strictly positive on \([0,1]\). Direct differentiation gives

\[
 P'(p)=4+34p-12p^2+p^3(100p-32)+p^5(54-56p)+54p^8.
\]

For \(0\le p\le8/25\), use \(4+34p-12p^2\ge4+22p\), \(p^3(100p-32)\ge-32p^3\ge-32(8/25)^2p\), and \(p^5(54-56p)\ge0\). Their sum is strictly positive. For \(8/25\le p\le1\), the cubic term is nonnegative, the fifth-power term is at least \(-2\), and the first three terms are at least \(4+22p\), giving \(P'(p)>0\). With \(P(0)=-3\) and \(P(1)=33\), the polynomial has exactly one zero in \((0,1)\). Hence \(c\) strictly increases before that point and strictly decreases afterward. The factorization of \(c\) gives \(c(p)/(1-p)^3\to11\) as \(p\uparrow1\).

**5. Occupancy–component response.** In any finite product Bernoulli model, differentiating the finite expectation with respect to \(p\) yields \(\frac{d}{dp}\mathbb E C_n=\operatorname{Cov}(C_n,N_n)/(p(1-p))\) for \(0<p<1\). The explicit formula is a linear polynomial in \(n\) plus a geometric corridor tail; its differentiated per-column limit equals \(c'(p)\) at each fixed interior \(p\), by absolute convergence of the differentiated series. The sign assertion follows.

## Verification

The standalone Python 3 script `verify.py` uses only the standard library. Running `python3 verify.py` enumerates every site subset for \(n=1,2,3,4,5\), separately constructs the occupied graph and union–find components, counts unit faces and long vacancy corridors, and checks Euler's identity for all \(37{,}448\) configurations. It separately checks the finite expectation and each face-intensity formula at six exact rational probabilities, and performs further rational polynomial and sign tests. The execution passed \(37{,}631\) assertions. This finite enumeration is a consistency test, not a substitute for the all-size proof above.

## Relationship to prior work

The occupation model is the standard square-lattice site-percolation model. Newman and Ziff (2000) give a general cluster-measuring algorithm and numerical square-lattice percolation observables, not an explicit three-row all-parameter component expectation or a vacancy-corridor face spectrum. Monetti and Albano (1993) study, using Monte Carlo, the number and length of width-spanning clusters at criticality in rectangular site-percolated grids; that observable is not the total number of connected occupied components in a fixed three-row strip. Chang and Shrock (2004) derive exact cluster density functions for **bond** percolation on lattice strips, a distinct probability model in which edges, rather than vertices, are independently retained. The present identity exploits the unusually restricted possible bounded faces in the three-row **site** problem. All these techniques are relevant context; no exclusivity or independent priority certification is asserted.

## Limitations

The exact finite expression and the geometric face classification apply to open three-row square strips, not wider strips or periodic transverse boundaries. The asymptotic density and covariance statements concern a fixed occupation probability, and no critical-window theorem is claimed. The covariance sign is an asymptotic per-column statement, not an all-finite-size sign theorem. A general unpublished or unlocated site-percolation transfer-matrix calculation could cover the expression, and the historical novelty comparison is not exhaustive. Neither the exact value of the infinite-plane percolation threshold nor any two-dimensional critical exponent is addressed. The calculation and computer checks have not been independently mathematically audited.

## References

1. M. E. J. Newman and R. M. Ziff, *Efficient Monte Carlo algorithm and high-precision results for percolation*, arXiv:cond-mat/0005264 (first posted 16 May 2000), https://arxiv.org/abs/cond-mat/0005264.
2. R. A. Monetti and E. V. Albano, *Percolation on the square lattice in a \(L\times M\) geometry: Analysis of percolation clusters properties*, Z. Phys. B **90**, 351–355 (1993), https://sedici.unlp.edu.ar/bitstream/handle/10915/146216/Documento_completo.pdf?sequence=1.
3. S.-C. Chang and R. Shrock, *Exact results for average cluster numbers in bond percolation on lattice strips*, Physical Review E **70**, 056130 (2004), arXiv:cond-mat/0407070, https://arxiv.org/abs/cond-mat/0407070.
