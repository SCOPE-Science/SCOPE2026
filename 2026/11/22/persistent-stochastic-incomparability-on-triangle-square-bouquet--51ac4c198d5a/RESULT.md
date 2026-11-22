# Persistent stochastic incomparability on triangle–square bouquets

## Finding
For every integer \(r\ge2\), the random sequential and uniform-static maximal independent-set *cardinality* laws on the triangle–square bouquet \(G_r\) are strictly incomparable in first-order stochastic order. Their exact three-point distributions are
\[
\begin{array}{c|cc}
\text{size}&\text{sequential}&\text{static}\\\hline
2&\dfrac{r+1}{(r+2)(2r+1)}&\dfrac1{1+2^{r+1}}\\[4pt]
r+1&\dfrac{2r}{3(2r+1)}&\dfrac{2^r}{1+2^{r+1}}\\[4pt]
r+2&1-\dfrac{r+1}{(r+2)(2r+1)}-\dfrac{2r}{3(2r+1)}&\dfrac{2^r}{1+2^{r+1}}
\end{array}
\]
For every \(r\ge2\), the cumulative distributions cross strictly at sizes \(2\) and \(r+1\), and
\[
d_{\mathrm{TV}}\bigl(\mathcal L(S_r),\mathcal L(T_r)\bigr)=\frac{2^r}{1+2^{r+1}}-\frac{2r}{3(2r+1)}\longrightarrow\frac16.
\]
The small-size probability ratio between sequential and static sampling grows asymptotically like \(2^r/r\).

## Assumptions and scope
The graph \(G_r\) consists of \(r\) triangles and one four-cycle identified at one hub vertex \(h\), with all other vertices distinct and no extra edges; its vertex count is \(2r+4\). The sequential model selects uniformly among currently available vertices, occupies the selected vertex, and excludes its neighbors, continuing until no vertex remains available. Equivalently, assign independent uniform priorities in \((0,1)\) and process them in increasing order. The static model chooses uniformly from all inclusion-maximal independent sets. Both random variables count vertices, not configurations. The statements hold for every integer \(r\ge2\), with no asymptotic assumption except for the displayed limits.

## Proof
Write the four-cycle as \(h-a-b-c-h\). If \(h\) is occupied, each triangle's other vertices are excluded and the opposite four-cycle vertex \(b\) is necessarily occupied, producing size \(2\). Otherwise each triangle supplies exactly one of its two nonhub vertices. On the remaining three-vertex path \(a-b-c\), either the middle vertex is occupied, giving size \(r+1\), or both endpoints are occupied, giving size \(r+2\). For each of these two options there are exactly \(2^r\) maximal independent sets. There is one size-two maximal set. Therefore the total number is \(1+2^{r+1}\), proving the static column.

For the sequential law, use independent uniform priorities. Let the priority of \(h\) be \(t\in(0,1)\). Its acceptance requires both nonhub vertices in each of the \(r\) triangles to have priorities larger than \(t\), an event of probability \((1-t)^{2r}\). On the square, \(h\) is available at time \(t\) precisely when either both neighbors \(a,c\) have priorities larger than \(t\), or the opposite vertex \(b\) precedes their earliest priority and that earliest priority does not exceed \(t\). The square event has conditional probability
\[
(1-t)^2+\int_0^t2u(1-u)\,du=(1-t)^2+t^2-\frac{2t^3}{3}.
\]
The triangle priorities and square priorities are independent, so
\[
\begin{aligned}
\Pr(S_r=2)&=\int_0^1(1-t)^{2r}\left((1-t)^2+t^2-\frac{2t^3}{3}\right)dt\\
&=\frac1{2r+3}+\frac2{(2r+1)(2r+2)(2r+3)}\\
&\quad-\frac4{(2r+1)(2r+2)(2r+3)(2r+4)}\\
&=\frac{r+1}{(r+2)(2r+1)}.
\end{aligned}
\]

Next, the terminal set has size \(r+1\) exactly when \(b\) is the earliest of the three priorities for \(a,b,c\), and \(h\) is rejected due to some triangle. Indeed, the earlier \(b\) blocks both \(a,c\), and cannot block \(h\), so rejection of \(h\) then occurs precisely if at least one triangle has a nonhub priority below that of \(h\). The event that \(b\) is first among \(a,b,c\) has probability \(1/3\), independently of the triangle and hub priorities. The probability that all \(2r\) triangle nonhub priorities exceed that of \(h\) is \(1/(2r+1)\), by uniform relative ranks. Consequently,
\[
\Pr(S_r=r+1)=\frac13\left(1-\frac1{2r+1}\right)=\frac{2r}{3(2r+1)}.
\]
Complementation gives the last sequential mass.

For all \(r\ge2\), \(\Pr(S_r=2)>\Pr(T_r=2)\): indeed \(\Pr(S_r=2)>1/(2r+3)\), while \(1+2^{r+1}>2r+3\). At the next support value,
\[
\Pr(S_r\le r+1)<\frac{2r+3}{3(2r+1)}<\frac12<\frac{1+2^r}{1+2^{r+1}}=\Pr(T_r\le r+1),
\]
where the middle strict inequality holds because \(r\ge2\). Hence the two cumulative laws cross. Finally, the mass difference at size \(r+1\) is strictly negative, while those at sizes \(2\) and \(r+2\) are positive by the two crossing inequalities. For three-point laws, total variation is the magnitude of the unique negative mass difference, yielding the displayed exact formula and limit \(1/6\). The two rare-mass asymptotics follow immediately from their rational and exponential formulas.

## Verification
The standalone file `CHECK.py` independently implements exact rational sequential dynamics by recursion over all available-vertex masks, and enumerates maximal independent sets directly rather than relying on the proof's structure. It compares both full laws for \(r\in\{2,3,4\}\) and checks rational crossover and total variation identities for \(2\le r\le80\). Run `python3 CHECK.py` from the unpacked directory. The finite checks serve as diagnostic cross-validation; the integral, enumeration and inequalities above establish the all-parameter result.

## Relationship to prior work
Higuita-Diaz, López and Roldán-Correa (arXiv:2611.14718v1, Sections 2 and 5.3) define the two ensembles and give exactly the \(r=2\), eight-vertex triangle–square example, including crossing cumulative probabilities \(3/20\) versus \(1/9\) and \(5/12\) versus \(5/9\). That finite instance is credited, not new. Their general connected counterexample family in Section 5.1 has only two possible occupancy sizes and therefore cannot itself establish the present three-point crossing. The new claim is the exact analysis for every \(r\ge2\), the persistence of incompatibility under a natural shared-hub enlargement, and the limiting total-variation and rare-state comparison. Results on clique-only bouquets, wheels and individual cycles do not directly cover the quadrilateral-bearing family. General random greedy independent-set theory supplies context but is not represented as an independently new model.

## Limitations
The graph family has unbounded hub degree and does not test the degree-at-most-three conjecture in the motivating paper. No claim is made for every block graph or every cycle bouquet, for other sampling measures, or that the rate \(1/6\) is extremal among graphs. Searches do not establish uniqueness or publication priority; an unindexed general theorem for shared-vertex graph compositions could subsume the result. Independent external mathematical assessment has not occurred.

## References
1. R. Higuita-Diaz, L. López, A. Roldán-Correa, *Stochastic Dominance in Discrete Parking Processes on Graphs*, arXiv:2611.14718v1 (first submitted 2026-11-10), https://arxiv.org/html/2611.14718v1 .
2. *Greedy maximal independent sets via local limits*, *Random Structures & Algorithms* 64 (2024), 986–1015, https://doi.org/10.1002/rsa.21200 .
