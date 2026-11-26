# Independent mathematical audit

## correctness

PASS

For the Apéry sum, ordinary binomial Lucas implies the stated Apéry digit factorization: a surviving summand needs every j_i≤n_i from binomial(n,j); if adding n+j has a first carry, its digit n_i+j_i−11<j_i makes binomial(n+j,j) vanish modulo 11. The surviving terms factor over digits, with overflowing digit terms zero in the individual sums as well. Direct computation leaves exactly digit 5 forbidden. In the ordered-pair problem the initial carry is zero and the final carry is free. By inclusion-exclusion, each target-digit row has 9 choices except for the collision of the two excluded summands, which yields 10 (digit 10 for carry 0 and digit 0 for carry 1). Every ordinary digit sum 0 through 20 occurs; for 0 through 10 take 0+s except for 5, use 1+4 for 5, and reflect for sums above 10. Thus every initial digit below 10 populates both carries, as do subsequent digits 1–9; equality at the lower bound requires exactly those subsequent digits. At the upper bound the unique maximizing transition from carry 0 takes digit 10 and stays at carry 0, giving the all-tens target. In counting equality of sums the signed carry lies in {−1,0,1}, with entry H(11q′−q) and unrestricted terminal state. The reflected sector has matrix rows (333,576) and (320,590), trace 923 and determinant 12150, giving the energy recurrence. The cylinder probabilities R_r/100^r lie between positive bounds and at most 10^(−r), proving full support and no atoms. For singularity, apply the ergodic theorem to the carry together with the current two input digits: both next-carry outcomes can be forced with extreme input pairs, so this finite lifted chain is irreducible, and the all-zero state has a self-loop. Its stationary law is the uniform carry (the two switch probabilities are 45/100) times the uniform digit pair. The output digit frequencies are 19/200 at 0 and 10 and 9/100 elsewhere, separating the measure from Haar. Finally the square-cylinder sum is E_r/10000^r; the positive matrix gives growth at its Perron root, which exceeds 10000/11 because the characteristic polynomial there is −59850/121. Independent direct enumeration through r=3 recovered the extrema (r=3: minimum 729 at 810 targets, unique maximum 1000 at 1330); independent carry and spectrum computations gave energies 1, 910, 827780, 752984440, 684947111120 through r=4 and dimension approximately 0.999746761157. These checks support the constants but do not replace the all-depth derivation. The frozen CHECK.py was read, not executed.

## originality

PASS

The supported distinct claim is the complete ordered modular fiber law and extremal target classification for the Apéry nondivisibility support at 11, together with its specific all-depth energy and 11-adic distribution. The digit criterion follows from classical Lucas input and direct digit residues and is not independently credited as novel. The closest indexed analogues have significant method overlap, especially the center-deleted Franel example at base five, but their available statements do not establish a theorem implying the reviewed base-eleven claims. Priority remains provisional at the source access bounds below.

## value

PASS

For a classical arithmetic sequence’s natural nondivisibility support, this resolves all ordered sum multiplicities, not just coverage or an early finite table. The sharp rare and frequent target classifications and modular energy quantify the local additive law. The limiting distribution shows why full coverage can coexist with singularity, and its exact near-one dimension distinguishes a qualitative bias from its precise square-mass growth. The value is these additive and measure invariants, not a recomputed Apéry residue table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
