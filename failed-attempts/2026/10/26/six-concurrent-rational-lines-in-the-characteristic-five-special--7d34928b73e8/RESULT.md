# Six concurrent rational lines in the characteristic-five special fibre of Bring’s curve

## Finding
Let \(e_j\) denote the \(j\)-th elementary symmetric polynomial in five homogeneous coordinates \(X_0,\ldots,X_4\). Let \(\mathscr B\subset\mathbb P^4_{\mathbb Z}\) be the complete intersection \(e_1=e_2=e_3=0\), the integral root-coordinate model of Bring’s curve. Over \(k=\mathbb F_5\), its scheme-theoretic fibre is a reduced union of exactly six distinct \(k\)-lines through \(P=[1:1:1:1:1]\). This is the only singular point. The six branches are geometrically distinct and smooth, and their tangent directions lie on a smooth conic in \(\mathbb P^2\). The singularity has \(\delta=9\), associated-graded local Hilbert function \((1,3,5,6,6,\ldots)\), and normalization \(\bigsqcup_{i=1}^{6}\mathbb P^1\). The fibre has \(31\) rational points over \(\mathbb F_5\).

## Assumptions and scope
All scheme equalities are over \(\mathbb F_5\), or its algebraic closure after scalar extension. This is the specified integral embedding, not an assertion concerning minimal regular or stable models of Bring’s curve. In characteristics other than \(2,3\), the three elementary-symmetric equations are equivalent to the more familiar power-sum equations of degrees \(1,2,3\) by Newton identities; in particular this is the classical equation in characteristic five. The generic complex fibre is the genus-four Bring curve.

## Proof
On \(X_4\ne0\), normalize \(X_4=1\), put \(X_i=1+U_i\) for \(i=0,1,2,3\), and use \(e_1=0\) to eliminate \(U_3=-U_0-U_1-U_2\). Set \(u=U_0\), \(v=U_1\), \(w=U_2\). Direct expansion in characteristic five gives \(e_2=Q\) and \(e_3=3Q+C\), where
\[
Q=-(u^2+uv+uw+v^2+vw+w^2),\qquad C=-(u+v)(u+w)(v+w).
\]
Thus the affine chart is **exactly** the homogeneous affine cone \(\operatorname{Spec}k[u,v,w]/(Q,C)\), with vertex \(u=v=w=0\) corresponding to \(P\). The quadratic form \(Q\) is nondegenerate in characteristic five; its projective vanishing set is a smooth conic. On \(u+v=0\), the residual equation is \(u^2+w^2=0\), whose two simple rational solutions have \(w=2u\) or \(w=3u\). Permuting \(u,v,w\) gives six distinct projective directions, represented by the two triples \((1,4,2),(1,4,3)\), \((1,2,4),(1,3,4)\), and \((2,1,4),(3,1,4)\), equivalently the normalized set
\[
\{(1,2,3),(1,2,4),(1,3,2),(1,3,4),(1,4,2),(1,4,3)\}.
\]
The smooth conic and the reduced cubic intersection meet transversely at each of these six points (each factor defines a line meeting the conic in two simple points, with no intersections of different factors on the conic). Therefore \((Q,C)\) is the radical homogeneous ideal of six distinct lines through the affine origin. Their projective closures give six distinct projective lines through \(P\). Since \(e_1,e_2,e_3\) is a projective complete intersection of multidegree \((1,2,3)\) and degree six, no other one-dimensional component or embedded component occurs: the fibre is equidimensional Cohen–Macaulay, and its six known reduced degree-one components already account for the full degree. All intersections between distinct lines are at \(P\), so no other singular points exist.

The completed local ring at \(P\) is the completion of the graded one-dimensional complete intersection \(R=k[u,v,w]/(Q,C)\). Its Hilbert series is \((1-t^2)(1-t^3)/(1-t)^3\), with graded dimensions \(1,3,5,6,6,\ldots\). Each branch is a line and therefore normal, so the normalization of the local ring is the product of six formal power series rings. In degree \(n\), the normalization has six independent homogeneous coefficients. The normalization quotient has degree-wise dimensions \(6-1=5\), \(6-3=3\), \(6-5=1\), and zero thereafter, hence \(\delta=9\). Equivalently, the arithmetic genus is \(0+9-(6-1)=4\), agreeing with the genus-four complete-intersection formula. Six \(\mathbb F_5\)-lines each have six rational points, and all meet only at the common rational point, hence the count is \(1+6(6-1)=31\).

## Verification
Run `python3 verify_bring5.py` with Python 3 and SymPy installed. The program symbolically reconstructs the chart equations, exhaustively lists the six projective directions, checks nondegeneracy and distinctness, and enumerates the \(\mathbb P^3(\mathbb F_5)\) points of the fibre to confirm the 31-point count. The Hilbert-series and conductor-length calculation above is an exact general proof, not an extrapolation from finite points.

## Relationship to prior work
The classical genus-four root-coordinate model and \(S_5\) symmetry are standard, as recalled in Braden–Northover. Serre’s *Topics in Galois Theory*, Chapter 8, Section 8.3.2, Exercise (d) lists good reduction away from characteristics \(2,5\), while Exercise (e) describes the characteristic-two semistable reduction. These established facts are not presented as new. The result here describes the **missing characteristic-five special fibre of the displayed integral embedding**, its six-line decomposition, and its intrinsic local \(\delta\)-invariant. A different integral/stable model need not have this special fibre.

## Limitations
This is not a computation of the stable reduction, Néron model, component intersection pairing of a regular surface, or monodromy. An equivalent description may occur in older discussions not located in the searches. The classification is for the displayed integral complete intersection, not every model of the generic curve.

## References
1. H. W. Braden and T. P. Northover, *Bring's Curve: its Period Matrix and the Vector of Riemann Constants*, arXiv:1206.6004v1 (first posted 26 June 2012), especially Introduction and Equation (1.1), https://arxiv.org/abs/1206.6004.
2. J.-P. Serre, *Topics in Galois Theory*, Chapter 8, Section 8.3.2, exercise on the Bring curve, especially (d) and (e), https://www.ms.uky.edu/~sohum/ma561/notes/workspace/books/serre_galois_theory.pdf.
