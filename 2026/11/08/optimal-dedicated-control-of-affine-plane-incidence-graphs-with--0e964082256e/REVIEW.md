# Scientific review

## Correctness — PASS

The incidence identity \(MM^{\mathsf T}=qI+J\) holds by the affine-plane axioms, so \(M\) has full row rank and the complete Laplacian spectrum has eigenspace multiplicities \(1,q^2-1,q,q^2-1,1\). The dimension lower bound and line-only kernel lower bound follow from PBH. For the explicit placement, the selected line measurements enforce \(x_Q=-x_P\) for all points \(Q\) on the omitted line; the sum-zero constraint then forces \(x_P=0\) for \(q\ge2\). Parallel-class kernel sampling and the two constant eigenspaces complete PBH. Each selected line has two white point neighbors and each selected point at least two white line neighbors, proving the stalled property. The embedded standard-library checker passes exact incidence, rank, and zero-forcing tests for \(q\in\{2,3,5,7,11\}\). Finite samples are consistency checks, not the proof of universal quantification.

## Originality — PASS on inspected evidence, with residual risk

Burgarth et al. (2011), Theorem 4.1 and its converse discussion, provide only a sufficient zero-forcing criterion; they even demonstrate a small non-zero-forcing controllable set, but not this affine-plane family or an exact optimal count. Yuan et al. (2013) show that the maximum eigenvalue multiplicity gives the minimum number of freely placed independent inputs and offer a general driver-selection method. Thus the scalar \(q^2-1\) is *not* claimed to be unrelated to their theory: the specific value follows once the affine-plane spectrum is supplied. The new assertion is the **simultaneously optimal, explicit dedicated coordinate placement using only \(q\) line inputs, with a stalled zero-forcing process**, over all affine planes regardless of coordinatization. Monshizadeh et al. (2014) study robust structural controllability for matrix families, not the fixed incidence Laplacian. A historical projective-plane incidence control result pertains to the graph of a projective rather than affine plane, and is neither an implication of nor a substitute for this deleted-line geometry. Targeted full-text and searchable record comparisons did not locate a dominating affine-plane construction, but specialist and unindexed literature is a remaining priority risk.

## Value — PASS

The exact optimum and the sharp minimum number of line-side actuators are natural controllability invariants of resolvable incidence networks. The construction is uniform in the order and in the chosen plane and gives a direct geometric installation scheme, not a numerical search. The stalled zero-forcing property is mathematically significant because a common topology-only sufficient condition cannot certify even a PBH-optimal placement. No claim about zero-forcing number, numerical conditioning or energy is made.

## Scope and residual limitations

Only fixed, real, unweighted, undirected incidence Laplacians with independent standard-coordinate inputs are treated. The existence condition on affine planes and the distinction between general input-channel rank and dedicated coordinate placement are essential. The finite verification covers only prime-field examples; abstract incidence axioms supply the all-plane proof. The accessible 2014 Farrugia–Sciriha item was available in abstract form only and could not be excluded by a full-text comparison; its stated adjacency and signless-Laplacian focus is not obviously the present theorem. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
