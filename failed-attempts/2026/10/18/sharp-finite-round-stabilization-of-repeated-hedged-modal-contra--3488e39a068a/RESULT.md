# Sharp finite-round stabilization of repeated hedged modal contraction

## Finding

Fix the one-agent-language formula \(\varphi=\Diamond_a\neg p\), equivalently \(\neg B_a p\). For every finite nonempty Kripke carrier \(W\) of size \(n\), every set of agents containing \(a\), every valuation of \(p\), and all initial doxastic relations (without reflexivity, transitivity or seriality assumptions), iterating the same hedged public contraction on \(\varphi\) stabilizes in at most \(n\) strict model transformations. This bound is attained for every \(n\) with a single agent and a single atom.

More precisely, define \(P=V(p)\) and \(A_t=\{w\in W:R_{a,t}(w)\subseteq P\}\). In the initial relation \(R_{a,0}\), consider the directed graph induced on \(A_0\). Whenever \(A_t\) still contains a world where \(p\) is false, its next stage is obtained by simultaneously deleting all vertices without a successor inside the current set:

\[
A_{t+1}=\{w\in A_t:R_{a,0}(w)\cap A_t\ne\varnothing\}.
\]

After no such false-\(p\) vertex remains, at most one additional contraction is needed. In contrast, repeated contraction on any modal-depth-zero (propositional) formula stabilizes after one application, on any carrier. Thus the first modal depth already permits arbitrarily long finite transients under a *fixed* formula.

## Assumptions and scope

We use the exact edge-addition definition of hedged public announcements in Belardinelli and Zhang (2026, Definition 4.1). A Kripke model \(M_t=(W,(R_{b,t})_{b\in\mathrm{Ag}},V)\) has nonempty finite \(W\), any nonempty set of agents, and arbitrary binary relations. Contraction does not change \(W\) or \(V\). At world \(w\), agent \(b\)'s successor set is enlarged to include *all* worlds where the contracted formula was false before that update, if and only if all current \(b\)-successors satisfy the formula. Formally, for \(A_t=\{u:M_t,u\models\neg\varphi\}\),

\[
R_{b,t+1}(w)=
\begin{cases}
R_{b,t}(w)\cup A_t,&R_{b,t}(w)\cap A_t=\varnothing,\\
R_{b,t}(w),&R_{b,t}(w)\cap A_t\ne\varnothing.
\end{cases}
\]

The contraction formula \(\varphi=\neg B_a p\) has a distinguished agent \(a\); other agents update in parallel by the same rule. Empty successor sets are permitted. A *strict* transformation means some ordered accessibility pair has been added. A stabilization horizon is the number of strict transformations before a fixed model is reached. No simultaneous deletion of possible worlds or S5 restriction is assumed.

## Proof

**1. Antitone counterexample sets.** The truth of atomic \(p\) remains fixed. Since every accessibility row only grows, the set
\[
A_t=\{u:M_t,u\models B_a p\}=\{u:R_{a,t}(u)\subseteq P\}
\]
is decreasing: \(A_{t+1}\subseteq A_t\). If \(A_t=\varnothing\), the formula has no counterexamples and the update changes no relation.

**2. A constant counterexample set forces termination.** Assume \(A_t\ne\varnothing\) and \(A_{t+1}=A_t\). Every successor row of every agent in \(M_{t+1}\) meets \(A_t\): a row that already met it is unchanged, while a disjoint row receives all of it. Since \(A_{t+1}=A_t\), every row now fails the condition for adding new edges. Thus \(M_{t+2}=M_{t+1}\). In a sequence of strict transformations there can therefore be only strict descents of \(A_t\), followed possibly by one final strict step with no descent. If it ends at the empty set there are at most \(|A_0|\) descents. Otherwise at most \(|A_0|-1\) descents precede the last possible strict step. In either case at most \(|A_0|\le n\) strict transformations occur. This argument applies to arbitrarily many other agents because the same \(A_t\) drives all their rows.

**3. Exact sink-pruning description.** Write \(Q=W\setminus P\), and let \(H\) be \(R_{a,0}\) restricted to \(A_0\). Suppose \(A_t\cap Q\ne\varnothing\). Every \(u\in A_t\) has retained its original \(a\)-successor row: at any preceding stage at which it could have been enlarged, adding the then-current counterexample set (which contains a \(Q\)-world) would have inserted a false-\(p\) successor, excluding \(u\) permanently from all later \(A\)'s. Hence for \(u\in A_t\), \(R_{a,t}(u)=R_{a,0}(u)\). If this row intersects \(A_t\), no update occurs and \(u\) stays in \(A_{t+1}\). If it is disjoint from \(A_t\), the row acquires all of \(A_t\), including a false-\(p\) world, so \(u\) leaves \(A_{t+1}\). This proves
\[
A_{t+1}=\{u\in A_t:R_{a,0}(u)\cap A_t\ne\varnothing\}.
\]
If \(A_t\cap Q=\varnothing\), all new edges point only to true-\(p\) worlds, so \(A_{t+1}=A_t\), and Step 2 gives stabilization after at most this one further update. The same conclusion applies if sink pruning has reached an unchanged set containing false-\(p\) worlds.

