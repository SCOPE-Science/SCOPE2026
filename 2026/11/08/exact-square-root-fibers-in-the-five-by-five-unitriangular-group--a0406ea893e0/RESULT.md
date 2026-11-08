# Exact square-root fibers in the five-by-five unitriangular group

## Finding

Let \(k\) be a field of characteristic \(2\), and set \(G=\operatorname{UT}_5(k)\). An element of the second term of the lower central series \(\gamma_2(G)\) is uniquely written as \(I+S\), where the only possibly nonzero entries of \(S\) are
\[
(u,v,w,x,y,z)=(S_{13},S_{24},S_{35},S_{14},S_{25},S_{15}).
\]
The **exact image of the squaring word map** \(g\mapsto g^2\) consists of precisely the elements \(I+S\) satisfying both implications
\[
 v=0\ \Longrightarrow\ uw=0,
 \qquad
 v\ne0\ \text{and}\ u=w=0\ \Longrightarrow\ vz=xy.
\]
These implications are sufficient over **every** characteristic-two field; there are no further restrictions.

For \(k=\mathbb F_q\) (\(q\) any power of \(2\)), write \(R_q(u,v,w,x,y,z)\) for the number of square roots of \(I+S\) inside \(G\). The **complete square-root fiber formula** is

| Target condition | \(R_q\) |
| --- | ---: |
| \(v\ne0\), \((u,w)\ne(0,0)\) | \(q^3(q-1)\) |
| \(v\ne0\), \(u=w=0\), \(vz=xy\) | \(q^4(q-1)\) |
| \(v=0\), exactly one of \(u,w\) nonzero | \(q^4(q-1)\) |
| \(u=v=w=0\), \(xy\ne0\) | \(q^4(q-1)\) |
| \(u=v=w=0\), exactly one of \(x,y\) nonzero | \(q^4(q^2-1)\) |
| \(u=v=w=x=y=0\), \(z\ne0\) | \(3q^5(q-1)\) |
| \(u=v=w=x=y=z=0\) | \(q^5(5q-4)\) |
| All other targets in \(\gamma_2(G)\) | \(0\) |

Every target outside \(\gamma_2(G)\) likewise has zero square roots. In particular,
\[
\boxed{\bigl|\{g^2:g\in\operatorname{UT}_5(\mathbb F_q)\}\bigr|
=q^6-q^5+q^4+q^3-q^2.}
\]
The known fact that individual squares fail to form a subgroup starting at matrix size five is *not* claimed as new.

## Assumptions and scope

The image characterization holds for any field \(k\) of characteristic \(2\). The displayed cardinality and the root-fiber table require the finite field \(\mathbb F_q\) with \(q=2^m\), \(m\ge1\). All ordered matrix entries and square roots are counted as distinct elements. Group squares and the subgroup **generated** by group squares are not conflated. For \(n=5\), \(\gamma_2(\operatorname{UT}_5(k))\) consists of matrices whose first superdiagonal is zero, with the six coordinates displayed above.

## Proof

**1. A literal coordinate square.** Write an arbitrary \(g=I+N\in G\) with ten strict-upper-triangular coordinates
\[
\begin{array}{c|cccccccccc}
\text{position}&12&23&34&45&13&24&35&14&25&15\\
\hline
\text{entry}&a&b&c&d&e&f&g_0&h&i&j
\end{array}
\]
(the letter \(g_0\) is a scalar, not a group element). Since \(\operatorname{char}k=2\), \((I+N)^2=I+N^2\). Direct multiplication gives
\[
 u=ab,\quad v=bc,\quad w=cd,\qquad
 x=af+ec,\quad y=bg_0+fd,\quad z=ai+eg_0+hd.
\tag{1}
\]
The coordinate \(j\) is always free. In particular, the first superdiagonal vanishes.

**2. Necessity and sufficiency.** If \(v=bc=0\), then \(b=0\) or \(c=0\); hence \(uw=abcd=0\). If \(v\ne0\), then \(b,c\ne0\). The conditions \(u=w=0\) force \(a=d=0\), after which \(x=ec\), \(y=bg_0\), \(z=eg_0\), so \(vz=xy\).

Conversely, suppose the two restrictions hold. If \(v\ne0\), choose
\[
 b=1,\quad c=v,\quad a=u,\quad d=w/v,\quad f=0,\quad
 e=x/v,\quad g_0=y.
\]
When \((u,w)\ne(0,0)\), the remaining equation \(ai+hd=z+eg_0\) is solvable in \((h,i)\); when \(u=w=0\), it is exactly the assumed equation \(vz=xy\). Take \(j=0\).

When \(v=0,u\ne0\), necessarily \(w=0\); take \(a=u,b=1,c=d=0,f=x/u,g_0=y,i=z/u\), and set \(e=h=j=0\). When \(v=0,w\ne0\), necessarily \(u=0\); take \(a=b=0,c=1,d=w,e=x,f=y/w,h=z/w\) and \(g_0=i=j=0\).

Finally suppose \(u=v=w=0\). If \(y=0\), take \(a=1,b=c=d=0,f=x,i=z\) and all unspecified variables zero. If \(x,y\ne0\), take \(a=1,b=c=0,f=x,d=y/x,i=z\) and all unspecified variables zero. If \(x=0,y\ne0\), take \(a=b=c=0,d=1,f=y,h=z\) and all unspecified variables zero. These cover every remaining target. This proves the exact image characterization over arbitrary characteristic-two fields.

