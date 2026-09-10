# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A boundary-contact detector for one Mazur-type Stein cork via d3 and Heegaard Floer contact class
- **Round:** 2026-09-07-first-light-01
- **Lane:** 662
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Differential Topology
- **Method:** Stein handle-calculus with Heegaard Floer contact invariant and d3 comparison across the cork boundary involution

## Problem

Fix one explicit Mazur-type contractible Stein handle diagram D* with Stein structure J0 and let J1 be the pullback Stein structure under the cork boundary involution tau on Y=partial W*. Are the induced boundary contact structures xi0 and xi1 non-isotopic tight contact structures distinguished by the three-dimensional invariant d3 and the Heegaard Floer contact class, proving J0 and J1 non-homotopic and obstructing tau from extending as a contactomorphism?

## Attempted claim

Let W* be the fixed Mazur-type contractible Stein cork with Stein structure J0 given by diagram D*, let tau be its boundary involution, J1=tau*J0, and xi0, xi1 the induced contact structures on Y=partial W*. Then xi0 and xi1 are non-isotopic tight contact structures with d3(xi1)!=d3(xi0) and distinct Heegaard Floer contact classes c+(xi0)!=c+(xi1) in HF+(-Y), so J0 and J1 are non-homotopic Stein structures and tau does not extend as a contactomorphism.

## Research outcome

TARGET disproved: d3 is natural under the orientation-preserving cork involution, so the claimed d3(xi1)!=d3(xi0) for the tau-pullback pair is impossible for every diagram; the conjoined d3-plus-c+ detector claim is false as stated.

## Why this attempt failed

Failed axes: originality, value.

originality: claim_route is explicitly TARGET (research_report.claim_route=TARGET); audited normally with no preset-value presumption. Live retrieval executed as one scope_literature_search call with three normalized forms: (a) literal Mazur-cork τ-pullback d3-inequality, (b) Gompf-d3 naturality/invariance under orientation-preserving diffeomorphism/pushforward, (c) dominance census/classification of Mazur-type Stein-cork boundary contacts by d3/c+. Tool returned 20 fused results with partial coverage (SerpBase ok all three; Crossref ok all three; OpenAlex error on query 0, zero hits on queries 1-2 after internal retries); continued with available providers. No fused source states the lane-662 disproof verbatim, and no source states the original target distinction — consistent with Admission originality PASS for the target. HOWEVER headline equality d3(τ*ξ0)=d3(ξ0) is a direct mechanical corollary of a known stronger fact: general diffeomorphism/homotopy invariance of Gompf d3. Gompf (1998) homotopy classification + Ding-Geiges-Stipsicz survey (cited in DRAFT itself as method) prove d3 depends only on homotopy class at fixed Spin^C; Etnyre/support-norm note and contact-surgery-numbers snippet retrieved (plane field on rational homology sphere determined up to homotopy by Spin^C + d3/Γ) entail naturality d3(φ*ξ)=d3(ξ) for orientation-preserving φ. Instantiation φ=τ requires no cork-specific diagram, tb/rot count, or Floer analysis; DRAFT proves it for ANY contractible W, ANY orientation-preserving τ, ANY ξ0, confirming generality. This is exactly the 'corollary/repackaging of a known stronger fact' failure mode. Prior need not state W*/τ verbatim to cover claim; substantive implication suffices. Therefore originality FAILS. Never repairable per policy. value: Independently worth finding later? No. The equality is mechanically implied by textbook d3 invariance; no new exact invariant value, census, classification, table row, or method is produced. No diagram D*, tb/rot, χ/σ, d3 number, or HF computation specific to W* is needed or supplied — proof is diagram-independent by design. A future researcher needing d3(τ*ξ)=d3(ξ) needs only the general Gompf/DGS invariance, not this instance. Negative payoff (closing the d3-gap route for pullback pairs, redirecting to genuinely distinct pairs like Karakurt-Oba-Ukida admissible-vs-planar) is useful lane hygiene and the Remarks repair direction is sound, but guidance alone is not an independently retrievable result under the STANDARD (reject textbook restatements, mere certificates, unexplained enumerations even if correct). The admitted target's value does not transfer to a trivial corollary disproving it; value must inhere in the submitted headline. FAIL.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: Disproves only the conjoined target as stated (which demands the d3 gap); says nothing about the c+ comparison alone, about contactomorphism extension, or about Stein-homotopy of genuinely distinct (non-pullback) Stein structures such as the Karakurt-Oba-Ukida admissible-vs-planar pair. Interior reading J1=tau*J0 is ill-posed (tau defined only on Y); proof grants the charitable boundary-pushforward reading.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
