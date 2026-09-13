# Aut(O2): naive metric incompleteness and CLI-ness question (local analysis)

## Naive left-invariant metric
Fix dense sequence (a_n) in unit ball of O2. On End(O2) (unital *-endomorphisms,
point-norm topology) define
  d(phi,psi) = sum_n 2^{-n} ||phi(a_n)-psi(a_n)||.
This metrizes point-norm topology; on Aut(O2) it is left-invariant because every
gamma in Aut(O2) is isometric:
  d(gamma phi, gamma psi) = d(phi,psi).
(End(O2),d) is complete: pointwise limit of *-homomorphisms is a *-homomorphism.

## Proper-endomorphism limit (conditional on Kirchberg-Phillips uniqueness)
Let s1,s2 be canonical generators of O2 and phi(x)=s1 x s1^*+s2 x s2^* (canonical
shift). phi is a unital injective *-endomorphism with proper range (s1,s2 not in
range). By Kirchberg-Phillips uniqueness for embeddings of O2 (every unital
*-homomorphism O2 -> O2 is approximately unitarily equivalent to any other),
there are unitaries u_n in O2 with Ad(u_n) -> phi pointwise. Each Ad(u_n) is an
(inner) automorphism, so (Ad(u_n)) is d-Cauchy in Aut(O2) with limit phi outside
Aut(O2). Hence the naive metric is incomplete on Aut(O2).

## Consequence
Incompleteness of one left-invariant metric does NOT prove Aut(O2) is non-CLI
(CLI asks existence of some complete compatible left-invariant metric). So:
- Positive route "H=Aut(O2), f=id" is blocked: cannot certify CLI-ness, and
  heuristic evidence (Rokhlin dense conjugacy class, turbulent-group conjectures)
  points against Aut(O2) being CLI.
- Ruling Aut(O2) non-CLI from scratch would need a topological obstruction
  (e.g. turbulent-group => non-CLI, or Baire-category game in the left
  completion), which is itself a research-level lemma requiring references.
- Any other explicit CLI host (H,Y,f) would need Borel invariants separating
  conjugacy classes despite K_*(O2)=0 and approximate innerness; no candidate.

Status: positive route blocked; negative route is the credible one but needs
external exact statements (see WORKLOG Route A).
