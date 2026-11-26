# Independent mathematical audit

## correctness

PASS

For the companion matrix A, A^4 is not I mod 13 and A^14 = −I mod 13, while A^28 = I mod 13; all proper divisors of 28 divide 4 or 14. Writing U=A^28=I+169B, the checked seed is B ≡ [[6,6],[6,7]] mod 13. For d>0, the coefficients of the higher terms of (U^d−I)/(169d) have valuation at least 2(j−1)−v_13(j)>0 for j>=2. Thus the unit test for a branch difference is (A^rB)_12 ≡ 6(P_(r+1)−P_r). Vanishing contradicts the Pell norm (P_(r+1)−P_r)^2−2P_r²=(−1)^r, since 6 and 7 are nonsquares mod 13. This proves exact valuation, for all r and for either order of u,v after swapping. Each branch is consequently bijective onto its seed coset at finite precision; the 28 seeds have four zeros and two of each other class. A scalar period forces P_T=0 and P_(T+1)=1 modulo the modulus, hence A^T=I; the matrix order mod 13 and the valuation at r=0 force the predicted divisor of T. The binomial bound also proves that this period works, including k=2. The all-level images give the closure and normalized measure 13/169, and periodicity gives infinitely many representatives. Independently, the recurrence-only replay in /workspace/branches/e657e1e7-49a8-41be-bfc9-eada841436a5/ recovered the seed mod 2197, all residue classes and counts at levels 2–6, return and prime-divisor reductions of the proposed period, and the valuation in 1120 bounded pairs. This replay did not use the frozen script and does not substitute for the proof at arbitrary precision.

## originality

PASS

Pass for the exact scalar support, stable fiber counts and their uniform branch explanation at 13, not for the Pell–Wieferich anomaly, the single-index divisibility law, or the recurrence period alone. The strongest relevant comparisons include balancing valuation and completeness results since balancing numbers are half the even Pell subsequence. A single-index valuation law can shorten the branch proof via the Pell addition formulas, but the sources inspected do not establish the scalar distribution across the even and odd branches, or the resolved multiplicities. This is a best-of-knowledge assessment with explicit access risk.

## value

PASS

13 is the first Pell–Wieferich obstruction, not an arbitrary numerical example. At this prime period stabilization at the first two levels does not tell how much scalar coverage is lost, whether further lifts are full, or how many indices realize any specified value. The result gives exactly this reusable local information, including the exceptional fourfold zero-coset fiber, and identifies the uniform noncancellation that prevents any new loss at higher precision.

The dated certificate retains the supplied scientific assessment, sources and limitations.
