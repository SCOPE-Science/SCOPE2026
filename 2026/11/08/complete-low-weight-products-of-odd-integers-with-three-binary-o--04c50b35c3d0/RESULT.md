# Complete low-weight products of odd integers with three binary ones

## Finding
Let \(s_2(n)\) count the ones in the canonical binary expansion of the positive integer \(n\). For odd positive integers \(a,b\) with \(s_2(a)=s_2(b)=3\), the condition \(s_2(ab)\leq3\) holds if and only if, after arranging \(a\leq b\), the triple \((a,b,ab)\) is one of
\[
(25,41,1025),\quad(7,7,49),\quad(7,19,133),\quad(7,37,259),
\]
\[
(11,35,385),\quad(13,21,273),\quad(21,49,1029).
\]
The first triple has product weight \(2\), and the other six have product weight \(3\). Thus the sharp largest product in this class is \(1029\), with the unique maximizing unordered factor pair \(\{21,49\}\).

## Assumptions and scope
The factors are *positive odd integers*, and their binary weights are both exactly \(3\). The inequality on product weight includes \(1\), but that case is impossible because odd three-bit factors are at least \(7\), and the only odd power of two is \(1\). The classification is up to factor exchange; there are seven unordered pairs (thirteen ordered pairs, counting the diagonal pair once). No assertion is made for even factors or product weight at least \(4\).

## Proof
**Global reduction (published input).** Kaneko and Stoll [1, Theorems 2.1 and 2.2] prove the following for positive odd \(a,b\) of binary weights \(\ell,m\geq2\): if \(s_2(ab)=2\), then \(ab<2^{-4+2\ell m}\), and if \(s_2(ab)=3\) and \(\max\{\ell,m\}\geq3\), then \(ab<2^{-13+4\ell m}\). Both apply at \(\ell=m=3\), giving respectively
\[
s_2(ab)=2\Longrightarrow ab<2^{14},\qquad
s_2(ab)=3\Longrightarrow ab<2^{23}.
\]
The source proof of its nontrivial second bound is a finite carry-propagation analysis (Section 4), with the first bound in Section 3. These are cited published theorems, not claims newly proved here.

**Exhaustive finite reduction.** A positive odd integer of weight \(2\) is uniquely \(1+2^j\) with \(j\geq1\), and one of weight \(3\) is uniquely \(1+2^i+2^j\) with \(1\leq i<j\). The strict product bounds restrict possible products to the \(13\) weight-two integers \(1+2^j\) for \(1\leq j\leq13\), and the \(\binom{22}{2}=231\) weight-three integers \(1+2^i+2^j\) for \(1\leq i<j\leq22\). These are exact, exhaustive exponent ranges; there is no unsearched larger product.

For each candidate product \(N\), the smaller factor \(a\) must satisfy \(7\leq a\leq\lfloor\sqrt N\rfloor\), must be odd with binary weight \(3\), and must divide \(N\); its complementary factor \(b=N/a\) must also have binary weight \(3\). The independent exact-integer divisor census in `independent_check.py` checks all these possibilities, with no heuristic filtering. It performs \(5523\) integer trial divisions over the two product-weight classes and returns precisely the seven listed triples. It therefore proves both completeness and the stated maximum.

**Independent enumeration.** To cross-check the finite conclusion without using the product-first divisibility algorithm, `verify.py` independently constructs all \(231\) odd three-bit candidates with higher exponent at most \(22\) and checks all \(3672\) unordered pairs whose product is less than \(2^{23}\). The product bound implies all factors have higher exponent at most \(22\), so this factor-first list also has no unsearched tail. Its low-weight output agrees with the product-first computation. The two methods use only exact integer arithmetic; source code and recorded outputs accompany this result.

Finally, direct binary-weight checks of the seven triples verify the *if* direction. Since the product-first enumeration is exhaustive under the cited global bounds, the *only-if* direction follows.

## Verification
Run `python3 verify.py` and `python3 independent_check.py` in the directory containing those two files. The first prints `VERIFY_OK`; the second prints `INDEPENDENT_CHECK_OK`. Their captured outputs are supplied in `verify_output.txt` and `independent_output.txt`. No external packages are required. The finite enumerations establish the classification only when combined with the published global bounds above; they do not purport to prove those bounds by experiment.

## Relationship to prior work
Kaneko and Stoll [1] introduce the sparse-product system \(s_2(ab)=k\), \(s_2(a)=\ell\), \(s_2(b)=m\). Their Theorems 2.1 and 2.2 prove effective global bounds for \(k=2,3\), but the inspected statement and proofs do not enumerate the complete \((\ell,m)=(3,3)\) case. This result determines that symmetric case, jointly for the two lowest possible nontrivial product weights, with its sharp largest product.

Aloui et al. [2] study sparse *squares*, a different diagonal restriction \(a=b\); the previously known square \(7^2=49\) is therefore not claimed as an independent discovery. The published exact \((k,\ell,m)=(3,2,3)\) classification [3] treats a factor of weight \(2\), not two factors of weight \(3\). Its bound-and-enumeration approach is related, but its two factor pairs cannot imply the seven pairs above. Search non-detection does not prove publication priority.

## Limitations
This is a natural small complete Diophantine classification, not a new uniform sparse-product bound. It depends on published Theorems 2.1 and 2.2; the exhaustive part is finite and reproducible. The classification does not address product weights at least \(4\) and is not a classification for arbitrary factor weights. Earlier unindexed observations of the same small case cannot be excluded.

## References
[1] H. Kaneko and T. Stoll, *Products of integers with few nonzero digits*, arXiv:2112.03077v1 (first posted 6 December 2021), Theorems 2.1 and 2.2, Sections 3–4; *Uniform Distribution Theory* 17 (2022).

[2] K. Aloui, D. Jamet, H. Kaneko, S. Kopecki, P. Popoli and T. Stoll, *On the binary digits of n and n squared*, arXiv:2203.05451v1 (first posted 10 March 2022), especially Section 2 on sparse squares.

[3] *Exact (3,2,3) binary-weight product classification*, public mathematical record at https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-3-2-3-binary-weight-product-classification--28456ef398f9 (inspected RESULT.md).
