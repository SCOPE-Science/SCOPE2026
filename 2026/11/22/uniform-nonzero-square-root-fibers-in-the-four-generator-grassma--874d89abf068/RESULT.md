# Uniform nonzero square-root fibers in the four-generator Grassmann algebra

## Finding
Let \(E=\bigwedge_{\mathbb F_q}V\), where \(\dim V=4\), and let \(J=\bigoplus_{i=1}^4\bigwedge^iV\) be its augmentation ideal. For a prescribed target \(b\in E\), write \(b=b_0+b_+\) with \(b_0\in\mathbb F_q\) and \(b_+\in J\). Put \(N_q(b)=\#\{x\in E:x^2=b\}\).

**Theorem (odd characteristic).** If \(q\) is odd, the complete prescribed-target census is
\[
N_q(b)=\begin{cases}
2,&b_0\in(\mathbb F_q^\times)^2,\\
q^{12}+q^{10}-q^7,&b=0,\\
q^7(q^3-1),&b_0=0,\ b_+\in J^3\setminus\{0\},\\
0,&\text{otherwise}.
\end{cases}
\]
Here \(J^3=\bigwedge^3V\oplus\bigwedge^4V\), of vector-space dimension five. Thus **every nonzero value of the square map on the radical has exactly the same number of square roots**, despite the distinct rank-two and rank-four strata of the underlying bivectors. There are exactly
\[
q^5+\frac{q-1}{2}\,q^{15}
\]
distinct squares in \(E\). In particular, the restricted square map \(J\to J^3\) is surjective with one exceptional (zero) fiber and a constant common size on every nonzero fiber.

**Characteristic-two boundary.** For every even prime power \(q\), all \(x=a+y\), \(y\in J\), satisfy \(x^2=a^2\). Hence \(N_q(b)=q^{15}\) if \(b\) is scalar and \(N_q(b)=0\) otherwise.

## Assumptions and scope
The product is the *ordinary associative* product of the exterior algebra, i.e. \(v\wedge v=0\) and \(v\wedge w=-w\wedge v\). The field is any finite field; \(q\) denotes its order, not necessarily a prime. The theorem counts labeled algebra elements and exact prescribed outputs, not isomorphism classes, multiplication-operator ranks, or merely the total number of square-zero elements. The superscript on \(J^3\) denotes the third ideal power, not a third exterior power of \(J\).

## Proof
**1. Remove the scalar fiber.** Every \(x=a+y\) has unique \(a\in\mathbb F_q\), \(y\in J\). As shown below, \(y^3=0\) for every \(y\in J\). If \(q\) is odd, a target with nonzero scalar \(b_0\) has roots only if \(b_0=a^2\) for some nonzero \(a\). For each of its exactly two possible scalars \(a\), the radical part of the root is uniquely determined by
\[
y=\frac{b_+}{2a}-\frac{b_+^2}{8a^3}.
\]
Indeed, \(b_+^3=0\) and direct multiplication gives \((a+y)^2=b_0+b_+\); conversely the same truncated binomial expression is forced. If \(b_0\) is a nonsquare there are no roots. If \(b_0=0\), any root has \(a=0\), reducing the problem to \(J\).

**2. Reduce radical squaring to two wedge maps.** Every radical element is uniquely \(y=v+w+z+t\), with \(v\in V\), \(w\in\bigwedge^2V\), \(z\in\bigwedge^3V\), \(t\in\bigwedge^4V\). Graded anticommutation and the four-dimensional degree cutoff yield
\[
y^2=2v\wedge w+w\wedge w\in\bigwedge^3V\oplus\bigwedge^4V.
\]
The coordinates \(z,t\) are free, contributing \(q^5\) roots for each solution \((v,w)\). Multiplying \(y\) by \(y^2\) gives zero: the only putative term of degree at most four is \(v\wedge v\wedge w\), which vanishes. Hence \(y^3=0\), as used in Step 1.

Fix \(u\in\bigwedge^3V\) and \(s\in\bigwedge^4V\). We count pairs \((v,w)\) solving
\[
2v\wedge w=u,\qquad w\wedge w=s.
\]

**3. Nonzero top-degree component.** In odd characteristic \(w\wedge w=2\operatorname{Pf}(w)\Omega\), in any oriented basis with top generator \(\Omega\). A two-form \(w\) has alternating rank \(0\), \(2\), or \(4\); its square is nonzero precisely when the rank is four. The number of rank-four two-forms is
\[
R_4(q)=q^2(q-1)(q^3-1).
\]
This follows, for instance, by the \(\operatorname{GL}_4(q)\)-orbit of a nondegenerate alternating form, whose stabilizer is \(\operatorname{Sp}_4(q)\). Multiplying a basis vector by an arbitrary nonzero scalar scales the Pfaffian by that scalar, so each fixed nonzero value \(s\) occurs for exactly \(R_4(q)/(q-1)=q^2(q^3-1)\) such two-forms. For each of them, \(v\mapsto2v\wedge w\) is an isomorphism \(V\to\bigwedge^3V\). Thus *every* \(u\), including zero, gives exactly \(q^2(q^3-1)\) pairs when \(s\ne0\).

**4. Zero top-degree component and nonzero cubic component.** If \(s=0\), either \(w=0\) or \(w\) is a nonzero decomposable two-form. When \(u\ne0\), \(w=0\) is impossible. Every nonzero cubic \(u\in\bigwedge^3V\) determines a unique three-dimensional support hyperplane \(H\subset V\). For decomposable nonzero \(w\) with its support plane \(L\), the equation \(v\wedge w=u/2\) is solvable exactly when \(L\subset H\). There are \({3\brack2}_q=q^2+q+1\) two-planes in \(H\), and \(q-1\) nonzero scalar multiples of their wedge generators. Thus there are \((q-1)(q^2+q+1)=q^3-1\) eligible choices of \(w\). For each, the map \(V\to\bigwedge^3V\), \(v\mapsto v\wedge w\), has rank two and a two-dimensional kernel, giving \(q^2\) solutions \(v\). Consequently the number is again \(q^2(q^3-1)\).

**5. Zero target.** If \(u=s=0\), the choice \(w=0\) allows all \(q^4\) vectors \(v\). Nonzero rank-two two-forms are counted by
\[
R_2(q)=(q-1){4\brack2}_q=(q^2+1)(q^3-1).
\]
Every such \(w\) allows \(q^2\) vectors \(v\) in its support plane, so the number of pairs is
\[
q^4+q^2R_2(q)=q^7+q^5-q^2.
\]
Multiplication by the free \(q^5\) coordinates \((z,t)\) gives \(q^{12}+q^{10}-q^7\), while every nonzero radical target has \(q^5\cdot q^2(q^3-1)=q^7(q^3-1)\) roots. No target outside \(J^3\) occurs. All cases are now exhausted.

**6. Characteristic two and consistency.** When \(q\) is even, the exterior algebra is commutative with square-zero generators; Frobenius gives \((a+y)^2=a^2\). It is a bijection on \(\mathbb F_q\), proving the even-field formula. Finally, for odd \(q\), the radical fiber totals satisfy
\[
(q^{12}+q^{10}-q^7)+(q^5-1)q^7(q^3-1)=q^{15},
\]
as required, and the stated number of image values follows by adding all targets with nonzero square scalar parts.

## Verification
The accompanying `checker.py` independently multiplies bit-mask exterior monomials with antisymmetric signs. It exhaustively checks all \(3^{10}=59049\) choices of \((v,w)\) over \(\mathbb F_3\), comparing every one of the \(3^5=243\) target fibers to the theorem. It also checks every \(2^{10}\) such input in characteristic two and performs 64 independently chosen nonzero-scalar target tests each over \(\mathbb F_3\) and \(\mathbb F_5\), verifying both explicit roots by genuine multiplication. The exact captured output is in `checker_output.txt`. These finite checks corroborate, but do not replace, the proof for every finite field.

## Relationship to prior work
Domokos and Zubor [1], Sections 1–2, analyze commutative subalgebras and square-zero odd subspaces of finite Grassmann algebras. They do not enumerate prescribed squares of arbitrary nonhomogeneous algebra elements. Fonseca [2] examines graded polynomial identities of the infinite Grassmann algebra over finite fields of odd characteristic, not the square-map fibers of the four-generator algebra. Bavula [3], Section 2, classifies its automorphism-group structures and generators rather than prescribed algebraic squares.

The previously published regular-multiplication Jordan-stratum census [4], for exactly this four-generator algebra, gives the frequencies of zero versus nonzero squares as a consequence of \(L_y^2=L_{y^2}\). In particular, **the zero-square count is already implied by [4] and is not separately asserted as new**. Its seven element-type strata and the alternating-rank counts do **not**, however, determine how the nonzero square values distribute over the different nonzero elements of \(J^3\). The distinctive result here is the *constant nonzero prescribed-target fiber* across both the nonzero cubic and nonzero top-degree cases, and its complete extension across the scalar branches. A separate published commuting-pair census [5] addresses the ordinary bracket \([x,y]\), not \(x^2=b\); it does not imply the asserted uniformity.

## Limitations
This proves a result for four exterior generators and finite fields only; it does not assert a corresponding uniformity in larger exterior ranks or in arbitrary nilpotent associative algebras. The standard alternating-form orbit counts and previously known square-zero total are used as inputs. An unindexed source might already contain an equivalent prescribed-fiber theorem; historical priority has not been independently certified. No independent mathematical audit has been performed.

## References
[1] M. Domokos and M. Zubor, *Commutative subalgebras of the Grassmann algebra*, arXiv:1403.2916, first public 2014-03-12, https://arxiv.org/abs/1403.2916.

[2] L. F. G. Fonseca, *\(\mathbb Z_2\)-graded identities of the Grassmann algebra over a finite field*, arXiv:1403.0888, first public 2014-03-04, https://arxiv.org/abs/1403.0888.

[3] V. V. Bavula, *The Jacobian map, the Jacobian group and the group of automorphisms of the Grassmann algebra*, arXiv:math/0703352, first public 2007-03-12, https://arxiv.org/abs/math/0703352.

[4] *Complete regular-multiplication Jordan strata in the four-generator exterior algebra*, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-complete-regular-multiplication-jordan-strata-in-the-four-genera--f47eadf1cf1d/RESULT.md. See the rank-\(L_y^2\) strata and their exact point counts.

[5] *Commuting-pair threshold in fourth-order Grassmann algebras and the five-generator centralizer spectrum*, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-commuting-pair-threshold-in-fourth-order-grassmann-algebras-and--b94809d1e9e0/RESULT.md.
