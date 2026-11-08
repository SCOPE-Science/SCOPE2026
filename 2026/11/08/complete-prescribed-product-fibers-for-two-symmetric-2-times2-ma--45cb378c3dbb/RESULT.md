# Complete prescribed-product fibers for two symmetric \(2\times2\) matrices over finite fields

## Finding
Let \(k=\mathbb F_q\) be an arbitrary finite field, of any prime-power order \(q\), and write \(\operatorname{Sym}_2(k)\) for the three-dimensional vector space of symmetric \(2\times2\) matrices. For each prescribed \(C\in M_2(k)\), define
\[
F_q(C)=\#\{(A,B)\in\operatorname{Sym}_2(k)^2:AB=C\}.
\]
The map is surjective, and its **entire labeled, ordered fiber distribution** is the following seven-stratum table. The right column also counts the target matrices of the indicated kind.

| Target type for \(C\) | \(F_q(C)\) | Number of such \(C\) |
|---|---:|---:|
| Zero | \(3q^3-q^2-q\) | \(1\) |
| Rank one, \(\operatorname{tr}C=0\) | \(2q(q-1)\) | \(q^2-1\) |
| Rank one, \(\operatorname{tr}C\ne0\) | \((q-1)(2q-1)\) | \(q(q^2-1)\) |
| Invertible scalar | \(q^2(q-1)\) | \(q-1\) |
| Invertible, non-scalar, one repeated eigenvalue in \(k\) | \(q(q-1)\) | \((q-1)(q^2-1)\) |
| Invertible with two distinct eigenvalues in \(k\) | \((q-1)^2\) | \(\frac{q(q+1)(q-1)(q-2)}2\) |
| Invertible with irreducible characteristic quadratic over \(k\) | \(q^2-1\) | \(\frac{q^2(q-1)^2}2\) |

The non-scalar repeated-eigenvalue row refers to a single size-two Jordan block, including characteristic two. Empty strata, such as the split-distinct invertible case at \(q=2\), contribute zero targets. A target's fiber depends only on the listed similarity-invariant type, and **all seven formulas hold without a characteristic restriction**.

## Assumptions and scope
All factors are symmetric under ordinary transpose, including in characteristic two; they need not be invertible. Counts refer to ordered pairs of actual matrices, not conjugacy classes. The target-stratum sizes are numbers of individual matrices in \(M_2(k)\), and coincidences between numerical fiber values at small \(q\) do not merge the mathematical strata.

A 1959 source on symmetric transpose intertwiners has only month-precision (July 1959) in its inspected original. The recorded exact date \(2007\text{-}09\text{-}16\) is the verified day-specific public timestamp of the subsequently inspected arXiv preprint, **not** a claim that the classical factorization originated in 2007. The classical existence of two-symmetric-factor decompositions is prior work; the result here is the target-by-target multiplicity law, including singular factors.

## Proof
**1. Similarity invariance.** If \(C=AB\) with \(A,B\) symmetric, then for \(P\in GL_2(k)\),
\[
PCP^{-1}=(PAP^{\mathsf T})(P^{-\mathsf T}BP^{-1}),
\]
and both new factors are symmetric. Thus \(F_q(C)\) depends only on the similarity class of \(C\).

**2. Invertible first factors.** For an invertible symmetric \(A\), the equation \(AB=C\) determines \(B=A^{-1}C\). The latter is symmetric if and only if
\[
CA=AC^{\mathsf T}.
\]
Writing \(C=\begin{psmallmatrix}u&v\\w&z\end{psmallmatrix}\) and \(A=\begin{psmallmatrix}a&b\\b&c\end{psmallmatrix}\), this condition is just
\[
wa+(z-u)b-vc=0. \tag{1}
\]
If \(C\) is non-scalar, (1) cuts out a two-dimensional space of symmetric intertwiners. Every non-scalar \(2\times2\) matrix is cyclic. An invertible symmetric solution \(A_0\) exists directly from the rational canonical form: for a split-distinct diagonal matrix choose \(I\); for a Jordan matrix \(\begin{psmallmatrix}\lambda&1\\0&\lambda\end{psmallmatrix}\) choose \(\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}\); and for an irreducible quadratic companion \(\begin{psmallmatrix}0&-\delta\\1&\tau\end{psmallmatrix}\) choose \(\begin{psmallmatrix}-\delta&0\\0&1\end{psmallmatrix}\), where \(\delta\ne0\). The same property persists under similarity by congruence.

The two linearly independent matrices \(A_0,CA_0\) are symmetric and span the solutions of (1); hence every solution is \((xI+yC)A_0\). It is invertible exactly when \(xI+yC\) is a unit in \(k[C]\). The unit counts in the three cyclic cases are respectively
\[
(q-1)^2,\qquad q(q-1),\qquad q^2-1,
\]
for split-distinct, repeated-root Jordan, and irreducible quadratic characteristic polynomials. This holds whether \(C\) is invertible or rank one. For a nonzero scalar \(C\), every symmetric invertible \(A\) works. There are \(q^2-1\) nonzero rank-one symmetric matrices (one projective line of images times \(q-1\) nonzero scalars), so there are \(q^3-(q^2-1)-1=q^2(q-1)\) invertible symmetric matrices.

**3. Nonzero rank-one targets.** If \(\operatorname{rank}C=1\), at least one factor must have rank one; the possibilities are (invertible, rank one), (rank one, invertible), and (rank one, rank one). In the first two cases the preceding symmetrizer count applies to \(C\) and \(C^{\mathsf T}\), respectively. When \(\operatorname{tr}C=0\), \(C\) is nonzero nilpotent and these cases contribute \(q(q-1)\) each; when \(\operatorname{tr}C\ne0\), \(C\) has two distinct eigenvalues \(0,\operatorname{tr}C\), and they contribute \((q-1)^2\) each.