**4. Sharp witness for every carrier size.** For each \(n\ge1\), put \(W=\{0,1,\ldots,n-1\}\), choose one agent \(a\), set \(P=W\setminus\{0\}\), and let the only initial arrows be \(i\,R_{a,0}\,(i+1)\) for \(0\le i<n-1\). All initial rows are subsets of \(P\), so \(A_0=W\), and the only false-\(p\) world in \(A_0\) is \(0\). The pruning recurrence gives \(A_t=\{0,\ldots,n-1-t\}\) for \(0\le t\le n\), with \(A_n=\varnothing\). At each stage exactly the last remaining world gains a false-\(p\) successor and exits \(A_t\); hence each of the \(n\) updates is strict. This includes \(n=1\), where the initially empty row receives its own world.

**5. Minimal modal depth.** If a contracted formula \(\psi\) is purely propositional, its truth set and its counterexample set \(A=\{u:M,u\models\neg\psi\}\) do not change under any number of edge additions. After one contraction, every agent/world row either already intersected \(A\) or now contains all of \(A\). A second contraction adds nothing. This argument works for infinite carriers as well. It is sharp when \(A\ne\varnothing\) and an initial row avoids \(A\). Combining this with Step 4 proves that modal depth one is the first depth with unbounded finite horizons.

## Verification

The standalone Python 3 program `verify.py` uses exact integer bit masks and no external libraries. Run `python3 verify.py` from its directory. It independently simulates the contraction definition; for the single-agent fragment it checks every relation and Boolean valuation for \(n=1,2,3\), with 4,164 cases, plus 50,000 seeded random cases on carriers of sizes four through six. For two agents it checks 1,032 exhaustive models on one and two worlds; 30,000 seeded cases with four agents test sizes three through five. For every case it verifies the \(n\)-round upper bound and, whenever the required false-\(p\) witness is present, the predicted outgoing-sink recursion. It separately checks 4,164 depth-zero idempotence cases and explicit sharp path witnesses for sizes one through 29. The observed output begins `VERIFY_OK`.

These tests are corroboration only: the universal bound, exact recursion, and sharpness for every \(n\) follow from the symbolic proof above.

## Relationship to prior work

Belardinelli and Zhang (2026, arXiv:2606.31861, Definition 4.1) introduce exactly the contraction operator used here, prove reduction axioms and analyze preservation and success. Their conclusion singles out iterative properties of the broader generalized dynamic framework for future study. The inspected sections, including the appendix, do not state this finite-horizon theorem, its exact sink-pruning rule, or its modal-depth threshold. The present result is restricted to the repeated application of one fixed formula in their basic hedged-announcement semantics, not a theorem about all generalized event models.

Earlier work on iterated belief change, public announcements, and global/local announcements uses different updates or studies other logical properties. Those results do not directly furnish a bound for the repeated edge-addition operator analyzed here. Sink removal in finite directed graphs is a standard operation; its identification with this specific modal contraction is the claimed reduction, not a claim that sink peeling itself is new.

## Limitations

The theorem assumes a finite world set, and the precise \(n\)-bound is not asserted for infinite frames. It treats a fixed depth-one formula whose sole modal operator is \(\Diamond_a\); a general modal formula may behave differently. No claim is made about arbitrary GDEL event-model compositions, frame-condition preservation, or independent verification. The finite experiments are not evidence of an infinite-domain theorem. A differently phrased earlier analysis of the same contraction remains an originality risk.

## References

- Gaia Belardinelli and Snow Zhang, *Belief Contraction in Dynamic Epistemic Logic*, EPTCS 447 (2026), 137–157, DOI: 10.4204/EPTCS.447.8, arXiv:2606.31861, first submitted 2026-06-30. Full-text sections and appendix inspected via https://www.researchgate.net/publication/408302467_Belief_Contraction_in_Dynamic_Epistemic_Logic .
- Francesco Belardinelli, Hans van Ditmarsch, and Wiebe van der Hoek, *A Logic for Global and Local Announcements*, EPTCS 251 (2017), arXiv:1707.08735. Related but distinct update semantics.
- Jan-Willem Roorda, Wiebe van der Hoek, and John-Jules Meyer, *Iterated Belief Change in Multi Agent Systems*, Logic Journal of the IGPL 11 (2003), 223–246, DOI: 10.1093/jigpal/11.2.223. Earlier general framework with different update semantics.
