# Trace-zero Gauss-fixed schemes on characteristic-two cyclic Klein cubics

## Finding
For every integer \(n\ge 3\), put
\[
X_n=V(F_n)\subset\mathbb P^{n-1}_{\mathbb F_2},\qquad
F_n=\sum_{i\in\mathbb Z/n\mathbb Z}X_i^2X_{i+1}.
\]
Use the indicated ordered coordinates to identify the dual projective space with \(\mathbb P^{n-1}\). The resulting marked Gauss map \(\gamma_n:X_n\to X_n\) has finite étale fixed-point scheme
\[
\operatorname{Fix}(\gamma_n)\simeq
\operatorname{Spec}\mathbb F_2[t,t^{-1}]/(\operatorname{Tr}_n(t)),
\qquad \operatorname{Tr}_n(t)=\sum_{j=0}^{n-1}t^{2^j}.
\]
It has degree \(2^{n-1}-1\); its geometric points correspond, with arithmetic Frobenius respected, to nonzero trace-zero elements of \(\mathbb F_{2^n}\). The point corresponding to \(t\) is
\[
[t:t^2:t^4:\cdots:t^{2^{n-1}}].
\]
For \(m\ge1\), put \(d=\gcd(m,n)\). The exact fixed-scheme point counts are
\[
\#\operatorname{Fix}(\gamma_n)(\mathbb F_{2^m})=
\begin{cases}2^d-1,&n/d\text{ even},\\2^{d-1}-1,&n/d\text{ odd}.\end{cases}
\]
Equivalently, with \(N_e\) denoting the displayed count for \(m=e\) and \(e\mid n\), let
\[
c_d=\frac1d\sum_{e\mid d}\mu(d/e)N_e,\qquad d\mid n.
\]
Then \(Z(\operatorname{Fix}(\gamma_n)/\mathbb F_2,T)=\prod_{d\mid n}(1-T^d)^{-c_d}\). For the classical cyclic Klein cubic threefold \(n=5\), the fixed scheme is the disjoint union of three copies of \(\operatorname{Spec}\mathbb F_{32}\), so its 15 geometric points form three degree-five Frobenius orbits, with zeta function \((1-T^5)^{-3}\).

## Assumptions and scope
The base field is \(\mathbb F_2\); all schemes, dual identifications, and fixed loci use the displayed coordinates. In particular, the "fixed points of the Gauss map" refers to the identification of a point and its tangent hyperplane by matching their ordered coordinate vectors, not to a coordinate-independent fixed-point notion. The formula holds for all \(n\ge3\) and over every finite extension. The hypersurface is smooth because \(\partial F_n/\partial X_i=X_{i-1}^2\) and these derivatives never vanish simultaneously in projective space.

## Proof
**1. The marked Gauss endomorphism.** In characteristic two,
\[
\gamma_n([x_0:\ldots:x_{n-1}])=
[x_{n-1}^2:x_0^2:\ldots:x_{n-2}^2].
\]
Direct substitution gives \(F_n(\gamma_n(x))=F_n(x)^2\), so the map carries \(X_n\) into itself. It is the composition of a cyclic permutation and the relative Frobenius and is thus purely inseparable of degree \(2^{n-2}\). These general Gauss-map features of Frobenius forms are background, not the new claim.

**2. Unique normalization of a projectively fixed vector.** Over an algebraically closed extension, \(\gamma_n(x)=\lambda x\) for some nonzero scalar \(\lambda\). No coordinate of \(x\) can vanish: one zero propagates cyclically through the equations to all coordinates. Multiplication of \(x\) by \(\lambda^{-1}\) gives the unique representative \(y\) of its projective class with \(\gamma_n(y)=y\), because \(\gamma_n(a x)=a^2\gamma_n(x)\). Writing \(t=y_0\ne0\), the fixed equations yield \(y_i=t^{2^i}\) and \(t^{2^n}=t\); hence \(t\in\mathbb F_{2^n}^{\times}\). Conversely these formulas produce every projectively fixed point of the ambient map, and the normalization is algebraic on the chart where all coordinates are nonzero.

