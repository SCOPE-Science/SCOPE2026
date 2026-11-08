# The first nontrivial local five-term zero-sum constant: \(s_5^*=11\)

## Finding
Let \(s_p^*\) be the smallest integer \(L\) for which **every** sequence of \(L\) integers individually coprime to the prime \(p\) has **exactly \(p\) indexed terms** whose sum is divisible by \(p\) but not by \(p^2\). Repetition of values is permitted, but selected indices are distinct. The exact value for \(p=5\) is
\[
\boxed{s_5^*=11.}
\]
This establishes the first nontrivial prime case beyond the previously established general upper bound \(s_p^*\le 3p-2\). The proof supplies a finite certificate for the eleven-term assertion and a concrete ten-term obstruction. An auxiliary exact classification identifies the twelve residue multiplicity profiles supporting a ten-term obstruction.

## Assumptions and scope
All sequences consist of integer **units modulo \(5\)**. A forbidden five-term subsequence has sum congruent to one of \(5,10,15,20\) modulo \(25\), not congruent to \(0\). Only the prime \(5\) is treated. No assumption of distinct numerical values or bounded integer magnitude is made.

## Proof
**1. The sharp lower bound.** Take
\[
(1,1,1,1,21,2,2,2,2,17).
\]
There are five entries congruent to \(1\) modulo \(5\), and five congruent to \(2\). If a five-index subset contains \(x\) entries from the first class and \(5-x\) from the second, its sum is \(x+2(5-x)\equiv-x\pmod5\). Hence a sum divisible by \(5\) must use all five entries from one class. In either case the sum is exactly \(25\). This ten-term sequence is forbidden-witness-free, so \(s_5^*\ge11\).

**2. Finite-field lifting criterion.** For an arbitrary sequence of \(n\) units modulo \(25\), uniquely write each entry as \(r_i+5y_i\pmod{25}\), with \(r_i\in\{1,2,3,4\}\) and \(y_i\in\mathbb F_5\). For any five-index set \(I\) with \(\sum_{i\in I}r_i\equiv0\pmod5\), the selected sum is a multiple of \(25\) exactly when
\[
\sum_{i\in I}y_i\equiv-\frac{1}{5}\sum_{i\in I}r_i\pmod5.
\]
The quotient is an integer because the chosen residue sum is divisible by five. Thus the sequence is forbidden-witness-free if and only if this explicitly specified **affine system over \(\mathbb F_5\)** is consistent. With fixed residue multiplicities \((a,b,c,d)\) (counts of \(1,2,3,4\) respectively), the system is independent of the ordering of equal residues. Each composition of \(n\) into four counts is therefore a complete equivalence class for this test.

**3. A complete ten-term profile lemma.** Exact Gaussian elimination modulo \(5\) over all \(\binom{13}{3}=286\) compositions with \(a+b+c+d=10\) shows that the affine system is consistent for exactly the following twelve profiles:

```text
(0,0,5,5) (0,4,2,4) (0,5,0,5) (0,5,5,0)
(1,4,4,1) (2,0,4,4) (4,1,1,4) (4,2,4,0)
(4,4,0,2) (5,0,0,5) (5,0,5,0) (5,5,0,0)
```

Six have coefficient rank \(2\) and six have rank \(8\). This is a **finite exact lemma**, not statistical evidence. Its full enumeration, equations, and elimination operations are supplied in two standalone pure-integer programs: `verify_zero_sum.py` and `verify_zero_sum.cpp`. They iterate each four-count composition and every five-index subset, append the equation when its residue sum is zero, and perform row reduction over the five-element field. The number \(286\) is exhaustive by the stars-and-bars count. Independent implementations agree with the displayed list and ranks; either program reconstructs the certificate without supplied data files.

**4. Excluding eleven terms.** Suppose an eleven-term sequence had no permitted five-subsum. Deleting any one term would leave a forbidden-witness-free ten-term sequence. Its residue count profile must consequently belong to the twelve profiles in Step 3. Every listed ten-term profile has all counts at most \(5\); it is either two counts equal to \(5\), or two counts equal to \(4\) and two remaining counts totaling \(2\).

Let \(c\) be the four-count profile of the hypothetical eleven-term sequence. If some count is at least \(6\), deleting an entry from another positive class retains that count, hence gives an excluded ten-term profile. If no other class is present, deletion leaves ten copies of one class, also excluded. Thus every count is at most \(5\).

