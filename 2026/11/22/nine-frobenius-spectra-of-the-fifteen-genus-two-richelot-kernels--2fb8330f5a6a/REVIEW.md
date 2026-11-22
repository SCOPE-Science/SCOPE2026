# Research assessment: Nine Frobenius spectra of the fifteen genus-two Richelot kernels

## Correctness — PASS

The six Weierstrass roots describe the 16 even-subset modulo complement classes in the Jacobian's geometric two-torsion. Each of the fifteen maximal isotropic subgroups corresponds to an unordered perfect matching of the roots. Frobenius relabels roots according to their sextic factorization degrees; all eleven integer partitions of six are exhausted. The attached exact arithmetic/permutation program replays the eleven orbit counts, checks fixed-point counts for every relevant Frobenius power, confirms the two collisions, and verifies both squarefree characteristic-seven witnesses. No finite experiment substitutes for the six-root equivariance proof.

## Originality — PASS, with significant derivability and historical-priority risk

Bruin–Doerksen (2009, https://arxiv.org/abs/0902.3480, Sections 4 and 6) already provide the general Galois-stable quadratic-splitting description, and even analyze the subgroup stabilizer and conditions for multiple rational kernels. The Kunzweiler finite-field isogeny computation (ePrint 2022/990, 2022-08-03, https://eprint.iacr.org/2022/990; published 2024) and the Magma Richelot handbook provide the method context. The present narrower arithmetic statement is the explicit *complete eleven-type Frobenius cycle and zeta table*, its nine distinct spectra, and exactly two branch-partition collisions, including a pair with equal kernel-scheme zeta but different rational Jacobian two-torsion. Source and published-record comparisons found no same table; this is not evidence of absolute priority. The familiar S6 syntheme action implies each row after finite calculation, so a preexisting group-theory table or an inaccessible appendix remains a substantial risk. The closest differently named 15-line Igusa result has the duad, not syntheme, action. See `AUDIT.json` for the detailed four named overlap checks and material-read limits.

## Value — PASS

The finite étale scheme of maximal isotropic (2,2)-isogeny kernels is a natural arithmetic construction: rational subgroup schemes need not consist of rational torsion points. Exactly classifying every possible kernel orbit profile gives the full extension-field zeta data for every odd-characteristic squarefree sextic model; explicit equal-zeta/different-torsion examples demonstrate why counting rational branch factors or rational generators alone is insufficient. The result is finite and relies on a classical action, but its 11-type classification and two arithmetic counterexamples are complete and directly relevant to finite-field isogeny descent.

## Limitations

This concerns kernel subgroup schemes, not the number of isogeny maps modulo automorphisms or smooth genus-two codomains. The full geometric S6 model, Richelot kernel interpretation and their rational descent are known. The complete older Takashima–Yoshida text and all historical appendices were not read, and no independent mathematical validation has occurred. The 2022 finite-field isogeny work motivates this arithmetic question; substantially older Galois theory is cited and credited, not re-presented as new.

Self-review: passed. Independent audit: not yet performed.
