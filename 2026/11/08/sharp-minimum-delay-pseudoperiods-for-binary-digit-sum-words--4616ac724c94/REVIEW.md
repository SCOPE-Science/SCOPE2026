# Self-review

## Correctness — PASS

The horizon lower bound is forced at the zero starting position: the only admissible positive shift up to \(2^m-1\) is the all-ones \(m\)-bit integer. The proposed family of \(2m-1\) shifts passes the infinite return test by an exhaustive binary-carry dichotomy. When no power-of-two shift works, the low bits must have form \(0^a1^{m-a}\), the high trailing-one run has residue \(r\in\{1,\ldots,a\}\), and the complement shift indexed by \(a-r\) has weight change divisible by \(m\). The exact admissible-offset sets at the \(m+1\) compulsory witnesses and the \(m-2\) Hamming-layer witnesses are pairwise disjoint; this gives a matching lower bound without using finite enumeration. The packaged stdlib verifier reports `VERIFY_OK moduli=9 assertions=79047`. Its finite scope is supplemental.

## Originality — PASS, qualified

Meleshko–Ochem–Shallit–Shan (arXiv:2207.10171, 2022) introduce pseudoperiods and treat the classical two-letter Thue–Morse case; this does not provide the arbitrary-modulus support optimum. Zhao–Zhang (Journal of Integer Sequences 20 (2017), Article 17.3.3) establish a sharp consecutive-window alphabet-coverage theorem, yielding a dense-window benchmark, not a uniform sparse shift set with optimality proof. Searches for modular digit-sum pseudoperiods, equivalent fixed self-return offset formulations, and tabulated covering supports identified no covering implication. Remaining risk is an unindexed or differently expressed prior result, or a non-obvious equivalent corollary; originality is not independently certified.

## Mathematical value — PASS

The finding is a complete infinite-family tradeoff theorem for a natural invariant linked to two published directions. It proves that the least possible maximum shift is exponential while the least support size at that horizon is exactly linear, and identifies mandatory shifts and Hamming-weight classes. These are structural bounds rather than a small numerical gain or an arbitrary finite computation.

## Limits and primary evidence

The theorem **does not** prove that \(2m-1\) is the minimum support when arbitrarily large maximum shifts are permitted, nor does it classify all possible optimal shift sets. The verifier covers only moduli \(2\) through \(10\), while the general proof covers every integer \(m\ge2\). Primary sources checked: [Zhao–Zhang, 2017](https://cs.uwaterloo.ca/journals/JIS/VOL20/Zhao/zhao23.pdf), especially Theorems 4–5 and Corollary 12; [Meleshko–Ochem–Shallit–Shan, 2022](https://arxiv.org/html/2207.10171v3), especially Definition 1, Proposition 2, and Sections 3–4. The scientific comparisons and search scopes appear in `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
