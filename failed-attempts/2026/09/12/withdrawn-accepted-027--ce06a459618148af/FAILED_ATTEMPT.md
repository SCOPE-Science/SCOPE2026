# FAILED ATTEMPT — NOT A VALIDATED FINDING

Record: `2026/09/12/027`  
Independent audit date: 2026-09-28 (UTC)  
Task: `e18be9f5efb960e9c92ed317c6afd109`

This package is not accepted as a validated research finding under the three-axis audit. It is retained intact for provenance and should be relocated to the assignment-designated failed path.

## Correctness

The finite ledger is internally correct. An independent residue DP gives |VT_0(26;25)|=1,290,556 and 1,290,555 usable words after removing 0^25, so a 2^20 subcode fits. The R1/R2 marker rule prevents the six-bit no-deletion window from being forged by any single deletion, and the deletion branch always exposes a genuine one-deletion trace of the 25-bit VT word. Thus the deletion-only decoder is zero-error for every per-segment deletion pattern. The rates 640/1024=0.625 and log2(1,290,556)/32≈0.6343613 are also correct.

## Originality

Li, He, and Tang already publish the same marker+codeword+marker VT construction for the segmented single-insdel channel and prove that it corrects one insertion or deletion per segment with linear-time encoding/decoding and redundancy log2(n-6)+7 bits. The submitted deletion-only n=32 instance is therefore a restriction and numerical specialization of a stronger prior theorem. The exact VT residue count and the choice of a 2^20 integer subcode are routine finite arithmetic, not a new coding construction or theorem.

## Scientific value

The N=1024 statement simply concatenates 32 instances of the already-published segment code, so deterministic zero error has no new finite-blocklength probability analysis. The advertised 0.68 bound is only a loose codebook-counting ceiling for this named family, not a channel converse, and follows from the same small VT census. The ledger is useful as implementation/reproducibility material but does not clear the standalone scientific-value threshold.

## Consequence

The original package remains useful as computational evidence or target triage, but its research headline must not be represented as an independently validated standalone finding.

## Evidence

- [Li–He–Tang, Marker+Codeword+Marker: A Coding Structure for Segmented Single-Insdel/-Edit Channels](https://arxiv.org/abs/2402.04890): Publishes the same MCM/VT family for arbitrary segment length, proves correction of segmented single-insdel errors, and states redundancy log2(n-6)+7 with linear-time encoding/decoding; this strictly covers the submitted deletion-only correctness theorem before n=32 is substituted.
- [Li–He–Tang, IEEE Transactions on Communications version](https://doi.org/10.1109/tcomm.2025.3622957): Peer-reviewed publication of the general MCM construction and stronger single-insdel result.
