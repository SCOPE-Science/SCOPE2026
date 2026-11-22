# Sharp sum-of-run-exponents bound for binary words with three marked letters

## Finding
For every integer \(n\ge13\), let \(\mathcal W_{n,3}\) be the set of binary words of length \(n\) containing exactly three symbols \(1\). For each run \((s,e,p)\) of a word \(w\), with zero-based half-open interval \([s,e)\), write its exponent as \((e-s)/p\). The run must have least period \(p\), length at least \(2p\), and be maximal under extension with that period. Define \(\operatorname{Exp}(w)\) as the sum of the exponents of **all** runs, including unary (period-one) runs.

Put \(m=\lfloor(n-1)/4\rfloor\). Then the exact fixed-composition extremum is
\[
\boxed{\max_{w\in\mathcal W_{n,3}}\operatorname{Exp}(w)=n+3-\frac1m-\frac2{m+1}.}
\]
One maximizing word is
\[
w_{n}=0^{m-1}1\,0^{m-1}1\,0^m1\,0^{n-3m-1}.
\]
Consequently the best possible sum of exponents within this sparse class is \(n+3-O(1/n)\), with exact four-step corrections in \(n\). The onset \(n=13\) cannot be changed to \(n=12\): at length twelve the maximum is \(167/12\), whereas the displayed expression would give \(83/6\).

## Assumptions and scope
All words are finite, linear, binary, and position-indexed starting at zero. Every run is an occurrence interval with least period, not a factor spelling or a maximal constant-letter block alone. A period \(p\) of \(w[s:e]\) means \(w[i]=w[i+p]\) for all \(s\le i<e-p\). A run is a maximal such interval satisfying \(e-s\ge2p\) and no shorter positive period. Its exponent is precisely \((e-s)/p\). There are exactly three ones and no constraint on how many zeros precede, separate, or follow them. All quantifiers are over integer \(n\ge13\); no assertion is made for the shorter range.

## Proof
Write the positions of the three ones as \(x<y<z\) and set \(p=y-x\), \(q=z-y\). The total exponent of all period-one zero runs is at most the number of zeros, \(n-3\); equality holds exactly when every nonempty zero block has length at least two. Period-one one runs contribute at most three in total, and are absent when \(p,q\ge2\).

**Only adjacent-gap nonunary periods occur.** Consider a run of least period \(h\ge2\). Its first \(2h\) symbols consist of two identical blocks, each necessarily containing one \(1\), since the entire word contains only three. Consequently two of its ones occur exactly \(h\) apart. If its interval contains a third one, periodicity forces that third one onto the same arithmetic progression (the three ones in the interval have consecutive spacing \(h\)). A run cannot contain the first and third ambient ones without also containing the middle one. Thus every nonunary run has period \(p\) or \(q\). For any fixed least period, the maximal run containing the corresponding two ones is unique. If \(p=q\), the two constructions merge into one run of exponent at most \(4-1/p\), and its total with all zero runs is strictly less than \(n+1\). If \(p=q=1\), the sole one-block is a period-one run of exponent three and there is no nonunary run.

If precisely one of \(p,q\) equals one, the adjacent pair forms a period-one run of exponent two. The only possible nonunary period is the other gap, whose maximal interval contains exactly two ones and has exponent strictly less than three; hence the full exponent sum is less than \(n+2\). These cases and \(p=q\) cannot maximize because, for \(m\ge3\), the claimed maximum is greater than \(n+2\).

