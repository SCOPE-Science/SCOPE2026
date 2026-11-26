# Independent mathematical audit

## correctness

PASS

In the bilateral shift an A=11 bond followed by a consecutive B=00 bond bounds exactly 11(01)^j00, of gap 2(j+1). The local tables give A motion left and B motion right, with only separation-two B,A pairs deleted. Surviving defects preserve order: only B,A gaps shrink, and at the smallest possible gap their defects disappear rather than cross. For consecutive output A,B, their ordered ancestors bracket at least one consecutive input A,B transition, so the ancestral gap is at least 2(t+1) on X_t and the output gap at least 2(t+2). Conversely the Rule-226 reflected branch G moves A right and B left; there are no collisions on an output avoiding 1100, and the remaining gaps after G meet X_t's bound. The five-bit discrepancy table shows F(Gy)=y on that shift. Thus F(X_t)=X_{t+1}, including t=0, and induction gives every stage. Basis words are pairwise noncontaining because their only 11 and 00 are the terminal defects. Every finite avoiding word can be extended by a constant zero left tail and constant one right tail without creating an A-to-B defect pair. Therefore the avoiding-word languages are actual bilateral image languages, the basis is exactly minimal, and W_t is in Y_t but not Y_{t+1}, the first difference at length 2t+4. The independent bounded replay script independent_check.py checked the full four- and five-bit tables and 32 finite-block cases through t=4 (largest input block length 14); those checks supplement the all-time induction. The shipped verifier was inspected, not executed. No finite-ring or asynchronous generalization is asserted.

## originality

PASS

The distinct supported claim is the exact bilateral minimal forbidden basis at arbitrary finite t and the sharp first-loss clock. Previously stated t=1 reachability and inverse, and the separately recorded t=2 list, are credited and are not new. Accessible prior statements give local dynamics, individual-block preimages, or small-time languages, not the all-time two-inclusion classification. The main inaccessible process-graph source remains an explicit priority risk.

## value

PASS

The exact minimal bases for a standard number-conserving cellular automaton characterize all finite-time reachable words on the bilateral full shift, not just the entropy or an isolated early image. The new obstruction's sharp length at every step gives strict descent and quantifies what can be distinguished by a fixed observation window. The inverse construction is a finite-depth reachability method; neither the t=1 nor the t=2 computation alone supplies the invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
