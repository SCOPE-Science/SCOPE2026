# Exact four-factor reconstruction profiles of height-two Dyck words

## Finding

Let \(\mathcal H_n\) be the binary Dyck words of semilength \(n\ge1\) with nesting height at most two. Encode an up-step by `1` and a down-step by `0`. Observe, for every binary string of length one, two, three, or four, its number of overlapping contiguous occurrences. Write \(R_n\) for the number of distinct resulting vectors on \(\mathcal H_n\). Then

\[
\boxed{\sum_{n\ge1}R_nz^n=\frac{z(1+z^2+z^3-z^4+3z^5-z^6+2z^7-2z^8)}{(1-z)^2(1-z^3)(1-z^4)}}.
\]

In particular \(R_n=n^3/18+O(n^2)\); the coefficients form a degree-three quasipolynomial with least period twelve. The initial values for \(n=1,\ldots,17\) are

\[
1,2,4,8,12,20,30,43,58,78,101,129,160,197,239,287,339.
\]

More precisely, there is an exact feasibility classification of the complete observations: for a path with at least one non-unit primitive component, its observation is uniquely represented by the tuple \((n,b,c,d,f,g)\) described below, and the inequalities below characterize all tuples that occur. The single all-unit path provides one further observation at each semilength. Consequently \(R_n\) is also the maximum size of a zero-error code whose receiver sees only these four-factor multiplicities.

## Assumptions and scope

A Dyck word has equally many `1` and `0` symbols and every prefix has at least as many `1` symbols as `0` symbols. Nesting height is the largest prefix excess. Height at most two forces a unique factorization into *primitive components*

\[
B_p=1(10)^{p-1}0,\qquad p\ge1,
\]

with positive integer semilengths \(p_1,\ldots,p_t\) summing to \(n\). This is an ordinary composition of \(n\). A unit component has \(p_i=1\), a short long component has \(p_i=2\), and an extended long component has \(p_i\ge3\). Define

\[
 b=\#\{i:p_i=2\},\quad c=\#\{i:p_i\ge3\},\quad L=b+c,
\]
\[
 d=\#\{i<t:p_i\ge2,\ p_{i+1}\ge2\},\quad
 f=\mathbf1_{\{p_1=1\}},\quad g=\mathbf1_{\{p_t=1\}}.
\]

These parameters are relevant when \(L\ge1\). Put \(k=L-d\), the number of runs of long components, and \(a_0=k-1+f+g\), the minimum number of unit components compatible with the long-component runs and the two endpoints. All tuples have integers \(b,c,d,n\), binary \(f,g\), and satisfy \(b,c\ge0\), \(L=b+c\ge1\), \(0\le d<L\). Their **necessary and sufficient** remaining constraints are:

- If \(c\ge1\): \(n\ge2b+3c+a_0\).
- If \(c=0\), \(k=1\) and \(f=g=0\): \(n=2b\).
- In every other case with \(c=0\): \(n\ge2b+a_0\).

For \(L=0\), the unique word is \((10)^n\). Observations are linear, overlapping, oriented, and include the multiplicities at every length up to four; they are neither cyclic nor unordered Parikh/composition observations.

## Proof

**1. Local factor identity.** Every length-four factor is either internal to one component, crosses one boundary, or crosses two boundaries with a unit component in the middle. Separating those three cases yields, for \(L\ge1\), the following complete table; all unlisted four-letter factors have multiplicity zero:

| Factor | Multiplicity |
|---|---|
| `1100` | \(b\) |
| `1101` | \(c\) |
| `0100` | \(c\) |
| `1010` | \(n-3L+1-f-g+d\) |
| `0101` | \(n-2b-3c-f-g\) |
| `1011` | \(L-1+f-d\) |
| `0010` | \(L-1+g-d\) |
| `0011` | \(d\) |
| `1001` | \(L-1+g\) |
| `0110` | \(L-1+f\) |

