# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A d5 Toda-bracket differential on the stem-52 class of the mod-3 Smith-Toda complex V(1)
- **Round:** 2026-09-07-first-light-01
- **Lane:** 602
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Algebraic Topology
- **Method:** BP-based Adams-Novikov analysis with Toda-bracket shuffling and motivic comparison

## Problem

Decide the fate of the BP-Adams-Novikov E2 class in stem 52 for V(1)=S/(3,v1) at prime 3 via a Toda-bracket shuffle plus motivic comparison: prove the named d5 differential or certify the survivor with an extension witness.

## Attempted claim

In the BP-based Adams-Novikov spectral sequence for V(1)=S/(3,v1) at prime 3, the E2 class g in bidegree (s,t)=(3,55) (stem 52, chromatic beta-family generator in the Miller-Ravenel-Wilson/Shimomura E2 chart for BP_*/(3,v1)) supports d_5(g)=h up to a 3-adic unit, where h is the nonzero E2 class in bidegree (8,59) (stem 51), proved by a logged Toda-bracket shuffle <3,v1,- > identity plus a motivic-weight comparison map to the C-motivic Adams chart.

## Research outcome

TARGET resolved as FALSE: both named E2 groups vanish (t=55,59 odd vs even-concentrated cobar), so the claimed nonzero d5(g)=h is impossible. Self-contained proof in output/DRAFT.md with replayable parity script.

## Why this attempt failed

Failed axes: originality, value.

originality: Headline audited: E2^{3,55}(V1)=0 and E2^{8,59}(V1)=0 at p=3 by even concentration, hence no nonzero d5(g)=h. Normalized into three forms and searched in one scope_literature_search call (literal bidegree/differential; equivalent BP_*/(3,v1)/Ext/cobar/beta-family forms; dominance/broader census/classification/database). Fused 20 results; coverage partial=true (OpenAlex q1 error 'key pool unavailable HTTP 400', OpenAlex q0/q2 zero hits but status ok; SerpBase and Crossref ok) — recorded and continued with available providers plus direct nLab/Ravenel sources; one failure never establishes priority. Nearest priors (Shimomura 1997 L2-V1 d5/d9 to E10, Shimomura 2000 L2-V0, Isaksen et al. 2302.09123 prime-2 motivic mmf/tmf, MRW 1977 periodic phenomena) do not record the exact bidegrees, but that absence does not confer priority because a strictly stronger textbook theorem substantively implies the headline: BP_* even, BP_*BP even, BP_*(V1)=BP_*/(p,v1) even => Ext^{s,t}=0 for all s and all odd t (Ravenel Green Book; nLab Toda-Smith page confirms BP_*(V1)=BP_*/(p,v1) and |vi|=2(p^i-1)). Instantiation at t=55,59 yields the claim mechanically. Title/embedding similarity was not used; hypothesis-conclusion comparison shows prior implies claim. Hence the finding is a corollary/repackaging/recomputation of a known stronger fact. Adversarial checklist (synonyms, encodings, subset-of-broader-theorem, table row, recomputation) was tested — see decisive_checks. Originality FAILS; per policy never repairable. value: Correct disproof of an admitted-target premise, but not independently worth retrieving. The general even-vanishing lemma (Ext^{s,t}(V1)=0 for t odd) is textbook and future researchers cite the general lemma, not the instantiation at (3,55),(8,59). The two bidegrees have no pre-computation motivation except the admitted target, whose premise (nonzero beta-generator at t=55,59 odd) is false on elementary parity checkable at Admission — i.e. an ADMISSION_DEFECT context: target E2 existence contradicts even concentration. Value requires object+invariant motivated before computation, value not known/mechanically implied, and future need for the precise fact; here value is mechanically implied by evenness and scope is two arbitrary odd-t points among infinitely many. Falls under textbook restatement / mere instantiation / recomputation with no new differential witness, survivor, extension, method template, or downstream constraint beyond '0->0 vacuous'. Correcting the admission error is useful for this lane but does not create a citable invariant for chromatic/motivic/surgery programs. Value FAILS.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Disproves only the named nonzero d5 between nonzero classes in (3,55)->(8,59); a vacuous 0->0 differential is not ruled out but does not satisfy the claim. Does not decide any other V(1) bidegree with t even, any L2-localized differential, or any motivic comparison statement beyond the endpoint nonexistence. Uses standard BP degrees and cofiber sequences only.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
