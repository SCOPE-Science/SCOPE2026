# An integral length-27 complete-intersection Fano scheme on a one-line cubic

## Finding

For the primitive cubic surface over the integers
\[
\mathcal X:\quad xy^2+yt^2+z^3=0\quad\subset\mathbf P^3_{\mathbf Z},
\]
let \(F_1(\mathcal X/\mathbf Z)\) be its relative Hilbert scheme of projective lines (equivalently, of subschemes with Hilbert polynomial \(m+1\)). The complete integral scheme admits the following two-generator, two-relation presentation:
\[
\boxed{F_1(\mathcal X/\mathbf Z)\cong
\operatorname{Spec}\frac{\mathbf Z[c,d]}{\left(
 c^3+9c^2d^4+6cd^8+d^{12},\;
 3c^2d+6cd^5+2d^9
 \right)}.}
\]
This scheme is **finite flat of rank \(27\)** over \(\mathbf Z\). Its geometric fiber over every field, including characteristics \(2\) and \(3\), is supported at just the single line \(L:\,y=z=0\), and is a zero-dimensional local complete-intersection Gorenstein scheme of length \(27\) and embedding dimension \(2\). With \(\deg c=4\) and \(\deg d=1\), the fiber algebra is positively graded with Hilbert series
\[
\boxed{H(s)=\frac{(1-s^9)(1-s^{12})}{(1-s)(1-s^4)}}
\]
and one-dimensional socle in weight \(16\). In characteristic \(3\) there is a particularly transparent specialization:
\[
\boxed{F_1(\mathcal X_{\mathbf F_3})\cong
\operatorname{Spec}\frac{\mathbf F_3[c,d]}{(c^3,d^9)}.}
\]
The classical fact that the corresponding complex cubic has exactly one *geometric* line, and the general enumerative multiplicity \(27\), are **background**, not novelty assertions. The claim is the exact **integral** and bad-characteristic local algebra, including the weighted degeneration, not the raw count \(27\).

## Assumptions and scope

Here \(\mathbf P^3_{\mathbf Z}\) has homogeneous coordinates \([x:y:z:t]\), and \(F_1\) is the closed subscheme of \(\operatorname{Gr}(2,4)_{\mathbf Z}\) cut out by the cubic's restriction to the tautological rank-two bundle. All assertions refer to this fixed integral equation, not to every form in its characteristic-zero projective-equivalence class. For a geometric fiber, the point \(L\) means its corresponding point of the Grassmannian, not a line of multiplicity \(27\) as an effective divisor on the cubic. The indicated grading belongs to the infinitesimal parameter ring, not to the homogeneous coordinates of \(\mathcal X\).

## Proof

**1. Every geometric line lies in one Grassmann chart, in every characteristic.** Let \(P=[0:1:0:0]\). The projective line \(K:\,x=t=0\) meets \(\mathcal X\) only at the geometric support \(P\), because restriction of the cubic equation to \(K\) is \(z^3=0\). No geometric projective line on \(\mathcal X\) contains \(P\). Indeed, were a line through \(P\) spanned by \(P\) and \(Q=[\alpha:\beta:\gamma:\delta]\), expand the defining cubic at \(sP+uQ\):
\[
\mathcal F(sP+uQ)
 =\alpha s^2u+(2\alpha\beta+\delta^2)su^2
 +(\alpha\beta^2+\beta\delta^2+\gamma^3)u^3.
\]
Its vanishing as a polynomial in \(s,u\) forces \(\alpha=\delta=\gamma=0\) over **any** field, so \(Q=P\), a contradiction. A line on \(\mathcal X\) whose projection to the \([x:t]\)-coordinate plane is not an isomorphism must meet \(K\) and hence contain \(P\). Thus every geometric point of the line scheme lies in the standard affine Grassmann chart where each line is uniquely written
\[
y=ax+bt,\qquad z=cx+dt.
\]
Because the Fano scheme is of finite type over \(\mathbf Z\), its closed complement to this chart has no geometric points in any fiber and is therefore empty as a scheme. Consequently this chart covers the entire relative Hilbert scheme, including nilpotent directions.

**2. Four equations, then elimination.** Substitute \(y=ax+bt\) and \(z=cx+dt\) into \(xy^2+yt^2+z^3\). Its coefficients of \(x^3,x^2t,xt^2,t^3\) are respectively
\[
a^2+c^3,\quad 2ab+3c^2d,\quad b^2+a+3cd^2,\quad b+d^3.
\]
The last two are monic linear equations in \(a\) and \(b\) after elimination:
\[
b=-d^3,\qquad a=-d^6-3cd^2.
\]
Substituting into the first two yields exactly the two displayed integral relations. Every step is an isomorphism of affine \(\mathbf Z\)-schemes; in particular no division by \(2\) or \(3\) has been used.

**3. Geometric support and complete intersection.** Write \(f=c^3+9c^2d^4+6cd^8+d^{12}\) and \(g=3c^2d+6cd^5+2d^9\). If \(d=0\), \(f=0\) forces \(c=0\). If \(d\ne0\), put \(u=c/d^4\). Then \(f/d^{12}\) and \(g/d^9\) become
\[
F(u)=u^3+9u^2+6u+1,
\qquad G(u)=3u^2+6u+2.
\]
Their integer Sylvester resultant is \(\operatorname{Res}(F,G)=-1\), as verified exactly by the displayed finite determinant in the accompanying script. It is therefore a unit in every field, and \(F\) and \(G\) share no root in any characteristic. Hence every geometric fiber of \(\mathbf Z[c,d]/(f,g)\) has exactly one support point, \(c=d=0\).

