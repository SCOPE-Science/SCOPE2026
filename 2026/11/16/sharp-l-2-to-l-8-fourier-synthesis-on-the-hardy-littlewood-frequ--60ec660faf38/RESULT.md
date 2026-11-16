# Sharp \(L^2\)-to-\(L^8\) Fourier synthesis on the Hardy–Littlewood frequency triple

## Finding
Let \(\mathbb T=\mathbb R/\mathbb Z\) have normalized Haar measure and \(P(t)=a+b e^{2\pi i t}+c e^{6\pi i t}\), where the coefficients are arbitrary complex numbers, not all zero. The sharp inequality
\[
\|P\|_{L^8(\mathbb T)}\le K_8 (|a|^2+|b|^2+|c|^2)^{1/2}
\]
has \(K_8^8=9.22177072362030\ldots\), hence \(K_8=1.32008467721721\ldots\).

Here is an exact algebraic description, which does not depend on decimal approximations. Put \(z=1-x-y\),
\[
W(x,y)=\sum_{j=0}^{12}\bigl([u^j](x+yu+zu^3)^4\bigr)^2,
\quad S(x,y)=x^2+y^2+z^2,\quad R(x,y)=\frac{W(x,y)}{S(x,y)^4}.
\]
There exists exactly one point \((x_*,y_*)\) in the rational square \([27/100,40/100]^2\) satisfying both polynomial equations
\[
W_xS-4WS_x=0,\qquad W_yS-4WS_y=0.
\]
It lies inside the probability simplex \(x>0,y>0,z>0\); its coordinates are
\[
(x_*,y_*,z_*)=(0.33317142810340987\ldots,0.34986453758311672\ldots,0.31696403431347341\ldots).
\]
Exactly \(K_8^8=R(x_*,y_*)\). Every nonzero extremizer is
\[
(a,b,c)=\lambda\bigl(x_*,y_*e^{i\theta},z_*e^{3i\theta}\bigr),\qquad
\lambda\in\mathbb C\setminus\{0\},\quad\theta\in\mathbb R.
\]
The corresponding normalized squared magnitudes are \((0.33246974291886\ldots,0.36662027234362\ldots,0.30090998473752\ldots)\): they are neither equal nor the same as the sixth-moment optimal profile.

## Assumptions and scope
Only the exact integer frequency support \(\{0,1,3\}\), the eighth moment and arbitrary complex coefficient amplitudes are considered. Frequency translation and multiplication of all frequencies by any nonzero integer preserve this continuous-circle problem. The \(L^8\) norm is normalized by total Haar measure one; the coefficient \(\ell^2\) norm is unnormalized. No finite sampling or finite-group aliasing is asserted.

## Proof
Write \(A=|a|\), \(B=|b|\), \(C=|c|\). Parseval applied to the fourth power gives
\[
\|P\|_8^8=\sum_{j=0}^{12}\bigl|[u^j](a+bu+cu^3)^4\bigr|^2.
\]
Each coefficient is a sum of monomials with nonnegative integer multinomial coefficients, so its absolute value does not exceed the coefficient of \((A+Bu+Cu^3)^4\). Equality simultaneously holds when \(3\arg b-2\arg a-\arg c\equiv0\pmod{2\pi}\). Conversely, for \(ABC>0\), the frequency-three coefficient contains the nonzero terms \(4ab^3\) and \(4a^3c\), so equality in that coefficient forces precisely this phase relation. Thus the complete complex optimization reduces to the nonnegative real one, and phase equality is strict off this relation for interior amplitudes.

Expanding the real fourth convolution and squaring its coefficients gives the homogeneous polynomial
\[
\begin{aligned}
F(A,B,C)={}&A^8+16A^6B^2+16A^6C^2+36A^4B^4+32A^4B^3C\\
&+144A^4B^2C^2+36A^4C^4+16A^2B^6+24A^2B^5C\\
&+144A^2B^4C^2+48A^2B^3C^3+144A^2B^2C^4+16A^2C^6\\
&+B^8+16B^6C^2+36B^4C^4+16B^2C^6+C^8.
\end{aligned}
\]
Because of homogeneity, set \(A+B+C=1\). Then \(x=A,y=B,z=C=1-x-y\), and the objective is precisely \(R=W/S^4\).

If any amplitude vanishes, the two-frequency binomial moment inequality yields \(R\le\binom84/16=35/8\). An interior rational test \((A,B,C)=(1000,1050,951)\), rescaled arbitrarily, gives \(R>46/5\). Consequently every global maximum is interior, and any maximum occurs where \(R>46/5\).

