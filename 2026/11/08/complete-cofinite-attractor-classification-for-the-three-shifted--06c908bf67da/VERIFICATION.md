---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For odd composite n>=29, EulerPhi(n)<=n-sqrt(n), giving strict one-step descent; for prime p>=29, F(p)=p+2, and if p+2 composite then F²(p)<p, while for twin primes p,p+2, 3|p+4 gives F³(p)<p. Thus repeated strict descent at block endpoints reaches odd states <=27. The displayed 13-node finite transition table has exactly cycles 9, (11,13,15), (23,25). To classify full basins, every preimage of an exceptional cycle input s solves EulerPhi(m)=s-3. The rigorous lower bound EulerPhi(m)>=sqrt(m/2) for all m means all preimages for s-3<=30 lie below 2*30²=1800. An independent sieve enumerated *every* m<=1800 with totient in {0,1,2,4,6,20,22,26,28,30} and reproduced the ten exact source inverse rows. Reversing the arrows exhausts E1={1,2,3,4,5,6,7,8,9,10,12,14,18} and E2={23,25,29,31,33,44,46,50,58,62,66}, with no additional preimages; 66 is largest exception, hence 67 sharp. All n<=200000 checked independently. The all-positive-integer conclusion uses inverse-totient cutoff plus descent, not the finite 200000 test.

## originality

PASS

The October 13 and 18 published shift-three theorems already prove *all three periodic cycles* and the sharp 25 absorbing endpoint; those are expressly credited, not called novel. The prior October 18 finite verifier tabulates basin counts through 10^6 but its theorem does not exclude larger exceptional inverse chains. The submitted contribution is the unrestricted exact exceptional basin sets (13 and 11 values), cofinite 3-cycle basin, and sharp first universal threshold 67 from a proven inverse-totient cutoff. The OEIS inverse-totient sequence explicitly lists much of the requisite finite preimage table, but does not formulate or prove the dynamical exhaustive predecessor-closure theorem. The independent sharp basin result survives, with known-table-deduction residual risk.

## value

PASS

A natural complete global basin classification for a nonlinear arithmetic dynamical system. Known eventual-cycle results and even numerical basin counts do not establish the exact number 24 of exceptional starts or the universal n>=67 threshold. A proven finite inverse-totient cutoff gives a reusable technique for converting known attractors into globally exact basins; the sharp exceptional set is an exact, independently useful invariant, not an arbitrary finite slice. Its elementary dependence on known tables is acknowledged.

The dated certificate retains the supplied scientific assessment, sources and limitations.
