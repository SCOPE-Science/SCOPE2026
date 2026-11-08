# Exact embedded-centralizer spectrum of the strictly upper-triangular four-by-four algebra

## Finding

Let \(k=\mathbb F_q\), with \(q\) any prime power, and \(N=N_4(k)\) the algebra of strictly upper-triangular \(4\times4\) matrices. For \(X\in N\) set \(C_N(X)=\{Y\in N:XY=YX\}\). Centralizers are counted **as actual embedded subalgebras**, not as element-indexed occurrences, conjugacy classes, or possible dimensions.

**Theorem.** Exactly \(2q^3+q^2+3\) distinct subalgebras occur among the \(C_N(X)\). The complete distribution, including the number of elements \(X\) producing any *one fixed* centralizer in a row, is

| Centralizer type | Dimension over \(k\) | Distinct centralizers | Elements per centralizer |
| --- | ---: | ---: | ---: |
| Full algebra | \(6\) | \(1\) | \(q\) |
| Hyperplane | \(5\) | \(q+1\) | \(q(q-1)\) |
| Generic codimension two | \(4\) | \(q^3+q^2\) | \(q(q-1)\) |
| Exceptional codimension two | \(4\) | \(1\) | \(q^3(q-1)\) |
| Codimension three | \(3\) | \(q^3-q\) | \(q^2(q-1)\) |

For the finite algebra group \(UT_4(q)=1+N\), precisely the same number of distinct centralizer subgroups arises, and their orders are obtained from the dimensions above by \(r\mapsto q^r\). The multiplicities of group elements giving each fixed subgroup coincide with the last column.

## Assumptions and scope

The coefficient ring is a finite field of arbitrary characteristic; in particular characteristic two is included. Centralizers are taken **inside** \(N\), rather than inside the full matrix algebra. The algebra \(N\) is associative and nonunital. Equality of centralizers means equality of subsets, or equivalently equality of their \(k\)-linear subspaces. The theorem counts labeled embedded centralizers, without modding out by automorphisms or conjugation.

## Proof

Write
\[
X=aE_{12}+bE_{13}+cE_{14}+dE_{23}+eE_{24}+fE_{34},
\]
where the six coefficients range independently over \(k\). For
\(Y=A E_{12}+B E_{13}+C E_{14}+D E_{23}+E E_{24}+F E_{34}\), direct multiplication gives
\[
[X,Y]=(aD-dA)E_{13}+(dF-fD)E_{24}
 +(aE+bF-eA-fB)E_{14}.
\]
Thus \(c\) and \(C\) do not affect the commutation relation. In the coordinate order \((A,B,D,E,F)\), the annihilator equations have row vectors
\[
 r_1=(-d,0,a,0,0),\qquad
 r_2=(0,0,-f,0,d),\qquad
 r_3=(-e,-f,0,a,b).
\]
Let \(R_X\subseteq k^5\) denote their span. Because each \(C_N(X)\) is the kernel of this linear map together with the free \(E_{14}\) coordinate, **two elements have equal centralizers if and only if their rowspaces \(R_X\) coincide**. Its codimension in \(N\) equals \(\dim R_X\).

We classify the possible rowspaces, preserving their fibers under \(X\mapsto R_X\):

**Case 1: \(d=a=f=0\).** If also \(b=e=0\), all rows vanish. This yields the unique full centralizer and \(q\) elements from the arbitrary \(c\). Otherwise only \(r_3=(-e,0,0,0,b)\) survives. Its one-dimensional span gives a projective point in the coordinate plane \((A,F)\): exactly \(q+1\) different centralizers of dimension \(5\). Each projective point admits \(q-1\) nonzero representatives \((b,e)\), and the free \(c\) gives \(q(q-1)\) elements per centralizer.

**Case 2: \(d=0\) and \((a,f)\ne(0,0)\).** The first two rows span the single \(D\)-coordinate line. Modulo that line, the third row is \((-e,-f,0,a,b)\). Thus \(R_X\) is specified by a one-dimensional subspace of the four-coordinate \((A,B,E,F)\) space not contained in the two-dimensional subspace defined by \(B=E=0\). Its number is
\[
\frac{q^4-1}{q-1}-\frac{q^2-1}{q-1}=q^3+q^2.
\]
Every such line has \(q-1\) nonzero representatives \((-e,-f,a,b)\), and arbitrary \(c\) gives \(q(q-1)\) elements per dimension-four centralizer.

**Case 3: \(d\ne0\) and \(a=f=0\).** Here \(r_1\) and \(r_2\) span exactly the \(A\)- and \(F\)-coordinate directions; \(r_3\) belongs to this same two-space for all \((b,e)\). This is one additional dimension-four centralizer, distinct from Case 2 because the latter contains the \(D\)-line. There are \((q-1)q^2\) choices of \((d,b,e)\), giving \(q^3(q-1)\) elements after the free \(c\) is included.

**Case 4: \(d\ne0\) and \((a,f)\ne(0,0)\).** Normalize
\[
\alpha=a/d,\qquad\phi=f/d,\qquad
\gamma=(\phi b-\alpha e)/d.
\]
Elementary row operations put \(R_X\) in the canonical basis
\[
(-1,0,\alpha,0,0),\qquad
(0,0,-\phi,0,1),\qquad
(0,-\phi,\gamma,\alpha,0).
\]
All three rows are independent because \((\alpha,\phi)\ne(0,0)\). The rowspace itself determines \((\alpha,\phi)\) from its intersection with the \((A,D,F)\)-coordinate three-space, and then determines \(\gamma\) uniquely from the remaining normalized row, whose \((B,E)\) coordinates are \((-\phi,\alpha)\). Conversely, every choice of \((\alpha,\phi)\ne(0,0)\) and \(\gamma\in k\) occurs. Hence there are exactly \(q(q^2-1)=q^3-q\) distinct dimension-three centralizers. For any fixed triple, \(d\in k^\times\) is arbitrary, and \((b,e)\) satisfies one nonzero linear equation \(\phi b-\alpha e=d\gamma\), allowing \(q\) choices. Including \(c\), each such centralizer has \(q^2(q-1)\) elements in its fiber.

