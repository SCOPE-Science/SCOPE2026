# Reparametrization orbits of the first non-thin truncated-polynomial subalgebras over \(\mathbb F_2\) and \(\mathbb F_4\)

## Finding
Let \(R_q=\mathbb F_q[t]/(t^{14})\), with \(q\in\{2,4\}\), and let the \(\mathbb F_q\)-algebra automorphism group act on unital subalgebras by changes of parameter \(t\mapsto ut+\sum_{j=2}^{13}c_jt^j\), where \(u\ne0\). Among the *non-thin* subalgebras (defined below), there are exactly **11 orbits for \(q=2\)** and **29 orbits for \(q=4\)**. Their complete orbit-size distributions, separated by exponent set, are:

| Field | Exponent set | Orbit size : number of orbits | Embedded subalgebras |
| --- | --- | --- | ---: |
| \(\mathbb F_2\) | \(E_0=\{0,4,6,8,10,12,13\}\) | \(8:6,\ 16:1\) | 64 |
| \(\mathbb F_2\) | \(E_1=E_0\cup\{11\}\) | \(4:4\) | 16 |
| \(\mathbb F_4\) | \(E_0\) | \(384:14,\ 768:1,\ 1536:4\) | 12,288 |
| \(\mathbb F_4\) | \(E_1\) | \(48:4,\ 96:6\) | 768 |

The full totals of non-thin embedded subalgebras are therefore \(80\) and \(13{,}056\), respectively. The labeled counts were known; **the orbit partitions and stabilizer-size information are the assertion here**. No assertion is made about other field orders.

## Assumptions and scope
The ambient ring is the truncated polynomial algebra over the displayed *fixed* field, and equivalence means conjugacy under its field-linear algebra automorphisms, not abstract isomorphism of subalgebras. For a subalgebra \(S\), write \(\mathfrak m=S\cap tR_q\), let \(E(S)\) consist of orders of nonzero elements of \(S\), and define \(S\) to be non-thin when the minimal additive-monoid generator count of \(E(S)\setminus\{0\}\) exceeds \(\dim_{\mathbb F_q}(\mathfrak m/\mathfrak m^2)\). The finite exponent semigroup is interpreted in the usual truncated sense. The relevant classification and unique normal forms are from F. Franco Muñoz, arXiv:1812.03576, Theorem 6 and Propositions 7--8. In characteristic two the defining non-thin condition on the parameter named \(a\) is exactly \(a\ne0\).

## Proof
**Canonical forms and completeness.** Set
\[
 A=t^4+at^5+bt^7+dt^9+ft^{11},\qquad
 B=t^6+ct^7+et^9+gt^{11}.
\]
For \(E_0\), every non-thin subalgebra is represented uniquely by the span of \(1,A,B,t^{13},A^2,AB,A^3\), with \((a,b,c,d,e,f,g)\in\mathbb F_q^7\) and \(a\ne0\). For \(E_1\), delete the terms involving \(f,g\), and take the span of \(1,A,B,t^{11},t^{13},A^2,AB,A^3\), with \((a,b,c,d,e)\in\mathbb F_q^5\) and \(a\ne0\). All calculations are modulo \(t^{14}\). These forms are the complete two non-thin families from the cited classification, and the pivots of their reduced bases are precisely \(E_0\) and \(E_1\). They have respectively \(q^7-q^6\) and \(q^5-q^4\) distinct members. A direct multiplication check confirms closure and the radical embedding dimensions \(2\) and \(3\); the relevant valuation-semigroup generator counts are \(3\) and \(4\). The identity \(A^3-B^2=at^{13}\) explains the non-thin defect when \(a\ne0\).

**Generation of the full ambient automorphism group.** Every \(\mathbb F_q\)-algebra automorphism sends \(t\) to \(ut+\sum_{j=2}^{13}c_jt^j\) with \(u\in\mathbb F_q^\times\); conversely every such substitution is invertible. Starting from the lowest unequal coefficient, successive elementary changes \(t\mapsto t+ct^m\) for \(2\le m\le13\), together with dilation, generate all substitutions. In \(\mathbb F_2\), take \(c=1\); in \(\mathbb F_4=\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\), take \(c\in\{1,\alpha\}\) and the dilation \(t\mapsto\alpha t\). Each choice has a polynomial inverse modulo \(t^{14}\). For fixed \(m\), the two elementary changes span the additive coefficient space; conjugation and triangular coefficient elimination then generate the whole group.

