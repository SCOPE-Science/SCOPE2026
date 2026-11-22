# Self-review

## Correctness — PASS

The single claim is the exact universal norm \(H_{n,k}(\varepsilon)\), its fundamental temporal period and initial time profile. The free-space operator norm equals the Lipschitz constant by normalized molecules. A permutation's action on unordered pairs has precisely the stated allowable periods. The complementary forward path of length \(\ell-(k\bmod\ell)\) bounds the \(k\)-step distance expansion; division by the initial distance (at least one) and the diameter bound (at most two) yields the upper envelope. An explicit assignment of distances along a maximizing pair orbit, with all other distances equal to one, is a genuine metric and attains equality at every \(n\ge3\), \(k\ge0\), and \(\varepsilon\ge0\). The residue zero set establishes the least positive temporal period, and a two-case comparison proves the initial linear profile. For two points only one unordered pair exists. A standard-library finite checker returned `MULTISTEP_FREE_PERMUTATION_DIAGNOSTIC_OK 5536379`; it is not the infinite proof.

## Originality — PASS (literature-qualified)

The most decisive comparator is Kadets–Zavarzina, *Plastic pairs of metric spaces* (2023), Section 2.2, Theorems 2.6–2.7 and Lemma 2.5 (https://arxiv.org/abs/2301.06589): the maximal pair-orbit length and the sharp **single-step** defect modulus are previously known. Those results are credited. The current theorem fixes a defect budget for \(f\) yet optimizes every \(k\)-th induced operator norm and classifies its full time-periodic envelope. Applying the published one-step result to \(f^k\) generally gives a weaker bound, because the contraction defect of \(f^k\) is not the original one-step defect. No checked comparator establishes the exact residue profile, the sharp constructions for every time, or the fundamental \(\operatorname{lcm}(1,\ldots,n)\) envelope period. Duzer's 2026 compact plasticity theorem is qualitative, and Cúth–Doucha–Titkos and Cobollo–Peris give different isometric/dynamical statements. Searches and relevant research-record comparison cannot exclude unpublished or differently indexed equivalent work.

## Mathematical value — PASS

This supplies a complete, exact time-dependent operator-norm stability invariant of finite Lipschitz-free permutation dynamics under a natural additive one-step near-rigidity constraint. Its time profile has an unexpectedly large **least** period equal to the least common multiple of all cardinalities from one to \(n\), although any fixed permutation can have a much shorter period, and its first half-cycle worst-case amplification decays with a sharp linear law. Every bound is attained by explicit normalized metrics. The theorem quantifies how one-step almost-noncontraction does (and does not) propagate through all powers; it is not a mere renaming of the already-known one-step result.

## Closest literature and limits

The sharp single-step plasticity theorem is credited to Kadets and Zavarzina (2023). Duzer (2026) treats the zero-defect rigidity phenomenon on compact quasi-metric spaces; Cúth, Doucha and Titkos (2024) classify isometries of Lipschitz-free spaces; Cobollo and Peris (2025) provide the induced-operator norm identity in a dynamics context. The claim applies only to bijections of symmetric finite metrics with off-diagonal distances in \([1,2]\). It is not asserted for arbitrary quasi-metrics, noninjective maps, or general Banach operators. Unindexed exact multistep results remain an originality risk.

Self-review: passed. Independent audit: not yet performed.
