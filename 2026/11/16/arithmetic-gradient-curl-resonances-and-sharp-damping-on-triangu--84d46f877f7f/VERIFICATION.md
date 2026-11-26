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

Independently label the vertices b_j=2j, t_(j+1)=2j+1. The vertex Laplacian is that of the square of C_(2n), with shifts ±1 and ±2. For the chosen face orientations the face Gram matrix is 3I minus adjacency of the weak dual cycle C_(2n): each plus face shares just D_j and V_j with two minus faces, with opposite incidence signs. Thus for a (2n)-th root w=e^{it} the respective spectra are 4-2cos(t)-2cos(2t) and 3-2cos(t). Pair the modes t and t+pi to obtain the claimed bands including even-n degeneracies. The vertex Laplacian has just one zero; the face Gram matrix is strictly positive. Since B1 B2=0, the full edge operator then has a one-dimensional harmonic complement. The cellwise tuple (T,B,V,D)=(2,2,-1,1) gives a harmonic vector with nonzero circulation along a rail. The smaller nonzero-sector gradient branch decreases strictly with c, attains g_n at j=1,n-1, and g_n<=g_3=4, the remaining trivial-sector gradient eigenvalue. The curl minimum is 1. Equalizing a*g_n and 2-a uniquely optimizes their minimum. Directly g_6=3-sqrt(3)>1; cos(pi/7)>43/48>(sqrt(21)-1)/4, so g_7<1; g_n decreases and has the claimed n^-2 asymptotic. In doubled-cycle coordinates, a face eigenvalue of 4 requires w^2+w+1=0, while a vertex eigenvalue of 5 requires w^4+w^3+w^2+w+1=0. Since 3 and 5 are odd, their respective primitive roots occur iff 3 or 5 divides n. The opposite sectors supply the anchors from w=-1 for gradient 4 and curl 5. A shared eigenvalue acts by one scalar in both sectors, so scalar separation is impossible there. No converse excluding other shared eigenvalues is stated. Independent sorted-simplex incidence replay (evidence/5/reproduce.py and replay.txt) supports these calculations for n=3..26 but is not the all-n proof.

## originality

PASS

The Hodge split, harmonic count and ordinary circulant spectra are established inputs. The directly supported contribution is their joint weighted gap design and the precise two anchored cross-sector coincidences on the specified annulus. Neither the analogous cycle gain optimization nor the general Hodge filtering framework covers these joint claims in the inspected sources.

## value

PASS

On a natural periodic simplicial mesh, the exact design weights and the size at which the preferred damping sector reverses give an actionable sharp relaxation bound. The two intersection tests address a distinct exact filter-design question: 4 and 5 are not arbitrarily chosen test numbers, but values anchored in the respective sectors by the w=-1 doubled-cycle mode at every size. The arithmetic gives infinite explicit failures of scalar separation while not claiming failures are confined to them. Value lies in the joint design and obstruction, not in carrying out a routine Fourier diagonalization in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
