# Determinant law and independent Poisson obstructions for alternating two-agent S5 possibility

## Finding

Let \(n\ge1\) and \(d\ge1\) be integers. Choose two independent uniformly random perfect matchings on \(2n\) labelled worlds; adding all loops to each matching makes two equivalence relations \(E\) and \(F\). Independently, let proposition \(p\) hold at each world with probability \(u\in[0,1]\), and write \(q=1-u\). Let \(G_{n,d}\) be the event that, **at every world**, both alternating possibility formulas of exactly \(d\) modalities, starting with \(\Diamond_E\) and \(\Diamond_F\) respectively and ending with \(p\), hold. Put \(k=2d\). Define the \(k\times k\) matrix \(T_k(u)\), indexed by \(0,\ldots,k-1\), by \((T_k)_{i0}=u\), \((T_k)_{i,i+1}=q\) for \(i<k-1\), and all other entries zero; contributions to the same entry add if needed. Then the following identity holds **exactly for every** \(n,d,u\):

\[
\boxed{\Pr(G_{n,d})=\frac{[z^n]\det(I_k-zT_k(u)^2)^{-1/2}}{[z^n](1-z)^{-1/2}}.}
\]

The square root is the unique formal power series with constant coefficient one. In particular, \(\det(I_k-zT_k(u)^2)=g_k(\sqrt z)g_k(-\sqrt z)\), where \(g_k(t)=1-u\sum_{j=1}^kq^{j-1}t^j\); the product is a polynomial in \(z\).

For fixed \(d\), assume \(q=q_n\to0\) and \(nq_n^{2d}\to t\in[0,\infty)\). Let \(X_{E,n,d}\) and \(X_{F,n,d}\) be, respectively, the numbers of \(E\)-equivalence classes and \(F\)-equivalence classes whose corresponding alternating-start formula is false. Then

\[
\boxed{(X_{E,n,d},X_{F,n,d})\ \xrightarrow{\mathrm d}\ (P_E,P_F),\quad P_E,P_F\ \text{independent Poisson}(t),}
\]

and hence \(\Pr(G_{n,d})\to e^{-2t}\). If instead \(q_n\to0\) and \(nq_n^{2d}\to\infty\), this probability tends to zero. For fixed \(c>0\) and \(q_n=c n^{-1/(2d)}\), let \(D_n\) be the least positive depth for which \(G_{n,D_n}\) holds, with \(D_n=\infty\) if no such depth exists. Then

\[
\Pr(D_n=d)\to e^{-2c^{2d}},\qquad \Pr(D_n=d+1)\to 1-e^{-2c^{2d}},
\]

and the probability of every other depth tends to zero.

Finally, for fixed \(d\ge1\) and \(u\in(0,1)\), let \(\rho\) be the Perron eigenvalue of \(T_k(u)\) and \(\lambda_2,\ldots,\lambda_k\) its other eigenvalues counted with multiplicity. Then \(0<\rho<1\), \(|\lambda_j|<\rho\), and

\[
\boxed{\Pr(G_{n,d})\sim C_{d,u}\rho^{2n},\qquad C_{d,u}=\prod_{j=2}^{k}\left(1-\frac{\lambda_j^2}{\rho^2}\right)^{-1/2}>0.}
\]

The product is interpreted by analytic continuation from \(z=0\) and takes the positive real branch. Thus the exact coefficient law gives both a sharp rare-unmarked critical window and the fixed-marking exponential decay rate.

## Assumptions and scope

The two pairings are independent and uniform on all perfect matchings, not uniform on connected cycles or on simple degree-two graphs. Loops are added only to make each matching a reflexive equivalence relation; a coincident edge of the two matchings is allowed. The valuation of the single atom \(p\) is independent over worlds and independent of both pairings. A possibility \(\Diamond_E\psi\) is true at \(w\) if \(\psi\) is true at some \(E\)-equivalent world, including \(w\). Every statement is about finite labelled frames and global truth at all worlds. Formulas alternate strictly between the two agents, with no temporal operators or other atoms.

## Proof

