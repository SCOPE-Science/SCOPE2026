# Review: two-row odd-island shift entropy and periodic zeta

## Correctness

**PASS.** A seven-state parity-frontier graph recognizes exactly those two-row configurations whose finite occupied components have odd size. Its primitive, right-resolving presentation gives the entropy as the logarithm of the Perron root of a factored characteristic polynomial. For periodic label sequences, the only difference between periodic symbols and periodic graph states comes from no-break configurations: all occupied components extend infinitely, giving two parity lifts for an even singleton-column count and zero for an odd count. The signed three-state matrix subtracts this discrepancy exactly, proving the rational zeta formula. A standalone standard-library program verifies both characteristic polynomials and 174,760 separate finite component decisions. The all-length conclusions are proved analytically.

## Originality

**PASS, subject to historical-priority risk.** The motivating 2025 Callard thesis, Section 7.1, explicitly describes the planar finite-odd-component shift and its soficity but does not compute horizontal strip entropy or periodic-point zeta. Hochman's full one-page original problem note defines the parity shift without these computations. General finite-state methods and hard-square strip entropy techniques do not themselves give the quintic or the necessary signed correction. Targeted searches for the exact polynomial, initial periodic counts, object aliases and stronger formulations found no equivalent published value. Older specialized ladder enumerations or unpublished seminar notes remain possible; no independent priority certification is asserted.

## Value

**PASS.** The two-row strip is the first width at which vertical connectivity affects the odd-component condition, making its complete entropy and periodic-point census natural reference invariants at the unresolved planar frontier. The rational zeta numerator is not cosmetic: it corrects the double-counting and omission of configurations with horizontally infinite islands in a right-resolving cover. The result gives a reproducible algebraic benchmark for wider-strip investigations.

## Limits and closest sources

Only the infinite two-row ladder with open vertical boundary, horizontal shift and nearest-neighbor cells is treated. The result does not decide planar soficity, quantify arbitrary strip width or establish unrestricted two-dimensional spatial entropy. The arithmetic proof and finite checker are supplied; an independent mathematical audit has not occurred. Closest sources are Callard's 2025 thesis (Section 7.1), Hochman's original problem note and the hard-square strip-entropy setting of Pavlov (arXiv:1011.1983, abstract only).

Self-review: passed. Independent audit: not yet performed.
