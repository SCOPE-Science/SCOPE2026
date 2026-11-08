# Scientific review

## Correctness: PASS

The theorem states the dyadic strips, the exceptional boundary extension, Lebesgue-distributed initial points, all real \(s>0\), all integer \(t\ge0\), and the restriction \(t\ge2\) on exact Wasserstein distance. The branch map gives independent binary digits and level waits of one or two iterations; the two cases yield the full moment recurrence. The eigenvalues and leading coefficient follow from the recurrence. Strong law and renewal CLT yield the stated normalization and variance. For transport, the dynamics is in the right half of the torus after two steps, and a matching primal coupling/dual Lipschitz witness proves equality. The rational checker independently reproduced the recurrence at 44 nontrivial moment/time pairs and additional transition assertions. Finite checks do not replace the analytical proof.

## Originality: PASS within inspected evidence

The originating full text [1, Example 4.1] presents the same countably piecewise translation and only establishes qualitative concentration on a non-invariant vertical segment. The earlier full text [2, Section 4] treats different systems with qualitative weak-ergodic limits. Targeted searches for dyadic focusing, exact moment recurrences, fair binary renewal coding, Gaussian fluctuations and Wasserstein distance found no stronger statement covering these particular joint conclusions. The ordinary renewal CLT and optimal-transport duality are standard and are not claimed as new. It remains possible that an unindexed source contains the exact calculation; no exhaustive publication-priority guarantee is asserted.

## Mathematical value: PASS

For a locally isometric system with no invariant limit measure, the new exact concentration spectrum quantifies a qualitative phenomenon previously unexplained in time. The strict separation between the typical focusing exponent and the sharp mean transportation rate is a natural structural effect of exceptional initial conditions. The result covers all positive moments and every time, rather than an ad hoc invariant or a finite numerical enumeration.

## Reproducibility and limitations

Run `python3 verify_focusing.py` using Python's standard library. The certificate checks rational integrals over explicit dyadic branch cylinders, independent binary waits, and the right-half-torus transport condition. It does not compute noninteger moments or prove the limiting CLT; those follow from the written analytical argument. The theorem makes no claims about arbitrary initial singular measures or finite-partition piecewise isometries. The explicit null-boundary value makes the weak limit non-invariant, and unknown unindexed literature remains a novelty risk.

Self-review: passed. Independent audit: not yet performed.

## Sources

[1] M. Blank, *Invariant measures of torus piecewise isometries*, https://arxiv.org/abs/2106.16021, Section 4.

[2] M. Blank, *Ergodic averaging with and without invariant measures*, https://arxiv.org/abs/1709.06327, Section 4.
