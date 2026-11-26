# Four Frobenius spectra of Fermat-quartic sextactic points

## Finding

Let \(k=\mathbb F_q\) have characteristic \(p\geq11\). On the smooth Fermat quartic \(C/k\) defined by \(X^4+Y^4+Z^4=0\), let \(S\) denote the reduced proper sextactic-point scheme, excluding the twelve hyperflexes. Then \(S\) is a finite étale scheme of degree \(48\) with equations
\[
S=V\bigl(X^4+Y^4+Z^4,\;(X^4-Y^4)(Y^4-Z^4)(Z^4-X^4)\bigr)\subset\mathbb P^2_k.
\]
The complete Frobenius cycle type and Hasse–Weil zeta function of \(S\) are as follows. In the two rows where \(q\equiv1\pmod8\), the quartic-residue condition is evaluated in \(k^\times\).

| Condition | Cycle type on 48 points | \(Z(S/k,T)\) |
|---|---|---|
| \(q\equiv1\pmod8\), \(-2\) a fourth power | \(1^{48}\) | \((1-T)^{-48}\) |
| \(q\equiv1\pmod8\), \(-2\) not a fourth power | \(2^{24}\) | \((1-T^2)^{-24}\) |
| \(q\equiv3\pmod8\) | \(1^{12}2^{18}\) | \((1-T)^{-12}(1-T^2)^{-18}\) |
| \(q\equiv5\pmod8\) | \(4^{12}\) | \((1-T^4)^{-12}\) |
| \(q\equiv7\pmod8\) | \(2^{24}\) | \((1-T^2)^{-24}\) |

