# A dense arithmetic first-order limit spectrum for two random involutions

## Finding

For each positive integer \(n\), let \(\sigma_n\) and \(\tau_n\) be **independent uniformly chosen involutions** of \([n]\). Regard \(([n],\sigma_n,\tau_n)\) as a structure in the language of two unary function symbols, with equality. The following statements hold.

1. **First-order convergence and arithmetic:** for every first-order sentence \(\varphi\), the limit \(L_\varphi=\lim_{n\to\infty}\Pr(([n],\sigma_n,\tau_n)\models\varphi)\) exists. There is an effectively obtainable positive integer \(D_\varphi\) such that \(L_\varphi\in\mathbb Q[e^{-1/D_\varphi}]\). The exact limiting expression is effectively obtainable as a rational polynomial in this exponential value (inefficient general-purpose locality bounds are permitted).
2. **Dense logical probability spectrum:** the set \(\{L_\varphi:\varphi\text{ first-order}\}\) is dense in \([0,1]\). In particular the model does not satisfy a zero–one law.
3. **Component input (previously known in substance):** for every fixed finite list of connected, isomorphism-distinct two-involution structures \(H_1,\ldots,H_t\), their component multiplicities converge jointly to independent Poisson variables of respective means \(1/|\operatorname{Aut}(H_j)|\). This component result is presented as a proof input, not as an independent historical-priority claim.

The first two conclusions provide an explicit arithmetical and topological description of the full first-order limiting probability spectrum for a natural pair of constrained random functions.

## Assumptions and scope

An involution is a permutation \(u\) satisfying \(u(u(x))=x\) for all \(x\). **Uniform** means each involution on \([n]\) has the same probability; the two choices are independent. In the undirected edge-coloured graph associated with the pair, a red edge joins \(x\ne\sigma(x)\) to \(\sigma(x)\), and a blue edge joins \(x\ne\tau(x)\) to \(\tau(x)\). A vertex fixed by a function retains a loop for that function in the relational encoding. Blue and red edges may be parallel between two vertices. The Gaifman degree is at most two.

Every connected component is a properly alternating red/blue path or an alternating even cycle. A one-vertex path is fixed by both maps. There is one isomorphism type of \(m\)-vertex path when \(m\) is odd, and two types when \(m\) is even; their colour-preserving automorphism groups have order \(1\) and \(2\), respectively. There is one alternating \(2k\)-cycle type for each \(k\ge1\), with colour-preserving automorphism group of order \(2k\) (for \(k=1\) it is the parallel-edge two-cycle).

All assertions concern fixed first-order sentences as \(n\to\infty\). The length of a term, the quantifier rank and the finite set of function symbols remain fixed independently of \(n\). No monadic second-order convergence, effective complexity bound of practical size, or uniform-in-sentence convergence rate is asserted.

## Proof

**Step 1: Exact mixed factorial moments.** Write \(I_n\) for the number of involutions on an \(n\)-element set. A classical asymptotic formula is
\[
I_n\sim \sqrt{n!}\,e^{\sqrt n}(8\pi e n)^{-1/4}.
\]
For every fixed nonnegative integer \(M\), therefore,
\[
\frac{I_{n-M}}{I_n}\sim n^{-M/2}.
\]
Fix pairwise nonisomorphic component types \(H_1,\ldots,H_t\) and nonnegative integers \(r_1,\ldots,r_t\). Put \(M=\sum_j r_j|H_j|\), and let \(C_{H_j}(n)\) count connected components isomorphic to \(H_j\). Assigning the specified \(M\) distinct labels to the ordered component copies can be done in
\[
(n)_M\prod_{j=1}^t|\operatorname{Aut}(H_j)|^{-r_j}
\]
ways. For each involution the restriction on these labels is fully prescribed and the remainder is an arbitrary involution on the other \(n-M\) labels. Independence gives the **exact identity**
\[
\mathbb E\!\left[\prod_{j=1}^t(C_{H_j}(n))_{r_j}\right]
=(n)_M\left(\frac{I_{n-M}}{I_n}\right)^2
\prod_{j=1}^t|\operatorname{Aut}(H_j)|^{-r_j}
\quad (n\ge M).
\]
It converges to \(\prod_j |\operatorname{Aut}(H_j)|^{-r_j}\). Mixed factorial moments therefore yield joint convergence to independent Poisson variables with the claimed means. For odd path sizes these means are \(1\); for each of the two even-path types they are \(1/2\); for an alternating \(2k\)-cycle they are \(1/(2k)\). These asymptotic component laws agree with the component generating functions and cycle laws in Lugo (2009).

