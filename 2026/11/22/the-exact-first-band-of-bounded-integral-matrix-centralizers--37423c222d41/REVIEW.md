# Independent mathematical audit

## correctness

PASS

A nonscalar A has a rational commutant spanned by I,A (choose a vector cyclic for A). Its integral commutant is parametrized by one free diagonal entry and an integer multiple j of the primitive triple (b,c,a−d)/g by Bézout. The box permits |j|≤S=⌊2gH/M⌋ with M=max(2|b|,2|c|,|a−d|); for each j the diagonal overlap is 2H+1−(p/g)|j| with p=|a−d|. Summing gives (2H+1)(2S+1)−(p/g)S(S+1). Because S≥g≥1 and p/g≤2H/S, this is at least 2HS+2S+1. Thus C_H≤4H forces S=g=1, while p≥L_H(z)≥H+2 with g=1 conversely forces S=1 and enforces the threshold 6H+3−2p≤zH. Scalars are excluded by their full box count. The multiplicity of p is 2(2H+1−p) and the coprime (b,c) count is Möbius inversion, giving the exact sum including empty bands. Taking p=2H,b=1,c=0 attains the lower bound 2H+3. The unrestricted diagonal-pair count T is (z−2)^2H²/4+O(H), uniformly including the empty region. For multiples of r, count diagonal pairs by the same linear weight on a progression: weighted summation by parts gives T_r=T/r+O(H) from prefix discrepancy at most one. The off-diagonal count of one coordinate is (2H+1)/r+O(1), so the error in the Möbius sum is bounded by ∑_{r≤2H}O(H³/r²+H²/r+H)=O(H³). Extending the main series produces 1/ζ(3); division by (2H+1)^4 gives the uniform stated law and the z=4 density. The independently written bounded replay agreed with direct AB=BA at all 3,107 A at H=1,2,3, and with the finite event formula in all 35 tested half-step thresholds over H=1,…,7 (evidence note /workspace/branches/4762f248-a59e-4f6c-95bd-6fdf1b17ee01/bounded-centralizer-check.md). The supplied checker and VERIFICATION.md were inspected, not executed. The uniform error follows from the proof, not from the replay; no Lean or external expert attestation is claimed.

## originality

PASS

The fixed-matrix formula is already known and determines what a brute-force distribution would be. The claimed contribution is a structural first-band predicate, exact distribution summed across the growing entry box, and uniform lower-edge CDF, not the parametrization or the commuting-pair total. No equivalent evaluated tail law was found in the inspected comparisons.

## value

PASS

For commuting-pair statistics in the standard symmetric entry box, a lower-tail CDF is a natural complement to the known mean. The range is a structural band, cut out by the gap between S=1 and S≥2, not arbitrary sample heights. The exact primitive-region characterization and uniform quadratic edge law describe where small centralizers occur and give their mass; the pointwise formula and example attaining the minimum alone would not justify the value verdict.

The dated certificate retains the supplied scientific assessment, sources and limitations.
