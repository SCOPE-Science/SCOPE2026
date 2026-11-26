# Prescribed-output fibers of the two-by-two matrix anticommutator over every finite field

## Finding
Let \(q\) be an arbitrary prime power, let \(F=\mathbb F_q\), and, for each \(C\in M_2(F)\), set
\[
N_q(C)=\#\{(X,Y)\in M_2(F)^2:XY+YX=C\}.
\]
The following formulas give **every prescribed-output fiber**, including its characteristic-dependent behavior. When \(q\) is even,
\[
N_q(C)=\begin{cases}
0,&\operatorname{tr}(C)\ne0,\\
q^6+q^5-q^3,&C=0,\\
q^5-q^3,&C\ne0,\ \operatorname{tr}(C)=0.
\end{cases}
\tag{1}
\]
For odd \(q\), set \(B_q=q(q-1)(q^2-q-1)\). For a nonscalar \(C\), let \(k(C)\) denote the number of \(F\)-rational projective lines in \(\ker C\) and let \(e(C)\) denote the number of \(F\)-rational eigenlines of \(C\) with **nonzero** eigenvalue, counting lines rather than eigenvalues. Then
\[
N_q(C)=\begin{cases}
B_q+q^2(q^3-1)+q^2(q^2-1)+q^4,&C=0,\\
B_q+q^2(q^3-1),&C=cI,\ c\in F^\times,\\
B_q+q^2(q-1)+q(q-1)\bigl(q+1+(q-1)k(C)-e(C)\bigr),&C\text{ nonscalar}.
\end{cases}
\tag{2}
\]
This also gives the complete fiber-size distribution on all similarity classes of targets: for a nonscalar target the allowed ordered pairs \((k,e)\) are \((0,0)\), \((0,1)\), \((0,2)\), \((1,0)\), and \((1,1)\), whenever the corresponding similarity type exists over \(F\). In particular, in odd characteristic the fibers separate nonzero nilpotent, rank-one semisimple, nonzero repeated-root Jordan, split semisimple and irreducible targets; in even characteristic every nonzero trace-zero target has the same fiber size.

## Assumptions and scope
All matrices are **labeled** matrices over the stated finite field; no quotient by simultaneous conjugation is taken. The pairs \((X,Y)\) are ordered, both factors range over the complete matrix algebra, and the target \(C\) is fixed. The zero matrix counts as scalar; \(k(C)\) and \(e(C)\) are used only for nonscalar targets. An eigenline with eigenvalue zero is counted in \(k(C)\), not in \(e(C)\). There are exactly \(q+1\) rational lines in \(F^2\). The two formulas are stated for all prime powers, not only prime fields.

## Proof
For fixed \(X\), the map \(L_X:M_2(F)\to M_2(F)\), \(Y\mapsto XY+YX\), is linear. A target in its image has exactly \(q^{4-\operatorname{rank}L_X}\) preimages. We first assume \(\operatorname{char}F\ne2\).

**Invertible nonzero-trace matrices.** In a splitting field, if \(X\) has eigenvalues \(\alpha,\beta\), the determinant of \(L_X\) is \(4\alpha\beta(\alpha+\beta)^2=4\det(X)(\operatorname{tr}X)^2\). Because this is a polynomial identity, it holds without a splitting hypothesis. It follows that \(L_X\) is bijective precisely when \(\det X\ne0\) and \(\operatorname{tr}X\ne0\). Now \(|\operatorname{GL}_2(F)|=q(q-1)^2(q+1)\), whereas the trace-zero invertibles number \(q^2(q-1)\): trace-zero matrices are \(\begin{psmallmatrix}a&b\\c&-a\end{psmallmatrix}\), and precisely \(q^2\) of the \(q^3\) have determinant zero (for each of the \(q+1\) lines \(L\subset F^2\), exactly \(q-1\) nonzero nilpotent matrices have image and kernel equal to \(L\), and zero is the remaining singular matrix). Thus exactly \(B_q=q(q-1)(q^2-q-1)\) such \(X\) contribute one solution for every target.

**Nonzero trace-zero matrices.** The polarization of Cayley–Hamilton gives, in every characteristic,
\[
XY+YX=(\operatorname{tr}X)Y+(\operatorname{tr}Y)X+\bigl(\operatorname{tr}(XY)-\operatorname{tr}X\operatorname{tr}Y\bigr)I.
\tag{3}
\]
In odd characteristic a nonzero trace-zero \(X\) cannot be scalar. Equation (3) shows \(\operatorname{im}L_X=\operatorname{span}_F\{I,X\}\), a two-dimensional subspace: the two coefficient functionals are independent because the trace pairing is nondegenerate and \(I,X\) are independent. There are \(q^3-1\) such \(X\); all permit a scalar target, with \(q^2\) lifts each. For a nonscalar \(C\), writing \(C=C_0+\tfrac12\operatorname{tr}(C)I\), precisely the \(q-1\) nonzero matrices on the line \(F C_0\) permit \(C\), again with \(q^2\) lifts each.

