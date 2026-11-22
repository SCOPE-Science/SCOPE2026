# Two persistent Frobenius ambiguities in genus-four hyperelliptic spin schemes, and a sharp five-extension recovery theorem

## Finding

Let \(q\) be odd and \(C/\mathbb F_q\) any smooth genus-four hyperelliptic curve whose branch divisor consists of ten distinct geometric points. Let \(W_o\) and \(W_e\) be the finite étale schemes of its geometrically odd and even theta characteristics, of degrees \(120\) and \(136\). Write \(\lambda\vdash10\) for the cycle partition of arithmetic Frobenius on the ten branch points, and let \(O_n=|W_o(\mathbb F_{q^n})|\) and \(E_n=|W_e(\mathbb F_{q^n})|\).

**Theorem.** As \(\lambda\) ranges over the \(42\) partitions of ten, the ordered pair of full Frobenius orbit spectra on \((W_o,W_e)\) has exactly \(40\) possibilities. Exactly two distinct-partition pairs share both spectra:

* \(\lambda=(8,2)\) and \(\lambda=(8,1,1)\): odd cycles \(4^2 8^{14}\), even cycles \(1^2 2^1 4^1 8^{16}\).
* \(\lambda=(4,4,2)\) and \(\lambda=(4,4,1,1)\): odd cycles \(2^4 4^{28}\), even cycles \(1^4 2^2 4^{32}\).

Here \(d^m\) denotes \(m\) Frobenius orbits each of length \(d\), not exponentiation of geometric objects. The odd scheme alone has \(40\) different spectra; the even scheme alone has \(37\).

**Sharp bounded-extension recovery.** The five pairs of integer counts
\[
((O_1,E_1),(O_2,E_2),(O_3,E_3),(O_4,E_4),(O_5,E_5))
\]
determine the *complete* Frobenius orbit spectra, and hence the exact finite-scheme zeta functions of both \(W_o\) and \(W_e\). No first-four-extension version has this property. The number of distinguishable joint profiles from the first \(1,2,3,4,5\) extension degrees is respectively \(22,33,39,39,40\). In particular, the partitions \((10)\) and \((5,5)\) have the same count pairs \((O_n,E_n)=(0,1)\) for every \(1\le n\le4\), but for \(n=5\) their counts are \((0,16)\) and \((120,136)\). Both partitions are realized by squarefree degree-ten polynomials over \(\mathbb F_3\).

A separate sharp statement is that every such genus-four curve acquires an odd theta characteristic over an extension of degree at most \(10\); for a transitive ten-cycle all \(120\) odd characteristics lie in twelve degree-ten orbits, so this degree bound cannot be lowered.

For each of the \(42\) branch partitions, the complete exact odd/even cycles and first-five-extension counts are given in the bundled `spin_spectra_42.tsv`. An executable, dependency-free verifier is bundled as `verify_genus4_spin.py`.

## Assumptions and scope

The base field is any finite field of odd characteristic, including nonprime fields. The curve is geometrically smooth and hyperelliptic of genus four; it need not admit a rational branch point. A convenient affine model is \(y^2=f(x)\) with \(f\) a squarefree polynomial of degree ten, although the group-theoretic result also covers branch configurations with infinity included. Odd and even theta characteristics refer to geometric line-bundle classes \(L\) with \(L^{\otimes 2}\simeq\omega_C\), classified by the parity of \(h^0(C_{\overline{\mathbb F}_q},L)\). As the base is a finite field and these schemes are finite étale in odd characteristic, geometric Frobenius-fixed classes are rational points of the corresponding finite schemes. We count objects, not isomorphism classes of hyperelliptic curves.

## Proof

**1. Canonical subset model.** Let \(P_1,\ldots,P_{10}\) be the geometric ramification points, and \(H\) a fiber of the hyperelliptic degree-two map. The standard relations are \(2P_i\sim H\), \(K_C\sim3H\), and \(P_1+\cdots+P_{10}\sim5H\). The \(120=\binom{10}{3}\) odd theta characteristics are represented uniquely by divisors \(P_i+P_j+P_k\) for distinct triples. The \(136\) even characteristics are the ten classes \(P_i+H\) and the \(126=\frac12\binom{10}{5}\) classes \(\sum_{i\in S}P_i-H\), where \(|S|=5\) and \(S\) and its complement are identified. Each represents a square root of \(K_C\), and the classical normal-form theorem for hyperelliptic theta characteristics says these are all distinct except for the stated five-subset complementation. Their respective dimensions of sections have parity odd (triple) and even (singleton and five-subset class). The construction commutes with every permutation of branch points, in particular with arithmetic Frobenius.

