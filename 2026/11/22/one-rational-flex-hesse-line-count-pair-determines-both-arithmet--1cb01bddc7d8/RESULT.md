# One rational flex–Hesse-line count pair determines both arithmetic configuration zeta functions

## Finding

**Theorem.** Let \(q\) be any prime power with \(\operatorname{char}\mathbb F_q\ne3\), and let \(C\subset\mathbb P^2_{\mathbb F_q}\) be a geometrically smooth plane cubic. Write \(\mathcal F_C\) for its reduced scheme of nine geometric flexes and \(\mathcal H_C\) for its reduced scheme of twelve geometric lines each containing three flexes. Put
\[
 f=\#\mathcal F_C(\mathbb F_q),\qquad h=\#\mathcal H_C(\mathbb F_q).
\]
Then the **known residue \(q\bmod3\)** and the **single pair \((f,h)\)** uniquely determine both full finite-étale zeta functions \(Z(\mathcal F_C,T)\) and \(Z(\mathcal H_C,T)\). In particular, they determine rational counts for every extension \(\mathbb F_{q^n}\), \(n\ge1\). Among the affine Frobenius actions compatible with each residue there are exactly seven different joint cycle spectra if \(q\equiv1\pmod3\), and exactly three if \(q\equiv2\pmod3\). The following complete table gives the reconstruction.

| \(q\bmod3\) | \((f,h)\) | Flex permutation cycles | Hesse-line permutation cycles |
|---|---|---|---|
| \(1\) | \((9,12)\) | \(1^9\) | \(1^{12}\) |
| \(1\) | \((3,3)\) | \(1^3 3^2\) | \(1^3 3^3\) |
| \(1\) | \((1,4)\) | \(1 2^4\) | \(1^4 2^4\) |
| \(1\) | \((1,1)\) | \(1\,2\,6\) | \(1\,2\,3\,6\) |
| \(1\) | \((1,0)\) | \(1\,4^2\) | \(2^2 4^2\) |
| \(1\) | \((0,3)\) | \(3^3\) | \(1^3 3^3\) |
| \(1\) | \((0,0)\) | \(3^3\) | \(3^4\) |
| \(2\) | \((3,4)\) | \(1^3 2^3\) | \(1^4 2^4\) |
| \(2\) | \((1,0)\) | \(1\,8\) | \(4\,8\) |
| \(2\) | \((0,1)\) | \(3\,6\) | \(1\,2\,3\,6\) |

Here \(d^m\) denotes \(m\) cycles of length \(d\). If the cycle lengths of either scheme are \(d_1,\ldots,d_s\), its zeta function is \(\prod_{i=1}^{s}(1-T^{d_i})^{-1}\). The table therefore also gives explicit rational point counts over every extension.

The second count is **genuinely needed in general**: over \(\mathbb F_7\), the three smooth plane cubics
\[
 Y^2Z=X^3+XZ^2+Z^3,\qquad Y^2Z=X^3+3Z^3,\qquad Y^2Z=X^3+5Z^3
\]
all have exactly one rational flex, but respectively have zero, one, and four rational Hesse lines. The field residue is necessary in the stated lookup: the same pair \((1,0)\) is compatible with determinants \(1\) and \(2\) but then has different complete spectra.

## Assumptions and scope

A flex is a geometric point where the tangent meets \(C\) with multiplicity three. A Hesse line is a geometric projective line containing three distinct geometric flexes, **not** a tangent at a flex. These are Galois-invariant finite reduced configuration schemes; \(\mathcal F_C\) has degree nine and \(\mathcal H_C\) degree twelve. The characteristic-three case is explicitly excluded because the geometric three-torsion need not be étale and the nine-flex configuration changes. Characteristic two is included: the contact-multiplicity definition, rather than a Hessian determinant, is used. The finite-field cubic is not required to possess a rational flex. The table classifies arithmetic spectra allowed by the full affine action; it does **not** assert that every row occurs for every particular field size.

## Proof

**1. Affine flex torsor.** Choose a geometric flex \(O\) of \(C\) as the identity in \(E=C_{\overline{\mathbb F}_q}\). The hyperplane section equals \(3O\), so the geometric flexes are exactly \(E[3]\), with nine points because the characteristic is not three. Three distinct points of \(E[3]\) lie on a projective line if and only if their sum is \(O\), by the degree-three divisor relation. Thus their triples are precisely the twelve affine lines \(v+H\) for \(v\in V=\mathbb F_3^2\) and each one-dimensional vector subspace \(H\le V\). Equivalently they are the sets \(\{(x,y):ax+by=c\}\) where \((a,b)\ne(0,0)\), with scalars modulo three. This identification works even if \(O\) is not rational.

**2. Arithmetic affine action.** Frobenius on the flex torsor takes the form \(\phi(v)=Av+b\), with \(A\in\operatorname{GL}_2(\mathbb F_3)\) and \(b\in V\). The Weil pairing on \(E[3]\) gives \(\det A\equiv q\pmod3\). Frobenius sends each geometric Hesse line \(v+H\) to \(Av+b+AH\). Consequently the two base-field counts are the cardinalities of the following explicitly defined finite solution sets:
\[
 f=\#\{v\in V:(A-I)v=-b\},\qquad
 h=\sum_{\substack{H\le V,\ \dim H=1\\ AH=H}}\#\{v+H\in V/H:(A-I)v+b\in H\}.
\]
The second condition is independent of the coset representative since \(AH=H\).

