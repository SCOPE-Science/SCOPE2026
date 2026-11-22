# A genus-two normalization and four ordinary singularities for the general unexpected octic

## Finding

Let the thirteen points in \(\mathbb P^2_{\mathbb C}\) be the configuration of Malara, Section 6.1. Form the fat point scheme
\[
Z_3=3P_1+3P_3+3P_{11}+\sum_{i\notin\{1,3,11\}}P_i,
\]
and for a moving general point \(Q\) define the three-dimensional vector space of degree-eight forms
\[
L_Q=[I_{Z_3}\cap I_Q^5]_8.
\]
For general \(Q\), a general member \(C\) of the projective net \(\mathbb P(L_Q)\) is geometrically integral. Its entire geometric singularity basket is exactly three ordinary triple points, at \(P_1,P_3,P_{11}\), and one ordinary quintuple point, at \(Q\). There are no other singularities, including at infinity. The normalization of \(C\) is smooth of genus \(2\), and so is hyperelliptic.

If \(\widetilde C\) denotes the strict transform on the blow-up of these four marked points, then \(\widetilde C^2=12\).

## Assumptions and scope

All assertions are over an algebraically closed field of characteristic zero, specifically \(\mathbb C\). The thirteen distinct points, in order, are

`(1:0:0), (-1:1:0), (0:1:0), (1:1:0), (-1:-1:1), (1:-1:1), (-1:1:1), (1:1:1), (0:-1:1), (-1:0:1), (0:0:1), (1:0:1), (0:1:1)`.

An *ordinary multiple point of multiplicity* \(m\) means that the lowest nonzero homogeneous term in local parameters is a product of \(m\) distinct linear factors over \(\mathbb C\). “General” means outside a proper Zariski-closed subset of the indicated parameter variety. The claim concerns a general member of the net, not its known reducible subsystem.

## Proof

**The irreducible parameter family.** Malara's Section 6.2 computes \(\dim L_Q=3\) for general \(Q\); hence over a nonempty Zariski-open subset \(U\subset\mathbb P^2\) the kernels of the interpolation matrices form a rank-three vector bundle. Its projectivization \(T\to U\) is an irreducible projective-plane bundle. The same source exhibits an absolutely irreducible member at \(Q=(-59:-21:35)\). Since geometric integrality is open for the flat projective family of degree-eight Cartier divisors, the geometrically integral locus is a nonempty Zariski-open subset of \(T\).

**An exact regular-resolution witness.** At \(Q_0=(2:5:1)\), use the basis \(x^ay^bz^{8-a-b}\) for \(0\leq a\leq8\), \(0\leq b\leq8-a\), in that order. Evaluate all homogeneous partial derivatives of total order less than \(3\) at each of the three distinguished triple points, the values at the other ten base points, and all homogeneous partial derivatives of total order less than \(5\) at \(Q_0\). This gives a redundant but exact \(75\times45\) rational matrix of rank \(42\) and kernel dimension \(3\). The integral form \(F\) defined explicitly in `CHECK.py` lies in this kernel.

The exact first homogeneous terms of \(F\) in suitable affine parameters \((u,v)\) have orders \(3,3,3,5\). Their discriminants upon setting \(v=1\), respectively, are

- `-100042374075668087000000`,
- `-3273121304829444096`,
- `1193158290011212276992000000`,
- `15151100085243033791347187385761290361241600000000`.

The leading coefficients in \(u\) are nonzero, and the discriminants are nonzero. Thus the prescribed four singularities are ordinary of their stated multiplicities; one blow-up at each resolves them.

