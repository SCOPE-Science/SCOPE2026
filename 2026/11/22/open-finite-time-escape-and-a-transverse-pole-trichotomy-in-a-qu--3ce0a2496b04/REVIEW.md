# Self-review

## Correctness — PASS

The axial line is exactly invariant. Along it, reciprocal height satisfies the analytic Riccati initial-value equation \(w_s=c-bw+aw^2\), forcing a simple pole of positive height. The transverse variational equation is a genuine regular-singular scalar equation; its bounded solution, reduction-of-order independent mode, and leading coefficients have been derived explicitly. The nonlinear tube argument uses simultaneous strict height-growth, lateral-boundary and cumulative-drift inequalities, uniform for all sufficiently large heights. The asymptotic limit of \(yz^{-1/c}\) follows from an integrable coefficient and forcing after reparameterization by monotone height; the formula for \(x_\infty-x\) then follows by integration. All assumptions and quantifiers are stated. Symbolic identities and numerical diagnostics were replayed from the standalone source file; computation is not the proof of the infinite assertions.

The source parameters \((a,b,c)=(0.1,0.195,0.1)\) have negative scalar discriminant \(-0.001975\), establishing all-height axial escape independently of plotted bounded trajectories. Explicit tube parameters \((a,b,c,p,\kappa,X,Y,Z)=(1,0,2,3/4,3/2,1,1,10^4)\) satisfy every uniform strict inequality. The proof does not turn transverse linearization into a nonlinear conclusion outside its stated range.

## Originality — PASS within the inspected evidence

The closest primary source is Zhang et al., DOI 10.3934/mmc.2023032: its complete accessible sixteen-page paper describes this exact vector field, equilibria, Hopf bifurcations, numerical chaotic trajectories and electronic simulation, not finite-time blow-up, sharp axial transverse pole exponents or open escape tubes. The later Fan et al. family, DOI 10.1142/S0218127424501499, was compared using its author-uploaded full-text sections: it instead starts with \(\dot x=z\), \(\dot y=x-yz\), and has distinct quadratic terms, so it does not imply the theorem through a literal model specialization. Standard Riccati, Frobenius and invariant-tube techniques are established prior mathematical tools, not claimed innovations. The novel assertion concerns this precise parameterized flow and a linked finite-time pole/tube classification. Broader or unindexed equivalent mathematical statements are an explicit remaining priority risk; unsuccessful indexing alone is not proof of novelty.

## Value — PASS

A system studied primarily through hidden chaotic attractors and finite numerical integrations can also admit exact finite-time escaping solutions. The result makes this distinction mathematically sharp at the published no-equilibrium coefficients, identifies a codimension-two axial escape trajectory with three distinct transverse singular-response regimes, and proves that for positive quadratic strength above a natural threshold the escaping behavior occupies a full-dimensional open set. The nonzero asymptotic coefficient on an open subregion is a quantitative description beyond merely asserting unboundedness. These are significant dynamical-domain and model-interpretation questions, not arbitrary parameter or rounding examples.

## Closest literature and limitations

X. Zhang et al., *Mathematical Modelling and Control* 3 (2023), 400–415, DOI 10.3934/mmc.2023032; L. Fan et al., *International Journal of Bifurcation and Chaos* 34 (2024), 2450149, DOI 10.1142/S0218127424501499. Only axial and high-height open-set solutions are classified, not all global dynamics. The linearized critical pole is not a claim of nonlinear stability; unindexed mathematical literature and generic structural theorems remain a priority risk. A secondary article host reports 15 December 2023 whereas the journal publisher reports 27 December 2023; both dates satisfy the stated scientific date range.

Self-review: passed. Independent audit: not yet performed.
