# Nine pure-modal normal forms and exact observation fibers on Boolean compatibility frames

## Finding

For every integer \(n\ge 2\), let \(W_n=\mathcal P([n])\setminus\{\varnothing\}\) and give it the symmetric reflexive compatibility relation \(uRv\) exactly when \(u\cap v\ne\varnothing\). On the full event algebra \(\mathcal P(W_n)\), pure compositions of the usual Kripke necessity \(\Box\) and possibility \(\Diamond\), including the empty composition, yield **exactly nine distinct unary operations**, independently of \(n\):
\[
 \mathrm{id},\quad \Box,\quad\Diamond,\quad\Box^2,\quad\Box\Diamond,\quad\Diamond\Box,\quad\Diamond^2,\quad\Box^2\Diamond,\quad\Diamond^2\Box.
\]

Moreover, the joint observation map \(U\mapsto(\Box U,\Diamond U)\) has exactly \(2^{n+1}-1\) possible values, with an exact multiplicity formula for every value. Consequently, one can quantify precisely how much information these two modal observations preserve about an arbitrary event.

Put \(D_A=\{v\in W_n:v\subseteq A\}\) and \(H_A=\{v\in W_n:v\cap A\ne\varnothing\}\), for \(A\subseteq[n]\). The set of possible joint observations is
\[
 \{(\varnothing,H_S):S\subseteq[n]\}\ \cup\ \{(D_T,W_n):T\subseteq[n]\}.
\]
The two indexed families intersect in exactly the single observation \((\varnothing,W_n)\).

Define the classical finite-cover count
\[
 F(s)=\sum_{j=0}^{s}(-1)^j\binom{s}{j}2^{2^{s-j}-1}\quad(s\ge0).
\]
This is the preexisting covering sequence OEIS A003465, not a newly claimed combinatorial sequence. For \(S\subsetneq[n]\), the observation \((\varnothing,H_S)\) has \(F(|S|)\) preimages. For nonempty \(T\subseteq[n]\), the observation \((D_T,W_n)\) has \(F(n-|T|)\) preimages. The shared observation \((\varnothing,W_n)\) has exactly
\[
 F(n)-\sum_{t=1}^{n}\binom nt F(n-t)
\]
preimages. These three disjoint cases exhaust all events \(U\subseteq W_n\).

## Assumptions and scope

The underlying frame is the **entire** nonzero finite Boolean power set. The semantics are classical two-valued Kripke event semantics: for \(U\subseteq W_n\), \(\Box U=\{v:R(v)\subseteq U\}\) and \(\Diamond U=\{v:R(v)\cap U\ne\varnothing\}\). Words contain only the two unary modal operators, with no Boolean connective inserted between modalities. Their arguments may be arbitrary events, not merely Boolean values of single atomic formulas.

For an event \(U\), define its support and guaranteed support
\[
 S(U)=\bigcup_{v\in U}v,\qquad T(U)=[n]\setminus\bigcup_{v\in W_n\setminus U}v.
\]
The union of an empty family is empty. Notice that \(i\in T(U)\) means *all* nonempty worlds containing \(i\) belong to \(U\). All formula identities below quantify over every event \(U\subseteq W_n\) and all integers \(n\ge2\).

## Proof

### 1. Exact support descriptions

The world \(v\) has a successor inside \(U\) precisely when one of its atoms occurs in some member of \(U\). Thus
\[
 \Diamond U=H_{S(U)}.
\]
A world \(v\) has **all** successors in \(U\) exactly when no excluded world contains any atom of \(v\), or equivalently \(v\subseteq T(U)\). Therefore
\[
 \Box U=D_{T(U)}.
\]
For \(A\subseteq[n]\) we use the identities
\[
 S(D_A)=A,\qquad T(H_A)=A,
\]
where the first follows from the singleton worlds and the second follows from the fact that an atom belongs to every excluded-world complement precisely when it lies in \(A\). Also, \(H_A=W_n\) exactly when \(A=[n]\), and \(D_A=\varnothing\) exactly when \(A=\varnothing\). These elementary identities give the following complete evaluation table (write \(S=S(U)\), \(T=T(U)\)):