For rank-one symmetric matrices, write \(A=\alpha uu^{\mathsf T}\) and \(B=\beta vv^{\mathsf T}\) for nonzero vectors \(u,v\) spanning their fixed image lines and nonzero scalars \(\alpha,\beta\). Then \(AB=\alpha\beta(u^{\mathsf T}v)uv^{\mathsf T}\). For a prescribed rank-one \(C\), the image and row lines fix \(u,v\), and \(u^{\mathsf T}v=0\) exactly when \(\operatorname{tr}C=0\). Thus the rank-one/rank-one case contributes zero for trace zero, and exactly \(q-1\) choices for nonzero trace. Summing gives the two rank-one formulas.

**4. Zero target.** Partition first factors by rank. If \(A=0\), any of the \(q^3\) symmetric second factors works. For each of the \(q^2(q-1)\) invertible symmetric first factors, only \(B=0\) works. For each of the \(q^2-1\) rank-one symmetric first factors, \(AB=0\) forces \(\operatorname{im}B\) into the one-dimensional kernel of \(A\); the symmetric choices are \(B=\beta vv^{\mathsf T}\) with \(\beta\in k\), giving exactly \(q\) choices. Consequently
\[
F_q(0)=q^3+q^2(q-1)+q(q^2-1)=3q^3-q^2-q.
\]

**5. Target multiplicities.** The rank-one nilpotent matrices form one similarity class of size \(q^2-1\). For each nonzero trace, the rank-one diagonalizable class has size \(q(q+1)\). Among invertible matrices, the nonzero scalars provide \(q-1\) targets; each Jordan class has size \(q^2-1\); each unordered pair of distinct nonzero eigenvalues gives a class of size \(q(q+1)\); and each monic irreducible quadratic gives a class of size \(q(q-1)\). There are \(q(q-1)/2\) monic irreducible quadratics. These are the target counts in the table. Their total is \(q^4\), and the sum of their products with the corresponding fiber values is \(q^6\). Both equalities also have an independent exact polynomial certificate in the verification artifacts. Since each fiber value is positive whenever its stratum is nonempty, the multiplication map is surjective. \(\square\)

## Verification
The standalone standard-library program `verify_symmetric_product.py` exhaustively enumerates both factors and **every target** over \(\mathbb F_q\) at \(q=2,3,4,5,7,8,9\). Nonprime fields use explicit irreducible polynomials, not integers modulo a composite number. It verifies each individual target and the total \(q^6\) ordered pairs. In particular, for \(q=3\) it gives a zero-target fiber of \(69\), and for \(q=4\) a zero-target fiber of \(172\). The actual output is embedded as `verification_output.txt`.

The separate standard-library `verify_mass_identities.py` checks the two symbolic polynomial identities at seven distinct integer arguments; because both differences are rational polynomials of degree at most six, this is an exact identity certificate, not an extrapolation about arbitrary fields. Its output is embedded as `mass_output.txt`. The unrestricted fiber theorem is proven above independently of these finite checks.

## Relationship to prior work
The classical symmetric symmetrization theorem establishes that any matrix over a field is a product of two symmetric matrices. Taussky–Zassenhaus (1959) proves existence of a nonsingular symmetric transpose intertwiner and describes the cyclic case. The present result **does not** claim either existence or the cyclic centralizer correspondence as new. The added mathematical object is the exact prescribed-target fiber distribution: especially the zero fiber, two rank-one trace strata, and the distribution of all targets by their multiplicities.

Horn–Sergeichuk (public preprint 2007) studies congruence with transposes, not finite-field multiplication fibers. Dopico–Uhlig (2015/2016) develops algorithms for computing symmetrizers, not the complete finite-field fiber histogram. Seroussi–Lempel (1980) concerns the different factorization \(A=BB^{\mathsf T}\) for a **symmetric** prescribed matrix. No identified work in the inspected sources gives the seven-stratum count. Similarity classes, polynomial centralizers, and the corresponding elementary unit counts are recognized as standard ingredients rather than independently new facts.

## Limitations
The theorem is for \(2\times2\) ordinary symmetric factors and **all** finite-field characteristics; it does not enumerate higher matrix dimensions, factorization orbits, or other matrix involutions. Historical priority beyond the inspected sources is not certified: the 1981 paper *Partitions of a symmetric matrix over a finite field* was accessible only in abstract form, with its displayed equation unavailable, so it is a named residual risk. No independent mathematical audit has been performed.

## References
1. O. Taussky and H. Zassenhaus, *On the similarity transformation between a matrix and its transpose*, Pacific Journal of Mathematics 9 (1959), 893–896, DOI: 10.2140/pjm.1959.9.893. Full four-page article inspected at https://msp.org/pjm/1959/9-3/pjm-v9-n3-p25-s.pdf.
2. R. A. Horn and V. V. Sergeichuk, *Congruences of a square matrix and its transpose*, preprint arXiv:0709.2489, publicly posted 2007-09-16; corresponding journal work Linear Algebra and its Applications 389 (2004), 347–353. https://arxiv.org/abs/0709.2489.
3. F. Dopico and F. Uhlig, *Computing matrix symmetrizers, part 2: New methods using eigendata and linear means; a comparison*, Linear Algebra and its Applications, DOI: 10.1016/j.laa.2015.06.031.
4. G. Seroussi and A. Lempel, *Factorization of Symmetric Matrices and Trace-Orthogonal Bases in Finite Fields*, SIAM Journal on Computing 9 (1980), 758–767, DOI: 10.1137/0209059.
5. *Partitions of a symmetric matrix over a finite field*, Linear and Multilinear Algebra 10 (1981), DOI: 10.1080/03081088108817423. Abstract-only comparison; full text not inspected.
