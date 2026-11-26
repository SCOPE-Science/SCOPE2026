# Four exact Weil spectra for all eight-branch Howe covers over the seven-element field

## Finding

Over \(k=\mathbb F_7\), partition the full set \(\mathbb P^1(k)\) of eight rational base points into disjoint four-element subsets, and take both possible independent quadratic twists of the associated elliptic double covers. There are exactly \(35\cdot4=140\) such *coefficient-marked* genus-five Howe covers in the normalization specified below. Their complete Hasse–Weil numerators have exactly four possible values, with the following multiplicities:

| Rational Weil numerator \(L_C(T)\) | Marked covers | \(\#C(k)\) | \(\#C(\mathbb F_{49})\) | Jacobian \(7\)-rank |
|---|---:|---:|---:|---:|
| \((1+7T^2)^5\) | 84 | 8 | 120 | 0 |
| \((1+7T^2)^3(1-4T+7T^2)^2\) | 14 | 0 | 88 | 2 |
| \((1+7T^2)^3(1+4T+7T^2)^2\) | 14 | 16 | 88 | 2 |
| \((1+7T^2)^3(1-4T+7T^2)(1+4T+7T^2)\) | 28 | 8 | 88 | 2 |

The 84 members in the first row attain the genus-five Hasse–Weil bound \(50+10\cdot7=120\) after base extension to \(\mathbb F_{49}\). Their Jacobians are supersingular. All 140 Jacobians are isogenous over \(\mathbb F_7\) to products of five elliptic curves. These counts describe marked equations, not distinct abstract curve isomorphism classes; the general existence of maximal genus-five curves over \(\mathbb F_{49}\) is not claimed to be new.

## Assumptions and scope

Write \(k=\mathbb F_7\), and let \(T\) range over the 35 three-element subsets of \(k\). Put \(B=k\setminus T\) (four elements) and
\[
 f_T(x)=\prod_{a\in T}(x-a),\qquad g_B(x)=\prod_{b\in B}(x-b).
\]
Choose independently \(u,v\in\{1,3\}\), representatives for the two square classes of \(k^\times\). Define \(C_{T,u,v}\) as the smooth projective normalization of the integral fiber product
\[
 y^2=u f_T(x),\qquad z^2=v g_B(x).
\]
The branch sets are \(T\cup\{\infty\}\) and \(B\); they are disjoint and together exhaust \(\mathbb P^1(k)\). This convention uniquely represents every unordered partition by declaring the branch quartet containing infinity to be the first cover. The models are *marked by their base coordinate, this partition, and the two square classes*, so no assertion is made about pairwise nonisomorphism as unmarked curves.

All 140 fiber products are geometrically integral: the two classes of \(f_T\) and \(g_B\) are independent in \(\overline{k}(x)^\times/\overline{k}(x)^{\times2}\), because their sets of odd valuations are disjoint and nonempty. The resulting \((\mathbb Z/2\mathbb Z)^2\)-cover of \(\mathbb P^1\) has eight simple inertia-two branch places, hence Riemann–Hurwitz gives \(2g-2=4(-2)+8\cdot2=8\), so \(g=5\).

## Proof

**1. The three quotient curves and the fixed genus-three factor.** The three nontrivial characters of the biquadratic covering group correspond to the quotients
\[
 E_1:y^2=u f_T(x),\quad E_2:z^2=v g_B(x),\quad D:w^2=uv\,f_T(x)g_B(x)=uv(x^7-x).
\]
The first two curves have genus one; the last has genus three. As \(7\) is odd, étale \(\ell\)-adic character decomposition for \(\ell\ne2,7\) splits the first cohomology into the three nontrivial quotient-character components. Equivalently, the usual group-algebra correspondences give a prime-to-seven isogeny decomposition of Jacobians. Thus
\[
 L_{C_{T,u,v}}(Z)=L_{E_1}(Z)L_{E_2}(Z)L_D(Z).
\]

The genus-three curve \(D\) has eight \(k\)-rational points (seven finite branch points and one at infinity). Over \(\mathbb F_{49}\), the \(k\)-linear map \(x\mapsto x^7-x\) has a kernel of size seven and a one-dimensional trace-zero image of size seven. Every nonzero element of that image is a square in \(\mathbb F_{49}\): choose \(i^2=-1\) so the image is \(ki\), and both \(i\) and each element of \(k^\times\) are squares in \(\mathbb F_{49}\). The coefficients \(uv\in k^\times\) also become squares. Consequently
\[
 \#D(\mathbb F_{49})=1+7+42\cdot2=92.
\]
For the six Weil eigenvalues \(\alpha_j\) of \(D\), the Weil bound implies \(|\alpha_j^2|=7\), while the point count forces \(\sum_{j=1}^{6}\alpha_j^2=50-92=-42\). Equality in the triangle inequality forces each \(\alpha_j^2=-7\). Therefore, for every \(u,v\),
\[
 L_D(Z)=(1+7Z^2)^3.
\]
This also shows the genus-three factor is supersingular.

**2. The two classes of four-point branch sets.** The group \(\operatorname{PGL}_2(\mathbb F_7)\) acts sharply three-transitively on the eight rational projective-line points; its order is \(8\cdot7\cdot6=336\). On the five possible cross ratios \(\lambda\in\mathbb F_7\setminus\{0,1\}\), the anharmonic substitutions \(\lambda\mapsto1-\lambda\) and \(\lambda\mapsto1/\lambda\) give exactly the two orbits
\[
 H=\{2,4,6\},\qquad Q=\{3,5\}.
\]
For each fixed cross ratio there are 336 ordered distinct quadruples. Dividing by the 24 labellings of a four-point subset, the two projective orbits consist of \(336\cdot3/24=42\) harmonic quartets and \(336\cdot2/24=28\) equianharmonic quartets. Taking complements is projectively equivariant and cannot exchange orbits of unequal sizes. It follows that among the 35 unordered complementary pairs there are precisely 21 harmonic pairs and 14 equianharmonic pairs.

A genus-one double cover of \(\mathbb P^1_{\mathbb F_7}\) branched at four distinct rational points is a quadratic twist of a Legendre representative \(Y^2=X(X-1)(X-\lambda)\). The direct seven-term Legendre-character sums at \(\lambda=2\) and \(\lambda=3\) are, respectively, \(0\) and \(-4\), so the Frobenius traces of these representatives are \(0\) and \(4\). Projective changes of branch coordinate can introduce only a quadratic twist, which changes the trace sign, not its magnitude. Hence both elliptic traces vanish for a harmonic complementary pair, whereas each trace independently has magnitude four for an equianharmonic pair.

**3. Exhaustive Weil spectra.** Write \(t_1,t_2\) for the Frobenius traces of \(E_1,E_2\). By the above decomposition,
\[
 L_C(Z)=(1+7Z^2)^3(1-t_1Z+7Z^2)(1-t_2Z+7Z^2).
\]
For each of the 21 harmonic partitions, the four choices of \((u,v)\) all give \((t_1,t_2)=(0,0)\). For each of the 14 equianharmonic partitions, the four choices of \((u,v)\) give the four ordered pairs \((4,4),(4,-4),(-4,4),(-4,-4)\), one of each. Identifying the two mixed ordered pairs gives the four rows and frequencies \(84,14,14,28\) of the table.

By the Lefschetz point-count identity,
\[
 \#C(\mathbb F_7)=8-t_1-t_2,\qquad
 \#C(\mathbb F_{49})=120-t_1^2-t_2^2.
\]
This gives the displayed \(\mathbb F_7\)- and \(\mathbb F_{49}\)-point counts. The two harmonic elliptic factors have trace zero and are supersingular; the equianharmonic factors have traces \(\pm4\), prime to seven, and are ordinary. The genus-three factor is always supersingular. The prime-to-seven Jacobian isogeny and the corresponding Newton slopes therefore give exactly the listed \(7\)-ranks \(0\) and \(2\). Finally, a supersingular elliptic curve with Frobenius polynomial \(1+7Z^2\) exists over \(\mathbb F_7\); Honda–Tate or the same Frobenius polynomial identifies the genus-three quotient Jacobian up to isogeny with its third power. Therefore all five-dimensional Jacobians here are completely elliptic-split up to isogeny.

## Verification

Run the packaged dependency-free Python program as \(\texttt{python3 scripts/verify.py}\). It enumerates all 35 sets \(T\) and all four twist pairs, independently counts normalization points over \(\mathbb F_7\) and \(\mathbb F_{49}=\mathbb F_7[i]/(i^2+1)\) using local quadratic characters (including the fiber at infinity), checks both traces, validates the complement and cross-ratio classes, and verifies the point counts and frequencies for all 140 cases. It also tests the trace-zero image calculation for \(D\). The program returned `EIGHT_BRANCH_HOWE_F7_VERIFIED 35 partitions 140 marked covers`. Exhaustion is complete for the explicitly defined 140 marked models, not for all genus-five curves or all possible quadratic covers over \(\mathbb F_7\).

## Relationship to prior work

Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, II*, arXiv:2401.00760v1 (posted January 1, 2024), studies non-hyperelliptic genus-five Howe covers with two disjoint elliptic branch quartets and constructs their plane sextic models, treating geometric singularities rather than this complete arithmetic spectrum over the fully rational eight-point base. The factorization through the three involution quotients is standard and is not claimed as new.

Howe, *Curves of medium genus with many points*, arXiv:1609.01838, treats finite-field genus-five curve construction and point-count techniques; its genus-five construction involving two genus-two quotients and one elliptic quotient does not imply the present all-eight-point partition spectrum. Özbudak, Gülmez Temür and Yayla, *An exhaustive computer search for finding new curves with many points among fibre products of two Kummer covers over \(\mathbb F_5\) and \(\mathbb F_7\)* (2013), conducts a broader genus/degree search to extract **large \(\mathbb F_7\)-point** records. Its published tables list selected records, not the 140 marked models' complete zeta polynomials or the \(\mathbb F_{49}\) maximum-frequency split; here \(\#C(\mathbb F_7)\le16\). The existing manYPoints genus-five table for \(q=49\) already establishes that 120 is achievable; neither its extremal bound nor the existence of maximal curves is claimed as original.

Published nearby mathematical records treating particular characteristic-seven Howe pencils, singular genus-five plane models, and Humbert–Edge curves use different branch sets, quotients, or base fields and do not imply the four-polynomial classification with its marked frequencies. This is a claim-specific best-knowledge originality assessment, not an assertion that no equivalent unindexed classification exists.

## Limitations

The result concerns precisely the 140 coefficient-marked covers, not isomorphism classes, polarizations, independent algebraic-geometric classifications of all genus-five curves, or the \(a\)-number. The proof of the infinite extension-field point counts rests on the Weil numerator factorization, not finite empirical point counts. A prior unpublished or unindexed enumeration of the same 35 complementary eight-point partitions could imply the new table; no historical uniqueness is certified.

## References

1. M. Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, II*, arXiv:2401.00760v1, publicly posted 2024-01-01. https://arxiv.org/abs/2401.00760
2. E. W. Howe, *Curves of medium genus with many points*, arXiv:1609.01838, 2016. https://arxiv.org/abs/1609.01838
3. F. Özbudak, B. Gülmez Temür and O. Yayla, *An exhaustive computer search for finding new curves with many points among fibre products of two Kummer covers over F5 and F7*, Turkish Journal of Mathematics 37 (2013), 908–913. https://doi.org/10.3906/mat-1206-26
4. manYPoints database, genus five over 49 elements. https://manypoints.org/Details.aspx?g=5&q=49
