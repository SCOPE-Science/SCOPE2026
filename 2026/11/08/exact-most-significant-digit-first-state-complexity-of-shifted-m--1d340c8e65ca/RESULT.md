# Exact most-significant-digit-first state complexity of shifted modular ruler sequences

## Finding

Fix integers \(b\ge2\), \(m\ge2\), and \(c\ge0\). Set \(d=c+1\) and define the \(b\)-adic valuation \(\nu_b(N)=\max\{e\ge0:b^e\mid N\}\) for every positive integer \(N\). Consider the automatic sequence
\[
R_{b,m,c}(n)=\nu_b(n+d)\bmod m,\qquad n\ge0.
\]
The input convention is **most-significant digit first**, allowing arbitrarily many leading zeros; output is produced at the end of a finite base-\(b\) digit string.

Define \(K=\min\{k\ge0:b^k\ge d\}\) and the strictly decreasing positive offsets
\[
q_j=\left\lceil\frac{d}{b^j}\right\rceil,\qquad 0\le j\le K,
\]
so \(q_K=1\). For \(K=0\), put \(H=0\); otherwise put
\[
H=1+\max_{0\le i<j\le K}\nu_b(q_i-q_j).
\]
In particular, \(H\le K\). Build the depth-\(H\) radix-\(b\) trie, **least-significant digit first**, of the residues \(-q_0,\ldots,-q_K\) modulo \(b^H\). Each active trie node has at least one marked descendant. For every missing child of an active node of depth \(h<H\), let \(r\) be its residue represented by its \(h+1\) low-order digits, \(0\le r<b^{h+1}\), and form the signature
\[
S_r=\bigl(\nu_b(r+q_j)\bmod m\bigr)_{j=0}^{K}.
\]
Let \(\mathcal S_{\rm off}\) be the set of those signatures (an empty set when \(H=0\)). For every \(0\le i\le K\) and \(0\le t<m\), define a leaf signature \(V_{i,t}\in\{0,\ldots,m-1\}^{K+1}\) by
\[
(V_{i,t})_j=
\begin{cases}
t,&j=i,\\
\nu_b(|q_i-q_j|)\bmod m,&j\ne i.
\end{cases}
\]
Then the **exact minimal complete DFAO state count** is
\[
\boxed{\operatorname{sc}^{\rm MSD}_{b,m}(c)=
\left|\mathcal S_{\rm off}\ \cup\ \{V_{i,t}:0\le i\le K,\ 0\le t<m\}\right|.}
\]
This is a finite *arithmetic formula*: it only uses the \(K+1\) offsets and a trie of depth at most \(K\), not a general DFA minimization. It yields an explicit minimal automaton and the all-shifts bound
\[
\operatorname{sc}^{\rm MSD}_{b,m}(c)
\le (K+1)\bigl(m+(b-1)K\bigr).
\]
In particular, for fixed \(b,m\) the complexity is \(O((\log(c+2))^2)\).

## Assumptions and scope

The sequence is indexed by nonnegative integers. Every finite word over digits \(\{0,\ldots,b-1\}\), including the empty word and words with leading zeros, encodes its usual base-\(b\) integer; the DFAO must return \(R_{b,m,c}\) for *all* these representations. A state is counted even when its output equals another state's output if their future output functions differ. The case \(d=1\) is included: \(K=H=0\) and the formula returns \(m\). No infinite or limiting digit representations are used.

## Proof

**1. Exact right-context invariants.** Let \(p\) be an already-read MSD-first prefix with numerical value \(n\). Append a suffix \(w\) of length \(\ell\) with integer value \(r\), where \(0\le r<b^\ell\). The resulting integer is \(b^\ell n+r\). If \(r+d\) is not divisible by \(b^\ell\), its valuation is less than \(\ell\), so
\[
\nu_b(b^\ell n+r+d)=\nu_b(r+d)
\]
is independent of \(n\). Otherwise the unique such \(r\) is \((-d)\bmod b^\ell\), and \(r+d=b^\ell q_\ell\). Then
\[
\nu_b(b^\ell n+r+d)=\ell+\nu_b(n+q_\ell).
\]
For \(\ell\ge K\), \(q_\ell=1=q_K\). Hence two prefixes have identical output for every continuation if and only if their vectors
\[
\Phi(n)=\bigl(\nu_b(n+q_j)\bmod m\bigr)_{j=0}^{K}
\]
are equal. Necessity is witnessed for each coordinate \(j\) by the length-\(j\) suffix encoding \((-d)\bmod b^j\), including the empty suffix when \(j=0\); sufficiency follows from the preceding dichotomy for every suffix. Thus the exact number of minimal MSD-first DFAO states is \(|\{\Phi(n):n\ge0\}|\), and all classes are reachable because every \(n\) has a finite digit representation.

**2. Distinct depth-\(H\) leaves.** The offsets \(q_0,\ldots,q_K\) strictly decrease until \(1\): if \(q_j>1\), then \(\lceil q_j/b\rceil<q_j\). For \(K>0\), every nonzero difference \(|q_i-q_j|\) is less than \(d\le b^K\), so \(\nu_b(|q_i-q_j|)<K\) and \(H\le K\). By the definition of \(H\), the residues \(-q_i\bmod b^H\) are pairwise distinct. When \(K=0\), the depth-zero trie has its single root and no missing children.

