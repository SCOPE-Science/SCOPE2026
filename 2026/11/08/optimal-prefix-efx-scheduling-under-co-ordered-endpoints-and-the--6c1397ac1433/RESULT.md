# Optimal prefix-EFX scheduling under co-ordered endpoints and the sharp thin-nesting obstruction

## Finding

**Theorem.** Fix an integer \(m\ge2\). Consider a finite stream of strictly positive-duration, half-open jobs \(J_i=[s_i,e_i)\) with unit value for every machine, arriving in the order
\[
 s_1\le s_2\le\cdots\le s_N,\qquad e_1\le e_2\le\cdots\le e_N.
\]
There is an irrevocable deterministic online policy that, after every prefix of the input, (a) schedules as many jobs as an unconstrained offline optimum, (b) makes the machine job counts differ by at most one, and (c) never moves or revokes an accepted job. Consequently its allocation is EFX, and hence EF1, after every arrival; the optimal online fair competitive ratio and offline price of fairness are both exactly \(1\) on this class.

The order condition is **co-ordering of start and finish times**. Every proper-interval representation without containment can be put in this order, breaking equal starts by increasing ends. The stated order condition can also admit certain equal-start nested pairs; co-ordering, rather than a purely graph-theoretic properness assumption, is the precise hypothesis. This theorem does *not* assert online optimality for arbitrary interval streams or arbitrary arrival orders.

The structural hypothesis is sharp even against arbitrarily small changes in length. For every \(m\ge2\) and every \(\varepsilon>0\), there exist exactly \(m+2\) unit-value jobs whose lengths belong to \([1,1+\varepsilon]\), with unconstrained schedulable count \(m+2\) but maximum EF1 (or EFX) schedulable count \(m+1\). Moreover, among **all** interval families on \(m\) machines, no example with fewer than \(m+2\) input jobs can have a positive EF1 welfare loss. Thus \(m+2\) is the exact first obstruction size for unrestricted intervals, and infinitesimal nesting suffices to attain it.

## Assumptions and scope

An input consists of a finite sequence of intervals with real endpoints \(s_i<e_i\). Machines are identical and have unit additive valuation for each accepted job. A feasible assignment chooses a subset of intervals and assigns each chosen interval to exactly one of \(m\) machines, with pairwise-disjoint half-open intervals on any one machine. Unassigned intervals contribute neither welfare nor utility. A machine's utility is the number of intervals assigned to it.

With these valuations, EFX and EF1 are equivalent to the arithmetic requirement that the maximum machine load minus the minimum load is at most one. Indeed, for every ordered pair of machines, deleting any one interval from the second machine must eliminate envy; all intervals are positively valued and interchangeable for utility purposes. Thus fair welfare means maximum feasible accepted cardinality subject to this load discrepancy bound.

The main positive result assumes starts and finishes are **co-ordered** as displayed, not that the intervals all have exactly the same duration. In particular, it covers equal-length jobs, shifted and length-varying proper interval presentations, and repeated equal endpoints. With distinct start times, co-ordering excludes a later-starting interval from ending earlier than a previous interval; ties may be arranged by increasing finishes. A prefix means the first \(p\) presented jobs, for each \(0\le p\le N\).

## Proof

**1. Online policy.** Process intervals in input order. When \(J_i\) arrives, count earlier *accepted* intervals that are active at \(s_i\), i.e. \(s_j\le s_i<e_j\). Reject \(J_i\) if the count is \(m\), and otherwise accept it. Number accepted intervals \(1,2,3,\ldots\) chronologically and assign the \(r\)-th accepted interval to machine \(1+((r-1)\bmod m)\). No later decisions are modified.

**2. Ordered-subsequence criterion.** If \(i_1<\cdots<i_t\) are indices from a co-ordered stream, these \(t\) intervals are feasible on \(m\) machines *if and only if*
\[
  e_{i_j}\le s_{i_{j+m}}\quad\text{for every }1\le j\le t-m.
\]
Sufficiency: assign intervals in index order cyclically to machines; consecutive intervals of a single machine have indices separated by \(m\), hence do not overlap. Necessity: if \(e_{i_j}>s_{i_{j+m}}\), then, by monotonicity of starts and ends, the \(m+1\) intervals \(i_j,\ldots,i_{j+m}\) are simultaneously active at time \(s_{i_{j+m}}\), contradicting capacity \(m\). Equality is allowed because the jobs are half-open.

