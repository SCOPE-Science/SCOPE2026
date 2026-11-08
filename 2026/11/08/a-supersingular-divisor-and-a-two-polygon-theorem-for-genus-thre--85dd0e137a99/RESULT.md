# A supersingular divisor and a two-polygon theorem for genus-three order-four hyperelliptic curves in characteristic three

## Finding
Let \(k\) be algebraically closed of characteristic \(3\). For \(a,b,c\in k\), let \(C_{a,b,c}\) be the smooth projective model of
\[
 y^2=x^7+a x^5+b x^3+c x.
\]
The polynomial is squarefree, and hence \(C_{a,b,c}\) has genus \(3\), if and only if
\[
 c(b^3-a^2b^2+a^3c)\ne0.
\]
Every such curve has an order-four automorphism whose square is its hyperelliptic involution. Put \(t=a^3c+b^3\). Then the \(3\)-rank \(f\), \(a\)-number and Newton polygon \(\operatorname{NP}\) of its Jacobian satisfy
\[
\begin{array}{c|c|c|c}
\text{condition}&f&a(C)&\operatorname{NP}(\operatorname{Jac}(C))\\\hline
 t\ne0&2&1&(0,0,\frac12,\frac12,1,1)\\
 t=0&0&1&(\frac12,\frac12,\frac12,\frac12,\frac12,\frac12).
\end{array}
\]
Here the Newton polygon is specified by the multiset of six slopes; the second case is supersingular but **not** superspecial. The iterated Cartier ranks are, respectively, \(2,2,2,\ldots\) and \(2,1,0,0,\ldots\). Both strata are nonempty. On the smooth parameter locus, the supersingular condition cuts out a reduced, irreducible, smooth divisor. It has the explicit one-parameter normal-form parametrization
\[
 y^2=x^7+x^5+B x^3-B^3x,\quad B\in k^\times,
\]
up to coordinate rescaling. This parametrization is not asserted to be injective on moduli points.

## Assumptions and scope
All statements are over an algebraically closed field \(k\) of characteristic exactly \(3\), for the marked hyperelliptic coordinate presentation written above. \(f\) means \(\dim_{\mathbb F_3}\operatorname{Jac}(C)[3](k)\), and \(a(C)=\dim_k\operatorname{Hom}(\alpha_3,\operatorname{Jac}(C)[3])\). The Cartier operator \(\mathcal C\) on \(H^0(C,\Omega^1)\) is semilinear; the ranks of its iterates are well defined. By “supersingular” we mean all Newton slopes equal \(1/2\), not superspeciality or vanishing Cartier. No assertion about a full coarse-moduli isomorphism or a complete Ekedahl–Oort classification is needed.

## Proof

**1. Smoothness, genus and symmetry.** Write \(f(x)=x h(x^2)\) with \(h(u)=u^3+a u^2+b u+c\). In characteristic \(3\), the roots of \(f\) are distinct exactly when \(c\ne0\) and \(h\) is squarefree; its discriminant is \(a^2b^2-b^3-a^3c\). The asserted smoothness condition follows. A squarefree polynomial of degree seven defines a smooth genus-three hyperelliptic curve. Choose \(i\in k\) with \(i^2=-1\). Because \(f(-x)=-f(x)\), the automorphism \((x,y)\mapsto(-x,iy)\) has square \((x,y)\mapsto(x,-y)\) and therefore order four.

**2. Cartier–Hasse–Witt computation.** The standard basis of holomorphic differentials is \(dx/y,\ x\,dx/y,\ x^2\,dx/y\). For \(p=3\), since \(f^{(p-1)/2}=f\), the coefficient construction gives the matrix
\[
H=\begin{pmatrix}0&c&0\\ a&0&b\\0&1&0\end{pmatrix}
\]
for Cartier coefficients in the standard indexing \(H_{ij}=[x^{3i-j}]f\). The semilinear Frobenius on the dual first cohomology is represented by \(T=H^{\mathsf T}\). Explicitly, for \((u,v,w)\in k^3\),
\[
 F(u,v,w)=(a v^3,\ c u^3+w^3,\ b v^3).
\]
Set \(S=cu^3+w^3\), and let \(t=a^3c+b^3\). Then
\[
F^2(u,v,w)=(a S^3,\ t v^9,\ b S^3).
\]
The first iterate has rank two: \(c\ne0\) and \((a,b)\ne(0,0)\) by smoothness. If \(t\ne0\), the map \((S,v)\mapsto(tS^9,tv^9)\), describing the induced \(S\)- and \(v\)-coordinates under \(F^2\), is bijective on \(k^2\). Thus all Frobenius/Cartier iterates have rank two. If \(t=0\), the second iterate has rank one and the third vanishes, by substituting into the same formula. Hence the Cartier rank sequences are \(2,2,\ldots\) and \(2,1,0,\ldots\). The \(a\)-number is \(3-\operatorname{rank}(\mathcal C)=1\) in both cases; the \(3\)-rank is the stable semilinear Frobenius rank, hence respectively \(2\) and \(0\).

