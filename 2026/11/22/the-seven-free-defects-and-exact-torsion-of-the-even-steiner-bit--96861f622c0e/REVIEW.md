# Review of the even-Steiner bitangent incidence lattice

## Correctness — PASS

For an even-theta-marked smooth plane quartic in characteristic different from two, the classical octad model identifies bitangents with the \(28\) two-subsets of eight points and the selected parity-even Steiner complexes with the \(35\) unordered four-four partitions. The standard theta test makes their incidence matrix exactly \(M_{S,e}=1\) when the edge \(e\) lies entirely in one part. The Gram identity \(M^{\mathsf T}M=8I-2A+7J\) is proved by direct combinatorial counts; its eigenvalues \(180,0^{\times7},12^{\times20}\) show rational rank \(21\) and establish the equal-degree saturation. The submitted \(474\)-operation integer certificate replays to Smith form \(1^{\times7},2^{\times13},6,0^{\times7}\); independent integer Smith calculation agreed. Thus correctness covers both the exact torsion and its geometric interpretation. Limit: no claim about actual Picard groups or Galois-module refinements.

## Originality — PASS, subject to residual historical risk

Plaumann–Sturmfels–Vinzant (arXiv:1008.4104, Sections 5–6) already give the \(28+35\) octad labels and twelve-bitangent memberships; Bergvall (arXiv:2106.13072, Sections 2.2–2.5) gives the theta and Steiner interpretations. The previous complete **63-complex** integral incidence result concerns a different \(28\times63\) matrix of full rational rank; its published RESULT.md was checked and contains no integral determination of the naturally restricted \(35\)-complex submatrix. The present result has a new free defect, a new exact equal-degree saturation and a distinct torsion group. Searches for the parity-even restriction, its rank, Smith factors and balanced-partition matrix did not locate a prior identical result. A historically obscure graph-design table could nevertheless predate the calculation; no complete priority guarantee is asserted.

## Mathematical value — PASS

Choosing an even theta characteristic is a geometrically canonical marking, and exactly \(35\) Steiner complexes are even with respect to that marking. The integral reconstruction question asks which combinations of the \(28\) associated bitangents can be assembled from **only these canonical complexes**. The theorem answers completely: the rationally reachable combinations are precisely those with equal octad vertex degrees, but integral assembly faces \(13\) independent order-two factors and an additional order-six factor (including genuine three-torsion). The latter has the direct witness that every Steiner-support vector has equal vertex degree divisible by three, whereas a perfect matching has equal vertex degree one. The full obstruction has sharp universal exponent six. These are natural and nontrivial obstructions that neither the original \(63\)-complex full Smith form nor rational permutation characters determine. Their precise values matter to integral incidence presentations and arithmetic invariant-lattice calculations; no unsupported downstream theorem is claimed.

## References and limits

Primary inspected full texts: Plaumann–Sturmfels–Vinzant, https://arxiv.org/abs/1008.4104; Bergvall, https://arxiv.org/abs/2106.13072; the previously published full-63 integral lattice theorem, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-integral-steiner-reconstruction-lattice-of-plane-quartic-bitange--b76c5509eb43. Exact calculation is reproducible with `verify.py` and `certificate.json`. An independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
