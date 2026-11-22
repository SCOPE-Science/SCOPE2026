# Cyclotomic Frobenius splitting of the twenty-four Klein-quartic flexes

## Finding
Consider the literal smooth plane Klein quartic
\[
C:\quad X^3Y+Y^3Z+Z^3X=0
\]
over a finite field \(\mathbb F_q\), with \(q=p^n\), \(p\ge5\), \(p\ne7\), and \(n\ge1\). Let \(W\) be the *reduced ordinary-inflection scheme*: its geometric points are those where the tangent line has intersection multiplicity three with \(C\). Then \(W\) has exactly \(24\) geometric points, all ordinary flexes; it is finite étale over \(\mathbb F_q\), and the full Frobenius cycle structure is

| \(q\pmod7\) | Frobenius cycle decomposition on \(W\) | \(\#W(\mathbb F_q)\) | \(Z(W,T)\) |
|---|---|---:|---|
| \(1\) | \(1^{24}\) | 24 | \((1-T)^{-24}\) |
| \(6\) | \(1^6 2^9\) | 6 | \((1-T)^{-6}(1-T^2)^{-9}\) |
| \(2,4\) | \(1^3 3^7\) | 3 | \((1-T)^{-3}(1-T^3)^{-7}\) |
| \(3,5\) | \(1^3 3^1 6^3\) | 3 | \((1-T)^{-3}(1-T^3)^{-1}(1-T^6)^{-3}\) |

In particular all flexes split over \(\mathbb F_{q^{\operatorname{ord}_7(q)}}\), and the common splitting field has exactly this degree. The three coordinate vertices are rational in every characteristic of this scope. Over the localization \(R=\mathbb Z[1/42]\), the entire flex-support scheme has a cyclotomic decomposition
\[
W_R\simeq \operatorname{Spec}(R)^{\sqcup3}\ \sqcup\ \operatorname{Spec}\bigl(R\otimes_{\mathbb Z}\mathcal O_{K^+}\bigr)\ \sqcup\ \operatorname{Spec}\bigl(R\otimes_{\mathbb Z}\mathcal O_K\bigr)^{\sqcup3},
\]
where \(K=\mathbb Q(\zeta_7)\) and \(K^+=\mathbb Q(\zeta_7+\zeta_7^{-1})\). The claim concerns this intrinsic finite flex configuration, *not* the zeta function of the whole curve or its bitangent lines.

## Assumptions and scope
The displayed homogeneous equation and its rational projective coordinates are fixed. We exclude characteristic two, three, and seven; no statement is made about twists, which need not have the same arithmetic flex splitting. The Hessian criterion for an ordinary flex applies here, and the proof establishes reducedness; a characteristic-dependent collision does not get silently counted as separate geometric flexes. For the integral scheme, all assertions are made after inverting \(2,3,7\). Its coordinate-projection decomposition is a statement over that localized base. In the factorization below the polynomials are written as integer polynomials in the affine coordinate \(x=X/Z\).

## Proof
**1. Smoothness and the Hessian.** Put \(F=X^3Y+Y^3Z+Z^3X\). Its partial derivatives are \(3X^2Y+Z^3\), \(X^3+3Y^2Z\), \(Y^3+3Z^2X\). At a singular point having a zero coordinate the gradient conditions force all three coordinates to be zero, impossible. At a point with no zero coordinates, multiplication of the three gradient equations forces \(28(XYZ)^3=0\). Thus \(C\) is smooth for the stated primes. The Hessian is exactly
\[
\det(\operatorname{Hess}F)=-54H,\quad
H=X^5Z-5X^2Y^2Z^2+XY^5+YZ^5.
\]
Its intersection with \(C\) has degree \(4\cdot6=24\) by Bézout. The three coordinate vertices belong to it; the two vertices on \(Z=0\) are transverse points of the intersection, and the third, \([0:0:1]\), has affine local equations starting with \((x,y)\), so it is also transverse.

**2. Exact elimination of all remaining flexes.** In \(Z=1\), write
\[
f=y^3+x^3y+x,\qquad h=x^5-5x^2y^2+xy^5+y.
\]
An exact integer resultant yields
\[
\operatorname{Res}_y(f,h)=-x\,P_3(x)P_{6,1}(x)P_{6,2}(x)P_{6,3}(x),
\]
with
\[
\begin{aligned}
P_3(x)&=x^3+x^2-2x-1,\\
P_{6,1}(x)&=x^6-5x^5+11x^4-13x^3+9x^2-3x+1,\\
P_{6,2}(x)&=x^6+2x^5+4x^4+x^3+2x^2-3x+1,\\
P_{6,3}(x)&=x^6+2x^5+4x^4+8x^3+9x^2+4x+1.
\end{aligned}
\]
The product \(R(x)=xP_3P_{6,1}P_{6,2}P_{6,3}\) has absolute discriminant
\[
|\operatorname{disc}(R)|=2^{42}7^{77}.
\]
The last *linear* subresultant is
\[
D(x)y+N(x),\quad D(x)=x^{14}+50x^7+1,\quad N(x)=2x^{12}+38x^5.
\]
For each of the four factors \(P_3,P_{6,i}\), the absolute resultant with \(D\) has only prime factors \(2\) and \(7\): respectively \(2^6 7^4\), and \(2^{12}7^8\) for each sextic. Thus over any admissible residue characteristic the denominator is invertible at every root, and every root \(x\) determines a unique affine intersection point \((x,-N(x)/D(x))\). Since \(R\) is squarefree, this gives exactly \(22\) distinct affine intersection points. Together with the two distinct points at infinity they exhaust Bézout's \(24\) intersection points, all of multiplicity one. Hence every flex is ordinary and the scheme is reduced and finite étale, uniformly on the stated base.

**3. Cyclotomic field identification.** Let \(\zeta=\zeta_7\) and \(\Phi_7(t)=1+t+\cdots+t^6\). Direct substitutions in \(\mathbb Z[t]/\Phi_7(t)\) give
\[
\begin{array}{rcl}
P_3(\zeta^3+\zeta^4)&=&0,\\
P_{6,1}(1+\zeta^4)&=&0,\\
P_{6,2}(\zeta^4+\zeta^5)&=&0,\\
P_{6,3}(\zeta^3+\zeta^5)&=&0.
\end{array}
\]
The cubic generator \(\zeta^3+\zeta^4\) has degree three and generates the maximal real subfield \(K^+\). Each sextic generator has degree six and generates \(K\): in each case its polynomial is separable and irreducible in characteristic zero, of degree six, and its value lies in \(K\). Their respective polynomial discriminants are \(7^2\), \(-7^5\), \(-2^6 7^5\), and \(-2^6 7^5\). The index of each generated order in the maximal order is therefore supported only at \(2\) and \(7\), so after inverting \(2,7\), these become precisely the maximal cyclotomic orders. Each factor defines an étale component over \(R\), and the unique \(y\) formula identifies the affine flex scheme with these four factors and the affine origin. The two rational infinity points provide the remaining sections, giving the displayed decomposition.

**4. Frobenius and zeta function.** For a residue field \(\mathbb F_q\), cyclotomic arithmetic Frobenius sends \(\zeta\) to \(\zeta^q\). On each of the three copies of \(K\), multiplication by \(q\) in \((\mathbb Z/7\mathbb Z)^\times\) acts regularly on six embeddings. On the single copy of \(K^+\), it acts on the three cosets modulo \(\{\pm1\}\). The three rational sections are fixed. The orders of \(q\) in the sextic group and in its cubic quotient give the four displayed cycle partitions. The finite-étale zeta identity \(Z(W,T)=\prod_{\mathcal O}(1-T^{|\mathcal O|})^{-1}\) then gives all four rational functions, with the same law applying to every extension \(\mathbb F_{p^n}\). Because the scheme contains sextic regular Galois orbits, the common splitting extension degree is exactly \(\operatorname{ord}_7(q)\), not merely a divisor of it.

## Verification
The accompanying standalone `VERIFY.py` uses exact SymPy rational/integer polynomial arithmetic and modular polynomial factorization. It verifies the Hessian determinant, complete resultant factorization, squarefree discriminant, and the four primitive-seventh-root equations. It checks the predicted factor-degree cycle types and separately enumerates rational curve-Hessian intersections over the prime fields of characteristics \(5,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101\). It prints `KLEIN_24_FLEX_CYCLOTOMIC_FROBENIUS_VERIFIED`. The subresultant and resultant-with-denominator identities were independently evaluated in exact polynomial arithmetic; the universal arithmetic assertion follows from these integer identities and cyclotomic étale descent, not the finite set of sample fields. Run `python3 VERIFY.py` with Python 3 and SymPy 1.14 or compatible version.

## Relationship to prior work
Elkies' *The Klein Quartic in Number Theory* establishes the classical orbit of 24 inflection/Weierstrass points and their geometric interpretation. Poonen–Schaefer–Stoll, *Twists of X(7)* (2005), use the eight classical Galois-stable flex triples in a different arithmetic problem. Dimca–Ilardi–Pokora–Sticlaru (initial public preprint 2023-01-03), in their study of free-curve arrangements, use the inflectional tangent geometry of the Klein curve. These precedents do not, in the material inspected, state the uniform good-characteristic decomposition into three rational points, one real-cyclotomic cubic, and three cyclotomic sextics or the four explicit prime-power Frobenius spectra. A prior characteristic-five calculation already gives the \(q=5\) cycle type \(1^3 3^1 6^3\) and the eight triangle orbits; that special case is not claimed as new. A previously established uniform modulo-seven law for the *28 bitangents* is also credited; bitangents and flex points are distinct configurations and their Frobenius representations have different dimensions and cycle decompositions.

## Limitations
The theorem concerns a specific plane model of the Klein quartic, not every twist, and excludes bad characteristics. It is not a new classification of the abstract 24 geometric flexes or the 28 bitangents, and gives no new complete curve zeta function. The ingredients are classical geometry and cyclotomic algebra; a historical-priority risk remains that an equivalent representation of the Galois action is implicitly available in an older unpublished table or in deeper sections of the twist literature. The cited comparison is not a proof of novelty. No independent mathematical audit has been performed.

## References
1. N. D. Elkies, *The Klein Quartic in Number Theory*, in *The Eightfold Way*, MSRI Publications 35 (1999), pp. 51–102, especially its 24-point proposition. https://library.slmath.org/books/Book35/files/elkies.pdf
2. B. Poonen, E. F. Schaefer, M. Stoll, *Twists of X(7) and primitive solutions to x²+y³=z⁷*, first submitted 2005-08-10, Sections 11.1–11.2. https://arxiv.org/abs/math/0508174
3. A. Dimca, G. Ilardi, P. Pokora, G. Sticlaru, *Construction of Free Curves by Adding Lines to a Given Curve*, first submitted 2023-01-03. https://arxiv.org/abs/2301.01117
4. *Frobenius splitting of the characteristic-five Klein quartic's flex triangles* (previous arithmetic calculation of the characteristic-five specialization), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-frobenius-splitting-of-the-characteristic-five-klein-quartic-s-f--07295989c49b
5. *Cyclotomic Frobenius classification of the Klein quartic bitangents in odd characteristic* (distinct 28-line configuration), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-cyclotomic-frobenius-classification-of-the-klein-quartic-bitange--332d2be7d5dd
