# The exact Paley-25 shattering polynomial and its exceptional triples

## Finding
Let \(P_{25}\) be the Paley graph on \(\mathbb F_{25}\). Its concept class is the family of **open** neighborhoods \(\mathcal N_{25}=\{N(y):y\in\mathbb F_{25}\}\); a query on \(x\) tests whether \(x-y\) is a nonzero square. Write \(\Phi_{25}(z)=\sum_{S\text{ shattered}}z^{|S|}\). The exact polynomial is
\[
\Phi_{25}(z)=1+25z+300z^2+2200z^3+3600z^4.
\]
In particular, \(\operatorname{VCdim}(\mathcal N_{25})=4=\lfloor\log_2 25\rfloor\), and \(P_{25}\) is the first Paley graph, by increasing permissible field order, with VC dimension \(4\) for its open neighborhoods.

The \(100\) nonshattered triples are precisely the **square-equilateral triples** \(\{u,u+d,u+\lambda d\}\), where \(u\in\mathbb F_{25}\), \(d\) is a nonzero square and \(\lambda^2-\lambda+1=0\). The \(3600\) shattered four-subsets have exactly eight orbits under the \(600\)-element affine semilinear group described below; their orbit sizes are \(600,600,150,600,600,600,300,150\).

## Assumptions and scope
Use \(\mathbb F_{25}=\mathbb F_5[t]/(t^2-2)\). Because \(2\) is nonsquare in \(\mathbb F_5\), this quotient is a field. Encode \(a+bt\) as the integer \(a+5b\), with \(0\le a,b<5\); these are only coordinate labels, not elements of the ring \(\mathbb Z/25\mathbb Z\). Set \(Q=\{x^2:x\in\mathbb F_{25}^{\times}\}\) and \(N(y)=y+Q\). There are exactly \(25\) concepts, one per possible center, and the zero difference is **not** a neighbor. Centers are allowed to lie inside a queried support. A support \(S\) is shattered when \(\{S\cap N(y):y\in\mathbb F_{25}\}=2^S\).

For the orbit statement use only the named subgroup \(G=\{x\mapsto a x^{5^\epsilon}+b: a\in Q,\ b\in\mathbb F_{25},\ \epsilon\in\{0,1\}\}\), of order \(12\cdot25\cdot2=600\). No claim is made about the group of all set-system symmetries.

## Proof
**Exact finite counting.** The accompanying dependency-free `paley25_verify.py` is a complete deterministic enumeration, not statistical sampling. In the field representation above, the program constructs all \(12\) nonzero squares, and for each unordered support \(S\) computes all \(25\) traces \(S\cap N(y)\) as distinct binary masks. A support of cardinality \(s\) is shattered if and only if every one of its \(2^s\) possible trace masks occurs. The program implements this test twice: directly as a set of trace masks, and independently as nonempty intersections of neighborhood-bitset fibers. The two methods are asserted equal for every support containing zero of sizes at most four. Translation by a field element preserves every trace profile and supplies an exact orbit-count identity: for \(s>0\), the total number of shattered \(s\)-subsets equals \(25/s\) times the number of shattered \(s\)-subsets containing zero (count incidences of shattered subsets with their \(s\) elements). For four-subsets the program also independently visits **all** \(\binom{25}{4}=12650\) supports without translation reduction.

The exhaustive check yields exactly \(25,300,2200,3600\) shattered subsets at sizes \(1,2,3,4\), respectively. At size five, shattering would require at least \(2^5=32\) distinct center traces, but only \(25\) centers exist. Therefore no support of size at least five is shattered, giving the entire polynomial and the exact dimension. A concrete four-point witness is \(S=\{0,2,5,10\}\), with a center for each label mask, in binary mask order \(0\) through \(15\):

```
5 24 0 21 7 17 8 1 16 2 19 3 11 9 14 6
```

**Exceptional triples.** The same unrestricted finite test visits every one of the \(\binom{25}{3}=2300\) triples. Exactly \(100\) fail. In \(\mathbb F_{25}\), the equation \(\lambda^2-\lambda+1=0\) has exactly the encoded roots \(13\) and \(18\). The verifier separately constructs \(\{u,u+d,u+\lambda d\}\) for every \(u\), every \(d\in Q\), and these roots; deduplicating produces precisely \(100\) triples, and equality of this generated set with the complete set of failures is explicitly asserted. Thus the classification is exact, not a guess based on a sample.

