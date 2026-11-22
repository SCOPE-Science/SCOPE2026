# Exact coset-visit Grundy law and sharp P-language state complexity for finite-group word subtraction

## Finding
Let \(G\) be an arbitrary finite group, \(H\leq G\) a subgroup, and let the alphabet consist of one symbol for every element of \(G\). A legal move deletes a nonempty suffix whose ordered product belongs to \(H\). For a word \(w=g_1\cdots g_n\), put \(p_0=e\) and \(p_j=g_1\cdots g_j\) for \(1\le j\le n\). The Sprague--Grundy value is exactly
\[
\gamma(w)=\#\{0\le j<n:p_jH=p_nH\}.
\]
In particular, the Grundy value is the number of previous visits to the *left* coset occupied by the complete word. With \(q=|G|\), \(h=|H|\), and independently uniformly sampled letters, every \(n\ge0\) and \(0\le k\le n\) satisfy
\[
\#\{w\in G^n:\gamma(w)=k\}=\binom nk h^k(q-h)^{n-k},
\]
with the usual empty-word convention. Hence \(\gamma(W_n)\) is binomial with parameters \(n\) and \(h/q\), and the exact P-position count is \((q-h)^n\) for \(n\ge1\).

If, in addition, \(H\trianglelefteq G\), then the P-position language \(\{w:\gamma(w)=0\}\) has a minimal complete deterministic finite automaton with *exactly* \(2^{[G:H]}\) states. The bound is attained for every normal subgroup, including the trivial and whole-group boundary cases. The subgroup rule therefore gives a fully explicit family with exponential P-language state complexity despite its elementary quotient presentation.

## Assumptions and scope
Words are finite sequences over the *full labeled alphabet* \(\Sigma=G\); every group element is a distinct input letter, including the identity. Products use the order of the word. The game is normal-play impartial word subtraction: from \(us\) one may remove the suffix \(s\ne\varepsilon\) precisely if its product lies in \(H\). All games terminate because the word shortens. A P-position is a word of Grundy value zero. The binomial law and coset-visit identity hold for any subgroup, including nonnormal subgroups. Normality is required only for the quotient-group automaton statement. State complexity means the number of states in the minimal complete DFA, including the initial state, for all finite lengths simultaneously.

## Proof
**1. The legal predecessors are exactly earlier occurrences of one coset.** A move from the word of length \(n\) to its prefix of length \(j<n\) is legal exactly when \(p_j^{-1}p_n\in H\). This is equivalent to \(p_jH=p_nH\). The cosets in this sentence are *left cosets* \(gH\), which remain meaningful when \(H\) is not normal.

**2. Grundy induction.** Order every visit to a fixed left coset by prefix length, starting at its first visit. The empty prefix is the first visit to \(H\). Suppose the current prefix is the \((t+1)\)-st visit to its coset, meaning there are precisely \(t\) earlier visits. Every legal option is precisely one of these \(t\) earlier prefixes, by Step 1. By induction on prefix length, their Grundy values are exactly \(0,1,\ldots,t-1\), each once. Their minimum excluded nonnegative integer is \(t\). The first visit has no legal option and value zero. This proves the claimed formula for every word and every subgroup.

**3. The exact probability law.** For uniformly independent input letters, the map from \((g_1,\ldots,g_n)\) to their successive cumulative products \((p_1,\ldots,p_n)\) is a bijection on \(G^n\): recover \(g_1=p_1\) and \(g_i=p_{i-1}^{-1}p_i\). Thus the \(n\) nonempty prefix products, and their left cosets, are independent uniform random variables. Conditional on the last coset, its matches among the \(n-1\) earlier *nonempty* prefixes have binomial law \(\mathrm{Bin}(n-1,h/q)\), and this count has the same distribution for every last coset, so it is independent of the last coset. The additional match with the empty prefix occurs exactly when the last coset is \(H\), an independent Bernoulli variable of parameter \(h/q\). Adding yields \(\mathrm{Bin}(n,h/q)\). Multiplication by \(q^n\) gives the stated exact integer counts. At \(n=0\), the empty word has Grundy zero.