**Step 2: Saturation of nonclosed local types.** Interpret the two functions as binary graphs of functions, including fixed-point loops. Every resulting relational structure has Gaifman degree at most \(2\). Fix a radius \(R\) and cutoff \(T\). A rooted \(R\)-ball is called *closed* when every vertex in the ball has its red and blue function-successors inside the ball; equivalently, this ball constitutes an entire connected component. Any closed \(R\)-ball has at most \(2R+2\) vertices, because connected components are paths or cycles of maximum degree two.

The number of roots realizing any closed ball type is a fixed nonnegative integer linear combination of component counts \(C_H(n)\) with \(|H|\le2R+2\). In particular, the vector of all such counts, truncated at \(T\), converges in distribution by Step 1.

Every realizable *nonclosed* rooted \(R\)-ball type occurs in infinitely many distinct alternating path component types of increasing odd order: extend its boundary edges along an alternating path beyond radius \(R\), and choose the far endpoints to make the total order odd. Any fixed selection of \(K\) such distinct path types has jointly independent Poisson limiting multiplicities, each with mean \(1\). Consequently, for every fixed \(T\), the probability that the given nonclosed rooted type occurs at least \(T\) times tends to \(1\): first select sufficiently many fixed distinct odd path sizes so that the sum of their limiting Poisson counts exceeds \(T\) with probability arbitrarily near \(1\), then let \(n\) grow. There are only finitely many rooted \(R\)-ball types in degree two, so all nonclosed types are simultaneously saturated with probability tending to one.

**Step 3: The complete first-order convergence law.** Translate a given functional first-order sentence \(\varphi\) into the equivalent relational sentence for the graphs of the two functions. This can be done by introducing variables for nested terms. By effective bounded-degree Hanf locality, there exist computable \(R,T\) such that the truth of this sentence is determined by the counts of each rooted \(R\)-ball type, truncated at \(T\). Step 2 makes all nonclosed counts eventually saturated and expresses every closed count through finitely many small-component counts. Their joint Poisson limits from Step 1 therefore determine \(L_\varphi\).

More explicitly, let \(\mathcal H_R\) be the finite family of all component types with at least one root having a closed \(R\)-ball. Put \(\mu_H=1/|\operatorname{Aut}(H)|\). The limiting probability can be computed by summing independent Poisson weights over the finitely many truncated component-count vectors \((\min(C_H,T))_{H\in\mathcal H_R}\); a finite representative can be built from the requisite small components together with sufficiently many sufficiently long alternating paths to saturate every nonclosed local type. Each Poisson point mass below \(T\), and each corresponding upper tail, is a rational polynomial in \(e^{-\mu_H}\). Since all \(\mu_H\) are positive rationals, taking a common denominator \(D_\varphi\) proves \(L_\varphi\in\mathbb Q[e^{-1/D_\varphi}]\). All described finite transformations are effective, without a claim of tractable complexity.

**Step 4: Density.** For any fixed odd positive integer \(m\), first-order logic can assert that there exists a whole connected component isomorphic to the unique alternating path of order \(m\): existentially name its \(m\) distinct vertices, prescribe both function values on them, and require the named set be closed under both functions. Let \(E_m\) denote this sentence. From Step 1, for any finite list of distinct odd sizes the truth indicators of \(E_m\) converge jointly to independent Bernoulli variables with common parameter \(p=1-e^{-1}\in(0,1)\).

