# A twelve-periodic quadratic law for uniquely reconstructible binary trigram spectra

## Finding
For a binary word \(w=w_1\cdots w_n\), its **trigram spectrum** is the eight-component vector \(P_3(w)\) recording, with multiplicity, every contiguous factor of length \(3\). Define
\[
U_n=\bigl|\{w\in\{0,1\}^n:\; P_3^{-1}(P_3(w))\cap\{0,1\}^n=\{w\}\}\bigr|.
\]
For every integer \(n\ge9\),
\[
\boxed{U_n=\frac{n^2+28n+c_{n\bmod12}}2},
\]
where the constants \(c_0,\ldots,c_{11}\) are, in residue order,
\[
(-88,-85,-108,-85,-88,-97,-96,-85,-100,-85,-96,-97).
\]
For \(3\le n\le8\), the exact values are
\[
(U_3,U_4,U_5,U_6,U_7,U_8)=(8,14,26,46,74,92).
\]
In particular, \(U_n=\frac12n^2+14n+O(1)\): an asymptotically vanishing fraction \(U_n/2^n\) of binary strings is uniquely reconstructible from its full, unordered trigram spectrum.

## Assumptions and scope
Words are **linear**, not cyclic, and are distinguished as labeled bit strings (not modulo reversal, rotation, or complementation). The observation records multiplicities of all length-\(3\) contiguous substrings, without supplying either endpoint. The source length \(n\) is fixed and known. No sequencing noise or omitted reads are allowed. The theorem concerns integers \(n\ge3\), when the observation includes at least one trigram.

## Proof
For \(n\ge3\), interpret each trigram \(abc\) as a directed arc from the pair \(ab\) to \(bc\) in the four-vertex binary order-two de Bruijn graph. The profile is exactly the directed arc-multiplicity vector. A reconstruction is an Euler trail in this directed multigraph, read as a vertex walk, with parallel copies of an identical arc indistinguishable.

A standard proper-transposition characterization of Euler-trail uniqueness under a **fixed** initial vertex gives a finite-state decision procedure (Li and Xie, 2005, Section 2). A state stores the first vertex \(s\), current vertex \(p\), for each of the four vertices the most recently observed successor \(f(v)\) or an unset mark, a four-bit set of vertices flagged by an alternating-successor circuit, and whether any vertex other than \(s\) has been visited. At a new bit \(b\), the next vertex is \(a=(2p+b)\bmod4\). If the successor of \(p\) was previously set to a different value, follow the stored successor cycle starting at \(p\) and flag all its vertices. Reject the transition if \(a\) is flagged; otherwise update \(f(p)=a\), \(p=a\), and the visit flag. This is the four-vertex specialization of the cited uniqueness criterion, with its transition order stated explicitly in `verify.py`.

This fixed-start test must be supplemented because the complete spectrum does **not** announce the initial pair. For a nonclosed Euler trail, indegree/outdegree imbalance determines the initial vertex. For a closed Euler trail that visits at least two different vertices, rotating the same closed trail to begin at a different visited vertex gives a different reconstruction with the same spectrum. The only closed trail that survives is a repeated self-loop at a single vertex. Thus an accepting state must also satisfy \(p\ne s\), or have visited no vertex other than \(s\).

There are four possible initial two-bit vertices. Reachability under the two bit transitions gives exactly \(166\) accepting-or-intermediate nonfailure states. Let \(M\) be their nonnegative integer transition-count matrix: \(M_{ij}\) counts the labels \(b\in\{0,1\}\) taking state \(i\) to state \(j\). Let \(r_2\) have one unit at each of the four initial states and zero elsewhere, and let \(a\) be the indicator column of globally acceptable states. Then \(r_n=r_2 M^{n-2}\) and \(U_n=r_n a\) for \(n\ge3\). An exact integer calculation from the fully specified \(166\)-state automaton gives the **vector identity**
\[
r_{45}-3r_{33}+3r_{21}-r_9=0.
\]
Right-multiplication by \(M^k\) yields, for **every** integer \(n\ge9\),
\[
U_{n+36}-3U_{n+24}+3U_{n+12}-U_n=0.
\]
Thus each residue class modulo \(12\) is quadratic in the quotient variable. The exact values through \(n=44\) (three consecutive values for each residue) determine the displayed quadratic formula in every class. The exceptions at \(3\le n\le8\) follow from the same transition recurrence. This completes the all-length proof for \(n\ge3\).

## Verification
Run `python3 verify.py` in the extracted directory. It regenerates the states and edges from the explicit transition definition, checks every entry against `transition_table.json`, recomputes all four certificate row vectors in `recurrence_certificate.json`, checks the vector identity coordinatewise, and verifies direct lengths through \(65\). Run `python3 independent.py` to compare an independent exhaustive, multiplicity-sensitive enumeration of all binary words for lengths \(3\) through \(16\). Both scripts use Python's standard library only. The state-vector identity, not agreement on finitely many scalar samples, is the certificate for unbounded \(n\).

## Relationship to prior work
Kontorovich (2004) established general regularity of uniquely decodable \(k\)-gram embeddings, and Li and Xie (2005) gave a deterministic test for uniqueness of Euler trails. Kontorovich and Trachtenberg (2011) supplied a compact NFA for bigram uniqueness. Kiah, Puleo, and Milenkovic (2014, 2015 revision) treated DNA read profiles and equivalence classes via restricted de Bruijn graphs and polytope enumeration. The regularity and DFA tests are **not** new. The new claim is the *explicit* binary linear-trigram singleton count for every length, its surprisingly exact period-\(12\) quadratic law, and an integer finite-state recurrence certificate. These are not the same as counting all spectrum classes, or as the previously studied binary bigram case.

## Limitations
The count is for a binary alphabet, contiguous trigrams, an unanchored linear profile, and exact multiplicities. The automaton reduction uses the proper-transposition criterion from published Euler-trail theory; it is not a new proof of that general criterion. A highly relevant 2004 primary article could not be read in full; an earlier equivalent explicit enumerator remains a historical-priority risk. The finite-state identity has been cross-checked against the stated direct enumerations, but has not undergone an external independent audit. No claim of practical DNA-channel robustness is made.

## References
1. L. Kontorovich, *Uniquely decodable n-gram embeddings*, Theoretical Computer Science 329 (2004), 271–284. https://doi.org/10.1016/j.tcs.2004.10.010
2. Q. Li and H.-M. Xie, *Finite automata for testing uniqueness of Eulerian trails*, preprint publicly available July 20, 2005. https://arxiv.org/abs/cs/0507052
3. A. Kontorovich and A. Trachtenberg, *Unique decodability of bigram counts by finite automata*, preprint November 28, 2011. https://arxiv.org/abs/1111.6431
4. H. M. Kiah, G. J. Puleo, and O. Milenkovic, *Codes for DNA sequence profiles*, first preprint October 31, 2014. https://arxiv.org/abs/1410.8837