To verify the non-obvious entries, a component of size two contributes the internal factor `1100`; each component of size at least three contributes one each of `1101` and `0100`, as well as \(p-2\) copies of `1010` and \(p-3\) copies of `0101`. A boundary contributes `1011`, `0010`, `0011`, or `1010` according as its left/right types are unit/long, long/unit, long/long, or unit/unit; it also contributes `1001` if its left component is long and `0110` if its right component is long. A unit component with neighbors on both sides contributes a further `0101` crossing two boundaries. Writing \(a\) for the unit-component count and using \(a-\#\{\text{unit runs}\}=\#\{\text{unit-unit boundaries}\}\), with \(\#\{\text{unit runs}\}=k-1+f+g\), cancels \(a\) from the table. Every factor not listed is excluded by the height-two block grammar.

**2. Reconstruction of the tuple.** From the table, a four-factor vector gives \(b=N_{1100}\), \(c=N_{1101}\), \(d=N_{0011}\), \(g=N_{1001}-L+1\), and \(f=N_{0110}-L+1\). Thus distinct feasible tuples yield distinct complete observations. The all-unit word contains neither `1100` nor `1101` and is distinguished from every word with a long component. Conversely the displayed table determines all length-four multiplicities from the tuple. For paths of semilength at least two, the first three bits are `101` when \(f=1\) and `110` when \(f=0\), while the last three are `010` when \(g=1\) and `100` when \(g=0\); the all-unit case is immediate. Standard prefix/suffix incidence equations determine each three-factor multiplicity from the four-factor multiplicities and the first/last three symbols, then each two-factor and one-factor multiplicity. Hence equality of the tuples is exactly four-Abelian equivalence on \(\mathcal H_n\), including the small cases \(n=1,2\) by direct inspection.

**3. Feasibility and witnesses.** The \(L\) long components form \(k=L-d\ge1\) consecutive long runs. Exactly \(k-1\) unit components must separate these runs, and \(f\) or \(g\) imposes a unit component at the corresponding endpoint. Hence at least \(a_0=k-1+f+g\) unit components are needed. If \(k=1\) and \(f=g=0\), every component is long, so there can be no unit component. Otherwise any number of additional unit components can be inserted into an existing interior unit group (when \(k\ge2\)) or an endpoint unit group (when \(f+g\ge1\)), preserving \(b,c,d,f,g\). Each of the \(b\) size-two components consumes two units of semilength and each of the \(c\) extended components consumes at least three. If \(c\ge1\), all surplus semilength can be placed in one extended component. If \(c=0\), only added unit components can absorb surplus, except the forced-all-long case. These observations prove the three stated constraints and give explicit witnesses: begin with \(k\) long runs, allocate \(L\) long components among them, label any \(c\) long components as extended, put one unit component in each required separating and endpoint gap, then add surplus as prescribed.

**4. Enumeration.** Count tuples with \(b+c=L\ge1\), \(1\le k\le L\), and \(f,g\in\{0,1\}\). For \(c\ge1\), every admissible tuple contributes the tail \(z^{2b+3c+k-1+f+g}/(1-z)\). For \(c=0\), the exceptional case \((k,f,g)=(1,0,0)\) contributes only \(z^{2L}\); all other cases contribute \(z^{2L+k-1+f+g}/(1-z)\). The all-unit path contributes \(z/(1-z)\). Geometric summation gives

\[
\begin{aligned}
F(z)&=\frac z{1-z}+\frac{z^2}{1-z^2}
+\frac{z^2(2z+z^2)}{(1-z^2)(1-z)}\\
&\quad+\frac{(1+z)^2}{(1-z)^2}\left(\frac{z^5}{1-z^2}-\frac{z^6}{1-z^3}+\frac{z^3}{(1-z^2)(1-z^3)}-\frac{z^4}{(1-z^3)(1-z^4)}\right),
\end{aligned}
\]

which simplifies to the boxed generating function. Its denominator has poles of orders four at \(z=1\), and simple non-cancelled poles at primitive third and fourth roots of unity, respectively. This proves the least quasipolynomial period twelve and the \(n^3/18\) leading term.

**5. Optimality of the observation code.** Two codewords may coexist exactly when their observation vectors differ. Selecting one constructed witness for every feasible tuple (and the all-unit path) achieves \(R_n\) codewords; pigeonhole gives the matching upper bound.

## Verification

The standalone `verify_exhaustive.py` enumerates every composition at each semilength \(1\le n\le17\), independently computes all overlapping factors of lengths at most four, and checks both directions of the tuple equivalence and the exact feasibility conditions. The standalone `verify_transfer.py` compares tuple enumerations with an independent truncated power-series product through semilength 55 and independently checks the full ten-row four-factor table on 500 seeded random height-two words up to semilength 250. The programs are standard-library-only and may be run with `python3 verify_exhaustive.py` and `python3 verify_transfer.py`; their successful completion prints `EXHAUSTIVE_OK` and `TRANSFER_AND_OCCURRENCE_OK`. These finite computations corroborate, but do not replace, the all-length argument above.

As an explicit first collision, the distinct primitive-component sequences \((1,1,2,1)\) and \((1,2,1,1)\) give the same complete observation at semilength five. The count \(R_5=12\) is smaller than the \(16\) admissible height-two words, whereas all words are distinguished through semilength four.

## Relationship to prior work

The notion of four-Abelian equivalence and a polynomial-growth theorem for general finite words follow Karhumäki, Saarela and Zamboni (2013), but those results do not determine the exact set of realizable joint profiles within height-two Dyck words. Sapounakis, Tasoulas and Tsikouras (2009), and Manes, Sapounakis, Tasoulas and Tsikouras (2011), study counts of occurrences of individual fixed patterns and related bijections across Dyck paths; their univariate pattern-count results do not give the simultaneous four-factor image or its capacity. Prior three-Abelian classifications for unrestricted Dyck paths concern a coarser observation; even at semilength four, the height-two component sequences \((1,1,2)\) and \((1,3)\) agree on all factors through length three but differ at length four. Previously published circular four-gram results under the forbidden-adjacency constraint `11` concern a different source language and cyclic observations; the present paths can contain `11` and `00`.

## Limitations

The classification concerns only Dyck words of height at most two, binary oriented overlapping factor multiplicities of all lengths one through four, and error-free observations. It does not give every equivalence-class fiber size, reconstruction from unordered factor compositions, a result for unrestricted-height Dyck words, or any noisy-channel capacity. Literature searches and inspected primary works did not establish an earlier equivalent joint-profile count, but lack of an indexed result does not prove absolute novelty; historical priority remains open to further expert comparison.

## References

1. A. Sapounakis, I. Tasoulas, P. Tsikouras, *Enumeration of strings in Dyck paths: A bijective approach*, Discrete Mathematics 309 (2009), 3032–3039, DOI: https://doi.org/10.1016/j.disc.2008.08.005 (available online 2008-09-24).
2. K. Manes, A. Sapounakis, I. Tasoulas, P. Tsikouras, *General Results on the Enumeration of Strings in Dyck Paths*, Electronic Journal of Combinatorics 18 (2011), P74, DOI: https://doi.org/10.37236/561.
3. J. Karhumäki, A. Saarela, L. Q. Zamboni, *On a generalization of Abelian equivalence and complexity of infinite words*, arXiv:1301.5104v1 (2013-01-22), https://arxiv.org/abs/1301.5104.
