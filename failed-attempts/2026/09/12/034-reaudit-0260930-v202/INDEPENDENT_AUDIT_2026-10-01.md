# Independent mathematical audit — SCOPE-20260912-034

**Audit date (UTC):** 2026-10-01 (UTC)  
**Disposition:** failed

## Final claim reviewed

Double-relative K2 of the split node over F7 contains a Z/48 subgroup

## Correctness — PASS

The conductor calculation is correct: A={f in F_7[t]:f(1)=f(-1)}=F_7+(t^2-1)F_7[t], so A/I=F_7 and B/I=F_7 x F_7. Double-relative K-theory is the total homotopy fiber of the conductor square, giving the standard long exact corner sequence. Quillen gives K_3(F_7)=Z/48 and homotopy invariance identifies K_3(F_7[t]) with it; both evaluations t=+/-1 induce the same map, so the image in K_3(F_7 x F_7)=(Z/48)^2 is the diagonal and its cokernel Z/48 injects into K_2(A,B,I). Fresh finite-group arithmetic independently reproduced the diagonal cokernel. The claim is only a subgroup statement; the full K_2(A,B,I) is not computed.

## Originality — FAIL

The named F_7 statement is a direct specialization of standard double-relative/Mayer-Vietoris formalism plus Quillen’s finite-field K_3 computation and homotopy invariance. Once the split-node conductor square is written down, the Z/48 boundary subgroup is mechanically implied; exact wording or the number 48 need not appear in an earlier title for the claim to be covered.

### Equivalent formulations
Reasoning: The record’s boundary formulation is an equivalent presentation of the standard total-homotopy-fiber long exact sequence.

Searches:
- Resultary: birelative K2 split node conductor Z/48
- Geller-Weibel K(A,B,I): II

Evidence:
- The double-relative group is the total-fiber obstruction to excision for the conductor square.

### Broader coverage
Reasoning: These results dominate the q=7 calculation and in the same split-node setup give the analogous diagonal cokernel for general odd q.

Searches:
- Quillen finite-field K-theory
- Geller-Weibel double-relative K-theory
- Morrow pro-excision for one-dimensional rings

Evidence:
- General double-relative exact sequences apply to arbitrary excision squares; Quillen computes K_3(F_q)=Z/(q^2-1).

### Exact database or table
Reasoning: The lack of an exact database row does not overcome the direct implication from broader prior theorems.

Searches:
- Resultary exact semantic search for split node F7 Z/48

Evidence:
- Resultary returned the same SCOPE record and no independent exact table entry.

### Claim versus prior implication
Reasoning: The final claim follows by substituting the record’s conductor square into prior general machinery, so it is covered as a corollary.

Searches:
- Geller-Weibel exact-sequence framework
- Quillen 1972 finite-field K-groups

Evidence:
- The corner map is diagonal after homotopy invariance; its cokernel is Z/48.

### Source inspections

- **K(A,B,I): II** (doi:10.1007/BF00538431). Trigger: definition and exact-sequence framework for double-relative K-theory. Material read: primary full text around the definition of K(A,B,I) as an excision obstruction and the associated exact-sequence formalism. Method: full-text inspection. Assessment: general framework covers the boundary construction used here. Evidence: The paper treats double-relative groups as the obstruction to Mayer-Vietoris/excision for such squares.
- **On the cohomology and K-theory of the general linear groups over a finite field** (Quillen, Annals of Mathematics 96 (1972)). Trigger: finite-field K_3 input. Material read: the theorem-level finite-field K-group computation as cited by the record. Method: primary theorem comparison. Assessment: supplies K_3(F_7)=Z/48, the only numerical input. Evidence: For finite F_q, K_{2i-1}(F_q) has order q^i-1; i=2 gives 48.

### Checked sources

- Resultary semantic search
- Geller-Weibel 1989 primary paper
- Quillen 1972 primary theorem
- Morrow arXiv:1211.1533 contextual pro-excision paper

### Residual risks

- No attempt was made to compute the full birelative K_2 group; the audit only checks the subgroup claim and its prior implication.

## Scientific value — FAIL

As a q=7 instance the result is a short mechanical specialization of general double-relative exact-sequence machinery and Quillen’s table. The package gives no mathematical reason that q=7 or the exact number 48 is a natural boundary, and it does not compute the full birelative group. Correctness and reproducibility therefore do not by themselves meet the value bar for this narrow invariant.

## Limitations

- The audit does not compute the full K_2(A,B,I); it only validates the boundary subgroup and judges that subgroup claim to be prior-implied/routine.

The finding is not accepted because all three scientific axes do not pass. The original research files and evidence are preserved in the failed-attempt package.
