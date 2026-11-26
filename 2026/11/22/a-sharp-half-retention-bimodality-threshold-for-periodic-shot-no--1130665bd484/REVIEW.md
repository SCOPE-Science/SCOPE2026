# Independent mathematical audit

## correctness

PASS

For deterministic gaps, the Laplace factor in Wang–Zhang is q(s)=exp(−sγw)=q^s and the renewal rate is 1/w, giving the exact claimed weights and MFPT normalization. Independently, if f(y) is the remaining mean jump count at scaled signal y≤x, first-step conditioning gives f(y)=1+exp(qy)∫_{qy}^x exp(−u)f(u)du. The entire series f(y)=1+∑_{n≥1}(x^n−(qy)^n)∏_{j=1}^{n−1}(1−q^j)/n! satisfies f′=q(f−1−f(qy)) and f(x/q)=1; integrating this identity recovers the first-step equation. The latter is a contraction on bounded functions on [0,x]. For the shape theorem, the sign of a_{n+1}−a_n is that of F_n−1, with F_n=q^n[(n+2)−(n+1)q], F_n−F_{n+1}=(n+2)q^n(1−q)^2, F_n→0, and F_1−1=(2q−1)(1−q). Include the initial ratio C_1/C_0=x: for q≤1/2 all ratios are nonincreasing, including at the boundary q=1/2; otherwise log-concavity already fails at index 2. In the open reciprocal window, away from ties, the ratios yield consecutive signs +,−,+,− for C_{n+1}−C_n, hence exactly two strict maxima at 1 and at least 3. The individual equality thresholds with C_1 grow to infinity, so their minimum over n≥3 is attained. At 1/M, C_2<C_1 and no subsequent ratio exceeds 1; at 1/a_1, C_3>C_2=C_1. These give the strict bounds and exclude index 2 and index 0 at the first global transition. Inspected frozen VERIFICATION.md and proof_check.py without executing the uploaded script; the proof controls all indices, not just its checked window.

## originality

PASS

The exact coefficient and ratio are prior; the inspected closest results do not establish the finite-threshold mode classification or its first nonadjacent global transition. The conclusion is bounded by the inspected literature and index.

## value

PASS

At deterministic arrivals the retention has a direct physical meaning and the dominant summands are the terms used to analyze or sum the exact MFPT. A sharp cutoff for log-concavity, an explicit two-peak window and a nonadjacent first global-mode switch identify where single-peak intuition for that sum fails. This is useful without implying any bimodality of the physical hitting index or a quantified approximation error.

The dated certificate retains the supplied scientific assessment, sources and limitations.
