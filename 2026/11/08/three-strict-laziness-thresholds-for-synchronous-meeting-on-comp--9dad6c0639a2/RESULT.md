# Three strict laziness thresholds for synchronous meeting on complete split graphs

## Finding
For all integers \(a,b\ge 2\), let \(G=K_a\vee\overline{K_b}\) be the complete split graph with a clique of size \(a\) and a nonadjacent class of size \(b\). Two independent walkers start at distinct vertices and, simultaneously at each integer step, hold with common probability \(p\in(0,1)\), otherwise move to a uniformly chosen neighbor. The meeting time is their first positive simultaneous vertex coincidence. Write \(H_{CC},H_{CI},H_{II}\) for the mean meeting times when initially at distinct clique vertices, at a clique and an independent vertex, and at distinct independent vertices, respectively.

There exist exactly three strict thresholds \(0<\alpha_{a,b}<\beta_{a,b}<\gamma_{a,b}<1\). Across the four open intervals between them the complete strict orders are

\[
\begin{array}{c|c}
0<p<\alpha_{a,b}&H_{II}<H_{CC}<H_{CI}\\
\alpha_{a,b}<p<\beta_{a,b}&H_{II}<H_{CI}<H_{CC}\\
\beta_{a,b}<p<\gamma_{a,b}&H_{CI}<H_{II}<H_{CC}\\
\gamma_{a,b}<p<1&H_{CI}<H_{CC}<H_{II}.
\end{array}
\]

At each threshold precisely the indicated adjacent pair is tied: \(H_{CC}=H_{CI}\) at \(\alpha\), \(H_{CI}=H_{II}\) at \(\beta\), and \(H_{CC}=H_{II}\) at \(\gamma\). All other inequalities remain strict. The thresholds are the unique roots in \((0,1)\) of, respectively, the explicit quadratics \(Q_{a,b}\), \(R_{a,b}\), \(S_{a,b}\) below.

## Assumptions and scope
All graphs are finite, connected, simple and unweighted. The holding decisions and neighbor choices of the two walkers are independent between agents and steps. One step means both walkers update simultaneously, and a meeting is counted only when the two endpoint vertices coincide (not when they exchange locations along an edge). The starting vertices are distinct; \(a,b\ge2\) ensures that all three classes exist. No assertion is made at \(p=0\) or \(p=1\), where periodicity or nonmoving behavior may matter.

Put \(d=a+b-1\), \(q=(1-p)/d\), \(r=(1-p)/a\), and \(c=p+(a-1)q\). Then \(H=(H_{CC},H_{CI},H_{II})^\mathsf{T}\) is \((I-M)^{-1}{\bf1}\), for

\[
M=\begin{pmatrix}
c^2-2pq-(a-2)q^2&2bcq&b(b-1)q^2\\
(a-1)rc&pc+bq(1-p)&(b-1)pq\\
a(a-1)r^2&2par&p^2
\end{pmatrix}.
\]

To state the thresholds, let \(Q=q_0+q_1p+q_2p^2\) and \(R=r_0+r_1p+r_2p^2\), where

\[
\begin{aligned}
q_0&=a+b^2+b-1,\\
q_1&=-a^2-5ab+2a-5b^2+5b-2,\\
q_2&=a^2+3ab-a+2b^2-2b+1;\\
r_0&=-b(a^2+3ab-2a+b^2-3b),\\
r_1&=2a^3+8a^2b-5a^2+8ab^2-16ab+3a+b^3-9b^2+5b-1,\\
r_2&=a^2b+3a^2+3ab^2+6ab-3a+2b^3+2b^2-3b+1.
\end{aligned}
\]

Set \(S=(b-1)Q+R\).

## Proof
**Absorbing reduction.** The graph automorphism orbits of unordered distinct vertex pairs are precisely \(CC\), \(CI\), \(II\). The probabilities of transitioning among these nonmeeting classes are the entries of \(M\), obtained by partitioning the independent one-step destinations. For example, from \(II\), the probability of landing at distinct clique vertices is \(a(a-1)r^2\), of landing in different parts is \(2par\), and of remaining at the same two distinct independent vertices is \(p^2\). From each orbit there is a strictly positive probability of meeting within at most two steps, since \(0<p<1\). Hence the substochastic matrix \(M\) is transient, so \(I-M\) is a nonsingular \(M\)-matrix with \(\Delta=\det(I-M)>0\). First-step conditioning gives \((I-M)H={\bf1}\).

**Exact differences.** Cramer's rule and algebraic cancellation give
\[
\begin{aligned}
\Delta(H_{CC}-H_{CI})&=-\frac{(b-1)(1-p)^2}{a d^3}Q(p),\\
\Delta(H_{CI}-H_{II})&=-\frac{(1-p)^2}{a d^3}R(p),\\
\Delta(H_{CC}-H_{II})&=-\frac{(1-p)^2}{a d^3}S(p).
\end{aligned}
\]
The three identities, including the defining polynomial coefficients, are checked exactly in the accompanying independent symbolic checker.

