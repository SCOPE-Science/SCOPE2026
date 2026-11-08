# Exact rational line-section spectra of the ternary BKS quartic over two short extensions

## Finding

Write \(C\subset\mathbb P^2_{\mathbb F_3}\) for the projective quartic
\[
2Y^4-X^3Z-XZ^3-XY^2Z+X^2Z^2=0.
\]
For each \(Q\in\{27,81\}\), let \(C_Q=C(\mathbb F_Q)\). For a rational line \(L\), define its *rational line-section weight* \(w(L)=\#(L(\mathbb F_Q)\cap C_Q)\). For a rational point \(P\), define its *four-secant multiplicity*
\[
s(P)=\#\{L\in (\mathbb P^2_{\mathbb F_Q})^\vee(\mathbb F_Q):P\in L,\ w(L)=4\}.
\]
The complete rational line-section distributions are:

| \(Q\) | \(\# C_Q\) | \(w=0\) | \(w=1\) | \(w=2\) | \(w=3\) | \(w=4\) |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 27 | 31 | 240 | 256 | 195 | 42 | 24 |
| 81 | 79 | 2520 | 2290 | 1515 | 114 | 204 |

The complete multiplicity distributions are:

| \(Q\) | Location of \(P\) | \(s(P)\colon\#P\) |
| ---: | --- | --- |
| 27 | \(P\in C_Q\) | \(0\colon7,\ 4\colon24\) |
| 27 | \(P\notin C_Q\) | \(0\colon282,\ 1\colon312,\ 2\colon132\) |
| 81 | \(P\in C_Q\) | \(0\colon3,\ 10\colon72,\ 24\colon4\) |
| 81 | \(P\notin C_Q\) | \(0\colon108,\ 1\colon1332,\ 2\colon2496,\ 3\colon1248,\ 4\colon1134,\ 5\colon240,\ 18\colon6\) |

Thus over \(\mathbb F_{27}\) there are exactly **282** rational points off the quartic which lie on no four-secant, and over \(\mathbb F_{81}\) there are exactly **108**. In particular the rational point configurations on this quartic are not complete \((k,4)\)-arcs in either of these two short extensions. In both fields there are lines with four distinct rational intersection points.

## Assumptions and scope

The base field has characteristic three. The two extension fields have exactly \(27\) and \(81\) elements; no statement is made for general \(q\) or higher extension degrees. \(C_Q\) denotes the **entire** rational point set of the projective plane curve, including its rational singular points. The weight \(w(L)\) counts **distinct rational points**, not scheme-theoretic intersection multiplicities. A four-secant has four different rational points and therefore meets the degree-four plane curve transversally at those points.

This quartic is the \(q=3\) specialization of the rational BKS curve whose affine equation is \(Y^{q+1}-(X^q+X)+(Y^2-2X)^{(q+1)/2}=0\), as in Korchmáros–Nagy–Szőnyi, §4.2, formula (5). Its projective closure is precisely the displayed homogeneous equation. The BKS quartic is rational, with three rational ordinary nodes; that geometry is established in prior work. The arithmetic here concerns its rational line sections over two specified extensions.

## Proof

The following is an exhaustive, finite-field proof accompanied by complete standard-library Python code in `verify_bks.py`. The proof is finite because each asserted number concerns a completely specified finite field and every point and line is explicitly enumerated.

**1. Exact field models.** Work in the polynomial quotient \(\mathbb F_3[T]/(f)\). For degree three take \(f=T^3+2T+1\), and independently \(f=T^3+2T+2\). For degree four take \(f=T^4+T+2\), and independently \(f=T^4+2T+2\). Every one has no root in \(\mathbb F_3\); the quartics are additionally indivisible by each of the three monic irreducible quadratics \(T^2+1\), \(T^2+T+2\), and \(T^2+2T+2\). Therefore all four defining polynomials are irreducible. The verifier performs these trial-division tests and constructs addition, multiplication and inversion tables by coefficient arithmetic modulo the chosen \(f\). It verifies all nonzero inverses.

**2. Exhaustive projective representatives.** Each point of \(\mathbb P^2(\mathbb F_Q)\) has exactly one representative in
\[
\{[1:a:b]:a,b\in\mathbb F_Q\}\cup\{[0:1:b]:b\in\mathbb F_Q\}\cup\{[0:0:1]\}.
\]
There are \(Q^2+Q+1\) representatives. The same set of triples independently indexes every rational projective line by the dual equation \(\lambda X+\mu Y+\nu Z=0\).

**3. Exhaustive curve-point and line-section computation.** Evaluate the displayed homogeneous quartic with exact quotient-field arithmetic at every canonical point. For each dual line triple, test its dot product with every point found on the quartic; its number of zeros is exactly \(w(L)\). This produces \(31\) curve points and the first line-spectrum row for \(Q=27\), and \(79\) points and the second row for \(Q=81\). The complete tables are encoded as executable assertions in the verifier, rather than being inferred from a sample. The code independently generates every four-secant as the span of a pair of distinct rational curve points and checks that this agrees exactly with the four-weight portion of the dual-line census.

**4. Exhaustive point-incidence computation.** Having determined the complete set \(S\) of four-secants, compute \(s(P)=\#\{L\in S:P\in L\}\) for **every** projective point, and divide the resulting histogram into those lying on or off the curve. This yields the claimed four multiplicity rows. Since every external point is enumerated, the zero classes of respective sizes \(282\) and \(108\) are exhaustive and certify non-completeness.

**5. Independent arithmetic representations and consistency.** All four distributions are recomputed with two *distinct irreducible polynomial presentations* of each field, and the outcomes are asserted identical. Independently, the normalization map \(t\mapsto[2(t+1)^4:2+t+t^3:1]\), together with \([1:0:0]\), is checked pointwise against the quartic. The three nodes \([1:2:1]\), \([1:0:2]\), \([1:1:1]\) are also identified by exact evaluation; their normalization behavior agrees with extension parity. The two incidence identities
\[
\sum_L w(L)=\# C_Q\,(Q+1),\qquad \sum_P s(P)=\#S\,(Q+1)
\]
are checked exactly in both fields. For \(Q=27\) the respective values are \(868\) and \(672\), and for \(Q=81\) they are \(6478\) and \(16728\). These checks are independent constraints on the enumerated histograms.

Every step is constructive over finite sets; no statistical inference, untested infinite assertion or external computational service is used.

## Verification

Run `python3 verify_bks.py` with a standard Python 3 interpreter. It imports only `collections` and `itertools` from the standard library, creates the finite fields and exact incidence data from scratch, and raises on any disagreement. Its successful final line is `BKS_SHORT_EXTENSION_COMPLETE_EXACT_CENSUS_PASS`. The reported field sizes, point counts, full spectra and incidence totals are built into the code as explicit testable integer assertions. The file is supplied as part of the same package.

## Relationship to prior work

Korchmáros, Nagy, and Szőnyi, *Algebraic approach to the completeness problem for \((k,n)\)-arcs in planes over finite fields*, arXiv:2302.10162 (first public 20 February 2023), §4.2, establish the BKS family and its singular/normalization geometry; their §7.2 and introduction address eventual completeness for the larger extensions and explicitly leave the rational BKS cases \(r=3,4\) open. This note retains that established geometry and supplies exact arithmetic line-section and point-multiplicity spectra for the first base-field case \(q=3\) in the two open extension degrees. The claimed data are not consequences of the cited large-extension theorem, because its hypotheses exclude these degrees. The existence of a finite parameterization and the arc/curve correspondence themselves are not new claims.

## Limitations

This is a complete exact census for two small fields, not a formula for general odd \(q\) or other extensions. The count includes all rational points of the singular plane model; substituting the normalization's rational-point set would change the problem. Arithmetic identities in the code are exhaustive finite certificates, not an independently machine-formalized proof. The absence of an equivalent older or differently represented census cannot be guaranteed.

## References

Korchmáros, G.; Nagy, G. P.; Szőnyi, T. *Algebraic approach to the completeness problem for \((k,n)\)-arcs in planes over finite fields*. arXiv:2302.10162 (20 February 2023), subsequently *Journal of Combinatorial Theory, Series A* **204** (2024), article 105851, DOI: 10.1016/j.jcta.2023.105851. Primary sections consulted: introduction, §4.2, §7.2.