**Rank-one nonzero-trace matrices.** Such an \(X\) is \(aP\), with \(a\in F^\times\), and \(P\) the projection onto a line \(U\) along a distinct line \(L\). In the decomposition \(F^2=U\oplus L\), the equation for \(Y\) has a solution if and only if the \(L\to L\) block of \(C\) vanishes; if so, \(\operatorname{rank}L_X=3\), giving exactly \(q\) choices for \(Y\). For a fixed line \(L\), if \(C(L)=0\), all \(q\) choices of complementary \(U\) work; if \(C(L)\not\subseteq L\), precisely \(U=C(L)\) works; and if \(0\ne C(L)\subseteq L\), no \(U\) works. Consequently the number of admissible ordered complements is
\[
qk(C)+(q+1-k(C)-e(C))=q+1+(q-1)k(C)-e(C).
\]
For a scalar \(C\ne0\), none work; for \(C=0\), all \(q(q+1)\) work. Multiplication by the \(q-1\) possible values of \(a\) and by \(q\) preimages per admissible projection produces the last term of (2), or \(q^2(q^2-1)\) at zero. Finally \(X=0\) gives \(q^4\) choices for \(Y\) only at \(C=0\). The three disjoint types of \(X\) exhaust the algebra and yield (2).

**Characteristic two.** Then \(XY+YX=XY-YX\), so \(\operatorname{tr}(XY+YX)=0\). Each scalar \(X\) gives the zero map; there are \(q\) such \(X\) and \(q^4\) choices of \(Y\), contributing \(q^5\) at zero only. For every nonscalar \(X\), a cyclic vector exists, and a commuting operator is determined by its action on that vector; hence the centralizer is \(\operatorname{span}\{I,X\}\), of dimension two; by nondegeneracy of the trace pairing the image of the commutator map is the trace-orthogonal complement of this centralizer, hence has dimension two and each admissible target has \(q^2\) lifts. For \(C=0\), all \(q^4-q\) nonscalar \(X\) qualify. For nonzero trace-zero \(C\), the equation \(\operatorname{tr}(CX)=0\) imposes a nontrivial linear constraint and admits exactly \(q^3\) matrices \(X\), among which the \(q\) scalars are excluded. This gives \(q^6+q^5-q^3\) and \(q^5-q^3\), respectively, proving (1).

## Verification
The accompanying standalone file `verify.py` independently enumerates every ordered pair of matrices and every target over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\). In particular, the extension field of order four is realized as \(\mathbb F_2[t]/(t^2+t+1)\). It computes actual matrix products and actual projective eigenlines, without using the linear-map proof, compares every target fiber with (1) or (2), and checks that all fiber cardinalities sum to \(q^8\). Run `python3 verify.py`; the last line must be `VERIFY_OK`. These finite enumerations are checks, not replacements for the proof above.

## Relationship to prior work
The 2010 work of Britnell–Wildon classifies which matrix similarity classes can contain commuting representatives; its class-level compatibility results do not give the present prescribed **anticommutator target** multiplicities. The 2010 preprint by Kanel-Belov–Malev–Rowen analyzes image sets of noncommutative polynomials on two-by-two matrices, notably over quadratically closed fields, rather than the finite-field cardinality of each individual fiber. Huang's 2021 full-text enumeration of \(AB=\zeta BA\) covers the **zero target** \(XY+YX=0\) when \(\zeta=-1\) and the characteristic is odd (and ordinary commuting pairs in characteristic two). Thus the zero-fiber count alone is not proposed as original. The asserted new contribution is the uniform, full prescribed-**nonzero**-target distribution, including its dependence on rational kernel/eigenlines and its characteristic-two collapse. The older fixed-target commutator literature and the change of variables \((X,Y)\mapsto (X+Y,X-Y)\) in odd characteristic are plausible equivalence routes, and could affect priority.

## Limitations
No claim is made about matrices of order greater than two, scheme-theoretic singularities, or quotient counts under conjugation. The factor labels matter. In odd characteristic, the substitution \(U=X+Y\), \(V=X-Y\) gives \(U^2-V^2=2C\); any preexisting complete count for this difference-of-squares equation would subsume (2). Absolute literature uniqueness has not been established. The evidence for correctness is the complete proof above plus finite checks; independent audit has not been performed.

## References
1. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811 (first posted 6 January 2010).
2. A. Kanel-Belov, S. Malev and L. Rowen, *The images of non-commutative polynomials evaluated on 2 by 2 matrices*, arXiv:1005.0191 (first posted 3 May 2010), *Proc. Amer. Math. Soc.* 140 (2012), 465–478.
3. Y. Huang, *Counting on the variety of modules over the quantum plane*, arXiv:2110.15570 (2021), especially Theorems 1.1–1.2; used for comparison, not as an archive-period source.
4. J. Johnson, A. Porter and P. Varineau, *Commutators over finite fields* (1978); first three pages inspected for comparison with fixed-commutator target counts.
