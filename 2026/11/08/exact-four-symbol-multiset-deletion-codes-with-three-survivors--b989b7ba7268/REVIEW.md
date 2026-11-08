# Scientific review: exact four-symbol three-survivor multiset codes

## Correctness — PASS

The deletion-decoding requirement is equivalent to a bounded multiset intersection \(\Omega(x,y)\leq2\), because the receiver retains precisely three symbols. For \(n\geq9\), disjoint nonempty heavy-coordinate index sets impose the four-word bound. For \(n=3\), all 20 vectors are usable; for \(4\leq n\leq8\), the explicitly enumerated lexicographic compatibility graphs admit no cliques of respective target sizes \(12,7,6,6,6\), by an exhaustive exact recursion with justified pruning. All lower-bound witnesses and their deletion descendants were checked directly by the packaged checker. The finite computation is exhaustive over each claimed finite domain, not a claim of infinite-search completeness.

## Originality — PASS, subject to residual historical priority risk

The closest published 2026 three-survivor theorem (Kreindel–Essayag–Zabokritskiy, arXiv:2601.05636v1, §3.5) supplies general bounds and the underlying intersection characterization, but not exact \(q=4\) values. The 2026 companion arXiv:2603.18322v1 concerns exact ball geometry and resulting bounds, not the maximum quaternary code size at each length. Kovačević–Tan (arXiv:1612.08837) supplies the general simplex metric and asymptotics, with no matching finite profile. An indexed published ternary three-survivor finding covers \(q=3\), not the quaternary exceptional lengths; its large-length method is appropriately credited. Search and index evidence does not exclude an unknown older exact table; the public ternary finding's entire primary text could not be accessed.

## Value — PASS

This resolves the first alphabet size beyond ternary for a natural high-deletion multiset code problem: exact capacity at every blocklength, four separate exceptional regimes, explicit optimal witnesses, and a sharp stabilization threshold at length nine. This is a finite/infinite extremal classification motivated by the source paper's non-tight three-survivor bounds, rather than an arbitrary parameter sample. The complete finite certificates are very small and reusable.

## Limits

Not a classification of extremal code isomorphism types, other alphabets, or other received multiset sizes; no independent mathematical audit is claimed.

Self-review: passed. Independent audit: not yet performed.
