# Arithmetic descent of two characteristic-five cubic exceptional models

## Finding

Over \(k=\mathbb F_5\), consider the two explicitly defined smooth cubic surfaces
\[
S_{\mathrm{sp}}:\ xy(y-x)=zw(w-z),\qquad
S_{\mathrm{ns}}:\ x(x^2-2y^2)=z(z^2-2w^2)
\]
in \(\mathbb P^3_k\), with homogeneous coordinates \([x:y:z:w]\). They are isomorphic over \(\mathbb F_{25}\) but are not isomorphic over \(k\). Their arithmetic geometry differs as follows:

| Invariant | Split-tangent model \(S_{\mathrm{sp}}\) | Nonsplit model \(S_{\mathrm{ns}}\) |
|---|---:|---:|
| Geometric lines | 27 | 27 |
| \(k\)-rational lines | 15 | 3 |
| Frobenius orbits of length two | 6 | 12 |
| Arithmetic Picard rank | 6 | 4 |
| Picard discriminant | \(-2\) | \(-8\) |
| Arithmetic Picard discriminant group | \(\mathbb Z/2\mathbb Z\) | \((\mathbb Z/2\mathbb Z)^3\) |
| Number of \(k\)-points | 51 | 31 |

For every \(n\ge1\), the complete point-count formulas are
\[
\#S_{\mathrm{sp}}(\mathbb F_{5^n})=1+5^{2n}+5^n(6+(-1)^n),
\]
\[
\#S_{\mathrm{ns}}(\mathbb F_{5^n})=1+5^{2n}+5^n(4+3(-1)^n).
\]
Equivalently, their complete zeta functions are
\[
Z(S_{\mathrm{sp}},T)=\frac1{(1-T)(1-25T)(1-5T)^6(1+5T)},
\]
\[
Z(S_{\mathrm{ns}},T)=\frac1{(1-T)(1-25T)(1-5T)^4(1+5T)^3}.
\]
The split surface is the projectivized tangent cubic \(rw(w-r)-r'w'(w'-r')\) occurring in the characteristic-five triple-point resolution of Burek–Chmiel–Cynk–Oczko. Their \(\mathbb F_{25}\) exceptional equation equals the base change of the nonsplit displayed model. The two equations should **not** be regarded as the same descent over \(\mathbb F_5\).

## Assumptions and scope

The ground field is exactly \(\mathbb F_5\), and geometric means over its algebraic closure. The arithmetic Picard lattice is \(\operatorname{Pic}(S)\) with its integral intersection pairing. For smooth cubic surfaces \(\operatorname{Pic}^0=0\), \(\operatorname{Br}(\mathbb F_5)=0\), and consequently the geometric Picard Frobenius invariants are the arithmetic Picard group. The discriminant group of a nondegenerate integral lattice \(L\) is \(L^\vee/L\). All assertions concern these explicit projective cubic models; we do not infer a second cubic exceptional divisor in the same resolution.

## Proof

**Smoothness and common geometric model.** The binary cubics \(f_{\mathrm{sp}}(x,y)=xy(y-x)\) and \(f_{\mathrm{ns}}(x,y)=x(x^2-2y^2)\) have three distinct projective roots in characteristic five, so their two partial derivatives vanish simultaneously only at the origin. Their differences in disjoint pairs of variables define smooth cubic surfaces. Both binary cubics split into three distinct linear factors over \(\mathbb F_{25}=\mathbb F_5[s]/(s^2-2)\). The triply transitive action of \(\operatorname{PGL}_2(\mathbb F_{25})\) on ordered triples of distinct projective points supplies \(M\in\operatorname{GL}_2(\mathbb F_{25})\) and \(c\in\mathbb F_{25}^{\times}\) with \(f_{\mathrm{ns}}(M(x,y))=c f_{\mathrm{sp}}(x,y)\). Applying the same \(M\) to both pairs of coordinates cancels \(c\), giving the asserted cubic-surface isomorphism over \(\mathbb F_{25}\).

**All 27 lines over \(\mathbb F_{25}\).** For either binary cubic \(f\), list its three projective root lines \(\ell_i=0\). The nine lines \(\ell_i(x,y)=\ell_j(z,w)=0\) lie on \(f(x,y)=f(z,w)\). In addition, each \(M\in\operatorname{GL}_2(\mathbb F_{25})\) satisfying \(f\circ M=f\) gives a graph line \((z,w)=M(x,y)\). Exact four-coefficient expansion, using the field model above, gives 18 distinct preserving matrices for each form. The nine root-pair lines and eighteen graph lines are pairwise distinct. The classical theorem that a smooth cubic surface over an algebraically closed field has exactly 27 lines makes this an exhaustive list. Direct fifth-power Frobenius permutation of the resulting coordinate spans fixes, respectively, \(9+6=15\) and \(1+2=3\) lines, with remaining lines in pairs. Both forms split fully over \(\mathbb F_{25}\).

**The integral arithmetic lattices.** Any two distinct lines meet with intersection number one precisely when their two 2-dimensional coordinate subspaces intersect nontrivially, tested by a \(4\times4\) field-matrix rank; otherwise their intersection is zero, and each line has self-intersection \(-1\). The resulting \(27\times27\) matrices have rank seven, each row has ten off-diagonal ones, and they admit seven-line submatrices with determinant \(1\). Because the full geometric Picard intersection lattice of a cubic surface is unimodular of rank seven and lines generate it, these seven classes give *integral*, not merely rational, bases.

