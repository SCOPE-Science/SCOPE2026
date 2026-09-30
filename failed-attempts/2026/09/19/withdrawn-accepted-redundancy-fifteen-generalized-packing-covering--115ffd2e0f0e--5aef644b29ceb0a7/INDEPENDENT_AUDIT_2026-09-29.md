# Independent Audit — 2026/09/19/redundancy-fifteen-generalized-packing-covering--115ffd2e0f0e

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `fe4cf6ebd220c8c0dfb96546f71007acbf5af3ba`
- Disposition: **FAILED**

## Correctness

**PASS** — The mathematics of the redundancy-15 closure checks. The source reduction leaves the binary residual tuple (q,t,r)=(2,3,6), and d_3(C)>=15 implies d_4(C^perp)>=k+2 by the stated parity-check nullity argument. After shortening nine independent dual coordinates, the six-dimensional code has N=k+6 and d_4>=N-4. The projective-line multiplicity condition then gives N<=64: if a zero column occurs, summing all 651 line constraints gives the bound; without zero columns, a multiplicity at least three gives N<=35, while the 0/1/2 multiplicity case gives N<=64 by pairing double points with forced zero points. Thus n<=73. Independent exact arithmetic reproduces V_8(73,6)=20,282,523,983,828<2^45=35,184,372,088,832. The theorem is therefore correct.

## Originality

**FAIL** — This record is not original within the public repository timeline. The earlier record 2026/09/18/packing-covering-redundancy-fifteen--96101bcc4ffa was introduced in commit 521ee48c27a54baf7111e2d6603a00a7aba90184 at 2026-09-18T02:02:52Z, more than a day before this record's first public commit da480f3c07d11c95c0028007bdc654329bc94124 at 2026-09-19T10:25:23Z. The earlier record proves the same universal redundancy-at-most-15 theorem, reduces to the same exceptional binary tuple (15,3,6), obtains the same six-dimensional line-multiplicity bound N<=64 and the same n<=73 covering-ball contradiction. The current proof is a reformulation of that already-public result, not an independent new theorem.

## Scientific value

**FAIL** — The argument is clear and correct, but as a repository research record it adds no substantive theorem, parameter range, sharper bound, or distinct mechanism beyond the earlier public redundancy-15 record. A duplicate exposition can be useful pedagogically, yet it does not meet the independent scientific-value threshold for a validated finding.

## Sources

- **Auxiliary Codes and the Generalized Packing-Covering Conjecture** — Isaac Barouch Essayag; Aryeh Lev Zabokritskiy. https://arxiv.org/abs/2609.19098 — Primary external source proving the universal statement through redundancy 14 and supplying the reduction machinery.
- **Earlier SCOPE redundancy-15 record** — SCOPE-Science repository. https://github.com/SCOPE-Science/SCOPE2026/tree/521ee48c27a54baf7111e2d6603a00a7aba90184/2026/09/18/packing-covering-redundancy-fifteen--96101bcc4ffa — Public commit 521ee48c27a54baf7111e2d6603a00a7aba90184, 2026-09-18T02:02:52Z; already proves the same redundancy-15 theorem with the same exceptional binary tuple, N<=64 bound and n<=73 covering contradiction.

## Limitations

- The failure is for originality and independent scientific value, not mathematical correctness.
- The audit uses repository commit chronology as direct priority evidence; it does not make a broader claim about external publication priority.
- The result remains a valid proof of redundancy 15, but it should not coexist as a separately validated research finding duplicating the earlier record.

## Independent checks

```json
{
  "proof_reconstructed": true,
  "line_cap_bound_checked": true,
  "covering_volume": 20282523983828,
  "required_volume": 35184372088832,
  "prior_public_record": "2026/09/18/packing-covering-redundancy-fifteen--96101bcc4ffa",
  "prior_result_blob_sha": "18aa98eb7a5d134d70f1dd8e7c4c4730cadcd65e",
  "prior_first_commit": "521ee48c27a54baf7111e2d6603a00a7aba90184",
  "prior_first_commit_time_utc": "2026-09-18T02:02:52Z",
  "current_first_commit": "da480f3c07d11c95c0028007bdc654329bc94124",
  "current_first_commit_time_utc": "2026-09-19T10:25:23Z",
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Preprints and lawful open-access sources were checked first; no decisive comparison remained inaccessible, so Oxford Download was not required.
