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

PASS: On X0!=0 eliminate Q and transform to coordinates a=X1/X0, z=X2/X0-a², y=X3/X0-a³ to get hypersurface y²+z³=0; similarly on X4!=0. In char 3 the Jacobian ideal is (y,z³). The only points with X0=X4=0 are [0:1:0:0:0] and [0:0:0:1:0]; direct gradient rank is two at each, hence no omitted singular support. On the singular subscheme X4/X0=a^4 and b=a^-1,zprime=a^-4 z EXACTLY, no higher nilpotent corrections. That transition gives split symmetric nilpotent algebra with line bundle O(-4) and its square O(-8); the hyperplane ratio yields O_J(1)=π*O(4). Direct-sum Euler characteristics sum (4m-4j+1) to 12m-9; deg=12,p_a=10 and h0 formula follow by P1 cohomology. The global projective reduced CI is unmixed and integral on dense chart, with no extra surface at X0=0; its tangent parametrization matches it. Inspected exact finite-field verifier equations and independent symbolic chart/gradient reasoning; no use of finite rank checks as proof of the global algebra.

## originality

PASS

PASS best-of-knowledge: Aprodu–Farkas–Papadima–Raicu–Weyman arXiv:1810.11635 gives odd-characteristic Gorenstein/syzygy/normalization results for tangent varieties and covers the old CI-level component; its inspected Theorem 5.1 and jet-bundle Section 5.4 do not calculate the intrinsic Fitting/Jacobian singular scheme, global nilpotent twist or genus of this char3 quartic. Chipalkatti and Kurmann discuss coincident roots mainly characteristic zero, where derivative of z³ does NOT vanish. A published related transvectant CI theorem concerns odd-degree rational normal curves r>=7 over C and only local generic Jacobian cycles, not global char3 degree-four split thickening. Different characteristic-two chordal ribbon is also inapplicable. Historical specialist coverage remains a risk, but no stronger theorem implying this precise invariant was established.

## value

PASS

PASS: The Jacobian singular subscheme is a canonical geometric invariant, unlike mere equation renaming. Characteristic three kills the transverse cubic derivative and raises the local cusp singular-scheme length from 2 (ordinary characteristic) to 3. The exact degree-four twist of the nilpotent generator determines degree/genus/sheaf sections and is not inferable from reduced singular support or generic cycle multiplicity alone. A fully explicit wild-characteristic scheme structure is intrinsically useful, with no paper-size or arbitrary-dimension requirement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
