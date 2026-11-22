# Scientific review — Exact multi-deletion subcodes of repeated message blocks

## Correctness — PASS
All definitions, integer constraints, and the exactly-\(t\)-deletion semantics are explicit. The critical lemma counts marked message blocks in a matched subsequence. At most \(t\) blocks contain deleted symbols on the source side; at most \(t\) further blocks straddle deleted symbols on the other side. A clean whole block exists for \(r\ge2t+1\), showing exact cyclic alignment, with signed shift no greater than \(t\). The converse uses a common contiguous overlap. This produces disjoint powers of cycles, from which gap counting and standard primitive-necklace Möbius inversion yield the exact capacity and count of all optimizers. A standalone checker exhaustively compares deletion-descendant sets, and for small universes enumerates all independent sets; its successful finite tests complement, rather than replace, the proof. No unproved infinite inference is drawn from the code.

## Originality — PASS (qualified)
Actual comparisons considered arbitrary deletion-shadow frameworks (Sloane 2002), general reconstruction through insertion/deletion (Sala et al. 2016), the cyclic permutation-phase overlap law, and the disjoint-alphabet conjugate-power maximal-subsequence law. The nearest earlier result treats one insertion in doubled blocks, and is not the present \(t\ge2\) deletion theorem after multiple complete block repeats. None of the accessible results states a complete arbitrary-message confusability criterion together with a classification and enumeration of all optimal restricted subcodes. Earlier unindexed coverage remains possible. A related 2010 repetition-error article was read only at abstract level due full-text access limitations; that model locally repeats symbols rather than deleting arbitrary symbols from repeated entire blocks.

## Mathematical value — PASS
Arbitrary-symbol deletion after deterministic whole-message replication is a natural synchronization-channel model. The exact rotation graph exposes why repeated blocks cannot eliminate cyclic-phase ambiguity, quantifies the maximal code size at every block length, counts every optimum, and proves the asymptotic rate loss \(1/(t+1)\). The claim does not aspire to determine unrestricted error-correcting codes or the minimal necessary repeat factor.

## Scope and limitations
The clean-block proof assumes \(q\ge2\), \(m\ge1\), \(t\ge2\), and \(r\ge2t+1\); the output is a linear subsequence of exactly \(rm-t\) symbols. The finite verifier checks small cases only. Historical priority remains qualified and independent review is outstanding.

Self-review: passed. Independent audit: not yet performed.
