# Exact four-colour 2-homogeneous census of Möbius ladders

## Finding

For each integer \(m\ge3\), let \(M_{2m}\) be the Möbius ladder on \(2m\) vertices. A proper vertex colouring \(c\) is *2-homogeneous* when every open neighbourhood has exactly two colours. Let \(h_m\) count such colourings from the named palette \(\{0,1,2,3\}\) with labelled vertices; no quotient by automorphisms or palette permutations is taken.

Set
\[
A(z)=(1-z)(1+z^2)^3(1-2z-4z^2)(1-z+2z^2)(1+2z+4z^2)^3(1-z^2-2z^3)^3(1-z-3z^2-3z^3+4z^4+8z^5)^2
\]
and
\[
B(z)=(1-2z)(1+z)^2(1-z+z^2+z^3)^3(1+z-z^2+7z^3+2z^4-16z^6)^3.
\]
Then
\[
\boxed{\sum_{m\ge3}h_mz^m=z\left(\frac{B'(z)}{B(z)}-\frac{A'(z)}{A(z)}\right)}.
\]
The first eight values at \(m=3,\ldots,10\) are \(216,48,600,720,5544,8160,59400,98880\), and
\[
\boxed{h_m=(1+\sqrt5)^m+O(3^m)}.
\]
In fact \(h_m>0\) at every such width, and no proper 2-homogeneous colouring uses three or fewer colours. Thus every colouring counted by \(h_m\) uses all four. The claim of originality concerns the complete enumerator and growth rate, not a palette-minimum result.

## Assumptions and scope

The graph is finite, simple and cubic. Its columns \(v_i=(a_i,b_i)\), \(0\le i<m\), each have a vertical rung. Consecutive columns are joined in the same row and the last column is joined crosswise to the first. Equivalently, the graph is a cycle of length \(2m\) with antipodal chords. Properness requires unequal colours at every edge. At a vertex, the three neighbouring colours must have multiplicities \(2,1\), not \(3\) or \(1,1,1\).

## Proof

