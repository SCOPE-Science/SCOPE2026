# Scientific review

## Correctness — PASS

The result concerns all prime powers \(q\ge2\), a geometrically smooth and integral scheme-theoretic complete intersection of bidegrees \((q+1,q+2)\) in \(\mathbb P^3_{\mathbb F_q}\), and the stated assumption that every rational point lies on the curve. On any rational line the binary restrictions are \(\lambda(s^qt-st^q)\) and \(\ell(s,t)(s^qt-st^q)\). Integrality excludes the case that both restrictions vanish identically. This proves the reduced or uniquely doubled intersection schemes and excludes all nonrational points on rational lines. The rational-point ideal forces the degree-\(q+1\) equation to be alternating Frobenius; a degenerate alternating matrix would give a singular point of the curve at a rational radical vector, contradicting smoothness. The tangent plane then identifies rational tangent lines with the isotropic lines of the nondegenerate alternating form. Every isotropic line has a unique doubled rational point, forcing the tangent bijection. Frobenius conjugate degree-two points would span a rational line, so none exists. Adjunction and Newton identities give the genus and initial zeta coefficients. No finite computation is used to establish the universal statement.

Two standalone standard-library arithmetic verifiers were executed on the published examples over \(\mathbb F_2\) and \(\mathbb F_3\). They check quadratic-extension point counts and symplectic line incidences and are not substitutes for a general proof or independent smoothness certificates.

## Originality — PASS with residual priority risk

Campbell–Dedvukaj–McCormick–Moon–Morales, *On algebraic space filling curves*, arXiv:2310.09293v1 (2023-10-17), was inspected in full available HTML, notably its Section 2 ideal generators, Lemma 3.2 on smooth Frobenius surfaces, Corollary 3.5 on degree minimality, and Table 1 of examples. These are acknowledged as prior work. The inspected source does **not** give the universal scheme-theoretic intersection profile of every rational line, the point–line tangent bijection, or the exclusion of quadratic closed points; those implications are proved here from the line-restriction factorization. Related published plane-filling and product-surface constructions use different ambient geometries; arithmetic background on random complete intersections does not dominate the new statement. Targeted semantic mathematical-record and literature searches for tangent matching, quadratic closed points, Frobenius-minor line sections and symplectic polar spaces did not locate a stronger theorem. Failure to locate a statement is not a proof of priority. A classically known equivalent description in finite generalized-quadrangle terminology remains a genuine risk.

## Mathematical value — PASS

The motivating literature establishes existence and degree optimality of smooth projective-three-space filling complete intersections. The new theorem derives the complete rational-line section dichotomy, an unexpected exact matching of the symplectic point-and-line incidence geometry by curve tangents, and a uniform degree-two closed-point gap. These are structural properties holding for *all* such curves, not arbitrary parameters of a finite example. The initial zeta-coefficient universality is a nontrivial arithmetic corollary. The theorem does not assert that every prime power admits a qualifying curve, determine all zeta coefficients, or classify all possible matchings.

## Closest sources and remaining limitations

1. A. Campbell et al., *On algebraic space filling curves*, arXiv:2310.09293v1, Sections 2–5, especially Lemma 3.2, Corollary 3.5 and Table 1: constructions and form theory are prior; the line-section and arithmetic stratification are not stated there.
2. A. Bucur and K. Kedlaya, *The probability that a complete intersection is smooth*, J. Théor. Nombres Bordeaux 24 (2012), 541–556: general complete-intersection smoothness setting, not the all-rational-points or tangent matching problem.
3. Related plane-filling work by A. Asgarli and D. Ghioca (2023) concerns plane curves and does not imply the statement for a space complete intersection.

Independent review of the mathematical argument and historical priority has not been performed.

Self-review: passed. Independent audit: not yet performed.
