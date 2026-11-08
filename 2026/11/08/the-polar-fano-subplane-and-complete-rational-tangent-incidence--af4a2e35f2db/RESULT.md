# The polar Fano subplane and complete rational tangent incidence of the Klein quartic over eight elements

## Finding
Let \(k=\mathbb F_8=\mathbb F_2(\alpha)\), with \(\alpha^3+\alpha+1=0\), and let \(K\subset\mathbb P^2_k\) be the smooth Klein quartic
\[
F(X,Y,Z)=X^3Y+Y^3Z+Z^3X=0.
\]
For a rational smooth point \(Q\in K(k)\), write \(T_QK\) for its projective tangent line. Define the polar base-point set
\[
U=V(F_X,F_Y,F_Z)(k)=\{[1:t:t^5]:t\in k^\times\}.
\]
Then \(U\) is a seven-point embedded Fano subplane \(\operatorname{PG}(2,2)\) of \(\operatorname{PG}(2,8)\), entirely outside \(K\). The 24 distinct lines \(T_QK\), for \(Q\in K(k)\), are **exactly** the 24 rational projective lines disjoint from \(U\). Moreover, for every \(P\in\mathbb P^2(k)\),
\[
\#\{Q\in K(k):P\in T_QK\}=
\begin{cases}
0,&P\in U,\\
2,&P\in K(k),\\
4,&P\in\mathbb P^2(k)\setminus(U\cup K(k)).
\end{cases}
\]
The incidence spectrum is therefore \(0^7,2^{24},4^{42}\). In particular this point-maximal genus-three quartic is not tangent-filling over \(k\), and its exact seven-point tangent defect coincides with its polar base locus.

## Assumptions and scope
All points and lines counted in the theorem are **\(k\)-rational**; all tangencies are at points of \(K(k)\). The assertion does not concern tangent lines based at nonrational geometric points, nor arbitrary plane quartics. A line is disjoint from \(U\) if it contains none of its seven rational points. The geometric smoothness of \(K\) follows from the partial derivatives as proved below. The 24-point count is known classically (Pellikaan and Elkies), but is also derived here from an orbit and the Serre bound.

## Proof
**1. Smoothness and polar points.** In characteristic two,
\[
(F_X,F_Y,F_Z)=(X^2Y+Z^3,\ X^3+Y^2Z,\ Y^3+Z^2X).
\]
A common projective zero of these derivatives cannot have any zero coordinate: one zero coordinate forces the other two to vanish. With all coordinates nonzero, multiplying the three equations respectively by \(X,Y,Z\) shows \(X^3Y=Y^3Z=Z^3X\ne0\); hence \(F\ne0\) because three equals one in characteristic two. Thus \(K\) is geometrically smooth and has genus three.

For a common derivative zero normalize \(X=1\), put \(Z=z\), and obtain \(Y=z^3\), \(z^7=1\). Conversely these equations annul every derivative. All seven roots are distinct and lie in \(k^\times\); moreover \(F(1,z^3,z)=z^3\ne0\). Reparametrizing \(t=z^3\) gives the claimed set \(U=\{[1:t:t^5]\}\). Since \(z^7-1\) has nonzero derivative at every root, the polar base scheme is reduced there.

The map \(u\mapsto(u,u^4,u^2)\) is \(\mathbb F_2\)-linear and sends the three-element basis \(1,\alpha,\alpha^2\) to columns with determinant one in \(k\). Thus its image is a three-dimensional \(\mathbb F_2\)-subspace spanning \(k^3\); its seven nonzero vectors, up to \(\mathbb F_2^\times\), give an embedded Fano plane. Indeed, dividing \([u:u^4:u^2]\) by \(u\) gives \([1:u^3:u]\), and \(t=u^3\) gives \(u=t^5\).

