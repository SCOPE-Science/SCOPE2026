# A joint Poisson(2) component law for parity-conditioned random circle graphs

## Finding

Let \(M_n\) be a uniformly random perfect matching of \(2n\) distinctly labeled sites in cyclic order, with \(n\ge2\). The *circle graph* \(G_n\) has one vertex per matched chord and joins chords whose endpoints alternate. Condition on the natural Gauss-parity event \(E_n\) that every vertex of \(G_n\) has even degree. Let \(K_n\) be the number of connected components, \(L_n\) the number of vertices in a largest component, and \(S_n\) the number of chords joining cyclically adjacent sites.

For \(Z\sim\operatorname{Poisson}(2)\), the **joint** total-variation approximation is

\[
 d_{\mathrm{TV}}\!\left(\mathcal L((K_n,n-L_n)\mid E_n),\,\mathcal L((1+Z,Z))\right)=O(n^{-1}).
\]

In particular, under the even-degree condition, the graph has with probability \(1-O(n^{-1})\) exactly one component containing all non-simple chords and only isolated simple chords outside it; furthermore

\[
 \Pr(G_n\text{ is connected}\mid E_n)=e^{-2}+O(n^{-1}).
\]

The simple-chord count has the following **exact all-size binomial moments**, for integers \(0\le r\le n\):

\[
 \mathbb E\!\left[\binom{S_n}{r}\mid E_n\right]
 =\frac{1}{(n)_r}\frac{2n}{2n-r}\binom{2n-r}{r},
 \qquad (n)_r=\frac{n!}{(n-r)!}.
\]

Consequently, \(d_{\mathrm{TV}}(\mathcal L(S_n\mid E_n),\operatorname{Pois}(2))=O(n^{-1})\). The standard unrestricted matching ensemble instead has a \(1+\operatorname{Pois}(1)\) component limit (Flajolet–Noy); the conditioning therefore changes the Poisson parameter rather than merely selecting a negligible exceptional set. Earlier exact enumeration of *chord-connected permutations* is credited below; novelty is not claimed for that sequence or for the Gauss-parity bijection.

## Assumptions and scope

The \((2n-1)!!\) perfect matchings of the cyclic sites \(\{0,1,\ldots,2n-1\}\) are equally likely before conditioning. A chord is simple when its endpoints are adjacent modulo \(2n\), including the wraparound adjacency. The graph is the crossing/interlacement graph, not the geometrical drawing viewed as a one-regular graph. Graph components count isolated chords as size-one components. The total-variation distance on a countable state space is one-half the sum of absolute point-mass differences. The result is unconditional in the value of \(n\) except the explicit \(n\ge2\) restriction, and the error statements are uniform as \(n\to\infty\).

The Gauss even-degree condition is **necessary but not sufficient** for a chord diagram to be realizable as a plane curve; no such realizability condition is imposed or claimed. In particular, conditioning on every crossing degree even is the entire model, not a uniform choice from realizable knot diagrams.

## Proof

**1. The parity-conditioned probability space.** Consider any chord joining sites \(a<b\). Let \(I\) consist of the \(b-a-1\) sites strictly between its endpoints. Every other chord contributes zero, one, or two endpoints to \(I\), and contributes an odd number precisely when it crosses the distinguished chord. Hence

\[
 \deg_{G_n}(a,b)\equiv b-a-1\pmod2.
\]

All crossing degrees are even if and only if every matched chord joins sites of opposite parity. Thus, conditional on \(E_n\), the matching is a **uniform bijection** between the \(n\) even-labeled sites and the \(n\) odd-labeled sites, i.e. a uniform parity-reversing pairing or uniform permutation. There are exactly \(n!\) such matchings, so

\[
 \Pr(E_n)=\frac{n!}{(2n-1)!!}
 =\frac{2^n}{\binom{2n}{n}}
 \sim\frac{\sqrt{\pi n}}{2^n}.
\]

This parity-reversing permutation representation is classical; it is the same diagram ensemble introduced in Blitvić's chord-connected permutation enumeration.

**2. Exact binomial moments of simple chords.** A set of \(r\) simple chords can occur together if and only if it is an \(r\)-edge matching of the cycle \(C_{2n}\). By the standard cycle matching count, there are

\[
 m_{n,r}=\frac{2n}{2n-r}\binom{2n-r}{r}
\]

