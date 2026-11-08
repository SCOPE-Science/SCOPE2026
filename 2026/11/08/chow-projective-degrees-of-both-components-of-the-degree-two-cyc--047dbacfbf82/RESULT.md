# Chow-projective degrees of both components of the degree-two cycle variety

## Finding

Let \(n\ge3\) and \(1\le p\le n-2\) be integers, and let \(C_{p,2}(\mathbb P^n)\) be the **reduced** complex Chow variety of effective dimension-\(p\), degree-two cycles, endowed with its standard projective embedding by Chow forms. It has two irreducible components: \(Q_{p,n}\), the closure of smooth quadric hypersurfaces in their own \((p+1)\)-planes, and \(R_{p,n}\), the locus of sums of two linear \(p\)-planes. This finding computes **both** components' projective degrees by a finite expression valid for every \(p,n\), and determines exactly which components contribute to the top-dimensional degree of the entire Chow variety.

Put
\[
N=n+1,\quad k=p+1,\quad K=p+2,\quad g=K(N-K),\quad r=\binom{K+1}{2},\quad D=g+r-1,\quad d=k(N-k).
\]
For an index subset \(I\subset\{0,\ldots,n\}\) with \(|I|=K\), define
\[
H_I=-\sum_{a\in I}a,\quad
\Delta_I=\prod_{a\in I}\prod_{b\notin I}(b-a),\quad
S_{I,j}=[t^j]\prod_{a\le b,\ a,b\in I}(1-(a+b)t)^{-1}.
\]
(The product uses each unordered pair, including diagonal pairs, exactly once.) Then the exact integer degrees are
\[
\boxed{\deg Q_{p,n}=\sum_{\substack{I\subset\{0,\ldots,n\}\\|I|=K}}\frac{1}{\Delta_I}
\sum_{j=0}^{g}\binom{D}{r-1+j}(2H_I)^{g-j}S_{I,j}},
\]
\[
\boxed{\deg R_{p,n}=
\frac12\binom{2d}{d}
\left(\frac{d!\prod_{i=0}^{k-1}i!}{\prod_{i=0}^{k-1}(N-k+i)!}\right)^2}.
\]
The first sum is rational term by term but has an integer value. The dimensions obey
\[
\boxed{\dim R_{p,n}-\dim Q_{p,n}=\frac p2(2n-3p-3)}.
\]
Consequently the degree of the full (possibly non-equidimensional) reduced Chow variety—defined by its top-dimensional Hilbert-polynomial coefficient—is \(\deg R_{p,n}\) for \(2n>3p+3\), is \(\deg Q_{p,n}\) for \(2n<3p+3\), and is their **sum** exactly at \(2n=3p+3\). The tie occurs precisely for odd \(p\), with \(n=3(p+1)/2\), inside the stated domain.

Some exact values, each with the dimensions of the two components ordered as \((\dim Q,\dim R)\), are:

| \((p,n)\) | \((\dim Q,\dim R)\) | \(\deg Q\) | \(\deg R\) | degree of full variety |
| --- | --- | ---: | ---: | ---: |
| \((1,3)\) | \((8,8)\) | 92 | 140 | 232 |
| \((1,4)\) | \((11,12)\) | 6620 | 11550 | 11550 |
| \((2,4)\) | \((13,12)\) | 2865 | 11550 | 2865 |
| \((3,6)\) | \((24,24)\) | 6522193496 | 288592936632 | 295115130128 |

The \((1,3)\) degrees 92 and 140 were computed previously by Bürgisser–Kohn–Lairez–Sturmfels and serve as a boundary check, not a novelty claim. The all-parameter formulas and the higher-dimensional numerical instances are the claimed contribution.

## Assumptions and scope

Work over \(\mathbb C\), with the reduced variety and the standard Chow-form projective polarization. Require integers \(n\ge3\) and \(1\le p\le n-2\): the excluded zero-dimensional cycle and divisor extremes have a different component containment pattern. Degree of a non-equidimensional union always means degree of its maximal-dimensional components, with distinct maximal-dimensional components' degrees added. The numbers do not depend on a normalization of Chow coordinates.

## Proof

**1. Two components and their dimensions.** An irreducible nondegenerate projective variety of degree two is a quadric hypersurface in its span; reducible degree-two cycles are sums of two degree-one linear cycles. For \(1\le p\le n-2\), a general union of two \(p\)-planes does not lie inside a \((p+1)\)-plane. Thus the two images are distinct irreducible components. Let \(V=\mathbb C^N\), \(G=\operatorname{Gr}(k,V)\), and \(B=\operatorname{Gr}(K,V)\) with \(k=p+1\), \(K=p+2\). The first component is the generically one-to-one image of \(Y=\mathbb P(\operatorname{Sym}^2S^\vee)\to B\), where \(S\) is the tautological rank-\(K\) subbundle; its general member has a uniquely determined span. The second is the generically one-to-one image of \(\operatorname{Sym}^2G\), since a general cycle identifies its two distinct irreducible components. Hence \(\dim Q=g+r-1=D\) and \(\dim R=2d\). Direct simplification gives \(2d-D=p(2n-3p-3)/2\).

