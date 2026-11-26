# Sharp four-sign quadratic-residue universality over finite fields

## Finding

Let \(q\) be an odd prime power, let \(\mathbb F_q\) be the field of \(q\) elements, and let \(\chi_q\) denote its quadratic character, extended by \(\chi_q(0)=0\). For each sign word \(\varepsilon\in\{-1,1\}^4\), define
\[
N_q(\varepsilon)=\#\{x\in\mathbb F_q:\chi_q(x+j)=\varepsilon_j\ (0\le j<4)\}.
\]
Here each integer shift \(j\) means the corresponding element of the prime subfield. Define the exceptional set
\[
E=\{5,7,11,13,17,19,23,25,29,31,41,49,53\}.
\]
**Theorem.** All sixteen four-sign words occur in \(\mathbb F_q\) if and only if the characteristic is at least five and \(q\notin E\). Consequently, among odd prime powers of characteristic at least five, every field of order at least \(59\) realizes all sixteen words, and this universal lower threshold is sharp: \(\mathbb F_{53}\) lacks the all-residue word. The first successful field order is \(37\), whereas \(41\), \(49\), and \(53\) still fail; notably, the nonprime fields of orders \(25\) and \(49\) are exceptional.

When the characteristic is three, the first and fourth entries of any four-block coincide, so universality fails. In characteristic two every nonzero element is a square, so sixteen distinct quadratic square/nonsquare patterns are likewise impossible.

## Assumptions and scope

The four coordinates are \(x,x+1,x+2,x+3\), considered **inside the finite field**, and no coordinate may vanish in a signed word. An extension field \(\mathbb F_{p^r}\) is not a ring of integers modulo \(p^r\); the assertion concerns field-square status, not integer quadratic residues modulo composite numbers. For prime fields the admissible starts correspond exactly to the ordinary representatives \(1\le x\le p-4\); for extensions, every field element is eligible subject to four nonzero shifts. Multiplicity formulas for individual words are not asserted.

## Proof

**1. The analytic infinite tail.** Assume \(\operatorname{char}\mathbb F_q\ge5\). The four excluded starts \(B=\{0,-1,-2,-3\}\) are distinct. For a prescribed sign word \(\varepsilon\), expand the indicator product over the whole field:
\[
16N_q(\varepsilon)=\sum_{x\in\mathbb F_q}\prod_{j=0}^3(1+\varepsilon_j\chi_q(x+j))
-\sum_{x\in B}\prod_{j=0}^3(1+\varepsilon_j\chi_q(x+j)).
\]
At a start in \(B\), exactly one character is zero, and each of the other three factors is zero or two. Thus the correction is nonnegative and at most \(4\cdot8=32\).

For the full-field sum, the empty subset contributes \(q\); every one-factor character sum is zero. For any distinct \(a,b\in\mathbb F_q\), \(\sum_x\chi_q((x+a)(x+b))=-1\), so the total contribution from the six pair subsets is at least \(-6\).

For any three distinct shifts, the smooth cubic model \(y^2=\prod_{j\in J}(x+j)\) is a genus-one curve, hence Hasse's theorem gives
\[
\left|\sum_{x\in\mathbb F_q}\chi_q\left(\prod_{j\in J}(x+j)\right)\right|\le2\sqrt q.
\]
There are four such three-factor sums. The smooth projective completion of the monic quartic \(y^2=x(x+1)(x+2)(x+3)\) is also genus one and has **two** rational points over infinity. Therefore its affine character sum \(S_4\) satisfies \(\left|S_4+1\right|\le2\sqrt q\). Combining the contributions gives
\[
\boxed{16N_q(\varepsilon)\ge q-10\sqrt q-39.}
\]
For \(q>169\), writing \(t=\sqrt q>13\), the right side factors as \((t-13)(t+3)>0\), so **every** sign word occurs in every such finite field. Notice that this proves all extension degrees at once, rather than just prime moduli.

**2. An exhaustive small-field certificate.** It remains to treat prime powers \(q\le169\), because the analytic inequality at \(169\) is only nonnegative. Characteristic three fails as explained above. The standalone Python 3 program `verify.py` deterministically enumerates every prime power \(q\le169\) of characteristic at least five and calculates every one of the sixteen sign counts, not merely a sample. There are exactly \(42\) such fields.