Any Boolean combination of \(K\) distinct such sentences has a limiting probability equal to the probability of a union of atoms in a \(K\)-fold Bernoulli product. The maximum atom weight is \((\max\{p,1-p\})^K\to0\). Order these atoms arbitrarily and include successive atoms until their cumulative probability first exceeds a prescribed \(a\in[0,1]\). The resulting Boolean combination has limiting probability within that maximum atom weight of \(a\). Therefore the set of limiting first-order probabilities is dense in \([0,1]\). In particular \(\Pr(E_1)\to1-e^{-1}\), ruling out a zero–one law.

## Verification

The accompanying standalone standard-library Python program `check_involutions.py` enumerates all pairs of involutions through seven labels, classifies every connected two-colour component, verifies that component sizes add to the domain size, and checks eleven exact mixed factorial-moment identities per domain size against the unrestricted-involution counting formula. The total number of ordered pairs enumerated over domain sizes one through seven is \(60{,}397\).

Execute `python check_involutions.py`. Its final output line is `INVOLUTION_COMPONENT_MOMENTS_OK 60397 11`. This is a finite exact check of the component formulas, **not** an exhaustive check of first-order sentences and not a proof of the asymptotic or locality steps.

## Relationship to prior work

Lugo's 2009 paper gives the generating function for the alternating path-and-cycle decomposition of pairs of random involutions (Theorem 4.1) and the Poisson path/cycle contribution to permutation cycle counts (Theorem 5.1, Section 6). The component Poisson input above is thus established mathematics, not an independent discovery. The focus here is the **full two-function first-order limiting law**, its effective rational-exponential arithmetic and its dense probability spectrum.

Mirabi and Shelah (first arXiv posting July 13, 2026) develop component-sensitive first-order laws for different sparse graph models using Hanf locality and Poisson component thresholds. Their hypotheses concern pruned independent-edge graphs and percolated tori; neither random involution-pair distribution nor the present limiting probability spectrum follows directly from their stated theorems. Hanf locality itself is classical. General disjoint-union limit-law frameworks, particularly Compton's work, may provide abstract sufficient conditions for convergence, and are not claimed as new principles here. The specific complete arithmetic-and-density statement was not identified in the accessible literature, but historical priority has not been independently established.

## Limitations

The arithmetic conclusion concerns **first-order** logic over the exact two-involution sampling law. It does not assert a monadic-second-order limit law, a rate of convergence, or a sharp complexity bound for the effective algorithm. The Poisson component distribution is substantially covered by Lugo (2009), and the locality device is classical. An inaccessible full comparison with Compton's 1987 general framework leaves residual risk that a stronger general result implies some of the stated logical consequences. No claim of absolute historical novelty or independent audit is made.

## References

1. Mostafa Mirabi and Saharon Shelah, *Limit laws for component-pruned sparse random graphs and percolated tori*, arXiv:2607.11033, first posted 2026-07-13, primary MSC2020 03C13. Sections 1–2 and 4 explain the relevant locality method for different random structures.
2. Michael Lugo, *The cycle structure of compositions of random involutions*, arXiv:0911.3604, first posted 2009-11-18. In particular Theorems 4.1 and 5.1 and Section 6.
3. Kevin J. Compton, *A logical approach to asymptotic combinatorics I: First order properties*, Advances in Mathematics 65 (1987), 65–96. Full text not inspected; comparison remains a historical-priority risk.
4. W. Hanf, *Model-theoretic methods in the study of elementary logic*, 1965, and R. Fagin, L. Stockmeyer, and M. Vardi, finite bounded-degree Hanf locality (as referenced by Mirabi–Shelah).
