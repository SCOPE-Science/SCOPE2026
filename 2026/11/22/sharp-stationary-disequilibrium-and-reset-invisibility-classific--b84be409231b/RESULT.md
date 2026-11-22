# Sharp stationary disequilibrium and reset-invisibility classification for finite network walks

## Finding

For an irreducible finite-state discrete-time random walk with transition matrix \(P\), stationary law \(\pi\), and independent identically distributed positive-integer renewal intervals \(L\) between complete resets to vertex \(v\), write \(\mu=\mathbb E L<\infty\). Define the pre-reset mismatch probability
\[
q=\Pr_v(X_L\ne v)=1-\mathbb E[(P^L)_{vv}],
\]
where the walk is run without resetting during each excursion and \(L\) is independent of it. Its equilibrium-renewal occupation law \(p\) satisfies the **sharp network-independent inequality**
\[
\boxed{d_{\rm TV}(p,\pi)\ge\frac{q}{2\mu}.}
\]
Equality holds for every clock on the simple random walk on a star, reset to its hub; thus the universal constant cannot be improved. Moreover \(p=\pi\) **if and only if** every scheduled reset is pathwise position-invisible: \(\Pr_v(X_L=v)=1\). If \(P\) has period \(d\), this happens exactly when the cyclic class containing \(v\) consists solely of \(v\) and \(\Pr(d\mid L)=1\). On any finite connected loopless undirected simple graph with at least two vertices, this is equivalent to a star graph reset to its center with an even-valued clock.

## Assumptions and scope

Let \(S\) be a finite set of \(n\ge2\) states. Let \(P=(P_{ij})_{i,j\in S}\) be an irreducible row-stochastic matrix, with unique strictly positive invariant row vector \(\pi P=\pi\). No reversibility or diagonalizability is required. Fix \(v\in S\). The positive-integer-valued random variable \(L\) has finite positive mean \(\mu\); independent copies of \(L\) and of the underlying \(P\)-walk excursions are drawn between resets to \(v\). A cycle of length \(\ell\) contributes its positions at discrete ages \(k=0,\ldots,\ell-1\), then an instantaneous reset to \(v\) replaces its endpoint. The law \(p\) is the stationary equilibrium-renewal marginal, equivalently the long-time occupation average. For arithmetic clocks or periodic \(P\), a fixed-phase one-time law need not converge; no pointwise temporal convergence is asserted.

Use \(e_v\) for the unit row vector and \(d_{\rm TV}(a,b)=\tfrac12\sum_{i\in S}|a_i-b_i|\). A *cyclic class* is a member of the usual period-\(d\) partition \(S=C_0\sqcup\cdots\sqcup C_{d-1}\) with transitions from \(C_j\) to \(C_{j+1\pmod d}\). The graph corollary uses the nearest-neighbor simple random walk (no holding) on a connected loopless undirected simple graph.

## Proof

**(1) Occupation and balance.** The discrete renewal-reward theorem gives
\[
p=\frac1\mu\mathbb E\left[\sum_{k=0}^{L-1}e_vP^k\right].
\]
The sums are absolutely convergent because each summand is a probability vector and \(\mathbb E L<\infty\). Write \(\nu=\mathbb E[e_vP^L]\). Telescoping every cycle yields the exact *renewal flux identity*
\[
\boxed{\mu p(I-P)=e_v-\nu.}\tag{1}
\]
Since \(\nu\) is a probability law, \(d_{\rm TV}(e_v,\nu)=1-\nu_v=q\), hence
\[
d_{\rm TV}(p,pP)=\frac q\mu.\tag{2}
\]
Because \(\pi P=\pi\) and stochastic kernels contract total variation,
\[
\frac q\mu=d_{\rm TV}(p,pP)
\le d_{\rm TV}(p,\pi)+d_{\rm TV}(\pi,pP)
\le2d_{\rm TV}(p,\pi),
\]
which proves the universal bound.

**(2) Exact invisibility.** If \(p=\pi\), (1) gives \(\nu=e_v\) and hence \(q=0\). Conversely if \(q=0\), then \(\nu=e_v\), so (1) gives \(pP=p\); uniqueness of the invariant probability of irreducible \(P\) gives \(p=\pi\). Since \(0\le(P^\ell)_{vv}\le1\), \(q=0\) is equivalent to \((P^\ell)_{vv}=1\) for each \(\ell\) with \(\Pr(L=\ell)>0\). Thus each reset maps a particle already at \(v\) to \(v\), almost surely.

