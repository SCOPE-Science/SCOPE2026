# A six-stratum Jordan census and principal right-ideal count for the cubic quantum complete intersection

## Finding
Let \(k\) contain a primitive cube root \(\zeta\), and let
\[
A=k\langle x,y\rangle/(x^3,y^3,xy-\zeta yx),\qquad J=(x,y).
\]
All radical elements \(f\in J\) satisfy \(f^3=0\). Exactly six Jordan partitions occur for left multiplication \(L_f:A\to A\): \((3,3,3)\), \((3,2,2,1,1)\), \((2,2,2,1,1,1)\), \((2,2,1,1,1,1,1)\), \((2,1,1,1,1,1,1,1)\), and \((1,1,1,1,1,1,1,1,1)\). Their ranks are respectively \(6,4,3,2,1,0\). The corresponding loci are smooth, geometrically irreducible, locally closed reduced varieties of dimensions \(8,6,5,3,1,0\). In particular, ranks five, seven, and eight never occur.

If \(k=\mathbb F_Q\), where \(Q\) is any prime power admitting a primitive cube root (equivalently \(Q\equiv1\pmod3\)), the numbers of radical elements in the six rank strata are respectively
\[
(Q^2-1)Q^6,\quad Q^5(Q-1),\quad (Q^2-1)Q^3,\quad Q(Q^2-1),\quad Q-1,\quad 1.
\]
Thus exactly \(Q^5\) radical elements square to zero, with \(Q^5-1\) nonzero square-zero elements. The numbers of **distinct proper principal right ideals** of dimensions \(6,4,3,2,1,0\) are respectively
\[
Q(Q+1),\quad Q^2,\quad Q(Q+1),\quad Q+1,\quad 1,\quad 1.
\]
Including the unit right ideal, the total number of principal right ideals is \(3(Q^2+Q+1)+1\).

## Assumptions and scope
The field \(k\) is arbitrary except that it contains an element \(\zeta\) of multiplicative order three; both characteristic two and odd characteristics other than three are allowed. The algebra \(A\) has the Poincaré–Birkhoff–Witt basis \(x^i y^j\), \(0\le i,j<3\), hence dimension nine. The two-sided maximal ideal \(J=(x,y)\) has dimension eight. The multiplication operator is **left** multiplication; its image \(fA\) is a **right** ideal. The geometric statements are about reduced locally closed loci after passage to an algebraic closure. No conclusions about nonreduced scheme structures are asserted.

## Proof
**All radical elements are cubically nilpotent.** Work first in the untruncated quantum plane \(B=k\langle x,y\rangle/(xy-\zeta yx)\). Let \(S=k[u,v]\), \(D=\operatorname{diag}(1,\zeta,\zeta^2)\), and let \(P\) cyclically permute the three standard basis vectors so that \(DP=\zeta PD\). There is a representation \(\rho:B\to M_3(S)\) taking \(x\mapsto uD\), \(y\mapsto vP\). The characteristic polynomial of \(\rho(g)\), for any polynomial \(g\in (x,y)\), is invariant under separately multiplying \(u\) and \(v\) by \(\zeta\), since these changes are induced by conjugations by \(P^{-1}\) and \(D\), respectively. Hence its three nonleading coefficients lie in \(k[u^3,v^3]\) and have zero constant term. Modulo \((u^3,v^3)\), the characteristic polynomial is \(t^3\). Cayley–Hamilton gives \(\rho(g)^3=0\) there. The induced map \(A\to M_3(k[u,v]/(u^3,v^3))\) is injective, since the images \(u^i v^jD^iP^j\) of the nine PBW basis monomials have distinct scalar monomial supports and each matrix coefficient vector is nonzero. Thus \(f^3=0\) in \(A\) for every \(f\in J\).

**The top rank stratum.** Write \(f=f_1+f_{\ge2}\) by total PBW degree. If \(f_1=\alpha x+\beta y\ne0\), the leading homogeneous blocks of \(L_f\) across successive degrees \(0,1,2,3\) have ranks \(1,2,2,1\): for example, on degree one the two images are independent because \(f_1x\) and \(f_1y\) have independent coefficient vectors unless \(\alpha=\beta=0\), and the degree-two-to-three assertion follows analogously. Different blocks land in distinct graded degrees, so \(\operatorname{rank}L_f\ge6\). Since \(L_f^3=0\) on a nine-dimensional space, its rank is at most six. The resulting Jordan type is necessarily \((3,3,3)\), and \(\operatorname{rank}L_f^2=3\). This is an open affine rank stratum of dimension eight and cardinality \((Q^2-1)Q^6\).

