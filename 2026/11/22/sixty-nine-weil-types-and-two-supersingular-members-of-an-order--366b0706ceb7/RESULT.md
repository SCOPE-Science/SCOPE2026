# Sixty-nine Weil types and two supersingular members of an order-six genus-four family over \(\mathbb F_{11}\)

## Finding
Let \(\mathbb F_{11}\) be the field with eleven elements and consider the smooth projective completions of
\[
 C_{a,b}:\quad y^2=x^{10}+x^7+a x^4+b x,
 \qquad (a,b)\in\mathbb F_{11}^2.
\]
Among the \(101\) coefficient pairs defining smooth genus-four curves, there are exactly **\(69\) distinct genus-four Hasse–Weil numerators** and therefore \(69\) Jacobian isogeny types over \(\mathbb F_{11}\). Their multiplicities among the marked coefficient pairs are \(49\) types occurring once, \(13\) twice, \(5\) three times, one five times and one six times. The Jacobian \(11\)-rank distribution is
\[
\begin{array}{c|rrrr}
 11\text{-rank}&0&1&2&3\\\hline
 \text{marked curves}&2&5&15&79
\end{array}.
\]
In particular no such Jacobian is ordinary. The **only two supersingular Jacobians** in this normalized \(\mathbb F_{11}\)-parameter family occur at \((a,b)=(3,7)\) and \((8,3)\). They have the same numerator
\[
 L(T)=1+11T^2+1331T^6+14641T^8
      =(1+11T^2)^2(1-11T^2+121T^4),
\]
but neither curve is superspecial: in both cases the Cartier operator has rank two and the Jacobian has \(a\)-number two.

This is a classification of **coefficient-marked curves and their Jacobian isogeny types** in the stated fixed family, not an isomorphism classification of the underlying curves.

## Assumptions and scope
Throughout, the characteristic and finite base field are exactly \(11\) and \(\mathbb F_{11}\). Write
\[
 Q_{a,b}(u)=u^3+u^2+au+b,\qquad
 \Delta(a,b)=a^2-4a^3+18ab-27b^2-4b.
\]
The branch polynomial is \(xQ_{a,b}(x^3)\). It is squarefree precisely when \(b\Delta(a,b)\neq0\) in \(\mathbb F_{11}\), yielding the \(101\) smooth parameter pairs and genus four. There are no other parameter identifications in the definition of the marked count.