**2. Explicit fixed-point formula.** Fix an extension degree \(n\ge1\). If the cycle lengths of \(\operatorname{Frob}_q^n\) on the ten branches are \(\ell_1,\ldots,\ell_c\), write \(m_j=\#\{i:\ell_i=j\}\). A fixed three-subset is a union of cycles, hence
\[
O_n=\binom{m_1}{3}+m_1m_2+m_3.
\]
The first even component contributes \(m_1\) singleton classes. A class of complementary five-subsets is fixed exactly if Frobenius either fixes either representative or exchanges the two representatives. The number of invariant five-subsets is the coefficient
\[
 b_5=[z^5]\prod_{i=1}^{c}(1+z^{\ell_i}).
\]
The number of five-subsets that Frobenius carries to their complements is \(a_5=2^c\) if all the \(\ell_i\) are even, and \(a_5=0\) otherwise: along each even cycle one must alternate membership, with two possible starting signs. In either case precisely five of the ten elements are selected. Since two complementary subsets represent one even characteristic, the exact formula is
\[
E_n=m_1+\frac{b_5+a_5}{2}.
\]
This derivation applies in every odd characteristic and to each power of Frobenius. For a branch cycle of length \(d\), its \(n\)-th power consists of \(\gcd(d,n)\) cycles of length \(d/\gcd(d,n)\), making the formulas explicit from \(\lambda\) alone.

**3. Complete finite classification with a bounded certificate.** Every permutation of ten objects is conjugate to exactly one of the \(42\) integer partitions \(\lambda\vdash10\). The bundled standard-library verifier constructs all of them recursively in nonincreasing order. For each, it independently (A) traverses every orbit of the induced permutation on all \(120\) three-subsets and all \(10+126=136\) even subset classes, and (B) evaluates the formulas in Step 2 for all powers \(1\le n\le\operatorname{lcm}(\lambda)\) and compares against the orbit cycle counts. This is *exhaustive finite proof*, not sampling curves: every possible Frobenius conjugacy class of the ten-branch permutation occurs among the \(42\) cases; every point of each spin set is visited; the complete list of powers through the permutation order checks every periodic fixed-point count. The resulting verified table yields exactly \(40\) distinct joint orbit spectra, with the two pairs listed above and no others. The same table gives \(40\) odd spectra and \(37\) even spectra.

**4. Sharp five-extension recovery.** Enumerating the exact fixed-point formulas for the first \(n\) extensions for \(n=1,2,3,4,5\), the exact numbers of equivalence classes are \(22,33,39,39,40\). At \(n=5\), two branch types have identical first-five signatures if and only if they already have identical full joint spectra. Thus these five count pairs determine both zeta functions. The explicit spectra for \(\lambda=(10)\) are odd \(10^{12}\), even \(1^1 5^3 10^{12}\); for \(\lambda=(5,5)\) they are odd \(5^{24}\), even \(1^1 5^{27}\). They agree on the first four extension count pairs and disagree on the fifth, proving optimality. For a finite permutation scheme with orbit multiplicities \(c_d\), the zeta function is \(\prod_d(1-T^d)^{-c_d}\).

**5. Explicit realizations and sharp odd descent.** Over \(\mathbb F_3\), put
\[
 Q=x^2+1,\quad A=x^4+x+2,\quad B=x^4+2x+2,\quad H=x^8+x^2+2,
\]
\[
 D_1=x^5+2x+1,\quad D_2=x^5+2x+2,\quad F=x^{10}+2x^2+1.
\]
Every one of these seven monic polynomials is irreducible over \(\mathbb F_3\), as checked by the standard finite-field irreducibility test \(x^{3^d}\equiv x\pmod f\) and the associated gcd conditions for each prime divisor of \(d=\deg f\); the verifier includes all exact polynomial arithmetic and checks. The squarefree sextuple of degree-ten polynomials \(HQ\), \(Hx(x-1)\), \(ABQ\), \(ABx(x-1)\), \(F\), \(D_1D_2\) realizes respectively the six branch types \((8,2)\), \((8,1,1)\), \((4,4,2)\), \((4,4,1,1)\), \((10)\), \((5,5)\). Their curves \(y^2=f(x)\) are smooth genus four. All \(42\) partitions occur over sufficiently large odd finite fields, but over a small fixed field some partitions cannot occur (for example, ten rational branch points are impossible over \(\mathbb F_3\)). The six patterns needed for the two ambiguity pairs and for the sharp-cutoff example are exhibited over \(\mathbb F_3\); the sharp odd-descent lower bound is realizable over *every* finite field of odd order because an irreducible degree-ten polynomial exists over every finite field. A transitive ten-cycle acts on all odd three-subsets in twelve ten-cycles, proving the maximal minimal descent degree of ten.

## Verification

The exact standalone verifier `verify_genus4_spin.py` uses only the Python standard library, creates `spin_spectra_42.tsv` deterministically, and checks all \(42\) cycle types by direct orbit traversal and the independent closed fixed-point formulas for every power through the permutation order. It also verifies each claimed exact number of distinct spectra, both exceptional joint collisions, all first-five-extension signatures, the sharp example and the irreducibility of the seven explicit \(\mathbb F_3\) polynomials. Invocation: `python3 verify_genus4_spin.py` in the same directory as this file; compare the resulting TSV with the bundled TSV. The resulting success marker is `GENUS4_HYPERELLIPTIC_SPIN_42_TYPES_40_JOINT_SPECTRA_VERIFIED`. The mathematical proof of the infinite-field-uniform assertion is the classical branch-subset description plus the fixed-point formula; the finite enumeration covers all \(42\) permutations, not finitely many sampled finite fields.

## Relationship to prior work

Braden and Disney-Hogg, *Orbits of Theta Characteristics* (2024 preprint, subsequently published), study automorphism-group orbit actions on theta characteristics, with selected low-genus examples. Their results motivate studying these orbits but do not present this universal arithmetic Frobenius cycle census or its sharp recovery cutoff for arbitrary genus-four hyperelliptic branch cycle partitions. Eilers, *Rosenhain–Thomae Formulae for Higher Genera Hyperelliptic Curves* (2018), supplies classical hyperelliptic theta-subset geometry; that description is used and credited, not claimed as new. Misme, *Computing Theta Characteristics and their Galois action on general curves of moderate genus* (2026), describes Galois-theta algorithms and examples on general curves; its available full-text examples do not show the present universal \(42\)-type finite-field hyperelliptic result. A published study of a two-parameter genus-four hyperelliptic Jacobian-square family determines only four branch-point Frobenius types for that **specific family**, not these theta spectra for all \(42\) types. The contribution here is the complete exact spin-scheme arithmetic comparison, its two inescapable ambiguities, and the sharp five-extension determination of the induced zeta functions.

## Limitations

The five-extension signature recovers the pair of theta *zeta functions*, not necessarily the branch partition: exactly the two pairs of permanently ambiguous partitions remain indistinguishable by all extension counts. Nor does the theorem reconstruct branch coordinates, distinguish nonisomorphic curves sharing a branch partition, or compute the Hasse–Weil zeta function of the curve itself. The result is for odd characteristic only. A potentially equivalent older group-theoretic cycle table or an unindexed theorem deriving the same spectra from the standard theta-subset correspondence cannot be excluded; scientific priority should be independently checked before publication. No independent audit is claimed.

## References

1. H. W. Braden and L. Disney-Hogg, *Orbits of Theta Characteristics*, arXiv:2404.09890v1, first public 15 April 2024, https://arxiv.org/html/2404.09890v1 .
2. K. Eilers, *Rosenhain–Thomae Formulae for Higher Genera Hyperelliptic Curves*, Journal of Nonlinear Mathematical Physics 25 (2018), doi:10.1080/14029251.2018.1440744, https://www.atlantis-press.com/journals/jnmp/125950502/view .
3. T. Misme, *Computing Theta Characteristics and their Galois action on general curves of moderate genus*, arXiv:2610.29449 (2026), https://arxiv.org/abs/2610.29449 .
4. Published study, *Four Frobenius types in a two-parameter genus-four Jacobian-square family*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-four-frobenius-types-in-a-two-parameter-genus-four-jacobian-squa--9c29cb326f10 .
