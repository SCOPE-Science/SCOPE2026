# Sharp one-insertion sphere volumes of layered set partitions

## Finding

Let \(P\) be a partition of \([n]\), represented by its canonical restricted-growth word \(w=0^{a_1}1^{a_2}\cdots(k-1)^{a_k}\), where \(k\ge1\), \(a_i\ge1\), and \(\sum_i a_i=n\). Such a partition is called **layered**. Form \(\mathcal I(P)\) by inserting one new indexed element into any of the \(n+1\) linear gaps and putting it either into an existing block or into a new singleton block. Standardize block names by first occurrence. Count equal output partitions only once, whether or not they are layered.

If \(L_1,\ldots,L_h\) are the lengths of the maximal chains of consecutive singleton blocks (the list can be empty), then
\[
|\mathcal I(P)|=(n+1)(k+1)-n-\sum_{j=1}^{h}\binom{L_j+1}{2}.
\]

For fixed \(1\le k\le n\), put \(B=(n+1)(k+1)-n\), \(t=\min\{k,n-k\}\), \(s=k-t\), \(\ell=t+1\), and \(s=\ell a+b\), where \(0\le b<\ell\). Set
\[
T_{\min}=(\ell-b)\binom{a+1}{2}+b\binom{a+2}{2},\qquad
T_{\max}=\begin{cases}\binom{k+1}{2},&n=k,\\\binom{k}{2},&n>k.\end{cases}
\]
Then the minimum sphere volume is \(B-T_{\max}\), and the maximum is \(B-T_{\min}\). When \(n=k\), both occur uniquely at the all-singleton partition. When \(n>k\), the minimum occurs at exactly two compositions (one if \(k=1\)): one nonsingleton part of size \(n-k+1\) at either endpoint. For \(k<n<2k\), the maximum occurs at exactly \(\binom{t+1}{b}\) compositions: all \(t=n-k\) nonsingleton parts have size two, with singleton runs of lengths \(a\) and \(a+1\) in the \(t+1\) gaps around them, of which exactly \(b\) have the larger length. For \(n\ge 2k\), the maximum occurs at the \(\binom{n-k-1}{k-1}\) compositions with all parts at least two.

For example, \((1,1,2)\) and \((1,2,1)\) have the same length and number of blocks but respective sphere volumes 13 and 14.

## Assumptions and scope

Blocks are unlabeled; canonical labels merely record order of first occurrence. Insertion preserves the order and the block equivalences of the original elements. All output partitions on \([n+1]\) are allowed. Equality means equality of the final partitions, not their insertion histories. The formulas include \(n=k\), \(k=1\), and the case of no singleton runs.

## Proof

**1. Split by output block count.** There are \((n+1)(k+1)\) histories: a choice of gap and either an old block or a new singleton. The two types have respectively \(k\) and \(k+1\) blocks in the output, so their images are disjoint.

**2. New-singleton outputs.** Insertion inside a nonsingleton block splits its interval, producing a nonlayered output; the inserted singleton position is uniquely determined by that split. Insertions at block boundaries remain layered. In that case the nonsingleton parts keep their order and sizes, so the output composition determines which intervening or endpoint gap in the list of nonsingleton parts gained a singleton. All \(L+1\) insertion sites around the \(L\) consecutive singletons in that gap give the same output. Thus each singleton run of length \(L\) accounts for \(L\) lost histories, and there are \(n+1-\sum_j L_j\) new-singleton outputs.

**3. Old-block outputs.** An old-block insertion yields a layered output exactly when the gap is in or at an endpoint of the selected block's interval. There are \(a_i+1\) such gaps for block \(i\), all giving the same composition with its \(i\)-th part increased by one. Thus \(n+k\) histories give \(k\) layered outputs, and \((k-1)n\) histories give nonlayered outputs.

To count collisions among these last histories, regard each history of an output \(Q\) as deleting one of its positions to recover \(P\). A history in this class deletes a member of a block of size at least two. A noncontiguous block not containing the deleted position can become contiguous only if that position is the sole gap between two contiguous runs of that block. In particular, two distinct deletions outside a block cannot both make that same noncontiguous block contiguous.

Suppose two positions to be deleted belong to distinct blocks \(X,Y\). Any block other than \(X,Y\) must already be contiguous. If \(X\) is noncontiguous, deleting the position in \(Y\) must close its sole gap. That position is flanked by members of \(X\), so is isolated in \(Y\); because \(Y\) has size at least two, \(Y\) is noncontiguous too. The same argument applies if \(Y\) is initially known to be noncontiguous. As \(Q\) is nonlayered, both are therefore noncontiguous, and each deleted position is flanked by members of the other block. The positions must be adjacent: if the deleted member of \(X\) were not a neighbor of the gap-closing member of \(Y\), its deletion would leave two members of \(X\) still separated by that member of \(Y\). After exchanging \(X,Y\) if necessary, the two positions are the middle \(Y,X\) in a consecutive segment \(X^u Y X Y^v\), where \(u,v\ge1\). The runs \(X^u\) and \(Y^v\) exhaust the other occurrences of their respective blocks because each block must become contiguous when its isolated position is deleted. The two resulting layered compositions have respective consecutive parts \((u+1,v)\) and \((u,v+1)\) at the same place. They cannot both equal \(P\).

