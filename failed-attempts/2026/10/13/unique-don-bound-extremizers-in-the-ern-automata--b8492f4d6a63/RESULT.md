# Unique Don-bound extremizers in the Černý automata
## Finding
For the standard \(n\)-state Černý automaton \(C_n\), take \(Q=\{0,\ldots,n-1\}\), let \(a(i)=i+1\pmod n\), and let \(b(n-1)=0\) while \(b(i)=i\) for \(i<n-1\). For a nonempty \(S\subseteq Q\), let \(\tau(S)\) be the least length of a word \(w\) with \(Qw=S\).

For every \(1\le k<n\),
\[
\max_{|S|=k}\tau(S)=n(n-k),
\]
and the unique equality case in this labeling is
\[
S_k=\{n-1,0,1,\ldots,k-2\}.
\]
Thus the known Don bound is not only sharp at every cardinality layer of \(C_n\): its exact-image equality case is unique.

## Assumptions and scope
The statement uses the displayed standard labeling. Relabeling states transports the unique extremizer accordingly. The result concerns exact image reachability \(Qw=S\), not merely avoiding a forbidden set or reaching some subset of \(S\). No claim is made for arbitrary completely reachable automata.

## Proof
Write indices modulo \(n\). For a nonempty proper subset \(S\), choose
\[
t(S)=\min\{t\in\{0,\ldots,n-1\}:t\in S,\ t-1\notin S\}.
\]
Such a cyclic boundary always exists. Rotate \(S\) backwards by \(t=t(S)\): put \(R=S a^{-t}\). Then \(0\in R\) and \(n-1\notin R\). Hence \(U=R\cup\{n-1\}\) has one more state and satisfies \(Uba^t=S\). Induction on \(n-|S|\) therefore gives
\[
\tau(S)\le n(n-|S|),
\]
because \(t+1\le n\).

Moreover, \(t(S)=n-1\) if and only if the only excluded-to-included cyclic boundary occurs just before \(n-1\). For a \(k\)-set this forces exactly \(S=S_k\). Consequently every \(k\)-set other than \(S_k\) has \(t(S)\le n-2\), and the same induction yields the strict estimate
\[
\tau(S)\le n(n-k)-1.
\]

It remains to show \(\tau(S_k)\ge n(n-k)\). Read a reaching word backwards from \(S_k\) toward \(Q\). The inverse of \(a\) is a one-step backward rotation. A reverse \(b\)-step can increase cardinality only when the current set contains \(0\) and omits \(n-1\); then the unique larger predecessor is obtained by adjoining \(n-1\). Starting from \(S_k\), the first such configuration appears only after \(n-1\) inverse rotations. Any earlier reverse \(b\)-step is either impossible or does not enlarge the set and can be deleted from a shortest reverse path. After those \(n-1\) rotations and the cardinality-increasing reverse \(b\)-step, the larger predecessor is exactly \(S_{k+1}\). Induction therefore forces at least \(n\) letters for each of the \(n-k\) necessary cardinality increases, so \(\tau(S_k)\ge n(n-k)\). The word \((ba^{n-1})^{n-k}\) reaches \(S_k\), giving equality.

## Verification
The bundled `verify.py` independently breadth-first searches the complete power automaton for every \(2\le n\le12\). It checks every nonempty subset, every exact reaching distance, the unique equality set at every cardinality, the explicit equality word, and the reverse-extension lemma used above. Its expected terminal line starts with `VERIFY_OK`.

## Relationship to prior work
Don proved in 2016 that the relevant aperiodically 1-contracting class, including the Černý family, has every \(k\)-subset reachable within \(n(n-k)\); that paper is the source of the layerwise upper bound. Ferens and Szykuła later explicitly noted that the Černý automata meet the Don bound at every subset size and displayed the worst subsets for \(n=4\). The present statement identifies and proves the unique equality set for every \(n\) and every layer. A nearby avoiding-set result has the same numerical scale for consecutive forbidden blocks, but avoiding a set only requires the final image to lie somewhere in its complement, whereas the theorem here fixes the image exactly.

## Limitations
The equality classification is for the standard Černý family and does not classify Don-bound equality in other completely reachable automata. The originality search cannot exclude an obscure or unindexed note that records the same all-\(n\) equality characterization. The finite verifier is a check of the proof pattern, not a substitute for the all-\(n\) argument.

## References
1. H. Don, “The Černý Conjecture and 1-Contracting Automata,” *Electronic Journal of Combinatorics* 23(3), P3.12 (2016), DOI: 10.37236/5616. Published 2016-07-22; MSC 68R05.
2. R. Ferens and M. Szykuła, “Recognizing Completely Reachable Automata in Quadratic Time,” *ACM Transactions on Algorithms* 22(2) (2026), DOI: 10.1145/3798283.