For every \(m\geq1\), put \(d_m=\gcd(4,q^m-1)\), and write \(\delta_m=1\) when \((-2)^{(q^m-1)/d_m}=1\) in \(\mathbb F_{q^m}\), and \(\delta_m=0\) otherwise. Then
\[
\boxed{\#S(\mathbb F_{q^m})=3d_m^2\delta_m.}
\]
The common geometric splitting field in characteristic zero is \(K=\mathbb Q(i,\beta)\), where \(\beta^4=-2\), with Galois group \(D_4\) of order eight. Thus among rational primes \(p\geq11\), the four listed cycle types \(1^{48}\), \(2^{24}\), \(1^{12}2^{18}\), \(4^{12}\) occur with natural densities respectively \(1/8\), \(3/8\), \(1/4\), \(1/4\).

## Assumptions and scope

All finite-field claims concern the fixed Fermat equation over a finite field of characteristic at least eleven, not arbitrary twists or geometrically isomorphic plane quartics. A proper sextactic point is a nonhyperflex point where an osculating conic has contact order at least six, equivalently a nonhyperflex point of positive \(2K_C\)-Weierstrass weight in these characteristics. The characteristic threshold matters: the explicit classical \(2K_C\)-Wronskian used below has coefficient divisible by five and seven, so its ordinary characteristic-zero interpretation cannot automatically be carried into those characteristics. The result makes no claim about intrinsic sextactic schemes in characteristics two, three, five or seven.

## Proof

**1. Identify the intrinsic sextactic divisor.** On the affine chart \(Z=1\), with \(Y=y\neq0\) and \(X=x\), the curve is \(f=x^4+y^4+1=0\), and differentiation with respect to \(x\) along the curve is \(D=\partial_x-(x^3/y^3)\partial_y\). The six sections of \(2K_C\) are locally represented by \(1,x,y,x^2,xy,y^2\) up to a common nonvanishing trivializing factor. Their six-by-six jet Wronskian has the exact formal identity
\[
\det(D^i h_j)_{0\leq i,j\leq5}=4y''\left(45y^{(4)}y^{(3)}y''-9y^{(5)}(y'')^2-40(y^{(3)})^3\right),
\]
where primes denote \(D\)-derivatives. Substituting \(D(y)=-x^3/y^3\) and reducing by the curve relation yields the exact rational-function identity
\[
W=\frac{22680x^5(x^4-y^4)(x^4+y^4)^4(x^4+2y^4)(2x^4+y^4)}{y^{40}}.
\]
The integer coefficient is \(22680=2^3\cdot3^4\cdot5\cdot7\), a unit for \(p\geq11\). Since \(x^4+y^4=-1\) on this chart, away from the coordinate hyperflexes the zero set is precisely the union of the three equal-fourth-power conditions \(X^4=Y^4\), \(Y^4=Z^4\), \(Z^4=X^4\). Symmetry treats the remaining affine charts. At each of the twelve coordinate hyperflexes the Wronskian vanishes with order five; the displayed factors show that each of the other 48 zeros is simple. Independently, the total \(2K_C\)-Wronskian weight is \(6(8+5(2))=108=12\cdot5+48\). Hence the 48-point complete intersection \(S\) is exactly the proper sextactic scheme. The included symbolic verifier independently reconstructs both Wronskian identities; their displayed algebraic formulas specify the computation without relying on the verifier for an infinite-field proof.

**2. Decompose the 48 points into three disjoint arithmetic blocks.** None has a zero coordinate: for example \(X=0\) together with \(X^4+Y^4+Z^4=0\) forces the three factors of the second equation to be nonzero in characteristic at least eleven. Thus normalize \(X=1\) and set \(u=Y/X\), \(v=Z/X\). The three factors give precisely
\[
\begin{array}{lll}
S_1: & u^4=1, & v^4=-2,\\
S_2: & v^4=1, & u^4=-2,\\
S_3: & u^4=-1/2, & v^4=-1/2.
\end{array}
\]
The three blocks are pairwise disjoint because a point satisfying two equal-fourth-power conditions would satisfy \(X^4=Y^4=Z^4\), contradicting \(3X^4=0\). Each block has sixteen geometric points because all quartic polynomials are separable in the allowed characteristics. This proves finite étaleness and the displayed defining scheme.

**3. Determine all extension counts.** In a finite cyclic multiplicative group of order \(Q-1\), the equation \(t^4=a\) with \(a\neq0\) has \(d=\gcd(4,Q-1)\) solutions if \(a^{(Q-1)/d}=1\), and zero otherwise. Every block therefore contributes either \(d^2\) or zero rational points: the auxiliary equations \(t^4=1\) always have \(d\) solutions, and \(-1/2\) is a fourth power if and only if \(-2\) is, by inversion. Applying this for \(Q=q^m\) proves \(\#S(\mathbb F_{q^m})=3d_m^2\delta_m\).

**4. Deduce the precise Frobenius cycles.** The multiplicative-group formula shows \(-2\) is a square in \(\mathbb F_q\) precisely when \(q\equiv1,3\pmod8\), and a nonsquare when \(q\equiv5,7\pmod8\). If \(q\equiv1\pmod8\), all fourth roots of unity are rational; either all 48 points are rational or none are, according to the quartic-residue condition. In the latter case every point splits over the quadratic extension, giving 24 transpositions. For \(q\equiv3\pmod8\), the formula gives 12 rational points and 48 points over the quadratic extension, so Frobenius has twelve fixed points and eighteen transpositions. For \(q\equiv7\pmod8\), it gives zero rational points and 48 over the quadratic extension, so there are 24 transpositions. For \(q\equiv5\pmod8\), there are zero points already over the quadratic extension, but all 48 over the fourth-degree extension, yielding twelve four-cycles. These cases give the table and the zeta functions \(Z(S/k,T)=\prod_{P\ \mathrm{closed}}(1-T^{\deg P})^{-1}\).

**5. Compute the arithmetic Galois group and prime densities.** Every coordinate in the three blocks lies in \(K=\mathbb Q(i,\beta)\) with \(\beta^4=-2\), and these coordinates generate that field. Eisenstein's criterion at two makes \(\mathbb Q(\beta)\) a degree-four extension. The field does not already contain \(i\): otherwise it would equal \(\mathbb Q(\zeta_8)\), since \(\beta^2/i=\sqrt2\), but then it would contain the real element \(2^{1/4}=\beta/\zeta_8\), contradicting the fact that the real subfield of \(\mathbb Q(\zeta_8)\) has degree two. Thus \([K:\mathbb Q]=8\). The automorphisms \(r:\beta\mapsto i\beta,\;i\mapsto i\) and \(s:\beta\mapsto\beta,\;i\mapsto-i\) satisfy \(r^4=s^2=1\), \(srs=r^{-1}\), giving \(\operatorname{Gal}(K/\mathbb Q)\cong D_4\). For an ordered pair of root exponents on any sixteen-point block, \(r\) adds one to the exponent of \(\beta\) and \(s\) negates both root-of-unity exponents. Hence the identity has cycle type \(1^{48}\), the two order-four rotations give \(4^{12}\), the central involution and two reflections have type \(2^{24}\), and the other two reflections have type \(1^{12}2^{18}\). These four sets have cardinalities \(1,2,3,2\) out of eight. Since \(K\) is unramified outside two, Chebotarev gives the stated natural prime densities among \(p\geq11\). This does not assert independent distribution for arbitrary prime powers.

## Verification

Two standalone checkers are provided. `verify_2wronskian.py` requires Python 3 and SymPy; it constructs the six-by-six jet determinant and differentiates the Fermat equation to verify the exact factored Wronskian, printing `SYMBOLIC_2WRONSKIAN_CERTIFIED_OK`. The Python 3 standard-library script `verify_sextactic_frobenius.py` independently enumerates rational points of \(S\) over each prime field of characteristic at least eleven through 199. It additionally enumerates points over quadratic fields for primes 11, 13, 17, 19 and 23, checks the formula block-by-block, and prints `ALL_FINITE_FIELD_CHECKS_OK`. Both checks were run on the shipped scripts. These finite enumerations and symbolic transformations supplement, but do not replace, the general arguments above.

## Relationship to prior work

Alwaleed and Sakai (2009) explicitly classified the complex \(2\)-Weierstrass points of Kuribayashi quartics, including the 48 sextactic points and 12 hyperflexes at the Fermat parameter. Merta and Zieliński (2024 preprint) gave the same sextactic-point complete intersection \(S\), and Toft and Moe (2024 preprint) discussed Fermat-curve sextactic arrangements. The geometric point count, coordinates, complete-intersection ideal, and characteristic-zero osculating geometry are therefore **not new**. A separately published arithmetic-specialization calculation gives a finite-flat integral model of this exact 48-point scheme and determines its special fibers in characteristics two and three; that **does not state the good-characteristic Frobenius cycle types, point-count formula, zeta factors, or arithmetic-density partition** derived here. Popolitov and Shakirov's 2012 study of quartic undulation invariants is older related quartic-contact background, but concerns tangent lines of fourth-order contact rather than the sextactic finite scheme. The new contribution claimed here is only the full arithmetic splitting classification and its dihedral prime densities, not the previously known equations. Known coordinates make the computations accessible, and unindexed equivalent Galois calculations remain a historical-priority risk.

## Limitations

The theorem applies to the fixed Fermat equation and intrinsic sextactic points in characteristic at least eleven. It does not classify twists or characteristic-five/seven osculation, where the displayed Wronskian coefficient vanishes. The Chebotarev density concerns rational primes, not relative frequencies of all finite fields. An explicit arithmetic consequence of known coordinates can be independently rediscovered; novelty priority is provisional pending a wider literature audit. There has been no independent mathematical review.

## References

1. K. Alwaleed and F. Sakai, *Geometry and computation of 2-Weierstrass points on Kuribayashi quartic curves*, Saitama Mathematical Journal 26 (2009), 67–82, especially the Fermat parameter and Lemma 5. https://www.rimath.saitama-u.ac.jp/research/pdf/smj26-5.pdf (public day of initial appearance not established).
2. A. Popolitov and Sh. Shakirov, *On Undulation Invariants of Plane Curves*, arXiv:1208.5775, first posted 2012-08-28. https://arxiv.org/abs/1208.5775 .
3. Ł. Merta and M. Zieliński, *On quartics with the maximal number of maximal tangency lines*, arXiv:2410.13997, first posted 2024-10-17, Section 4.1. https://arxiv.org/abs/2410.13997 .
4. N. P. A. Toft and T. K. Moe, *The Fermat curves and arrangements of lines and conics*, arXiv:2412.16993, first posted 2024-12-22, Sections 2.2.4 and 3.1. https://arxiv.org/abs/2412.16993 .
5. *Arithmetic specialization of the 48 Fermat-quartic sextactic points*, published scientific result, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-arithmetic-specialization-of-the-48-fermat-quartic-sextactic-poi--4a76ca8d33ca/RESULT.md .
