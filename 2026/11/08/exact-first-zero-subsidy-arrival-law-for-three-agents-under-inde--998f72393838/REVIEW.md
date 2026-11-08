# Scientific review

## Correctness — PASS
The collision deletion lemma is proved for all strict three-agent preference profiles. Its stochastic conditional step handles both the two-agent and the three-agent collision, including previously revealed favorites, so the full product is an exact probability identity at every horizon. The first-hitting distribution follows from monotone feasibility, and a gamma ratio establishes the factorial tail. An exhaustive independent comparison through six houses checks each finite enumeration result but is not used as a proof for arbitrary horizons.

## Originality — PASS, with explicit risks
Gan, Suksompong and Voudouris (2019) already prove a general deterministic algorithm based on deleting houses attached to minimal Hall violators and a separate high-probability theorem when agent count grows. This work credits that algorithm and adds an exact three-agent random-stream first-feasible-arrival distribution. Teh and collaborators (2026) introduce the sequential house-and-subsidy setting but the material inspected did not supply that exact law. Search comparisons include first-arrival aliases, specific rational probabilities, generalization to random independent preferences, and nearby two-sided matching / random-priority findings. The later preprint's full appendices were not completely accessible and unindexed parallel calculations remain a risk.

## Mathematical value — PASS
The complete law yields exact prefix success probabilities, individual arrival hazards, finite expected first-zero-subsidy time, and a sharp superexponential tail; these are useful offline feasibility benchmarks against which a sequential mechanism with costly recourse can be judged. Three agents are a natural first multi-collision model. No operational online implementation or budget competitiveness is claimed.

## Limits and nearest literature
The assertion covers three agents with iid atomless utilities and unrestricted terminal reassignment only. Closest: Gan–Suksompong–Voudouris, *Envy-Freeness in House Allocation Problems*, arXiv:1905.00468; Teh–Cohen–Celine–Yu–Wooldridge, *Online House Allocation with Subsidy*, arXiv:2609.29691v1; Manurangsi, *Envy-Free Allocations for Random Non-Additive Valuations*, arXiv:2610.34434. The latter concerns different partition-type random allocation.

Self-review: passed. Independent audit: not yet performed.
