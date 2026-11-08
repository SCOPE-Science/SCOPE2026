# The ramified \(27\)-line scheme of the Clebsch cubic at \(5\)

## Finding
Let \(R=\mathbb Z_5\). In \(\mathbb P^4_R\) consider the **fixed diagonal integral model**
\[
\mathcal X=V\!\left(\sum_{i=0}^4X_i,\sum_{i=0}^4X_i^3\right).
\]
Let \(F=\operatorname{Hilb}^{\mathrm{line}}(\mathcal X/R)\) be the relative Hilbert scheme of projective lines, equivalently the cubic-section zero scheme in \(\operatorname{Gr}_R(2,4)\). There is an isomorphism of **entire finite flat \(R\)-schemes**
\[
\boxed{F\cong\coprod_{15}\operatorname{Spec}R\ \sqcup\ \coprod_6\operatorname{Spec}R[t]/(t^2+t-1).}
\]
The quadratic factors are the totally ramified integer rings \(\mathbb Z_5[\sqrt5]\). Thus \(F\) has degree \(27\), while its special fiber is
\[
\boxed{F_{\mathbb F_5}\cong\coprod_{15}\operatorname{Spec}\mathbb F_5\ \sqcup\ \coprod_6\operatorname{Spec}\mathbb F_5[\varepsilon]/(\varepsilon^2).}
\]
The special Clebsch cubic has precisely one ordinary double point and exactly \(21\) geometric lines, all defined over \(\mathbb F_5\): fifteen avoid the node, and six pass through it. The six doubled Hilbert points correspond **exactly** to the six lines through the node. The discriminant ideal of the finite \(R\)-algebra \(\Gamma(F,\mathcal O_F)\) is \(5^6R\).

## Assumptions and scope
All assertions concern the displayed integral equation after base change to \(\mathbb Z_5\). The term *line* means a geometrically linear closed subscheme with Hilbert polynomial \(m+1\). The relative Hilbert scheme is taken in the hyperplane \(\sum X_i=0\), which is canonically \(\mathbb P^3_R\). The special-fiber assertion is scheme-theoretic, not just a point count. No claim is made about other integral models or primes.

## Proof

### 1. Singular geometry and all special lines
Write \(k=\mathbb F_5\). Since \(3\) is invertible, the projective Jacobian equations on \(\sum X_i=0\) require all five squares \(X_i^2\) to be equal. In a geometric point this gives \(X_i=\pm a\); the hyperplane equation forces the number of plus signs to be \(0\) or \(5\) modulo \(5\). Consequently the unique singular point is \(P=[1:1:1:1:1]\).

Every vector of the hyperplane \(\sum X_i=0\) is uniquely \(s(1,1,1,1,1)+(a,b,c,-a-b-c,0)\). Define
\[
q=a^2+b^2+c^2+(a+b+c)^2,
\qquad
h=a^3+b^3+c^3-(a+b+c)^3.
\]
The special cubic is exactly \(3sq+h=0\). The quadratic form \(q\) has symmetric matrix \(I_3+J_3\) and determinant \(4\ne0\) in \(k\), so \(P\) is an ordinary double point. Moreover,
\[
h=-3(a+b)(a+c)(b+c),\qquad q|_{a+b=0}=2(a^2+c^2).
\]
Cyclic variants of the second equality show that \(q=h=0\) cuts out six distinct \(k\)-points on the smooth conic \(q=0\). They have no three collinear; the intersections are transverse because the three linear factors of \(h\) meet the conic in disjoint simple pairs.

Projection from \(P\) to \(\mathbb P^2_{[a:b:c]}\) classifies **all geometric lines**. A line through \(P\) lies on the cubic if and only if its direction is a common zero of \(q,h\), yielding six lines. If a line \(L\) avoids \(P\), projection restricts to an isomorphism \(L\to\ell\) onto a line \(\ell\subset\mathbb P^2\). Its \(s\)-coordinate is linear along \(\ell\); hence \(q|_\ell\) divides \(h|_\ell\). Since \(q\) is a smooth conic and \(q,h\) meet transversely, \(\ell\) cannot be tangent to \(q\); it must join two distinct points in the six-point base locus. Conversely every such chord defines a line using \(s=-h/(3q)\) on \(\ell\). There are \(\binom62=15\) chords, proving that the list of \(21\) lines is exhaustive even over an algebraic closure. The fifteen familiar matching lines \((A,-A,B,-B,0)\), under coordinate permutations, are distinct lines avoiding \(P\); therefore they are exactly the fifteen chord lines. All twenty-one lines are \(k\)-rational.

