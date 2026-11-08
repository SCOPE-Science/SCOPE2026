# Seed-independent full dissemination and sharp path optimality in finite-tree stifling rumor networks

## Finding
Let \(T=(V,E)\) be any finite undirected tree on \(n\ge2\) vertices, and choose any initial informed spreader \(r\in V\). At each spreader \(v\), transmission to each ignorant neighbor has rate \(\beta_v>0\), while the spreader becomes a stifler at rate \(\gamma_v>0\) per already informed neighbor. Ignorants become spreaders upon first hearing the rumor; stiflers and spreaders remain informed forever. Put \(d_v=\deg_T(v)\) and \(\alpha_v=\gamma_v/\beta_v\). Then the probability that **every vertex ever hears the rumor** is
\[
\mathbb P_r(\text{full dissemination})
=\prod_{v\in V}\;\prod_{j=1}^{d_v-1}
\frac{d_v-j}{d_v-j+\alpha_v j}.
\]
The empty product for a leaf is one. In particular, the probability is independent of the seed \(r\), even with arbitrary positive vertex-dependent rate ratios. If every ratio has the same value \(\alpha>0\), the probability depends only on the degree multiset, and among all trees on \(n\) vertices it satisfies the **sharp** bound
\[
\mathbb P_r(\text{full dissemination})\le (1+\alpha)^{-(n-2)},
\]
with equality if and only if \(T\) is a path. For \(n=2\), the only tree is a path and full dissemination is certain.

## Assumptions and scope
The graph is a finite simple connected tree. There is one initial spreader and every other vertex is ignorant. At any moment, an active spreader \(v\) makes independent directed contacts to each ignorant neighbor at rate \(\beta_v\). Each already informed neighbor, whether spreader or stifler, contributes \(\gamma_v\) to the rate at which \(v\) becomes a stifler. Only the initiating spreader is stifled by unsuccessful contact. Stiflers cannot spread further; no one forgets the rumor. All vertex-originated contact clocks are independent. Rates depend on the originating vertex, not which one of its neighbors is contacted, and have no time dependence. The target event concerns *ever being informed*, not the terminal number of active spreaders or the dissemination time.

## Proof
Root \(T\) at \(r\). Each non-root vertex has exactly one parent, and cannot be informed before its parent: this follows from the uniqueness of the path from \(r\). Consequently, when a non-root vertex \(v\) is first informed, its parent is informed and all its children are ignorant. When \(v\) subsequently informs a child, that child remains informed regardless of how its own spreader activity ends.

For the root with degree \(d\), after it has informed \(j\) children and while still spreading, there are \(d-j\) ignorant children and \(j\) informed children. Competing exponential event rates are \(\beta_v(d-j)\) for the next newly informed child and \(\gamma_v j\) for cessation. Thus its probability of informing *all* \(d\) children before cessation is
\[
\prod_{j=0}^{d-1}\frac{d-j}{d-j+\alpha_v j}
=\prod_{j=1}^{d-1}\frac{d-j}{d-j+\alpha_v j}=:F_v(d).
\]
The factor at \(j=0\) equals one.

For a non-root vertex with degree \(d\), its parent contributes one permanently informed neighbor. When it has informed \(j\) of its \(d-1\) children, there are \(d-1-j\) ignorant children and \(j+1\) informed neighbors. Its complete-child probability therefore is
\[
\prod_{j=0}^{d-2}\frac{d-1-j}{d-1-j+\alpha_v(j+1)}
=\prod_{\ell=1}^{d-1}\frac{d-\ell}{d-\ell+\alpha_v\ell}=F_v(d).
\]
The root and non-root local factors coincide exactly.

For independence, pre-sample for every vertex the local sequence of prospective child contacts and stifling contacts after its possible activation, using clocks originating at that vertex. Such sequences are mutually independent because they use disjoint vertex-originating clocks. On a tree, the status of a vertex's parent remains informed after activation and the status of each child switches from ignorant to informed only upon a successful contact from that vertex. Thus the local event that every child is informed before the vertex stifles is well defined without reference to clock outcomes at any other vertex. Full dissemination occurs if and only if all these local events occur: induction down the rooted tree proves both directions. Multiplying their probabilities yields the displayed seed-independent product.