It remains to consider distinct gaps \(p,q\ge2\). Reversal does not change run exponents, so assume \(p<q\). Any period-\(p\) run uses \(x,y\) but cannot include \(z\), and is confined to an interval starting at least \(\max\{0,x-p+1\}\) and ending no later than \(x+2p\). Thus, if it exists, its exponent \(E_p\) satisfies
\[
E_p\le3-\frac1p-\frac{(p-1-x)_+}{p}.
\]
Likewise a period-\(q\) run contains \(y,z\) but excludes \(x\), so it starts at least at \(x+1\), ends no later than \(\min\{n,x+p+2q\}\), and has exponent \(E_q\) satisfying
\[
E_q\le2+\frac{p-1}{q}-\frac{(x+p+2q-n)_+}{q}.
\]
An absent run contributes zero and also satisfies the corresponding upper inequality, since each right-hand upper bound is positive. Since \(p<q\), the two nonnegative boundary deficits obey
\[
(p-1-x)_++(x+p+2q-n)_+\ge (2p+2q-1-n)_+.
\]
Weighting each deficit by at least \(1/q\) gives the two simultaneous bounds
\[
E_p+E_q\le\min\!\left\{5-\frac1p+\frac{p-1}{q},\;3-\frac1p+\frac{n-p}{q}\right\}.\tag{1}
\]
If \(p\le m\), use \(q\ge p+1\) in the first bound to obtain
\[
E_p+E_q\le6-\frac1p-\frac2{p+1}\le6-\frac1m-\frac2{m+1}.
\]
If \(p\ge m+1\), the second bound gives
\[
E_p+E_q\le g(p):=2-\frac1p+\frac{n+1}{p+1}.
\]
For positive integral \(p\) in this range, \(g(p+1)<g(p)\), because
\[
g(p)-g(p+1)=\frac{n+1}{(p+1)(p+2)}-\frac1{p(p+1)}>0.
\]
Using \(n\le4m+4\) and \(m\ge3\), we have
\[
g(p)\le g(m+1)\le6-\frac1{m+1}-\frac3{m+2}\le6-\frac1m-\frac2{m+1}.
\]
The last inequality is equivalent to \(m^2-2m-2\ge0\), true for all integers \(m\ge3\). Adding at most \(n-3\) from the zero runs gives the universal required upper bound.

**Attainment.** For \(m=\lfloor(n-1)/4\rfloor\), the construction in the finding has three ones at \(m-1,2m-1,3m\), hence gaps \(p=m\), \(q=m+1\), with all four zero blocks of length at least two (because \(m\ge3\) and \(n\ge4m+1\)). Its four zero-block runs contribute exactly \(n-3\). Its first nonunary run is \([0,3m-1)\) with period \(m\) and exponent \(3-1/m\). Its second nonunary run is \([m,4m+1)\) with period \(m+1\) and exponent \(3-2/(m+1)\). The classification above excludes any other nonunary run. Their exponents sum to the upper bound \(n+3-1/m-2/(m+1)\), completing the proof.

## Verification
The standalone Python 3 source `verify.py` independently reconstructs runs by scanning periodicity equalities at every candidate period, determines their least periods, and sums exact rational exponents. A second exhaustive method scans all substring intervals and checks maximality directly. These implementations agreed on all \(715\) three-one words of lengths three through twelve. Full enumeration of all \(31,465\) weight-three words from lengths three through thirty confirms both the claimed maximum and an explicit maximizing word for each of the eighteen lengths thirteen through thirty. Actual command: `python3 verify.py`; captured output is in `verification_output.txt`. The infinite theorem rests on the preceding proof, not on the finite verification.

## Relationship to prior work
Czarkowski's 2026 paper *Improved Bounds on the Sum of Exponents of Runs in a String* (CPM 2026, DOI 10.4230/LIPIcs.CPM.2026.23, first publicly dated 2026-06-08) defines the same exponent statistic and proves universal upper bounds, including \(2.2n\) in the binary case, **without fixing Hamming weight**. This generic bound does not imply the exact fixed-three-one formula or the maximizing family. The published *Exact run spectrum of binary words with three marked ones* (2026-11-08; link below) classifies how many runs a three-one word has and gives its run-count generating function. Counting runs does not determine the sum of their rational exponents; it neither states nor entails this extremum. The classical Runs Theorem of Bannai and collaborators establishes a universal cardinality bound, not a fixed-weight exponent maximum. The argument here independently derives the required structural classification and optimizes weighted lengths.

## Limitations
Only linear binary words of exactly three ones and lengths \(n\ge13\) are covered. The extremum for other Hamming weights, the cyclic setting, and the complete distribution of exponent sums are not determined. No complete classification or count of all maximizing words is claimed. An unindexed equivalent closed-form specialization in earlier research is a residual priority risk. Independent mathematical validation has not been performed; finite experiments supplement rather than replace the displayed proof.

## References
1. Arkadiusz Czarkowski, *Improved Bounds on the Sum of Exponents of Runs in a String*, CPM 2026, DOI 10.4230/LIPIcs.CPM.2026.23, first public date 2026-06-08. https://doi.org/10.4230/LIPIcs.CPM.2026.23
2. *Exact run spectrum of binary words with three marked ones*, public mathematical research record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-run-spectrum-of-binary-words-with-three-marked-ones--195f68bb7ba1
3. H. Bannai et al., *The “Runs” Theorem*, SIAM Journal on Computing 46 (2017), DOI 10.1137/15M1011032. https://doi.org/10.1137/15M1011032