**Finite exhaustive orbit certificate.** Represent every algebra by its uniquely determined reduced row-echelon \(\mathbb F_q\)-basis with increasing lowest-degree pivots, encoded as a tuple of fourteen-coordinate vectors. Compute multiplication by truncated polynomial convolution, construct the two canonical families with \(a\ne0\), and compute the action of each generator by substituting its powers into every basis vector followed by reduction. The script `verify.py` enumerates **all** \(64+16\) or \(12{,}288+768\) distinct canonical subalgebras, verifies the pivots, non-thin radical dimensions and multiplicative closure, then breadth-first searches the directed generator graph, deleting each reached algebra from the unseen set. Because the stated substitutions generate *all* automorphisms, these connected components are the actual orbits, not sample subsets. The resulting component multiplicities are exactly the four rows in the table. As a second explicit finite certificate, `orbit_certificate.json` stores one canonical parameter vector and the size for every one of the \(40\) orbits; `verify_certificate.py` separately generates each recorded orbit and checks disjointness, its size and exhaustive coverage of the labeled families.

## Verification
With Python 3 in the directory containing the three artifacts, run `python verify.py` and `python verify_certificate.py`. Each ends with `VERIFY_OK` and asserts the complete distributions for both fields. The field model for \(\mathbb F_4\) is encoded by binary polynomial representatives modulo \(\alpha^2+\alpha+1\), with \(\alpha\) encoded as integer `2`. No third-party dependencies, random input or hidden assets are needed. All \(13{,}136\) classified subalgebras across both fields are accounted for, and the certificate records all \(40\) representative orbits. Exhaustion of these finite parameter spaces is sufficient because the cited classification proves the parameter spaces exhaust the non-thin subalgebras and the elementary substitutions generate the full automorphism group.

## Relationship to prior work
Franco Muñoz's 2018 work establishes the first possible non-thin truncation at exponent \(14\), proves both canonical forms and counts the **embedded** subalgebras, but does not provide the finite-field automorphism-orbit distributions. Binyamin--Greuel--Mehmood--Pfister (2023, arXiv:2301.09409, especially §5.1) classify unimodal parametrized plane branches over algebraically closed fields of positive characteristic, including semigroup \(\langle4,6,13\rangle\). Their analytic right-left equivalence and algebraically closed setting differ from the **finite-field ambient change-of-parameter action** and the separate \(E_1\) stratum here. That classification is related background and may inform geometric orbit structure but does not directly supply the forty finite rational orbits. Related classifications of short local algebras or of automorphisms of different truncated coordinate-cross algebras likewise concern different moduli problems.

## Limitations
The result proves the orbit counts only for \(\mathbb F_2\) and \(\mathbb F_4\), not a formula for all characteristic-two fields or arbitrary fields. It concerns embedded subalgebras of \(\mathbb F_q[t]/(t^{14})\), not abstract algebra isomorphism classes or the entire analytic classification of plane branches. The finite exhaustive calculation uses, rather than reproves from first principles, the cited full classification of non-thin families; its enumeration, generator completeness, multiplication, orbit coverage and disjointness are directly reproducible. Publication priority outside inspected accessible literature remains open to independent investigation.

## References
1. F. Franco Muñoz, *The existence of non-thin subalgebras of \(K[x]/(x^n)\) and related numerical monoids*, arXiv:1812.03576 (first public version 2018-12-09), Theorem 6 and Propositions 7--8.
2. M. A. Binyamin, G.-M. Greuel, K. Mehmood, G. Pfister, *Classification of Unimodal Parametric Plane Curve Singularities in Positive Characteristic*, arXiv:2301.09409 (2023), §5.1.
