# A sharp \(3^5\) square-image saturation threshold in the four-clique evolution algebra

## Finding
Let \(q\) be a prime power. The four-clique evolution algebra \(E=E_{K_4}(\mathbb F_q)\) has a natural basis \(e_1,\ldots,e_4\) and multiplication
\[
e_i e_j=0\ (i\ne j),\qquad e_i^2=\sum_{j\ne i}e_j.
\]
Let \(\operatorname{Sq}(E)=\{x^2:x\in E\}\) and let \(E^2\) denote the **linear span** of all pairwise products (not the set of individual squares). Then
\[
\boxed{\#\operatorname{Sq}(E)=
\begin{cases}
q^4,&\operatorname{char}\mathbb F_q=2,\\[2pt]
((q+1)/2)^4,&\operatorname{char}\mathbb F_q\notin\{2,3\},\\[2pt]
q^3-\delta(q),&\operatorname{char}\mathbb F_q=3,
\end{cases}}
\]
where
\[
\boxed{\delta(3)=12,\quad\delta(9)=240,\quad
\delta(27)=1248,\quad\delta(81)=240,\quad
\delta(3^r)=0\ (r\ge5).}
\]
Consequently the set of individual squares **equals the linear square** precisely when the characteristic is two or the characteristic is three and \(q\ge243\). In characteristic three, \(E^2\) is the three-dimensional coordinate-sum-zero hyperplane, so this is **not** surjectivity onto the four-dimensional algebra.

