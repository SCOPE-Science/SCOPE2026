# Exact two-step majority attractor basins on \(K_{n,n,n}\)

## Finding

For every integer \(n\ge1\), consider synchronous binary majority with tie retention on the complete tripartite graph \(K_{n,n,n}\), whose three labelled parts each have \(n\) vertices. Every initial configuration reaches a fixed point or a primitive period-two orbit **within two simultaneous updates**. A configuration with initial part-wise counts \((a,b,c)\in\{0,\ldots,n\}^3\) enters a primitive two-cycle if and only if, after permuting the three parts,
\[
a+b=n,\qquad \min(a,b)<c<\max(a,b).
\]
The three possible choices of the middle, permanently frozen part are disjoint. The number of **labelled initial configurations in the eventual two-cycle basins** is exactly
\[
B_n=3\sum_{a=0}^{n}\binom{n}{a}\binom{n}{n-a}\sum_{\min(a,n-a)<c<\max(a,n-a)}\binom{n}{c}.
\]
The number of configurations already lying on primitive two-cycles is \(P_n=6(2^n-2)\), and the number of non-consensus fixed configurations is \(H_n=\binom{n}{n/2}^3\) for even \(n\), and zero for odd \(n\). Precisely \((8^n-B_n-H_n)/2\) initial configurations converge to each of the two consensus fixed points. The non-consensus fixed configurations are exactly those with each part containing half ones (possible only for even \(n\)).

For i.i.d. unbiased initial opinions, the probability of eventual primitive period-two motion satisfies the sharp asymptotic
\[
\Pr(\text{eventual primitive period two})\sim \frac{6\arctan(1/\sqrt{2})}{\pi^{3/2}\sqrt{n}}
=\frac{0.663193377639\ldots}{\sqrt n}.
\]
This probability is polynomially small even though the fraction of configurations **already periodic at time zero** is exponentially small.

## Assumptions and scope

Vertices carry opinions in \(\{0,1\}\). At each integer time all vertices synchronously compare opinions of their \(2n\) graph neighbors, adopt the strict majority, and retain their own opinion if exactly \(n\) neighbors have each opinion. There are no loops or edges inside parts; all edges between different parts are present. Vertex identities within each part are retained when counting initial configurations. The statements hold for every integer \(n\ge1\), including tie cases; probabilities use independent fair Bernoulli opinions initially.

A *basin* here means the set of initial configurations whose forward trajectory enters the specified eventual attractor. Reaching a period-two orbit within two updates means that the configuration at time \(2\) belongs to that orbit, not that every initial configuration has period two.

## Proof

**1. Exact quotient dynamics.** Let \((a,b,c)\) be the three counts of opinion-one vertices, and write \(S=a+b+c\), \(T=S-n\). The common neighbor-one count for every vertex of the first part is \(b+c=S-a\); similarly for the others. Thus the quotient update is
\[
F_n(a,b,c)=(\psi_n(a,b+c),\psi_n(b,a+c),\psi_n(c,a+b)),
\]
where \(\psi_n(v,s)=n\) if \(s>n\), \(\psi_n(v,s)=0\) if \(s<n\), and \(\psi_n(v,s)=v\) if \(s=n\). Equivalently, comparing each part count to \(T\), a part becomes all ones when its count is less than \(T\), becomes all zeros when its count is greater than \(T\), and otherwise retains every individual opinion unchanged (not merely its count). Hence a part is nonuniform after one update only if its original count equals \(T\).

**2. If no count equals \(T\), consensus follows.** After one update all parts are homogeneous. A homogeneous state with zero, one, two or three all-one parts maps in at most one further update to the corresponding all-zero or all-one consensus (zero or one all-one parts yield zero; two or three yield one). These two consensus states are fixed.

**3. Exactly one equality.** Suppose \(c=T\), so \(a+b=n\), and \(a,b\ne T\). If \(a<T<b\) or \(b<T<a\), the first update makes the other two parts all ones and all zeros, respectively, leaving every opinion in part three unchanged. Since these two homogeneous parts then have neighbor-one counts \(c\) and \(n+c\), they exchange their opinions at every update, whereas the third part always sees exactly \(n\) ones and retains all its opinions. This is a primitive period-two orbit. The inequalities are exactly \(\min(a,b)<c<\max(a,b)\). If the two other counts both lie below or both above \(T\), they become equal homogeneous parts and the next update gives consensus.