| Word | Value on \(U\) |
| --- | --- |
| \(\mathrm{id}\) | \(U\) |
| \(\Box\) | \(D_T\) |
| \(\Diamond\) | \(H_S\) |
| \(\Box^2\) | \(W_n\) if \(U=W_n\); otherwise \(\varnothing\) |
| \(\Box\Diamond\) | \(D_S\) |
| \(\Diamond\Box\) | \(H_T\) |
| \(\Diamond^2\) | \(W_n\) if \(U\ne\varnothing\); otherwise \(\varnothing\) |
| \(\Box^2\Diamond\) | \(W_n\) if \(S=[n]\); otherwise \(\varnothing\) |
| \(\Diamond^2\Box\) | \(W_n\) if \(T\ne\varnothing\); otherwise \(\varnothing\) |

For example \(\Box\Diamond U=D_S\), since a world is necessary relative to the hitting family \(H_S\) exactly if all of its atoms belong to \(S\). For \(\Box^2U\), a proper event excludes some world \(v\), so the full world \([n]\) is not in \(\Box U\); consequently every state has an excluded successor in \(\Box U\) and \(\Box^2U=\varnothing\). The other table entries follow by the same support calculus.

### 2. Closure and nine distinct operators

Here is the full prefix transition table, where \(B\) denotes prefixing by \(\Box\) and \(D\) denotes prefixing by \(\Diamond\). Each entry follows by substituting the preceding evaluation table; hence all longer words reduce to one of the nine normal forms.

| Existing word | Prefix \(B\) | Prefix \(D\) |
| --- | --- | --- |
| \(\mathrm{id}\) | \(B\) | \(D\) |
| \(B\) | \(BB\) | \(DB\) |
| \(D\) | \(BD\) | \(DD\) |
| \(BB\) | \(BB\) | \(BB\) |
| \(BD\) | \(BBD\) | \(D\) |
| \(DB\) | \(B\) | \(DDB\) |
| \(DD\) | \(DD\) | \(DD\) |
| \(BBD\) | \(BBD\) | \(BBD\) |
| \(DDB\) | \(DDB\) | \(DDB\) |

To prove minimality for \(n=2\), enumerate the three worlds as \(\{1\},\{2\},\{1,2\}\). Use three test events with binary incidence masks \(1,3,5\) respectively. In the displayed order of the nine normal forms, their output-mask triples are
\[
 (1,3,5),\ (0,0,1),\ (5,7,7),\ (0,0,0),\ (1,7,7),\
 (0,0,5),\ (7,7,7),\ (0,7,7),\ (0,0,7).
\]
All nine triples are distinct.

For \(n>2\), partition \([n]\) into two nonempty parts \(A_1,A_2\). Sending \(v\in W_n\) to the nonempty set \(\{i:v\cap A_i\ne\varnothing\}\in W_2\) is a surjective bounded morphism of compatibility frames. Indeed, intersecting worlds have intersecting images; conversely, given a desired target neighbor of the image of \(v\), select an atom of \(v\) in one common part and arbitrary atoms from the other required parts to construct a preimage neighbor. Both modalities therefore commute with inverse image. Since inverse image is injective on events, all nine operations that differ for \(n=2\) remain distinct for every larger \(n\).

### 3. Observation spectrum and exact fibers

The support \(S(U)\) and the guaranteed support \(T(U)\) satisfy the dichotomy
\[
 T(U)\ne\varnothing\ \Longrightarrow\ S(U)=[n].
\]
Indeed, for \(i\in T(U)\), the full world \([n]\), which contains \(i\), must lie in \(U\). Hence only the two families of joint observations in the Finding are possible.

Conversely, if \(S\subsetneq[n]\), the event consisting of singleton worlds \(\{i\}\), \(i\in S\), has support \(S\) and empty guaranteed support; this includes the empty event. If \(T\ne\varnothing\), the event \(H_T\) has guaranteed support \(T\) and full support. Finally, for \(n\ge2\), the event \(\{[n]\}\) has full support and empty guaranteed support. Hence every listed pair is realized. The two \(2^n\)-member families meet only at \((\varnothing,W_n)\), proving the cardinality \(2^{n+1}-1\).

