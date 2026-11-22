# Integral component group of the resolved icosahedral fifteen-line boundary

## Finding

The reduced strict-transform-plus-exceptional boundary of the classical fifteen-line icosahedral reflection arrangement is a stable nodal curve with 31 rational components, 75 nodes and arithmetic genus 45. Its dual graph \(\Gamma\) has integral critical group
\[
\boxed{K(\Gamma)\cong\mathbb Z/527\mathbb Z\ \oplus\ (\mathbb Z/5797\mathbb Z)^4.}
\]
Equivalently, its prime-primary groups are \((\mathbb Z/11\mathbb Z)^4\), \((\mathbb Z/17\mathbb Z)^5\) and \((\mathbb Z/31\mathbb Z)^5\). The spanning-tree count is
\[
\tau(\Gamma)=11^4\cdot17^5\cdot31^5=595146407909049887.
\]
The same group is the *geometric* Néron component group for every proper regular split semistable smoothing with this special fiber and unit edge lengths.

## Assumptions and scope

Work over \(\mathbb C\). Fix \(\varphi\in\mathbb C\) with \(\varphi^2-\varphi-1=0\), and choose the six distinct poles in \(\mathbb P^2\)
\[
\begin{gathered}
(0:1:\varphi),\ (0:1:-\varphi),\ (1:\varphi:0),\\
(1:-\varphi:0),\ (\varphi:0:1),\ (-\varphi:0:1).
\end{gathered}
\]
For each two-element subset of these six poles, take their joining projective line; the resulting fifteen distinct lines form the standard projective icosahedral \(H_3\) reflection arrangement. Let \(X\to\mathbb P^2\) be the simultaneous blowup of all its intersection points of multiplicity at least three. Let \(D\) be the reduced union in \(X\) of the fifteen strict line transforms and all newly introduced exceptional curves. Its nodes are transverse and its components are smooth rational curves. The graph \(\Gamma\) has one vertex per component and one edge per node, without contracting the fifteen retained ordinary double intersections.

For a connected graph \(\Gamma\), \(K(\Gamma)\) means the finite cokernel of any cofactor of its integer Laplacian (equivalently, its degree-zero divisor class group). The group statement is over \(\mathbb Z\), not merely a rational-Laplacian spectrum or a group order. A geometric Néron identification is asserted only for a regular proper split semistable model over a discrete valuation ring whose reduced special fiber has this graph, geometric multiplicity one and thickness one at every node.

## Proof

**1. Exact incidence reconstruction.** Represent \(a+b\varphi\) by the rational pair \((a,b)\), with multiplication
\[
(a,b)(c,d)=(ac+bd,ad+bc+bd).
\]
For the six displayed projective poles, take the cross product for all \(\binom62=15\) pairs, projectively normalizing its first nonzero coordinate to one. These fifteen normals are distinct and, after swapping the second and third coordinates, coincide with the conventional \(H_3\) root-normal set consisting of three coordinate axes and all twelve cyclic permutations of \((1,arphi,arphi-1)\) with independent signs on its final two entries; the script checks this equality of normalized projective sets exactly. For each of the \(\binom{15}2=105\) unordered pairs of normals, take and projectively normalize their cross product. Two line pairs belong to the same intersection point exactly when their normalized cross products agree in \(\mathbb Q(\varphi)^3\). The exhaustive, transparent rational-arithmetic enumeration in `verify_icosahedral_boundary.py` produces fifteen classes with two incident lines, ten with three and six with five. These exhaust all \(105=15+10\binom32+6\binom52\) line pairs.

**2. Stable dual graph and genus.** Blow up the ten triple and six quintuple points, separating all original line branches there. Each such point introduces one exceptional component meeting its incident strict transforms once. Each of the fifteen original double intersections remains a transverse node. Thus there are \(15+10+6=31\) components, \(15+10\cdot3+6\cdot5=75\) nodes, and connected arithmetic genus \(75-31+1=45\). Exact reconstruction gives degrees six for every strict line component, three for every triple-point exceptional and five for every quintuple exceptional. Every genus-zero component has at least three nodes; hence \(D\) is stable.

**3. Independent determinant and spectral checks.** Form the integer \(31\times31\) Laplacian \(L\) from the 75 edges. Fraction-free Bareiss elimination of each of two different principal \(30\times30\) cofactors gives
\[
\det L_{\mathrm{red}}=595146407909049887=11^4\,17^5\,31^5.
\]
Independently, exact integer Faddeev–LeVerrier iteration on all 31 vertices gives the complete characteristic polynomial
\[
\det(uI-L)=u(u^2-12u+31)^6(u^2-10u+17)^5(u^2-7u+11)^4.
\]
The coefficient of \(u\) is \(31\tau(\Gamma)\) because there are 31 Laplacian eigenvalues and precisely one is zero. This agrees with both cofactor determinants by the matrix-tree theorem; connectivity also follows from the explicit edge construction.

