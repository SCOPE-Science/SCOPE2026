# Exact enumeration of ternary bigram-uniquely-decodable words

## Finding

Let \(\Sigma=\{0,1,2\}\). A word \(w=w_1\cdots w_n\in\Sigma^n\), with \(n\ge1\), is **bigram-uniquely-decodable** if it is the only word with its complete vector of ordered adjacent-pair frequencies. In particular the vector records the count of each \(ab\in\Sigma^2\), and the first and last letters can be inferred from this vector when they differ; in the Eulerian case where they agree the initial vertex is part of the reconstruction convention. To avoid any ambiguity in conventions, this result explicitly observes the first and last letter as well as the nine bigram counts. Define \(S_n\) to count uniquely reconstructible indexed words under that observation, and \(S_0=1\).

The exact counts are
\[
S_0=1,\qquad (S_1,S_2,S_3,S_4,S_5)=(3,9,27,69,135),
\]
and, for every integer \(n\ge6\),
\[
\boxed{S_n=3n^2+27n-63.}
\]
Equivalently,
\[
\boxed{\sum_{n\ge0}S_nz^n=\frac{1+3z^2+8z^3+12z^4-18z^6-12z^7+12z^8}{(1-z)^3}.}
\]
For a uniformly sampled indexed ternary word, the reconstruction-unique probability is \(S_n/3^n\sim3n^2/3^n\).

## Assumptions and scope

The alphabet is labeled and has exactly three symbols. Words are linear rather than cyclic, their positions are indexed, and all nine **oriented** contiguous bigram multiplicities are observed, along with the two endpoint symbols. Every word is counted once, not up to reversal, relabeling or rotation. A reconstruction is considered different if even one position changes. The enumerator does **not** count merely attainable read profiles or cyclic Markov types; it counts the singleton fibers of the stated observation.

## Proof

**1. Obstruction criterion.** Let \(B(w)\) denote the pair-frequency multiset together with the endpoints. The local obstruction theorem of Kontorovich and Trachtenberg (2011), Theorem 2, characterizes nonunique bigram reconstruction by the simultaneous presence, for some ordered triple \((x,a,b)\) with \(a\ne x\) and \(b\ne x\), of (i) a factor matching \(ax(\Sigma\setminus\{a\})^*b\) and (ii) a factor matching \(a(\Sigma\setminus\{x\})^*b\). The two occurrences may appear in either order and may overlap. There are exactly twelve triples over \(\Sigma\).

**2. Finite-state exact realization.** For each triple, attach a pair of states \((i,j)\). The first component \(i\in\{0,1,2,3\}\) indicates respectively: no active first-pattern prefix; suffix \(a\); suffix \(ax(\Sigma\setminus\{a\})^*\); or a completed first-pattern match. The second component \(j\in\{0,1,2\}\) analogously tracks no active second-pattern prefix, a suffix \(a(\Sigma\setminus\{x\})^*\), or a completed second-pattern match. Completed flags are absorbing. Reading a new letter \(c\), these components update exactly by the conditional cases in the standalone `verify_automaton.py`; any transition in which both flags have completed is rejected. Starting with all \((0,0)\), breadth-first search reaches exactly 247 nonreject product states. All 247 are accepting because absence of a completed pair means no obstruction has yet arisen. If \(M\) is their \(247\times247\) integer adjacency matrix (multiplicity of letters labeling an allowed transition) and \(e_0\) the starting-state unit column, the obstruction theorem gives
\[
S_n=e_0^{\mathsf T}M^n\boldsymbol 1\qquad(n\ge0).
\]
The code constructs this matrix implicitly from the transition definitions; it does not store a separately trusted numerical table.

**3. Finite exact certificate and infinite recurrence.** The supplied checker, using only arbitrary-precision integer arithmetic and deterministic finite-state enumeration, verifies the full **247-coordinate vector identity**
\[
\boxed{M^6(M-I)^3\boldsymbol1=\boldsymbol0.}
\]
Every component is calculated, not just its projection onto \(e_0\). Multiplication by \(M^{n-6}\) now proves for every integer \(n\ge6\)
\[
S_{n+3}-3S_{n+2}+3S_{n+1}-S_n=0.
\]
The exact starting values at \(n=6,7,8\) are \(207,273,345\). Consequently the sequence is quadratic from \(n=6\) onward, and solving for its coefficients gives \(3n^2+27n-63\). The five preceding values are computed by the same transitions. Multiplying the complete generating series by \((1-z)^3\) produces the displayed numerator. Since the numerator and recurrence are exact identities, checking finite word lengths is not being used as proof of the infinite formula.

## Verification

Execute `python3 verify_automaton.py` from the directory containing the package files. The checker rebuilds the twelve simultaneous pattern detectors, all 247 reachable states, the exact continuation vectors \(M^n\boldsymbol1\), and the length-six vector identity; it also reports the initial values and compares with brute-force reconstruction counts through length ten. Execute `python3 verify_profiles.py` for a separate direct enumeration of every ternary indexed word through length ten, computing the nine oriented bigram counts and endpoints literally and checking all singleton fibers. Both scripts require only the Python standard library. The output messages include the success checks. The finite vector identity, together with the cited obstruction theorem and commutativity of polynomials in \(M\), completes the all-length proof.

## Relationship to prior work

Kontorovich (2004) established the regularity of uniquely decodable \(n\)-gram embeddings and described valid and singleton bigram profiles. Kontorovich and Trachtenberg (arXiv:1111.6431, first posted November 28, 2011) supplied the explicit obstruction criterion and the small-alphabet deterministic automaton framework, including a reported minimal ternary deterministic automaton with 84 states. These earlier recognition results are not claimed here as new. The present contribution is the explicitly evaluated all-length enumerator, its exact quadratic tail and rational generating function for **linear ternary singleton read fibers**. Counts of all feasible linear two-gram multispectra, constrained homopolymer-free profiles, and uniquely recoverable cyclic necklaces are different enumerands, even where similar graph-theoretic tools apply.

## Limitations

The claim is restricted to three symbols, to complete oriented adjacent-pair frequencies with endpoint knowledge, and to one indexed linear word. It does not determine the exact coefficient law on arbitrary alphabet sizes or for longer reads. The verification programs establish the finite-state identities independently of heuristics, but the obstruction equivalence is cited from primary literature rather than reproved in full. A relevant 2004 original full text was not accessible during this review; its abstract establishes regularity and singleton-profile classification, but a possible unindexed explicit specialization remains a historical-priority risk. No independent mathematical audit is asserted.

## References

1. L. Kontorovich, “Uniquely decodable n-gram embeddings,” *Theoretical Computer Science* 329 (2004), 271–284. DOI: https://doi.org/10.1016/j.tcs.2004.10.010 (bibliographic record and abstract examined; full original text not available).
2. A. Kontorovich and A. Trachtenberg, “Unique decodability of bigram counts by finite automata,” first posted November 28, 2011, https://arxiv.org/abs/1111.6431 (full preprint examined, especially Theorem 2).
3. For context on related but distinct feasible-profile and cyclic-type enumerations: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-ternary-ordered-bigram-multispectrum-counts-and-the-degree--f0497779133f and https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-quasipolynomial-census-of-uniquely-reconstructible-ternary-cycli--7070e1d35506 (indexed research summaries inspected, not their full repository files).
