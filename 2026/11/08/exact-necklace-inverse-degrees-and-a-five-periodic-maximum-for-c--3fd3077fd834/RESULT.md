# Exact necklace inverse degrees and a five-periodic maximum for cyclic Rule 12

## Finding
For each integer \(n\ge1\), apply elementary cellular automaton Rule 12 to indexed binary rings of length \(n\): \((F_nx)_i=x_i(1-x_{i-1})\), with indices modulo \(n\). For an output necklace \([y]\), let \(\delta_n([y])\) be the number of input necklaces mapped into it. If \(y\) is identically zero, \(\delta_n([y])=2\). Otherwise list the positions of its \(k\ge1\) ones in cyclic order and their successive positive circular gaps \(d_1,\ldots,d_k\), summing to \(n\). If any \(d_i=1\), its degree is zero. Otherwise let \(\ell\mid k\) be the least period of the gap list, \(h=k/\ell\), and \(A=\prod_{i=1}^{\ell}(d_i-1)\). Then
\[
\delta_n([y])=\frac1h\sum_{j=0}^{h-1} A^{\gcd(h,j)}.
\]
In particular, the maximum \(M(n)=\max_{[y]}\delta_n([y])\) is given, for \(1\le n\le20\), by the complete ordered list
\[
2,2,2,3,4,5,6,8,12,15,20,24,36,48,60,80,108,144,192,240,
\]
and, for all \(n\ge21\), writing \(n=5k+r\) with \(0\le r<5\), by
\[
M(5k+r)=\begin{cases}
243\cdot4^{k-4},&r=0,\\
81\cdot4^{k-3},&r=1,\\
27\cdot4^{k-2},&r=2,\\
9\cdot4^{k-1},&r=3,\\
3\cdot4^k,&r=4.
\end{cases}
\]
Every maximum is attained by an explicit output: use cyclic one-gaps \((4,4,4,4,4,5,\ldots,5)\) when \(5\mid n\) and \(n\ge25\), and the \(0\)–\(4\) copies of gap \(4\), respectively, needed to make the remaining gaps \(5\) when \(n\ge21\) is not divisible by \(5\). These nonconstant gap words can be arranged to be primitive. For \(n\le20\), the exhaustive partition verifier supplies maximizers.

## Assumptions and scope
Necklaces identify cyclic rotations only (not reversal or complementation), inputs and outputs are length-\(n\) binary rings, and a predecessor is counted once per rotation orbit. The local rule ignores the right neighbor and emits a one exactly at a cyclic \(01\) transition. Periods of a nonempty gap list are measured in numbers of ones, not in bit positions. For a one-element gap list, \(\ell=h=1\). All formulas concern one synchronous update, not iterated dynamics.

## Proof
**All labeled fibers.** A nonzero output must mark precisely the \(01\) transitions of the input; consequently two marked positions cannot be adjacent. Between consecutive marked positions at distance \(d\ge2\), the input starts with one, ends in zero just before the next mark, and must contain exactly one \(10\) transition. There are exactly \(d-1\) placements of this transition. Disjoint gaps are independent, yielding \(\prod_i(d_i-1)\) labeled predecessors, and every binary output with isolated ones is feasible. An output without ones comes only from the two constant inputs.

**Rotation quotient.** Write the cyclic gap list as \(h\) repetitions of a primitive list of \(\ell\) gaps. An input predecessor specifies one transition placement in each gap, with \(A\) choices per primitive block. The stabilizer of the output is the cyclic group of order \(h\), rotating these \(h\) choice blocks. The predecessor necklaces above \([y]\) are precisely its orbits: rotations taking a predecessor to another predecessor of the *same indexed* output are exactly the output's stabilizer. Burnside's lemma gives the displayed sum. If gap lengths are not all equal, placing equal gaps in consecutive groups produces a primitive cyclic list (a nonconstant cyclic list with only two transitions between gap types cannot be a proper power). Thus the complete product of all gaps is achievable as a necklace inverse degree for every nonuniform multiset of gaps. A uniform list with gap \(d\), repeated \(k\) times, has degree \(\frac1k\sum_{j=0}^{k-1}(d-1)^{\gcd(k,j)}\).

**Optimization.** The labeled product problem is to maximize \(\prod(d_i-1)\) over integers \(d_i\ge2\) summing to \(n\). Replacing a gap \(d\ge8\) by gaps \(5\) and \(d-5\) strictly increases the product. The local comparisons \((3,3)\to(6)\), \((3,5)\to(4,4)\), \((3,6)\to(4,5)\), \((4,6)\to(5,5)\), \((6,6)\to(4,4,4)\), and \((6,5,5)\to(4,4,4,4)\) all increase product; a gap of \(2\) is dominated except alone, and a gap \(7\) paired with another gap is similarly dominated after checking the finitely many allowed \(3\)–\(7\) partners. Thus for \(n\ge12\) all unconstrained optimizers use gaps \(4,5\), with five copies of \(4\) replaceable by four copies of \(5\), strictly increasing product. This gives the usual five-residue optimum, but if all optimal gaps coincide, the necklace quotient may reduce the degree.