**3. The cubic restriction.** On a normalized fixed vector,
\[
F_n(y)=\sum_{i=0}^{n-1}t^{2^{i+2}}
       =\left(\sum_{i=0}^{n-1}t^{2^i}\right)^4.
\]
The summand \(\operatorname{Tr}_n(t)\) belongs to \(\mathbb F_2\), so \(F_n(y)=0\) if and only if \(\operatorname{Tr}_n(t)=0\). The polynomial \(\operatorname{Tr}_n(t)/t\) has degree \(2^{n-1}-1\), constant term one, and only simple roots: \(\operatorname{Tr}_n'(t)=1\), while \(t=0\) is a simple trace root.

**4. Scheme structure, not only set-theoretic points.** The ambient projective map \(\gamma_n\) has zero differential. Therefore its graph meets the diagonal transversely at every geometric fixed point: on a tangent vector the difference of the two differentials is \(-\mathrm{id}\). The ambient fixed scheme, and hence its closed subscheme cut out by \(F_n\), are reduced and étale over \(\mathbb F_2\). The normalization in Step 2 is defined algebraically on the fixed scheme, with inverse given by the displayed homogeneous coordinates; the condition in Step 3 gives an isomorphism of finite étale schemes, not merely a bijection over an algebraic closure. This proves the stated trace-zero presentation and degree.

**5. Arithmetic descent.** Arithmetic Frobenius acts on the normalized parameter by \(t\mapsto t^2\). An element of \(\mathbb F_{2^n}\) is rational over \(\mathbb F_{2^m}\) exactly when it belongs to \(\mathbb F_{2^d}\), \(d=\gcd(n,m)\). The absolute trace restricts to \((n/d)\operatorname{Tr}_{\mathbb F_{2^d}/\mathbb F_2}\), proving the two cases for its nonzero kernel. The Euler product for a finite étale scheme and Möbius inversion give the stated zeta function.

**6. The Klein cubic threefold.** For \(n=5\), the trace-zero equation for \(t\ne0\) is
\[
1+t+t^3+t^7+t^{15}
=(t^5+t^2+1)(t^5+t^3+1)
(t^5+t^3+t^2+t+1).
\]
Each factor is irreducible over \(\mathbb F_2\). Thus the fixed scheme has three closed points, each of residue degree five, accounting for all 15 geometric fixed points.

## Verification
The standalone Python program `verify.py` uses exact arithmetic over \(\mathbb F_2\) and \(\mathbb F_{32}\). It checks the formal Frobenius/Gauss polynomial identity for \(3\le n\le10\), the trace polynomial identity, all three degree-five irreducible factors, all 15 nonzero trace-zero elements of \(\mathbb F_{32}\), their three five-element Frobenius orbits, the cubic equation, and the Gauss fixed-point equations. Run `python verify.py`. The recorded output in `verification_output.txt` ends in `VERIFY_OK`. The general theorem is proved algebraically above; the finite range of code checks is not an infinite proof.

## Relationship to prior work
González-Aguilera and Liendo introduce the cyclic Klein cubic forms over characteristic zero in their 2010 preprint and study their automorphisms, not this characteristic-two marked Gauss fixed scheme. Kadyrsizova and collaborators prove general facts about Frobenius-form hypersurfaces, including the inseparable Gauss map and smooth dual; those background facts already cover the Gauss-map formula's general setting. The present arithmetic statement instead determines the complete *fixed scheme* under the marked Gauss endomorphism and all of its Frobenius orbits via the trace-zero kernel. Furukawa also classifies Gauss-rank-zero cubic embeddings in characteristic two, including the threefold case, but the inspected treatment addresses differential rank and geometric characterizations rather than the marked cyclic arithmetic fixed scheme. The older classical and the broader Frobenius-form theorems do not by themselves state this scheme or its exact zeta function. No historical priority claim is made beyond the inspected sources.

## Limitations
The result depends on the displayed coordinate matching of the dual projective space; changing that marking changes the fixed-point problem. The calculation does not classify arbitrary Gauss periodic points, noncyclic Frobenius forms, other automorphisms, or deformations. Historical priority remains provisional because exhaustive inspection of all specialist literature is not possible here. No independent scientific audit has been performed.

## References
1. V. González-Aguilera and A. Liendo, *Automorphisms of prime order of smooth cubic n-folds*, arXiv:1002.4136, first posted 2010-02-22, https://arxiv.org/abs/1002.4136.
2. Z. Kadyrsizova et al., *Lower Bounds on the F-pure Threshold and Extremal Singularities*, arXiv:2009.13679, Section 8.5, Proposition 8.6, https://arxiv.org/abs/2009.13679.
3. K. Furukawa, *Cubic hypersurfaces admitting an embedding with Gauss map of rank 0*, Advances in Mathematics 230 (2012), 1174–1183, https://doi.org/10.1016/j.aim.2012.03.006.
4. B. Brosowsky et al., *Geometry of Smooth Extremal Surfaces*, arXiv:2110.15908, for related positive-characteristic Frobenius-form geometry, https://arxiv.org/abs/2110.15908.
