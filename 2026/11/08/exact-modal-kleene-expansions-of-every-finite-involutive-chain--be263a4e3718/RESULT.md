# Exact modal Kleene expansions of every finite involutive chain

## Finding
Let \(C_n=\{0,1,\ldots,n-1\}\) be the chain with meet \(\min\), join \(\max\), and Kleene involution \(\sim i=n-1-i\), for each integer \(n\geq2\). Let \(A_n\) be the number of unary maps \(\Box:C_n\to C_n\) satisfying the modal Kleene axioms (MK), (Pos), and (Con) of Celani–Menchón–Miguelez. Let \(N_n\) count the **normal** maps among them, namely those with \(\Box(n-1)=n-1\). For odd \(n\), let \(P_n\) count center-preserving maps with \(\Box((n-1)/2)=(n-1)/2\), and \(NP_n\) count maps satisfying both requirements.

For every \(h\geq1\), the complete enumeration is

\[
\begin{aligned}
 A_{2h}&=\binom{2h-1}{h}^{2}+\binom{2h}{h+1},\\
 N_{2h}&=\binom{2h-1}{h}\left(\binom{2h-2}{h-1}+1\right),\\
 A_{2h+1}&=\binom{2h}{h}^{2}+\binom{2h}{h+1},\\
 N_{2h+1}&=\binom{2h}{h}\binom{2h-1}{h-1}+\binom{2h-1}{h},\\
 P_{2h+1}&=\binom{2h}{h}^{2},\\
 NP_{2h+1}&=\binom{2h}{h}\binom{2h-1}{h-1}.
\end{aligned}
\]

Every isomorphism of the underlying ordered chains is the identity; hence these also enumerate isomorphism types of modal expansions on the specified underlying chains. Furthermore,

\[
\lim_{n\to\infty}\frac{N_n}{A_n}=\frac12,
\qquad \lim_{h\to\infty}\frac{P_{2h+1}}{A_{2h+1}}=1,
\]

and the exact proportion of non-center-preserving expansions on odd chains obeys

\[
\frac{A_{2h+1}-P_{2h+1}}{A_{2h+1}}
\sim\frac{\sqrt{\pi h}}{4^h}.
\]

This is a complete, rather than sampled, classification of all unary operations satisfying these particular axioms on all finite Kleene chains.

## Assumptions and scope
The unary operator \(f=\Box\) satisfies for all \(x,y,z\in C_n\):

\[
\begin{aligned}
\mathrm{(MK)}:\;&f(x\wedge y)=f(x)\wedge f(y),\\
\mathrm{(Pos)}:\;&\sim f(z\vee\sim z)\leq f(z\vee\sim z),\\
\mathrm{(Con)}:\;&f(x\vee(z\wedge\sim z))\leq f(x)\vee\sim f(x\vee(z\wedge\sim z)).
\end{aligned}
\]

No preservation of \(0\) or \(1\), no idempotence, and no additional implication axioms are assumed. Normality and, where defined, center preservation are counted separately, not silently imposed. The chain involution makes \(C_n\) a Kleene algebra: the greatest possible \(x\wedge\sim x\) is below the least possible \(y\vee\sim y\). For even \(n\), the chain has no involution-fixed center.

## Proof
**1. Reduction of (MK).** On a finite total order, preservation of binary meets is equivalent to monotonicity. Indeed, if \(x\leq y\), then \(f(x)=f(x\wedge y)=\min(f(x),f(y))\), so \(f(x)\leq f(y)\); conversely a monotone map preserves minima.

Set \(\ell=\lfloor(n-1)/2\rfloor\) and \(u=n-1-\ell\). The values of \(z\vee\sim z\) form the interval \(\{u,\ldots,n-1\}\), whereas those of \(z\wedge\sim z\) form \(\{0,\ldots,\ell\}\).

**2. Reduction of (Pos).** An element \(v\) is positive, meaning \(\sim v\leq v\), precisely when \(v\geq u\). Hence monotonicity reduces (Pos) to the single inequality \(f(u)\geq u\).

**3. Reduction of (Con).** Put \(t=x\vee(z\wedge\sim z)\). Since \(t\geq x\), monotonicity yields \(f(t)\geq f(x)\). The (Con) inequality becomes

\[f(t)\leq\max\{f(x),n-1-f(t)\}.\]

It is automatic if \(f(t)\leq\ell\). If \(f(t)>\ell\), then \(n-1-f(t)<f(t)\), and the inequality forces \(f(t)=f(x)\). In particular, whenever \(0\leq x\leq t\leq\ell\), the conclusion applies by taking \(z=t\); and these are the only potentially nontrivial pairs, because if \(x>\ell\), then \(t=x\).

It follows that (Con) holds **if and only if** either \(f(\ell)\leq\ell\) or \(f\) is constant on \(\{0,\ldots,\ell\}\). For necessity, if \(f(\ell)>\ell\), choose \(x=0\), \(t=\ell\) to get \(f(0)=f(\ell)\), then use monotonicity. For sufficiency, below threshold all applicable values are nonpositive, while above threshold the lower segment is constant, ensuring the required equality.

**4. Disjoint normal forms.** Combining the two reductions gives precisely two cases:

* **Split case:** \(f(\ell)\leq\ell\) and \(f(u)\geq u\). If \(n=2h\), choose an arbitrary nondecreasing lower half with values in \(\{0,\ldots,h-1\}\), independently of an arbitrary nondecreasing upper half with values in \(\{h,\ldots,2h-1\}\). If \(n=2h+1\), the middle value must be \(f(h)=h\); choose the \(h\) lower and the \(h\) upper values independently, within the respective \((h+1)\)-point ranges.
* **Upper-constant case:** \(f(0)=\cdots=f(\ell)=j\), with \(j\geq h\) when \(n=2h\), and \(j>h\) when \(n=2h+1\). The remaining \(h\) values are any nondecreasing sequence from \(j\) through \(n-1\). These cases are disjoint.

A nondecreasing sequence of length \(r\) using \(s\) possible values has \(\binom{r+s-1}{r}\) choices. Thus the split contributions are \(\binom{2h-1}{h}^{2}\) and \(\binom{2h}{h}^{2}\), respectively. In the upper-constant case, letting \(s\) be the number of available upper values gives exactly

\[\sum_{s=1}^{h}\binom{h+s-1}{h}=\binom{2h}{h+1}\]

in either parity, by the hockey-stick identity. These prove both formulas for \(A_n\).

**5. Normality and centers.** Requiring the final value to equal the top reduces a length-\(h\) upper segment to a length-\((h-1)\) segment with its last entry specified. In the split case this gives the respective factors \(\binom{2h-2}{h-1}\) and \(\binom{2h-1}{h-1}\). In the upper-constant case the count becomes

\[\sum_{s=1}^{h}\binom{h+s-2}{h-1}=\binom{2h-1}{h},\]

which proves both formulas for \(N_n\). When \(n=2h+1\), the involution-fixed center is \(h\), and \(f(h)=h\) holds exactly in the split case. This gives \(P_{2h+1}\) and \(NP_{2h+1}\).

**6. Limits.** Write \(b_h=\binom{2h}{h}\). The upper-constant contribution is \(\frac{h}{h+1}b_h\); the split contribution is \(b_h^2/4\) for even chains and \(b_h^2\) for odd chains. Since \(b_h\sim4^h/\sqrt{\pi h}\), the upper-constant fraction is exponentially small. In the split case, the normality fractions are respectively \(h/(2h-1)\) and exactly \(1/2\), so the full normality fraction tends to \(1/2\). In odd chains, the non-center-preserving fraction equals

\[
\frac{\tfrac{h}{h+1}b_h}{b_h^2+\tfrac{h}{h+1}b_h}
=\frac{h}{(h+1)b_h+h}
\sim\frac{\sqrt{\pi h}}{4^h}.
\]

All assertions follow.

## Verification
The standalone Python 3 script `check_modal_kleene_chains.py` enumerates all nondecreasing unary tables on each chain for \(2\leq n\leq9\), directly tests (MK), (Pos), (Con) for every table, and checks equivalence to the derived two-case criterion. It then compares the exact totals, normal totals, center-preserving totals where applicable, and both cases with the stated closed formulas. All tests passed. No external packages or hidden inputs are used; run `python3 check_modal_kleene_chains.py`. The infinite-family classification and asymptotics are proven above, not inferred from these finite checks.

| \(n\) | All \(A_n\) | Normal \(N_n\) | Center-preserving (if odd) |
|---:|---:|---:|---:|
| 2 | 2 | 2 | — |
| 3 | 5 | 3 | 4 |
| 4 | 13 | 9 | — |
| 5 | 40 | 21 | 36 |
| 6 | 115 | 70 | — |
| 7 | 415 | 210 | 400 |
| 8 | 1281 | 735 | — |
| 9 | 4956 | 2485 | 4900 |

## Relationship to prior work
Celani, Menchón, and Miguelez introduced the (MK), (Pos), and (Con) modal Kleene algebra equations and characterized their twist-product, centered, normal, and dual representations (arXiv:2608.10937, August 11, 2026; particularly Definition 3.5 and Propositions 3.19–3.23). Those foundational results supply the exact algebraic class being counted. The result here directly classifies *all* operators on the elementary finite involutive chains and supplies binomial size formulas and limiting proportions. Neither the inspected sections of that source nor the indexed results examined supplied these exact counts.

The existing finite-chain results on Heyting preconditionals, Gödel monadic expansions, and birelational intuitionistic frames involve different signatures and different compatibility axioms. They cannot imply these counts without an additional equivalence, and no such equivalence was identified. A programming-semiring literature also uses the phrase “modal Kleene algebra” for a different signature involving Kleene star; it must not be conflated with the present De Morgan/Kleene-lattice variety.

## Limitations
The carrier is required to be a finite linearly ordered Kleene lattice with the unique order-reversing involution. The theorem does not enumerate operators on other finite Kleene algebras or impose modal identities beyond those explicitly stated. Although the proof is self-contained and computations are reproducible, novelty is only assessed against the inspected literature and accessible indexed records; an unindexed equivalent enumeration remains possible. No independent mathematical or historical-priority audit has been performed.

## References
1. S. Celani, P. Menchón, and V. Miguelez, *A Modal Expansion of Kleene Algebras via Twist Structures*, arXiv:2608.10937 (first posted August 11, 2026), https://arxiv.org/abs/2608.10937 ; especially Definition 3.5, Proposition 3.19, and Definition 3.20.
2. G. Struth and collaborators, work on *modal Kleene algebras* in program semantics (different semiring/Kleene-star signature); e.g. J. Desharnais, B. Möller, G. Struth, *Termination in modal Kleene algebra*, used only as a terminological non-equivalence check.
