# Scientific review

## Correctness — PASS
The sextic smoothness, elliptic-square Jacobian decomposition, exact quadratic character sums, and Frobenius-fixed even-subset description prove the claim. The universal quadratic-factor dichotomy and inversion orbit count are written out, and `verify.py` independently checks every coefficient-marked case and both twists over the two primes. The equal-Weil/different-two-torsion pair is explicitly \(s=0,1\) with \(t=-2\) and respective rational two-torsion orders \(4,16\). No finite calculation is used to infer an unproved infinite statement.

## Originality — PASS, qualified
Arul et al., *Doubly isogenous genus-2 curves with \(D_4\)-action*, arXiv:2102.11419, give the same curve model, the elliptic-square decomposition, general isogeny-pair bounds and the aggregate statistic \(P(13)=6\). Those are not new. Cardona–Quer, arXiv:math/0203165, give the earlier general classification (using \(D_8\) for the order-eight dihedral group). The exact first-prime mixed-two-torsion event and complete marked mixed-Weil-class spectrum do not follow from the quoted aggregate statistic without the separate character sums and root splitting tests. a mathematical-record index comparisons include a different isomorphic-Jacobian family at field sizes congruent to three modulo four and a separate characteristic-three dihedral two-torsion classification. The full primary supplementary machine data remained inaccessible, so an unindexed earlier computation remains a substantive historical priority risk.

## Mathematical value — PASS
The case is a precise boundary for the failure of Weil-isogeny data to recover rational Jacobian two-torsion inside a natural one-dimensional moduli family. The two competing torsion structures coexist in exactly two trace bins, and the general parameter-count formula explains why such coexistence first becomes possible. This refines zeta-function comparisons by a moduli-geometric 2-division invariant, rather than just listing point counts.

## Scope and limitations
The stated minimum concerns primes congruent to one modulo four in the specified marked family; arbitrary prime powers, all genus-two curves, and stronger doubly-isogenous covers are outside the finding. Curves are distinguished over the base field by rational Jacobian two-torsion, not claimed geometrically nonisomorphic. Prior primary results and residual priority risks are disclosed in `RESULT.md` and `AUDIT.json`. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
