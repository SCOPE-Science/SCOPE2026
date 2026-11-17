# A one-sweep reversible core and exact orbit spectrum for sequential elementary Rule 23

## Finding
Fix an integer \(n\ge3\). Let \(F_n\) be a complete left-to-right, in-place sweep of elementary cellular automaton Rule 23 on the labelled cyclic binary ring \(\{0,\ldots,n-1\}\). The sites are updated once, in the order \(0,1,\ldots,n-1\), by the complement of the majority of the current left, center and right bits.

Define the boundary-antialigned core
\[
\mathcal S_n=\{x\in\{0,1\}^n:x_0\ne x_{n-1}\}.
\]
For odd \(n\), let \(\mathcal E_n\) consist of the two alternating binary words of length \(n\), beginning with opposite symbols; for even \(n\), put \(\mathcal E_n=\varnothing\). Then **the one-sweep image equals the complete recurrent set**:
\[
F_n(\{0,1\}^n)=\operatorname{Per}(F_n)=\mathcal S_n\sqcup\mathcal E_n.
\]
Consequently, every initial configuration is recurrent after at most one sweep, and precisely \(2^{n-1}+2\mathbf 1_{n\text{ odd}}\) labelled configurations are recurrent. The sharp maximum first-recurrence-entry time is one.

On \(\mathcal S_n\), the nonlinear sweep is exactly the signed cyclic shift
\[
F_n(x_0,x_1,\ldots,x_{n-1})=(1-x_1,1-x_2,\ldots,1-x_{n-1},x_1).
\]
For odd \(n\), the two exceptional alternating words form one two-cycle.

For each integer \(t\ge1\), let \(g=\gcd(n-1,t)\) and \(N_n(t)=|\operatorname{Fix}(F_n^t)|\). The **entire temporal orbit spectrum** is determined by
\[
\boxed{N_n(t)=\begin{cases}
2^g,&n\text{ even},\\
2^g\,\mathbf 1_{\,2\mid t/g}+2\mathbf 1_{\,2\mid t},&n\text{ odd}.
\end{cases}}
\]
In particular, the maximum primitive period is exactly \(n-1\) for even \(n\), and \(2(n-1)\) for odd \(n\). The number of labelled primitive orbits of length \(t\) equals \(\frac1t\sum_{d\mid t}\mu(t/d)N_n(d)\), with \(\mu\) the ordinary Möbius function.

## Assumptions and scope
Bits are \(0\) and \(1\), with periodic spatial indexing. All expressions refer to the *post-sweep* map, not synchronous updating or random asynchronous updating. For a local triple \((a,b,c)\), Rule 23 uses \(f(a,b,c)=1-\operatorname{maj}(a,b,c)\), where \(\operatorname{maj}(a,b,c)=1\) when at least two inputs equal one. During the sweep, a site uses neighbors' **current** values: sites already visited may have changed, while not-yet-visited sites retain their old values. At the final site the right neighbor is the already updated site zero. Ring labels and update order are fixed, so states are not identified under spatial translation or bit complement.

A state is recurrent if some positive iterate of \(F_n\) fixes it; its first-entry time is the least nonnegative number of sweeps required to reach such a state. Temporal fixed counts refer to all initially specified configurations, with no extra state or phase coordinate.

## Proof
Write \(x\) for the input and \(y=F_n(x)\) for the output. The local rule has the elementary property that if \(f(a,b,c)=c\), then necessarily \(a=b=1-c\); equivalently, if the update output agrees with its right input, the other two inputs are both opposite.

**Step 1: the core is invariant, with an explicit bijection.** Suppose \(x_0\ne x_{n-1}\). The first update uses the complementary pair \((x_{n-1},x_0)\) and therefore returns \(y_0=1-x_1\). Inductively, for \(1\le i\le n-2\), the already updated left bit is \(y_{i-1}=1-x_i\), so the left and center inputs are complementary and \(y_i=1-x_{i+1}\). The final update sees the complementary pair \((y_{n-2},x_{n-1})\) and right input \(y_0=1-x_1\); hence \(y_{n-1}=x_1\). Thus \(y_0\ne y_{n-1}\) and the displayed formula holds. The internal vector \((x_1,\ldots,x_{n-1})\) uniquely determines \(x_0=1-x_{n-1}\), and the induced signed shift is bijective. Therefore \(F_n\) permutes the entire core \(\mathcal S_n\).

**Step 2: there are no other image states except the two specified ones.** Assume instead \(y_{n-1}=y_0=b\). At the last update the right input equals \(b\); to output \(b\), its other inputs must both equal \(1-b\). Thus \(y_{n-2}=x_{n-1}=1-b\). For each \(i=n-2,n-3,\ldots,1\), knowing \(y_i=x_{i+1}=c\), the same local-rule property forces \(y_{i-1}=x_i=1-c\). It follows that the output bits alternate from \(y_0=b\) to \(y_{n-2}=1-b\), forcing \(n\) odd. The first update, with \(x_1=b\) and \(x_{n-1}=1-b\), then forces \(x_0=1-b\). Therefore both \(x\) and \(y\) are alternating words of odd length. Conversely, direct substitution shows that the two alternating words interchange under one sweep. The output set is precisely the stated disjoint union. Since the core is permuted and the exceptional pair is a two-cycle, the entire image is recurrent and every recurrent point lies in the image.