**4. Complete integral Smith invariants.** Exact Gaussian elimination over the three finite fields gives the following data for a \(30\times30\) reduced cofactor:
\[
\begin{array}{c|ccc}
\text{prime}&11&17&31\\\hline
v_p(\det L_{\mathrm{red}})&4&5&5\\
\operatorname{nullity}_{\mathbb F_p}(L_{\mathrm{red}})&4&5&5
\end{array}.
\]
For an integer matrix of nonzero determinant, the number of Smith entries divisible by a prime equals its modular nullity, and the sum of their valuations equals its determinant valuation. Equality here forces every divisible Smith entry to have exponent exactly one. As the determinant has no other prime divisors, the invariant factors are 25 units, one entry \(17\cdot31=527\), and four entries \(11\cdot17\cdot31=5797\). This proves the stated complete isomorphism of \(K(\Gamma)\), not only its order.

**5. Néron specialization.** The graph-Jacobian/component-group theorem for a regular semistable curve with reduced special fiber and unit node thicknesses identifies the geometric component group of the Jacobian's Néron model with \(K(\Gamma)\). Apply that theorem to any smoothing satisfying the explicit hypotheses. No assertion is made about singular or nonregular total spaces.

## Verification

With Python 3 and its standard library, run `python3 verify_icosahedral_boundary.py` beside this document. The standalone script reconstructs all six poles, the fifteen lines and their exact identification with the conventional Coxeter arrangement, 105 line-pair intersections, thirty-one components and 75 graph edges with exact quadratic-field arithmetic. It checks two fraction-free cofactor determinants, all 32 coefficients of the characteristic polynomial, modular ranks for \(11,17,31\), and the integer invariant-factor product. It terminates with `ICOSAHEDRAL_15_LINE_STABLE_BOUNDARY_INTEGRAL_GROUP_OK`. The finite calculation is exhaustive because it enumerates every line pair and every entry of the finite graph Laplacian; the graph-to-Néron interpretation uses the stated general theorem rather than extrapolation from finite examples.

## Relationship to prior work

The icosahedral reflection arrangement and its singularity pattern are classical, described by Hirzebruch's study of arrangements [1], the Coxeter-arrangement analysis of Hoge–Röhrle [2], and Calvo's detailed treatment of the same 15-line/31-point configuration [3]. Prior exact studies of its modular reductions [5,6] determine the 15/10/6 double/triple/quintuple incidence partition and marked-point reductions, but do not calculate the Laplacian integral Smith form of the **resolved 31-component nodal boundary**. The general graph-Jacobian/Néron correspondence [4] does not compute a particular critical group. The present statement is therefore the specific complete integral group for this stable boundary and its eligible smoothings; it does not rename a standard invariant or assert that the classical intersection lattice itself is new.

## Limitations

The group is the graph critical group and conditional geometric Néron component group, **not** the Picard group of the blowup surface or the abstract Picard group of the singular curve. Arbitrary edge thicknesses, nonregular semistable models, special fibers with different contractions and bad-characteristic reductions are excluded. The numerical proof rests on finite exhaustive exact arithmetic included with this result. Historical originality is a targeted comparison rather than a proof that no obscure Smith-normal-form calculation already exists; a relevant book chapter on line arrangements was not available in full text.

## References

[1] F. Hirzebruch, *Arrangements of Lines and Algebraic Surfaces*, 1983, especially discussions of reflection arrangements. https://hirzebruch.mpim-bonn.mpg.de/id/eprint/244/1/hirzebrucharr.pdf

[2] T. Hoge and G. Röhrle, *Nice reflection arrangements*, arXiv:1505.04603, first posted 2015-05-18. https://arxiv.org/abs/1505.04603

[3] S. Calvo, *The icosahedral line configuration and Waldschmidt constants*, arXiv:2209.01499, first posted 2022-09-03. https://calvosebastian.github.io/docs/papers/Calvo_Icosahedral_2023.pdf

[4] The graph-Jacobian/Néron-component comparison as used in M. Baker, O. Amini, E. Brugallé, and J. Rabinoff, *Lifting harmonic morphisms I: Metrized complexes and Berkovich skeleta*, Theorem 8.2; see also Raynaud's original component-group comparison. https://www.math.ens.psl.eu/~amini/Publications/hmmcI.pdf

[5] *Arithmetic reduction and point collisions of the icosahedral reflection arrangement*, published research note. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-arithmetic-reduction-and-point-collisions-of-the-icosahedral-ref--c9c0a9f0a98b

[6] *Dyadic collapse and the thirty-one marked points of the icosahedral mirror arrangement*, published research note. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-dyadic-collapse-and-the-thirty-one-marked-points-of-the-icosahed--2c18195212c4
