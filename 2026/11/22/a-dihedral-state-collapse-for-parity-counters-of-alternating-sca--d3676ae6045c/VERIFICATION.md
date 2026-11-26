---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The two integer reflections give exactly the alternating prefix-counter updates by Pascal and reflected binomial identities, including j=1 and t<0. In F2[[X]], (1+X)^L=1+X^L gives the required periodicity through every j<L. The empty word gives zero in all positive coordinates; 01 advances one residue. Lucas's mask at u=k distinguishes the half-period shift and all smaller candidate periods divide that half-period. Every pair therefore has a common distinguishing suffix of the form (01)^a. An independent linear-algebra check: on the full prefix vector the two letter maps are involutions I+A,I+B, with A,B supported on complementary entries of the first subdiagonal. R=(I+B)(I+A)=I+U has U with unit first subdiagonal. U^j e0 first becomes nonzero at index j, and the order of R and orbit size of e0 are exactly L by characteristic-two squaring. The second involution fixes e0, so the whole orbit is the rotation orbit. For a difference with leading coordinate j, the kth coordinate of U^(k-j) times that difference is one; consequently some power of R distinguishes the pair. This also checks the lower bound independently of Lucas. Inspected the supporting files without executing uploaded programs; independently ran the fresh replay for 10,230 direct subset-count comparisons and exact orbit/output distinguishability at 14 dyadic boundary lengths through 128. The finite checks supplement, not replace, the all-length proof.

## originality

PASS

Bounded best-of-knowledge assessment for the all-length minimal parity counter, not a priority claim for the counting recurrence or small lengths. The overlap at k=3 is known, and the indexed three-run parity family has no targets of length at least four with strict alternation. General counting representations do not compute the rotation orbit or prove minimality.

## value

PASS

A uniform, sharp streaming memory classification for a natural target family: 2^k candidate prefix patterns collapse to between k+1 and 2k actual states, with provably no further identifications. Two reflections and powers-of-two jumps explain why the natural periodic suffix is enough to distinguish states. This is considerably more than checking isolated examples or giving a general counter construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
