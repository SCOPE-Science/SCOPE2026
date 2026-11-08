# Review of the balanced Johnson-graph tuple-orbit theorem

## Correctness — PASS

The argument relies on the **published** group equality \(\operatorname{Aut}(J(2k,k))\cong S_{2k}\times C_2\), whose exact action is given by coordinate relabelling and complementation. Every higher-arity orbit is classified by its full Venn-cell count vector; complement reverses bit patterns. The fixed-point count is a stars-and-bars calculation, the full-group orbit count is an application of Burnside's lemma, and equality-pattern Möbius inversion converts all tuples to distinct tuples. The triple-intersection fiber and its reflection follow from eight explicitly enumerated nonnegative cell counts. A separate four-block stabilizer count and finite cubic sums verify the closed parity formulas. Relative-interior and full-rank arguments justify the Ehrhart exponent for fixed arity. `checker.py` independently reproduces the stated small exhaustive counts, the formulas through \(k=25\), and all automorphisms of the smallest graph. No finite run is offered in place of a general proof.

## Originality — PASS within inspected evidence

The October 2026 source concerns model-theoretic limit properties, not finite complete tuple-orbit profiles; Ganesan and Jones determine the underlying automorphism group and ordinary pair orbitals, not the evaluated ternary fiber or higher-arity complement-fixed census. The closest identified mathematical-record findings instead concern tuple-orbit profiles of unrelated homogeneous structures or Johnson-slice harmonic analyses. The accepted claim is specifically the complete evaluated profile, sharp ternary symmetry defect and asymptotic complement-pairing rate, **not** the earlier automorphism theorem or general Burnside, Stirling and Ehrhart identities. This comparison is not a proof of historical uniqueness: older association-scheme literature might subsume part of the enumeration, and the full Jones article could not be inspected.

## Mathematical value — PASS

The pairwise association scheme sees precisely the same vertex-pair types with or without the extra complement symmetry, while the first informative ternary level admits a fully explicit fiber classification and polynomial enumeration. This sharp arity boundary is a natural finite-model-theoretic symmetry question raised by work on finite Johnson-graph limits. The all-arity formula and vanishing fraction of complement-fixed orbit types identify how pervasive the additional symmetry is among finite tuple types, beyond the textbook group-order computation. Every balanced size and every fixed arity is covered; the result is not an arbitrary finite instance or a renamed general theorem.

## Closest literature and limitations

See Benediktsson–Macpherson–Adler, arXiv:2610.40054v1, and Ganesan, arXiv:1412.5055v1, with Jones, DOI:10.1016/j.ejc.2004.01.012, for prior groups and pair orbitals. The latter publication was available only in public excerpts. Earlier higher-order Johnson-scheme enumerations remain a residual priority risk. The asymptotic ratio weights orbit types uniformly and does not describe the frequency of randomly selected labelled tuples.

Self-review: passed. Independent audit: not yet performed.