**The second radical layer.** Suppose \(f\in J^2\). Write the degree-two part \(f_2=ax^2+bxy+cy^2\). The higher part has two coefficients in degree three and one in degree four. Quantum multiplication gives
\[
f^2=\zeta^{-1}(b^2-\zeta^2ac)x^2y^2.
\]
If \(f_2\ne0\), the map from degree zero to degree two has rank one and the map from degree one to degree three, in PBW bases \(x,y\) and \(x^2y,xy^2\), is
\[
M=\begin{pmatrix}\zeta^{-1}b&a\\\zeta^{-2}c&b\end{pmatrix},\qquad
\det M=\zeta^{-1}(b^2-\zeta^2ac).
\]
The image of degree-two input contributes a further independent one-dimensional degree-four output (multiplication by \(f_2\) cannot annihilate all degree-two inputs unless \(f_2=0\)). Degree-three corrections to \(f\) change neither these ranks nor their independence, by graded triangular elimination. Thus \(\operatorname{rank}L_f=2+\operatorname{rank}M\): four if \(\Delta=b^2-\zeta^2ac\ne0\), three if \(\Delta=0\) and \(f_2\ne0\). In the former case \(\operatorname{rank}L_f^2=1\), and in the latter it is zero. In the latter case the characteristic-polynomial rank of \(M\) is one because the nonzero triple \((a,b,c)\) makes the matrix nonzero.

The hypersurface \(\Delta=0\) is the affine quadric cone over a nonsingular conic, which is geometrically irreducible; its only singular point is its vertex \((0,0,0)\), also in characteristic two. Its \(\mathbb F_Q\)-point count is \(Q^2\) (there are \(Q+1\) projective conic points, each with \(Q-1\) nonzero scalar representatives, plus zero). The nonzero cone times the three freely chosen higher coefficients is the smooth five-dimensional rank-three stratum, containing \((Q^2-1)Q^3\) points. Its complement in the degree-two coefficient space times the same affine three-space is the smooth six-dimensional rank-four stratum, with \((Q^3-Q^2)Q^3=Q^5(Q-1)\) points. The full reduced square-zero locus is \(\{\Delta=0\}\times\mathbb A^3\), irreducible of dimension five.

**The bottom layers.** If \(f\in J^3\setminus J^4\), the degree-three part is nonzero and the only possible nonzero multiplication images occur in degrees three and four, giving rank two and Jordan type \((2,2,1,1,1,1,1)\). This stratum is \(\mathbb A^3\setminus\mathbb A^1\), smooth irreducible and has \((Q^2-1)Q\) points. For \(f\in J^4\setminus0\), left multiplication has rank one, giving \(Q-1\) points; zero is the remaining singleton. The partitions follow uniquely from \(\operatorname{rank}L_f\), \(\operatorname{rank}L_f^2\), and \(L_f^3=0\). The six counts sum to \(Q^8\).

**Distinct principal right ideals.** The ring \(A\) is finite-dimensional local with residue field \(\mathbb F_Q\). For any nonzero \(fA\) of dimension \(r\), the quotient \(fA/fJ\) is one-dimensional by Nakayama and cyclicity. Therefore precisely \((Q-1)Q^{r-1}\) elements of \(fA\) generate the same right ideal. Divide the number of elements of each positive multiplication rank by this factor to obtain the stated dimension-by-dimension principal right-ideal counts. Add the zero ideal and the unique unit ideal to obtain the total.

## Verification
The reproducible standalone checker `check_quantum_cubic.py` directly multiplies PBW basis elements, constructs nine-by-nine left-multiplication matrices and computes their ranks and those of their squares using finite-field row reduction. It exhaustively tests the **entire radical over \(\mathbb F_4\)** (65,536 elements), including **all distinct proper principal right ideals** by canonical row-reduced spans. It also exhaustively tests \(J^2\) over \(\mathbb F_7\) (117,649 elements), and 125 additional nonzero-linear-part elements each over \(\mathbb F_7\) and \(\mathbb F_{13}\). Every tested count matches the formulas; the direct output is stored in `verification_output.txt`. These finite enumerations are checks, not proofs for arbitrary fields.

## Relationship to prior work
Benson, Erdmann and Holloway introduced rank varieties for quantum complete intersections, including regular modules restricted along nonzero **linear** combinations of generators; that setting motivates the present **all-radical-element** problem. Bergh, Erdmann and Jorgensen study constant Jordan type along such linear pencils. Bergh and Erdmann study cohomology of quantum complete intersections. These works supply the relevant algebra and representation context but the inspected statements do not provide this six-stratum all-radical census or the associated count of distinct principal right ideals. The six numerical multiplicity polynomials coincide with those for the commutative modular group algebra \(\mathbb F_q[C_3\times C_3]\) in characteristic three; this is a structural comparison, not an assertion that those earlier commutative results imply the present characteristic-not-three quantum theorem. General theorems not identified here may still imply or subsume the formulas.

## Limitations
The classification is for a **specific cubic two-generator** quantum complete intersection with a primitive third root, not all quantum complete intersections. It does not classify left ideals, two-sided ideals, all right ideals, indecomposable modules, or the nonreduced scheme structures of rank degeneracy loci. Only the reduced geometric strata and principal right ideals are described; no independent validation or claim of exhaustive historical priority is made.

## References
1. D. J. Benson, K. Erdmann, M. Holloway, *Rank varieties for a class of finite-dimensional local algebras*, J. Pure Appl. Algebra 211 (2007), 497–510, doi:10.1016/j.jpaa.2007.02.006. Early online 2007-03-25.
2. P. A. Bergh, K. Erdmann, *(Co)homology of quantum complete intersections*, arXiv:0709.3029 (2007).
3. P. A. Bergh, K. Erdmann, D. A. Jorgensen, *Modules of Constant Jordan Type over Quantum Complete Intersections*, arXiv:1910.06714 (2019), published in Documenta Math.
