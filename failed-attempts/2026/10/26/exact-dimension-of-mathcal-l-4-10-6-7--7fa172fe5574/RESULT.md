# Exact dimension of \(\mathcal L_{4,10}(6^7)\)

## Finding

Let \(p_1,\ldots,p_7\) be seven general points of \(\mathbb P^4\) over a field of characteristic zero. The vector space \(\mathcal L_{4,10}(6^7)\) of degree-\(10\) hypersurfaces having multiplicity at least \(6\) at every \(p_i\) has dimension
\[
\dim \mathcal L_{4,10}(6^7)=141.
\]
Its associated projective linear system therefore has projective dimension \(140\).

This equals the secant-linear prediction for this case of the \(n+3\)-point interpolation conjecture.

## Assumptions and scope

The seven points are general in \(\mathbb P^4\), so every five are linearly independent and there is a unique rational normal quartic \(C\) through them. Multiplicity \(6\) means that all local Taylor coefficients of total degree less than \(6\) vanish at each point. The dimension stated above is the vector-space dimension, not the projective dimension.

## Proof

The space of degree-\(10\) forms in five variables has dimension
\[
N=\binom{10+4}{4}=1001.
\]
A point of multiplicity \(6\) supplies
\[
q=\binom{4+6-1}{4}=\binom94=126
\]
jet conditions, so the seven points give \(7q=882\) rows in the interpolation matrix.

**Upper bound on the rank.** For each of the \(\binom72=21\) lines \(L_{ij}\) joining two marked points, restriction to \(L_{ij}\cong\mathbb P^1\) is a section of \(\mathcal O_{\mathbb P^1}(10)\), a vector space of dimension \(11\). The order-\(6\) jets at the two endpoints give \(12\) linear functionals on that \(11\)-dimensional space, hence one linear relation among the ambient point-jet conditions for each line. Each such relation uses only the fifth-order directional jets at the two endpoints. For general points, the six chord directions at any fixed point have linearly independent fifth powers in the \(56\)-dimensional space \(\operatorname{Sym}^5(T_{p_i}^*\mathbb P^4)\). Looking at these fifth-order jet components point by point shows that the \(21\) line relations are independent.

The rational normal quartic \(C\) has degree \(4\), so restriction of a degree-\(10\) form to \(C\) lies in \(H^0(C,\mathcal O_C(40))\), of dimension \(41\). The seven marked points impose \(42\) order-\(6\) jets on this restriction, giving one further relation. That relation has a nonzero fifth-order tangent-jet coefficient: otherwise it would be a relation among only the \(35\) lower-order jets, which are independent because the restriction map onto those jets is surjective. For a general marked configuration, at every marked point the tangent fifth power is outside the span of the six chord fifth powers. This is a nonempty open condition: for the standard rational normal quartic with parameter values \(0,1,\ldots,6\), a \(7\times7\) minor of the tangent-plus-chord fifth-power matrix has determinant \(11\pmod{101}\). Hence, at a point where the curve relation has nonzero fifth-order coefficient, its fifth-order component cannot be a linear combination of the line-relation components. The curve relation is independent of all \(21\) line relations. Thus there are \(22\) independent relations among the \(882\) point-jet conditions, and the interpolation matrix has rank at most
\[
882-22=860.
\]
Consequently, \(\dim\mathcal L_{4,10}(6^7)\ge1001-860=141\).

**Matching rank certificate.** Apply a projective change of coordinates so that the first five points are the coordinate vertices. The multiplicity-\(6\) conditions at those vertices leave precisely the \(381\) degree-\(10\) monomials whose five exponents are all at most \(4\); the first five points therefore contribute rank \(1001-381=620\). Take the remaining two points to have affine coordinates
\[
(6,56,63,3),\qquad (97,130,133,106).
\]
All coordinates and all \(2\times2\) minors of these two coordinate vectors are nonzero, so the seven points are in general linear position. Their remaining jet matrix has \(252\) rows and \(381\) columns. The included pure-Python certificate constructs this integer matrix and exhibits a \(240\times240\) minor with determinant congruent to \(9\) modulo \(101\). That determinant is nonzero over characteristic zero, so the full interpolation matrix has rank at least \(620+240=860\) on this configuration. A nonzero minor persists on a nonempty Zariski-open set, giving generic rank at least \(860\). Combined with the universal rank upper bound, the generic rank is exactly \(860\), and
\[
\dim\mathcal L_{4,10}(6^7)=1001-860=141.
\]

## Verification

The reproducible file `rank_certificate.py` verifies the \(252\times381\) matrix dimensions, the rank \(240\) modulo \(101\), and the selected minor determinant \(9\) modulo \(101\). The modular computation is used only to prove a nonzero minor over characteristic zero; it is not used as a substitute for the geometric upper bound. The proof of the upper bound uses the \(21\) independent line relations and the additional independent rational-normal-curve relation.

For the conjectural formula, \(k_C=7\cdot6-4\cdot10=2\). The secant-linear dimension is
\[
\binom{14}{4}-7\binom94+\binom72\binom44+\binom44
=1001-882+21+1=141.
\]

## Relationship to prior work

Brambilla, Dumitrescu, and Postinghel formulate the secant-linear dimension conjecture for systems based at \(n+3\) general points in Conjecture 6.4 of their 2015 preprint. They prove it for \(n\le3\), for Cremona transforms of systems with \(k_C\le1\), and for several listed homogeneous families. The present case has \(n=4\) and \(k_C=2\). Its Cremona parameter is \(6+6+6+6+6-3\cdot10=0\), so it is already Cremona-reduced and is not covered by the \(k_C\le1\) result. The computation and geometric rank argument establish this individual case without asserting the full conjecture.

## Limitations

This result resolves only the parameter vector \((d;m_1,\ldots,m_7)=(10;6,\ldots,6)\). It does not prove the secant-linear dimension conjecture for other multiplicities or dimensions. The modular certificate is finite and exact; the passage to general points uses the nonzero-minor open-set argument together with the geometric rank bound. Independent audit has not been performed.

## References

Maria Chiara Brambilla, Olivia Dumitrescu, and Elisa Postinghel, “On the effective cone of \(\mathbb P^n\) blown-up at \(n+3\) points,” arXiv:1501.04094 (first public version: 2015-01-16), especially Conjecture 6.4 and Propositions 6.9, 6.12–6.14. DOI: 10.1080/10586458.2015.1099060.