**Four-set orbit certificate.** Multiplication by a square, translation, and the Frobenius map \(x\mapsto x^5\) each preserve adjacency, hence preserve the shattering property. The verifier applies every one of the \(600\) such maps to each unassigned shattered quadruple, checks every resulting quadruple is in the independently enumerated shattered list, and removes its complete orbit. The eight orbit representatives in integer field coordinates, followed by orbit sizes, are:

```
(0,1,2,5):600; (0,1,2,8):600; (0,1,5,6):150;
(0,1,5,11):600; (0,1,5,15):600; (0,1,5,23):600;
(0,1,8,15):300; (0,1,10,11):150.
```

Their sum is \(3600\), and the remaining list is empty. No orbit relies on a guessed symmetry or an unchecked stabilizer.

**First admissible field order.** The prime powers congruent to \(1\) modulo \(4\) and less than \(25\) are \(5,9,13,17\). The same exhaustive program computes their complete support coefficients through degree four, giving dimensions \(2,2,3,3\), respectively. A class of \(q<16\) or \(q=17\) concepts could in principle shatter at most \(\lfloor\log_2 q\rfloor\) points, and the exhaustive checks settle the remaining cases. Hence \(25\) is the first allowed Paley order with VC dimension four.

## Verification
Run `python3 paley25_verify.py` with a standard Python 3 interpreter. It requires only the standard library. All field operations, trace tests, cardinalities and orbit actions are reconstructed from the code, without downloaded graph tables. It prints `PALEY25_SHATTERING_PASS` after asserting every result. The full direct quadruple pass checks \(12650\) four-subsets, while the triple exceptional-set comparison checks all \(2300\) triples. All calculations are finite and fully exhausted; no inference from partial enumeration to an infinite assertion is used. The available check is reproducible but not an independent external mathematical audit.

## Relationship to prior work
McDonald, Sahay and Wyman [1] formulate the same additive-translate VC dimension and prove asymptotic character-sum bounds. Their Proposition 1.7 describes translation/dilation invariance; this is acknowledged, not presented as new. Their numerical section explicitly restricts to **prime** fields and does not provide the degree-by-degree Paley-25 counts, the exceptional-triple criterion or four-set orbit census. Pham, Senger, Tait and Nguyen [2] give general pseudorandom-graph bounds, not the exact present finite-field classification. Coudert and coauthors [3] give general algorithms for graph VC dimension, using **closed** neighborhoods in their stated convention; a general computability algorithm is not an already tabulated answer for this open-neighborhood family. None of the inspected material supplies these particular coefficients or orbit classifications.

## Limitations
The enumeration and structural facts concern the single field order \(25\) and the listed four smaller Paley orders only; no all-prime-power formula is claimed. This is a finite exact result, conditional on faithfully executing the included complete exhaustive checker, and its historical priority has not been independently certified. The chosen affine semilinear subgroup is not asserted to equal every automorphism of every related incidence structure. Graph conventions using **closed** neighborhoods or forbidding hypothesis centers within the support define different trace systems and are outside this result. The explicit smallest-order statement ranges over prime-power orders admitting undirected Paley graphs, not arbitrary pseudorandom graphs.

## References
[1] B. McDonald, A. Sahay and E. L. Wyman, *The VC-dimension of quadratic residues in finite fields*, arXiv:2210.03789, first public 2022-10-07; especially Definitions 1.1–1.2, Proposition 1.7, and §4. https://arxiv.org/abs/2210.03789

[2] T. Pham, S. Senger, M. Tait and Nguyen Thu-Huyen, *VC-dimension and pseudo-random graphs*, arXiv:2303.07878, first public 2023-03-14. https://arxiv.org/abs/2303.07878

[3] D. Coudert, M. Csikós, G. Ducoffe and L. Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588, first public 2024-05-13. https://arxiv.org/abs/2405.07588
