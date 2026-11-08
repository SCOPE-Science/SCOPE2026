# Sharp binary four-window permutation-burst spheres and their six extremizers

## Finding
For every integer \(n\ge4\), the largest possible number of distinct outputs of a single length-four substring-permutation operation on a binary word is exactly \(3n-6\). Exactly six binary input words attain it: the length-\(n\) prefixes of the four infinite periodic sequences with period-four blocks `0011`, `0110`, `1100`, `1001`, and the two alternating sequences with period-two blocks `01`, `10`. The operation permits every permutation of the four symbols, including the identity; it acts on exactly one contiguous four-position window.

## Assumptions and scope
Let \(\mathcal X_n=\{0,1\}^n\), \(n\ge4\). For \(x\in\mathcal X_n\), define \(\mathcal P_4(x)\) as the set of binary words \(y\) for which there are an index \(i\in\{1,\ldots,n-3\}\) and a permutation \(\sigma\in S_4\) such that the block \((y_i,\ldots,y_{i+3})\) equals the rearrangement of \((x_i,\ldots,x_{i+3})\) specified by \(\sigma\), with all coordinates outside the block unchanged. Set \(B_4(x)=|\mathcal P_4(x)|\). The identity output \(x\) is counted once. Neither cyclic wraparound nor multiple operations is permitted. For a binary word \(u\), write \(w(u)\) for its number of ones.

## Proof
**Step 1 (an exact output-support partition).** Any permissible output preserves total Hamming weight and changes at most four consecutive coordinates. Over the binary alphabet, the set of altered coordinates therefore has size zero, two, or four. There is one zero-change output. For any distinct positions \(i<j\) with \(j-i\le3\) and \(x_i\ne x_j\), flipping these two symbols realizes exactly one output: select any four-position window containing both and interchange the two different symbols. Such a window exists because \(n\ge4\) and their separation is at most three. Conversely, every two-change output arises uniquely this way. A four-change output is possible precisely on a four-position window containing exactly two ones; it is then the bitwise complement of that entire window, and that window is determined uniquely by the altered support. Distinct supports identify distinct outputs. Consequently
\[
B_4(x)=1+\sum_{d=1}^{3}\sum_{i=1}^{n-d}\mathbf1\{x_i\ne x_{i+d}\}+\sum_{i=1}^{n-3}\mathbf1\{w(x_i\cdots x_{i+3})=2\}.\tag{1}
\]
This wordwise evaluation is a direct specialization of the general formula for substring-permutation spheres given by Chen and Milenkovic; it is used here to solve a separate optimization/equality problem and is not claimed to be new in itself.

**Step 2 (sharp extension inequality).** Given \(x\in\mathcal X_n\) and a new terminal bit \(b\), let \(r\) be the number of entries among the final three symbols of \(x\) that differ from \(b\). Formula (1) gives
\[
B_4(xb)-B_4(x)=r+\mathbf1\{r=2\}\in\{0,1,3\}.\tag{2}
\]
Indeed, the only newly counted unequal pairs end at the appended position, and the only newly counted all-four change is the new final window, which has weight two if and only if \(r=2\). Thus the increase is at most three for every word and extension.

**Step 3 (base case).** At \(n=4\), a permutation can produce every binary four-word with the same Hamming weight as its input, hence \(B_4(x)=\binom{4}{w(x)}\le6\). Equality holds for exactly the six weight-two words. Repeated use of (2) yields \(B_4(x)\le6+3(n-4)=3n-6\) for all \(n\ge4\).

**Step 4 (all and only equality cases).** Each length-four maximizing word contains exactly two ones, so its last three symbols contain both a zero and a one. Suppose a maximizing prefix has a final three-symbol block containing both binary values. Then \(r=3\) is impossible for any appended bit. By (2), equality in the three-unit extension bound holds if and only if \(r=2\), meaning that the appended bit must be the unique minority symbol among those final three. This is a unique extension, and the new final four-symbol block again contains two ones, so the mixed-final-three property persists. Starting from each of the six weight-two length-four words, this rule yields one infinite maximizing sequence and no others. Directly applying the rule yields the four period-four sequences with blocks `0011`, `0110`, `1100`, `1001`, and two alternating sequences with blocks `01`, `10`. Their length-\(n\) prefixes are distinct for every \(n\ge4\), and (2) attains equality at each extension. This proves both the sharp maximum and exact equality classification. \(\square\)

## Verification
The included standalone `checker.py` independently constructs every reachable output by all twenty-four block permutations for every binary source of lengths \(4\) through \(12\). It checks equality with formula (1), the maximum \(3n-6\), and exact equality with the six predicted extremizers. The checks cover \(8{,}176\) binary inputs and pass; they are finite cross-checks, not a substitute for the preceding proof. Run `python3 checker.py` using only the Python standard library.

## Relationship to prior work
Chen and Milenkovic, *Correcting Burst Errors with Applications to DNA-Based Data Storage*, arXiv:2610.15701v1 (first posted October 11, 2026), introduce exactly this binary substring-permutation channel. Section II gives a stronger **per-word** formula for \(\phi_k(x)=|P_k(x)|\) at all burst lengths and uses it for probabilistic coding lower bounds. Formula (1) above follows from that prior formula, so it is not an independent contribution. The mathematical claim here is instead the sharp optimization of \(\phi_4\) over all source words at every block length \(n\ge4\), with the complete six-word equality characterization. The inspected primary manuscript develops asymptotic redundancy and code constructions rather than stating that extremum or its equality cases. Its motivating nanopore platform uses physical four-symbol sensing windows. Limited-permutation channels allowing disjoint adjacent transpositions should not be conflated with the present all-permutations-of-one-contiguous-block channel.

## Limitations
The theorem is binary, concerns one exactly four-symbol permutation window without wraparound, and measures the number of distinct outputs rather than optimal code size. It does not prove results for arbitrary alphabet sizes, larger burst lengths, multiple bursts, or coding-rate optima. The per-word sphere formula is established in the cited source, and this optimization could have an unindexed or implicit earlier presentation. The result has not undergone an independent mathematical audit.

## References
Chen, Y.-P. and Milenkovic, O. (2026). *Correcting Burst Errors with Applications to DNA-Based Data Storage*. arXiv:2610.15701v1, first posted October 11, 2026. https://arxiv.org/abs/2610.15701. In particular, Section II, equation for \(\phi_k(x)\) and Figure 1's four-symbol sensing example.