**Exhaustion of the singular set.** Put \(f(x,y)=F(x,y,1)\). Eliminate \(y\) from \((f,f_x)\), \((f,f_y)\), and \((f_x,f_y)\). Their three exact resultants have \(x\)-degrees \(38,41,37\), and their monic greatest common divisor is
\[
x^4(x-2)^{16}.
\]
Consequently every affine singular point has first coordinate \(0\) or \(2\). At the former, the monic polynomial gcd in \(y\) of \(f,f_x,f_y\) is \(y^2\), and at the latter it is \((y-5)^4\). Thus the only affine singular points are \(P_{11}\) and \(Q_0\). At infinity,
\[
F(x,y,0)=11028x^3y^3(x-y)(x+y).
\]
The two simple roots are smooth points of the plane curve; its only possible infinity singularities are \(P_1\) and \(P_3\), already checked as ordinary triples. This exhausts the projective singularities of \(F\).

**Passing from a witness to generic members.** Blow up the smooth relative projective plane along the four disjoint marked sections \(P_1,P_3,P_{11},Q\) over the open set \(U\). The universal sections in the class \(8H-3E_1-3E_3-3E_{11}-5E_Q\) form a flat family of effective Cartier divisors. Smoothness of their proper transforms, together with nonvanishing of the four leading tangent coefficients and discriminants, is an open property on \(T\). The explicit witness at \(Q_0\) proves that this open set is nonempty. As \(T\) is irreducible, it intersects the nonempty geometric-integrality open set supplied by Malara's different witness. For general \(Q\), a general member belongs to their intersection, and therefore has exactly the four ordinary singularities claimed and no others.

**Genus and divisor class.** A plane octic has arithmetic genus \((8-1)(8-2)/2=21\). The \(\delta\)-invariant of an ordinary \(m\)-fold point is \(m(m-1)/2\). The four singularities contribute \(3+3+3+10=19\). Thus the smooth normalization of the generic integral octic has genus \(21-19=2\). On the four-point blow-up the strict-transform class has square \(8^2-3^2-3^2-3^2-5^2=12\). Every smooth genus-two curve in characteristic zero is hyperelliptic.

## Verification

The standalone `CHECK.py` uses exact rational arithmetic through SymPy to reconstruct the interpolation matrix, verify its rank and the displayed integral equation, determine the four exact tangent multiplicities and nonzero discriminants, compute the three resultants and their gcd, check both affine fibers, and certify the infinity factorization. Its assertions pass. The genericity argument uses open-locus geometry plus the independent absolutely irreducible member explicitly recorded in the initiating paper; no finite sample is claimed to prove geometric integrality by itself.

## Relationship to prior work

Malara (2026), Section 6.2, identifies the unexpected \((8,5)\) net, its dimension and splitting type, the two-dimensional reducible subsystem obtained by multiplying the unexpected sextic by conics, and at least one absolutely irreducible octic. Those facts do not determine whether the general integral member has further singularities, nor its geometric genus. The present result establishes the complete generic singularity basket and exact normalization genus for that three-dimensional system. Malara and Tutaj-Gasińska (2022) develop the related reduced-configuration interpolation theory, not this fat-base-plane-octic singularity classification. Other published classifications of unexpected quartics, sextics and octics concern different point schemes and do not imply the stated result.

## Limitations

Only a nonempty general-parameter open locus is classified; exceptional moving points and special members, including reducible products of sextics and conics, may have different singularities. This is not a classification of the full discriminant locus or of the genus-two moduli of the normalizations. Exact computation certifies the displayed witness only; the extension to general members relies on the stated algebraic-geometric openness argument and published geometric-integrality witness. Publication priority relative to unindexed theses or computational tables remains subject to external review.

## References

1. Grzegorz Malara, *Fat base schemes and unexpected hypersurfaces of type \((d+k,d)\)*, arXiv:2611.04564v1, 3 November 2026, Sections 6.1–6.2. https://arxiv.org/html/2611.04564v1
2. Grzegorz Malara and Halszka Tutaj-Gasińska, *On unexpected curves of type \((d+k,d)\)*, arXiv:2109.00769v2, 28 October 2022. https://arxiv.org/html/2109.00769v2
