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

The return of (F_n,F_(n+1)) to (0,1) is equivalent to M^n=I, so scalar periods equal matrix orders. Direct prime-level iteration gives 16 and 10; the two displayed powers are I+pB with unit upper off-diagonal in B. The binomial p-power lift gives v_p(F_(Pt))=1+v_p(t) for nonzero t, which proves the exact prime-power orders; gcd=2 and lcm=80·7^(a−1)·11^(b−1). For a period increment h=Pt with t nonzero, L_h+2 is a unit, so (L_h−2)(L_h+2)=5F_h² gives v_p(L_h−2)=2v_p(F_h). In the Fibonacci addition law, if L_r is a unit the term F_hL_n uniquely has the smallest valuation: the normalized Fibonacci branch is an isometry at each finite precision, giving one preimage per target in its residue disk. The excluded indices are 4 and 12 modulo 16 and 5 modulo 10. In those branches F_r is a unit, so the Lucas addition law instead makes the normalized Lucas map isometric and onto the divisible Lucas classes. The identity L_n²=5F_n²+4(-1)^n, with 10F_r a unit, then identifies the exceptional frequency with R_(p,k). For D=0 the root is divisible by p^ceil(k/2), giving p^floor(k/2) choices (including k=1); nonzero represented D has no root unless its valuation is even and the unit part is a square, and gives 2p^h roots when v_p(D)=2h≥2. Generalized CRT gives one index for each pair of equally paritied local indices, none otherwise. The seven-adic support sizes (even, odd, intersection) are (3A+2Q_7,4A,2A), A=7^(a−1), and eleven-adic sizes are (5B,2B+Q_11,B), B=11^(b−1), with Q at exponents a−2,b−2. Inclusion–exclusion yields the finite formula; Q_p counts squares and its normalized limit is the sum of the even valuation weights, p/[2(p+1)]. Substitution proves the two-variable density and discrepancy, not just a diagonal limit. A fresh recurrence replay checked complete parity tables and the root counts up to local exponent five and every composite fiber and support for all nine exponent pairs in [1,3]², including the stated support values 35, 1755 and 130525. Replay: python /workspace/replay_frozen.py 1. Finite checks do not establish the all-exponent theorem without the proof.

## originality

PASS

Pass is for the exact mixed Fibonacci frequency and support laws with the parity obstruction and quantified mixed density; it is not for the prime-power densities, local branch structure in itself, or CRT. The verified prior support results are substantial, and a same-day distinct index supplies the whole eleven-adic local frequency component already at proof level. None of the inspected stronger statements provides the parity-synchronized finite precision pushforward across both primes and the resulting mixed coefficient law without the additional finite-precision counts and synchronized support analysis.

## value

PASS

The attained residues and their frequencies are natural invariants of the classical Fibonacci orbit. The smallest shared period modulus in this two-prime family enforces a concrete correlation: separate large local ranges do not combine independently. The exact all-target finite counts, support cardinality and nonzero asymptotic deficit quantify that correlation, covering the regular and ramified branches without orbit enumeration. This is more informative than an arbitrary finite modulus example or a repetition of the local image densities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
