# A rank threshold for quasismooth anticanonical hypersurfaces with repeated heavy weights
## Finding
Let \(r,m\ge2\) and \(a\ge1\) be integers, and write
\[
X_{r,m,a}=\mathbb P(1^r,a^m),\qquad d=r+ma.
\]
Then \(X_{r,m,a}\) is canonical exactly when \(a\le r\), and terminal exactly when \(a<r\). A general hypersurface \(Y_d\subset X_{r,m,a}\) of anticanonical degree \(d\) is quasismooth exactly when
\[
a\mid r
\]
or
\[
r\ge m\quad\text{and}\quad a\mid(r-1).
\]
Thus, among the canonical members \(1\le a\le r\), the number whose general anticanonical hypersurface is quasismooth is
\[
Q_{\mathrm{can}}(r,m)=\tau(r)+\mathbf 1_{r\ge m}\bigl(\tau(r-1)-1\bigr),
\]
and among terminal members it is
\[
Q_{\mathrm{term}}(r,m)=\tau(r)-1+\mathbf 1_{r\ge m}\bigl(\tau(r-1)-1\bigr).
\]
The second branch therefore appears precisely at the rank threshold \(r=m\). The unique canonical nonterminal member with quasismooth general anticanonical hypersurface is \(a=r\).

## Assumptions and scope
The ground field is algebraically closed of characteristic zero. The notation \(1^r\) and \(a^m\) denotes repeated weights. Because there are at least two unit weights, the ambient weighted projective space is well formed. The claim concerns a general anticanonical hypersurface, not every member of the anticanonical linear system. The divisor-counting function \(\tau(n)\) counts positive divisors of \(n\).

## Proof
The singular locus of \(X_{r,m,a}\) is the heavy coordinate stratum \(\mathbb P(a^m)\) when \(a>1\). At a general point of that stratum, the transverse quotient is \(\frac1a(1^r)\); the remaining \(m-1\) directions are fixed. For a nontrivial element indexed by \(1\le j<a\), its transverse age is \(rj/a\). The minimum is \(r/a\), so the Reid--Tai criterion gives canonical singularities exactly for \(a\le r\) and terminal singularities exactly for \(a<r\).

For quasismoothness, apply Fletcher's coordinate-subset criterion to a general degree-\(d\) hypersurface. Any coordinate subset containing a unit-weight coordinate satisfies the monomial alternative because a pure power of that coordinate has degree \(d\). It remains to inspect subsets consisting only of heavy coordinates. Let such a subset have \(k\) coordinates.

A degree-\(d\) monomial supported on the heavy subset exists exactly when \(a\mid d\), equivalently \(a\mid r\). Suppose this fails. Fletcher's second alternative requires \(k\) monomials whose heavy-supported parts are multiplied by \(k\) distinct coordinates outside the subset. An outside heavy coordinate cannot work, because that would require \(a\mid(d-a)\), again equivalent to \(a\mid r\). An outside unit coordinate works exactly when \(a\mid(d-1)\), equivalently \(a\mid(r-1)\). Hence the only available rescue coordinates are the \(r\) unit coordinates. The criterion must hold for the full heavy subset, where \(k=m\), so this rescue branch works exactly when \(r\ge m\) and \(a\mid(r-1)\). This proves the quasismoothness classification.

Inside the canonical range \(1\le a\le r\), the first branch contributes \(\tau(r)\) values. If \(r\ge m\), the second branch contributes all divisors of \(r-1\), except \(a=1\), already counted in the first branch; this contributes \(\tau(r-1)-1\). For terminal members one removes the divisor \(a=r\) from the first branch. Since \(r\nmid(r-1)\), the canonical nonterminal quasismooth member is uniquely \(a=r\).

## Verification
The bundled script `artifacts/verify_equal_weight_anticanonical.py` implements Fletcher's subset criterion directly by enumerating every coordinate subset and testing weighted-semigroup reachability; it does not hard-code the classification. It exhaustively checks all \(128\) cases with \(2\le r,m\le5\) and \(1\le a\le8\). It separately evaluates all quotient ages in those cases, then replays the divisor-count formulas for every \(2\le r,m\le100\). The finite computation is only a regression check; the proof above establishes the result for all stated integers.

## Relationship to prior work
Fletcher's quasismoothness theorem gives the general coordinate-subset criterion used here, but does not state this repeated-heavy specialization or its rank threshold. The affine-chart description of weighted projective space and the Reid--Tai age criterion reduce the ambient singularity calculation to \(\frac1a(1^r)\). Chen--Chen--Chen provide later weighted-complete-intersection context and explicitly use quasismoothness via smoothness of the affine cone away from the origin. The new point is the simultaneous specialization across all \(r,m,a\): when \(a\nmid r\), the full heavy coordinate stratum needs \(m\) distinct unit-coordinate Jacobian directions, creating the sharp condition \(r\ge m\), and this yields the exact divisor counts above.

## Limitations
No claim is made about special anticanonical members, Hodge numbers, deformation equivalence, or moduli components. The exact-day bibliographic metadata inspected for Fletcher's original MPIM preprint is unavailable: the archive records it only as 1989. For date-valued metadata the package therefore uses the earliest exact-day source among the sources with day-resolved public records and records this limitation rather than inventing a day. Literature search cannot exclude an equivalent statement hidden under substantially different notation, although the general criterion, later weighted-complete-intersection literature, semantic database searches, and the closest prior local result were compared at the statement/implication level.

## References
A. R. Fletcher, *Working with Weighted Complete Intersections*, MPIM Preprint Series 1989 (35), especially Theorem 1.5.1 and the affine-chart discussion in Section 1.2.

L. Borisov, *Minimal Discrepancies of Toric Singularities*, arXiv:math/0505167, first public version 2005-05-10; used for the toric cyclic-quotient discrepancy criterion.

J.-J. Chen, J. A. Chen, and M. Chen, *On Quasismooth Weighted Complete Intersections*, arXiv:0908.1439, first public version 2009-08-11.
