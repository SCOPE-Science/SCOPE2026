# Independent mathematical audit

## correctness

PASS

JR fails exactly if some outside candidate has q_n or more supporters among the uncovered voters. Given the columns of a fixed quota-exact committee, the uncovered set has at most n−q_n voters, and an outside candidate's uncovered count is binomial with that many or fewer trials. For p_n≤1/k+1/(4k²), the gap from its mean to q_n is at least n/(2k²), so Hoeffding gives exp(−n/(2k⁴)) per pair, with probability zero if there are no uncovered voters. Union-bounding gives the claimed simultaneous relation, also when m_n=k. The quota-column count is exactly binomial by independence. For x=q_n/n, Stirling gives (2πnx(1−x))^(−1/2) exp(−n D(x||p_n))(1+o(1)), with nD(x||p_n)→λ²/(2v_k) and x(1−x)→v_k; rounding contributes only O(1/n) to x. This proves the stated local constant. The quota count converges to Poisson at finite supply ratio, including zero; the simultaneous relation transfers both counts and the existence event. Bounding the count discrepancy by C(m_n,k) on the bad event and using the binomial factorial moment proves the claimed mean convergence. At diverging supply the binomial mean diverges and its variance is at most its mean. At fixed p≠1/k, positive relative entropy defeats polynomial supply. The supplied script checks only finite instances and numerical diagnostics; it was inspected, not run, and the proof does not rely on it.

## originality

FAIL

The distinct indexed record db3611093bd6 explicitly states the same quota-to-DR equivalence with exponential error and the same critical transformed-Poisson committee count and existence laws, in a moving-approval window that includes this one. This is demonstrable scientific overlap, not a finding about which record was first or its provenance. The explicit error in the frozen unconditional guarantee is weaker than the direct quantitative consequence of the earlier Elkind et al. JR proof, and the expectation and off-critical consequences do not leave a distinct substantial remainder.

## value

FAIL

The critical DR supply curve and transformed committee count are meaningful scientific objects, but those substantive outputs are already matched by the distinct indexed finding. The remaining unconditional error constant is weaker than a direct consequence of the existing JR argument; the mean follows by an elementary factorial moment and polynomially bounded error. The record does not leave a separate, useful quantitative advance to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