For reproducibility order the nine root-pair lines lexicographically, then graph lines by lexicographically ordered quadruples \((a,b,c,d)\) of elements of \(\{0,\dots,24\}\) representing entries of \(M\). The seven-line bases (zero-indexed) are
\[
(0,4,8,9,12,13,1)\quad\text{and}\quad(0,4,8,11,18,26,2),
\]
respectively. Fifth-power Frobenius on their line classes gives integral matrices \(C_{\mathrm{sp}},C_{\mathrm{ns}}\) satisfying \(C^2=I\) and \(C^{\mathsf T}BC=B\), where \(B\) is the corresponding unimodular intersection matrix. Exact integer-kernel bases of \(C-I\) have identity submatrices in their free-coordinate rows, so are saturated and describe the full integral fixed lattices. Their Gram matrices are
\[
K_{\mathrm{sp}}=\begin{pmatrix}
-1&0&0&0&0&1\\
0&-1&0&0&0&1\\
0&0&-1&0&0&0\\
0&0&0&-1&0&0\\
0&0&0&0&-2&0\\
1&1&0&0&0&-1
\end{pmatrix},
\]
\[
K_{\mathrm{ns}}=\begin{pmatrix}
-1&0&0&1\\
0&-2&0&2\\
0&0&-6&-2\\
1&2&-2&-3
\end{pmatrix}.
\]
Their determinants are \(-2\) and \(-8\); their Smith normal forms have diagonal entries \((1,1,1,1,1,2)\) and \((1,2,2,2)\), respectively. Thus the invariant Picard ranks are six and four and the asserted discriminant groups follow.

**Point counts and zeta functions.** The geometric second étale cohomology of any smooth cubic surface is generated by divisors; its Frobenius eigenvalues are five times those of its geometric Picard action. Since \(C^2=I\), the eigenvalues of normalized Frobenius are \(\pm1\). The fixed lattice ranks above give normalized multiplicities \((6,1)\) and \((4,3)\). The Grothendieck trace formula, with only even cohomology, gives the point-count formulas for *every* positive \(n\), and the zeta products follow. Direct finite-field crosschecks are available: for \(f_{\mathrm{sp}}\) the five fibers of \(f:\mathbb F_5^2\to\mathbb F_5\) have sizes \((13,3,3,3,3)\), while those of \(f_{\mathrm{ns}}\) all have size five. The identity \(\#S(\mathbb F_5)=(\sum_b\#f^{-1}(b)^2-1)/4\) then yields 51 and 31. Both forms have \(801\) points over \(\mathbb F_{25}\), in agreement with the initiating paper's arithmetic count.

## Verification

The accompanying `verify_exceptional_cubics.py` is a standalone exact-arithmetic checker requiring Python 3 and SymPy. It constructs \(\mathbb F_{25}\), exhaustively finds preserving graph matrices, independently constructs all twenty-seven line spans for both models, verifies their incidence and Frobenius actions, finds unimodular Picard bases, computes saturated Frobenius-fixed lattice Gram and Smith forms, and checks direct \(\mathbb F_5\) point counts. Its assertions are exact, not floating-point. The mathematical reasoning above (especially 27-line completeness, generation of Picard and the cohomological trace formula) justifies claims beyond finite tests.

## Relationship to prior work

The initiating characteristic-five threefold paper proves the existence and smoothness of the exceptional cubic over a field containing \(\mathbb F_{25}\) and computes \(\#E(\mathbb F_{25})=801\) and \(\#E(\mathbb F_{625})=395001\). Its construction also exhibits the *split tangent cubic* in local charts. It does not determine the comparison of the two specified \(\mathbb F_5\) forms, their full Frobenius actions on all 27 lines, saturated arithmetic Picard lattices or base-field zeta functions.

The classical 27-line theorem, Segre's constraints on rational-line numbers, McKean's general classification and Rybakov–Trepalin's analysis of minimal cubic-surface Galois classes give background, not an explicit computation of this pair's arithmetic Picard lattices. The present computation uses their structural framework; neither the classical possible line counts nor the general Weyl group classification alone identifies the integral invariant lattices of these two specific models.

## Limitations

No claim is made that \(S_{\mathrm{ns}}\) is the actual \(\mathbb F_5\)-exceptional descent in the initiating resolution: only its \(\mathbb F_{25}\) isomorphism class is used there. The full automorphism groups of the forms, arithmetic Brauer groups and integral Chow motives are not determined. An exhaustive priority search of all older classification tables or unpublished computations was not possible. The findings have had self-review only, not independent audit.

## References

- D. Burek, T. Chmiel, S. Cynk, M. Oczko, *A projective Calabi–Yau threefold in characteristic 5 non-liftable to characteristic 0*, arXiv:2611.15943v1 (November 11, 2026), especially Sections 4.1 and 4.3. https://arxiv.org/html/2611.15943v1
- S. McKean, *Rational lines on smooth cubic surfaces*, arXiv:2101.08217 (2021), especially Theorems 1.1–1.2 and the line-incidence discussion. https://arxiv.org/abs/2101.08217
- S. Rybakov and A. Trepalin, *Minimal cubic surfaces over finite fields*, arXiv:1611.02475 (2016; revised 2017), for general finite-field Picard Galois classes. https://arxiv.org/abs/1611.02475
