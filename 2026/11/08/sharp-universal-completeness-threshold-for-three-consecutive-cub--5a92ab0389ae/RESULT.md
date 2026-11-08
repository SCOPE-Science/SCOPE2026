# Sharp universal completeness threshold for three consecutive cubic-residue coset colors

## Finding
For each prime \(p\equiv1\pmod3\), write \(C_p=(\mathbb F_p^{\times})^3\) and let \(h_p\) be the least integer \(h\ge2\) whose reduction is not in \(C_p\). Define a color \(c_p(x)\in\{0,1,2\}\) for each nonzero residue \(x\) by \(x\in h_p^{c_p(x)}C_p\). Set
\[
\mathcal W_3(p)=\{(c_p(n),c_p(n+1),c_p(n+2)):1\le n\le p-3\}.
\]
Then **all twenty-seven three-letter cubic-coset patterns occur** for every eligible prime at least \(307\):
\[
\mathcal W_3(p)=\{0,1,2\}^3\quad(p\ge307,\ p\equiv1\pmod3\text{ prime}).
\]
The immediately preceding eligible prime \(283\) has exactly twenty-six patterns, and its unique missing pattern is \((0,0,0)\). Hence \(307\) is the smallest **eligible prime** beyond which every eligible prime has the full ternary three-letter language. This is not the least numerical integer lower bound; it is the sharp admissible-prime cutoff.

## Assumptions and scope
Every field is \(\mathbb F_p\) with \(p\equiv1\pmod3\) prime. All three positions are nonzero residues and are represented by the ordinary consecutive integers \(n,n+1,n+2\) with \(1\le n\le p-3\), so no wraparound-zero ambiguity occurs. Interchanging the two nontrivial cosets permutes color labels \(1\) and \(2\); completeness and the exceptional all-zero pattern are invariant under that relabeling. The chosen least noncube makes the finite certificate unambiguous.

## Proof
Fix such a prime and a nontrivial cubic character \(\chi:\mathbb F_p\to\{0,1,\omega,\omega^2\}\), with \(\chi(0)=0\), where \(\omega^3=1\) and \(\omega\ne1\). Choose \(\chi(h_p)=\omega\). For a target word \(t=(t_0,t_1,t_2)\in\{0,1,2\}^3\), put
\[
Q_{t_j}(u)=1+\omega^{-t_j}\chi(u)+\omega^{-2t_j}\chi(u)^2.
\]
For every nonzero \(u\), this equals \(3\) if \(c_p(u)=t_j\) and zero otherwise. At \(u=0\) it equals \(1\). Let \(N_t(p)\) be the number of starting residues \(n\in\mathbb F_p\setminus\{0,-1,-2\}\) producing the target word. Thus
\[
27N_t(p)=\sum_{x\in\mathbb F_p}\prod_{j=0}^2Q_{t_j}(x+j)-E_t,
\]
where \(E_t\) is the sum of the contributions of \(x=0,-1,-2\). At each of those three arguments, one factor equals \(1\) and the other two factors each lie in \(\{0,3\}\), whence \(0\le E_t\le27\).

Expand the product into \(3^3=27\) terms, indexed by exponent vectors \((e_0,e_1,e_2)\in\{0,1,2\}^3\). The all-zero exponent vector contributes \(p\). For a nonzero exponent vector supported at \(r\) of the three distinct shifts, the corresponding character sum has absolute value at most \((r-1)\sqrt p\). Indeed, it is the sum of the nontrivial cubic character of the polynomial \(\prod_{e_j>0}(x+j)^{e_j}\), which is not a cube and has exactly \(r\) distinct zeros, so the standard Weil multiplicative-character bound applies. For \(r=1\), the sum vanishes by translation and nontrivial character orthogonality. For \(r=2\), there are \(\binom32\cdot2^2=12\) terms and each has absolute value at most \(\sqrt p\). For \(r=3\), there are \(2^3=8\) terms, each bounded by \(2\sqrt p\). All phase coefficients have modulus one. Therefore, uniformly in the twenty-seven target words,
\[
27N_t(p)\ge p-(12+16)\sqrt p-27=p-28\sqrt p-27.
\]
For \(p\ge841=29^2\) the right-hand side is positive: writing \(y=\sqrt p\ge29\), one has \(y^2-28y-27=(y-29)(y+1)+2>0\). Hence every target word is realized for every eligible prime \(p\ge841\).

