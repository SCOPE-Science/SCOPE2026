# Independent three-axis audit — 2026-09-22 campaign

## Record and source identity

- Source path: `2026/09/08/035`
- Audited repository: `SCOPE-Science/SCOPE2026`
- Current default-branch head checked before publication proposal: `820dc1c4e0650c1818a7c355cd4d2624c476805d`
- Audited source tree: `7e954b8dbff8b66d68b66fc4fd822fabafc26582`
- `RESULT.md` blob: `fe9b47fd0e453e0afb7c89284ade6aadb25b8031`
- `VERIFICATION.md` blob: `83b03a7f246da30fad50fa39962dbb6d7f0519f0`
- Review date (UTC): 2026-09-23
- Review type: separate AI independent audit. This is not a human/expert attestation and not a Lean/formal verification.

The source tree still matched the assignment's immutable tree guard when this audit was performed.

## Claim audited

The record studies
\[
A_0=\mathbb Q[x,y,z]/(x^3,y^3,z^3,xyz)
\]
and claims that its Hilbert function is `(1,3,6,6,3)`, that every linear form fails maximal rank from degree 2 to degree 3, hence the non-Lefschetz locus is all of \(\mathbb P^2\), and that multiplication by \(x+y+z\) has graded ranks `(1,3,5,3)` and Jordan partition `[5,4,4,2,2,1,1]`. The record also claims novelty for the varying-linear-form/non-Lefschetz-locus statement.

## Correctness — PASS

I independently rebuilt the quotient from its monomial basis rather than relying on the historical `AUDIT.json`.

A monomial survives exactly when each exponent is at most 2 and at least one exponent is 0. Direct enumeration gives graded dimensions
`{0:1, 1:3, 2:6, 3:6, 4:3}`, agreeing with the claimed Hilbert function and total dimension 19.

Using the degree-2 basis `(x^2,xy,y^2,xz,yz,z^2)` and the degree-3 basis `(x^2y,xy^2,x^2z,y^2z,xz^2,yz^2)`, I independently formed the multiplication matrix for \(L=ax+by+cz\):
\[
M_2=
\begin{pmatrix}
b&a&0&0&0&0\\
0&b&a&0&0&0\\
c&0&0&a&0&0\\
0&0&c&0&b&0\\
0&0&0&c&0&a\\
0&0&0&0&c&b
\end{pmatrix}.
\]
Exact symbolic determinant computation gives `det(M_2)=0`; at `(a,b,c)=(1,1,1)` its rank is 5. This independently confirms that the square middle multiplication map is singular identically.

I also independently constructed the full 19-by-19 multiplication operator for \(L=x+y+z\) from the quotient monomial basis. Exact rational ranks/nullities gave
`dim ker(L^k) = 7,12,15,18,19` for `k=1,...,5`, yielding Jordan block sizes `[5,4,4,2,2,1,1]`. These checks reproduce the substantive algebraic claims without using the record's verifier.

No correctness defect was found in the stated finite algebra calculations.

## Originality — FAIL

The headline algebra and its failure of the Weak Lefschetz Property are explicitly in the literature long before this record.

Holger Brenner and Almar Kaid, *Syzygy Bundles on P^2 and the Weak Lefschetz Property*, arXiv:math/0604406v2 (2006; Illinois J. Math. 51 (2007)), Example 3.1, studies exactly the monomial almost complete intersection
\((X^3,Y^3,Z^3,XYZ)\). In the full text, Example 3.1 states that
\(K[X,Y,Z]/(X^3,Y^3,Z^3,XYZ)\) does not have WLP and gives a parameterized kernel vector for the degree-2 to degree-3 map for a generic linear form. See:
https://arxiv.org/html/math/0604406v2#S3

More specifically, the paper's Example 3.1 identifies the same ideal and shows the map \(A_2\to A_3\) for a generic linear form is neither injective nor surjective; the paper also notes `dim A_2 = dim A_3 = 6`. The relevant full-text discussion is at arXiv HTML lines corresponding to Example 3.1, especially the displayed statements around the exact algebra and generic kernel.

Migliore, Miró-Roig and Nagel, *Monomial ideals, almost complete intersections and the Weak Lefschetz Property*, arXiv:0811.1023 / Trans. AMS 363 (2011), independently records the same example in its introduction and gives broader failure criteria. Its introduction explicitly says Brenner–Kaid's example is the ideal `(x^3,y^3,z^3,xyz)` and that it fails WLP. Its Corollary 7.4 covers the same ideal in the family
\(I_{\alpha,\beta,\gamma,t}=(x^{\alpha+t},y^{\beta+t},z^{\gamma+t},x^\alpha y^\beta z^\gamma)\):
take \((\alpha,\beta,\gamma,t)=(1,1,1,2)\), which is case (3) with \(\rho=0\). See:
https://arxiv.org/abs/0811.1023
and the full-text Corollary 7.4.

This coverage is not merely adjacent. It implies the record's central non-Lefschetz-locus conclusion. The non-Lefschetz locus is a determinantal closed subset of the parameter plane. Since the exact same 6-by-6 middle map fails maximal rank for a generic linear form in the older work, its determinant vanishes on a dense open set and therefore is the zero polynomial. Consequently the degree-2 degeneracy locus is the whole \(\mathbb P^2\), set-theoretically and with the same zero principal Fitting ideal used by the record. Thus the claimed “whole-plane locus” does not create a new regime from the older WLP failure result.

Searches used included the exact ideal, “monomial almost complete intersection weak Lefschetz”, “non-Lefschetz locus monomial ACI”, and the cited Brenner–Kaid / Migliore–Miró-Roig–Nagel works. The decisive sources were available in full on arXiv, so no institutional-download fallback was needed.

## Scientific value — FAIL

After subtracting the prior-art coverage, the surviving content is a direct determinant certificate for an already-known exact example and a Jordan partition for one chosen linear form. The determinant identity is a useful pedagogical check, but it does not establish a new family, classification, rank-stratification, structural mechanism, or extension of the known WLP theory. In fact, generic failure in the older exact example already forces the determinant polynomial to vanish identically, so even the whole-plane Fitting-locus conclusion follows routinely.

The single-point Jordan partition `[5,4,4,2,2,1,1]` is a reproducible finite invariant, but the record gives no theorem connecting that partition to a broader class, no classification of special linear forms, and no reusable consequence. On the campaign's stated value standard, this residual finite computation is not enough to support a validated finding.

## Bounded repair considered

A bounded repair can accurately reframe the material as an explicit worked certificate for the classical Brenner–Kaid example, cite the 2006/2007 and 2011 sources, and retain the Jordan calculation as supplementary data. That repair would fix the novelty wording but would not produce an original and scientifically substantive result. A legitimate future retry would need a genuinely new theorem—such as a nontrivial family of locus schemes, a rank-stratification/classification not implied by generic WLP failure, or a structural result about Jordan types—with literature comparison showing that it is not already covered.

## Final disposition

- Correctness: **PASS**
- Originality: **FAIL**
- Scientific value: **FAIL**
- Disposition: **failed / withdraw from validated findings**

The package should be preserved for provenance in the assigned failed-attempt destination. This disposition does not allege that the computations are wrong; it records that the record does not pass the independent three-axis gate because its central scientific claim is already known and the remaining one-off calculations do not supply enough new scientific value.
