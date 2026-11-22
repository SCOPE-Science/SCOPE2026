# Three radical packets and the complete minimum-height section census of Brahmagupta's elliptic curve

## Finding

Let \(t\) be transcendental over \(\overline{\mathbb Q}\), and consider the elliptic curve
\[
 E:\quad Y^2=X^3+4t^4X+4t^2
 \qquad\text{over }\overline{\mathbb Q}(t).
\]
The geometric Mordell–Weil group is torsion-free of rank six, with minimum positive Néron–Tate height \(4/3\). Its **entire set of 54 sections of minimum positive height** has the following explicit arithmetic description. This concrete radical classification, rather than the general rank-six or 54-vector theorem, is the new assertion.

Set
\[
\begin{array}{c|c}
\tau & W_\tau \\
\hline
1/32&4096\\
(-1+\sqrt2)/16&-17408-12288\sqrt2\\
(-1-\sqrt2)/16&-17408+12288\sqrt2
\end{array}.
\]
For each of these three rows, independently choose **every** one of the eight distinct complex roots \(b\) of \(b^8=W_\tau\), then define
\[
 a=\tau b^4,\quad e=\frac{b^3}{4},\quad
 d=\frac{3ab^2-b^6/16}{4}.
\]
The corresponding point is
\[
 S_{\tau,b}=\bigl(bt+at^2,\;2t+et^2+dt^3\bigr).
\]
In addition take the three points
\[
 S_{a,0}=(at^2,2t),\qquad a\in\{0,2i,-2i\}.
\]
These are **27 distinct points**. Together with their distinct inverses \((X,-Y)\), they are **exactly all 54 minimum-height points** of \(E(\overline{\mathbb Q}(t))\).

Moreover, the field generated over \(\mathbb Q\) by the coefficients of all these 54 sections is a finite **Galois extension with a \(2\)-group Galois group**. In particular, the arithmetic Galois action on all geometric minimum-height sections is solvable and has no odd prime factor in its group order. More explicitly, all coefficients lie in the splitting field over \(\mathbb Q\) of
\[
 (B^8-4096)\bigl(B^{16}+34816B^8+1048576\bigr),
\]
which also contains \(\sqrt2\) and \(i\); adding eighth roots of unity suffices to describe its splitting field. This is a special arithmetic feature of this coefficient family; the general \(E_6^*\) minimum-section theorem has generic Galois group \(W(E_6)\) of order \(51840\).

## Assumptions and scope

The base field has characteristic zero. The transcendental parameter \(t\) is not assigned any numerical value. The term *section* means an element of the geometric Mordell–Weil group \(E(\overline{\mathbb Q}(t))\) of the relatively minimal elliptic surface over \(\mathbb P^1_t\). Height is the standard Shioda height pairing normalized so that the positive minimum of \(E_6^*\) equals \(4/3\). All points in the displayed list are defined over finite algebraic extensions of \(\mathbb Q(t)\), not necessarily over \(\mathbb Q(t)\) itself.

The polynomial model and the section \((0,2t)\) come from Choudhry, *An ancient diophantine problem of Brahmagupta*, arXiv:2611.19315v1, first public on 2026-11-14. Choudhry works over \(\mathbb Q(t)\) and obtains rational families of solutions. The novel component here is the special arithmetic factorization and complete **geometric** minimum-section coefficient spectrum.

## Proof