**1. Alternating-cycle representation.** Fix the first pairing. Contract its \(n\) pairs to labelled vertices. A second pairing partitions them into bicoloured alternating cycles; a component with \(\ell\) first-pair vertices has \(2\ell\) original worlds and forms an even cyclic sequence with alternating pair edges. For a prescribed subset of \(\ell\) first-pair vertices, the number of second matchings connecting them in one component is \(2^{\ell-1}(\ell-1)!\) (the formula also holds for the double-edge \(\ell=1\) component). Consequently, the component-count distribution is

\[
\Pr(C_1=c_1,\ldots,C_n=c_n)=\frac{n!}{(1/2)^{\overline n}}\prod_{\ell=1}^n\frac{(1/(2\ell))^{c_\ell}}{c_\ell!},\qquad\sum_\ell\ell c_\ell=n.
\]

Here \((1/2)^{\overline n}\) denotes the rising factorial. The exponential generating series for these weights is \((1-z)^{-1/2}\).

**2. Equivalence of modal failure and a cyclic zero run.** On a bicoloured component, the worlds reachable from any starting world by a prescribed alternating \(d\)-modality word are exactly \(2d\) consecutive positions in the cyclic word, interpreted modulo \(2\ell\), or the entire component when \(2d\ge2\ell\). Taking both initial agents and all starting worlds sweeps every cyclic starting position. Therefore \(G_{n,d}\) holds on this component exactly when every cyclic block of \(k=2d\) consecutive positions contains a marked world. For a component shorter than \(k\), the cyclic word is periodically repeated, so the same assertion means that at least one world in that component is marked. This convention covers coincident pairing edges without an exception.

**3. Transfer matrix and exact cycle index.** The state \(i\in\{0,\ldots,k-1\}\) records the number of consecutive unmarked positions immediately before reading a bit. Reading a mark resets this count to zero with weight \(u\); reading an unmarked bit advances by one with weight \(q\), unless this would create a forbidden \(k\)-run. Closed state walks of length \(2\ell\) are in weight-preserving bijection with admissible cyclic words of length \(2\ell\). Thus their total probability is \(a_\ell=\operatorname{tr}(T_k^{2\ell})\). For \(u\in(0,1)\), uniqueness of the stationary state walk for each admissible word follows because every admissible periodic word contains a mark; the endpoints \(u=0,1\) follow directly. The cycle index in step 1 therefore gives

\[
\sum_{n\ge0}b_nz^n=\exp\!\left(\sum_{\ell\ge1}\frac{\operatorname{tr}(T_k^{2\ell})}{2\ell}z^\ell\right)=\det(I_k-zT_k^2)^{-1/2}.
\]

Dividing \(b_n\) by \([z^n](1-z)^{-1/2}=\binom{2n}{n}/4^n\) proves the first identity. The formula for \(g_k\) follows by computing \(\det(I-tT_k)\); multiplying the determinants with \(t=\pm\sqrt z\) gives the displayed polynomial expression.

**4. Joint critical window.** A component with \(\ell\le d\) first-pair vertices contributes at most \(2\ell\) exceptional candidate starting windows. From the exact cycle count, \(\mathbb E C_\ell\to1/(2\ell)\) for each fixed \(\ell\), so the expected number of worlds on such short components is bounded by a constant depending on \(d\). Their chance of being entirely unmarked tends to zero. All remaining components have length \(2\ell>k\). Their \(n-O_{\mathsf P}(1)\) first-agent and \(n-O_{\mathsf P}(1)\) second-agent classes give distinct cyclic windows of exactly \(k\) positions. Conditional on the pairings, each such window is unmarked with probability \(q_n^k\). Every window overlaps only \(O_d(1)\) other windows, and distinct overlapping windows have a union of at least \(k+1\) vertices. Thus a two-colour Poisson approximation by the dependency-graph method has first error term \(O_d(nq_n^{2k})\) and overlap term \(O_d(nq_n^{k+1})\), both vanishing when \(nq_n^k\to t<\infty\) and \(q_n\to0\). The two colours therefore converge jointly to independent Poisson variables with mean \(t\), including \(t=0\). Exact independence of disjoint windows holds conditional on the pairings, so this convergence persists after averaging over them.