**3. Prefixes leaving the trie.** Given an integer \(n\ge0\) whose first \(H\) least significant digits differ from each marked residue, follow the residue digits until the first missing child, at depth \(h+1\), with recorded residue \(r\). For each \(j\), \(n+q_j\not\equiv0\pmod{b^{h+1}}\) while \(n\equiv r\pmod{b^{h+1}}\). Consequently \(\nu_b(n+q_j)=\nu_b(r+q_j)<h+1\), hence \(\Phi(n)=S_r\). Conversely every missing-child signature occurs at the integer \(n=r\). Therefore these prefixes yield exactly \(\mathcal S_{\rm off}\).

**4. Prefixes reaching a marked leaf.** Otherwise \(n\equiv -q_i\pmod{b^H}\) for a unique \(i\). For \(j\ne i\), write \(n+q_j=(n+q_i)+(q_j-q_i)\). The first summand is divisible by \(b^H\), while the second has valuation less than \(H\); therefore
\[
\nu_b(n+q_j)=\nu_b(|q_j-q_i|).
\]
The remaining coordinate \(\nu_b(n+q_i)\bmod m\) is arbitrary. For every residue \(t\in\{0,\ldots,m-1\}\), choose a sufficiently large integer \(e\ge H\) with \(e\equiv t\pmod m\) and \(b^e>q_i\); then \(n=b^e-q_i\ge0\) realizes \(V_{i,t}\). Thus the marked leaves yield exactly the stated leaf-signature family. When \(H=0\), there is only the single offset \(q_0=1\); the same witness realizes all \(m\) signatures.

**5. Completion and cost.** Every nonnegative integer either first enters a missing child or reaches one unique marked leaf. Steps 1–4 prove both inclusions in the displayed formula, with no unproved infinite enumeration. To construct the minimal DFAO, use these distinct signatures as states, initial state \(\Phi(0)\), output equal to the first signature coordinate, and digit-\(a\) transition \(\Phi(n)\mapsto\Phi(bn+a)\). Step 1 proves this transition is independent of the chosen representative \(n\). All states are reachable and pairwise right-distinguishable by Step 1. For the size bound, there are at most \((K+1)H\) active internal trie nodes (each depth has at most \(K+1\) nodes), and each has at most \(b-1\) missing children. Thus there are at most \((b-1)(K+1)H\) off-trie signatures and at most \(m(K+1)\) leaf signatures. Using \(H\le K\) proves the bound.

## Verification

The standalone `checker.py` implements the finite formula, constructs explicit integer witnesses for every signature, evaluates the original arithmetic sequence independently, discovers MSD-first transitions by breadth-first search of integer prefixes, and runs Moore partition refinement on the resulting complete DFAO. Run:

```
python3 checker.py
```

The check passed for all \(896\) parameter triples with \(2\le b\le5\), \(2\le m\le5\), and \(0\le c<56\): \(12{,}136\) formula-witness tests, \(107{,}520\) direct arithmetic evaluations, and \(896\) independent automaton-minimization comparisons. The argument above, not the sample, proves the unbounded theorem.

For a visible orientation distinction, the binary case with \(m=2\), \(c=10\) (so \(d=11\)) has \(9\) MSD-first states by this formula, while an independent least-significant-digit-first automaton computation gives \(8\) states. The digit direction is not cosmetic.

## Relationship to prior work

Moradi, Rampersad, and Shallit (arXiv:2512.10017, first released 2025-12-10) study state complexity of arithmetic subsequences and shifts, and exhibit general bounds and a fixed-addition relation-automaton formula. Their Theorem 5 concerns a **two-input addition relation**, not the single-output valuation-residue sequence; their Sections 4.2–4.3 study shifted Thue–Morse and powers-of-two indicators, not the simultaneous shifted valuation signatures here. Moradi, Popoli, Shallit, and Vukusic (arXiv:2603.18858, first released 2026-03-19) obtain strong shift bounds for the Fibonacci word under Zeckendorf representations, a different sequence and numeration system. Kosoy (arXiv:2607.17369, first released 2026-07-19) motivates RTL/LTR automaticity as distinct complexity measures; her learning bounds do not compute this minimal-state invariant. These works motivate the question but do not assert the displayed arithmetic trie classification.

## Limitations

This result treats deterministic finite automata with output for the shifted *modular valuation* word, not unrestricted integer-valued ruler sequences or other arithmetic translations. The formula is exact but involves a finite set cardinality; it is not a single elementary expression solely in \(b,m,c\). The quadratic logarithmic bound need not be sharp, and the theorem does not identify a globally optimal upper bound over all shifts at fixed \(b,m\). The result has undergone only self-review, not independent mathematical validation; historical priority beyond the inspected sources is not certified.

## References

- D. Moradi, N. Rampersad, J. Shallit, *Complexity of Linear Subsequences of \(k\)-Automatic Sequences*, arXiv:2512.10017v5 (initial public version 2025-12-10), especially Sections 3 and 4. https://arxiv.org/html/2512.10017v5
- D. Moradi, P. Popoli, J. Shallit, I. Vukusic, *State Complexity of Shifts of the Fibonacci Word*, arXiv:2603.18858v1 (initial public version 2026-03-19), Sections 1–4. https://arxiv.org/html/2603.18858v1
- V. Kosoy, *Stringological Sequence Prediction II: Right-to-Left Automaticity and Related Complexity Measures*, arXiv:2607.17369 (initial public version 2026-07-19), Section 3. https://arxiv.org/abs/2607.17369
- J.-P. Allouche, J. Shallit, *Automatic Sequences: Theory, Applications, Generalizations*, Cambridge University Press, 2003, for the classical kernel/automatic-sequence framework.
