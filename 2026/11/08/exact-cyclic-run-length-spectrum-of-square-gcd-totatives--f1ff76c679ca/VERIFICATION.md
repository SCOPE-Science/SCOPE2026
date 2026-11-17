---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

At p^a the allowed valuations min(v_p(x),a) are precisely even ones, including zero only if a even. For r<=p, p-r residue classes avoid p, while each of r classes containing a single multiple of p admits B_p(a-2) eligible lifts for a>=2; for p<r<=2p exactly 2p-r classes contain one multiple; r>=2p has two multiples separated by p so at least one forbidden valuation one. At a=1 only p-r classes contribute. CRT multiplies the independent local counts without statistical assumptions. Positivity at local r=p-1 or 2p-1 proves exact global longest run; second finite difference W(r)-2W(r+1)+W(r+2) counts maximal cyclic runs because A_n is a proper subset n>=2. Fresh direct integer gcd/isqrt enumeration checked 699 moduli n2..700, 10394 windows and 41473 histogram entries.

## originality

PASS

One-point beta(n)=number of x with square gcd is classical. Schemmel totients count blocks of units, agreeing with the squarefree special case, but at prime powers a>=2 allowing v_p even including v_p=2 creates distinct local correction B_p(a-2). The earlier full arbitrary-shift theorem for regular integers modulo n uses valuations 0 or exactly a and is not equivalent (indeed for squarefree n every residue regular, while only units are square-gcd admissible); it does not dominate square-gcd run frequencies.

## value

PASS

Square-gcd totatives arise naturally from alternating divisor counts; the maximal run length and full run spectrum are canonical arithmetic statistics, extending a one-point multiplicative function to joint consecutive correlations and sharp periodic gaps. The exact parity-of-valuation corrections are not a trivial unit case or table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
