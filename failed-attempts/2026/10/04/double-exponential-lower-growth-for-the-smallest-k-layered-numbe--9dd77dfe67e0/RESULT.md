# Double-exponential lower growth for the smallest \(k\)-layered number

## Finding
Let
\[
\mathcal K=\{k\ge2:\text{there exists a \(k\)-layered positive integer}\}.
\]
For each \(k\in\mathcal K\), let \(L_k\) denote the smallest \(k\)-layered number.

Then
\[
\liminf_{\substack{k\to\infty\\k\in\mathcal K}}
\frac{\log\log L_k}{k}
\ge e^{-\gamma},
\]
where \(\gamma\) is the Euler--Mascheroni constant.

Equivalently, for every \(\varepsilon>0\), there is a threshold \(k_0(\varepsilon)\) such that every
\[
k\in\mathcal K,\qquad k\ge k_0(\varepsilon),
\]
satisfies
\[
L_k\ge
\exp\!\left(
\exp\!\left((e^{-\gamma}-\varepsilon)k\right)
\right).
\]

Thus, if \(k\)-layered numbers exist for arbitrarily large \(k\), their smallest representatives grow at least double-exponentially in \(k\). This is substantially stronger on the lower-bound side than the exponential growth suggested in Jokar's Conjecture 2.5.

## Assumptions and scope
A positive integer \(n\) is \(k\)-layered if its positive divisors can be partitioned into \(k\) subsets having equal sum.

Jokar proves the elementary necessary condition
\[
\sigma(n)\ge kn
\]
for every \(k\)-layered integer \(n\). Equivalently, its abundancy index satisfies
\[
\frac{\sigma(n)}{n}\ge k.
\]

The argument below uses Grönwall's classical maximal-order theorem
\[
\limsup_{n\to\infty}
\frac{\sigma(n)}{n\log\log n}
=e^\gamma.
\]

The theorem is conditional only in the sense that \(L_k\) is defined for \(k\in\mathcal K\). It does not prove that \(\mathcal K\) is infinite; the existence of \(k\)-layered numbers for every \(k\) is separately open in Jokar's paper.

## Proof
Fix \(\varepsilon>0\).

By Grönwall's theorem, there exists \(N_\varepsilon\) such that every integer
\[
n\ge N_\varepsilon
\]
satisfies
\[
\frac{\sigma(n)}{n\log\log n}
\le e^\gamma+\varepsilon.
\]
Indeed, this is exactly the eventual upper-bound consequence of the stated \(\limsup\).

Now let \(k\in\mathcal K\) and suppose \(L_k\ge N_\varepsilon\). Since \(L_k\) is \(k\)-layered, Jokar's necessary condition gives
\[
k\le \frac{\sigma(L_k)}{L_k}.
\]
Combining the two inequalities yields
\[
k\le
(e^\gamma+\varepsilon)\log\log L_k,
\]
and hence
\[
\frac{\log\log L_k}{k}
\ge
\frac{1}{e^\gamma+\varepsilon}.
\]

As \(k\to\infty\) through \(\mathcal K\), one necessarily has \(L_k\to\infty\): otherwise infinitely many distinct values of \(k\) would be bounded above by the finitely many abundancy indices
\[
\frac{\sigma(n)}n
\]
for integers in a fixed finite interval. Therefore the condition \(L_k\ge N_\varepsilon\) holds for every sufficiently large \(k\in\mathcal K\).

Taking the lower limit along \(\mathcal K\) gives
\[
\liminf_{\substack{k\to\infty\\k\in\mathcal K}}
\frac{\log\log L_k}{k}
\ge
\frac{1}{e^\gamma+\varepsilon}.
\]
Finally let \(\varepsilon\downarrow0\). This gives
\[
\liminf_{\substack{k\to\infty\\k\in\mathcal K}}
\frac{\log\log L_k}{k}
\ge e^{-\gamma}.
\]

For the equivalent explicit form, fix \(\delta>0\). The lower-limit statement implies that all sufficiently large \(k\in\mathcal K\) satisfy
\[
\log\log L_k\ge(e^{-\gamma}-\delta)k.
\]
Exponentiating twice gives
\[
L_k\ge
\exp\!\left(
\exp\!\left((e^{-\gamma}-\delta)k\right)
\right).
\]

## Verification
The proof has no finite search or numerical certificate.

The proof-critical chain is:
\[
k\le\frac{\sigma(L_k)}{L_k}
\]
from the necessary condition for \(k\)-layered numbers, followed by the eventual Grönwall bound
\[
\frac{\sigma(n)}n\le(e^\gamma+\varepsilon)\log\log n,
\]
followed by a lower-limit passage and two exponentiations.

The quantifiers are important. The theorem is asserted only for \(k\in\mathcal K\), and the limiting statement is along those \(k\). No existence theorem for all \(k\) is inferred.

As a consistency check against the source, Jokar's tabulated smallest \(k\)-layered values for \(1\le k\le8\) all satisfy the elementary prerequisite
\[
\sigma(L_k)\ge kL_k.
\]
Those finite data are not evidence for the asymptotic theorem.

## Relationship to prior work
Jokar's 2022 paper introduces the notation for the smallest \(k\)-layered number, determines it for
\[
1\le k\le8,
\]
and states Conjecture 2.5 that its size grows exponentially with \(k\). The same paper explicitly notes that existence for every \(k\) remains open and proves the necessary condition
\[
\sigma(n)\ge kn.
\]

The earlier Mahanta--Saikia--Yaqubi paper develops structural results for \(k\)-layered numbers but does not state an asymptotic lower bound for the smallest \(k\)-layered number.

The current OEIS entry for the smallest \(k\)-layered number records the known values through \(k=8\) and cites Jokar's 2022 paper, but does not state a growth theorem.

Targeted searches using the source conjecture number, the phrases “smallest \(k\)-layered number,” “double exponential,” “Grönwall,” and “abundancy maximal order” did not locate a published implication of the form proved here. The argument is also not implied by the finite table: its content comes from combining the \(k\)-layered abundancy constraint with the maximal order of the divisor-sum function.

## Limitations
The theorem gives only a lower bound.

It does not prove that a \(k\)-layered number exists for every \(k\), does not give an upper bound of comparable size, and therefore does not determine the true growth order of \(L_k\).

The phrase “grows exponentially” in Conjecture 2.5 is informal. The present result should therefore be read as a rigorous strengthening of its lower-growth direction, not as a claim that the full intended asymptotic content of that conjecture has been settled.

Search non-detection is not a proof of novelty. A short unpublished observation combining the same two ingredients could exist.

## References
1. Farid Jokar, “On \(k\)-layered numbers,” arXiv:2207.09053v1, first posted 19 July 2022; MSC \(11A25\), \(11D99\), \(11Y99\).
2. Pankaj Jyoti Mahanta, Manjil P. Saikia, and Daniel Yaqubi, “Some properties of Zumkeller numbers and \(k\)-layered numbers,” arXiv:2008.11096v1; *Journal of Number Theory* 217 (2020), 218--236.
3. T. H. Grönwall, “Some asymptotic expressions in the theory of numbers,” *Transactions of the American Mathematical Society* 14 (1913), 113--122.
4. OEIS A355757, smallest \(n\)-layered number.
