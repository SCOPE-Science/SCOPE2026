# Two point counts distinguish all smooth \(2\)-bic cubic surfaces over \(\mathbf F_2\)

## Finding
Let \(A=(a_{ij})\) range over all nonsingular \(4\times4\) matrices over \(\mathbf F_2\). Write
\[
S_A=\left\{[X_0:X_1:X_2:X_3]\in\mathbf P^3_{\mathbf F_2}: F_A(X)=\sum_{i,j=0}^{3}a_{ij}X_i^2X_j=0\right\},\qquad N_r(A)=\# S_A(\mathbf F_{2^r}).
\]
Then for any nonsingular matrices \(A,B\), the equality \(\big(N_1(A),N_2(A)\big)=\big(N_1(B),N_2(B)\big)\) holds **if and only if** the smooth cubic surfaces \(S_A,S_B\) are isomorphic over \(\mathbf F_2\). Equivalently, their first two finite-field point counts are a complete arithmetic isomorphism invariant within this smooth \(2\)-bic family. The first count alone is not sufficient. There are precisely ten projective classes, and the complete checked census is:

| Row masks for \(A\) | Orbit size | Stabilizer | \(N_1\) | \(N_2\) |
|---|---:|---:|---:|---:|
| `1,2,4,8` | 420 | 48 | 7 | 45 |
| `1,2,4,9` | 3360 | 6 | 7 | 21 |
| `1,2,4,11` | 5040 | 4 | 7 | 29 |
| `1,2,4,15` | 1120 | 18 | 3 | 21 |
| `1,2,5,10` | 1120 | 18 | 9 | 33 |
| `1,2,5,11` | 4032 | 5 | 5 | 25 |
| `1,2,7,11` | 420 | 48 | 3 | 29 |
| `1,2,8,7` | 1260 | 16 | 11 | 29 |
| `1,2,9,6` | 3360 | 6 | 9 | 17 |
| `2,1,8,4` | 28 | 720 | 15 | 45 |

## Assumptions and scope
The ground field is exactly \(\mathbf F_2\), the ambient space is \(\mathbf P^3\), and all coefficients \(a_{ij}\) are binary. “\(2\)-bic” refers to cubics in the linear subspace spanned by the monomials \(X_i^2X_j\), not arbitrary ternary or quaternary cubic forms. A row mask \(m_i\in\{0,\ldots,15\}\) encodes row \(i\) of \(A\) by the binary digits \(a_{i0},\ldots,a_{i3}\), with the least-significant digit first. Both smoothness and isomorphism are geometric/algebraic notions, not merely rational-point nonsingularity.

## Proof
**Smoothness.** Because the characteristic is two,
\[\frac{\partial F_A}{\partial X_j}=\sum_i a_{ij}X_i^2.\]
If \(A\) is invertible, all partial derivatives vanish simultaneously only at the zero vector over an algebraic closure, so \(S_A\) is geometrically smooth. Conversely, if \(A\) is singular then \(A^{\mathsf T} X^{[2]}=0\) has a nonzero solution over the algebraic closure; Euler's identity \(3F_A=\sum X_j\partial_jF_A\) puts that solution on the cubic, hence it is a geometric singular point.

**Equivalence.** Every isomorphism of smooth cubic surfaces identifies their anticanonical linear systems, hence extends to a projective linear change of their natural anticanonical embeddings in \(\mathbf P^3\). For \(G\in\operatorname{GL}_4(\mathbf F_2)\), the substitution \(X=GY\) sends \(A\) to \(G^{\mathsf T}AG\), since \(G^{[2]}=G\). The monomials \(X_i^2X_j\) are linearly independent, and \(\mathbf F_2^\times=\{1\}\), so projective equivalence is exactly ordinary matrix congruence under \(\operatorname{GL}_4(\mathbf F_2)\), whose order is \(20160\).

