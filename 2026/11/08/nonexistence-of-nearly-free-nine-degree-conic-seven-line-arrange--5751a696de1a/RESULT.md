# Nonexistence of nearly free degree-nine conic–seven-line arrangements with simple intersections

## Finding

There is no nearly free reduced plane curve over \(\mathbb C\) consisting of one smooth conic and seven distinct lines whose singularities are exclusively ordinary nodes \(A_1\), tacnodes \(A_3\), and ordinary triple points \(D_4\). The conclusion is only for the one-conic/seven-line stratum of degree nine.

## Assumptions and scope

Let \(D=Q\cup L_1\cup\cdots\cup L_7\subset\mathbb P^2_{\mathbb C}\), where \(Q\) is smooth and the lines are distinct. Nearly free means that the saturation quotient of the Jacobian ideal of a reduced equation of \(D\) is nonzero, with each graded component of dimension at most one. A line tangent to \(Q\) contributes one tacnode and cannot participate in a triple on \(Q\); all other lines are called secants. A triple on \(Q\) consists of \(Q\) and two distinct secants, all transverse. In particular a contact point does not lie on another line of the arrangement.

## Proof

**Numerical reduction.** Write \(n,t,s\) for the numbers of nodes, tacnodes, and triples of \(D\). By Gałecka [1, Theorem 3.4, Propositions 4.1 and 4.4], near freeness implies \(4\le r=\operatorname{mdr}(D)\le\lfloor9/2\rfloor=4\), hence \(\tau(D)=8^2-4(8-4)-1=47\), and
\[8+n+\tfrac34s\ge 7+\tfrac52t.\]
Bézout and the local Tjurina numbers give \(n+2t+3s=35\) and \(n+3t+4s=47\). Consequently \(s=12-t\), \(n=t-1\), and \(1\le t\le4\).

Write \(u\) for the triples off \(Q\), \(v\) for the triples on \(Q\), and \(h=7-t\) for the number of secants. Thus \(u+v=12-t\) and \(v\le h\) by Bézout on the secants, so \(u\ge5\). In the arrangement of just the seven lines, the number of double points is **\(21-3u\)**: the \(v\) intersections on \(Q\) remain double points when the conic is removed. The number of double points off \(Q\) is \(21-3u-v\). No point of the line arrangement has multiplicity at least four. The strong line inequality of Hirzebruch [2, Section 6, (9)] therefore gives \(21-3u+3u/4\ge7\), so \(u\le6\).

No three distinct tangents to \(Q\) concur, since they would give three collinear points on the smooth dual conic. Let \(a,b,g\) count the off-conic triples with respectively two, one, and zero tangents. Thus \(u=a+b+g\). Counting the pairs of tangents, the pairs of secants, and the mixed pairs, respectively, gives
\[
a\le\binom t2,\qquad b+3g+v\le\binom h2,\qquad 2(a+b)\le th.
\]
At the \(b\)-type triples on any fixed tangent, the pairs of secants are disjoint, so \(b\le t\lfloor h/2\rfloor\). We will use also the simple graph on the secant lines with one edge per pair meeting on \(Q\). Its maximum degree is two and all edges correspond to distinct points. In particular, when \(v=h\) it is a disjoint union of simple cycles.

**One tangent.** Here \(a=0\), \(b\le3\), and \(u\ge5\) forces \(g\ge2\). Since \(b+g+v=11\) and \(b+3g+v\le15\), we have \(g=2,b=3,u=5,v=6\). Every secant participates in one \(b\)-type triple (the pairs at the tangent are disjoint) and has exactly two on-conic pair intersections. Each secant has six incidences with other lines, counted by pairs. The \(b\)-type triple and the two on-conic intersections account for four; all six line double points are on \(Q\). Thus each secant participates in exactly one of the two \(g\)-type triples. The secants form two disjoint pencils of three with distinct centers \(A,B\) off the tangent. In the affine chart with the tangent at infinity, the \(b\)-type triples pair the pencils' lines in parallel directions, once in each direction. The central symmetry \(x\mapsto A+B-x\) exchanges the pencils, exchanges the six distinct off-diagonal intersections in pairs, and preserves \(Q\) because five distinct points determine a smooth conic. Its restriction to \(Q\cong\mathbb P^1\) is a nonidentity involution, so has two fixed points over \(\mathbb C\). But its only plane fixed points are the line at infinity and the affine midpoint. The former has just one point on \(Q\) by tangency. The midpoint cannot lie on \(Q\), since it is distinct from and collinear with two exchanged affine conic points. This is a contradiction.

**Two tangents.** Here \(a\le1\), \(b+3g+v\le10\), and \(a+b+g+v=10\), giving \(2g\le a\le1\), hence \(g=0\). The bound \(b\le4\) now forces \(a=1,b=4,u=5,v=5\). The on-conic pair graph on the five secants is a 5-cycle; its complement is also a 5-cycle. Let \(S_*\) be the secant through the intersection of the two tangents. Each tangent participates in two \(b\)-type triples and cannot use \(S_*\) in either. Its pairs must therefore form a perfect matching in the complement cycle with \(S_*\) deleted. This is a four-vertex path, which has just one perfect matching, so the two tangents would use the same secant pair at a \(b\)-type triple, contrary to the absence of fourfold intersections.

