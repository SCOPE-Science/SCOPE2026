# Three extension counts recover the Frobenius type from the 16 lines and 40 squares of a degree-four del Pezzo surface

## Finding
For every smooth degree-four del Pezzo surface \(X/\mathbb F_q\), in any characteristic, let \(L_X\) be the finite étale scheme of its sixteen geometric exceptional curves and let \(Q_X\) be the finite étale scheme of its forty geometric anticanonical divisors consisting of four distinct exceptional curves with square intersection graph.

The sixteen-line action alone has twelve possible cycle spectra across the eighteen conjugacy classes of \(W(D_5)\). The forty-square action alone has sixteen possible spectra. The ordered pair of actions has eighteen, one for each Weyl conjugacy class. More strongly, the six integers
\[
\bigl(\#L_X(\mathbb F_{q^n}),\#Q_X(\mathbb F_{q^n})\bigr)_{n=1,2,3}
\]
already distinguish all eighteen classes and determine the two finite-étale zeta functions.

The cutoff three is minimal on the full Weyl group. Two distinct Weyl conjugacy classes have line spectrum \(2^2 6^2\). The class of size **80** has square spectrum \(1^1 3^1 6^6\); the class of size **160** has square spectrum \(1^1 3^5 6^4\). Both give count pairs \((0,1)\), \((4,1)\) in degrees one and two, but they give \((0,4)\) and \((0,16)\), respectively, in degree three. Minimality is for the Weyl-group classification and does not require realizing both classes over each particular finite field.

## Assumptions and scope
The ground field is any finite field, with no restriction on its characteristic. A degree-four del Pezzo surface is a smooth projective geometrically integral surface with ample anticanonical class and \(K_X^2=4\). Over an algebraic closure it is a blowup of the projective plane at five points in general position, with sixteen geometric exceptional \((-1)\)-curves. An intersection square is an unordered set of four such curves whose pairwise intersection graph is a chordless four-cycle; their sum is an anticanonical divisor. We count those divisors, not orderings of their components or intersection points. The finite Galois sets of curves and divisors descend to the indicated finite étale schemes.

A Frobenius cycle spectrum \(\{r^{c_r}\}\) means \(c_r\) orbits of length \(r\). Its finite étale zeta function is \(\prod_r(1-T^r)^{-c_r}\), and its number of points over an extension of degree \(n\) is \(\sum_{r\mid n}r c_r\). The conclusions classify possible Frobenius actions; they do not assert existence of every conjugacy type over every specified \(\mathbb F_q\).

## Proof
Use a geometric blowup marking with divisor basis \(H_0,E_1,\ldots,E_5\), where \(H_0^2=1\), \(E_i^2=-1\), distinct basis elements are orthogonal, and \(-K_X=3H_0-\sum E_i\). The sixteen exceptional classes are
\[
 E_i,\qquad H_0-E_i-E_j\ (i<j),\qquad 2H_0-\sum E_i.
\]
Label the conic class by zero in the even-weight subgroup
\[
V=\{v\in\mathbb F_2^5:\textstyle\sum_i v_i=0\},
\]
label \(E_i\) by the weight-four vector \(u_i\) with its only zero in coordinate \(i\), and label \(H_0-E_i-E_j\) by \(u_i+u_j\). The intersection pairing gives adjacency exactly at Hamming distance four. This graph is triangle-free, and each vertex has five neighbors. Relative to the zero vertex, each nonzero nonneighbor is identified by the pair of its neighbors among the five neighbors of zero.

Translations by \(V\) and coordinate permutations preserve adjacency; they give \(16\cdot120=1920\) automorphisms. Conversely the image of zero and the permutation of its five neighbors determine the graph automorphism, by the pair description. The automorphism group is therefore exactly \(V\rtimes S_5\), the standard even signed-permutation model of \(W(D_5)\).

The forty squares are the four cosets of \(\langle u_i,u_j\rangle\) for each \(i<j\):
\[
\{v,v+u_i,v+u_j,v+u_i+u_j\}.
\]
Indeed, each gives a four-cycle, and the edge differences around any four-cycle sum to zero. The only nonempty relation among distinct \(u_i\)'s is the sum of all five, so the two directions in a four-cycle must each occur twice, on opposite edges. If \(D\) is the sum of its four exceptional curves, the intersection matrix gives \(D^2=D\cdot(-K_X)=(-K_X)^2=4\). The class \(D+K_X\) has square zero and is perpendicular to \(-K_X\), so by the Hodge index theorem it is numerically zero. In the free blowup basis with nondegenerate intersection matrix it is therefore zero in the Picard group. Thus these are anticanonical divisors, and the two Frobenius actions are induced from the same element of \(W(D_5)\).

The exact-integer program `verify.py` constructs the divisor-class graph, enumerates its square divisors and matches them to the binary model. It computes the spectra for all \(1920\) affine transformations and determines the conjugacy classes by conjugating with four independent even translations and four adjacent coordinate transpositions, which generate the whole group. It gives eighteen classes, twelve line spectra, sixteen square spectra, and eighteen joint spectra. There are respectively thirteen, seventeen, and eighteen signatures through degrees one, two, and three. The unique two-degree collision is the pair of rows displayed in the finding; see `frobenius_spectra.csv`.

For clarity, the class sizes in that collision can also be counted directly. Write an affine element as \(v\mapsto t+\pi v\). Its signed cycle data are the cycle lengths of \(\pi\) and the sum of the bits of \(t\) on each cycle, viewed as positive for even and negative for odd. These classify conjugacy: translations modify the bits on each cycle by \(s+\pi s\), allowing all changes of even sum on that cycle, and coordinate permutations match cycles of the same length and sign. A conjugating translation can be made even by adding the indicator of an odd-length cycle, which does not change \(s+\pi s\). Such a cycle always exists in five coordinates. In the row with square spectrum \(1^1 3^1 6^6\) the signed lengths are one positive 3-cycle and two negative fixed coordinates; the \(20\) choices of 3-cycle and \(4\) even masks on it give size \(80\). For \(1^1 3^5 6^4\) there is a negative 3-cycle with one negative and one positive fixed coordinate; the \(20\) choices of 3-cycle, \(4\) odd masks on it and \(2\) choices of the negative fixed coordinate give size \(160\). The identical two-degree signatures and distinct third-degree signatures give the sharp cutoff on the full group.

## Verification
Run `python3 verify.py` with the companion files. The program uses only the Python standard library and regenerates `frobenius_spectra.csv`, giving one row per conjugacy class, its representative, size, both spectra and the six extension counts. The two colliding rows in this table have class sizes 80 and 160 as above. The final success marker is `DEGREE_FOUR_DEL_PEZZO_16_LINES_40_SQUARES_18_CLASSES_SHARP_3_EXTENSIONS_VERIFIED`.

## Relationship to prior work
Bergvall–Gounelas describe the degree-four Weyl-group geometry and the transitive action on four-component anticanonical curves in their study of marked del Pezzo moduli. Meroni–Ranestad–Sinn, Propositions 3.3–3.4, count forty hyperplane sections and describe the four-line intersection squares. The geometric count and configuration are not claimed new. Banwait–Fité–Loughran provide related background on Frobenius traces of del Pezzo surfaces. The contribution here is the joint arithmetic classification for the two specific incidence schemes and the sharp inverse statement from the first three extension counts, rather than the cardinality of the geometric configuration or a classification by Picard traces.

## Limitations
This is a uniform possible-action theorem, not a field-by-field realization theorem for the eighteen Weyl classes. It determines the line and square zeta functions, not the full zeta function of \(X\). The finite-group computation is exact. A previously unindexed cycle-index or permutation-character calculation could affect historical priority.

## References
- O. Bergvall and F. Gounelas, *Cohomology of moduli spaces of Del Pezzo surfaces*, arXiv:1904.10249, §7.4, https://arxiv.org/abs/1904.10249.
- C. Meroni, K. Ranestad, and R. Sinn, *Convex hulls of surfaces in fourspace*, arXiv:2209.01151, Propositions 3.3–3.4, https://arxiv.org/abs/2209.01151.
- B. Banwait, F. Fité, and D. Loughran, *Del Pezzo surfaces over finite fields and their Frobenius traces*, arXiv:1606.00300, https://arxiv.org/abs/1606.00300.
