# Independent mathematical audit

## correctness

PASS

Reflexivity and transitivity give R_a R_a=R_a, so consecutive repeats can be removed from each word. A subsequence path is a path for any containing word by inserting reflexive steps. Every normalized word contains a minimal normalized word, so satisfying the minimal conjunction is equivalent to satisfying the original under every valuation; retaining a selected endpoint per minimal word proves the upper bound on arbitrary frames. For the lower bound, take the prefix trie of those minimal words. There are no consecutive same-label edges on a branch, so the reflexive transitive closure for a given label adds only loops. A walk to a marked leaf must take the unique forward branch in order with optional stays, and exists exactly when the leaf word is a subsequence of the query word. The minimal antichain therefore forces every originally marked leaf to be retained. This concerns subvaluations of the original marked set, not arbitrary relocations of marks. The empty word produces the singleton antichain and one-world witness. For q>=2 the full reduced depth-d layer has q(q-1)^(d-1) members. Every nonempty shorter reduced word has a continuation to that layer; prefix-incomparable words have disjoint continuation sets. The full layer is a subsequence antichain, so the bound is sharp, while for q=1 the only reduced possibilities are the letter and the comparable empty word. The q=2 plateau and q=3 exponential case follow. Independent replay: python3 /workspace/checks/frozen_replay.py 1; exhausts the 29 preorders on three labeled worlds, their 841 ordered pairs, all starts and valuations for five representative conjunctions, plus two exact larger chain-pair constructions for rank-two long-word examples. These checks are bounded; the proof supplies the sharp result on all frames.

## originality

PASS

The supported distinct result is the exact least retention budget and its sharp alphabet/depth extremum for this restricted family. Standard S4 reductions, relational-word techniques and existence of uniform finite budgets are not the originality claim.

## value

PASS

The least budget is a natural quantitative version of strong continuity, and the trie makes it an exact finite obstruction as well as an upper bound. The plateau for two independent modalities despite arbitrary nesting, versus depth-exponential worst cases for at least three, is a meaningful structural distinction rather than an isolated small-instance count. No generalization to universal modalities or interacting frame relations is assumed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
