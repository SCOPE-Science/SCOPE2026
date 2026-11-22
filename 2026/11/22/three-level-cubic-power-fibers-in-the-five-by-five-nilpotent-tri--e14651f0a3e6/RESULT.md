# Three-level cubic-power fibers in the five-by-five nilpotent triangular algebra

## Finding
For a finite field \(k=\mathbb F_q\), let \(N_5(k)\) be the ten-dimensional associative algebra of strictly upper-triangular \(5\times5\) matrices, and set
\[
P_Z=\#\{X\in N_5(k):X^3=Z\}.
\]
For every \(Z=A E_{14}+B E_{25}+C E_{15}\), the complete fiber distribution is
\[
\boxed{
P_Z=\begin{cases}
q^5(q-1)^2,&(A,B)\ne(0,0),\\
q^5(2q^3-3q^2+1),&A=B=0,\ C\ne0,\\
q^5(5q^3-5q^2+1),&A=B=C=0.
\end{cases}}
\]
Every target in \(N_5(k)^3\) occurs and no target outside this three-dimensional ideal occurs. The three positive values are distinct for every \(q\ge2\). In particular, the zero-output probability of a uniformly chosen \(X\) is
\[
\Pr(X^3=0)=5q^{-2}-5q^{-3}+q^{-5}.
\]
For characteristic-three fields the same distribution describes the cube-word map on the five-by-five upper-unitriangular group, since \((I+X)^3=I+X^3\). Thus every element of its third lower-central subgroup is a cube, with nonconstant cube-root multiplicities (the group's center has the enhanced nonidentity fibers).

## Assumptions and scope
The field \(k\) is finite of arbitrary prime-power order \(q\ge2\); no restriction on its characteristic is required for the associative-algebra theorem. Matrix units \(E_{ij}\) have \(i<j\), and \(N_5(k)^3\) is the \(k\)-linear span of \(E_{14},E_{25},E_{15}\). Powers are ordinary associative products, not the Frobenius map on entries. Group consequences require characteristic exactly three. The fiber count is for individually prescribed targets, not a count up to conjugacy.

## Proof
Write the ten coordinates of \(X\) as
\[
a=X_{12},\quad b=X_{23},\quad c=X_{34},\quad d=X_{45},
\quad e=X_{13},\quad f=X_{24},\quad g=X_{35},
\]
with \(X_{14},X_{25},X_{15}\) left free. Multiplication of strictly upper-triangular matrices gives exactly
\[
(X^3)_{14}=abc,\qquad (X^3)_{25}=bcd,\qquad
(X^3)_{15}=abg+adf+ecd,
\]
and all other entries vanish. The three uppermost free coordinates of \(X\) never enter \(X^3\), producing a universal factor \(q^3\) in every fiber.

For fixed \((a,b,c,d)\), the last output coordinate is the linear functional
\[
(e,f,g)\longmapsto cd\,e+ad\,f+ab\,g.
\]
If the coefficient triple \((cd,ad,ab)\) is nonzero, every prescribed \(C\) has exactly \(q^2\) choices of \((e,f,g)\); if the triple is zero, only \(C=0\) is possible and has \(q^3\) choices.

Suppose \((A,B)=(abc,bcd)\ne(0,0)\). Then \(b,c\ne0\), and each choice of \((b,c)\in(k^\times)^2\) determines uniquely \(a=A/(bc)\) and \(d=B/(bc)\). The functional is nonzero (its coefficient \(cd\) is nonzero if \(B\ne0\), and \(ab\) is nonzero if \(A\ne0\)). The number of solutions including the three free coordinates is therefore \((q-1)^2q^2q^3=q^5(q-1)^2\), independently of \(C\).

Now suppose \(A=B=0\). The number of quadruples \((a,b,c,d)\) obeying \(abc=bcd=0\) is
\[
H=q^3+(q-1)q^2+(q-1)^2=2q^3-2q+1.
\]
This partitions by \(b=0\), by \(b\ne0,c=0\), and by \(b,c\ne0\) with \(a=d=0\). Among those quadruples, the coefficient triple vanishes exactly when
\[
ab=ad=cd=0.
\]
Counting separately \(b=0\) and \(b\ne0\) gives
\[
S=(q^2+q-1)+(q-1)(2q-1)=3q^2-2q.
\]
Thus \(H-S=2q^3-3q^2+1\) quadruples have a nonzero linear functional. For nonzero \(C\), only those contribute, each with \(q^2\) middle-coordinate choices and \(q^3\) free choices, proving the second fiber formula. For \(C=0\), all \(H-S\) nondegenerate quadruples contribute \(q^2\), while all \(S\) degenerate quadruples contribute \(q^3\). Hence
\[
P_0=q^3\bigl[q^2(H-S)+q^3S\bigr]
=q^5(5q^3-5q^2+1).
\]
All three expressions are strictly positive for \(q\ge2\). They sum with multiplicities \((q^2-1)q\), \(q-1\), and \(1\) respectively to \(q^{10}\), establishing exhaustiveness, surjectivity onto \(N_5(k)^3\), and the zero-output probability after division by \(q^{10}\). The three values are distinct: their differences, in increasing order, equal \(q^5[(2q^3-3q^2+1)-(q-1)^2]=2q^6(q-1)^2\) and \(q^5[3q^3-2q^2]=q^7(3q-2)\), respectively.

In characteristic three, the binomial identity \((I+X)^3=I+3X+3X^2+X^3=I+X^3\) identifies the additive-algebra fibers with the group cube-word fibers, without requiring commutativity. Its third lower-central subgroup is \(I+N_5(k)^3\), so every such group target is indeed a cube.

## Verification
A standalone Python checker is included as `CHECKER.py`, with its genuine recorded output as `CHECKER_OUTPUT.txt`. The checker computes the full matrix cube by independent matrix multiplication over the prime fields of orders \(2,3,5,7\) and over \(\mathbb F_4\). It enumerates every choice of the seven active coordinates and explicitly accounts for the three free upper coordinates, verifying every one of the \(q^3\) prescribed targets and the total number \(q^{10}\) of matrices. Finite enumerations corroborate the displayed all-field proof; they do not establish that infinite statement by themselves.

## Relationship to prior work
Sosnovsky's 2012 study of verbal widths of triangular groups and Bier's 2012 work on unitriangular verbal widths establish power-word image and width background, not a target-by-target cube-root census. Dolfi, Singh, and Yadav (2019) examine \(p\)-power images and conjugacy classes, and for the first surjective range identify the entire lower-central image; image membership does not determine prescribed fiber multiplicities. Menshov and Roman'kov (2015) study adjoining roots inside larger unitriangular groups, a different root-existence setting. Relevant indexed records for unitriangular powers at the first nonsurjective threshold (size \(p+3\)), characteristic-two five-by-five square fibers, and four-by-four cube/Engel distributions address distinct domains or words. The resulting three-valued cubic-fiber law is assessed as a separate claim, without asserting that a complete historical priority check has been achieved.

## Limitations
The full distribution on the five-by-five algebra is established, not a general formula in arbitrary matrix size. The group interpretation applies only in characteristic three. There is residual risk of an earlier implicit exact fiber formula in the literature on nilpotent-group power words or flag-preserving matrix roots, and no independent external audit has been performed.

## References
1. Yu. V. Sosnovsky, *On the Width of Verbal Subgroups of the Groups of Triangular Matrices over a Field of Arbitrary Characteristic*, arXiv:1201.6513v1 (first public 2012-01-31), https://arxiv.org/html/1201.6513v1.
2. A. Bier, *The width of verbal subgroups in the group of unitriangular matrices over a field*, International Journal of Algebra and Computation 22 (2012), 1250019, https://doi.org/10.1142/S0218196712500191.
3. S. Dolfi, A. Singh, M. K. Yadav, *\(p\)-Power conjugacy classes in \(U(n,q)\) and \(T(n,q)\)*, arXiv:1905.04244v1 (2019), https://arxiv.org/abs/1905.04244.
4. A. Menshov, V. Roman'kov, *Adjunction of roots to unitriangular groups over prime finite fields*, arXiv:1506.02806v1 (2015), https://arxiv.org/abs/1506.02806.
