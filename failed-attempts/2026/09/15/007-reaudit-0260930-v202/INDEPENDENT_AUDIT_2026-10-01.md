# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260915-007`

## Correctness — PASS

The stated bound follows. For a PCF unicritical polynomial, \(c\) is an algebraic integer and every archimedean conjugate has modulus at most 2, hence \(h(c)\le\log 2\). The standard global height estimate gives \(|h(f(x))-d h(x)|\le h(c)+\log2\), so telescoping against the canonical height yields \(h(x)\le2\log2\) for preperiodic \(x\). If \(x\) has degree at most \(D\), its primitive minimal polynomial has Mahler measure at most \(4^D\), and the elementary coefficient bound gives absolute coefficients at most \(8^D\). Counting possible polynomials and their roots yields the claimed coarse \(D^2(2\cdot8^D+1)^{D+1}\) upper bound. The package script correctly reproduces the arithmetic examples.

Sources:
- Ferraguti–Pagano, Abelian dynamical Galois groups for unicritical polynomials, Lemma 4.1
- standard Weil/canonical height comparison
- artifacts/compute_B.py

Risks:
- The bound is intentionally very coarse and counts many algebraic numbers that are not preperiodic.

## Originality — FAIL

Ferraguti and Pagano explicitly prove the decisive PCF parameter bound: \(c\) is an algebraic integer, every postcritical value is archimedean-bounded by 2, and they immediately record \(h(c)\le\log2\) and apply Northcott. From that published lemma, the audited degree-independent preperiodic bound follows mechanically by the standard canonical-height comparison and an elementary explicit Northcott coefficient count. The exact enormous formula is not a new mathematical phenomenon; it is a crude explicit instantiation of those standard steps.

### equivalent_formulations

Searches:
- Resultary: PCF unicritical polynomial number field degree-independent bound rational preperiodic points height Northcott
- Ferraguti–Pagano Lemma 4.1

Evidence:
- The exact Resultary hit is this record. Ferraguti–Pagano explicitly state the same PCF height bound on \(c\).

Reasoning:
Equivalent formulations as bounded PCF parameter height plus Northcott and as a canonical-height preperiodic bound lead to the same standard argument.

### broader_coverage

Searches:
- Ferraguti–Pagano, Lemma 4.1
- standard canonical-height telescoping
- Northcott theorem

Evidence:
- The published lemma supplies the only PCF-specific input; the remaining steps are general height theory.

Reasoning:
This broader combination directly dominates the claimed qualitative theorem and leaves only a crude explicit constant calculation.

### exact_database_or_table

Searches:
- Northcott finite sets of bounded degree and height

Evidence:
- No special database is required: an elementary coefficient count mechanically produces a finite explicit bound once height and degree are bounded.

Reasoning:
The exact numerical formula is not protected from coverage merely because a prior source does not tabulate it.

### claim_vs_prior_implication

Searches:
- claim versus Ferraguti–Pagano plus standard height inequalities

Evidence:
- Ferraguti–Pagano explicitly conclude \(h(c)\le\log2\) from PCF; standard height comparison then bounds all preperiodic heights uniformly in \(d\).

Reasoning:
The audited theorem is a direct corollary followed by a deliberately loose explicit counting estimate.

### source_inspections
- **Abelian dynamical Galois groups for unicritical polynomials** — arXiv:2303.04783. Trigger: Highly relevant PCF unicritical source. Material read: Accessible full-text copy, including Lemma 4.1 and the paragraph immediately applying it to logarithmic Weil height and Northcott. Method: Primary full-text theorem comparison. Assessment: DECISIVE PRIOR COVERAGE of the PCF-specific height input. Evidence: Lemma 4.1 states that PCF forces integrality of \(c\) and archimedean bound 2; the next paragraph states \(h(c)\le\log2\) and invokes Northcott.
- **Assigned bound script** — artifacts/compute_B.py. Trigger: Explicit constant calculation. Material read: Complete source file. Method: Line-by-line inspection and independent arithmetic check. Assessment: Correct arithmetic, but it does not create originality beyond the standard explicit Northcott count. Evidence: It reproduces \(B(1)=289\) and \(B(2)=8586756\).

### checked_sources

- Ferraguti–Pagano arXiv:2303.04783
- standard canonical-height theory
- Northcott theorem
- assigned RESULT.md and artifacts/compute_B.py
- Resultary semantic search

### residual_risks

- A sharper explicit bound may still be worthwhile, but the audited formula is not presented or justified as sharp.

## Scientific value — FAIL

The qualitative uniform finiteness follows immediately from a known uniform PCF height bound plus standard canonical-height and Northcott theory, while the displayed constant is an intentionally enormous coefficient-count bound with no extremal or structural significance. Correctness and explicitness alone do not make this routine instantiation a valuable new mathematical gap under the required standard.

Sources:
- Ferraguti–Pagano Lemma 4.1
- Northcott theorem

Risks:
- This judgment does not diminish the importance of sharp uniform boundedness questions; it concerns only this crude bound.

## Limitations

- Scientific rejection is originality/value based, not correctness based.
- The result excludes the fixed point at infinity, as stated.
- No claim is made that the bound is remotely sharp.

## Disposition

**FAILED**
