# Quadratic closed-point dichotomy for optimal plane sextics over \(\mathbb F_7\)

## Finding
Let \(C\subset\mathbb P^2_{\mathbb F_7}\) be a smooth plane sextic with \(\#C(\mathbb F_7)=36\). Up to \(\mathbb F_7\)-projective equivalence there are exactly two such curves, represented by
\[
C_{\mathrm{s}}:X^6+Y^6+5Z^6=0,\qquad
C_{\mathrm{c}}:X^6+2Y^6+4Z^6=0.
\]
Their quadratic-extension point counts are exactly
\[
\#C_{\mathrm{s}}(\mathbb F_{49})=42,\qquad
\#C_{\mathrm{c}}(\mathbb F_{49})=36.
\]
Consequently, among all smooth \(36\)-point sextics over \(\mathbb F_7\), exactly one projective equivalence class has no closed points of degree two, while the other has exactly three such closed points. Both have genus \(10\). The subscripts distinguish a transposition-stabilized coefficient class from a cyclically stabilized coefficient class; no assertion about the entire geometric automorphism group is required.

## Assumptions and scope
Here \(\mathbb F_7\) is the field of seven elements; all equivalences are by \(\mathrm{PGL}_3(\mathbb F_7)\). A closed point has degree two when its residue field is \(\mathbb F_{49}\). We count ordinary geometric points over each field, not geometric intersections with multiplicity. The field \(\mathbb F_{49}=\mathbb F_7[\iota]/(\iota^2+1)\) is a quadratic extension because \(-1\) is nonsquare modulo seven. The two equations define nonsingular curves since their three partial derivatives are nonzero multiples of \(X^5,Y^5,Z^5\), and cannot vanish simultaneously in projective space. The genus is \((6-1)(6-2)/2=10\).

## Proof
**Exhaustion of the optimal family.** Homma's Theorem 1.3 (arXiv:2105.04784, first public May 11, 2021) and Ferreira--Speziali's Theorem 4.4 (arXiv:2211.14288) establish that all smooth plane sextics with \(36\) rational points over \(\mathbb F_7\) belong, up to \(\mathbb F_7\)-projective equivalence, to \(aX^6+bY^6+cZ^6=0\), with \(a,b,c\ne0\) and \(a+b+c=0\). Homma proves equivalence is exactly projective coefficient permutation, and gives two classes for \(q=7\). The representatives \((1,1,5)\) and \((1,2,4)\) are inequivalent: the former has two equal coefficients while the latter has three distinct coefficients, and multiplication by a common nonzero scalar and permutation preserve this distinction. Each has \(36\) rational points because precisely the triples with all three coordinates nonzero are on the curve.

**The sixth-power subgroup.** In \(\mathbb F_{49}^{\times}\), the image \(H\) of the sixth-power map is exactly the subgroup of eighth roots of unity. It has eight elements, every member has exactly six preimages, and \(H\cap\mathbb F_7^{\times}=\{1,-1\}\), because \(\mathbb F_{49}^{\times}\) has order \(48\) and \(\mathbb F_7^{\times}\) has order \(6\). For the affine chart \(Z=1\), set \(h=X^6\), \(k=Y^6\). Either value is zero or belongs to \(H\).

For \(C_{\mathrm{s}}\), a zero coordinate would require the remaining sixth power to be \(2\), not in \(H\). With both coordinates nonzero, the equation becomes \(h=2-k\), with \(h,k\in H\). The exact polynomial identity
\[
\gcd_{\mathbb F_7[T]}\bigl(T^8-1,(2-T)^8-1\bigr)=T-1
\]
shows that the unique possible \(k\) is \(1\), and then \(h=1\). Six choices for each sixth root produce exactly \(36\) affine points.

For \(C_{\mathrm{c}}\), if either coordinate vanishes the other sixth power must be \(3\) or \(5\), again not in \(H\). For two nonzero coordinates, \(h=3-2k\), and an equally exact identity
\[
\gcd_{\mathbb F_7[T]}\bigl(T^8-1,(3-2T)^8-1\bigr)=T-1
\]
forces \(h=k=1\). Thus this curve also has exactly \(36\) affine points. These two polynomial gcds may be checked by the included standalone Euclidean-algorithm program; they are finite algebraic identities, not extrapolations from point samples.

**Points at infinity.** If \(Z=0\), then \(Y\ne0\), and after setting \(Y=1\) the remaining equation is \(X^6=-b/a\). The first curve requires \(X^6=-1\), which has six solutions because \(-1\in H\). The second requires \(X^6=-2=5\), which has no solutions since \(5\notin H\). Therefore \(\#C_{\mathrm{s}}(\mathbb F_{49})=36+6=42\) and \(\#C_{\mathrm{c}}(\mathbb F_{49})=36\).

Finally, if \(B_2(C)\) denotes the number of degree-two closed points, then \(\#C(\mathbb F_{49})=\#C(\mathbb F_7)+2B_2(C)\). This gives \(B_2(C_{\mathrm{s}})=3\) and \(B_2(C_{\mathrm{c}})=0\), completing the claimed classification.

## Verification
Run `python3 verify_gcd.py` to recompute both gcd identities in \(\mathbb F_7[T]\) with an explicit Euclidean algorithm. Run `python3 verify_projective.py` for an independent exhaustive enumeration of all \(2451\) projective points of \(\mathbb F_{49}\) in disjoint affine charts; the field is represented exactly by pairs of residues modulo \(7\). Both programs require only the Python standard library. Recorded outputs are `VERIFY_GCD_OK`, `VERIFY_POINT_COUNT (1, 1, 5) affine= 36 infinity= 6 total= 42`, `VERIFY_POINT_COUNT (1, 2, 4) affine= 36 infinity= 0 total= 36`, and `VERIFY_PROJECTIVE_OK`.

## Relationship to prior work
Homma (2021) establishes the projective equivalence classification and proves that there are two classes at \(q=7\); the initial counts of \(36\) rational points and the coefficient-permutation equivalence are prior facts. Ferreira and Speziali (2022) establish that these are all smooth sextics attaining the Sziklai bound. The new arithmetic comparison is the exact \(\mathbb F_{49}\)-point/degree-two closed-point dichotomy of the complete pair, not the two-class classification. Standard Jacobi-sum formulas for diagonal curves could also serve as a general method of determining extension counts; they do not by themselves give the two explicit numbers without additional evaluation.

## Limitations
The result concerns the first field \(\mathbb F_7\) for which this extremal sextic family has two projective classes. It does not give full zeta functions, counts over higher extensions, or a comparable dichotomy for every \(q\). Exact numerical values for these particular twists could conceivably occur in older computational tables not located in the cited sources; priority requires an independent literature check.

## References
- M. Homma, *On maximal plane curves of degree 3 over F4, and Sziklai's example of degree q-1 over Fq*, arXiv:2105.04784 (first submitted 2021-05-11), especially Theorem 1.3 and Section 2. https://arxiv.org/abs/2105.04784
- W. de Paula Ferreira and P. Speziali, *Optimal plane curves of degree q-1 over a finite field*, arXiv:2211.14288 (first submitted 2022-11-25), especially Theorems 2.7 and 4.4. https://arxiv.org/abs/2211.14288
- A. Weil, *Numbers of solutions of equations in finite fields*, Bull. Amer. Math. Soc. 55 (1949), 497–508 (general background on diagonal-curve arithmetic; not an explicit count for the two curves).
