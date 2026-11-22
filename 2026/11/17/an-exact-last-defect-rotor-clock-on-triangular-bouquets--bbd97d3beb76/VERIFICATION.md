---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS. For a bidirected bouquet of k triangles with a single chip at hub h and exact specified cyclic rotor order (increment-before-move), every nonhub directed rotor cycle is exactly the local two-cycle (a_j,b_j) with initial bits (1,0). By the recurrent-state unicycle criterion of Holroyd et al., the initially all-good states (3^k) are already recurrent. For any state with bad petals, scanning earlier petals in hub order costs six moves per good and four per bad, changing a bad petal to a good state; after the hub's arrival at the final bad petal J, the chip lies on the only remaining directed cycle. Thus first entry τ=6J−2B+1 (B prior bad petals), *not* first return to hub. Counting trailing good petals and independent preceding choices proves H_k(z)=3^k+Σ_{j=0}^{k−1}3^{k−1−j}z(z^4+3z^6)^j; H_k(1)=4^k, maximum 6k−5 has 3^{k−1} realizers. Differentiate at z=1 for Eτ=(11/2)k−21+21(3/4)^k. If S_k~Bin(k,1/4) and R=k−1−J is tight geometric trailing-good count, τ=6k−3−6R−2S_k on S_k>0. The binomial CLT yields normalization sqrt(3k/4). Independently implemented full deterministic chip+rotor orbit and first repetition, exhaustively checked all 1,364 initial assignments for k=1..5 against τ and H_k histogram, including maxima 1,7,13,19,25 and counts 1,3,9,27,81. Original verify_rotor.py source inspected; independent simulation corroborates the explicit all-k excursion proof.

## originality

PASS

PASS best-of-knowledge. The standard single-chip unicycle criterion and Eulerian recurrent tours are prior general results, but do not supply the labelled distribution of *transient entrance times* for initial peripheral rotor choices on this specific non-tree bouquet with a fixed hub cyclic order. Resultary contains related transient clocks on cycles, sunlets, comb trees and spiders, none of whose model-specific formulas imply the present last-bad-petal histogram. Novelty is the exact first-recurrence law/CLT, not the unicycle criterion or standard CLT.

## value

PASS

PASS. Entry to full deterministic rotor recurrence on a natural cactus graph is distinct from Eulerian period and hub return time. The last-defect formula completely classifies labelled initial rotor states, yields a sharp rare maximal-delay shell and demonstrates Gaussian versus extremal clocks. This is a motivated natural exact initial-condition invariant, not a generic restatement of a unicycle criterion. Fixed ordering and initial hub state are essential limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
