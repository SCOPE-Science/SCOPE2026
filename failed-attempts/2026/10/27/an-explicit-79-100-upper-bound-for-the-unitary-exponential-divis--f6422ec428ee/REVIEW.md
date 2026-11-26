# Independent mathematical audit

## correctness

PASS

Multiplicativity and the exponent-one sign yield a genuine prefix majorant R and positive tail majorant Z. Finite cylinders and their endpoint conventions are correct by CRT. For fixed k, write Z^k as a product of 1+alpha_p 1_{v_p=1}, alpha_p=(1+1/p)^k-1. In empirical averages, a term for a set of primes is bounded by the product of alpha_p/p using the count of multiples of their product; even with a cylinder indicator the contribution of terms meeting primes above Y is at most exp(S_k)(exp(sum_{p>Y}alpha_p/p)-1). This tends to zero uniformly. Finite-prime CRT and this bound justify the cylinder-weighted infinite moment and Markov bound without any continuity assumption on Z. Strict Z<1/q_i gives the strict reverse comparison. For density existence Trudgian §4 cites Erdős–Wintner for the positive comparison. Independently, the CRT log-ratio model converges in distribution: tail exponents ≥2 occur with probability O(sum_{p>Y}p^-2), and the positive exponent-one log tail has expected value bounded by the same sum. The model is non-atomic: on finite blocks of primes >Y≥3 conditioned on exponents 0 or 1, products of (p+1)/p for different subsets are distinct by the greatest differing prime. Their maximal point mass is at most the product of p/(p+1), tending to zero as the block grows; the omitted higher-valuation event has probability O(sum_{p>Y}p^-2). Independence of the other primes and then Y→∞ give both strict densities. The independent replay matched all required exact arithmetic for L and 100N-21den=7112052632825517341269506617745901663335169421629440000>0; replay source and output are /workspace/branches/5e365845-1233-4b85-82bc-b62d817857cf/replay_record5.py and replay_output.txt in that directory. The arithmetic alone does not prove the tail argument or an exact density value.

## originality

FAIL

The earlier indexed 2026/10/18 result directly bounds the same strict positive comparison by 0.779672276<0.79, even for upper asymptotic density, and proves a larger lower bound for the same strict negative comparison. The assigned arithmetic certificate is valid, but changing its construction or producing a different exact rational does not make the dominated scientific claim distinct.

## value

FAIL

The density problem is meaningful and the computation is reproducible, but both final quantitative claims are weaker than existing rigorous bounds for the same events. A different small-prime/high-moment implementation might be useful if it yielded a substantive performance or mathematical result; no such claim is established in this record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
