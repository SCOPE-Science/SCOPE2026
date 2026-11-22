# An elementary inradius density and a parabolic rare-shape law for unit-base random-direction triangles

## Finding

Fix one side of a Euclidean triangle to have length \(1\), and select its three unoriented side directions independently and uniformly modulo \(\pi\). These directions determine the triangle's similarity class almost surely. Let \(R\) be its inradius. Its complete density, including the exact endpoint domain, is

\[
p(r)=\frac{16}{\pi^2(1+4r^2)}\left[\arccos(2r)+2r\operatorname{arcosh}\left(\frac{1}{2r}\right)\right],\qquad 0<r<\frac12.
\]

The density is zero off \([0,1/2]\), continuous at both endpoints with \(p(0)=8/\pi\) and \(p(1/2)=0\), and has exactly one strict interior maximum, at \(r_*=0.0764841973658\ldots\), where \(p(r_*)=2.8664645227022\ldots\). The distribution has the sharp expansions

\[
\Pr(R\le t)=\frac8\pi t+\frac{16}{\pi^2}t^2\log\frac1t+O(t^2),\qquad t\downarrow0,
\]

\[
\Pr\left(R>\frac12-h\right)=\frac{64}{3\pi^2}h^{3/2}+O(h^{5/2}),\qquad h\downarrow0.
\]

These two endpoints have distinct conditional shape laws. Write \(\alpha,\beta\) for the two angles adjacent to the unit side and put

\[
u=\frac{\alpha+\beta}{2},\qquad v=\frac{\alpha-\beta}{2}.
\]

For the upper-tail event \(R>1/2-h\), the pair

\[
\left(\frac{\pi/2-u}{2h},\frac{v}{2\sqrt h}\right)
\]

converges in total variation to uniform area probability on \(\{(a,b):a\ge0,\ a+b^2<1\}\), whose area is \(4/3\). For the lower-tail event \(R\le t\), with probability tending to \(1/2\) either adjacent angle is the small one; its ratio to \(2t\) and the other angle divided by \(\pi\) converge jointly to independent \(\operatorname{Uniform}(0,1)\) variables. The mixture and upper-limit assertions concern this unit-side model, not fixed circumradius or uniform random vertices.

## Assumptions and scope

Let the three independent directions be sampled modulo \(\pi\). Anchor one of them, and express the remaining two relative to it; they are independent uniform points on a circle of circumference \(\pi\). Their ordered cyclic gap lengths, with the distinguished direction as starting point, have joint Dirichlet\((1,1,1)\) law after division by \(\pi\). The triangle's unordered interior angles are precisely those three gaps (up to reflection); hence, labeling the angles adjacent to the chosen unit side as \(\alpha,\beta\), their joint density is \(2/\pi^2\) on

\[
\{(\alpha,\beta):\alpha>0,\ \beta>0,\ \alpha+\beta<\pi\}.
\]

This is the same uniform angular simplex studied in earlier random-triangle literature. The scale is fixed by the *predesignated* side, not by the longest side, perimeter, area, or circumradius. All three directions are assumed independent and continuous; parallel and concurrent degeneracies are null events. Every probability here is with respect to this angular sampling.

## Proof

**1. Inradius as an angular functional.** The two segments of the unit base meeting the incircle's tangency point have lengths \(R\cot(\alpha/2)\) and \(R\cot(\beta/2)\), so

\[
R=\frac{1}{\cot(\alpha/2)+\cot(\beta/2)}
 =\frac{\cos v-\cos u}{2\sin u}.
\]

The change of coordinates has Jacobian \(d\alpha\,d\beta=2\,du\,dv\); consequently \((u,v)\) has density \(4/\pi^2\) on \(0<u<\pi/2,\ |v|<u\). Since \(\cos v\le1\), the maximum at each \(u\) is \(\tfrac12\tan(u/2)\), increasing to \(1/2\). Thus \(0<R<1/2\) almost surely; the supremum occurs only in the boundary limit \((u,v)=(\pi/2,0)\).