such sets, including \(m_{n,0}=1\). Every prescribed set joins sites of opposite parity. Its probability in a uniformly sampled parity-reversing pairing equals \(1/(n)_r\), since the remaining \(n-r\) parity pairs may be assigned arbitrarily. Summation over prescribed sets gives the exact formula in the finding. The special case \(r=1\) yields the exact mean \(\mathbb E[S_n\mid E_n]=2\).

**3. An explicit Poisson approximation.** Write \(q_{n,r}=\mathbb E[\binom{S_n}{r}\mid E_n]\) and \(q_{n,r}=0\) for \(r>n\). For \(0\le r\le n\), cancellation in the preceding formula yields

\[
 q_{n,r}=\frac{2^r}{r!}A_{n,r},\qquad
 A_{n,r}=\frac{2n}{2n-r}\prod_{j=0}^{r-1}
 \left(1-\frac{r-j}{2(n-j)}\right).
\]

For \(n\ge4\) and \(1\le r\le n/2\), the prefactor is at most two, exceeds one by at most \(r/n\), and the deficit of the product from one is bounded by the sum of its nonnegative factor deficits. Hence

\[
 |A_{n,r}-1|\le\frac r n+
 2\sum_{j=0}^{r-1}\frac{r-j}{2(n-j)}
 \le\frac{r^2+2r}{n}\le\frac{3r^2}{n}.
\]

For \(n/2<r\le n\), the elementary bound \(0\le A_{n,r}\le2\) gives the same last bound, and for \(r>n\) put \(A_{n,r}=0\), when it remains valid. Therefore

\[
 \left|q_{n,r}-\frac{2^r}{r!}\right|\le
 \frac{3r^2}{n}\frac{2^r}{r!}\qquad(r\ge0,\ n\ge4).
\]

For any nonnegative integer-valued random variable with these finite factorial moments, binomial inversion gives \(\Pr(S_n=s\mid E_n)=\sum_{r\ge s}(-1)^{r-s}\binom rs q_{n,r}\). The analogous absolutely convergent series with \(q_r=2^r/r!\) describes a \(\operatorname{Pois}(2)\) variable. Summing absolute differences and using \(\sum_{s=0}^r\binom rs=2^r\), we obtain the concrete, nonoptimized bound

\[
 d_{\mathrm{TV}}(\mathcal L(S_n\mid E_n),\operatorname{Pois}(2))
 \le\frac{3}{2n}\sum_{r\ge0}\frac{4^r r^2}{r!}
 =\frac{30e^4}{n}\quad(n\ge4).
\]

The finite error estimate is weak numerically at modest sizes but is a valid uniform \(O(n^{-1})\) proof.

**4. A closed-interval obstruction.** Call a consecutive cyclic interval of \(2k\) sites *closed* if no matching chord has exactly one endpoint inside it. A deterministic component-decomposition observation is the following: unless the diagram consists of one crossing component and simple isolated chords, or all its chords are simple, it contains a closed cyclic interval of \(2k\) endpoints for some \(2\le k\le\lfloor n/2\rfloor\). Here the phrase 'one crossing component' permits that component to be a singleton when all other isolated chords are simple.

For completeness, components of the crossing graph define noncrossing clusters of chord endpoints: any chord outside a connected crossing cluster which avoids crossing that cluster must have both endpoints in **one** gap between consecutive endpoints of the cluster. If there are two nontrivial clusters, a gap holding one of them gives a closed interval containing at least two chords, or else its complementary cyclic interval does; choose the side containing at most half the total chords. If there is only one nontrivial cluster, a non-simple isolated chord encloses a nonempty closed interior gap; should that gap contain only one chord, take the consecutive block including the enclosing chord as well. Taking the smaller closed side then gives a block of between two and half the chords. If there are no nontrivial components, this same nesting argument applies unless all chords are simple. This standard witness principle is the same structural mechanism behind the monolithic-diagram argument for unrestricted chord diagrams; the present use requires the different conditioned probability below. In small sizes the harmless all-simple exception is handled separately.

In the parity-reversing model, every consecutive interval of \(2k\) sites has exactly \(k\) sites of each parity. Its probability of being closed is therefore exactly

\[
 \frac{k!(n-k)!}{n!}=\binom nk^{-1}.
\]

For \(n\ge2\), the probability that *all* chords are simple equals \(2/n!\), since a cycle of even length has two perfect matchings. The union bound gives

\[
 \Pr\big((K_n,n-L_n)\ne(1+S_n,S_n)\mid E_n\big)
 \le\frac2{n!}+2n\sum_{k=2}^{\lfloor n/2\rfloor}\binom nk^{-1}.
\]