**(3) Finite-chain cyclic-class classification.** Suppose \((P^\ell)_{vv}=1\) for a supported \(\ell\). Necessarily \(d\mid\ell\) by the cyclic decomposition. The exact return implies \((P^{j\ell})_{vv}=1\) for every positive integer \(j\). The finite irreducible periodic-chain limit, along multiples of \(d\), is \(\lim_{j\to\infty}(P^{j\ell})_{vv}=d\pi_v\); therefore \(d\pi_v=1\). Every cyclic class has total invariant mass \(1/d\), and \(\pi_i>0\) for all states, so the class containing \(v\) must be the singleton \(\{v\}\). All supported \(\ell\) are multiples of \(d\). Conversely if this cyclic class is \(\{v\}\) and every \(L\) is divisible by \(d\), the walk is in that class at every pre-reset time, hence at \(v\) almost surely, so \(q=0\). This proves the necessity and sufficiency.

**(4) Graph classification.** For a connected, loopless, undirected graph, the simple random walk has period \(2\) exactly if the graph is bipartite and period \(1\) otherwise. The period-one cyclic class is the entire vertex set and cannot be a singleton. For a bipartite graph, the two cyclic classes are its vertex partitions. A singleton bipartition containing \(v\) forces every edge to touch \(v\) by connectedness; therefore the graph is exactly a star centered at \(v\). The required divisibility of \(L\) is then evenness. The converse follows immediately.

**(5) Sharpness.** Let \(P\) be the neighbor-uniform walk on the star \(K_{1,m}\), \(m\ge1\), with \(v\) its hub. Starting from \(v\), every even age is at the hub and every odd age is uniform on the leaves. Let \(w=\Pr(L\text{ odd})\). A length-\(L\) excursion has exactly \(\lceil L/2\rceil\) hub observations, so
\[
p_v=\frac{\mathbb E\lceil L/2\rceil}{\mu}
=\frac12+\frac w{2\mu},
\qquad
\pi_v=\frac12.
\]
The remainder of \(p\) and \(\pi\) is uniform on the leaves, giving
\[
d_{\rm TV}(p,\pi)=\frac w{2\mu},\qquad
q=\Pr_v(X_L\ne v)=w.
\]
Thus equality in the claimed bound holds for every positive finite-mean reset clock, including clocks with \(w>0\), and the prefactor \(1/2\) is optimal. All conclusions follow.

## Verification

The standalone Python 3 script `check.py` uses only the standard library and exact rational arithmetic to reconstruct stationary distributions and renewal-occupation laws for every connected undirected simple graph on two through five vertices (\(771\) graphs) and multiple reset lengths and roots. It tests the balance identity, the sharp inequality, the exact zero-bias classification, directed stochastic examples, star equality for mixed clocks, and a directed-cycle periodic-clock example. Run `python3 check.py`. One execution completed \(19{,}556\) exact check instances: \(19{,}030\) undirected graph/root/clock instances, \(480\) positive directed instances, and \(46\) star and cycle sharpness/periodicity checks. Exact finite checks do not replace the unrestricted proof in the previous section.

## Relationship to prior work

The network-resetting stationary distribution and renewal-reward framework are **not** claimed as new. Riascos, Boyer, Herringer and Mateos (2019, arXiv:1910.13568; especially stationary spectral formula and network examples) derive the constant-reset stationary occupation law. Chen and Ye (2022, arXiv:2208.06212; especially Sections II and VI) derive stationary occupation for time-dependent resetting hazards. The new assessed assertion is the all-clock, all-finite-chain sharp \(q/(2\mu)\) disequilibrium lower bound **together with** the iff pathwise-invisibility and complete periodic-cyclic-class/star characterization. These are not identified as stated results in the inspected sources. They use established renewal theory and finite Markov-chain periodicity; a broad general theorem elsewhere might imply them without identical terminology. This is a self-review, not independent publication certification.

## Limitations

The bound quantifies total variation of the *equilibrium-renewal occupation law*, not a necessarily existing fixed-time limit of a periodic renewal process. The graph iff corollary assumes simple, loopless, undirected neighbor-uniform walks; directed and weighted periodic chains obey the more general cyclic-class criterion. The theorem does not optimize a reset clock at fixed mean, and the bound is not asserted pointwise sharp on each fixed non-star topology. Equality of static occupation laws does not imply equality of trajectory laws or of resetting-event counts. Independence of reset intervals from motion and finite mean are essential hypotheses. Prior art might implicitly contain consequences of the general formulas; the stated novelty is in the sharp inequality and complete equality case.

## References

1. A. P. Riascos, D. Boyer, P. Herringer, and J. L. Mateos, *Random walks on networks with stochastic resetting*, arXiv:1910.13568, first publicly posted 2019-10-29. https://arxiv.org/abs/1910.13568
2. A. P. Riascos and collaborators, *Discrete-time random walks and Lévy flights on arbitrary networks: when resetting becomes advantageous?*, arXiv:2110.15437, first publicly posted 2021-10-28. https://arxiv.org/abs/2110.15437
3. H. Chen and Y. Ye, *Random walks on complex networks under time-dependent stochastic resetting*, arXiv:2208.06212, first publicly posted 2022-08-12. https://arxiv.org/abs/2208.06212
