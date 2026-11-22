# Scientific review

## Correctness (C): PASS
The proof in `RESULT.md` establishes forced first and last markers of every bounded output one-run, independence of the resulting binary input blocks, and the exact compositions/zero-run-avoidance inverse factors. Counting the output-run grammars proves the two generating functions. The strictly ordered positive roots yield the exponential ratio. Executing `verify.py` tests all 50 width/length instances with input lengths at most 16; it is supporting finite evidence, not a replacement for the proof.

## Originality (O): PASS, subject to the stated risks
The 2020 binary sliding-window constrained-code paper counts admissible source words under window-weight bounds, not Boolean OR measurement image populations. The 2022 local-histogram reconstruction paper retains integer local counts, so it does not directly supply the coarsened binary observation image or singleton counts. Jen (1989) already provides generic CA preimage recurrences and explicit Rule 254 preimage expressions; these earlier results are credited and are relevant prior coverage for the width-three per-output problem. The distinct contribution assessed here is the all-width, all-length exact image and singleton-output rational generating functions and a strict asymptotic gap, neither found as an explicit statement in those inspected sources. Other unindexed formulae remain a priority risk.

## Value (V): PASS
The measurement map is a natural noise-free sliding binary event detector. Exact attainable-output counts determine optimal noiseless codebook size, and exact singleton-output counts measure when reconstruction is intrinsically unique. Their strict exponential separation and the full runwise inverse-list formula expose a nontrivial distinction between the two notions for every finite sensor width.

## Limits
The linear, ordered, finite noiseless Boolean-OR model and fixed-width asymptotic are essential; circular/noisy/thresholded or multidimensional models are not analyzed. The verification checks small instances only. There has been no independent mathematical or priority audit.

Self-review: passed. Independent audit: not yet performed.