Cases 1–4 are disjoint by rank or by presence of the \(D\)-coordinate line; within the rank-three case the canonical parameters are intrinsically recovered from the rowspace. Summing the numbers of distinct rowspaces gives
\[
1+(q+1)+(q^3+q^2)+1+(q^3-q)=2q^3+q^2+3.
\]
As a separate consistency check, multiplying each row's count by its fiber size and summing gives \(q^6=|N|\). This also shows the table is exhaustive.

Finally, multiplication in \(1+N\) satisfies \((1+X)(1+Y)=(1+Y)(1+X)\) exactly when \(XY=YX\). Hence \(C_{1+N}(1+X)=1+C_N(X)\), a bijection of embedded centralizer structures respecting individual fibers. This completes the proof.

## Verification

Run the bundled Python program with `python3 verify.py`. The program constructs \(N\) from its six standard matrix units, independently computes commutator coefficients by ordinary matrix multiplication, forms row-reduced echelon spaces over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7\), and compares both the distinct-centralizer counts and every fiber multiplicity with the formulas. In the binary extension field it uses \(\mathbb F_4\cong\mathbb F_2[t]/(t^2+t+1)\). Successful execution prints `VERIFY_OK_N4_CENTRALIZERS`.

Observed numbers of distinct centralizers at these field orders are \(23,66,147,278,738\), respectively. The program enumerates all \(q^5\) effective parameter tuples for each listed field, with \(q\) central choices suppressed and restored algebraically. Finite enumeration corroborates, but does not establish, the theorem for all prime powers; the four-case proof establishes the universal claim.

## Relationship to prior work

The study of centralizer-number invariants is motivated by Dutta–Basnet–Nath, who classify finite rings with at most five distinct centralizers. Kundu–Naik–Singh study nilpotent Lie algebras with exactly two centralizer dimensions; their breadth-type hypotheses exclude the four-dimensional breadth spectrum \(0,1,2,3\) found here. Majeed–Ramkumar give the explicit three commutation equations and the *possible centralizer orders* for \(UT_4(p)\) in their Table 1. Those equations and orders are prior results, and part of the rank-three group structure can be inferred from their clique decomposition. The result here instead resolves equality between centralizer subspaces, counts all distinct embedded centralizers (particularly the two very different codimension-two fibers), and includes nonprime finite fields. Anil Kumar–Prajapati (2015), more directly, explicitly introduced equality of centralizer subgroups in \(UU_4(\mathbb F_q)\), and their Lemma 22 ALREADY counts \(q^2(q-1)\) such classes on the subset where \(d=0\) and \(af\ne0\), each of size \(q(q-1)\); their Theorem 15 supplies a count on the regular-superdiagonal subset. These covered components are acknowledged and not claimed new. Their work does not state or derive the whole-group equality classification, including the central and exceptional codimension-two strata. Bhunia studies conjugacy classes of centralizers for an upper-triangular invertible group over infinite fields of odd characteristic; conjugate centralizers and equal embedded centralizers are different counting problems.

The closest relevant literature has therefore been compared by its mathematical conclusions, not by title. This inspection does not establish worldwide publication priority; a broader unpublished or unlocated theorem might imply the formula.

## Limitations

The claim applies only to strictly upper-triangular \(4\times4\) matrices and the associated algebra groups over finite fields. It does not enumerate centralizers in the full \(4\times4\) matrix ring, triangular algebras with diagonal elements, larger unitriangular groups, conjugacy classes of centralizers, or centralizer-lattice intersection patterns. The exact formula is a labeled-subalgebra count, not a similarity-class count. The finite checks do not certify the infinite family independently; the universal proof is algebraic. Publication priority remains provisional.

## References

1. R. Kundu, T. K. Naik, A. Singh, *Nilpotent Lie algebras with two centralizer dimensions over a finite field*, arXiv:2208.07676v1, first posted August 16, 2022. https://arxiv.org/abs/2208.07676
2. M. Majeed, P. B. Ramkumar, *Commuting Graph of Unitriangular Group UT(4, p)*, arXiv:2608.09235v1, first posted August 10, 2026, esp. §2 and Table 1; §5 and §6. https://arxiv.org/abs/2608.09235
3. J. Dutta, D. K. Basnet, R. K. Nath, *Characterizing some rings of finite order*, arXiv:1510.08207, first posted October 28, 2015. https://arxiv.org/abs/1510.08207
4. S. Bhunia, *Conjugacy classes of centralizers in the group of upper triangular matrices*, arXiv:1901.07869v1, first posted January 23, 2019. https://arxiv.org/abs/1901.07869
5. C. P. Anil Kumar, S. K. Prajapati, *Maximal Non-commuting Sets in Unipotent Upper-triangular Linear Group \(UU_4(\mathbb F_q)\)*, institutional preprint dated February 18, 2015; see Definition 4, Theorem 15, Lemma 22, and §§4–5. https://www.isibang.ac.in/~statmath/eprints/2015/1.pdf
