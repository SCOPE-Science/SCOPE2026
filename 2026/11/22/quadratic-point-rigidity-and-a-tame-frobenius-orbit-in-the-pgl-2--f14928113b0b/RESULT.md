# Quadratic-point rigidity and a tame Frobenius orbit in the \(\mathrm{PGL}(2,q)\)-invariant plane-curve pencil

## Finding

For every odd prime power \(q\ge 5\) and every \(\lambda\in\mathbb F_q\setminus\{0,1,-1\}\), let \(C_\lambda\) be the smooth plane curve
\[
Y^{q+1}-X^qZ-XZ^q-\lambda(Y^2-2XZ)^{(q+1)/2}=0.
\]
Then
\[
\#C_\lambda(\mathbb F_q)=q+1,\qquad
\#C_\lambda(\mathbb F_{q^2})=\frac{q^3+q+2}{2}.
\]
Consequently the number of degree-two closed points of \(C_\lambda\) is \((q^3-q)/4\), independent of the smooth non-Hermitian parameter. Under the established \(\mathrm{PGL}(2,q)\)-action, the \((q^3-q)/2\) points of \(C_\lambda(\mathbb F_{q^2})\setminus C_\lambda(\mathbb F_q)\) constitute **exactly one** of the two geometric tame short orbits of that size. The other tame short orbit contributes no \(\mathbb F_{q^2}\)-points.

The smooth Hermitian member \(\lambda=0\) instead has \(q^3+1\) quadratic-extension points, so the count jumps by precisely \((q^3-q)/2\) at the enhanced-symmetry member.

## Assumptions and scope

The parameter \(q\) is an odd prime power, not necessarily prime. All counts concern geometric points rational over the indicated finite fields, not scheme lengths. The coefficients and parameter lie in \(\mathbb F_q\). For \(\lambda\ne\pm1\), geometric smoothness is established in Borges--Korchmáros--Speziali, Lemma 4.23(ii). The generic group-orbit statement applies only to \(\lambda\ne0,\pm1\). No statement about extension degrees beyond two or the full Weil polynomial is made.

## Proof

**Points over the base field.** In the affine chart \(Z=1\), write \(x=X/Z\), \(y=Y/Z\), and \(w=y^2-2x\). Over \(\mathbb F_q\) the equation becomes \(w-\lambda w^{(q+1)/2}=0\). If \(w\ne0\), Euler's criterion gives \(w^{(q-1)/2}=\pm1\), inconsistent with \(\lambda\notin\{1,-1\}\). Thus \(w=0\), giving exactly \(q\) affine points \((x,y)=(y^2/2,y)\). At \(Z=0\) the equation is \((1-\lambda)Y^{q+1}=0\), giving only \([1:0:0]\). Therefore the base-field count is \(q+1\).

**Quadratic extension.** Take \((x,y)\in\mathbb F_{q^2}^2\) on the affine curve. Let \(N\) and \(\operatorname{Tr}\) denote norm and trace to \(\mathbb F_q\). The equation is
\[
N(y)-\operatorname{Tr}(x)=\lambda w^{(q+1)/2},\qquad w=y^2-2x.
\]
Because \(\lambda\ne0\), the left side implies \(w^{(q+1)/2}\in\mathbb F_q\). For nonzero \(w\), this is equivalent to \(w^{(q^2-1)/2}=1\), namely that \(w\) is a square in \(\mathbb F_{q^2}\); zero is also a square. Write \(w=t^2\), and eliminate \(x=(y^2-t^2)/2\). The remaining equation becomes
\[
N(y)-\tfrac12\operatorname{Tr}(y^2)
+\tfrac12\operatorname{Tr}(t^2)-\lambda N(t)=0.
\]
Choose \(\theta\in\mathbb F_{q^2}\) with \(\theta^q=-\theta\) and \(D=\theta^2\in\mathbb F_q\) a nonsquare. Write \(y=c+d\theta\) and \(t=a+b\theta\), where \(a,b,c,d\in\mathbb F_q\). Substitution gives exactly
\[
(1-\lambda)a^2+D(1+\lambda)b^2-2Dd^2=0.
\]
For \(\lambda\ne\pm1\), this is a nondegenerate ternary quadratic form, with determinant \(-2D^2(1-\lambda^2)\ne0\). Its projective zero locus is a nonsingular conic with \(q+1\) points, so the affine zero set has \(1+(q-1)(q+1)=q^2\) triples \((a,b,d)\). The free coordinate \(c\) has \(q\) choices. The map \(t\mapsto t^2\) is two-to-one for \(t\ne0\), but one-to-one for \(t=0\). In the quadratic-form zero set, \(t=0\) forces \(a=b=d=0\), leaving exactly \(q\) choices of \(c\). Thus the affine curve has \(q+(q^3-q)/2=(q^3+q)/2\) quadratic-extension points. Add the unique point at infinity to obtain \((q^3+q+2)/2\). All equivalences above are reversible.

