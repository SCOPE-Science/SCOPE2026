# Universal three-level commutator fibers of Heisenberg groups over square-zero local rings

## Finding

**Theorem.** Let \(R\) be a finite commutative unital local ring with maximal ideal \(\mathfrak m\), \(\mathfrak m^2=0\), residue field \(R/\mathfrak m\cong\mathbb F_q\), and \(d=\dim_{\mathbb F_q}\mathfrak m\ge2\). Put \(t=|R|=q^{d+1}\) and \(v=|\mathfrak m|=q^d\). For every integer \(h\ge1\), let \(H_h(R)\) be the finite Heisenberg group with elements \((a,b,c)\), where \(a,b\in R^h\) and \(c\in R\), and multiplication
\[
(a,b,c)(a',b',c')=(a+a',\,b+b',\,c+c'+a\cdot b').
\]
For any \(z\in R\), define the exact prescribed-commutator fiber
\[
N_h(z)=\#\{(g,g')\in H_h(R)^2:[g,g']=(0,0,z)\},
\]
using the convention \([g,g']=gg'g^{-1}g'^{-1}\). Write
\[
A=t^{4h-1},\qquad B=t^{2h-1}v^{2h},\qquad C=t^{2h-1}(v/q)^{2h}.
\]
Then
\[
\boxed{\quad
\frac{N_h(z)}{t^2}=\begin{cases}
A+(q-1)B+(t-q)C,&z=0,\\
A+(q-1)B-qC,&0\ne z\in\mathfrak m,\\
A-B,&z\in R^\times.
\end{cases}\quad}
\]
These three values are strictly decreasing and strictly positive. They occur at respectively \(1\), \(v-1\), and \(t-v\) targets. **Every** central element is a single commutator; no noncentral element is a commutator. In particular, the commutator map is surjective onto the entire derived subgroup \(\{(0,0,z):z\in R\}\), and the fiber multiset depends only on \((q,d,h)\), not on the isomorphism type or the characteristic of \(R\).

The ordinary commuting probability is exactly
\[
\boxed{\ \Pr(gg'=g'g)
=q^{-4h}+q^{-d-1}\bigl(1+(q-1)q^{-2h}-q^{1-4h}\bigr).\ }
\]
For fixed \(q\) and \(h\), as \(d\) increases, it approaches \(q^{-4h}\), with exponentially small correction. Conditioned on two uniformly selected elements commuting, their images in the quotient \(H_h(R/\mathfrak m)\) are both central with probability
\[
\boxed{\ \frac{q^{-4h}}{q^{-4h}+q^{-d-1}(1+(q-1)q^{-2h}-q^{1-4h})}\longrightarrow 1.\ }
\]
Thus the limiting commuting mass is supported on pairs whose **horizontal** coordinates lie entirely in the square-zero ideal. For \((q,d,h)=(2,2,1)\), the horizontal fiber sizes at zero, nonzero radical, and units are respectively \(832,576,384\); the corresponding full-group fibers are respectively \(53248,36864,24576\). As a structural comparison, the principal local ring \(\mathbb Z/8\mathbb Z\), of the same cardinality \(8\), has four determinant-fiber levels rather than three, with zero-target count \(736\) (versus \(832\) for the nonprincipal square-zero ring). This is a change in the shape of the entire word-map distribution, not only in one count.

## Assumptions and scope

All rings are associative, finite, commutative, unital, local, and nonzero. As \(\mathfrak m^2=0\), multiplication by \(R\) on \(\mathfrak m\) factors through \(R/\mathfrak m=\mathbb F_q\), making \(\mathfrak m\) an \(\mathbb F_q\)-vector space of dimension \(d\). Thus \(|R|=q^{d+1}\). The condition \(d\ge2\) is essential to the **new nonprincipal-ring scope**: such rings are not principal ideal rings and, since their socle has dimension at least two, are not Frobenius. Both equal and mixed characteristic are allowed; for instance, \(\mathbb F_q\oplus\mathbb F_q^d\) with square-zero second summand and \(\mathbb Z/4[\epsilon]/(2\epsilon,\epsilon^2)\) are included where the parameters apply. The unit set is \(R^\times=R\setminus\mathfrak m\).

A prescribed commutator *fiber* counts ordered pairs of group elements, with independent choices of the two central coordinates; those choices account for the factor \(t^2\). The ring elements \(z=0\), \(z\in\mathfrak m\setminus\{0\}\), and \(z\in R^\times\) are mutually exclusive and exhaust the possible targets. No assertion is made for rings with \(\mathfrak m^2\ne0\), for nonlocal rings, or for higher nilpotency-class groups.

## Proof

**Step 1: the commutator is a symplectic dot product.** Direct multiplication and inversion in the displayed group law give
\[
[(a,b,c),(a',b',c')]=(0,0,a\cdot b'-a'\cdot b).
\]
The two central coordinates \(c,c'\) are arbitrary. Let \(f_h(z)=N_h(z)/t^2\) denote the number of horizontal quadruples \((a,b,a',b')\in R^{4h}\) giving the indicated dot-product difference. The underlying horizontal map is a sum of \(h\) independent expressions \(a_i b'_i-a'_i b_i\).

**Step 2: Fourier transform without a Frobenius-ring assumption.** Write \(\widehat R\) for the group of complex additive characters of \((R,+)\). This finite group has cardinality \(t\), and character orthogonality applies even though the ring has no generating character. For \(\chi\in\widehat R\) let
\[
I_\chi=\{a\in R:\chi(ax)=1\text{ for every }x\in R\}.
\]
This is an ideal. Summing first over the right-hand multiplicand gives
\[
\sum_{a,x\in R}\chi(ax)=\sum_{a\in R}t\,\mathbf1_{a\in I_\chi}=t|I_\chi|.
\]
The negative product gives the same value by inversion or by negating an input. The independence of the \(2h\) product terms therefore proves the exact character identity
\[
\widehat f_h(\chi)=\sum_{z\in R}f_h(z)\chi(z)=(t|I_\chi|)^{2h}.
\]
Inverting the additive Fourier transform,
\[
f_h(z)=t^{-1}\sum_{\chi\in\widehat R}(t|I_\chi|)^{2h}\overline{\chi(z)}.
\tag{1}
\]
No division by the residue characteristic, nondegenerate ring trace, or chosen splitting of \(R\) is required.

**Step 3: exhaustive annihilator classification.** There are exactly three character types.

* For the unique trivial character, \(I_\chi=R\), of cardinality \(t\).
* There are exactly \(q-1\) nontrivial characters that annihilate \(\mathfrak m\), namely the nontrivial characters of \(R/\mathfrak m\). Each has \(I_\chi=\mathfrak m\), of cardinality \(v\): every ideal element acts into \(\mathfrak m\), whereas a unit acts surjectively on \(R\) and cannot annihilate a nontrivial character.
* There are exactly \(t-q\) characters whose restriction to \(\mathfrak m\) is nontrivial. Such a character also excludes every unit from \(I_\chi\). Fix a nontrivial additive character \(\psi\) of \(\mathbb F_q\); since every additive character of the \(\mathbb F_q\)-vector space \(\mathfrak m\) equals \(\psi\circ L\) for a unique \(\mathbb F_q\)-linear functional \(L:\mathfrak m\to\mathbb F_q\), the restriction is \(\psi\circ L\) with \(L\ne0\). For \(a\in\mathfrak m\), \(aR=\mathbb F_q a\) because \(\mathfrak m^2=0\). Therefore \(a\in I_\chi\) precisely when \(L(a)=0\), giving \(I_\chi=\ker L\) of cardinality \(q^{d-1}=v/q\).

These types exhaust all \(t\) additive characters. This is the critical step where the nonprincipal \(d\)-dimensional socle enters the exact count.

**Step 4: evaluate the character sums.** Let \(S_1(z)\) be the sum of \(\overline{\chi(z)}\) over the \(q-1\) nontrivial characters of \(R/\mathfrak m\). By additive orthogonality,
\[
S_1(z)=\begin{cases}q-1,&z\in\mathfrak m,\\-1,&z\notin\mathfrak m.\end{cases}
\]
The sum over characters nontrivial on \(\mathfrak m\) is the sum over *all* characters minus the sum over the \(q\) characters trivial on \(\mathfrak m\), hence
\[
S_2(z)=\begin{cases}t-q,&z=0,\\-q,&0\ne z\in\mathfrak m,\\0,&z\notin\mathfrak m.\end{cases}
\]
Substituting the three annihilator sizes and these two sums into (1) gives
\[
f_h(z)=t^{-1}\left(t^{4h}+S_1(z)(tv)^{2h}+S_2(z)(tv/q)^{2h}\right),
\]
which is exactly the three-branch formula with \(A,B,C\) in the finding.

**Step 5: distinctness, surjectivity, and normalization.** For nonzero radical targets and units,
\[
f_h(0)-f_h(z\in\mathfrak m\setminus\{0\})=tC>0,
\qquad
f_h(z\in\mathfrak m\setminus\{0\})-f_h(z\in R^\times)=q(B-C)>0.
\]
The smallest fiber is \(A-B>0\) since \(A/B=(t/v)^{2h}=q^{2h}>1\). Thus every central target occurs, all three levels are distinct, and no noncentral target occurs by Step 1. As a normalization check, the sum of the fibers with target multiplicities \(1,v-1,t-v\) is \(t^{4h}\), the total number of horizontal quadruples; multiplying by \(t^2\) recovers the \(t^{4h+2}\) ordered pairs of group elements.

**Step 6: commutativity saturation.** Dividing the zero fiber by \(t^{4h}\) and collecting terms gives
\[
\Pr(gg'=g'g)
=t^{-1}\{1+(q-1)q^{-2h}+(t-q)q^{-4h}\}
=q^{-4h}+q^{-d-1}\{1+(q-1)q^{-2h}-q^{1-4h}\}.
\]
Both horizontal vectors have all \(4h\) coordinates in \(\mathfrak m\) with probability \((v/t)^{4h}=q^{-4h}\). Since \(\mathfrak m^2=0\), they necessarily commute. Dividing this probability by the full commuting probability gives the conditional expression. At fixed \(q,h\) its denominator tends to \(q^{-4h}\), so the conditional mass tends to one with error \(O_{q,h}(q^{-d})\), completing the theorem.

## Verification

The standalone `check.py` independently implements arithmetic for the equal-characteristic square-zero extensions \(\mathbb F_q\oplus\mathbb F_q^d\) at \((q,d)=(2,1),(2,2),(2,3),(3,1),(3,2),(5,1)\) (here the implementation uses prime fields) and the mixed-characteristic example \(\mathbb Z/4[\epsilon]/(2\epsilon,\epsilon^2)\), which has \((q,d)=(2,2)\). It enumerates **every** one of the \(t^4\) horizontal quadruples for \(h=1\) and compares all \(t\) prescribed-target counts to the formula; the largest exhaustive case has \(531441\) quadruples. It then computes the exact sum-convolution of the independent \(h=1\) distribution to verify all targets for \(h=2,3\). As a separate elementary comparator the checker exhaustively enumerates determinants over the principal ring \(\mathbb Z/8\mathbb Z\), recovering zero-target count \(736\) and four distinct fiber sizes. The text file `check_output.txt` contains the actual successful output; it terminates with `PASS: all exhaustive tests and convolution comparisons`. Reproduce with `python3 check.py`. These small-ring checks corroborate the algebraic proof for every \(q,d,h\); they cannot establish the infinite family by enumeration alone.

## Relationship to prior work

Prasad, Singla, and Spallone (arXiv:1212.6157v1, 26 December 2012), *Similarity of matrices over local rings of length two*, Section 10, treat precisely nonprincipal square-zero local rings and establish the universality of **similarity classes of matrices** over coefficient rings with the same residue field and radical dimension. Their Theorem 10.3 and Corollary 10.4 address the orbit classification of individual matrices, not fixed-determinant counts of pairs or prescribed Heisenberg commutator word fibers. Their explicit nonprincipal-ring Section 10 example and its warning about difficult matrix-pair classification are closely relevant, but do not imply the three numerical fiber formulas.

Choosuwan, Jitman, and Udomkavanich (arXiv:1605.06826v1, 22 May 2016), *Determinants of Matrices over Commutative Finite Principal Ideal Rings*, establish exact prescribed determinant counts for arbitrary matrix size over finite **chain** rings and products of such rings. Their Sections 3 and 4 genuinely cover fixed determinant fibers for the \(2\times2\) case on principal rings; those cases are not claimed here. Their concluding Section 5 expressly identifies the analogous counting problem over **general finite local rings** as an interesting further problem. A local ring with \(\mathfrak m^2=0\) and \(d\ge2\) has a nonprincipal maximal ideal, hence lies outside both their chain-ring and principal-ideal-ring theorems. The present theorem solves the prescribed alternating bilinear (determinant when \(h=1\)) fiber problem for precisely that nonprincipal square-zero class, and additionally gives every higher symplectic rank and the limiting commutativity law.

Schein and Voll (arXiv:1401.0266v1, 1 January 2014) analyze **normal-subgroup zeta functions** of Heisenberg groups over characteristic-zero compact discrete valuation rings, using lattice and Coxeter enumeration. Their group object supplies an archival Heisenberg context, but their normal-subgroup counts neither enumerate prescribed commutators nor apply the nonprincipal square-zero hypothesis.

Further published exact-result comparisons include *Heisenberg commuting graphs over finite chain rings recover exactly residue size and length* (2026), which treats full commuting graphs and zero-determinant incidences on chain rings; *Chermak–Delgado submodule lattices of truncated-ring Heisenberg groups* (2026), which classifies submodule and centralizer lattices for principal truncated polynomial rings; and *Universal Fourier spectrum of the determinant-zero cone over finite chain rings* (2026), whose Fourier transform concerns the **zero-determinant indicator** of a principal ring, not the fibers of prescribed determinant values on non-Frobenius local rings. These stronger-looking titles were compared by hypotheses and conclusions. In particular, a chain-ring theorem cannot cover the nonprincipal class just by changing its coefficients.

## Limitations

The result is not a full solution to prescribed determinants over **arbitrary** finite local rings. It is confined to square-zero maximal ideals of embedding dimension at least two, and to symplectic Heisenberg commutators, not arbitrary matrix size or arbitrary multilinear word maps. The formulas do not enumerate conjugacy classes or subgroup zeta functions. No general consequence for local rings with higher nilpotency index is proved. Although no exact dominating historical statement was found in the checked primary full texts and indexed records, an implicit corollary in broader historical character-sum or determinantal-distribution literature remains an originality risk. The algebraic proof and the finite test program have not been independently audited.

## References

1. A. Prasad, P. Singla, and S. Spallone, *Similarity of matrices over local rings of length two*, first posted 2012-12-26, arXiv:1212.6157v1, https://arxiv.org/abs/1212.6157. Especially Section 10, Theorem 10.3 and Corollary 10.4.
2. M. M. Schein and C. Voll, *Normal zeta functions of the Heisenberg groups over number rings II—the non-split case*, first posted 2014-01-01, arXiv:1401.0266v1, https://arxiv.org/abs/1401.0266. Sections 1–3.
3. P. Choosuwan, S. Jitman, and P. Udomkavanich, *Determinants of Matrices over Commutative Finite Principal Ideal Rings*, first posted 2016-05-22, arXiv:1605.06826v1, https://arxiv.org/abs/1605.06826. Sections 2–5, notably Theorems 3.8, 3.11, 4.1 and the final open-direction remark.
4. *Heisenberg commuting graphs over finite chain rings recover exactly residue size and length*, mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-heisenberg-commuting-graphs-over-finite-chain-rings-recover-exac--09fc688bed1d.
5. *Chermak–Delgado submodule lattices of truncated-ring Heisenberg groups*, mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-chermak-delgado-submodule-lattices-of-truncated-ring-heisenberg--53be67859697.
6. *Universal Fourier spectrum of the determinant-zero cone over finite chain rings*, mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-universal-fourier-spectrum-of-the-determinant-zero-cone-over-fin--34c64b212a4e.