For completeness the global localization and uniqueness are certified using **exact integers**, not a floating-point sample. Define
\[
H(x,y)=5W(x,y)-46S(x,y)^4.
\]
The integer Taylor-box certificate in `artifacts/verify.py` subdivides the unit square into rational dyadic boxes. Every box intersecting the open simplex but not entirely contained in \(Q=[27/100,40/100]^2\) is either certified to have \(H<0\), or recursively subdivided. On a dyadic box centered at \((A/M,B/M)\) with radius \(1/M\), the program exactly expands \(M^8H((A+u)/M,(B+v)/M)\), and proves negativity via \(T_{00}+\sum_{(i,j)\ne(0,0)}|T_{ij}|<0\) for \(|u|,|v|\le1\). The finite recursion visits 253 boxes, with maximum depth six; the 14 boxes lying entirely in \(Q\) are allowed, and all cells on or beyond the simplex boundary are separately covered by the boundary inequality. Therefore every global maximizer lies in \(Q\).

Inside \(Q\), write \(W_i=\partial_iW\), \(S_i=\partial_iS\). The numerator of the Hessian \(\partial_{ij}R\), whose denominator is \(S^6>0\), is
\[
N_{ij}=W_{ij}S^2-4S(W_iS_j+W_jS_i+WS_{ij})+20WS_iS_j.
\]
The exact Taylor-box certificates prove \(N_{xx}<0\), \(N_{yy}<0\), and \(N_{xx}N_{yy}-N_{xy}^2>0\) on the *whole* rational square \(Q\). The first two assertions each require a single box; the determinant requires five boxes at depth at most one. The coefficient bounds are constructed using integer arithmetic with denominator \(100M\) and numerator \(27M+13(2i+1)+13u\), so every inequality is finite and exact. Hence the Hessian is negative definite throughout \(Q\), making \(R\) strictly concave there.

A global maximizer exists by compactness, is interior in \(Q\) by the strict \(46/5\) gap, and solves \(W_xS-4WS_x=W_yS-4WS_y=0\). Strict concavity makes the solution unique and proves the global sharp value. The forced phase condition gives exactly the displayed extremizers.

## Verification
Run `python artifacts/verify.py` with SymPy installed. It reconstructs the fourth convolution from three monomials; checks the complete expansion of \(F\); verifies global localization by a finite dyadic interval tree; computes the exact Hessian numerators and determinant; verifies rational negativity certificates over \(Q\); and numerically isolates the unique stationary point only after uniqueness has been proved algebraically. The normalized sharp constant and amplitudes are printed. An additional finite complex-coefficient check cross-compares Parseval with the direct convolution as a computational consistency check only. The infinite-domain proof uses the coefficientwise majorization and the exact rational certificates, not finite numerical experiments.

## Relationship to prior work
Krenedits studies classical signed idempotent Hardy–Littlewood trinomials at non-even exponents, whereas this result concerns arbitrary coefficient amplitudes at the eighth moment. De Dios Pont, Greenfeld, Ivanisvili and Madrid study additive energies of subsets of discrete cubes; their general energy bounds do not give this exact three-frequency weighted sharp constant. A published exact sixth-moment result on the same three-frequency support determines a different operator norm and a different amplitude profile; its third convolution does not determine the fourth. Other published exact eighth-moment results address the distinct supports \(\{0,1,2\}\) and \(\{0,1,4\}\), whose collision patterns and norms differ. Those three directly comparable full texts were inspected.

## Limitations
The classification does not treat other exponents, arbitrary three-frequency spectra or finite cyclic sampling, where wraparound produces additional additive collisions. The algebraic constant is specified by two rational polynomial stationarity equations on a rational isolating square; no radical formula is claimed. The explicit rational certificate requires SymPy for symbolic expansion but performs decisive sign comparisons using integer arithmetic. An older exact \(\Lambda(8)\) or Nikolskii-constant table under another parametrization could affect historical priority; no independent priority determination has been performed.

## References
1. Sándor Krenedits, *Three-term idempotent counterexamples in the Hardy–Littlewood majorant problem*, arXiv:1006.0409v1, first public 2010-06-02, https://arxiv.org/abs/1006.0409.
2. Jaume de Dios Pont, Rachel Greenfeld, Paata Ivanisvili and José Madrid, *Additive energies on discrete cubes*, arXiv:2112.09352v1, first public 2021-12-17, https://arxiv.org/abs/2112.09352.
3. *Sharp \(L^2\to L^6\) norm for the Hardy–Littlewood frequency triple*, published research record 2026/10/11/SCOPE-sharp-l-2-to-l-6-norm-for-the-hardy-littlewood-frequency-triple--753ad1798bf5.
4. *Sharp \(L^8/L^2\) norm for the consecutive three-frequency spectrum*, published research record 2026/10/11/SCOPE-sharp-l-8-l-2-norm-for-the-consecutive-three-frequency-spectrum--69c7d8c4e990.
5. *Sharp eighth-moment norm at the first fourth-order resonance*, published research record 2026/10/11/SCOPE-sharp-eighth-moment-norm-at-the-first-fourth-order-resonance--5598303b6ef1.