**1. Singular fibers and height.** For this Weierstrass model,
\[
 \Delta=-256t^4(16t^8+27),\qquad c_4=-192t^4.
\]
At \(t=0\), the model is minimal with \(\operatorname{ord}_0\Delta=4\), \(\operatorname{ord}_0c_4=4\), and \(\operatorname{ord}_0c_6=2\), giving a Kodaira \(IV\) fiber. The eight distinct roots of \(16t^8+27\) each have type \(I_1\), since \(c_4\) is nonzero there. At infinity set \(u=1/t\), \(x'=u^2X\), \(y'=u^3Y\); then \(y'^2=x'^3+4x'+4u^4\), whose discriminant at \(u=0\) is nonzero. Consequently the minimal elliptic surface has \(\chi(\mathcal O)=1\), is rational, and has geometric Picard number ten. Shioda–Tate gives
\[
 \operatorname{rank}E(\overline{\mathbb Q}(t))
 =10-2-(3-1)=6.
\]
The Shioda height formula for any nonzero section \(S\) here is
\[
 \langle S,S\rangle=2+2(S\cdot O)-\operatorname{contr}_{0}(S),
\]
with \(\operatorname{contr}_{0}(S)=0\) on the identity component of the type \(IV\) fiber and \(2/3\) on either nonidentity component. At the type \(I_1\) fibers the contribution is zero. As \(S\cdot O\ge0\), every section of positive height has height at least \(4/3\); in fact no nonzero torsion section can have height zero. The section \((0,2t)\) is disjoint from \(O\) and specializes to the singular point \((0,0)\) on the type \(IV\) fiber, meeting a nonidentity component after resolution. Its height is \(4/3\), so the positive minimum is attained. All minimum-height sections are precisely those disjoint from \(O\) and meeting a nonidentity component at the type \(IV\) fiber.

**2. Polynomial restriction.** Since \(\chi=1\) and \(S\cdot O=0\), the global Weierstrass coordinate bounds are \(\deg_t X\le2\), \(\deg_tY\le3\). At the type \(IV\) fiber, a minimum-height section reduces to its singular point, so \(X(0)=Y(0)=0\). The original Weierstrass equation forces \(Y\)'s linear coefficient to equal \(\pm2\); choose the positive sign first. Therefore every candidate is necessarily
\[
 X=bt+at^2,\qquad Y=2t+et^2+dt^3.
\]
Conversely every polynomial point of this form is disjoint from \(O\) and meets a nonidentity component, hence has height \(4/3\).

**3. Exact elimination.** Comparing the coefficients of \(t^3,t^4,t^5,t^6\) after inserting the candidate into the curve gives, respectively,
\[
\begin{aligned}
4e-b^3&=0,\\
e^2+4d-3ab^2&=0,\\
2ed-3a^2b-4b&=0,\\
d^2-a^3-4a&=0.
\end{aligned}
\]
The first two yield \(e=b^3/4\) and \(d=(3ab^2-b^6/16)/4\). If \(b=0\), the remaining equation is \(a(a^2+4)=0\), giving exactly the three asserted sections.

If \(b\ne0\), the last two equations are respectively equivalent to
\[
\begin{aligned}
384a^2-48ab^4+b^8+512&=0,\\
-4096a^3+2304a^2b^4-96ab^8-16384a+b^{12}&=0.
\end{aligned}
\]
Putting \(\tau=a/b^4\) and \(W=b^8\) converts these to
\[
 W(384\tau^2-48\tau+1)=-512,
\quad W(-4096\tau^3+2304\tau^2-96\tau+1)=16384\tau.
\]
Eliminating \(W\) reduces exactly to
\[
 (32\tau-1)(256\tau^2+32\tau-1)=0.
\]
The three distinct \(\tau\)'s and their corresponding nonzero \(W\)'s are precisely the rows in the displayed table. Each row has eight distinct eighth roots \(b\), and each solution reconstructs a unique valid point. Therefore there are \(3+3\cdot8=27\) candidate points with positive \(Y\)-coefficient, and their negatives give 54 in total. The exhaustion argument in Step 2 proves there are no others.

For an independent exact elimination certificate, put \(z=b^2\). The resultant of the two last equations as polynomials in \(a\) is
\[
 -2097152(z^4-4096)(z^8+34816z^4+1048576).
\]
The displayed degree-twelve polynomial is squarefree and has no zero root, confirming precisely twelve nonzero \(z\)'s and hence twenty-four nonzero \(b\)'s.

**4. Arithmetic Galois group.** Let \(L\) be the splitting field over \(\mathbb Q\) of the displayed degree-twenty-four polynomial in \(B\). It contains roots of \(B^8-4096\), hence contains a primitive eighth root of unity, \(\sqrt2\), and \(i\). The other degree-sixteen factor splits into \((B^8-W_+)(B^8-W_-)\) over \(\mathbb Q(\sqrt2)\), with \(W_\pm=-17408\pm12288\sqrt2\). Hence over \(\mathbb Q(\zeta_8)\) the field \(L\) is generated by at most three eighth roots. Kummer automorphisms send each root to an eighth-root-of-unity multiple of itself, making its relative Galois group a \(2\)-group. Since \(\operatorname{Gal}(\mathbb Q(\zeta_8)/\mathbb Q)\) is also a \(2\)-group, \(\operatorname{Gal}(L/\mathbb Q)\) is a \(2\)-group. Every displayed section coefficient is in \(L\). Conversely, every root \(b\) of the degree-twenty-four polynomial occurs as the coefficient of \(t\) in the \(X\)-coordinate of one of the displayed sections, so the field generated by **all** their coefficients contains \(L\). Thus the coefficient field equals this normal splitting field, and the claim follows without asserting its exact group order.

## Verification

The standalone, standard-library-plus-SymPy program `verify.py` checks the discriminant and reduction calculations, Choudhry's starting section and its double, all four coefficient identities, both normalized elimination equations, all three radical coefficient branches and nonvanishing, the resultant factorization, and squarefreeness. Run it from a Python 3.10+ environment with SymPy 1.12+ as `python verify.py`. The script verifies exact algebra, not general geometric theorems; the rank, heights, and exhaustive section argument use the standard cited elliptic-surface results and the proof above. No numerical samples are used to infer the infinite classification.

## Relationship to prior work

Choudhry (2026) introduced exactly this elliptic model for rational families in Brahmagupta's square problem, proved that \((0,2t)\) has infinite order, and computed its multiples; no complete radical minimum-section spectrum was found in the source's Section 2.1. Shioda (1995, §§4–5) establishes that any nondegenerate rational elliptic surface with one type \(IV\) reducible fiber has an \(E_6^*\) Mordell–Weil lattice and 54 minimum sections, with generic arithmetic monodromy \(W(E_6)\), and gives a construction of 27 geometric sections for general coefficients. The **rank, abstract 54-count and general construction are not new here**. The result not supplied by that general theorem is the concrete three-radical-packet factorization, fully explicit section formulas, and resulting special \(2\)-group splitting behavior for Choudhry's coefficients. This comparison does not rule out an earlier specialization or equivalent expression in less accessible sources.

## Limitations

This is a geometric classification over \(\overline{\mathbb Q}(t)\), not a computation of the arithmetic Mordell–Weil rank over \(\mathbb Q(t)\) and not a classification of all sections of arbitrary height. The arithmetic Galois group is shown to be a \(2\)-group, but its exact order and orbit structure are not determined. The result does not resolve the original Brahmagupta Diophantine problem. Specializing \(t\) can change the section behavior and is not covered. An independently reviewed novelty assessment remains to be conducted.

## References

1. A. Choudhry, *An ancient diophantine problem of Brahmagupta*, arXiv:2611.19315v1 (first public 2026-11-14), https://arxiv.org/abs/2611.19315, especially §2.1, equation (2.4).
2. T. Shioda, *Weierstrass Transformations and Cubic Surfaces*, Commentarii Mathematici Universitatis Sancti Pauli 44 (1995), §§4–5, https://rikkyo.repo.nii.ac.jp/record/9956/files/AA00610867_44-01_06.pdf.
3. T. Shioda, *On the Mordell-Weil lattices*, Commentarii Mathematici Universitatis Sancti Pauli 39 (1990): Shioda height pairing and lattice formula (cited via Shioda 1995).
