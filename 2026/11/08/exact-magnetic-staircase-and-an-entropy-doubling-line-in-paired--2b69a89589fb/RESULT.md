# Exact magnetic staircase and an entropy-doubling line in paired complete-graph Ising antiferromagnets

## Finding

Let \(n\ge2\), \(J>0\), \(K\ge0\), and \(h\in\mathbb R\). Pair \(2n\) labeled Ising spins as \((a_i,b_i)\), \(1\le i\le n\). Give all inter-pair edges antiferromagnetic coupling \(J\) and each intra-pair edge coupling \(K\). Thus \(K=0\) is the cocktail-party graph and \(K=J\) is the uniformly coupled complete graph. Write \(\kappa=K/J\), \(t=|h|/J\), and \(s=\tfrac12\sum_{i=1}^n(a_i+b_i)\in\{-n,\ldots,n\}\). For \(h\ge0\), each ground-state sector has \(s\ge0\), except that when \(h=0,\kappa=0\), and \(n\) is odd, the additional sector \(s=-1\) is a ground sector.

Define \(d_s=(n-s)\bmod2\), for \(0\le s\le n\). The ground sectors and their exact numbers of labeled configurations follow by minimizing the indicated energy \(E_s\), with all minimizers included:

\[
\begin{array}{c|c|c}
\text{coupling range}&E_s/J&g_s\\ \hline
0\le\kappa<1&2s^2-n+(\kappa-1)(n-2d_s)-2ts&\begin{cases}\binom n{(n+s)/2},&d_s=0,\\2n\binom{n-1}{(n-1+s)/2},&d_s=1;\end{cases}\\
\kappa=1&2s^2-n-2ts&\binom{2n}{n+s}\\
\kappa>1&2s^2-n+(\kappa-1)(2s-n)-2ts&\binom ns2^{n-s}.
\end{array}
\]

For each fixed \(\kappa>0\), the strictly increasing transition fields between sectors \(s\) and \(s+1\), \(0\le s<n\), are exactly
\[
t_s=\begin{cases}
2s+2-\kappa,&0<\kappa<1\text{ and }s\equiv n\pmod2,\\
2s+\kappa,&0<\kappa<1\text{ and }s\not\equiv n\pmod2,\\
2s+1,&\kappa=1,\\
2s+\kappa,&\kappa>1.
\end{cases}
\]

At a transition exactly the two adjacent sectors minimize; between successive transitions exactly one sector minimizes. At \(\kappa=0\), neighboring transition fields coincide in pairs: for even \(n\), each \(t=2,6,\ldots,2n-2\) has three ground sectors \(s=2j,2j+1,2j+2\) (with \(j=0,\ldots,n/2-1\)); for odd \(n\), \(t=0\) has sectors \(s=-1,0,1\), while each \(t=4,8,\ldots,2n-2\) has three sectors \(s=2j-1,2j,2j+1\). For negative \(h\), reverse all spin labels, mapping \(s\) to \(-s\). In any sector, the ground configurations are precisely those realizing the relevant extremal number of opposite-spin pairs, or every pairing pattern if \(\kappa=1\).

At fixed \(J,K,h\) as \(n\to\infty\), the zero-temperature residual entropy per spin is exactly
\[
\lim_{n\to\infty}\frac{\log\Omega_n(J,K,h)}{2n}=\begin{cases}\log2,&K=J,\\\tfrac12\log2,&K\ne J,\end{cases}
\]
where \(\Omega_n\) denotes the total number of ground configurations, including all coexisting sectors. Thus the matching-coupling equality is an exact entropy-doubling line; the isolated \(K=0\) transition-field coincidences also admit explicit triple-sector multiplicities.

## Assumptions and scope

Spins are classical values \(\pm1\). The full Hamiltonian is \(H=J\sum_{1\le i<j\le 2n,\ \{i,j\}\notin M}\sigma_i\sigma_j+K\sum_{\{i,j\}\in M}\sigma_i\sigma_j-h\sum_{i=1}^{2n}\sigma_i\), with \(M\) the fixed perfect matching. Couplings are not rescaled by system size. The theorem concerns **global** zero-temperature minima, not metastable single-spin local minima, dynamics, or finite-temperature phase transitions. The logarithm is natural and Boltzmann's constant is set to one.

## Proof

