# Parallel-class rigidity and the exact packing-colouring census of finite affine-plane incidence graphs

## Finding
Let \(\mathcal A\) be any finite affine plane of order \(q\ge3\), including a non-Desarguesian plane if one exists. Let \(G\) denote its simple point–line incidence graph. Then
\[
\chi_\rho(G)=q^2-q+3.
\]
More precisely, a map \(c:V(G)\to\{1,\ldots,q^2-q+3\}\) is a minimum-palette packing colouring if and only if there are distinct parallel directions \(D_2,D_3\) such that

1. every point has colour \(1\);
2. the \(q\) lines of direction \(D_2\) have colour \(2\);
3. the \(q\) lines of direction \(D_3\) have colour \(3\);
4. the other \(q(q-1)\) lines are assigned all colours from \(4\) to \(q^2-q+3\), each exactly once.

There are exactly
\[
(q+1)q\,\bigl(q(q-1)\bigr)!
\]
such *named* optimum colourings. The independence number is \(q^2+q\) (all lines), but no optimum uses that maximum independent shore for colour \(1\); it uses the smaller point shore of size \(q^2\).

## Assumptions and scope
An affine plane of order \(q\) has \(q^2\) points, \(q(q+1)\) lines, \(q+1\) parallel classes of \(q\) pairwise disjoint lines, exactly \(q\) points per line, and exactly \(q+1\) lines incident with a point. Every pair of distinct points lies on one line; lines in distinct parallel classes meet at one point. No field structure is used.

For an integer \(k\ge1\), a *packing \(k\)-colouring* is an assignment \(c:V(G)\to\{1,\ldots,k\}\) for which equal colour \(i\) on distinct vertices requires graph distance strictly greater than \(i\). Empty colour classes are allowed. The smallest possible \(k\) is \(\chi_\rho(G)\). A *named* colouring distinguishes the numerical colour labels and the actual vertices of the given plane. The theorem assumes \(q\ge3\), and makes no claim about the exhaustive optimum classification at order two.

## Proof
**Step 1: distances and the two small positive colour classes.** Any two points have distance two. Two distinct lines have distance two if they meet and distance four if they are parallel. A point and nonincident line have distance three, while an incident point–line pair has distance one. Thus \(\operatorname{diam}(G)=4\). A colour used with index \(i\ge4\) is necessarily a singleton.

A colour-\(3\) class with at least two vertices consists entirely of lines in a single parallel class, and therefore has size at most \(q\). A colour-\(2\) class contains at most one point and its lines must be mutually parallel. If it contains a point, it omits the unique line of that direction through the point; hence it contains at most \(1+(q-1)=q\) vertices. If it has no points, it also has at most \(q\) vertices. Therefore, for the colour classes \(C_i=c^{-1}(i)\),
\[
|C_2|\le q,\qquad |C_3|\le q.
\]

**Step 2: sharp independent-set lemma with at least one point.** Let \(C_1=A\sqcup B\) be independent, with \(A\) points and \(B\) lines. Suppose \(A\ne\varnothing\), and fix \(x\in A\). Remove the point \(x\) and all \(q+1\) lines through it from the incidence structure. The resulting bipartite graph \(H_x\) has \(q^2-1\) points and \(q^2-1\) lines, and is \(q\)-regular on both sides: every remaining point lies on \(q\) remaining lines, and every remaining line contains \(q\) remaining points. Every subset of its line shore has at least as many neighbouring points by counting incidence edges, so
\[
|B|\le |N(B)|\le q^2-|A|,\qquad |C_1|\le q^2.
\]
The graph \(H_x\) is connected. Indeed, for two remaining points \(p,z\), if their joining line avoids \(x\), they are joined by a two-edge path in \(H_x\). Otherwise choose a point \(w\) outside their common line through \(x\); the lines joining \(p\) to \(w\) and \(w\) to \(z\) both avoid \(x\), giving a four-edge path. Every remaining line has point neighbours, so the whole graph is connected.

We also need the equality case. If \(|C_1|=q^2\) and \(B=\varnothing\), then \(A\) is the full point shore. Otherwise equality forces \(|B|=|N(B)|>0\) inside the connected \(q\)-regular bipartite graph \(H_x\). Equality in the degree count implies every line adjacent to \(N(B)\) belongs to \(B\); therefore \(B\sqcup N(B)\) is a union of connected components of \(H_x\). Connectivity forces \(B\) to be all \(q^2-1\) lines avoiding \(x\), and then independence forces \(A=\{x\}\). We have shown that the only independent sets of size \(q^2\) which contain a point are the entire point shore and, for each point \(x\), the union of \(\{x\}\) with all lines not passing through \(x\).

**Step 3: upper bound on the total occupancy of the first three colours.** Write \(T=|C_1|+|C_2|+|C_3|\). If \(C_1\) contains a point, Steps 1 and 2 give \(T\le q^2+2q\). If \(C_1\) contains no point, all points used by colours \(2\) and \(3\) number at most two, because each of those colours can contain at most one point; the line vertices appearing among the first three colours are pairwise disjoint subsets of the \(q^2+q\) lines. Thus
\[
T\le q^2+q+2<q^2+2q\quad(q\ge3).
\]
Consequently \(T\le q^2+2q\) always. To have equality, \(C_1\) must contain a point and attain size \(q^2\), while each of \(C_2,C_3\) must attain size \(q\).

