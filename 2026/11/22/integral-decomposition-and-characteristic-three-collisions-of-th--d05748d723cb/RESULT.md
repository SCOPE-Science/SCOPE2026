# Integral decomposition and characteristic-three collisions of the Penrose forty-point scheme

## Finding
Let \(R=\mathbb Z[x,y,z,w]\) and let \(Z\subset\mathbb P^3_{\mathbb Z}\) be the projective scheme cut out by the five homogeneous quartics
\[
xyzw,\quad w(x^3-y^3+z^3),\quad z(x^3+y^3+w^3),\quad
y(-x^3+z^3+w^3),\quad x(y^3+z^3-w^3).
\]
Write \(\mu_3=\operatorname{Spec}\mathbb Z[t]/(t^3-1)\). There is an isomorphism of finite schemes **over \(\mathbb Z\)**
\[
\boxed{\quad Z\simeq\coprod_{i=1}^{4}\operatorname{Spec}\mathbb Z\;\amalg\;
\coprod_{i=1}^{4}(\mu_3\times_{\mathbb Z}\mu_3).\quad}
\]
The four sections are the coordinate points. The four rank-nine components have explicit embeddings
\[
[0:1:u:-v],\qquad [1:0:-u:-v],\qquad
[1:u:0:v],\qquad [1:-u:v:0],\qquad u^3=v^3=1.
\]
In particular, \(Z\to\operatorname{Spec}\mathbb Z\) is finite flat of degree \(40\). For every algebraically closed field of characteristic different from \(3\), its fiber has \(40\) distinct reduced points. Its characteristic-three fiber instead has exactly eight geometric support points: four reduced coordinate points and four nonreduced points of length nine. At each nonreduced point, the completed local ring is
\[
\boxed{\;k[[s,t]]/(s^3,t^3),\qquad
H_{\mathfrak m}(T)=1+2T+3T^2+2T^3+T^4.\;}
\]
Thus the complete geometric fiber length is \(4+4\cdot9=40\), the maximal ideal of each nonreduced local ring has nilpotency index \(5\), and characteristic \(3\) is the **only** bad-reduction prime. The eight reduced support points are
\[
[1:0:0:0],\ [0:1:0:0],\ [0:0:1:0],\ [0:0:0:1],
\]
\[
[0:1:1:-1],\ [1:0:-1:-1],\ [1:1:0:1],\ [1:-1:1:0].
\]

## Assumptions and scope
All schemes use the displayed *integral quartic ideal* and its ordinary projective \(\operatorname{Proj}\); no unrelated model or choice of reduction is intended. All geometric fiber assertions are over an algebraically closed residue field. A reduced fiber means geometrically reduced. The theorem concerns this specific arithmetic model of the forty-point Penrose configuration, not every possible arithmetic model of its characteristic-zero point set.

## Proof
**1. Candidate components.** Let \(Y\) be the union of the four coordinate sections and the four closed subschemes parametrized in the finding. For example, the component with first coordinate zero has homogeneous equations
\[
x=0,\qquad z^3-y^3=0,\qquad w^3+y^3=0.
\]
It lies wholly in the chart \(y\ne0\), because \(y=0\) would force all homogeneous coordinates to vanish. In that chart it has algebra \(\mathbb Z[u,v]/(u^3-1,v^3-1)\), via \(z/y=u\), \(w/y=-v\). The other three rank-nine components have the analogous descriptions. They are pairwise disjoint, and disjoint from the coordinate sections, since their three nonzero coordinates are units. Direct substitution shows that all five generating quartics vanish on every component, so \(Y\hookrightarrow Z\) is a closed immersion. Each component of \(Y\) is finite flat over \(\mathbb Z\), of rank one or nine; hence \(Y\) is finite flat of rank \(40\).

**2. Geometric support of a fiber.** Fix an algebraically closed field \(k\) of arbitrary characteristic. The equation \(xyzw=0\) forces at least one zero coordinate. If two coordinates vanish, the remaining quartics force at least one further zero: for instance \(x=y=0\) gives \(wz^3=zw^3=0\), so the point is coordinate. The other five choices of two zero coordinates are symmetric direct checks. If exactly one coordinate vanishes, the other three are units. On \(x=0\), the first quartic forces \(x=0\) in the local scheme and two of the remaining equations force
\[
(z/y)^3=1,\qquad (w/y)^3=-1.
\]
The third nontrivial equation follows from these two. The other three one-zero strata analogously yield the four pairs of cube-root equations in the finding. Thus the geometric support of \(Z_k\) is precisely the support of \(Y_k\).