**3. Exhaustive, exact finite classification.** There are exactly \((3^2-1)(3^2-3)=48\) invertible matrices, each paired with nine translations: **432** possible affine maps. The supplied verifier loops over all \(3^4\) matrix entries, discards precisely the singular matrices, and loops over all nine translations. Independently it builds the twelve lines both as solutions to the four slope families of linear equations and as translated three-point subgroups, with equality checked exactly. For every affine map, it computes the permutation on nine points and on twelve lines, and separately verifies the fixed-line solution criterion above. From the full 432-element set, it obtains exactly the ten joint spectra in the table, seven with determinant one and three with determinant two. Within each determinant class all seven or three pairs \((f,h)\) are distinct. This proves the reconstruction assertion for every smooth plane cubic, since every such Frobenius action occurs within the enumerated group. The same verifier independently computes **eleven affine conjugacy classes**; two distinct determinant-two affine conjugacy classes happen to yield the same joint spectrum. Thus the theorem intentionally recovers the **two zeta functions**, not the affine conjugacy class in general.

**4. Base-field sharpness examples.** For a short Weierstrass cubic \(y^2=x^3+ax+b\) in characteristic seven, infinity is a rational flex. Its other flexes form \(E[3]\), and their nonzero \(x\)-coordinates satisfy the classical three-division polynomial \(3x^4+6ax^2+12bx-a^2\). The three models in the theorem have, respectively, \(\#E(\mathbb F_7)=5,13,7\); hence \(E(\mathbb F_7)[3]\) consists only of infinity in every case and \(f=1\). Their division polynomials have respectively zero, one, and four distinct roots in \(\mathbb F_7\). Each rational root corresponds to a Frobenius-stable order-three subgroup \(H\), hence to its Hesse line through infinity. Because Frobenius fixes no nonzero three-torsion vector, the induced map on the quotient \(V/H\) cannot have eigenvalue one, so no other coset of \(H\) is fixed. Therefore \(h\) equals the number of those roots and is respectively zero, one and four. The packaged verifier checks point counts, discriminants and roots by exact \(\mathbb F_7\) arithmetic.

## Verification

Run `python3 hesse_verify.py` in a directory containing the supplied standalone script. It uses only Python's standard library, checks both independent constructions of the twelve Hesse lines, exhaustive enumeration of all 432 affine maps, the fixed-line linear criterion for every map, and their 11 conjugacy classes. The machine-readable file `hesse_spectra.csv` contains the ten reconstruction rows, including frequencies among the 432 affine maps; the script prints the same table. The standalone verifier also checks the three explicit \(\mathbb F_7\) curves. All computations are exact modular integer operations, not probabilistic tests or finite approximations to an infinite claim.

## Relationship to prior work

The nine-flex/twelve-line Hesse geometry, its affine-plane incidence and the geometrically acting Hessian group are **classical**. Artebani–Dolgachev, *The Hesse pencil of plane cubic curves* (2006), Section 2, explicitly describes the twelve lines as cosets of four order-three subgroups. Popov, *The variety of flexes of plane cubics* (first public 2024-08-29), Section 3.3, Lemma 6, describes the geometric collinearity identification and the special-affine projective symmetry group; this is the primary motivating geometric source. Bruen–Hirschfeld–Wehlau, *Cubic Curves, Finite Geometry and Cryptography* (2011), Sections 3 and 6, classify the possible numbers of rational flexes (zero, one, three, nine) and discuss finite-field curve normal forms. These results are used, not claimed as new.

The additional statement is **arithmetic**: the determinant restriction from the Weil pairing, the full ten-spectrum joint Frobenius table (including determinant-two arithmetic actions), and the one-field two-count reconstruction of both *complete* configuration zeta functions. The finite-field survey's four-way count of flexes alone neither distinguishes the three explicit \(\mathbb F_7\) examples nor supplies their Hesse-line zeta functions. The classical geometric identification alone does not state the reconstruction cutoff. A previously unindexed equivalent affine-group character table could imply the finite computation and remains a historical-priority risk.

## Limitations

The theorem does not determine the underlying cubic, its point-count Weil polynomial, or all affine conjugacy classes. It does not cover characteristic three, and it does not establish realizability of every permitted spectrum over every finite field. Novelty is assessed against the named accessible literature, not against every unpublished or unindexed calculation. Independent mathematical validation has not been performed.

## References

1. V. L. Popov, *The variety of flexes of plane cubics*, arXiv:2408.16488 (first made public 2024-08-29), especially Section 3.3, Lemma 6. https://arxiv.org/abs/2408.16488
2. A. A. Bruen, J. W. P. Hirschfeld, D. L. Wehlau, *Cubic Curves, Finite Geometry and Cryptography*, arXiv:1107.4387 (2011), especially Sections 3 and 6. https://arxiv.org/abs/1107.4387
3. M. Artebani, I. Dolgachev, *The Hesse pencil of plane cubic curves*, arXiv:math/0611590 (2006), especially Section 2. https://arxiv.org/abs/math/0611590
