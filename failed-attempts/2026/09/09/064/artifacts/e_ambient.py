"""Ambient-rescue check (§H): the ONLY ambient manifold pinned in the admitted
sources (Teng §2.1) is the elliptic surface E(n), n>=2, in which W embeds
and along which the f^k twist is PROVED non-extending (via Fintushel-Stern
knot surgery: regluing W by f^k in E(n) = knot surgery by k-twist knot,
distinguished by Alexander polynomials [7]).

E(n): chi = 12n, sigma = -8n (standard elliptic-surface invariants).
Contractible requires chi=1 -> 12n=1 impossible. Closed (no boundary) ->
not a Stein domain in the compact-with-boundary (Gompf/Teng/Takahashi) sense.
Knot surgery preserves homeomorphism type (Freedman) so (E(n), E(n)_{K_k})
is a genuine homeomorphic-but-not-diffeomorphic pair -- but it is closed,
simply-connected, chi=12n, NOT contractible, NOT Stein, and its trisections
are CLOSED (not relative), so the 'g=3 vs >=4 relative' clause is N/A.

Conclusion: the single source-pinned ambient rescue lands entirely outside
the target class. No contractible ambient containing C1 is pinned anywhere
in Teng/Takahashi. The target's 'homeomorphic compact contractible Stein'
pair therefore has no source-grounded ambient reading either.
"""
import json

rows = []
for n in [2, 3, 4]:
    rows.append({"n": n, "chi": 12 * n, "sigma": -8 * n,
                 "contractible": (12 * n == 1), "closed": True,
                 "stein_domain": False, "relative_trisection_applies": False})
out = {
    "ambient": "E(n), n>=2 (Teng §2.1)",
    "rows": rows,
    "twist_pair": "(E(n), E(n)_{K_k}): homeomorphic (Freedman), "
                  "non-diffeomorphic (FS/Alexander [7])",
    "in_target_class": False,
    "reason": "closed, chi=12n>>1, not Stein, closed (not relative) trisections",
    "contractible_ambient_pinned": False,
}
print(json.dumps(out, indent=2))
assert all(r["chi"] != 1 for r in rows)