**2. Polarization on the pair component.** Write \(h_1,h_2\) for the Plücker hyperplane classes on \(G\times G\). Multiplicativity of Chow forms makes the pullback of the Chow hyperplane class \(h_1+h_2\). The map \(G\times G\to R\) has generic degree two (factor transposition). Since \(\dim G=d\),
\[
\deg R=\frac12\int_{G\times G}(h_1+h_2)^{2d}=
\frac12\binom{2d}{d}\left(\int_Gh^d\right)^2.
\]
The hook-length formula for the rectangular Grassmannian gives
\(\int_G h^d=d!\prod_{i=0}^{k-1}i!/\prod_{i=0}^{k-1}(N-k+i)!\).

**3. Polarization on the quadric component.** On \(Y=\mathbb P(E)\) with \(E=\operatorname{Sym}^2S^\vee\), use the **lines** convention, so \(\mathcal O_Y(-1)\subset\pi^*E\). Set \(\xi=c_1(\mathcal O_Y(1))\) and \(h=c_1(\det S^\vee)\). A codimension-\(p+1=k\) linear subspace is expressed by \(k\) linear forms. Restricting their wedge to \(S\) gives an element of \(\bigwedge^kS^\vee\cong S\otimes\det S^\vee\). Evaluating a quadratic form \(q\in\operatorname{Sym}^2S^\vee\) on this element produces a quadratic Chow expression with two determinant factors. This defines the Chow map from the tautological line after tensoring by \((\det S)^{\otimes2}\), so its hyperplane class pulls back to
\[
\mathcal L=c_1\bigl(\mathcal O_Y(1)\otimes(\det S^\vee)^{\otimes2}\bigr)=\xi+2h.
\]
The generic quadric has unique span; therefore its image has degree \(\int_Y(\xi+2h)^D\), with no generic-map-degree divisor. For the stated lines convention, the projective bundle pushforward is \(\pi_*(\xi^{r-1+j})=s_j(E)\), where \(s(E)=c(E)^{-1}\). Thus
\[
\deg Q=\sum_{j=0}^{g}\binom D{r-1+j}\int_B(2h)^{g-j}s_j(E).
\]

**4. Explicit all-parameter evaluation.** Let a one-dimensional torus act diagonally on \(V\) with distinct integer weights \(0,1,\ldots,n\). At a fixed point \(I\) of \(B=\operatorname{Gr}(K,N)\), the Chern roots of \(S^\vee\) are \(-a\) for \(a\in I\); hence \(h\) evaluates to \(H_I\), the roots of \(E=\operatorname{Sym}^2S^\vee\) are \(-(a+b)\) for unordered pairs in \(I\), and the equivariant tangent Euler class is \(\Delta_I=\prod_{a\in I,b\notin I}(b-a)\). The localization formula for top-degree characteristic numbers gives exactly the displayed finite sum for \(\deg Q\). Denominators are harmless because the total equals the integral of an integral power of the Chow hyperplane class. The dimension comparison then proves the final three-way rule.

## Verification

The accompanying standalone `CHECK.py` uses only Python's standard library. Run `python3 CHECK.py`. Its first calculation uses the displayed fixed-point sum with two independent sets of distinct weights; its second calculation expands the corresponding symmetric Chern-root polynomial and extracts its top Grassmannian Schur coefficient by multiplying with the Vandermonde determinant. The methods agree for \((p,n)=(1,3),(1,4),(2,4),(1,5),(2,5)\). Additional exact fixed-point computations cover \((3,6)\), including the first higher-dimensional equal-dimension wall. The published \((1,3)\) degrees \(92,140\) are reproduced. This checks arithmetic and sign conventions but does not replace the general geometric proof.

## Relationship to prior work

Chen–Hu–Ma (2026, arXiv:2610.39498) give the two-component projective-bundle/symmetric-product description and compute rational cohomology and Poincaré series. Those structures are used here; their examined introduction and Sections 3–5 do not give the above Chow-embedding degree formulas. Bürgisser–Kohn–Lairez–Sturmfels (2015, arXiv:1508.07219, Section 2) compute the exact degrees \(92\) and \(140\) of the two components for conics and pairs of lines in \(\mathbb P^3\), and hence the total \(232\); that case is expressly prior work. The present result is a uniform intersection-theoretic evaluation and higher-dimensional calculation, not a new derivation of the known case. The general decomposition of degree-two Chow varieties and Grassmannian intersection machinery are standard ingredients, not newly claimed.

## Limitations

This computes projective degrees, not defining ideals, scheme-theoretic singularities, or full Hilbert polynomials. The degree of a non-equidimensional union excludes lower-dimensional components by definition. The finite arithmetic checks are sample validations; the infinite range depends on the displayed proof. Literature priority for the all-parameter formula is not independently certified: another source may derive the same degrees from general projective-bundle intersection theory. No assertion of a new general Chow-variety decomposition is made.

## References

1. Y. Chen, W. Hu and D. Ma, *Poincaré series of degree-two Chow varieties*, arXiv:2610.39498v1 (first public submission 2026-10-29), Sections 1, 3–5. https://arxiv.org/abs/2610.39498
2. P. Bürgisser, K. Kohn, P. Lairez and B. Sturmfels, *Computing the Chow variety of quadratic space curves*, arXiv:1508.07219 (2015), Section 2. https://arxiv.org/abs/1508.07219
3. W. Hu, *The multiplicative group action on singular varieties and Chow varieties*, J. Pure Appl. Algebra 225 (2021), Article 106667, especially Section 4.2 on components. https://doi.org/10.1016/j.jpaa.2021.106667
4. Standard projective bundle, Schubert integration, hook-length and torus localization formulas are used in their conventional forms.
