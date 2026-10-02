# Independent mathematical audit — Prime-power action images obstruct psi-divisibility in cyclic-by-cyclic groups

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **failed**.

## Correctness

**PASS** — The centralizer-difference identity is correct: the standard normal-cyclic-Sylow formula rewrites as \(\psi(G)=A\psi(C)+p^\alpha(\psi(H)-\psi(C))\), and \(A=\psi(C_{p^\alpha})\) is coprime to \(p\). For \(H=C_{q^\beta}\) with action image \(q^\gamma\), the kernel is \(C_{q^{\beta-\gamma}}\), the cyclic prime-power sum difference factors by \(q^{2(\beta-\gamma)+1}(q^{2\gamma}-1)/(q+1)\), and the action gives \(q^\gamma\mid p-1\), so the \(q\)-power factor is coprime to \(A\). The resulting exact gcd formula and strict nondivisibility inequality are algebraically valid. Independent compatible parameter checks reproduced the formula.

Checked sources: Assigned RESULT.md and inspected verifier source; Lazorec 2021 full preprint; Published 20 September 2026 cyclic-Sylow obstruction result; Independent spot computations.

Residual correctness risks: The finite computation is corroborative only; the proof is elementary algebra from the normal-cyclic-Sylow formula..

## Originality

**FAIL** — A published 20 September 2026 result already proves the strictly broader theorem that every semidirect product with a noncentral normal cyclic Sylow subgroup and coprime complement is not psi-divisible. Its proof displays the same decomposition \(\psi(G)=A\psi(C)+p^\alpha(\psi(H)-\psi(C))\). Because \(\gcd(A,p)=1\), taking a gcd with \(A\) immediately gives the audited centralizer-difference identity; specializing \(H\) and \(C\) to cyclic prime-power groups then gives the advertised exact gcd by one standard cyclic-sum subtraction. Thus both the nondivisibility conclusion and the quantitative core are mechanically implied by the earlier published result.

### Equivalent formulations

Searches/sources: Resultary query: psi-divisible cyclic Sylow obstruction Z-groups; Published 20 September 2026 result SCOPE-psi-divisibility-cyclic-sylow-obstruction-z-groups--80065f617da2; Lazorec 2021 ZM-group obstruction.

Evidence: The 20 September theorem applies to every nontrivial coprime action on a normal cyclic \(p\)-group, hence contains every group in the audited prime-power-complement theorem. Its proof already writes the same centralizer decomposition from which the audited gcd identity follows by taking gcd with \(A\).

The audited theorem is an equivalent/specialized quantitative repackaging of a broader result published the previous day.

### Broader coverage

Searches/sources: Complete 20 September 2026 cyclic-Sylow obstruction RESULT.md; Z-group classification corollaries in that record.

Evidence: The prior theorem assumes only a cyclic normal \(p\)-group and an arbitrary coprime complement with nontrivial action. The audited family \(C_{p^\alpha}\rtimes C_{q^\beta}\) and its cyclic-complement corollaries are strict special cases.

Broader published coverage is decisive.

### Exact database or table

Searches/sources: Resultary semantic search for psi-divisibility semidirect products and exact gcd; Published-record chronology 20 September versus 21 September.

Evidence: The search returned the 20 September broader obstruction immediately below the audited exact match. The broader record predates the audited record and contains the needed formula in its proof.

No exact-title distinction can overcome the prior mathematical implication.

### Claim versus prior implication

Searches/sources: Take gcd of the prior identity \(\psi(G)=A c+p^\alpha(h-c)\) with \(A\); Insert \(H=C_{q^\beta}\), \(C=C_{q^{\beta-\gamma}}\).

Evidence: Since \(\gcd(A,p)=1\), the prior displayed identity gives \(\gcd(A,\psi(G))=\gcd(A,h-c)\) immediately. The cyclic prime-power formula factors \(h-c\) into a \(q\)-power times \((q^{2\gamma}-1)/(q+1)\), and \(A\equiv1\pmod q\), yielding the audited formula.

The exact gcd formula requires no new nonstandard lemma beyond direct substitution into the prior proof.

### Source inspections

- **A cyclic-Sylow obstruction to psi-divisibility and the classification of Z-groups** — DECISIVE_COVERAGE.
  Identifier: https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-psi-divisibility-cyclic-sylow-obstruction-z-groups--80065f617da2
  Trigger: Near-identical objects and an earlier, apparently broader published theorem.
  Material read: Complete published RESULT.md, including the theorem, formula (1), proof, and Z-group corollaries.
  Method: public full text
  Evidence: It proves nondivisibility for every noncentral normal cyclic Sylow subgroup with coprime complement and displays the decomposition that mechanically yields the audited exact gcd identity.
- **On a divisibility property involving the sum of element orders** — OLDER_PARTIAL_PRIOR.
  Identifier: https://arxiv.org/abs/2003.01678
  Trigger: Primary pre-2026 ZM-group source cited by both records.
  Material read: Complete open preprint, including the normal-cyclic-Sylow formula and Proposition 2.4.
  Method: lawful open-access full text
  Evidence: It gives the established semidirect-product formula and an exponent-restricted ZM obstruction; the decisive failure comes from the later 20 September theorem.

Residual originality risks:
- None identified.

## Scientific value

**FAIL** — After the broader 20 September theorem is treated as prior, the surviving quantitative formula is a direct gcd-and-substitution calculation from an identity already printed in that prior proof. The prime-power complement and image/kernel corollaries therefore do not constitute a separately motivated mathematical gap under the stated value standard.

Residual value risks: None identified..

## Final assessment

The mathematics checked above is retained as evidence, but the final claim is scientifically rejected because originality and value do not survive the earlier broader published result. The complete original package is to be preserved in the designated failed-attempt location.

Earlier review evidence remains separately identified and is not relabeled as this independent assessment.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
