# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Information-Spectrum Converse with Explicit Marker Overhead for Segmented Block-by-Block Deletion Codes at N=1024
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1145
- **Disposition:** NO_RESULT
- **Domain:** Information Theory
- **Method:** Dobrushin-style information-spectrum meta-converse with synchronization penalty

## Problem

Consider the binary segmented single-deletion channel with segment length 32 and blocklength N=1024 (32 segments, at most one deletion per segment, boundaries unknown) and the class of block-by-block decodable codes that resynchronize per segment. Using Dobrushin-style information-spectrum reasoning with explicit marker-resynchronization accounting, decide whether every such code at block error at most 1e-3 has rate at most 0.78, with the penalty term separately identified.

## Attempted claim

For the binary segmented single-deletion channel with segment length 32 and blocklength N=1024, every block-by-block decodable code with block error probability at most 1e-3 has information rate at most 0.78 bits per channel use, where the 0.78 ceiling decomposes into a memoryless information-spectrum outage term plus an explicit per-segment marker-uncertainty penalty that vanishes when boundaries are revealed; the upper bound R*(1024,1e-3)<=0.78 is the TARGET.

## Research outcome

Target blocked: proved an explicit fixed-marker deletion collision and certified the conditional tax arithmetic (798.58 of 798.72 bits), but the bounded recovery test showed the memoryless outage term near 0.89, leaving the universal 0.78 converse unproved; clean exit with artifacts preserved.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No full converse was proved: the marker tax was certified only for a fixed single-bit-marker construction rather than all block-by-block resync strategies, the log2(33) packing overhead used is a zero-error figure whose finite-error correction is unquantified, and the information-spectrum outage term was only heuristically estimated near 0.89 via Monte Carlo, so the 0.78 ceiling remains undecided and the partial certificate is preserved for future work.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No full converse was proved: the marker tax was certified only for a fixed single-bit-marker construction rather than all block-by-block resync strategies, the log2(33) packing overhead used is a zero-error figure whose finite-error correction is unquantified, and the information-spectrum outage term was only heuristically estimated near 0.89 via Monte Carlo, so the 0.78 ceiling remains undecided and the partial certificate is preserved for future work.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
