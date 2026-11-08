# Parity and one-defect transitions for Lipschitz variance on contracted equilateral matchings

## Finding

Let \(k\ge2\) be an integer and \(0<\lambda<1\). Partition \(2k\) points into \(k\) matched pairs. Give matched distinct points distance \(\lambda\) and all points belonging to different pairs distance \(1\); write \(M_{k,\lambda}\) for this finite metric and equip it with uniform probability. The sharp variance of real one-Lipschitz functions is

\[
\boxed{\operatorname{spr}(M_{k,\lambda})=
\begin{cases}
\frac14,&k\text{ even},\\[3pt]
\frac14-\frac{1}{4k^2}+\frac{[\lambda((2k-1)\lambda-2(k-1))]_+}{4k^2},&k\text{ odd},
\end{cases}}
\]
where \([u]_+=\max\{u,0\}\). For odd \(k\), the exact optimizer transition occurs at
\[
\boxed{\lambda_k=\frac{2(k-1)}{2k-1}.}
\]

Every maximizer is determined up to an additive constant, a permutation of pairs, and reversal of vertices within each pair. For even \(k\), it assigns \(0\) to both vertices in precisely half of the pairs and \(1\) to both vertices in the other half. For odd \(k\) below the transition, it is binary with \((k-1)/2\) or \((k+1)/2\) whole pairs at \(1\) and the others at \(0\). Above the transition, its values on exactly one pair are either \((0,\lambda)\) or \((1-\lambda,1)\), while the remaining \(k-1\) pairs consist of equally many whole \((0,0)\) and \((1,1)\) pairs. At the transition, exactly the two described types coexist. No other maximizers occur.

Thus the entire equilateral variance \(1/4\) survives contracting a perfect matching precisely when the number of matched pairs is even (at every fixed \(0<\lambda<1\)). For odd \(k\), there is an initial constant-variance plateau followed by a strict one-defect quadratic recovery as the shortened distances increase toward \(1\).

## Assumptions and scope

The ground set has \(2k\ge4\) distinct points. All its off-diagonal distances are positive; the metric triangle inequality holds because the only short edges form a matching. For a real function \(f\) define \(\operatorname{Lip}(f)=\max_{u\ne v}|f(u)-f(v)|/d(u,v)\), and
\[
\operatorname{spr}(M)=\max_{\operatorname{Lip}(f)\le1}
\left(\frac1{|M|}\sum_{v\in M}f(v)^2-\left(\frac1{|M|}\sum_{v\in M}f(v)\right)^2\right).
\]
The maximum exists by compactness modulo constants. No claim is made here for nonuniform vertex probabilities, unequal shortening parameters, or intersecting short edges. The endpoint \(\lambda=1\) is not included in the optimizer classification because the matching constraints then disappear.

## Proof

**1. Extremal reduction and the six paired states.** Fix a basepoint value to zero. The one-Lipschitz potentials form a compact convex polytope. The variance quadratic form is strictly convex on the quotient by constants, because every vertex has positive probability. Hence each maximizing potential is a vertex of this polytope. At a vertex the graph of tight distance inequalities is connected: its signed incidence vectors must span the \((2k-1)\)-dimensional quotient, and a graph's incidence rank is one less than its number of vertices exactly when it is connected.

Tight edges of length \(\lambda\) form a matching and therefore cannot alone connect \(2k\ge4\) vertices. A vertex potential must contain a tight edge of length \(1\). Since all pairwise metric distances are at most \(1\), its range is exactly \(1\); shift its minimum to \(0\) and its maximum to \(1\). In any matched pair, at least one endpoint lies at \(0\) or \(1\), for otherwise that pair cannot connect by a tight edge to any other pair. A pair cannot contain both \(0\) and \(1\) because \(\lambda<1\). A second, interior endpoint must be separated from the first by exactly \(\lambda\) or it has no tight edge. Thus the only possible ordered pair states are
\[
(0,0),\ (1,1),\ (0,\lambda),\ (\lambda,0),\ (1-\lambda,1),\ (1,1-\lambda).
\]
There must be at least one lower and one upper pair, where the three states containing \(0\) are lower and the three containing \(1\) are upper. Conversely, every assignment of these states with both lower and upper pairs is feasible and is a vertex: tight cross-pair edges connect every zero anchor to every one anchor; a remaining interior endpoint is attached by its own tight short edge. This reproduces the relevant tight-edge argument for this special metric independently of any general polytope facet theorem.

**2. Pairwise elimination of multiple split pairs.** Call a pair *split* if it has one interior value. Reverse within-pair order when convenient. If a split lower pair \((0,\lambda)\) and a split upper pair \((1-\lambda,1)\) coexist, replace them by whole pairs \((0,0)\) and \((1,1)\). Their total sum remains \(2\), while their sum of squares rises by \(2\lambda(1-\lambda)>0\); thus the variance strictly increases, contradicting optimality.

If two lower split pairs coexist, their four values are \((0,\lambda),(0,\lambda)\). Consider two feasible pure replacements: with probability \(\lambda\) put one pair at \((0,0)\) and the other at \((1,1)\), and with probability \(1-\lambda\) put both pairs at \((0,0)\). The expected total sum of these four vertices is unchanged at \(2\lambda\), while their expected sum of squares rises from \(2\lambda^2\) to \(2\lambda\). Writing \(2k\) for the total number of vertices, the random replacement increases *expected* variance by exactly
\[
\frac{2\lambda-2\lambda^2}{2k}-\frac{4\lambda(1-\lambda)}{(2k)^2}
=\frac{(k-1)\lambda(1-\lambda)}{k^2}>0.
\]
At least one of the two deterministic feasible replacements therefore improves the variance. By replacing \(f\) with \(1-f\), the same conclusion holds for two upper split pairs. Combining the three cases, **every maximizing potential contains at most one split pair**. This conclusion uses strict inequalities and is valid for every \(k\ge2\) and \(0<\lambda<1\).

