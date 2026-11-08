# Galois logarithmic Gauss maps of four-corner rectangular curves

## Finding
For integers \(m,n\ge 2\) and \(\lambda\in\mathbb C^*\setminus\{1\}\), let \(C_{m,n,\lambda}\) be the closure in \(\mathbb P^1\times\mathbb P^1\) of the torus curve
\[
F(x,y)=1+x^m+y^n+\lambda x^my^n=0.
\]
The curve is smooth, geometrically connected, and has genus \((m-1)(n-1)\). Its logarithmic Gauss map \(\gamma=[xF_x:yF_y]\), extended across the boundary, is a **Galois covering of degree \(2mn\)**, with full deck group
\[
\operatorname{Deck}(\gamma)\cong(\mu_m\times\mu_n)\rtimes(\mathbb Z/2\mathbb Z),
\]
where the involution acts on each root-of-unity factor by inversion.

For either square root \(s\) of \(\lambda\), its complete branch-value set is
\[
\left\{0,\ \infty,\ \frac{m}{n}\frac{s-1}{s+1},\ \frac{m}{n}\frac{s+1}{s-1}\right\}.
\]
The four values are distinct. The ramification partition over \(0\) is \(m^{2n}\) (exactly \(2n\) points, each of index \(m\)); over \(\infty\) it is \(n^{2m}\); and over each of the two remaining values it is \(2^{mn}\). These are all branch points. Here partition powers denote multiplicities, not algebraic powers in an equation.

## Assumptions and scope
All curves and morphisms are over \(\mathbb C\). The parameters satisfy exactly \(m,n\in\mathbb Z_{\ge2}\), \(\lambda\ne0,1\). The logarithmic Gauss map is defined on the dense torus by the logarithmic normal \([xF_x:yF_y]\) and extended uniquely to the smooth projective curve. A Galois covering means that the function-field extension \(\mathbb C(C_{m,n,\lambda})/\mathbb C(\gamma)\) is Galois. This does not classify the full automorphism group of the curve.

## Proof
**Smoothness and irreducibility.** Set \(u=x^m\) and \(v=y^n\). In the torus, simultaneous vanishing of \(F_x,F_y\) would give \(u=v=-1/\lambda\), forcing \(F=1-1/\lambda\ne0\). The closure has bidegree \((m,n)\) and homogeneous equation
\[
X_0^mY_0^n+X_1^mY_0^n+X_0^mY_1^n+\lambda X_1^mY_1^n=0.
\]
It meets the four coordinate boundary divisors in respectively \(n,n,m,m\) distinct points, none at a toric fixed point. At the first two, the derivative in the \(y\)-direction is nonzero; at the other two, the derivative in the \(x\)-direction is nonzero. Thus the closure is smooth. In \(\mathbb C(x)\) the equation becomes
\[
y^n=-\frac{1+x^m}{1+\lambda x^m}.
\]
The rational function on the right has simple zeros at the \(m\) distinct roots of \(1+x^m\) and simple poles at the \(m\) distinct roots of \(1+\lambda x^m\), with the sets disjoint. The equation is Eisenstein at any simple zero, so irreducible over \(\mathbb C(x)\). Therefore the smooth closure is connected and irreducible. The bidegree-genus formula gives \(g=(m-1)(n-1)\).

**The intermediate rational map.** On \(C\), \(v=-(1+u)/(1+\lambda u)\). With \(c=(m/n)(\lambda-1)\), direct differentiation gives
\[
\frac{xF_x}{yF_y}=\frac{mu(1+\lambda v)}{nv(1+\lambda u)}
=h(u):=\frac{cu}{(1+u)(1+\lambda u)}.
\]
This equality holds as a rational-function identity and hence determines the extension to the boundary. The map \(u:C\to\mathbb P^1\) has degree \(mn\): the rational map \(x\mapsto x^m\) has degree \(m\), and the displayed Eisenstein equation in \(y\) gives degree \(n\) over \(\mathbb C(x)\). The function \(h:\mathbb P^1\to\mathbb P^1\) has degree \(2\), so \(\deg\gamma=2mn\).

**The complete deck group.** For \(\zeta^m=\eta^n=1\), the rotations \((x,y)\mapsto(\zeta x,\eta y)\) preserve the curve and \(\gamma\). Choose \(\alpha,\beta\in\mathbb C^*\) with \(\alpha^m=\beta^n=1/\lambda\), and put \(\sigma(x,y)=(\alpha/x,\beta/y)\). The substitution \((u,v)\mapsto(1/(\lambda u),1/(\lambda v))\) carries \(F\) to \(F/(\lambda uv)\), so \(\sigma\) restricts to an involution of the curve. Also \(h(1/(\lambda u))=h(u)\), hence it preserves \(\gamma\). Conjugation by \(\sigma\) inverts each rotation. These transformations form a subgroup of order \(2mn\), exactly the degree of the finite covering, and therefore constitute its entire deck group. In particular the extension is Galois.

