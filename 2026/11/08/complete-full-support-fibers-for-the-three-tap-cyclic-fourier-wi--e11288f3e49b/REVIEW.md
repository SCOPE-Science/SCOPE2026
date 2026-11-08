# Mathematical review

## Correctness — PASS

At every translated three-tap polynomial, a full cyclic frequency sweep recovers exactly the three local autocorrelations. In dimensions \(N=2m\) with odd \(m\ge3\), equality of the lag-two term forces any comparison signal to differ only by unimodular factors on even and odd sites. Equal lag-one terms either merge these factors or imply adjacent correlations alternate by one fixed phase and its inverse. This forces constant two-step coefficient ratios, an \(m\)-th root of unity, and the unique additional partner. The converse is checked by direct substitution; all quantifiers and the degenerate \(\delta=1\) boundary are handled. Finite checker tests support but do not replace this proof.

## Originality — PASS, with residual priority risk

The primary 2021 periodic-STFT results of Bendory–Cheng–Edidin and the 2015 Jaganathan–Eldar–Hassibi nonvanishing-window results establish generic recovery, not a classification of every fiber for this fixed flat three-tap window. Bartusel's 2023 exact short-window theorems assume separated zero sites and thus do not apply to full-support signals. Closest indexed related claims on two-tap nonvanishing fibers and odd-order endpoint-lag recovery differ in their measurement supports or arithmetic assumptions. Searches for equivalent fixed three-tap full-support fibers did not locate an implication covering the explicit classification. An unindexed specialist derivation may exist; this is a self-review, not an independent priority certificate.

## Mathematical value — PASS

The three-tap flat window is the most elementary overlapping local Fourier measurement with a lag-one correlation containing two terms. Characterizing its exact failures, rather than merely proving almost-everywhere uniqueness, makes its deterministic limitations transparent. The full two-element fiber law and exact exceptional geometry have direct mathematical content across infinitely many cyclic lengths.

## Scope and verification limits

Only cyclic lengths twice an odd integer at least three, full modulation/translation sampling, nowhere-zero signals, and equal nonzero taps are covered. The theorem does not assert stability, arbitrary even-order recovery, or independent validation. The standalone checker checks representative periods and reconstructs correlations; the universal result follows analytically.

Self-review: passed. Independent audit: not yet performed.
