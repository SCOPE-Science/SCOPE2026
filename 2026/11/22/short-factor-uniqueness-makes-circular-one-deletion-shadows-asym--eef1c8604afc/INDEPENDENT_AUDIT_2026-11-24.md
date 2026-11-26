# Independent mathematical audit

## correctness

PASS

For two equal deletion necklaces, align the outputs. Each presentation has n−ell intact starts among n−1 output starts, so at least n−2ell+1 positions are intact in both. Uniqueness makes their source starts identical. Cutting there gives equal linear deletions, which force all letters between the two deleted positions to agree. Conversely positions in one cyclic run give the same output. For the probability, the selected starts of the d-shift cannot contain a whole shift orbit: with g=gcd(n,d), the shortest cyclic interval containing a residue class has size n−g+1. In particular the order-two case cannot select an antipodal pair, so no undirected edge is counted twice. The ell constraints form a forest and their exact match probability is q^(−ell). The union bound under the same indexed-word coupling implies the TV estimate. The cyclic transition PGF is the trace of the nth power of (1−z)I+zJ divided by q^n; moving the constant-word atom gives R_n*. This also handles the repeated boundary edge at n=2. For n≥3 the indicators are pairwise independent, and n−1 path indicators are independent, yielding the stated moments and CLT; the coupling error transfers them at the claimed rates. The source checker was inspected, not executed: its deterministic loop omits ell=n/2 for even n despite the broader account in RESULT.md. The independently written /workspace/review_checks.py, argument 5, exhausted that boundary through n=14,8,6 for q=2,3,4 respectively (including n=2), with no failures. The proof, not the finite check, covers the full range. The exact PGF is for R_n*, not for D_n, and the source model is indexed uniform, not uniform over necklaces.

## originality

PASS

Pass for the general deterministic short-factor synchronization and its quantitative IID circular-shadow law. The traditional linear run identity, the binary circular maximum, and the de Bruijn special case are overlap, not the full claim. Priority is bounded by the available comparisons.

## value

PASS

The cyclic quotient creates real cross-run collisions, so a deterministic sufficient condition and quantitative transfer to an explicit finite reference law are useful for circular deletion models. The bound is stronger than the displayed polynomial-rate corollary if ell=floor(n/2) is chosen, but the result does not determine the sharp failure probability or exact D_n histogram. Distinct outputs, not their probabilities, are the relevant invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