If \(C_1=\{x\}\cup\{\text{all lines avoiding }x\}\), the only lines not in \(C_1\) pass through \(x\) and are pairwise at distance two; hence \(C_3\) can contain at most one of them. It cannot contain that line together with a point, or two points, since the corresponding distances are at most three and two. Therefore \(|C_3|\le1<q\), a contradiction. Hence equality \(T=q^2+2q\) forces \(C_1\) to be the entire point shore. The remaining vertices are all lines. A \(q\)-element colour-\(2\) or colour-\(3\) class of lines must be exactly one parallel class, and the two classes must be distinct.

**Step 4: palette bound, construction and enumeration.** The graph has \(2q^2+q\) vertices. Colours indexed at least four are singleton classes, so any packing \(k\)-colouring with \(k\ge3\) satisfies
\[
2q^2+q\le |C_1|+|C_2|+|C_3|+(k-3)
\le q^2+2q+k-3,
\]
and consequently \(k\ge q^2-q+3\). A colouring with at most two colours would leave every vertex in the first three classes, contradicting \(2q^2+q>q^2+2q\) (as the unused classes may be taken empty).

Choose an ordered pair of distinct line directions, give colour one to all points, colours two and three to those respective entire directions, and use separate colours \(4,\ldots,q^2-q+3\) on the other \(q(q-1)\) lines. This is a valid packing colouring with the lower-bound palette. Equality throughout the counting bound is necessary for any optimum and forces exactly the classification established in Step 3, with every higher colour used on one remaining line. There are \((q+1)q\) ordered pairs of directions and \((q(q-1))!\) bijections from the leftover lines to the remaining named colours. This proves all assertions.

## Verification
The standalone script `verify_packing.py` independently constructs the affine plane of order three, computes graph distances, enumerates every one of its 8,876 colour-one independent sets and every admissible colour-two and colour-three subset of size at most three, and maximizes total occupancy of the first three colours subject to disjointness. It obtains a unique optimum profile with coverage 15 and exactly 12 ordered triples of classes, yielding \(\chi_\rho=9\) and 8,640 named optimum colourings. The enumeration is exhaustive for order three only; it does not substitute for the all-order proof.

The independent script `verify_geometry.py` constructs the affine planes of orders three and four with different field and incidence routines (including arithmetic in the four-element field), checks all point-pair and line-pair incidences, diameter four, the claimed explicit optimal colouring, the point-containing independent-set equality cases for all nonempty point subsets, and connected \(q\)-regular residual incidence graphs for every removed point. Both scripts run with Python 3 and the standard library alone:

```sh
python3 verify_packing.py
python3 verify_geometry.py
```

## Relationship to prior work
Goddard, Hedetniemi, Hedetniemi, Harris and Rall introduced broadcast chromatic colourings, now called packing colourings, in 2008. Their general definition and diameter-two bounds are the starting point, not claims of novelty here.

Fresán-Figueroa, González-Moreno and Olsen studied packing chromatic numbers of regular Moore graphs corresponding to symmetric generalized polygons, including projective-plane incidence graphs. An affine-plane incidence graph is biregular, with \(q\)-valent line vertices and \((q+1)\)-valent point vertices, so their regular Moore-graph hypotheses fail. Their projective-plane theorem has diameter three and uses different distance restrictions; it does not imply the present diameter-four affine-plane value or enumeration. A separate result on optimum packing colourings of projective-plane incidence graphs likewise does not imply the affine statement by deleting a line: such deletion changes the diameter and the colour-two/colour-three admissibility patterns.

Related work on affine-plane hypergraph colourings concerns monochromatic line constraints rather than metric-distance packing classes. A search of the accessible mathematical-results index and targeted literature did not reveal the exact affine formula or rigidity theorem. This is evidence for an originality assessment, not a proof of historical novelty.

## Limitations
The result is conditional only on the existence of an affine plane of a given order, and assumes \(q\ge3\). It does not treat the exceptional binary affine plane or classify non-optimal colourings. The stated census counts named colour labels and the actual vertices, without identifying colourings under plane automorphisms. Priority over inaccessible or unindexed literature cannot be guaranteed. The scripts verify two small orders and are not independent formal certification of the infinite proof.

## References
1. W. Goddard, S. M. Hedetniemi, S. T. Hedetniemi, J. M. Harris, D. F. Rall, *Broadcast Chromatic Numbers of Graphs*, Ars Combinatoria 86 (2008), 33–49. https://combinatorialpress.com/ars-articles/volume-086-ars-articles/broadcast-chromatic-numbers-of-graphs/ (first published 31 January 2008).
2. J. Fresán-Figueroa, D. González-Moreno, M. Olsen, *On the packing chromatic number of Moore graphs*, arXiv:1909.11638 (2019), https://arxiv.org/abs/1909.11638; Discrete Applied Mathematics 289 (2021), 185–193, https://doi.org/10.1016/j.dam.2020.10.009.