It remains to check all eligible primes \(p<841\). The standalone Python-3 program `verify.py` implements exact integer primality testing, two independently constructed cubic-coset labelings (one from the cube subgroup and one from a primitive root), and complete enumeration of all \(p-3\) admissible starts for each eligible prime. Its result is: among the seventy eligible primes at most \(840\), the primes at which any word is missing are exactly
\[
7,13,19,31,37,43,61,67,79,127,151,163,283.
\]
All forty-two eligible primes in the interval \([307,840]\) realize every word. At \(283\), the one omitted word is \((0,0,0)\). The next prime congruent to one modulo three is \(307\), completing the sharp admissible-prime classification.

## Verification
Run `python3 verify.py` in the same directory as this file. The program uses only Python's standard library, prints the complete exception list, compares subgroup and discrete-log assignments for each prime, and concludes `VERIFY_OK` if all assertions pass. An exact saved run is reproduced in `verify_output.txt`; the displayed proof establishes the infinite range, whereas the program certifies only its stated finite range. It additionally checks that \(307\) has explicit starting positions for all twenty-seven words.

Two instructive finite counterexamples to the implication from monochromatic to full-word existence are \(p=151\) and \(p=163\): in both cases the word \((0,0,0)\) does occur, but the word \((2,0,2)\) is absent with the least-noncube orientation. Thus the earlier all-cubic-residue existence theorem alone does not imply the present completeness claim.

## Relationship to prior work
The classical 1962 theorem of D. H. Lehmer, E. Lehmer, W. H. Mills and J. L. Selfridge classifies primes **without** any three consecutive cubic residues. Its last exceptional prime is \(283\), establishing exactly the all-zero-pattern boundary, but not the presence of every mixed coset word. Rabung and Jordan (1970) concern runs confined to a single power-residue class; their conditions likewise do not entail all mixed three-color words. Hu and Chen (2020), and Yuan and Zhang (2022), count specific cubic-residue configurations involving expressions such as \(a+a^{-1}\) and \(a-a^{-1}\), rather than consecutive mixed coset triples. The result here adds simultaneous realization of all twenty-seven patterns at the optimal admissible-prime threshold; the cutoff for the single \((0,0,0)\) pattern is classical and is not claimed to be new.

## Limitations
This result concerns three positions only, prime fields with \(p\equiv1\pmod3\), and presence/absence rather than exact pattern frequencies. It does not classify length-four words, composite moduli, or optimal first-occurrence positions. The two cubic nonresidue cosets are intrinsically exchangeable. The 1962 all-residue exceptional list and the standard character-sum bound are prior results. Publication-priority claims for the full mixed-word threshold remain subject to possible older or unindexed statements; an especially plausible older source, Emma Lehmer's 1983 *Patterns of Power Residues*, was not accessible in full and therefore is not claimed to have been ruled out by a whole-text comparison. The displayed finite code checks are not an independent scientific audit.

## References
1. J. Hu and Z. Chen, *On distribution properties of cubic residues*, AIMS Mathematics **5** (2020), 6051–6060, https://doi.org/10.3934/math.2020388 (first publicly released 2020-07-23).
2. D. H. Lehmer, E. Lehmer, W. H. Mills, J. L. Selfridge, *Machine Proof of a Theorem on Cubic Residues*, Mathematics of Computation **16** (1962), 407–415, https://doi.org/10.2307/2003130.
3. J. R. Rabung and J. H. Jordan, *Consecutive Power Residues or Nonresidues*, Mathematics of Computation **24** (1970), 737–740, https://doi.org/10.2307/2004850.
4. X. Yuan and W. Zhang, *On cubic residues and related problems*, Indian Journal of Pure and Applied Mathematics **54** (2023), 806–815 (online 2022-08-02), https://doi.org/10.1007/s13226-022-00299-6.
5. E. Lehmer, *Patterns of Power Residues*, Journal of Number Theory **17** (1983), 37–46, https://doi.org/10.1016/0022-314X(83)90004-5 (full text not inspected).
6. Standard Weil bound for nontrivial multiplicative-character sums of a polynomial with \(r\) distinct roots, under the non-perfect-power condition.