**3. All-pure candidates.** If exactly \(a\) of the \(k\) pairs are \((1,1)\), the variance is
\[
V_{\mathrm{pure}}(a)=\frac{a(k-a)}{k^2}.
\]
For even \(k\), its maximum is \(1/4\), attained only at \(a=k/2\). Since every Lipschitz function has range at most one, Popoviciu's variance bound gives \(\operatorname{Var}(f)\le1/4\), with equality only for a half-and-half binary distribution; thus the even case and its full equality classification follow immediately.

For odd \(k\), the pure maximum is
\[
B_k=\frac{k^2-1}{4k^2},
\]
attained only for \(a=(k-1)/2\) or \(a=(k+1)/2\).

**4. One-split candidates and the sharp transition.** By the symmetry \(f\mapsto1-f\), assume the unique split pair is \((0,\lambda)\). If \(a\) of the remaining \(k-1\) pairs are all one, its variance equals
\[
V_{\mathrm{mix}}(a)=\frac{2a+\lambda^2}{2k}-\frac{(2a+\lambda)^2}{4k^2}.
\]
The exact finite difference is
\[
V_{\mathrm{mix}}(a+1)-V_{\mathrm{mix}}(a)=\frac{k-2a-\lambda-1}{k^2}.
\]
For odd \(k=2r+1\), this is positive when \(a<r\) and negative when \(a\ge r\), so its unique maximum over \(0\le a\le k-1\) occurs at \(a=r=(k-1)/2\). Write this maximum as \(W_k(\lambda)\). Direct expansion gives
\[
W_k(\lambda)-B_k=
\frac{\lambda((2k-1)\lambda-2(k-1))}{4k^2}.
\]
The sign changes exactly at \(\lambda_k=2(k-1)/(2k-1)\). Comparing the exhaustive pure and one-split possibilities establishes the displayed sharp variance and every equality configuration. The case of one upper split pair is obtained by complementation. At equality of the two candidate values, both classes maximize; no others can, by the strict elimination in Step 2 and the strict discrete unimodality in this step. \(\square\)

## Verification

The included standalone Python program `verify_matching_spread.py` uses integer numerators for rational shortening parameters. It independently reconstructs every dual extreme potential from signed tight spanning trees for \(k=2\) and \(k=3\) (including the critical length \(4/5\)), and checks that this set agrees with the six-state classification. It also maximizes the exact variance numerator over all \(6^k\) assignments for \(2\le k\le6\), checking the formula and **all equality cases** at \(22\) parameter instances. It evaluates the exact phase boundary for odd \(k\le23\). The program printed `ALL_MATCHED_EQUILATERAL_SPREAD_CHECKS_OK`. These computations check finite instances; the proof above establishes the theorem for every integer \(k\ge2\) and all real \(\lambda\in(0,1)\).

Reproduce by running `python3 verify_matching_spread.py` with Python's standard library; no third-party packages are required.

## Relationship to prior work

Addario-Berry, Janson and McDiarmid's 2009 full text introduces the classical finite-graph spread and records the sharp equilateral complete-graph value. Gordon and Petrov's 2016 full text studies the combinatorics of finite-metric Lipschitz polytopes, including tight-constraint admissibility and generic metrics, rather than sharp variances of these nongeneric matching-contracted metrics. The published result *Facet enumeration for equilateral metrics with independently shortened pairs* classifies precisely the six-state dual extreme potentials for arbitrary matching-contracted metrics and counts them; this supplies an overlapping, stronger **vertex classification**, but does not optimize their centered squared norm, derive at-most-one-split localization, or give this parity-sensitive phase threshold. The published *Sharp Euclidean Banach--Mazur distance of real finite equilateral Lipschitz-free spaces* optimizes the uncontracted equilateral space against all Euclidean norms, a different functional and parameter regime. Its balanced binary calculation is consistent with the uncontracted limiting value. None of those inspected full texts states a variance formula or optimizer transition for the present family. This comparison does not establish exhaustive novelty in all literature.

## Limitations

The result is specific to finite real Lipschitz functions, strictly positive equal vertex masses, and an equilateral metric with one *perfect matching* of equal shortened distances. It does not classify arbitrary positive vertex weights, unmatched singleton vertices, differing matched-pair distances, higher moments, or arbitrary short-edge graphs. The metric at \(\lambda=1\) has a larger optimizer family not covered by the displayed classification; the spread converges to \(1/4\) as \(\lambda\uparrow1\). The proof is an exact finite-dimensional argument, not an independent validation or a claim of precedence over all unindexed sources.

## References

1. L. Addario-Berry, S. Janson, C. McDiarmid, *On the spread of random graphs*, arXiv:0902.1156v1, first public 2009-02-06, https://arxiv.org/abs/0902.1156.
2. J. Gordon, F. Petrov, *Combinatorics of the Lipschitz polytope*, arXiv:1608.06848v1, first public 2016-08-24, https://arxiv.org/html/1608.06848v1.
3. *Facet enumeration for equilateral metrics with independently shortened pairs*, public 2026-10-11, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-facet-enumeration-for-equilateral-metrics-with-independently-sho--3bd6d7048744/RESULT.md.
4. *Sharp Euclidean Banach--Mazur distance of real finite equilateral Lipschitz-free spaces*, public 2026-10-11, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-sharp-euclidean-banach-mazur-distance-of-real-finite-equilateral--1cb03298c970/RESULT.md.
