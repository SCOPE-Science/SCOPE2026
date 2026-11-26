# Complete square-root fibers at the first unitriangular nonsurjectivity threshold

## Finding
Let \(q=2^e\) with \(e\geq1\), and let \(G=UT_5(\mathbb F_q)\) be the group of upper unitriangular \(5\times5\) matrices. Every square belongs to the subgroup \(G_2\) whose first superdiagonal vanishes. Write an arbitrary element of \(G_2\) as \(I+C\), with its six potentially nonzero upper entries
\[
(A,B,C_0,D,E,F)=(C_{13},C_{24},C_{35},C_{14},C_{25},C_{15}).
\]
The letter \(C_0\) is a scalar coordinate, not the target matrix. Put \(N_q(A,B,C_0,D,E,F)=\#\{g\in G:g^2=I+C\}\). Define the \(2\times2\) matrix
\[
M=\begin{pmatrix} B&E\\D&F\end{pmatrix}.
\]
The exact value of \(N_q\) is the **sum of all contributions from the following mutually disjoint root strata**; conditions within different rows need not be disjoint as target conditions, because the corresponding sets of roots are disjoint:

| Condition on the target | Contribution to \(N_q\) |
| --- | --- |
| \(A B C_0\ne0\) | \((q-1)q^3\) |
| Exactly one of \(A,C_0\) is nonzero and \(B=0\) | \((q-1)^2q^3\) |
| \(A=B=C_0=D=E=0\) | \((q-1)^2q^4\) |
| \(A=B=C_0=0\) and \(DE\ne0\) | \((q-1)q^4\) |
| \(A\ne0,\ C_0=0\) | \((q-1)q^3\) |
| \(A=0,\ C_0\ne0\) | \((q-1)q^3\) |
| \(A=B=C_0=E=0\) | \((q-1)q^5\) |
| \(A=B=C_0=D=0\) | \((q-1)q^5\) |
| \(A=C_0=0\) and \(\operatorname{rank}M=1\) | \((q-1)q^4\) |
| \(A=C_0=0\) and \(M=0\) | \((2q^2-1)q^4\) |

In particular, a target with nonzero first superdiagonal has no roots; targets in \(G_2\) have roots exactly under the following four alternatives:

1. \(A C_0\ne0\) and \(B\ne0\), with \(D,E,F\) arbitrary;
2. exactly one of \(A,C_0\) is nonzero, with \(B,D,E,F\) arbitrary;
3. \(A=C_0=0,\ B\ne0\), and \(BF=DE\);
4. \(A=B=C_0=0\), with \(D,E,F\) arbitrary.

Consequently the square image has exactly
\[
\boxed{\#\{g^2:g\in UT_5(\mathbb F_q)\}=q^6-q^5+q^4+q^3-q^2,}
\]
and the fiber over the identity has exactly
\[
\boxed{N_q(0,0,0,0,0,0)=5q^6-4q^5.}
\]
This is the first dimension at which the square map fails to cover its generated verbal subgroup: for \(2\le n\le4\), every element of \(\gamma_2(UT_n(\mathbb F_q))\) is a single square, whereas for \(n=5\) the image is a proper subset of \(\gamma_2(G)=G_2\).

## Assumptions and scope
All assertions concern finite fields \(\mathbb F_q\) of characteristic two, with \(q\ge2\). The group notation \(UT_n\) always means upper unitriangular matrices. Coordinates in the table range independently over \(\mathbb F_q\); zero tests, products, and rank are taken within that field. The identity-fiber formula counts group elements whose square is the identity (not the number of elements of order exactly two). No assumption is made that \(q\) is prime.

## Proof
Write \(g=I+X\) with the ten strict upper entries of \(X\) named
\[
\begin{array}{llll}
 a=X_{12},&b=X_{23},&c=X_{34},&d=X_{45},\\
 e=X_{13},&f=X_{24},&h=X_{14},&i=X_{25},\\
 j=X_{15},&g_0=X_{35}.&&
\end{array}
\]
Since the characteristic is two, \((I+X)^2=I+X^2\). Direct matrix multiplication gives exactly six equations:
\[
\begin{aligned}
 A&=ab,&B&=bc,&C_0&=cd,\\
 D&=af+ec,&E&=bg_0+fd,&F&=ai+eg_0+hd.
\end{aligned}
\tag{1}
\]
The variable \(j\) is always free. Partition the roots into the four disjoint cases according to whether \(a\) and \(d\) are zero.

**Case I: \(a d\ne0\).** The first three equations force \(b=A/a\), \(c=C_0/d\), and \(B=AC_0/(ad)\). For fixed \((a,d)\), the map \((e,f,g_0)\mapsto(D,E)\) has rows \((c,a,0)\) and \((0,d,b)\). It has rank two unless \(b=c=0\); in that exceptional case its rank is one. The equation for \(F\) imposes one independent linear condition on \((h,i)\), leaving \(q\) choices, and \(j\) contributes another factor \(q\). If \(A,B,C_0\) are all nonzero, \(ad=AC_0/B\) has \(q-1\) choices of \((a,d)\), and the remaining equations have \(q^3\) choices; this gives the first row. If exactly one of \(A,C_0\) is nonzero, one needs \(B=0\), there are \((q-1)^2\) choices of \((a,d)\), and again \(q^3\) choices thereafter; this gives the second row. Finally if \(A=C_0=0\), then \(B=0\), \(b=c=0\), and \(D=af,E=fd\). When \(D=E=0\), every nonzero \((a,d)\) works; when \(DE\ne0\), exactly \(q-1\) such pairs work; when exactly one is nonzero none work. The remaining four free parameters give \(q^4\) completions. This yields rows three and four.

**Case II: \(a\ne0,d=0\).** Necessarily \(C_0=0\). If \(A\ne0\), then \(b=A/a\ne0\), \(c=B/b\), and the two linear equations \(D=af+ec\), \(E=bg_0\) have exactly \(q\) solutions in \((e,f,g_0)\). The equation for \(F\) leaves \(q\) choices of \((h,i)\), and \(j\) is free, giving \((q-1)q^3\) roots and row five. If \(A=0\), then \(b=0\) and \(B=E=0\); \(c\) is arbitrary, the \(D\)-equation leaves \(q^2\) possibilities in \((e,f,g_0)\), while \(h,i,j\) contribute \(q^3\). Hence row seven.

**Case III: \(a=0,d\ne0\).** This is the transpose-reversal of Case II, with \((A,D,a)\) and \((C_0,E,d)\) interchanged, giving rows six and eight. The two cases are disjoint even when their conditions on the target overlap.

**Case IV: \(a=d=0\).** Necessarily \(A=C_0=0\), and the remaining equations reduce to
\[
\begin{pmatrix}B&E\\D&F\end{pmatrix}=
\begin{pmatrix}b\\e\end{pmatrix}
\begin{pmatrix}c&g_0\end{pmatrix}.
\tag{2}
\]
Every nonzero rank-one matrix over \(\mathbb F_q\) has precisely \(q-1\) ordered outer-product representations. The zero matrix has exactly \(2q^2-1\), because one of the two vectors must vanish. The variables \(f,h,i,j\) are free, giving the last two table rows.

All roots lie in exactly one of these four cases, so the table exhausts every fiber. The four image alternatives follow immediately. Their respective target counts are \((q-1)^3q^3\), \(2(q-1)q^4\), \((q-1)q^2\), and \(q^3\). These sum to \(q^6-q^5+q^4+q^3-q^2\). Evaluating the table at the zero target gives \(5q^6-4q^5\).

For the minimality assertion, \(UT_n\) with \(n\le2\) has trivial commutator subgroup. In \(UT_3\), any coefficient of the sole second-superdiagonal position is \(ab\). For \(UT_4\), write the three second-or-higher-superdiagonal target coordinates as \((u,v,w)\), and the squaring equations as \(u=ab,v=bc,w=ae+dc\). If \((u,v)\ne(0,0)\), take \(b=1,a=u,c=v\), then solve for \((d,e)\). If \(u=v=0\), take \(b=c=0,a=1,e=w\). Thus every target in \(\gamma_2\) is a square for \(n\le4\). For \(n=5\), the target \(A=C_0=0,B=1,D=E=0,F=1\) has \(BF\ne DE\) and has no square root. Independently, the classical power-word verbal subgroup is \(G_2\), confirming that \(UT_5\) is the first nonsurjective case.

## Verification
The standalone `verify.py` enumerates the square polynomial for all \(2^{10}\) group elements over \(\mathbb F_2\) and \(4^{10}\) elements over \(\mathbb F_4\), using irreducible polynomial \(T^2+T+1\) for the latter field. For each of the \(q^6\) potential targets, it compares the observed multiplicity with the ten-row formula and checks normalization, image size, and zero fiber. Direct literal matrix-squaring checks are independently executed for every binary element and a deterministic sample of quaternary elements. It prints `VERIFY_OK_UT5_SQUARE_FIBERS` if every check passes. Those finite checks cannot establish the formula for all \(e\); the four-case algebraic proof does so.

## Relationship to prior work
A. Bier's 2012 power-word width theorem identifies \(n=5\) as the first characteristic-two threshold at which the square-word width is two instead of one. Dolfi, Singh and Yadav (arXiv:1905.04244, Sections 1 and 3) establish that the square image is proper for \(n\ge5\) and obtain global lower estimates. Their analysis does not state the ten-stratum pointwise fiber table above, or the exact five-by-five image polynomial. Soffer (arXiv:1411.5389) develops conjugacy-class estimates for unitriangular groups; the conjugacy-class count is a different invariant from the distribution of a power-word map. All classical facts about matrix powers, rank-one factorizations, and verbal subgroups are used as background, not asserted as new.

## Limitations
The formula concerns \(UT_5\), squaring, and finite fields of characteristic two. It neither extends to general \(UT_n\) nor determines higher power words, odd-characteristic square roots, or conjugacy-class-refined fibers. The historical originality comparison is based on accessible primary statements and searched records; an equivalent implicit formula in earlier unpublished tables or textbooks cannot be ruled out. No independent mathematical audit has been performed.

## References
- A. Bier, *The width of verbal subgroups in the group of unitriangular matrices over a field*, International Journal of Algebra and Computation **22** (2012), article 1250019, DOI: 10.1142/S0218196712500191. Accessible author paper: https://pdfs.semanticscholar.org/ce40/e2080f04704859e482e378de546406687d2c.pdf.
- S. Dolfi, A. Singh, M. K. Yadav, *\(p\)-power conjugacy classes in \(U(n,q)\) and \(T(n,q)\)*, arXiv:1905.04244 (2019), https://arxiv.org/abs/1905.04244.
- A. Soffer, *Upper bounds on the number of conjugacy classes in unitriangular groups*, arXiv:1411.5389 (initial public arXiv submission 2014-11-19), https://arxiv.org/abs/1411.5389.
