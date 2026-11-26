# Two-point punctures of scale-two binary hypercube Rips complexes through dimension six

## Finding
For an integer \(3\le n\le6\), let \(Q_n=\{0,1\}^n\) have Hamming distance. For two distinct words \(a,b\in Q_n\) of Hamming distance \(d\), let \(X_{n;a,b}\) be the inclusive scale-two Vietoris–Rips complex on \(Q_n\setminus\{a,b\}\): its nonempty faces are precisely finite subsets whose pairwise Hamming distances are at most two.

The integral homotopy type is determined completely by \(n\) and \(d\). If \(n=3\), it is contractible for \(d=1,2\), and it is \(S^2\) for \(d=3\). If \(4\le n\le6\), then
\[
X_{n;a,b}\simeq
\begin{cases}
\bigvee^{b_n^\mathrm{near}}S^3,&d=1\text{ or }2,\\
\bigvee^{b_n^\mathrm{far}}S^3,&3\le d\le n,
\end{cases}
\]
with \((b_4^\mathrm{near},b_4^\mathrm{far})=(3,1)\), \((b_5^\mathrm{near},b_5^\mathrm{far})=(32,29)\), and \((b_6^\mathrm{near},b_6^\mathrm{far})=(173,169)\). This is a finite-dimensional classification, **not** a claim that a formula holds for arbitrary \(n\).

## Assumptions and scope
All distances are those of the **original** Hamming cube: deleting words does not recompute shortest paths. The scale is inclusive \(r=2\); vertices of the Rips complex are the remaining binary words. For each \(n,d\), an isometry of the cube sends every unordered pair at distance \(d\) to \(\{0,(1\ll d)-1\}\), by translation and coordinate permutation. It therefore suffices to establish one case per \(n,d\), comprising exactly \(3+4+5+6=18\) cases.

## Proof
The accompanying compressed certificate describes a complete finite acyclic discrete-Morse matching for each of the 18 representatives. Each nonempty face is encoded as an increasing tuple of integers in \([0,2^n-1]\), interpreted as binary words. Its operations are either (i) a pair \((\sigma,\tau)\), where \(\sigma\) is a codimension-one face with **exactly one** remaining coface, \(\tau\), and \(\tau\) is maximal in the remaining complex; or (ii) deletion of one maximal face, recorded as critical. A pair step is an elementary free-face collapse of the current complex. A critical step removes a maximal face and records one Morse cell. The process is performed on a descending sequence of subcomplexes. The matched face pairs constitute an acyclic discrete-Morse vector field: a closed alternating gradient path would have an earliest removed matched pair whose other upper incident face was still present then, contradicting freeness. The maximal-facet deletion stages cannot create such a closed path, because their cells are unmatched.

The independently implemented verifier reconstructs **every** face by lexicographically extending pairwise Hamming-compatible subsets; it does not trust a supplied face list or assume the claimed ranks. For each step, it checks live-face membership, codimension one, unique immediate coface, maximality, and updates all remaining incidences. It checks that no faces remain and that the critical-cell census agrees with the stated values. The recorded censuses are exactly one critical vertex and no positive critical cells for \(n=3,d=1,2\); one vertex and one two-cell for \(n=3,d=3\); and for every \(4\le n\le6\) exactly one vertex and \(b_n^\mathrm{near}\) or \(b_n^\mathrm{far}\) three-cells, with no other critical cells. By the discrete-Morse CW equivalence, a CW complex with a single zero-cell and cells only in one dimension \(k\ge2\) is a wedge of \(k\)-spheres: all attaching maps land in the point. Thus the listed **integral homotopy types**, not merely field homology ranks, follow. The explicit integer encoding and all finite quantifiers are checked by the standalone verifier.

## Verification
Run `python3 verify_morse.py` next to `morse_cases.json.gz`, using Python 3.9 or newer and no external packages. It enumerates and checks all 18 finite cases and outputs the expected census. The verification reads 48,578 face occurrences across the cases and individually validates every operation of the compressed certificate. `EXPECTED.txt` contains the exact expected output. In particular, all critical-cells-only-in-dimension-three assertions are verified by finite exhaustive proof certificates, rather than inferred from numerical homology calculations. The certificates do not purport to prove statements for \(n>6\).

## Relationship to prior work
Adamaszek and Adams, *On Vietoris–Rips complexes of hypercube graphs* (arXiv:2103.01040, original 2021), proved that the unpunctured scale-two complex is a wedge of three-spheres and, in their Theorem 8, proved a stronger classification for integer-initial subsets of binary words. The present distance-one cases follow by isometry from that prior integer-initial-subset theorem and are included for completeness, **not claimed novel**. Their theorem does not classify removal of arbitrary pairs at distance two or more. Goyal, Shukla and Singh (arXiv:2009.12130, 2020) determine homotopy types of clique complexes of line graphs, a construction that can model a single vertex's link, but not directly the double-punctured complex. Bendersky, Elia and Grbić (arXiv:2605.00705, first public May 1, 2026, primary MSC including 55U10) study cohomological structure and induced subcomplexes of Hamming Rips complexes; their published results do not state the above two-puncture classification. The current contribution is the **distance-sensitive exact integral homotopy census**, especially the cases with \(d\ge2\).

## Limitations
The classification is deliberately finite, through \(n=6\), and the equalities of ranks across all farther distances have **not** been proved for arbitrary dimensions. The discrete-Morse certificates are finite computational proofs whose integrity depends on the fully included, independently replayable operations and verifier; there is no independent third-party mathematical audit. It remains possible that an unindexed equivalent classification exists. The 2026 paper motivates the study of induced subcomplexes, but does not establish this result as a consequence.

## References
1. M. Bendersky, S. Elia, J. Grbić, *Cohomological properties of the Vietoris–Rips complex of a hypercube graph*, arXiv:2605.00705 (first posted 2026-05-01), https://arxiv.org/abs/2605.00705 ; open-access journal text https://doi.org/10.1017/prm.2026.10175.
2. M. Adamaszek, H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040 (2021), especially Lemma 7 and Theorem 8, https://arxiv.org/pdf/2103.01040.
3. S. Goyal, S. Shukla, A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130 (first posted 2020-09-25), https://arxiv.org/abs/2009.12130.
