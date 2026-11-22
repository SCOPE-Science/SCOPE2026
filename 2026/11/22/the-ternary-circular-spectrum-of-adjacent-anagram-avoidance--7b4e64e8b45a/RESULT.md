# The ternary circular spectrum of adjacent anagram avoidance

## Finding

Let \(\Sigma=\{0,1,2\}\). For each integer \(n\ge1\), let \(C_n\) be the number of indexed periodic words \(w\in\Sigma^n\) such that, at every integer index interpreted modulo \(n\), the two length-two factors \(w_iw_{i+1}\) and \(w_{i+2}w_{i+3}\) have different symbol-count vectors. The periodic extension is used even for \(n<4\). Define
\[
F(z)=1-z+z^3,\qquad G(z)=1-z-2z^2-3z^3-2z^4,
\]
\[
H(z)=1+z+2z^2+3z^3-3z^6-2z^7.
\]
Then the complete periodic-orbit zeta function is
\[
\boxed{\exp\left(\sum_{n\ge1}\frac{C_nz^n}{n}\right)=\frac{1}{F(z)G(z)H(z)^2}.}
\]
Equivalently,
\[
\sum_{n\ge1}C_nz^n=-z\frac{d}{dz}\log(F(z)G(z)H(z)^2).
\]
The first fifteen counts are \(0,0,6,60,90,216,462,1332,3282,7980,18876,46812,115440,283626,691986\). The exact number of primitive necklaces of length \(n\), with alphabet symbols labeled and rotations identified but not reflections, is
\[
\boxed{P_n=\frac1n\sum_{d\mid n}\mu(d)C_{n/d}},
\]
and the exact total number of necklaces is \(N_n=\frac1n\sum_{d\mid n}\varphi(d)C_{n/d}\). These formulas cover every positive length, not only a computed finite range.

## Assumptions and scope

A length-four factor is forbidden if its initial pair and final pair are anagrams, including but not limited to ordinary tandem squares. This is **only** Abelian-square avoidance with root length exactly two: repetitions of other root lengths and adjacent equal single symbols may occur. The symbols are three distinct labeled letters. An indexed word distinguishes its starting index; necklaces identify cyclic rotations. For periodic words of length below four, windows wrap around more than once, as required by the bi-infinite periodic extension.

## Proof

Index the \(27\) states by triples \((a,b,c)\in\Sigma^3\). Define an integer \(27\times27\) matrix \(T\) by
\[
T_{(a,b,c),(b',c',d)}=\begin{cases}1&b'=b,\ c'=c,\ \{a,b\}_{\rm multi}\ne\{c,d\}_{\rm multi},\\0&\text{otherwise}.\end{cases}
\]
Every edge appends one symbol, testing precisely the new length-four window. Closed walks of length \(n\) in this three-letter overlap graph correspond bijectively to the indexed periodic words counted by \(C_n\). This remains true at \(n=1,2,3\), because a closed walk forces the correct repeated-coordinate identifications. Consequently \(C_n=\operatorname{tr}(T^n)\) for every \(n\ge1\).

An exact integer characteristic-polynomial calculation gives
\[
\det(\lambda I-T)=\lambda^6(\lambda^3-\lambda^2+1)(\lambda^4-\lambda^3-2\lambda^2-3\lambda-2)
(\lambda^7+\lambda^6+2\lambda^5+3\lambda^4-3\lambda-2)^2.
\]
This is not a numerical factorization: `verify_spectrum.py` builds all matrix entries as integers, calculates the traces of powers through \(27\), applies Newton's identities with checked exact integer divisions to obtain every coefficient of \(\det(I-zT)\), and checks the factorization coefficient by coefficient. The nonzero factors of \(\det(I-zT)\) are exactly \(F(z)G(z)H(z)^2\). For every finite matrix,
\[
\det(I-zT)^{-1}=\exp\left(\sum_{n\ge1}\operatorname{tr}(T^n)z^n/n\right)
\]
as an identity of formal power series; this proves the zeta formula for all lengths. Möbius inversion of periodic points by least period gives the primitive-orbit formula; Burnside's lemma gives the unrestricted necklace formula. Both formulas involve integer counts even though expressed as rational sums.

## Verification

Two independently formulated checks accompany the proof. `verify_spectrum.py` checks all \(27\) characteristic coefficients and the first fifteen power traces using exact integers and only Python's standard library. `verify_bruteforce.py` independently tests every ternary indexed word for every length through eleven (with exhaustive modular-window comparisons), and independently verifies the primitive-necklace relation through length nine. Both scripts run with `python3` from the extracted directory and print success only after assertions pass.

## Relationship to prior work

Shur's paper on ternary square-free circular words studies avoidance of **all ordinary squares** on circular words, including the length-two repetition of a single symbol; it proves a different existence theorem, not the present fixed-root-length-two Abelian cyclic enumeration. Huova and Karhumäki study \(k\)-Abelian equivalence and avoidance of **all** such squares, which differs from requiring only the two adjacent length-two windows to have different Parikh vectors. Open-boundary counting of these four-letter obstructions has a much shorter recurrence; it does not by itself determine the closed-walk counts or the extra cubic and septic spectral factors given here. The ordinary transfer-matrix and Möbius inversion principles are standard and are not claimed as new.

## Limitations

The claim is specific to a ternary alphabet and to Abelian squares with half-length exactly two, and does not enumerate all Abelian-square-free words. The proof gives complete indexed and rotation-class counts but not a separate classification of rotation-plus-alphabet-relabeling classes. Historical prior statements under other names cannot be ruled out solely from literature search. No independent mathematical audit has been performed.

## References

1. A. M. Shur, *On ternary square-free circular words*, arXiv:1009.5759, first publicly posted 2010-09-29, https://arxiv.org/abs/1009.5759 ; Electronic Journal of Combinatorics **17** (2010), R140.
2. M. Huova and J. Karhumäki, *Observations and Problems on k-abelian avoidability*, arXiv:1104.4273, first publicly posted 2011-04-21, https://arxiv.org/abs/1104.4273 .
3. Standard finite-state transfer identity and the classical Möbius/Burnside inversion formulas; matrix and enumerative computations reproduced in the accompanying scripts.
