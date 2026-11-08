# Self-review

**Correctness — PASS.** The interval sumset identity gives an exact integer cover of each layer, and saturation at \(k=q+\lceil(q-1)/t\rceil\) follows from intervals of offsets that overlap on the integer lattice. Below the cutoff, the inequality \(K<2q\) restricts the scaled positive part to one generator and gives the precise deleted intervals. The construction at the penultimate layer proves uniform sharpness. An independent finite dynamic-programming checker verified \(4650\) parameter cases, \(900\) small-field formulas, and \(250\) cutoff witnesses. The general assertion rests on the symbolic proof, not on finite checking.

**Originality — PASS, with priority qualifications.** The closest paper, Marques–Mendoza–Quoos–Tizziotti (arXiv:2508.17022), already provides an exact general Apéry-set formula for the *cardinality* of the footprint. The new result therefore does not claim the first general numerical evaluation, and binary/ternary numerical formulas alone do not establish novelty. The contribution is the full surviving set, a uniform cutoff across all widths, and proof that its layer coefficient is best possible, which are not asserted in the relevant primary text. Targeted literature and mathematical-record searches did not locate an equivalent result; unindexed priority remains a risk.

**Mathematical value — PASS.** The sharp cutoff identifies exactly how many semigroup sumset layers can contain uncovered elements, independently of the multiplicity and without an Apéry minimization. It is a natural structural refinement of the newly studied small-width Geil–Matsumoto problem, and the full interval decomposition yields concrete arithmetic calculations in the binary and ternary cases. It is not offered as a broad general theorem about arbitrary numerical semigroups or as a new bound for all curves.

Scientific limitation: previous work implies computability of all numerical values; the added information is set-level support and sharp uniform saturation. Research priority beyond the inspected literature is not independently certified.

Self-review: passed. Independent audit: not yet performed.
