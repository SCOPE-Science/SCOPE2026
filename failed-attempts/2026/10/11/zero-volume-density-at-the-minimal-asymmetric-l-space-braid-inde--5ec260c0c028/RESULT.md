# Zero volume density at the minimal asymmetric L-space braid index
## Finding
For every integer \(n\ge1\), let \(K_n\) be the closure of the Baker--Teragaito positive four-braid
\[
\beta_n=[(1,2,3)^4,2,1,3,2,2,1,1,2,1,1,1,1,1,2^{2n}].
\]
Then the displayed braid diagram is crossing-minimal and
\[
c(K_n)=2n+25=2g(K_n)+3.
\]
If \(N=S^3\setminus(K_0\cup c)\) denotes the fixed hyperbolic two-cusped parent used in the construction, then
\[
\operatorname{Vol}(S^3\setminus K_n)<\operatorname{Vol}(N)
\]
for every \(n\ge1\). Consequently
\[
0<\frac{\operatorname{Vol}(S^3\setminus K_n)}{c(K_n)}
<\frac{\operatorname{Vol}(N)}{2n+25}\longrightarrow0.
\]
Thus the family has volume density tending to zero at constant braid index \(4\). This is the smallest braid index at which an asymmetric L-space knot can occur: the source recalls that L-space knots of braid index below \(4\) are strongly invertible.

## Assumptions and scope
Crossing number \(c(K)\) is the minimum number of crossings among all planar diagrams of \(K\). Hyperbolic volume is the volume of the complete finite-volume metric on the knot complement.

Baker and Teragaito prove for every \(n\ge1\) that \(K_n\) is an asymmetric hyperbolic L-space knot, that its braid index is \(4\), and that
\[
g(K_n)=n+11.
\]
They also construct a fixed hyperbolic link complement \(N=S^3\setminus(K_0\cup c)\) and obtain \(S^3\setminus K_n\) from \(N\) by the nontrivial filling of the \(c\)-cusp with slope \(-1/n\).

No claim is made for \(n=0\), for other braid-index-four knots, or for nonhyperbolic fillings.

## Proof
The repeated block \((1,2,3)^4\) contributes \(12\) crossings. The fixed block
\[
(2,1,3,2,2,1,1,2,1,1,1,1,1)
\]
contributes \(13\), and the final power contributes \(2n\). Hence the source diagram has
\[
2n+25
\]
crossings, so \(c(K_n)\le2n+25\).

For any oriented diagram \(D\) of a knot \(K\), let \(c_D\) be its crossing number and \(s_D\) its number of Seifert circles. The canonical Seifert surface has genus
\[
g_D=\frac{c_D-s_D+1}{2}.
\]
Since \(g(K)\le g_D\),
\[
c_D\ge2g(K)+s_D-1.
\]
Yamada's theorem identifies the minimum possible value of \(s_D\) with the braid index \(b(K)\). Therefore every diagram satisfies
\[
c_D\ge2g(K)+b(K)-1,
\]
and hence
\[
c(K)\ge2g(K)+b(K)-1.
\]
For the present family, Baker and Teragaito give \(g(K_n)=n+11\) and \(b(K_n)=4\). Substitution gives
\[
c(K_n)\ge2(n+11)+4-1=2n+25.
\]
This matches the source diagram, proving exact crossing-minimality.

For the volume statement, each \(S^3\setminus K_n\) is a hyperbolic nontrivial Dehn filling of the fixed hyperbolic manifold \(N\). Hyperbolic Dehn filling strictly decreases volume, so
\[
\operatorname{Vol}(S^3\setminus K_n)<\operatorname{Vol}(N).
\]
Dividing by the exact crossing number gives
\[
0<\frac{\operatorname{Vol}(S^3\setminus K_n)}{c(K_n)}
<\frac{\operatorname{Vol}(N)}{2n+25}.
\]
The right-hand side tends to \(0\), proving the asserted volume-density limit.

## Verification
The primary manuscript was checked at the definition of \(\beta_n\), Theorem 1.2, Lemma 3.1, and the fixed-parent Dehn-filling construction. These give the exact braid word, the genus \(n+11\), braid index \(4\), hyperbolicity, asymmetry, the L-space property, and the common hyperbolic parent.

The only general inputs are Yamada's theorem that braid index equals the minimum number of Seifert circles and the standard strict volume-decrease theorem for hyperbolic Dehn filling. The crossing identity is symbolic; no finite census or numerical volume computation is used as an infinite proof.

At \(n=1\), the formula gives \(c(K_1)=27\), consistent with the source identification \(K_1\) as `t12533` and its displayed positive four-braid.

## Relationship to prior work
Baker and Teragaito introduce the family to realize asymmetry at braid index \(4\) and prove its genus, braid index, L-space property, hyperbolicity, and common Dehn-filling origin. The inspected manuscript does not state the exact crossing number, crossing-minimality of the displayed braid, or the volume-density limit.

The crossing conclusion requires combining the family-specific genus and braid-index computation with Yamada's general theorem. The volume-density conclusion then combines the exact crossing growth with the source's fixed hyperbolic parent and strict volume decrease under hyperbolic filling. Searches for the exact formula \(2n+25\), crossing-minimality, fixed-braid-index volume density, and the `t12533` family did not locate a covering statement.

## Limitations
The theorem gives a uniform upper bound on volume, not an exact volume formula and not monotonicity of \(\operatorname{Vol}(S^3\setminus K_n)\) in \(n\). The conclusion that volume density tends to zero uses only positivity and the uniform parent-volume bound.

The crossing formula applies to this specific Baker--Teragaito family. It does not classify crossing-minimal representatives of all braid-index-four L-space knots.

The originality check cannot exclude an unindexed note containing the same short synthesis. The claim does not assert independent validation.

## References
1. K. L. Baker and M. Teragaito, *On asymmetric hyperbolic L-space knots of braid index four*, arXiv:2510.07618v1, first posted 2025-10-08.
2. S. Yamada, *The minimal number of Seifert circles equals the braid index of a link*, Inventiones Mathematicae 89 (1987), 347--356, DOI `10.1007/BF01389082`.
3. B. Martelli, *An Introduction to Geometric Topology*, Theorem 15.4.1 on strict volume decrease under nontrivial hyperbolic Dehn filling.
