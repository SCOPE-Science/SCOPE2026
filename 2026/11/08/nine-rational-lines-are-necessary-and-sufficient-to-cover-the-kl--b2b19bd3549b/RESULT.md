# Nine rational lines are necessary and sufficient to cover the Klein quartic over \(\mathbb F_{31}\)

## Finding
Consider the Klein plane quartic \(K: X^3Y+Y^3Z+Z^3X=0\) over \(\mathbb F_{31}\). Let \(\tau(K)\) be the minimum number of rational projective lines whose union contains all of \(K(\mathbb F_{31})\). Then
\[\boxed{\tau(K)=9.}\]
Its \(32\) rational points admit exactly \(31\) four-secant lines. Among all collections of four-secant lines, the largest collection having pairwise disjoint intersections with \(K(\mathbb F_{31})\) has size \(6\).

## Assumptions and scope
The base field is exactly \(\mathbb F_{31}\); a line and a point are rational if defined over this field. A four-secant is a line containing four **distinct rational** curve points. The minimum is taken over arbitrary rational projective lines, not merely lines tangent to or meeting the curve in a prescribed pattern. The quartic is smooth in characteristic \(31\): the characteristic is different from \(7\), and the classical Klein quartic has good reduction here (alternatively apply the projective Jacobian criterion directly).

## Proof
Normalize every nonzero triple \((a,b,c)\in\mathbb F_{31}^3\) by multiplying by the inverse of its first nonzero entry. This represents every rational projective point exactly once and, dually, every rational projective line \(aX+bY+cZ=0\) exactly once. There are \(31^2+31+1=993\) such triples. Enumerate those satisfying \(a^3b+b^3c+c^3a=0\); there are \(32\). For each of the \(993\) normalized line triples, test its dot product against all \(32\) normalized curve points. The resulting **complete** line intersection spectrum, ordered by numbers of rational intersection points \(0,1,2,3,4\), is
\[(354,334,256,18,31).\]
No line has more than four geometric intersection points with the quartic by Bézout; the exhaustive enumeration also directly checks this for all rational lines.

For each of the \(31\) four-secants, form a bit mask of its rational curve-point set. Run a finite recursion that selects four-secants in increasing index order, at every step discarding later four-secants that meet one already selected in a rational curve point. This is a complete enumeration of all pairwise curve-disjoint families: each such family has a unique increasing index sequence, and the recursion follows it. The numbers of recursion nodes at depths \(0\) through \(7\) are
\[(1,31,270,804,805,207,3,0).\]
Thus there is no family of seven pairwise disjoint four-secants; the maximum is exactly six (there are three six-element families). Every cover by eight lines of \(32\) points would, since each line contains at most four curve points, have to consist of eight **pairwise disjoint four-secants**, impossible. Hence \(\tau(K)\ge9\).

For the reverse bound the following nine line coefficient triples give an explicit cover (coordinates reduced modulo \(31\)):

```text
(0,1,30)
(1,0,11)
(1,1,26)
(1,5,25)
(1,13,3)
(1,16,26)
(1,18,27)
(1,23,23)
(1,26,0)
```

The verifier tests that the union of their rational curve-point masks is exactly the \(32\)-point set. Consequently \(\tau(K)\le9\), proving equality.

## Verification
Run `python3 VERIFY.py` with ordinary Python 3. The complete standalone verifier contains the normalization, all \(993\) line-point incidence tests, the full four-secant family recursion, and the nine-line covering check. No third-party software or downloaded input is required. The recursion is exhaustive rather than randomized; its explicitly defined branching proves the finite nonexistence statement. Re-running the integer arithmetic from the program, rather than trusting a prior log, verifies the finite certificate.

## Relationship to prior work
Asgarli, Dassarma, Ghioca, MacLean and Stokdyk (2026), *Covering plane curves over finite fields with lines*, study general bounds on the number of rational lines needed to cover rational points. The present fact supplies an exact small-field extremal value for the classical Klein quartic, with a strict gap above the elementary Bézout counting bound \(\lceil32/4\rceil=8\). Prior finite-geometric literature records the \(24\)-point Klein quartic arc over \(\mathbb F_{29}\); this is a different field and does not imply the nine-line \(\mathbb F_{31}\) cover value. No universal or historical-priority claim is made.

## Limitations
The result is specific to one field and one smooth quartic. It does not establish an asymptotic covering law or classify all minimum covers, and the finite certificate does not prove any analogous statement over other fields. The motivating paper's full text was not accessible for complete same-object comparison; a previously unnoticed equivalent claim cannot be ruled out. Independent external validation remains unperformed.

## References
1. A. Asgarli, S. Dassarma, D. Ghioca, A. MacLean and E. Stokdyk, *Covering plane curves over finite fields with lines*, arXiv:2610.13042 (first posted October 9, 2026), https://arxiv.org/abs/2610.13042 .
2. *Special (k,2)-arcs for q = 29*, Section 6.14 (account of the known complete 24-point Klein quartic arc over \(\mathbb F_{29}\)), https://backoffice.biblio.ugent.be/download/4337100/8642807 .
