---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

For fixed q>=2, count each palindrome-prefix/suffix split s to get at most (m+1)q^(ceil(m/2)+1) admissible length-m targets. At odd m, each of m cyclic-reflection cut classes has exactly q^((m+1)/2) words. A primitive word cannot occur under two distinct reflections, since their composition is a nonidentity rotation; at most m q^(m/3) words are nonprimitive, as any proper period divisor of odd m is <=m/3. Hence |P_{q,m}|>=m(q^((m+1)/2)-m q^(m/3))=Omega_q(m q^(m+1)/2) for sufficiently large odd m. For any target w, X counts its M=N-m+1 possible starts. Overlapping simultaneous hits at shift d<m have probability <=q^(-m-d), and nonoverlapping hits are independent; E X^2 <= mu^2+mu(1+2/(q-1)), mu=M q^-m. Paley-Zygmund/Cauchy-Schwarz yields P(X>0)>=mu/(mu+1+2/(q-1)), with union upper bound min(1,Nq^-m). Summing target counts above/below h=floor(log_q N) gives O_q(sqrt N log_q N), and choosing the largest odd m<=h gives matching Omega, covering all large N and both parities of h. A newly written direct checker (not imported from repository) enumerated q=2 odd m=3,5,7,9,11 and q=3 odd m=3,5,7,9, plus exact q=2,N=4..7 and q=3,N=4..6 random-host expectations and occurrence inequalities. These finite tests corroborate, but do not substitute for, the general proof. No substantive correctness gap found.

## originality

PASS

A best-of-knowledge novelty survives for the expected number of distinct P^2 factors within a uniformly random host: Kemp/Guo already establish language counts and split structure, Rubinchik--Shur prove single-palindrome (not two-palindrome) random expectation, Borchert--Rampersad deterministic extremes, and Duchon--Nicaud--Pivoteau alpha-gapped patterns. None of the checked applicable statements alone determines Theta_q(sqrt N log_q N) for the P^2 host statistic, and no broader universal occupancy theorem was identified. The probabilistic occupancy argument is simple and conceptually related to standard techniques, and potential historical priority from inaccessible Kemp and unidentified sparse-language theorems remains an explicit risk. A full novelty guarantee is not asserted.

## value

PASS

The quantity is a natural extension of palindromic richness: count distinct contiguous factors of a random word that have palindromic length at most two. The result identifies a genuine log N increase over the known Theta(sqrt N) behavior of single palindromes. The explanation is structural: odd-length primitive necklace/reflection cuts contribute a linear-in-m multiplicity of allowable words, and overlapping-hit control translates this to realized random-host distinctness. It holds for every fixed alphabet q>=2 rather than an arbitrary tiny slice. It is an order theorem, not a sharp coefficient, and its straightforward second-moment methods limit depth, but the unknown exact natural growth order is a useful standalone fact beyond reprinting the Kemp census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
