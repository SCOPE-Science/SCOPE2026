---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

C PASS: The full cyclic action on undirected K_n edges has precisely one orbit E_d for each chord distance 1<=d<=floor(n/2), and each dihedral reflection preserves E_d. Equal barycentric orbit masses therefore give equality—not just homotopy equivalence—of geometric C_n and D_n fixed sets. The union circulant G(n,S) is connected iff gcd(n,S)=1. For |S|>=2 its degree >=3 including the even antipodal edge case, and Watkins's connected vertex-transitive bound kappa>=2(degree+1)/3 makes it 3-vertex-connected; a coprime singleton is an ordinary cycle, not 3-connected. Hence fixed faces consist of gcd(n,S)>1 sets plus isolated coprime singleton distances. Cover the nonunit subcomplex by simplices for each prime p dividing n; all nonempty intersections are simplices with witness distance product of primes <=n/2. Its nerve is S^{omega(n)-2} for squarefree composite n and contractible for nonsquarefree composites; for primes it is empty. Adding phi(n)/2 isolated unit distances gives all claimed integral homology and n=30 first multi-degree H0=Z^4,H1=Z. An independent graph adjacency/reachability check enumerated all distance subsets n=4..11 and all deletions of <=2 vertices; this corroborates but does not prove general Watkins/nerve statements.

## originality

FAIL

O FAIL: A separately published stronger theorem 'An arithmetic jump in cyclic and dihedral fixed spaces of graph-connectivity complexes' expressly treats all three j=1,2,3, and its j=3 case is the exact full content of the assigned non-three-connected claim: equality of C_n/D_n fixed loci, gcd nonunit nerve plus phi(n)/2 isolated Hamiltonian orbits, prime-divisor squarefree/nonsquarefree homotopy and n=30 mixed-degree Betti numbers. It additionally gives j=1,2 cases and n=210. The two published records were added in the SAME reconciliation commit on 2026-11-17 02:18:15Z; no unsupported claim of earlier chronology, priority or misconduct is made. Nevertheless the current one-claim theorem is already wholly covered mathematically by that stronger published statement, so proof variants and stand-alone verification do not constitute an original surviving result. No disclaimer repairs this coverage.

## value

PASS

V PASS: Geometric full-group fixed loci of classical graph-connectivity complexes have a natural equivariant-topological motivation; their full integral homotopy classification and first mixed-dimensional reduced homology at n=30 are meaningful and nontrivial, even though the same mathematics is already published in a stronger three-connectivity-threshold result. Value and correctness do not repair originality failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