**3. The online policy is feasible.** Suppose the newly accepted interval is the \(r\)-th accepted interval. If \(r\le m\), its machine has not previously been used. If \(r>m\) and its prior cyclic predecessor, accepted interval \(r-m\), were active at \(s_i\), all of the intervening \(m-1\) accepted intervals would also still be active there (their finishing times are no earlier). The current policy would then detect \(m\) active accepted jobs and reject \(J_i\), a contradiction. Thus its cyclic predecessor has finished. The policy's assignment is feasible by induction.

**4. Maximum cardinality after every prefix.** Let \(g_r\) be the index of the policy's \(r\)-th acceptance, when one exists. Let \(o_1<\cdots<o_t\) index an arbitrary feasible solution among the first \(p\) inputs. We show \(g_r\) exists and \(g_r\le o_r\) for all \(1\le r\le t\). The base \(r\le m\) follows because all of the first \(\min(m,p)\) jobs can be accepted, and the policy accepts them. For \(r>m\), assume \(g_j\le o_j\) for \(j<r\). Feasibility of the reference solution and step 2 give
\[
 s_{o_r}\ge e_{o_{r-m}}\ge e_{g_{r-m}}.
\]
If the policy had already accepted \(r\) jobs by the arrival of \(o_r\), then \(g_r\le o_r\) and there is nothing to prove. Otherwise, at that arrival its accepted set has exactly \(r-1\) jobs or fewer. It cannot have fewer than \(r-1\): by induction, the \((r-1)\)-st acceptance occurred no later than \(o_{r-1}<o_r\). Its first \(r-m\) accepted jobs have all finished by time \(s_{o_r}\), since finishes are nondecreasing. Hence at most \(m-1\) accepted jobs are active, so the policy accepts \(o_r\) and \(g_r\le o_r\). This completes the induction, including the existence argument. In particular the policy accepts at least \(t\) jobs, for every feasible solution and every prefix \(p\); hence it is offline-cardinality-optimal for every prefix.

**5. Fairness.** After accepting \(t\) jobs, cyclic assignment gives every machine either \(\lfloor t/m\rfloor\) or \(\lceil t/m\rceil\) jobs, including at times when no new jobs are accepted. By the equivalence in the assumptions, the allocation is EFX and EF1 for every arrival prefix. Since it achieves full unconstrained welfare, both relevant ratios are \(1\), and no algorithm can improve them.

**6. Arbitrarily thin nesting obstruction.** Choose \(0<\delta<\min\{1/4,\varepsilon/2\}\). Take the three disjoint unit jobs
\[
 I_0=[0,1),\quad I_1=[1,2),\quad I_2=[2,3),
\]
and \(m-1\) copies of the job
\[
 H=[1-\delta,\,2+\delta).
\]
Every copy of \(H\) overlaps all three \(I_j\), and all copies of \(H\) pairwise overlap. Schedule each copy on a separate machine and all three unit jobs on the remaining machine. This feasible schedule accepts \(m+2\) jobs and is therefore an unconstrained optimum. But in *every* feasible assignment of all \(m+2\) jobs, each copy of \(H\) occupies its own machine, cannot share that machine with any other job, and the three unit jobs are forced onto the last machine. The load vector, up to permutation, is \((3,1,\ldots,1)\), violating EF1. For a feasible fair schedule, remove one copy of \(H\): this leaves \(m-2\) long jobs and all three unit jobs, which can occupy the two remaining machines as a pair and a singleton, attaining \(m+1\) accepted jobs with loads \((2,1,\ldots,1)\). This also covers \(m=2\), for which the sole copy of \(H\) is removed and the three unit jobs split as two plus one. Thus the fair optimum is precisely \(m+1\). Every job has length \(1\) or \(1+2\delta<1+\varepsilon\).

