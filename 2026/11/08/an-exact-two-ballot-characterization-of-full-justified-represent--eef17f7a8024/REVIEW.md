# Scientific review: exact two-ballot FJR+ characterization

## Correctness — PASS

The theorem uses Teh's nonnegative fractional-violation system, including the elected-candidate cap in (C5). Identical voter types can be averaged without changing the violation ratio. A deficient type that approves no unelected candidate cannot participate; a participating type alone costs exactly \(\ell\) candidate weight per unit voter weight. If both participate, an unelected common candidate yields an EJR+ violation. Otherwise the only potential weight sharing occurs on \(r\) common *elected* candidates, with savings at most \(r\min(s,t)\). The candidate-weight inequality is tight at all three extremal voter-weight ratios. Fractional-linearity on either side of equal type weights rules out an additional interior maximum. The supported-winner corollary follows by adding the two strict utility deficits, and Pareto optimality disposes of unsupported winners by a swap. The example's FJR and EJR+ inequalities and its explicit level-four fractional witness are checked directly.

Reproducibility: `python verify.py` with the stated dependency compared the closed formula against the published FJR+ LP on 3,852 exhaustively generated small two-type cases and 1,653 deterministic pseudorandom larger cases. It also checked the strictness example against literal FJR/EJR+ predicates. The infinite theorem rests on the proof, not these computations.

## Originality — PASS, with limits

The nearest primary paper is Teh (arXiv:2608.11500v1, August 11, 2026). Its Definition 3.1 introduces the fractional system, Proposition 3.8 shows strictness against FJR plus EJR+ for unrestricted ballots, and Proposition 3.9 reduces FJR+ to lower quota for *disjoint* party lists. This result instead gives a necessary-and-sufficient explicit test for two possibly overlapping ballot types, plus equivalence with EJR+ for supported/Pareto-optimal committees and a two-type counterexample when support fails. Dong and Peters (arXiv:2605.04612v1) axiomatically characterize EJR+ and separately analyze FJR; their inspected definitions and results do not establish the fractional two-type theorem. A related existence theorem for two ballot types concerns JUQ, JNQ and EJR+, not the FJR+ decision problem. Searches of those sources, the accessible research database and existing related records did not identify a covering statement. Search incompleteness and unindexed equivalent results remain possible.

## Mathematical value — PASS

The new FJR+ axiom was introduced as a computably verifiable strengthening of two important representation conditions. It matters to know when the added fractional test is mathematically indispensable, rather than running a linear program by default. The exact two-type formula provides such a characterization on a basic structured preference domain that allows overlapping approvals, distinguishes the behavior of supported versus unsupported winners, and explains why Pareto efficiency eliminates the extra FJR+ obstruction there. The zero-support counterexample is not offered as a stand-alone defect check: it marks a necessary boundary of the structural equivalence.

## Remaining limitations

The characterization is for unweighted binary approval utilities, Hare quotas, a fixed-size integral committee, and at most two ballot types. It does not cover more ballot types, generalized project costs, or weighted/FJR+ variants. The reproducibility code uses floating-point linear-program optimization for small samples; the analytical inequalities and exact rational counterexample provide the proof. The literature review is not a certification of global novelty, and no independent audit was performed.

Self-review: passed. Independent audit: not yet performed.
