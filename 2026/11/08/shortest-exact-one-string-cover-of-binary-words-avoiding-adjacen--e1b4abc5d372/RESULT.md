# Shortest exact one-string cover of binary words avoiding adjacent zeros

## Finding
Fix any integer \(k\ge 2\), and let \(\mathcal D_k\) be the set of binary length-\(k\) words having no contiguous occurrence of `00`. Define \(\operatorname{spec}_k(W)\) to be the **set** of contiguous length-\(k\) factors of a finite, linear binary word \(W\). Then
\[
\min\bigl\{|W|:\operatorname{spec}_k(W)=\mathcal D_k\bigr\}=F_{k+2}+F_k,
\]
where \(F_0=0,F_1=1\) and \(F_{n+2}=F_{n+1}+F_n\). In every shortest representation, there are exactly \(F_k-k+1\) repeated length-\(k\) windows (counted with multiplicity beyond the first occurrence of each factor). This repetition overhead is zero exactly for \(k=2,3,4\), and is positive for every \(k\ge5\). The optimal word can be constructed deterministically from an Euler trail in a directed multigraph.

## Assumptions and scope
Strings are finite and **linear**, not cyclic; the alphabet is \(\{0,1\}\). The spectrum records factors without multiplicity. Repeated allowed factors are permitted, but **no** unlisted factor is permitted. A representation consists of exactly **one** string; multiple strings, separator symbols, and reverse-complement identifications are excluded. The theorem applies to all integer \(k\ge2\). For the distinct boundary case \(k=1\), the shortest word is `01` (or `10`), of length two, and the displayed formula does not apply.

## Proof
Let \(L=k-1\). Form an edge-centric directed de Bruijn graph \(G\): its vertices are all legal binary length-\(L\) words, and each legal length-\(k\) word \(a_1\cdots a_k\) gives an edge from \(a_1\cdots a_L\) to \(a_2\cdots a_k\). The graph is strongly connected: from any vertex, appending sufficiently many ones reaches \(1^L\); from there appending the target vertex reaches that vertex, with every intermediate factor still legal. Moreover, the number of edges is \(F_{k+2}\), by the Fibonacci recurrence for binary words with no adjacent zeros.

Any legal one-string spectrum cover traces a directed walk traversing every edge of \(G\) at least once. Conversely, every such edge-covering walk spells a word with precisely the required factor set, and each additional traversal increases its length by one. Write \(R\) for the number of traversals beyond the first of each edge. The word length is \(F_{k+2}+L+R\).

For \(L\ge2\), define the imbalance \(\delta(v)=\deg^+(v)-\deg^-(v)\) of the **original** graph. Inspecting allowed predecessors and successors gives \(\delta(v)=1\) when \(v\) starts with `0` and ends with `1`; \(\delta(v)=-1\) when it starts with `1` and ends with `0`; otherwise \(\delta(v)=0\). Let \(N\) be the negatively imbalanced vertices, and let \(j(v)\) be the number of initial consecutive ones for \(v\in N\). Counting the vertices in \(N\) for which the first \(t\) symbols are all ones gives \(F_{L-t}\), hence
\[
S:=\sum_{v\in N}j(v)=\sum_{t=1}^{L-1}F_{L-t}=F_{L+1}-1=F_k-1.
\]
Indeed, a legal word of length \(L-t\) ending in zero is counted by \(F_{L-t}\) (including the one-symbol base case).

Define a potential \(g\) on vertices: if \(v\) contains a zero, let \(g(v)\) be its number of initial consecutive ones (possibly zero); set \(g(1^L)=L-1\). Then \(0\le g(v)\le L-1\), and **every** directed edge \(v\to w\) satisfies \(g(v)-g(w)\le1\): shifting a leading `1` reduces its initial run by at most one, shifting a leading `0` cannot create a positive drop, and the all-ones case follows from its special value. In particular, \(g=0\) at every positively imbalanced vertex, and \(g(v)=j(v)\) at every negatively imbalanced vertex. Therefore
\[
\sum_vg(v)\delta(v)=-S.
\]
Consider the extra traversals of an arbitrary covering walk that starts at vertex \(s\) and ends at vertex \(t\). Their imbalance is \(\mathbf1_s-\mathbf1_t-\delta\). Summing potential drops along the extra traversals yields exactly
\[
\sum_{\mathrm{extra}\ v\to w}\bigl(g(v)-g(w)\bigr)=g(s)-g(t)+S.
\]
Each drop is at most one, so
\[
R\ge g(s)-g(t)+S\ge S-(L-1)=F_k-k+1.
\]
This is a lower bound even if extra traversals form arbitrarily repeated walks, or if the covering word has different endpoints.

