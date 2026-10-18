# Independent mathematical audit

## correctness

PASS

For n>=1,b>=2, g=gcd(n,b-1), q=(b-1)/g, the digit congruence gives D subset g*N. The residues jn mod (b-1) for j=1..q cover every multiple-of-g residue because gcd(n/g,q)=1. Set T=max_{1<=j<=q} s_b(jn). For any t>=T divisible by g, choose j with s_b(jn)=u congruent t mod (b-1), and apply Clokie et al. Theorem 4 to attain t=u+r(b-1). Carry-free concatenation proves D union {0} additive; scaling gives a numerical semigroup with conductor at most ceil(T/g). Independent finite automaton computed all 1000 admissible targets across 200 (base,modulus) instances.

## originality

FAIL

The principal infinite tail is a direct corollary of Clokie–Lidbetter–Molina Lovett–Shallit–Witzman Theorem 4 plus the elementary fact that jn covers every gcd-compatible residue modulo b-1. No new nonstandard arithmetic lemma or genuinely narrower unresolved case is required. Concatenation is the standard zero-carry identity, and numerical-semigroup status is the definition once cofinite closure is established. Thus the original claim does not survive the strong prior-implication standard despite absence of identical words in the earlier paper.

## value

FAIL

The attainable spectrum is a natural object, but the asserted new result is an immediate arithmetic corollary of a published all-parameter progression theorem, with a nonoptimal threshold assembled from the first q obvious seeds. The semigroup observation is routine concatenation and supplies neither the exact conductor nor a new obstruction/classification beyond the prior implication. It is not a substantive independent advance under the same value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
