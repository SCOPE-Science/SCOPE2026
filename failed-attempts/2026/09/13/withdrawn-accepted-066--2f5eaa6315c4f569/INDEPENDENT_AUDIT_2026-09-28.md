# Independent Audit — 2026/09/13/066

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `49ce6a0d5d1864f25dbe25841b9d37fcb681b3e3`
- Disposition: **FAILED**

## Correctness

**PASS** — The five-pair covering certificate is correct. Exact integer inequalities certify W0=2290867 as floor((10^12)^0.53). Each listed pair has gap at most 80, and the successive reach values overlap so that every integer x from 10^12 through 10^12+10^7 is covered by at least one pair inside [x-W0,x], which is contained in [x-x^0.53,x]. The supplied verifier's trial-division bound is also complete: every listed candidate is below (1000005)^2, so division by all primes through 1000005 certifies primality. The proof does not rely on the larger segmented-sieve census.

## Originality

**PASS** — The exact finite five-pair chain at this numerical height is a newly assembled certificate rather than a direct numerical consequence stated in the cited asymptotic bounded-gap literature. Its originality is narrow and computational: it is the particular exact certificate, not a new theorem about prime gaps.

## Scientific value

**FAIL** — The result is a one-off finite verification over a fixed 10^7-wide interval, proved by ten primality checks and elementary overlap inequalities. It gives no new method, asymptotic estimate, distributional phenomenon, or reusable theorem beyond the specific requested constants. The certificate can be useful for validation of that benchmark, but its mathematical scope is too narrow for an independent research finding.

## Sources

- Bounded gaps between primes in short intervals (Ryan Alweiss; Steven Luo): https://arxiv.org/abs/1707.05437 — Nearest asymptotic background; it does not supply the record's exact finite chain at 10^12.
- Assigned record snapshot (SCOPE-Science/SCOPE2026): https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/13/066 — Contains the self-contained verify_chain.py certificate audited here.

## Limitations

- The scientific-value verdict does not question the finite claim's truth.
- The audit relies on the self-contained chain proof rather than independently reproducing the 12,290,868-integer segmented census, which is not load-bearing.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence. Open-access/preprint sources were checked first; Oxford Download was not needed.