**7. Minimality of the obstruction size.** For an arbitrary interval family, let \(L\) be its maximum schedulable cardinality. If \(L\le m\), put every accepted job of an optimal schedule on a different machine: no two intervals share a machine and the load discrepancy is at most one. If \(L=m+1\), any feasible optimal schedule on \(m\) machines has some machine containing at least two compatible jobs. Select two such jobs, assign them to one machine, and put the remaining \(m-1\) jobs on distinct other machines. The resulting schedule is feasible and has loads \((2,1,\ldots,1)\), so it is EF1. If the input has fewer than \(m+2\) jobs, necessarily \(L\le m+1\). Therefore welfare loss first becomes possible at \(m+2\), and step 6 attains this lower bound.

## Verification

The standalone `CHECK.py` uses exact rational interval endpoints and exhaustive subset searches to compare the online policy with the offline maximum on \(14{,}965\) finite instances, including repeated starts and co-ordered nonidentical durations. It also checks the thin-nesting family for five machine counts and exactly enumerates the EF1 optimum for small machine counts. Running `python CHECK.py` in the directory containing this document and the script reports `PASS: 14965 finite instances (greedy, fairness and obstruction).` The universal quantifiers and sharp first-instance claim follow from the analytic arguments above, not from finite testing.

## Relationship to prior work

Borst, Shahkarami and Vaish introduce the fair interval-scheduling setting, prove general upper and lower bounds for unweighted offline EF1 and online EF1 scheduling, and allow intervals to be nested. Their general sharp online deterministic ratio is \(2-1/m\), compared with the exact ratio \(1\) here **under the co-ordered-endpoints restriction**. Their unweighted lower-bound witness already uses the important long-versus-disjoint-short geometry, with \(m-1\) long intervals overlapping \(2m-1\) short intervals. Our thin-nesting witness is a near-unit modification of this known mechanism, with **three** shorts and an exact \(m+2\)-job minimality theorem. Their general bound does not establish the co-ordered every-prefix optimum or the arbitrarily small length-perturbation boundary. Faigle and Nawijn's earlier optimal online interval scheduler, cited by Borst et al., allows replacement of accepted jobs; the new constructive point here is **no replacement plus cyclic EFX at every prefix** for co-ordered endpoints. We do not claim novelty for the underlying greedy acceptance principle or long/short obstruction motif. Our result does not challenge the general lower bound.

Curbelo and Malko analyze online coloring of proper/unit interval representations with a freely chosen (non-start-ordered) arrival sequence and a different objective (number of colors). Their coloring game is not this irrevocable start-ordered, maximum-cardinality, prefix-EFX problem. Established equitable-coloring results for claw-free graphs, discussed by Gomes, Lima and dos Santos and attributed to de Werra, imply related *static* equitable colorability of unit-interval conflict graphs. We do **not** claim novelty for static equitable colorability or for the individual basic earliest-finish and cyclic-coloring ingredients. The stated contribution is the combined prefix-optimal fair scheduling theorem and the sharp arbitrary-short-nesting obstruction and minimality theorem.

## Limitations

The positive theorem requires both the arrival order and the nondecreasing finish-time order. It does not treat arbitrary-length nested jobs, arrivals in adversarial order unrelated to start times, weighted utilities, heterogeneous machines, or a different fairness definition. The instability family only demonstrates that an arbitrarily small *multiplicative duration deviation* can destroy the full-welfare guarantee; it does not give the global worst-case ratio for near-unit intervals. Earlier unindexed work may contain an equivalent composite theorem or variant, and further independent literature review is warranted. The finite verifier is a consistency check, not a substitute for proof or independent audit.

## References

1. S. Borst, G. Shahkarami and R. Vaish, *Fair Division Meets Scheduling: Approximately Envy-Free Interval Scheduling*, first public 15 August 2026, arXiv:2608.15159, https://arxiv.org/abs/2608.15159 .
2. I. R. Curbelo and H. R. Malko, *On the on-line coloring of unit interval graphs with proper interval representation*, first public 11 January 2024, arXiv:2401.05648, https://arxiv.org/abs/2401.05648 .
3. G. de C. M. Gomes, C. V. G. C. Lima and V. F. dos Santos, *Parameterized Complexity of Equitable Coloring*, first public 30 October 2018, arXiv:1810.13036, https://arxiv.org/abs/1810.13036 . This paper discusses earlier equitable-colorability of claw-free graphs attributed to de Werra.
