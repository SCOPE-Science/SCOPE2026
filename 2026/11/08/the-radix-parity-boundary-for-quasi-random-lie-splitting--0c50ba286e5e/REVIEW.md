# Review: The radix-parity boundary for quasi-random Lie splitting

## Correctness — PASS

The two-operator implementation matches the point-to-permutation ordering in Li–Liu–Wan [1, §2]: a radical-inverse point in the upper half yields the factor \(e^{\tau A}e^{\tau B}\). Even-base digit comparison is exact, including the threshold and finite expansions. The odd-base middle-digit recursion proves the explicit imbalance \(S_{N_k}=1-mk\), not merely a finite numerical pattern. The product-telescoping and Abel-summation argument gives a uniform \(O(\tau^2)\) bound for every bounded generator pair at fixed time. The three-dimensional upper-triangular example gives the exact error \(\tau^2|S_N|/2\) by central nilpotence, independently of asymptotic estimates. Exact rational diagnostics in `verify.py` passed, but are supplementary and do not certify infinitely many cases.

## Originality — PASS, with priority risk

The primary article [1, §§2–4, 6], inspected in full-text HTML in its current revision, proves generic \(O(\tau^2(1+\log N))\) bounds and its sign sequence has a logarithmic discrepancy estimate. The displayed results do not give the exact even-versus-odd radix split, an improved all-even-base error bound, or an odd-base lower-bound witness. Classical Strang pairing [2] and radical-inverse digit recurrences [3] are expressly recognized as ingredients, not claimed original. Comparison searches for the source title, van der Corput half-interval parity, logarithmic sharpness and nilpotent Lie error did not reveal an equivalent published operator-splitting theorem in the searched records. Residual risk: an equivalent result may exist in historical discrepancy analyses or an unindexed numerical splitting note; an absence of a search hit is not proof of uniqueness.

## Value — PASS

The source's convergence rate has an apparently uniform logarithmic loss. This result proves exactly when that loss is an artifact of the estimate and when it cannot be removed from a universal theorem in the two-operator bounded-linear setting. The even-base result gives a stronger guaranteed rate; the odd-base witness proves that no universal \(O(\tau^2)\) estimate is possible. The radix-two Strang equivalence distinguishes a familiar symmetric scheme from a genuinely aperiodic driver, aiding interpretation of convergence experiments and radix selection. The complete odd-versus-even classification is a motivated numerical-method boundary rather than an arbitrary digit computation.

## Closest literature and limitations

[1] Lei Li, Yunxiao Liu and Chenchen Wan, *Quasi-random splitting method for accurate and efficient multiphysics simulation*, arXiv:2603.27654, §3.2 (signs and logarithmic bounds), §4.1 (bounded linear convergence) and §6 (conclusion). Historical context: Strang (1968) [2]; Dick and Pillichshammer (2010) [3]. The extension is confined to two operators and bounded linear generators; no claim is made for more operators, arbitrary nonlinear systems, floating point arithmetic or the broader original source framework. The lower bound is supplied by one exact family at infinitely many time-step counts, not by every generator pair.

Self-review: passed. Independent audit: not yet performed.