Now assume \(\alpha_v=\alpha>0\) everywhere. For each integer \(d\ge1\), write
\[
F(d)=\prod_{j=1}^{d-1}\left(1+\alpha\frac{j}{d-j}\right)^{-1}.
\]
Pair the factors with indices \(j\) and \(d-j\). Set \(u=j/(d-j)>0\). The product of the two reciprocal factors' denominators satisfies
\[
(1+\alpha u)(1+\alpha/u)
=(1+\alpha)^2+\alpha(u+u^{-1}-2)\ge(1+\alpha)^2,
\]
with equality exactly when \(u=1\). For odd \(d\), all factors are paired. For even \(d\), the single middle factor equals \(1+\alpha\). Hence
\[
F(d)\le(1+\alpha)^{-(d-1)}.
\]
For \(d\ge3\), some pair has \(j\ne d-j\), giving strict inequality; for \(d=1,2\), equality holds. The handshaking identity for a tree gives
\[
\sum_{v\in V}(d_v-1)=2(n-1)-n=n-2.
\]
Multiplication of the local bounds now gives the claimed upper bound, and equality requires all degrees at most two. A connected tree of maximum degree at most two is a path. Conversely every path attains equality. This also proves uniqueness up to tree isomorphism.

## Verification
The accompanying standalone `verify.py` uses exact rational arithmetic and a direct three-state Markov-chain recursion without invoking the product formula to compute full-dissemination probabilities. It independently checks all possible seeds for every Prüfer-labelled tree of orders two through five and sampled trees of orders six and seven, under three positive rate profiles including heterogeneous values. The script reports 567 tree/profile tests and 2958 individual root comparisons, all exact. It separately checks the homogeneous sharp bound on those trees. Execute `python3 verify.py` from the directory containing the file. The infinite-family theorem comes from the written proof, not the finite checks.

As illustrations, for \(\alpha=1\) a path of order five has full-coverage probability \(1/8\), whereas the star of order five has probability \(3/32\). Two nonisomorphic trees of order six with the same degree multiset \(\{3,2,2,1,1,1\}\) both have probability \(1/18\) at \(\alpha=1\), regardless of the initial spreader.

## Relationship to prior work
The stifling-rumor framework and the question of source influence are motivated by Borge-Holthoefer and Moreno (2011 preprint), which reports mean-reach simulations for variants of the rumor model on real networks, not an exact all-informed event for finite trees. Coletti, Rodríguez and Schinazi (2012 preprint) study an interacting spatial rumor process with forgetting on an infinite lattice; their extinction-survival conditions do not imply this finite-tree formula. Junior, Rodríguez and Speroto (2020) derive local offspring laws in homogeneous **infinite Cayley trees**, an important predecessor for the local competing-hazard calculation used here. Their branching-process survival criteria do not establish the finite irregular-tree, vertex-heterogeneous, seed-independent product nor the sharp all-tree path optimum. This result uses the local-law mechanism but adds a global finite-tree factorization, root invariance and a degree-extremal inequality. The usual epidemic/rumor model must not be confused with push-pull protocols without stifling or with global homogeneous mixing.

## Limitations
The formula requires a tree, uniform outgoing contact rates across neighbors of a given vertex, and permanent informed status. It need not hold for cyclic networks, edge-specific rates, independent spontaneous cessation, forgetting, or other stifling rules. The path comparison requires a common positive rate ratio; it does not assert a path extremum for arbitrary vertex-specific ratios or for mean reach, expected time, or other objectives. The exact mathematical statement has been checked against selected published sources but historical priority is not independently established, and related older rumor and reliability literature may contain equivalent ingredients.

## References
1. J. Borge-Holthoefer and Y. Moreno, *Absence of influential spreaders in rumor dynamics*, arXiv:1112.2239v1, publicly posted 2011-12-10; https://arxiv.org/abs/1112.2239.
2. C. F. Coletti, P. M. Rodríguez and R. B. Schinazi, *A spatial stochastic model for rumor transmission*, arXiv:1202.4019v1, publicly posted 2012-02-17; https://arxiv.org/abs/1202.4019.
3. V. V. Junior, P. M. Rodríguez and A. Speroto, *The Maki-Thompson rumor model on infinite Cayley trees*, arXiv:2005.11440; https://arxiv.org/abs/2005.11440.