For \(n\ge6\), binomial unimodality bounds the last expression by

\[
 \frac2{n!}+\frac4{n-1}+\frac{6n}{(n-1)(n-2)}=O(n^{-1}).
\]

Off this exceptional event, the crossing graph comprises exactly one component of size \(n-S_n\) and \(S_n\) singleton simple-chord components, so \(K_n=1+S_n\) and \(n-L_n=S_n\). A coupling inequality combined with step 3 gives the asserted **joint** total-variation bound. Since this joint law places probability \(e^{-2}\) on \((1,0)\), and \(K_n=1\) is the graph-connectivity event, the connectivity formula follows. \(\square\)

## Verification

The reproducible standard-library file `verify.py` independently enumerates **all** unrestricted chord matchings through six chords, checking equivalence of the Gauss even-degree and opposite-endpoint-parity conditions and the exact count \(n!\). It separately enumerates every parity-reversing pairing through eight chords and verifies the exact simple-chord binomial moments, the reconstructed finite distributions, and every observed failure of the one-giant-component property against the closed-interval witness. Rational tests through \(n=65\) check the intermediate moment error inequality. Executing `python verify.py` in this directory returns `VERIFY_OK 75108 finite exact assertions`.

These are finite corroborations. The all-size claims depend on the combinatorial counting, deterministic witness argument, and analytic error inequalities in the proof, not on extrapolation from enumerated sizes.

## Relationship to prior work

Blitvić's *Stabilized-Interval-Free Permutations and Chord-Connected Permutations* (2014), Definitions 2–3 and Theorem 3, already introduces **exactly this parity-reversing matching ensemble**, defines its connected chord diagrams and enumerates connected instances using noncrossing-partition generating functions. The OEIS chord-connected permutation sequence A390400 records these earlier exact connected counts. Neither the ensemble, its permutation encoding, nor its exact connected-count sequence is claimed as new. The joint random **component-count/largest-component** total-variation law with a rate, including the \(\operatorname{Pois}(2)\) parameter and the explicit high-probability component profile, is the present contribution.

Flajolet and Noy's unrestricted matching model has \(1+\operatorname{Pois}(1)\) components and a single giant component. Acan's related simple-chord and monolithic arguments also use unrestricted uniform pairings. The conditional ensemble here is *exponentially rare* under the unrestricted law, so none of those unrestricted distributional conclusions transfers directly. Paguyo's Poisson approximation for simple chords likewise concerns the unrestricted model; a later sharp \(\operatorname{Pois}(1)\) correction for that model cannot supply the present parity-conditioned theorem. The comparison does not assert new classical matching counts or the parity criterion.

## Limitations

The theorem is restricted to uniform perfect matchings conditioned only on even crossing degrees, with cyclic labeling fixed. It does **not** describe random realizable Gauss diagrams, nonuniform pairings, arbitrary graph degree-parity conditioning, or detailed internal structure of the giant component. The stated \(O(n^{-1})\) constants are not optimized. The finite exact enumeration and noncrossing decomposition of chord-connected permutations were known; identifying the same object in the earlier paper is essential to scope the novelty correctly. Although no inspected published source states the **joint** total-variation limit and explicit rate, stronger implicit consequences of prior exact combinatorial generating functions remain a historical-priority risk. No independent external validation has been performed.

## References

1. N. Blitvić, *Stabilized-Interval-Free Permutations and Chord-Connected Permutations*, DMTCS Proceedings AT, FPSAC 2014, pp. 801–814, https://dmtcs.episciences.org/2443/pdf (Definitions 2–3, Theorem 3 and Section 2.3).
2. M. Noy, *Enumeration of Geometric Configurations on a Convex Polygon*, seminar notes dated 16 December 1999, https://algo.inria.fr/seminars/sem99-00/noy1.html (Section 2, unrestricted component and giant-component limits, joint work with P. Flajolet).
3. H. Acan, *On a uniformly random chord diagram and its intersection graph*, arXiv:1501.01489, first posted 7 January 2015, https://arxiv.org/abs/1501.01489 (simple chords, monolithic diagrams and unrestricted intersection graph).
4. J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134, https://arxiv.org/abs/2104.01134 (unrestricted simple-chord Poisson approximation; comparison only).
5. *OEIS A390400*, Number of chord-connected permutations, https://oeis.org/A390400 (the already known exact connected counts of the parity-reversing matching model).