**4. At least two equalities.** If \(a=b=T\), the identity \(S=n+T\) implies \(c=n-T\). For \(T<n/2\), the first update replaces the third part by zeros, and the next replaces both other parts by zeros; for \(T>n/2\), the symmetric argument gives all ones. If \(T=n/2\), all three counts equal \(n/2\), and each vertex sees exactly \(n\) ones forever. Thus these, and only these, are the additional fixed configurations. The cases exhaust all initial triples and establish \(F_n^4=F_n^2\) at the vertex level.

**5. Census.** The period-two criterion chooses a frozen part in three ways; the remaining two part counts sum to \(n\). The number of labelled assignments with given triple of counts is \(\binom na\binom n{n-a}\binom nc\), yielding \(B_n\). The three choices are disjoint: two different choices would force two of the counts equal, contradicting the strict middle condition. For an initial configuration already on a primitive two-cycle, choose its frozen part (three choices), its nonuniform frozen assignment (\(2^n-2\) choices), and which of the two other parts is all ones (two choices), giving \(P_n\). The fixed all-half count is \(H_n\). Global opinion complementation exchanges the two consensus basins and preserves the other types, proving their equal sizes and the formula \((8^n-B_n-H_n)/2\).

**6. Asymptotic probability.** Let \(A,B,C\) be independent \(\operatorname{Bin}(n,1/2)\) random variables. The three frozen-part events are disjoint, so
\[
\frac{B_n}{8^n}=3\Pr(A+B=n)\Pr\!\left(\,|C-n/2|<|A-n/2|\ \middle|\ A+B=n\right).
\]
The first factor is \(\binom{2n}{n}4^{-n}\sim(\pi n)^{-1/2}\). Conditional on \(A+B=n\), the distribution of \(A\) is hypergeometric with \(\operatorname{Var}(A)=n^2/(4(2n-1))\), independent of \(C\), whose variance is \(n/4\). Their joint centered fluctuations divided by \(\sqrt n\) converge to independent Gaussians with variances \(1/8\) and \(1/4\). The strict-cone boundary has Gaussian probability zero. The limiting conditional probability is the angular probability
\[
\Pr(|Z_2|<|Z_1|/\sqrt2)=\frac2\pi\arctan(1/\sqrt2),
\]
where \(Z_1,Z_2\) are independent standard normal variables. Combining limits gives the stated constant.

## Verification

The scripts `code/check_direct.py` and `code/check_compressed.py` are standalone Python 3 programs using only the standard library. Run `python3 code/check_direct.py` and `python3 code/check_compressed.py` from a folder containing `code/`. The former enumerates every labelled vertex state for \(1\le n\le5\), applies the vertex-wise update (not a pre-reduced quotient), and checks attraction, the criterion, orbit populations, and complement symmetry. The latter independently iterates the quotient map for every count triple through \(n=30\), weights triples by exact binomial multiplicity and checks all formulas; it additionally calculates the approach to the limiting constant for \(n=100,200,500\). Captured reproducible output is in `verification/direct_output.txt` and `verification/compressed_output.txt`. None of these finite computations substitutes for the all-size proof or the central limit theorem.

## Relationship to prior work

Synchronous majority dynamics and the classical period-at-most-two phenomenon on finite undirected graphs are established; see Benjamini, Chan, O'Donnell, Tamuz and Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs* (arXiv:1405.2486v1, May 11, 2014), and the earlier general threshold-function work by Goles and Olivos (1980). Those general results do not by themselves count exact **eventual basins** or establish the tripartite square-root law. The new claim is the exact tripartite basin criterion, its labelled initial-condition census, and the asymptotic prefactor; it does not claim novelty of the general period-two bound. Nearby exact results about initially periodic states for multipartite networks also differ from counting the entire eventual basin of each attractor.

## Limitations

This theorem assumes exactly three *equally sized* labelled parts, synchronous *open-neighbor* majority and retention of a previous opinion on ties. It does not cover asynchronous updates, unequal part sizes, biased initial distributions, perturbed graphs, or exact absorption probabilities for nonuniform randomness. The asymptotic is a leading equivalence, not a finite-size error bound. Previous results on related threshold networks may contain equivalent formulations that were not found in the sources inspected; historical priority is therefore qualified. Independent scientific validation has not been performed.

## References

1. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1 (first public May 11, 2014), https://arxiv.org/abs/1405.2486 .
2. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1 .
