# Independent Audit — 2026/09/19/redundancy-fifteen-generalized-packing-covering--a1d17c619bef

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `cfaf6a5e7961e89e463b51dd7ac96171482139e9`
- Disposition: **FAILED**

## Correctness

**PASS** — The weaker exceptional-case estimate used here is still sufficient and correct. From d_3(C)>=15 one gets d_4(C^perp)>=k+2. Shortening on nine independent coordinates and discarding forced-zero coordinates yields a binary six-dimensional code of length N<=k+6 with d_4>=k+2, hence every two-space contains at most N-d_4<=4 generator columns with multiplicity. The submitted line-cap lemma is valid: direct enumeration of the possible zero multiplicity z and maximal nonzero multiplicity M gives maxima 64,64,34,4,4 for z=0,...,4. Therefore N<=64 and d_4<=N gives k<=62, so n<=77. Independent exact arithmetic confirms V_8(77,6)=28,229,190,167,564<2^45=35,184,372,088,832. The finite parameter reduction is consistent with the same source framework, so the stated redundancy-15 conclusion follows.

## Originality

**FAIL** — The main theorem had already appeared publicly in the repository before this record. The earlier record 2026/09/18/packing-covering-redundancy-fifteen--96101bcc4ffa first appeared in commit 521ee48c27a54baf7111e2d6603a00a7aba90184 at 2026-09-18T02:02:52Z; this record first appeared in commit 543f1ebc68d0fdef4910c3d3d16fbb77c0ede006 at 2026-09-19T09:12:19Z. The earlier record proves the same universal redundancy-at-most-15 conclusion by the same residual tuple and a stronger version of the same six-dimensional line-multiplicity argument, obtaining n<=73 rather than the present n<=77. Thus neither the theorem nor the decisive mechanism is new here.

## Scientific value

**FAIL** — The record provides a correct alternate presentation, but its intermediate bound is weaker than the already-public record and it yields no additional parameter regime or new structural consequence. As an independent research record it therefore lacks incremental scientific value even though the proof is self-contained and valid.

## Sources

- **Auxiliary Codes and the Generalized Packing-Covering Conjecture** — Isaac Barouch Essayag; Aryeh Lev Zabokritskiy. https://arxiv.org/abs/2609.19098 — Primary external source for the redundancy-14 theorem and reduction framework.
- **Earlier SCOPE redundancy-15 record** — SCOPE-Science repository. https://github.com/SCOPE-Science/SCOPE2026/tree/521ee48c27a54baf7111e2d6603a00a7aba90184/2026/09/18/packing-covering-redundancy-fifteen--96101bcc4ffa — Public commit 521ee48c27a54baf7111e2d6603a00a7aba90184, 2026-09-18T02:02:52Z; predates this record and proves the same theorem with a stronger n<=73 exceptional-case bound.

## Limitations

- The failure is for originality and scientific value, not correctness.
- The current proof's n<=77 route is sufficient but weaker than the earlier public n<=73 route.
- Repository chronology establishes duplication inside SCOPE; no broader external priority claim is needed for this disposition.

## Independent checks

```json
{
  "proof_reconstructed": true,
  "line_cap_case_maxima_by_zero_multiplicity": [
    64,
    64,
    34,
    4,
    4
  ],
  "covering_volume_n77": 28229190167564,
  "required_volume": 35184372088832,
  "prior_public_record": "2026/09/18/packing-covering-redundancy-fifteen--96101bcc4ffa",
  "prior_first_commit": "521ee48c27a54baf7111e2d6603a00a7aba90184",
  "prior_first_commit_time_utc": "2026-09-18T02:02:52Z",
  "current_first_commit": "543f1ebc68d0fdef4910c3d3d16fbb77c0ede006",
  "current_first_commit_time_utc": "2026-09-19T09:12:19Z",
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Preprints and lawful open-access sources were checked first; no decisive comparison remained inaccessible, so Oxford Download was not required.
