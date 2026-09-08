# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Replayable Ehrhart h*-distribution with triangulation cross-check and IDP/extremal witnesses across the 4319 Kreuzer-Skarke reflexive 3-polytopes
- **Round:** 2026-09-07-first-light-01
- **Lane:** 64
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Convex Geometry
- **Method:** lattice-point Ehrhart enumeration with dilate counting plus regular-triangulation normalized-volume cross-check and replay

## Problem

Load the 4319 Kreuzer-Skarke reflexive 3-polytopes as explicit integer vertex lists (normalized so 0 is the unique interior lattice point). For each polytope P: (i) by direct box enumeration count L_P(t)=|tP intersect Z^3| for t=0,1,2,3; (ii) interpolate the unique cubic Ehrhart polynomial through these 4 values; (iii) extract normalized volume V=3!*lead(L_P) and h*-vector (h0,h1,h2,h3) via Ehrhart series sum_{t>=0} L_P(t) z^t = (h0+h1 z+h2 z^2+h3 z^3)/(1-z)^4, checking h0=h3=1 and palindromicity; (iv) independently compute V by summing normalized simplex volumes over at least one regular triangulation of P and require equality with (iii); (v) test unimodality of h* and test IDP by checking every lattice point of 2P is a sum of two lattice points of P. Tabulate the full frequency distribution of h*-vectors and V, log all point counts, and report either certified non-unimodal / non-IDP witnesses with explicit points and triangulation certificates, or certified absence plus the volume-vs-point-count extremal polytope(s) maximizing V for given |P intersect Z^3|.

## Attempted claim

Complete checkable census: frequency table of distinct h*-vectors and normalized volumes over all 4319 polytopes with dilate-count logs (t=0..3) and per-polytope triangulation volume agreement; plus verdict on unimodality (list of non-unimodal h* with point-count logs, or certified empty list confirming h*=(1,a,a,1) unimodal) and verdict on IDP (explicit decomposition-failure point in 2P with certificate, or certified all-decomposable), plus at least one volume-vs-point-count extremal witness with explicit vertices, lattice points, and triangulation certificate and replay script.

## Research outcome

From-scratch audit of all 4319 KS reflexive 3-polytopes with dilate counts, exact h* table (33 palindromic vectors, gaps a=33,34), triangulation-cross-checked volumes (4..72 even, max 72 at ids 7/11 with |P|=39), certified-empty non-unimodal and 2P/3P-decomposition-failure lists, header cross-checks, and ~3s replay script.

## Why this attempt failed

Failed axes: originality, value.

originality: The headline mathematical content is implied by prior theorems plus the frozen input itself, not new. (a) Form h*=(1,a,a,1): for any 3D reflexive polytope Hibi's palindromic theorem gives h_i=h_{3-i}, h0=1 always, and h3 = #interior =1 since 0 is the unique interior point; degree<=3. Hence palindromicity, h0=h3=1, V=sum(h)=2a+2, and trivial unimodality (1<=a>=1) are textbook corollaries, not discoveries. (b) Distribution equivalence: auditor verified L1=h1+4 hence V=2a+2=2n-6 where n=|P cap Z^3|=L(1). The committed point-count distribution is therefore an exact shift of the input file's own published Mpts header column (RefPoly.d3 headers 'M:#'), and the h*/V tables are a deterministic relabeling of that column. Extremal witnesses E1/E2 are the input's max-Mpts rows (headers already read 'M:39'), with volume by a single tetrahedron determinant -- standard. Gaps a=33,34 / V=68,70 / n=37,38 are observed absences in that column with no structural explanation. (c) Prior art substantively covers the route and conclusion: Kreuzer-Skarke 1998 classification (the 4319 list, geometry, Hodge/volume data); Hibi/Stanley Ehrhart theory; GRDB/PALP/Sage hosting of reflexive 3-polytope invariants (volumes, point counts); Hegedus-Higashitani-Kasprzyk (arXiv:1503.05739) and Braun-Davis-Solus (arXiv:1608.01614) on reflexive Ehrhart roots and IDP-vs-unimodality; Amendola-Oldekop (arXiv:2311.13572) computing ML degrees of all 4319 classes, establishing that re-tabulating one more invariant over the same 4319 list with a script is an established pattern, not a new result. The candidate's own topic.json admits 'not a new classification theorem' and frames the delta as a 'verification dataset'. A timestamp, frozen hash, or failed prior-art search does not establish priority. No substantively new object, gap theorem, or method beyond standard dilate-count plus fan volume is contributed. value: Not independently worth finding later under SCOPE. The result is a textbook corollary (Hibi palindromicity + Stanley) applied exhaustively to a published list, combined with an unexplained enumeration: 33 h* values as relabels of known point counts, volume range, mode a=9/V=20, gaps a=33,34 stated without proof or structural reason, extremal tetrahedra already identifiable from input headers, certified-empty lists that are theorem-vacuous (unimodality trivial) or partial (k=2,3 decomposition does not decide IDP, as the draft honestly notes). It is a re-derivation/re-display of the KS Mpts column with a replay script and a fan-volume cross-check -- useful engineering hygiene but not a citable mathematical advance for mirror symmetry or Ehrhart positivity, and it tests folklore that the draft itself concedes is already strongly suggested by literature. Falls squarely into reject categories: textbook restatement (palindromic/unimodal form), mere reparameterization (V=2n-6 transform of published counts), and unexplained enumeration (gap absences with no theory).

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: 2P/3P decomposition success does not prove full IDP for all k (reported as tested-level absence, not an IDP theorem); origin-fan triangulation assumes certified reflexivity and convex-facet fan validity; KS header values used as cross-check, not re-derived; no new classification beyond Kreuzer-Skarke list.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