**2. Exact exceedance and density.** For \(0<r<1/2\), put \(u_0=2\arctan(2r)\). At fixed \(u\), the condition \(R>r\) is equivalent to \(|v|<\arccos(\cos u+2r\sin u)\), possible exactly for \(u>u_0\). Therefore

\[
S(r):=\Pr(R>r)=\frac8{\pi^2}\int_{2\arctan(2r)}^{\pi/2}\arccos(\cos u+2r\sin u)\,du.
\]

The moving lower endpoint contributes nothing when differentiating, because its integrand is zero there. Accordingly,

\[
-S'(r)=\frac{16}{\pi^2}\int_{u_0}^{\pi/2}\frac{\sin u}{\sqrt{1-(\cos u+2r\sin u)^2}}\,du.
\]

For evaluation, set \(q=\sqrt{1+4r^2}\), \(\delta=\arctan(2r)\), and \(z=u-\delta\). The denominator becomes \(\sqrt{1-q^2\cos^2z}\), and the numerator is \(\sin u=(\sin z+2r\cos z)/q\). The transformed limits are \(\delta\) and \(\pi/2-\delta\). The two elementary primitives are

\[
\int\frac{\sin z\,dz}{\sqrt{1-q^2\cos^2z}}
=-\frac1q\arcsin(q\cos z),
\]

\[
\int\frac{\cos z\,dz}{\sqrt{1-q^2\cos^2z}}
=\frac1q\operatorname{arcosh}\left(\frac{q\sin z}{2r}\right).
\]

At the lower limit their inverse-function arguments equal \(1\); at the upper limit they are \(2r\) and \(1/(2r)\), respectively. Substitution yields the displayed elementary density, with the precise factor \(16/\pi^2\). The angular-domain construction shows \(S(0)=1\) and \(S(1/2)=0\), proving its normalization without numerical integration.

**3. Exactly one mode.** Let

\[
A(r)=\arccos(2r)+2r\operatorname{arcosh}\left(\frac1{2r}\right),\qquad Q(r)=1+4r^2.
\]

Here \(A(r)>0\), and direct differentiation gives

\[
A'(r)=2\operatorname{arcosh}\left(\frac1{2r}\right)-\frac4{\sqrt{1-4r^2}},
\quad
A''(r)=-\frac2{r\sqrt{1-4r^2}}-\frac{16r}{(1-4r^2)^{3/2}}<0.
\]

