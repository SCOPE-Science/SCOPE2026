# Independent mathematical audit

## correctness

PASS

Exact GP(n,2) closed-neighborhood GF2 equations give y_i=1+x_{i-1}+x_i+x_{i+1} and x_j+x_{j+1}+x_{j+5}+x_{j+6}=0, hence differences a_j=x_j+x_{j+1} are five-periodic and x has period <=10. Cyclic compatibility leaves 2/4 patterns if 5∤n, 32 if odd multiple of five, and 64 if 10|n. Five-period patterns have weights 3,5,7 with multiplicities 10,12,10; 32 twisted ten-period patterns have weight n. Independent 10-seed enumerator, corrected to deduplicate repeated seeds for n<10, reproduced each weight histogram for n=5..50. General theorem rests on recurrence and complete 32-pattern classification.

## originality

PASS

The published same-family Lights Out literature treats homogeneous kernel nullity/weight structure; the submitted problem is the fixed nonzero-syndrome coset (I+A)s=1, whose weight enumerator is not determined by the homogeneous weight enumerator alone. Caro–Klostermeyer odd domination framework and Hatzl–Wagner generic parity algorithms do not evaluate this GP(n,2) affine coset; Wang–Zhang exact-one code problem is stricter, and similarly numbered induced-matching optimum counts edges rather than odd-dominating vertex subsets. Resultary yielded a separate GP(n,3) all-on result and differently defined GP(n,2) domination results, no earlier identical affine enumerator. Best-of-knowledge PASS, with old primary-source gaps.

## value

PASS

Odd domination and Lights Out are standard closed-neighborhood binary codes; determining the complete all-on coset weight distribution on the classic generalized Petersen family is a natural exact invariant. The sharp divisibility-by-five optimum shift and count of exactly ten minimizers provide a structural census beyond general solvability or kernel dimension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