The program constructs prime fields directly; for quadratic extensions it constructs \(\mathbb F_{p^2}=\mathbb F_p[T]/(T^2-d)\), where \(d\) is the least integer at least two that is nonsquare modulo \(p\). The only cubic extension needed is \(\mathbb F_{125}=\mathbb F_5[T]/(T^3+T+1)\). Every displayed defining polynomial is checked irreducible: in degree two by the nonsquare test, in degree three by the absence of roots. Multiplication and nonzero square sets are computed exactly. The quadratic character is independently checked against field Euler powers for **every nonzero element**. Four-step starts, zero exclusions, and all missing word masks are exhaustive integer loops. No statistical sampling, heuristic primality test, external finite-field library, or presupposed character table is used.

The exact census produces the thirteen exceptional orders in \(E\), and every other eligible prime power at most \(169\) realizes every word. At orders \(41\) and \(53\) the missing word is \((1,1,1,1)\); at \(49\) the only missing bit masks are \(11\) and \(13\), with bit \(j\) encoding whether coordinate \(j\) is a residue. The complete exceptional-mask certificate is in `finite_census.txt` and reproducible via `verify.py`. In particular, \(37\) realizes all words while \(53\) does not; the next eligible prime power is \(59\). The analytic tail and the finite census cover every odd prime power and prove the theorem.

## Verification

Run `python3 verify.py` with an ordinary Python 3 installation. It prints `VERIFICATION_OK` and the complete list of exceptional orders and their missing masks. The verifier exhausts all \(42\) eligible prime powers of order at most \(169\); it constructs all field elements and enumerates every possible start for each. It separately verifies Euler's character criterion and every field-size count. The statement for all larger prime powers is the symbolic Hasse-bound argument in the proof, not an extrapolation from finite computations.

## Relationship to prior work

Shinagawa, Eriguchi, Satake, and Nuida (first arXiv appearance 2022-09-05, arXiv:2209.01859; journal 2023) investigate the existence of arbitrary quadratic-residue sign strings over **prime fields**, including the least prime admitting all strings of fixed length. Their general estimates do not state the sharp eventual threshold \(59\) or the extension-field exceptions. Wang and Fang (2023) calculate selected homogeneous-run formulas and bounds for **prime fields**; these do not determine all sixteen mixed patterns over every prime power. Cohen (arXiv:2402.10737, first 2024-02-16) evaluates triple patterns over finite fields and four-term homogeneous configurations in characteristic five, but does not give the present all-sign exception list.

The closest later analysis is Buchaev and Tsfasman (arXiv:2607.17418, first 2026-07-19), which derives explicit Frobenius-trace formulas for the counts of **all mixed words over prime fields**. Thus the prime-field part of the finite census is not claimed as a new counting theory or independent of their more general formula. Their stated prime-only domain does not directly classify the nonprime fields \(25\) and \(49\), nor does it explicitly give the all-prime-power universal cutoff. Classical quadratic-character indicator expansions and Hasse's bound are used without originality claims. A published six-term quadratic-sign universality theorem proves the weaker four-sign consequence for primes at least \(461\); a separate published quartic-coset four-block theorem proves a different, more restrictive all-color statement only for primes congruent to one modulo four and at least \(3373\). Neither implies the sharp finite-field statement here.

## Limitations

The theorem classifies **existence of all sixteen sign words**, not the individual values of \(N_q(\varepsilon)\), the shortest witnessing starts, or prime-power residue *rings*. Its proof uses the classical Hasse estimate and a finite census; it supplies no new bound for arbitrary block length. Existing elliptic-trace formulas may imply the prime-field portion after additional evaluation, and an equivalent unindexed finite-field classification may exist. No cryptographic security or communication-complexity improvement is claimed.

## References

1. K. Shinagawa, R. Eriguchi, S. Satake, K. Nuida, *Private simultaneous messages based on quadratic residues*, arXiv:2209.01859 (2022-09-05); *Designs, Codes and Cryptography* **91** (2023), 3915–3932, DOI 10.1007/s10623-023-01279-5.
2. X. Wang, H. Fang, *The Distribution Properties of Consecutive Quadratic Residue Sequences*, first published 2023-10-03, DOI 10.1155/2023/5253261.
3. S. D. Cohen, *Triples and quadruples of consecutive squares or non-squares in a finite field*, arXiv:2402.10737 (2024-02-16).
4. A. Buchaev, M. Tsfasman, *Quadratic residue patterns of length 4 and 5*, arXiv:2607.17418 (2026-07-19).
5. H. Hasse, classical bound for point counts on smooth genus-one curves over finite fields.
