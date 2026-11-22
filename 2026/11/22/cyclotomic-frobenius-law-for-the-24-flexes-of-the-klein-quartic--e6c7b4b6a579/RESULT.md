# Cyclotomic Frobenius law for the 24 flexes of the Klein quartic in every good odd characteristic

## Finding
For each prime \(p\ge5\), \(p\ne7\), let \(C_p\) denote the smooth plane quartic
\[
C_p:\quad X^3Y+Y^3Z+Z^3X=0\subset\mathbf P^2_{\mathbf F_p}.
\]
Its Hessian intersection \(W_p\subset C_p\) is reduced finite étale of degree \(24\), and consists of exactly the ordinary inflection (weight-one Weierstrass) points. The geometric points of \(W_p\) have the following arithmetic Frobenius cycles:

| Residue \(p\bmod7\) | Frobenius cycle type | \(\#W_p(\mathbf F_p)\) | Splitting degree |
|:--|:--|--:|--:|
| \(1\) | \(1^{24}\) | 24 | 1 |
| \(6\) | \(1^6 2^9\) | 6 | 2 |
| \(2,4\) | \(1^3 3^7\) | 3 | 3 |
| \(3,5\) | \(1^3 3^1 6^3\) | 3 | 6 |

In the row order above, the finite-scheme Hasse–Weil zeta functions are
\[
\begin{aligned}
Z(W_p,T)\in\{&(1-T)^{-24},\;(1-T)^{-6}(1-T^2)^{-9},\\
&(1-T)^{-3}(1-T^3)^{-7},\;(1-T)^{-3}(1-T^3)^{-1}(1-T^6)^{-3}\}.
\end{aligned}
\]
Equivalently, for every integer \(n\ge1\),
\[
\#W_p(\mathbf F_{p^n})=3+3\mathbf1_{p^n\equiv\pm1\;(\bmod7)}+18\mathbf1_{p^n\equiv1\;(\bmod7)}.
\]
The common splitting field of all \(24\) geometric flexes on the same fixed quartic over \(\mathbf Q\) is precisely \(\mathbf Q(\zeta_7)\). The contribution is the **uniform reduction and Frobenius classification in every permitted odd characteristic**; the characteristic-five row was previously computed separately and is included for completeness, not claimed anew.

## Assumptions and scope
The plane model and its projective coordinates are fixed. Let \(\zeta=\zeta_7\), a primitive seventh root of unity, and \(K=\mathbf Q(\zeta)\). For \(p\ge5\) except \(7\), the plane model is nonsingular: the partials are \(3X^2Y+Z^3\), \(X^3+3Y^2Z\), and \(Y^3+3Z^2X\). If a coordinate is zero, all three partials cannot vanish; if none is zero, multiplying the three gradient relations forces \(28(XYZ)^3=0\), impossible in the stated characteristics.

For a smooth plane quartic over these characteristics, the Hessian intersects the curve in its flex divisor with degree \(24\). In this proof its reducedness is shown by explicit integral coordinates and Bézout rather than assumed from general characteristic-zero theory. We count a flex point, not its tangent line or the full curve's rational points. The \(\mathbf F_p\)-form is not varied by an arithmetic twist.

## Proof
**1. Integral Hessian and affine eliminant.** Set \(F=X^3Y+Y^3Z+Z^3X\), and define the integral sextic
\[
H=X^5Z-5X^2Y^2Z^2+XY^5+YZ^5.
\]
Direct differentiation gives \(\det(\operatorname{Hess}F)=-54H\). Since \(p\ge5\), \(H=0\) is the Hessian locus of \(F\) up to a nonzero scalar. In the chart \(Z=1\) write
\[
f=x^3y+y^3+x,\qquad h=x^5-5x^2y^2+xy^5+y.
\]
Let
\[
\begin{aligned}
A(x)&=x^3+x^2-2x-1,\\
B(x)&=x^6-5x^5+11x^4-13x^3+9x^2-3x+1,\\
C(x)&=x^6+2x^5+4x^4+x^3+2x^2-3x+1,\\
D(x)&=x^6+2x^5+4x^4+8x^3+9x^2+4x+1.
\end{aligned}
\]
An exact integer resultant calculation yields
\[
\operatorname{Res}_y(f,h)=-xA(x)B(x)C(x)D(x).
\]
All four nontrivial factors are irreducible over \(\mathbf Q\), with degrees \(3,6,6,6\). These identities are reproduced by the included checker.

**2. Explicit full cyclotomic coordinates.** In \(\mathcal O_K=\mathbf Z[\zeta]\), four projective flexes with \(Z=1\) have affine \((x,y)\) coordinates:
\[
\begin{array}{c|l|l}
\text{factor}& x & y\\\hline
A & \zeta^3+\zeta^4 & \zeta^2+\zeta^3+\zeta^4+\zeta^5\\
B & 1+\zeta^4 & \zeta+\zeta^2+\zeta^4+\zeta^5\\
C & \zeta^5+\zeta^4 & 1+\zeta+\zeta^2+\zeta^3\\
D & \zeta^5+\zeta^3 & 1+\zeta^2+\zeta^3+\zeta^5
\end{array}
\]
Reduce \(f(x,y)\) and \(h(x,y)\) modulo \(1+\zeta+\cdots+\zeta^6\): both remainders vanish for each row. Eliminating \(\zeta\) from \(\Phi_7(\zeta)=0\) and the displayed \(x\) yields the factor \(A^2\) for the first row and \(B,C,D\) respectively for the other rows. In particular the Galois conjugates give \(3+6+6+6=21\) distinct finite points with nonzero \(x\). The three coordinate vertices also belong to \(F=H=0\): \([1:0:0]\), \([0:1:0]\), \([0:0:1]\), of which the last is the \(x=0\) point in this chart.

**3. Uniform good reduction and completeness.** The discriminants of \(A,B,C,D\) are respectively \(7^2,-7^5,-2^6 7^5,-2^6 7^5\); the pairwise resultants among the five factors \(x,A,B,C,D\) have no prime divisors except \(2\) and \(7\). Thus, for every prime \(p\ge5\), \(p\ne7\), all \(22\) affine \(x\)-roots remain simple and pairwise disjoint after reduction. All displayed coordinates are algebraic integers, so their reduction modulo primes above \(p\) still satisfies \(f=h=0\). There are \(21\) nonzero-\(x\) flex points, plus the three coordinate vertices, giving \(24\) distinct geometric intersection points. Bézout's theorem gives total intersection number \(4\cdot6=24\), since the nonzero affine resultant proves that the two curves have no common component, so each point has local intersection multiplicity exactly one and there are no others. Every point is therefore an ordinary flex, and \(W_p\) is reduced and finite étale over \(\mathbf F_p\).

**4. Frobenius cycles.** Since \(p\ne7\), Frobenius in \(K/\mathbf Q\) sends \(\zeta\mapsto\zeta^p\) modulo any prime above \(p\). The three coordinate vertices are fixed. The cubic row has a three-element orbit on which \(\zeta\mapsto\zeta^{-1}\) acts trivially, while each sextic row has a free six-element orbit under \((\mathbf Z/7\mathbf Z)^\times\). Consequently the cubic contributes \(3\) fixed points if \(p\equiv\pm1\pmod7\), and otherwise one three-cycle. Each sextic contributes \(6/d\) Frobenius cycles of length \(d=\operatorname{ord}_7(p)\). Combining these contributions proves all four cases and the extension-count/zeta formulas. A sextic row has a full degree-six orbit over \(\mathbf Q\), proving that no proper subfield of \(K\) contains all \(24\) flexes over \(\mathbf Q\).

## Verification
Execute `python3 VERIFY.py` after installing the stated `requirements.txt`. The checker recomputes the exact integer Hessian, affine eliminant, all four cyclotomic point identities, four primitive minimal polynomials and the separation certificates (discriminants and pairwise resultants), as well as all six Galois substitution cycle profiles. It ends in `KLEIN_FLEX_CYCLOTOMIC_CERTIFIED_OK`. These finite symbolic calculations establish the hypotheses of a proof valid for infinitely many prime characteristics; sampling finite fields alone would not justify the theorem.

## Relationship to prior work
Elkies's *The Klein Quartic in Number Theory* (1998, §2, pp. 64–65) gives the unique 24-point orbit of ordinary flexes for the complex curve, and the order-168 automorphism action; it does not tabulate the four Frobenius profiles in every good odd prime. Poonen–Schaefer–Stoll (first arXiv version 2005-08-10, §11.1) describe the 24 flexes and their eight Galois-stable tangent triangles, but do not give the present uniform finite-characteristic classification. A prior characteristic-five calculation proves the \(p=5\) flex cycle profile \(1^3 3^1 6^3\), which is included here only as a previously known row. A different previously published computation classifies all 28 bitangent-line Frobenius cycles over good odd primes; those are different finite schemes, whose arithmetic behavior does not itself determine the 24 flex coordinates or their Frobenius cycles. The additional result is the integral certificate that these exact 24 flexes stay distinct for all permitted primes, coupled to the four-row orbit classification.

## Limitations
No assertion concerns the full zeta function or Jacobian of \(C_p\), its other arithmetic twists, characteristic two or three, or the singular reduction in characteristic seven. The proof uses exact symbolic verification with SymPy, not independent external validation. Historical priority is provisional: classical orbit theory permits the arithmetic determination in principle, and unindexed tables may record equivalent formulas. The characteristic-five case is previously known and contributes no new novelty.

## References
1. N. D. Elkies, *The Klein Quartic in Number Theory*, MSRI Publications 35 (1998), §2, pp. 64–65. https://library.slmath.org/books/Book35/files/elkies.pdf
2. B. Poonen, E. F. Schaefer, M. Stoll, *Twists of X(7) and primitive solutions to x²+y³=z⁷*, original arXiv submission 2005-08-10, §11.1. https://arxiv.org/abs/math/0508174
3. *Frobenius splitting of the characteristic-five Klein quartic's flex triangles*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-frobenius-splitting-of-the-characteristic-five-klein-quartic-s-f--07295989c49b
4. *Cyclotomic Frobenius classification of the Klein quartic's bitangents in odd characteristic*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-cyclotomic-frobenius-classification-of-the-klein-quartic-bitange--332d2be7d5dd
5. G. Egan, *Klein's Quartic Equation*, 2006, classical flex geometry. https://www.gregegan.net/SCIENCE/KleinQuartic/KleinQuarticEq.html
