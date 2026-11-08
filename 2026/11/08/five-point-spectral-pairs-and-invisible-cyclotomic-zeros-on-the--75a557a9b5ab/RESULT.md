# Five-point spectral pairs and invisible cyclotomic zeros on the thirty-cycle

## Finding
Let \(G=\mathbb Z/30\mathbb Z\). For a five-element subset \(A\subseteq G\), an *exponential spectrum* is a five-element \(B\subseteq G\) such that \(\sum_{a\in A}e^{2\pi i a(b-b')/30}=0\) whenever \(b\ne b'\) belong to \(B\). Let \(s(A)\) count the distinct spectra as unordered subsets (not modulo translation), and let \(Z(A)\) be the set of orders \(d>1\) dividing 30 for which the cyclotomic polynomial \(\Phi_d\) divides \(P_A(X)=\sum_{a\in A}X^a\) in \(\mathbb Z[X]\).

Exactly \(7776\) of the \(\binom{30}{5}=142506\) five-element sets are spectral, namely the transversals of reduction modulo five. Their spectrum multiplicities have exactly four levels:

| Constraint on \(A\), in addition to being a transversal mod five | Number of such sets | \(s(A)\) |
| --- | ---: | ---: |
| Neither one parity nor one residue modulo three | 7200 | 6 |
| One parity but not one residue modulo three | 480 | 96 |
| One residue modulo three but not one parity | 90 | 486 |
| One residue modulo six | 6 | 7776 |

The total number of ordered spectral pairs \((A,B)\) is exactly \(179676\). Moreover, the *complete* Fourier-zero cyclotomic stratification, including nonspectral sets, is

| \(Z(A)\) | Number \(A\) | \(s(A)\) |
| --- | ---: | ---: |
| \(\varnothing\) | 127590 | 0 |
| \(\{6\}\) | 7020 | 0 |
| \(\{5\}\) | 6840 | 6 |
| \(\{5,6\}\) | 360 | 6 |
| \(\{5,10\}\) | 480 | 96 |
| \(\{5,15\}\) | 90 | 486 |
| \(\{6,30\}\) | 120 | 0 |
| \(\{5,10,15,30\}\) | 6 | 7776 |

Thus \(360\) spectral sets have an additional *order-six* Fourier zero that creates no additional exponential spectrum: the frequency-basis count is still six. This distinction between zeros and usable orthogonality patterns is the key qualitative feature.

## Assumptions and scope
All sets are subsets of the precisely specified finite cyclic group \(G\); every five-element subset is counted once. Frequencies and spatial points are represented by residues \(0,\ldots,29\). There are no arbitrary phase weights. An exponential spectrum consists of five *distinct* residues and is counted as an actual subset, without factoring translation or automorphism symmetries. A Fourier zero with additive order \(d\) means a primitive \(d\)-th root annihilates the indicator mask. The theorem is a finite exact classification, not an assertion concerning arbitrary cyclic orders.

## Proof
**1. Cyclotomic equivalence.** Write \(\zeta=e^{2\pi i/30}\). For distinct \(b,b'\), \(P_A(\zeta^{b-b'})=0\) if and only if \(\Phi_{30/\gcd(30,b-b')}\) divides \(P_A\). Thus a set \(B\) is a spectrum if and only if all ten pairwise difference orders belong to \(Z(A)\). This converts the problem into a finite exact integer divisibility and clique count; no numerical root-of-unity tolerance is needed.

**2. Exhaustive integer classification.** The attached independent file `CHECK.py` constructs every cyclotomic polynomial \(\Phi_d\) for \(d\mid30\), represents \(X^a\bmod\Phi_d\) by an exact integer vector, and evaluates all \(\binom{30}{5}=142506\) indicator masks using integer vector addition. It independently enumerates every five-frequency subset \(B\), takes the seven-bit union of its ten difference orders, then counts containment in each Fourier-zero mask. Integer assertions compare the complete resulting joint distribution against the eight rows above. This is an exhaustive finite certificate because both outer loops iterate the complete combinations of five distinct integers among \(0,\ldots,29\), and the cyclotomic-remainder criterion is an equivalence. The source is small, deterministic and standard-library-only.

**3. Why the nonzero spectrum counts have four levels.** A five-element set is a transversal modulo five precisely when its five primitive fifth-root contributions cancel. In that case \(\Phi_5\mid P_A\), and the verified zero classification allows exactly four further patterns. If \(Z(A)=\{5\}\), a five-frequency spectrum must lie in a coset of the order-five subgroup \(6G\), yielding six choices. Adding an order-six zero does not create a five-clique of permissible differences: any edge of order six shares its residue modulo five; an additional vertex joined to both endpoints by differences of orders five or six must lie in that same residue class modulo five. Induction then forces a putative five-clique to be contained in one six-point residue class modulo five, where pairwise differences of order six permit at most two vertices. Hence the extra \(\Phi_6\) zero contributes no new spectra.

If \(Z(A)=\{5,10\}\), allowed distinct frequency differences all have order five or ten, equivalently are nonzero multiples of three other than the order-two difference 15. Thus \(B\) lies in one residue class modulo three, choosing one element from each of its five antipodal pairs: \(3\cdot2^5=96\) spectra. If \(Z(A)=\{5,15\}\), allowed differences are even, and difference of order three is forbidden. Thus \(B\) lies in one parity class, picking one representative from each of five three-point cosets: \(2\cdot3^5=486\). Finally, for \(Z(A)=\{5,10,15,30\}\), the allowed pairwise differences have orders divisible by five, equivalently distinct residues modulo five; every transversal modulo five is a spectrum, giving \(6^5=7776\). The two nonspectral nonempty zero masks \(\{6\}\) and \(\{6,30\}\) admit no five-clique: every permitted nonzero frequency difference in either case is odd (orders six and thirty), so three distinct vertices would include two of the same parity and hence have a forbidden even difference.

**4. Counting sets.** Every transversal modulo five chooses independently one of the six representatives for each of the five residues, hence \(6^5=7776\) possibilities. Exactly \(2\cdot3^5=486\) are single-parity, \(3\cdot2^5=96\) are single-residue modulo three, and their intersection consists of six cosets of \(6G\). Inclusion-exclusion gives \(7776-486-96+6=7200\) generic sets, \(486-6=480\) one-parity-only sets, and \(96-6=90\) one-mod-three-only sets. Summing the four counts weighted by their spectrum multiplicities gives \(7200\cdot6+480\cdot96+90\cdot486+6\cdot7776=179676\). The independent cyclotomic-remainder census resolves the additional order-six split into 6840 and 360.

## Verification
Run `python3 CHECK.py` with Python 3 using only the standard library. It reports:

```
CHECK_OK total_sets=142506 spectral_sets=7776 ordered_spectral_pairs=179676
SPECTRUM_LEVELS 6:7200 96:480 486:90 7776:6
FOURIER_ZERO_ANOMALY order_6_extra=360 rank_effect=0
```

All cyclotomic computations, difference-order tests, and set-counting loops use exact integer arithmetic. Assertions compare the full eight-row zero distribution and all spectral multiplicities, not merely examples. No timeout, floating-point tolerance, or inference from a partial sample is used. The compact program is an exhaustive proof certificate for the fixed group of order thirty; the elementary reductions explain the structure behind its output.

## Relationship to prior work
The spectral–tiling equivalence in square-free cyclic groups and the criterion using cyclotomic divisibility are established background. In particular, Shi's theorem for three-prime cyclic groups, Malikiosis's structural results, and Somlai's 2026 square-free extensions supply the broader setting; none of their inspected statements gives the eight-stratum zero census, the four exact per-set spectrum multiplicities, or the 360 spectrally invisible order-six zeros. The novelty claim is about those precise counts and their interpretation, **not** about the established equivalence of spectrality and tiling or the cyclotomic method itself.

## Limitations
This is restricted to five-element subsets of the group of order thirty and frequency sets of cardinality five. The verification is exhaustive only in this fixed finite domain; it gives no theorem for arbitrary square-free groups. Unindexed equivalent enumerations of short cyclic Fourier masks, and relevant inaccessible full texts, remain possible publication-priority risks. Independent validation has not been performed.

## References
1. G. Somlai, *Fuglede's Conjecture on Cyclic Groups of Square-Free Order: The Case of Rapidly Growing Prime Factors*, arXiv:2607.26534, first public 2026-07-29, https://arxiv.org/abs/2607.26534.
2. R.-D. Malikiosis, *On the structure of spectral and tiling subsets of cyclic groups*, Forum of Mathematics, Sigma **10** (2022), e23, https://doi.org/10.1017/fms.2022.14.
3. R. Shi, *Fuglede's conjecture holds on cyclic groups of order \(pqr\)*, arXiv:1805.11261, https://arxiv.org/abs/1805.11261.
4. T. Y. Lam and K. H. Leung, *On vanishing sums of roots of unity*, Journal of Algebra **224** (2000), 91–109, https://doi.org/10.1006/jabr.1999.8089.
5. H. Tan and Y. Zhang, *Fuglede's Conjecture for Cyclic Groups of Square-free Order*, arXiv:2610.02218, https://arxiv.org/abs/2610.02218 (relevant abstract inspected; complete text inaccessible at review time).