**3. Root-fiber counts away from the deepest stratum.** When \(v\ne0\), \(b\) has \(q-1\) choices and then \(a=u/b,c=v/b,d=w/c\) are forced. The variable \(f\) has \(q\) choices and then \(e,g_0\) are forced by \(x,y\). If \((u,w)\ne(0,0)\), one nontrivial linear equation in \(h,i\) has \(q\) solutions, while \(j\) has \(q\) choices: \((q-1)q^3\) roots. If \(u=w=0\), the constraint is precisely \(vz=xy\) and \(h,i,j\) are free, giving \((q-1)q^4\) roots. When \(v=0\) and exactly one of \(u,w\) is nonzero, solving in the analogous order leaves one nonzero first-superdiagonal coordinate and four free scalar choices, giving \((q-1)q^4\) roots.

**4. All three second-superdiagonal coordinates zero.** If \(u=v=w=0\), partition inputs in equation (1) into three disjoint cases: \(b\ne0\), \(b=0,c\ne0\), and \(b=c=0\). A direct count (with \(j\) included) gives

| Condition on \(x,y,z\) | \(b\ne0\) | \(b=0,c\ne0\) | \(b=c=0\) |
| --- | ---: | ---: | ---: |
| \(xy\ne0\) | \(0\) | \(0\) | \((q-1)q^4\) |
| \(x\ne0,y=0\) | \(0\) | \((q-1)q^5\) | \((q-1)q^4\) |
| \(x=0,y\ne0\) | \((q-1)q^5\) | \(0\) | \((q-1)q^4\) |
| \(x=y=0,z\ne0\) | \((q-1)^2q^4\) | \((q-1)^2q^4\) | \((q^2+q-2)q^4\) |
| \(x=y=z=0\) | \((q-1)(2q-1)q^4\) | \((q-1)(2q-1)q^4\) | \((q^2+2q-2)q^4\) |

Here the first two columns follow by fixing the nonzero variable \(b\) or \(c\) and solving the remaining linear constraints. In the third column, \(x=af\), \(y=fd\): when \((x,y)\ne(0,0)\), the choice \(f\ne0\) is forced, leaving \((q-1)q^4\) solutions; when \(x=y=0\), split further into \(f=0\) or \(f\ne0\) and count the scalar equation \(eg_0=z\). Its numbers of solutions are \(q-1\) for \(z\ne0\) and \(2q-1\) for \(z=0\). Summing the three columns gives the last four nontrivial rows of the root-fiber table. This verifies all zero-boundary cases rather than extrapolating from the generic locus.

**5. Total image size.** If \(v=0\), there are \(2q-1\) admissible pairs \((u,w)\) and \(q^3\) unconstrained triples \((x,y,z)\). If \(v\ne0\), there are \((q-1)(q^2-1)q^3\) admissible targets with \((u,w)\ne(0,0)\), and \((q-1)q^2\) with \(u=w=0\), because \(z\) is then uniquely determined. Thus the image size is
\[
(2q-1)q^3+(q-1)(q^2-1)q^3+(q-1)q^2
=q^6-q^5+q^4+q^3-q^2.
\]
Summing \(R_q\) over all six-coordinate targets gives \(q^{10}=|G|\), an independent algebraic consistency check.

## Verification

Run `python3 verify_squares.py` using a standard Python 3 interpreter. It independently constructs the full five-by-five matrices and multiplies them over \(\mathbb F_2\) and \(\mathbb F_4\), enumerates all possible source coordinates (restoring the free upper-right entry), and compares **every** target's actual square-root multiplicity with the preceding table. The finite-field multiplication in the checker uses an explicit polynomial basis, not a symbolic assumption about the image. The exhaustive results are 52 squares among 64 possible derived-subgroup elements over \(\mathbb F_2\), and 3,376 among 4,096 over \(\mathbb F_4\). The checker also verifies a concrete failure of closure under multiplication. The record `verification_output.txt` contains the corresponding replayed result.

These finite checks test the theorem but do not establish its universal quantifiers. The preceding coordinate arguments prove the result for every characteristic-two field (and the counting formulas for all finite such fields).

## Relationship to prior work

Sosnovsky's treatment of triangular-group power-word width and Agnieszka Bier's work on verbal subgroups of unitriangular groups supply the broad width context. Bier proves a sharp width-two result for the square word starting at matrix size five in characteristic two. That already establishes that the set of squares is not a subgroup; we do not claim this threshold or the width result as new. Dolfi, Singh and Yadav's study of prime-power maps proves structural bounds for the power image and explicitly tabulates 52 and 3,376 squares for the size-five groups over fields of orders 2 and 4. Those known numerical examples agree exactly with our formula. The contribution assessed here is the **all-field six-coordinate membership criterion and complete, uniform square-root fiber distribution**, including the image-count polynomial for every binary field size. Neither cited primary statement supplies these formulas. A more general unlocated character-theoretic or word-map formula could imply this specialization; priority remains provisional.

## Limitations

The calculations are specific to five-by-five unitriangular groups and the square word in characteristic two. They do not determine the image or root-fiber spectrum for arbitrary larger unitriangular groups, other word maps or odd characteristic. The algebraic proof is self-contained; the computational checks are limited to fields with two and four elements. Historical originality has not been independently certified.

## References

1. Yu. V. Sosnovsky, *On the Width of Verbal Subgroups of the Groups of Triangular Matrices over a Field of Arbitrary Characteristic*, arXiv:`1201.6513` (public January 31, 2012), especially Section 1, Theorem 1.
2. A. Bier, *The Width of Verbal Subgroups in the Group of Unitriangular Matrices over a Field*, International Journal of Algebra and Computation **22** (2012), 1250019, DOI: `10.1142/S0218196712500191` (first public journal version March 8, 2012).
3. S. Dolfi, A. Singh, M. K. Yadav, *p-Power Conjugacy Classes in U(n,q) and T(n,q)*, arXiv:`1905.04244` (initial public preprint May 10, 2019), especially Proposition 3.4, Theorem A, and the size-five computational table in Section 3.
