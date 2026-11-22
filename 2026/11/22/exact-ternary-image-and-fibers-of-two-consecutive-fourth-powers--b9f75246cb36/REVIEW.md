# Review: Exact ternary image and fibers of two consecutive fourth powers

## Correctness — PASS

For \(F(x)=x^4+(x+1)^4\), the integral-to-three affine substitution \(t=2x+1\) gives \(8F=t^4+6t^2+1\). Hensel's lemma maps each of the two unit input classes bijectively to the full target residue disk \(1+3\mathbb Z_3\). On the unique singular input class \(t=3s\), the map is \(1/8+(27/4)s^2(1+(3/2)s^2)\); the square-root coordinate change is a bijective three-adic isometry. Root counting for squares at every precision then yields the exact target-by-target fiber law, the image-count formula and the rational density \(25/72\). The embedded exhaustive enumeration of the formula and direct polynomial images passes for \(3^1\) through \(3^9\). Computation is a consistency check, not the infinite proof.

## Originality — PASS on inspected evidence

Ding and Zieve's 2023 preprint, arXiv:2309.14979, gives finite-field quartic-value-set cardinalities and sums (Lemma 3.1 and Theorem 1.3); the full text was inspected and does not assert the prime-power residue-ring image or fiber distribution of this polynomial. Finch-Smith, Harrington and Wong's 2023 published scope concerns polynomial residues modulo primes at least five, so excludes characteristic three and higher prime powers. Sun's 2003 quartic-congruence paper is explicitly for primes greater than three, not this local ring. Indexed public records with ternary square branches concern different polynomial families. No statement was found implying the presented exact \(3\)-adic image and every finite fiber. Nonetheless a general local quartic algorithm or an unindexed source could implicitly recover the specialization, so global priority remains uncertain.

## Value — PASS

The sum of consecutive fourth powers is a natural Diophantine polynomial, and three is an arithmetically exceptional prime: its derivative degenerates on exactly one residue class. This sharp classification quantifies both the full ball coming from smooth branches and the nontrivial quadratic obstruction in the singular branch. In addition to deciding local solvability, the theorem determines the complete multiplicity of each congruence and the exact Haar density. The local denominator \(72\) is not an arbitrary finite table entry; it comes from a structural splitting into one full residue ball and a scaled square-value set.

## Closest sources and limitations

The 2023 finite-field work of Ding and Zieve is the closest primary treatment of quartic images; it is carefully distinguished from residue rings modulo \(3^k\). Published analyses of a sixth binomial polynomial modulo powers of three and fourth-degree Dickson polynomials modulo powers of two are methodologically related but concern different input objects. Only the local prime three and exponent four are classified. The finite checker does not constitute an infinite or independent proof, and an implicit previously published general quartic theorem remains a priority risk.

Self-review: passed. Independent audit: not yet performed.