For equality, put \(v_*=1^{L-1}0\) and \(p_*=01^{L-1}\). Every negatively imbalanced vertex other than \(v_*\) has a unique expression \(v=1^{j}u\), where \(1\le j\le L-2\) and \(u\) begins and ends in zero and is legal. Duplicate the directed path of exactly \(j\) edges obtained by appending `1` successively to \(v\). The resulting endpoint is \(u1^j\), a positively imbalanced vertex. The assignment \(v\mapsto u1^j\) is a bijection from the negative vertices other than \(v_*\) onto the positive vertices other than \(p_*\) (inverse: remove the final run of ones and prepend it). Consequently the augmented directed multigraph is balanced at every vertex except \(p_*\), of imbalance \(+1\), and \(v_*\), of imbalance \(-1\). Because the original graph is strongly connected, the augmented multigraph has an Euler trail from \(p_*\) to \(v_*\). The added edge count is exactly
\[
\sum_{v\in N\setminus\{v_*\}}j(v)=S-(L-1)=F_k-k+1.
\]
The spelled word is a valid one-string spectrum cover and has the stated minimum length.

Finally, when \(L=1\) (that is, \(k=2\)), the vertices `0` and `1` have balanced in- and outdegrees, and the original graph is Eulerian. Hence \(R=0\), yielding length \(F_4+F_2=4\). The formula for repeated windows follows by subtracting the \(F_{k+2}\) distinct required windows from the total \(|W|-k+1\). The Fibonacci values show \(F_k-k+1=0\) exactly for \(k=2,3,4\), and it is strictly increasing thereafter.

## Verification
Run `python3 checker.py` using Python's standard library. The checker constructs the augmented graph and Euler trail, checks balance, enforces the original legal spectrum exactly, verifies the number of extra windows and the potential bound for every \(k\) from \(2\) through \(13\), and independently enumerates the shortest admissible word by breadth-first search for \(k=2,3,4,5\). The infinite statement is proved above rather than inferred from bounded runs.

## Relationship to prior work
Chakraborty, Grossi, Kimura, Punzi, Sadakane and Zuba (first public February 23, 2026) examine exact spectrum-preserving representations and emphasize **no-repetition** path/cycle and necklace covers. Schmidt, Khan, Alanko, Pibiri and Tomescu (2023) provide a general polynomial-time framework for minimum-size, potentially repeating k-mer set representations using **a set of strings**. Their optimization algorithms furnish related graph methods but do not state this closed-form one-string all-\(k\) Fibonacci value, its unavoidable repetition count, or the explicit matching lower/upper construction. Moreno and Matamala (2007) study Eulerian minimal de Bruijn sequences for languages with forbidden substrings, particularly periodic/cyclic legal words; the finite **linear** dictionary here gives an imbalanced graph and requires repeated windows. The exact closed-form one-string specialization and its potential certificate are the mathematical contribution assessed here; an earlier implicit specialization cannot be excluded conclusively.

## Limitations
The formula does not optimize an arbitrary number of output strings or allow false-positive k-mers. It does not describe the number or uniqueness of optimal words, larger forbidden factor families, larger alphabets, or circular-only dictionaries. Source priority remains subject to independent expert comparison. Computational checks are bounded and do not certify the infinite claim on their own.

## References
1. S. Chakraborty, R. Grossi, R. Kimura, G. Punzi, K. Sadakane, W. Zuba, *Variations on the Problem of Identifying Spectrum-Preserving String Sets* (2026), https://arxiv.org/abs/2602.19408 (first posted February 23, 2026).
2. S. Schmidt, S. Khan, J. N. Alanko, G. E. Pibiri, A. I. Tomescu, *Matchtigs: minimum plain text representation of k-mer sets*, Genome Biology 24:136 (2023), https://doi.org/10.1186/s13059-023-02968-z.
3. E. Moreno, M. Matamala, *Minimum de Bruijn Sequence in a Language with Forbidden Substrings* (2007), https://arxiv.org/abs/0711.1695.
