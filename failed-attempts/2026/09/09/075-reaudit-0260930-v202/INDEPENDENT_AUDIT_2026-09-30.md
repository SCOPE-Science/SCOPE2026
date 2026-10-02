# Independent mathematical audit — SCOPE-20260909-075

Outcome: **FAILED**.

## Correctness
**PASS** — The rational circulant theta-prime witness has trace one, nonnegative entries, zeros on C7 edges, positive exact LDL pivots, and objective 82827/25000. Bukh-Cox Proposition 4 gives H_f(C_(2k+1);F)=k+1/2 for every field, hence H_f(C7;F)=7/2, and multiplicativity gives the stated power-four obstruction.

## Originality
**FAIL** — The Haemers leg H_f(C7)=7/2 is explicitly prior in Bukh-Cox Proposition 4. For the theta-prime leg, automorphism averaging reduces the C7 SDP to the two nonedge-distance circulant coefficients; the standard Lovasz odd-cycle optimum has both coefficients nonnegative, so the entrywise-nonnegative variant attains the same classical value about 3.317667, already stronger than the record's 3.31308 floor. The advertised level-1 obstruction is therefore mechanically implied by established bounds.

## Value
**FAIL** — The exact rational LDL point is reproducible but weaker than the classical exact C7 theta certificate, while the second leg is a published exact formula. Packaging those known facts does not create a new mathematically meaningful obstruction.

## Source inspections
- **Bukh-Cox, On a fractional version of Haemers' bound, arXiv:1802.00476v2** — Full HTML inspected. Proposition 4 states H_f(C_(2k+1);F)=k+1/2 for every field; Theorem 3 gives multiplicativity. Consequence: H_f(C7)=7/2 and its strong-power consequence are explicit prior results
- **Lovasz, On the Shannon capacity of a graph, IEEE Trans. Inf. Theory 25 (1979)** — Classical odd-cycle theta formula compared with the C7 symmetry-reduced SDP; the optimum is about 3.317667. Consequence: the theta-prime >3.30 obstruction is already mechanically available from the standard nonnegative C7 optimum

## Residual risk
See the accompanying JSON audit for the explicit residual-risk record.
