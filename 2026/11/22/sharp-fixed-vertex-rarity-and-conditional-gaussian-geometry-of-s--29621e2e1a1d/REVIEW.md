# Scientific review: binary-cube fixed vertices of Coxeter involutions

## Correctness — PASS

The theorem reduces to a uniquely specified finite signed-orbit count, followed by a uniform positive-parameter saddle-point estimate for \([z^n]e^{tz+z^2}\). Each involutive signed permutation has \(k\) two-cycles and \(n-2k\) singleton cycles. Cube-vertex fixation forces each singleton sign to be positive, giving the exact distribution and showing that all vertex-fixing involutions lie in the even-signed group. The saddle integral has one principal peak and an exponentially suppressed parity peak when \(t>0\), giving the sharp constant \(e^{3/8}\); the conditional moment-generating function gives the Gaussian dimension law. The standalone checker enumerated the actual action through dimension six and checked the constant numerically through dimension one thousand. Finite checks are not substitutes for the asymptotic proof. Risk: standard uniform Fourier remainder estimates must be preserved if the theorem is restated for other models.

## Originality — PASS, subject to historical-priority uncertainty

Chen's 1992/1993 work already proves the balanced-signed-cycle fixed-vertex criterion in greater generality; the present exact spectrum is explicitly credited as a consequence and is NOT the claimed novelty. Gutierres–Mamede–Santos (2024) provide the underlying involution counting recurrences; Arumugam–Dietrich–Glasby (2022) give unrestricted wreath-product derangement distributions rather than the fixed-vertex conditional distribution of involutions. The assessed claim is the sharp stretched-exponential **conditional** fixed-vertex probability (including type-\(D\)'s factor two) together with the conditional Gaussian dimension law. Semantically targeted database comparisons returned no direct instance of either conditional asymptotic. This does not establish absolute priority; another source may have combined these standard ingredients already.

## Mathematical value — PASS

A signed-permutation involution acts on an exponentially large vertex set, yet almost all such involutions have no fixed vertex. The precise rarity scale and its sharp constant quantify a natural restricted derangement problem not answered by the unrestricted wreath-product density theorem. The type-\(B\)/type-\(D\) contrast shows that a parity restriction doubles rare-event probability even though the two groups have the same number of fixed-vertex involutions. The Gaussian law characterizes the dimension of the exceptional affine fixed-point sets. The exact spectrum is a necessary bridge, not claimed as a new standalone result.

## Closest literature and limits

- W. Y. C. Chen, *Induced Cycle Structures of the Hyperoctahedral Group* (1992 proceedings text), Proposition 3.5; direct source for the general fixed-point criterion.
- V. Arumugam, H. Dietrich, S. P. Glasby, *Derangements in wreath products of permutation groups*, arXiv:2207.01215 (2022); unrestricted product-action fixed-point distributions.
- G. Gutierres, R. Mamede, J. L. Santos, *Hamilton cycles for involutions of classical types*, arXiv:2401.12839 (2024); signed involution counts and Gray codes.

Risks include equivalent conditional asymptotics in an unindexed source, and dependency on the precise standard binary-cube action. No independent mathematical audit has taken place.

Self-review: passed. Independent audit: not yet performed.
