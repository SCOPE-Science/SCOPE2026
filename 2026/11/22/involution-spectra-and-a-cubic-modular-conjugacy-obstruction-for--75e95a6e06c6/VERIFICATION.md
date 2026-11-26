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

The characteristic ideal A² is the entire quadratic tensor space. Multiplication forces action F=g⊗g on it while the higher block h:V→V⊗V is arbitrary. Squaring this block-triangular map gives g²=I and Fh+hg=0; conjugating by a shear of block f translates h by fg−Ff. Thus with T(h)=Fhg the solution space is ker(I+T) and translations are im(I−T). In odd characteristic T is diagonalizable and translations exhaust that kernel. A negative sign on the three tensor indices arises from either one or all three negative factors, giving 3a²(n−a)+(n−a)³ and the GL block-diagonal centralizer. Independently in characteristic two, choose a basis of V consisting of r pairs swapped by g (each J₂ is similar to a swap), and s fixed vectors. The induced action on the basis of Hom(V,V⊗V) permutes triples, with exactly s³ singleton orbits and (n³−s³)/2 swaps. Each swap contributes a line to both the kernel and the image; a singleton contributes one kernel dimension and no image. This gives exactly e=(n³+s³)/2=s³+2rs(n−r)+rn², shear-orbit dimension n³−e, and q^{s³} shear orbits, all lifts linearizable by a shear iff s=0. In a basis ordered as im(g−I), singleton complement, and chosen preimages, commuting matrices have block form [[A,B,C],[0,D,E],[0,0,A]]. Invertibility is equivalent to invertible A and D, giving q^{r²+2rs}G_rG_s. The count includes identity and classifies only the stipulated fixed-linear-part shear orbits. Separately checked the n=2 totals: q⁸+(q²−1)q⁴ at q=2 is 304; 1+q⁸+q(q+1)q⁴ is 7534 and 409376 at q=3 and 5. Inspected the bundled source, finite rank checks and recorded results without running the frozen code; the all-field conclusion follows from the algebraic argument, not those prime-field samples.

## originality

PASS

The strongest inspected analogue is an anti-involution census on the same algebra. Its reversal-twisted representation changes both the exact count and the modular obstruction. The general shear/cohomology construction is standard, but the asserted ordinary automorphism counts and explicit cubic obstruction compare a distinct representation and were not covered by an inspected formula.

## value

PASS

The result computes an exact torsion invariant for a canonical free finite algebra family in both characteristic regimes and sharply specifies when identity-linear conjugation removes all higher terms. The number of surviving conjugacy orbits is cubic in the singleton dimension on a logarithmic scale, rather than a generic modular existence example. The separate ordinary and reversal-twisted counts are useful when choosing the symmetry notion for these algebras.

The dated certificate retains the supplied scientific assessment, sources and limitations.
