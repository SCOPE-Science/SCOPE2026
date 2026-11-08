# Self-review

## Correctness (C): PASS

The open-hole convention and the distinct interval endpoints are explicit. At the threshold \(a=7/17\), the eight partition intervals have images with endpoints in a forward-invariant eight-cycle and the distinct two-cycle \(\{0,1\}\). Reconstructing their branch images gives the displayed exact directed graph. Its only strongly connected components are simple cycles of lengths two, four, one and one; all other paths enter one of these. A survivor that reaches an endpoint enters the boundary cycle. For any other survivor, eventual periodic cell itineraries and strict expansion force eventual periodic *points*. The exact periodic census is therefore complete. Hole monotonicity and the fact that the boundary cycle meets both endpoints prove sharpness. The zeta factors and zero-entropy consequence are derived from the complete census, not from enumeration.

Independent diagnostics in `verify_period_window.py` check the exact transition table, the recurrent components, all displayed cycle points, and fixed-point counts through order \(16\) at four exact parameters. These finite checks are evidence, not a proof of unbounded quantifiers. There is no extrapolation from the checker to the theorem.

## Originality (O): PASS within reviewed evidence

Ding–Steiner–Sun (arXiv:2610.03327v1) supply broad survivor/kneading theory and entropy/dimension plateaux, but their inspected Section 4 does not provide the sharp \(7/17\) cutoff, the unique eight-cycle, or the all-order zeta census on the symmetric slice. The closest published published-finding corpus statement covers symmetric holes only through \(2/5\), and its left-endpoint periodic census is incorporated as previously known. Glendinning–Hege (arXiv:2508.21429v1) covers general chaos-boundary mechanisms but not this exact negative-doubling window. Olivares-Vinales (arXiv:2405.10560v2) treats general interval-map zeta theory rather than this specific survivor. General Markov and kneading methods are acknowledged; the novelty assessment concerns a sharp motivated finite classification not printed in the inspected sources. Priority remains provisional because an unlocated specialized calculation may exist.

## Mathematical value (V): PASS

The full next parameter phase after the known four-cycle threshold has a natural sharp rational endpoint, rather than an arbitrary sample or minor numerical improvement. The proof establishes that the system remains globally eventually periodic and zero entropy until a *new* primitive eight-cycle enters exactly at that endpoint, and it supplies the complete zeta change for all iterates. This distinguishes periodic-orbit bifurcations from entropy changes in a natural one-parameter family; the exact cutoff informs finite-resolution open-system dynamics without claiming larger generalizations.

## Limitations

The theorem covers only \(2/5\le a\le7/17\) and only the specified symmetric open-hole interval dynamics. It does not classify larger holes, asymmetric holes, nonlinear maps, transient preimage multiplicities, or behavior immediately to the right of \(7/17\). Independent scientific audit remains outstanding, and historical priority against every specialized paper has not been certified.

Self-review: passed. Independent audit: not yet performed.
