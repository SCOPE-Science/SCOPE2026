# Scientific review: first nonmonotonicity of cyclotomic binomial filters

## Correctness

**PASS.** The statement uses exactly the rational-congruence normalization in Miska's Definition 2.2. Root-of-unity orthogonality gives an integer elementary-symmetric numerator divided by \(c!\). Pascal's identity reduces the infinite family over all integer arguments to the finite set \(0\le c<d\) at argument \(-1\). The provided checker uses an exact recurrence, checks every \((d,t,c)\) with \(2\le d\le36\), \(1\le t\le d\), \(0\le c<d\), and separately reconstructs each rational coefficient using reciprocals. Its threshold table, \(d=36\) passing-order list, and explicit reduced nondivisible witness establish the claims. The reasoning \(t\ge d\Rightarrow C_t(d)\) is an exact polynomial-degree identity; it closes the otherwise infinite order range. There are no numerical tolerances.

## Originality

**PASS subject to bibliographic limitations.** Miska's arXiv:2203.03281v1 was inspected through its definition, general theorem, exact finite-test lemma, sufficient-condition proposition, and final examples. It treats fixed-order classification (fully enumerating orders one through five) but does not state the sharp first failure of upward closure in order, the complete validity pattern at modulus \(36\), or the adjacent contrast between orders \(15\) and \(16\). Its Theorem 2.3 explicitly excludes exceptional mixed-prime moduli, which include the example for both relevant orders. Related recorded results on prime-base binomial congruences and Sun's multinomial congruence have different defining quantities and do not themselves imply the claim. Searches for aliases, the exact parameters, monotonicity, and tabulated profiles found no covering theorem; absence from those searches is not a uniqueness proof. The publisher's full version was not accessed, and an implicit or unindexed result is possible.

## Value

**PASS.** The fixed-order family is naturally organized by its cyclotomic filter order. Determining whether validity persists when that order increases is a structural question, not an arbitrary numerical curiosity. The result proves that a tempting upper-set or threshold picture is false, locates its least modulus, and completely classifies all orders at that boundary. A minimal counterexample with a complete congruence-profile certificate is a meaningful boundary theorem, albeit smaller in scope than a general classification of all nonmonotone moduli.

## Evidence and limitations

The source's binomial-congruence family and exact finite-test lemma are prior work, not newly claimed. The novel assertion is the exact first nonmonotone modulus and full order profile. Exhaustive computation is used only after a proved reduction of infinitely quantified integer arguments and all orders to finite exact arithmetic. The present analysis is not independent verification by an external researcher. The published journal full text was not inspected; the complete relevant arXiv preprint was read.

Self-review: passed. Independent audit: not yet performed.