If \(nq_n^k\to\infty\), discard the bounded-in-probability small components and greedily select at least \(\Omega_d(n)\) pairwise disjoint long-component windows. Their unmarked events are conditionally independent, so the probability of avoiding all of them is at most \((1-q_n^k)^{\Omega_d(n)}+o(1)\to0\). Monotonicity of the global success event with depth follows from reflexivity of \(E,F\). At \(q_n=c n^{-1/(2d)}\), the depth-\(d\) critical law applies, all lower depths fail with probability tending to one, and depth \(d+1\) succeeds with probability tending to one by the zero-intensity case. This proves the two-point depth law.

**5. Fixed-marking asymptotic.** For \(0<u<1\), the finite nonnegative matrix \(T_k(u)\) is primitive (every state can reset to state zero, and state zero has a positive self-loop). Its spectral radius \(\rho\) is simple and strictly dominates the moduli of all other eigenvalues. Since the last row has sum \(u<1\) and the matrix is irreducible, \(\rho<1\). The determinant factors as \((1-\rho^2z)\prod_{j=2}^k(1-\lambda_j^2z)\). The second factor is analytic and nonzero on a disk strictly larger than \(|z|\le\rho^{-2}\). Standard square-root coefficient asymptotics give \([z^n]\det(I-zT_k^2)^{-1/2}\sim C_{d,u}\rho^{2n}/\sqrt{\pi n}\). Since \([z^n](1-z)^{-1/2}\sim1/\sqrt{\pi n}\), the final asymptotic follows.

## Verification

The included standalone standard-library checker enumerates all \((2n-1)!!\) second pairings for \(n=1,2,3,4\), all \(2^{2n}\) Boolean valuations, and depths \(d=1,2,3\) at exact rational marking probability \(u=2/5\). It compares (i) truth of the actual alternating modal formulas at every world, (ii) independent component-factor probabilities, and (iii) rational coefficient extraction from the determinant's trace expansion. All 12 combinations agree exactly. A separate calculation enumerates all pairings through \(n=5\) and checks 15 exact expected-cycle-count formulas. The command is `python checker.py`. These finite tests check identities and boundary cases; they do not replace the analytic arguments for all sizes and asymptotic limits.

## Relationship to prior work

Zantedeschi (2026) develops modal exchangeability on S4 and S5 frames and motivates probabilistic questions involving epistemic accessibility; its representation theorems are for valuation laws on structured frames and do not state these random-pairing determinant probabilities. Aldini and Fusco (2026) develop a multi-agent S5 model-and-logic framework, not the present random frame model. The independent Bernoulli rare-run Poisson method is classical; in particular Godbole (1991) studies runs in a fixed Bernoulli sequence. The new jointly assessed object is the exact finite matching-pair coefficient identity, its two-agent obstruction spectrum, and the fixed-probability spectral rate. The matching-cycle count and the logarithmic determinant identity are classical combinatorial tools, not claimed as separate discoveries.

## Limitations

The pairings must be independent and uniform, all equivalence classes have size two, the marking bits are independent, and modal success is global for both alternating starting agents. The convergence results fix the formula depth. The result does not establish a comparable determinant for larger equivalence classes, correlated matchings, other modal operators, or general S5 frames. The apparent absence of an equivalent theorem is assessed only against the inspected sources and queried research records, not by an exhaustive historical-priority search; an older abstract-only runs paper was not inspected in full. No independent mathematical audit has been performed.

## References

1. Daniel Zantedeschi (2026), *A Modal de Finetti Theorem: Exchangeability under S4 and S5*, arXiv:2603.27547v1, first public 29 March 2026, https://arxiv.org/html/2603.27547v1.
2. Alessandro Aldini and Ludovico Fusco (2026), *Bridging concurrency theory and epistemic models: a formal framework for dynamic multi-agent systems*, Journal of Logic, Language and Information, first published 11 March 2026, DOI:10.1007/s10849-026-09461-3.
3. Anant P. Godbole (1991), *Poisson approximations for runs and patterns of rare events*, Advances in Applied Probability **23**(4), 851–865, DOI:10.2307/1427680.
4. Richard Arratia, Larry Goldstein and Louis Gordon (1989), *Two moments suffice for Poisson approximations: the Chen–Stein method*, Annals of Probability **17**, 9–25, DOI:10.1214/aop/1176991491.