The sign of \(p'(r)\) equals the sign of \(H(r)=Q(r)A'(r)-8rA(r)\). Its derivative is exactly \(H'(r)=Q(r)A''(r)-8A(r)<0\), while \(H(0+)=+\infty\) and \(H(1/2-)=-\infty\). Hence \(H\) has exactly one zero and the density is strictly increasing before it and strictly decreasing afterward. Bisection gives the numerical mode quoted above; its existence and uniqueness are analytic, not inferred from bisection.

**4. Sharp endpoints and marked shapes.** As \(r\downarrow0\), \(\arccos(2r)=\pi/2-2r+O(r^3)\) and \(\operatorname{arcosh}(1/(2r))=\log(1/r)+O(r^2)\). Thus

\[
p(r)=\frac8\pi+\frac{32}{\pi^2}r\log\frac1r+O(r).
\]

Integrating gives the lower-tail formula, including its logarithmic second term. As \(h\downarrow0\), the square-root expansions of the two inverse functions at their endpoints yield \(p(1/2-h)=32\sqrt h/\pi^2+O(h^{3/2})\). Integrating again proves the upper-tail formula.

For the upper marked law, put \(u=\pi/2-d\). Taylor expansion in the unique near-maximizing region gives

\[
\frac12-R=\frac d2+\frac{v^2}4+O(d^2+d v^2+v^4).
\]

On \(R>1/2-h\), necessarily \(d=O(h)\) and \(v=O(\sqrt h)\); this follows directly from \(u>2\arctan(2R)\) and \(\cos v>\cos u+2R\sin u\). Setting \(d=2ha\) and \(v=2\sqrt h\,b\), the rescaled admissible sets converge in area to \(a\ge0,\ a+b^2<1\). The original \((u,v)\) density is constant and the Jacobian is \(4h^{3/2}\); dominated convergence on a fixed containing rectangle gives total-variation convergence to uniform measure on the limit domain. Its area is \(4/3\), giving once more \((4/\pi^2)(4h^{3/2})(4/3)=64h^{3/2}/(3\pi^2)\).

For the lower marked law, the only zero-inradius boundary is \(\alpha=0\) or \(\beta=0\). For \(\beta\) bounded away from \(0\) and \(\pi\), the exact cotangent relation gives \(R=\alpha/2+O(\alpha^2)\) uniformly as \(\alpha\to0\), and symmetrically for \(\beta\to0\). On a strip \(0<\alpha<2t\), the scaled variables \(\alpha/(2t)\) and \(\beta/\pi\) have asymptotically constant joint density. The intersection of two corner strips is \(O(t^2)\), and the omitted endpoints of the surviving long-angle coordinate have vanishing relative mass as the cutoff tends to zero. Each of the two side strips contributes \(4t/\pi+o(t)\). This establishes the fair mixture and independent uniform marks, with total-variation convergence.

## Verification

The attached standard-library script `VERIFY.py` recomputes the density integral, independently integrates the original inverse-cosine survival representation at six thresholds, checks the unique mode numerically, compares both endpoint normalizations, and uses a seeded angular-simplex simulation. It prints `ALL_CHECKS_PASSED` when those finite diagnostics meet their stated tolerances. The analytical argument above supplies the proof; none of the numerical checks is used to certify an infinite-domain claim.

## Relationship to prior work

The uniform-angle simplex itself is classical and is not claimed as new. The earlier study by Daley, Ebert and Swift of a triangle scaled to a unit side derives distributions of side ratios, two side-order statistics, and area. Its published abstract does not list the incircle-radius density; however its full text was not accessible for a decisive whole-paper comparison. Edelman and Strang's 2014 note presents the uniform-angle simplex and distinguishes it from Gaussian-vertex sampling, without providing this inradius evaluation in the inspected relevant material. Gates's more general 1994 line-set shape model is a plausible broader framework; its accessible abstract addresses shape and maximum-angle distributions, but the complete text was not available. The claimed novelty is narrowly the evaluated elementary **unit-base inradius density**, its rigorous single-mode property, the two endpoint expansions, and their conditional shapes—not the triangle model or the fact that any scalar distribution is the pushforward of the known full angle law.

An exact inradius expectation/variance for triangles of *unit circumradius*, sampled by three uniform points on a circle, was published by Kórus in 2020; that normalization produces a different inradius random variable. A published record in the open mathematical database titled *The full inradius law and two contrasting tails of random cyclic triangles* also uses fixed circumradius and therefore does not directly evaluate the unit-side random variable. Since not every potentially relevant historical full text was inspectable, historical priority is provisional.

## Limitations

The theorem is restricted to planar triangles generated by independent uniform **directions** and scaled by one predesignated side. It does not apply without modification to area-uniform vertices, random lines with differently weighted directional laws, normalized longest sides, or fixed circumradius. The two conditional laws concern the specified opposite endpoints, not an interpolation for other shape constraints. The historical coverage comparison has access limitations, and no independent mathematical audit has been performed.

## References

1. D. J. Daley, S. Ebert and R. J. Swift, *Size distributions in random triangles*, *Journal of Applied Probability* 51A (2014), 283–295, DOI: https://doi.org/10.1239/jap/1417528481. A public conference-program entry of June 13, 2013 appears at https://www.mat.umk.pl/panel/wp-content/uploads/biuletyn-informacyjny-2_2013.pdf#page=39.
2. A. Edelman and G. Strang, *Random Triangle Theory with Geometry and Applications*, dated September 27, 2014, https://math.mit.edu/~edelman/publications/random_triangle.pdf.
3. J. Gates, *Shape distributions for planar triangles by dual construction*, *Advances in Applied Probability* 26 (1994), 324–333, DOI: https://doi.org/10.2307/1427438.
4. P. Kórus, *Average Values of Triangles*, *Fundamental Journal of Mathematics and Applications* 3 (2020), 57–60, DOI: https://doi.org/10.33401/fujma.692916.
