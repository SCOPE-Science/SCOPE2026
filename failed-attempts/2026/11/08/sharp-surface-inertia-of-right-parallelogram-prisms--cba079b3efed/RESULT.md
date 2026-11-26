# Sharp surface inertia of right parallelogram prisms

## Finding
Let \(K=P\times[-h,h]\subset\mathbb R^3\), where \(h>0\) and \(P\) is any nondegenerate Euclidean parallelogram in a plane perpendicular to the prism axis. Let \(A\) be the surface area, \(c=A^{-1}\int_{\partial K} x\,dS(x)\) its surface centroid, and \(J=\int_{\partial K}\|x-c\|^2\,dS(x)\). Then
\[
\boxed{\frac{J}{A^2}\ge\frac5{72}},
\]
with equality if and only if \(K\) is a cube, up to rigid motion and positive scaling. Thus the sharp cuboid surface-inertia inequality persists under arbitrary shear of a right parallelogram prism's planar base. The proof yields an explicit nonnegative deficit decomposition.

## Assumptions and scope
The base is an arbitrary (possibly very slender or sheared) **nondegenerate** parallelogram, both base side lengths are positive, its interior angle lies strictly between zero and \(\pi\), and the lateral generator is **perpendicular** to the base. No lower bounds on the angle or aspect ratios are imposed. The surface mass measure is ordinary area, not volume or edge length. All boundaries consist of six Euclidean faces. The centroid \(c\) is the center of symmetry.

## Proof
Set the two base edge-vector lengths to \(a,b>0\), let \(\phi\in(0,\pi)\) be their angle, and write \(B=ab\sin\phi\) for the base area and \(L=2(a+b)\) for its perimeter. The base centered at the origin has the parametrization \(tu+sv\) for \(t,s\in[-1/2,1/2]\), with \(\|u\|=a\), \(\|v\|=b\). Symmetry forces the surface centroid of \(K\) to be the origin.

Direct integration on the two base faces yields the planar polar integral \(I_B=B(a^2+b^2)/12\). The planar polar integral on the *boundary* of the parallelogram is
\[
I_{\partial B}=2b(a^2/4+b^2/12)+2a(b^2/4+a^2/12)=(a+b)^3/6.
\]
The base-edge formula is independent of \(\phi\) because opposite-edge contributions cancel the cross term. Integrating height \(z\in[-h,h]\) over the four rectangular lateral faces, and adding both end faces at \(z=\pm h\), gives precisely
\[
A=2B+4h(a+b),\qquad
J=\frac{B(a^2+b^2)}6+\frac{h(a+b)^3}3+2Bh^2+\frac{4h^3(a+b)}3.
\]

By positive homogeneity \(J/A^2\) is unchanged under uniform scaling. Hence normalize \(a+b=1\), set \(x=ab\) and \(y=B=ab\sin\phi\). The exact domain satisfies \(0<y\le x\le1/4\). In these coordinates,
\[
A=2y+4h,\qquad J=\frac{y(1-2x)}6+\frac h3+2yh^2+\frac43h^3.
\]
A direct polynomial expansion, displayed below as an explicit positive certificate, gives
\[
\begin{aligned}
72J-5A^2={}&24y(\tfrac14-x)\\
&+(1-4y)\,8h(12h^2-10h+3)\\
&+y(4h-1)^2(24h+1)+20y(\tfrac14-y).
\end{aligned}
\]
Every summand is nonnegative because \(h>0\), \(0<y\le x\le1/4\), and \(12h^2-10h+3=12(h-5/12)^2+11/12>0\). If equality holds, strict positivity of the quadratic forces \(y=1/4\). Therefore \(x=1/4\), \(a=b=1/2\), and \(\sin\phi=1\), while the third summand forces \(h=1/4\). The base is a square and the full prism has equal width, depth and height, hence is a cube. Conversely the unit-scaled cube gives \(J/A^2=5/72\). This proves the theorem for **every** admissible right parallelogram prism; no finite case enumeration is used as an infinite proof.

## Verification
The accompanying standalone `verify.py` checks the polynomial identity symbolically with exact arithmetic and evaluates the surface integral independently on all six planar faces using Gaussian quadrature. It compares the analytic surface area and moment with 4,000 independently generated shear/size/height examples, plus the sharp lower bound. These checks are corroborative, not substitutes for the analytical argument. Execute `python verify.py` with Python, SymPy and NumPy installed.

## Relationship to prior work
Freitas, Laugesen and Liddell (2007), Theorem 5, established the same \(5/72\) constant with a unique cube equality case for **rectangular boxes**, which have mutually perpendicular base edges. Their Theorems 3 and 4 concern triangular and regular-polygon prisms. The present assertion is the extension of that sharp constant and equality classification to all right parallelogram-base prisms, including sheared bases. The 2026 preprint by Csató, Giovagnoli and Roy addresses broad existence theorems for weighted surface-perimeter extremals and a planar shape classification, but does not state this sharp three-dimensional restricted-class theorem. These antecedents are not represented as discoveries of the present note.

## Limitations
The theorem does not concern general skew-lateral (oblique-axis) parallelepipeds, arbitrary convex quadrilateral prisms, or global minimizers among all convex surfaces. The right-hand sharp constant is attained already in the known cuboid subfamily; new mathematical content is the full shear-inclusive inequality and exact deficit certificate. No independent priority audit has been conducted. The 2007 source is publicly available as a manuscript whose title page carries the date December 19, 2007; its exact first online-release day has not been separately established, although 2007 publication is independently corroborated.

## References
1. P. Freitas, R. S. Laugesen and G. F. Liddell, *On convex surfaces with minimal moment of inertia*, *Journal of Mathematical Physics* **48** (2007), 122902, DOI: 10.1063/1.2823888. Author-posted full text: https://www.researchgate.net/publication/228883213_On_convex_surfaces_with_minimal_moment_of_inertia .
2. G. Csató, D. Giovagnoli and P. Roy, *Weighted Perimeters and pth Moments of Inertia of Convex Curves and Surfaces*, arXiv:2608.19851v1 (2026), https://arxiv.org/abs/2608.19851 .