**Step 3: the period formula.** Set \(L=n-1\). Under the coordinate identification \(\mathcal S_n\cong\{0,1\}^L\), the core permutation is
\[
T(b_1,\ldots,b_L)=(1-b_2,\ldots,1-b_L,b_1).
\]
A single step rotates coordinates by one and complements exactly \(L-1\) of the \(L\) traversed edges. The permutation of coordinates induced by \(T^t\) has exactly \(g=\gcd(L,t)\) cycles. Following any such cycle of length \(L/g\) involves \(t/g\) complete circuits of the signed shift, so the parity of complemented edges is \((L-1)t/g\). If that parity is odd, the fixed-coordinate equation is inconsistent on every cycle; if even, one free binary choice per cycle gives exactly \(2^g\) fixed vectors. For even \(n\), \(L-1\) is even and the condition always holds. For odd \(n\), \(L-1\) is odd and it holds exactly when \(t/g\) is even. The exceptional pair contributes two points precisely when \(t\) is even. This proves the formula.

For even \(n\), \(L\) is odd and \(T^L\) is the identity. For odd \(n\), \(L\) is even and \(T^L\) complements all bits, so \(T^{2L}\) is the identity. To prove both upper bounds are attained, start with the all-zero internal vector. For \(1\le k<L\), its \(k\)-th image has \(L-k\) leading ones followed by \(k\) zeros when \(k\) is odd, and \(L-k\) leading zeros followed by \(k\) ones when \(k\) is even; in either case it is not all-zero or all-one. When \(L\) is odd, the \(L\)-th image is zero; when \(L\) is even, it is all-one and the next \(L\) steps complement the preceding orbit, first returning to zero after \(2L\) steps. Thus the sharp primitive periods are exactly \(L\) and \(2L\), respectively. Standard Möbius inversion gives the primitive-orbit count.

## Verification
Two standalone Python 3 scripts, `verify_rule23.py` and `verify_signed_shift.py`, are supplied. The first performs literal bit-by-bit Rule-23 sweeps, compares all one-step images against the stated membership criterion, checks that the image is a permutation-invariant recurrent set, and verifies every \(N_n(t)\) for \(3\le n\le14\) and \(1\le t\le2n\). The second uses an independently coded packed-bit truth table and affine signed-shift implementation; it checks the conjugacy for every core state through \(n=17\) and independently verifies temporal fixed counts through \(n=11\). Both scripts were executed with Python 3 and their exact outputs are included in `direct_output.txt` and `signed_output.txt`.

Sample counts are \(|\operatorname{Per}(F_5)|=18\), \(|\operatorname{Per}(F_6)|=32\), \(|\operatorname{Per}(F_7)|=66\) and \(|\operatorname{Per}(F_8)|=128\). These finite calculations test the proof but do not replace the all-\(n\) argument.

## Relationship to prior work
Wolfram (1983) defines elementary binary cellular automata and their standard synchronous setting. Inokuchi and Sato (2000) analyze nonlinear threshold rules, including Rule 23, under **fixed spatial boundaries and simultaneous updates**. Neither dynamics is the labelled cyclic, in-place, ordered sweep studied here. Donoso-Leiva, Goles, Ríos-Wilson and Sené (arXiv:2509.07797, original preprint 2025, revised 2026) study which sequential update orders can lead to fixed points. In their Theorem 12, Rule 23 on even rings has a covering by suitable state-dependent update orders; their treatment does not give the one-pass image, affine recurrent conjugacy, or all-period counts for the fixed natural order. Distinct previously indexed findings about synchronous Rule 232, cyclic Rule 3, and ordered Rule 60 do not imply these Rule-23 statements because their local maps or update conventions differ.

## Limitations
This is a theorem for one specific deterministic cyclic scan order, not every permutation of site updates, and for all labelled rings of size at least three. The result concerns the recurrence structure of the globally finite map rather than probabilistic asynchronous trajectories. The original Wolfram rule was published in 1983, but historical priority of the present derived statement cannot be ruled out from unindexed archival work. The proof and programs have not been independently externally audited.

## References
- S. Wolfram, *Statistical Mechanics of Cellular Automata*, Reviews of Modern Physics **55** (1983), 601–644, published 1 July 1983. https://doi.org/10.1103/RevModPhys.55.601 ; open-author PDF: https://content.wolfram.com/sw-publications/2020/08/statistical-mechanics-cellular-automata.pdf
- S. Inokuchi and T. Sato, *On Limit Cycles and Transient Lengths of Cellular Automata with Threshold Rules*, Bulletin of Informatics and Cybernetics **32** (2000), 23–60. https://doi.org/10.5109/13492 ; open repository: https://catalog.lib.kyushu-u.ac.jp/opac_download_md/13492/p023.pdf
- I. Donoso-Leiva, E. Goles, M. Ríos-Wilson and S. Sené, *On the Convergence of Elementary Cellular Automata under Sequential Update Modes*, arXiv:2509.07797 (first posted 9 September 2025; version 2 dated 24 February 2026), https://arxiv.org/pdf/2509.07797 . Subsequently published in Theoretical Computer Science **1086** (2026), article 116250.
