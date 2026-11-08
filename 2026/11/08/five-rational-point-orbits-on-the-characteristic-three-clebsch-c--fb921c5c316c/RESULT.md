# Five rational point orbits on the characteristic-three Clebsch cubic

## Finding
Let \(k=\mathbb F_9=\mathbb F_3[\iota]/(\iota^2+1)\), and let \(X\subset\mathbb P^4_k\) be the Clebsch cubic surface
\[
X:\quad \sigma_1(x_0,\ldots,x_4)=\sigma_3(x_0,\ldots,x_4)=0,
\]
where \(\sigma_j\) is the degree-\(j\) elementary symmetric polynomial. The faithful coordinate-permutation action of \(G=S_5\) on the \(145\) rational points \(X(k)\) has **exactly five orbits**. Their representatives, sizes, stabilizers up to isomorphism, and numbers of containing geometric lines are:

| Representative in \(\mathbb P^4(k)\) | Orbit size | Stabilizer | Lines through a point |
|---|---:|---|---:|
| \((0,0,0,1,-1)\) | 10 | \(S_3\times C_2\) | 3 |
| \((0,1,1,-1,-1)\) | 15 | \(D_8\) (order 8) | 2 |
| \((0,1,-1,\iota,-\iota)\) | 30 | \(C_4\) | 1 |
| \((1,1,\iota,\iota,1+\iota)\) | 30 | \(C_2\times C_2\) | 2 |
| \((0,1,-1,1+\iota,-1-\iota)\) | 60 | \(C_2\) | 2 |

In particular, **every \(k\)-rational point has a nontrivial involutory projective symmetry**, and none has trivial stabilizer. The rational-point line-incidence distribution is exactly \(30\) on one line, \(105\) on two lines, and \(10\) on three lines. The two distinct size-\(30\) orbits have nonisomorphic stabilizers and different line incidence.

## Assumptions and scope
All coordinates and points are over the exact field \(\mathbb F_9\), not an arbitrary field of characteristic three; \(\iota^2=-1\). A projective point is a nonzero quintuple modulo multiplication by \(k^\times\). The action of \(S_5\) permutes the five coordinates. The word *line* means a projective line geometrically contained in this smooth cubic surface, not an arbitrary secant. The result classifies rational points under the specified full coordinate-permutation group; it is not a classification of cubic surfaces.

## Proof
**Smoothness.** Work over an algebraic closure of characteristic three. On the hyperplane \(\sigma_1=0\), the partial derivatives of \(\sigma_3\) are \(\sigma_2+x_i^2\). A singular point therefore has \(x_i^2=x_j^2\) for all \(i,j\). If all vanish, the coordinates are zero. Otherwise the five coordinates are \(\pm a\), and \(\sigma_1=0\) forces four of one sign and one of the other (since characteristic is three). For that multiplicity pattern \(\sigma_3=\pm a^3\ne0\), a contradiction. Thus \(X\) is smooth.

**Five projective orbits.** Direct substitution in \(\sigma_1=\sigma_3=0\) verifies the five representative points. Orbit-stabilizer follows by asking which \(\lambda\in k^\times\) preserves the multiset of five coordinates, then permuting repeated entries. The first has a triple zero and an opposite pair, giving \(S_3\times C_2\) of order \(12\). The second has one zero and two double entries exchanged by scalar \(-1\), giving \(D_8\) of order \(8\). The third has nonzero entries equal to the cyclic order-four subgroup \(\{\pm1,\pm\iota\}\), giving \(C_4\). The fourth has two repeated pairs, with no nonidentity scalar preserving their multiset, giving \(C_2^2\). The fifth has two opposite pairs but no fourth-root scalar symmetry, giving \(C_2\). The orbits are disjoint by zero-pattern, multiplicity, and stabilizer order (with the two size-\(30\) representatives distinguished by their nonisomorphic order-four stabilizers).

These sizes sum to \(10+15+30+30+60=145\). The surface contains \(27\) rational lines, as independently proved below. A split smooth cubic surface over \(\mathbb F_q\) has \(q^2+7q+1\) rational points, by its blow-up description as \(\mathbb P^2\) at six rational points (also [2], Corollary 3.2). At \(q=9\), this is \(145\), so the disjoint five orbits exhaust every rational point.

