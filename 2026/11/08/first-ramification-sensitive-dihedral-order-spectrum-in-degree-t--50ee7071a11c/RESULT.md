# First ramification-sensitive dihedral-order spectrum in degree-two matrix groups

## Finding
Let \(R=\mathbb Z/25\mathbb Z\) and \(S=\mathbb F_5[\varepsilon]/(\varepsilon^2)\). For \(T\in\{R,S\}\), let \(\mathcal I(T)=\{g\in\operatorname{GL}_2(T):g^2=1\}\), **including the identity**, and let \(d_T(m)\) count ordered pairs \((g,h)\in\mathcal I(T)^2\) for which \(gh\) has exact multiplicative order \(m\). Both sets of involutive elements have cardinality \(752\). The complete nonzero distribution is:

| \(m\) | \(d_R(m)\) | \(d_S(m)\) |
|---|---:|---:|
| 1 | 752 | 752 |
| 2 | 3752 | 3752 |
| 3 | 15000 | 15000 |
| 4 | 15000 | 15000 |
| 5 | 18000 | 168000 |
| 6 | 15000 | 15000 |
| 10 | 18000 | 168000 |
| 15 | 60000 | 60000 |
| 20 | 60000 | 60000 |
| 25 | 150000 | 0 |
| 30 | 60000 | 60000 |
| 50 | 150000 | 0 |

All omitted orders have count zero. Each column totals \(752^2=565504\), and both have exactly \(4504\) ordered commuting pairs. Thus an identical involution count and commuting-pair count conceal an exact separation of the complete two-involution product-order spectra: \(300000\) ordered pairs over \(R\) have product of order \(25\) or \(50\), whereas no pair over \(S\) does.

## Assumptions and scope
The rings are precisely \(\mathbb Z/25\mathbb Z\) and \(\mathbb F_5[\varepsilon]/(\varepsilon^2)\), which have the same residue field and cardinality. The result makes no claims for other ring sizes, dimensions or primes.

## Proof
This is a **finite exhaustive certificate**, not a conjectural extrapolation. The accompanying complete, standalone C++ program `verify_orders.cpp` enumerates all \(25^4=390625\) matrices in each \(M_2(T)\). For each matrix it checks invertibility by the nonvanishing of its determinant modulo \(5\) (the exact unit criterion in these local rings) and computes its square in \(T\); equality with the identity characterizes \(\mathcal I(T)\) without omissions. Each ring is represented by the integers \(0,\ldots,24\). For \(R\), addition and multiplication are taken modulo \(25\). For \(S\), \(a+5b\) represents \(a+b\varepsilon\), with independent componentwise addition modulo \(5\) and multiplication \((a+b\varepsilon)(c+d\varepsilon)=ac+(ad+bc)\varepsilon\). The matrix product is computed directly by the four matrix entries and the ring operations.

The algorithm then enumerates **every ordered pair** of the involutive matrices (exactly \(565504\) pairs in each ring), multiplies the two matrices, and determines exact order by repeated multiplication from the identity up to exponent \(300\), recording the first return to identity. The bound suffices by the computed exhaustive list and can also be independently bounded by the order of \(\operatorname{GL}_2(T)\), which is \(25^2\lvert\operatorname{GL}_2(\mathbb F_5)\rvert=300000\); the program records no unclassified product. Thus each line of its output is an exhaustively proven finite integer count. The counts in each column sum to \(565504\). The count of commuting ordered pairs is separately computed using a direct comparison of \(gh\) and \(hg\).

For an independent structural population check, every involution of odd residue characteristic has complementary eigenspace projectors \((1\pm g)/2\). In rank two, each nontrivial involution is conjugate to \(\operatorname{diag}(1,-1)\), and the number of ordered complementary rank-one direct summands is \(5(5+1)\times25=750\); adding \(\pm I\) gives precisely \(752\) involutions in each ring. The direct enumeration verifies this independently of the classification.

## Verification
Compile `verify_orders.cpp` using `g++ -O3 -std=c++17 verify_orders.cpp -o verify_orders` and run `./verify_orders`. Compare standard output with `verification_output.txt`. The output totals, exact orders and both commuting counts must match. The program is closed, deterministic, needs no external data, and is included in this package. It computes each ring independently; no count is inferred from the other ring.

## Relationship to prior work
Singla (2010) proves that complex representation-degree distributions of general linear groups over length-two finite principal local rings depend only on the residue field, and describes exceptions to isomorphism of mixed- and equal-characteristic groups. This finding calculates an **involution product-order distribution**, which representation dimensions and class-count correspondence do not alone determine. In particular the two groups considered here are outside the small isomorphism exceptions in the cited introduction. No statement of the above exact finite product-order distribution was located in the inspected 2010 primary source or in relevant research-record searches. This does not establish historical priority against all possible broader character-table or two-involution results.

## Limitations
This is a finite exact result for the smallest odd prime outside the cited degree-two isomorphism exceptions; it is not an all-prime formula. A complete proof of a general inequality or a universal ring distinction is not claimed. Verification is same-model only and independent audit has not been performed.

## References
- P. Singla, *On Representations of General Linear Groups over Principal Ideal Local Rings of Length Two*, arXiv:1001.5304v1, 2010-01-29, introduction and Theorem 1.2.
- J. Fulman, R. Guralnick, D. Stanton, *Asymptotics of the number of involutions in finite classical groups*, arXiv:1602.03611v1, 2016-02-11 (field-group context, not a length-two pair-order count).