**4. Construction of the P-language DFA when \(H\) is normal.** Write \(Q=G/H\) with identity \(1\) and order \(r=[G:H]\). At a word with current quotient prefix product \(x\), let \(V\subseteq Q\) be the set of all quotient prefix products (including the empty and current prefixes), and normalize to \(T=x^{-1}V\), so \(1\in T\). Let \(f\in\{0,1\}\) indicate whether the current quotient state has not appeared at an earlier prefix (\(f=1\) exactly for a P-position). The initial state is \((\{1\},1)\). Reading a letter of quotient value \(y\in Q\) sends
\[
(T,f)\longmapsto\bigl(y^{-1}T\cup\{1\},\;\mathbf 1_{\{y\notin T\}}\bigr).
\]
Accept the states with \(f=1\). This proves recognition by at most \(2\cdot2^{r-1}=2^r\) states.

**5. Reachability of every DFA state.** Fix any \(T\subseteq Q\) containing \(1\). If \(T=\{1\}\), the empty word reaches \((T,1)\). Otherwise choose \(t\in T\setminus\{1\}\) and put \(x=t^{-1}\). Since \(1=xt\in xT\) and \(x\in xT\), first traverse the elements of \(xT\setminus\{x\}\) in any order starting at \(1\), then visit \(x\) for the first time. This is possible because every element of \(Q\) is represented by an input letter: any desired transition from state \(a\) to state \(b\) uses an input with quotient \(a^{-1}b\). The final normalized visited set is \(T\), and freshness is one. Appending a letter in \(H\), whose quotient is \(1\), preserves \(T\) but makes freshness zero. Therefore every pair \((T,f)\) is reachable.

**6. Pairwise distinguishability.** Different freshness bits are distinguished by the empty continuation because exactly freshness-one states accept. If two states have the same freshness bit but different normalized sets \(T\ne U\), choose \(y\in T\triangle U\). A one-letter continuation whose quotient is \(y\) makes the next freshness bits unequal, so the continuation distinguishes the states. Every one of the \(2^r\) reachable states has a different right language. The DFA is minimal.

For \(H=G\), this construction has two states, accepting only the empty word; for \(H=\{e\}\), it has \(2^{|G|}\) states.

## Verification
`check_grundy.py` directly computes the mex of legal game options, independently obtains prefix-coset visits, and compares the full exact binomial counts. It checks cyclic groups of orders three and four (including a nontrivial proper subgroup) through length seven and the nonnormal transposition subgroup of \(S_3\) through length five. It does not assume the theorem when generating the legal moves. `check_minimal_dfa.py` builds the claimed transition system, performs reachability search and independent Moore equivalence refinement, and checks the one-letter distinguishing condition. It covers all cyclic quotient groups of orders one through six, the Klein four-group, and \(S_3\). Both tests passed. These finite checks support but do not replace the all-parameter proof above.

## Relationship to prior work
Inoue and Inazu (2026), *Word Subtraction Games*, establishes regularity of the P-position language for regular subtraction sets and gives general automata for fixed Grundy levels (Section 3.4, Corollary 3.10). The paper raises structural group-language questions in Problem 3.1. These general results do not assert a coset-visit Grundy identity, a binomial law for all values, or sharp \(2^{[G:H]}\) state complexity. The earlier truncation-game analysis by Hetyei (2009/2010) studies strongly Bernoulli type truncations and enumerations of kernel positions; its Section 2 states that extension to arbitrary Bernoulli-type games is open in that setting. The present subgroup rule need not satisfy the required prefix-closure hypothesis, and the cited decomposition theorem does not give the claimed finite-group language-state bound.

## Limitations
The exact minimal-state formula assumes the full group alphabet and normality of \(H\). With restricted generating alphabets or nonnormal \(H\), the coset Grundy law remains valid, but the stated quotient-automaton minimality argument does not directly apply. The distribution assumes independent uniform letters; biased input need not be binomial. No independent audit has been performed. No claim of uniqueness among unindexed or inaccessible literature is made.

## References
1. Y. Inoue and H. Inazu, *Word Subtraction Games*, arXiv:2611.09157v1, first publicly posted November 6, 2026, https://arxiv.org/html/2611.09157v1 .
2. G. Hetyei, *Enumeration by kernel positions for strongly Bernoulli type truncation games on words*, arXiv:0912.0573v1, 2009, https://arxiv.org/html/0912.0573v1 .