Thus two histories of the same nonlayered \(Q\) for a fixed \(P\) must delete members of the same block \(X\). All other blocks of \(Q\) must be contiguous by the sole-gap observation. The only way either member can be deleted to make \(X\) contiguous is that \(X\) consists of two separated positions, each a run of length one. Write \(b_1,\ldots,b_m\) for the lengths of the contiguous intervening blocks, where \(m\ge1\). The two deletion compositions agree exactly when \((1,b_1,\ldots,b_m)=(b_1,\ldots,b_m,1)\), that is, when all the intervening blocks are singletons. So each collision corresponds to two distinct blocks in one singleton run of \(P\). Conversely, for a pair of positions \(i<j\) of singleton blocks in one run of \(P\), pair positions \(i\) and \(j+1\) in the output, keep intervening positions singleton, and keep the blocks before and after this segment unchanged up to index shifts. This gives the unique output for that pair, and deleting either member of the pair gives \(P\). The output then has exactly two histories: any other history would require a collision across different blocks or a third position in \(X\). The number of lost histories is therefore \(\sum_j\binom{L_j}{2}\), giving \(k+(k-1)n-\sum_j\binom{L_j}{2}\) old-block outputs.

Adding the two classes yields the claimed volume, using \(L+\binom L2=\binom{L+1}{2}\).

**4. Optimize the singleton-run penalty.** At most \(t\) blocks can have size greater than one. If fewer than \(t\) do, a singleton is available and there is a block of size at least three, since the number of extra elements \(n-k\) exceeds the number of nonsingleton blocks. Transferring one element from that block to the singleton, without changing the order of parts, splits or shortens its singleton run and strictly reduces the penalty. Thus every minimizer of the penalty uses \(t\) nonsingletons. If \(k<n<2k\), these all have size two. Allocate the remaining \(s\) singleton parts to \(t+1\) gaps. A transfer from a longer gap to one shorter by at least two strictly decreases the sum of \(\binom{L+1}{2}\); the allocations with gap lengths differing by at most one all give the same penalty. This proves \(T_{\min}\) and the stated count for this range. If \(n\ge2k\), any composition without singletons gives penalty zero, and all others have positive penalty. Distributing \(n-2k\) excess elements among the \(k\) parts gives the stated count. The case \(n=k\) has only the all-singleton composition.

For the maximum penalty when \(n>k\), there are at most \(k-1\) singletons. The function \(f(L)=\binom{L+1}{2}\) is strictly increasing, and \(f(x+y)-f(x)-f(y)=xy>0\) for positive \(x,y\). Thus the penalty is at most \(f(k-1)\), with equality only for \(k-1\) singletons in one run, with the empty run allowed for \(k=1\). The single nonsingleton block is then of size \(n-k+1\) and at an endpoint. When \(n=k\), the penalty is \(f(k)\) for the unique composition. Subtracting from \(B\) gives the volume extrema.

## Verification

The accompanying Python program `check.py` enumerates the positive compositions of integers through ten and constructs normalized insertion outputs to check the volume, the extrema and their attaining counts. It separately enumerates output partitions and computes their one-deletion preimages for source length at most seven. The recorded output is `VERIFY_OK forward_layered_cases 1023 extremal_strata 55 independent_reverse_cases 127 max_n 10`. These are finite checks, not the basis of the all-length proof.

## Relationship to prior work

Restricted-growth presentations and layered partitions are standard in set-partition pattern avoidance (Sagan; Dahlberg et al.). Bean, Bell and Ollson study horizontal and vertical insertion encodings and the regularity of restricted-growth languages, not the same counting problem as the full one-element sphere. A closely related structural result is described in the catalogue entry for *Exact distance-resolved collisions of one-deletion set-partition reads*: a general classification of when two positions of an output have equal deletion reads. The theorem here counts distinct outputs conditional on one layered source, and then determines the sharp volumes and all attaining compositions at fixed \((n,k)\). The direct collision argument above supplies the needed source-specific enumeration.

## Limitations

Only one insertion into a layered source is treated; outputs need not be layered. This does not assert an insertion-code capacity or a formula for arbitrary sources or multiple insertions. The finite checker does not prove the infinite theorem, and the related-work comparison is not a claim of exhaustive historical priority.

## References

1. B. E. Sagan, *Pattern Avoidance in Set Partitions*, https://arxiv.org/abs/math/0604292.
2. S. Dahlberg et al., *Set partition patterns and statistics*, https://arxiv.org/abs/1502.00056.
3. C. Bean, P. C. Bell, A. Ollson, *The Insertion Encoding of Restricted Growth Functions*, https://doi.org/10.1007/s00026-026-00832-y.
4. *Exact distance-resolved collisions of one-deletion set-partition reads*, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-exact-distance-resolved-collisions-of-one-deletion-set-partition--d07bd07e8019.
