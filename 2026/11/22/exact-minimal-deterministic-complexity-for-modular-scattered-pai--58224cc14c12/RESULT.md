# Exact minimal deterministic complexity for modular scattered pairs under a forbidden zero-run transition

## Finding
For every integer \(r\ge2\) and modulus \(m\ge2\), let
\[
L_{r,m}=\{w\in\{0,1\}^*:0^r1\text{ is not a contiguous factor of }w,\ \binom{w}{01}\equiv0\pmod m\}.
\]
Here \(\binom{w}{01}\) is the number of ordered index pairs spelling the *scattered* pattern \(01\). The minimum number of states in a **complete deterministic finite automaton** for this language is exactly
\[
\boxed{\operatorname{sc}(L_{r,m})=rm^2+2.}
\]
More precisely, its right-language classes consist of exactly \(rm^2\) distinct active modular/run signatures, one accepting terminal zero-run class, and one rejecting empty-right-language class. At the sharp boundary \(r=1\), avoidance of the factor \(01\) forces \(L_{1,m}=1^*0^*\), whose minimal complete automaton has three states for every \(m\ge2\). These statements concern deterministic *complete* recognition, not partial or Wheeler automata.

## Assumptions and scope
Words are finite over exactly \(\{0,1\}\), including the empty word. A *contiguous factor* is a consecutive block; a *scattered subsequence occurrence* is an increasing choice of positions. Hence \(\binom{w}{01}\) counts pairs \(i<j\) with \(w_i=0,w_j=1\), with multiplicity. Only a final congruence check to residue zero is imposed. All modulus arithmetic below occurs in \(\mathbb Z/m\mathbb Z\), and a rejecting sink is included in every complete automaton. The assumptions \(r,m\ge2\) are necessary for the displayed polynomial formula; the case \(r=1\) is stated separately.

## Proof
**A natural complete recognizing automaton.** Before any forbidden factor appears, track the triple \((a,c,j)\), where \(a\) is the number of zeros modulo \(m\), \(c\) is the number of scattered \(01\) occurrences modulo \(m\), and \(j\) is the number of trailing zeros truncated to \(r\). The initial triple is \((0,0,0)\). The transitions are
\[
\begin{aligned}
(a,c,j)\xrightarrow{0}&(a+1,c,\min(r,j+1)),\\
(a,c,j)\xrightarrow{1}&(a,c+a,0)\quad(j<r),\\
(a,c,r)\xrightarrow{1}&\bot,
\end{aligned}
\]
where \(\bot\) is an absorbing rejecting sink. All non-sink triples with \(c=0\) accept. The transitions follow directly because appending a \(1\) creates one new scattered \(01\) for each earlier zero. This automaton recognizes precisely \(L_{r,m}\).

**Exact quotient collapse at the terminal run.** From \((a,c,r)\), any suffix containing a \(1\) must fail, because the next \(1\) would complete the forbidden factor. A suffix of zeros changes neither \(c\) nor the terminal-run condition. Thus all \((a,0,r)\) have the same right language \(0^*\), while all \((a,c,r)\) with \(c\ne0\) have the empty right language, equal to \(\bot\). Collapsing these gives the upper bound of \(rm^2+2\) states (for \(r\ge2\)).

**Reachability of every active triple.** Fix \(0\le j<r\) and residues \(a,c\). Choose any positive integer \(k\equiv a-j\pmod m\), and then a nonnegative integer \(t\equiv c-k(k+1)/2\pmod m\). The word
\[
W=0\,1^{t+1}(01)^{k-1}0^j
\]
contains \(k+j\) zeros, has trailing-zero length exactly \(j\), and avoids \(0^r1\): every zero-run preceding a one has length one. Its scattered \(01\) count is exactly \(t+k(k+1)/2\), since the respective one-blocks see \(1,2,\ldots,k\) previous zeros. Therefore \(W\) reaches \((a,c,j)\). The terminal accepting class is reached by \(0^r\), and the rejecting class by \(0^r1\).

**Separation of different modular counters.** Fix any active triple \((a,c,j)\), with \(j<r\). For arbitrary positive integers \(b,d\), the continuation \(1^b0\,1^d\) remains admissible, since the newly introduced internal zero-run has length one and \(r\ge2\). The final scattered-pair residue is
\[
F_{a,c}(b,d)=c+ab+(a+1)d\pmod m.
\]
The coefficient pair \((a,a+1)\) generates the additive group \(\mathbb Z/m\mathbb Z\), so \(F_{a,c}\) assumes every residue as \((b,d)\) vary, even when both exponents are required positive. In particular, its zero fibre is nonempty.