For each smooth pair, define \(N_n(a,b)=\#C_{a,b}(\mathbb F_{11^n})\), and define the numerator by
\[
 Z(C_{a,b},T)=\frac{L_{a,b}(T)}{(1-T)(1-11T)}.
\]
The phrase Jacobian \(11\)-rank means the dimension of the étale part of its \(11\)-torsion over an algebraic closure. “Supersingular” means all Newton slopes equal \(1/2\), not merely \(11\)-rank zero.

## Proof
**Smoothness and exhaustiveness.** Since \(11\) is prime to \(2\) and \(3\), the zero at \(x=0\) of \(xQ_{a,b}(x^3)\) is simple exactly when \(b\ne0\); its other nine zeros are simple exactly when the cubic \(Q_{a,b}\) has three distinct nonzero roots. The cubic discriminant is \(\Delta\). Exhausting \(a,b\in\{0,\ldots,10\}\) and retaining \(b\Delta\ne0\) gives exactly \(101\) pairs. All these models have squarefree degree-ten branch polynomial and therefore genus \(4\).

**Exact extension counts.** For \(n=1,2,3,4\), denote the quadratic character on \(\mathbb F_{11^n}\) by \(\chi_n\), extended by \(\chi_n(0)=0\). The leading coefficient of the degree-ten branch polynomial is the square \(1\); therefore both points at infinity are rational over every extension, and
\[
 N_n(a,b)=11^n+2+\sum_{x\in\mathbb F_{11^n}}
    \chi_n\bigl(x^{10}+x^7+a x^4+b x\bigr).
\]
`WEIL_TABLE.csv` contains the **complete** \(101\)-row enumeration of these four counts, the first four Weil coefficients and the resulting \(11\)-rank. The program `verify.py` exhaustively reconstructs every count by polynomial-residue finite-field arithmetic using *two distinct quotient-field models of each extension*. For each model and degree it also verifies that every nonzero element satisfies \(z^{11^n-1}=1\), which certifies that the chosen degree-\(n\) defining polynomial is irreducible. Every possible \(x\) and every smooth \((a,b)\) is checked; no sampling is involved.

**Reconstruction of all Weil numerators.** Let \(s_n=11^n+1-N_n\) for \(1\le n\le4\), and set \(e_0=1\). Newton's identities give
\[
 k e_k=\sum_{i=1}^{k}(-1)^{i-1}e_{k-i}s_i
 \quad (1\le k\le4),\qquad \ell_k=(-1)^k e_k.
\]
The genus-four functional equation then determines the other four coefficients:
\[
 L(T)=1+\ell_1T+\ell_2T^2+\ell_3T^3+\ell_4T^4
 +11\ell_3T^5+121\ell_2T^6+1331\ell_1T^7+14641T^8.
\]
Thus the four certified extension counts determine the complete zeta function, not only a truncated series. Exact grouping of the \(101\) resulting coefficient vectors yields \(69\) different polynomials, with the multiplicities stated in the finding. Over a finite field, equality of the Weil polynomial is equivalent to isogeny of the Jacobians.

**Ranks and the exceptional supersingular class.** The \(11\)-rank of the Jacobian is the degree of the reduction of \(L(T)\) modulo \(11\); the complete coefficient table gives the rank distribution \((2,5,15,79)\) for ranks \((0,1,2,3)\). Exactly the two pairs \((3,7)\), \((8,3)\) have reduction \(L(T)\equiv1\pmod{11}\). Their common numerator factors as displayed above. The two quadratic factors \(1+11T^2\) and the quartic factor \(1-11T^2+121T^4\) both have all reciprocal-root \(11\)-adic slopes equal to \(1/2\), by their Newton polygons. Hence the two Jacobians are supersingular. Any supersingular abelian variety has \(11\)-rank zero, so no other smooth marked member can be supersingular.

Finally, for these two models the Cartier–Manin matrix in the basis \(dx/y,x\,dx/y,x^2\,dx/y,x^3\,dx/y\) is \((c_{11i-j})_{1\le i,j\le4}\), where \(c_m\) is the coefficient of \(x^m\) in \((x^{10}+x^7+a x^4+b x)^5\). Direct modular expansion and row reduction, performed in `verify.py`, give rank \(2\) in both cases. Consequently the two genus-four Jacobians have \(a\)-number \(4-2=2\), so they are not superspecial.

## Verification
Run `python verify.py` beside `WEIL_TABLE.csv` using Python 3 and NumPy. It prints `C6_F11_WEIL_69_TYPES_101_CURVES_VERIFIED` upon success. The verifier checks field-model irreducibility, both independent extension-field presentations, all \(404\) reported extension counts in each presentation, all Weil polynomial coefficients and ranks, smoothness of every included pair, uniqueness of the exceptional pairs, the exact 69-type multiplicity distribution and the Cartier ranks of the two supersingular cases. It does not query online services.

## Relationship to prior work
Kudo–Nakagawa–Takagi (arXiv:2210.14822, first public 2022-10-26) establish this normalized genus-four order-six-automorphism family, its Cartier–Manin coefficient method and an algorithm for **superspecial** members; those elements are prior work. Their principal tabulation focuses on characteristics \(p\ge17\), not on the complete \(\mathbb F_{11}\) Weil spectrum. Kudo–Harashita (arXiv:1907.00894) study superspecial hyperelliptic genus-four curves in small characteristic; this calculation concerns mostly nonsuperspecial curves and their complete zeta functions. A public earlier characteristic-eleven calculation of this same family determines Cartier-rank strata and all \(101\) smooth marked parameters, but explicitly does **not** compute zeta functions or full Newton polygons. The new claim is the complete \(69\)-type Weil spectrum and consequent exceptional supersingular classification, not that pre-existing Cartier stratification.

## Limitations
This statement does not identify geometric or rational isomorphism classes among the \(101\) marked curves, does not extend the census to parameters in \(\mathbb F_{11^n}\) for \(n>1\), and does not determine full Newton polygons for the \(99\) other parameter pairs. The exact arithmetic establishes the counts for the stated finite set, not a general parameter-space classification over the algebraic closure. An unindexed older table could affect historical priority; no independent expert audit has been performed.

## References
1. M. Kudo, T. Nakagawa and T. Takagi, *Efficient search for superspecial hyperelliptic curves of genus four with automorphism group containing* \(\mathbb Z_6\), arXiv:2210.14822v1, first public 2022-10-26. https://arxiv.org/abs/2210.14822 ; full open text: https://link.springer.com/article/10.1007/s11786-023-00571-w
2. M. Kudo and S. Harashita, *Algorithmic study of superspecial hyperelliptic curves over finite fields*, arXiv:1907.00894v1, first public 2019-07-01. https://arxiv.org/abs/1907.00894
3. *The unique Cartier-rank-one member of a cyclic-six genus-four family in characteristic eleven*, publicly indexed 2026-11-08, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-the-unique-cartier-rank-one-member-of-a-cyclic-six-genus-four-fa--7ea8fcd1fef1/RESULT.md
