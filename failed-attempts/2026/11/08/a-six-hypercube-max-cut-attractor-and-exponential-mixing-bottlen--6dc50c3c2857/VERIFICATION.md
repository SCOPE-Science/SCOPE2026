---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The 2n+1 closed-neighborhood rule makes a vertex flip iff >=n of its 2n neighbors agree with it, exactly the non-decreasing-cut condition. The cut functional 2n(x+y+z)-2(xy+xz+yz) is multi-affine; its maximizers are precisely states with two monochromatic opposite parts and the third free. A sweep makes A unanimous and B opposite in <=2n permitted flips, yielding a path from any state. The six n-cubes intersect in six nonconstant monochromatic junctions, giving 6(2^n-1) recurrent states; all neutral flips are reversible, making uniform pi stationary. Two endpoints yield precisely 2n outgoing directed flips from a chosen face; Q/pi(F)=2/(3*2^n). The TV bound via pi(.|F) and a crossing union bound gives t_mix(1/4)>floor(3*2^n/4); n=2 stationary face mass bound also holds. Hypercube edge count gives local activity 2^n/[3(2^n-1)]. Independent maxcut enumeration confirms recurrent candidate size 18,42,90 for n=2,3,4. A finite check is not the all-n proof.

## originality

FAIL

Decisively covered in principal structure by a full-text earlier Resultary theorem (published 2026-10-26) for the IDENTICAL stochastic closed-neighborhood minority process on the IDENTICAL balanced K_{m,m,m}. It already proves the single connected recurrent class, 6(2^m-1) states, six hypercubes glued at six junctions, uniform stationary law and an exponential TV mixing bottleneck. The new 2n versus 3n reachability path, 0.75*2^n versus 0.5*2^n lower-bound coefficient, and stationary flip-rate count refine existing elementary counting and do not rescue the already-covered core. This is direct implication, not merely matching titles.

## value

FAIL

The natural six-cube recurrent geometry and exponential mixing bottleneck are significant ideas, but these exact ideas have already been established in the same model. The modest constant strengthening in a lower bound and reducing a constructive flip path from three to two sweeps are elementary local refinements of the known face-flux argument, not a substantively motivated standalone improvement. Stationary flip rate follows by edge counting in the known hypercube union.

The dated certificate retains the supplied scientific assessment, sources and limitations.