**3. Newton slopes.** The order-four automorphism induces an action of \(\mathbb Z[i]\) on the Jacobian with \(i^2=-1\), so the rational Dieudonné module admits the unramified quadratic field \(\mathbb Q_3(i)\). In each Newton-slope sub-isocrystal, decomposition under the two eigenspaces of \(i\) over Witt vectors of \(k\) is interchanged by semilinear Frobenius: a chosen Witt lift of \(i\) is carried by the Witt Frobenius to \(-i\). Consequently **each slope has even multiplicity**. In a height-six polarized isocrystal, slopes occur symmetrically under \(\lambda\leftrightarrow1-\lambda\); their multiplicities are also divisible by their reduced denominators. With \(3\)-rank \(0\), any off-central slope has reduced denominator at least \(3\), so its multiplicity must be a multiple of both its denominator and \(2\); together with the distinct complementary slope this would require more than six dimensions. Thus all six slopes equal \(1/2\). With \(3\)-rank \(2\), there are exactly two slope-zero and two slope-one directions; the remaining two necessarily have slopes \(1/2,1/2\). These give the stated Newton polygons. Since Cartier rank is two, \(a=1\), ruling out superspeciality even on the supersingular divisor.

**4. Geometry of the jumping locus.** On \(t=0\), smoothness forces \(a\ne0\) and \(b\ne0\). Indeed if either vanishes, \(t=0\) makes the smoothness discriminant vanish. Substituting \(c=-b^3/a^3\) into the discriminant factor gives \(-a^2b^2\ne0\). Hence the jumping locus inside the smooth three-dimensional coefficient space is \(\{a,b\in k^\times,\ c=-b^3/a^3\}\), isomorphic to \((\mathbb G_m)^2\). It is therefore a reduced, smooth, irreducible divisor; equivalently \(\partial t/\partial c=a^3\ne0\) on it. Replacing \(x\) by \(\sqrt a\,x\), with a corresponding rescaling of \(y\), normalizes \(a=1\); then \(B=b/a^2\ne0\) and \(c'=-B^3\). Conversely every such \(B\) gives a smooth curve. Generic smooth examples with \(t\ne0\) exist, for instance \((a,b,c)=(0,1,1)\), for which the discriminant factor is \(1\). The two strata are nonempty.

## Verification
The independent symbolic identities \(H^{(3)}H\), \(H^{(9)}H^{(3)}H\) and the smoothness-discriminant substitution were checked exactly in characteristic three by `verify.py`. An elementary finite-field implementation separately checked polynomial squarefreeness by Euclidean gcd, Frobenius ranks through the fourth iterate, and the jump condition over all coefficient triples in \(\mathbb F_3\) and \(\mathbb F_9\), as well as a structured sample over \(\mathbb F_{27}\) containing the entire displayed exceptional one-parameter slice over that field. Reproduction: `python3 verify.py`. The finite-field checks are corroboration, not an extrapolation to arbitrary algebraically closed fields: the proof above supplies the uniform argument. Expected final output line: `ALL_CHECKS_PASSED`.

## Relationship to prior work
Achter–Glass–Pries, Lemma 3.6, identifies the order-four hyperelliptic locus of genus \(g\ge3\), including its irreducibility, dimension \(g-1\), and positive generic \(p\)-rank. Its equation for a genus-three order-four model is equivalent, after branch normalization, to the odd degree-seven model used here; that prior work **does not** give the explicit characteristic-three hypersurface \(a^3c+b^3=0\), the constant \(a\)-number, full iterated Cartier ranks, or its two Newton polygons. The general hyperelliptic invariant and symmetry classifications of Lercier–Ritzenthaler and Gutierrez–Sevilla–Shaska provide context, not this characteristic-three arithmetic stratification. Vollaard–Wedhorn study unitary supersingular PEL Shimura varieties; they give much broader ambient arithmetic geometry, but no coefficient criterion for this particular hyperelliptic family. The standard Hasse–Witt/Cartier coefficient formula is classical and is **not** asserted as new. The contribution is the combined exact stratification and its explicit supersingular divisor, including the Newton-slope conclusion forced by order-four symmetry.

## Limitations
This is a classification for the indicated order-four **marked family**, not an independent classification of all genus-three curves or all higher automorphism groups. Its supersingular normal-form parameter may identify isomorphic unmarked curves. The Dieudonné argument does not determine full Ekedahl–Oort types. All novelty claims are qualified by possible unlocated specialty literature; no independent expert priority review has been performed.

## References
- J. Achter, D. Glass and R. Pries, *Curves of given \(p\)-rank with trivial automorphism group*, arXiv:0708.2199v1 (first posted 16 August 2007), especially Lemma 3.6. https://arxiv.org/abs/0708.2199
- I. Vollaard and T. Wedhorn, *The supersingular locus of the Shimura variety of \(GU(1,n-1)\) II*, arXiv:0804.1522v1 (9 April 2008). https://arxiv.org/abs/0804.1522
- R. Lercier and C. Ritzenthaler, *Hyperelliptic curves and their invariants: geometric, arithmetic and algorithmic aspects*, arXiv:1111.4152v1 (17 November 2011). https://arxiv.org/abs/1111.4152
- J. Gutierrez, D. Sevilla and T. Shaska, *Hyperelliptic curves of genus 3 with prescribed automorphism group*, arXiv:1209.2938v1 (13 September 2012). https://arxiv.org/abs/1209.2938
- Classical Cartier–Manin coefficient computation for odd-characteristic hyperelliptic curves, used here in its standard degree-seven instance.
