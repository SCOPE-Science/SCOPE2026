# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260913-009`

Disposition: **FAILED**

## Correctness — PASS

The separating curve \(c=[a_1,b_1]\) becomes null after the handlebody meridians \(b_1,b_2\) are killed; as a simple null-homotopic boundary curve it bounds a disk in the handlebody, so the twist extends and the resulting double is \(\#^2(S^1\times S^2)\). Its Betti numbers are \((1,2,2,1)\). For \(G=SL_2\), the tangent complex at the trivial local system is \(C^*(M;\mathfrak{sl}_2)[1]\), giving dimensions \((3,6,6,3)\) and virtual dimension zero. Calaque's boundary theorem supplies the Lagrangian restriction maps; the package's exact rank/isotropy check matches these calculations.

## Originality — FAIL

The derived-symplectic and boundary-Lagrangian assertions are direct instances of PTVV/Calaque, while the topology after a disk-bounding separating twist and the trivial-local-system cohomology are elementary consequences. The tuple \((3,6,6,3)\) is mechanically implied by the standard tangent formula and Betti numbers, so exact absence from a table does not make it original.

### Equivalent formulations

**Searches:** published SCOPE records: genus two Heegaard SL2 tangent cohomology; Calaque mapping stacks boundary Lagrangian

**Evidence:** Calaque explicitly states that \(Loc_G(M)\to Loc_G(\partial M)\) is Lagrangian for compact oriented manifolds with boundary.

The record's two handlebody maps are exactly this boundary-restriction construction.

### Broader coverage

**Searches:** PTVV shifted symplectic mapping stacks; Calaque arXiv:1306.3235 full text

**Evidence:** The prior theorems apply to arbitrary reductive \(G\) and oriented manifolds, not just genus two and \(SL_2\).

The structural stack claims are special cases of broader published theorems.

### Exact database or table

**Searches:** published SCOPE semantic search for the exact \((3,6,6,3)\) tuple

**Evidence:** Only the same SCOPE record was an exact hit.

The dimensions follow immediately from \(b(M)=(1,2,2,1)\) and \(\dim\mathfrak{sl}_2=3\), so a separate table is unnecessary for prior implication.

### Claim versus prior implication

**Searches:** Calaque Theorem 2.9 / Example 3.1; standard tangent complex of local-system mapping stacks

**Evidence:** Calaque gives the Lagrangian restriction map; the standard mapping-stack tangent formula is \(C^*(M;ad\rho)[1]\).

After the elementary identification \(M\cong\#^2(S^1\times S^2)\), all displayed tangent dimensions and duality follow formally.

### Source inspections

- **Lagrangian structures on mapping stacks and semi-classical TFTs** (https://arxiv.org/abs/1306.3235). Trigger: boundary-Lagrangian assertion. Material read: Theorem 2.9 discussion and Example 3.1 around the restriction \(Loc_G(M)\to Loc_G(\partial M)\). Method: full-text inspection. Assessment: directly covers the structural claim. Evidence: The paper states that an oriented manifold with boundary gives a natural Lagrangian structure on the restriction mapping stack.
- **Shifted Symplectic Structures** (https://arxiv.org/abs/1111.3209). Trigger: 0-shifted symplectic surface character stack and derived Lagrangian intersection. Material read: the mapping-stack shifted-symplectic theorem and Lagrangian-intersection framework. Method: primary theorem comparison. Assessment: general background strictly broader than the record. Evidence: Classifying stacks of reductive groups are shifted symplectic and oriented mapping stacks inherit shifted symplectic forms.

### Checked sources

- published SCOPE semantic search
- Calaque arXiv:1306.3235
- PTVV arXiv:1111.3209

### Residual risks

- No global component structure or enumerative invariant was audited because the record expressly disclaims those claims.

## Scientific value — FAIL

The exact example combines a standard disk-twist simplification with the standard local-system tangent formula. It does not reveal a new structural obstruction, boundary phenomenon, or unknown invariant; the displayed dimensions are a textbook-level multiplication of Betti numbers by \(\dim\mathfrak{sl}_2\).

## Limitations

- The audit is local at the trivial representation and does not assess any unclaimed Tor, Behrend, component, or enumerative invariant.

The finding is not accepted because all three scientific axes do not pass. The original research files and evidence are preserved in the failed-attempt package.