### 2. The twelve ramified generic lines
Let \(t\) satisfy \(t^2+t-1=0\), put \(R'=R[t]\), and consider the vectors
\[
 u=(2,t,-1-t,-1-t,t),\qquad v=(0,1,t,-t,-1).
\]
They lie in \(\sum X_i=0\), and direct expansion gives the polynomial identity
\[
\sum_{i=0}^4(\lambda u_i+\mu v_i)^3
 =-6\lambda(\lambda^2+\mu^2t)(t^2+t-1)=0
\]
in \(R'[\lambda,\mu]\). Thus their span defines an \(R'\)-valued point of the Fano scheme. Its Plücker coordinates satisfy
\[
p_{01}=2,\qquad p_{02}=2t.
\]
Hence the coordinate function \(p_{02}/p_{01}\) recovers the full ring generator \(t\), not merely a proper suborder. The twelve generic lines obtained by permuting the five coordinates are distinct and form six Galois-conjugate pairs, as is also explicit in Polo-Blanco and Top's classical list. The other fifteen generic lines are the matching lines. Because the characteristic-zero cubic is smooth, these are all \(27\) generic geometric lines.

The polynomial \(t^2+t-1\) has discriminant \(5\). Setting \(\varepsilon=t-2\) gives \(\varepsilon^2+5\varepsilon+5\), an Eisenstein polynomial, so \(R'\) is the integer ring of a totally ramified quadratic extension. Modulo \(5\), the above two spanning vectors reduce to the constant vector \(2(1,1,1,1,1)\) and \((0,1,2,3,4)\). Their permutations give exactly six distinct lines through \(P\): the affine group of permutations \(i\mapsto ai+b\) of \(\mathbb F_5\) is the stabilizer of the resulting projective line, of order \(20\) in \(S_5\), so its orbit has size \(120/20=6\). The twelve generic lines specialize two-to-one to these six special lines. The fifteen matching sections specialize injectively to the other fifteen lines.

### 3. Flatness and identification of the entire Hilbert scheme
Let \(G=\operatorname{Gr}_R(2,4)\), smooth of relative dimension \(4\), with universal rank-two subbundle \(\mathcal U\). The cubic defines a section of the rank-four vector bundle \(\operatorname{Sym}^3(\mathcal U^\vee)\); its zero locus is \(F\). Both geometric fibers are finite by the line classifications above, so properness gives that \(F\to\operatorname{Spec}R\) is finite. Locally on the regular five-dimensional total space \(G\), the four components of this section cut out a scheme of dimension one. They form a regular sequence, and \(F\) is Cohen–Macaulay. Since every special fiber local ring is zero-dimensional, \(5\) is a parameter and a non-zero-divisor. Therefore \(F\) is finite flat over \(R\), of generic rank \(27\).

As \(R\) is complete, the twenty-one distinct rational special points separate the finite \(R\)-algebra of \(F\) into twenty-one local factors. For the fifteen matching-line points, the explicit sections induce surjections from the corresponding local factors onto \(R\), so each has rank at least one. For each of the six node-line points, the \(R'\)-valued family above (after a coordinate permutation) induces a surjection from the local factor onto \(R'\): in the relevant Plücker chart, the ratio \(p_{02}/p_{01}\), suitably relabeled, maps to \(t\). Thus these six local factors have ranks at least two. Their sum is at least \(15+6\cdot2=27\), already equal to the entire flat rank. Each surjection must therefore be an isomorphism. This proves the claimed complete scheme decomposition, with no residual embedded or vertical components.

Finally \(R'/5R'\cong\mathbb F_5[\varepsilon]/(\varepsilon^2)\), and each quadratic factor has discriminant ideal \(5R\). The product algebra has discriminant ideal \(5^6R\).

## Verification
The accompanying standard-library Python script checks the cubic identity and Plücker generator over \(\mathbb Z[t]/(t^2+t-1)\), the twelve distinct generic permutation lines and their pairwise reduction to six special directions, the six transverse rational base points, and all \(21\) displayed special lines. As an independent finite cross-check it enumerates the \(806\) lines of \(\mathbb P^3(\mathbb F_5)\) and finds precisely these \(21\) on the cubic. The finite-field enumeration by itself does not exclude non-rational geometric lines; that completeness follows from the projection proof above. It also does not certify flatness; the regular-sequence argument establishes that property.

## Relationship to prior work
Polo-Blanco and Top (2009, §5.1) provide the classical equations and their \(15+12\) generic lines, including the quadratic field \(\mathbb Q(\sqrt5)\). Vikulova (2025, Proposition 1.5(i) and introductory discussion) states that the Clebsch diagonal cubic is singular in characteristic five and locates its singular point. Neither inspected statement gives the relative Hilbert scheme over \(\mathbb Z_5\), proves its finite flatness across the singular special fiber, or identifies its six exact ramified local rings. The general geometric facts about one-nodal cubic surfaces explain the \(21\) reduced line supports but do not alone identify the integral algebra. No assertion is made that the generic \(27\)-line classification or the existence of the characteristic-five singular point is new.

## Limitations
The decomposition is for the fixed diagonal integral model and the completion at \(5\), not for arbitrary degenerations of cubic surfaces. The formula determines the finite relative line Hilbert scheme, but not arbitrary Hilbert schemes of higher-degree curves. The explicit classical line formula makes the result potentially approachable by existing degeneration theory; historical priority beyond the inspected sources has not been independently established.

## References
1. I. Polo-Blanco and J. Top, *A remark on parameterizing nonsingular cubic surfaces*, Computer Aided Geometric Design 26 (2009), 842–849, §5.1. First available online 2009-06-06. DOI: 10.1016/j.cagd.2009.06.001. Author-hosted full text: https://www.math.rug.nl/~top/potop.pdf.
2. A. V. Vikulova, *The most symmetric smooth cubic surface*, Sbornik: Mathematics 216 (2025), 168–209, especially Proposition 1.5 and the characteristic-five discussion. DOI: 10.4213/sm10161e. Full text: https://www.mathnet.ru/php/archive.phtml?jrnid=sm&option_lang=eng&paperid=10161&wshow=paper.
