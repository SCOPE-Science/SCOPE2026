---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Iterating the word-overlap update t times gives a q-ary NOR tree on the initial coordinates ending with the output's prefix of length d-t. Its q child blocks have disjoint terminal-word classes; different output prefixes give disjoint blocks partitioning all initial coordinates. At t=d there is just one block, so every configuration reaches the uniform oscillator. At d-1 the q blocks can be independently set to yield different outputs (constant leaf inputs realize either polarity), so the bound is sharp. Block independence gives the CDF for integer t and the exact labelled counts and phase split; uniformity persists, so this is first uniform time, not first hit of the all-one phase. For phi(x)=(1-x)^q, the second iterate's derivative is strictly unimodal and h(x)-x has at most three zeros by Rolle. They are 0,p_*,1; the expansions at the endpoints give the signs and yield attraction to the respective endpoints off p_*. For the smaller error along a fixed parity, L=-log(error) satisfies L_{next}=qL+O(1); starting once L is large and summing the normalized recurrence bounds it above and below by positive multiples of q per pair of updates. Odd parity has the same scale by the one-step map. Thus m=q^(d-t) and error switch from m*error diverging to vanishing across t=2 log_q d plus or minus a sufficiently large fixed constant. At p_* the exact integer-s tail is the stated doubly exponential bound; p=0,1 give T=0. These arguments require fixed q and p for the asymptotics. New exact graph enumeration for (q,d)=(2,1),(2,3),(2,4),(3,2),(4,2) checked the first-entry law at p=1/2,2/5 and the fair-bit phase counts; e.g. the (2,4) shells are (2,6560,2400,36288,20286). Replay: python3 /workspace/reviews/reproduce.py 1; /workspace/reviews/reproduce-output.txt. Bundled code and recorded output were read, not executed; the asymptotics are proved, not inferred from these cases.

## originality

PASS

Credit the recurrent uniform oscillator already mentioned in the close Kautz record, the word-prefix partition in the same-graph OR proof, and the isolated critical point and endpoint convergence of the elementary NOR-tree probability map. The retained distinct claim is the de Bruijn NOR first-uniform-time distribution and the logarithmic-depth versus full-depth timing law. The closest Kautz theorem shares the scalar recursion and the disjoint-tree method, but tests a different event under a different word constraint and has a separate frozen contribution. Its critical observable is fixed-phase mass, not synchronization time. The same-graph OR distribution is a different hitting probability without the critical map. Neither is an exact statement on the assigned initial distribution and NOR first-uniform event. The comparison does not claim priority ordering between same-day records.

## value

PASS

The same finite network can have a typical synchronous first-entry time of order log d or almost the entire worst-case depth depending on a single fixed initialization bias. This is a meaningful distinction for inhibitory Boolean dynamics on a standard graph, quantified by an exact joint first-entry law; it is not a claim of new single-tree probabilities or mere recovery of an eventual oscillator. No approaching-critical window is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
