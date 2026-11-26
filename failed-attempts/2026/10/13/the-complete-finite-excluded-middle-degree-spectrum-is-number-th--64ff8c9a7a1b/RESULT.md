# The complete finite excluded-middle degree spectrum is number-theoretic
## Finding
For a finite nontrivial Heyting algebra \(H\), write
\[
d_{\mathrm{EM}}(H)=\frac{|\{a\in H:a\vee\neg a=1\}|}{|H|}.
\]
The set of all possible excluded-middle degrees is exactly
\[
\left\{\prod_{i=1}^r\frac{2}{n_i}:r\ge 1,\ n_i\ge2\right\}.
\]
Equivalently, if \(p/q\in(0,1]\) is in lowest terms, then \(p/q\) occurs if and only if either \(p=1\), or \(p=2^a\) for some \(a\ge1\), \(q\) is odd, and \(\Omega(q)\ge a\), where \(\Omega\) counts prime factors with multiplicity.

Thus, for example, \(2/3,1/2,4/9,2/5,4/15,8/27,16/81\) occur, whereas \(4/5,8/15,8/21,16/45,3/4,6/7\) do not.

## Assumptions and scope
The algebra is finite and nontrivial. The notation \(C_n\) denotes the \(n\)-element Heyting chain. Fractions in the arithmetic characterization are always reduced. No claim is made here about infinite Heyting algebras or about probability measures other than the uniform measure on a finite algebra.

## Proof
Bumpus and Kocsis identify the elements satisfying excluded middle with the Boolean center and prove multiplicativity of equation-satisfiability degrees under direct products. Their proof of the sharp \(2/3\) bound also shows that every nontrivial central element \(c\) yields a Heyting-algebra decomposition
\[
H\cong H_c\times H_{\neg c},
\]
where \(H_c=\{x:x\le c\}\).

Iterate this decomposition until no factor has a nontrivial central element. This gives
\[
H\cong H_1\times\cdots\times H_r,
\]
where every \(H_i\) has center \(\{0,1\}\). Put \(n_i=|H_i|\). Each factor has exactly two excluded-middle elements, so multiplicativity gives
\[
d_{\mathrm{EM}}(H)=\prod_{i=1}^r\frac{2}{n_i}.
\]
This proves necessity. Conversely, for arbitrary integers \(n_i\ge2\), the chain \(C_{n_i}\) has center exactly \(\{0,1\}\), so the product \(\prod_i C_{n_i}\) realizes the prescribed product of fractions. Hence the product description is exact.

For the number-theoretic form, write a product as \(2^r/N\), where \(N=\prod_i n_i\). Since each \(n_i\ge2\), one has \(\Omega(N)\ge r\). If the reduced numerator is \(1\), every \(1/q\) occurs already in \(C_{2q}\). Otherwise the reduced numerator is \(2^a\). Writing \(N=2^s q\) after cancellation gives \(a=r-s\), and
\[
s+\Omega(q)=\Omega(N)\ge r=s+a,
\]
so \(\Omega(q)\ge a\). Conversely, if \(q\) is odd and \(\Omega(q)\ge a\), partition the prime factors of \(q\), counted with multiplicity, into \(a\) nonempty groups. Their products \(q_1,\ldots,q_a\) satisfy \(q_i\ge3\) and \(q=\prod_i q_i\), while
\[
\prod_{i=1}^a d_{\mathrm{EM}}(C_{q_i})=\prod_{i=1}^a\frac2{q_i}=\frac{2^a}q.
\]
This proves the arithmetic criterion.

## Verification
An exact replay enumerates all \(4{,}473\) labelled posets on at most five points, constructs their upset Heyting algebras, computes negation and excluded-middle elements, decomposes each comparability graph into connected components, and checks both the product formula and the reduced-fraction criterion. It also checks the arithmetic equivalence on a finite box of product parameters and explicit positive and negative regression examples. The replay returns `VERIFY_OK 89093 exact assertions; 4473 labelled posets checked`.

## Relationship to prior work
Bumpus and Kocsis prove that excluded-middle elements form the Boolean center, prove multiplicativity under products, and use central splitting to establish the sharp \(2/3\) gap. Those ingredients make the present theorem a short structural and arithmetic extraction, but the paper does not state a complete spectrum of possible excluded-middle degrees or the reduced-fraction membership criterion. Direct full-text checks found no occurrences of “spectrum,” “possible values,” “prime factors,” or “factorization” in the source.

The familiar extremal families \(C_3\times C_2^k\) at degree \(2/3\) and \(C_4\times C_2^k\) at degree \(1/2\) appear as the first two rungs of this complete spectrum, but those two rungs alone do not determine the general product semigroup or the arithmetic membership test.

## Limitations
The derivation is short enough that an equivalent formulation may exist as uncatalogued folklore. The originality assessment is therefore a literature-search result, not a proof of historical priority. Independent audit has not yet been performed.

## References
Benjamin Merlin Bumpus and Zoltan A. Kocsis, “Degree of Satisfiability in Heyting Algebras,” arXiv:2110.11515; *Journal of Symbolic Logic* 90(2), 533–551, DOI: 10.1017/jsl.2024.2.
