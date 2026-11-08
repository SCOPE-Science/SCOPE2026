# Complete prime-polynomial unit groups over finite fields

## Finding
Let \(q\) be a prime power and let \(f\in\mathbb F_q[t]\) be monic of degree \(n\ge1\). Every residue class modulo \(f\) has a unique polynomial representative of degree less than \(n\). Call \(f\) **complete for prime-polynomial units** if each nonidentity element of \((\mathbb F_q[t]/(f))^\times\) has an irreducible polynomial as that representative. Irreducible means nonconstant and irreducible over \(\mathbb F_q\).

For \(h\ge0\), let
\[
R_h(t)=\prod_{\substack{P\in\mathbb F_2[t]\;\text{monic irreducible}\\1\le\deg P\le h}}P(t),\qquad R_0(t)=1.
\]
**Classification theorem.** The modulus \(f\) is complete for prime-polynomial units if and only if \(q=2\) and
\[
R_{\lfloor(n-1)/2\rfloor}(t)\mid f(t).
\]
Consequently the only possible degrees are \(1\le n\le6\). There are exactly **18 monic complete moduli** in total, and their full unit groups have order at most \(12\). The bound is attained precisely for the four complete monic degree-six moduli.

The exact classification by degree is:

| \(n\) | Required divisor of \(f\) | Number of monic \(f\) | Unit-group orders (with multiplicity) |
|---|---|---:|---|
| 1 | \(1\) | 2 | \(1,1\) |
| 2 | \(1\) | 4 | \(1,2,2,3\) |
| 3 | \(t(t+1)\) | 2 | \(2,2\) |
| 4 | \(t(t+1)\) | 4 | \(3,4,4,4\) |
| 5 | \(t(t+1)(t^2+t+1)\) | 2 | \(6,6\) |
| 6 | \(t(t+1)(t^2+t+1)\) | 4 | \(12,12,12,12\) |
| \(n\ge7\) | no possible modulus | 0 | none |

In the two-variable family \(f=R_2 g\) of degree six, \(g\) ranges independently over all four monic quadratic polynomials in \(\mathbb F_2[t]\); this is the complete equality family for the maximal group order.

## Assumptions and scope
The coefficient field is exactly \(\mathbb F_q\), not an infinite field. The modulus is an arbitrary monic nonconstant polynomial, not necessarily irreducible or squarefree. All residue representatives are canonical reduced polynomials (degree less than \(n\)); unlike arbitrary associates, these are uniquely specified. The identity \(1\) is exempt from the irreducibility condition, and a nonzero constant other than \(1\) is not irreducible. The classification counts monic polynomials, not isomorphism types of quotient rings or groups.

## Proof
**1. Exclude larger coefficient fields.** If \(q>2\), choose \(c\in\mathbb F_q^\times\setminus\{1\}\). Since \(f\) is nonconstant, its residue is a nonidentity unit with canonical representative \(c\), which is a constant and hence not irreducible. Thus \(q=2\) is necessary.

**2. Exact small-factor criterion for \(q=2\).** Write \(h=\lfloor(n-1)/2\rfloor\). If an irreducible polynomial \(P\) of degree \(d\le h\) does not divide \(f\), then \(P^2\) has degree \(2d<n\), is reducible, and is coprime to \(f\). It is therefore a nonidentity unit representative contradicting completeness. This proves \(R_h\mid f\).

Conversely, assume \(R_h\mid f\). If a nonconstant polynomial \(a\) of degree less than \(n\) is reducible, it has at least two nonconstant irreducible factors counting multiplicity. One of these factors \(P\) has degree at most \(\lfloor\deg(a)/2\rfloor\le h\). Thus \(P\mid R_h\mid f\), so \(\gcd(a,f)\ne1\). No reducible nonconstant polynomial represents a unit, and \(1\) is the only nonzero constant over \(\mathbb F_2\). Thus every nonidentity unit representative is irreducible, proving the equivalence.

**3. Degree cutoff.** Let \(S(h)=\deg R_h\). Over \(\mathbb F_2\) there are exactly two monic irreducibles of degree one, one of degree two, and two of degree three, giving \(S(1)=2\), \(S(2)=4\), \(S(3)=10\). There is at least one monic irreducible of every positive degree over a finite field; hence for \(h\ge3\),
\[
S(h+1)\ge S(h)+(h+1).
\]
Starting from \(S(3)=10\), induction gives \(S(h)\ge2h+4\) for all \(h\ge3\). But if \(h=\lfloor(n-1)/2\rfloor\), then \(n\le2h+2\); consequently \(\deg R_h>n\) when \(n\ge7\), so \(R_h\nmid f\). This excludes all larger degrees without computational extrapolation.

**4. Exact count.** For \(n=1,2\) the divisor is \(1\) and there are \(2^n\) monic degree-\(n\) choices. For \(n=3,4\), \(R_h=t(t+1)\) has degree two, leaving \(2^{n-2}\) monic quotient choices. For \(n=5,6\), \(R_h=t(t+1)(t^2+t+1)\) has degree four, leaving \(2^{n-4}\) choices. The counts \(2,4,2,4,2,4\) sum to \(18\).

**5. Group orders.** For any monic \(f\) of degree \(n\), the polynomial Euler-totient formula is
\[
\left|(\mathbb F_2[t]/(f))^\times\right|=2^n\prod_{P\mid f}\left(1-2^{-\deg P}\right),
\]
with distinct monic irreducible divisors \(P\). Applying this to the six families gives the table. In degree six, \(f=t(t+1)(t^2+t+1)g\), with \(g\) any monic quadratic: if \(g\) is the unique irreducible quadratic, the totient is \(12\); if \(g\) is a product of linear factors, it is again \(12\). Every other complete modulus has unit-group order at most \(6\), proving the exact maximum and equality family.

## Verification
The accompanying standalone `verify.py` represents polynomials over \(\mathbb F_2\) as binary integers. It implements exact polynomial division, polynomial gcd, trial-factor irreducibility, and independent full-residue enumeration of unit representatives. It compares the structural divisor criterion against direct enumeration for all \(n\le8\), checks the counts through \(n=10\), and prints `VERIFY_OK` only when every check passes. The separate totient calculations in the proof yield the displayed unit-group-order multisets. The finite tests are corroboration; the degree cutoff and full classification follow from the proof for every \(n\).

## Relationship to prior work
Trey Li, *Groups of Prime Units* (arXiv:2611.01793v1, publicly posted 1 November 2026), defines the integer-modulus notion, classifies nine **complete integer** examples, and explicitly asks in Question 6.6 about analogues over polynomial rings over finite fields. Its results do not state the polynomial classification above. The current theorem solves the complete-group subcase of that question under canonical degree-bounded representatives. Ordinary polynomial factorization and finite-field irreducibility counts are standard inputs; those ingredients are not claimed as new.

## Limitations
This theorem does not classify proper subgroups of polynomial units whose elements have irreducible representatives, nor does it settle the polynomial analogues of compact groups or the infinitude questions about prescribed subgroup orders. It is a result about canonical polynomial representatives; alternate conventions for choosing representatives can change the problem.

## References
1. Trey Li, *Groups of Prime Units*, arXiv:2611.01793v1 (first posted 2026-11-01), Sections 1, 2 and Question 6.6. https://arxiv.org/html/2611.01793v1
2. FLINT documentation, *Defining polynomials*, section on counts of irreducible polynomials over finite fields. https://flintlib.org/doc/algorithms/finite-fields/defining-polynomials.html
