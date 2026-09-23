# Independent audit — 2026-09-22 campaign

**Record:** SCOPE-20260907-013  
**Original source path:** `2026/09/07/013`  
**Audited repository state:** `1182b71328a408a740c274616869ab885009b620`  
**RESULT.md blob:** `46af968f6b91caa2a68777f88d2734a717a1ddaf`  
**Review date:** 2026-09-23 UTC  
**Reviewer:** separate AI independent audit; no Lean or expert attestation is claimed.

## Claim audited

The record proves nonexistence of a cyclic `(51,25,12)` difference set by using multiplier 13 to reduce to 924 fixed candidates, and presents the candidate spectra as a rerunnable certificate.

## Correctness — PASS

I independently reconstructed multiplication-by-13 orbits on `Z_51`: three singletons and twelve four-orbits. A fresh enumeration of all `C(12,6)=924` fixed 25-subsets containing singleton 0 found **0** difference sets. The independently obtained max-deviation histogram is exactly `2:48, 3:96, 4:558, 5:80, 6:36, 7:40, 8:36, 9:16, 10:8, 12:6`, and the closest candidate is combination `(0,1,2,3,8,9)` with counts in `[10,14]` and squared deviation 56. These agree with RESULT.md. The multiplier-orbit reduction is mathematically sound given the cited First Multiplier Theorem.

## Originality — FAIL

The record itself correctly acknowledges that bare nonexistence was already known. Baumert and Gordon, *On the existence of cyclic difference sets with small parameters*, arXiv:math/0304502 / Fields Institute Communications 41 (2004), is explicitly devoted to resolving the remaining small cyclic-difference-set parameter cases and extending cyclic Hadamard nonexistence searches. The record's claimed residual novelty is therefore not the theorem but only an explicit 924-candidate multiplier-13 catalog and spectra for one already-settled triple.

I searched `cyclic (51,25,12) difference set`, `Hadamard difference set 51 25 12`, `multiplier 13 difference set 51`, and the Baumert–Gordon small-parameter literature. I also checked contemporary `(51,25,12)` Hadamard-design literature to distinguish the cyclic question from existence of noncyclic symmetric designs. No uncovered new mathematical statement remained after subtracting the known cyclic nonexistence result.

## Scientific value — FAIL

A deterministic 924-case replay is useful as a pedagogical certificate, but it is too small and too parameter-specific to constitute a substantial reusable contribution once the nonexistence theorem is removed. It introduces no stronger bound, classification, reusable algorithmic reduction beyond the standard multiplier theorem, or new family. The spectra do not change the known existence frontier.

## Repair assessment

No bounded repair preserves this record's identity while making the surviving contribution both original and scientifically substantial. Reframing the package as a reproducibility example would be honest, but would not satisfy the repository's validated-finding threshold.

## Final disposition

**FAILED.** Correct computation, but failed originality and value after known prior coverage is accounted for.