For fixed proper \(S\), an event of support \(S\) is exactly a subfamily of the nonempty subsets of \(S\) whose union equals \(S\); inclusion-exclusion gives \(F(|S|)\) choices. For fixed nonempty \(T\), the complement \(W_n\setminus U\) is exactly such a covering family of \([n]\setminus T\), giving \(F(n-|T|)\) choices. The remaining events have full support and empty guaranteed support; subtract from the total \(F(n)\) full-support events the disjoint classes with \(|T|\ge1\) to get the stated shared-fiber formula.

This completes the normal-form, spectrum, and multiplicity proofs for every \(n\ge2\).

## Verification

The accompanying standalone Python 3 checker `verify_modal_word_monoid.py` evaluates the Kripke modalities directly from the compatibility adjacency relation, independently of the symbolic closed forms. It exhaustively enumerates every event for \(n=1,2,3,4\), verifies all nine formulas, checks the prefix table, computes all joint-observation fibers, and compares their cardinalities to inclusion-exclusion.

| Atoms | Events checked | Distinct operations | Joint observations | \(F(n)\) | Shared-fiber size |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 2 | 1 | 2 | 1 | 0 |
| 2 | 8 | 9 | 7 | 5 | 2 |
| 3 | 128 | 9 | 15 | 109 | 90 |
| 4 | 32,768 | 9 | 31 | 32,297 | 31,826 |

The \(n=1\) row is an explicitly excluded boundary case: the frame has only one reflexive world, so its necessity and possibility maps are identity. Finite testing is corroboration; the arbitrary-size result follows from the proof above.

## Relationship to prior work

Jockwich, Tarafder and Venturi (2026) introduced the Boolean co-consistency frame in their internal modal logic of forcing and studied its validity logic, representation, and finite hierarchy. This result uses precisely their nonzero finite Boolean frame, but addresses the different quantitative questions of pure-modal composition normal forms and joint observation fibers. The paper's treatment of arbitrary translated formulas, rather than just translated atomic formulas, is essential here: with the standard coordinate translation, finite Boolean combinations of atomic formulas define every event. This definability mechanism was also established in prior work on the strict finite hierarchy; it is not claimed as new here.

The earlier public result *Every finite stage of the internal forcing logic hierarchy is strict* determines the sharp domatic obstruction for bounded-morphic complete quotients and gives coordinate formulas for arbitrary fiber valuations. It does **not** give a normal-form monoid or exact two-modality event-fiber spectrum. The classical covering numbers \(F(s)\) themselves already appear as OEIS A003465; their use as exact modal-observation multiplicities is the contribution here, not their discovery.

General facts about normal modal operators, duality, and composition are older. The specific nine-element transformation monoid and complete paired-fiber classification were not found in the inspected sources; bibliographic non-detection is not a proof of historical priority.

## Limitations

The result does not classify arbitrary induced subframes, incomplete finite Boolean algebras, infinite atom sets, modal formulas containing Boolean connectives between successive modal operators, or full modal equivalence classes under unrestricted syntax. The nine operations act on all events and represent pure nested-modal contexts only. For \(n=1\) only identity occurs. This work contains a proof and finite corroboration but no independent mathematical or historical-priority audit.

## References

1. Santiago Jockwich, Sourav Tarafder, Giorgio Venturi, *The Internal Modal Logic of Forcing*, arXiv:2607.25977, first version posted 28 July 2026. https://arxiv.org/abs/2607.25977
2. *Every finite stage of the internal forcing logic hierarchy is strict*, published mathematical research result, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-every-finite-stage-of-the-internal-forcing-logic-hierarchy-is-st--069a2c03aeb3
3. OEIS Foundation, A003465, *Number of ways to cover an n-set*, https://oeis.org/A003465; includes historical citations to C. G. Wagner, *Covers of finite sets* (1973).
4. Patrick Blackburn, Maarten de Rijke, Yde Venema, *Modal Logic*, Cambridge University Press, 2001 (general background on Kripke semantics and bounded morphisms).