For \(n=5k\), the all-\(5\) product is \(4^k\) but its output has a nontrivial stabilizer for \(k>1\). For a nonuniform multiset, normalize its product by \(4^{n/5}\). The factors for gap sizes \(d\) are \(\rho_d=(d-1)/4^{d/5}\). They are strictly below one, and \(\rho_4^5=243/256\). Any gap \(d\notin\{4,5\}\) has factor at most \(\rho_6<243/256\), since \((d-1)/4^{d/5}\) decreases for \(d\ge6\), and direct comparison handles \(d=2,3\). Hence if \(k\ge5\), the greatest nonuniform product is obtained by exactly five gaps of size \(4\), the remaining gaps size \(5\), giving \(243\cdot4^{k-4}\); any additional five size-\(4\) gaps multiply by a factor \(243/256<1\). For \(2\le k\le4\), five size-\(4\) gaps either do not fit or, at \(n=20\), give a uniform output and therefore are not eligible as a *nonuniform* competitor. Any nonuniform multiset of total cost \(5k\) must contain a gap outside \(\{4,5\}\). The best product defect is a size-\(4\) gap paired with size \(6\), producing ratio \(\rho_4\rho_6=15/16\). Indeed \(\rho_2,\rho_3,\rho_7\) and all \(\rho_d\) with \(d\ge8\) are less than \(15/16\), and the remaining size-\(6\) defect requires at least one balancing non-\(5\) gap modulo five. With at most four units of five in the cost budget, only a size-\(4\) balancing defect can attain this ratio; other choices have strictly smaller combined ratios. For \(n\ge21\) not divisible by five, the unconstrained optimal mix of size-\(4\) and size-\(5\) gaps is nonuniform and therefore achievable without a stabilizer.

For a uniform list of \(k\ge2\) gaps of size \(d\ge3\), the necklace count is at most \(\tfrac34(d-1)^k\). Gap size \(2\) gives degree one and can be set aside. This follows immediately for \(k=2\), and for \(k\ge3\) by bounding each nonidentity rotation's fixed words by \((d-1)^{\lfloor k/2\rfloor}\) and summing the Burnside average. These uniform degrees are below the available nonuniform bounds \(\frac{15}{16}\) or \(\frac{243}{256}\) times the unconstrained product, so cannot win at \(n\ge21\). The residual cases through \(n=20\), including single-gap outputs, are exhausted by the integer-partition computation in `verify.py`. This proves the full formula.

## Verification
Run `python3 verify.py` from the same directory. The checker independently constructs all necklaces and predecessor orbit sets for lengths \(1\) through \(14\), comparing every nonempty fiber with the Burnside formula; it also enumerates every nondecreasing partition into gaps at lengths \(1\) through \(25\) and compares the optimized degrees with the closed formulas. The actual replay produced `VERIFY_OK cyclic_necklaces= 209 brute_lengths=1..14 partition_lengths=1..25`. Finite checks are not substituted for the all-length argument.

## Relationship to prior work
Jen's 1989 work gives a general preimage calculus and explicitly treats Rule 12's product-type preimage counts for *finite linear blocks*; that precursor is not claimed as new. Fukś's 2003 analysis addresses iterated preimage sequences of short blocks; a 2013 arXiv posting provides a verifiable public timestamp for this line of work. The present contribution concerns the cyclic rotation quotient, exactly accounts for periodic output stabilizers, and resolves its all-length maximum with a five-residue law and symmetry-induced exceptions. Closely related necklace predecessor studies for Rules 90 and 150 use different (linear over \(\mathbb F_2\)) local maps and are not statements about Rule 12.

## Limitations
This is one-step, binary, cyclic Rule 12 only; it does not classify temporal basins or higher-step fibers. The novelty comparison does not establish priority over all potentially unindexed earlier derivations of this particular necklace quotient. The 1989 and 2003 sources have year-verified publication dates but are not used as day-verified dates; the dated 2013 arXiv posting anchors the archival cohort. No independent mathematical audit has been performed.

## References
- Erica Jen, “Enumeration of Preimages in Cellular Automata,” *Complex Systems* 3 (1989), 421–456. https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf
- Henryk Fukś, “Sequences of Preimages in Elementary Cellular Automata,” *Complex Systems* 14 (2003), 29–43. https://wpmedia.wolfram.com/uploads/sites/13/2018/02/14-1-2.pdf
- Henryk Fukś, “Sequences of preimages in elementary cellular automata,” arXiv:1305.6533, initial public submission 2013-05-28. https://arxiv.org/abs/1305.6533
- Stephen Wolfram, “Statistical mechanics of cellular automata,” *Reviews of Modern Physics* 55 (1983), 601–644. https://doi.org/10.1103/RevModPhys.55.601
