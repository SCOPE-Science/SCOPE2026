# Independent Audit — 2026/09/11/026

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `508de9e44bbb16bf24b2a194bb5d18b4210a3001`
- Disposition: **FAILED**

## Correctness

**PASS** — The nonexistence proof is mathematically sound. If q>p are distinct odd primes, Sylow counting forces the q-Sylow subgroup to be unique in every group of order p^2q: n_q=p is impossible and n_q=p^2 would force q|(p-1)(p+1), leaving q=p+1, impossible for odd q. Thus the additive q-Sylow is characteristic and lambda-invariant; as a left ideal it is also a multiplicative subgroup, and uniqueness on the multiplicative side makes it normal, hence an ideal. If q<p, n_p=q would require q≡1 mod p, impossible, so the additive p-Sylow of order p^2 yields the corresponding ideal. Therefore no ideal-simple skew brace of odd order p^2q exists. The q|p+1 corollary and the p=2/order-12 exception are consistent with this argument.

## Originality

**FAIL** — The claimed research contribution is too close to already-classified and already-standard structure. Acri–Bonatto give exhaustive classifications of skew braces of size p^2q and explicitly use characteristic Sylow subgroups as ideals in the same order window. The submitted theorem is obtained by a short Sylow-congruence case split plus that established ideal mechanism. Even if the exact one-sentence universal corollary is not highlighted in those papers, the submission does not introduce a new classification method, brace invariant, construction, or structural mechanism beyond the existing p^2q classification framework.

## Scientific value

**FAIL** — As a standalone research finding, the result adds too little beyond the completed p^2q census and standard Sylow/ideal argument to justify a validated record. It is a useful explanatory corollary and a good consistency check on proposed simple examples, but it does not materially advance the finite-simple-skew-brace classification problem. The mathematical statement should be preserved as evidence, but not promoted as an independent validated finding.

## Limitations

- The rejection is for originality and scientific value, not correctness.
- This audit does not re-enumerate every isomorphism class in Acri–Bonatto; it checks that the submitted proof uses the same established order-window mechanism and adds only the elementary odd-prime Sylow split.

## Sources

- Skew braces of size p^2 q I: abelian type — A. Acri; M. Bonatto: https://arxiv.org/abs/2004.04291 — Exhaustive p^2q classification for abelian type; includes the characteristic-Sylow ideal mechanism used in this order window.
- Skew braces of size p^2 q II: non-abelian type — A. Acri; M. Bonatto: https://arxiv.org/abs/2004.04232 — Completes the p^2q classification in non-abelian type.
- On a family of simple skew braces — N. P. Byott: https://arxiv.org/abs/2405.16154 — Provides simple-brace context and the p=2/order-12 boundary behavior, not an odd p^2q novelty.

GitHub was read only as evidence. The pre-existing AUDIT.json was treated as evidence rather than authority; this disposition reflects an independent three-axis assessment.