We use the following elementary affine-fibre fact: if two surjective affine maps \(F,G:(\mathbb Z/m\mathbb Z)^2\to\mathbb Z/m\mathbb Z\) have identical nonempty zero fibres, then \(G=uF\) for some multiplicative unit \(u\pmod m\). Indeed, translating by any point in the common zero fibre makes the maps homomorphisms with the same kernel; each induces an isomorphism from the common cyclic quotient to \(\mathbb Z/m\mathbb Z\), and the induced automorphism multiplies by a unit. Equality of acceptance on all suffixes \(1^b0\,1^d\) thus forces equality of these affine zero fibres. Comparing the difference between the two linear coefficients gives \(1=u\cdot1\), hence \(u=1\). Comparing first coefficients and constants then yields \(a=a'\) and \(c=c'\). Consequently any two active triples having different \((a,c)\) are Myhill–Nerode distinguishable, regardless of their run states.

**Separation of different active run states.** Suppose \((a,c,j)\) and \((a,c,j')\) have identical counters with \(j<j'<r\). Put \(h=r-j'\ge1\). The suffix
\[
0^h1^b0\,1^d
\]
forces the state with run length \(j'\) to reject, because its first \(1\) completes a run of \(r\) zeros. From run length \(j\), the same suffix is admissible: \(j+h<r\), and the remaining new zero-run has length one. Its final count is \(c+(a+h)b+(a+h+1)d\pmod m\). Since the two coefficients are consecutive, positive integers \(b,d\) can be chosen to make the residue zero. This suffix accepts from the shorter run state and rejects from the longer run state.

**Terminal classes and exact minimum.** Every active triple has an accepted continuation containing a \(1\), by the preceding surjectivity argument. Hence no active triple is equivalent to the terminal right language \(0^*\); nor is it equivalent to the rejecting empty right language. The terminal accepting class and rejecting class differ already on the empty suffix. Every one of the \(rm^2+2\) claimed classes is reachable, and all are pairwise distinguished, proving minimality by Myhill–Nerode. For \(r=1\), avoiding contiguous \(01\) is equivalent to membership in \(1^*0^*\), which has the familiar three inequivalent prefix states (before the first zero; after a zero; rejected). \(\square\)

## Verification
The standalone standard-library `verify.py` constructs the reachable product DFA from its transitions, independently minimizes it using partition refinement, and compares recognition to direct scattered-pair counting and substring exclusion. Executing `python verify.py` produced:

```text
PASS 117 independent reachable-DFA minimizations
PASS 51175 direct word-membership comparisons
All m=2..14, r=1..9 attain the claimed formula.
```

The 117 parameter pairs cover every \(1\le r\le9\) and \(2\le m\le14\). The direct comparisons independently enumerate all binary words through length ten for \(1\le r\le5\) and \(2\le m\le6\). These finite tests corroborate but cannot replace the uniform reachability and distinguishing-suffix proof.

## Relationship to prior work
Lejeune, Rigo and Rosenfeld (2020) study equality classes of ordinary scattered-subsequence counts, with links to nilpotent groups; they do not supply this modular constrained-language state count in the inspected text. Renard, Rigo and Whiteland (2024) treat q-deformed binomial counts and recognition by finite groups; a general modular recognizability statement alone does not prove a minimum state count after intersecting with a forbidden contiguous-factor language. The published exact state-complexity result for unrestricted modular scattered \(0^d1\) counting concerns the *counted pattern*, not a simultaneously forbidden contiguous \(0^r1\) pattern. A published exact prefix-sorting result for avoiding contiguous \(0^r1\) concerns the unconstrained avoidance language and trim partial/Wheeler state complexities, not the modular scattered-pair condition. Exact-integer scattered-pair-count languages also differ from this modular residue constraint. The present contribution is the sharp state count and explicit quotient collapse for their interaction.

## Limitations
The formula concerns only binary scattered \(01\) counts modulo a common \(m\), a single forbidden contiguous factor \(0^r1\), and a complete deterministic automaton. It does not give a full classification for arbitrary forbidden patterns, multiple modular counters, or nondeterministic automata. The comparison to literature and indexed findings is bounded and cannot certify priority against unindexed equivalent work; relevant general texts may contain unnoticed special cases. The verification script is finite evidence rather than a machine proof of all parameters. Independent mathematical validation has not been performed.

## References
- M. Lejeune, M. Rigo and M. Rosenfeld, *On the binomial equivalence classes of finite words*, arXiv:2001.11732, first publicly posted 2020-01-31, https://arxiv.org/abs/2001.11732 .
- A. Renard, M. Rigo and M. A. Whiteland, *Introducing q-deformed binomial coefficients of words*, arXiv:2402.05838, first publicly posted 2024-02-08, https://arxiv.org/abs/2402.05838 .
- *Exact prefix-sorting state cost for avoiding a binary zero-run factor*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-prefix-sorting-state-cost-for-avoiding-a-binary-zero-run-f--294ac7d4ffb0 .
- *Exact state complexity of modular scattered zero-power–one counts*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-state-complexity-of-modular-scattered-zero-power-one-count--9df1828ce330 .
- *Prime-power staircases in modular scattered-subsequence automata*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-prime-power-staircases-in-modular-scattered-subsequence-automata--b8dbc861b2e5 .