**3. Scheme structure at every support point.** At a one-zero point, the product \(xyzw\) is a unit times the zero coordinate, so its equation removes that coordinate scheme-theoretically. Two other quartics are unit multiples of the two independent cube-root equations, and the fifth equation is their combination. Therefore the complete local rings of \(Z_k\) and \(Y_k\) coincide. At a coordinate point three quartics have independent linear terms with unit coefficients in the three affine coordinates; for example at \([1:0:0:0]\) they are \(w(1-y^3+z^3)\), \(z(1+y^3+w^3)\), and \(y(-1+z^3+w^3)\). Hence the local ring is exactly \(k\) there. The same unit-coefficient check applies to the other coordinate points. This proves that \(Y_k\to Z_k\) is an isomorphism for every algebraically closed \(k\), in every characteristic.

**4. Global identification, not just equal geometric sets.** Since \(Z\) is projective over \(\mathbb Z\) and every geometric fiber has finitely many support points, its structure map is proper and quasi-finite, hence finite. The closed immersion \(Y\hookrightarrow Z\) therefore gives a surjection of finite \(\mathbb Z\)-modules \(\mathcal O(Z)\twoheadrightarrow\mathcal O(Y)\) with finite kernel \(K\). As \(Y\) is flat over \(\mathbb Z\), tensoring with any residue field preserves the injection \(K\otimes k\hookrightarrow\mathcal O(Z_k)\). The preceding local calculation gives \(K\otimes k=0\) for every prime and for \(\mathbb Q\). Applying Nakayama's lemma to the localization of \(K\) at each prime gives \(K=0\). Thus \(Y\cong Z\), proving the claimed integral decomposition and flatness.

**5. Reduction at \(3\).** In characteristic \(3\), \(u^3-1=(u-1)^3\). Set \(s=u-1\), \(t=v-1\). Each rank-nine factor is \(k[s,t]/(s^3,t^3)\), with only the support point \((s,t)=(0,0)\). Its standard monomial basis \(s^it^j\) for \(0\le i,j\le2\) has nine elements; grouping by total degree gives the stated local Hilbert function. The highest nonzero monomial degree is four. For residue characteristic other than \(3\), \(u^3-1\) is separable, so the two-coordinate factor is geometrically reduced with nine points. Hence only residue characteristic \(3\) is bad.

## Verification
The accompanying `check.py` directly evaluates the five quartics on all rational projective points for eight small prime fields; it finds the expected counts \(8,8,8,40,8,40,8,40\) in characteristics \(2,3,5,7,11,13,17,19\). It also checks the nine basis monomials and local Hilbert function \((1,2,3,2,1)\). These finite checks are consistency tests, not a substitute for the general scheme-theoretic proof. Reproduce using `python3 check.py`.

## Relationship to prior work
Hanumanthu, Huizenga, Kettinger, Merta, Szemberg and Szpond (arXiv:2611.13108v1, November 9, 2026) display the same quartic ideal over the complex numbers in Section 4.1, determine its forty points, and compute their Waldschmidt constant. Dumnicki, Malara and Tutaj-Gasińska (2025, Example 6.3) also display the ideal and study unexpected hypersurfaces in characteristic zero. Waegell and Aravind (arXiv:1701.06512) identify the forty complex rays of the Penrose dodecahedron and Witting polytope. None of these inspected treatments establishes the present integral decomposition, finite-flat assertion, or characteristic-three local structure. The theorem is about an arithmetic scheme rather than a new count of the forty complex points.

## Limitations
This classification is specific to the five displayed quartics. It does not determine the modular reductions of the full reflecting-hyperplane arrangement or the modular reflection-group action. It does not claim that every integral model of the complex configuration has identical bad reduction. The arithmetic decomposition is proved internally; publication priority beyond the cited primary treatments and searched mathematical records remains subject to historical indexing gaps. No independent validation has been performed.

## References
1. K. Hanumanthu, J. Huizenga, J. Kettinger, Ł. Merta, T. Szemberg, and J. Szpond, *Waldschmidt constants and invariant geometry for exceptional rank-four complex reflection groups*, arXiv:2611.13108v1 (publicly submitted November 9, 2026), §4.1, https://arxiv.org/abs/2611.13108.
2. M. Dumnicki, G. Malara, and H. Tutaj-Gasińska, *Matrixwise (approach to unexpected hypersurfaces) reloaded*, Journal of Algebraic Combinatorics 62:52 (2025), Example 6.3, https://doi.org/10.1007/s10801-025-01477-5.
3. M. Waegell and P. K. Aravind, *The Penrose dodecahedron and the Witting polytope are identical in* \(\mathbb{CP}^3\), arXiv:1701.06512v2, https://arxiv.org/abs/1701.06512.