**1. Transfer and twisted closure.** Let \(Q\) be the 12 ordered pairs of distinct named colours, and use the state set
\[
\mathcal S=\{(u,v)\in Q^2:u_0\ne v_0,\ u_1\ne v_1\}.
\]
For each \(u\) there are seven choices of \(v\), so there are 84 states. The entry \(T_{(u,v),(v',w)}\) is one exactly when \(v'=v\) and \(|\{u_0,v_1,w_0\}|=|\{u_1,v_0,w_1\}|=2\); otherwise it is zero. Membership in the state set guarantees all vertical and within-row properness constraints. The two equalities impose the neighbourhood conditions at the middle rung. Let \(J\) swap both rows in both columns. A length-\(m\) walk from \((v_0,v_1)\) to \((Jv_0,Jv_1)\) is exactly a valid colouring when the seam is crosswise: the last two transitions check the neighbourhoods of column \(m-1\) and the row-swapped column 0. Conversely the labelled columns determine the entire walk, without a factor for cyclic shifts. Therefore \(h_m=\operatorname{tr}(T^m J)\).

**2. Determinant certificate.** The row swap commutes with \(T\) and has no fixed state. Choose the lexicographically first representative from each of its 42 pairs. The matrices in the two row-swap sectors have entries
\[
(T_\pm)_{r,s}=T_{r,s}\pm T_{r,Js}.
\]
Consequently \(h_m=\operatorname{tr}(T_+^m)-\operatorname{tr}(T_-^m)\). The exact finite algebra certificate gives \(\det(I-zT_+)=A(z)\) and \(\det(I-zT_-)=B(z)\). For replay, start with \(W_0=I\) for each block \(D\), and at \(k=1,\ldots,42\) set \(c_k=-\operatorname{tr}(DW_{k-1})/k\) and \(W_k=DW_{k-1}+c_kI\). Comparing \((1,c_1,\ldots,c_{42})\) with the corresponding product above, padded with zeros, verifies every coefficient by integer operations. For any finite square matrix \(D\),
\[
-z\frac{d}{dz}\log\det(I-zD)=\sum_{m\ge1}\operatorname{tr}(D^m)z^m.
\]
The traces in the two sectors agree for \(m=1,2\), as follows from their first two determinant coefficients. Their difference gives the claimed formal series at all widths \(m\ge3\).

**3. Palette exclusion and witnesses.** For three colours, write an initial column as \((a,b)\) and let \(c\) be the remaining colour. The proper adjacent column can only be \((b,a),(b,c)\) or \((c,a)\). If it is \((b,a)\), the third column is forced to be \((c,c)\) by the two middle-column neighbourhood tests, and no transition is possible. If it is \((b,c)\), the third column is forced to be \((c,a)\); each next proper state preserves the same cyclic orientation. The case \((c,a)\) gives the opposite orientation by row exchange. The row swap reverses these orientations, so a proper state cannot reach its row exchange. A smaller palette is also excluded, being a subset of a three-colour palette. For four colours put \(u=(0,1)\) and \(v=(2,3)\). The successive-column lists \((u,v,u,v)\), \((u,v,u,Ju,Jv)\), and \((u,v,Jv,u,Ju,Jv)\) pass the two local tests at every transition of their overlapping pairs. They give a two-step return to \((u,v)\) and three- and four-step walks to \((Ju,Jv)\), respectively. Prepending any number of two-step returns gives every odd or even width in scope.

**4. Asymptotic.** The reciprocal monic polynomial for \(1-2z-4z^2\) has roots \(1\pm\sqrt5\). The positive one occurs once in \(T_+\) and is the only eigenvalue of either sector with modulus exceeding three. For the remaining linear and quadratic factors the other moduli are less than three by their explicit roots. On \(|x|=3\), the sum of lower-term magnitudes of each reversed monic cubic is bounded by \(5\) or \(13\) against \(27\); for the reversed degree-five and degree-six factors the bounds are \(209<243\) and \(547<729\), respectively. Rouché's theorem puts all these roots in the open disk. Traces of powers are sums of eigenvalue powers with algebraic multiplicity, so the single leading eigenvalue has coefficient one and the remaining contributions are \(O(3^m)\).

## Verification

The accompanying standard-library `verify.py` reconstructs the states and computes every characteristic-polynomial coefficient of the two blocks. It also checks the initial Newton sums, enumerates labelled graph assignments for widths 3, 4 and 5, checks short twisted witnesses and verifies full reachability for the three-colour transfer. The replay marker is `VERIFY_OK`. The all-width count rests on the transfer equivalence and full determinant certificate, not the bounded graph enumeration.

## Relationship to prior work

Hao, Liu and Romaniello prove a four-colour existence upper bound for proper 2-homogeneous colourings of cubic **bipartite** graphs. The cycle of length \(2m\) forces alternating parts, and its antipodal chords cross those parts exactly when \(m\) is **odd**. Their existence bound thus applies to odd widths, not even widths, and does not count colourings. Madaras and Šurimová study homogeneous graph colourings. The chirality obstruction of [A chirality obstruction for dynamic three-colourings of cubic ladders](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-a-chirality-obstruction-for-dynamic-three-colourings-of-cubic-la--a86238493a14/RESULT.md) excludes three colours for the weaker, at-least-two-neighbour-colours condition on these ladders. This also implies the three-colour obstruction here, but existence of a four-colour two-dynamic colouring need not imply existence under the exact-two condition.

[Twisted transfer enumeration of proper conflict-free colorings of Möbius ladders](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-twisted-transfer-enumeration-of-proper-conflict-free-colorings-o--15a66a7edbf3/RESULT.md) gives a named-colour census on the same family using a related twisted transfer construction. In a cubic neighbourhood, the proper conflict-free condition also allows three distinct colours, so this is not the same census: for widths four and five it gives 336 and 3600 rather than 48 and 600. The asymptotic here concerns only the exact-two condition.

## Limitations

Only the four-label 2-homogeneous census on this Möbius ladder family is counted; no larger-palette, arbitrary cubic graph, or automorphism-orbit census is claimed. The exact factorization is supported by the finite integer coefficient certificate. The comparisons do not settle historical priority against unindexed enumerators.

## References

- Rong-Xia Hao, Jianbing Liu and Federico Romaniello, *On 2-Homogeneous Colourings of Cubic Bipartite Graphs*, [arXiv:2611.16649v1](https://arxiv.org/abs/2611.16649).
- Tomáš Madaras and Mária Šurimová, *Homogeneous colourings of graphs*, *Mathematica Bohemica* 148 (2023), 105–115. [DOI:10.21136/MB.2022.0007-21](https://doi.org/10.21136/MB.2022.0007-21).
