# Independent mathematical audit

## correctness

PASS

Adding one in base b verifies the trailing-(b−1) interpretation of ν_b(n+1), including n=0 and composite b. The declared automaton advances on b−1 and resets on any smaller digit; its lasso starts with a transient positions and ends with a p-cycle. Its initial state is fixed by zero. All states are reached by a suitable string of maximal digits; two states merge only if their entire controller tails agree, since a suffix of t maximal digits tests the t-th entry of the tail. If i<j<a+p and the tails coincide, d=j−i is a period from i onward. Every eventual period of the p-periodic primitive tail is divisible by p (translation by d on residues modulo p would otherwise give period gcd(p,d)). For i≥a this contradicts 0<d<p. For i<a, transfer the p-period identity to every index from i by adding sufficiently many multiples of d to both terms; this contradicts minimal onset a. Thus there are exactly a+p states. With the input-alphabet prefix metric, a word's best state relabeling matches until the first arrival at a state by a different digit than an earlier arrival. Thus earliest conflict at the ℓ-th edge gives raw opacity 2^(1−ℓ), normalized by M_b=1/2, as in Allouche–Yao Theorems 1–2 (no conflict gives zero). For b≥3, 01 is a length-two conflict at the common reset state. For binary a>0 the reset destination is distinct from every advance destination and there is no conflict. For binary a=0 only state 0 can conflict; a one-arrival requires at least p ones since the previous reset or start. If a zero-arrival precedes it, at least p+1 edges are needed, and if the one-arrival comes first, at least one subsequent edge is still needed. 01^p realizes the bound including p=1. A period-p single 1 per period, a constant controller, and a nonperiodic initial entry followed by a constant tail realize all published levels as stated. For arbitrary Y the reviewed invariant is the input-prefix opacity of the intrinsic transition graph as explicitly scoped in RESULT.md line 18; no distance between Y-valued outputs and input digits is asserted. This proof is valid for the whole declared domain. The supplied finite checker and its counts were inspected as recorded evidence, not executed.

## originality

PASS

The retained contribution is the intrinsic size and complete base/onset/period classification of valuation-controlled words. Allouche–Yao's framework, the path criterion, the constant and period-doubling examples, and the generic DFAO minimization principle are prior. The adjacent catalog hits classify genuinely different inputs to these methods. No distinct full valuation-controller classification was verified in the bounded comparison.

## value

PASS

Valuation-controlled sequences extend familiar automatic words such as period-doubling. The exact minimization and opacity together explain how one transient segment can make a binary automaton transparent despite the same eventual period, whereas adding a second reset digit makes graph opacity maximal. The full infinite dyadic binary spectrum follows for even just binary-valued controllers. This is useful structural classification beyond any individual known example, within the input-prefix metric only.

The dated certificate retains the supplied scientific assessment, sources and limitations.
