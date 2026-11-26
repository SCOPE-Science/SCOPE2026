# Independent mathematical audit

## correctness

PASS

With the counting inner product and indexed atoms, the frame operator entry at difference s is the cyclic autocorrelation at s multiplied by 1+χˢ, where χ=exp(2πik/N); this follows by summing the translated entries at fixed difference. The diagonal is 12 and the nonzero lag indices ±1,…,±5 are distinct for every N≥12, so the positive-lag conditions are exactly (1+χˢ)r_s=0 with aperiodic r_s. Because r₅ is a unit phase, χ⁵=−1 leaves orders two or ten. In the order-ten case normalize g₀=1 and name the rest A,B,C,D,E. Lag four gives E=−DA and lag one gives u+v+w=0 for u=B/A, v=C/B, w=D/C. The unit triple is equilateral, so uvw=u³ and |v−u|=√3. Lag three now gives Au(v−u)+u³=0, which cannot hold by unequal moduli. Thus χ=−1, N even, k=N/2. At that gap the even-lag constraints are the sum of the two length-three aperiodic autocorrelations. After dividing out first-tap phases, using x as the first triple's middle phase, and scaling by the common phase ramp x, the second middle and first last phases h,t satisfy 1+h+t(1−1/h)=0 with |h|=|t|=1. This excludes h=1, then forces |1+h|=|1−h|, h=±i and t=−1. It gives exactly (a,b,ax,±ibx,−ax²,bx²); inverse parameters are read from the first four taps, so both tori are disjoint and the parametrization is one-to-one. The q-phase condition is i∈μ_q and a,b,x∈μ_q, giving 2q³ only when 4 divides q and the required gap exists. Frozen CHECK_EXACT.py, CHECK.py and their two logs are supplementary replay paths; their alphabet tests do not prove the continuous exclusion, which is symbolic. Uploaded checkers were inspected, not executed.

## originality

PASS

The known finite-Gabor criterion and the length-three quaternary Golay census are not new. The substantive remainder is the across-N, continuous-phase exclusion of the alternative order-ten gap, together with an exact classification at the remaining gap as a single theorem. The prior general frame criterion reduces order ten to four lag zeros but does not make them inconsistent. A canonical Huffman formulation captures precisely those zeros, but the inspected constructions are not a classification of constant-modulus length-six sequences, and the closest polyphase sequence paper reports numerical minima, not exact exclusion. The inspected quaternary census cannot by itself classify other alphabets or continuous phases.

## value

PASS

In full-translation two-channel design the highest lag leaves a genuine alternative modulation order, so assuming antipodality from the quaternary Golay slice would not answer the problem. The equilateral-triple obstruction settles that alternative uniformly over the unit circle and every cyclic order in scope. Combined with the explicit admissible windows, it provides an exact design test and alphabet count rather than a re-enumeration of the known quaternary case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