**Exactly one crossing per pair.** Direct substitution yields
\[
\begin{array}{ll}
Q(0)=a+b^2+b-1>0,&Q(1)=-2(b-1)(a+b-1)<0,\\
R(0)=-b(a^2+3ab-2a+b^2-3b)<0,&R(1)=2(a+b-1)(a^2+3ab+b^2-b)>0,\\
S(0)=-(a-1)(ab+3b^2-2b+1)<0,&S(1)=2(a+b-1)(a^2+3ab+b-1)>0.
\end{array}
\]
All displayed factors have the indicated signs for \(a,b\ge2\). Each is a polynomial in \(p\) of degree at most two; opposite endpoint signs imply exactly one simple root in \((0,1)\) (two interior roots would force equal endpoint signs). Call them \(\alpha,\beta,\gamma\).

**The strict order of the crossings.** The Sylvester resultant factorizes exactly as
\[
\operatorname{Res}_p(Q,R)=-2(a+b-1)\bigl(a(b-2)+(b-1)^2\bigr)P(a,b).
\]
Write \(u=a-2\ge0\) and \(v=b-2\ge0\). The polynomial \(P\) has the following exact expansion, with every listed coefficient strictly positive:
\[
\begin{aligned}
P(u+2,v+2)={}&u^7+(11v+32)u^6\\
&+(51v^2+298v+433)u^5\\
&+(129v^3+1135v^2+3312v+3208)u^4\\
&+(192v^4+2261v^3+9937v^2+19328v+14049)u^3\\
&+(168v^5+2484v^4+14621v^3+42842v^2+62527v+36391)u^2\\
&+(80v^6+1428v^5+10564v^4+41475v^3+91194v^2+106542v+51711)u\\
&+16v^7+336v^6+3004v^5+14832v^4+43706v^3+76917v^2+74910v+31171.
\end{aligned}
\]
Consequently the resultant is strictly negative everywhere on the connected real quadrant \(a,b\ge2\), and \(Q,R\) never share an interior root. Their unique roots vary continuously; thus the ordering of \(\alpha\) and \(\beta\) is constant over this quadrant. At \(a=b=2\), evaluating at \(p=4/15\) gives \(Q=-41/225<0\) and \(R=-128/75<0\), so \(\alpha<4/15<\beta\). Therefore \(\alpha<\beta\) for all admissible sizes. At \(p=\beta\), since \(Q(\beta)<0\), one has \(S(\beta)=(b-1)Q(\beta)<0\). Because \(S(1)>0\) and \(S\) has one interior root, \(\gamma>\beta\). The three sign formulas now yield exactly the four displayed orderings. At each distinct crossing only its corresponding difference vanishes. This proves the theorem.

## Verification
The standalone \(`checker.py`\) independently forms the three-orbit transition matrix, symbolically inverts it, derives the quadratics from the three differences, verifies their endpoint factorizations and the entire Sylvester-resultant identity, and checks all 36 strictly positive coefficients of the shifted resultant factor. Separately, it constructs the full unordered-pair chain directly on each of six graph sizes and three rational holding probabilities and compares every individual starting pair against the reduced exact formula. It passes 267 exact comparisons. Run with \(`python checker.py`\) using Python 3 and SymPy; output begins \(`VERIFY_OK`\).

## Relationship to prior work
General meeting/coalescence bounds on graphs are given by Kanade, Mallmann-Trenn and Sauerwald (2016), and Oliveira and Peres (2018). Alpern and Zeng (2021), Section 2, establish the absorbing fundamental-matrix treatment for synchronous independent lazy walkers; their solved gathering networks in Sections 4–5 are cycles, not the complete split family. Eguchi and collaborators (2023) analyze a different adversarial non-atomic, single-agent-at-a-time model. These results motivate the problem and supply broad methods, but do not themselves specify the three strict size-uniform phase boundaries here. The matrix method by itself is not claimed as new; the exact all-parameter root ordering is the contribution. No historical-priority guarantee is claimed.

## Limitations
The result concerns only two independent synchronous walkers, common homogeneous holding probability, complete split graphs with both classes of size at least two, and expected first coincidence from distinct starting vertices. It does not characterize distributions of meeting times, optimizing \(p\), asynchronous interactions, or robust estimation from sampled trajectories. No independent audit has been performed, and older or differently indexed sources could contain equivalent classifications.

## References
1. Kanade, Mallmann-Trenn and Sauerwald (2016), *On coalescence time in graphs: When is coalescing as fast as meeting?* https://arxiv.org/abs/1611.02460.
2. Oliveira and Peres (2018), *Random walks on graphs: new bounds on hitting, meeting, coalescing and returning*. https://arxiv.org/html/1807.06858v1.
3. Alpern and Zeng (2021), *Social Distancing, Gathering, Search Games: Mobile Agents on Simple Networks*. https://arxiv.org/html/2111.05958v1.
4. Eguchi, Ooshita, Inoue and Tixeuil (2023), *Meeting Times of Non-atomic Random Walks*. https://arxiv.org/html/2305.11590v1.
