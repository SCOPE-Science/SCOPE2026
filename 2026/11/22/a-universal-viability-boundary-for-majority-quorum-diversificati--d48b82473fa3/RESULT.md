# A universal viability boundary for majority-quorum diversification in mirrored environments

## Finding

Let \(n=2r+1\) be any odd integer with \(r\geq1\), and let \(0<\ell<h<1\). A cohort consists of \(k\) individuals with phenotype A and \(n-k\) with phenotype B. One of two environmental states occurs, each with probability \(1/2\). In the first state the respective survival probabilities are \((h,\ell)\); in the second they are \((\ell,h)\). Survival indicators are independent **conditional on the environmental state**. Define success as at least \(r+1\) surviving individuals, and let \(F_r(k;h,\ell)\) be its unconditional probability.

**Theorem (sharp majority-quorum allocation).** All optimal integer allocations \(0\leq k\leq 2r+1\) are exactly:

- \(k=0\) and \(k=2r+1\) when \(h+\ell<1\) (complete specialization);
- every \(k\) when \(h+\ell=1\), with \(F_r(k;h,\ell)=1/2\);
- \(k=r\) and \(k=r+1\) when \(h+\ell>1\) (as equal a mixture as parity permits).

The inequalities between distinct allocation classes are strict away from the boundary. The transition is **independent of cohort size** throughout the entire odd-size family. In particular, each phenotype has the same unconditional individual survival probability \((h+\ell)/2\); that marginal quantity, rather than an environmental-variance tuning parameter, determines whether diversification or specialization maximizes the probability of passing the specified quorum.

For \(0\leq k<r\) define
\[
P_{r,k}=\Pr\{\operatorname{Bin}(2r-k,h)+\operatorname{Bin}(k,\ell)=r\},\qquad
Q=\frac{h(1-h)}{\ell(1-\ell)}.
\]
The independent binomials in this expression are conditional Bernoulli counts with their stated probabilities. The exact allocation-increment identity is
\[
\boxed{F_r(k+1;h,\ell)-F_r(k;h,\ell)=\frac{h-\ell}{2}P_{r,k}\bigl(Q^{k-r}-1\bigr).}
\]
This gives both the strict ordering and its exact magnitude.

## Assumptions and scope

This is a finite-cohort **one-season majority-survival** model, motivated by establishment that requires more than half of a founding cohort to survive. Types have equal initial resource cost. Each seed or individual is preassigned to one of two phenotypes before the state is known; the realized environmental state is shared by the entire cohort. There is no selection of phenotype after observing that state, no density dependence, no interaction among survivor indicators conditional on state, no demographic replenishment, and no multi-generation optimization.

Equally likely states and exactly mirrored type-specific probabilities are essential hypotheses. The full theorem covers every odd cohort size at least three, every integer allocation and all real \(0<\ell<h<1\). No continuous relaxation of the integer choice is used. The result is not asserted for even cohort sizes, other survival quorums, unequal state probabilities, or imperfectly mirrored phenotypes.

## Proof

Fix \(r\geq1\). For independent Bernoulli sums, let \(T(k;a,b)\) denote the probability of at least \(r+1\) successes among \(k\) trials with probability \(a\) and \(2r+1-k\) trials with probability \(b\). By definition,
\[
F_r(k;h,\ell)=\frac{T(k;h,\ell)+T(k;\ell,h)}2.
\]
Interchanging the phenotype labels and the two equally likely environmental states proves \(F_r(k)=F_r(2r+1-k)\).

**Step 1: one-phenotype substitution.** Coupling a Bernoulli variable of probability \(b\) to one of probability \(a\) while holding the other \(2r\) indicators fixed, the event of achieving \(r+1\) survivors changes only if exactly \(r\) of those other indicators survive. Therefore
\[
F_r(k+1)-F_r(k)=\frac{h-\ell}{2}(A_{r,k}-P_{r,k}),
\]
where
\[
A_{r,k}=\Pr\{\operatorname{Bin}(k,h)+\operatorname{Bin}(2r-k,\ell)=r\}
\]
and \(P_{r,k}\) is defined above. All binomials on the right are independent within their sums.

**Step 2: exact central-mass reciprocity.** Consider any binary word of length \(2r\) with precisely \(r\) ones. Under the product measure defining \(A_{r,k}\), its first \(k\) positions have success probability \(h\), and its remaining positions probability \(\ell\). Complement every bit. Give the first \(k\) complemented positions probability \(\ell\) and the rest probability \(h\). This is a bijection between the \(r\)-success words contributing to \(A_{r,k}\) and those contributing to \(P_{r,k}\). If the original first block has \(a\) ones, the original word has likelihood
\[
h^a(1-h)^{k-a}\ell^{r-a}(1-\ell)^{r-k+a},
\]
whereas the complemented word under the swapped probabilities has likelihood
\[
(1-\ell)^a\ell^{k-a}(1-h)^{r-a}h^{r-k+a}.
\]
Their ratio is independent of \(a\), and equals
\[
\left(\frac{h(1-h)}{\ell(1-\ell)}\right)^{k-r}=Q^{k-r}.
\]
Summing over all such words gives \(A_{r,k}=Q^{k-r}P_{r,k}\), proving the boxed increment identity. Notice that \(P_{r,k}>0\).

