# Exact semilinear orbit classification of zero-Welch three-spaces over \(\mathbb F_{512}\)

## Finding
Let \(F=\mathbb F_2[t]/(t^9+t^4+1)\), and for each \(\mathbb F_2\)-linear three-space \(E\le F\), put
\[
S(E)=\sum_{x\in E}x^{19}.
\]
The \(1606\) spaces with \(S(E)=0\) form exactly **two** orbits under the semilinear transformations \(E\mapsto a E^{2^j}\) (\(a\in F^\times\), \(0\le j<9\)). Their sizes are \(73\) and \(1533\). The orbit of size \(73\) is the family \(\{a\mathbb F_8:a\in F^\times\}\), where \(\mathbb F_8\) is the unique subfield with eight elements. The larger orbit is represented by
\[
E_0=\langle 1,t^3,t^8+t^7+t^6+t^5\rangle_{\mathbb F_2}.
\]
Under scalar multiplication alone there are exactly four orbits: one of length \(73\) and three of length \(511\); Frobenius cyclically permutes the latter three. This describes all configurations, not only their number.

## Assumptions and scope
The quotient polynomial \(t^9+t^4+1\) is irreducible over \(\mathbb F_2\), so \(F\) has order \(512\). Field elements are represented by nine-bit coefficient vectors; addition is bitwise exclusive-or, multiplication is binary polynomial multiplication reduced modulo the indicated polynomial. The element \(t\) is the class of the indeterminate. For sets, \(E^{2^j}=\{x^{2^j}:x\in E\}\). Only linear (not translated affine) three-spaces are classified. The Welch exponent is \(2^4+3=19\).

## Proof
**1. Symmetry and the exceptional subfield.** For nonzero \(a\), the Welch sum satisfies \(S(aE)=a^{19}S(E)\). The Frobenius operation gives \(S(E^2)=S(E)^2\); both preserve vanishing. Since \(3\mid9\), the field contains exactly one \(\mathbb F_8\). In its nonzero cyclic multiplicative group of order seven, \(19\equiv5\pmod7\), hence \(\sum_{x\in\mathbb F_8}x^{19}=\sum_{x\in\mathbb F_8^\times}x^5=0\). Thus every scalar multiple \(a\mathbb F_8\) is a solution. The stabilizer of \(\mathbb F_8\) under \(F^\times\) has order seven, yielding \(511/7=73\) distinct spaces.

**2. Normalized spaces and the finite certificate.** Every three-space containing \(1\) is \(\langle1,u,v\rangle_{\mathbb F_2}\) for independent residue classes of \(u,v\) modulo \(\langle1\rangle\). There are therefore \(\genfrac{[}{]}{0pt}{}{8}{2}_2=(255\cdot254)/6=10795\) such spaces. Enumerate all \(2\le u<v<512\), form the eight possible exclusive-or sums of \(1,u,v\), retain the sets of cardinality eight, and deduplicate. For each, evaluate the exclusive-or of the eight exact field powers of exponent \(19\). There are exactly \(22\) zero-sum normalized spaces.

For a normalized solution \(E\), all its normalized scalar representatives are precisely \(u^{-1}E\) for \(u\in E^\times\). The \(22\) zero-sum normalized spaces split into four disjoint classes of cardinalities \(1,7,7,7\). The singleton is the explicitly checked subfield \(\mathbb F_8\). The three seven-element classes correspond to scalar orbits of length \(511\). Frobenius fixes the singleton and induces a three-cycle on the other classes. Thus the semilinear orbit sizes are \(73\) and \(3\cdot511=1533\).

**3. Explicit generic representative.** The eight elements of \(E_0\), in nine-bit integer encoding, are exactly \(\{0,1,8,9,480,481,488,489\}\). The certificate checks their degree-three linear independence and their exact zero Welch sum. It also verifies that their seven normalizations are distinct and that Frobenius sends their class successively through all three seven-member classes, proving the claimed representative and orbit structure.

**4. Independent count via literature.** Direct trace arithmetic gives the binary Kloosterman sum \(\operatorname{Kl}_{9}=-5\). Theorem 1.1 of Cheng--Hu yields exactly \((511)(513-3(-5))/168=1606\) zero-Welch three-spaces and \((513-3(-5))/24=22\) containing one. These published formulas corroborate, but do not supply, the new orbit decomposition.

## Verification
Run `python3 welch9_orbits_verify.py` using the standard library. The script checks irreducibility by Rabin's criterion; all nonzero field inverses; all \(10795\) normalized three-spaces; all \(22\) zero-sum configurations; their exact partition into normalization classes; the Frobenius permutation; the two explicit representatives; and independently the \(511\)-term Kloosterman sum. All arithmetic is finite, exact, and exhaustive. The output includes `CERTIFICATE_OK` and `SEMILINEAR_ORBITS (73, 1533) TOTAL 1606`.

## Relationship to prior work
Cheng and Hu, *Counting subspaces with prescribed Welch sums* (arXiv:2610.15694v1, publicly released 11 October 2026), prove an exact total count for every odd degree via Kloosterman sums (Theorem 1.1) but do not classify the scalar or semilinear equivalence classes for degree nine. Hou and Zhao, *Further Results on Sum-Freedom of Binary and q-ary Functions* (arXiv:2609.31489v1), formulated the third-order Welch sum-freedom conjecture and reported finite checks. A previously published construction already supplies the \(\mathbb F_8\) zero-sum example for all odd degrees divisible by three; that example is explicitly credited here. Earlier work also classified a degree-seven zero-Welch family as one scalar orbit. What is established here is the complete, distinct degree-nine **two-orbit classification**, including the three generic scalar classes and their Galois relation. No claim of a new existence theorem or a new formula for the total count is made.

## Limitations
This is an exact result for the field with \(512\) elements. It makes no assertion about the semilinear orbit decomposition for larger fields. The published Kloosterman counting theorem is used for an independent check of the total; the exhaustive finite certificate independently obtains the orbit classification. Equivalent orbit data could exist in an unindexed older table. Independent mathematical validation has not been performed.

## References
1. K. Cheng and J. Hu, *Counting subspaces with prescribed Welch sums*, arXiv:2610.15694v1 (2026), especially Theorem 1.1 and Sections 3--4. https://arxiv.org/html/2610.15694v1
2. X.-D. Hou and S. Zhao, *Further Results on Sum-Freedom of Binary and q-ary Functions*, arXiv:2609.31489v1 (2026). https://arxiv.org/abs/2609.31489