**2. The 24 rational flexes.** The transformations
\[
h:[X:Y:Z]\mapsto[X:\alpha Y:\alpha^5Z],\qquad
\sigma:[X:Y:Z]\mapsto[Y:Z:X]
\]
preserve \(K\) and \(U\) and generate a group of order 21. The point \(P_0=[1:1:\alpha]\) belongs to \(K\). The three \(\langle h\rangle\)-orbits of \(P_0,\sigma(P_0),\sigma^2(P_0)\) each have size seven and are distinct: after normalizing the first coordinate to one, the invariant \(Z/Y^5\) takes the distinct values \(\alpha,\alpha^2,\alpha^4\). The three coordinate vertices form a second orbit and lie on \(K\). Consequently \(\#K(k)\ge24\). The Serre point bound for genus three over \(\mathbb F_8\) is \(8+1+3\lfloor2\sqrt8\rfloor=24\), so these are all its rational points.

Every one of these points is a flex. At \([1:0:0]\) the tangent is \(Y=0\), with intersection order three. At \(P_0\) the gradient is \((\alpha,\alpha^3,\alpha^6)\) and the tangent can be parametrized by \([1:1+s:\alpha+\alpha^4s]\); direct substitution gives
\[
F(1,1+s,\alpha+\alpha^4s)=\alpha^3s^3+\alpha^4s^4.
\]
Hence contact order is exactly three; the group carries these flexes to all 24 points. Two different flexes cannot share a tangent line, since their intersection multiplicities with a quartic would sum to at least six, contrary to Bézout. Thus the 24 tangents are distinct.

**3. The tangent lines avoid the Fano subplane.** For the vertex representative the tangent is \(Y=0\), which contains no \([1:t:t^5]\) with \(t\ne0\). For \(P_0\), evaluating its tangent on the seven points \([1:\alpha^j:\alpha^{5j}]\), in increasing \(j=0,\dots,6\), gives the nonzero sequence
\[
\alpha^2,\ \alpha,\ 1,\ \alpha^4,\ \alpha^2,\ \alpha^3,\ \alpha^2.
\]
Because \(h\) and \(\sigma\) preserve the subplane, all 24 tangents avoid \(U\). A Fano subplane has seven extended lines meeting \(U\) in three points, and exactly 42 ambient lines meeting \(U\) in one point (each Fano point lies on six such lines). Of the 73 lines in \(\operatorname{PG}(2,8)\), the remaining 24 avoid \(U\). Our 24 distinct tangents exhaust them.

**4. Which ambient points have two or four tangents?** The seven extended Fano lines have six points each outside \(U\), and their intersections with one another lie in \(U\), so their union outside \(U\) has precisely 42 points. We show \(K(k)\) is disjoint from those seven lines. The coordinate vertex \([1:0:0]\) is on no line containing three points of \(U\): a line through that vertex meets \(U\) where \(bt+ct^5=0\), which has at most one nonzero solution (\(t^4\) permutes \(k^\times\)). At \(P_0\), the seven joining lines to the seven points of \(U\), with \(t=\alpha^j\) in order, have the following pairwise distinct normalized coefficient triples:
\[
(1,1,0),\ (1,\alpha^3,1),\ (0,1,\alpha^6),\ (1,0,\alpha^6),\ (1,\alpha^4,\alpha^4),\ (1,\alpha^6,\alpha),\ (1,\alpha^5,\alpha^3).
\]
Thus no Fano line passes through \(P_0\). By the group action, every rational point of \(K\) avoids those seven lines. There are exactly 24 points outside their union, so they are precisely the 24 points of \(K(k)\).

For \(P\in U\), no line disjoint from \(U\) passes through \(P\). For \(P\notin U\) outside the seven extended Fano lines, the seven Fano points lie on seven distinct lines through \(P\); among the nine lines through \(P\), exactly two avoid \(U\). For \(P\notin U\) lying on one of the seven extended Fano lines, three of the Fano points share a line through \(P\), while the other four determine four distinct lines; exactly four of its nine lines avoid \(U\). These are precisely the 24 tangent lines by Step 3, proving the formula and its full partition. \(\square\)

## Verification
Two independent standalone pure-Python programs accompany this theorem. Run `python3 verify_tangents.py` to enumerate all 73 projective points and lines using \(\mathbb F_2[z]/(z^3+z+1)\), compute the curve and polar loci, check tangent distinctness and characterize all 24 tangent lines by their disjointness from \(U\), verify line intersections \(0^{24},1^{42},3^7\) with \(U\), and count the exact incidence spectrum. Run `python3 verify_symmetry.py` to perform a separate test using the different field model \(\mathbb F_2[z]/(z^3+z^2+1)\), and verify the group orbit, flex tangent, Fano line incidence, and representative exclusions. Both programs require only the Python standard library. Their outputs validate finite identities; the preceding algebraic and finite-geometry proof establishes the stated classification.

## Relationship to prior work
Asgarli and Ghioca, *Tangent-filling plane curves over finite fields* (first public 26 February 2023, arXiv:2302.13420), introduce the tangent-filling question and motivate the exact complement of rational tangent unions. The quartic model and its 24 rational points over eight elements are classical; Pellikaan (1998) identifies a Fano **incidence design on the nonzero coordinates of 21 curve points**, and Elkies (1998) studies the rational points and the classical 24 flex points. These are not claimed as new. The embedded polar seven-point Fano **subplane of the ambient projective plane**, its identification with the exact tangent defect, the characterization of the 24 tangent lines as the lines avoiding that subplane, and the entire \(0/2/4\) incidence partition are the present claims. A Fano design abstractly associated with curve coordinates does not alone identify a polar subplane of ambient \(\operatorname{PG}(2,8)\) or imply this tangent partition.

## Limitations
The point count, quartic model, classical flex geometry and abstract Fano combinatorics are prior facts, not new discoveries. The result concerns this single curve over eight elements, not all maximal curves, all finite fields, or tangent lines based at geometric nonrational points. It does not classify higher-degree tangent-filling curves. A published but unindexed equivalent finite-geometric description of these 24 lines remains a historical-priority risk; independent mathematical and historical review is not performed here.

## References
- S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420v1, 26 February 2023, https://arxiv.org/abs/2302.13420 .
- R. Pellikaan, *The Klein quartic, the Fano plane and curves representing designs*, in *Codes, Curves, and Signals: Common Threads in Communications*, pp. 9–20, 1998, https://ruudp.win.tue.nl/paper/32.pdf .
- N. D. Elkies, *The Klein Quartic in Number Theory*, in *The Eightfold Way*, MSRI Publications 35, 1998, https://dash.harvard.edu/bitstreams/7312037c-57aa-6bd4-e053-0100007fdf3b/download .
