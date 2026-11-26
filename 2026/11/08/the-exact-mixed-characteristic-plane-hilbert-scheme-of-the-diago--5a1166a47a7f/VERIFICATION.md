---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The change from the six X_i to the five y_i with sum zero and the cone coordinate t is invertible over Z_2 because 5 is a unit. Exact expansion gives F_S − 6tE_2 − 120t³. The smooth special surface forces every cone plane to contain the vertex. For each corresponding line, the two normal derivatives are squares of independent linear forms: their lack of common zero is smoothness along the line. Their products with the three plane coordinates give six independent cubic monomials, so the special plane scheme is reduced. The exact finite line census was independently reproduced (357 lines over F4, 27 on the surface, 15 fixed and 12 nonisotropic). One can also see why isotropy characterizes the fixed lines: write W for the sum-zero five-coordinate space and B for its symplectic dot form; a contained F4 line L satisfies L^(2) = L^⊥ by the four coefficients of the Hermitian restriction. Thus B-isotropy is equivalent to Frobenius stability. For a lift to W_2 choose base representatives of the vertex with y=0 and of the two line vectors with t=0, then allow arbitrary twice-linear changes. Modulo four the F_S variation, after division by two and reduction, is a sum of linear forms times u² and v², so cannot alter [tuv]; this coefficient from 2tE_2 is precisely B(a,b). A nonisotropic plane has no such lift. The fifteen distinct pairing sections exist integrally. Projectivity together with the finite special fiber gives finiteness: the locus of positive fiber dimension is closed and its proper image would contain the closed point if nonempty. Henselian splitting and the finite étale special algebra give each factor as a quotient of the corresponding unramified DVR (lift the separable residue generator, then apply Nakayama over the base); its ideal is either zero or (2^e). The section forces zero at each rational factor; the obstruction forces e=1 at each quadratic factor. Thus the ring decomposition holds without inferring it from a count of geometric planes. Independent replay at /workspace/branches/8d642a3f-0502-4ba8-9a16-73e49930992a/replay_record3.py and replay_output.txt also checked tangent rank six and a nonzero obstruction for an explicit F4 representative. This replay corroborates only the finite inputs and representative calculation, not the universal deformation and ring arguments.

## originality

PASS

Pass is for the mixed-characteristic local rings of the specified diagonal model, in particular the obstruction modulo four. The closest prior text already establishes the same model after completion, the same geometric fiber lengths and fields of definition, the reduced special plane scheme by the normal-derivative argument, and nonflatness. None of these are credited as new. Its proof of nonflatness does not compute vertical thickness. The explicit nonzero mixed cubic coefficient in the relative deformation distinguishes the present assertion from that prior result. No equivalent thickness computation was established in the inspected sources.

## value

PASS

The scheme is a natural moduli invariant of a classical degeneration. The exact integral thickness measures failure of the extra planes to persist even infinitesimally in mixed characteristic, information not captured by the 15-to-27 jump or a zero relative tangent space. The obstruction separates length one from all higher uniformizer lengths and therefore resolves a precise gap in the previous reduced-fiber calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