If one count equals \(5\), deletion from another positive class leaves a ten-term profile containing a count \(5\). The classification forces this deletion profile to consist of exactly two counts \(5\). The original profile must therefore have two counts \(5\) and one count \(1\). Deleting an entry from either five-count class then leaves a ten-term profile with counts \(5,4,1\), which is absent from the list: contradiction.

If all counts are at most \(4\), every ten-term deletion profile in the list must have at least two counts equal to \(4\). The eleven-term original must therefore have at least two four-count classes. Deleting a term from either one leaves at most one four-count class, since there cannot be three four-count classes in a total of eleven terms. Again the resulting ten-term profile is absent: contradiction.

Every possible profile yields a contradiction. Hence all eleven-term sequences have a permitted five-subsum, proving \(s_5^*\le11\). Together with Step 1, this proves the theorem.

## Verification
The Python verifier independently constructs and reduces every affine constraint system for all \(286\) ten-term and \(364\) eleven-term profiles. The C++ verifier enumerates subsets through independent bit masks rather than Python combinations and implements separate modular row reduction. Both report exactly twelve solvable ten-term profiles, including their ranks, and no solvable eleven-term profiles. The Python program additionally verifies that deleting any index from any eleven-term profile cannot always land in the allowed twelve-profile list and checks the ten-term sharpness witness. Embedded stdout artifacts are `verification_output.txt` and `verification_cpp.txt`.

To reproduce from the standalone files, run `python3 verify_zero_sum.py` and (with a C++17 compiler) `g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_zero_sum.cpp -o verify_zero_sum && ./verify_zero_sum`. These are exhaustive finite checks whose coverage and reduction logic constitute the finite certificate; they are not an appeal to an unbounded experimental pattern.

## Relationship to prior work
Gao, Jiang, Lei, Lin, and Yang introduced this prime-index local constant, conjectured \(s_p^*=2p+1\) for all primes \(p\ge3\), and established the general bound \(s_p^*\le3p-2\), giving \(s_5^*\le13\) [1]. Sun independently formulated the equivalent prime-modulus one-dimensional constant \(s_1(5)\) and conjectured its value \(11\) [2]. Li, Ling, Sun, and Zhu gave general lower bounds and studied higher-rank and variable-length constants, rather than this exact prime-five upper bound [3]. Gao, Jiang, and Mu studied a different condition in which the selected subsequence has **at most** the prescribed number of terms; it does not settle the exact-five-term question [4]. The earlier publicly indexed research record computing the composite case \(s_1(4)=9\) likewise does not imply this prime-five result [5].

## Limitations
The result treats only \(p=5\), not all primes. The ten-profile classification and eleven-term exclusion rely on exact finite arithmetic certificates whose full algorithms are supplied. The originating journal article's complete institutional-access text was unavailable for inspection; its publicly accessible abstract states the conjecture and the weaker bound, and closely related subsequent full text was inspected. This leaves a historical-priority risk that a sharper special case could be buried in inaccessible or unindexed primary material. Independent expert audit has not been performed.

## References
[1] W. Gao, X. Jiang, W. Lei, C. Lin, W. Yang, *A new problem from zero-sum theory*, Acta Arithmetica 224 (2026), 71–79; first online 2026-05-31. DOI: `10.4064/aa251115-21-1`. Publisher abstract: https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/online/116456/a-new-problem-from-zero-sum-theory.

[2] Z.-W. Sun, *On zero-sum problems of two new types*, arXiv:2606.18234 (2026). https://arxiv.org/abs/2606.18234.

[3] Y. Li, S. Ling, Z. Sun, S. Zhu, *Proofs and disproofs of some conjectures on zero-sum problems of new types*, arXiv:2610.19965 (2026). https://arxiv.org/abs/2610.19965.

[4] W. Gao, X. Jiang, Y. Mu, *Two local zero-sum problems*, arXiv:2607.11313 (2026). https://arxiv.org/abs/2607.11313.

[5] published-finding corpus research record, *Exact evaluation of \(s_1(4)\) and the eight-term extremals* (2026), identifier `2026/10/4/SCOPE-exact-evaluation-of-s-1-4-and-the-eight-term-extremals--e0dfeeac2337`.
