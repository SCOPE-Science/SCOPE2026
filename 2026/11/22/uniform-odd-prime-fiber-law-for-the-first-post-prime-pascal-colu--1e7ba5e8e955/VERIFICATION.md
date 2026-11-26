---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

There is exactly one factor of p in (p+1)!. On n=r+pt with r nonzero modulo p, cancel the unique linear factor pt and reduce the remaining product modulo p to obtain F(r+pt)=rt+pQ_r(t), Q_r integral over Z_p. Divided differences are units after extracting t-u, so the map induces a bijection at every precision and on Z_p. On n=pt cancel two factors of p before dividing by the factorial, obtaining G(t)=F(pt)/p with G(t) congruent coefficientwise to t(t-1). The exact symmetry G(1-t)=G(t) gives G(1/2+s)=G(1/2)+s^2 W(s^2) with W congruent to 1. The unique root E(s) of W(s^2) congruent to 1 exists by Hensel lifting; E(s)-E(u) is divisible by p(s-u), since E(s)+E(u) is a unit and the difference of their squares is divisible by p(s-u). This makes s*E(s) an isometric bijection. Alpha_p=pG(1/2) has valuation one. Counting solutions of the resulting square equation modulo p^(h-1) gives p lifts per root modulo p^h, including the modulus-one convention. The falling-factorial denominator proves periodicity with shift p^(h+1); F(1+p^h) has valuation h-1 whereas F(1)=0, so the least period, which divides p^(h+1), is not a proper divisor. The target-class restriction and h=1 boundary both follow.

## originality

PASS

The exact p=3 case and its square branch occur in two materially overlapping same-day records; their timestamps do not decide priority. The supported distinct claim is the entire odd-prime exact law, in particular its extension beyond the known ternary column. The literature inspected establishes universality and the least period, which the frozen claim already excludes from novelty; it does not establish the general singular-branch law or frequencies.

## value

PASS

At the first column just past the prime, one input residue class ceases to be a regular Hensel branch. Counting all target residues identifies exactly how that class redistributes mass, which surjectivity cannot answer. The exact square normal form gives a usable structural description at every precision and for every odd prime, not a numerical extension of a ternary table or a new proof of the known period alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
