---
audit_date: 2026-10-01
status: failed
---

# Independent scientific audit

## Final claim

For connected graphs, the maximum fixed-order gap \(\gamma_{\rm cer}-\gamma\) is \(n/2\) for even \(n\) and \((n-3)/2\) for odd \(n\); the proposed equality classification uses coronas and diadems and includes the factor-two statement \(\gamma_{\rm cer}=2\gamma\) exactly for coronas.

## Correctness — PASS

Tracing equality through the standard construction behind \(\gamma_{\rm cer}\le\gamma+|S_1|\le2\gamma\) forces every vertex of a suitable minimum dominating set to be a weak support with exactly its private leaf outside the set, hence a corona. The fixed-order parity bounds then follow from \(\gamma\le n/2\), the impossibility of certified domination number \(n-1\), and the published characterizations of \(\gamma_{\rm cer}=n\) and \(\gamma_{\rm cer}=n-2\). The Graph-Atlas artifact exhaustively matches the theorem through order seven but is corroborative only.

**Checked sources.** Assigned RESULT.md and artifacts/verify_graph_atlas.py at the frozen source tree; Dettlaff--Lemańska--Topp--Ziemann--Żyliński, Certified domination, arXiv:1606.03257 full HTML; Dettlaff et al., Graphs with equal domination and certified domination numbers, 2019

**Residual risks.** No correctness defect was found.

## Originality — FAIL

The final theorem is covered at the required implication level by the foundational certified-domination paper. Its Theorem 3.3 proof gives the half-shadowed weak-support construction, Corollary 3.5 gives \(\gamma_{\rm cer}\le2\gamma\) with corona sharpness, Theorem 5.3 characterizes \(\gamma_{\rm cer}=n\) by coronas in the connected case, and Section 5.1 characterizes \(\gamma_{\rm cer}=n-2\) by diadems for connected graphs of order at least five. Following equality through the already-published proof yields the factor-two converse with no new nonstandard lemma; the parity gap classification is then a short corollary of those published large-value theorems and the classical domination bound.

### Equivalent formulations

The gap-extremum and factor-two-equality formulations are consequences of the same published inequality chain and large-value classifications.

### Broader coverage

The published large-value theory is broad enough to dominate the fixed-order classification once the elementary order bounds are inserted.

### Exact database or table

Absence of the exact gap formula in a database does not restore originality because the primary theorems mechanically imply it.

### Claim versus prior implication

The claimed new core is a routine equality-case extraction and combination of already published results.

**Checked sources.** https://arxiv.org/abs/1606.03257; https://doi.org/10.7494/OpMath.2019.39.6.815; published mathematical corpus search

**Residual risks.** No residual search risk can overcome the direct implication from the inspected foundational paper.

## Value — FAIL

The parity formula and corona/diadem packaging are neat, but once the published factor-two proof and the published \(n\) and \(n-2\) classifications are assembled, the remaining work is a short equality-case trace and classical order bound. Under the shared value bar, that is a routine corollary rather than a separate motivated mathematical gap.

**Checked sources.** Dettlaff et al. 2016 foundational full text; Dettlaff et al. 2019 equality paper

**Residual risks.** The statement remains useful as a concise corollary package.

## Limitations

- Finite simple connected graphs only.
- The rejection is scientific prior-implication coverage, not a correctness or access failure.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and value.
