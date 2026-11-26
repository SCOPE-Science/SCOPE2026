# Independent mathematical audit

## correctness

PASS

The open-state conjugacy is exact: for g(z)=Φ(z)-1/2, the update in the normal coordinate is z-a g(z). Strict decrease of q(u)=g(u)/u=∫₀¹φ(su)ds gives pointwise strict decrease in amplitude off zero for a<=2/φ(0); continuity excludes a positive limiting amplitude. At criticality the cubic term is +z³/3 after the linear term -z. Squaring yields v_next=v-(2/3)v²+O(v³), whose reciprocal increments tend to 2/3 as long as v never vanishes. This gives the two critical constants, with precisely the stated finite-hit exception. Adding the two displacement equations forces opposite points, and a q(u)=2 gives uniqueness iff a>a_c. The return multiplier is (1-aφ(u))². Along the branch aφ(u)=2/[∫₀¹exp(u²(1-s²)/2)ds] decreases strictly from 2 to 0; this gives stability, monotonicity on either side of the zero, and unique superstability. The expansion of q gives u²~6(a-a_c)/a_c. At large gain the exact identity a/4-u=(a/2)(1-Φ(u)) first gives u/a→1/4, then Mills' ratio gives a/4-u=O(φ(u)), hence φ(u)/φ(a/4)→1; substituting back yields all three stated constants. An independent bracketed solve using the series for the integral of exp(-t²) gave u_s≈1.399985276878204 and a_s≈6.678663688751936. The supplied checker was inspected, not executed. The supercritical assertion is global uniqueness of the pair, but local attraction; no broader basin conclusion is needed.

## originality

PASS

The normal-quantile family is within a known shift construction, and the logit all-gain diagram is a close qualitative analogue. The probit theorem adds its exact critical relaxation coefficient, all-gain multiplier and unique superstable gain, and Gaussian rather than logistic tail and multiplier constants. None of the strongest inspected statements implies those results under its own hypotheses. This assessment is evidence-bounded, not a priority certification.

## value

PASS

An exact quantitative response law for the natural normal-quantile counterpart of the established logit model: the oscillation remains locally stable at every supercritical gain yet becomes almost neutral on a Gaussian scale, with an explicit unique gain of fastest linear relaxation and a sharp law at the flip. These distinctions are relevant when comparing feedback strengths and distributions, beyond a generic flip assertion. The value is for the deterministic map and its stated stability notions, not applied performance or a global supercritical classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
