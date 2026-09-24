# Independent audit — Goldbach-comet band census

**Review date (UTC):** 2026-09-24  
**Source path:** `2026/09/08/053`  
**Audited source tree:** `31a32d4249565c912c367ca70278ba3505e00008`  
**Review type:** separate AI independent audit.

## Claim audited

The record computes unordered Goldbach counts for every even target in the half-open interval `[210000,252000)`, aggregates them by target residue modulo 30, and reports exact band means/order/gaps plus Hardy–Littlewood-normalized residual statistics.

## Correctness — PASS

I independently generated primes through 252000 and obtained `pi(252000)=22203` with 3396 primes in `[210000,252000]`. I then computed the Goldbach counts independently by convolving the prime indicator and converting ordered convolution counts to unordered counts, with direct integer arithmetic for the diagonal correction. Across all 21,000 even targets I reproduced the record's 15 band sums exactly:

`0:4748970, 2:1770618, 4:1790339, 6:3570483, 8:1766583, 10:2383891, 12:3555482, 14:1776489, 16:1789521, 18:3556878, 20:2365554, 22:1786228, 24:3565034, 26:1783145, 28:1789793`.

Dividing by 1400 gives the exact order `8<2<14<26<22<16<28<4<20<10<12<18<24<6<0` and minimum adjacent gap `34/175`, again matching the record. Recomputing the stated singular-series normalization `H(n)=C2*n/(log n)^2 * product_{odd p|n}(p-1)/(p-2)` gives the same residual-band ordering, maximum absolute residual `0.2599740089406617` at target 215596, `G=1189`, and overall mean residual about `1.195115420728894`. Thus the numerical census is internally correct under its stated half-open convention and normalization.

## Originality — FAIL

A decisive pre-existing source was missed by the earlier review. Serge Durand's December 2025 manuscript *Empirical Verification of the 2:1:1 Modular Law in Goldbach Partitions up to 300,000* computes and publishes the complete unordered Goldbach counting function for every even target from 4 through 300,000, together with an open `goldbach_counts.csv` dataset and code, archived at Zenodo DOI `10.5281/zenodo.17042193`. It also studies modular structure through modulus 30.

The entire target interval `[210000,252000)` in this record is therefore already contained in the earlier public exact dataset. Once those pointwise counts exist, the record's 15 target-residue band sums, means, ordering, and exact gaps are obtained by routine filtering/grouping of published values. The Hardy–Littlewood residual columns add a standard singular-series normalization to the same already-published counts; they do not restore originality of the finite census. This is stronger than merely finding a qualitatively similar plot: the prior work publishes the raw values from which the headline exact table is mechanically derived.

## Scientific value — FAIL

After subtracting the pre-existing complete count dataset, the surviving contribution is a window-specific regrouping and standard normalization on one moderate interval. The three coarse tiers are the familiar singular-series/Goldbach-comet phenomenon, and the within-tier fine ordering is explicitly a finite-window census fact rather than a theorem or reusable structural result. The record supplies careful certification, but certification alone does not create a scientifically distinct contribution when the underlying exact values were already published and the new outputs are routine aggregations.

A bounded repair cannot rescue the record without replacing it by a genuinely new question: moving to a previously uncovered range, proving a structural theorem about band separation, or deriving a nontrivial error law would be new research rather than a correction of this record.

**Final disposition: FAILED — prior exact data cover the full interval, and the residual analysis is not sufficiently original or scientifically distinct.**
