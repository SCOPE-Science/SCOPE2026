# Independent mathematical audit

## correctness

PASS

At the positive equilibrium the bracket vanishes; differentiating it using u₀(1−u₀)=β(u₀+α) gives A=αβ/(u₀+α) and the convolution coefficient −C=−u₀²/(u₀+α). For frequency k=2πj/L, integrate the periodized kernel over one period by unfolding to the real line; its multiplier is exp(−σk²). Hence λ_j=f_D(k²), f_D(z)=A−Cexp(−σz)−Dz. The zero mode is negative and high frequencies decay. Strict concavity reduces the phase diagram to the interior maximum at z*=log(σC/D)/σ for D<σC; its sign changes once as q=t(1−log t), t=D/(σC), increases from 0 to 1. W_{−1} solves the critical equation on 0<t<1. At criticality the only neutral lengths are those with some k_j²=z_c, and no mode grows. Below criticality the two positive roots follow by putting w=σ(z−A/D) into w exp(w)=−(σC/D)exp(−σA/D); the ordered branches give the two roots. A strict open gap exists between I_j and I_(j+1) exactly when j<k₋/(k₊−k₋), because both starts and ends increase. Equality gives an isolated neutral contact (no other interval covers it), and all later intervals overlap. This gives the ceiling formula, including ratios at or below one. For δ=D_c−D, put z=z_c+√δ v and divide f by δ. At δ=0 the continuation gives z_c−σD_cv²/2 with two simple roots in v; the implicit-function argument in √δ gives errors O(δ) in z. Taking square roots and the integer ceiling yields the displayed coefficient and bounded remainder. The rational example gives the scaled values 0,321,0 at z=9,10,16, so strict concavity forces the band (3,4); the given roots r/2 and 1/2 make the positive upper equilibrium homogeneously stable, and interval arithmetic gives exactly the two indicated gaps and the neutral contact at 2π. Independent replay /workspace/branches/be4f96ec-cab6-4d8c-bf9c-bb5546a7ce38/independent-check.md confirms the rational identities and gives N√δ=0.390,0.395,0.3957 at δ=10⁻⁴,10⁻⁶,10⁻⁸ for A/C=1/2 and σ=C=1, against coefficient 0.39580152… . The supplied script was inspected, not executed. Finite numerics do not establish the theorem; nonlinear stability is not asserted.

## originality

PASS

The Gaussian dispersion and continuous onset, and the idea of testing admissible discrete modes, are prior inputs. The surviving distinct part is the exact all-circumference strict-return census (including contacts), its sharp accumulation coefficient, and the exact admissible realization. The reviewed primary results do not give an all-length gap census or its critical count for this model, nor a stronger count theorem from which those are supplied by substituting parameters.

## value

PASS

Checking that some mode grows at a fixed length misses the repeated, bounded intervals of strict stabilization as length is varied. The exact count, isolated threshold contacts, and the unbounded near-onset growth with its sharp coefficient quantify those interruptions for a natural controlled habitat-length sweep; the admissible exact example shows they actually occur without relying on numerical near-zero signs. This does not claim ecological field validation or nonlinear patterns.

The dated certificate retains the supplied scientific assessment, sources and limitations.