**Point-count computation.** Define the binary bilinear function \(b_A(u,v)=u^{\mathsf T}Av\). The first count is
\[N_1(A)=\sum_{0\ne u\in\mathbf F_2^4}[b_A(u,u)=0].\]
For the second, fix \(\mathbf F_4=\mathbf F_2[\omega]/(\omega^2+\omega+1)\), and write \(X=u+\omega v\) with \(u,v\in\mathbf F_2^4\). Since \(\omega^2=1+\omega\), substitution yields \(F_A(u+\omega v)=c_A(u,v)+\omega d_A(u,v)\), where
\[
\begin{aligned}
c_A(u,v)&=b_A(u+v,u)+b_A(v,v),\\
d_A(u,v)&=b_A(u+v,v)+b_A(v,u)+b_A(v,v).
\end{aligned}
\]
Every projective point over \(\mathbf F_4\) has precisely three nonzero affine representatives, so
\[N_2(A)=\frac13\sum_{(u,v)\in\mathbf F_2^4\times\mathbf F_2^4\setminus\{(0,0)\}}[c_A(u,v)=d_A(u,v)=0].\]
These formulas are exact; no sampling or asymptotic approximation is involved.

**Exhaustive class partition.** The first checker enumerates all \(2^{16}\) matrices, retains exactly \(20160\) invertible ones, and computes the transitive closure of the congruence action under all elementary transvections \(I+E_{ij}\), \(i\ne j\), which generate \(\operatorname{GL}_4(\mathbf F_2)\). It obtains ten disjoint orbits with sizes listed above, summing to \(20160\). The second checker independently enumerates all \(20160\) invertible change-of-basis matrices, calculates each displayed stabilizer directly, and recomputes \(N_2\) using an independent \(\mathbf F_4\) multiplication table. All ten signatures \((N_1,N_2)\) are distinct, while multiple classes have \(N_1=7\), \(N_1=3\) and \(N_1=9\). Both directions of the finding follow.

## Verification
Run `python3 checks/classify.py` and `python3 checks/verify.py` with Python 3.8 or later and only its standard library. The captured outputs are `checks/classify_output.txt` and `checks/verify_output.txt`, respectively. The two checkers agree on every representative, orbit size, stabilizer order and point-count pair. Source files contain the full bounded enumeration and no outside data or unlisted dependencies. The first uses congruence-orbit breadth-first search; the second independently checks direct stabilizers and \(\mathbf F_4\) field evaluation.

## Relationship to prior work
Kadyrsizova et al. identify the non-Frobenius-split cubic subspace and its single geometrically smooth projective class over an algebraic closure; the present question is about inequivalent \(\mathbf F_2\)-forms and their rational point counts. Cheng develops the geometry and normal forms of \(q\)-bic hypersurfaces, mainly over algebraically closed fields. Karaoğlu already gives a complete classification of **all** cubic surfaces over \(\mathbf F_2\), including their rational-point counts, equations and projective automorphism orders. Thus a ten-class subfamily census by itself must not be presented as newly discovered. Karaoğlu further studies extension-field counts and related incidence types, but the inspected Theorems 3.4 and 4.1–4.7 and tables do not state that the **pair of point counts over \(\mathbf F_2\) and \(\mathbf F_4\)** determines the isomorphism class within the smooth \(2\)-bic locus. The contribution claimed here is precisely that arithmetic recognition property and its explicit point-count signatures, not the general classification of cubics.

## Limitations
The result concerns only smooth \(2\)-bic cubic surfaces over \(\mathbf F_2\), not all smooth cubics or a universal zeta-function Torelli theorem. It does not classify all twists of cubic surfaces over arbitrary extensions. The calculation is independently executable but has not undergone independent external audit. Literature priority risk remains: published tables of extension-field point counts or unpublished database records may implicitly or explicitly encode the same ten signatures. The check against the accessible Karaoğlu text is statement-by-statement, not a claim that any particular uninspected supplemental data set excludes coverage.

## References
- Z. Kadyrsizova et al., Cubic Surfaces of Characteristic Two, arXiv:2007.12018v1 (first posted 2020-07-23), Sections 3–5; https://arxiv.org/abs/2007.12018
- F. Karaoğlu, Nonsingular cubic surfaces over F_{2^k}, Turkish Journal of Mathematics 45 (2021), 2492–2510, DOI 10.3906/mat-2102-10; especially Theorem 3.4, Tables 1–3, and Section 4.
- R. Cheng, q-bic threefolds and their surface of lines, arXiv:2402.09884v1 (2024-02-15), Sections 1.1, 1.3 and 1.5; https://arxiv.org/html/2402.09884v1