**All lines and their incidence.** Consider the projective spans \(A\) and \(B\) over \(k\):
\[
A=\mathbb P\langle(1,-1,0,0,0),(0,0,1,-1,0)\rangle,
\]
\[
B=\mathbb P\langle(0,1,-1,1+\iota,-1-\iota),
(1,0,1+\iota,-1,-1-\iota)\rangle.
\]
Their spanning vectors lie on \(\sigma_1=0\). Exact substitution shows that \(\sigma_3\) vanishes identically along each span; equivalently, the \(10\) distinct \(k\)-points of each span satisfy \(\sigma_3=0\), which forces the binary cubic restriction to vanish identically. The \(S_5\)-orbit of \(A\) comprises the \(15\) coordinate-pairing lines. The orbit of \(B\) comprises \(12\) additional lines, none having one coordinate identically zero. These orbit cardinalities follow by enumerating the \(120\) coordinate permutations, with line equality determined by their exact \(10\)-point sets; alternatively by their permutation stabilizers of orders \(8\) and \(10\), respectively. Since a smooth cubic surface has exactly \(27\) geometric lines, these two orbits exhaust all of them, and they are all \(k\)-rational.

For a point \(v\), the number of containing lines of each type equals the number of distinct members of the finite sets \(\{gA:g\in S_5\}\) and \(\{gB:g\in S_5\}\) that contain \(v\). Testing the five displayed representatives by exact quintuple comparison gives the respective counts \((3,0),(2,0),(1,0),(0,2),(1,1)\). These counts are constant on \(S_5\)-orbits. The two independent executable verifiers calculate the line orbits and the incidence counts in different ways. This completes the point-orbit and incidence classification.

## Verification
The self-contained standard-library scripts `verify_orbits.py` and `verify_census.py` require Python 3. The first independently constructs the two \(S_5\)-line orbits, checks the five representatives and their stabilizers, and checks each orbit's line incidence. The second enumerates every rational point by four free coordinates and the trace hyperplane equation, then enumerates every contained rational line from pairs of rational points, and checks the full orbit decomposition. Both were executed successfully from their actual package paths. Exact \(\mathbb F_9\) arithmetic uses integer representatives \(a+3b\) for \(a+b\iota\) with \(a,b\in\{0,1,2\}\). The finite exhaustive certificate is over \(\mathbb F_9\) only; no extrapolation to other fields is asserted.

## Relationship to prior work
The characteristic-independent alternate Clebsch equation \(\sigma_1=\sigma_3=0\), the \(S_5\) action, and the group-theoretic classification are given by Dolgachev–Duncan [1], notably Section 6 and Section 12. Betten–Hirschfeld–Karaoglu [2, Table 1] already identify the split diagonal cubic over \(\mathbb F_9\), its \(10\) Eckardt points, and group of order \(120\); their Corollary 3.2 gives the surface point count. Betten–Karaoglu [3] classify split cubics over small fields and describe line configurations and group orders. None of these prior statements supplies the exact **five point-orbit decomposition with its two different order-four stabilizers and orbit-specific line incidences**. This distinction is the claim of the present result; the known surface, equation, line count and total point count are not claimed as new.

## Limitations
This is an exact arithmetic result for a single canonically distinguished surface over a single field, motivated by its characteristic-three symmetry and smallest split realization, not a general formula over extensions. It does not classify geometric orbits over an algebraic closure. It does not imply that the same five orbits persist over larger fields. The historical-priority comparison is not an independent literature audit, and an older finite-geometric table of point orbits could exist under other terminology.

## References
[1] I. Dolgachev and A. Duncan, *Automorphisms of cubic surfaces in positive characteristic*, arXiv:1712.01167, initially public 2017-12-04, https://arxiv.org/abs/1712.01167 ; particularly Sections 6, 12, 13.

[2] A. Betten, J. W. P. Hirschfeld and F. Karaoglu, *Classification of cubic surfaces with twenty-seven lines over the finite field of order thirteen*, European Journal of Mathematics 4 (2018), 37–50, initially public 2017-09-27, https://doi.org/10.1007/s40879-017-0182-0 ; specifically Table 1, Section 2, Corollary 3.2.

[3] A. Betten and F. Karaoglu, *Cubic surfaces over small finite fields*, Designs, Codes and Cryptography 87 (2019), 931–953, 2018 preprint available via https://doi.org/10.1007/s10623-018-0590-2 ; Tables 2–3 and Sections 4–6.