**Three tangents.** Here \(a+b+g+v=9\), \(a\le3\), and \(b+3g+v\le6\), hence \(a=3,g=0\) and \(b\in\{2,3\}\). Call the tangents \(T_i\) for \(i=1,2,3\); the three secants through their pair intersections are distinct, and we label \(S_i\) the one through the intersection of the other two tangents. Write \(S_4\) for the remaining secant. A \(b\)-type triple on \(T_i\) can only use \(S_i,S_4\), because the two other secants already meet \(T_i\) at the \(a\)-type triples. All six secant pairs are used by \(b\) or \(v\); in particular the three pair intersections of \(S_1,S_2,S_3\) lie on \(Q\). If \(b=2\), then \(v=4\), so the on-conic pair graph must be a 4-cycle, not contain a triangle. If \(b=3\), normalize \(T_1,T_2,T_3\) to the coordinate axes and \(S_4\) to \(x+y+z=0\) (it misses the three tangent vertices). The other three secants are \(y+z=0,x+z=0,x+y=0\). Their three pair intersections, up to scaling, are
\[(1,1,-1),\quad(1,-1,1),\quad(-1,1,1).\]
The dual conic matrix has zero diagonal and off-diagonal entries \(A,B,C\) at positions \(12,13,23\), respectively, because the coordinate axes are tangent; \(ABC\ne0\) by nonsingularity. The primal equation is given by its adjugate, i.e.
\[-C^2x^2-B^2y^2-A^2z^2+2BCxy+2ACxz+2AByz=0.\tag{1}\]
Subtracting its value at the second point from its value at the first gives \(4C(B-A)\); subtracting its value at the third from its value at the first gives \(4B(C-A)\). If all three values vanish, then \(A=B=C\), but the first value is then \(-5A^2\ne0\). This eliminates \(b=3\).

**Four tangents.** Here \(v=8-u\) is 2 or 3, and \(b+3g+v\le3\) gives \(g=0\), \(b\le3-v\), so \(a=u-b\ge5\). Each of the three secants contains at most two vertices of tangent pairs, because a tangent cannot meet that secant twice. At least two secants thus each join two vertices of disjoint tangent pairs, making them two of the three diagonal lines of the complete quadrilateral of tangents. Their intersection is on neither a tangent nor \(Q\): normalize the tangents to \(x=0,y=0,z=0,x+y+z=0\) and the diagonals are \(x+y=0,x+z=0,y+z=0\). Their pair intersections are the three points listed above, visibly off the tangents. In (1) the fourth tangency says \(A+B+C=0\); the three values at these points are \(4BC,4AC,4AB\), all nonzero.

The pair of diagonal secants therefore uses an off-conic secant pair that does not contribute to \(b\). This forces \(v=2\), \(b=0\) (only one off-conic pair is then available), so \(u=a=6\). All three secants would have to be the three diagonal lines, and none of their pair intersections is on \(Q\), contradicting \(v=2\). This finishes the proof.

## Verification and limitations

`verify_constraints.py` independently checks the finite numerical reduction and the adjugate polynomial evaluations with exact integer arithmetic. The script is not the proof of the geometric exclusions, which use the pencil symmetry, matching obstruction, and explicit conic calculations above. The incorrect count \(21-3u-v\) cannot be used as the total number of double points of the line-only arrangement.

This excludes neither arrangements with several conics nor examples admitting other singularities, such as ordinary quadruple points. Historical priority is not implied by proving this statement. Gałecka leaves degrees eight and nine open in the cited classification; the numerical inequalities here leave surviving incidence patterns, which require the extra geometry.

The cases with \(u=6\) also fall under the previously recorded sharp Tjurina bound for conics adjoining the non-Fano seven-line arrangement [3], which gives \(\tau\le46\) in that stratum. That bound does not address \(u=5\). Pokora's example [4, Theorem 4.1] has four ordinary quadruple points and is outside the present hypotheses.

## References

1. A. Gałecka, *On the nearly freeness of conic-line arrangements with nodes, tacnodes, and ordinary triple points*, arXiv:2204.13969, Bol. Soc. Mat. Mex. 28, 67 (2022), DOI: 10.1007/s40590-022-00461-4.
2. F. Hirzebruch, *Singularities of Algebraic Surfaces and Characteristic Numbers*, MPI preprint 85-39 (1985), Section 6, inequality (9), https://archive.mpim-bonn.mpg.de/id/eprint/2262/1/preprint_1985_39.pdf .
3. *Sharp Tjurina bound for conics adjoining the non-Fano seven-line arrangement*, Resultary record 20d0ed6a92c8, §6.
4. P. Pokora, *On the Numerical Terao Conjecture*, arXiv:2608.05662, Theorem 4.1.
