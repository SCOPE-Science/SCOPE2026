# Scientific review: sharp path-TV-ball projection sensitivity

## Correctness — PASS

The theorem quantifies all real inputs and every fixed radius \(R>0\), with \(n\ge2\). Polyhedral nearest-point projection has finitely many affine selections. For each nontrivial face, partition the vertices by zero-difference edges. The corresponding tangent projector is \(H=A-gg^{\mathsf T}/\|g\|_2^2\), with block averaging \(A\), signed active-edge vector \(s\) and \(g=AD^{\mathsf T}s\). The blockwise sign calculation proves \(V_n(g)=\|g\|_2^2\), and hence \(V_n(Hh)\le2V_n(h)\). Direct two-edge face calculations give \(1\) for \(n=2,3\). Distinct finite, monotone inputs give exact ratio \(2\) for every \(n\ge4\), with scaling preserving it at all positive radii. The embedded checker independently verifies all face matrices at 2–8 sites and explicit sharp witnesses at 4–39 sites using rational arithmetic. Finite tests are supportive, not a substitute for the unrestricted proof.

## Originality — PASS, with priority qualification

The 2004 Combettes–Pesquet author manuscript provides the natural constrained-TV restoration motivation and discusses computing the constrained solution by convex-analytic techniques; it does not state the sharp *two-input variation seminorm* of the Euclidean TV-ball projector or the four-site transition in the inspected portions. Yang–Barber characterize contraction for isotonic regression, which has a monotone-cone constraint rather than a variation budget. The accessible 2006 Darbon–Sigelle abstract concerns TV minimization under fidelity constraints, with different primal objective and constraint. Search and implication comparisons against relevant published mathematical records, including sharp stability of weighted \(\ell_1\)-ball projections and of Euclidean simplex projections, found no theorem covering this precise path-TV-ball result. Residual historical coverage is possible; unindexed or inaccessible older papers were not ruled out.

## Mathematical value — PASS

The exact \(1\)-to-\(2\) transition is a natural finite-size stability boundary for a widely used constrained denoising model: the Hilbert nearest-point inequality does not answer stability in the signal's own adjacent-variation seminorm. The face-gradient sign identity is a reusable structural proof ingredient, not a numerical coincidence. The uniform sharp constant and explicit extremal perturbations make the result useful for stability benchmarking.

## Limitations

No claims are made for periodic signals, arbitrary graphs, weighted vertex/edge measures, non-Euclidean fidelity, penalty-based (rather than radius-constrained) TV denoising, or varying radius between inputs. The literature search is not exhaustive; independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
