# Independent Audit — 2026/09/14/020

Audit date: 2026-09-28 (UTC)
Audited tree: `077c5b2bfc0ac332dca7a02da826fc65b8ab30d4`

## Disposition

**FAILED** — Rejected for correctness: the claimed local asymptotic stability under downstream R0<=1 is false at an undriven equality case, where the downstream disease-free block has a zero eigenvalue.

## Correctness

**FAIL**. The block-triangular threshold and recursive equilibrium construction are largely sound, but the LAS statement is too strong at equality. If a downstream link carries no exposed or infective movement, then D_j=0. Choose the corresponding effective downstream reproduction number Rtilde_j=1 (allowed by the hypothesis R0^(j)<=1, e.g. with no susceptible inflow so Rtilde_j=R0^(j)=1). The linearized (E_j,I_j) block has characteristic polynomial lambda^2+(a_j+b_j)lambda+a_j b_j-beta_j S_j sigma_j, whose constant term is zero at Rtilde_j=1, so it has a zero eigenvalue. Hence the asserted equilibrium is not locally asymptotically stable in that admitted edge case. A sufficient corrected hypothesis is strict Rtilde_j<1 whenever D_j=0 (in particular downstream R0^(j)<1). The numerical verifier only samples strict subcritical values and therefore misses this boundary.

## Originality

**UNRESOLVED**. One-way epidemic-patch literature already contains the max-of-patch reproduction-number structure and source/downstream endemic-boundary behavior in two-patch SEIRD/SIR/SIS models, while older work treats one-way multi-patch chains in related compartment systems. I did not identify an open-access source proving exactly this three-patch mass-action SEIR recursive quadratic theorem. Because the submitted theorem is incorrect at equality and no exact covering prior was established, originality is left unresolved rather than inferred either way.

## Scientific value

**FAIL**. The recursive triangular construction is potentially useful as a clean special-case lemma, but the published headline includes a false stability boundary and the surviving strict-subcritical version is a straightforward cascade of single-patch algebra. As submitted it does not clear the standard for a standalone validated research finding.

## Evidence and limitations

Repository files were read from the exact assigned/current tree; GitHub was used only as evidence and was not modified. Lawful open-access/preprint sources were checked first:
- https://doi.org/10.3389/fams.2023.1024571 — Djiomba Njankou–Nyabadza: a one-directional two-patch SEIRD model where the system reproduction number is the largest patch reproduction number and source/endemic boundary equilibria are analyzed.
- https://doi.org/10.1016/j.mbs.2005.09.002 — Arino–Jordan–van den Driessche: multi-patch epidemic models including one-way migration structure and SEIR-type examples.

Independent checks:
- Independent linearization of a disease-free downstream patch gives det[[−a,beta*S],[sigma,−b]]=ab−beta*S*sigma, hence a zero eigenvalue exactly when the effective patch reproduction number equals one.

No inaccessible material is represented as read. Literature absence was not treated as proof of novelty; where exact prior coverage remained uncertain, the originality axis is explicitly marked unresolved.
