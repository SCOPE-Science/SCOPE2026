# Scientific review: universal square-gap root profile

## Correctness

**PASS.** The exact membership criterion is \(z=qm+r\in\langle m,m+1\rangle\) precisely when \(q\ge r\). Inserting squares yields the region \(y>mx^2/(m+1)\). The complete quadratic correlation identity gives \(|T_m(h,k)|^2\le m\gcd(2k,m)\), with no primality restriction. Two-dimensional Erdős–Turán–Koksma, then at most \(\lceil m^{1/6}\rceil\) vertical strips, gives the uniform bound \(O(m^{5/6}\log(2m))\), including every interval endpoint. The accompanying checker replays thousands of direct finite verifications, but these are not substitutes for the analytic proof. The standard multidimensional discrepancy inequality is the cited external mathematical input.

## Originality

**PASS within checked literature.** Chappelon and Ramírez Alfonsín (2020) and Binner (2021) determine the largest omitted square in relevant numerical semigroups; Binner's Lemma 6 already gives the key elementwise criterion. Neither inspected full primary manuscript states a count of all square gaps with the universal root-density law or a uniform local quantitative rate. Searches checked equivalent formulations, broader theorems, potential tabulations, and implication direction. Shor's gap-residue equidistribution paper is an additional related source assessed from its abstract only; this cannot justify a whole-document absence claim. It studies all gaps mod fixed integers rather than the stated varying-modulus square-gap root statistic. Unindexed equivalent applications remain possible. Only the counting/profile theorem is offered as new, not its known ingredients.

## Mathematical value

**PASS.** Where the square Frobenius invariant records one extremal square, the square-gap count and its normalized-root distribution quantify the complete missing-square population. The explicit density \(1-t^2\), total constant \(2/3\), and uniform all-moduli error are natural structural data not implied by maximal-gap or ordinary-genus results. The contribution is meaningful even though the exponent is not claimed sharp and no unrelated downstream theorem is asserted.

## Scope and limitations

Applies only to \(\langle m,m+1\rangle\) and macroscopic root intervals, not arbitrary generator pairs or shrinking windows. Its novelty assessment rests on accessible sources and targeted searches and cannot exclude every unindexed equivalent. Independent scientific validation is not claimed.

Self-review: passed. Independent audit: not yet performed.
