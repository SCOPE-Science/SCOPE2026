# Independent mathematical audit

## correctness

PASS

PASS: In RESULT.md (3), the exact symbol is T/(1-exp(-Tp_j))-T/2-1/p_j, p_j=lambda+(2pi b^j)^alpha+i2pi b^j. For T=tau_N b^{-N}, j<=N-K has Tp_j=O(b^{-K}) and phi(z)=1/(1-e^{-z})-1/2-1/z=O(z), so its T^{-alpha} contribution vanishes; j>=N+K is bounded by O(b^{-alpha K})+o(1), allowing K→∞ after N→∞. For each fixed j-N=k, the T^{-alpha} symbol is zero at noninteger phase tau b^k and tends to (2pi tau b^k)^(-alpha) at integer phase. For 1<=tau<b no k<0 resonates, and first integer depth r uniquely maximizes the fixed-offset values. With tau_N=m/b^r+xi b^{-(1-alpha)N}, first-order expansion has real damping tau0(2pi)^alpha b^(alpha r) and imaginary detuning 2pi b^r xi; this proves the Lorentzian width exactly. Boundary tau=1 is handled only in the pointwise theorem, while boundary-layer theorem correctly restricts tau0 in (1,b). Independent direct scalar numerical calculations for b=2,3,4 and detunings 0,0.5,-1.5 reproduce 9 predicted values within 1.4e-5; finite checks do not prove the supremum limit. All claims require 0<alpha<1, lambda>0, geometric spectrum and pointwise tau; no uniform-in-tau convergence.

## originality

PASS

PASS best-of-knowledge: Castillo's Theorem 5.9 and Proposition 5.10(b) already prove O(T^alpha) and a matching dyadic lower bound for precisely the b=2 diagonal spectrum, so neither general convergence nor optimal exponent is novel. Their exact displayed bound at T=2^{-N} does not state or mathematically determine the every-mesh-ratio popcorn function, first-base-power denominator rule, or the two-sided detuning Lorentzian constant. The published continuous-frequency first-alias theorem explicitly assumes L²(R) multiplication and monotone continuous damping and has no sparse geometric radix discontinuity. Both are explicitly credited; no full earlier equivalent fine-phase computation was identified.

## value

PASS

PASS: The exact mesh-ratio discontinuity and its universal near-resonance layer identify where standard semigroup resolvent sampling attains or loses its expected normalized error, a natural stability/aliasing phenomenon for a geometrically discretized spectrum. Exact constants and detuning scale are distinct nontrivial invariants not implied by the prior sharp order, and are useful for phase-sensitive numerical analysis. No general arbitrary-generator or uniform-tau claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
