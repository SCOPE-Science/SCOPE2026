# Scientific review: short excursions in a tied-down simple walk

## Correctness — PASS

The finite law follows from a fully specified Catalan primitive-excursion generating function, exact Lagrange coefficient extraction, and equality of all factorial moments to those of the stated hypergeometric law. The \(k=n\) and \(n=1\) boundaries are expressly separated. The Rayleigh density follows from the explicit marginal return-count mass and a Gaussian product tail; the second-order mixture follows by a hypergeometric finite-population CLT applied at \(k\sim x\sqrt n\), and the correlation correction follows from conditional-variance decomposition and moment bounds. Exact enumeration of all fair bridges through \(n=9\) and larger coefficient checks are finite corroborations, not the proof. Residual risk: standard finite-population CLT and the uniform tail/moment argument must be interpreted with the compact-parameter restrictions given in the proof.

## Originality — PASS, qualified

The literature search covered ordered excursion lengths, macroscopic ranked-excursion functionals, Dyck returns and hills, discrete local-time conditioning, and exact hypergeometric aliases. Targeted mathematical-record searches found no matching mathematical claim. There is **substantial** preexisting coverage of the underlying product-Catalan excursion-length law (Serlet 2014, equation (6)), and of macroscopic excursion-count generating functions (Lindell–Holst 2007, Proposition 3.1). Therefore neither the elementary decomposition nor the full ordered-length joint probability is claimed as new. The assessed additional statement is the explicit hypergeometric reduction together with its nontrivial two-scale Rayleigh–Gaussian limit and asymptotic correlation rate. The general formulas could permit an implicit derivation of the finite reduction, which remains a historical-priority risk; no inspected theorem states this combined microscopic limit.

## Value — PASS

A short excursion is a natural microscopic return event; the total number of returns is the discrete local-time statistic. Their dependence is quantified exactly in finite samples by a classical named probability law rather than a difficult coefficient sum. At macroscopic time, the return count has \(\sqrt n\)-fluctuations, while conditional short-excursion noise lives on the distinct \(n^{1/4}\) scale with a non-Gaussian normal variance mixture. The exact correlation approach rate specifies a measurable finite-size limit. These identify a structural multiscale dependence not supplied by marginal count results alone.

## Closest prior work and limitations

- Csáki–Hu (2003): ranked lengths and heights; no observed conditional length-two-count law.
- Lindell–Holst (2007), Proposition 3.1: general count generating function in fixed macroscopic intervals, not the microscopic \(2\)-step scale.
- Serlet (2014), formula (6): exact product-Catalan joint ordered lengths, a real stronger finite distribution antecedent, but paper analyzes \(k=o(\sqrt n)\), not the typical \(k\asymp\sqrt n\) noise scale.
- Cameron–McLeod (2016): separate Dyck hill and return enumeration, not the stated conditioned bridge law.

Risk: a previously unlocated specialization or unpublished notes may have the explicit hypergeometric law or two-scale limit. No claim of independent verification or publication is made.

Self-review: passed. Independent audit: not yet performed.