The equations \(f,g\) are weighted homogeneous of weights \(12,9\), where \(\deg c=4\), \(\deg d=1\). As they have no common projective zero over any field, they form a regular sequence in the two-dimensional polynomial ring over each field. Thus every geometric fiber is a zero-dimensional complete intersection; the Koszul resolution gives its Hilbert series, total length \(12\cdot9/(4\cdot1)=27\), and Gorenstein socle weight \(12+9-4-1=16\). Both relations have vanishing linear terms at the origin, and the tangent space has dimension \(2\).

The relative Fano scheme is projective as a closed subscheme of the Grassmannian, but has just been shown affine; thus it is finite over \(\mathbf Z\). Its generic fiber has length \(27\) and every geometric special fiber has length \(27\). For the finite \(\mathbf Z\)-module underlying the coordinate ring, any nonzero torsion would increase the dimension of the special fiber at some prime beyond its generic rank. Therefore the module is torsion-free and hence free of rank \(27\); the morphism is finite flat. This uses the actual fiber dimensions, not an unsupported assumption that a finite complete intersection is automatically flat over the base.

**4. Characteristic-three special fiber.** Reducing the two equations modulo \(3\) gives \(f=c^3+d^{12}\) and \(g=2d^9\). Thus the ideal is exactly \((c^3,d^9)\), proving the displayed local Artin algebra and independently recovering length \(3\cdot9=27\) in this exceptional characteristic. In characteristic \(2\), the equations instead reduce to \(f=c^3+c^2d^4+d^{12}\) and \(g=c^2d\), which also form a zero-dimensional complete intersection by the uniform resultant argument.

## Verification

Run `python3 verify.py` using Python 3's standard library; `verification_output.txt` records the actual execution. The verifier calculates the exact \(5\times5\) Sylvester determinant \(-1\), expands the Grassmann-chart coefficient identities, checks the rational Hilbert series coefficients and total length \(27\), and exhaustively enumerates projective lines over \(\mathbf F_2,\mathbf F_3,\mathbf F_5,\mathbf F_7\). It prints `ALL_CHECKS_PASSED`. Finite-field enumeration checks only small characteristic examples. The proof above—not those enumerations—establishes the integral scheme isomorphism and every geometric fiber.

## Relationship to prior work

Brundu and Logar's classical classification identifies this cubic as the unique complex cubic surface having only one geometric line (the T1 model). Alper, Bogart and Velasco, *A lower bound for the determinantal complexity of a hypersurface*, arXiv:1505.02205v1 (8 May 2015), explicitly use this same equation and prove its determinantal complexity over characteristic zero. Both references make the object natural; neither contains the two-relation integral Hilbert algebra asserted here.

There is also stronger directly relevant *later* prior work: Alexander Golys's public Mathematics Stack Exchange answer of 24 March 2024 to *Find all lines on cubic surface* treats a projectively equivalent one-line \(E_6\) cubic over characteristic different from two, gives four Grassmann-chart equations and a length-\(27\) monomial-basis calculation. Separately, a MathOverflow discussion in 2020 explains why finite Fano schemes of cubic surfaces have total multiplicity \(27\). Thus even the **nonreduced length \(27\)** and the existence of an explicit field-level scheme chart are not claimed new. The present scope is the fixed integer model's integral two-equation presentation, its proof of flatness uniformly at primes \(2\) and \(3\), and particularly its exactly monomial characteristic-three fiber and graded socle structure. None of these more specific statements was identified in the inspected sources; further specialized algebraic-geometry sources may contain equivalent computations.

## Limitations

The statement concerns the indicated integral normal form and relative scheme of lines. The integral presentation is not a classification of all integral models or quadratic/projective twists. No claim is made that its generic length \(27\) is a new enumerative phenomenon. The proof does not establish historical priority against every earlier source; independent mathematical review has not been performed. The verifier's bounded finite-field enumeration is not a proof in arbitrary characteristic.

## References

1. J. Alper, T. Bogart, M. Velasco, *A lower bound for the determinantal complexity of a hypersurface*, arXiv:1505.02205v1 (first public preprint 2015-05-08), Introduction, Theorem 1.8 and Brundu–Logar reference. https://arxiv.org/html/1505.02205v1
2. M. Brundu and A. Logar, *Parametrization of the orbits of cubic surfaces*, Transactions of the American Mathematical Society 350 (1998), classification of the T1 surface; extended text *Classification of cubic surfaces with computational methods*, §2. https://mige-web.units.it/brundu/lavori/cubic1_long.pdf
3. A. Golys, answer (2024-03-24) to *Find all lines on cubic surface*, Mathematics Stack Exchange, including explicit Grassmann chart and length-27 local computation for a one-line cubic surface. https://math.stackexchange.com/questions/3944438/find-all-lines-on-cubic-surface
4. *Interpretation of “27” lines for cubic surface with rational double points*, MathOverflow discussion (2020), finite Fano-scheme multiplicities. https://mathoverflow.net/questions/370654/interpretation-of-27-lines-for-cubic-surface-with-rational-double-points