For every \(q=3^r\), let \(\chi\) be the quadratic character, extended by \(\chi(0)=0\). For a target \(y=(y_1,\ldots,y_4)\) in the hyperplane, the exact *prescribed* square fiber is
\[
\boxed{\#\{x\in E:x^2=y\}=\sum_{t\in\mathbb F_q}\prod_{i=1}^4(1+\chi(t-y_i)).}
\]
Outside that hyperplane it is zero. This fiber reduction is the counting tool; the assessed new result is the complete image-size and sharp saturation classification above, not the already known zero-target fiber count.

## Assumptions and scope
Finite fields of every characteristic are included, with the **unweighted** undirected simple graph \(K_4\) and its specified natural basis. The map is a single algebra square \(x\mapsto x^2\) in a nonassociative commutative algebra, not repeated squaring or an associative group power. A square target is any vector in \(E\). The linear square \(E^2\) is the span of \(uv\), for \(u,v\in E\). The threshold is over powers of three, so \(q=243\) is the first saturating odd field in the resonant characteristic.

## Proof
**1. Graph-adjacency factorization.** Write \(x=\sum_i x_i e_i\), \(s_i=x_i^2\), and \(T=\sum_i s_i\). Then \((x^2)_i=T-s_i\). In column form, the quadratic map is \((J_4-I_4)(s_1,\ldots,s_4)^\mathsf T\), where \(J_4\) is the all-ones matrix and \(\det(J_4-I_4)=-3\). As the \(e_i^2\) span the image of the adjacency matrix, this matrix also determines \(E^2\).

**2. Nonresonant characteristics.** If the characteristic is different from three, the matrix is invertible and \(E^2=E\). In characteristic two, coordinatewise squaring is a bijection of every finite field, so the algebra-square map is a bijection and has image size \(q^4\). In odd characteristic different from three, each coordinate square has \((q+1)/2\) possible values, independently. Invertibility gives the displayed \(((q+1)/2)^4\) image size, strictly less than \(q^4\).

**3. Resonant characteristic and target reduction.** In characteristic three, \(J_4-I_4\) has kernel spanned by \((1,1,1,1)\) and image
\[
H=\{y\in\mathbb F_q^4:\sum_i y_i=0\},\qquad |H|=q^3.
\]
For any \(y\in H\), all solutions of \((J_4-I_4)s=y\) are \(s_i=t-y_i\), with \(t\in\mathbb F_q\). Indeed, \(\sum_i(t-y_i)=4t=t\) in characteristic three, so the chosen parameter is precisely \(T\). Consequently \(y\) is an algebra square if and only if there is a \(t\) such that every \(t-y_i\) is a field square, including zero. A nonzero field square has exactly two roots and zero has exactly one; this gives the displayed exact prescribed-fiber formula.

**4. Uniform saturation beyond the finite exceptional range.** Let \(d\le4\) be the number of *distinct* coordinates among \(y_1,\ldots,y_4\), and write their values as \(a_1,\ldots,a_d\). For \(t\notin\{a_1,\ldots,a_d\}\), the indicator that all \(t-a_i\) are nonzero squares is \(2^{-d}\prod_{i=1}^d(1+\chi(t-a_i))\). Expand this product by nonempty subsets. A one-factor complete character sum is zero. By the classical Weil bound for a squarefree product of \(k\ge2\) distinct linear factors, its complete character sum has absolute value at most \((k-1)\sqrt q\). Restricting any subset sum to the complement of the \(d\) excluded roots discards at most \(d-k\) terms of absolute value at most one. Therefore the number \(M\) of simultaneous *nonzero* square translates satisfies
\[
2^d M\ \ge\ q-d-\sqrt q\sum_{k=2}^d\binom dk(k-1)
-\sum_{k=1}^d\binom dk(d-k).
\]
For \(d\le4\), the worst coefficients are respectively \(17\) and \(28\), so
\[
2^d M\ge q-4-17\sqrt q-28.
\]
For any power of three \(q\ge729\), the right side is at least \(729-4-459-28=238>0\) and increases with \(q\). Hence every \(y\in H\) is an individual square over all \(\mathbb F_{3^r}\) with \(r\ge6\).

**5. Exact finite cutoff certificate.** The only remaining characteristic-three fields are \(3,9,27,81,243\). The standalone `check_k4_square_image.py` enumerates all \(q^3\) targets in \(H\), writing the fourth coordinate as the negative of the first three. It constructs \(\mathbb F_{3^r}\) from the explicit monic irreducible polynomial stated in its `MODULI` table, verifies irreducibility by division against every possible monic proper factor up to half the degree, builds the addition table and complete square set, and represents
\[
B(a)=\{t\in\mathbb F_q:t-a\text{ is a square}\}
\]
by a bitset. For each triple \((a,b,c)\), the test \(B(a)\cap B(b)\cap B(c)\cap B(-a-b-c)=\varnothing\) is exact. All \(q^3\) targets are traversed without sampling; the resulting deficit counts are, in increasing field order, \(12,240,1248,240,0\). A second direct enumeration of all quadruples of field-square values independently verifies the image sizes at \(q=3,9,27\). The finite exhaustive computation and the uniform Weil-bound argument jointly establish every case and the sharp threshold.

## Verification
Run `python3 check_k4_square_image.py` using Python 3 without external packages. Exact output for the five finite-field certificates and the independent direct-square-coordinate cross-checks is embedded in `verification_output.txt`. The exhaustive target ranges are \(27,729,19683,531441,14348907\) for \(q=3,9,27,81,243\), respectively. The polynomial irreducibility and finite-field multiplication are executed inside the checker; no separate proprietary field table is assumed. The code proves the finite bounded cases only. The large-field conclusion rests on the character-sum argument in the proof.

As an overlap consistency check, for the zero target in characteristic three, the fiber formula yields \(1+16(q-1)/2=8q-7\), agreeing with the known complete-multipartite square-zero count at resonance. That zero-fiber equality is not asserted as new.

## Relationship to prior work
Elduque and Labra, *Evolution algebras and graphs* (2013), establish the graph/evolution-algebra construction and connect graph structure to the algebra's linear square. Their sections on graph association, nilpotency, and automorphisms do not give this finite-field image-size cutoff. A published complete-multipartite *square-zero locus* result establishes, in particular, the already-covered \(K_4\) zero-fiber count \(8q-7\) in characteristic three, but no result for all prescribed nonzero targets or for saturation of the entire linear square. A published characteristic-two graphical squaring theorem concerns cycles and preperiods, not the odd-characteristic \(3^5\) image cutoff. A weighted directed-cycle theorem concerns a different graph and its iterated dynamics. Standard multiplicative-character estimates and finite-field arithmetic are tools, not claimed new results.

The common-square-translate statement can also be formulated as an intersection property of quadratic-residue translates, closely related to Paley graph and Paley tournament incidences. A broader prior Paley-incidence theorem could imply part of the large-field existence statement; the exact small-field deficit vector and this evolution-algebra formulation remain subject to historical-priority uncertainty.

## Limitations
No statement is made for other graph sizes or nonconstant edge weights. In characteristic three, the set of squares only saturates \(E^2\), never the whole four-dimensional algebra. The code is an exhaustive finite-field certificate, not a replacement for a symbolic proof of all field sizes; the Weil bound supplies that infinite step. The result does not classify every nonzero target's multiplicity beyond the explicit formula.

## References
1. A. Elduque and A. Labra, *Evolution algebras and graphs*, arXiv:1312.4685v1, publicly posted 2013-12-17, Sections 2–4. https://arxiv.org/abs/1312.4685
2. A. Kh. Khudoyberdiyev, B. A. Omirov, I. Qaralleh, *Few remarks on evolution algebras*, arXiv:1307.0993v1 (2013), for classical absolute nilpotents and background. https://arxiv.org/abs/1307.0993
3. *Finite-field square-zero geometry of complete multipartite evolution algebras*, published mathematical result, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-finite-field-square-zero-geometry-of-complete-multipartite-evolu--555bc289f00b/RESULT.md
4. *Exact finite-extension orbit census for graphical evolution-algebra squaring*, published mathematical result, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-finite-extension-orbit-census-for-graphical-evolution-alge--57cba8b84ace/RESULT.md
5. *Arithmetic cycle and basin spectra of weighted cyclic evolution algebras*, published mathematical result, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-arithmetic-cycle-and-basin-spectra-of-weighted-cyclic-evolution--469a88eb67c9/RESULT.md
6. Classical Weil bound for quadratic character sums of squarefree univariate polynomials over finite fields.