**Step 3: signs and all global optima.** For \(k<r\), the exponent \(k-r\) is negative. Consequently the sign of \(Q^{k-r}-1\) is the sign of \(\ell(1-\ell)-h(1-h)\), which factors as \((h-\ell)(h+\ell-1)\). Since \(h-\ell>0\), every increment \(F_r(k+1)-F_r(k)\), \(0\leq k<r\), has the sign of \(h+\ell-1\). By the established reflection symmetry, this strict monotonicity on the first half determines the complete set of global maximizing integers, including both tied end or central choices as applicable.

At \(h+\ell=1\), the two environmental probability lists are exact complements; for an odd number of trials, a success in one state corresponds to failure of the strict majority event after bit-complementation. Thus the two conditional majority probabilities add to one and \(F_r(k)=1/2\) for every \(k\), confirming the tie and completing the proof.

## Verification

The independent, exact-rational implementation `verify.py` constructs each Poisson-binomial mass function by Bernoulli polynomial convolution. It checks reflection symmetry, central-mass reciprocity, the allocation-increment formula, and all optimality regimes for \(1\leq r\leq10\) and a dense rational grid \(\ell=i/10\), \(h=j/10\), \(1\leq i<j\leq9\), plus boundary and explicit examples. Executing `python3 verify.py` produced `11303 exact assertions passed`.

For \(n=5\), \(h=3/4\) and \(\ell=1/2\), the probabilities at \(k=0,1,2\) are, respectively,
\[
\frac{715}{1024},\quad\frac{23}{32},\quad\frac{187}{256},
\]
and are reflected at \(k=5,4,3\); hence balancing wins. Replacing \(\ell\) by \(1/8\) changes these exact values to
\[
\frac{14951}{32768},\quad\frac{6763}{16384},\quad\frac{2969}{8192},
\]
so specialization wins. At \((h,\ell)=(3/4,1/4)\) all allocations give \(1/2\).

These finite calculations verify the supplied implementation and examples; the word-bijection proof, not enumeration, covers all allowed cohort sizes and real parameters.

## Relationship to prior work

Biological bet-hedging and the evolutionary value of diversified phenotypes were discussed by Seger and Brockmann (1987), Simons (2011), and Svardal, Rueffler and Hermisson (2011). Their focal long-term or genetic selection criteria differ from the fixed-cohort, one-season **majority-survival event** optimized here. Haaland and colleagues (2018) distinguish short-term insurance from long-term bet-hedging, but analyze continuous phenotype distributions and arithmetic/geometric fitness, not this mirrored two-type finite-quorum classification.

The elementary relationship to Poisson-binomial sums and to majority-voting probability is acknowledged: swapping one Bernoulli variable invokes a pivotal \(r\)-success event. In related majority-panel research, varying panel size, pre-fixed patterns of expertise, or committee grouping are different optimization problems from choosing a phenotype composition in an equally likely **shared environment whose type competencies reverse**. The available indexed scientific summaries did not disclose a theorem which implies the present size-uniform trichotomy. This is a statement-level best-knowledge comparison, not a certification that all historical literature has been exhausted.

## Limitations

This is an idealized threshold-success model, not evidence that evolutionary diversification will be selected in wild populations or that any specific ecological restoration strategy should be implemented. It optimizes a single-season majority event, not mean survivors, survival probability for arbitrary quorums, expected fitness, or long-run geometric growth. Conditional independence and the exact state-switch symmetry are particularly restrictive. The literature search and selected primary-text inspection do not exclude an unlocated equivalent result in older probability or collective-decision theory; independent assessment of historical priority has not been performed.

## References

1. Seger, J. and Brockmann, H. J. (1987). *What is bet-hedging?* Oxford Surveys in Evolutionary Biology 4, 182–211. Author-hosted text: https://seger.biology.utah.edu/Seger_Brockmann_87.pdf
2. Simons, A. M. (2011). *Modes of response to environmental change and the elusive empirical evidence for bet hedging.* Proceedings of the Royal Society B 278, 1601–1609. First public online March 16, 2011. https://doi.org/10.1098/rspb.2011.0176 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC3081777/
3. Svardal, H., Rueffler, C. and Hermisson, J. (2011). *Comparing environmental and genetic variance as adaptive response to fluctuating selection.* Evolution 65, 2492–2513. https://doi.org/10.1111/j.1558-5646.2011.01318.x
4. Haaland, T. R., Wright, J., Tufto, J. and Ratikainen, I. I. (2019; online 2018). *Short-term insurance versus long-term bet-hedging strategies as adaptations to variable environments.* Evolution 73, 145–157. https://doi.org/10.1111/evo.13659
5. Ben-Yashar, R. and Danziger, L. (2014). *On the optimal composition of committees.* CESifo Working Paper 4685. https://www.ifo.de/en/cesifo/publications/2014/working-paper/optimal-composition-committees
