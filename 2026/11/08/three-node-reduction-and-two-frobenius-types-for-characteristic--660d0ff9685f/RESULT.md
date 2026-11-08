# Three-node reduction and two Frobenius types for characteristic-two Fricke cubics

## Finding
Let \(k=\mathbb F_q\), \(q=2^m\), \(m\geq1\), and let \(d\in k^\times\). Write \(c\in k^\times\) for the unique square root of \(d\), and set \(\epsilon=(-1)^{\operatorname{Tr}_{k/\mathbb F_2}(c^{-1})}\). For the affine Fricke surface \(U_d\) given by \(x^2+y^2+z^2+xyz=d\), its projective closure \(S_d\) has exactly three rational ordinary double points. Its minimal resolution \(Y_d\) is a smooth geometrically rational weak del Pezzo surface of degree three. For every \(n\geq1\),
\[
\#U_d(\mathbb F_{q^n})=q^{2n}+1+\epsilon^nq^n,\qquad
\#Y_d(\mathbb F_{q^n})=q^{2n}+1+(6+\epsilon^n)q^n.
\]
Consequently,
\[
Z(Y_d/k,T)=\frac{1}{(1-T)(1-q^2T)(1-qT)^6(1-\epsilon qT)}.
\]
Arithmetic Frobenius acts on the rank-seven geometric Picard group with characteristic polynomial \((X-1)^6(X-\epsilon)\). Both Frobenius types occur when \(q\geq4\): exactly \(q/2-1\) nonzero parameters have \(\epsilon=1\), and \(q/2\) have \(\epsilon=-1\).

## Assumptions and scope
All geometric assertions concern the explicit projective closure
\[
S_d:\quad w(x^2+y^2+z^2)+xyz+dw^3=0\quad\subset\mathbb P^3_k
\]
in characteristic two, and its minimal resolution of singularities. Every parameter is nonzero. This is a statement about that integral affine equation and its specified projective closure; no identification with a moduli-theoretic character variety in characteristic two is assumed. In point-count formulas \(d\), \(c\), and \(\epsilon\) are fixed in \(k\), and extension is always from \(k\) to \(\mathbb F_{q^n}\).

## Proof
**Singularities.** The four homogeneous partial derivatives of the displayed cubic are \(yz,xz,xy,x^2+y^2+z^2+dw^2\). Thus at a singular geometric point at most one of \(x,y,z\) is nonzero. If \(w=0\), the final derivative excludes every such projective point. If \(w\ne0\), normalize \(w=1\); because \(d\ne0\), precisely the three points \([c:0:0:1]\), \([0:c:0:1]\), \([0:0:c:1]\) occur. Near the first, setting \(x=c+u\) gives \(u^2+y^2+z^2+cyz+uyz=0\). The invertible linear change \(v=u+y+z\) gives \(v^2+cyz+uyz=0\); its quadratic tangent cone \(v^2+cyz=0\) is a smooth projective conic, since its only potential gradient-zero point \([1:0:0]\) does not lie on it. Hence the singularity is an ordinary quadratic double point, with smooth split exceptional conic. The other two follow by symmetry.

**Resolution and Picard rank.** Blowing up these three disjoint ordinary double points resolves them, and each exceptional divisor is a smooth split conic with \(q^n+1\) extension-field points. Projection from any rational node shows that the cubic is rational: a general line through that node meets the cubic twice at the node and once at a rationally determined residual point. The minimal resolution is therefore geometrically rational. The anticanonical divisor is the pullback of a hyperplane section and has self-intersection three, so the resolution is weak del Pezzo of degree three. The standard Picard formula for smooth rational surfaces gives \(\operatorname{rank}\operatorname{Pic}(Y_{\bar k})=10-K^2=7\).

