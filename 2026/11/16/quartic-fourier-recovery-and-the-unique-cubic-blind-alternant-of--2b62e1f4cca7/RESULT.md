# Quartic Fourier recovery and the unique cubic blind alternant of three-by-three standard Young tableaux

## Finding

Let \(\mathcal T\) be the set of all standard Young tableaux of the square shape \(3\times3\). For integers \(j\in\{1,\dots,9\}\) and row-major cell indices \(c\in\{0,\dots,8\}\), set \(X_{j,c}(T)=1\) exactly when entry \(j\) occupies cell \(c\), and zero otherwise. Let \(V_d\subset\mathbb R^{\mathcal T}\) be the linear span of all products of at most \(d\) indicators \(X_{j,c}\), including the empty product.

**Theorem.** The complete degree-zero through degree-four rank hierarchy is

\[
(\dim V_0,\dim V_1,\dim V_2,\dim V_3,\dim V_4)=(1,11,31,41,42).
\]

Consequently three-entry joint location marginals fail to identify an arbitrary distribution on \(\mathcal T\) by exactly one signed direction; four-entry joint marginals do identify every distribution. The unique cubic blind signed direction has support 24, with 12 positive and 12 negative coefficients. The associated two supported probability measures disagree on an explicit four-entry event by \(1/12\).

## Assumptions and scope

A standard tableau is a filling of a \(3\times3\) array by \(1,\ldots,9\), increasing left-to-right and top-to-bottom. Each tableau is encoded by the *cell-order word* \(w=(w_1,\ldots,w_9)\), where \(w_j\) is the row-major index of the cell containing entry \(j\). Thus the cell poset is the product of two three-element chains. The hook-length product is \(8640\), so \(|\mathcal T|=9!/8640=42\).

An observation of order at most \(d\) is any joint probability fixing the cells of at most \(d\) distinct entries. The linear map from signed measures \(\nu\) to all such observations is dual to \(V_d\); its kernel has dimension \(42-\dim V_d\). Equivalently, encode a tableau by the \(81\)-bit incidence vector \( (X_{j,c})\). The degree-at-most-\(d\) Boolean Walsh characters \((-1)^{\sum_{(j,c)\in S}X_{j,c}}\), for \(|S|\le d\), have the same restricted span by the expansions \((-1)^x=1-2x\) and \(x=(1-(-1)^x)/2\).

## Proof

**The cubic blind alternant.** In the cell-order words, consider the subset \(\mathcal B\) consisting of all

\[
(0,(1,3)_\pi,(2,4,6)_\sigma,(5,7)_\tau,8),
\]

where \(\pi,\tau\) independently range over the two permutations of their indicated pairs, and \(\sigma\) over all six permutations of its indicated triple. These are all valid linear extensions of the square grid poset; hence \(|\mathcal B|=2\cdot6\cdot2=24\). Define \(\nu(T)\) to be the product of the permutation signs on the three blocks for \(T\in\mathcal B\), and zero elsewhere. Exactly 12 coefficients are positive, 12 negative.

Fix an event assigning cells to at most three entries. To prevent sign-reversing transposition cancellation in a block of size \(r\), such an event must fix at least \(r-1\) entries of that block. All three blocks would therefore require at least \(1+2+1=4\) fixed entries. At most three constraints leave two freely swappable entries in one block, and their transposition reverses \(\nu\) without changing the event. Thus \(\sum_{T\in\mathcal T}\nu(T)f(T)=0\) for every \(f\in V_3\).

Take \(\mu_+\) and \(\mu_-\) to be the uniform distributions on the 12 tableaux with \(\nu=+1\) and the 12 with \(\nu=-1\). They have identical observations through degree three. The event assigning entries \(2,4,5,7\) to row-major cells \(1,2,4,5\), respectively, selects precisely one tableau of \(\mathcal B\). The signed sum on this event is \(1\), so its probability differs by exactly \(1/12\) between the two measures.

**Exact ranks and uniqueness.** The finite calculation is expressed entirely as an exact integer computation. Enumerate linear extensions by repeatedly selecting a cell whose left and upper predecessor have already appeared. For each \(k\in\{0,\ldots,4\}\), and each compatible assignment of \(k\) entries to cells, form the vector \(v\in\{0,1\}^{42}\) recording which tableaux satisfy the assignment. Duplicate vectors may be discarded without affecting their span. For each \(d\), construct the integer Gram matrix \(G_d=\sum_{|J|\le d}v_Jv_J^\top\). Exact fraction-free Gaussian elimination gives the ranks \(1,11,31,41,42\) for \(d=0,1,2,3,4\). Since a matrix and its real Gram matrix have the same rank, these are precisely \(\dim V_d\). The nonzero columns at exact degrees zero through four yield, after per-degree deduplication, 1, 22, 130, 271 and 298 indicator vectors respectively. `verify_exact.py` gives the full executable rank certificate.

An independently implemented growth-by-shapes enumerator forms the same observation family by fixing cells rather than entries and computes the ranks over three primes \(1000003\), \(1000033\) and \(1000037\); every rank agrees with the exact result. This is `verify_independent.py`. In particular \(\dim V_3=41\), so the constructed \(\nu\) spans the *entire* cubic annihilator. As \(\dim V_4=42\), no nonzero signed measure is invisible at degree four. This completes the proof.

## Verification

Run `python3 verify_exact.py` and `python3 verify_independent.py` using Python 3 with no third-party dependencies. The first program asserts the complete tableau count, calculates all five ranks over the integers, confirms cubic annihilation, and checks the explicit four-point witness. The second independently enumerates tableaux via Young-shape growth and calculates the same rank hierarchy using three modular fields, which supplies independent lower-rank witnesses. Both were executed successfully on the bundled scripts. Finite exhaustive calculation is used only for this 42-point domain; no extrapolation to larger tableau shapes is claimed.

## Relationship to prior work

McKay, Morse and Wilf (first public version 2000-08-22) study joint prescribed-entry probabilities for natural *uniform* random-tableau laws, including more than one designated cell; their main theorems do not determine the rank or kernel of the observation map on **all** probability distributions on \(\mathcal T\). Pittel and Romik (2004) study asymptotic shapes and the positions of entries under the uniform law of larger square tableaux. De Loof, De Meyer and De Baets (2006) provide ideal-lattice algorithms for linear-extension counting and rank probabilities. These results motivate finite location observations but do not directly establish the five-rank hierarchy here. The simple tableau count and hook-length formula are classical and are not claimed as new.

## Limitations

The claim concerns only the \(42\) tableaux of shape \(3\times3\) and arbitrary finite signed or probability measures on them, with observations that name entries and cells. It does not address unknown-tableau reconstruction from jeu-de-taquin minors, the shape of a uniform random large tableau, or a general formula for larger rectangular shapes. Literature comparisons leave a residual possibility of an equivalent, unindexed incidence-rank computation. Exact finite computation and a proved alternating cancellation establish the claimed finite statement, not novelty by themselves.

## References

- B. D. McKay, J. Morse, and H. S. Wilf, *The distributions of the entries of Young tableaux*, arXiv:math/0008160 (first version 2000-08-22), https://arxiv.org/abs/math/0008160.
- B. Pittel and D. Romik, *Limit shapes for random square Young tableaux and plane partitions*, arXiv:math/0405190 (first version 2004-05-11), https://arxiv.org/abs/math/0405190.
- K. De Loof, H. De Meyer and B. De Baets, *Exploiting the lattice of ideals representation of a poset*, *Fundamenta Informaticae* 71 (2006), 309–321, https://doi.org/10.3233/FUN-2006-712-309.
