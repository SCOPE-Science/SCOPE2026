# Parity-stable inversion of cyclic Rule 90 on Lucas-constrained inputs

## Finding

Let \(A_n\) be the indexed binary words of length \(n\ge2\) that avoid neighboring ones, including across the cyclic boundary. Apply synchronous Rule 90, \((\Phi_n x)_i=x_{i-1}+x_{i+1}\) over \(\mathbb F_2\), allowing unrestricted intermediate states. Put \(I_{n,t}=\Phi_n^t(A_n)\) for \(t\ge0\). Let two sources be equivalent at time \(t\) if their time-\(t\) outputs agree.

If \(n\) is odd, all these equivalence classes are singletons and the image sizes are constant. If \(n\) is even, set \(s=v_2(n)\) and \(T=2^{s-1}\). The image size drops strictly at **every** step from \(t-1\) to \(t\) for \(1\le t\le T\), and is constant for \(t\ge T\). The source equivalence classes themselves cease changing at exactly \(T\). In particular the first-step partition persists forever at lengths \(2\bmod4\), whereas at every length divisible by four the first step is followed by at least one further strict coarsening.

## Assumptions and scope

The sites are indexed and no spatial symmetry is quotiented. The neighbors are counted by their two positions in the formula, so at \(n=2\) they coincide and cancel. The condition on adjacent ones restricts the starting word only. Stabilization refers to image **sizes** and to equivalence classes of sources, not to equality of the sets of output words at successive times.

## Proof

Identify a configuration with its coordinate polynomial in \(\mathbb F_2[z]/(z^n-1)\). Rule 90 is multiplication by \(z^{-1}(z+1)^2\). Write \(n=2^s u\) with \(u\) odd; \(z^u-1\) has a simple root at 1, and hence \(z^n-1\) has root multiplicity \(2^s\) there. In the quotient by a polynomial \(g\), the kernel of multiplication by \(f\) consists of multiples of \(g/\gcd(f,g)\): divide by the common factor and use coprimality. Therefore the time-\(t\) kernel, including \(t=0\), has dimension \(\min(2t,2^s)\) and the kernels are nested in time. For odd \(n\), the positive-time kernel is exactly \(\{0,1^n\}\). Two different admissible inputs could agree in output only if they were complements. This would force cyclic alternation (neither `00` nor `11`), impossible at odd length.

For even \(n\), the kernel stabilizes at \(T=2^{s-1}\), so no further source classes can merge after time \(T\). To see that no step through time \(T\) is lost by the source restriction, put \(M=2^s\). For each \(1\le t\le T\), take the length-\(M\) word with polynomial
\[
       w_t(z)=(z+1)^{M-2t},
\]
and repeat the word \(u\) times to obtain an indexed length-\(n\) word \(x_t\). The exponent \(M-2t\) is nonnegative and even, so \(w_t\) is a polynomial in \(z^2\). Thus \(x_t\) is supported on even positions and is admissible. The periodic repetition map from length \(M\) to length \(n\) is injective and intertwines Rule 90, since it simply repeats the local cyclic neighborhoods. On the shorter ring \(z^M-1=(z+1)^M\). The product of \(w_t\) with \((z+1)^{2t}\) is zero there, whereas its product with \((z+1)^{2t-2}\) is \((z+1)^{M-2}\), nonzero. Unit shifts do not affect these conclusions. Consequently \(x_t\) and the zero word have distinct time-\(t-1\) outputs and identical time-\(t\) outputs. Since applying an update cannot separate already equal outputs, this is a strict decrease in the number of distinct outputs at every stated step. The proof includes \(M=2\) and exponent zero.

## Verification

The theorem is established by the polynomial proof and the admissible witness for each step. The standard-library `CHECK.py` exhausts the admissible initial words for \(2\le n\le16\), counts outputs through two steps beyond the predicted stabilization time, and verifies the witnesses separately for every asserted strict step in this range. The finite computation is corroborative only.

## Relationship to prior work

The additive Rule 90 kernel on unrestricted indexed states is classical; see Miller and Bardzell, §3, Corollary 5, for the one-step two-versus-four predecessor count. For comparison with the all-state time boundary, *Sharp mod-four stabilization and zero-mode rank dichotomy for permuted Rule 90 rings* includes the unrestricted first-versus-second rank dichotomy with the identity permutation. That result alone cannot guarantee strict loss from a restricted source at any particular step. The point here is the exact duration of strict information loss on cyclic no-`11` sources, witnessed at **each** increasing kernel stage by a word in that source language. The one-step constrained inverse-fiber census is not claimed here: *Sharp separation threshold for lossless cyclic Rule 90 readout* gives it in the one-zero separation case for \(n\ge5\). The indexed cyclic source language is the one used for Lucas cubes by Mollard.

## Limitations

No count of the general time-\(t\) fiber sizes or of the magnitude of each strict loss is asserted. The argument does not cover other separation distances, sequential updates, or nontrivial permutations after each update. The comparison to earlier literature is bounded and does not certify historical priority.

## References

1. N. R. Miller and M. J. Bardzell, *The Evolution Homomorphism and Permutation Actions on Group Generated Cellular Automata*, Complex Systems 15 (2004), 121–136, §3. https://content.wolfram.com/uploads/sites/13/2018/02/15-2-2.pdf
2. M. Mollard, *Maximal hypercubes in Fibonacci and Lucas cubes*, arXiv:1201.1494. https://arxiv.org/abs/1201.1494
3. *Sharp mod-four stabilization and zero-mode rank dichotomy for permuted Rule 90 rings*. https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-sharp-mod-four-stabilization-and-zero-mode-rank-dichotomy-for-pe--39040a59fa6b
4. *Sharp separation threshold for lossless cyclic Rule 90 readout*. https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-sharp-separation-threshold-for-lossless-cyclic-rule-90-readout--b1a0513ff160
