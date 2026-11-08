# Review of the exact least genus quasiperiod theorem

## Correctness — PASS
The gap-interval characterization follows by comparing the number of generators in a representation with the quotient \(\lfloor N/a\rfloor\). Exact counting of multiples in each gap interval gives the floor sum. Its decomposition into complete blocks of length \(p\) and a final tail yields an exact quadratic branch formula, not an asymptotic approximation. The gcd expression for its linear coefficient follows from the standard, explicitly stated finite floor-sum identity. Minimality follows from the locations of the two largest values of the gcd statistic, and from strictly unequal constant terms on suitable pairs of branches. The exceptional moduli \(p=2\) and \(p=4\) are treated separately. Exact separately implemented dynamic-programming checks passed on 3,375 pairs of parameters; these do not replace the symbolic proof.

## Originality — PASS, qualified
Adeniran et al. (arXiv:1809.09360), Theorem 1.3, give a generic root-of-unity formula for the quotient genus; Section 3 analyzes the three-generator arithmetic progression in cases where the modulus divides the first generator. It does not state the unrestricted sharp least period or gcd-dependent linear coefficient. Liu (arXiv:2607.23076), Theorem 1.4, studies the *Frobenius number*, not genus, of a *two*-generator quotient and shows a period dividing the quotient modulus. Liu (arXiv:2604.26415) considers a different quotient family with divisibility assumptions. The exact doubled period and its arithmetic obstruction are neither statements nor immediate specializations of these results. Related searchable research claims about two-generator quotients were also distinguished. A hidden equivalent computation or derivation from the general root-of-unity identity remains a historical-priority risk.

## Mathematical value — PASS
The result gives a sharp, uniform least-period classification, including the exceptional factor-two collapse, for a natural first embedding-dimension-three family. It goes beyond numerical evaluation by exposing the gcd-controlled linear coefficient and showing precisely why the full period cannot be compressed. It answers a natural structural question left open by period-divisibility bounds for consecutive two-generator quotients and earlier genus identities. The method is specifically for a three-term interval and does not classify arbitrary arithmetic progressions.

## Limitations
The full result is established by elementary exact arithmetic, with no external proof assistant and no independent verification. The source comparison uses the relevant open primary texts and indexed records, but cannot prove global historical priority.

Self-review: passed. Independent audit: not yet performed.