**Tame short orbit.** Borges--Korchmáros--Speziali, Proposition 4.26, identifies the three geometric short \(\mathrm{PGL}(2,q)\)-orbits for \(\lambda\ne0,\pm1\): the \(q+1\) conic points and two orbits, each of size \((q^3-q)/2\); every other orbit has group order \(q^3-q\). The quadratic-extension point set is invariant under \(\mathrm{PGL}(2,q)\) since the transformations are defined over \(\mathbb F_q\). It contains the conic-point orbit and exactly \((q^3-q)/2\) further points. Hence it contains precisely one entire tame short orbit and no long orbit.

**Hermitian comparison.** For \(\lambda=0\), the affine equation is \(N(y)=\operatorname{Tr}(x)\). There are \(q^2\) choices of \(y\), and the trace map has exactly \(q\) preimages of each value; this gives \(q^3\) affine points and the same unique point at infinity. Hence \(\#C_0(\mathbb F_{q^2})=q^3+1\). Subtracting the generic count proves the jump.

## Verification

The standalone `verify.py` enumerates the points of the affine projective models over \(\mathbb F_{p^2}\) for every permitted parameter over the prime fields \(p=5,7,11\), including the Hermitian comparison. Its extension counts are respectively \(66,176,672\) for all nonzero smooth parameters, and \(126,344,1332\) for the Hermitian parameters. These finite computations check examples only; the preceding norm/trace and quadratic-form argument proves the uniform statement for every odd prime power.

Reproduce: `python3 verify.py` (Python standard library; no dependencies).

## Relationship to prior work

Borges--Korchmáros--Speziali, *Plane curves with a large linear automorphism group in characteristic p*, arXiv:2202.05765 (first submitted 11 February 2022), introduce the pencil, establish the smoothness, identify the full automorphism group, and classify the three short geometric orbits (Lemma 4.23, Theorem 4.25, Proposition 4.26). They also study genus and \(p\)-rank in Section 8.1. None of the inspected relevant statements specifies which tame short orbit is defined pointwise over the quadratic extension, or the uniform non-Hermitian quadratic point count. The result here adds that arithmetic distinction; it is not a claim to discover the curves or their geometric orbit lengths.

Korchmáros--Nagy--Szőnyi (2024) consider a related but *rational singular* curve and Hermitian point-set geometry, not this smooth non-Hermitian pencil. No full claim of priority is made against inaccessible or unindexed work.

## Limitations

The proof concerns only the first two rational-point counts. The formula does not determine full zeta functions, isomorphism classes, or higher-extension point counts. The two singular parameters \(\lambda=\pm1\) are excluded. The assertion about short orbits relies on the cited geometric classification, while the arithmetic count has an independent elementary proof. A not-yet-indexed equivalent quadratic-point calculation is a residual priority risk.

## References

1. H. Borges, G. Korchmáros, and P. Speziali, *Plane curves with a large linear automorphism group in characteristic p*, arXiv:2202.05765v1 (11 February 2022), Sections 4.8 and 8.1. https://arxiv.org/html/2202.05765v1
2. G. Korchmáros, G. P. Nagy, and T. Szőnyi, *Algebraic approach to the completeness problem for (k,n)-arcs in planes over finite fields*, Journal of Combinatorial Theory, Series A 204 (2024), 105851. https://doi.org/10.1016/j.jcta.2023.105851
