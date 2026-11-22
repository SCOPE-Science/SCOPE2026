# The sharp prime-field covering threshold for two eighth powers

## Finding

For every prime \(p\), define the number of represented residues
\[
\alpha_8(p)=\#\{a\in\mathbb F_p:\text{there exist }x,y\in\mathbb F_p\text{ with }x^8+y^8=a\}.
\]
The equality \(\alpha_8(p)=p\) fails **exactly** at
\[
\mathcal E=\{5,13,17,29,41,73,89,97,113,137,233,257,337,761\}.
\]
The complete exceptional counts are:

| Prime \(p\) | \(\alpha_8(p)\) |
|---:|---:|
| 5 | 3 |
| 13 | 10 |
| 17 | 5 |
| 29 | 22 |
| 41 | 21 |
| 73 | 46 |
| 89 | 56 |
| 97 | 73 |
| 113 | 85 |
| 137 | 86 |
| 233 | 204 |
| 257 | 225 |
| 337 | 295 |
| 761 | 666 |

Consequently, **every element of \(\mathbb F_p\) is the sum of two eighth powers for every prime \(p\ge769\)**, and \(769\) is the least prime beyond which this property holds for every prime. The largest exceptional prime is \(761\), immediately followed by the prime \(769\).

## Assumptions and scope

All fields are prime fields \(\mathbb F_p\), including characteristic two. Both summands can be zero, and the target may be zero. This theorem classifies residue-set coverage, not the number of ordered representations of each target; it does not assert the same threshold for arbitrary finite fields or prime-power rings.

## Proof

**Large-prime part.** Fix an odd prime \(p\) and a nonzero target \(a\in\mathbb F_p\). Consider the projective Fermat twist
\[
C_a:\quad X^8+Y^8=aZ^8.
\]
The three partial derivatives of its defining polynomial cannot vanish simultaneously at a projective point since \(8a\ne0\) in \(\mathbb F_p\). Thus \(C_a\) is a smooth plane curve of degree eight and genus \((8-1)(8-2)/2=21\). Hasse--Weil gives
\[
\#C_a(\mathbb F_p)\ge p+1-42\sqrt p.
\]
On the line at infinity \(Z=0\), the equation \(X^8+Y^8=0\) has at most eight rational projective points. Therefore the number of affine solutions satisfies
\[
\#\{(x,y)\in\mathbb F_p^2:x^8+y^8=a\}\ge p-7-42\sqrt p.
\]
This lower bound is strictly positive for every prime \(p\ge1783\): it is already positive at \(1783\), and the right side increases for real \(p>441\). The target \(a=0\) is represented by \((0,0)\). Hence all primes at least \(1783\) have full coverage.

**Finite part.** Every prime \(p\le1777\) can be handled exhaustively by forming
\[
H_p=\{x^8\bmod p:0\le x<p\},\qquad
A_p=\{(u+v)\bmod p:u,v\in H_p\}.
\]
This equality is a tautological equivalence between all possible residue representations and the computed sumset; no unexamined inputs remain. The standalone `verify.py` enumerates **all 275 primes** not exceeding \(1777\) with a sieve, forms these exact sets, and checks \(\#A_p=p\) except at the fourteen displayed primes, where it checks the displayed exact counts. An independent repeated-squaring routine recomputes each power image and checks every cardinality. The prime \(p=2\) also has full coverage.

Combining the large-prime bound with the complete finite census proves the exact exception list and therefore sharpness of \(769\).

**Arithmetic reduction.** For odd \(p\), the nonzero eighth-power image is the unique subgroup of \(\mathbb F_p^\times\) of index \(\gcd(8,p-1)\). Thus for \(p\equiv3,7\pmod8\) it equals the nonzero square image, and for \(p\equiv5\pmod8\) it equals the nonzero fourth-power image. The exceptional primes \(5,13,29\) are in the fourth-power branch; the remaining eleven are in the genuinely eighth-power branch \(p\equiv1\pmod8\). This reduction corroborates, but is not required for, the exhaustive proof.

## Verification

Run `python3 verify.py` in the directory containing this document. The recorded output appears in `checks.txt`. The verifier uses only the Python 3 standard library. It checks all primes through \(1777\), verifies the multiplicative-subgroup cardinality formula and recomputes power images via separate repeated squaring. It also checks the integer inequality certifying positivity of the Hasse--Weil bound. The infinite assertion depends on the stated geometric theorem, **not** on extrapolation from experiments.

## Relationship to prior work

Arias, Borja and Anaya (2023), *Counting Integers Representable as Sums of k-th Powers Modulo n*, define the same represented-residue invariant for general exponents. Their Corollary 21 proves eventual full coverage, giving the sufficient bound \(p>7^4=2401\) at exponent eight. Their Section 6 explicitly classifies fourth, fifth and sixth powers, including the exceptional fourth-power primes \(5,13,29\), but does not give the sharp eighth-power prime classification above. Bergelson, Best and Iosevich (2020) study the general two-power representation question and give large-field results, not the complete prime exception set at exponent eight. The present claim is therefore the **sharp complete eighth-power specialization**, not novelty in the Hasse--Weil method or in the modular Waring problem itself.

## Limitations

The finite table is certified by an executable, exhaustive integer computation; there is no independent formal proof certificate for every finite case. Literature searches cannot rule out every uncatalogued equivalent census. A relevant earlier thesis by S. Anaya (2022), cited in related literature, was not available as inspectable complete text and remains an explicit bibliographic risk. The exact counts for the fourth-power branch are already covered by the 2023 article; the principal new information is the eleven genuinely octic exceptions and their sharp global threshold. No independent review has been performed.

## References

1. F. Arias, J. Borja, S. Anaya, *Counting Integers Representable as Sums of k-th Powers Modulo n*, **Journal of Integer Sequences** 26 (2023), Article 23.8.1, published August 28, 2023. https://cs.uwaterloo.ca/journals/JIS/VOL26/Borja/borja4.pdf
2. V. Bergelson, A. Best, A. Iosevich, *Sums of Powers in Large Finite Fields: A Mix of Methods*, arXiv:2009.09518 (first posted September 2020). https://arxiv.org/abs/2009.09518
3. Hasse--Weil bound for point counts on smooth projective curves over finite fields (standard theorem).
4. S. Anaya, *Conteo de enteros representables como sumas de potencias k-ésimas módulo n*, undergraduate thesis, Universidad de Córdoba (2022), bibliographic citation in later work; full text not inspected.
