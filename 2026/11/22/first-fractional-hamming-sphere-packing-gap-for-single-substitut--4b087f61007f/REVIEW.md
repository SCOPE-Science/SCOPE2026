# Scientific review

## Correctness — PASS

The received alphabet is all binary words of length \(2n\), including those violating the Dyck constraint. The pairwise distance criterion is proved using the radius-one-ball intersection rule and constant Hamming weight of Dyck words. Integer witnesses and rational primal/dual assignments are complete for semilengths one through six. Exact arithmetic checks all packing and covering constraints; the independently reproducible exhaustive compatibility-graph maximum-clique search checks the full 132-source instance at semilength six. A separate integer-programming implementation agrees. Non-exhaustive numerical solver output is not being substituted for the exhaustive argument.

## Originality — PASS (qualified)

The most relevant inspected antecedent is Ardila's *The Catalan matroid* (https://arxiv.org/abs/math/0209354): it supplies the basis interpretation but does not state the radius-one Hamming packing optimum or code-size sequence. Cohen–Tetali–Yeliussizov address basis-exchange mixing (https://arxiv.org/abs/1505.06710), and Mütze–Standke–Wiechert address Gray-code adjacency (https://arxiv.org/abs/1603.02525). Yazdi–Kiah–Milenkovic construct balanced weakly mutually uncorrelated codes using Dyck paths (https://arxiv.org/abs/1601.08176), but the inspected construction does not give the exact optimum and fractional gap for the full Dyck alphabet. Related deletion and constrained-code statements use different channels and do not logically imply this finite classification. Standard unrestricted constant-weight bounds also do not imply the Dyck-specific maximum: the published table at length 12, weight 6 and minimum distance 4 lists at least 132 unrestricted codewords, rather than the constrained optimum 22. Searches of pertinent terminology and prior research records found no matching claim; unindexed or inaccessible earlier computations remain a real priority risk.

## Mathematical value — PASS

The object is a classical Catalan matroid's full basis family, and one-bit substitution is a canonical error model. The first failure of the natural fractional sphere-packing relaxation is a motivated boundary, not an arbitrary coordinate slice. The exact integral and fractional values, together with full reproducible primal/dual and exhaustive combinatorial certificates, provide a meaningful test instance for coding on constrained matroid bases. This is a finite boundary result and does not claim general higher-dimensional capacity.

## Remaining limits

No semilength greater than six, asymptotic rate, optimizer census, or stream synchronization property is established. External priority is qualified by the completeness of available historical searches. Independent mathematical validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
