# Review of the exact signed two-Cauchy protected-gap frame bound

## Correctness — PASS

The theorem fixes all parameters and uses the convention in `RESULT.md`. The standard critical-density Zak isometry gives precisely the factor \(\alpha\) in the optimal lower frame bound. The Fourier transform of an upper-half-plane Cauchy pole is supported on the negative half-line; summing its negative-frequency geometric series gives the stated rational Zak multiplier. For a negative real residue ratio the numerator has real coefficients and is affine in the unit-circle variable. This makes zero detection exact at the two points \(z=\pm1\), and the intervals \(I_-\) and \(I_+\) follow without a numerical zero hunt.

The main nonstandard lemma is the **global angular minimization**: if \(F(y)=N(y)/D(y)\) has affine \(N\), positive quadratic \(D\) with strictly positive quadratic coefficient, then choosing the smaller endpoint quotient makes \(N-mD\) concave and nonnegative at both endpoints, hence nonnegative everywhere. This proves the angular minimum is an endpoint. Frequency minimization then has one strictly increasing branch and a unimodal branch with no interior minima. The third endpoint is explicitly dominated. The resulting exact formula, equality at one-sided Zak endpoints, and the unique max-min ratio are therefore proved for all stated parameters. The script was run successfully from its own actual path and checked sampled fibers and algebra; its finite checks are corroboration only.

## Originality — PASS, with specified residual priority risk

The key source is Belov–Kulikov–Lyubarskii's rational-window paper, first publicly posted 16 March 2021. Its accessible full text includes a general frame criterion, the Herglotz positive-residue theorem, and in Section 1.7.2 an explicit announcement that qualitative two-kernel **frame sets** can be completely described, with detailed proofs to appear elsewhere. This prevents treating the zero-locus classification alone as new. The reviewed claim instead requires the precise **sharp lower frame constant** throughout the signed protected component and its exact maximizing residue; neither that quantitative identity nor its angular concavity proof is stated in the inspected material. The single-Cauchy frame-operator source concerns one pole, and the inspected other search hits do not imply the signed two-pole optimal constant. The specific risk is an unlocated later detailed two-kernel treatment or stronger Zak bound theorem that contains the quantitative result. Search absence is not a proof of priority.

## Value — PASS

Critical-density frame existence alone does not quantify reconstruction stability. Here a sign-changing two-pole window can lose its frame property on two separate residue ranges and regain it between them. The theorem gives **the exact optimal lower frame bound at every ratio in that recovering component**, with two different boundary coefficients and a unique maximizing pole mixture. This is a motivated first signed case outside the positive-residue Herglotz theorem and a parameter-design result, not a fixed-parameter numerical curiosity. It does not claim broad Gabor-frame optimization outside its precisely specified family.

## Closest literature and limitations

Primary: Belov, Kulikov, Lyubarskii, *Gabor frames for rational functions*, arXiv:2103.08959, §§1.4, 1.7.2, 2; and *Gabor frame operator for the Cauchy kernel*, arXiv:2212.08915 (one-pole abstract and scope). Standard Zak criterion: Gröchenig, *Foundations of Time-Frequency Analysis*. The result is restricted to critical rectangular lattices, fixed distinct positive pole heights, and real relative negative residues; it supplies no new upper frame-bound or general lattice theorem. An independent check of scientific priority and proof has not occurred.

Self-review: passed. Independent audit: not yet performed.
