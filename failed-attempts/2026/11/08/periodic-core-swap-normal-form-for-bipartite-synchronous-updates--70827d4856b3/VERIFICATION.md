---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: On finite periodic points, g=f∘g and k=g∘f are intertwining (notation disambiguated by writing h=f∘g); g gives a bijection between periodic cores with inverse h^{-1}∘f on that core. Thus F(x,y)=(f(y),g(x)) conjugates to T(u,v)=(h(v),u) on P_h². Even iterates have A_(n/2)^2 fixed points, odd iterates A_n, and Möbius inversion gives exact primitive periods. Direct all-function checks over X,Y of sizes 1..3 cover 900 function pairs and 7200 iterate identities (n=1..8), agreeing. The K(K−1) primitive-period-two population follows by F² fixed =K² and F fixed=K. The proof is general for arbitrary finite maps and does not imply that general strict-majority dynamics have only periods 1 or 2. The graph application is valid for odd-degree bipartite strict-majority update, where there are no tie-retaining self-state dependencies.

## originality

FAIL

FAIL: A previously published stronger all-coordinate cyclic-permutation theorem proves exactly #Fix(F^m)=a_{m/gcd(m,s)}^{gcd(m,s)}. Its proof explicitly says it needs only composable maps between sets, not continuity of intervals. Specializing s=2 gives the identical odd/even fixed-point counts for arbitrary finite f,g. The earlier proof transports periodic points bijectively among coordinate maps, so the present periodic-core conjugacy is its elementary coordinate reparameterization. Möbius inversion and K(K-1) are immediate consequences. A new alternate name 'periodic-core swap normal form' cannot make a covered theorem original; the odd-degree bipartite majority example just specializes the same arbitrary-map statement.

## value

FAIL

FAIL: The all-finite-map fixed-point formula, Möbius orbit census, and K(K−1) two-period count are already direct s=2 corollaries of a previously published stronger s-coordinate theorem. The core conjugacy is a routine coordinate transport from the same proof; the majority-graph application is a substitution into that general identity. No motivated new independent exact fact survives beyond known theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