**Counting the affine points.** Put \(c^2=d\) and \(\psi(t)=(-1)^{\operatorname{Tr}_{k/\mathbb F_2}(t)}\). Solutions with \(x=0\) or \(y=0\) contribute \(2q-1\), because the other squared expression has a unique square root and the intersection \(x=y=0\) is counted twice. When \(xy\ne0\), setting \(a=x^{-1}, b=y^{-1}, t=z/(xy)\) changes the equation into
\[
t^2+t=(a+b+cab)^2.
\]
The characteristic-two Artin–Schreier criterion counts two solutions if and only if \(\operatorname{Tr}(a+b+cab)=0\), so the number in this stratum equals
\[
(q-1)^2+\sum_{a,b\in k^\times}\psi(a+b+cab).
\]
For \(a=c^{-1}\) the inner sum in \(b\) is \((q-1)\psi(c^{-1})\); for other nonzero \(a\) it is \(-\psi(a)\). Since \(\sum_{a\in k^\times}\psi(a)=-1\), the entire character sum is \(1+q\epsilon\). Adding the \(2q-1\) boundary points yields \(q^2+1+q\epsilon\). Over \(\mathbb F_{q^n}\) the absolute trace of \(c^{-1}\in k\) is \(n\) times its trace over \(k\), giving the claimed \(\epsilon^n\).

**Compactification and zeta function.** The divisor \(w=0\) is the triangle \(xyz=0\) in \(\mathbb P^2\) and has exactly \(3q^n\) points for every \(n\). Thus \(\#S_d(\mathbb F_{q^n})=q^{2n}+1+(3+\epsilon^n)q^n\). Replacing each of the three rational singular points by its split exceptional \(\mathbb P^1\) adds \(3q^n\) further points. Applying the defining exponential identity for the zeta function, \(Z(Y_d/k,T)=\exp(\sum_{n\ge1}\#Y_d(\mathbb F_{q^n})T^n/n)\), gives the displayed factorization.

**Frobenius and parameter classes.** For a smooth geometrically rational surface, the geometric Picard group has rank seven, all odd \(\ell\)-adic cohomology vanishes, and \(H^2_{\mathrm{et}}\) is the Picard lattice tensored with \(\mathbb Q_\ell(-1)\). The all-extension trace formula therefore forces the characteristic polynomial \((X-1)^6(X-\epsilon)\) on Picard. Squaring is a bijection of \(k^\times\), as is inversion; the trace has \(q/2\) elements in each fiber, with zero only in the trace-zero fiber. This gives precisely \(q/2-1\) and \(q/2\) parameters.

## Verification
The standalone script `checks/markoff_verify.py` performs exact arithmetic in \(\mathbb F_{2^m}\) for every \(1\le m\le6\), checking **all** parameter values and **all** affine triples against the character-sum formula. Running it prints `VERIFY_OK` as recorded in `checks/output.txt`. These finite computations verify the small-field witnesses; the general results, Picard polynomial, and zeta function follow from the preceding proof, not from extrapolation. The verification program uses only the standard Python library.

## Relationship to prior work
Boalch and Paluba's 2013 study introduces the complex Fricke family \(xyz+x^2+y^2+z^2+\sum b_i x_i+c=0\), including its Markov and Cayley specializations; it does not assert this characteristic-two three-node model or the trace-controlled Frobenius factors. Bourgain–Gamburd–Sarnak study the Markoff dynamics and strong approximation. De Courcy-Ireland and Lee study Markoff surfaces over odd prime fields, including odd-prime Legendre-symbol point-count expressions; their formulas do not directly apply in characteristic two. Earlier finite-field cubic-surface point-count work and general rational-surface cohomology provide context but do not by themselves identify the parameter-dependent trace sign for this specific characteristic-two family. This distinction is mathematical, not a proof of historical priority.

## Limitations
The formula is restricted to nonzero \(d\) and the indicated projective closure. It does not describe the degenerate zero fiber, arithmetic of higher-dimensional character varieties, or automorphism/monodromy orbit classification. The general geometric Picard identification uses standard rational-surface and ordinary-double-point facts, independently of the finite verifier. Specialist literature may contain an equivalent characteristic-two count under a different normalization; independent priority review remains necessary.

## References
1. P. Boalch and R. Paluba, *Symmetric cubic surfaces and G₂ character varieties*, arXiv:1305.6594, first posted May 28, 2013, introduction and Section 7; journal publication 2016.
2. J. Bourgain, A. Gamburd and P. Sarnak, *Markoff Triples and Strong Approximation*, arXiv:1505.06411, first posted May 24, 2015.
3. M. de Courcy-Ireland and S. Lee, *Experiments with the Markoff Surface*, arXiv:1812.07275, December 18, 2018, Section 2.
4. L. Carlitz, *The number of points on certain cubic surfaces over a finite field*, 1957, odd-characteristic counting context.
