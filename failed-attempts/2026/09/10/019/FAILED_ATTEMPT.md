# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** The Borodin-Kostochka threshold cell for claw-free graphs at Delta=8
- **Round:** 2026-09-07-first-light-01
- **Lane:** 531
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Graph Theory
- **Method:** structural graph decomposition with discharging and DP-coloring reducibility certificates

## Problem

Decide the Borodin-Kostochka threshold cell for claw-free graphs at maximum degree 8: is every claw-free graph with Delta=8 and omega<=6 necessarily 7-colorable, and if not, exhibit a minimal explicit refuting witness?

## Attempted claim

Every claw-free graph G with maximum degree Delta(G)=8 and clique number omega(G)<=6 satisfies chi(G)<=7; otherwise there exists an explicit minimal claw-free witness H with Delta(H)=8, omega(H)<=6, and chi(H)=8.

## Research outcome

Target's universal (claw-free, Delta=8, omega<=6 => chi<=7) is FALSE. Explicit 8-vertex-critical witness H=C5[+]K3 (15 vertices; Delta=8, omega=6, alpha=2, chi=8; every H-v retains Delta=8/omega=6 and is 7-colorable), fully edge-verified from committed adjacency lists. Additionally Q=Circ(13;{1,2,3,5}) (Delta=8, omega=4, chi=7, 7-vertex-critical) falsifies the preset fallback universal chi<=6 on the (8,<=4) slice.

## Why this attempt failed

Failed axes: originality, value.

originality: Route is TARGET (report declares claim_route TARGET satisfying the target's witness disjunct). The headline witness H=C5[K3]=C5 boxtimes K3 with (Delta,omega,chi)=(8,6,8) and alpha<=2 is verbatim prior art, not a new existence claim. Cranston-Rabern exposition (arXiv:1305.3526 / Graphs with chi=Delta have big cliques) explicitly constructs 'five disjoint copies of K3 ... adding edges ... i-j=1 mod 5' and states '8-regular with omega=6 and chi>=15/2=8 ... so chi=8' -- that is exactly H. Open Problem Garden BK page states 'requirement Delta>=9 is necessary, as one can see by looking at the strong product of C5 and K3'. Recent BK correspondence-coloring paper (arXiv:2603.14427v1) states 'C5 boxtimes K3 ... is 8-regular and has clique number 6, yet chromatic number 8 (since |V|=15 and every independent set has size at most two). This shows Delta>=9 is necessary.' Christofides-Edwards-King (arXiv:1109.3092) cites C5 boxtimes K3 as the tightness example for BK and Reed. Since priors record alpha<=2 ('each color used on at most 2 vertices' / 'independent set at most two'), claw-freeness (alpha<3=alpha(K1,3)) is a mechanically implied one-liner, not a substantive new observation. Hence the refutation 'not every (claw-free) Delta=8 omega<=6 graph is 7-colorable' was already implied by the canonical sharpness example plus one line. The added '8-vertex-critical' packaging (explicit H-v 7-colorings retaining Delta/omega) is a routine 14-vertex coloring check, not a new theorem, and does not create priority. DRAFT itself concedes 'C5 boxtimes K3 ... BK literature cites C5 boxtimes K3 as showing Delta>=9 hypothesis is necessary ... The graph H itself is therefore not claimed as new.' Admission's PASS missed this because it searched exact cell phrasing ('claw-free Delta 8') instead of recognizing the canonical example is itself claw-free. A failed search does not establish priority. Q=Circ(13;{1,2,3,5}) does not rescue headline originality. value: Correct but textbook restatement with mechanically implied qualifier. The retrieval value of '(8,6,8) needs Delta>=9' is already captured by the BK-sharpness citations above; adding 'and alpha=2 so claw-free' plus routine deletion colorings contributes no new reusable lemma, criterion, or boundary: general BK literature already teaches Delta>=9 is necessary via this exact graph, and Reed value ceil((8+1+6)/2)=8 tightness on H is likewise cited as known. This is the policy's 'textbook restatement / mere parameter substitution / unexplained enumeration' exclusion even if verified. Vertex-critical certificates are exact but routine verifications of a known object, not a motivated unknown invariant: the object and triple were known before computation, and the extra criticality check is not a future-research bottleneck. Does not meet the narrow-datum rescue (motivated before computation, not known/mechanically implied) because the datum was known and claw-freeness is mechanically implied.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Graph C5[+]K3 as an unlabeled graph is a known BK-tightness example, not claimed as new; the contribution is its audited minimal-witness certification deciding the admitted cell. Q presented as explicit certified witness, not 'first known'. Minimal = vertex-critical (single-vertex deletions), not unique/smallest-order. Chromatic lower bounds via alpha-counting (exact) plus verified colorings; a DSATUR 7-color UNSAT run on H timed out and is NOT load-bearing. Fallback success criterion (universa…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
