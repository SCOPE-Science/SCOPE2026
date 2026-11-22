# Independent mathematical audit

## correctness

PASS

Reconstructed projection D_L from mutually orthogonal signed block contrasts h_t, R=I-2D and R1=1. Every real open-path signal is a constant plus its n-1 weighted unit jumps. The sharp variation operator norm therefore equals the maximum over jump images, not merely an experimental lower bound. A within-block nonmidpoint jump with a=2 min(q,L-q)/L produces 1+(2+c)a variation (c available active-block exterior ends); the exact midpoint yields 1+c. Maximizing q and active block yields C(L,b)=1+c_b at L=2, otherwise 1+(2+c_b)(1-2/L), with c_b=0,1,2 for b=1,2,>=3. One step attains each finite value, the universal supremum 5 is not attained at finite L. Inspected actual RESULT.md 9b2513e8a40e39de7df5e337b89f3651ca0cdcfc and verify.py blob 38d4160749e9d73a490313202cdd8f1dd1509fd0 in audited tree. Independently checked all 532 unit steps at even L=2..14 and b=1..4 with exact rational arithmetic. Those finite tests corroborate the all-L step reduction, not replace it.

## originality

PASS

Best-of-knowledge no encompassing published theorem found for the exact finite open-path BV norm of the one-level Haar sign involution with end-block distinctions. Broader Haar unconditionality and BV coefficient embedding results employ different norms or all-level transforms. The explicit c_b boundary law and finite sharp one-jump extremizers are not supplied by the checked prior statements. This is a qualified priority assessment, not evidence that all historical literature was indexed.

## value

PASS

The simple orthogonal Haar sign flip is a natural wavelet perturbation; its exact induced total-variation norm varies with physical open-path boundaries and converges to a sharp unattained 5. The precise b=1,2,>=3 transition, extremizer and finite-vs-asymptotic behavior quantify a nontrivial stability defect that cannot be inferred from Euclidean orthogonality. A reusable exact operator norm for all even block sizes is a motivated structural result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
