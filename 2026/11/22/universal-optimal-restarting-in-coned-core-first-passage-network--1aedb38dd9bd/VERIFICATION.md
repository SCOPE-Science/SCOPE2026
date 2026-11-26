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

Reconstructed RESULT.md lines 33–70. With rates per edge, every core vertex has rate 1 to g and r to s, and g has aggregate rate m−1 into the core. Internal edges cancel from the class generator, so strong lumpability gives the same entire absorption law from s. Reset at s is a self-event. The finite killed system is transient since all states have a positive-probability path to a within a common finite time. Writing D=r²+(m+1)r+1, elimination gives G−S=(m+r)/D and (S−1)/(2+r)=1+(m+r)/D, hence S=r+4+(r+2m−1)/D, equivalent to the claimed mean and giving S(0)=2m+3. Differentiation independently gives D²+D−(r+2m−1)D′ as the numerator. For m≥3 its coefficients change sign once, the value at 0 is negative and the value at √2 is m(3+2√2)+11+8√2>0, proving a unique global minimum in the stated interval. At the root, F/m² tends uniformly to r²−2 on the interval. The 1/m coefficient of F/m² at √2 is 2√2+3; implicit differentiation gives the claimed rate correction. The mean's 1/m coefficient at fixed r>0 is −1−3/r−2/r², and its leading term is stationary at √2; this gives the stated optimal mean correction. An independent exact full-generator check compared H empty and H=K₂ at m=3,r=1/2 and found mean 161/26 and Laplace transform 3258/9767 at z=1/3 in both cases (replay: evidence/3/full_generator_check.py with Python and SymPy; observed output: evidence/3/full_generator_check.out). This checks those instances, not the universal quantifier. The frozen verify.py was inspected, not executed.

## originality

PASS

Strong lumpability and the general Poisson-restart identity are known. The supported distinct result is the exact finite-m optimizer and large-core expansion for this marked, per-edge-rate network, made uniform over arbitrary internal cores by the class generator. The closest catalogue theorem on the same clique-tail graph resets at a different vertex and actually has the opposite small-rate conclusion at length three.

## value

PASS

The coned core is a natural motif for separating internal complexity from excursions into a trap: every core vertex has the same exit rate despite arbitrary interconnection. The valuable part is not merely applying lumpability to a finite graph. It gives a uniform comparison between linearly diverging unrestarted means and bounded optimally restarted means, with a unique finite-core rate and first corrections. The same unmarked clique-tail topology can instead disfavor restart when the reset vertex is moved to the gateway, making the dependence on the marked dynamics scientifically useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