**All inertia groups.** The Kummer map \(\pi:C\to\mathbb P^1_u\) is branched only at \(u=0,\infty,-1,-1/\lambda\). Over \(u=0,\infty\) there are \(n\) points at each, all of ramification index \(m\), because \(x^m=u\) and \(v\) is a unit. Over \(u=-1,-1/\lambda\) there are \(m\) points at each, all of index \(n\), because \(v\) has respectively a simple zero and a simple pole. Elsewhere \(\pi\) is unramified. The function \(h\) takes the first pair of base values to \(0\), and the second pair to \(\infty\); it is unramified at all four.

Its derivative is
\[
h'(u)=\frac{c(1-\lambda u^2)}{(1+u)^2(1+\lambda u)^2}.
\]
Thus its only critical points are \(u=\pm1/s\), each simple, and their values are \(c/(1\pm s)^2\), equivalently the two nonzero finite values in the theorem. Because \(\lambda\ne0,1\), neither critical point lies over a branch point of \(\pi\), and the two critical values are distinct. Each lifts to \(mn\) unramified points of \(\pi\), now of index \(2\) under \(\gamma=h\circ\pi\). Multiplying indices in this composition proves exactly the four claimed ramification partitions.

**Exhaustion.** The total contribution to the ramification divisor is
\[
2n(m-1)+2m(n-1)+2mn=6mn-2m-2n,
\]
which agrees with \(2g-2+2\deg\gamma\) by Riemann--Hurwitz, independently corroborating that the list is exhaustive.

## Verification
The accompanying `verify.py` uses exact symbolic rational-function arithmetic to check the logarithmic derivative identity, reciprocal symmetry, the quadratic discriminant for \(h\), and the branch-value formulas. For five integral triples \((m,n,\lambda)\), it checks all partition degrees, the Riemann--Hurwitz identity, and constructs the claimed finite permutation group, with its inversion relations. Run `python verify.py` with SymPy installed. The recorded result is in `verify_output.txt`. These sample checks are not substituted for the general proof above.

## Relationship to prior work
Martin and Pochekutov (arXiv:1202.4659, 2012) develop logarithmic Gauss maps and their discriminants, including the general normalized Newton-volume degree bound, but their specific computed examples are a different torus cubic and a three-variable hypersurface. Madani and Nisse (arXiv:1205.2917, 2012) develop the general log-Gauss/coamoeba framework; they do not identify this regular four-branch covering. Lang (arXiv:1504.07256, 2015) treats (generalized) simple Harnack curves and totally real logarithmic Gauss maps, not the stated deck group and ramification partitions.

Hidalgo, Kontogeorgis, Leyton-Álvarez and Paramantzoglou (arXiv:1409.3063, 2014) study generalized Fermat curves and their Kummer automorphism groups. Their covering and automorphism results are relevant background when the two Kummer exponents coincide, but the inspected statements do not identify the logarithmic Gauss map or the present four-inertia partition. The claim does not assert a new abstract automorphism group of the underlying curve.

The general formula for the map degree is already predicted by Newton-polygon theory: the rectangle has normalized area \(2mn\), so the degree alone is not claimed as new. The independently assessed structural result is that this particular **entire positive-genus family has a Galois logarithmic Gauss map** with the explicit generalized-dihedral deck group and complete four-value branch profile. Searches did not identify this exact combination; historical priority remains provisional.

## Limitations
The statement is confined to characteristic zero and to the four-corner family with \(\lambda\ne0,1\). It does not classify all Galois logarithmic Gauss maps, the full automorphism groups of the curves, the real amoeba topology, or arithmetic descent of the automorphisms. Priority against unlocated specialist descriptions of Kummer covers and logarithmic Gauss maps remains open. No independent audit is claimed.

## References
- B. Martin and D. Pochekutov, *Discriminant and Singularities of Logarithmic Gauss Map, Examples and Application*, first submitted 2012-02-21, arXiv:1202.4659, https://arxiv.org/abs/1202.4659.
- F. Madani and M. Nisse, *Generalized logarithmic Gauss map and its relation to (co)amoebas*, first submitted 2012-05-14, arXiv:1205.2917, https://arxiv.org/abs/1205.2917.
- L. Lang, *A generalisation of simple Harnack curves*, first submitted 2015-04-27, arXiv:1504.07256, https://arxiv.org/abs/1504.07256.
- R. Hidalgo, A. Kontogeorgis, M. Leyton-Álvarez and P. Paramantzoglou, *Automorphisms of the Generalized Fermat curves*, first submitted 2014-09-10, arXiv:1409.3063, https://arxiv.org/abs/1409.3063.