Write \(p\), \(q\), \(k\) for the numbers of matched pairs with values \((+,+)\), \((-,-)\), and opposite spins, respectively. Then \(p+q+k=n\), \(p-q=s\), and the matching interaction sum equals \(n-2k\). Using \(\sum_{i<j}\sigma_i\sigma_j=(4s^2-2n)/2\) gives the identity
\[
H/J=2s^2-n+(\kappa-1)(n-2k)-2(h/J)s.
\]
For any fixed \(s\), the feasible \(k\)'s are exactly \(0\le k\le n-|s|\) with \(k\equiv n-|s|\pmod2\). If \(\kappa<1\) the energy is minimized at the **smallest** feasible \(k\), namely \(d_s\); if \(\kappa>1\) it is minimized at the **largest**, \(n-|s|\); and if \(\kappa=1\) it is independent of \(k\). This gives the three energy formulas. Counting choices of matched pair types and the two orientations of each opposite pair gives respectively \(g_s=\binom n{(n+s)/2}\), \(2n\binom{n-1}{(n-1+s)/2}\), \(\binom ns2^{n-s}\), and the unrestricted \(\binom{2n}{n+s}\).

For positive field, comparing \(s\) with \(-s\) shows the nonnegative sector wins; at zero field, the only nonzero-magnetization zero-cost ground sectors arise when \(\kappa=0\), \(n\) odd, and \(|s|=1\), directly from the quadratic formula. For \(s\ge0\), the differences \(E_{s+1}-E_s\) are \(2J(t_s-t)\) with \(t_s\) as displayed. For \(\kappa>0\) these thresholds are strictly increasing, so the energy is discrete convex and the listed sectors are exactly all global minimizers. At \(\kappa=0\), alternate adjacent thresholds coincide, yielding precisely the indicated triples (and the zero-field spin-reversal sector). There are no further minima because subsequent energy differences increase strictly after each tie.

For fixed \(K,h,J\), the minimizing \(|s|\) remains bounded as \(n\to\infty\) by the quadratic energy and the explicitly bounded thresholds (the parity offset does not grow). When \(K<J\), the central binomial counts with at most one opposite pair are \(2^{n+o(n)}\); when \(K>J\), \(\binom ns2^{n-s}=2^{n+o(n)}\); at \(K=J\), \(\binom{2n}{n+s}=2^{2n+o(n)}\). A bounded number of coexisting sectors changes no exponential rate. This proves the residual entropy formula, including the parity-sensitive \(K=0\) endpoint.

## Verification

The complete exact-state verifier \(verify.py\) calculates the predicted sector energies and multiplicities and independently enumerates all labeled spin configurations of the full Hamiltonian for \(1\le n\le6\), seven coupling ratios \(0,1/4,3/4,1,5/4,2,4\), and seventeen field ratios \(0,1/4,3/4,1,3/2,2,5/2,3,15/4,4,17/4,5,6,7,8,10,12\). It asserts exact agreement of ground energies and counts in every sector for all \(714\) combinations. Use \(python3 verify.py\) from the extracted package directory. The proof, not these finite tests, establishes all \(n\) and continuous parameter ranges.

## Relationship to prior work

The infinite-range antiferromagnetic spin models of Chakrabarti and Inoue (2005) and Chakrabarti, Das and Inoue (2005) use bipartite, transverse-field or random-field interactions rather than a perfect matching with an independently tunable coupling; their examined Hamiltonians and calculations do not assert this paired-bond phase diagram. Varma (2013) analyzes geometrically different finite-degree ladders and kagome lattices via saturation-field transfer matrices; its full text does not present this complete-graph matching deformation. Dubi and Di Ventra (2009) treat a random-coupling lattice spin glass by a dimer mean-field approximation, not an exactly specified complete graph with a deterministic matching coupling (their Hamiltonian and Eq. (4)). The present exact bond-group counting is elementary but the combined all-coupling, all-field ground-state classification and entropy ridge are distinct statements. The standard complete-graph \(K=J\) special case is not claimed to be independently new.

## Limitations

Historical priority is subject to deeper searches, especially for equivalent paired Curie–Weiss models described using block interactions rather than graph names. The entropy result holds at exactly zero temperature with fixed unscaled couplings and field; it does not claim a thermodynamic finite-temperature transition or any uniform assertion as \(K\) approaches \(J\) with \(n\). Coupled-field ground-state results on other graph families cannot be inferred by changing a name. Independent validation has not been performed.

## References

1. B. K. Chakrabarti and J.-i. Inoue, *A solvable quantum antiferromagnet model*, arXiv:cond-mat/0508218 (first posted 2005-08-09), https://arxiv.org/abs/cond-mat/0508218.
2. B. K. Chakrabarti, A. Das and J.-i. Inoue, *Analysis of the long-range random field quantum antiferromagnetic Ising model*, arXiv:cond-mat/0512043 (2005-12-02), https://arxiv.org/abs/cond-mat/0512043.
3. V. K. Varma, *Antiferromagnetic Ising model saturation field entropies: ladders and kagome lattice*, arXiv:1305.4606 (2013-05-20), https://arxiv.org/abs/1305.4606.
4. Y. Dubi and M. Di Ventra, *Dimer mean-field model for the Ising spin glass*, arXiv:0912.2959 (2009-12-15), https://arxiv.org/abs/0912.2959.
